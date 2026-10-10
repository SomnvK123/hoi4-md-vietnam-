import os
import re

# ======================================================================
# 1. CREATE common/ideas/VIE_md_ideas_v32_navy.txt
# ======================================================================

ideas_content = """# ======================================================================
# Y NIEM QUOC GIA HAI QUAN NHAN DAN VIET NAM V32.1 (VPN IDEAS)
# ======================================================================

ideas = {
	country = {
		# ------------------------------------------------------------------
		# NEN TANG SAN SANG CHIEN DAU HAI QUAN (VPA_Naval_Readiness)
		# ------------------------------------------------------------------
		VPA_Naval_Readiness_1 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_org_factor = 0.03
				naval_morale_factor = 0.03
			}
		}

		VPA_Naval_Readiness_2 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_org_factor = 0.05
				naval_morale_factor = 0.05
				experience_gain_navy_factor = 0.05
			}
		}

		VPA_Naval_Readiness_3 = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_org_factor = 0.08
				naval_morale_factor = 0.06
				naval_coordination = 0.05
				experience_gain_navy_factor = 0.08
			}
		}

		# ------------------------------------------------------------------
		# TRUC C: TU CHU DONG TAU QUAN SU
		# ------------------------------------------------------------------
		VIE_naval_shipbuilding_spirit = {
			picture = generic_coastal_navy
			allowed = { original_tag = VIE }
			modifier = {
				industrial_capacity_dockyard = 0.05
				production_speed_dockyard_factor = 0.05
			}
		}

		VIE_naval_shipbuilding_spirit_2 = {
			picture = generic_coastal_navy
			allowed = { original_tag = VIE }
			modifier = {
				industrial_capacity_dockyard = 0.10
				production_speed_dockyard_factor = 0.10
				naval_speed_factor = 0.03
			}
		}

		# ------------------------------------------------------------------
		# TRUC S: NHAN BIET TINH HINH BIEN (MDA)
		# ------------------------------------------------------------------
		VIE_maritime_domain_awareness_spirit = {
			picture = generic_sea_focused_navy
			allowed = { original_tag = VIE }
			modifier = {
				navy_surface_detection_factor = 0.08
				navy_submarine_detection_factor = 0.06
			}
		}

		VIE_maritime_domain_awareness_spirit_2 = {
			picture = generic_sea_focused_navy
			allowed = { original_tag = VIE }
			modifier = {
				navy_surface_detection_factor = 0.15
				navy_submarine_detection_factor = 0.12
				naval_coordination = 0.04
			}
		}

		# ------------------------------------------------------------------
		# TRUC L: DUY TRI HAM DOI & HAU CAN
		# ------------------------------------------------------------------
		VIE_fleet_sustainment_spirit = {
			picture = generic_coastal_defense_ships
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.06
				navy_fuel_consumption_factor = -0.05
			}
		}

		VIE_fleet_sustainment_spirit_2 = {
			picture = generic_coastal_defense_ships
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.12
				navy_fuel_consumption_factor = -0.10
				naval_speed_factor = 0.04
			}
		}

		# ------------------------------------------------------------------
		# HOC THUYET X: SEA DENIAL (KHUOC TU QUYEN SU DUNG BIEN)
		# ------------------------------------------------------------------
		VIE_sea_denial_doctrine_spirit = {
			picture = generic_sub_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_submarine_attack_factor = 0.08
				navy_submarine_detection_factor = 0.08
				navy_screen_defence_factor = 0.05
			}
		}

		VIE_sea_denial_doctrine_spirit_2 = {
			picture = generic_sub_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_submarine_attack_factor = 0.15
				navy_submarine_detection_factor = 0.12
				navy_screen_defence_factor = 0.10
				naval_coordination = 0.05
			}
		}

		# ------------------------------------------------------------------
		# HOC THUYET Y: SEA ASSURANCE (BAO DAM QUYEN SU DUNG BIEN)
		# ------------------------------------------------------------------
		VIE_sea_assurance_doctrine_spirit = {
			picture = generic_escort_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_screen_attack_factor = 0.08
				navy_max_range_factor = 0.08
				naval_morale_factor = 0.05
			}
		}

		VIE_sea_assurance_doctrine_spirit_2 = {
			picture = generic_escort_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_screen_attack_factor = 0.12
				navy_screen_defence_factor = 0.08
				navy_max_range_factor = 0.15
				naval_morale_factor = 0.08
				naval_coordination = 0.06
			}
		}

		# ------------------------------------------------------------------
		# CAPSTONE F02: SUC MANH HAI QUAN BEN VUNG
		# ------------------------------------------------------------------
		VIE_sustainable_naval_combat_power_spirit = {
			picture = generic_naval_manufacturer
			allowed = { original_tag = VIE }
			modifier = {
				navy_org_factor = 0.10
				naval_morale_factor = 0.08
				naval_coordination = 0.08
				navy_anti_air_attack_factor = 0.10
				navy_surface_detection_factor = 0.10
				navy_submarine_detection_factor = 0.10
			}
		}

		# ------------------------------------------------------------------
		# Y NIEM TAM THOI TU QUYET DINH CHIEN DICH (TIMED DECISION MODIFIERS)
		# ------------------------------------------------------------------
		VIE_idea_molniya_production_active = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				production_speed_dockyard_factor = 0.08
				navy_screen_attack_factor = 0.05
			}
		}

		VIE_idea_gepard_batch_active = {
			picture = generic_navy_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_screen_defence_factor = 0.08
				navy_anti_air_attack_factor = 0.08
			}
		}

		VIE_idea_kilo_submarine_active = {
			picture = generic_sub_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_submarine_attack_factor = 0.10
				navy_submarine_detection_factor = 0.05
			}
		}

		VIE_idea_domestic_corvette_active = {
			picture = generic_coastal_navy
			allowed = { original_tag = VIE }
			modifier = {
				industrial_capacity_dockyard = 0.10
			}
		}

		VIE_idea_island_bastion_active = {
			picture = generic_coastal_defense_ships
			allowed = { original_tag = VIE }
			modifier = {
				navy_surface_detection_factor = 0.10
				navy_anti_air_attack_factor = 0.05
			}
		}

		VIE_idea_sea_denial_ambush_active = {
			picture = generic_sub_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_submarine_attack_factor = 0.12
				naval_morale_factor = 0.05
			}
		}

		VIE_idea_coastal_defense_readiness_active = {
			picture = generic_coastal_defense_ships
			allowed = { original_tag = VIE }
			modifier = {
				navy_screen_defence_factor = 0.10
				navy_org_factor = 0.05
			}
		}

		VIE_idea_convoy_protection_active = {
			picture = generic_escort_bonus
			allowed = { original_tag = VIE }
			modifier = {
				navy_screen_defence_factor = 0.08
				naval_coordination = 0.05
			}
		}

		VIE_idea_extended_sea_presence_active = {
			picture = generic_sea_focused_navy
			allowed = { original_tag = VIE }
			modifier = {
				navy_max_range_factor = 0.12
				naval_morale_factor = 0.06
			}
		}
	}
}
"""

with open('common/ideas/VIE_md_ideas_v32_navy.txt', 'w', encoding='utf-8') as f:
    f.write(ideas_content)
print('Created common/ideas/VIE_md_ideas_v32_navy.txt')

# ======================================================================
# 2. CREATE common/decisions/VIE_md_decisions_navy.txt
# ======================================================================

decisions_content = """# ======================================================================
# QUYET DINH CHIEN LUOC & DONG TAU HAI QUAN V32.1
# ======================================================================

VIE_military_readiness_category = {

	# ------------------------------------------------------------------
	# KHÍ TÀI & DỰ ÁN ĐÓNG TÀU CHỦ LỰC
	# ------------------------------------------------------------------

	VIE_decision_molniya_production_run = {
		icon = GFX_decision_generic_naval
		cost = 40

		days_remove = 180
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_w02_missile_boat_modernization
		}

		available = {
			command_power > 20
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_molniya_production_run"
			add_command_power = -20
			set_temp_variable = { treasury_change = -2 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_idea_molniya_production_active days = 180 }
		}

		ai_will_do = {
			factor = 15
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_gepard_batch_procurement = {
		icon = GFX_decision_generic_naval
		cost = 50

		days_remove = 240
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_w03_modern_frigates_in_ranks
		}

		available = {
			command_power > 25
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_gepard_batch_procurement"
			add_command_power = -25
			set_temp_variable = { treasury_change = -3 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_idea_gepard_batch_active days = 240 }
		}

		ai_will_do = {
			factor = 15
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_kilo_submarine_sustainment = {
		icon = GFX_decision_generic_naval
		cost = 45

		days_remove = 180
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_w04_diesel_electric_submarine_power
		}

		available = {
			command_power > 20
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_kilo_submarine_sustainment"
			add_command_power = -20
			set_temp_variable = { treasury_change = -2 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_idea_kilo_submarine_active days = 180 }
		}

		ai_will_do = {
			factor = 15
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_domestic_corvette_lead_ship = {
		icon = GFX_decision_generic_naval
		cost = 50

		days_remove = 240
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_c06_vietnam_corvette_generation
		}

		available = {
			command_power > 25
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_domestic_corvette_lead_ship"
			add_command_power = -25
			set_temp_variable = { treasury_change = -3 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_idea_domestic_corvette_active days = 240 }
		}

		ai_will_do = {
			factor = 15
		}
	}

	VIE_decision_island_bastion_fortification = {
		icon = GFX_decision_generic_fortification
		cost = 35

		days_remove = 180
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_l04_island_maritime_supply_line
		}

		available = {
			command_power > 15
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_island_bastion_fortification"
			add_command_power = -15
			set_temp_variable = { treasury_change = -2 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_idea_island_bastion_active days = 180 }
		}

		ai_will_do = {
			factor = 10
			modifier = { factor = 2 has_war = yes }
		}
	}

	# ------------------------------------------------------------------
	# CHIẾN DỊCH HỌC THUYẾT X (SEA DENIAL)
	# ------------------------------------------------------------------

	VIE_decision_sea_denial_ambush_drills = {
		icon = GFX_decision_generic_naval
		cost = 35

		days_remove = 120
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_x02_force_preservation_under_pressure
		}

		available = {
			command_power > 15
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_sea_denial_ambush_drills"
			add_command_power = -15
			add_timed_idea = { idea = VIE_idea_sea_denial_ambush_active days = 120 }
		}

		ai_will_do = {
			factor = 15
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_coastal_defense_readiness = {
		icon = GFX_decision_generic_fortification
		cost = 45

		days_remove = 180
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_x04_defense_in_depth_maritime
		}

		available = {
			command_power > 20
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_coastal_defense_readiness"
			add_command_power = -20
			add_timed_idea = { idea = VIE_idea_coastal_defense_readiness_active days = 180 }
		}

		ai_will_do = {
			factor = 15
			modifier = { factor = 2 has_war = yes }
		}
	}

	# ------------------------------------------------------------------
	# CHIẾN DỊCH HỌC THUYẾT Y (SEA ASSURANCE)
	# ------------------------------------------------------------------

	VIE_decision_convoy_protection_patrol = {
		icon = GFX_decision_generic_naval
		cost = 35

		days_remove = 120
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_y02_enhance_convoy_escort_efficiency
		}

		available = {
			command_power > 15
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_convoy_protection_patrol"
			add_command_power = -15
			add_timed_idea = { idea = VIE_idea_convoy_protection_active days = 120 }
		}

		ai_will_do = {
			factor = 15
			modifier = { factor = 2 has_war = yes }
		}
	}

	VIE_decision_extended_sea_presence_surge = {
		icon = GFX_decision_generic_naval
		cost = 45

		days_remove = 180
		days_re_enable = 360

		visible = {
			has_completed_focus = VIE_nav_y04_extended_sea_patrol_operations
		}

		available = {
			command_power > 20
		}

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_decision_extended_sea_presence_surge"
			add_command_power = -20
			add_timed_idea = { idea = VIE_idea_extended_sea_presence_active days = 180 }
		}

		ai_will_do = {
			factor = 15
			modifier = { factor = 2 has_war = yes }
		}
	}
}
"""

with open('common/decisions/VIE_md_decisions_navy.txt', 'w', encoding='utf-8') as f:
    f.write(decisions_content)
print('Created common/decisions/VIE_md_decisions_navy.txt')
