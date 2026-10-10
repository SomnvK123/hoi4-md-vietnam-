# -*- coding: utf-8 -*-
"""
Generator script to build and verify V34 Vietnamese Naval Branch
40 Focuses · Organic Diamond Flow · 3 Strategic Doctrines (P/G/B)
"""

import os
import re

FOCUS_DATA = [
    # Y = 2
    {
        "id": "VIE_nav_n00_maritime_strategy_21st",
        "name": "Chiến lược Biển Việt Nam thế kỷ XXI",
        "desc": "Xác lập định hướng phát triển sức mạnh biển toàn diện, bảo vệ vững chắc chủ quyền biển đảo, thềm lục địa và các lợi ích kinh tế biển của Tổ quốc trong kỷ nguyên mới.",
        "icon": "GFX_focus_VIE_naval_defence_2030",
        "cost": 7,
        "x": 10, "y": 1, "rel": "VIE_modernize_vpa",
        "abs_x": 212, "abs_y": 2,
        "prereq": ["VIE_modernize_vpa"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_MILITARY_LAWS"],
        "rewards": [
            "navy_experience = 15",
            "add_command_power = 20",
            "add_political_power = 30",
        ]
    },
    # Y = 3
    {
        "id": "VIE_nav_t01_organization_reform",
        "name": "Đánh giá và kiện toàn tổ chức Hải quân",
        "desc": "Rà soát toàn diện cơ cấu lực lượng, tình trạng vũ khí kỹ thuật và hoàn thiện mô hình tổ chức chỉ huy, tạo tiền đề nâng cao chất lượng huấn luyện và sẵn sàng chiến đấu.",
        "icon": "GFX_focus_VIE_nf_command_reform_1",
        "cost": 5,
        "x": -5, "y": 1, "rel": "VIE_nav_n00_maritime_strategy_21st",
        "abs_x": 207, "abs_y": 3,
        "prereq": ["VIE_nav_n00_maritime_strategy_21st"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_command_power = 15",
            "add_ideas = VIE_nav_organization_reform_spirit"
        ]
    },
    {
        "id": "VIE_nav_i01_shipbuilding_industry",
        "name": "Củng cố nền công nghiệp đóng tàu quân sự",
        "desc": "Đầu tư nâng cấp năng lực các nhà máy đóng tàu quân đội như Ba Son, Sông Thu, Hồng Hà; làm chủ công nghệ đóng mới tàu tuần tra và sửa chữa lớn khí tài hải quân.",
        "icon": "GFX_focus_VIE_ba_son_shipyards",
        "cost": 5,
        "x": 5, "y": 1, "rel": "VIE_nav_n00_maritime_strategy_21st",
        "abs_x": 217, "abs_y": 3,
        "prereq": ["VIE_nav_n00_maritime_strategy_21st"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "add_tech_bonus = { name = VIE_i01_naval_tech bonus = 0.50 uses = 1 category = CAT_naval }",
            "add_ideas = VIE_nav_shipbuilding_industry_spirit"
        ]
    },
    # Y = 4
    {
        "id": "VIE_nav_t02_officer_sailor_quality",
        "name": "Nâng cao chất lượng sĩ quan và thủy thủ",
        "desc": "Chuẩn hóa chương trình đào tạo tại Học viện Hải quân, tăng cường giờ đi biển thực tế, nâng cao bản lĩnh chính trị và trình độ ngoại ngữ, kỹ thuật của cán bộ thủy thủ.",
        "icon": "GFX_focus_VIE_nf_training_standardization",
        "cost": 5,
        "x": -2, "y": 1, "rel": "VIE_nav_t01_organization_reform",
        "abs_x": 205, "abs_y": 4,
        "prereq": ["VIE_nav_t01_organization_reform"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_ideas = VIE_nav_officer_sailor_quality_spirit"
        ]
    },
    {
        "id": "VIE_nav_t03_regional_commands",
        "name": "Kiện toàn lực lượng các Vùng Hải quân",
        "desc": "Củng cố năng lực chỉ huy tác chiến, phân định rõ khu vực trách nhiệm chiến lược từ Vùng 1 đến Vùng 5, nâng cao khả năng phản ứng cơ động bảo vệ vùng biển chủ quyền.",
        "icon": "GFX_focus_VIE_nf_regional_command",
        "cost": 5,
        "x": 2, "y": 1, "rel": "VIE_nav_t01_organization_reform",
        "abs_x": 209, "abs_y": 4,
        "prereq": ["VIE_nav_t01_organization_reform"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_command_power = 20",
            "add_ideas = VIE_nav_regional_commands_spirit"
        ]
    },
    {
        "id": "VIE_nav_i02_technology_transfer_molniya",
        "name": "Tiếp nhận công nghệ đóng tàu chiến đấu hiện đại",
        "desc": "Thực hiện thành công chương trình chuyển giao công nghệ đóng tàu tên lửa tấn công nhanh Molniya Project 1241.8 trong nước, tạo bước đột phá về năng lực công nghệ đóng tàu quân sự.",
        "icon": "GFX_focus_VIE_nf_first_force",
        "cost": 5,
        "x": -2, "y": 1, "rel": "VIE_nav_i01_shipbuilding_industry",
        "abs_x": 215, "abs_y": 4,
        "prereq": ["VIE_nav_i01_shipbuilding_industry"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "add_tech_bonus = { name = VIE_i02_corvette_tech bonus = 0.50 uses = 1 category = CAT_surface_ships }",
            "add_ideas = VIE_nav_technology_transfer_spirit"
        ]
    },
    {
        "id": "VIE_nav_i03_ship_systems_integration",
        "name": "Làm chủ thiết kế và tích hợp hệ thống hạm tàu",
        "desc": "Từng bước tự chủ trong việc thiết kế kết cấu thân vỏ, tích hợp hệ thống chỉ huy chiến đấu CMS, radar dẫn bắn và cảm biến quang điện tử trên các lớp tàu mặt nước.",
        "icon": "GFX_focus_VIE_naval_systems_integration",
        "cost": 5,
        "x": 2, "y": 1, "rel": "VIE_nav_i01_shipbuilding_industry",
        "abs_x": 219, "abs_y": 4,
        "prereq": ["VIE_nav_i01_shipbuilding_industry"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "add_tech_bonus = { name = VIE_i03_naval_electronics bonus = 0.50 uses = 1 category = CAT_naval }",
            "add_ideas = VIE_nav_systems_integration_spirit"
        ]
    },
    # Y = 5
    {
        "id": "VIE_nav_w01_surface_combatants",
        "name": "Hiện đại hóa lực lượng tàu chiến đấu mặt nước",
        "desc": "Duy trì khả năng sẵn sàng chiến đấu cao cho các lữ đoàn tàu tuần tiễu, nâng cấp hệ thống điện tử và vũ khí tên lửa trên các tàu chiến mặt nước hiện có.",
        "icon": "GFX_focus_VIE_nf_surface_force",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_t02_officer_sailor_quality",
        "abs_x": 205, "abs_y": 5,
        "prereq": ["VIE_nav_t02_officer_sailor_quality"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_tech_bonus = { name = VIE_w01_surface_tech bonus = 0.50 uses = 1 category = CAT_surface_ships }",
            "add_ideas = VIE_nav_surface_combatants_spirit"
        ]
    },
    {
        "id": "VIE_nav_w04_kilo_submarine_force",
        "name": "Xây dựng lực lượng tàu ngầm hiện đại",
        "desc": "Xây dựng Lữ đoàn 189 tàu ngầm tinh nhuệ, đưa vào vận hành 6 tàu ngầm diesel-điện Kilo 636.1 trang bị tên lửa hành trình Club-S, tạo ra năng lực răn đe ngầm chiến lược dưới lòng biển.",
        "icon": "GFX_focus_VIE_nf_submarine_force",
        "cost": 7,
        "x": 2, "y": 1, "rel": "VIE_nav_t02_officer_sailor_quality",
        "abs_x": 207, "abs_y": 5,
        "prereq": ["VIE_nav_t02_officer_sailor_quality"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "navy_experience = 20",
            "add_tech_bonus = { name = VIE_w04_submarine_tech bonus = 0.75 uses = 1 category = CAT_submarines }",
            "set_country_flag = VIE_nav_w04_kilo_unlocked"
        ]
    },
    {
        "id": "VIE_nav_t04_joint_command_system",
        "name": "Hoàn thiện hệ thống chỉ huy hiệp đồng Hải quân",
        "desc": "Kết nối Sở Chỉ huy Quân chủng với các Bộ Tư lệnh Vùng, các biên đội tàu cơ động và lực lượng phòng thủ bờ biển, hình thành mạng lưới chỉ huy điều hành thống nhất.",
        "icon": "GFX_focus_VIE_nf_command_reform_2",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_t03_regional_commands",
        "abs_x": 209, "abs_y": 5,
        "prereq": ["VIE_nav_t02_officer_sailor_quality", "VIE_nav_t03_regional_commands"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_command_power = 25",
            "add_ideas = VIE_nav_joint_command_spirit"
        ]
    },
    {
        "id": "VIE_nav_i04_domestic_corvette_class",
        "name": "Phát triển thế hệ tàu hộ vệ do Việt Nam đóng mới",
        "desc": "Triển khai dự án đóng mới lớp tàu hộ vệ săn ngầm và đa năng thế hệ mới tại Nhà máy Sông Thu, khẳng định năng lực tự chủ hoàn toàn kỹ thuật đóng tàu chiến hiện đại của đất nước.",
        "icon": "GFX_focus_VIE_small_combatant_construction",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_i02_technology_transfer_molniya",
        "abs_x": 215, "abs_y": 5,
        "prereq": ["VIE_nav_i02_technology_transfer_molniya", "VIE_nav_i03_ship_systems_integration"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "navy_experience = 15",
            "add_tech_bonus = { name = VIE_i04_corvette_tech bonus = 0.75 uses = 1 category = CAT_surface_ships }",
            "set_country_flag = VIE_nav_i04_song_thu_unlocked"
        ]
    },
    {
        "id": "VIE_nav_s01_maritime_surveillance",
        "name": "Mở rộng khả năng cảnh giới vùng biển",
        "desc": "Triển khai hệ thống trạm radar bờ biển tầm xa, tích hợp dữ liệu trinh sát quang học và vệ tinh, nâng cao khả năng phát hiện sớm mọi hoạt động trên các vùng biển trọng điểm.",
        "icon": "GFX_focus_VIE_scs_assert_maritime_rights",
        "cost": 5,
        "x": 0, "y": 2, "rel": "VIE_nav_i01_shipbuilding_industry",
        "abs_x": 217, "abs_y": 5,
        "prereq": ["VIE_nav_t01_organization_reform"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_ideas = VIE_nav_maritime_surveillance_spirit"
        ]
    },
    {
        "id": "VIE_nav_l01_naval_bases",
        "name": "Hiện đại hóa căn cứ Hải quân",
        "desc": "Nâng cấp cơ sở hạ tầng các quân cảng Cam Ranh, Đà Nẵng, Hải Phòng, Phú Quốc; trang bị cầu cảng hiện đại, trạm nạp nhiên liệu và cơ sở kỹ thuật bảo đảm cho hạm đội.",
        "icon": "GFX_focus_VIE_scs_cam_ranh_port",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_i03_ship_systems_integration",
        "abs_x": 219, "abs_y": 5,
        "prereq": ["VIE_nav_t01_organization_reform"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_ideas = VIE_nav_naval_bases_spirit"
        ]
    },
    # Y = 6 (Bụng Cánh Buồm - 8 nodes)
    {
        "id": "VIE_nav_w02_missile_boats",
        "name": "Phát triển lực lượng tàu tên lửa cơ động",
        "desc": "Biên chế các biên đội tàu tên lửa cao tốc Molniya và BPS-500, sở hữu hỏa lực diệt hạm tập trung Uran-E với khả năng tác chiến đánh luồn, phục kích bất ngờ trên biển.",
        "icon": "GFX_focus_VIE_small_combatant_construction",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_w01_surface_combatants",
        "abs_x": 205, "abs_y": 6,
        "prereq": ["VIE_nav_w01_surface_combatants"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_tech_bonus = { name = VIE_w02_missile_boat bonus = 0.50 uses = 1 category = CAT_surface_ships }",
            "set_country_flag = VIE_nav_w02_molniya_unlocked"
        ]
    },
    {
        "id": "VIE_nav_w03_multirole_frigates",
        "name": "Tiếp nhận và làm chủ tàu hộ vệ đa nhiệm",
        "desc": "Khai thác làm chủ lực lượng khinh hạm Gepard 3.9 (Project 11661E), trang bị hỏa lực chống hạm, phòng không Palma và trực thăng săn ngầm Ka-28, đóng vai trò nòng cốt hạm đội.",
        "icon": "GFX_focus_VIE_nf_regional_frigates",
        "cost": 7,
        "x": 2, "y": 1, "rel": "VIE_nav_w01_surface_combatants",
        "abs_x": 207, "abs_y": 6,
        "prereq": ["VIE_nav_w01_surface_combatants"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_tech_bonus = { name = VIE_w03_frigate bonus = 0.50 uses = 1 category = CAT_destroyers }",
            "set_country_flag = VIE_nav_w03_gepard_unlocked"
        ]
    },
    {
        "id": "VIE_nav_s03_subsurface_recon",
        "name": "Hiện đại hóa trinh sát biển và dưới mặt nước",
        "desc": "Trang bị hệ thống định vị thủy âm sonar cố định và cơ động, nâng cao năng lực trinh sát phát hiện tàu ngầm đối phương và bảo vệ an toàn các luồng hàng hải trọng yếu.",
        "icon": "GFX_focus_VIE_nf_denial_command",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_t04_joint_command_system",
        "abs_x": 209, "abs_y": 6,
        "prereq": ["VIE_nav_s01_maritime_surveillance"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_ideas = VIE_nav_subsurface_recon_spirit"
        ]
    },
    {
        "id": "VIE_nav_s02_island_defense_forces",
        "name": "Củng cố lực lượng bảo vệ đảo",
        "desc": "Tăng cường năng lực tác chiến phòng thủ đảo cho Lữ đoàn 146 và các đơn vị Trường Sa; củng cố công sự, trận địa pháo và các trạm quan sát cảnh giới kiên cố.",
        "icon": "GFX_focus_VIE_scs_spratly_fortification",
        "cost": 5,
        "x": 2, "y": 1, "rel": "VIE_nav_t04_joint_command_system",
        "abs_x": 211, "abs_y": 6,
        "prereq": ["VIE_nav_s01_maritime_surveillance"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_ideas = VIE_nav_island_defense_spirit",
            "set_country_flag = VIE_nav_s02_bastion_unlocked"
        ]
    },
    {
        "id": "VIE_nav_l02_overhaul_maintenance",
        "name": "Chuẩn hóa hệ thống bảo dưỡng và đại tu",
        "desc": "Xây dựng quy trình kỹ thuật sửa chữa định kỳ, trung tu và đại tu tàu mặt nước và tàu ngầm trong nước, giảm thiểu phụ thuộc vào cơ sở kỹ thuật nước ngoài.",
        "icon": "GFX_focus_VIE_naval_mro",
        "cost": 5,
        "x": -2, "y": 1, "rel": "VIE_nav_i04_domestic_corvette_class",
        "abs_x": 213, "abs_y": 6,
        "prereq": ["VIE_nav_l01_naval_bases"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_ideas = VIE_nav_overhaul_maintenance_spirit"
        ]
    },
    {
        "id": "VIE_nav_l03_island_logistics",
        "name": "Xây dựng hệ thống hậu cần biển đảo",
        "desc": "Tổ chức tuyến vận tải tiếp tế định kỳ và đột xuất cho các đảo và nhà giàn DK1; nâng cao năng lực dự trữ nước ngọt, lương thực và nhiên liệu trong mọi điều kiện thời tiết.",
        "icon": "GFX_focus_VIE_scs_dk1_platforms",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_i04_domestic_corvette_class",
        "abs_x": 215, "abs_y": 6,
        "prereq": ["VIE_nav_l01_naval_bases"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_ideas = VIE_nav_island_logistics_spirit"
        ]
    },
    {
        "id": "VIE_nav_h01_fleet_development_priority",
        "name": "Ưu tiên xây dựng hạm đội tác chiến hiện đại",
        "desc": "Chuyển hướng chiến lược tập trung nguồn lực phát triển các biên đội tàu chiến đấu mặt nước đa năng, sẵn sàng vươn khơi làm chủ các vùng biển khu vực.",
        "icon": "GFX_focus_VIE_nf_greenwater",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_s01_maritime_surveillance",
        "abs_x": 217, "abs_y": 6,
        "prereq": ["VIE_nav_t04_joint_command_system", "VIE_nav_w01_surface_combatants"],
        "mutually_exclusive": ["VIE_nav_p01_integrated_defense_choice"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_ideas = VIE_nav_fleet_development_h1"
        ]
    },
    {
        "id": "VIE_nav_p01_integrated_defense_choice",
        "name": "Lựa chọn chiến lược phòng thủ biển tích hợp",
        "desc": "Tập trung xây dựng thế trận chống tiếp cận/chống thâm nhập khu vực (A2/AD) nhiều tầng, kết hợp hỏa lực tên lửa bờ biển, tàu ngầm Kilo và hệ thống công sự đảo.",
        "icon": "GFX_focus_VIE_nf_denial",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_l01_naval_bases",
        "abs_x": 219, "abs_y": 6,
        "prereq": ["VIE_nav_t04_joint_command_system", "VIE_nav_w01_surface_combatants"],
        "mutually_exclusive": ["VIE_nav_h01_fleet_development_priority"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_ideas = VIE_nav_integrated_defense_p1"
        ]
    },
    # Y = 7
    {
        "id": "VIE_nav_w05_asw_fleet_defense",
        "name": "Nâng cao năng lực chống ngầm và tự vệ hạm đội",
        "desc": "Trang bị ngư lôi săn ngầm hiện đại, nâng cao năng lực phối hợp giữa trực thăng săn ngầm hải quân Ka-28 và hệ thống hỏa lực phòng vệ trên tàu chiến.",
        "icon": "GFX_focus_VIE_nf_naval_aviation",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_w02_missile_boats",
        "abs_x": 205, "abs_y": 7,
        "prereq": ["VIE_nav_w03_multirole_frigates", "VIE_nav_s03_subsurface_recon"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_ideas = VIE_nav_asw_defense_spirit"
        ]
    },
    {
        "id": "VIE_nav_s04_joint_island_defense",
        "name": "Hiệp đồng bảo vệ biển đảo",
        "desc": "Tổ chức thế trận hiệp đồng tác chiến chặt chẽ giữa Hải quân, Phòng không - Không quân, Cảnh sát biển, Kiểm ngư và Hải đội Dân quân thường trực.",
        "icon": "GFX_focus_VIE_scs_maritime_militia",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_w03_multirole_frigates",
        "abs_x": 207, "abs_y": 7,
        "prereq": ["VIE_nav_s02_island_defense_forces", "VIE_nav_s03_subsurface_recon"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_ideas = VIE_nav_joint_island_defense_spirit"
        ]
    },
    {
        "id": "VIE_nav_l04_support_rescue_vessels",
        "name": "Phát triển lực lượng tàu hỗ trợ và cứu hộ",
        "desc": "Biên chế tàu cứu nạn tàu ngầm đa năng Yết Kiêu 927 và các tàu vận tải tiếp tế thế hệ mới, bảo đảm an toàn tuyệt đối cho hoạt động tác chiến của hạm đội.",
        "icon": "GFX_focus_VIE_nf_replenishment",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_s03_subsurface_recon",
        "abs_x": 209, "abs_y": 7,
        "prereq": ["VIE_nav_l02_overhaul_maintenance", "VIE_nav_l03_island_logistics"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 10",
            "add_ideas = VIE_nav_support_rescue_spirit"
        ]
    },
    {
        "id": "VIE_nav_p02_coastal_island_network",
        "name": "Xây dựng mạng lưới phòng thủ bờ – đảo",
        "desc": "Liên kết chặt chẽ các trận địa tên lửa phòng thủ bờ biển Bastion-P, Redut-M với các cụm đảo tiền tiêu, hình thành lá chắn hỏa lực bảo vệ vững chắc lãnh hải.",
        "icon": "GFX_focus_VIE_nf_denial_defence",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_l02_overhaul_maintenance",
        "abs_x": 213, "abs_y": 7,
        "prereq": ["VIE_nav_p01_integrated_defense_choice", "VIE_nav_s02_island_defense_forces"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_ideas = VIE_nav_coastal_island_network_spirit"
        ]
    },
    {
        "id": "VIE_nav_p03_island_territory_defense",
        "name": "Củng cố lực lượng bảo vệ các địa bàn biển đảo",
        "desc": "Tăng cường năng lực cơ động tác chiến và hỏa lực cho Lữ đoàn Hải quân đánh bộ 101 và 147, sẵn sàng đổ bộ tái chiếm và bảo vệ các đảo trọng yếu.",
        "icon": "GFX_focus_VIE_sf_marine",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_l03_island_logistics",
        "abs_x": 215, "abs_y": 7,
        "prereq": ["VIE_nav_p01_integrated_defense_choice", "VIE_nav_l03_island_logistics"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_ideas = VIE_nav_island_territory_defense_spirit"
        ]
    },
    {
        "id": "VIE_nav_h02_multirole_task_groups",
        "name": "Hình thành các biên đội tàu tác chiến đa nhiệm",
        "desc": "Tổ chức các biên đội tác chiến kết hợp khinh hạm hộ vệ, tàu pháo tên lửa cao tốc và tàu bảo đảm hậu cần, có năng lực tuần tra tác chiến độc lập tầm trung.",
        "icon": "GFX_focus_VIE_nf_medium_force",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_h01_fleet_development_priority",
        "abs_x": 217, "abs_y": 7,
        "prereq": ["VIE_nav_h01_fleet_development_priority", "VIE_nav_w03_multirole_frigates", "VIE_nav_l02_overhaul_maintenance"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 20",
            "add_ideas = VIE_nav_multirole_task_groups_spirit"
        ]
    },
    # Y = 8
    {
        "id": "VIE_nav_s05_unified_maritime_picture",
        "name": "Hình thành hệ thống nhận thức tình hình biển thống nhất",
        "desc": "Hợp nhất toàn bộ dữ liệu cảnh giới từ radar bờ, tàu ngầm, máy bay tuần thám và các trạm quan sát đảo thành một bức tranh nhận thức tình hình biển (MDA) thời gian thực.",
        "icon": "GFX_focus_VIE_nf_operating_range",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_s04_joint_island_defense",
        "abs_x": 207, "abs_y": 8,
        "prereq": ["VIE_nav_s04_joint_island_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 20",
            "add_ideas = VIE_nav_unified_maritime_picture_spirit"
        ]
    },
    {
        "id": "VIE_nav_l05_sustained_operations",
        "name": "Nâng cao khả năng duy trì hoạt động dài ngày",
        "desc": "Hoàn thiện quy trình luân phiên lực lượng, tiếp tế cơ động trên biển (RAS) và bảo dưỡng ngoài khơi, giúp tàu chiến có thể bám biển hoạt động liên tục nhiều tháng.",
        "icon": "GFX_focus_VIE_nf_ocean_escort",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_l04_support_rescue_vessels",
        "abs_x": 209, "abs_y": 8,
        "prereq": ["VIE_nav_l04_support_rescue_vessels"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 20",
            "add_ideas = VIE_nav_sustained_operations_spirit"
        ]
    },
    {
        "id": "VIE_nav_p04_layered_defense",
        "name": "Hiện đại hóa năng lực phòng thủ biển nhiều lớp",
        "desc": "Tích hợp tên lửa hành trình chống hạm tầm siêu âm, bãi thủy lôi thông minh và các bệ phóng ngụy trang cơ động, tạo nên thế trận phòng thủ hiểm hóc không thể xuyên phá.",
        "icon": "GFX_focus_VIE_nf_denial_subs",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_p02_coastal_island_network",
        "abs_x": 213, "abs_y": 8,
        "prereq": ["VIE_nav_p02_coastal_island_network"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 15",
            "add_ideas = VIE_nav_layered_defense_spirit"
        ]
    },
    {
        "id": "VIE_nav_g01_greenwater_navy",
        "name": "Định hướng xây dựng Hải quân biển gần hiện đại",
        "desc": "Xác lập học thuyết Hải quân biển gần (Green-water), tập trung xây dựng hạm đội mặt nước cơ động và lực lượng săn ngầm làm chủ hoàn toàn vùng đặc quyền kinh tế (EEZ).",
        "icon": "GFX_focus_VIE_nf_greenwater",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_p03_island_territory_defense",
        "abs_x": 215, "abs_y": 8,
        "prereq": ["VIE_nav_h02_multirole_task_groups"],
        "mutually_exclusive": ["VIE_nav_b01_bluewater_navy"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 20",
            "add_ideas = VIE_nav_greenwater_g1"
        ]
    },
    {
        "id": "VIE_nav_b01_bluewater_navy",
        "name": "Khởi động chương trình Hải quân biển xa",
        "desc": "Mở rộng tầm nhìn hướng ra đại dương (Blue-water), đặt mục tiêu xây dựng các cụm tàu chiến đấu có khả năng bảo vệ tuyến hàng hải huyết mạch và hiện diện tại các vùng biển xa.",
        "icon": "GFX_focus_VIE_nf_bluewater",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_h02_multirole_task_groups",
        "abs_x": 217, "abs_y": 8,
        "prereq": ["VIE_nav_h02_multirole_task_groups", "VIE_nav_l05_sustained_operations"],
        "mutually_exclusive": ["VIE_nav_g01_greenwater_navy"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 25",
            "add_ideas = VIE_nav_bluewater_b1"
        ]
    },
    # Y = 9
    {
        "id": "VIE_nav_p05_joint_coastal_defense",
        "name": "Hiệp đồng tác chiến phòng thủ biển",
        "desc": "Kết hợp nhịp nhàng các đòn phục kích của tàu ngầm Kilo với hỏa lực bờ biển và lực lượng không quân tiêm kích bom Su-30MK2, giáng đòn tiêu diệt các hạm đội tàu đối phương.",
        "icon": "GFX_focus_VIE_nf_denial_command",
        "cost": 7,
        "x": -2, "y": 1, "rel": "VIE_nav_p04_layered_defense",
        "abs_x": 211, "abs_y": 9,
        "prereq": ["VIE_nav_p03_island_territory_defense", "VIE_nav_p04_layered_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 20",
            "add_ideas = VIE_nav_joint_coastal_defense_spirit"
        ]
    },
    {
        "id": "VIE_nav_g02_advanced_frigates_asw",
        "name": "Hiện đại hóa lực lượng tàu hộ vệ và chống ngầm",
        "desc": "Trang bị các tàu hộ vệ cỡ lớn có khả năng tàng hình, hệ thống phóng thẳng đứng VLS hiện đại và sonar thủy âm kéo theo tiên tiến, nâng cao vượt bậc năng lực săn ngầm.",
        "icon": "GFX_focus_VIE_nf_regional_frigates",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_p04_layered_defense",
        "abs_x": 213, "abs_y": 9,
        "prereq": ["VIE_nav_g01_greenwater_navy", "VIE_nav_w05_asw_fleet_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 20",
            "add_tech_bonus = { name = VIE_g02_frigate_tech bonus = 0.50 uses = 1 category = CAT_destroyers }",
            "add_ideas = VIE_nav_advanced_frigates_asw_spirit"
        ]
    },
    {
        "id": "VIE_nav_b02_extended_deployment_fleet",
        "name": "Xây dựng hạm đội có khả năng triển khai dài ngày",
        "desc": "Đầu tư tàu hậu cần viễn dương cỡ lớn, hoàn thiện kỹ năng tiếp vận trên biển và khả năng phối hợp tác chiến liên tục nhiều tháng ở vùng biển quốc tế.",
        "icon": "GFX_focus_VIE_nf_carrier_group",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_g01_greenwater_navy",
        "abs_x": 215, "abs_y": 9,
        "prereq": ["VIE_nav_b01_bluewater_navy", "VIE_nav_s04_joint_island_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 25",
            "add_tech_bonus = { name = VIE_b02_ocean_tech bonus = 0.50 uses = 1 category = CAT_naval }",
            "add_ideas = VIE_nav_extended_deployment_spirit"
        ]
    },
    # Y = 10
    {
        "id": "VIE_nav_p06_active_coastal_defense_capstone",
        "name": "Hoàn thiện thế trận phòng thủ biển chủ động",
        "desc": "Đỉnh cao của học thuyết Phòng thủ tích hợp: xác lập thế trận phòng ngự chủ động kiên cường, biến từng mét biển, từng hòn đảo thành pháo đài thép bất khả xâm phạm.",
        "icon": "GFX_focus_VIE_nf_denial_defence",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_p05_joint_coastal_defense",
        "abs_x": 211, "abs_y": 10,
        "prereq": ["VIE_nav_p05_joint_coastal_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 30",
            "swap_ideas = { remove_idea = VIE_nav_integrated_defense_p1 add_idea = VIE_nav_integrated_defense_p6 }",
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
        "abs_x": 213, "abs_y": 10,
        "prereq": ["VIE_nav_g02_advanced_frigates_asw", "VIE_nav_l03_island_logistics"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 30",
            "swap_ideas = { remove_idea = VIE_nav_greenwater_g1 add_idea = VIE_nav_greenwater_g3 }",
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
        "abs_x": 215, "abs_y": 10,
        "prereq": ["VIE_nav_b02_extended_deployment_fleet"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 35",
            "swap_ideas = { remove_idea = VIE_nav_bluewater_b1 add_idea = VIE_nav_bluewater_b3 }",
            "set_country_flag = VIE_nav_b_doctrine_completed"
        ]
    },
    # Y = 11
    {
        "id": "VIE_nav_f01_tactical_doctrine_alignment",
        "name": "Hoàn thiện học thuyết tác chiến Hải quân",
        "desc": "Đúc kết kinh nghiệm thực tiễn và tinh hoa các học thuyết tác chiến, hoàn thiện cơ chế chỉ huy tham mưu và nghệ thuật quân sự Hải quân nhân dân Việt Nam.",
        "icon": "GFX_focus_VIE_nf_command_reform_1",
        "cost": 7,
        "x": 1, "y": 1, "rel": "VIE_nav_p06_active_coastal_defense_capstone",
        "abs_x": 212, "abs_y": 11,
        "prereq_or": [
            "VIE_nav_p06_active_coastal_defense_capstone",
            "VIE_nav_g03_self_reliant_greenwater_capstone",
            "VIE_nav_b03_sustained_bluewater_capstone"
        ],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 25",
            "add_command_power = 30",
            "add_political_power = 50"
        ]
    },
    # Y = 12
    {
        "id": "VIE_nav_f02_regular_modern_navy",
        "name": "Xây dựng Hải quân nhân dân Việt Nam chính quy, hiện đại",
        "desc": "Khẳng định tầm vóc mới của Hải quân nhân dân Việt Nam: Quân chủng cách mạng, chính quy, tinh nhuệ, hiện đại, làm nòng cốt quản lý và bảo vệ vững chắc chủ quyền biển đảo thiêng liêng của Tổ quốc.",
        "icon": "GFX_focus_VIE_naval_defence_law",
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_f01_tactical_doctrine_alignment",
        "abs_x": 212, "abs_y": 12,
        "prereq": [
            "VIE_nav_f01_tactical_doctrine_alignment",
            "VIE_nav_s05_unified_maritime_picture",
            "VIE_nav_l05_sustained_operations"
        ],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "navy_experience = 50",
            "add_command_power = 50",
            "add_political_power = 100",
            """if = {
				limit = { has_country_flag = VIE_nav_p_doctrine_completed }
				add_ideas = VIE_nav_capstone_integrated_defense_f2
			}
			else_if = {
				limit = { has_country_flag = VIE_nav_g_doctrine_completed }
				add_ideas = VIE_nav_capstone_greenwater_f2
			}
			else_if = {
				limit = { has_country_flag = VIE_nav_b_doctrine_completed }
				add_ideas = VIE_nav_capstone_bluewater_f2
			}
			else = {
				add_ideas = VIE_nav_capstone_greenwater_f2
			}""",
            "set_country_flag = VIE_navy_modernized"
        ]
    }
]

def generate_focus_tree_snippet():
    out = []
    out.append("\t######################################################################")
    out.append("\t## ĐỀ ÁN V34: NHÁNH HẢI QUÂN VIỆT NAM (ORGANIC DIAMOND FLOW - 40 FOCUS)")
    out.append("\t## TÂM ĐỐI XỨNG X = 212 · CÁNH BUỒM TỪ Y = 2 ĐẾN Y = 12")
    out.append("\t######################################################################\n")

    for f in FOCUS_DATA:
        out.append(f"\tfocus = {{")
        out.append(f"\t\tid = {f['id']}")
        out.append(f"\t\ticon = {f['icon']}\n")
        out.append(f"\t\tx = {f['x']}")
        out.append(f"\t\ty = {f['y']}")
        out.append(f"\t\trelative_position_id = {f['rel']}\n")
        out.append(f"\t\tcost = {f['cost']}\n")

        # Mutex
        if "mutually_exclusive" in f:
            mx_str = " ".join([f"focus = {mx}" for mx in f["mutually_exclusive"]])
            out.append(f"\t\tmutually_exclusive = {{ {mx_str} }}\n")

        # Prerequisites
        if "prereq_or" in f:
            out.append("\t\tprerequisite = {")
            for pr in f["prereq_or"]:
                out.append(f"\t\t\tfocus = {pr}")
            out.append("\t\t}\n")
        elif "prereq" in f:
            for pr in f["prereq"]:
                out.append(f"\t\tprerequisite = {{ focus = {pr} }}")
            out.append("")

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

IDEAS_CONTENT = """# ======================================================================
# ĐỀ ÁN V34: HẢI QUÂN NHÂN DÂN VIỆT NAM (NATIONAL SPIRITS & IDEAS)
# ======================================================================

ideas = {
	country = {

		# --- TRỤC NỀN TẢNG (T, I, W, S, L) ---

		VIE_nav_organization_reform_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_org = 3
				navy_leader_start_level = 1
			}
		}

		VIE_nav_shipbuilding_industry_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.05
				industrial_capacity_dockyard = 0.05
			}
		}

		VIE_nav_officer_sailor_quality_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				experience_gain_navy_factor = 0.10
				naval_org = 3
			}
		}

		VIE_nav_regional_commands_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_coordination = 0.05
				coastal_defense_coordination = 0.05
			}
		}

		VIE_nav_technology_transfer_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				research_speed_naval = 0.05
			}
		}

		VIE_nav_systems_integration_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				navy_radar_efficiency = 0.05
				screen_surface_detection = 0.05
			}
		}

		VIE_nav_surface_combatants_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.05
				navy_screen_attack_factor = 0.05
			}
		}

		VIE_nav_joint_command_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_coordination = 0.08
				planning_speed = 0.05
			}
		}

		VIE_nav_maritime_surveillance_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_detection = 0.05
				surface_detection = 0.05
			}
		}

		VIE_nav_naval_bases_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				naval_base_efficiency = 0.10
				repair_speed_factor = 0.05
			}
		}

		VIE_nav_subsurface_recon_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				sub_detection = 0.08
				navy_submarine_detection_factor = 0.08
			}
		}

		VIE_nav_island_defense_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				amphibious_defense = 0.10
				naval_strike_defense_factor = 0.05
			}
		}

		VIE_nav_overhaul_maintenance_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				repair_speed_factor = 0.10
				naval_attrition = -0.05
			}
		}

		VIE_nav_island_logistics_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				supply_consumption_factor = -0.05
				navy_max_range_factor = 0.05
			}
		}

		VIE_nav_fleet_development_h1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.05
				naval_speed_factor = 0.05
				escort_efficiency = 0.05
			}
		}

		VIE_nav_integrated_defense_p1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screen_surface_detection = 0.05
				navy_anti_air_attack_factor = 0.05
				naval_coordination = 0.05
			}
		}

		VIE_nav_asw_defense_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				sub_detection = 0.10
				navy_anti_submarine_attack_factor = 0.10
			}
		}

		VIE_nav_joint_island_defense_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				amphibious_defense = 0.15
				coastal_defense_coordination = 0.10
			}
		}

		VIE_nav_support_rescue_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				repair_speed_factor = 0.10
				convoy_escort_efficiency = 0.05
			}
		}

		VIE_nav_coastal_island_network_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_detection = 0.10
				naval_strike_defense_factor = 0.08
			}
		}

		VIE_nav_island_territory_defense_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				amphibious_defense = 0.15
				naval_org = 5
			}
		}

		VIE_nav_multirole_task_groups_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.10
				naval_coordination = 0.08
			}
		}

		VIE_nav_unified_maritime_picture_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_detection = 0.12
				sub_detection = 0.10
				naval_coordination = 0.10
			}
		}

		VIE_nav_sustained_operations_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.10
				repair_speed_factor = 0.15
				naval_attrition = -0.10
			}
		}

		VIE_nav_layered_defense_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				coastal_defense_coordination = 0.12
				navy_anti_air_attack_factor = 0.10
				screen_surface_detection = 0.08
			}
		}

		VIE_nav_greenwater_g1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.08
				navy_submarine_detection_factor = 0.08
				navy_surface_detection_factor = 0.08
			}
		}

		VIE_nav_bluewater_b1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.12
				naval_org = 5
				convoy_escort_efficiency = 0.10
			}
		}

		VIE_nav_joint_coastal_defense_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_coordination = 0.12
				amphibious_defense = 0.15
				naval_strike_defense_factor = 0.10
			}
		}

		VIE_nav_advanced_frigates_asw_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_anti_submarine_attack_factor = 0.15
				screening_efficiency = 0.10
				screen_surface_detection = 0.10
			}
		}

		VIE_nav_extended_deployment_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.15
				naval_speed_factor = 0.08
				convoy_escort_efficiency = 0.12
			}
		}

		# --- DOCTRINE CAPSTONES (P06, G03, B03) ---

		VIE_nav_integrated_defense_p6 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screen_surface_detection = 0.12
				navy_anti_air_attack_factor = 0.12
				naval_coordination = 0.12
				naval_strike_defense_factor = 0.12
				sub_detection = 0.12
			}
		}

		VIE_nav_greenwater_g3 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.15
				navy_submarine_detection_factor = 0.15
				navy_surface_detection_factor = 0.12
				naval_coordination = 0.10
				navy_anti_air_attack_factor = 0.08
			}
		}

		VIE_nav_bluewater_b3 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.22
				naval_org = 10
				convoy_escort_efficiency = 0.18
				naval_coordination = 0.12
			}
		}

		# --- CAPSTONE TỐI THƯỢNG F02 (THEO DOCTRINE ĐÃ CHỌN) ---

		VIE_nav_capstone_integrated_defense_f2 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_strike_defense_factor = 0.15
				sub_detection = 0.15
				naval_coordination = 0.15
				screen_surface_detection = 0.15
			}
		}

		VIE_nav_capstone_greenwater_f2 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.18
				navy_submarine_detection_factor = 0.15
				naval_org = 10
				escort_efficiency = 0.18
			}
		}

		VIE_nav_capstone_bluewater_f2 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.25
				naval_coordination = 0.18
				naval_org = 15
				convoy_escort_efficiency = 0.20
			}
		}

		# --- DECISION TIMED SPIRITS ---

		VIE_decision_domestic_corvette_construction_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.10
				industrial_capacity_dockyard = 0.08
			}
		}

		VIE_decision_kilo_sustainment_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				sub_detection = 0.10
				sub_visibility = -0.05
			}
		}

		VIE_decision_island_bastion_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_coastal_bunker_factor = 0.20
				amphibious_defense = 0.15
			}
		}

	}
}
"""

DECISIONS_CONTENT = """# ======================================================================
# ĐỀ ÁN V34: QUYẾT ĐỊNH MUA SẮM VÀ PHÁT TRIỂN HẢI QUÂN
# ======================================================================

VIE_naval_procurement_category = {

	VIE_decision_molniya_production_run = {
		icon = GFX_decision_generic_naval
		cost = 25

		days_remove = 180
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_n00_maritime_strategy_21st
		}

		available = {
			has_country_flag = VIE_nav_w02_molniya_unlocked
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_molniya_production_run"
			set_temp_variable = { treasury_change = -1.5 }
			modify_treasury_effect = yes
			navy_experience = 10
		}

		ai_will_do = {
			factor = 10
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_gepard_batch_procurement = {
		icon = GFX_decision_generic_naval
		cost = 30

		days_remove = 180
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_n00_maritime_strategy_21st
		}

		available = {
			has_country_flag = VIE_nav_w03_gepard_unlocked
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_gepard_batch_procurement"
			set_temp_variable = { treasury_change = -2.5 }
			modify_treasury_effect = yes
			navy_experience = 15
		}

		ai_will_do = {
			factor = 10
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_kilo_submarine_sustainment = {
		icon = GFX_decision_generic_naval
		cost = 25

		days_remove = 365
		days_re_enable = 365

		visible = {
			has_completed_focus = VIE_nav_n00_maritime_strategy_21st
		}

		available = {
			has_country_flag = VIE_nav_w04_kilo_unlocked
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_kilo_submarine_sustainment"
			set_temp_variable = { treasury_change = -2.0 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_decision_kilo_sustainment_spirit days = 365 }
		}

		ai_will_do = {
			factor = 10
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_domestic_corvette_lead_ship = {
		icon = GFX_decision_generic_dockyard
		cost = 35

		days_remove = 730
		days_re_enable = 365

		visible = {
			has_completed_focus = VIE_nav_n00_maritime_strategy_21st
		}

		available = {
			has_country_flag = VIE_nav_i04_song_thu_unlocked
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_domestic_corvette_lead_ship"
			set_temp_variable = { treasury_change = -1.8 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_decision_domestic_corvette_construction_spirit days = 730 }
		}

		ai_will_do = {
			factor = 10
		}
	}

	VIE_decision_island_bastion_fortification = {
		icon = GFX_decision_generic_fortification
		cost = 20

		days_remove = 365
		days_re_enable = 365

		visible = {
			has_completed_focus = VIE_nav_n00_maritime_strategy_21st
		}

		available = {
			has_country_flag = VIE_nav_s02_bastion_unlocked
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_island_bastion_fortification"
			set_temp_variable = { treasury_change = -1.0 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_decision_island_bastion_spirit days = 365 }
		}

		ai_will_do = {
			factor = 10
			modifier = { factor = 2 has_war = yes }
		}
	}

}
"""

def generate_loc_snippet():
    out = []
    out.append("### ============================================================")
    out.append("### ĐỀ ÁN V34: HẢI QUÂN NHÂN DÂN VIỆT NAM (40 FOCUS V34)")
    out.append("### ============================================================\n")

    # Focus titles & descs
    for f in FOCUS_DATA:
        fid = f["id"]
        fname = f["name"]
        fdesc = f["desc"]
        out.append(f' {fid}:0 "{fname}"')
        out.append(f' {fid}_desc:0 "{fdesc}"')

    out.append("\n### ============================================================")
    out.append("### NATIONAL SPIRITS & IDEAS HẢI QUÂN V34")
    out.append("### ============================================================\n")

    spirit_loc = {
        "VIE_nav_organization_reform_spirit": ("Kiện toàn Tổ chức Hải quân", "Cơ cấu tổ chức và chỉ huy các cấp được tinh gọn, chuẩn hóa, nâng cao kỷ luật và khả năng sẵn sàng cơ động."),
        "VIE_nav_shipbuilding_industry_spirit": ("Công nghiệp Đóng tàu Quân sự", "Các cơ sở đóng tàu quân sự nội địa được tăng cường nguồn lực, đáp ứng nhiệm vụ bảo đảm kỹ thuật và đóng mới."),
        "VIE_nav_officer_sailor_quality_spirit": ("Cán bộ Thủy thủ Tinh nhuệ", "Đội ngũ sĩ quan và thủy thủ được đào tạo bài bản, bản lĩnh kiên cường, làm chủ vững chắc vũ khí trang bị hiện đại."),
        "VIE_nav_regional_commands_spirit": ("Các Vùng Hải quân Vững mạnh", "Năng lực lãnh đạo chỉ huy và quản lý vùng biển của các Bộ Tư lệnh Vùng 1 đến Vùng 5 được củng cố toàn diện."),
        "VIE_nav_technology_transfer_spirit": ("Chuyển giao Công nghệ Đóng tàu", "Tiếp nhận và làm chủ quy trình công nghệ chế tạo thân vỏ và trang bị tàu chiến đấu tốc độ cao."),
        "VIE_nav_systems_integration_spirit": ("Làm chủ Tích hợp Hệ thống Hạm tàu", "Năng lực tự chủ tích hợp hệ thống radar cảnh giới, quang điện tử và quản lý chỉ huy chiến đấu CMS trên tàu."),
        "VIE_nav_surface_combatants_spirit": ("Lực lượng Tàu mặt nước Tác chiến", "Các hải đội tàu chiến đấu mặt nước nâng cao khả năng hiệp đồng chiến thuật và sẵn sàng xuất kích bảo vệ chủ quyền."),
        "VIE_nav_joint_command_spirit": ("Chỉ huy Hiệp đồng Hải quân", "Mạng lưới truyền tin tác chiến số hóa bảo đảm chỉ huy thông suốt từ Bộ Tư lệnh tới từng biên đội tàu đang làm nhiệm vụ."),
        "VIE_nav_maritime_surveillance_spirit": ("Hệ thống Cảnh giới Duyên hải", "Mạng lưới radar trinh sát tầm xa duyên hải cung cấp tham số mục tiêu chuẩn xác cho các lực lượng chiến đấu."),
        "VIE_nav_naval_bases_spirit": ("Hạ tầng Quân cảng Chiến lược", "Căn cứ Cam Ranh và hệ thống quân cảng duyên hải bảo đảm đầy đủ năng lực neo đậu, bảo quản và tiếp tế hạm đội."),
        "VIE_nav_subsurface_recon_spirit": ("Trinh sát Phát hiện Dưới mặt nước", "Khả năng phát hiện và theo dõi mục tiêu ngầm dưới nước bằng hệ thống sonar đa tầng được nâng cao rõ rệt."),
        "VIE_nav_island_defense_spirit": ("Phòng thủ Kiên cố Quần đảo", "Các điểm đảo tiền tiêu được kiên cố hóa công sự, sẵn sàng đánh bại mọi mưu toan tập kích đổ bộ của đối phương."),
        "VIE_nav_overhaul_maintenance_spirit": ("Quy trình Bảo dưỡng & Đại tu Chuẩn hóa", "Nâng cao năng lực sửa chữa lớn và kiểm định kỹ thuật tàu thuyền tại chỗ, duy trì hệ số kỹ thuật cao cho hạm đội."),
        "VIE_nav_island_logistics_spirit": ("Bảo đảm Hậu cần Biển đảo", "Hệ thống kho dự trữ và phương tiện vận tải bảo đảm tiếp tế thông suốt cho quân dân các vùng đảo tiền tiêu."),
        "VIE_nav_fleet_development_h1": ("Định hướng Phát triển Hạm đội", "Ưu tiên đầu tư trang bị các lớp tàu mặt nước đa nhiệm có tầm hoạt động lớn và khả năng tuần tra dài ngày."),
        "VIE_nav_integrated_defense_p1": ("Phòng thủ Biển Tích hợp (Giai đoạn I)", "Tập trung xây dựng ô hỏa lực bảo vệ vùng biển nhiều tầng, phối hợp giữa tên lửa bờ biển, tàu ngầm và công sự đảo."),
        "VIE_nav_asw_defense_spirit": ("Tác chiến Chống ngầm & Tự vệ", "Biên đội tàu mặt nước kết hợp trực thăng săn ngầm nâng cao hiệu quả săn lùng và tiêu diệt tàu ngầm đối phương."),
        "VIE_nav_joint_island_defense_spirit": ("Hiệp đồng Liên quân Phòng thủ Biển đảo", "Phối hợp tác chiến nhịp nhàng giữa Hải quân, Không quân, Cảnh sát biển và Dân quân tự vệ biển tạo thành sức mạnh tổng hợp."),
        "VIE_nav_support_rescue_spirit": ("Đội tàu Hỗ trợ & Cứu nạn Đa năng", "Tàu cứu nạn chuyên dụng và tàu tiếp dầu bảo đảm sự an toàn và khả năng hoạt động liên tục của các biên đội."),
        "VIE_nav_coastal_island_network_spirit": ("Mạng lưới Hỏa lực Bờ - Đảo", "Trận địa tên lửa bờ kết hợp cùng các công sự đảo khép kín vòng kiểm soát, sẵn sàng trừng phạt mọi hành vi xâm phạm."),
        "VIE_nav_island_territory_defense_spirit": ("Hải quân Đánh bộ Phòng ngự - Đổ bộ", "Lực lượng Hải quân đánh bộ tinh nhuệ, sẵn sàng tác chiến phòng thủ đảo và cơ động đổ bộ tái chiếm mục tiêu."),
        "VIE_nav_multirole_task_groups_spirit": ("Biên đội Tác chiến Đa nhiệm Hạm đội", "Biên đội khinh hạm và tàu hộ vệ có năng lực tự vệ, phòng không, chống ngầm và tiến công mặt nước đồng bộ."),
        "VIE_nav_unified_maritime_picture_spirit": ("Nhận thức Tình hình Biển Thống nhất (MDA)", "Tích hợp toàn diện mọi nguồn dữ liệu trinh sát thành bức tranh tình huống mặt biển thời gian thực cho Sở Chỉ huy."),
        "VIE_nav_sustained_operations_spirit": ("Duy trì Hoạt động Bền bỉ Trên biển", "Năng lực tiếp tế cơ động và sửa chữa trên biển giúp hạm đội duy trì hiện diện thường trực tại các vùng biển xa."),
        "VIE_nav_layered_defense_spirit": ("Lá chắn Phòng thủ Biển Đa tầng", "Hệ thống phòng thủ chiều sâu kết hợp tên lửa đối hạm, pháo bờ biển, chướng ngại vật ngầm và lưới lửa phòng không."),
        "VIE_nav_greenwater_g1": ("Hải quân Biển gần Hiện đại (Green-water I)", "Hạm đội mặt nước cơ động và lực lượng chống ngầm làm chủ hoàn toàn vùng biển đặc quyền kinh tế và thềm lục địa."),
        "VIE_nav_bluewater_b1": ("Chương trình Hải quân Biển xa (Blue-water I)", "Đặt nền móng kỹ thuật và hậu cần để đưa hạm đội vươn ra các vùng biển quốc tế và bảo vệ các tuyến hàng hải chiến lược."),
        "VIE_nav_joint_coastal_defense_spirit": ("Hiệp đồng Phòng ngự Biển Chiều sâu", "Phối hợp tiến công giữa tàu ngầm, không quân chiến dịch và hỏa lực bờ biển tạo thế áp đảo trước hạm đội đối phương."),
        "VIE_nav_advanced_frigates_asw_spirit": ("Khinh hạm Tàng hình & Chống ngầm", "Trang bị các lớp khinh hạm tàng hình thế hệ mới với vũ khí săn ngầm tầm xa, bảo vệ hạm đội trước mối đe dọa ngầm."),
        "VIE_nav_extended_deployment_spirit": ("Biên đội Triển khai Dài ngày", "Khả năng duy trì các biên đội tàu chiến tuần tra tầm xa với hậu cần tiếp tế viễn dương liên tục."),
        "VIE_nav_integrated_defense_p6": ("Thế trận Phòng thủ Biển Chủ động (Capstone P)", "Đỉnh cao của chiến lược phòng thủ: hệ thống bờ - đảo - ngầm đan xen tạo thành pháo đài thép bất khả xâm phạm."),
        "VIE_nav_greenwater_g3": ("Hải quân Biển gần Tự chủ (Capstone G)", "Hạm đội Green-water hoàn thiện, làm chủ hoàn toàn không gian tác chiến vùng biển đặc quyền kinh tế và các quần đảo."),
        "VIE_nav_bluewater_b3": ("Năng lực Tác chiến Biển xa Bền vững (Capstone B)", "Hải quân viễn dương có khả năng hiện diện thường trực, bảo vệ lợi ích quốc gia và hợp tác an ninh hàng hải quốc tế."),
        "VIE_nav_capstone_integrated_defense_f2": ("Hải quân Chính quy: Pháo đài Thép", "Hải quân nhân dân Việt Nam với thế trận bảo vệ biển đảo kiên cường, giữ vững từng tấc biển thiêng liêng của Tổ quốc."),
        "VIE_nav_capstone_greenwater_f2": ("Hải quân Chính quy: Làm chủ Vùng biển", "Hải quân hiện đại làm chủ vững chắc toàn bộ vùng biển khu vực, cơ động linh hoạt, hỏa lực tập trung và tinh nhuệ."),
        "VIE_nav_capstone_bluewater_f2": ("Hải quân Chính quy: Vươn khơi Đại dương", "Hải quân nhân dân Việt Nam tự tin vươn ra biển lớn, sở hữu hạm đội hùng hậu có khả năng tác chiến viễn dương."),
        "VIE_decision_domestic_corvette_construction_spirit": ("Dự án Đóng tàu Hộ vệ Sông Thu", "Đang tập trung nhân lực và cơ sở hạ tầng đóng mới tàu hộ vệ đa năng theo thiết kế nội địa."),
        "VIE_decision_kilo_sustainment_spirit": ("Duy tu Hạm đội Tàu ngầm Kilo", "Quy trình kiểm định và bảo dưỡng nâng cao tính tàng hình và khả năng bám bắt mục tiêu của tàu ngầm diesel-điện."),
        "VIE_decision_island_bastion_spirit": ("Kiên cố hóa Pháo đài Trường Sa", "Tăng cường năng lực phòng thủ công sự và khả năng chống trả tập kích đường không, đổ bộ đường biển tại các đảo.")
    }

    for sid, (sname, sdesc) in spirit_loc.items():
        out.append(f' {sid}:0 "{sname}"')
        out.append(f' {sid}_desc:0 "{sdesc}"')

    out.append("\n### ============================================================")
    out.append("### QUYẾT ĐỊNH & DANH MỤC HẢI QUÂN V34")
    out.append("### ============================================================\n")

    dec_loc = {
        "VIE_naval_procurement_category": ("Chương trình Mua sắm & Phát triển Hải quân", "Các dự án đầu tư đóng mới, tiếp nhận tàu chiến và kiên cố hóa hạ tầng quốc phòng biển đảo của Hải quân nhân dân Việt Nam."),
        "VIE_decision_molniya_production_run": ("Sản xuất Loạt Tàu tên lửa Molniya", "Cấp ngân sách đóng mới loạt tàu tên lửa tấn công nhanh đề án 1241.8 Molniya trong nước."),
        "VIE_decision_gepard_batch_procurement": ("Tiếp nhận Khinh hạm Gepard 3.9", "Ký kết hợp đồng tiếp nhận và bảo đảm kỹ thuật cho các khinh hạm tàng hình đa nhiệm lớp Gepard 3.9."),
        "VIE_decision_kilo_submarine_sustainment": ("Bảo đảm Kỹ thuật Hạm đội Kilo 636.1", "Đầu tư gói bảo dưỡng định kỳ và đại tu trang thiết bị điện tử, vũ khí cho 6 tàu ngầm Kilo."),
        "VIE_decision_domestic_corvette_lead_ship": ("Khởi đóng Tàu hộ vệ Đa năng Nội địa", "Khởi động dự án đóng mới chiếc tàu hộ vệ săn ngầm dẫn đầu tại Nhà máy Đóng tàu Sông Thu."),
        "VIE_decision_island_bastion_fortification": ("Kiên cố hóa Trận địa Biển đảo", "Đầu tư xây dựng thêm công sự pháo bờ biển và hầm ngầm kiên cố tại các thực thể đảo tiền tiêu.")
    }

    for did, (dname, ddesc) in dec_loc.items():
        out.append(f' {did}:0 "{dname}"')
        out.append(f' {did}_desc:0 "{ddesc}"')

    out.append("\n### Tech bonuses Hải quân V34")
    tech_loc = {
        "VIE_i01_naval_tech": "Nghiên cứu Kỹ thuật Đóng tàu Hải quân",
        "VIE_i02_corvette_tech": "Nghiên cứu Công nghệ Tàu chiến đấu Nhỏ",
        "VIE_i03_naval_electronics": "Nghiên cứu Điện tử & Cảm biến Hạm tàu",
        "VIE_w01_surface_tech": "Nghiên cứu Tàu Chiến đấu Mặt nước",
        "VIE_w04_submarine_tech": "Nghiên cứu Kỹ thuật Tàu ngầm Hiện đại",
        "VIE_i04_corvette_tech": "Nghiên cứu Chế tạo Tàu hộ vệ Nội địa",
        "VIE_w02_missile_boat": "Nghiên cứu Tàu tên lửa Cao tốc",
        "VIE_w03_frigate": "Nghiên cứu Khinh hạm Đa nhiệm",
        "VIE_g02_frigate_tech": "Nghiên cứu Khinh hạm Tàng hình & ASW",
        "VIE_b02_ocean_tech": "Nghiên cứu Kỹ thuật Tác chiến Biển xa"
    }
    for tid, tname in tech_loc.items():
        out.append(f' {tid}:0 "{tname}"')

    return "\n".join(out)

def main():
    print("Generating V34 Vietnamese Navy artifacts...")

    # 1. Focus tree snippet
    focus_snippet = generate_focus_tree_snippet()
    with open("scratch/v34_focus_tree_snippet.txt", "w", encoding="utf-8") as f:
        f.write(focus_snippet)
    print("Saved scratch/v34_focus_tree_snippet.txt")

    # 2. Ideas file
    with open("common/ideas/VIE_md_ideas_v34_navy.txt", "w", encoding="utf-8") as f:
        f.write(IDEAS_CONTENT)
    print("Saved common/ideas/VIE_md_ideas_v34_navy.txt")

    # 3. Decisions file
    with open("common/decisions/VIE_md_decisions_navy.txt", "w", encoding="utf-8") as f:
        f.write(DECISIONS_CONTENT)
    print("Saved common/decisions/VIE_md_decisions_navy.txt")

    # 4. Decision category
    cat_path = "common/decisions/categories/VIE_md_categories.txt"
    with open(cat_path, "r", encoding="utf-8") as f:
        cat_text = f.read()
    if "VIE_naval_procurement_category" not in cat_text:
        new_cat = """
# Chuong trinh Mua sam va Phat trien Hai quan V34
VIE_naval_procurement_category = {
	allowed = { original_tag = VIE }
	priority = 90
	visible = { has_completed_focus = VIE_nav_n00_maritime_strategy_21st }
}
"""
        with open(cat_path, "w", encoding="utf-8") as f:
            f.write(cat_text.strip() + "\n" + new_cat)
        print("Updated common/decisions/categories/VIE_md_categories.txt")
    else:
        print("Category already in VIE_md_categories.txt")

    # 5. Localisation
    loc_snippet = generate_loc_snippet()
    loc_path = "localisation/english/replace/VIE_md_vi_military_l_english.yml"
    with open(loc_path, "r", encoding="utf-8") as f:
        loc_text = f.read()
    
    # Check if already appended
    if "VIE_nav_n00_maritime_strategy_21st" not in loc_text:
        with open(loc_path, "w", encoding="utf-8") as f:
            f.write(loc_text.rstrip() + "\n\n" + loc_snippet + "\n")
        print("Appended V34 localisation to VIE_md_vi_military_l_english.yml")
    else:
        print("Localisation already present in VIE_md_vi_military_l_english.yml")

    # 6. Apply focus snippet to VIE_md_focus.txt
    focus_file = "common/national_focus/VIE_md_focus.txt"
    with open(focus_file, "r", encoding="utf-8") as f:
        focus_lines = f.readlines()

    # Check if V34 already in focus tree
    if any("VIE_nav_n00_maritime_strategy_21st" in line for line in focus_lines):
        print("V34 focuses already in VIE_md_focus.txt")
        return

    # Update header version
    header_idx = -1
    for i, line in enumerate(focus_lines[:30]):
        if "## v36" in line:
            header_idx = i
            break
    
    if header_idx != -1:
        v37_header = "## v37 (10/10/2026): Tai thiet ke toan dien nhanh Hai quan theo de an V34 (40 focus) voi nghe thuat do thi Hinh Qua Tram / Canh Buom (Organic Diamond Flow), truc tam doi xung X=212 tu Y=2 den Y=12. Cay focus: 332 -> 372 focus.\n"
        focus_lines.insert(header_idx, v37_header)
        print("Added v37 header to VIE_md_focus.txt")

    # Find insertion point: "# Nhánh Hải quân & CNQP Hải quân đã được gỡ bỏ"
    insert_idx = -1
    for i, line in enumerate(focus_lines):
        if "Nhánh Hải quân & CNQP Hải quân đã được gỡ bỏ" in line:
            insert_idx = i
            break
    
    if insert_idx == -1:
        # Fallback before VIE_force_47
        for i, line in enumerate(focus_lines):
            if "id = VIE_force_47" in line:
                insert_idx = i - 3
                break

    if insert_idx != -1:
        # Replace the comment line with the focus snippet
        focus_lines[insert_idx] = focus_snippet + "\n"
        with open(focus_file, "w", encoding="utf-8") as f:
            f.writelines(focus_lines)
        print(f"Inserted 40 V34 focuses into VIE_md_focus.txt at line {insert_idx+1}")
    else:
        print("ERROR: Insertion point not found in VIE_md_focus.txt!")

if __name__ == '__main__':
    main()
