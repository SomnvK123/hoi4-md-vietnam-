import re
from pathlib import Path
from collections import defaultdict
import sys
sys.path.insert(0, ".")

txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")
focuses = {}
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    for i in range(m.end(), len(txt)):
        if txt[i] == '{': brace += 1
        elif txt[i] == '}':
            brace -= 1
            if brace == 0: end = i + 1; break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    xm = re.search(r"\bx\s*=\s*(-?\d+)", block)
    ym = re.search(r"\by\s*=\s*(-?\d+)", block)
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    mut = re.findall(r"\bmutually_exclusive\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    focuses[fid] = {
        'id': fid, 'x': int(xm.group(1)) if xm else 0, 'y': int(ym.group(1)) if ym else 0,
        'rel': rel.group(1) if rel else None, 'prereqs': prereqs, 'mut': mut
    }

from tools.refine_categories import refine_categorize
mil_fids = [fid for fid, f in focuses.items() if refine_categorize(f) == 'QUAN_SU']

def get_depth(fid, memo=None):
    if memo is None: memo = {}
    if fid in memo: return memo[fid]
    f = focuses[fid]
    mil_p = [p for p in f['prereqs'] if p in mil_fids]
    if not mil_p:
        memo[fid] = 1
        return 1
    d = 1 + max(get_depth(p, memo) for p in mil_p)
    memo[fid] = d
    return d

depths = {fid: get_depth(fid) for fid in mil_fids}

services = {
    'Army': [f for f in mil_fids if 'lf_' in f or f == 'VIE_lf_army_reform'],
    'Navy': [f for f in mil_fids if 'nf_' in f or f in ['VIE_small_combatant_construction', 'VIE_ba_son_shipyards', 'VIE_naval_defence_2030', 'VIE_naval_defence_law', 'VIE_naval_mro', 'VIE_naval_systems_integration']],
    'Air Force': [f for f in mil_fids if 'airf_' in f or 'apm_' in f],
    'Common/CNQP': ['VIE_modernize_vpa', 'VIE_def_industry_law', 'VIE_military_enterprises_core', 'VIE_military_enterprises_divest']
}

for sname, fids in services.items():
    s_depths = [depths[f] for f in fids]
    print(f"\n=== {sname} ({len(fids)} focuses) | Critical Path: {max(s_depths)} rows ===")
    by_d = defaultdict(list)
    for f in fids:
        by_d[depths[f]].append(f.replace("VIE_", ""))
    for d in sorted(by_d):
        print(f"  Level {d:2d} ({len(by_d[d])} focuses): {by_d[d]}")
