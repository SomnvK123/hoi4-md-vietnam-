import re
from pathlib import Path
from collections import defaultdict, Counter
import sys

# Load current focus blocks
txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")

focuses = []
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    for i in range(m.end(), len(txt)):
        if txt[i] == "{": brace += 1
        elif txt[i] == "}":
            brace -= 1
            if brace == 0:
                end = i + 1
                break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    xm = re.search(r"\bx\s*=\s*(-?\d+)", block)
    ym = re.search(r"\by\s*=\s*(-?\d+)", block)
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    focuses.append({
        "id": fid, "x": int(xm.group(1)) if xm else 0, "y": int(ym.group(1)) if ym else 0,
        "rel": rel.group(1) if rel else None, "prereqs": prereqs,
        "block": block, "start": start, "end": end
    })

fmap = {f["id"]: f for f in focuses}

def get_abs(fid, dmap, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = dmap.get(fid)
    if not f or not f["rel"]: return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], dmap, visited)
    return rx + f["x"], ry + f["y"]

# Clone
tmap = {f["id"]: dict(f) for f in focuses}

# 1. CENTER DIPLOMACY (DOI NGOAI) INTO A SYMMETRICAL PYRAMID:
# Center VIE_asean_integration at abs_x = 46, abs_y = 12.
# In current file: VIE_asean_integration is at abs_x = 32 (x = -48 from doi_moi at 80).
# New abs_x = 46 -> x = 46 - 80 = -34.
tmap["VIE_asean_integration"]["x"] = -34
tmap["VIE_asean_integration"]["y"] = 12

# Shift all 33 children of VIE_asean_integration by -14 so they fan out [-14, +14] around 46!
for f in tmap.values():
    if f["rel"] == "VIE_asean_integration":
        f["x"] -= 14

# 2. CENTER BIEN DONG INTO A SYMMETRICAL PYRAMID:
# In current file: VIE_law_of_the_sea is at abs_x = 82 (x = 2 from doi_moi at 80).
# Its children span rel_x in [-14, 8]. Center is -3.
# Let's set VIE_law_of_the_sea at abs_x = 76 (x = 76 - 80 = -4, y = 13).
# And shift children by +3 so they span [-11, +11] around 76 (abs_x in [65, 87])!
tmap["VIE_law_of_the_sea"]["x"] = -4
tmap["VIE_law_of_the_sea"]["y"] = 13

for f in tmap.values():
    if f["rel"] == "VIE_law_of_the_sea" and f["id"] not in ["VIE_un_peacekeeping", "VIE_four_nos_doctrine"]:
        f["x"] += 3

# Bridge: un_peacekeeping & four_nos_doctrine:
# Peoples defence in Bien Dong: abs_x = 77, y = 17.
# Place un_peacekeeping at abs (81, 18), four_nos at abs (81, 19):
# Rel to law_of_the_sea (76, 13):
# un_peacekeeping: x = 81 - 76 = 5, y = 18 - 13 = 5
# four_nos_doctrine: x = 81 - 76 = 5, y = 19 - 13 = 6
tmap["VIE_un_peacekeeping"]["x"] = 5
tmap["VIE_un_peacekeeping"]["y"] = 5
tmap["VIE_four_nos_doctrine"]["x"] = 5
tmap["VIE_four_nos_doctrine"]["y"] = 6

# 3. COMPACT AN NINH:
# Place AN NINH close to Bien Dong:
# Bien Dong ends at abs_x = 87.
# Place AN NINH at abs_x in [91, 95] (center = 93):
# In current file: sec_cyber_control was at abs_x = 100 (x = 20 from doi_moi at 80).
# Shift by -7:
sec_fids = [
    "VIE_sec_cyber_control", "VIE_sec_surveillance_network", "VIE_sec_public_order",
    "VIE_sec_security_economy", "VIE_sec_cyber_sovereignty", "VIE_sec_loyalty_vetting",
    "VIE_sec_border_control", "VIE_sec_managed_opening"
]
for fid in sec_fids:
    tmap[fid]["x"] -= 7

# 4. COMPACT MILITARY (QUAN SU) PYRAMID:
# Military spans [175, 236], width = 61. Center is at abs 206!
# Aisle between KINH TE (ends at 170) and QUAN SU (starts at 175) is 5 columns.
# Head VIE_modernize_vpa at abs 206 (x = 206 - 80 = 126 from doi_moi at 80).
tmap["VIE_modernize_vpa"]["x"] = 126
tmap["VIE_modernize_vpa"]["y"] = 1
# Army: abs 180 -> rel_x = 180 - 206 = -26
tmap["VIE_lf_army_reform"]["x"] = -26
# Navy: abs 198 -> rel_x = 198 - 206 = -8
tmap["VIE_nf_training_standardization"]["x"] = -8
# Air Force: abs 218 -> rel_x = 218 - 206 = 12
tmap["VIE_airf_training_standardization"]["x"] = 12

# Calculate new absolute coordinates
for fid, f in tmap.items():
    f["new_abs_x"], f["new_abs_y"] = get_abs(fid, tmap)

# Check collisions
coords = defaultdict(list)
for fid, f in tmap.items():
    coords[(f["new_abs_x"], f["new_abs_y"])].append(fid)

dups = {k: v for k, v in coords.items() if len(v) > 1}
print(f"\nCOLLISION CHECK: {len(dups)} duplicate absolute coordinates found.")
for k, v in sorted(dups.items()):
    print(f"  Collision at {k}: {v}")

# Check minimum gaps on each row
by_row = defaultdict(list)
for fid, f in tmap.items():
    by_row[f["new_abs_y"]].append((f["new_abs_x"], fid))

bad_gaps = []
for y, items in sorted(by_row.items()):
    items.sort()
    for i in range(len(items) - 1):
        x1, f1 = items[i]
        x2, f2 = items[i+1]
        gap = x2 - x1
        if gap < 2:
            bad_gaps.append((y, f1, x1, f2, x2, gap))

print(f"GAPS < 2: {len(bad_gaps)}")
for g in bad_gaps[:10]:
    print(" ", g)

# Check upward arrows
upward = []
for fid, f in tmap.items():
    for p in f["prereqs"]:
        if p in tmap:
            pf = tmap[p]
            dy = f["new_abs_y"] - pf["new_abs_y"]
            if dy < 0:
                upward.append((p, fid, dy))

print(f"UPWARD ARROWS: {len(upward)}")
for u in upward:
    print(" ", u)

# Check branch bounds
sys.path.insert(0, str(Path.cwd()))
from tools.refine_categories import refine_categorize

branch_bounds = defaultdict(list)
for fid, f in tmap.items():
    c = refine_categorize(f)
    if f["id"] in ["VIE_china_plus_one", "VIE_mekong_climate_adaptation"]:
        c = "KINH_TE"
    elif f["id"] in ["VIE_bamboo_diplomacy", "VIE_gulf_investment"]:
        c = "DOI_NGOAI"
    branch_bounds[c].append(f)

print("\nNEW PYRAMID BRANCH BOUNDS:")
for c, flist in sorted(branch_bounds.items()):
    xs = [f["new_abs_x"] for f in flist]
    ys = [f["new_abs_y"] for f in flist]
    print(f"  {c:10s} : {len(flist):3d} focuses | abs_x: [{min(xs):3d}, {max(xs):3d}] (w={max(xs)-min(xs):2d}) | abs_y: [{min(ys):2d}, {max(ys):2d}]")

all_xs = [f["new_abs_x"] for f in tmap.values()]
print(f"\nOVERALL CANVAS SPAN: [{min(all_xs)}, {max(all_xs)}] (Total width: {max(all_xs) - min(all_xs)} columns)")
