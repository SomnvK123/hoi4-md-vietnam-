# -*- coding: utf-8 -*-
"""
Generator & Integrator for V34 Enhanced Naval Effects & Mechanics
"""

import os
import re

# ======================================================================
# 1. SCRIPTED EFFECTS
# ======================================================================
SCRIPTED_EFFECTS = """# ======================================================================
# ĐỀ ÁN V34: HẢI QUÂN NHÂN DÂN VIỆT NAM (SCRIPTED EFFECTS)
# ======================================================================

# --- KIỂM TRA VÀ CẤP NAVAL MASTERY / NAVY XP CHUẨN MD ---

VIE_nav_xp_10 = {
	if = {
		limit = { has_selected_naval_grand_doctrine = yes }
		add_mastery = { amount = 10 folder = naval }
	}
	else = {
		navy_experience = 10
	}
}

VIE_nav_xp_15 = {
	if = {
		limit = { has_selected_naval_grand_doctrine = yes }
		add_mastery = { amount = 15 folder = naval }
	}
	else = {
		navy_experience = 15
	}
}

VIE_nav_xp_20 = {
	if = {
		limit = { has_selected_naval_grand_doctrine = yes }
		add_mastery = { amount = 20 folder = naval }
	}
	else = {
		navy_experience = 20
	}
}

VIE_nav_xp_25 = {
	if = {
		limit = { has_selected_naval_grand_doctrine = yes }
		add_mastery = { amount = 25 folder = naval }
	}
	else = {
		navy_experience = 25
	}
}

VIE_nav_xp_30 = {
	if = {
		limit = { has_selected_naval_grand_doctrine = yes }
		add_mastery = { amount = 30 folder = naval }
	}
	else = {
		navy_experience = 30
	}
}

VIE_nav_xp_35 = {
	if = {
		limit = { has_selected_naval_grand_doctrine = yes }
		add_mastery = { amount = 35 folder = naval }
	}
	else = {
		navy_experience = 35
	}
}

VIE_nav_xp_50 = {
	if = {
		limit = { has_selected_naval_grand_doctrine = yes }
		add_mastery = { amount = 50 folder = naval }
	}
	else = {
		navy_experience = 50
	}
}

# --- NÂNG CẤP TRỤC T: TỔ CHỨC & CHỈ HUY (VPA_Naval_Org: 1 -> 2 -> 3 -> 4) ---

VIE_nav_upgrade_org = {
	if = {
		limit = { has_idea = VPA_Naval_Org_3 }
		swap_ideas = {
			remove_idea = VPA_Naval_Org_3
			add_idea = VPA_Naval_Org_4
		}
	}
	else_if = {
		limit = { has_idea = VPA_Naval_Org_2 }
		swap_ideas = {
			remove_idea = VPA_Naval_Org_2
			add_idea = VPA_Naval_Org_3
		}
	}
	else_if = {
		limit = { has_idea = VPA_Naval_Org_1 }
		swap_ideas = {
			remove_idea = VPA_Naval_Org_1
			add_idea = VPA_Naval_Org_2
		}
	}
	else = {
		add_ideas = VPA_Naval_Org_1
	}
}

# --- NÂNG CẤP TRỤC S: NHẬN THỨC BIỂN MDA (VPA_Maritime_MDA: 1 -> 2 -> 3 -> 4) ---

VIE_nav_upgrade_mda = {
	if = {
		limit = { has_idea = VPA_Maritime_MDA_3 }
		swap_ideas = {
			remove_idea = VPA_Maritime_MDA_3
			add_idea = VPA_Maritime_MDA_4
		}
	}
	else_if = {
		limit = { has_idea = VPA_Maritime_MDA_2 }
		swap_ideas = {
			remove_idea = VPA_Maritime_MDA_2
			add_idea = VPA_Maritime_MDA_3
		}
	}
	else_if = {
		limit = { has_idea = VPA_Maritime_MDA_1 }
		swap_ideas = {
			remove_idea = VPA_Maritime_MDA_1
			add_idea = VPA_Maritime_MDA_2
		}
	}
	else = {
		add_ideas = VPA_Maritime_MDA_1
	}
}

# --- NÂNG CẤP TRỤC L: CĂN CỨ & HẬU CẦN (VPA_Naval_Logistics: 1 -> 2 -> 3 -> 4 -> 5) ---

VIE_nav_upgrade_logistics = {
	if = {
		limit = { has_idea = VPA_Naval_Logistics_4 }
		swap_ideas = {
			remove_idea = VPA_Naval_Logistics_4
			add_idea = VPA_Naval_Logistics_5
		}
	}
	else_if = {
		limit = { has_idea = VPA_Naval_Logistics_3 }
		swap_ideas = {
			remove_idea = VPA_Naval_Logistics_3
			add_idea = VPA_Naval_Logistics_4
		}
	}
	else_if = {
		limit = { has_idea = VPA_Naval_Logistics_2 }
		swap_ideas = {
			remove_idea = VPA_Naval_Logistics_2
			add_idea = VPA_Naval_Logistics_3
		}
	}
	else_if = {
		limit = { has_idea = VPA_Naval_Logistics_1 }
		swap_ideas = {
			remove_idea = VPA_Naval_Logistics_1
			add_idea = VPA_Naval_Logistics_2
		}
	}
	else = {
		add_ideas = VPA_Naval_Logistics_1
	}
}

# --- NÂNG CẤP TRỤC I: CÔNG NGHIỆP ĐÓNG TÀU (VPA_Naval_Industry: 1 -> 2 -> 3 -> 4) ---

VIE_nav_upgrade_industry = {
	if = {
		limit = { has_idea = VPA_Naval_Industry_3 }
		swap_ideas = {
			remove_idea = VPA_Naval_Industry_3
			add_idea = VPA_Naval_Industry_4
		}
	}
	else_if = {
		limit = { has_idea = VPA_Naval_Industry_2 }
		swap_ideas = {
			remove_idea = VPA_Naval_Industry_2
			add_idea = VPA_Naval_Industry_3
		}
	}
	else_if = {
		limit = { has_idea = VPA_Naval_Industry_1 }
		swap_ideas = {
			remove_idea = VPA_Naval_Industry_1
			add_idea = VPA_Naval_Industry_2
		}
	}
	else = {
		add_ideas = VPA_Naval_Industry_1
	}
}

# --- XỬ LÝ PHẦN THƯỞNG CAPSTONE TỐI THƯỢNG F02 ---

VIE_nav_grant_capstone_f2 = {
	if = {
		limit = { has_country_flag = VIE_nav_p_doctrine_completed }
		add_ideas = VIE_nav_capstone_iron_shield
	}
	else_if = {
		limit = { has_country_flag = VIE_nav_g_doctrine_completed }
		add_ideas = VIE_nav_capstone_master_of_seas
	}
	else_if = {
		limit = { has_country_flag = VIE_nav_b_doctrine_completed }
		add_ideas = VIE_nav_capstone_ocean_surge
	}
	else = {
		add_ideas = VIE_nav_capstone_master_of_seas
	}

	# Bonus tự hào công nghiệp đóng tàu nội địa nếu đã hoàn thành I04
	if = {
		limit = { has_completed_focus = VIE_nav_i04_domestic_corvette_class }
		add_ideas = VIE_nav_shipbuilding_mastery
	}
}
"""

# ======================================================================
# 2. IDEAS CONTENT
# ======================================================================
IDEAS_CONTENT = """# ======================================================================
# ĐỀ ÁN V34: HẢI QUÂN NHÂN DÂN VIỆT NAM (NATIONAL SPIRITS & IDEAS)
# ======================================================================

ideas = {
	country = {

		# --- TRỤC T: TỔ CHỨC & CHỈ HUY (TIER 1..4) ---

		VPA_Naval_Org_1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_org = 3
				command_power_gain = 0.05
			}
		}

		VPA_Naval_Org_2 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_org = 5
				experience_gain_navy_factor = 0.10
				navy_leader_start_level = 1
			}
		}

		VPA_Naval_Org_3 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_org = 8
				coastal_defense_coordination = 0.08
				planning_speed = 0.10
			}
		}

		VPA_Naval_Org_4 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_org = 10
				naval_coordination = 0.12
				planning_speed = 0.15
				command_power_gain = 0.10
			}
		}

		# --- TRỤC S: NHẬN THỨC BIỂN MDA (TIER 1..4) ---

		VPA_Maritime_MDA_1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				surface_detection = 0.08
				naval_detection = 0.08
			}
		}

		VPA_Maritime_MDA_2 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				surface_detection = 0.10
				naval_detection = 0.10
				sub_detection = 0.12
				navy_submarine_detection_factor = 0.12
			}
		}

		VPA_Maritime_MDA_3 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				surface_detection = 0.12
				sub_detection = 0.15
				patrol_efficiency = 0.10
				coastal_defense_coordination = 0.10
			}
		}

		VPA_Maritime_MDA_4 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				surface_detection = 0.18
				sub_detection = 0.20
				naval_strike_defense_factor = 0.10
				naval_coordination = 0.10
			}
		}

		# --- TRỤC L: CĂN CỨ & HẬU CẦN (TIER 1..5) ---

		VPA_Naval_Logistics_1 = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				naval_base_efficiency = 0.10
				repair_speed_factor = 0.10
			}
		}

		VPA_Naval_Logistics_2 = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				repair_speed_factor = 0.15
				naval_attrition = -0.10
			}
		}

		VPA_Naval_Logistics_3 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				supply_consumption_factor = -0.10
				repair_speed_factor = 0.15
				navy_max_range_factor = 0.05
			}
		}

		VPA_Naval_Logistics_4 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				repair_speed_factor = 0.20
				convoy_escort_efficiency = 0.10
				escort_efficiency = 0.10
			}
		}

		VPA_Naval_Logistics_5 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.15
				repair_speed_factor = 0.25
				naval_attrition = -0.20
				convoy_escort_efficiency = 0.15
			}
		}

		# --- TRỤC I: CÔNG NGHIỆP ĐÓNG TÀU (TIER 1..4) ---

		VPA_Naval_Industry_1 = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.10
				industrial_capacity_dockyard = 0.05
			}
		}

		VPA_Naval_Industry_2 = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.15
				industrial_capacity_dockyard = 0.08
				research_speed_naval = 0.05
			}
		}

		VPA_Naval_Industry_3 = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.18
				industrial_capacity_dockyard = 0.12
				research_speed_naval = 0.10
			}
		}

		VPA_Naval_Industry_4 = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.20
				industrial_capacity_dockyard = 0.18
				research_speed_naval = 0.15
			}
		}

		# --- KHÍ TÀI ĐỘC BẢN ---

		VIE_nav_surface_fleet_readiness = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.08
				naval_speed_factor = 0.05
			}
		}

		VIE_nav_asw_mastery = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				sub_detection = 0.15
				navy_anti_submarine_attack_factor = 0.15
			}
		}

		VIE_nav_marine_brigades = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				amphibious_defense = 0.20
				naval_org = 5
			}
		}

		# --- HỌC THUYẾT P: PHÒNG THỦ TÍCH HỢP ---

		VPA_Integrated_Defense_Doctrine_1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				coastal_defense_coordination = 0.08
				amphibious_defense = 0.10
				screen_surface_detection = 0.08
			}
		}

		VPA_Integrated_Defense_Doctrine_Capstone = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				coastal_defense_coordination = 0.20
				amphibious_defense = 0.20
				naval_strike_defense_factor = 0.15
				sub_detection = 0.15
				screen_surface_detection = 0.12
			}
		}

		# --- HỌC THUYẾT H & G: GREEN-WATER NAVY ---

		VPA_Fleet_Development_Priority = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.08
				naval_speed_factor = 0.05
			}
		}

		VPA_Multirole_Task_Groups = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.10
				naval_coordination = 0.08
				escort_efficiency = 0.08
			}
		}

		VPA_Greenwater_Doctrine_1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.10
				patrol_efficiency = 0.10
				navy_anti_submarine_attack_factor = 0.10
			}
		}

		VPA_Greenwater_Doctrine_Capstone = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.18
				navy_anti_submarine_attack_factor = 0.18
				escort_efficiency = 0.15
				naval_org = 12
				patrol_efficiency = 0.15
			}
		}

		# --- HỌC THUYẾT B: BLUE-WATER NAVY ---

		VPA_Bluewater_Doctrine_1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.15
				convoy_escort_efficiency = 0.10
				naval_org = 5
			}
		}

		VPA_Bluewater_Doctrine_Capstone = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.25
				convoy_escort_efficiency = 0.20
				naval_coordination = 0.15
				naval_org = 10
				naval_speed_factor = 0.10
			}
		}

		# --- CAPSTONE TỐI THƯỢNG F02 ---

		VIE_nav_capstone_iron_shield = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				naval_strike_defense_factor = 0.20
				amphibious_defense = 0.25
				sub_detection = 0.20
				coastal_defense_coordination = 0.20
				screen_surface_detection = 0.15
			}
		}

		VIE_nav_capstone_master_of_seas = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.20
				navy_anti_submarine_attack_factor = 0.20
				naval_org = 15
				escort_efficiency = 0.20
				patrol_efficiency = 0.15
			}
		}

		VIE_nav_capstone_ocean_surge = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.30
				convoy_escort_efficiency = 0.25
				naval_coordination = 0.20
				naval_org = 15
				naval_speed_factor = 0.12
			}
		}

		VIE_nav_shipbuilding_mastery = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.25
				industrial_capacity_dockyard = 0.20
			}
		}

		# --- TIMED DECISION SPIRITS ---

		VIE_decision_molniya_surge_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.15
				industrial_capacity_dockyard = 0.10
			}
		}

		VIE_decision_gepard_fleet_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				screening_efficiency = 0.12
				naval_speed_factor = 0.05
			}
		}

		VIE_decision_kilo_sustainment_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				sub_detection = 0.15
				sub_visibility = -0.10
			}
		}

		VIE_decision_domestic_corvette_construction_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.20
				industrial_capacity_dockyard = 0.15
			}
		}

		VIE_decision_island_bastion_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_coastal_bunker_factor = 0.25
				amphibious_defense = 0.20
			}
		}

		VIE_decision_asw_combat_drill_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				sub_detection = 0.15
				navy_anti_submarine_attack_factor = 0.15
			}
		}

		VIE_decision_coastal_alert_surge_spirit = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				coastal_defense_coordination = 0.20
				naval_strike_defense_factor = 0.15
			}
		}

	}
}
"""

# ======================================================================
# 3. DECISIONS CONTENT
# ======================================================================
DECISIONS_CONTENT = """# ======================================================================
# ĐỀ ÁN V34: QUYẾT ĐỊNH MUA SẮM VÀ TÁC CHIẾN HẢI QUÂN
# ======================================================================

VIE_naval_procurement_category = {

	# ------------------------------------------------------------------
	# NHÓM 1: CHƯƠNG TRÌNH MUA SẮM & KHÍ TÀI (5 QUYẾT ĐỊNH)
	# ------------------------------------------------------------------

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
			VIE_nav_xp_10 = yes
			add_timed_idea = { idea = VIE_decision_molniya_surge_spirit days = 180 }
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
			VIE_nav_xp_15 = yes
			add_timed_idea = { idea = VIE_decision_gepard_fleet_spirit days = 180 }
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
			801 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }
			add_timed_idea = { idea = VIE_decision_island_bastion_spirit days = 365 }
		}

		ai_will_do = {
			factor = 10
			modifier = { factor = 2 has_war = yes }
		}
	}

	# ------------------------------------------------------------------
	# NHÓM 2: CHIẾN DỊCH TÁC CHIẾN & TUẦN TRA (3 QUYẾT ĐỊNH)
	# ------------------------------------------------------------------

	VIE_decision_scs_joint_patrol_mission = {
		icon = GFX_decision_generic_naval
		cost = 20

		days_remove = 180
		days_re_enable = 180

		visible = {
			has_completed_focus = VIE_nav_s01_maritime_surveillance
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_scs_joint_patrol_mission"
			VIE_nav_xp_15 = yes
			add_command_power = 10
		}

		ai_will_do = {
			factor = 10
		}
	}

	VIE_decision_asw_combat_drill = {
		icon = GFX_decision_generic_naval
		cost = 25

		days_remove = 180
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_s03_subsurface_recon
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_asw_combat_drill"
			VIE_nav_xp_15 = yes
			add_timed_idea = { idea = VIE_decision_asw_combat_drill_spirit days = 180 }
		}

		ai_will_do = {
			factor = 10
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_coastal_alert_surge = {
		icon = GFX_decision_generic_military
		cost = 30

		days_remove = 180
		days_re_enable = 180

		visible = {
			has_completed_focus = VIE_nav_p01_integrated_defense_choice
		}

		available = {
			OR = {
				has_war = yes
				threat > 0.20
			}
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_coastal_alert_surge"
			add_timed_idea = { idea = VIE_decision_coastal_alert_surge_spirit days = 180 }
		}

		ai_will_do = {
			factor = 20
			modifier = { factor = 3 has_war = yes }
		}
	}

}
"""

# ======================================================================
# 4. ENHANCED 40 FOCUS DATA
# ======================================================================
FOCUS_DATA = [
    # Y = 2
    {
        "id": "VIE_nav_n00_maritime_strategy_21st",
        "name": "Chiến lược Biển Việt Nam thế kỷ XXI",
        "desc": "Xác lập định hướng phát triển sức mạnh biển toàn diện, bảo vệ vững chắc chủ quyền biển đảo, thềm lục địa và các lợi ích kinh tế biển của Tổ quốc trong kỷ nguyên mới.",
        "icon": "GFX_focus_VIE_naval_defence_2030",
        "cost": 7,
        "x": 10, "y": 1, "rel": "VIE_modernize_vpa",
        "prereq": ["VIE_modernize_vpa"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_MILITARY_LAWS"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_command_power = 25",
            "add_political_power = 40",
            "set_country_flag = VIE_maritime_strategy_21st_active"
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
        "prereq": ["VIE_nav_n00_maritime_strategy_21st"],
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
        "cost": 5,
        "x": 5, "y": 1, "rel": "VIE_nav_n00_maritime_strategy_21st",
        "prereq": ["VIE_nav_n00_maritime_strategy_21st"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "VIE_nav_upgrade_industry = yes",
            "VIE_ind_prepaid_dockyard = yes",
            "add_tech_bonus = { name = VIE_i01_naval_tech bonus = 0.50 uses = 1 category = CAT_naval }"
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
        "prereq": ["VIE_nav_t01_organization_reform"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "VIE_nav_upgrade_org = yes",
            "navy_leader_start_level = 1"
        ]
    },
    {
        "id": "VIE_nav_t03_regional_commands",
        "name": "Kiện toàn lực lượng các Vùng Hải quân",
        "desc": "Củng cố năng lực chỉ huy tác chiến, phân định rõ khu vực trách nhiệm chiến lược từ Vùng 1 đến Vùng 5, nâng cao khả năng phản ứng cơ động bảo vệ vùng biển chủ quyền.",
        "icon": "GFX_focus_VIE_nf_regional_command",
        "cost": 5,
        "x": 2, "y": 1, "rel": "VIE_nav_t01_organization_reform",
        "prereq": ["VIE_nav_t01_organization_reform"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_command_power = 20",
            "VIE_nav_upgrade_org = yes"
        ]
    },
    {
        "id": "VIE_nav_i02_technology_transfer_molniya",
        "name": "Tiếp nhận công nghệ đóng tàu chiến đấu hiện đại",
        "desc": "Thực hiện thành công chương trình chuyển giao công nghệ đóng tàu tên lửa tấn công nhanh Molniya Project 1241.8 trong nước, tạo bước đột phá về năng lực công nghệ đóng tàu quân sự.",
        "icon": "GFX_focus_VIE_nf_first_force",
        "cost": 5,
        "x": -2, "y": 1, "rel": "VIE_nav_i01_shipbuilding_industry",
        "prereq": ["VIE_nav_i01_shipbuilding_industry"],
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
        "cost": 5,
        "x": 2, "y": 1, "rel": "VIE_nav_i01_shipbuilding_industry",
        "prereq": ["VIE_nav_i01_shipbuilding_industry"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "VIE_nav_upgrade_industry = yes",
            "add_tech_bonus = { name = VIE_i03_naval_electronics bonus = 0.50 uses = 1 category = CAT_naval }"
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
        "prereq": ["VIE_nav_t02_officer_sailor_quality"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_ideas = VIE_nav_surface_fleet_readiness",
            "add_tech_bonus = { name = VIE_w01_surface_tech bonus = 0.50 uses = 1 category = CAT_surface_ships }"
        ]
    },
    {
        "id": "VIE_nav_w04_kilo_submarine_force",
        "name": "Xây dựng lực lượng tàu ngầm hiện đại",
        "desc": "Xây dựng Lữ đoàn 189 tàu ngầm tinh nhuệ, đưa vào vận hành 6 tàu ngầm diesel-điện Kilo 636.1 trang bị tên lửa hành trình Club-S, tạo ra năng lực răn đe ngầm chiến lược dưới lòng biển.",
        "icon": "GFX_focus_VIE_nf_submarine_force",
        "cost": 7,
        "x": 2, "y": 1, "rel": "VIE_nav_t02_officer_sailor_quality",
        "prereq": ["VIE_nav_t02_officer_sailor_quality"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
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
        "prereq": ["VIE_nav_t02_officer_sailor_quality", "VIE_nav_t03_regional_commands"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "add_command_power = 30",
            "VIE_nav_upgrade_org = yes"
        ]
    },
    {
        "id": "VIE_nav_i04_domestic_corvette_class",
        "name": "Phát triển thế hệ tàu hộ vệ do Việt Nam đóng mới",
        "desc": "Triển khai dự án đóng mới lớp tàu hộ vệ săn ngầm và đa năng thế hệ mới tại Nhà máy Sông Thu, khẳng định năng lực tự chủ hoàn toàn kỹ thuật đóng tàu chiến hiện đại của đất nước.",
        "icon": "GFX_focus_VIE_small_combatant_construction",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_i02_technology_transfer_molniya",
        "prereq": ["VIE_nav_i02_technology_transfer_molniya", "VIE_nav_i03_ship_systems_integration"],
        "search_filters": ["FOCUS_FILTER_NAVY", "FOCUS_FILTER_RESEARCH"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "VIE_nav_upgrade_industry = yes",
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
        "prereq": ["VIE_nav_t01_organization_reform"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "VIE_nav_upgrade_mda = yes"
        ]
    },
    {
        "id": "VIE_nav_l01_naval_bases",
        "name": "Hiện đại hóa căn cứ Hải quân",
        "desc": "Nâng cấp cơ sở hạ tầng các quân cảng Cam Ranh, Đà Nẵng, Hải Phòng, Phú Quốc; trang bị cầu cảng hiện đại, trạm nạp nhiên liệu và cơ sở kỹ thuật bảo đảm cho hạm đội.",
        "icon": "GFX_focus_VIE_scs_cam_ranh_port",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_i03_ship_systems_integration",
        "prereq": ["VIE_nav_t01_organization_reform"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_upgrade_logistics = yes",
            "519 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } }",
            "522 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } }"
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
        "prereq": ["VIE_nav_w01_surface_combatants"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
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
        "prereq": ["VIE_nav_w01_surface_combatants"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
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
        "prereq": ["VIE_nav_s01_maritime_surveillance"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "VIE_nav_upgrade_mda = yes",
            "add_tech_bonus = { name = VIE_s03_sonar_tech bonus = 0.50 uses = 1 category = CAT_submarines }"
        ]
    },
    {
        "id": "VIE_nav_s02_island_defense_forces",
        "name": "Củng cố lực lượng bảo vệ đảo",
        "desc": "Tăng cường năng lực tác chiến phòng thủ đảo cho Lữ đoàn 146 và các đơn vị Trường Sa; củng cố công sự, trận địa pháo và các trạm quan sát cảnh giới kiên cố.",
        "icon": "GFX_focus_VIE_scs_spratly_fortification",
        "cost": 5,
        "x": 2, "y": 1, "rel": "VIE_nav_t04_joint_command_system",
        "prereq": ["VIE_nav_s01_maritime_surveillance"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "801 = { add_building_construction = { type = coastal_bunker level = 1 instant_build = yes } }",
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
        "prereq": ["VIE_nav_l01_naval_bases"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "VIE_nav_upgrade_logistics = yes"
        ]
    },
    {
        "id": "VIE_nav_l03_island_logistics",
        "name": "Xây dựng hệ thống hậu cần biển đảo",
        "desc": "Tổ chức tuyến vận tải tiếp tế định kỳ và đột xuất cho các đảo và nhà giàn DK1; nâng cao năng lực dự trữ nước ngọt, lương thực và nhiên liệu trong mọi điều kiện thời tiết.",
        "icon": "GFX_focus_VIE_scs_dk1_platforms",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_i04_domestic_corvette_class",
        "prereq": ["VIE_nav_l01_naval_bases"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "801 = { add_building_construction = { type = radar_station level = 1 instant_build = yes } }",
            "518 = { add_building_construction = { type = naval_base level = 1 instant_build = yes } }",
            "VIE_nav_upgrade_logistics = yes"
        ]
    },
    {
        "id": "VIE_nav_h01_fleet_development_priority",
        "name": "Ưu tiên xây dựng hạm đội tác chiến hiện đại",
        "desc": "Chuyển hướng chiến lược tập trung nguồn lực phát triển các biên đội tàu chiến đấu mặt nước đa năng, sẵn sàng vươn khơi làm chủ các vùng biển khu vực.",
        "icon": "GFX_focus_VIE_nf_greenwater",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_s01_maritime_surveillance",
        "prereq": ["VIE_nav_t04_joint_command_system", "VIE_nav_w01_surface_combatants"],
        "mutually_exclusive": ["VIE_nav_p01_integrated_defense_choice"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_ideas = VPA_Fleet_Development_Priority"
        ]
    },
    {
        "id": "VIE_nav_p01_integrated_defense_choice",
        "name": "Lựa chọn chiến lược phòng thủ biển tích hợp",
        "desc": "Tập trung xây dựng thế trận chống tiếp cận/chống thâm nhập khu vực (A2/AD) nhiều tầng, kết hợp hỏa lực tên lửa bờ biển, tàu ngầm Kilo và hệ thống công sự đảo.",
        "icon": "GFX_focus_VIE_nf_denial",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_l01_naval_bases",
        "prereq": ["VIE_nav_t04_joint_command_system", "VIE_nav_w01_surface_combatants"],
        "mutually_exclusive": ["VIE_nav_h01_fleet_development_priority"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_ideas = VPA_Integrated_Defense_Doctrine_1"
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
        "prereq": ["VIE_nav_w03_multirole_frigates", "VIE_nav_s03_subsurface_recon"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "add_ideas = VIE_nav_asw_mastery",
            "add_tech_bonus = { name = VIE_w05_asw_tech bonus = 0.50 uses = 1 category = CAT_destroyers }"
        ]
    },
    {
        "id": "VIE_nav_s04_joint_island_defense",
        "name": "Hiệp đồng bảo vệ biển đảo",
        "desc": "Tổ chức thế trận hiệp đồng tác chiến chặt chẽ giữa Hải quân, Phòng không - Không quân, Cảnh sát biển, Kiểm ngư và Hải đội Dân quân thường trực.",
        "icon": "GFX_focus_VIE_scs_maritime_militia",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_w03_multirole_frigates",
        "prereq": ["VIE_nav_s02_island_defense_forces", "VIE_nav_s03_subsurface_recon"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_15 = yes",
            "VIE_nav_upgrade_mda = yes"
        ]
    },
    {
        "id": "VIE_nav_l04_support_rescue_vessels",
        "name": "Phát triển lực lượng tàu hỗ trợ và cứu hộ",
        "desc": "Biên chế tàu cứu nạn tàu ngầm đa năng Yết Kiêu 927 và các tàu vận tải tiếp tế thế hệ mới, bảo đảm an toàn tuyệt đối cho hoạt động tác chiến của hạm đội.",
        "icon": "GFX_focus_VIE_nf_replenishment",
        "cost": 5,
        "x": 0, "y": 1, "rel": "VIE_nav_s03_subsurface_recon",
        "prereq": ["VIE_nav_l02_overhaul_maintenance", "VIE_nav_l03_island_logistics"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_10 = yes",
            "VIE_nav_upgrade_logistics = yes"
        ]
    },
    {
        "id": "VIE_nav_p02_coastal_island_network",
        "name": "Xây dựng mạng lưới phòng thủ bờ – đảo",
        "desc": "Liên kết chặt chẽ các trận địa tên lửa phòng thủ bờ biển Bastion-P, Redut-M với các cụm đảo tiền tiêu, hình thành lá chắn hỏa lực bảo vệ vững chắc lãnh hải.",
        "icon": "GFX_focus_VIE_nf_denial_defence",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_l02_overhaul_maintenance",
        "prereq": ["VIE_nav_p01_integrated_defense_choice", "VIE_nav_s02_island_defense_forces"],
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
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_l03_island_logistics",
        "prereq": ["VIE_nav_p01_integrated_defense_choice", "VIE_nav_l03_island_logistics"],
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
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_h01_fleet_development_priority",
        "prereq": ["VIE_nav_h01_fleet_development_priority", "VIE_nav_w03_multirole_frigates", "VIE_nav_l02_overhaul_maintenance"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "add_ideas = VPA_Multirole_Task_Groups"
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
        "prereq": ["VIE_nav_s04_joint_island_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_25 = yes",
            "VIE_nav_upgrade_mda = yes"
        ]
    },
    {
        "id": "VIE_nav_l05_sustained_operations",
        "name": "Nâng cao khả năng duy trì hoạt động dài ngày",
        "desc": "Hoàn thiện quy trình luân phiên lực lượng, tiếp tế cơ động trên biển (RAS) và bảo dưỡng ngoài khơi, giúp tàu chiến có thể bám biển hoạt động liên tục nhiều tháng.",
        "icon": "GFX_focus_VIE_nf_ocean_escort",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_l04_support_rescue_vessels",
        "prereq": ["VIE_nav_l04_support_rescue_vessels"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_20 = yes",
            "VIE_nav_upgrade_logistics = yes"
        ]
    },
    {
        "id": "VIE_nav_p04_layered_defense",
        "name": "Hiện đại hóa năng lực phòng thủ biển nhiều lớp",
        "desc": "Tích hợp tên lửa hành trình chống hạm tầm siêu âm, bãi thủy lôi thông minh và các bệ phóng ngụy trang cơ động, tạo nên thế trận phòng thủ hiểm hóc không thể xuyên phá.",
        "icon": "GFX_focus_VIE_nf_denial_subs",
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_p02_coastal_island_network",
        "prereq": ["VIE_nav_p02_coastal_island_network"],
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
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_p03_island_territory_defense",
        "prereq": ["VIE_nav_h02_multirole_task_groups"],
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
        "cost": 10,
        "x": 0, "y": 1, "rel": "VIE_nav_h02_multirole_task_groups",
        "prereq": ["VIE_nav_h02_multirole_task_groups", "VIE_nav_l05_sustained_operations"],
        "mutually_exclusive": ["VIE_nav_g01_greenwater_navy"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_25 = yes",
            "add_ideas = VPA_Bluewater_Doctrine_1"
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
        "prereq": ["VIE_nav_p03_island_territory_defense", "VIE_nav_p04_layered_defense"],
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
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_p04_layered_defense",
        "prereq": ["VIE_nav_g01_greenwater_navy", "VIE_nav_w05_asw_fleet_defense"],
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
        "cost": 7,
        "x": 0, "y": 1, "rel": "VIE_nav_g01_greenwater_navy",
        "prereq": ["VIE_nav_b01_bluewater_navy", "VIE_nav_s04_joint_island_defense"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_25 = yes",
            "add_tech_bonus = { name = VIE_b02_ocean_tech bonus = 0.50 uses = 1 category = CAT_naval }"
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
        "prereq": ["VIE_nav_p05_joint_coastal_defense"],
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
        "prereq": ["VIE_nav_g02_advanced_frigates_asw", "VIE_nav_l03_island_logistics"],
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
        "prereq": ["VIE_nav_b02_extended_deployment_fleet"],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_35 = yes",
            "swap_ideas = { remove_idea = VPA_Bluewater_Doctrine_1 add_idea = VPA_Bluewater_Doctrine_Capstone }",
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
        "prereq_or": [
            "VIE_nav_p06_active_coastal_defense_capstone",
            "VIE_nav_g03_self_reliant_greenwater_capstone",
            "VIE_nav_b03_sustained_bluewater_capstone"
        ],
        "search_filters": ["FOCUS_FILTER_NAVY"],
        "rewards": [
            "VIE_nav_xp_30 = yes",
            "add_command_power = 35",
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
        "prereq": [
            "VIE_nav_f01_tactical_doctrine_alignment",
            "VIE_nav_s05_unified_maritime_picture",
            "VIE_nav_l05_sustained_operations"
        ],
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

# ======================================================================
# 5. LOCALISATION SNIPPET
# ======================================================================
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
    out.append("### HỆ THỐNG Ý NIỆM TĂNG TIẾN (TIERED SPIRITS) HẢI QUÂN V34")
    out.append("### ============================================================\n")

    spirit_loc = {
        # Trục T
        "VPA_Naval_Org_1": ("Kiện toàn Tổ chức Hải quân (Cấp I)", "Cơ cấu tổ chức và chỉ huy các cấp bước đầu được chuẩn hóa, nâng cao ý thức kỷ luật và chỉ huy điều hành."),
        "VPA_Naval_Org_2": ("Chuẩn hóa Đào tạo Thủy thủ (Cấp II)", "Đội ngũ sĩ quan và thủy thủ được đào tạo bài bản, tăng cường giờ đi biển, nâng cao khả năng tác chiến thực tế."),
        "VPA_Naval_Org_3": ("Kiện toàn 5 Vùng Hải quân (Cấp III)", "Củng cố năng lực chỉ huy và phân định vùng biển chiến lược từ Vùng 1 đến Vùng 5, nâng cao khả năng hiệp đồng khu vực."),
        "VPA_Naval_Org_4": ("Chỉ huy Hiệp đồng Số hóa C4ISR (Cấp IV)", "Mạng lưới truyền tin tác chiến số hóa bảo đảm chỉ huy thông suốt và đồng bộ từ Bộ Tư lệnh tới từng biên đội tàu cơ động."),
        # Trục S
        "VPA_Maritime_MDA_1": ("Cảnh giới Duyên hải (Cấp I)", "Mạng lưới radar trinh sát tầm xa duyên hải cung cấp tham số mục tiêu mặt biển chuẩn xác cho các lực lượng tác chiến."),
        "VPA_Maritime_MDA_2": ("Trinh sát Thủy âm Dưới nước (Cấp II)", "Hệ thống sonar cố định và cơ động nâng cao khả năng phát hiện tàu ngầm và mối đe dọa ngầm dưới lòng biển."),
        "VPA_Maritime_MDA_3": ("Hiệp đồng An ninh Biển đảo (Cấp III)", "Phối hợp chia sẻ dữ liệu mục tiêu nhịp nhàng giữa Hải quân, Cảnh sát biển, Kiểm ngư và Hải đội Dân quân."),
        "VPA_Maritime_MDA_4": ("Nhận thức Biển Thống nhất MDA (Capstone)", "Bức tranh tình huống biển toàn cảnh thời gian thực, liên kết dữ liệu trinh sát đa tầng giúp dẫn đường tên lửa chính xác."),
        # Trục L
        "VPA_Naval_Logistics_1": ("Hạ tầng Quân cảng Căn cứ (Cấp I)", "Quân cảng Cam Ranh, Hải Phòng và các căn cứ duyên hải bảo đảm điều kiện neo đậu, bảo quản và tiếp tế cơ bản."),
        "VPA_Naval_Logistics_2": ("Đại tu Kỹ thuật Nội địa (Cấp II)", "Năng lực tự chủ kiểm định và sửa chữa lớn tàu thuyền trong nước, duy trì hệ số kỹ thuật cao cho hạm đội."),
        "VPA_Naval_Logistics_3": ("Bảo đảm Hậu cần Biển đảo (Cấp III)", "Tuyến vận tải tiếp tế và dự trữ nước ngọt, lương thực, nhiên liệu bảo đảm hoạt động thường trực tại Trường Sa và DK1."),
        "VPA_Naval_Logistics_4": ("Đội tàu Hỗ trợ & Cứu nạn (Cấp IV)", "Tàu cứu nạn chuyên dụng Yết Kiêu và tàu hậu cần đa năng bảo đảm sự an toàn và sức bền chiến đấu của hạm đội."),
        "VPA_Naval_Logistics_5": ("Bám biển Trường kỳ Viễn dương (Capstone)", "Khả năng tiếp tế cơ động trên biển (RAS) giúp biên đội duy trì hiện diện thường trực dài ngày ở các vùng biển xa."),
        # Trục I
        "VPA_Naval_Industry_1": ("Công nghiệp Đóng tàu Quân sự (Cấp I)", "Đầu tư nâng cấp các nhà máy Ba Son, Hồng Hà, Sông Thu, nâng cao năng lực đóng mới và sửa chữa tàu vỏ thép."),
        "VPA_Naval_Industry_2": ("Chuyển giao Công nghệ Tàu chiến (Cấp II)", "Làm chủ quy trình công nghệ chế tạo tàu tên lửa tấn công nhanh Molniya Project 1241.8 theo tiêu chuẩn quốc tế."),
        "VPA_Naval_Industry_3": ("Làm chủ Hệ thống Hạm tàu CMS (Cấp III)", "Tự chủ thiết kế thân vỏ, tích hợp radar dẫn bắn và hệ thống điều khiển chỉ huy chiến đấu hạm tàu CMS."),
        "VPA_Naval_Industry_4": ("Tự chủ Đóng tàu Hộ vệ Đa năng (Capstone)", "Năng lực công nghiệp hoàn thiện cho phép tự chủ đóng mới tàu hộ vệ săn ngầm thế hệ mới do Việt Nam thiết kế."),
        # Khí tài độc bản
        "VIE_nav_surface_fleet_readiness": ("Sẵn sàng Chiến đấu Tàu mặt nước", "Các lữ đoàn tàu tuần tiễu duy trì trạng thái ứng trực chiến đấu 100%, sẵn sàng xuất kích bảo vệ chủ quyền."),
        "VIE_nav_asw_mastery": ("Năng lực Chống ngầm Toàn diện", "Hiệp đồng chặt chẽ giữa tàu hộ vệ và trực thăng săn ngầm Ka-28, kiểm soát hoàn toàn các mối đe dọa dưới nước."),
        "VIE_nav_marine_brigades": ("Lữ đoàn Hải quân Đánh bộ Tinh nhuệ", "Lực lượng Hải quân đánh bộ 101 và 147 được huấn luyện cơ động cao, thiện chiến trong tác chiến đảo và đổ bộ."),
        # Học thuyết P
        "VPA_Integrated_Defense_Doctrine_1": ("Phòng thủ Biển Tích hợp (Giai đoạn I)", "Xây dựng tuyến phòng thủ bờ biển chiều sâu, kết hợp trận địa tên lửa cơ động và chốt chặn đảo."),
        "VPA_Integrated_Defense_Doctrine_Capstone": ("Lưới lửa Phòng thủ Bờ - Đảo (Capstone P)", "Hệ thống A2/AD hoàn chỉnh: tên lửa bờ Bastion-P, tàu ngầm Kilo và công sự đảo tạo thành lá chắn bất khả xâm phạm."),
        # Học thuyết H & G
        "VPA_Fleet_Development_Priority": ("Định hướng Phát triển Hạm đội", "Ưu tiên đầu tư trang bị các lớp tàu chiến đấu mặt nước đa nhiệm có tầm hoạt động lớn và hỏa lực mạnh."),
        "VPA_Multirole_Task_Groups": ("Biên đội Tác chiến Đa nhiệm Hạm đội", "Biên đội khinh hạm hộ vệ kết hợp tàu tên lửa và tàu bảo đảm có khả năng độc lập tác chiến trên biển."),
        "VPA_Greenwater_Doctrine_1": ("Hải quân Biển gần Hiện đại (Green-water I)", "Hạm đội mặt nước cơ động và lực lượng săn ngầm làm chủ hoàn toàn vùng biển đặc quyền kinh tế và thềm lục địa."),
        "VPA_Greenwater_Doctrine_Capstone": ("Hải quân Biển gần Tự chủ (Capstone G)", "Hạm đội Green-water hoàn thiện, bảo vệ trọn vẹn 200 hải lý vùng đặc quyền kinh tế và các tuyến đảo chủ quyền."),
        # Học thuyết B
        "VPA_Bluewater_Doctrine_1": ("Chương trình Hải quân Biển xa (Blue-water I)", "Đặt nền móng kỹ thuật và hậu cần để đưa hạm đội vươn ra các vùng biển quốc tế và bảo vệ các tuyến hàng hải."),
        "VPA_Bluewater_Doctrine_Capstone": ("Hải quân Biển xa Bền vững (Capstone B)", "Hải quân viễn dương có khả năng hiện diện thường trực, bảo vệ lợi ích quốc gia và hợp tác quốc tế trên đại dương."),
        # Capstone F02
        "VIE_nav_capstone_iron_shield": ("Hải quân Chính quy: Lá chắn Thép Biển Đông", "Đỉnh cao của thế trận quốc phòng toàn dân trên biển: từng mét bờ cõi và hòn đảo trở thành pháo đài thép kiên cường."),
        "VIE_nav_capstone_master_of_seas": ("Hải quân Chính quy: Làm chủ Vùng biển Chủ quyền", "Đỉnh cao của hạm đội cơ động hiện đại: làm chủ tuyệt đối vùng biển chủ quyền với sức mạnh tác chiến tinh nhuệ."),
        "VIE_nav_capstone_ocean_surge": ("Hải quân Chính quy: Hùng cường Vươn khơi Đại dương", "Đỉnh cao của hạm đội viễn dương: tự tin vươn ra biển lớn, bảo vệ chủ quyền và lợi ích quốc gia trên các đại dương."),
        "VIE_nav_shipbuilding_mastery": ("Tự chủ Công nghiệp Đóng tàu Chiến lược", "Nền công nghiệp đóng tàu quân sự tự chủ hoàn toàn, đủ sức đóng mới và bảo dưỡng mọi lớp tàu chiến đấu."),
        # Timed spirits
        "VIE_decision_molniya_surge_spirit": ("Cao trào Sản xuất Tàu tên lửa Molniya", "Đẩy nhanh tiến độ đóng mới và bàn giao loạt tàu tên lửa tấn công nhanh Project 1241.8 trong nước."),
        "VIE_decision_gepard_fleet_spirit": ("Nâng cấp Khinh hạm Gepard 3.9", "Tối ưu hóa khả năng tác chiến và tự vệ của các biên đội khinh hạm tàng hình Đinh Tiên Hoàng, Quang Trung."),
        "VIE_decision_kilo_sustainment_spirit": ("Duy tu Kỹ thuật Hạm đội Tàu ngầm Kilo", "Bảo dưỡng chuyên sâu nâng cao độ tĩnh âm và khả năng tác chiến bí mật của 6 tàu ngầm diesel-điện 636.1."),
        "VIE_decision_domestic_corvette_construction_spirit": ("Khởi đóng Tàu hộ vệ Sông Thu Dẫn đầu", "Dự án đóng mới tàu hộ vệ săn ngầm thế hệ mới tại Đà Nẵng đang được tập trung toàn bộ nguồn lực."),
        "VIE_decision_island_bastion_spirit": ("Kiên cố hóa Pháo đài Quần đảo Trường Sa", "Tăng cường năng lực phòng thủ công sự và khả năng chống trả tập kích đường không, đổ bộ đường biển tại các đảo."),
        "VIE_decision_asw_combat_drill_spirit": ("Diễn tập Tác chiến Chống ngầm Hạm đội", "Đợt tập trận săn ngầm liên vùng nâng cao khả năng phát hiện và tiêu diệt tàu ngầm đối phương."),
        "VIE_decision_coastal_alert_surge_spirit": ("Báo động Tác chiến Toàn tuyến Duyên hải", "Toàn bộ các trận địa pháo, tên lửa bờ biển và công sự đảo chuyển sang trạng thái sẵn sàng chiến đấu cao nhất.")
    }

    for sid, (sname, sdesc) in spirit_loc.items():
        out.append(f' {sid}:0 "{sname}"')
        out.append(f' {sid}_desc:0 "{sdesc}"')

    out.append("\n### ============================================================")
    out.append("### QUYẾT ĐỊNH & CHIẾN DỊCH HẢI QUÂN V34")
    out.append("### ============================================================\n")

    dec_loc = {
        "VIE_naval_procurement_category": ("Chương trình Mua sắm & Phát triển Hải quân", "Các dự án đầu tư đóng mới, tiếp nhận tàu chiến và kiên cố hóa hạ tầng quốc phòng biển đảo của Hải quân nhân dân Việt Nam."),
        "VIE_decision_molniya_production_run": ("Sản xuất Loạt Tàu tên lửa Molniya", "Cấp ngân sách đóng mới loạt tàu tên lửa tấn công nhanh đề án 1241.8 Molniya trong nước."),
        "VIE_decision_gepard_batch_procurement": ("Tiếp nhận Khinh hạm Gepard 3.9", "Ký kết hợp đồng tiếp nhận và bảo đảm kỹ thuật cho các khinh hạm tàng hình đa nhiệm lớp Gepard 3.9."),
        "VIE_decision_kilo_submarine_sustainment": ("Bảo đảm Kỹ thuật Hạm đội Kilo 636.1", "Đầu tư gói bảo dưỡng định kỳ và đại tu trang thiết bị điện tử, vũ khí cho 6 tàu ngầm Kilo."),
        "VIE_decision_domestic_corvette_lead_ship": ("Khởi đóng Tàu hộ vệ Đa năng Nội địa", "Khởi động dự án đóng mới chiếc tàu hộ vệ săn ngầm dẫn đầu tại Nhà máy Đóng tàu Sông Thu."),
        "VIE_decision_island_bastion_fortification": ("Kiên cố hóa Trận địa Biển đảo", "Đầu tư xây dựng thêm công sự pháo bờ biển và hầm ngầm kiên cố tại các thực thể đảo tiền tiêu."),
        "VIE_decision_scs_joint_patrol_mission": ("Tuần tra Liên hợp Vùng biển Chủ quyền", "Triển khai các biên đội tuần tra phối hợp bảo vệ an ninh ngư trường và chủ quyền vùng biển."),
        "VIE_decision_asw_combat_drill": ("Diễn tập Hiệp đồng Chống ngầm Hạm đội", "Tổ chức đợt huấn luyện thực binh săn ngầm giữa khinh hạm Gepard và trực thăng Ka-28."),
        "VIE_decision_coastal_alert_surge": ("Kích hoạt Báo động Phòng thủ Duyên hải", "Chuyển trạng thái sẵn sàng chiến đấu cao cho toàn bộ hệ thống tên lửa bờ và công sự đảo.")
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
        "VIE_s03_sonar_tech": "Nghiên cứu Hệ thống Sonar Định vị Thủy âm",
        "VIE_w05_asw_tech": "Nghiên cứu Vũ khí & Khí tài Chống ngầm",
        "VIE_g02_frigate_tech": "Nghiên cứu Khinh hạm Tàng hình & ASW",
        "VIE_b02_ocean_tech": "Nghiên cứu Kỹ thuật Tác chiến Biển xa"
    }
    for tid, tname in tech_loc.items():
        out.append(f' {tid}:0 "{tname}"')

    return "\n".join(out)

def main():
    print("Executing apply_v34_enhanced_effects.py...")

    # 1. Write scripted effects
    with open("common/scripted_effects/VIE_md_effects_v34_navy.txt", "w", encoding="utf-8") as f:
        f.write(SCRIPTED_EFFECTS)
    print("Saved common/scripted_effects/VIE_md_effects_v34_navy.txt")

    # 2. Write ideas
    with open("common/ideas/VIE_md_ideas_v34_navy.txt", "w", encoding="utf-8") as f:
        f.write(IDEAS_CONTENT)
    print("Saved common/ideas/VIE_md_ideas_v34_navy.txt")

    # 3. Write decisions
    with open("common/decisions/VIE_md_decisions_navy.txt", "w", encoding="utf-8") as f:
        f.write(DECISIONS_CONTENT)
    print("Saved common/decisions/VIE_md_decisions_navy.txt")

    # 4. Generate focus tree snippet
    snippet = generate_focus_tree_snippet()
    with open("scratch/v34_focus_tree_snippet.txt", "w", encoding="utf-8") as f:
        f.write(snippet)
    print("Saved scratch/v34_focus_tree_snippet.txt")

    # 5. Replace snippet in VIE_md_focus.txt
    focus_file = "common/national_focus/VIE_md_focus.txt"
    with open(focus_file, "r", encoding="utf-8") as f:
        focus_text = f.read()

    # Find V34 block in focus tree
    start_marker = "## ĐỀ ÁN V34: NHÁNH HẢI QUÂN VIỆT NAM (ORGANIC DIAMOND FLOW - 40 FOCUS)"
    end_marker = "focus = {\n\t\tid = VIE_force_47"

    start_idx = focus_text.find(start_marker)
    end_idx = focus_text.find(end_marker)

    if start_idx != -1 and end_idx != -1:
        # Locate the beginning of the comment line
        line_start = focus_text.rfind("\t", 0, start_idx)
        if line_start == -1:
            line_start = start_idx
        new_focus_text = focus_text[:line_start] + snippet + "\n\n\t" + focus_text[end_idx:]
        with open(focus_file, "w", encoding="utf-8") as f:
            f.write(new_focus_text)
        print("Updated VIE_md_focus.txt with enhanced focus rewards!")
    else:
        print(f"ERROR: Markers not found! start_idx={start_idx}, end_idx={end_idx}")

    # 6. Update localisation file
    loc_file = "localisation/english/replace/VIE_md_vi_military_l_english.yml"
    with open(loc_file, "r", encoding="utf-8") as f:
        loc_text = f.read()

    loc_marker = "### ĐỀ ÁN V34: HẢI QUÂN NHÂN DÂN VIỆT NAM (40 FOCUS V34)"
    loc_idx = loc_text.find(loc_marker)

    loc_snippet = generate_loc_snippet()
    if loc_idx != -1:
        # Replace existing V34 loc block
        new_loc_text = loc_text[:loc_idx].rstrip() + "\n\n" + loc_snippet + "\n"
    else:
        new_loc_text = loc_text.rstrip() + "\n\n" + loc_snippet + "\n"

    with open(loc_file, "w", encoding="utf-8") as f:
        f.write(new_loc_text)
    print("Updated VIE_md_vi_military_l_english.yml with enhanced localisation!")

if __name__ == '__main__':
    main()
