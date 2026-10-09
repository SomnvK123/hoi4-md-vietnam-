# -*- coding: utf-8 -*-
"""
Apply naval tree specification exactly matching HTML design (Hải quân Việt Nam V34 - Cánh Buồm)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

# The 40 focuses with exact HTML lines, extra, cost and coordinates
HTML_SPEC = [
    # ROW 0 (Y=2): N00
    {
        "id": "VIE_nav_n00_maritime_strategy_21st",
        "name": "Chiến lược Biển Việt Nam thế kỷ XXI",
        "desc": "Xác lập định hướng phát triển sức mạnh biển toàn diện, bảo vệ vững chắc chủ quyền biển đảo, thềm lục địa và các lợi ích kinh tế biển của Tổ quốc trong kỷ nguyên mới.",
        "icon": "GFX_focus_VIE_naval_defence_2030",
        "cost": 7,
        "x": 8, "y": 1, "rel": "VIE_modernize_vpa",
        "lines": ["VIE_modernize_vpa"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_MILITARY_LAWS"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_command_power = 25",
            "add_political_power = 40",
            "set_country_flag = VIE_maritime_strategy_21st_active"
        ]
    },
    # ROW 1 (Y=3): T01, I01
    {
        "id": "VIE_nav_t01_organization_reform",
        "name": "Đánh giá và kiện toàn tổ chức Hải quân",
        "desc": "Rà soát toàn diện cơ cấu lực lượng, tình trạng vũ khí kỹ thuật và hoàn thiện mô hình tổ chức chỉ huy, tạo tiền đề nâng cao chất lượng huấn luyện và sẵn sàng chiến đấu.",
        "icon": "GFX_focus_VIE_nf_command_reform_1",
        "cost": 7,
        "x": -5, "y": 1, "rel": "VIE_nav_n00_maritime_strategy_21st",
        "lines": ["VIE_nav_n00_maritime_strategy_21st"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "add_command_power = 15",
            "VIE_nav_upgrade_org = yes"
        ]
    },
    {
        "id": "VIE_nav_i01_shipbuilding_industry",
        "name": "Củng cố nền công nghiệp đóng tàu quân sự",
        "desc": "Đầu tư nâng cấp năng lực các nhà máy đóng tàu quân đội như Ba Son, Sông Thu, Hồng Hà; làm chủ công nghệ đóng mới tàu tuần tra và sửa chữa lớn khí tài hải quân.",
        "icon": "GFX_focus_VIE_ba_son_shipyards",
        "cost": 7,
        "x": 7, "y": 1, "rel": "VIE_nav_n00_maritime_strategy_21st",
        "lines": ["VIE_nav_n00_maritime_strategy_21st"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "VIE_nav_upgrade_industry = yes",
            "VIE_ind_prepaid_dockyard = yes",
            "add_tech_bonus = { name = VIE_i01_naval_tech bonus = 0.50 uses = 1 category = CAT_naval }"
        ]
    },
    # ROW 2 (Y=4): S01, T02, T03, L01, I02, I03
    {
        "id": "VIE_nav_s01_maritime_surveillance",
        "name": "Mở rộng khả năng cảnh giới vùng biển",
        "desc": "Tăng cường năng lực nhận thức tình huống biển (MDA) thông qua phối hợp dữ liệu vệ tinh, mạng lưới trạm radar bờ biển và hoạt động tuần tra thường trực.",
        "icon": "GFX_focus_VIE_scs_joint_surveillance",
        "cost": 7,
        "x": -4, "y": 1, "rel": "VIE_nav_t01_organization_reform",
        "lines": ["VIE_nav_t01_organization_reform"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "VIE_nav_upgrade_mda = yes"
        ]
    },
    {
        "id": "VIE_nav_t02_officer_sailor_quality",
        "name": "Nâng cao chất lượng sĩ quan và thủy thủ",
        "desc": "Hiện đại hóa Học viện Hải quân, chuẩn hóa chương trình đào tạo theo tiêu chuẩn quốc tế và tăng cường thời lượng thực hành huấn luyện dài ngày trên biển.",
        "icon": "GFX_focus_VIE_nf_command_reform_2",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_t01_organization_reform",
        "lines": ["VIE_nav_t01_organization_reform"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "VIE_nav_upgrade_org = yes"
        ]
    },
    {
        "id": "VIE_nav_t03_regional_commands",
        "name": "Kiện toàn các Vùng Hải quân",
        "desc": "Tổ chức lại Sở chỉ huy 5 Vùng Hải quân (Vùng 1 đến Vùng 5), phân định rõ địa bàn trách nhiệm tác chiến và nâng cao năng lực phản ứng nhanh trước mọi tình huống.",
        "icon": "GFX_focus_VIE_nf_command_reform_3",
        "cost": 6,
        "x": 3, "y": 1, "rel": "VIE_nav_t01_organization_reform",
        "lines": ["VIE_nav_t01_organization_reform"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "add_command_power = 20",
            "VIE_nav_upgrade_org = yes"
        ]
    },
    {
        "id": "VIE_nav_l01_naval_bases",
        "name": "Hiện đại hóa căn cứ Hải quân",
        "desc": "Nâng cấp cơ sở hạ tầng các quân cảng Cam Ranh, Đà Nẵng, Hải Phòng, Phú Quốc; trang bị cầu cảng hiện đại, trạm nạp nhiên liệu và cơ sở kỹ thuật bảo đảm cho hạm đội.",
        "icon": "GFX_focus_VIE_scs_cam_ranh_port",
        "cost": 7,
        "x": 7, "y": 1, "rel": "VIE_nav_t01_organization_reform",
        "lines": ["VIE_nav_t01_organization_reform"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_upgrade_logistics = yes",
            "519 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } }",
            "522 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } }"
        ]
    },
    {
        "id": "VIE_nav_i02_technology_transfer_molniya",
        "name": "Tiếp nhận công nghệ đóng tàu chiến đấu hiện đại",
        "desc": "Thực hiện thành công chương trình chuyển giao công nghệ đóng tàu tên lửa tấn công nhanh Molniya Project 1241.8 trong nước, tạo bước đột phá về năng lực công nghệ đóng tàu quân sự.",
        "icon": "GFX_focus_VIE_nf_first_force",
        "cost": 6,
        "x": -2, "y": 1, "rel": "VIE_nav_i01_shipbuilding_industry",
        "lines": ["VIE_nav_i01_shipbuilding_industry"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "VIE_nav_upgrade_industry = yes",
            "add_tech_bonus = { name = VIE_i02_corvette_tech bonus = 0.50 uses = 1 category = CAT_surface_ships }"
        ]
    },
    {
        "id": "VIE_nav_i03_ship_systems_integration",
        "name": "Làm chủ thiết kế và tích hợp hệ thống hạm tàu",
        "desc": "Từng bước tự chủ trong việc thiết kế kết cấu thân vỏ, tích hợp hệ thống chỉ huy chiến đấu CMS, radar dẫn bắn và cảm biến quang điện tử trên các lớp tàu mặt nước.",
        "icon": "GFX_focus_VIE_naval_systems_integration",
        "cost": 6,
        "x": 2, "y": 1, "rel": "VIE_nav_i01_shipbuilding_industry",
        "lines": ["VIE_nav_i01_shipbuilding_industry"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "VIE_nav_upgrade_industry = yes",
            "add_tech_bonus = { name = VIE_i03_naval_electronics bonus = 0.50 uses = 1 category = CAT_naval }"
        ]
    },
    # ROW 3 (Y=5): S02, S03, W01, W04, T04, L02, L03, I04
    {
        "id": "VIE_nav_s02_island_defense_forces",
        "name": "Củng cố lực lượng bảo vệ đảo",
        "desc": "Tăng cường năng lực tác chiến phòng thủ đảo cho Lữ đoàn 146 và các đơn vị Trường Sa; củng cố công sự, trận địa pháo và các trạm quan sát cảnh giới kiên cố.",
        "icon": "GFX_focus_VIE_scs_spratly_fortification",
        "cost": 6,
        "x": -1, "y": 1, "rel": "VIE_nav_s01_maritime_surveillance",
        "lines": ["VIE_nav_s01_maritime_surveillance"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "801 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }",
            "set_country_flag = VIE_nav_s02_bastion_unlocked"
        ]
    },
    {
        "id": "VIE_nav_s03_subsurface_recon",
        "name": "Hiện đại hóa trinh sát biển và dưới mặt nước",
        "desc": "Trang bị hệ thống định vị thủy âm sonar cố định và cơ động, nâng cao năng lực trinh sát phát hiện tàu ngầm đối phương và bảo vệ an toàn các luồng hàng hải trọng yếu.",
        "icon": "GFX_focus_VIE_nf_denial_command",
        "cost": 6,
        "x": 1, "y": 1, "rel": "VIE_nav_s01_maritime_surveillance",
        "lines": ["VIE_nav_s01_maritime_surveillance"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "801 = { add_building_construction = { type = radar_station level = 1 instant_build = yes } }",
            "VIE_nav_upgrade_mda = yes"
        ]
    },
    {
        "id": "VIE_nav_w01_surface_combatants",
        "name": "Hiện đại hóa lực lượng tàu mặt nước",
        "desc": "Tập trung hiện đại hóa hạm đội tàu chiến đấu mặt nước cơ động cao, nâng cấp vũ khí hỏa lực tên lửa chống hạm Uran-E và hệ thống phòng không tầm gần.",
        "icon": "GFX_focus_VIE_nf_light_combatants",
        "cost": 7,
        "x": -1, "y": 1, "rel": "VIE_nav_t02_officer_sailor_quality",
        "lines": ["VIE_nav_t02_officer_sailor_quality"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_tech_bonus = { name = VIE_w01_surface_tech bonus = 0.50 uses = 1 category = CAT_surface_ships }"
        ]
    },
    {
        "id": "VIE_nav_w04_kilo_submarine_force",
        "name": "Xây dựng lực lượng tàu ngầm diesel-điện",
        "desc": "Tiếp nhận và đưa vào vận hành hiệu quả 6 tàu ngầm Kilo Project 636.1 Varshavyanka thuộc Lữ đoàn 189, tạo nên quả đấm thép răn đe dưới lòng biển sâu.",
        "icon": "GFX_focus_VIE_kilo_submarines",
        "cost": 6,
        "x": 1, "y": 1, "rel": "VIE_nav_t02_officer_sailor_quality",
        "lines": ["VIE_nav_t02_officer_sailor_quality"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "add_tech_bonus = { name = VIE_w04_sub_tech bonus = 0.50 uses = 1 category = CAT_submarines }",
            "set_country_flag = VIE_nav_w04_kilo_unlocked"
        ]
    },
    {
        "id": "VIE_nav_t04_joint_command_system",
        "name": "Hoàn thiện hệ thống chỉ huy hiệp đồng Hải quân",
        "desc": "Xây dựng Trung tâm Sở chỉ huy tác chiến Hải quân hiện đại, ứng dụng công nghệ thông tin C4ISR để chỉ huy thông suốt các lực lượng tàu mặt nước, tàu ngầm và không quân hải quân.",
        "icon": "GFX_focus_VIE_nf_c4isr_command",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_t03_regional_commands",
        "lines": ["VIE_nav_t03_regional_commands"],
        "extra": ["VIE_nav_t02_officer_sailor_quality"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_command_power = 25",
            "VIE_nav_upgrade_org = yes"
        ]
    },
    {
        "id": "VIE_nav_l02_overhaul_maintenance",
        "name": "Nâng cao năng lực bảo dưỡng và đại tu hạm tàu",
        "desc": "Đầu tư các ụ nổi hiện đại và trạm sửa chữa kỹ thuật đồng bộ tại các nhà máy X51, X52, bảo đảm khả năng tự chủ bảo dưỡng cấp đốc và đại tu vũ khí trên tàu.",
        "icon": "GFX_focus_VIE_nf_fleet_repair",
        "cost": 6,
        "x": -1, "y": 1, "rel": "VIE_nav_l01_naval_bases",
        "lines": ["VIE_nav_l01_naval_bases"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "VIE_nav_upgrade_logistics = yes"
        ]
    },
    {
        "id": "VIE_nav_l03_island_logistics",
        "name": "Bảo đảm hậu cần cho các tiền đồn biển đảo",
        "desc": "Xây dựng hệ thống âu tàu, trạm cung ứng hậu cần - kỹ thuật tại đảo Song Tử Tây, Trường Sa Lớn và nhà giàn DK1, bảo đảm chỗ dựa vững chắc cho bộ đội và ngư dân bám biển.",
        "icon": "GFX_focus_VIE_scs_island_airstrip",
        "cost": 6,
        "x": 1, "y": 1, "rel": "VIE_nav_l01_naval_bases",
        "lines": ["VIE_nav_l01_naval_bases"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "VIE_nav_upgrade_logistics = yes",
            "518 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } }"
        ]
    },
    {
        "id": "VIE_nav_i04_domestic_corvette_class",
        "name": "Phát triển tàu hộ vệ đóng mới trong nước",
        "desc": "Nâng cấp cơ sở đóng tàu quân sự, tiến tới thiết kế và đóng mới các lớp tàu tuần tra xa bờ và tàu hộ vệ tên lửa tàng hình thế hệ mới mang thương hiệu Việt Nam.",
        "icon": "GFX_focus_VIE_nf_stealth_corvette",
        "cost": 10,
        "x": 2, "y": 1, "rel": "VIE_nav_i02_technology_transfer_molniya",
        "lines": ["VIE_nav_i02_technology_transfer_molniya", "VIE_nav_i03_ship_systems_integration"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "VIE_nav_upgrade_industry = yes",
            "add_tech_bonus = { name = VIE_i04_domestic_tech bonus = 0.75 uses = 1 category = CAT_surface_ships }",
            "set_country_flag = VIE_nav_i04_song_thu_unlocked"
        ]
    },
    # ROW 4 (Y=6): S04, W02, W03, L04
    {
        "id": "VIE_nav_s04_joint_island_defense",
        "name": "Hiệp đồng bảo vệ vùng biển đảo",
        "desc": "Tổ chức luyện tập cơ chế phối hợp tác chiến giữa Hải quân, Cảnh sát biển, Bộ đội Biên phòng và lực lượng dân quân tự vệ biển bảo vệ vững chắc các vùng biển được phân công.",
        "icon": "GFX_focus_VIE_scs_maritime_militia",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_s03_subsurface_recon",
        "lines": ["VIE_nav_s03_subsurface_recon"],
        "extra": ["VIE_nav_s02_island_defense_forces"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "VIE_nav_upgrade_mda = yes"
        ]
    },
    {
        "id": "VIE_nav_w02_missile_boats",
        "name": "Phát triển lực lượng tàu tên lửa cơ động",
        "desc": "Tổ chức khai thác, làm chủ hạm đội tàu tên lửa cao tốc Molniya và BPS-500, phát huy tối đa chiến thuật luồn sâu đánh bất ngờ với hỏa lực tập trung.",
        "icon": "GFX_focus_VIE_nf_missile_boats",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_w01_surface_combatants",
        "lines": ["VIE_nav_w01_surface_combatants"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_tech_bonus = { name = VIE_w02_fast_attack bonus = 0.50 uses = 1 category = CAT_light_combatants }",
            "set_country_flag = VIE_nav_w02_molniya_unlocked"
        ]
    },
    {
        "id": "VIE_nav_w03_multirole_frigates",
        "name": "Phát triển lực lượng tàu hộ vệ đa nhiệm",
        "desc": "Khai thác làm chủ lực lượng khinh hạm Gepard 3.9 (Project 11661E), trang bị hỏa lực chống hạm, phòng không Palma và trực thăng săn ngầm Ka-28, đóng vai trò nòng cốt hạm đội.",
        "icon": "GFX_focus_VIE_nf_regional_frigates",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_w04_kilo_submarine_force",
        "lines": ["VIE_nav_w01_surface_combatants"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_tech_bonus = { name = VIE_w03_frigate bonus = 0.50 uses = 1 category = CAT_destroyers }",
            "set_country_flag = VIE_nav_w03_gepard_unlocked"
        ]
    },
    {
        "id": "VIE_nav_l04_support_rescue_vessels",
        "name": "Phát triển lực lượng tàu hỗ trợ và cứu hộ",
        "desc": "Biên chế tàu cứu nạn tàu ngầm đa năng Yết Kiêu 927 và các tàu vận tải tiếp tế thế hệ mới, bảo đảm an toàn tuyệt đối cho hoạt động tác chiến của hạm đội.",
        "icon": "GFX_focus_VIE_nf_replenishment",
        "cost": 6,
        "x": 1, "y": 1, "rel": "VIE_nav_l02_overhaul_maintenance",
        "lines": ["VIE_nav_l02_overhaul_maintenance", "VIE_nav_l03_island_logistics"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "VIE_nav_upgrade_logistics = yes"
        ]
    },
    # ROW 5 (Y=7): S05, W05, L05
    {
        "id": "VIE_nav_s05_unified_maritime_picture",
        "name": "Hình thành hệ thống nhận thức tình hình biển thống nhất",
        "desc": "Hợp nhất toàn bộ dữ liệu cảnh giới từ radar bờ, tàu ngầm, máy bay tuần thám và các trạm quan sát đảo thành một bức tranh nhận thức tình hình biển (MDA) thời gian thực.",
        "icon": "GFX_focus_VIE_nf_operating_range",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_s04_joint_island_defense",
        "lines": ["VIE_nav_s04_joint_island_defense"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_25 = yes",
            "VIE_nav_upgrade_mda = yes"
        ]
    },
    {
        "id": "VIE_nav_w05_asw_fleet_defense",
        "name": "Nâng cao năng lực chống ngầm và tự vệ hạm đội",
        "desc": "Trang bị ngư lôi săn ngầm hiện đại, nâng cao năng lực phối hợp giữa trực thăng săn ngầm hải quân Ka-28 và hệ thống hỏa lực phòng vệ trên tàu chiến.",
        "icon": "GFX_focus_VIE_nf_naval_aviation",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_w03_multirole_frigates",
        "lines": ["VIE_nav_w03_multirole_frigates"],
        "extra": ["VIE_nav_s03_subsurface_recon"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_ideas = VIE_nav_asw_mastery",
            "add_tech_bonus = { name = VIE_w05_asw_tech bonus = 0.50 uses = 1 category = CAT_destroyers }"
        ]
    },
    {
        "id": "VIE_nav_l05_sustained_operations",
        "name": "Nâng cao khả năng duy trì hoạt động dài ngày",
        "desc": "Hoàn thiện quy trình luân phiên lực lượng, tiếp tế cơ động trên biển (RAS) và bảo dưỡng ngoài khơi, giúp tàu chiến có thể bám biển hoạt động liên tục nhiều tháng.",
        "icon": "GFX_focus_VIE_nf_ocean_escort",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_l04_support_rescue_vessels",
        "lines": ["VIE_nav_l04_support_rescue_vessels"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "VIE_nav_upgrade_logistics = yes"
        ]
    },
    # ROW 6 (Y=8): P01, H01
    {
        "id": "VIE_nav_p01_integrated_defense_choice",
        "name": "Lựa chọn chiến lược phòng thủ biển tích hợp",
        "desc": "Tập trung xây dựng thế trận chống tiếp cận/chống thâm nhập khu vực (A2/AD) nhiều tầng, kết hợp hỏa lực tên lửa bờ biển, tàu ngầm Kilo và hệ thống công sự đảo.",
        "icon": "GFX_focus_VIE_nf_denial",
        "cost": 8,
        "x": -5, "y": 3, "rel": "VIE_nav_t04_joint_command_system",
        "lines": ["VIE_nav_t04_joint_command_system"],
        "extra": ["VIE_nav_w01_surface_combatants"],
        "mutually_exclusive": ["VIE_nav_h01_fleet_development_priority"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_ideas = VPA_Integrated_Defense_Doctrine_1"
        ]
    },
    {
        "id": "VIE_nav_h01_fleet_development_priority",
        "name": "Ưu tiên xây dựng hạm đội tác chiến hiện đại",
        "desc": "Chuyển hướng chiến lược tập trung nguồn lực phát triển các biên đội tàu chiến đấu mặt nước đa năng, sẵn sàng vươn khơi làm chủ các vùng biển khu vực.",
        "icon": "GFX_focus_VIE_nf_greenwater",
        "cost": 8,
        "x": 2, "y": 3, "rel": "VIE_nav_t04_joint_command_system",
        "lines": ["VIE_nav_t04_joint_command_system"],
        "extra": ["VIE_nav_w01_surface_combatants"],
        "mutually_exclusive": ["VIE_nav_p01_integrated_defense_choice"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_ideas = VPA_Fleet_Development_Priority"
        ]
    },
    # ROW 7 (Y=9): P02, P03, H02
    {
        "id": "VIE_nav_p02_coastal_island_network",
        "name": "Xây dựng mạng lưới phòng thủ bờ – đảo",
        "desc": "Liên kết chặt chẽ các trận địa tên lửa phòng thủ bờ biển Bastion-P, Redut-M với các cụm đảo tiền tiêu, hình thành lá chắn hỏa lực bảo vệ vững chắc lãnh hải.",
        "icon": "GFX_focus_VIE_nf_denial_defence",
        "cost": 6,
        "x": -2, "y": 1, "rel": "VIE_nav_p01_integrated_defense_choice",
        "lines": ["VIE_nav_p01_integrated_defense_choice"],
        "extra": ["VIE_nav_s02_island_defense_forces"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "521 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }",
            "519 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }"
        ]
    },
    {
        "id": "VIE_nav_p03_island_territory_defense",
        "name": "Củng cố lực lượng bảo vệ các địa bàn biển đảo",
        "desc": "Tăng cường năng lực cơ động tác chiến và hỏa lực cho Lữ đoàn Hải quân đánh bộ 101 và 147, sẵn sàng đổ bộ tái chiếm và bảo vệ các đảo trọng yếu.",
        "icon": "GFX_focus_VIE_sf_marine",
        "cost": 6,
        "x": 2, "y": 1, "rel": "VIE_nav_p01_integrated_defense_choice",
        "lines": ["VIE_nav_p01_integrated_defense_choice"],
        "extra": ["VIE_nav_l03_island_logistics"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_ideas = VIE_nav_marine_brigades"
        ]
    },
    {
        "id": "VIE_nav_h02_multirole_task_groups",
        "name": "Hình thành các biên đội tàu tác chiến đa nhiệm",
        "desc": "Tổ chức các biên đội tác chiến kết hợp khinh hạm hộ vệ, tàu pháo tên lửa cao tốc và tàu bảo đảm hậu cần, có năng lực tuần tra tác chiến độc lập tầm trung.",
        "icon": "GFX_focus_VIE_nf_medium_force",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_h01_fleet_development_priority",
        "lines": ["VIE_nav_h01_fleet_development_priority"],
        "extra": ["VIE_nav_w03_multirole_frigates", "VIE_nav_l02_overhaul_maintenance"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "add_ideas = VPA_Multirole_Task_Groups"
        ]
    },
    # ROW 8 (Y=10): P04, G01, B01
    {
        "id": "VIE_nav_p04_layered_defense",
        "name": "Hiện đại hóa năng lực phòng thủ biển nhiều lớp",
        "desc": "Tích hợp tên lửa hành trình chống hạm tầm siêu âm, bãi thủy lôi thông minh và các bệ phóng ngụy trang cơ động, tạo nên thế trận phòng thủ hiểm hóc không thể xuyên phá.",
        "icon": "GFX_focus_VIE_nf_denial_subs",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_p02_coastal_island_network",
        "lines": ["VIE_nav_p02_coastal_island_network"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_command_power = 20",
            "set_country_flag = VIE_nav_p04_layered_active"
        ]
    },
    {
        "id": "VIE_nav_g01_greenwater_navy",
        "name": "Định hướng xây dựng Hải quân biển gần hiện đại",
        "desc": "Xác lập học thuyết Hải quân biển gần (Green-water), tập trung xây dựng hạm đội mặt nước cơ động và lực lượng săn ngầm làm chủ hoàn toàn vùng đặc quyền kinh tế (EEZ).",
        "icon": "GFX_focus_VIE_nf_greenwater",
        "cost": 8,
        "x": -2, "y": 1, "rel": "VIE_nav_h02_multirole_task_groups",
        "lines": ["VIE_nav_h02_multirole_task_groups"],
        "extra": [],
        "mutually_exclusive": ["VIE_nav_b01_bluewater_navy"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "add_ideas = VPA_Greenwater_Doctrine_1"
        ]
    },
    {
        "id": "VIE_nav_b01_bluewater_navy",
        "name": "Khởi động chương trình Hải quân biển xa",
        "desc": "Mở rộng tầm nhìn hướng ra đại dương (Blue-water), đặt mục tiêu xây dựng các cụm tàu chiến đấu có khả năng bảo vệ tuyến hàng hải huyết mạch và hiện diện tại các vùng biển xa.",
        "icon": "GFX_focus_VIE_nf_bluewater",
        "cost": 8,
        "x": 3, "y": 1, "rel": "VIE_nav_h02_multirole_task_groups",
        "lines": ["VIE_nav_h02_multirole_task_groups"],
        "extra": ["VIE_nav_l05_sustained_operations"],
        "mutually_exclusive": ["VIE_nav_g01_greenwater_navy"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_25 = yes",
            "add_ideas = VPA_Bluewater_Doctrine_1"
        ]
    },
    # ROW 9 (Y=11): P05, G02, B02
    {
        "id": "VIE_nav_p05_joint_coastal_defense",
        "name": "Hiệp đồng tác chiến phòng thủ biển",
        "desc": "Kết hợp nhịp nhàng các đòn phục kích của tàu ngầm Kilo với hỏa lực bờ biển và lực lượng không quân tiêm kích bom Su-30MK2, giáng đòn tiêu diệt các hạm đội tàu đối phương.",
        "icon": "GFX_focus_VIE_nf_denial_command",
        "cost": 6,
        "x": 2, "y": 1, "rel": "VIE_nav_p04_layered_defense",
        "lines": ["VIE_nav_p04_layered_defense"],
        "extra": ["VIE_nav_p03_island_territory_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "add_command_power = 25",
            "set_country_flag = VIE_nav_p05_joint_active"
        ]
    },
    {
        "id": "VIE_nav_g02_advanced_frigates_asw",
        "name": "Hiện đại hóa lực lượng tàu hộ vệ và chống ngầm",
        "desc": "Trang bị các tàu hộ vệ cỡ lớn có khả năng tàng hình, hệ thống phóng thẳng đứng VLS hiện đại và sonar thủy âm kéo theo tiên tiến, nâng cao vượt bậc năng lực săn ngầm.",
        "icon": "GFX_focus_VIE_nf_regional_frigates",
        "cost": 6,
        "x": 0, "y": 1, "rel": "VIE_nav_g01_greenwater_navy",
        "lines": ["VIE_nav_g01_greenwater_navy"],
        "extra": ["VIE_nav_w05_asw_fleet_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "add_tech_bonus = { name = VIE_g02_frigate_tech bonus = 0.50 uses = 1 category = CAT_destroyers }"
        ]
    },
    {
        "id": "VIE_nav_b02_extended_deployment_fleet",
        "name": "Xây dựng hạm đội có khả năng triển khai dài ngày",
        "desc": "Đầu tư tàu hậu cần viễn dương cỡ lớn, hoàn thiện kỹ năng tiếp vận trên biển và khả năng phối hợp tác chiến liên tục nhiều tháng ở vùng biển quốc tế.",
        "icon": "GFX_focus_VIE_nf_carrier_group",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_b01_bluewater_navy",
        "lines": ["VIE_nav_b01_bluewater_navy"],
        "extra": ["VIE_nav_s04_joint_island_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_25 = yes",
            "add_tech_bonus = { name = VIE_b02_ocean_tech bonus = 0.50 uses = 1 category = CAT_naval }"
        ]
    },
    # ROW 10 (Y=12): P06, G03, B03
    {
        "id": "VIE_nav_p06_active_coastal_defense_capstone",
        "name": "Hoàn thiện thế trận phòng thủ biển chủ động",
        "desc": "Đỉnh cao của học thuyết Phòng thủ tích hợp: xác lập thế trận phòng ngự chủ động kiên cường, biến từng mét biển, từng hòn đảo thành pháo đài thép bất khả xâm phạm.",
        "icon": "GFX_focus_VIE_nf_denial_defence",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_p05_joint_coastal_defense",
        "lines": ["VIE_nav_p05_joint_coastal_defense"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_30 = yes",
            "swap_ideas = { remove_idea = VPA_Integrated_Defense_Doctrine_1 add_idea = VPA_Integrated_Defense_Doctrine_Capstone }",
            "set_country_flag = VIE_nav_p_doctrine_completed"
        ]
    },
    {
        "id": "VIE_nav_g03_self_reliant_greenwater_capstone",
        "name": "Xây dựng hạm đội biển gần có năng lực tự chủ tác chiến",
        "desc": "Đỉnh cao của học thuyết Green-water: Hạm đội tác chiến hiện đại có khả năng kiểm soát và bảo vệ toàn bộ vùng biển khu vực và quần đảo với độ tin cậy và tự chủ cao nhất.",
        "icon": "GFX_focus_VIE_nf_ocean_escort",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_g02_advanced_frigates_asw",
        "lines": ["VIE_nav_g02_advanced_frigates_asw"],
        "extra": ["VIE_nav_l03_island_logistics"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_30 = yes",
            "swap_ideas = { remove_idea = VPA_Greenwater_Doctrine_1 add_idea = VPA_Greenwater_Doctrine_Capstone }",
            "set_country_flag = VIE_nav_g_doctrine_completed"
        ]
    },
    {
        "id": "VIE_nav_b03_sustained_bluewater_capstone",
        "name": "Hình thành năng lực tác chiến Hải quân biển xa bền vững",
        "desc": "Đỉnh cao của học thuyết Blue-water: Hình thành các biên đội tàu chiến đấu tầm xa, có khả năng tham gia các chiến dịch quốc tế và bảo vệ lợi ích hàng hải trên các đại dương.",
        "icon": "GFX_focus_VIE_nf_bluewater",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_b02_extended_deployment_fleet",
        "lines": ["VIE_nav_b02_extended_deployment_fleet"],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_35 = yes",
            "swap_ideas = { remove_idea = VPA_Bluewater_Doctrine_1 add_idea = VPA_Bluewater_Doctrine_Capstone }",
            "set_country_flag = VIE_nav_b_doctrine_completed"
        ]
    },
    # ROW 11 (Y=13): F01
    {
        "id": "VIE_nav_f01_tactical_doctrine_alignment",
        "name": "Hoàn thiện học thuyết tác chiến Hải quân",
        "desc": "Đúc kết kinh nghiệm thực tiễn và tinh hoa các học thuyết tác chiến, hoàn thiện cơ chế chỉ huy tham mưu và nghệ thuật quân sự Hải quân nhân dân Việt Nam.",
        "icon": "GFX_focus_VIE_nf_command_reform_1",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_g03_self_reliant_greenwater_capstone",
        "lines_or": [
            "VIE_nav_p06_active_coastal_defense_capstone",
            "VIE_nav_g03_self_reliant_greenwater_capstone",
            "VIE_nav_b03_sustained_bluewater_capstone"
        ],
        "extra": [],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_30 = yes",
            "add_command_power = 35",
            "add_political_power = 50"
        ]
    },
    # ROW 12 (Y=14): F02
    {
        "id": "VIE_nav_f02_regular_modern_navy",
        "name": "Xây dựng Hải quân nhân dân Việt Nam chính quy, hiện đại",
        "desc": "Khẳng định tầm vóc mới của Hải quân nhân dân Việt Nam: Quân chủng cách mạng, chính quy, tinh nhuệ, hiện đại, làm nòng cốt quản lý và bảo vệ vững chắc chủ quyền biển đảo thiêng liêng của Tổ quốc.",
        "icon": "GFX_focus_VIE_naval_defence_law",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_f01_tactical_doctrine_alignment",
        "lines": ["VIE_nav_f01_tactical_doctrine_alignment"],
        "extra": ["VIE_nav_s05_unified_maritime_picture", "VIE_nav_l05_sustained_operations"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_50 = yes",
            "add_command_power = 50",
            "add_political_power = 100",
            "add_stability = 0.05",
            "VIE_nav_grant_capstone_f2 = yes",
            "set_country_flag = VIE_navy_modernized"
        ]
    }
]

def generate_focus_snippet():
    out = []
    out.append("\t######################################################################")
    out.append("\t## ĐỀ ÁN V34: NHÁNH HẢI QUÂN VIỆT NAM (LAYOUT CÁNH BUỒM BLUE CHART)")
    out.append("\t## 40 FOCUS CHUẨN XÁC 100% THEO FILE THIẾT KẾ HTML V34")
    out.append("\t## LINES -> PREREQUISITE (VẼ ĐƯỜNG NỐI TRỰC QUAN)")
    out.append("\t## EXTRA -> AVAILABLE HAS_COMPLETED_FOCUS (LIÊN KẾT CHÉO ẨN ĐƯỜNG DÀI)")
    out.append("\t######################################################################\n")

    for f in HTML_SPEC:
        out.append("\tfocus = {")
        out.append(f'\t\tid = {f["id"]}')
        out.append(f'\t\ticon = {f["icon"]}\n')

        # Coordinates
        out.append(f'\t\tx = {f["x"]}')
        out.append(f'\t\ty = {f["y"]}')
        if "rel" in f:
            out.append(f'\t\trelative_position_id = {f["rel"]}')
        out.append(f'\n\t\tcost = {f["cost"]}\n')

        # Mutually exclusive
        if "mutually_exclusive" in f:
            for m in f["mutually_exclusive"]:
                out.append(f"\t\tmutually_exclusive = {{ focus = {m} }}")
            out.append("")

        # Prerequisite (from lines / lines_or)
        if "lines_or" in f:
            out.append("\t\tprerequisite = {")
            for pr in f["lines_or"]:
                out.append(f"\t\t\tfocus = {pr}")
            out.append("\t\t}\n")
        elif "lines" in f:
            for pr in f["lines"]:
                out.append(f"\t\tprerequisite = {{ focus = {pr} }}")
            out.append("")

        # Available (extra requirements)
        if f.get("extra"):
            out.append("\t\tavailable = {")
            for ext in f["extra"]:
                out.append(f"\t\t\thas_completed_focus = {ext}")
            out.append("\t\t}\n")

        # Search filters
        filters = " ".join(f.get("search_filters", ["FOCUS_FILTER_NAVY"]))
        out.append(f"\t\tsearch_filters = {{ {filters} }}\n")

        # AI will do
        out.append("\t\tai_will_do = {")
        out.append("\t\t\tbase = 75")
        out.append("\t\t\tmodifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }")
        out.append("\t\t}\n")

        # Rewards
        out.append("\t\tcompletion_reward = {")
        out.append(f'\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus {f["id"]}"')
        for r in f["rewards"]:
            for line in r.splitlines():
                out.append(f"\t\t\t{line.strip()}")
        out.append("\t\t}")
        out.append("\t}\n")

    return "\n".join(out)

def main():
    print("Generating exact HTML specification focus tree snippet...")
    snippet = generate_focus_snippet()

    focus_file = "common/national_focus/VIE_md_focus.txt"
    with open(focus_file, "r", encoding="utf-8") as f:
        focus_text = f.read()

    start_marker = "## ĐỀ ÁN V34: NHÁNH HẢI QUÂN VIỆT NAM"
    end_marker = "focus = {\n\t\tid = VIE_force_47"

    start_idx = focus_text.find(start_marker)
    end_idx = focus_text.find(end_marker)

    if start_idx != -1 and end_idx != -1:
        line_start = focus_text.rfind("\t", 0, start_idx)
        if line_start == -1: line_start = start_idx
        new_focus_text = focus_text[:line_start] + snippet + "\n\n\t" + focus_text[end_idx:]
        with open(focus_file, "w", encoding="utf-8") as f:
            f.write(new_focus_text)
        print("Updated VIE_md_focus.txt with HTML specification successfully!")
    else:
        print(f"ERROR: Markers not found! start_idx={start_idx}, end_idx={end_idx}")

if __name__ == '__main__':
    main()
