# -*- coding: utf-8 -*-
"""
test_v34_coords.py
Kiểm tra toán học tọa độ tuyệt đối, anchor dependency, gaps, duplicates cho 40 focus V34.
"""

focus_defs = [
    # LAYER 1 (Y=2): ROOT N00
    {"id": "VIE_nav_n00_maritime_strategy_21st", "rel": "VIE_modernize_vpa", "dx": 10, "dy": 1, "target_abs": (212, 2)},

    # LAYER 2 (Y=3): CHÂN KIỀNG T01 & I01
    {"id": "VIE_nav_t01_organization_reform", "rel": "VIE_nav_n00_maritime_strategy_21st", "dx": -5, "dy": 1, "target_abs": (207, 3)},
    {"id": "VIE_nav_i01_shipbuilding_industry", "rel": "VIE_nav_n00_maritime_strategy_21st", "dx": 5, "dy": 1, "target_abs": (217, 3)},

    # LAYER 3 (Y=4): 4 NHÁNH T02, T03, I02, I03
    {"id": "VIE_nav_t02_officer_sailor_quality", "rel": "VIE_nav_t01_organization_reform", "dx": -2, "dy": 1, "target_abs": (205, 4)},
    {"id": "VIE_nav_t03_regional_commands", "rel": "VIE_nav_t01_organization_reform", "dx": 2, "dy": 1, "target_abs": (209, 4)},
    {"id": "VIE_nav_i02_technology_transfer_molniya", "rel": "VIE_nav_i01_shipbuilding_industry", "dx": -2, "dy": 1, "target_abs": (215, 4)},
    {"id": "VIE_nav_i03_ship_systems_integration", "rel": "VIE_nav_i01_shipbuilding_industry", "dx": 2, "dy": 1, "target_abs": (219, 4)},

    # LAYER 4 (Y=5): HỘI TỤ ĐỆM & TRANG BỊ
    {"id": "VIE_nav_w01_surface_combatants", "rel": "VIE_nav_t02_officer_sailor_quality", "dx": 0, "dy": 1, "target_abs": (205, 5)},
    {"id": "VIE_nav_w04_kilo_submarine_force", "rel": "VIE_nav_t02_officer_sailor_quality", "dx": 2, "dy": 1, "target_abs": (207, 5)},
    {"id": "VIE_nav_t04_joint_command_system", "rel": "VIE_nav_t03_regional_commands", "dx": 0, "dy": 1, "target_abs": (209, 5)},
    {"id": "VIE_nav_i04_domestic_corvette_class", "rel": "VIE_nav_i02_technology_transfer_molniya", "dx": 0, "dy": 1, "target_abs": (215, 5)},
    {"id": "VIE_nav_s01_maritime_surveillance", "rel": "VIE_nav_t01_organization_reform", "dx": 10, "dy": 2, "target_abs": (217, 5)},
    {"id": "VIE_nav_l01_naval_bases", "rel": "VIE_nav_t01_organization_reform", "dx": 12, "dy": 2, "target_abs": (219, 5)},

    # LAYER 5 (Y=6): BỤNG CÁNH BUỒM (8 NÚT XÒE RỘNG NHẤT)
    {"id": "VIE_nav_w02_missile_boats", "rel": "VIE_nav_w01_surface_combatants", "dx": 0, "dy": 1, "target_abs": (205, 6)},
    {"id": "VIE_nav_w03_multirole_frigates", "rel": "VIE_nav_w01_surface_combatants", "dx": 2, "dy": 1, "target_abs": (207, 6)},
    {"id": "VIE_nav_s03_subsurface_recon", "rel": "VIE_nav_s01_maritime_surveillance", "dx": -8, "dy": 1, "target_abs": (209, 6)},
    {"id": "VIE_nav_s02_island_defense_forces", "rel": "VIE_nav_s01_maritime_surveillance", "dx": -6, "dy": 1, "target_abs": (211, 6)},
    {"id": "VIE_nav_l02_overhaul_maintenance", "rel": "VIE_nav_l01_naval_bases", "dx": -6, "dy": 1, "target_abs": (213, 6)},
    {"id": "VIE_nav_l03_island_logistics", "rel": "VIE_nav_l01_naval_bases", "dx": -4, "dy": 1, "target_abs": (215, 6)},
    {"id": "VIE_nav_h01_fleet_development_priority", "rel": "VIE_nav_t04_joint_command_system", "dx": 8, "dy": 1, "target_abs": (217, 6)},
    {"id": "VIE_nav_p01_integrated_defense_choice", "rel": "VIE_nav_t04_joint_command_system", "dx": 10, "dy": 1, "target_abs": (219, 6)},

    # LAYER 6 (Y=7): THU HẸP & ĐAN XEN VŨ KHÍ
    {"id": "VIE_nav_w05_asw_fleet_defense", "rel": "VIE_nav_w03_multirole_frigates", "dx": -2, "dy": 1, "target_abs": (205, 7)},
    {"id": "VIE_nav_s04_joint_island_defense", "rel": "VIE_nav_s02_island_defense_forces", "dx": -4, "dy": 1, "target_abs": (207, 7)},
    {"id": "VIE_nav_l04_support_rescue_vessels", "rel": "VIE_nav_l02_overhaul_maintenance", "dx": -4, "dy": 1, "target_abs": (209, 7)},
    {"id": "VIE_nav_p02_coastal_island_network", "rel": "VIE_nav_p01_integrated_defense_choice", "dx": -6, "dy": 1, "target_abs": (213, 7)},
    {"id": "VIE_nav_p03_island_territory_defense", "rel": "VIE_nav_p01_integrated_defense_choice", "dx": -4, "dy": 1, "target_abs": (215, 7)},
    {"id": "VIE_nav_h02_multirole_task_groups", "rel": "VIE_nav_h01_fleet_development_priority", "dx": 0, "dy": 1, "target_abs": (217, 7)},

    # LAYER 7 (Y=8): THU HẸP TIỀN ĐỀ HỌC THUYẾT
    {"id": "VIE_nav_s05_unified_maritime_picture", "rel": "VIE_nav_s04_joint_island_defense", "dx": 0, "dy": 1, "target_abs": (207, 8)},
    {"id": "VIE_nav_l05_sustained_operations", "rel": "VIE_nav_l04_support_rescue_vessels", "dx": 0, "dy": 1, "target_abs": (209, 8)},
    {"id": "VIE_nav_p04_layered_defense", "rel": "VIE_nav_p02_coastal_island_network", "dx": 0, "dy": 1, "target_abs": (213, 8)},
    {"id": "VIE_nav_g01_greenwater_navy", "rel": "VIE_nav_h02_multirole_task_groups", "dx": -2, "dy": 1, "target_abs": (215, 8)},
    {"id": "VIE_nav_b01_bluewater_navy", "rel": "VIE_nav_h02_multirole_task_groups", "dx": 0, "dy": 1, "target_abs": (217, 8)},

    # LAYER 8 (Y=9): HỌC THUYẾT CHUYÊN SÂU
    {"id": "VIE_nav_p05_joint_coastal_defense", "rel": "VIE_nav_p04_layered_defense", "dx": -2, "dy": 1, "target_abs": (211, 9)},
    {"id": "VIE_nav_g02_advanced_frigates_asw", "rel": "VIE_nav_g01_greenwater_navy", "dx": -2, "dy": 1, "target_abs": (213, 9)},
    {"id": "VIE_nav_b02_extended_deployment_fleet", "rel": "VIE_nav_b01_bluewater_navy", "dx": -2, "dy": 1, "target_abs": (215, 9)},

    # LAYER 9 (Y=10): ĐỈNH CAO HỌC THUYẾT
    {"id": "VIE_nav_p06_active_coastal_defense_capstone", "rel": "VIE_nav_p05_joint_coastal_defense", "dx": 0, "dy": 1, "target_abs": (211, 10)},
    {"id": "VIE_nav_g03_self_reliant_greenwater_capstone", "rel": "VIE_nav_g02_advanced_frigates_asw", "dx": 0, "dy": 1, "target_abs": (213, 10)},
    {"id": "VIE_nav_b03_sustained_bluewater_capstone", "rel": "VIE_nav_b02_extended_deployment_fleet", "dx": 0, "dy": 1, "target_abs": (215, 10)},

    # LAYER 10 (Y=11): HỘI TỤ HỌC THUYẾT
    {"id": "VIE_nav_f01_tactical_doctrine_alignment", "rel": "VIE_nav_p06_active_coastal_defense_capstone", "dx": 1, "dy": 1, "target_abs": (212, 11)},

    # LAYER 11 (Y=12): CAPSTONE TỐI THƯỢNG CHÍNH QUY HIỆN ĐẠI
    {"id": "VIE_nav_f02_regular_modern_navy", "rel": "VIE_nav_f01_tactical_doctrine_alignment", "dx": 0, "dy": 1, "target_abs": (212, 12)},
]

anchors = {'VIE_modernize_vpa': (202, 1)}

abs_coords = {}
errors = []

for i, f in enumerate(focus_defs):
    rel = f['rel']
    if rel not in anchors:
        errors.append(f"Focus {f['id']} references unknown or forward anchor {rel}")
        continue
    rx, ry = anchors[rel]
    ax = rx + f['dx']
    ay = ry + f['dy']
    if (ax, ay) != f['target_abs']:
        errors.append(f"Focus {f['id']} computed abs ({ax}, {ay}) != target {f['target_abs']}")
    abs_coords[f['id']] = (ax, ay)
    anchors[f['id']] = (ax, ay)

print(f"Total focus tested: {len(focus_defs)}")
if errors:
    print(f"Found {len(errors)} errors:")
    for e in errors:
        print("  -", e)
else:
    print("ALL 40 FOCUS OFFSETS & ABSOLUTE COORDINATES MATCH 100% PERFECTLY!")

# Check duplicates and gaps
by_y = {}
for fid, (ax, ay) in abs_coords.items():
    by_y.setdefault(ay, []).append((ax, fid))

print("\n--- LAYER BREAKDOWN ---")
for y in sorted(by_y.keys()):
    row = sorted(by_y[y])
    xs = [r[0] for r in row]
    print(f"Layer Y={y:2d} ({len(row)} nodes): X range [{min(xs)} .. {max(xs)}] -> {xs}")
    for i in range(len(xs) - 1):
        if xs[i+1] - xs[i] < 2:
            print(f"  WARNING: Gap < 2 between X={xs[i]} ({row[i][1]}) and X={xs[i+1]} ({row[i+1][1]})")

# Duplicates check
seen = {}
for fid, (ax, ay) in abs_coords.items():
    if (ax, ay) in seen:
        print(f"DUPLICATE at ({ax}, {ay}): {seen[(ax, ay)]} and {fid}")
    seen[(ax, ay)] = fid

print("Coordinate verification complete!")
