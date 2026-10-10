# -*- coding: utf-8 -*-
"""
Prototype layout simulation matching User Image 2
"""

# Let's define the 40 nodes with their tentative absolute coords (x, y)
# and parent anchors according to Image 2

NODES = [
    # Y = 2: NĂNG LỰC 1
    {"id": "VIE_nav_n00_maritime_strategy_21st", "x": 210, "y": 2, "rel": "VIE_modernize_vpa", "dx": 8, "dy": 1},

    # Y = 3: NĂNG LỰC 2
    {"id": "VIE_nav_t01_organization_reform", "x": 205, "y": 3, "rel": "VIE_nav_n00_maritime_strategy_21st", "dx": -5, "dy": 1},
    {"id": "VIE_nav_i01_shipbuilding_industry", "x": 217, "y": 3, "rel": "VIE_nav_n00_maritime_strategy_21st", "dx": 7, "dy": 1},

    # Y = 4: NĂNG LỰC 3
    {"id": "VIE_nav_s01_maritime_surveillance", "x": 201, "y": 4, "rel": "VIE_nav_t01_organization_reform", "dx": -4, "dy": 1},
    {"id": "VIE_nav_t02_officer_sailor_quality", "x": 205, "y": 4, "rel": "VIE_nav_t01_organization_reform", "dx": 0, "dy": 1},
    {"id": "VIE_nav_t03_regional_commands", "x": 208, "y": 4, "rel": "VIE_nav_t01_organization_reform", "dx": 3, "dy": 1},
    {"id": "VIE_nav_l01_naval_bases", "x": 212, "y": 4, "rel": "VIE_nav_t01_organization_reform", "dx": 7, "dy": 1},
    {"id": "VIE_nav_i02_technology_transfer_molniya", "x": 215, "y": 4, "rel": "VIE_nav_i01_shipbuilding_industry", "dx": -2, "dy": 1},
    {"id": "VIE_nav_i03_ship_systems_integration", "x": 219, "y": 4, "rel": "VIE_nav_i01_shipbuilding_industry", "dx": 2, "dy": 1},

    # Y = 5: NĂNG LỰC 4
    {"id": "VIE_nav_s02_island_defense_forces", "x": 200, "y": 5, "rel": "VIE_nav_s01_maritime_surveillance", "dx": -1, "dy": 1},
    {"id": "VIE_nav_s03_subsurface_recon", "x": 202, "y": 5, "rel": "VIE_nav_s01_maritime_surveillance", "dx": 1, "dy": 1},
    {"id": "VIE_nav_w01_surface_combatants", "x": 204, "y": 5, "rel": "VIE_nav_t02_officer_sailor_quality", "dx": -1, "dy": 1},
    {"id": "VIE_nav_w04_kilo_submarine_force", "x": 206, "y": 5, "rel": "VIE_nav_t02_officer_sailor_quality", "dx": 1, "dy": 1},
    {"id": "VIE_nav_t04_joint_command_system", "x": 208, "y": 5, "rel": "VIE_nav_t03_regional_commands", "dx": 0, "dy": 1},
    {"id": "VIE_nav_l02_overhaul_maintenance", "x": 211, "y": 5, "rel": "VIE_nav_l01_naval_bases", "dx": -1, "dy": 1},
    {"id": "VIE_nav_l03_island_logistics", "x": 213, "y": 5, "rel": "VIE_nav_l01_naval_bases", "dx": 1, "dy": 1},
    {"id": "VIE_nav_i04_domestic_corvette_class", "x": 217, "y": 5, "rel": "VIE_nav_i02_technology_transfer_molniya", "dx": 2, "dy": 1},

    # Y = 6: NĂNG LỰC 5
    {"id": "VIE_nav_s04_joint_island_defense", "x": 201, "y": 6, "rel": "VIE_nav_s02_island_defense_forces", "dx": 1, "dy": 1},
    {"id": "VIE_nav_w02_missile_boats", "x": 204, "y": 6, "rel": "VIE_nav_w01_surface_combatants", "dx": 0, "dy": 1},
    {"id": "VIE_nav_w03_multirole_frigates", "x": 206, "y": 6, "rel": "VIE_nav_w01_surface_combatants", "dx": 2, "dy": 1},
    {"id": "VIE_nav_l04_support_rescue_vessels", "x": 212, "y": 6, "rel": "VIE_nav_l02_overhaul_maintenance", "dx": 1, "dy": 1},

    # Y = 7: NĂNG LỰC 6
    {"id": "VIE_nav_s05_unified_maritime_picture", "x": 201, "y": 7, "rel": "VIE_nav_s04_joint_island_defense", "dx": 0, "dy": 1},
    {"id": "VIE_nav_w05_asw_fleet_defense", "x": 206, "y": 7, "rel": "VIE_nav_w03_multirole_frigates", "dx": 0, "dy": 1},
    {"id": "VIE_nav_l05_sustained_operations", "x": 212, "y": 7, "rel": "VIE_nav_l04_support_rescue_vessels", "dx": 0, "dy": 1},

    # Y = 8: HỌC THUYẾT 1
    {"id": "VIE_nav_p01_integrated_defense_choice", "x": 203, "y": 8, "rel": "VIE_nav_s05_unified_maritime_picture", "dx": 2, "dy": 1},
    {"id": "VIE_nav_h01_fleet_development_priority", "x": 210, "y": 8, "rel": "VIE_nav_l05_sustained_operations", "dx": -2, "dy": 1},

    # Y = 9: HỌC THUYẾT 2
    {"id": "VIE_nav_p02_coastal_island_network", "x": 201, "y": 9, "rel": "VIE_nav_p01_integrated_defense_choice", "dx": -2, "dy": 1},
    {"id": "VIE_nav_p03_island_territory_defense", "x": 205, "y": 9, "rel": "VIE_nav_p01_integrated_defense_choice", "dx": 2, "dy": 1},
    {"id": "VIE_nav_h02_multirole_task_groups", "x": 210, "y": 9, "rel": "VIE_nav_h01_fleet_development_priority", "dx": 0, "dy": 1},

    # Y = 10: HỌC THUYẾT 3
    {"id": "VIE_nav_p04_layered_defense", "x": 201, "y": 10, "rel": "VIE_nav_p02_coastal_island_network", "dx": 0, "dy": 1},
    {"id": "VIE_nav_g01_greenwater_navy", "x": 208, "y": 10, "rel": "VIE_nav_h02_multirole_task_groups", "dx": -2, "dy": 1},
    {"id": "VIE_nav_b01_bluewater_navy", "x": 213, "y": 10, "rel": "VIE_nav_h02_multirole_task_groups", "dx": 3, "dy": 1},

    # Y = 11: HỌC THUYẾT 4
    {"id": "VIE_nav_p05_joint_coastal_defense", "x": 203, "y": 11, "rel": "VIE_nav_p04_layered_defense", "dx": 2, "dy": 1},
    {"id": "VIE_nav_g02_advanced_frigates_asw", "x": 208, "y": 11, "rel": "VIE_nav_g01_greenwater_navy", "dx": 0, "dy": 1},
    {"id": "VIE_nav_b02_extended_deployment_fleet", "x": 213, "y": 11, "rel": "VIE_nav_b01_bluewater_navy", "dx": 0, "dy": 1},

    # Y = 12: HỌC THUYẾT 5 (CAPSTONES)
    {"id": "VIE_nav_p06_active_coastal_defense_capstone", "x": 203, "y": 12, "rel": "VIE_nav_p05_joint_coastal_defense", "dx": 0, "dy": 1},
    {"id": "VIE_nav_g03_self_reliant_greenwater_capstone", "x": 208, "y": 12, "rel": "VIE_nav_g02_advanced_frigates_asw", "dx": 0, "dy": 1},
    {"id": "VIE_nav_b03_sustained_bluewater_capstone", "x": 213, "y": 12, "rel": "VIE_nav_b02_extended_deployment_fleet", "dx": 0, "dy": 1},

    # Y = 13: HỘI TỤ 1
    {"id": "VIE_nav_f01_tactical_doctrine_alignment", "x": 208, "y": 13, "rel": "VIE_nav_g03_self_reliant_greenwater_capstone", "dx": 0, "dy": 1},

    # Y = 14: HỘI TỤ 2 (CAPSTONE TỐI THƯỢNG)
    {"id": "VIE_nav_f02_regular_modern_navy", "x": 208, "y": 14, "rel": "VIE_nav_f01_tactical_doctrine_alignment", "dx": 0, "dy": 1},
]

# Verify no duplicate coordinates
coords = {}
for n in NODES:
    pt = (n["x"], n["y"])
    if pt in coords:
        print(f"DUPLICATE COORDINATE: {pt} -> {coords[pt]} and {n['id']}")
    coords[pt] = n["id"]

print(f"Total nodes: {len(NODES)}, Unique coordinates: {len(coords)}")

# Check per layer
import collections
layers = collections.defaultdict(list)
for n in NODES:
    layers[n["y"]].append(n)

for y in sorted(layers.keys()):
    row = sorted(layers[y], key=lambda item: item["x"])
    xs = [item["x"] for item in row]
    # Check minimum gap between adjacent nodes in same row
    gaps = [xs[i+1] - xs[i] for i in range(len(xs)-1)]
    min_gap = min(gaps) if gaps else "N/A"
    names = [item["id"].replace("VIE_nav_", "") for item in row]
    print(f"Y={y:2d} ({len(row)} nodes): X range [{min(xs)}..{max(xs)}], min_gap={min_gap} -> {list(zip(xs, names))}")
