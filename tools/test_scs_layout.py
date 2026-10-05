import sys, os
sys.path.insert(0, os.path.abspath("."))
import re
import tools.analyze_scs as asc

# Proposed layout mapping for South China Sea & Law of the Sea (24 focuses)
# Root: VIE_law_of_the_sea at (76, 12), neo VIE_doi_moi_continues (80, 0): dx = -4, dy = 12

scs_layout = {
    # ROOT (y = 12)
    "VIE_law_of_the_sea": {
        "rel": "VIE_doi_moi_continues", "dx": -4, "dy": 12, # abs (76, 12)
        "prereqs": [], "avail": []
    },

    # =========================================================
    # TRUC 1: DAU TRANH PHAP LY & CHU QUYEN (7 focus)
    # Zone: x = 66 .. 72
    # =========================================================
    # y = 13
    "VIE_legal_warfare": {
        "rel": "VIE_law_of_the_sea", "dx": -10, "dy": 1, # abs (66, 13)
        "prereqs": ["VIE_law_of_the_sea"], "avail": []
    },
    "VIE_assert_maritime_rights": {
        "rel": "VIE_law_of_the_sea", "dx": -6, "dy": 1, # abs (70, 13)
        "prereqs": ["VIE_law_of_the_sea"], "avail": []
    },
    # y = 14
    "VIE_limited_war_doctrine": {
        "rel": "VIE_assert_maritime_rights", "dx": -2, "dy": 1, # abs (68, 14)
        "prereqs": ["VIE_assert_maritime_rights"], "avail": ["VIE_legal_warfare"]
    },
    "VIE_paracel_ultimatum": {
        "rel": "VIE_assert_maritime_rights", "dx": 0, "dy": 1, # abs (70, 14)
        "prereqs": ["VIE_assert_maritime_rights"], "avail": []
    },
    # y = 15
    "VIE_retake_north_spratlys": {
        "rel": "VIE_paracel_ultimatum", "dx": 0, "dy": 1, # abs (70, 15)
        "prereqs": ["VIE_paracel_ultimatum"], "avail": []
    },
    # y = 16
    "VIE_retake_east_spratlys": {
        "rel": "VIE_retake_north_spratlys", "dx": -2, "dy": 1, # abs (68, 16)
        "prereqs": ["VIE_retake_north_spratlys"], "avail": []
    },
    "VIE_retake_south_spratlys": {
        "rel": "VIE_retake_north_spratlys", "dx": 2, "dy": 1, # abs (72, 16)
        "prereqs": ["VIE_retake_north_spratlys"], "avail": []
    },

    # =========================================================
    # TRUC 2: THUC THI PHAP LUAT & HIEN DIEN BIEN (5 focus)
    # Zone: x = 74 .. 78
    # =========================================================
    # y = 13
    "VIE_fisheries_surveillance": {
        "rel": "VIE_law_of_the_sea", "dx": -2, "dy": 1, # abs (74, 13)
        "prereqs": ["VIE_law_of_the_sea"], "avail": []
    },
    "VIE_maritime_militia": {
        "rel": "VIE_law_of_the_sea", "dx": 2, "dy": 1, # abs (78, 13)
        "prereqs": ["VIE_law_of_the_sea"], "avail": []
    },
    # y = 14
    "VIE_coast_guard_law": {
        "rel": "VIE_fisheries_surveillance", "dx": 0, "dy": 1, # abs (74, 14)
        "prereqs": ["VIE_fisheries_surveillance"], "avail": []
    },
    "VIE_spratly_fortification": {
        "rel": "VIE_maritime_militia", "dx": 0, "dy": 1, # abs (78, 14)
        "prereqs": ["VIE_maritime_militia"], "avail": []
    },
    # y = 15
    "VIE_dk1_platforms": {
        "rel": "VIE_spratly_fortification", "dx": -2, "dy": 1, # abs (76, 15)
        "prereqs": ["VIE_spratly_fortification"], "avail": ["VIE_coast_guard_law"]
    },

    # =========================================================
    # TRUC 3: QUOC PHONG TOAN DAN & BON KHONG (7 focus)
    # Zone: x = 80 .. 84
    # =========================================================
    # y = 13
    "VIE_peoples_defence": {
        "rel": "VIE_law_of_the_sea", "dx": 6, "dy": 1, # abs (82, 13)
        "prereqs": ["VIE_law_of_the_sea"], "avail": []
    },
    # y = 14
    "VIE_provincial_defence_zones": {
        "rel": "VIE_peoples_defence", "dx": -2, "dy": 1, # abs (80, 14)
        "prereqs": ["VIE_peoples_defence"], "avail": []
    },
    "VIE_force_47": {
        "rel": "VIE_peoples_defence", "dx": 0, "dy": 1, # abs (82, 14)
        "prereqs": ["VIE_peoples_defence"], "avail": []
    },
    "VIE_un_peacekeeping": {
        "rel": "VIE_peoples_defence", "dx": 2, "dy": 1, # abs (84, 14)
        "prereqs": ["VIE_peoples_defence"], "avail": []
    },
    # y = 15
    "VIE_militia_law": {
        "rel": "VIE_provincial_defence_zones", "dx": 0, "dy": 1, # abs (80, 15)
        "prereqs": ["VIE_provincial_defence_zones"], "avail": []
    },
    "VIE_cyber_command": {
        "rel": "VIE_force_47", "dx": 0, "dy": 1, # abs (82, 15)
        "prereqs": ["VIE_force_47"], "avail": []
    },
    "VIE_four_nos_doctrine": {
        "rel": "VIE_un_peacekeeping", "dx": 0, "dy": 1, # abs (84, 15)
        "prereqs": ["VIE_un_peacekeeping"], "avail": []
    },

    # =========================================================
    # TRUC 4: HOP TAC AN NINH BIEN & CAM RANH (4 focus)
    # Zone: x = 86 .. 88
    # =========================================================
    # y = 13
    "VIE_scs_maritime_cooperation": {
        "rel": "VIE_law_of_the_sea", "dx": 10, "dy": 1, # abs (86, 13)
        "prereqs": ["VIE_law_of_the_sea"], "avail": []
    },
    # y = 14
    "VIE_scs_multilateral_exercise": {
        "rel": "VIE_scs_maritime_cooperation", "dx": 0, "dy": 1, # abs (86, 14)
        "prereqs": ["VIE_scs_maritime_cooperation"], "avail": []
    },
    "VIE_scs_cam_ranh_port": {
        "rel": "VIE_scs_maritime_cooperation", "dx": 2, "dy": 1, # abs (88, 14)
        "prereqs": ["VIE_scs_maritime_cooperation"], "avail": []
    },
    # y = 15
    "VIE_scs_joint_training": {
        "rel": "VIE_scs_multilateral_exercise", "dx": 0, "dy": 1, # abs (86, 15)
        "prereqs": ["VIE_scs_multilateral_exercise"], "avail": ["VIE_scs_cam_ranh_port"]
    }
}

print(f"Total mapped SCS focuses: {len(scs_layout)} (expected 24)")
missing = [fid for fid in asc.subtree if fid not in scs_layout]
print(f"Missing from layout: {missing}")

# Calculate absolute coordinates
abs_coords = {}
def get_abs_pos(fid, visited=None):
    if visited is None:
        visited = set()
    if fid in visited:
        return (0, 0)
    visited.add(fid)
    entry = scs_layout[fid]
    parent = entry["rel"]
    if parent == "VIE_doi_moi_continues":
        return (80 + entry["dx"], 0 + entry["dy"])
    px, py = get_abs_pos(parent, visited)
    return (px + entry["dx"], py + entry["dy"])

for fid in scs_layout:
    abs_coords[fid] = get_abs_pos(fid)

# Check collisions within SCS
coord_map = {}
collisions = []
for fid, (ax, ay) in abs_coords.items():
    if (ax, ay) in coord_map:
        collisions.append((fid, coord_map[(ax, ay)], (ax, ay)))
    else:
        coord_map[(ax, ay)] = fid

print(f"Collisions within SCS: {len(collisions)}")
for c in collisions:
    print("  Collision:", c)

# Check collisions with external focuses in the mod
ext_collisions = []
for fid, (ax, ay) in abs_coords.items():
    for ext_fid, ext_f in asc.focuses.items():
        if ext_fid not in scs_layout:
            if (ext_f['abs_x'], ext_f['abs_y']) == (ax, ay):
                ext_collisions.append((fid, ext_fid, (ax, ay)))

print(f"Collisions with external focuses: {len(ext_collisions)}")
for c in ext_collisions:
    print("  Collision:", c)

# Check gap violations
rows = {}
for fid, (ax, ay) in abs_coords.items():
    rows.setdefault(ay, []).append((ax, fid))

gap_violations = []
for y in sorted(rows.keys()):
    items = sorted(rows[y], key=lambda x: x[0])
    row_str = ", ".join([f"{fid}(x={ax})" for ax, fid in items])
    print(f"Row y={y:2} ({len(items):2} focuses): {row_str}")
    for k in range(len(items) - 1):
        dx = items[k+1][0] - items[k][0]
        if dx < 2:
            gap_violations.append((items[k][1], items[k+1][1], y, dx))

print(f"Gap violations (dx < 2): {len(gap_violations)}")
for g in gap_violations:
    print("  Gap violation:", g)

# Check prerequisite y_child > y_parent
prereq_violations = []
for fid, entry in scs_layout.items():
    ax, ay = abs_coords[fid]
    for p in entry["prereqs"]:
        if p in abs_coords:
            p_ax, p_ay = abs_coords[p]
            if ay <= p_ay:
                prereq_violations.append((fid, p, ay, p_ay))

print(f"Prerequisite y_child <= y_parent violations: {len(prereq_violations)}")
for pv in prereq_violations:
    print("  Prereq violation:", pv)
