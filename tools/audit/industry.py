"""Regression checks for the industry graph and policy effects; no game runtime emulation.

Run from any directory with Python 3.10+. Only the small trigger/effect subset used
by the scenarios is evaluated; unknown tokens fail instead of being assumed true.
"""
from pathlib import Path
import itertools
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
TOKEN = re.compile(r'\s+|\#[^\n]*|"(?:\\.|[^"\\])*"|>=|<=|==|[{}=<>]|[^\s{}=<>"#]+')


def parse(text):
    tokens = [m.group() for m in TOKEN.finditer(text) if not m.group().isspace() and not m.group().startswith('#')]
    index = 0

    def block(nested=False):
        nonlocal index
        result = []
        while index < len(tokens):
            key = tokens[index]
            if key == '}':
                if not nested:
                    raise ValueError('Unexpected closing brace')
                index += 1
                return result
            index += 1
            if index == len(tokens) or tokens[index] not in ('=', '==', '>', '<', '>=', '<='):
                result.append((key, '', None))
                continue
            op = tokens[index]
            index += 1
            if index == len(tokens):
                raise ValueError('Missing value')
            if tokens[index] == '{':
                index += 1
                val = block(True)
            else:
                val = tokens[index].strip('"')
                index += 1
            result.append((key, op, val))
        if nested:
            raise ValueError('Unclosed block')
        return result

    return block()


def read(relative):
    return parse((ROOT / relative).read_text(encoding='utf-8-sig'))


def values(block, key):
    return [v for k, _, v in block if k == key]


def value(block, key, default=None):
    found = values(block, key)
    return found[0] if found else default


def focus_map(text):
    tree = value(parse(text), 'focus_tree')
    return {value(b, 'id'): b for b in values(tree, 'focus')}


def positions(focuses):
    result = {}

    def xy(fid):
        if fid not in result:
            b = focuses[fid]
            x, y = int(value(b, 'x')), int(value(b, 'y'))
            parent = value(b, 'relative_position_id')
            if parent:
                px, py = xy(parent)
                x += px
                y += py
            result[fid] = (x, y)
        return result[fid]

    for fid in focuses:
        xy(fid)
    return result


def groups(b):
    return [values(g, 'focus') for g in values(b, 'prerequisite')]


def walk(block):
    for key, op, val in block:
        yield key, op, val
        if isinstance(val, list):
            yield from walk(val)


def branch_ids(focuses):
    found = {'VIE_industrialization_strategy'}
    while True:
        more = found | {f for f, b in focuses.items() if any(p in found for g in groups(b) for p in g)}
        if more == found:
            return found
        found = more


def state(completed=(), flags=(), date='2025.12.31', localization=0):
    return dict(completed=set(completed), flags=set(flags), date=date,
                variables={'VIE_ind_localization': localization}, treasury=0, pp=0,
                growth=0, bonus=0, buildings=0, temps={})


def compare(a, op, b):
    return {'=': a == b, '==': a == b, '>': a > b, '<': a < b,
            '>=': a >= b, '<=': a <= b}[op]


def condition(block, s, triggers):
    def one(key, op, val):
        if key == 'tooltip':
            return True
        if key in ('AND', 'custom_trigger_tooltip'):
            return condition(val, s, triggers)
        if key == 'OR':
            return any(one(k, o, v) for k, o, v in val)
        if key == 'NOT':
            return not condition(val, s, triggers)
        if key == 'count_triggers':
            minimum = int(value(val, 'amount'))
            return sum(one(k, o, v) for k, o, v in val if k != 'amount') >= minimum
        if key == 'has_completed_focus':
            return val in s['completed']
        if key == 'has_country_flag':
            return val in s['flags']
        if key == 'date':
            return compare(tuple(map(int, s['date'].split('.'))), op, tuple(map(int, val.split('.'))))
        if key == 'check_variable':
            return all(compare(s['variables'].get(k, 0), o, float(v)) for k, o, v in val)
        if key in triggers:
            result = condition(triggers[key], s, triggers)
            return result if val == 'yes' else not result
        if key == 'always':
            return val == 'yes'
        raise ValueError('Unsupported test trigger: ' + key)
    return all(one(k, o, v) for k, o, v in block)


def effect(block, s, effects, triggers):
    for key, _, val in block:
        if key in ('log', 'name', 'ai_chance', 'custom_effect_tooltip', 'add_ideas'):
            continue
        if key in ('hidden_effect',):
            effect(val, s, effects, triggers)
        elif key == 'if':
            if condition(value(val, 'limit'), s, triggers):
                effect([n for n in val if n[0] != 'limit'], s, effects, triggers)
        elif key in effects:
            effect(effects[key], s, effects, triggers)
        elif key == 'set_country_flag':
            s['flags'].add(val)
        elif key == 'add_to_variable':
            for k, _, v in val:
                if k != 'tooltip':
                    s['variables'][k] = s['variables'].get(k, 0) + float(v)
        elif key == 'set_temp_variable':
            s['temps'].update({k: float(v) for k, _, v in val})
        elif key == 'modify_treasury_effect':
            s['treasury'] += s['temps']['treasury_change']
        elif key == 'add_political_power':
            s['pp'] += float(val)
        elif key == 'increase_economic_growth':
            s['growth'] += 1
        elif key == 'add_tech_bonus':
            assert value(val, 'category') == 'CAT_microchips'
            assert float(value(val, 'bonus')) == .5 and int(value(val, 'uses')) == 1
            s['bonus'] += 1
        elif key == 'one_state_industrial_complex':
            s['buildings'] += 1
        elif key.isdigit():
            effect(val, s, effects, triggers)
        else:
            raise ValueError('Unsupported test effect: ' + key)


def main():
    focuses = focus_map((ROOT / 'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8-sig'))
    ids = branch_ids(focuses)
    pos = positions(focuses)
    triggers = {k: v for k, _, v in read('common/scripted_triggers/VIE_industry_triggers.txt')}
    effects = {k: v for k, _, v in read('common/scripted_effects/VIE_industry_effects.txt')}
    assert len(ids) == 39
    for f in ids:
        b = focuses[f]
        for g in groups(b):
            for p in g:
                assert pos[f][1] > pos[p][1], (f, p, 'same/backward row')
        for other in values(value(b, 'mutually_exclusive', []), 'focus'):
            assert f in values(value(focuses[other], 'mutually_exclusive', []), 'focus')
        for neighbor, (nx, ny) in pos.items():
            if neighbor != f and pos[f][1] == ny:
                assert abs(pos[f][0] - nx) >= 2, (f, neighbor, 'gap')
        internal = {v for k, _, v in walk(value(b, 'available', [])) if k == 'has_completed_focus'} & ids
        assert not internal, (f, 'hidden internal dependency', internal)
    old = focus_map(subprocess.check_output(['git', 'show', 'HEAD:common/national_focus/VIE_md_focus.txt'], cwd=ROOT).decode('utf-8-sig'))
    old_pos = positions(old)
    assert all(pos[f] == p for f, p in old_pos.items() if f not in ids), 'Moved another branch'
    assert all(focuses[f] == b for f, b in old.items() if f not in ids), 'Changed gameplay in another branch'
    before = __import__('json').loads((ROOT / '.claude/docs/industry/industry_before.json').read_text(encoding='utf-8'))
    for f, snapshot in before.items():
        if f not in ('VIE_china_plus_one', 'VIE_semiconductor_fab'):
            previous = value(parse(snapshot['block']), 'focus')
            assert value(focuses[f], 'completion_reward') == value(previous, 'completion_reward'), (f, 'changed reward')
    print('PASS: 39 focuses, forward rows, gaps, reciprocal exclusions, other branches unchanged')

    cap = focuses['VIE_modern_industrial_nation_2030']
    sector = value(value(triggers['VIE_ind_three_sectors'], 'custom_trigger_tooltip'), 'count_triggers')
    sectors = [n for n in sector if n[0] != 'amount']
    sector_focuses = [set(re.findall(r'VIE_\w+', str(n))) for n in sectors]
    loc_defs = values(read('common/scripted_localisation/VIE_industry_loc.txt'), 'defined_text')
    for bits in itertools.product((False, True), repeat=6):
        completed = set().union(*(f for f, bit in zip(sector_focuses, bits) if bit))
        s = state(completed, localization=45)
        assert condition(value(cap, 'available'), s, triggers) == (sum(bits) >= 3)
        for definition, bit in zip(loc_defs, bits):
            assert condition(value(values(definition, 'text')[0], 'trigger'), s, triggers) == bit
    s = state(set().union(*sector_focuses), localization=44.9)
    assert not condition(value(cap, 'available'), s, triggers)
    for incomplete in ('VIE_manufacturing_hub', 'VIE_chip_design'):
        s = state({'VIE_offshore_wind_fabrication', 'VIE_green_textiles', incomplete}, localization=45)
        assert not condition(value(cap, 'available'), s, triggers), 'Half a group counted'
    print('PASS: all 64 sector combinations, 45-point boundary, partial groups, six status getters')

    traditional = {f for f in ids if any(n in f for n in ('vinashin', 'shipbuilding', 'offshore_wind_fabrication', 'textile', 'yarn_forward', 'hoa_phat', 'supporting_industries', 'precision_mechanics', 'industrial_productivity', 'industrialization_strategy', 'nq23', 'nq29'))}
    s = state({'VIE_doi_moi_continues', 'VIE_cptpp_member', 'VIE_evfta'}, {'VIE_vinashin_crisis_processed'})
    pending = set(traditional)
    while pending:
        eligible = {f for f in pending if all(any(p in s['completed'] for p in g) for g in groups(focuses[f])) and condition(value(focuses[f], 'available', []), s, triggers)}
        assert eligible, ('Blocked traditional path', pending)
        for f in eligible:
            reward = value(focuses[f], 'completion_reward')
            s['variables']['VIE_ind_localization'] += sum(float(value(n[2], 'VIE_ind_localization', 0)) for n in reward if n[0] == 'add_to_variable')
        s['completed'].update(eligible)
        pending -= eligible
    assert all(any(p in s['completed'] for p in g) for g in groups(cap))
    assert condition(value(cap, 'available'), s, triggers)
    assert 'VIE_chip_design' not in s['completed'] and 'VIE_ev_revolution_batteries' not in s['completed']
    print('PASS: traditional ship/textile/steel path reaches capstone with', int(s['variables']['VIE_ind_localization']), 'points')

    events = {value(b, 'id'): b for b in values(read('events/VIE_industry_events.txt'), 'country_event')}
    options = values(events['vie_ind.1'], 'option')
    for choice, flag, opposite, option in [
        ('VIE_fdi_fast_track', 'VIE_fdi_open_door', 'VIE_fdi_technology_screening', options[0]),
        ('VIE_fdi_technology_screening', 'VIE_fdi_technology_screening', 'VIE_fdi_fast_track', options[1]),
    ]:
        s = state()
        effect(value(focuses[choice], 'completion_reward'), s, effects, triggers)
        first = (s['growth'], s['pp'], dict(s['variables']))
        for o in options:
            effect(o, s, effects, triggers)
        assert first == (s['growth'], s['pp'], s['variables']), 'Queued event duplicated/reversed policy'
        assert not condition(value(events['vie_ind.1'], 'trigger'), s, triggers)
        assert not condition(value(focuses[opposite], 'available'), s, triggers)
        assert condition(value(focuses[choice], 'bypass'), s, triggers)
        legacy = state()
        effect(option, legacy, effects, triggers)
        assert flag in legacy['flags'] and condition(value(focuses[choice], 'bypass'), legacy, triggers)
        effect(value(focuses[choice], 'completion_reward'), legacy, effects, triggers)
        assert first == (legacy['growth'], legacy['pp'], legacy['variables'])
        legacy['completed'].update({'VIE_manufacturing_hub', choice})
        assert all(any(p in legacy['completed'] for p in g) for g in groups(focuses['VIE_apple_supply_chain']))
    print('PASS: both FDI policies reach Apple; legacy/queued events grant rewards once')

    fab = focuses['VIE_semiconductor_fab']
    for choice, points in [('VIE_chip_design_packaging_priority', 2), ('VIE_chip_pilot_fab_priority', 3)]:
        s = state({'VIE_semiconductor_ambition', choice})
        effect(value(focuses[choice], 'completion_reward'), s, effects, triggers)
        assert s['variables']['VIE_ind_localization'] == points and s['bonus'] == 1
        for part in ('VIE_chip_design', 'VIE_osat_packaging', 'VIE_chip_engineers'):
            assert all(any(p in s['completed'] for p in g) for g in groups(focuses[part]))
        s['completed'].update({'VIE_chip_design', 'VIE_osat_packaging'})
        assert not all(any(p in s['completed'] for p in g) for g in groups(fab))
        s['completed'].add('VIE_chip_engineers')
        assert all(any(p in s['completed'] for p in g) for g in groups(fab))
        effect(value(fab, 'completion_reward'), s, effects, triggers)
        assert s['treasury'] == -3 and s['buildings'] == 1
    print('PASS: both chip priorities reach fab; support costs 3bn, one priced building call')

    eco = {value(b, 'id'): b for b in values(read('events/VIE_md_eco_p2.txt'), 'country_event')}
    for option in values(eco['vie_eco.5'], 'option'):
        assert 'VIE_vinashin_crisis_processed' in values(value(option, 'hidden_effect'), 'set_country_flag')
    processed = state(flags={'VIE_vinashin_crisis_processed'})
    scheduled = state(flags={'VIE_sched_vinashin'})
    avail = value(focuses['VIE_vinashin_restructuring_sbic'], 'available')
    assert condition(avail, processed, triggers) and not condition(avail, scheduled, triggers)
    fx = read('common/scripted_effects/VIE_md_effects_p2.txt')
    assert 'VIE_vinashin_crisis_processed' in values(value(value(fx, 'VIE_fb_vinashin'), 'hidden_effect'), 'set_country_flag')
    assert (ROOT / 'common/scripted_effects/VIE_md_effects_p2.txt').read_text(encoding='utf-8').count('set_country_flag = VIE_vinashin_crisis_processed') == 2
    print('PASS: Vinashin scheduling alone cannot unlock SBIC; options/fallback/late bookmark cover gate')
    print('ALL PASS (static checks; game runtime and AI behavior still require playtest)')


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, ValueError) as exc:
        print('FAIL:', exc)
        sys.exit(1)
