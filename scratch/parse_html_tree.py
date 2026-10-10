import json

HTML_DATA = [
    {"id": "N00", "title": "Hải quân Việt Nam trong thế kỷ XXI", "req": [], "lines": [], "extra": [], "group": "root", "cost": 6, "x": 1450, "y": 185, "row": 0},
    {"id": "T01", "title": "Đánh giá và kiện toàn tổ chức Hải quân", "req": ["N00"], "lines": ["N00"], "extra": [], "group": "reform", "cost": 7, "x": 960, "y": 361, "row": 1},
    {"id": "I01", "title": "Công nghiệp tàu quân sự", "req": ["N00"], "lines": ["N00"], "extra": [], "group": "industry", "cost": 7, "x": 1940, "y": 361, "row": 1},
    {"id": "S01", "title": "Cảnh giới vùng biển", "req": ["T01"], "lines": ["T01"], "extra": [], "group": "watch", "cost": 7, "x": 345, "y": 537, "row": 2},
    {"id": "T02", "title": "Nâng cao chất lượng sĩ quan và thủy thủ", "req": ["T01"], "lines": ["T01"], "extra": [], "group": "reform", "cost": 6, "x": 730, "y": 537, "row": 2},
    {"id": "T03", "title": "Kiện toàn các vùng Hải quân", "req": ["T01"], "lines": ["T01"], "extra": [], "group": "reform", "cost": 6, "x": 1100, "y": 537, "row": 2},
    {"id": "L01", "title": "Hiện đại hóa căn cứ Hải quân", "req": ["T01"], "lines": ["T01"], "extra": [], "group": "support", "cost": 7, "x": 1470, "y": 537, "row": 2},
    {"id": "I02", "title": "Tiếp nhận công nghệ đóng tàu", "req": ["I01"], "lines": ["I01"], "extra": [], "group": "industry", "cost": 6, "x": 1840, "y": 537, "row": 2},
    {"id": "I03", "title": "Thiết kế và tích hợp hạm tàu", "req": ["I01"], "lines": ["I01"], "extra": [], "group": "industry", "cost": 6, "x": 2220, "y": 537, "row": 2},
    {"id": "S02", "title": "Củng cố lực lượng bảo vệ đảo", "req": ["S01"], "lines": ["S01"], "extra": [], "group": "watch", "cost": 6, "x": 205, "y": 713, "row": 3},
    {"id": "S03", "title": "Trinh sát biển và dưới mặt nước", "req": ["S01"], "lines": ["S01"], "extra": [], "group": "watch", "cost": 6, "x": 520, "y": 713, "row": 3},
    {"id": "W01", "title": "Hiện đại hóa lực lượng mặt nước", "req": ["T02"], "lines": ["T02"], "extra": [], "group": "fleet", "cost": 7, "x": 835, "y": 713, "row": 3},
    {"id": "W04", "title": "Lực lượng tàu ngầm diesel–điện", "req": ["T02"], "lines": ["T02"], "extra": [], "group": "fleet", "cost": 6, "x": 1150, "y": 713, "row": 3},
    {"id": "T04", "title": "Chỉ huy hiệp đồng Hải quân", "req": ["T02", "T03"], "lines": ["T03"], "extra": ["T02"], "group": "reform", "cost": 6, "x": 1465, "y": 713, "row": 3},
    {"id": "L02", "title": "Bảo dưỡng và đại tu hạm tàu", "req": ["L01"], "lines": ["L01"], "extra": [], "group": "support", "cost": 6, "x": 1780, "y": 713, "row": 3},
    {"id": "L03", "title": "Hậu cần biển đảo", "req": ["L01"], "lines": ["L01"], "extra": [], "group": "support", "cost": 6, "x": 2095, "y": 713, "row": 3},
    {"id": "I04", "title": "Tàu hộ vệ đóng mới trong nước", "req": ["I02", "I03"], "lines": ["I02", "I03"], "extra": [], "group": "industry", "cost": 10, "x": 2410, "y": 713, "row": 3},
    {"id": "S04", "title": "Hiệp đồng bảo vệ biển đảo", "req": ["S02", "S03"], "lines": ["S03"], "extra": ["S02"], "group": "watch", "cost": 6, "x": 525, "y": 889, "row": 4},
    {"id": "W02", "title": "Lực lượng tàu tên lửa cơ động", "req": ["W01"], "lines": ["W01"], "extra": [], "group": "fleet", "cost": 6, "x": 850, "y": 889, "row": 4},
    {"id": "W03", "title": "Tàu hộ vệ đa nhiệm", "req": ["W01"], "lines": ["W01"], "extra": [], "group": "fleet", "cost": 6, "x": 1180, "y": 889, "row": 4},
    {"id": "L04", "title": "Tàu hỗ trợ và cứu hộ", "req": ["L02", "L03"], "lines": ["L02", "L03"], "extra": [], "group": "support", "cost": 6, "x": 1925, "y": 889, "row": 4},
    {"id": "S05", "title": "Bức tranh tình hình biển thống nhất", "req": ["S04"], "lines": ["S04"], "extra": [], "group": "watch", "cost": 10, "x": 525, "y": 1065, "row": 5},
    {"id": "W05", "title": "Chống ngầm và tự vệ hạm đội", "req": ["W03", "S03"], "lines": ["W03"], "extra": ["S03"], "group": "fleet", "cost": 6, "x": 1180, "y": 1065, "row": 5},
    {"id": "L05", "title": "Duy trì hoạt động dài ngày", "req": ["L04"], "lines": ["L04"], "extra": [], "group": "support", "cost": 10, "x": 1925, "y": 1065, "row": 5},
    {"id": "P01", "title": "Chiến lược phòng thủ biển tích hợp", "req": ["T04", "W01"], "lines": ["T04"], "extra": ["W01"], "group": "defense", "cost": 8, "x": 865, "y": 1241, "row": 6},
    {"id": "H01", "title": "Phát triển hạm đội hiện đại", "req": ["T04", "W01"], "lines": ["T04"], "extra": ["W01"], "group": "program", "cost": 8, "x": 1650, "y": 1241, "row": 6},
    {"id": "P02", "title": "Mạng lưới phòng thủ bờ – đảo", "req": ["P01", "S02"], "lines": ["P01"], "extra": ["S02"], "group": "defense", "cost": 6, "x": 640, "y": 1417, "row": 7},
    {"id": "P03", "title": "Bảo vệ địa bàn biển đảo", "req": ["P01", "L03"], "lines": ["P01"], "extra": ["L03"], "group": "defense", "cost": 6, "x": 965, "y": 1417, "row": 7},
    {"id": "H02", "title": "Biên đội tàu tác chiến đa nhiệm", "req": ["H01", "W03", "L02"], "lines": ["H01"], "extra": ["W03", "L02"], "group": "program", "cost": 6, "x": 1650, "y": 1417, "row": 7},
    {"id": "P04", "title": "Phòng thủ biển nhiều lớp", "req": ["P02"], "lines": ["P02"], "extra": [], "group": "defense", "cost": 6, "x": 640, "y": 1593, "row": 8},
    {"id": "G01", "title": "Green-water Navy hiện đại", "req": ["H02"], "lines": ["H02"], "extra": [], "group": "green", "cost": 8, "x": 1480, "y": 1593, "row": 8},
    {"id": "B01", "title": "Chương trình Blue-water Navy", "req": ["H02", "L05"], "lines": ["H02"], "extra": ["L05"], "group": "blue", "cost": 8, "x": 1930, "y": 1593, "row": 8},
    {"id": "P05", "title": "Hiệp đồng phòng thủ biển", "req": ["P03", "P04"], "lines": ["P04"], "extra": ["P03"], "group": "defense", "cost": 6, "x": 865, "y": 1769, "row": 9},
    {"id": "G02", "title": "Tàu hộ vệ và chống ngầm", "req": ["G01", "W05"], "lines": ["G01"], "extra": ["W05"], "group": "green", "cost": 6, "x": 1480, "y": 1769, "row": 9},
    {"id": "B02", "title": "Biên đội triển khai dài ngày", "req": ["B01", "S04"], "lines": ["B01"], "extra": ["S04"], "group": "blue", "cost": 10, "x": 1930, "y": 1769, "row": 9},
    {"id": "P06", "title": "Phòng thủ biển chủ động", "req": ["P05"], "lines": ["P05"], "extra": [], "group": "defense", "cost": 10, "x": 865, "y": 1945, "row": 10},
    {"id": "G03", "title": "Hạm đội biển gần đa nhiệm", "req": ["G02", "L03"], "lines": ["G02"], "extra": ["L03"], "group": "green", "cost": 10, "x": 1480, "y": 1945, "row": 10},
    {"id": "B03", "title": "Hải quân biển xa bền vững", "req": ["B02"], "lines": ["B02"], "extra": [], "group": "blue", "cost": 10, "x": 1930, "y": 1945, "row": 10},
    {"id": "F01", "title": "Hoàn thiện học thuyết Hải quân", "req": ["P06|G03|B03"], "lines": ["P06|G03|B03"], "extra": [], "group": "finish", "cost": 10, "x": 1460, "y": 2121, "row": 11},
    {"id": "F02", "title": "Hải quân Việt Nam chính quy, hiện đại", "req": ["F01", "S05", "L05"], "lines": ["F01"], "extra": ["S05", "L05"], "group": "finish", "cost": 10, "x": 1460, "y": 2297, "row": 12}
]

print("=== PHÂN TÍCH TỌA ĐỘ VÀ ĐƯỜNG NỐI TỪ FILE HTML ===")
print(f"Tổng số node: {len(HTML_DATA)}")

# Mapping id -> full ID
id_to_full = {
    "N00": "VIE_nav_n00_maritime_strategy_21st",
    "T01": "VIE_nav_t01_organization_reform",
    "I01": "VIE_nav_i01_shipbuilding_industry",
    "S01": "VIE_nav_s01_maritime_surveillance",
    "T02": "VIE_nav_t02_officer_sailor_quality",
    "T03": "VIE_nav_t03_regional_commands",
    "L01": "VIE_nav_l01_naval_bases",
    "I02": "VIE_nav_i02_technology_transfer_molniya",
    "I03": "VIE_nav_i03_ship_systems_integration",
    "S02": "VIE_nav_s02_island_defense_forces",
    "S03": "VIE_nav_s03_subsurface_recon",
    "W01": "VIE_nav_w01_surface_combatants",
    "W04": "VIE_nav_w04_kilo_submarine_force",
    "T04": "VIE_nav_t04_joint_command_system",
    "L02": "VIE_nav_l02_overhaul_maintenance",
    "L03": "VIE_nav_l03_island_logistics",
    "I04": "VIE_nav_i04_domestic_corvette_class",
    "S04": "VIE_nav_s04_joint_island_defense",
    "W02": "VIE_nav_w02_missile_boats",
    "W03": "VIE_nav_w03_multirole_frigates",
    "L04": "VIE_nav_l04_support_rescue_vessels",
    "S05": "VIE_nav_s05_unified_maritime_picture",
    "W05": "VIE_nav_w05_asw_fleet_defense",
    "L05": "VIE_nav_l05_sustained_operations",
    "P01": "VIE_nav_p01_integrated_defense_choice",
    "H01": "VIE_nav_h01_fleet_development_priority",
    "P02": "VIE_nav_p02_coastal_island_network",
    "P03": "VIE_nav_p03_island_territory_defense",
    "H02": "VIE_nav_h02_multirole_task_groups",
    "P04": "VIE_nav_p04_layered_defense",
    "G01": "VIE_nav_g01_greenwater_navy",
    "B01": "VIE_nav_b01_bluewater_navy",
    "P05": "VIE_nav_p05_joint_coastal_defense",
    "G02": "VIE_nav_g02_advanced_frigates_asw",
    "B02": "VIE_nav_b02_extended_deployment_fleet",
    "P06": "VIE_nav_p06_active_coastal_defense_capstone",
    "G03": "VIE_nav_g03_self_reliant_greenwater_capstone",
    "B03": "VIE_nav_b03_sustained_bluewater_capstone",
    "F01": "VIE_nav_f01_tactical_doctrine_alignment",
    "F02": "VIE_nav_f02_regular_modern_navy"
}

# Group by row
by_row = {}
for item in HTML_DATA:
    by_row.setdefault(item['row'], []).append(item)

for r in sorted(by_row.keys()):
    nodes = by_row[r]
    print(f"\n--- HÀNG (ROW) {r} (y = {nodes[0]['y']}) ---")
    for n in nodes:
        print(f"  {n['id']}: x_pixel={n['x']}, lines={n['lines']}, req={n['req']}, extra={n['extra']}")
