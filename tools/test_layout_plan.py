import re
from pathlib import Path
from collections import defaultdict, Counter
import sys
sys.path.insert(0, str(Path.cwd()))

txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")

focus_matches = []
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    end = m.end()
    for i in range(m.end(), len(txt)):
        if txt[i] == "{": brace += 1
        elif txt[i] == "}":
            brace -= 1
            if brace == 0:
                end = i + 1
                break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    x = int(re.search(r"\bx\s*=\s*(-?\d+)", block).group(1)) if re.search(r"\bx\s*=\s*(-?\d+)", block) else 0
    y = int(re.search(r"\by\s*=\s*(-?\d+)", block).group(1)) if re.search(r"\by\s*=\s*(-?\d+)", block) else 0
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    rel = rel.group(1) if rel else None
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    
    focus_matches.append({
        "id": fid, "x": x, "y": y, "rel": rel, "prereqs": prereqs,
        "block": block, "order": len(focus_matches)
    })

fmap = {f["id"]: f for f in focus_matches}

def get_abs(fid, dmap, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = dmap.get(fid)
    if not f: return 0, 0
    if not f["rel"]: return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], dmap, visited)
    return rx + f["x"], ry + f["y"]

# Old abs coordinates
for f in focus_matches:
    f["old_abs_x"], f["old_abs_y"] = get_abs(f["id"], fmap)

# Let's clone focuses to test new layout
new_fmap = {}
for f in focus_matches:
    new_fmap[f["id"]] = dict(f)

# Shift KINH_TE by shift_k = -32:
# VIE_doi_moi_continues moves from (112, 0) to (80, 0)
new_fmap["VIE_doi_moi_continues"]["x"] = 80
new_fmap["VIE_doi_moi_continues"]["y"] = 0

# CHINH_TRI:
# Keep CHINH_TRI absolute coordinates identical to old (x in [2, 24]),
# so any focus in CHINH_TRI whose rel == 'VIE_doi_moi_continues' has its relative x adjusted:
# new_rel_x = old_abs_x - 80 = (old_rel_x + 112) - 80 = old_rel_x + 32!
from tools.refine_categories import refine_categorize

for f in new_fmap.values():
    c = refine_categorize(f)
    if c == "CHINH_TRI":
        if f["rel"] == "VIE_doi_moi_continues":
            f["x"] = f["old_abs_x"] - 80
        elif f["id"] == "VIE_higher_education_law":
            f["x"] = 4 # rel to constitution_2013 (16, 10) -> (20, 11)
            f["y"] = 1
        elif f["id"] == "VIE_education_law_2019":
            f["x"] = 4
            f["y"] = 2
        elif f["id"] == "VIE_disaster_law_2013":
            f["x"] = 8 # rel to constitution_2013 -> (24, 11)
            f["y"] = 1
        elif f["id"] == "VIE_civil_defense_law_2023":
            f["x"] = 8
            f["y"] = 2

# QUAN_SU:
# Shift QUAN_SU by -28:
# All military focuses shift abs_x by -28.
# VIE_modernize_vpa was at (222, 1). New abs is (194, 1).
# Relative to VIE_doi_moi_continues (80, 0): rel_x = 194 - 80 = 114, rel_y = 1.
new_fmap["VIE_modernize_vpa"]["x"] = 114
new_fmap["VIE_modernize_vpa"]["y"] = 1

# What other focuses in QUAN_SU were directly anchored to VIE_doi_moi_continues?
for f in new_fmap.values():
    c = refine_categorize(f)
    if c == "QUAN_SU" and f["rel"] == "VIE_doi_moi_continues" and f["id"] != "VIE_modernize_vpa":
        f["x"] = (f["old_abs_x"] - 28) - 80

# DOI_NGOAI:
# Root: VIE_asean_integration
# Place at abs (32, 12):
# Relative to VIE_doi_moi_continues (80, 0):
new_fmap["VIE_asean_integration"]["x"] = 32 - 80 # -48
new_fmap["VIE_asean_integration"]["y"] = 12

# BIEN_DONG:
# Root: VIE_law_of_the_sea
# Place at abs (82, 13):
# Relative to VIE_doi_moi_continues (80, 0):
new_fmap["VIE_law_of_the_sea"]["x"] = 82 - 80 # 2
new_fmap["VIE_law_of_the_sea"]["y"] = 13

# un_peacekeeping & four_nos:
# In old layout, un_peacekeeping was anchored to VIE_law_of_the_sea at rel=(2, 5).
# If VIE_law_of_the_sea is at (82, 13), let's put un_peacekeeping at (64, 18) and four_nos at (64, 19)
# Relative to VIE_law_of_the_sea (82, 13):
# un_peacekeeping: x = 64 - 82 = -18, y = 18 - 13 = 5
new_fmap["VIE_un_peacekeeping"]["x"] = -18
new_fmap["VIE_un_peacekeeping"]["y"] = 5

# four_nos_doctrine:
# rel to law_of_the_sea: x = 64 - 82 = -18, y = 19 - 13 = 6
new_fmap["VIE_four_nos_doctrine"]["x"] = -18
new_fmap["VIE_four_nos_doctrine"]["y"] = 6

# AN_NINH:
# Root: VIE_sec_cyber_control
# Place at abs (100, 13):
new_fmap["VIE_sec_cyber_control"]["x"] = 100 - 80 # 20
new_fmap["VIE_sec_cyber_control"]["y"] = 13

# Other 7 focuses in AN_NINH were anchored to VIE_doi_moi_continues:
# In old layout:
# VIE_sec_surveillance_network: rel=(136, 23) -> abs=(248, 23). Delta from cyber_control: (-2, 1)
# VIE_sec_public_order: rel=(138, 23) -> abs=(250, 23). Delta: (0, 1)
# VIE_sec_security_economy: rel=(140, 23) -> abs=(252, 23). Delta: (+2, 1)
# VIE_sec_cyber_sovereignty: rel=(136, 24) -> abs=(248, 24). Delta: (-2, 2)
# VIE_sec_loyalty_vetting: rel=(138, 24) -> abs=(250, 24). Delta: (0, 2)
# VIE_sec_border_control: rel=(140, 24) -> abs=(252, 24). Delta: (+2, 2)
# VIE_sec_managed_opening: rel=(138, 25) -> abs=(250, 25). Delta: (0, 3)
sec_deltas = {
    "VIE_sec_surveillance_network": (-2, 1),
    "VIE_sec_public_order": (0, 1),
    "VIE_sec_security_economy": (2, 1),
    "VIE_sec_cyber_sovereignty": (-2, 2),
    "VIE_sec_loyalty_vetting": (0, 2),
    "VIE_sec_border_control": (2, 2),
    "VIE_sec_managed_opening": (0, 3)
}
for sid, (dx, dy) in sec_deltas.items():
    new_fmap[sid]["x"] = (100 + dx) - 80
    new_fmap[sid]["y"] = 13 + dy

# Calculate new absolute coordinates
for fid, f in new_fmap.items():
    f["new_abs_x"], f["new_abs_y"] = get_abs(fid, new_fmap)

# Check collisions
coords = defaultdict(list)
for fid, f in new_fmap.items():
    coords[(f["new_abs_x"], f["new_abs_y"])].append(fid)

dups = {k: v for k, v in coords.items() if len(v) > 1}
print(f"\nCOLLISION CHECK: {len(dups)} duplicate absolute coordinates found.")
for k, v in sorted(dups.items()):
    print(f"  Collision at {k}: {v}")

# Bounds check by branch
branch_bounds = defaultdict(list)
for fid, f in new_fmap.items():
    c = refine_categorize(f)
    branch_bounds[c].append(f)

print("\nNEW BRANCH BOUNDS:")
for c, flist in sorted(branch_bounds.items()):
    xs = [f["new_abs_x"] for f in flist]
    ys = [f["new_abs_y"] for f in flist]
    print(f"  {c:10s} : {len(flist):3d} focuses | abs_x: [{min(xs):3d}, {max(xs):3d}] | abs_y: [{min(ys):3d}, {max(ys):3d}]")
