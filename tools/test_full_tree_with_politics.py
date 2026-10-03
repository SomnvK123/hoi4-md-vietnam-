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
    focuses[fid] = {
        'id': fid, 'x': int(xm.group(1)) if xm else 0, 'y': int(ym.group(1)) if ym else 0,
        'rel': rel.group(1) if rel else None, 'prereqs': prereqs
    }

# Load new politics layout (absolute coordinates)
from tools.optimize_politics_pyramid import layout
politics_abs = {k: (v[0] + 2, v[1]) for k, v in layout.items()}

# Update tmap
tmap = {k: dict(v) for k, v in focuses.items()}

for fid, (ax, ay) in politics_abs.items():
    # Anchor directly to VIE_doi_moi_continues at (80, 0)
    tmap[fid]["rel"] = "VIE_doi_moi_continues"
    tmap[fid]["x"] = ax - 80
    tmap[fid]["y"] = ay

def get_abs(fid, dmap, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = dmap.get(fid)
    if not f or not f["rel"]: return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], dmap, visited)
    return rx + f["x"], ry + f["y"]

for fid, f in tmap.items():
    f["abs_x"], f["abs_y"] = get_abs(fid, tmap)

coords = defaultdict(list)
for fid, f in tmap.items():
    coords[(f["abs_x"], f["abs_y"])].append(fid)

dups = {k: v for k, v in coords.items() if len(v) > 1}
print(f"COLLISION CHECK (FULL MOD): {len(dups)} duplicates")
for k, v in dups.items():
    print(f"  Collision at {k}: {v}")

by_y = defaultdict(list)
for fid, f in tmap.items():
    by_y[f["abs_y"]].append((f["abs_x"], fid))

bad_gaps = []
for y, items in sorted(by_y.items()):
    items.sort()
    for i in range(len(items) - 1):
        x1, f1 = items[i]
        x2, f2 = items[i+1]
        if x2 - x1 < 2:
            bad_gaps.append((y, f1, x1, f2, x2, x2 - x1))
print(f"GAPS < 2: {len(bad_gaps)}")
for g in bad_gaps:
    print(" ", g)

upward = []
for fid, f in tmap.items():
    for p in f["prereqs"]:
        if p in tmap:
            pf = tmap[p]
            if f["abs_y"] <= pf["abs_y"]:
                upward.append((p, fid, pf["abs_y"], f["abs_y"]))
print(f"UPWARD ARROWS: {len(upward)}")
for u in upward:
    print(" ", u)

from tools.refine_categories import refine_categorize
branches = defaultdict(list)
for f in tmap.values():
    c = refine_categorize(f)
    if f["id"] in ["VIE_china_plus_one", "VIE_mekong_climate_adaptation"]: c = "KINH_TE"
    elif f["id"] in ["VIE_bamboo_diplomacy", "VIE_gulf_investment"]: c = "DOI_NGOAI"
    elif f["id"] in ["VIE_un_peacekeeping", "VIE_four_nos_doctrine"]: c = "BIEN_DONG"
    branches[c].append(f)

print("\nBRANCH BOUNDS:")
for c, flist in sorted(branches.items()):
    xs = [f["abs_x"] for f in flist]
    ys = [f["abs_y"] for f in flist]
    print(f"  {c:12s}: {len(flist):3d} focuses | X=[{min(xs):3d}, {max(xs):3d}] (w={max(xs)-min(xs):2d}) | Y=[{min(ys):2d}, {max(ys):2d}] (h={max(ys)-min(ys):2d})")
