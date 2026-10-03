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
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    mut = re.findall(r"\bmutually_exclusive\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    focuses[fid] = {'id': fid, 'prereqs': prereqs, 'mut': mut}

from tools.refine_categories import refine_categorize
pol_fids = [fid for fid, f in focuses.items() if refine_categorize(f) == 'CHINH_TRI']

# Let's design a 11-row Pyramid Layout with center at X = 12
# Available X columns: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22

layout = {
    # Row 1: Apex
    "VIE_prepare_congress_9": (12, 1),

    # Row 2: 3 nodes
    "VIE_grassroots_democracy": (8, 2),
    "VIE_resolution_congress_9": (12, 2),
    "VIE_mass_mobilization": (16, 2),

    # Row 3: 5 nodes
    "VIE_ethnic_policy": (6, 3),
    "VIE_national_assembly_role": (8, 3),
    "VIE_state_audit": (10, 3),
    "VIE_resolution_congress_10": (12, 3),
    "VIE_public_admin_reform": (16, 3),

    # Row 4: 5 nodes
    "VIE_party_members_private_business": (6, 4),
    "VIE_anti_corruption_steering": (8, 4),
    "VIE_anti_corruption_law": (10, 4),
    "VIE_resolution_congress_11": (12, 4),
    "VIE_decentralization": (16, 4),

    # Row 5: 5 nodes
    "VIE_asset_declaration": (6, 5),
    "VIE_tw4_party_building": (8, 5),
    "VIE_platform_2011": (10, 5),
    "VIE_resolution_congress_12": (12, 5),
    "VIE_rule_of_law_state": (16, 5),

    # Row 6: 5 nodes
    "VIE_party_inspection": (6, 6),
    "VIE_resolution_congress_13": (12, 6),
    "VIE_streamline_apparatus": (14, 6),
    "VIE_constitution_2013": (16, 6),
    "VIE_cybersecurity_law": (18, 6),

    # Row 7: 8 nodes
    "VIE_party_discipline": (6, 7),
    "VIE_peoples_oversight": (8, 7),
    "VIE_digital_anticorruption": (10, 7),
    "VIE_resolution_congress_14": (12, 7),
    "VIE_e_government": (14, 7),
    "VIE_resolution_57_68": (16, 7),
    "VIE_higher_education_law": (18, 7),
    "VIE_disaster_law_2013": (20, 7),

    # Row 8: 7 nodes
    "VIE_cadre_accountability": (4, 8),
    "VIE_asset_recovery": (6, 8),
    "VIE_concentration_of_power": (10, 8),
    "VIE_institutional_opening": (14, 8),
    "VIE_institutional_bottlenecks": (16, 8),
    "VIE_education_law_2019": (18, 8),
    "VIE_civil_defense_law_2023": (20, 8),

    # Row 9: 2 nodes
    "VIE_clean_cadres": (6, 9),
    "VIE_era_of_rising": (12, 9),

    # Row 10: 1 node (Base apex)
    "VIE_party_centennial_2030": (12, 10),
}

print(f"Total mapped: {len(layout)} / {len(pol_fids)}")
missing = set(pol_fids) - set(layout.keys())
print(f"Missing: {missing}")

# Verification:
# 1. Duplicates
coords = defaultdict(list)
for fid, (x, y) in layout.items():
    coords[(x, y)].append(fid)

dups = {k: v for k, v in coords.items() if len(v) > 1}
print(f"Duplicates: {len(dups)}")
for k, v in dups.items():
    print(f"  Collision at {k}: {v}")

# 2. Min gaps < 2
by_y = defaultdict(list)
for fid, (x, y) in layout.items():
    by_y[y].append((x, fid))

bad_gaps = []
for y, items in sorted(by_y.items()):
    items.sort()
    for i in range(len(items) - 1):
        x1, f1 = items[i]
        x2, f2 = items[i+1]
        if x2 - x1 < 2:
            bad_gaps.append((y, f1, x1, f2, x2, x2 - x1))
print(f"Gaps < 2: {len(bad_gaps)}")

# 3. Upward arrows
upward = []
long_jumps = []
for fid, (cx, cy) in layout.items():
    for p in focuses[fid]["prereqs"]:
        if p in layout:
            px, py = layout[p]
            if cy <= py:
                upward.append((p, fid, py, cy, cy - py))
            dx = abs(cx - px)
            if dx > 6:
                long_jumps.append((p, fid, dx))

print(f"Upward arrows (dy <= 0): {len(upward)}")
for u in upward:
    print(f"  Upward: {u[0]} (y={u[2]}) -> {u[1]} (y={u[3]}), dy={u[4]}")

print(f"Long jumps (dx > 6): {len(long_jumps)}")
for j in long_jumps:
    print(f"  Long jump dx={j[2]}: {j[0]} -> {j[1]}")
