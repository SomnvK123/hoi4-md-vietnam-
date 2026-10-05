#!/usr/bin/env python3
"""Fix raw (untranslated) text shown in focus tooltips of VIE_md_focus.txt.  Idempotent.

Visible raw sources handled (everything inside hidden_effect / custom_trigger_tooltip /
ai_will_do is skipped, so re-running is safe):
  * has_country_flag in available/bypass/limit      -> custom_trigger_tooltip with a VIE_flag_* key
  * check_variable in available/limit               -> custom_trigger_tooltip with a VIE_var_* key
                                                       (ruling_party = 7 -> emerging_autocracy_are_in_power)
  * set_country_flag = X in a reward                -> hidden_effect
  * add_to_variable / set_variable block, no tooltip -> hidden_effect
  * "if = { limit = { NOT = { has_country_flag = VIE_ax_initialized } } ... }" -> whole block hidden
New loc keys (VIE_flag_*_tt and _NOT) are appended to localisation/english/VIE_md_hardline_l_english.yml.

Usage: python tools/fix_focus_raw_text.py [--dry]
"""
import re, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOCUS = os.path.join(ROOT, 'common/national_focus/VIE_md_focus.txt')
LOC_NEW = os.path.join(ROOT, 'localisation/english/VIE_md_hardline_l_english.yml')
DRY = '--dry' in sys.argv

# check_variable (var, op, value) -> loc key, or None = replace by a MD trigger
CHECKVAR = {
    ('VIE_expressway_km', '>', '2599'): 'VIE_var_expressway_2600_tt',
    ('VIE_expressway_km', '>', '2999'): 'VIE_var_expressway_3000_tt',
    ('VIE_scs_tension', '>', '0'): 'VIE_var_scs_tension_1_tt',
    ('VIE_ind_localization', '>', '44'): 'VIE_var_localization_45_tt',
    ('VIE_var_air_delivered', '>', '11'): 'VIE_var_air_delivered_12_tt',
    ('VIE_nf_force_priority', '=', '1'): 'VIE_var_nf_priority_1_tt',
    ('VIE_nf_force_priority', '=', '3'): 'VIE_var_nf_priority_3_tt',
    ('VIE_lf_arm_done', '<', '3'): 'VIE_var_lf_arm_done_lt3_tt',
    ('VIE_lf_cap_done', '<', '2'): 'VIE_var_lf_cap_done_lt2_tt',
    ('VIE_rp', '>', '0'): 'VIE_var_rp_pos_tt',
}
# keys that may not exist yet -> (text, text when negated).  None = "Không đúng: <text>"
NEW_LOC = {
    'VIE_flag_VIE_sched_congress_9_tt': ('Đại hội IX đã khai mạc', None),
    'VIE_flag_VIE_sched_congress_10_tt': ('Đại hội X đã khai mạc', None),
    'VIE_flag_VIE_bop_active_tt': ('Cán cân định hướng của Đảng đang hoạt động', None),
    'VIE_flag_bankruptcy_incoming_collapse_tt': ('Ngân sách quốc gia đang đứng trước nguy cơ phá sản',
                                                 'Ngân sách quốc gia chưa đứng trước nguy cơ phá sản'),
    'VIE_var_rp_pos_tt': ('Áp lực cải cách lớn hơn 0', 'Áp lực cải cách đã về 0'),
}
# ruling_party = N  ->  MD trigger (chuẩn mục 6b)
RULING_PARTY = {
    '4': 'emerging_communist_state_are_in_power = yes',
    '7': 'emerging_autocracy_are_in_power = yes',
    '19': 'neutrality_neutral_communism_are_in_power = yes',
}
HIDDEN = {'hidden_effect', 'ai_will_do', 'log', 'search_filters', 'custom_trigger_tooltip', 'hidden_trigger', 'modifier',
          'icon', 'x', 'y', 'relative_position_id', 'prerequisite', 'mutually_exclusive', 'cost', 'id', 'allow_branch'}
VARFX = ('add_to_variable', 'set_variable', 'subtract_from_variable', 'multiply_variable', 'divide_variable', 'clamp_variable')


def read(p):
    raw = open(p, 'rb').read()
    return raw[:3] == b'\xef\xbb\xbf', raw.decode('utf-8-sig')


def write(p, bom, s):
    open(p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + s.encode('utf-8'))


def load_loc():
    loc = set()
    for f in glob.glob(os.path.join(ROOT, 'localisation/**/*.yml'), recursive=True):
        for ln in open(f, encoding='utf-8-sig'):
            m = re.match(r'\s*([A-Za-z0-9_.\-]+):\d*\s+"', ln)
            if m:
                loc.add(m.group(1))
    return loc


def parse(src):
    tok = re.compile(r'#[^\n]*|"[^"\n]*"|[{}=<>]|[^\s{}=<>#"]+')
    toks = [(m.group(0), src.count('\n', 0, m.start()) + 1) for m in tok.finditer(src) if not m.group(0).startswith('#')]
    pos = 0

    def block():
        nonlocal pos
        items = []
        while pos < len(toks):
            t, l = toks[pos]
            if t == '}':
                pos += 1
                return items
            if t in '{=<>':
                pos += 1
                continue
            pos += 1
            if pos < len(toks) and toks[pos][0] in ('=', '<', '>'):
                pos += 1
                if toks[pos][0] == '{':
                    pos += 1
                    v = block()
                else:
                    v = toks[pos][0]
                    pos += 1
                items.append((t, v, l))
            else:
                items.append((t, None, l))
        return items

    tree = block()
    ft = [v for k, v, l in tree if k == 'focus_tree'][0]
    return [v for k, v, l in ft if k == 'focus' and isinstance(v, list)]


def find_issues(focuses):
    issues = []  # (line, kind, payload, focus)

    def walk(items, fid, ctx):
        for k, v, l in items:
            if k in HIDDEN:
                continue
            if isinstance(v, list):
                if ctx == 'trig' and k == 'check_variable':
                    d = {kk: vv for kk, vv, _ in v}
                    issues.append((l, 'checkvar', d, fid))
                elif ctx == 'eff' and k in VARFX:
                    if not any(kk == 'tooltip' for kk, _, _ in v):
                        issues.append((l, 'var', k, fid))
                elif k == 'limit':
                    walk(v, fid, 'trig')
                else:
                    walk(v, fid, ctx)
            elif ctx == 'trig' and k == 'has_country_flag':
                issues.append((l, 'flag', v, fid))
            elif ctx == 'eff' and k == 'set_country_flag':
                issues.append((l, 'setflag', v, fid))

    for f in focuses:
        fid = next(v for k, v, l in f if k == 'id')
        for blk in ('available', 'bypass', 'allowed', 'cancel'):
            for k, v, l in f:
                if k == blk and isinstance(v, list):
                    walk(v, fid, 'trig')
        for blk in ('completion_reward', 'bypass_effect', 'select_effect'):
            for k, v, l in f:
                if k == blk and isinstance(v, list):
                    walk(v, fid, 'eff')
    return issues


def hide_ax_init_blocks(lines, nl):
    """Wrap the one-time VIE_ax_initialized guard 'if' blocks in hidden_effect."""
    out, i, n = [], 0, 0
    while i < len(lines):
        m = re.match(r'^(\t+)if = \{\s*$', lines[i])
        if (m and i + 1 < len(lines) and 'has_country_flag = VIE_ax_initialized' in lines[i + 1]
                and not (out and out[-1].strip() == 'hidden_effect = {')):
            ind = m.group(1)
            j = i + 1
            while not re.match(r'^' + ind + r'\}\s*$', lines[j]):
                j += 1
            out.append(ind + 'hidden_effect = {')
            out.extend('\t' + x for x in lines[i:j + 1])
            out.append(ind + '}')
            i = j + 1
            n += 1
        else:
            out.append(lines[i])
            i += 1
    return out, n


def main():
    bom, s = read(FOCUS)
    nl = '\r\n' if '\r\n' in s else '\n'
    lines = s.split(nl)
    lines, n_ax = hide_ax_init_blocks(lines, nl)
    s = nl.join(lines)
    focuses = parse(s)
    loc = load_loc()
    new_loc, report = {}, []

    def flag_key(flag):
        for k in ('VIE_flag_%s_tt' % flag, 'VIE_flag_%s_tt' % flag[4:] if flag.startswith('VIE_') else None):
            if k and k in loc:
                return k
        for k in ('VIE_flag_%s_tt' % flag, 'VIE_flag_%s_tt' % flag[4:] if flag.startswith('VIE_') else None):
            if k in NEW_LOC:
                return k
        return None

    lines = s.split(nl)
    for line, kind, payload, fid in sorted(find_issues(focuses), key=lambda x: -x[0]):
        t = lines[line - 1]
        ind = re.match(r'\t*', t).group(0)
        if kind == 'flag':
            key = flag_key(payload)
            if not key:
                report.append('NO KEY for flag %s (%s:%d)' % (payload, fid, line))
                continue
            pat = r'has_country_flag = %s\b' % re.escape(payload)
            lines[line - 1] = re.sub(pat, 'custom_trigger_tooltip = { tooltip = %s has_country_flag = %s }' % (key, payload), t, count=1)
        elif kind == 'setflag':
            lines[line - 1] = re.sub(r'set_country_flag = (\S+)', r'hidden_effect = { set_country_flag = \1 }', t, count=1)
        elif kind == 'checkvar':
            m = re.search(r'check_variable = \{ ([A-Za-z0-9_]+) ([<>=]) (\d+) \}', t)
            if not m:
                report.append('UNPARSED checkvar %s:%d: %s' % (fid, line, t.strip()))
                continue
            trip = m.groups()
            if trip[:2] == ('ruling_party', '=') and trip[2] in RULING_PARTY:
                rep = RULING_PARTY[trip[2]]
            elif trip in CHECKVAR:
                rep = 'custom_trigger_tooltip = { tooltip = %s %s }' % (CHECKVAR[trip], m.group(0))
            else:
                report.append('NO KEY for %s %s %s (%s:%d)' % (trip + (fid, line)))
                continue
            lines[line - 1] = t[:m.start()] + rep + t[m.end():]
        elif kind == 'var':
            m = re.match(r'^(\t+)((?:%s) = \{ [^{}]* \})\s*$' % '|'.join(VARFX), t)
            if not m:
                report.append('MULTILINE var %s:%d: %s' % (fid, line, t.strip()))
                continue
            lines[line - 1] = '%shidden_effect = { %s }' % (m.group(1), m.group(2))
            if payload == 'set_variable' and 'VIE_vinashin_risk = 0' in t:
                lines[line - 1] += nl + '%scustom_effect_tooltip = VIE_vinashin_risk_reset_tt' % m.group(1)
    s = nl.join(lines)
    new_loc = {k: v for k, v in NEW_LOC.items() if k not in loc}

    print('ax_init guards hidden: %d | new loc keys: %d | unresolved: %d' % (n_ax, len(new_loc), len(report)))
    for r in report:
        print('  !', r)
    if DRY:
        return
    write(FOCUS, bom, s)
    if new_loc:
        lb, ls = read(LOC_NEW)
        lnl = '\r\n' if '\r\n' in ls else '\n'
        if not ls.endswith(lnl):
            ls += lnl
        ls += lnl + ' # ---- Cờ lịch Đại hội (fix_focus_raw_text.py)' + lnl
        for k, (v, vn) in sorted(new_loc.items()):
            ls += ' %s:0 "%s"%s' % (k, v, lnl)
            ls += ' %s_NOT:0 "%s"%s' % (k, vn or 'Không đúng: ' + v, lnl)
        write(LOC_NEW, True, ls)


if __name__ == '__main__':
    main()
