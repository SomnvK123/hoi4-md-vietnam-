# -*- coding: utf-8 -*-
import os

focus_data = [
    # ======================================================================
    # TẦNG 1: NỀN TẢNG TỔ CHỨC (5 Focus)
    # ======================================================================
    {
        "id": "VIE_nav_redefine_naval_power",
        "code": "N00",
        "name": "Tái định hình sức mạnh Hải quân Việt Nam",
        "desc": "Trước yêu cầu bảo vệ chủ quyền biển đảo trong thời kỳ mới, Quân chủng Hải quân cần một lộ trình cải cách toàn diện, chuyển trọng tâm từ phòng thủ thụ động sang chủ động làm chủ vùng biển và bảo vệ vững chắc các tuyến đảo tiền tiêu.",
        "icon": "GFX_focus_VIE_naval_defence_law",
        "x": 14, "y": 1, "rel": "VIE_modernize_vpa",
        "cost": 7,
        "prereqs": [["VIE_modernize_vpa"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_redefine_naval_power"
			navy_experience = 25
			add_ideas = VPA_Naval_Readiness_1"""
    },
    {
        "id": "VIE_nav_inventory_fleet_strength",
        "code": "T01",
        "name": "Kiểm kê sức mạnh hạm đội",
        "desc": "Tổng kiểm kê tình trạng kỹ thuật của toàn bộ tàu mặt nước, tàu ngầm và khí tài bờ biển. Phân loại rõ các lớp tàu cần đại tu kéo dài niên hạn và các trang bị cũ cần thay thế.",
        "icon": "GFX_focus_VIE_nf_training_standardization",
        "x": 0, "y": 1, "rel": "VIE_nav_redefine_naval_power",
        "cost": 5,
        "prereqs": [["VIE_nav_redefine_naval_power"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_inventory_fleet_strength"
			navy_experience = 15
			add_command_power = 20"""
    },
    {
        "id": "VIE_nav_sea_days_quality",
        "code": "T02",
        "name": "Nâng cao chất lượng những ngày đi biển",
        "desc": "Tập trung huấn luyện thực chiến đường dài, nâng cao thời gian bám biển liên tục và khả năng làm chủ phương tiện trong điều kiện bão gió khắc nghiệt tại Biển Đông.",
        "icon": "GFX_focus_VIE_nf_operating_range",
        "x": 0, "y": 1, "rel": "VIE_nav_inventory_fleet_strength",
        "cost": 5,
        "prereqs": [["VIE_nav_inventory_fleet_strength"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_sea_days_quality"
			navy_experience = 15
			swap_ideas = { remove_idea = VPA_Naval_Readiness_1 add_idea = VPA_Naval_Readiness_2 }"""
    },
    {
        "id": "VIE_nav_standardize_combat_formations",
        "code": "T03",
        "name": "Chuẩn hóa đội hình chiến đấu",
        "desc": "Xây dựng các biên đội tàu chiến thuật tiêu chuẩn gồm tàu tên lửa, tàu săn ngầm và tàu quét mìn, bảo đảm khả năng hỗ trợ hỏa lực và cảnh giới lẫn nhau khi tác chiến trên biển.",
        "icon": "GFX_focus_VIE_nf_surface_force",
        "x": 0, "y": 1, "rel": "VIE_nav_sea_days_quality",
        "cost": 5,
        "prereqs": [["VIE_nav_sea_days_quality"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_standardize_combat_formations"
			navy_experience = 15
			add_doctrine_cost_reduction = { name = VIE_nav_doctrine_bonus cost_reduction = 0.5 uses = 1 category = naval_doctrine }"""
    },
    {
        "id": "VIE_nav_mission_command_transition",
        "code": "T04",
        "name": "Chuyển đổi sang chỉ huy theo nhiệm vụ",
        "desc": "Phân quyền linh hoạt cho thuyền trưởng và chỉ huy biên đội trên biển, cho phép tự chủ ra quyết định chiến thuật khi đường truyền thông tin liên lạc bị chế áp điện tử.",
        "icon": "GFX_focus_VIE_nf_regional_command",
        "x": 0, "y": 1, "rel": "VIE_nav_standardize_combat_formations",
        "cost": 7,
        "prereqs": [["VIE_nav_standardize_combat_formations"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_mission_command_transition"
			navy_experience = 20
			add_command_power = 30
			swap_ideas = { remove_idea = VPA_Naval_Readiness_2 add_idea = VPA_Naval_Readiness_3 }"""
    },

    # ======================================================================
    # TRỤC C: TỰ CHỦ ĐÓNG TÀU (6 Focus)
    # ======================================================================
    {
        "id": "VIE_nav_c01_restore_naval_shipbuilding",
        "code": "C01",
        "name": "Khôi phục nghề đóng tàu quân sự",
        "desc": "Tập trung đầu tư hạ tầng ụ nổi và xưởng cơ khí chính xác tại Nhà máy Ba Son và Nhà máy X51, tạo nền móng vững chắc cho công nghiệp đóng tàu quân sự độc lập.",
        "icon": "GFX_focus_VIE_ba_son_shipyards",
        "x": -10, "y": 1, "rel": "VIE_nav_mission_command_transition",
        "cost": 5,
        "prereqs": [["VIE_nav_mission_command_transition"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY FOCUS_FILTER_INDUSTRY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_c01_restore_naval_shipbuilding"
			navy_experience = 10
			521 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = { type = dockyard level = 1 instant_build = yes }
			}"""
    },
    {
        "id": "VIE_nav_c02_master_small_hull_construction",
        "code": "C02",
        "name": "Làm chủ kết cấu tàu cỡ nhỏ",
        "desc": "Tự chủ thiết kế và gia công thân vỏ tàu tuần tra, tàu pháo cỡ nhỏ bằng vật liệu thép chuyên dụng và hợp kim nhôm, giảm phụ thuộc vào nhập khẩu từ nước ngoài.",
        "icon": "GFX_focus_VIE_small_combatant_construction",
        "x": 0, "y": 1, "rel": "VIE_nav_c01_restore_naval_shipbuilding",
        "cost": 5,
        "prereqs": [["VIE_nav_c01_restore_naval_shipbuilding"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY FOCUS_FILTER_INDUSTRY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_c02_master_small_hull_construction"
			add_tech_bonus = { name = VIE_small_hull_tech bonus = 0.5 uses = 1 category = CAT_corvettes }
			add_ideas = VIE_naval_shipbuilding_spirit"""
    },
    {
        "id": "VIE_nav_c03_warship_systems_integration",
        "code": "C03",
        "name": "Đội ngũ tích hợp hệ thống tàu chiến",
        "desc": "Đào tạo các kỹ sư và chuyên gia công nghệ có khả năng tích hợp radar, cảm biến điện tử, sonar và bệ phóng tên lửa từ nhiều nguồn khác nhau lên cùng một thân tàu.",
        "icon": "GFX_focus_VIE_naval_systems_integration",
        "x": 0, "y": 1, "rel": "VIE_nav_c02_master_small_hull_construction",
        "cost": 5,
        "prereqs": [["VIE_nav_c02_master_small_hull_construction"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY FOCUS_FILTER_RESEARCH }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_c03_warship_systems_integration"
			navy_experience = 15
			add_tech_bonus = { name = VIE_systems_integration_tech bonus = 0.5 uses = 1 category = electronics }"""
    },
    {
        "id": "VIE_nav_c04_transfer_to_design_improvement",
        "code": "C04",
        "name": "Từ chuyển giao đến cải tiến thiết kế",
        "desc": "Tiếp thu hồ sơ thiết kế tàu chuyển giao từ đối tác quốc tế, từng bước hiệu chỉnh kết cấu và trang bị phù hợp với khí hậu nhiệt đới ẩm và điều kiện tác chiến biển Việt Nam.",
        "icon": "GFX_focus_VIE_naval_mro",
        "x": 0, "y": 1, "rel": "VIE_nav_c03_warship_systems_integration",
        "cost": 7,
        "prereqs": [["VIE_nav_c03_warship_systems_integration"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY FOCUS_FILTER_INDUSTRY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_c04_transfer_to_design_improvement"
			navy_experience = 20
			add_tech_bonus = { name = VIE_frigate_improvement_tech bonus = 0.5 uses = 1 category = CAT_frigates }"""
    },
    {
        "id": "VIE_nav_c05_naval_shipbuilding_ecosystem",
        "code": "C05",
        "name": "Hệ sinh thái đóng tàu quân sự",
        "desc": "Gắn kết các nhà máy đóng tàu quân đội với ngành luyện kim, điện tử viễn thông và cơ khí chế tạo dân sự, tạo chuỗi cung ứng linh kiện nội địa hóa cao cho hải quân.",
        "icon": "naval_industry",
        "x": 0, "y": 1, "rel": "VIE_nav_c04_transfer_to_design_improvement",
        "cost": 7,
        "prereqs": [["VIE_nav_c04_transfer_to_design_improvement"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY FOCUS_FILTER_INDUSTRY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_c05_naval_shipbuilding_ecosystem"
			set_temp_variable = { treasury_change = -3 }
			modify_treasury_effect = yes
			520 = {
				add_extra_state_shared_building_slots = 2
				add_building_construction = { type = dockyard level = 1 instant_build = yes }
			}
			swap_ideas = { remove_idea = VIE_naval_shipbuilding_spirit add_idea = VIE_naval_shipbuilding_spirit_2 }"""
    },
    {
        "id": "VIE_nav_c06_vietnam_corvette_generation",
        "code": "C06",
        "name": "Thế hệ tàu hộ vệ Việt Nam",
        "desc": "Khởi động dự án đóng tàu hộ vệ tên lửa thế hệ mới mang dấu ấn tự chủ công nghệ Việt Nam, mở ra chương trình đóng mới tàu chiến hiện đại tại các nhà máy trong nước.",
        "icon": "GFX_focus_VIE_naval_defence_2030",
        "x": 0, "y": 1, "rel": "VIE_nav_c05_naval_shipbuilding_ecosystem",
        "cost": 7,
        "prereqs": [["VIE_nav_c05_naval_shipbuilding_ecosystem"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY FOCUS_FILTER_INDUSTRY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_c06_vietnam_corvette_generation"
			navy_experience = 25
			custom_effect_tooltip = VIE_unlock_corvette_procurement_tt"""
    },

    # ======================================================================
    # TRỤC S: NHẬN BIẾT TÌNH HÌNH TRÊN BIỂN (5 Focus)
    # ======================================================================
    {
        "id": "VIE_nav_s01_resolve_observation_gaps",
        "code": "S01",
        "name": "Khắc phục khoảng trống quan sát",
        "desc": "Lắp đặt các trạm radar tầm xa và đài quan sát quang điện tử dọc bờ biển và trên các đảo tiền tiêu, xóa bỏ các vùng mù thông tin trên các vùng biển trọng điểm.",
        "icon": "GFX_focus_VIE_scs_law_of_the_sea",
        "x": -5, "y": 1, "rel": "VIE_nav_mission_command_transition",
        "cost": 5,
        "prereqs": [["VIE_nav_mission_command_transition"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY FOCUS_FILTER_RESEARCH }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_s01_resolve_observation_gaps"
			navy_experience = 10
			add_tech_bonus = { name = VIE_radar_observation_tech bonus = 0.5 uses = 1 category = electronics }"""
    },
    {
        "id": "VIE_nav_s02_expand_maritime_patrols",
        "code": "S02",
        "name": "Mở rộng hoạt động tuần thám",
        "desc": "Tăng cường tần suất tuần tra của máy bay tuần thám biển và tàu cảnh giới, duy trì hiện diện quan sát liên tục 24/7 trên các hải trình quốc tế và ngư trường truyền thống.",
        "icon": "GFX_focus_VIE_scs_assert_maritime_rights",
        "x": 0, "y": 1, "rel": "VIE_nav_s01_resolve_observation_gaps",
        "cost": 5,
        "prereqs": [["VIE_nav_s01_resolve_observation_gaps"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_s02_expand_maritime_patrols"
			navy_experience = 15
			add_ideas = VIE_maritime_domain_awareness_spirit"""
    },
    {
        "id": "VIE_nav_s03_upgrade_shipboard_sensors",
        "code": "S03",
        "name": "Nâng cấp cảm biến hạm tàu",
        "desc": "Hiện đại hóa các hệ thống sonar thủy âm thụ động/chủ động và radar bám bắt mục tiêu trên tàu chiến, nâng cao khả năng phát hiện tàu ngầm và tên lửa lướt biển của đối phương.",
        "icon": "GFX_focus_VIE_scs_maritime_militia",
        "x": 0, "y": 1, "rel": "VIE_nav_s02_expand_maritime_patrols",
        "cost": 5,
        "prereqs": [["VIE_nav_s02_expand_maritime_patrols"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY FOCUS_FILTER_RESEARCH }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_s03_upgrade_shipboard_sensors"
			add_tech_bonus = { name = VIE_ship_sensor_tech bonus = 0.5 uses = 1 category = electronics }"""
    },
    {
        "id": "VIE_nav_s04_multi_force_recon_linkage",
        "code": "S04",
        "name": "Kết nối trinh sát đa lực lượng",
        "desc": "Thiết lập mạng lưới chia sẻ dữ liệu mục tiêu tức thời giữa Hải quân, Cảnh sát biển, Không quân và các đài radar trinh sát bờ, tối ưu hóa thời gian phản ứng chiến thuật.",
        "icon": "GFX_focus_VIE_scs_coast_guard_law",
        "x": 0, "y": 1, "rel": "VIE_nav_s03_upgrade_shipboard_sensors",
        "cost": 7,
        "prereqs": [["VIE_nav_s03_upgrade_shipboard_sensors"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_s04_multi_force_recon_linkage"
			navy_experience = 20
			swap_ideas = { remove_idea = VIE_maritime_domain_awareness_spirit add_idea = VIE_maritime_domain_awareness_spirit_2 }"""
    },
    {
        "id": "VIE_nav_s05_unified_maritime_operational_picture",
        "code": "S05",
        "name": "Bức tranh tác chiến biển thống nhất",
        "desc": "Hoàn thiện hệ thống C4ISR biển, hiển thị bức tranh tác chiến thời gian thực trên toàn bộ vùng biển đặc quyền kinh tế và các quần đảo, làm tiền đề vững chắc cho tác chiến hiệp đồng.",
        "icon": "GFX_focus_VIE_scs_maritime_cooperation",
        "x": 0, "y": 1, "rel": "VIE_nav_s04_multi_force_recon_linkage",
        "cost": 7,
        "prereqs": [["VIE_nav_s04_multi_force_recon_linkage"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_s05_unified_maritime_operational_picture"
			navy_experience = 25
			add_political_power = 50
			custom_effect_tooltip = VIE_s05_gateway_tt"""
    },

    # ======================================================================
    # TRỤC W: SỨC MẠNH CHIẾN ĐẤU HẠM ĐỘI (7 Focus)
    # ======================================================================
    {
        "id": "VIE_nav_w01_restore_littoral_combat_power",
        "code": "W01",
        "name": "Khôi phục sức chiến đấu ven bờ",
        "desc": "Đại tu và phục hồi khả năng sẵn sàng chiến đấu cho các đơn vị tàu pháo tuần tiễu và tàu phóng lôi ven bờ, giữ vững an ninh tại các luồng hàng hải nội thủy.",
        "icon": "GFX_focus_VIE_nf_first_force",
        "x": 1, "y": 1, "rel": "VIE_nav_mission_command_transition",
        "cost": 5,
        "prereqs": [["VIE_nav_mission_command_transition"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_w01_restore_littoral_combat_power"
			navy_experience = 15"""
    },
    {
        "id": "VIE_nav_w02_missile_boat_modernization",
        "code": "W02",
        "name": "Đổi mới lực lượng tàu tên lửa",
        "desc": "Triển khai chương trình đóng mới và hiện đại hóa tàu tên lửa tấn công nhanh Molniya (Đề án 1241.8) trang bị 16 tên lửa diệt hạm Uran-E, nâng cao uy lực đột kích trên biển.",
        "icon": "GFX_focus_VIE_nf_greenwater",
        "x": -1, "y": 1, "rel": "VIE_nav_w01_restore_littoral_combat_power",
        "cost": 5,
        "prereqs": [["VIE_nav_w01_restore_littoral_combat_power"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_w02_missile_boat_modernization"
			navy_experience = 15
			custom_effect_tooltip = VIE_unlock_molniya_procurement_tt"""
    },
    {
        "id": "VIE_nav_w03_modern_frigates_in_ranks",
        "code": "W03",
        "name": "Tàu hộ vệ hiện đại vào đội hình",
        "desc": "Đưa các khinh hạm hộ vệ tên lửa tàng hình lớp Gepard 3.9 vào biên chế chiến đấu, tạo quả đấm mặt nước nòng cốt bảo vệ chủ quyền tại quần đảo Trường Sa.",
        "icon": "GFX_focus_VIE_nf_regional_frigates",
        "x": 0, "y": 1, "rel": "VIE_nav_w02_missile_boat_modernization",
        "cost": 7,
        "prereqs": [["VIE_nav_w02_missile_boat_modernization"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_w03_modern_frigates_in_ranks"
			navy_experience = 20
			custom_effect_tooltip = VIE_unlock_gepard_procurement_tt"""
    },
    {
        "id": "VIE_nav_w04_diesel_electric_submarine_power",
        "code": "W04",
        "name": "Năng lực tàu ngầm diesel-điện",
        "desc": "Xây dựng và phát huy tối đa sức mạnh chiến đấu của Lữ đoàn Tàu ngầm 189 với 6 tàu ngầm Kilo 636.1, xác lập năng lực răn đe chiến lược ngầm đầu tiên trong lịch sử hải quân.",
        "icon": "GFX_focus_VIE_nf_submarine_force",
        "x": 2, "y": 1, "rel": "VIE_nav_w01_restore_littoral_combat_power",
        "cost": 7,
        "prereqs": [["VIE_nav_w01_restore_littoral_combat_power"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_w04_diesel_electric_submarine_power"
			navy_experience = 20
			add_tech_bonus = { name = VIE_submarine_tech bonus = 0.5 uses = 1 category = CAT_submarines }
			custom_effect_tooltip = VIE_unlock_kilo_sustainment_tt"""
    },
    {
        "id": "VIE_nav_w05_overcome_asw_limitations",
        "code": "W05",
        "name": "Khắc phục hạn chế chống ngầm",
        "desc": "Trang bị khí tài săn ngầm tiên tiến, kết hợp trực thăng săn ngầm Ka-28 và sonar hạm tàu để chủ động dò tìm, vô hiệu hóa các mối đe dọa tàu ngầm xâm nhập.",
        "icon": "GFX_focus_VIE_nf_naval_aviation",
        "x": -1, "y": 1, "rel": "VIE_nav_w03_modern_frigates_in_ranks",
        "cost": 5,
        "prereqs": [["VIE_nav_w03_modern_frigates_in_ranks"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_w05_overcome_asw_limitations"
			navy_experience = 15
			add_tech_bonus = { name = VIE_asw_tech bonus = 0.5 uses = 1 category = CAT_helicopter_operators }"""
    },
    {
        "id": "VIE_nav_w06_flotilla_air_defense_and_protection",
        "code": "W06",
        "name": "Tự vệ và bảo vệ biên đội tàu",
        "desc": "Bổ sung tổ hợp pháo - tên lửa phòng không hạm tàu Palma và tên lửa tầm gần, thiết lập ô phòng không nhiều tầng che chắn cho biên đội tàu khi tác chiến xa bờ.",
        "icon": "GFX_focus_VIE_nf_ocean_escort",
        "x": 1, "y": 1, "rel": "VIE_nav_w03_modern_frigates_in_ranks",
        "cost": 5,
        "prereqs": [["VIE_nav_w03_modern_frigates_in_ranks"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_w06_flotilla_air_defense_and_protection"
			navy_experience = 15"""
    },
    {
        "id": "VIE_nav_w07_multi_component_force_warfare",
        "code": "W07",
        "name": "Tác chiến lực lượng đa thành phần",
        "desc": "Hợp luyện hiệp đồng chặt chẽ giữa tàu mặt nước, tàu ngầm, không quân hải quân và pháo binh - tên lửa bờ, hoàn thiện sức mạnh chiến đấu tổng hợp và mở ra lựa chọn học thuyết.",
        "icon": "GFX_focus_VIE_nf_medium_force",
        "x": 0, "y": 1, "rel": "VIE_nav_w06_flotilla_air_defense_and_protection",
        "cost": 7,
        "prereqs": [
            ["VIE_nav_w05_overcome_asw_limitations"],
            ["VIE_nav_w06_flotilla_air_defense_and_protection"],
            ["VIE_nav_w04_diesel_electric_submarine_power"]
        ],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_w07_multi_component_force_warfare"
			navy_experience = 25
			custom_effect_tooltip = VIE_w07_doctrine_choice_unlocked_tt"""
    },

    # ======================================================================
    # TRỤC L: DUY TRÌ HẠM ĐỘI (5 Focus)
    # ======================================================================
    {
        "id": "VIE_nav_l01_bases_as_part_of_fleet",
        "code": "L01",
        "name": "Căn cứ là bộ phận của hạm đội",
        "desc": "Coi hệ thống căn cứ quân cảng tại Đà Nẵng, Cam Ranh, Vũng Tàu và Phú Quốc là thành phần hữu cơ của hạm đội, bảo đảm kỹ thuật và hậu cần thông suốt.",
        "icon": "GFX_focus_VIE_nf_replenishment",
        "x": 8, "y": 1, "rel": "VIE_nav_mission_command_transition",
        "cost": 5,
        "prereqs": [["VIE_nav_mission_command_transition"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_l01_bases_as_part_of_fleet"
			navy_experience = 10
			add_ideas = VIE_fleet_sustainment_spirit"""
    },
    {
        "id": "VIE_nav_l02_reliable_overhaul_cycles",
        "code": "L02",
        "name": "Chu kỳ đại tu tin cậy",
        "desc": "Chuẩn hóa quy trình sửa chữa định kỳ, trung tu và đại tu máy móc động cơ tàu, hạn chế tối đa thời gian tàu phải nằm bờ chờ vật tư thay thế.",
        "icon": "GFX_focus_VIE_naval_mro",
        "x": -1, "y": 1, "rel": "VIE_nav_l01_bases_as_part_of_fleet",
        "cost": 5,
        "prereqs": [["VIE_nav_l01_bases_as_part_of_fleet"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_l02_reliable_overhaul_cycles"
			navy_experience = 15"""
    },
    {
        "id": "VIE_nav_l03_fuel_and_material_assurance",
        "code": "L03",
        "name": "Bảo đảm nhiên liệu và vật tư",
        "desc": "Dự trữ chiến lược nhiên liệu tàu chiến và đạn dược tại các kho ngầm ven biển, bảo đảm hạm đội có thể sẵn sàng xuất kích làm nhiệm vụ bất kỳ lúc nào.",
        "icon": "focus_generic_supply_line",
        "x": 1, "y": 1, "rel": "VIE_nav_l01_bases_as_part_of_fleet",
        "cost": 5,
        "prereqs": [["VIE_nav_l01_bases_as_part_of_fleet"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_l03_fuel_and_material_assurance"
			navy_experience = 15"""
    },
    {
        "id": "VIE_nav_l04_island_maritime_supply_line",
        "code": "L04",
        "name": "Duy trì tuyến bảo đảm biển đảo",
        "desc": "Huy động các tàu vận tải quân sự và tàu đổ bộ duy trì cầu hàng hải tiếp tế nước ngọt, lương thực và vật tư quốc phòng cho các điểm đảo Trường Sa.",
        "icon": "GFX_focus_VIE_nf_amphibious_fleet",
        "x": 1, "y": 1, "rel": "VIE_nav_l02_reliable_overhaul_cycles",
        "cost": 5,
        "prereqs": [
            ["VIE_nav_l02_reliable_overhaul_cycles"],
            ["VIE_nav_l03_fuel_and_material_assurance"]
        ],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_l04_island_maritime_supply_line"
			navy_experience = 15
			custom_effect_tooltip = VIE_unlock_island_bastion_tt"""
    },
    {
        "id": "VIE_nav_l05_fleet_operational_readiness_days",
        "code": "L05",
        "name": "Tăng số ngày sẵn sàng hạm đội",
        "desc": "Tối ưu hóa tỷ lệ tàu trực chiến trên biển so với tàu bảo dưỡng trong cảng, bảo đảm hệ số sẵn sàng chiến đấu cao nhất và là điều kiện để đạt capstone hải quân.",
        "icon": "GFX_focus_VIE_nf_lhd_program",
        "x": 0, "y": 1, "rel": "VIE_nav_l04_island_maritime_supply_line",
        "cost": 7,
        "prereqs": [["VIE_nav_l04_island_maritime_supply_line"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_l05_fleet_operational_readiness_days"
			navy_experience = 25
			swap_ideas = { remove_idea = VIE_fleet_sustainment_spirit add_idea = VIE_fleet_sustainment_spirit_2 }
			custom_effect_tooltip = VIE_l05_gateway_tt"""
    },

    # ======================================================================
    # HỌC THUYẾT X: SEA DENIAL (5 Focus)
    # ======================================================================
    {
        "id": "VIE_nav_x01_sea_denial_doctrine_choice",
        "code": "X01",
        "name": "Lựa chọn học thuyết khước từ quyền sử dụng biển",
        "desc": "Xác định triết lý tác chiến cốt lõi là Sea Denial: tập trung ngăn chặn và làm giảm khả năng kiểm soát biển của đối phương bằng tác chiến bất đối xứng và hỏa lực bờ.",
        "icon": "GFX_focus_VIE_nf_denial",
        "x": -3, "y": 1, "rel": "VIE_nav_w07_multi_component_force_warfare",
        "cost": 7,
        "prereqs": [["VIE_nav_w07_multi_component_force_warfare"]],
        "mutex": ["VIE_nav_y01_sea_assurance_doctrine_choice"],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_x01_sea_denial_doctrine_choice"
			navy_experience = 20
			add_ideas = VIE_sea_denial_doctrine_spirit"""
    },
    {
        "id": "VIE_nav_x02_force_preservation_under_pressure",
        "code": "X02",
        "name": "Bảo toàn lực lượng trước sức ép",
        "desc": "Áp dụng chiến thuật cơ động phân tán, tận dụng các luồng lạch, vũng vịnh và đảo đá hiểm trở để ẩn nấp và bảo tồn sức chiến đấu trước hỏa lực vượt trội của đối phương.",
        "icon": "GFX_focus_VIE_nf_denial_defence",
        "x": 0, "y": 1, "rel": "VIE_nav_x01_sea_denial_doctrine_choice",
        "cost": 5,
        "prereqs": [["VIE_nav_x01_sea_denial_doctrine_choice"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_x02_force_preservation_under_pressure"
			navy_experience = 15
			custom_effect_tooltip = VIE_unlock_sea_denial_ambush_tt"""
    },
    {
        "id": "VIE_nav_x03_defensive_information_superiority",
        "code": "X03",
        "name": "Ưu thế thông tin khi phòng thủ",
        "desc": "Khai thác tối đa lợi thế am hiểu địa hình đáy biển và dòng hải lưu ven bờ, duy trì bí mật vị trí và tạo bất ngờ chiến thuật khi triển khai mai phục đối phương.",
        "icon": "GFX_focus_VIE_nf_denial_command",
        "x": 0, "y": 1, "rel": "VIE_nav_x02_force_preservation_under_pressure",
        "cost": 5,
        "prereqs": [["VIE_nav_x02_force_preservation_under_pressure"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_x03_defensive_information_superiority"
			navy_experience = 15
			add_political_power = 40"""
    },
    {
        "id": "VIE_nav_x04_defense_in_depth_maritime",
        "code": "X04",
        "name": "Phòng thủ biển có chiều sâu",
        "desc": "Phối hợp chặt chẽ giữa lưới lôi ngầm, tên lửa bờ Bastion-P và tàu ngầm Kilo, hình thành các tuyến phòng thủ nhiều tầng nấc tiêu hao đối phương từ xa đến gần bờ.",
        "icon": "GFX_focus_VIE_nf_denial_subs",
        "x": 0, "y": 1, "rel": "VIE_nav_x03_defensive_information_superiority",
        "cost": 7,
        "prereqs": [["VIE_nav_x03_defensive_information_superiority"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_x04_defense_in_depth_maritime"
			navy_experience = 20
			custom_effect_tooltip = VIE_unlock_coastal_defense_readiness_tt"""
    },
    {
        "id": "VIE_nav_x05_credible_maritime_deterrence",
        "code": "X05",
        "name": "Năng lực răn đe biển đáng tin cậy",
        "desc": "Hoàn thiện học thuyết khước từ kiểm soát biển, biến vùng nước ven bờ và tiếp giáp lãnh hải thành khu vực có rủi ro cực lớn đối với bất kỳ kẻ thù xâm lược nào.",
        "icon": "GFX_focus_VIE_submarine_cables",
        "x": 0, "y": 1, "rel": "VIE_nav_x04_defense_in_depth_maritime",
        "cost": 7,
        "prereqs": [["VIE_nav_x04_defense_in_depth_maritime"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_x05_credible_maritime_deterrence"
			navy_experience = 25
			swap_ideas = { remove_idea = VIE_sea_denial_doctrine_spirit add_idea = VIE_sea_denial_doctrine_spirit_2 }"""
    },

    # ======================================================================
    # HỌC THUYẾT Y: SEA ASSURANCE (5 Focus)
    # ======================================================================
    {
        "id": "VIE_nav_y01_sea_assurance_doctrine_choice",
        "code": "Y01",
        "name": "Lựa chọn học thuyết bảo đảm quyền sử dụng biển",
        "desc": "Xác định triết lý tác chiến là Sea Assurance: chủ động bảo vệ quyền tự do hàng hải, duy trì hành lang vận tải biển an toàn và bảo vệ các hoạt động kinh tế biển hợp pháp.",
        "icon": "GFX_focus_VIE_nf_bluewater",
        "x": 3, "y": 1, "rel": "VIE_nav_w07_multi_component_force_warfare",
        "cost": 7,
        "prereqs": [["VIE_nav_w07_multi_component_force_warfare"]],
        "mutex": ["VIE_nav_x01_sea_denial_doctrine_choice"],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_y01_sea_assurance_doctrine_choice"
			navy_experience = 20
			add_ideas = VIE_sea_assurance_doctrine_spirit"""
    },
    {
        "id": "VIE_nav_y02_enhance_convoy_escort_efficiency",
        "code": "Y02",
        "name": "Nâng cao hiệu quả hộ tống",
        "desc": "Tổ chức lực lượng hộ tống chuyên trách cho các đoàn tàu vận tải hàng hải và tàu nghiên cứu dầu khí, bảo đảm tuyến đường biển huyết mạch luôn thông suốt.",
        "icon": "GFX_focus_VIE_nf_ocean_escort",
        "x": 0, "y": 1, "rel": "VIE_nav_y01_sea_assurance_doctrine_choice",
        "cost": 5,
        "prereqs": [["VIE_nav_y01_sea_assurance_doctrine_choice"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_y02_enhance_convoy_escort_efficiency"
			navy_experience = 15
			custom_effect_tooltip = VIE_unlock_convoy_protection_tt"""
    },
    {
        "id": "VIE_nav_y03_persistent_maritime_presence",
        "code": "Y03",
        "name": "Hiện diện liên tục trên biển",
        "desc": "Xoay vòng các biên đội tuần tra hiện diện liên tục tại các vùng biển giáp ranh, khẳng định chủ quyền thực tế và ngăn ngừa mọi hành vi đơn phương lấn chiếm.",
        "icon": "GFX_focus_VIE_scs_assert_maritime_rights",
        "x": 0, "y": 1, "rel": "VIE_nav_y02_enhance_convoy_escort_efficiency",
        "cost": 5,
        "prereqs": [["VIE_nav_y02_enhance_convoy_escort_efficiency"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_y03_persistent_maritime_presence"
			navy_experience = 15
			add_political_power = 40"""
    },
    {
        "id": "VIE_nav_y04_extended_sea_patrol_operations",
        "code": "Y04",
        "name": "Bảo đảm hành trình dài ngày",
        "desc": "Nâng cao năng lực hậu cần tiếp tế trên biển, cho phép các khinh hạm thực hiện các chuyến tuần tra tầm xa kéo dài nhiều tuần mà không cần cập cảng tiếp tế.",
        "icon": "GFX_focus_VIE_nf_operating_range",
        "x": 0, "y": 1, "rel": "VIE_nav_y03_persistent_maritime_presence",
        "cost": 7,
        "prereqs": [["VIE_nav_y03_persistent_maritime_presence"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_y04_extended_sea_patrol_operations"
			navy_experience = 20
			custom_effect_tooltip = VIE_unlock_extended_sea_presence_tt"""
    },
    {
        "id": "VIE_nav_y05_secure_vital_maritime_lanes",
        "code": "Y05",
        "name": "Giữ thông suốt các tuyến biển",
        "desc": "Hoàn thiện năng lực bảo đảm an ninh hàng hải trên toàn bộ vùng biển chủ quyền, tạo môi trường biển hòa bình, ổn định và an toàn cho phát triển kinh tế đất nước.",
        "icon": "GFX_focus_VIE_nf_carrier_group",
        "x": 0, "y": 1, "rel": "VIE_nav_y04_extended_sea_patrol_operations",
        "cost": 7,
        "prereqs": [["VIE_nav_y04_extended_sea_patrol_operations"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_y05_secure_vital_maritime_lanes"
			navy_experience = 25
			swap_ideas = { remove_idea = VIE_sea_assurance_doctrine_spirit add_idea = VIE_sea_assurance_doctrine_spirit_2 }"""
    },

    # ======================================================================
    # TẦNG 4: HỘI TỤ CAPSTONE (2 Focus)
    # ======================================================================
    {
        "id": "VIE_nav_f01_doctrine_aligned_navy_formation",
        "code": "F01",
        "name": "Định hình Hải quân theo chiến lược đã lựa chọn",
        "desc": "Tập trung mọi nguồn lực hoàn thiện cơ cấu hạm đội và hệ thống tác chiến theo hướng học thuyết đã được xác lập, bảo đảm tính thống nhất từ chỉ huy đến chiến thuật.",
        "icon": "goal_generic_navy_doctrines_tactics",
        "x": 3, "y": 1, "rel": "VIE_nav_x05_credible_maritime_deterrence",
        "cost": 7,
        "prereqs": [["VIE_nav_x05_credible_maritime_deterrence", "VIE_nav_y05_secure_vital_maritime_lanes"]],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_f01_doctrine_aligned_navy_formation"
			navy_experience = 30
			add_command_power = 40
			add_political_power = 50"""
    },
    {
        "id": "VIE_nav_f02_sustainable_naval_combat_power",
        "code": "F02",
        "name": "Sức mạnh Hải quân bền vững",
        "desc": "Đỉnh cao phát triển của Hải quân Nhân dân Việt Nam: kết hợp nhuần nhuyễn giữa học thuyết tác chiến vững vàng, bức tranh trinh sát toàn diện và năng lực duy trì hạm đội bền bỉ.",
        "icon": "GFX_focus_VIE_modernize_vpa",
        "x": 0, "y": 1, "rel": "VIE_nav_f01_doctrine_aligned_navy_formation",
        "cost": 10,
        "prereqs": [
            ["VIE_nav_f01_doctrine_aligned_navy_formation"],
            ["VIE_nav_s05_unified_maritime_operational_picture"],
            ["VIE_nav_l05_fleet_operational_readiness_days"]
        ],
        "mutex": [],
        "filters": "{ FOCUS_FILTER_NAVY }",
        "reward": """log = "[GetDateText]: [Root.GetName]: Focus VIE_nav_f02_sustainable_naval_combat_power"
			navy_experience = 50
			add_war_support = 0.05
			add_ideas = VIE_sustainable_naval_combat_power_spirit"""
    }
]

print(f'Total naval focuses: {len(focus_data)}')

# Build text block for VIE_md_focus.txt
focus_txt_blocks = []
for f in focus_data:
    block = f"""\tfocus = {{
\t\tid = {f['id']}
\t\ticon = {f['icon']}

\t\tx = {f['x']}
\t\ty = {f['y']}
\t\trelative_position_id = {f['rel']}

\t\tcost = {f['cost']}
"""
    for p in f['prereqs']:
        f_list = " ".join([f"focus = {fid}" for fid in p])
        block += f"\t\tprerequisite = {{ {f_list} }}\n"
    for m in f['mutex']:
        block += f"\t\tmutually_exclusive = {{ focus = {m} }}\n"

    block += f"""\n\t\tsearch_filters = {f['filters']}

\t\tai_will_do = {{
\t\t\tfactor = 10
\t\t}}

\t\tcompletion_reward = {{
\t\t\t{f['reward']}
\t\t}}
\t}}
"""
    focus_txt_blocks.append(block)

with open('scratch/v32_focuses.txt', 'w', encoding='utf-8') as out:
    out.write("\n".join(focus_txt_blocks))
print('Saved scratch/v32_focuses.txt')

# Build localisation entries
loc_lines = []
for f in focus_data:
    loc_lines.append(f' {f["id"]}:0 "{f["name"]}"')
    loc_lines.append(f' {f["id"]}_desc:0 "{f["desc"]}"')

# Also loc for tooltips, decisions, ideas
extra_loc = [
    # Tooltips
    ' VIE_unlock_corvette_procurement_tt:0 "§GMở khóa Quyết định chiến lược:§! §YKhởi đóng tàu hộ vệ nội địa thế hệ mới§!"',
    ' VIE_unlock_molniya_procurement_tt:0 "§GMở khóa Quyết định chiến lược:§! §YĐóng lô tàu tên lửa tấn công nhanh Molniya (Đề án 1241.8)§!"',
    ' VIE_unlock_gepard_procurement_tt:0 "§GMở khóa Quyết định chiến lược:§! §YTiếp nhận tàu hộ vệ tên lửa Gepard 3.9§!"',
    ' VIE_unlock_kilo_sustainment_tt:0 "§GMở khóa Quyết định chiến lược:§! §YBảo dưỡng & vũ trang nâng cấp hạm đội Kilo 636.1§!"',
    ' VIE_unlock_island_bastion_tt:0 "§GMở khóa Quyết định chiến lược:§! §YTăng cường công sự & trạm cảnh giới biển đảo§!"',
    ' VIE_w07_doctrine_choice_unlocked_tt:0 "§GMở khóa Lựa chọn Học thuyết Chiến lược:§! §YSea Denial§! hoặc §YSea Assurance§!"',
    ' VIE_s05_gateway_tt:0 "§GĐạt tiêu chuẩn Nhận biết Tình hình Biển toàn diện§! (Điều kiện mở Capstone cuối §YF02§!)"',
    ' VIE_l05_gateway_tt:0 "§GĐạt tiêu chuẩn Số ngày Sẵn sàng Hạm đội cao§! (Điều kiện mở Capstone cuối §YF02§!)"',
    ' VIE_unlock_sea_denial_ambush_tt:0 "§GMở khóa Quyết định chiến dịch:§! §YDiễn tập phục kích ngầm & phân tán lực lượng§!"',
    ' VIE_unlock_coastal_defense_readiness_tt:0 "§GMở khóa Quyết định chiến dịch:§! §YSẵn sàng lưới lửa bờ biển A2/AD§!"',
    ' VIE_unlock_convoy_protection_tt:0 "§GMở khóa Quyết định chiến dịch:§! §YTuần tra bảo vệ tuyến vận tải biển§!"',
    ' VIE_unlock_extended_sea_presence_tt:0 "§GMở khóa Quyết định chiến dịch:§! §YChiến dịch hiện diện dài ngày trên biển§!"',
    
    # Decisions
    ' VIE_decision_molniya_production_run:0 "Đóng lô tàu tên lửa Molniya (Đề án 1241.8)"',
    ' VIE_decision_molniya_production_run_desc:0 "Khởi đóng lô tàu tên lửa tấn công nhanh Molniya tại Nhà máy Ba Son nhằm tăng cường mật độ hỏa lực chống hạm ven bờ."',
    ' VIE_decision_gepard_batch_procurement:0 "Tiếp nhận tàu hộ vệ tên lửa Gepard 3.9"',
    ' VIE_decision_gepard_batch_procurement_desc:0 "Thực hiện hợp đồng chuyển giao tàu hộ vệ tên lửa Gepard 3.9, gia tăng đáng kể sức mạnh săn ngầm và phòng không hạm đội."',
    ' VIE_decision_kilo_submarine_sustainment:0 "Bảo dưỡng & vũ trang nâng cấp hạm đội Kilo 636.1"',
    ' VIE_decision_kilo_submarine_sustainment_desc:0 "Đại tu trang thiết bị âm học, bảo dưỡng ắc-quy và bổ sung cơ số tên lửa hành trình Klub-S cho các tàu ngầm Kilo."',
    ' VIE_decision_domestic_corvette_lead_ship:0 "Khởi đóng tàu hộ vệ nội địa thế hệ mới"',
    ' VIE_decision_domestic_corvette_lead_ship_desc:0 "Chính thức đặt ky đóng chiếc tàu hộ vệ đầu tiên do kỹ sư Việt Nam tự chủ thiết kế và tích hợp hệ thống vũ khí hiện đại."',
    ' VIE_decision_island_bastion_fortification:0 "Tăng cường công sự & trạm cảnh giới biển đảo"',
    ' VIE_decision_island_bastion_fortification_desc:0 "Gia cố công sự phòng thủ, lắp đặt đài radar và trạm quan sát thủy âm tại các đảo trọng điểm nhằm tạo mạng lưới cảnh giới liên hoàn."',
    ' VIE_decision_sea_denial_ambush_drills:0 "Diễn tập phục kích ngầm & phân tán lực lượng"',
    ' VIE_decision_sea_denial_ambush_drills_desc:0 "Tổ chức diễn tập tác chiến bất đối xứng, rèn luyện kỹ năng ngụy trang và bí mật phục kích tiêu hao đối phương."',
    ' VIE_decision_coastal_defense_readiness:0 "Sẵn sàng lưới lửa bờ biển A2/AD"',
    ' VIE_decision_coastal_defense_readiness_desc:0 "Đặt các lữ đoàn tên lửa bờ và trận địa pháo ven biển vào trạng thái sẵn sàng chiến đấu cao nhất."',
    ' VIE_decision_convoy_protection_patrol:0 "Tuần tra bảo vệ tuyến vận tải biển"',
    ' VIE_decision_convoy_protection_patrol_desc:0 "Điều động các biên đội khinh hạm hộ tống các đoàn tàu hàng và bảo đảm an toàn cho các tuyến hàng hải thiết yếu."',
    ' VIE_decision_extended_sea_presence_surge:0 "Chiến dịch hiện diện dài ngày trên biển"',
    ' VIE_decision_extended_sea_presence_surge_desc:0 "Tổ chức đợt tuần tra dài ngày liên tục tại các vùng biển xa, khẳng định chủ quyền và bảo vệ hoạt động khai thác tài nguyên biển."',

    # Ideas
    ' VPA_Naval_Readiness_1:0 "Sẵn sàng Chiến đấu Hải quân (Bậc 1)"',
    ' VPA_Naval_Readiness_1_desc:0 "Giai đoạn khởi đầu kiện toàn tổ chức và nâng cao kỷ luật sẵn sàng chiến đấu trong toàn Quân chủng Hải quân."',
    ' VPA_Naval_Readiness_2:0 "Sẵn sàng Chiến đấu Hải quân (Bậc 2)"',
    ' VPA_Naval_Readiness_2_desc:0 "Tăng cường thời gian huấn luyện thực tế trên biển, nâng cao năng lực chịu sóng gió và làm chủ trang thiết bị hạm tàu."',
    ' VPA_Naval_Readiness_3:0 "Sẵn sàng Chiến đấu Hải quân (Bậc 3)"',
    ' VPA_Naval_Readiness_3_desc:0 "Chỉ huy tác chiến linh hoạt theo nhiệm vụ, bảo đảm hạm đội hoạt động đồng bộ và hiệu quả trong mọi tình huống."',
    ' VIE_naval_shipbuilding_spirit:0 "Tự chủ Đóng tàu Quân sự (Bậc 1)"',
    ' VIE_naval_shipbuilding_spirit_desc:0 "Bước đầu làm chủ quy trình chế tạo thân vỏ tàu cỡ nhỏ và tích hợp trang thiết bị điện tử cơ bản."',
    ' VIE_naval_shipbuilding_spirit_2:0 "Hệ sinh thái Đóng tàu Quân sự (Bậc 2)"',
    ' VIE_naval_shipbuilding_spirit_2_desc:0 "Hình thành chuỗi liên kết công nghiệp hoàn chỉnh, cho phép đóng mới và cải tiến các lớp tàu chiến hiện đại."',
    ' VIE_maritime_domain_awareness_spirit:0 "Nhận biết Tình hình Biển (Bậc 1)"',
    ' VIE_maritime_domain_awareness_spirit_desc:0 "Mở rộng mạng lưới trạm quan sát và tuần tra biển, giảm thiểu các vùng mù radar."',
    ' VIE_maritime_domain_awareness_spirit_2:0 "Bức tranh Tác chiến Biển Thống nhất (Bậc 2)"',
    ' VIE_maritime_domain_awareness_spirit_2_desc:0 "Mạng lưới C4ISR biển hợp nhất, truyền dữ liệu thời gian thực giữa mọi lực lượng bảo vệ biển đảo."',
    ' VIE_fleet_sustainment_spirit:0 "Duy trì Hạm đội (Bậc 1)"',
    ' VIE_fleet_sustainment_spirit_desc:0 "Cải thiện công tác bảo đảm hậu cần, vật tư kỹ thuật và quy trình sửa chữa tại các quân cảng."',
    ' VIE_fleet_sustainment_spirit_2:0 "Sẵn sàng Hạm đội Bền bỉ (Bậc 2)"',
    ' VIE_fleet_sustainment_spirit_2_desc:0 "Tối ưu hóa chu kỳ sửa chữa và dự trữ hậu cần, nâng cao tỷ lệ tàu trực chiến dài ngày trên biển."',
    ' VIE_sea_denial_doctrine_spirit:0 "Học thuyết Khước từ Kiểm soát Biển (Bậc 1)"',
    ' VIE_sea_denial_doctrine_spirit_desc:0 "Tập trung tác chiến bất đối xứng, phục kích ngầm và tận dụng địa hình biển đảo để tiêu hao đối phương."',
    ' VIE_sea_denial_doctrine_spirit_2:0 "Khước từ Kiểm soát Biển Toàn diện (Bậc 2)"',
    ' VIE_sea_denial_doctrine_spirit_2_desc:0 "Lưới lửa phòng thủ nhiều tầng kết hợp răn đe ngầm hiệu quả cao, biến vùng biển thành khu vực nguy hiểm chết người đối với đối phương."',
    ' VIE_sea_assurance_doctrine_spirit:0 "Học thuyết Bảo đảm Quyền Sử dụng Biển (Bậc 1)"',
    ' VIE_sea_assurance_doctrine_spirit_desc:0 "Chủ động hộ tống, duy trì hiện diện và bảo vệ các tuyến giao thông biển huyết mạch."',
    ' VIE_sea_assurance_doctrine_spirit_2:0 "Bảo đảm Quyền Sử dụng Biển Toàn diện (Bậc 2)"',
    ' VIE_sea_assurance_doctrine_spirit_2_desc:0 "Năng lực tuần tra viễn hải và bảo vệ vững chắc mọi hoạt động kinh tế biển, ngư trường và tuyến hàng hải quốc tế."',
    ' VIE_sustainable_naval_combat_power_spirit:0 "Sức mạnh Hải quân Bền vững"',
    ' VIE_sustainable_naval_combat_power_spirit_desc:0 "Đỉnh cao phát triển của Hải quân Việt Nam: hạm đội hiện đại, trinh sát toàn diện, hậu cần vững chắc và học thuyết tác chiến sắc bén."',
    ' VIE_idea_molniya_production_active:0 "Đóng mới Tàu tên lửa Molniya"',
    ' VIE_idea_molniya_production_active_desc:0 "Dự án thi công lô tàu tên lửa Molniya đang được khẩn trương triển khai tại nhà máy đóng tàu."',
    ' VIE_idea_gepard_batch_active:0 "Tiếp nhận Tàu hộ vệ Gepard 3.9"',
    ' VIE_idea_gepard_batch_active_desc:0 "Đang thực hiện công tác tiếp nhận, huấn luyện kíp tàu và trang bị kỹ thuật cho tàu hộ vệ mới."',
    ' VIE_idea_kilo_submarine_active:0 "Hiện đại hóa Tàu ngầm Kilo"',
    ' VIE_idea_kilo_submarine_active_desc:0 "Chương trình nâng cấp âm học và vũ khí cho lực lượng tàu ngầm đang diễn ra theo kế hoạch."',
    ' VIE_idea_domestic_corvette_active:0 "Dự án Tàu hộ vệ Nội địa"',
    ' VIE_idea_domestic_corvette_active_desc:0 "Các kỹ sư quân sự đang dồn lực chế tạo mẫu tàu hộ vệ mang công nghệ tự chủ của Việt Nam."',
    ' VIE_idea_island_bastion_active:0 "Củng cố Tuyến phòng thủ Biển đảo"',
    ' VIE_idea_island_bastion_active_desc:0 "Công tác tăng cường công sự và khí tài quan sát tại các điểm đảo đang được đẩy mạnh."',
    ' VIE_idea_sea_denial_ambush_active:0 "Diễn tập Phục kích Ngầm"',
    ' VIE_idea_sea_denial_ambush_active_desc:0 "Lực lượng tàu ngầm và tàu tấn công nhanh đang thực hiện đợt diễn tập phục kích chiến thuật trên biển."',
    ' VIE_idea_coastal_defense_readiness_active:0 "Lưới lửa Bờ biển Sẵn sàng"',
    ' VIE_idea_coastal_defense_readiness_active_desc:0 "Các đơn vị tên lửa bờ và pháo binh ven biển duy trì trạng thái báo động chiến đấu cao."',
    ' VIE_idea_convoy_protection_active:0 "Chiến dịch Hộ tống Hàng hải"',
    ' VIE_idea_convoy_protection_active_desc:0 "Hải đội tàu hộ vệ đang triển khai tuần tra bảo vệ an toàn cho các đoàn tàu vận tải."',
    ' VIE_idea_extended_sea_presence_active:0 "Hiện diện Biển xa"',
    ' VIE_idea_extended_sea_presence_active_desc:0 "Hạm đội đang thực hiện chuyến hành trình dài ngày khẳng định chủ quyền tại vùng biển đặc quyền kinh tế."'
]

with open('scratch/v32_loc.txt', 'w', encoding='utf-8') as out:
    out.write("\n".join(loc_lines + extra_loc))
print('Saved scratch/v32_loc.txt')
