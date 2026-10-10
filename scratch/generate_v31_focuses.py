# -*- coding: utf-8 -*-
"""
Script tao toan bo 49 focus moi va cap nhat VIE_modernize_vpa cho De an V31
"""

def generate_focuses():
    return """
	###############################
	## DE AN V31: QUAN SU TOAN QUAN & LUC QUAN VIET NAM
	###############################

	# -------------------------------------------------------------
	# PHAN 1: CAI CACH VA CONG NGHIEP CAP TOAN QUAN (14 focus)
	# -------------------------------------------------------------

	### TRUC C: CAI CACH TO CHUC VA CHUYEN NGHIEP HOA (4 focus)
	focus = {
		id = VIE_mil_org_structure_review
		icon = GFX_focus_VIE_lf_army_reform

		x = -11
		y = 1
		relative_position_id = VIE_modernize_vpa

		cost = 5

		prerequisite = { focus = VIE_modernize_vpa }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_POLITICAL }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_org_structure_review"
			VIE_lf_xp_10 = yes
			add_political_power = 25
		}
	}

	focus = {
		id = VIE_mil_lean_efficient_force
		icon = GFX_focus_VIE_lf_fs_lean_corps

		x = -1
		y = 1
		relative_position_id = VIE_mil_org_structure_review

		cost = 7

		prerequisite = { focus = VIE_mil_org_structure_review }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_lean_efficient_force"
			VIE_lf_xp_15 = yes
			add_command_power = 15
		}
	}

	focus = {
		id = VIE_mil_professional_cadre
		icon = GFX_focus_VIE_lf_basic_training

		x = 1
		y = 1
		relative_position_id = VIE_mil_org_structure_review

		cost = 5

		prerequisite = { focus = VIE_mil_org_structure_review }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_professional_cadre"
			VIE_lf_xp_10 = yes
			add_command_power = 10
		}
	}

	focus = {
		id = VIE_mil_academies_and_training
		icon = GFX_focus_VIE_research_universities

		x = 0
		y = 2
		relative_position_id = VIE_mil_org_structure_review

		cost = 7

		prerequisite = { focus = VIE_mil_lean_efficient_force }
		prerequisite = { focus = VIE_mil_professional_cadre }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_academies_and_training"
			VIE_lf_xp_20 = yes
			add_command_power = 15
		}
	}

	### TRUC Q: HIEP DONG QUAN SU CAP TOAN QUAN (2 focus)
	focus = {
		id = VIE_mil_joint_command_system
		icon = GFX_focus_VIE_lf_command_reform_1

		x = 0
		y = 1
		relative_position_id = VIE_mil_academies_and_training

		cost = 7

		prerequisite = { focus = VIE_mil_academies_and_training }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_NAVY FOCUS_FILTER_AIR_FORCE }

		ai_will_do = {
			base = 75
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_joint_command_system"
			VIE_v31_upgrade_command_integration = yes
			add_command_power = 20
		}
	}

	focus = {
		id = VIE_mil_modern_joint_autonomous_vpa
		icon = GFX_focus_VIE_lf_force_complete

		x = 0
		y = 1
		relative_position_id = VIE_mil_joint_command_system

		cost = 7

		prerequisite = { focus = VIE_mil_joint_command_system }

		available = {
			VIE_v31_joint_modernization_ready = yes
		}

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_NAVY FOCUS_FILTER_AIR_FORCE }

		ai_will_do = {
			base = 85
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_modern_joint_autonomous_vpa"
			add_ideas = VIE_vpa_modern_joint_autonomous_idea
			VIE_lf_xp_50 = yes
			add_command_power = 30
			add_political_power = 50
		}
	}

	### TRUC I: CONG NGHIEP QUOC PHONG VA NGUON CUNG (7 focus)
	focus = {
		id = VIE_mil_ind_consolidation
		icon = GFX_focus_VIE_def_industry_law

		x = -7
		y = 1
		relative_position_id = VIE_modernize_vpa

		cost = 5

		prerequisite = { focus = VIE_modernize_vpa }

		search_filters = { FOCUS_FILTER_INDUSTRY FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_ind_consolidation"
			VIE_v31_upgrade_industrial_sustainment = yes
			add_political_power = 25
		}
	}

	focus = {
		id = VIE_mil_ind_mro_upgrade
		icon = GFX_focus_VIE_lf_logistics_merge

		x = -1
		y = 1
		relative_position_id = VIE_mil_ind_consolidation

		cost = 7

		prerequisite = { focus = VIE_mil_ind_consolidation }

		search_filters = { FOCUS_FILTER_INDUSTRY FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_ind_mro_upgrade"
			VIE_v31_upgrade_industrial_sustainment = yes
			VIE_lf_xp_15 = yes
		}
	}

	focus = {
		id = VIE_mil_ind_infantry_weapons_z111
		icon = GFX_focus_VIE_lf_arm_infantry_org

		x = 1
		y = 1
		relative_position_id = VIE_mil_ind_consolidation

		cost = 5

		prerequisite = { focus = VIE_mil_ind_consolidation }

		search_filters = { FOCUS_FILTER_INDUSTRY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_ind_infantry_weapons_z111"
			add_tech_bonus = {
				name = VIE_z111_infantry_weapons_bonus
				bonus = 0.5
				uses = 1
				category = CAT_infantry_weapons
			}
			VIE_lf_xp_10 = yes
		}
	}

	focus = {
		id = VIE_mil_ind_traditional_procurement
		icon = GFX_focus_VIE_special_relations_laos

		x = -1
		y = 2
		relative_position_id = VIE_mil_ind_consolidation

		cost = 5

		prerequisite = { focus = VIE_mil_ind_consolidation }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_INDUSTRY }

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_ind_traditional_procurement"
			VIE_lf_xp_15 = yes
			add_political_power = 25
		}
	}

	focus = {
		id = VIE_mil_ind_diversify_defense_partners
		icon = GFX_focus_VIE_multilateral_champion

		x = 1
		y = 2
		relative_position_id = VIE_mil_ind_consolidation

		cost = 5

		prerequisite = { focus = VIE_mil_ind_consolidation }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_INDUSTRY }

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_ind_diversify_defense_partners"
			VIE_lf_xp_15 = yes
			add_political_power = 25
		}
	}

	focus = {
		id = VIE_mil_ind_viettel_digital_military
		icon = GFX_focus_VIE_def_cyber_command

		x = 0
		y = 3
		relative_position_id = VIE_mil_ind_consolidation

		cost = 7

		prerequisite = { focus = VIE_mil_ind_consolidation }

		search_filters = { FOCUS_FILTER_RESEARCH FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_ind_viettel_digital_military"
			add_tech_bonus = {
				name = VIE_viettel_military_tech_bonus
				bonus = 0.5
				uses = 1
				category = CAT_computing_tech
			}
			VIE_lf_xp_15 = yes
		}
	}

	focus = {
		id = VIE_mil_ind_supply_chain_autonomy
		icon = GFX_focus_VIE_path_self_reliant_deterrence

		x = 0
		y = 4
		relative_position_id = VIE_mil_ind_consolidation

		cost = 7

		prerequisite = { focus = VIE_mil_ind_mro_upgrade }
		prerequisite = { focus = VIE_mil_ind_infantry_weapons_z111 }

		search_filters = { FOCUS_FILTER_INDUSTRY FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 75
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_mil_ind_supply_chain_autonomy"
			VIE_v31_upgrade_industrial_sustainment = yes
			VIE_lf_xp_25 = yes
		}
	}

	# -------------------------------------------------------------
	# PHAN 2: NHANH LUC QUAN VIET NAM (36 focus)
	# -------------------------------------------------------------

	### ROOT L0: HIEN DAI HOA LUC QUAN VIET NAM
	focus = {
		id = VIE_lf_root_modern_army
		icon = GFX_focus_VIE_lf_selective_modernization

		x = -20
		y = 1
		relative_position_id = VIE_modernize_vpa

		cost = 7

		prerequisite = { focus = VIE_modernize_vpa }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 80
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_root_modern_army"
			VIE_v31_upgrade_readiness = yes
			VIE_lf_xp_15 = yes
			add_command_power = 15
		}
	}

	### TRUC D: THE TRAN QUOC PHONG TOAN DAN (8 focus)
	focus = {
		id = VIE_lf_territorial_defense_foundation
		icon = GFX_focus_VIE_def_peoples_defence

		x = -5
		y = 1
		relative_position_id = VIE_lf_root_modern_army

		cost = 5

		prerequisite = { focus = VIE_lf_root_modern_army }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_territorial_defense_foundation"
			VIE_v31_upgrade_territorial_defense = yes
			VIE_lf_xp_10 = yes
		}
	}

	focus = {
		id = VIE_lf_local_forces_militia
		icon = GFX_focus_VIE_def_militia_law

		x = -1
		y = 1
		relative_position_id = VIE_lf_territorial_defense_foundation

		cost = 5

		prerequisite = { focus = VIE_lf_territorial_defense_foundation }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_local_forces_militia"
			add_manpower = 15000
			VIE_lf_xp_10 = yes
		}
	}

	focus = {
		id = VIE_lf_reserve_mobilization
		icon = GFX_focus_VIE_mass_mobilization

		x = 1
		y = 1
		relative_position_id = VIE_lf_territorial_defense_foundation

		cost = 5

		prerequisite = { focus = VIE_lf_territorial_defense_foundation }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_reserve_mobilization"
			add_manpower = 25000
			VIE_lf_xp_10 = yes
		}
	}

	focus = {
		id = VIE_lf_strategic_defense_zones
		icon = GFX_focus_VIE_def_provincial_defence_zones

		x = 0
		y = 1
		relative_position_id = VIE_lf_local_forces_militia

		cost = 7

		prerequisite = { focus = VIE_lf_local_forces_militia }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_strategic_defense_zones"
			VIE_v31_upgrade_territorial_defense = yes
			VIE_lf_xp_15 = yes
		}
	}

	focus = {
		id = VIE_lf_fortifications_defense_sites
		icon = GFX_focus_VIE_scs_spratly_fortification

		x = 0
		y = 1
		relative_position_id = VIE_lf_reserve_mobilization

		cost = 7

		prerequisite = { focus = VIE_lf_reserve_mobilization }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_fortifications_defense_sites"
			VIE_lf_xp_15 = yes
			add_command_power = 10
		}
	}

	focus = {
		id = VIE_lf_local_logistics_stockpiles
		icon = GFX_focus_VIE_lf_dev_territorial

		x = 1
		y = 1
		relative_position_id = VIE_lf_strategic_defense_zones

		cost = 7

		prerequisite = { focus = VIE_lf_strategic_defense_zones }
		prerequisite = { focus = VIE_lf_fortifications_defense_sites }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_local_logistics_stockpiles"
			VIE_v31_upgrade_territorial_defense = yes
			VIE_lf_xp_15 = yes
		}
	}

	focus = {
		id = VIE_lf_coordination_regular_local
		icon = GFX_focus_VIE_lf_dev_strategic

		x = 0
		y = 1
		relative_position_id = VIE_lf_local_logistics_stockpiles

		cost = 5

		prerequisite = { focus = VIE_lf_local_logistics_stockpiles }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_coordination_regular_local"
			VIE_lf_xp_15 = yes
			add_command_power = 10
		}
	}

	focus = {
		id = VIE_lf_active_defense_in_depth
		icon = GFX_focus_VIE_lf_fs_depth_defence

		x = 0
		y = 1
		relative_position_id = VIE_lf_coordination_regular_local

		cost = 7

		prerequisite = { focus = VIE_lf_coordination_regular_local }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 75
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_active_defense_in_depth"
			VIE_v31_upgrade_territorial_defense = yes
			VIE_lf_xp_25 = yes
			add_command_power = 15
		}
	}

	### TRUC B: HIEN DAI HOA LUC LUONG HOP THANH (8 focus)
	focus = {
		id = VIE_lf_standardize_infantry_structure
		icon = GFX_focus_VIE_lf_arm_infantry_train

		x = 0
		y = 1
		relative_position_id = VIE_lf_root_modern_army

		cost = 5

		prerequisite = { focus = VIE_lf_root_modern_army }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 75
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_standardize_infantry_structure"
			VIE_v31_upgrade_readiness = yes
			VIE_lf_xp_15 = yes
		}
	}

	focus = {
		id = VIE_lf_combined_arms_readiness
		icon = GFX_focus_VIE_lf_combined_arms

		x = 0
		y = 1
		relative_position_id = VIE_lf_standardize_infantry_structure

		cost = 5

		prerequisite = { focus = VIE_lf_standardize_infantry_structure }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 75
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_combined_arms_readiness"
			VIE_v31_upgrade_readiness = yes
			VIE_lf_xp_15 = yes
			add_command_power = 10
		}
	}

	focus = {
		id = VIE_lf_infantry_modern_equipment
		icon = GFX_focus_VIE_make_in_vietnam

		x = -1
		y = 1
		relative_position_id = VIE_lf_combined_arms_readiness

		cost = 7

		prerequisite = { focus = VIE_lf_combined_arms_readiness }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_infantry_modern_equipment"
			add_tech_bonus = {
				name = VIE_infantry_gear_bonus
				bonus = 0.5
				uses = 1
				category = CAT_infantry_weapons
			}
			VIE_lf_xp_15 = yes
		}
	}

	focus = {
		id = VIE_lf_combat_engineers
		icon = GFX_focus_VIE_lf_arm_engineers

		x = 1
		y = 1
		relative_position_id = VIE_lf_combined_arms_readiness

		cost = 5

		prerequisite = { focus = VIE_lf_combined_arms_readiness }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_combat_engineers"
			VIE_lf_xp_15 = yes
			add_command_power = 10
		}
	}

	focus = {
		id = VIE_lf_ground_artillery_modernization
		icon = GFX_focus_VIE_lf_arm_arty_org

		x = 0
		y = 2
		relative_position_id = VIE_lf_combined_arms_readiness

		cost = 7

		prerequisite = { focus = VIE_lf_combined_arms_readiness }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_ground_artillery_modernization"
			add_tech_bonus = {
				name = VIE_artillery_tech_bonus
				bonus = 0.5
				uses = 1
				category = CAT_artillery
			}
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_tactical_air_defense
		icon = GFX_focus_VIE_lf_cap_army_ad

		x = -1
		y = 1
		relative_position_id = VIE_lf_ground_artillery_modernization

		cost = 5

		prerequisite = { focus = VIE_lf_ground_artillery_modernization }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_tactical_air_defense"
			add_tech_bonus = {
				name = VIE_tactical_ad_bonus
				bonus = 0.5
				uses = 1
				category = CAT_air_defence
			}
			VIE_lf_xp_15 = yes
		}
	}

	focus = {
		id = VIE_lf_recon_tactical_command
		icon = GFX_focus_VIE_lf_cap_info_ops

		x = 1
		y = 1
		relative_position_id = VIE_lf_ground_artillery_modernization

		cost = 5

		prerequisite = { focus = VIE_lf_infantry_modern_equipment }
		prerequisite = { focus = VIE_lf_combat_engineers }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_recon_tactical_command"
			VIE_lf_xp_15 = yes
			add_command_power = 15
		}
	}

	focus = {
		id = VIE_lf_operational_logistics_maintenance
		icon = GFX_focus_VIE_lf_arm_arty_train

		x = 0
		y = 2
		relative_position_id = VIE_lf_ground_artillery_modernization

		cost = 7

		prerequisite = { focus = VIE_lf_tactical_air_defense }
		prerequisite = { focus = VIE_lf_recon_tactical_command }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 80
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_operational_logistics_maintenance"
			VIE_v31_upgrade_readiness = yes
			VIE_lf_xp_25 = yes
			add_command_power = 20
		}
	}

	### TRUC S: BINH CHUNG DAC CONG (5 focus, mo sau B1)
	focus = {
		id = VIE_lf_sf_consolidation
		icon = GFX_focus_VIE_sf_command

		x = 6
		y = 1
		relative_position_id = VIE_lf_standardize_infantry_structure

		cost = 5

		prerequisite = { focus = VIE_lf_standardize_infantry_structure }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_sf_consolidation"
			VIE_lf_xp_15 = yes
			add_command_power = 15
		}
	}

	focus = {
		id = VIE_lf_sf_selection_and_training
		icon = GFX_focus_VIE_sf_sapper_training

		x = 0
		y = 1
		relative_position_id = VIE_lf_sf_consolidation

		cost = 5

		prerequisite = { focus = VIE_lf_sf_consolidation }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_sf_selection_and_training"
			VIE_lf_xp_15 = yes
			add_command_power = 10
		}
	}

	focus = {
		id = VIE_lf_sf_ground_commando
		icon = GFX_focus_VIE_sf_sapper

		x = -1
		y = 1
		relative_position_id = VIE_lf_sf_selection_and_training

		cost = 7

		prerequisite = { focus = VIE_lf_sf_selection_and_training }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_sf_ground_commando"
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_sf_water_commando
		icon = GFX_focus_VIE_sf_marine

		x = 1
		y = 1
		relative_position_id = VIE_lf_sf_selection_and_training

		cost = 7

		prerequisite = { focus = VIE_lf_sf_selection_and_training }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_NAVY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_sf_water_commando"
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_sf_special_warfare_capstone
		icon = GFX_focus_VIE_sf_sapper_elite

		x = 0
		y = 2
		relative_position_id = VIE_lf_sf_selection_and_training

		cost = 7

		prerequisite = {
			focus = VIE_lf_sf_ground_commando
			focus = VIE_lf_sf_water_commando
		}

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 75
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_sf_special_warfare_capstone"
			VIE_v31_check_synergy = yes
			VIE_lf_xp_30 = yes
			add_command_power = 20
		}
	}

	### TRUC M: LUC LUONG CO GIOI VA PHAN CONG CHIEN DICH (6 focus, mutex R1)
	focus = {
		id = VIE_lf_doctrine_combined_arms_mechanized
		icon = GFX_focus_VIE_lf_arm_armor_org

		x = -2
		y = 1
		relative_position_id = VIE_lf_operational_logistics_maintenance

		cost = 7

		prerequisite = { focus = VIE_lf_operational_logistics_maintenance }
		mutually_exclusive = { focus = VIE_lf_doctrine_flexible_mobility }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_doctrine_combined_arms_mechanized"
			add_ideas = VPA_Land_Doctrine_Mech_1
			VIE_lf_xp_25 = yes
		}
	}

	focus = {
		id = VIE_lf_upgrade_armor_fleet
		icon = GFX_focus_VIE_lf_arm_armor_train

		x = -1
		y = 1
		relative_position_id = VIE_lf_doctrine_combined_arms_mechanized

		cost = 7

		prerequisite = { focus = VIE_lf_doctrine_combined_arms_mechanized }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_INDUSTRY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_upgrade_armor_fleet"
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_mechanize_infantry_units
		icon = GFX_focus_VIE_lf_fs_mobile_corps

		x = 1
		y = 1
		relative_position_id = VIE_lf_doctrine_combined_arms_mechanized

		cost = 7

		prerequisite = { focus = VIE_lf_doctrine_combined_arms_mechanized }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_RESEARCH }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mechanize_infantry_units"
			add_tech_bonus = {
				name = VIE_mechanized_tech_bonus
				bonus = 0.5
				uses = 1
				category = CAT_mechanized_equipment
			}
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_mobile_fire_support
		icon = GFX_focus_VIE_lf_fs_mobile_force

		x = 0
		y = 1
		relative_position_id = VIE_lf_upgrade_armor_fleet

		cost = 7

		prerequisite = { focus = VIE_lf_upgrade_armor_fleet }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mobile_fire_support"
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_core_mechanized_combined_arms
		icon = GFX_focus_VIE_lf_fs_main_corps

		x = 1
		y = 1
		relative_position_id = VIE_lf_mobile_fire_support

		cost = 7

		prerequisite = { focus = VIE_lf_mechanize_infantry_units }
		prerequisite = { focus = VIE_lf_mobile_fire_support }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_core_mechanized_combined_arms"
			VIE_lf_xp_25 = yes
			add_command_power = 15
		}
	}

	focus = {
		id = VIE_lf_operational_counteroffensive_capstone
		icon = GFX_focus_VIE_lf_cap_border_urban

		x = 0
		y = 1
		relative_position_id = VIE_lf_core_mechanized_combined_arms

		cost = 7

		prerequisite = { focus = VIE_lf_core_mechanized_combined_arms }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 80
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_operational_counteroffensive_capstone"
			swap_ideas = {
				remove_idea = VPA_Land_Doctrine_Mech_1
				add_idea = VPA_Land_Doctrine_Mech_2
			}
			VIE_v31_check_synergy = yes
			VIE_lf_xp_30 = yes
			add_command_power = 20
		}
	}

	### TRUC R: BO BINH CO DONG VA PHAN UNG NHANH (6 focus, mutex M1)
	focus = {
		id = VIE_lf_doctrine_flexible_mobility
		icon = GFX_focus_VIE_lf_cap_area_control

		x = 2
		y = 1
		relative_position_id = VIE_lf_operational_logistics_maintenance

		cost = 7

		prerequisite = { focus = VIE_lf_operational_logistics_maintenance }
		mutually_exclusive = { focus = VIE_lf_doctrine_combined_arms_mechanized }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_doctrine_flexible_mobility"
			add_ideas = VPA_Land_Doctrine_Mobility_1
			VIE_lf_xp_25 = yes
		}
	}

	focus = {
		id = VIE_lf_modernize_light_infantry
		icon = GFX_focus_VIE_sec_border_control

		x = 0
		y = 1
		relative_position_id = VIE_lf_doctrine_flexible_mobility

		cost = 5

		prerequisite = { focus = VIE_lf_doctrine_flexible_mobility }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_modernize_light_infantry"
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_mountain_jungle_warfare
		icon = GFX_focus_VIE_border_settlement

		x = -1
		y = 1
		relative_position_id = VIE_lf_modernize_light_infantry

		cost = 7

		prerequisite = { focus = VIE_lf_modernize_light_infantry }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mountain_jungle_warfare"
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_tactical_mobility_vehicles
		icon = GFX_focus_VIE_border_trade_gates

		x = 1
		y = 1
		relative_position_id = VIE_lf_modernize_light_infantry

		cost = 5

		prerequisite = { focus = VIE_lf_modernize_light_infantry }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 65
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_tactical_mobility_vehicles"
			VIE_lf_xp_20 = yes
		}
	}

	focus = {
		id = VIE_lf_rapid_reaction_forces
		icon = GFX_focus_VIE_def_limited_war_doctrine

		x = 0
		y = 2
		relative_position_id = VIE_lf_modernize_light_infantry

		cost = 7

		prerequisite = { focus = VIE_lf_mountain_jungle_warfare }
		prerequisite = { focus = VIE_lf_tactical_mobility_vehicles }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 70
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_rapid_reaction_forces"
			VIE_lf_xp_25 = yes
			add_command_power = 15
		}
	}

	focus = {
		id = VIE_lf_complex_terrain_mobile_capstone
		icon = GFX_focus_VIE_def_four_nos_doctrine

		x = 0
		y = 1
		relative_position_id = VIE_lf_rapid_reaction_forces

		cost = 7

		prerequisite = { focus = VIE_lf_rapid_reaction_forces }

		search_filters = { FOCUS_FILTER_ARMY }

		ai_will_do = {
			base = 80
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_complex_terrain_mobile_capstone"
			swap_ideas = {
				remove_idea = VPA_Land_Doctrine_Mobility_1
				add_idea = VPA_Land_Doctrine_Mobility_2
			}
			VIE_v31_check_synergy = yes
			VIE_lf_xp_30 = yes
			add_command_power = 20
		}
	}

	### TRUC F: HIEN DAI HOA VA HOI TU LUC QUAN (2 focus)
	focus = {
		id = VIE_lf_modernize_army_command_system
		icon = GFX_focus_VIE_lf_command_reform_2

		x = 2
		y = 1
		relative_position_id = VIE_lf_operational_counteroffensive_capstone

		cost = 7

		prerequisite = {
			focus = VIE_lf_operational_counteroffensive_capstone
			focus = VIE_lf_complex_terrain_mobile_capstone
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

if __name__ == "__main__":
    content = generate_focuses()
    print("Generated characters:", len(content))
    with open("scratch/v31_focuses_generated.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("Written to scratch/v31_focuses_generated.txt")
