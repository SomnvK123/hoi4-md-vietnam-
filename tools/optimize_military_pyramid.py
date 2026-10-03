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

# Let's inspect the entire Military DAG and find the tightest Y coordinate assignment
memo = {}
def get_depth(fid):
    if fid in memo: return memo[fid]
    f = focuses[fid]
    mil_p = [p for p in f['prereqs'] if p in mil_fids]
    if not mil_p:
        memo[fid] = 1
        return 1
    d = 1 + max(get_depth(p) for p in mil_p)
    memo[fid] = d
    return d

min_y = {fid: get_depth(fid) for fid in mil_fids}
print(f"Minimum possible Y for force_complete: {min_y['VIE_lf_force_complete']}")
print(f"Minimum possible Y for nf_regional_command: {min_y['VIE_nf_regional_command']}")
print(f"Minimum possible Y for airf_teaming: {min_y['VIE_airf_teaming']}")
