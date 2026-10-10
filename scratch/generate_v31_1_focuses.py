# Generator script for V31.1 Land Doctrine focuses

focuses_p = """
	### ======================================================================
	### HOC THUYET P: PHONG THU CHIEN LUOC CHU DONG (6 focus)
	### ======================================================================

	focus = {
		id = VIE_lf_p1_strategic_defense
		icon = GFX_focus_VIE_lf_fs_depth_defence

		x = -6
		y = 1
		relative_position_id = VIE_lf_operational_logistics_maintenance

		cost = 7

		prerequisite = { focus = VIE_lf_operational_logistics_maintenance }
		mutually_exclusive = { focus = VIE_lf_m1_combined_arms_mechanized }
		mutually_exclusive = { focus = VIE_lf_r1_flexible_mobile_warfare }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_p1_strategic_defense"
			add_ideas = VPA_Defensive_Doctrine_1
			VIE_lf_xp_25 = yes
		}
	}

	focus = {
		id = VIE_lf_p2_multi_layered_defense
		icon = GFX_focus_VIE_lf_fs_militia_units

		x = -1
		y = 1
		relative_position_id = VIE_lf_p1_strategic_defense

		cost = 5

		prerequisite = { focus = VIE_lf_p1_strategic_defense }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_p2_multi_layered_defense"
			VIE_lf_xp_20 = yes
			unlock_decision_tooltip = VIE_decision_p_backup_defense_line
		}
	}

	focus = {
		id = VIE_lf_p3_operational_reserves
		icon = GFX_focus_VIE_lf_fs_main_corps

		x = 1
		y = 1
		relative_position_id = VIE_lf_p1_strategic_defense

		cost = 5

		prerequisite = { focus = VIE_lf_p1_strategic_defense }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_p3_operational_reserves"
			VIE_lf_xp_20 = yes
			unlock_decision_tooltip = VIE_decision_p_operational_reserves_boost
		}
	}

	focus = {
		id = VIE_lf_p4_defensive_anti_breakthrough_firepower
		icon = GFX_focus_VIE_lf_arm_arty_org

		x = 0
		y = 1
		relative_position_id = VIE_lf_p2_multi_layered_defense

		cost = 7

		prerequisite = { focus = VIE_lf_p2_multi_layered_defense }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_p4_defensive_anti_breakthrough_firepower"
			VIE_lf_xp_25 = yes
			add_tech_bonus = {
				name = VIE_p4_artillery_bonus
				bonus = 0.5
				uses = 1
				category = CAT_artillery
			}
		}
	}

	focus = {
		id = VIE_lf_p5_protracted_combat_sustainment
		icon = GFX_focus_VIE_lf_dev_territorial

		x = 0
		y = 1
		relative_position_id = VIE_lf_p3_operational_reserves

		cost = 7

		prerequisite = { focus = VIE_lf_p3_operational_reserves }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_p5_protracted_combat_sustainment"
			VIE_lf_xp_25 = yes
			add_command_power = 15
		}
	}

	focus = {
		id = VIE_lf_p6_active_defense_counterattack
		icon = GFX_focus_VIE_lf_cap_area_control

		x = 0
		y = 3
		relative_position_id = VIE_lf_p1_strategic_defense

		cost = 10

		prerequisite = { focus = VIE_lf_p4_defensive_anti_breakthrough_firepower }
		prerequisite = { focus = VIE_lf_p5_protracted_combat_sustainment }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 80
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_p6_active_defense_counterattack"
			VIE_v31_upgrade_defensive_doctrine = yes
			VIE_v31_check_synergy = yes
			VIE_lf_xp_30 = yes
			add_command_power = 20
			unlock_decision_tooltip = VIE_decision_p_local_counterattack
		}
	}
"""

focuses_m = """
	### ======================================================================
	### HOC THUYET M: PHAN CONG CO GIOI HOP THANH (6 focus)
	### ======================================================================

	focus = {
		id = VIE_lf_m1_combined_arms_mechanized
		icon = GFX_focus_VIE_lf_arm_armor_org

		x = 0
		y = 1
		relative_position_id = VIE_lf_operational_logistics_maintenance

		cost = 7

		prerequisite = { focus = VIE_lf_operational_logistics_maintenance }
		mutually_exclusive = { focus = VIE_lf_p1_strategic_defense }
		mutually_exclusive = { focus = VIE_lf_r1_flexible_mobile_warfare }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_m1_combined_arms_mechanized"
			add_ideas = VPA_Mechanized_Doctrine_1
			VIE_lf_xp_25 = yes
		}
	}

	focus = {
		id = VIE_lf_m2_armor_combat_readiness
		icon = GFX_focus_VIE_lf_arm_armor_train

		x = -1
		y = 1
		relative_position_id = VIE_lf_m1_combined_arms_mechanized

		cost = 5

		prerequisite = { focus = VIE_lf_m1_combined_arms_mechanized }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_INDUSTRY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_m2_armor_combat_readiness"
			VIE_lf_xp_20 = yes
			unlock_decision_tooltip = VIE_decision_m_mbt_modernization
		}
	}

	focus = {
		id = VIE_lf_m3_mechanized_infantry_formations
		icon = GFX_focus_VIE_lf_combined_arms

		x = 1
		y = 1
		relative_position_id = VIE_lf_m1_combined_arms_mechanized

		cost = 5

		prerequisite = { focus = VIE_lf_m1_combined_arms_mechanized }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_m3_mechanized_infantry_formations"
			VIE_lf_xp_20 = yes
			unlock_decision_tooltip = VIE_decision_m_combined_arms_deployment
		}
	}

	focus = {
		id = VIE_lf_m4_mobile_fire_support
		icon = GFX_focus_VIE_lf_arm_arty_train

		x = 0
		y = 1
		relative_position_id = VIE_lf_m2_armor_combat_readiness

		cost = 7

		prerequisite = { focus = VIE_lf_m2_armor_combat_readiness }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_m4_mobile_fire_support"
			VIE_lf_xp_25 = yes
			add_tech_bonus = {
				name = VIE_m4_sp_arty_bonus
				bonus = 0.5
				uses = 1
				category = CAT_sp_artillery
			}
		}
	}

	focus = {
		id = VIE_lf_m5_operational_combined_arms_units
		icon = GFX_focus_VIE_lf_fs_lean_corps

		x = 0
		y = 1
		relative_position_id = VIE_lf_m3_mechanized_infantry_formations

		cost = 7

		prerequisite = { focus = VIE_lf_m3_mechanized_infantry_formations }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_m5_operational_combined_arms_units"
			VIE_lf_xp_25 = yes
			add_command_power = 15
		}
	}

	focus = {
		id = VIE_lf_m6_operational_mechanized_counteroffensive
		icon = GFX_focus_VIE_lf_force_complete

		x = 0
		y = 3
		relative_position_id = VIE_lf_m1_combined_arms_mechanized

		cost = 10

		prerequisite = { focus = VIE_lf_m4_mobile_fire_support }
		prerequisite = { focus = VIE_lf_m5_operational_combined_arms_units }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 80
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_m6_operational_mechanized_counteroffensive"
			VIE_v31_upgrade_mechanized_doctrine = yes
			VIE_v31_check_synergy = yes
			VIE_lf_xp_30 = yes
			add_command_power = 20
			unlock_decision_tooltip = VIE_decision_m_counteroffensive_surge
		}
	}
"""

focuses_r = """
	### ======================================================================
	### HOC THUYET R: TAC CHIEN CO DONG LINH HOAT (6 focus)
	### ======================================================================

	focus = {
		id = VIE_lf_r1_flexible_mobile_warfare
		icon = GFX_focus_VIE_lf_fs_mobile_force

		x = 6
		y = 1
		relative_position_id = VIE_lf_operational_logistics_maintenance

		cost = 7

		prerequisite = { focus = VIE_lf_operational_logistics_maintenance }
		mutually_exclusive = { focus = VIE_lf_p1_strategic_defense }
		mutually_exclusive = { focus = VIE_lf_m1_combined_arms_mechanized }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_r1_flexible_mobile_warfare"
			add_ideas = VPA_Mobile_Doctrine_1
			VIE_lf_xp_25 = yes
		}
	}

	focus = {
		id = VIE_lf_r2_modernize_mobile_infantry
		icon = GFX_focus_VIE_lf_arm_infantry_train

		x = -1
		y = 1
		relative_position_id = VIE_lf_r1_flexible_mobile_warfare

		cost = 5

		prerequisite = { focus = VIE_lf_r1_flexible_mobile_warfare }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_r2_modernize_mobile_infantry"
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_r3_terrain_adaptive_warfare
		icon = GFX_focus_VIE_lf_cap_border_urban

		x = 1
		y = 1
		relative_position_id = VIE_lf_r1_flexible_mobile_warfare

		cost = 5

		prerequisite = { focus = VIE_lf_r1_flexible_mobile_warfare }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_r3_terrain_adaptive_warfare"
			VIE_lf_xp_20 = yes
			unlock_decision_tooltip = VIE_decision_r_terrain_mobility_training
		}
	}

	focus = {
		id = VIE_lf_r4_tactical_motorized_mobility
		icon = GFX_focus_VIE_lf_arm_infantry_org

		x = 0
		y = 1
		relative_position_id = VIE_lf_r2_modernize_mobile_infantry

		cost = 7

		prerequisite = { focus = VIE_lf_r2_modernize_mobile_infantry }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_r4_tactical_motorized_mobility"
			VIE_lf_xp_25 = yes
			add_tech_bonus = {
				name = VIE_r4_motorized_bonus
				bonus = 0.5
				uses = 1
				category = CAT_motorized
			}
		}
	}

	focus = {
		id = VIE_lf_r5_rapid_reaction_corps
		icon = GFX_focus_VIE_lf_fs_mobile_corps

		x = 0
		y = 1
		relative_position_id = VIE_lf_r3_terrain_adaptive_warfare

		cost = 7

		prerequisite = { focus = VIE_lf_r3_terrain_adaptive_warfare }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_r5_rapid_reaction_corps"
			VIE_lf_xp_25 = yes
			unlock_decision_tooltip = VIE_decision_r_rapid_readiness_force
		}
	}

	focus = {
		id = VIE_lf_r6_terrain_maneuver_mastery
		icon = GFX_focus_VIE_lf_dev_strategic

		x = 0
		y = 3
		relative_position_id = VIE_lf_r1_flexible_mobile_warfare

		cost = 10

		prerequisite = { focus = VIE_lf_r4_tactical_motorized_mobility }
		prerequisite = { focus = VIE_lf_r5_rapid_reaction_corps }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 80
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_r6_terrain_maneuver_mastery"
			VIE_v31_upgrade_mobile_doctrine = yes
			VIE_v31_check_synergy = yes
			VIE_lf_xp_30 = yes
			add_command_power = 20
			unlock_decision_tooltip = VIE_decision_r_maneuver_tempo_surge
		}
	}
"""

focuses_f = """
	### ======================================================================
	### TRUC F: HIEN DAI HOA VA HOI TU CHI HUY TOAN QUAN (2 focus)
	### ======================================================================

	focus = {
		id = VIE_lf_modernize_army_command_system
		icon = GFX_focus_VIE_lf_command_reform_2

		x = 0
		y = 2
		relative_position_id = VIE_lf_m6_operational_mechanized_counteroffensive

		cost = 7

		prerequisite = {
			focus = VIE_lf_p6_active_defense_counterattack
			focus = VIE_lf_m6_operational_mechanized_counteroffensive
			focus = VIE_lf_r6_terrain_maneuver_mastery
		}

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 85
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_modernize_army_command_system"
			VIE_v31_upgrade_command_integration = yes
			VIE_lf_xp_25 = yes
			add_command_power = 20
		}
	}

	focus = {
		id = VIE_lf_modern_elite_combined_army_capstone
		icon = GFX_focus_VIE_lf_command_reform_3

		x = 0
		y = 1
		relative_position_id = VIE_lf_modernize_army_command_system

		cost = 7

		prerequisite = { focus = VIE_lf_modernize_army_command_system }

		available = {
			has_completed_focus = VIE_lf_active_defense_in_depth
		}

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 90
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_modern_elite_combined_army_capstone"
			set_country_flag = VIE_land_forces_modernized
			VIE_lf_xp_50 = yes
			add_command_power = 30
			add_political_power = 50
		}
	}
"""

full_replacement = focuses_p + focuses_m + focuses_r + focuses_f

focus_file = r'common\national_focus\VIE_md_focus.txt'
with open(focus_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace block from ### TRUC M: LUC LUONG CO GIOI to end of capstone
import re
pattern = re.compile(r'\t### TRUC M: LUC LUONG CO GIOI[\s\S]*?id = VIE_lf_modern_elite_combined_army_capstone[\s\S]*?\n\t\}\n', re.MULTILINE)
m = pattern.search(content)
if not m:
    print('Error: Pattern not found!')
else:
    print(f'Found block to replace: {len(m.group(0))} chars')
    new_content = content[:m.start()] + full_replacement.lstrip('\n') + content[m.end():]
    with open(focus_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Updated VIE_md_focus.txt successfully!')
