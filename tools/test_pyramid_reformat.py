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

for f in focuses:
    f["cur_abs_x"], f["cur_abs_y"] = get_abs(f["id"], fmap)

# Let's clone focuses to test compression
test_map = {f["id"]: dict(f) for f in focuses}

# Identify subtrees in KINH TE:
# 1. vinacomin & energy subtrees:
# Focuses anchored to vinacomin_founding:
# vinacomin_founding, bauxite_tay_nguyen, bauxite_suspend, rare_earths, than_quang_ninh, nui_phao_tungsten, thach_khe_mine_start
# And energy sector focuses (petrovietnam, refineries, hydro, solar, wind, nuclear)
# Currently vinacomin is at abs_x = 104.
# If we shift vinacomin by -10: abs_x becomes 94.
# All children anchored to vinacomin automatically shift by -10!
test_map["VIE_vinacomin_founding"]["x"] -= 10

# Energy focuses anchored to VIE_doi_moi_continues:
energy_fids = [
    "VIE_strategic_petroleum_reserve", "VIE_son_la_dam", "VIE_petrolimex_green_ev_hubs",
    "VIE_petrolimex_eneos_partnership", "VIE_petrovietnam_expansion", "VIE_shelve_nuclear",
    "VIE_revive_nuclear", "VIE_petrolimex_downstream_network", "VIE_500kv_grid",
    "VIE_dppa_market_reform", "VIE_dung_quat_refinery", "VIE_build_nuclear_plant",
    "VIE_net_zero_2050", "VIE_coal_power", "VIE_jetp_partnership", "VIE_solar_boom",
    "VIE_nghi_son_refinery", "VIE_solar_auction", "VIE_power_plan_8", "VIE_ninh_thuan_nuclear",
    "VIE_offshore_wind", "VIE_energy_security_2045"
]
for fid in energy_fids:
    test_map[fid]["x"] -= 10

# 2. industrialization subtree:
# VIE_industrialization_strategy was at abs_x = 130 (rel_x = 50 from doi_moi at 80).
# If we shift it by -18: rel_x becomes 32, abs_x becomes 112.
# All 24 children anchored to industrialization_strategy automatically shift by -18!
test_map["VIE_industrialization_strategy"]["x"] -= 18

# 3. internet & digital subtree:
# VIE_internet_expansion was at abs_x = 152 (rel_x = 72).
# If we shift it by -26: rel_x becomes 46, abs_x becomes 126.
# All 11 children anchored to internet_expansion automatically shift by -26!
test_map["VIE_internet_expansion"]["x"] -= 26

# Space & Science focuses anchored to VIE_doi_moi_continues:
science_fids = [
    "VIE_research_universities", "VIE_nuclear_research", "VIE_nafosted",
    "VIE_science_breakthrough", "VIE_vinasat", "VIE_earth_observation"
]
for fid in science_fids:
    test_map[fid]["x"] -= 26

# 4. upper_middle_income subtree:
# VIE_upper_middle_income was at abs_x = 166 (rel_x = 86).
# If we shift it by -28: rel_x becomes 58, abs_x becomes 138.
# All 7 children automatically shift by -28!
test_map["VIE_upper_middle_income"]["x"] -= 28

# 5. QUAN SU:
# VIE_modernize_vpa was at abs_x = 194 (rel_x = 114 from doi_moi at 80).
# If we shift it by -48: rel_x becomes 66, abs_x becomes 146!
# All 91 military children automatically shift by -48!
test_map["VIE_modernize_vpa"]["x"] -= 48

# 6. AN NINH:
# Currently at abs_x in [98, 102].
# If we shift AN NINH by -6: abs_x becomes [92, 96].
sec_fids = [
    "VIE_sec_cyber_control", "VIE_sec_surveillance_network", "VIE_sec_public_order",
    "VIE_sec_security_economy", "VIE_sec_cyber_sovereignty", "VIE_sec_loyalty_vetting",
    "VIE_sec_border_control", "VIE_sec_managed_opening"
]
for fid in sec_fids:
    test_map[fid]["x"] -= 6

# Calculate new absolute coordinates
for fid, f in test_map.items():
    f["new_abs_x"], f["new_abs_y"] = get_abs(fid, test_map)

# Check collisions
coords = defaultdict(list)
for fid, f in test_map.items():
    coords[(f["new_abs_x"], f["new_abs_y"])].append(fid)

dups = {k: v for k, v in coords.items() if len(v) > 1}
print(f"\nCOLLISION CHECK: {len(dups)} duplicate absolute coordinates found.")
for k, v in sorted(dups.items()):
    print(f"  Collision at {k}: {v}")

# Check branch bounds
sys.path.insert(0, str(Path.cwd()))
from tools.refine_categories import refine_categorize

branch_bounds = defaultdict(list)
for fid, f in test_map.items():
    c = refine_categorize(f)
    if f["id"] in ["VIE_china_plus_one", "VIE_mekong_climate_adaptation"]:
        c = "KINH_TE"
    elif f["id"] in ["VIE_bamboo_diplomacy", "VIE_gulf_investment"]:
        c = "DOI_NGOAI"
    branch_bounds[c].append(f)

print("\nNEW COMPACT BRANCH BOUNDS:")
for c, flist in sorted(branch_bounds.items()):
    xs = [f["new_abs_x"] for f in flist]
    ys = [f["new_abs_y"] for f in flist]
    print(f"  {c:10s} : {len(flist):3d} focuses | abs_x: [{min(xs):3d}, {max(xs):3d}] (w={max(xs)-min(xs):2d}) | abs_y: [{min(ys):2d}, {max(ys):2d}]")

# Check overall canvas width
all_xs = [f["new_abs_x"] for f in test_map.values()]
print(f"\nOVERALL CANVAS WIDTH: [{min(all_xs)}, {max(all_xs)}] (Total span: {max(all_xs) - min(all_xs)} columns)")

# Check minimum gaps on each row
by_row = defaultdict(list)
for fid, f in test_map.items():
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

print(f"GAPS < 2 (TOO CLOSE): {len(bad_gaps)}")
for g in bad_gaps[:10]:
    print(" ", g)
