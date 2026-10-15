"""Kiem tinh cac loi parser/provider v55-v61; khong thay the engine HOI4.

Chay: python tools/audit/error_log_regressions.py --md <MD> --game <HOI4>
"""
from __future__ import annotations

import argparse
import ast
import datetime
import itertools
import re
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
source = ast.parse((ROOT / 'tools/audit/audit.py').read_text(encoding='utf-8'))
namespace = {}
exec(compile(ast.Module(body=[n for n in source.body if isinstance(n, ast.FunctionDef)
                            and n.name in ('tokenize', 'parse')], type_ignores=[]),
             'audit_parser', 'exec'), namespace)
failures = []
checks = 0


def check(ok, label):
    global checks
    checks += 1
    if not ok:
        failures.append(label)
        print('FAIL', label)


def clean(text):
    return re.sub(r'"(?:\\.|[^"\\])*"|#[^\n]*',
                  lambda m: '\n' * m[0].count('\n'), text)


def load(relative):
    text = (ROOT / relative).read_text(encoding='utf-8-sig')
    # Khong xoa strings khi parse: can giu ID va log.
    text = re.sub(r'"(?:\\.|[^"\\])*"|#[^\n]*',
                  lambda m: m[0] if m[0].startswith('"') else '', text)
    return namespace['parse'](namespace['tokenize'](text))


def value(block, key, default=None):
    return next((v for k, op, v, line in block if k == key), default)


def walk(block):
    for k, op, v, line in block:
        yield k, op, v, line
        if isinstance(v, list):
            yield from walk(v)


def parse_text(text):
    text = re.sub(r'"(?:\\.|[^"\\])*"|#[^\n]*',
                  lambda m: m[0] if m[0].startswith('"') else '', text)
    return namespace['parse'](namespace['tokenize'](text))


def overlay(layers):
    # Uu tien VIE > MD > vanilla; cung duong dan chi nap mot file.
    result = {}
    for layer in layers:
        for relative, item in layer.items():
            result.setdefault(str(relative).replace('\\', '/').casefold(), item)
    return result


def effective_files(providers, folder, suffix):
    return overlay([{p.relative_to(root): p for p in (root / folder).rglob('*' + suffix)}
                    for root in providers])


def font_inventory(entries):
    bases = set()
    positions = {}
    overrides = []
    for path, blocks in entries.items():
        for index, (k, op, v, line) in enumerate(walk(blocks)):
            name = value(v, 'name') if isinstance(v, list) else None
            if k == 'bitmapfont':
                bases.add(name)
                positions.setdefault((path, name), index)
            elif k == 'bitmapfont_override':
                overrides.append((path, v, index))
    issues = []
    for path, block, index in overrides:
        name = value(block, 'name')
        if name not in bases:
            issues.append(('missing', path, name))
        if (path, name) in positions and positions[path, name] >= index:
            issues.append(('order', path, name))
    return bases, overrides, issues


def font_overlay_regressions():
    base = parse_text('bitmapfonts = { bitmapfont = { name = "test" path = "test" } }')
    override = parse_text('bitmapfonts = { bitmapfont_override = { name = "test" fontfiles = { "test" } languages = { "l_english" } } }')
    hidden = overlay([{'interface/fonts.gfx': override}, {'interface/fonts.gfx': base}])
    check(font_inventory(hidden)[2] == [('missing', 'interface/fonts.gfx', 'test')],
          'Font fixture: hidden vanilla base cannot satisfy override')
    merged = parse_text('bitmapfonts = { bitmapfont = { name = "test" path = "test" } bitmapfont_override = { name = "test" } }')
    check(not font_inventory({'interface/fonts.gfx': merged})[2], 'Font fixture: base precedes override')
    reversed_blocks = parse_text('bitmapfonts = { bitmapfont_override = { name = "test" } bitmapfont = { name = "test" path = "test" } }')
    check(font_inventory({'interface/fonts.gfx': reversed_blocks})[2] == [('order', 'interface/fonts.gfx', 'test')],
          'Font fixture: reject override before its local base')
    separate = overlay([{'interface/vie.gfx': override}, {'interface/fonts.gfx': base}])
    check(not font_inventory(separate)[2], 'Font fixture: distinct provider path remains effective')
    check(overlay([{'Interface/Fonts.gfx': 'VIE'}, {'interface/fonts.gfx': 'vanilla'}]) == {'interface/fonts.gfx': 'VIE'},
          'Font fixture: Windows path case normalization')
    legacy = 'common lineHeight=12 base=9 scaleW=256 scaleH=256 pages=1\nchar id=32 x=0 y=0 width=1 height=0 page=0\n'
    check(single_font_atlas(legacy), 'Font fixture: vanilla legacy single atlas without page declaration')
    check(not single_font_atlas(legacy.replace('pages=1', 'pages=2')), 'Font fixture: reject multipage legacy')
    check(not single_font_atlas(legacy.replace('page=0', 'page=1')), 'Font fixture: reject glyph on undeclared page')
    check(not single_font_atlas('common scaleW=256 scaleH=256 pages=1'), 'Font fixture: reject absent glyph metadata')
    header = bytearray(128)
    header[:4] = b'DDS '
    struct.pack_into('<II', header, 12, 256, 256)
    check(not font_provider_issues(legacy, header), 'Font fixture: valid FNT/DDS provider and atlas')
    check('missing FNT' in font_provider_issues(None, header), 'Font fixture: missing FNT rejected')
    check('missing DDS' in font_provider_issues(legacy, None), 'Font fixture: missing DDS rejected')
    check('DDS header' in font_provider_issues(legacy, b'broken'), 'Font fixture: broken DDS header rejected')
    struct.pack_into('<II', header, 12, 128, 256)
    check('atlas dimensions' in font_provider_issues(legacy, header), 'Font fixture: mismatched atlas rejected')


def single_font_atlas(text):
    # Garamond vanilla 1.19 dung common pages=1 + char page=0, khong co dong page file.
    common = re.search(r'^common\s+([^\n]+)', text, re.M)
    if not common or not re.search(r'\bpages=1\b', common[1]):
        return False
    declarations = re.findall(r'^page\s+id=(\d+)\s+file="([^"]+)"', text, re.M)
    glyphs = re.findall(r'^char\s+id=\d+\s+([^\n]+)', text, re.M)
    return bool(glyphs) and (not declarations or len(declarations)==1 and declarations[0][0]=='0') and all(
        re.search(r'\bpage=0\b', glyph) is not None for glyph in glyphs)


def font_provider_issues(text, header):
    issues = []
    if text is None:
        issues.append('missing FNT')
    elif not single_font_atlas(text):
        issues.append('single atlas/glyph page metadata')
    if header is None:
        issues.append('missing DDS')
    elif len(header) != 128 or header[:4] != b'DDS ':
        issues.append('DDS header')
    elif text is not None:
        height, width = struct.unpack_from('<II', header, 12)
        scale = re.search(r'scaleW=(\d+)\s+scaleH=(\d+)', text)
        if scale is None or (width, height) != tuple(map(int, scale.groups())):
            issues.append('atlas dimensions')
    return issues


def font_checks(md, game):
    providers = (ROOT, md, game)
    entries = {path: parse_text(path.read_text(encoding='utf-8-sig', errors='replace'))
               for path in effective_files(providers, 'interface', '.gfx').values()}
    bases, overrides, issues = font_inventory(entries)
    for issue, path, name in issues:
        check(False, f'Effective font {issue}: {path.name}: {name}')
    for path, block, index in overrides:
        if ROOT not in path.parents:
            continue
        name = value(block, 'name')
        check(name in bases, f'Font nen cho override {name}')
        check(set(k for k, op, v, line in block) <= {'name', 'fontfiles', 'languages'},
              f'Schema override {name}')
    font_sources = [(v, value(v, 'name')) for k, op, v, line in
                    walk(load('interface/fonts.gfx')) if k in ('bitmapfont', 'bitmapfont_override')]
    font_sources += [(v, value(v, 'name')) for k, op, v, line in
                     walk(load('interface/load_screen_font.gfx')) if k in ('bitmapfont', 'bitmapfont_override')]
    for block, name in font_sources:
        paths = [k for k, op, v, line in value(block, 'fontfiles', [])]
        if value(block, 'path'):
            paths.append(value(block, 'path'))
        for prefix in paths:
            fnt = next((root / (prefix + '.fnt') for root in providers
                        if (root / (prefix + '.fnt')).is_file()), None)
            # HOI4 dung cap prefix.fnt/prefix.dds: vanilla hoi_33.fnt cung
            # ghi page hoi_33_0.dds nhung provider thuc la hoi_33.dds.
            # Chi xu ly font mot atlas trong goi hien tai, khong bo qua multipage.
            texture = next((root / (prefix + '.dds') for root in providers
                            if (root / (prefix + '.dds')).is_file()), None)
            issues = font_provider_issues(fnt.read_text(encoding='utf-8-sig', errors='replace') if fnt else None,
                                          texture.read_bytes()[:128] if texture else None)
            check(not issues, f'Font provider {name}: {prefix}: {issues}')
    for path in (ROOT / 'interface').rglob('*.gui'):
        text = path.read_text(encoding='utf-8-sig')
        for font in re.findall(r'\bfont\s*=\s*"?([\w.]+)', text):
            check(font in bases, f'GUI font {path.name}: {font}')
    own = load('interface/fonts.gfx')
    for k, op, v, line in walk(own):
        if k == 'bitmapfont_override':
            check(value(v, 'name') not in ('loadscreen_header', 'loadscreen_tip'),
                  'Khong duplicate loadscreen override')
    base = next(v for k, op, v, line in walk(own)
                if k == 'bitmapfont' and value(v, 'name') == 'hoi_33w')
    check(value(base, 'path') == 'gfx/fonts/hoi_33', 'hoi_33w dung glyph hien co')
    for name in ('garamond_12', 'cw_3d_debug'):
        base = next((v for k, op, v, line in walk(own)
                     if k == 'bitmapfont' and value(v, 'name') == name), [])
        check(value(base, 'path') == 'gfx/fonts/garamond_12' and value(base, 'color') == '0xffffffff',
              f'Vanilla base schema {name}')


def tech_bonus_checks(md, game):
    categories = set()
    for path in effective_files((ROOT, md, game), 'common/technology_tags', '.txt').values():
        for k, op, v, line in parse_text(path.read_text(encoding='utf-8-sig')):
            if k.casefold() == 'technology_categories':
                categories.update(name for name, op, val, ln in walk(v))
    check('CAT_armored_fighting_vehicles' in categories, 'AFV category effective provider')
    check('CAT_motorized_mechanized' not in categories, 'Old XTC category rejected by effective MD provider')
    count = 0
    for folder in ('common', 'events', 'history'):
        for path in (ROOT / folder).rglob('*.txt'):
            for k, op, v, line in walk(load(path.relative_to(ROOT))):
                if k != 'add_tech_bonus':
                    continue
                for field, operator, category, ln in v:
                    if field == 'category':
                        count += 1
                        check(category in categories, f'Tech bonus category {path.relative_to(ROOT)}:{ln} {category}')
                if value(v, 'name') == 'VIE_lf_i5_bonus':
                    check(value(v, 'category') == 'CAT_armored_fighting_vehicles'
                          and value(v, 'uses') == '1' and value(v, 'bonus') == '0.50', 'XTC50% one use')
    check(count > 0, 'Technology bonus consumers found')
    print(f'Tech bonus: {count} category references checked against effective providers.')


def retire_checks(start):
    targets = ('VIE_Tran_Quang_Phuong', 'VIE_Tran_Viet_Khoa')
    # Doc thu tu tu live history; chi mo phong hai recruit/retire va guard cua chung.
    statements = []
    for node in start:
        k, op, v, line = node
        if k in ('recruit_character', 'retire_character') and v in targets:
            statements.append(node)
        elif k == 'if' and any(ck == 'retire_character' and cv in targets
                              for ck, co, cv, cl in walk(v)):
            statements.append(node)
    for target in targets:
        recruit = next(line for k, op, v, line in walk(start)
                       if k == 'recruit_character' and v == target)
        retires = [line for k, op, v, line in walk(start)
                   if k == 'retire_character' and v == target]
        check(len(retires) == 1 and recruit < retires[0], 'Thu tu recruit/retire ' + target)
        guard = [v for k, op, v, line in walk(start) if k == 'if'
                 and value(v, 'retire_character') == target]
        check(len(guard) == 1 and value(value(guard[0], 'limit'), 'has_character') == target,
              'Guard has_character ' + target)
    dates = (datetime.date(2000, 1, 1), datetime.date(2017, 1, 1),
             datetime.date(2002, 2, 6), datetime.date(2002, 2, 7), datetime.date(2002, 2, 8))
    for date, recruited in itertools.product(dates, (False, True)):
        chars = set()
        retired = []

        def condition(block):
            results = []
            for k, op, v, line in block:
                if k == 'date':
                    check(op == '<', 'Retire date operator')
                    results.append(date < datetime.date(*map(int, v.split('.'))))
                elif k == 'has_character':
                    results.append(v in chars)
                else:
                    raise AssertionError('Unknown retire fixture guard: ' + k)
            return all(results)

        def apply(block):
            for k, op, v, line in block:
                if k == 'if':
                    if condition(value(v, 'limit')):
                        apply([n for n in v if n[0] != 'limit'])
                elif k == 'recruit_character':
                    if recruited:
                        chars.add(v)
                elif k == 'retire_character':
                    check(v in chars, f'Khong retire nhan vat vang mat {date} {v}')
                    retired.append(v)
                    chars.discard(v)
                else:
                    raise AssertionError('Unknown retire fixture effect: ' + k)
        apply(statements)
        expected = set(targets) if recruited and date < datetime.date(2002, 2, 7) else set()
        check(set(retired) == expected, f'Retire window {date} recruited={recruited}')
        apply([n for n in statements if n[0] == 'if'])
        check(len(retired) == len(expected), 'Retire guard idempotent ' + str(date))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--md', type=Path, required=True)
    parser.add_argument('--game', type=Path, required=True)
    args = parser.parse_args()
    font_overlay_regressions()
    tech_bonus_checks(args.md, args.game)
    for folder in ('common', 'events', 'interface', 'history'):
        for path in (ROOT / folder).rglob('*'):
            if path.suffix not in ('.txt', '.gfx'):
                continue
            text = path.read_text(encoding='utf-8')
            check('\ufeff' not in text, f'BOM: {path.relative_to(ROOT)}')
            depth = 0
            valid = True
            for char in clean(text):
                if char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                    valid &= depth >= 0
            check(valid and depth == 0, f'Ngoac: {path.relative_to(ROOT)}')
            check(not re.search(r'check_variable\s*=\s*\{[^{}]*(==|>=|<=)', clean(text)),
                  f'So sanh ngan khong hop le: {path.relative_to(ROOT)}')
            check(not re.search(r'\bdate\s*(<=|>=)', clean(text)),
                  f'So sanh ngay: {path.relative_to(ROOT)}')
            check(not re.search(r'\bpolitical_power\s*[<>=]', clean(text)),
                  f'Trigger PP cu: {path.relative_to(ROOT)}')
    for path in (ROOT / 'localisation').rglob('*.yml'):
        check(path.read_bytes().startswith(b'\xef\xbb\xbf'), f'Loc BOM: {path.name}')
    for folder in ('scripted_effects', 'scripted_triggers'):
        definitions = []
        for path in (ROOT / 'common' / folder).glob('*.txt'):
            definitions.extend(k for k, op, v, line in load(path.relative_to(ROOT))
                               if isinstance(v, list))
        check(len(definitions) == len(set(definitions)), 'Khong trung dinh nghia ' + folder)

    # Kiem bien bang fixture naval doc live trigger; khong gia lap engine day du.
    import naval_scenarios as naval
    triggers = load('common/scripted_triggers/VIE_md_triggers.txt')
    cases = 0
    for k, op, v, line in walk(triggers):
        if k != 'check_variable' or value(v, 'var') is None:
            continue
        var = value(v, 'var')
        threshold = float(value(v, 'value'))
        compare = value(v, 'compare')
        for delta, expected in ((-0.001, False), (0, True), (0.001, True)):
            state = naval.State()
            state.variables[var] = threshold + delta
            check(compare == 'greater_than_or_equals', f'Operator dong {line}')
            check(state.condition([(k, '=', v, line)]) == expected, f'Bien {var} dong {line} delta {delta}')
            cases += 1
    decisions = load('common/decisions/VIE_md_politics_decisions.txt')
    side = next(v for k, op, v, line in walk(decisions) if k == 'VIE_side_project_decision')
    equality = next(v for k, op, v, line in walk(side) if k == 'check_variable'
                    and value(v, 'var') == 'VIE_last_side_project_epoch')
    for old, current in itertools.product((0, 1, 2), repeat=2):
        state = naval.State()
        state.variables.update(VIE_last_side_project_epoch=old, VIE_programme_epoch=current)
        check(state.condition([('check_variable', '=', equality, 0)]) == (old == current),
              f'Side project epoch {old}/{current}')
        state.variables['VIE_last_side_project_epoch'] = current
        check(state.condition([('check_variable', '=', equality, 0)]), 'Guard sau khi bat dau')
    check(value(side, 'cost') == '30' and value(side, 'days_remove') == '270', 'Gia/timer side project')

    for date in ((2013, 1, 1), (2023, 1, 1)):
        for delta in (-1, 0, 1):
            actual = datetime.date(*date) + datetime.timedelta(days=delta)
            state = naval.State(actual.year)
            state.month, state.day = actual.month, actual.day
            condition = [('NOT', '=', [('date', '>', '.'.join(map(str, date)), 0)], 0)]
            check(state.condition(condition) == (delta <= 0), f'Ngay <= {date} delta {delta}')

    effects = load('common/scripted_effects/VIE_md_effects_politics.txt')
    init = value(effects, 'VIE_init_political_system')
    init_if = value(init, 'if')
    check('VIE_political_system_initialized' in str(value(init_if, 'limit')), 'Guard khoi tao BoP')
    bop = value(init_if, 'set_power_balance')
    check(value(bop, 'set_value') == '0.0' and value(bop, 'value') is None, 'BoP set_value')
    check(value(bop, 'left_side') == 'VIE_bop_side_collective'
          and value(bop, 'right_side') == 'VIE_bop_side_central', 'BoP sides')
    for k, op, v, line in walk(effects):
        if k == 'add_power_balance_value':
            check({name for name, op, val, ln in v} == {'id', 'value'},
                  f'Schema add_power_balance_value dong {line}')
    for helper, delta in (('VIE_bop_add_collective', -0.05), ('VIE_bop_add_central', 0.05),
                          ('VIE_bop_add_large_collective', -0.30), ('VIE_bop_add_large_central', 0.30)):
        block = value(effects, helper)
        add = value(value(block, 'hidden_effect'), 'add_power_balance_value')
        check(value(add, 'id') == 'VIE_leadership_balance'
              and value(add, 'value') is not None
              and float(value(add, 'value')) == delta, helper + ' delta')
    hardline = value(triggers, 'VIE_hl_in_power')
    check(value(hardline, 'original_tag') == 'VIE'
          and value(hardline, 'emerging_communist_state_are_in_power') == 'yes', 'Hardline exact gate')
    tree = value(load('common/national_focus/VIE_md_focus.txt'), 'focus_tree')
    focuses = [value(v, 'id') for k, op, v, line in tree if k == 'focus']
    branch = focuses[focuses.index('VIE_review_public_administration'):focuses.index('VIE_asean_integration')]
    check(len(branch) == 74, '74 node chinh tri live')
    for term in ('ix', 'x', 'xi', 'xii', 'xiii', 'xiv'):
        # IX dung cac ID mo ta; X-XIV co prefix ky.
        if term != 'ix':
            check(sum(x.startswith('VIE_' + term) and re.match(r'VIE_' + term + r'\d', x)
                      is not None for x in branch) == 12, f'12 node {term}')

    ideas = value(value(load('common/ideas/VIE_md_ideas.txt'), 'ideas'), 'country')
    keys = ('VIE_lf_xtc_program_idea', 'VIE_lf_t1_light_tank_idea',
            'VIE_lf_spg_program_idea', 'VIE_lf_t2_main_tank_idea')
    total_cap = total_output = 0.0
    tags = (args.md / 'common/technology_tags/00_technology.txt').read_text(encoding='utf-8-sig')
    for key in keys:
        idea = value(ideas, key)
        check(value(idea, 'cancel_if_invalid') == 'no', key + ' persistence')
        for category, op, number, line in value(idea, 'research_bonus'):
            check(re.search(r'\b' + category + r'\b', tags) is not None, 'Category ' + category)
        mods = value(idea, 'modifier')
        total_cap += float(value(mods, 'production_factory_max_efficiency_factor', '0'))
        total_output += float(value(mods, 'industrial_capacity_factory', '0'))
    check(abs(total_cap - 0.15) < 1e-9 and abs(total_output - 0.20) < 1e-9, 'Tong bonus 4 idea')
    print(f'Bonus 4 idea: tran hieu suat +{total_cap:.0%}; san luong +{total_output:.0%} (toan nha may quan su).')
    history = load('history/countries/VIE - Vietnam.txt')
    start = value(history, '2000.1.1')
    retire_checks(start)
    font_checks(args.md, args.game)
    roster = [v for k, op, v, line in walk(start) if k == 'recruit_character' and v.startswith(('VIE_army_', 'VIE_air_'))]
    check(len(roster) == 12 and len(set(roster)) == 12, '12 startup roster history')
    startup = (ROOT / 'common/on_actions/VIE_md_on_actions_startup.txt').read_text(encoding='utf-8')
    check('recruit_character' not in startup, 'Startup khong recruit_character')
    docs = (args.game / 'documentation/triggers_documentation.md').read_text(encoding='utf-8-sig')
    check('greater_than_or_equals' in docs and 'compare = equals' in docs, 'Provider compare HOI4')
    print(f'{checks} checks; {cases} bien treasury/so tau; {len(failures)} FAIL. Engine runtime NOT RUN.')
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
