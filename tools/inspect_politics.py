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
pol_fids = [fid for fid, f in focuses.items() if refine_categorize(f) == 'CHINH_TRI']
print(f"Total CHINH TRI focuses: {len(pol_fids)}")

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = focuses.get(fid)
    if not f or not f['rel']: return f['x'], f['y']
    rx, ry = get_abs(f['rel'], visited)
    return rx + f['x'], ry + f['y']

for fid in sorted(pol_fids, key=lambda f: (get_abs(f)[1], get_abs(f)[0])):
    f = focuses[fid]
    ax, ay = get_abs(fid)
    p_str = ", ".join([p.replace("VIE_", "") for p in f['prereqs']])
    r_str = f['rel'].replace("VIE_", "") if f['rel'] else "None"
    short_id = fid.replace("VIE_", "")
    print(f"{short_id:30s} | abs=({ax:2d}, {ay:2d}) | rel={r_str:20s} ({f['x']:3d}, {f['y']:2d}) | prereqs=[{p_str}]")
