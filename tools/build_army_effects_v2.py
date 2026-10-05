# tools/build_army_effects_v2.py
import re, os

p17_path = r'common/scripted_effects/VIE_md_effects_p17.txt'
with open(p17_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Locate boundaries: from VIE_lf_n1_reward to end of VIE_lf_cap_reward
idx_first = text.find('VIE_lf_n1_reward = {')
idx_last = text.find('VIE_lf_cap_reward = {')

# Find end of VIE_lf_cap_reward
depth = 1
i = idx_last + len('VIE_lf_cap_reward = {')
while i < len(text) and depth > 0:
    if text[i] == '{': depth += 1
    elif text[i] == '}': depth -= 1
    i += 1

header = text[:idx_first]
trailer = text[i:]

# Ensure VIE_lf_xp_25 is defined in header
if 'VIE_lf_xp_25 = {' not in header:
    xp20_idx = header.find('VIE_lf_xp_20 = {')
    if xp20_idx != -1:
        # find end of VIE_lf_xp_20
        d = 1
        j = xp20_idx + len('VIE_lf_xp_20 = {')
        while j < len(header) and d > 0:
            if header[j] == '{': d += 1
            elif header[j] == '}': d -= 1
            j += 1
        xp25_def = '''
VIE_lf_xp_25 = {
	if = {
		limit = { has_selected_land_grand_doctrine = yes }
		add_mastery = {
			amount = 25
			folder = land
		}
	}
	else = {
		army_experience = 25
	}
}'''
        header = header[:j] + xp25_def + header[j:]

fav_discount_code = '''
VIE_lf_fav_discount = {
	if = {
		limit = {
			has_country_flag = VIE_lf_depth
			NOT = { has_completed_focus = VIE_lf_cap_border_urban }
		}
		reduce_focus_completion_cost = {
			focus = VIE_lf_cap_border_urban
			cost = 14
		}
	}
	if = {
		limit = {
			has_country_flag = VIE_lf_regular
			NOT = { has_completed_focus = VIE_lf_cap_army_ad }
		}
		reduce_focus_completion_cost = {
			focus = VIE_lf_cap_army_ad
			cost = 14
		}
	}
	if = {
		limit = {
			has_country_flag = VIE_lf_mobile
			NOT = { has_completed_focus = VIE_lf_cap_cyber_ew }
		}
		reduce_focus_completion_cost = {
			focus = VIE_lf_cap_cyber_ew
			cost = 14
		}
	}
}
'''

# Now define all 30 rewards with full Millennium Dawn style richness!
rewards_code = '''VIE_lf_n1_reward = {
	add_political_power = 50
	add_command_power = 25
	VIE_lf_xp_20 = yes
	set_temp_variable = { treasury_change = 1.0 }
	modify_treasury_effect = yes
	set_temp_variable = { temp_opinion = 5 }
	change_the_military_opinion = yes
	add_ideas = VIE_military_streamlining
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_army_personnel_cost_multiplier_modifier = -0.03 tooltip = VIE_tt_army_personnel_cost }
	VIE_lf_refresh = yes
}
VIE_lf_n2_reward = {
	add_command_power = 25
	VIE_lf_xp_20 = yes
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 400 producer = VIE }
	add_equipment_to_stockpile = { type = support_equipment amount = 200 producer = VIE }
	671 = { one_state_fuel_reserve = yes }
	672 = { one_state_fuel_reserve = yes }
	add_tech_bonus = {
		name = VIE_lf_n2_tech
		bonus = 1.0
		uses = 1
		category = CAT_util
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_supply_consumption_factor = -0.05 tooltip = VIE_tt_supply_consumption_factor }
	add_to_variable = { VIE_af_army_fuel_consumption_factor = -0.05 tooltip = VIE_tt_supply_consumption_factor }
	VIE_lf_refresh = yes
}
VIE_lf_n3_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 25
	add_doctrine_cost_reduction = {
		name = VIE_lf_n3_tech
		cost_reduction = 0.5
		uses = 1
		category = land_doctrine
	}
	add_tech_bonus = {
		name = VIE_lf_n3_tech
		bonus = 1.0
		uses = 1
		category = land_doctrine
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_experience_gain_army_factor = 0.05 tooltip = VIE_tt_experience_gain_army_factor }
	add_to_variable = { VIE_af_training_time_factor = -0.05 tooltip = VIE_tt_training_time_factor }
	add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
	VIE_lf_refresh = yes
}
VIE_lf_bb1_reward = {
	VIE_lf_xp_15 = yes
	add_equipment_to_stockpile = { type = APC_1 amount = 40 producer = VIE }
	add_tech_bonus = {
		name = VIE_lf_bb1_tech
		bonus = 1.0
		uses = 1
		category = CAT_infantry_weapons
	}
	if = {
		limit = { has_dlc = "Arms Against Tyranny" }
		mio:VIE_gdt_manufacturer = { add_mio_funds = 200 }
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_org_factor = 0.025 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
	VIE_lf_refresh = yes
}
VIE_lf_bb2_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 20
	add_equipment_to_stockpile = { type = infantry_weapons_type amount = 3000 producer = VIE }
	add_equipment_to_stockpile = { type = support_equipment amount = 150 producer = VIE }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_infantry_elite } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_infantry_elite }
		division_template = {
			name = "Su doan Bo binh 312"
			regiments = {
				Mot_Inf_Bat = { x = 0 y = 0 }
				Mot_Inf_Bat = { x = 0 y = 1 }
				Mot_Inf_Bat = { x = 0 y = 2 }
				Mot_Inf_Bat = { x = 1 y = 0 }
				Mot_Inf_Bat = { x = 1 y = 1 }
				Mot_Inf_Bat = { x = 1 y = 2 }
				Mot_Inf_Bat = { x = 2 y = 0 }
				Mot_Inf_Bat = { x = 2 y = 1 }
				Mot_Inf_Bat = { x = 2 y = 2 }
				Arty_Bat = { x = 3 y = 0 }
				Arty_Bat = { x = 3 y = 1 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
				L_Recce_Comp = { x = 0 y = 1 }
				Arty_Battery = { x = 0 y = 2 }
			}
		}
		create_unit = {
			division = "name = \\"Su doan Bo binh Co gioi 312\\" division_template = \\"Su doan Bo binh 312\\" start_experience_factor = 0.8 start_equipment_factor = 1.0"
			owner = ROOT
		}
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_defence_factor = 0.025 tooltip = VIE_tt_army_defence_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.02 tooltip = VIE_tt_supply_consumption_factor }
	VIE_lf_refresh = yes
}
VIE_lf_tg1_reward = {
	VIE_lf_xp_15 = yes
	add_equipment_to_stockpile = { type = medium_tank_destroyer_chassis_2 amount = 30 producer = VIE }
	add_tech_bonus = {
		name = VIE_lf_tg1_tech
		bonus = 1.0
		uses = 1
		category = CAT_main_battle_tanks
	}
	if = {
		limit = { has_dlc = "Arms Against Tyranny" }
		mio:VIE_gdt_manufacturer = { add_mio_funds = 200 }
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_speed_factor = 0.03 tooltip = VIE_tt_army_speed_factor }
	add_to_variable = { VIE_af_army_armor_attack_factor = 0.03 tooltip = VIE_tt_army_armor_attack_factor }
	VIE_lf_refresh = yes
}
VIE_lf_tg2_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 20
	add_equipment_to_stockpile = { type = medium_tank_destroyer_chassis_2 amount = 30 producer = VIE }
	add_equipment_to_stockpile = { type = APC_1 amount = 60 producer = VIE }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_armor_elite } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_armor_elite }
		division_template = {
			name = "Lu doan Tang Thiet giap 201"
			regiments = {
				armor_Bat = { x = 0 y = 0 }
				armor_Bat = { x = 0 y = 1 }
				armor_Bat = { x = 0 y = 2 }
				Mech_Inf_Bat = { x = 1 y = 0 }
				Mech_Inf_Bat = { x = 1 y = 1 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
				armor_Recce_Comp = { x = 0 y = 1 }
				SP_AA_Battery = { x = 0 y = 2 }
			}
		}
		create_unit = {
			division = "name = \\"Lu doan Xe tang - Thiet giap 201\\" division_template = \\"Lu doan Tang Thiet giap 201\\" start_experience_factor = 0.8 start_equipment_factor = 1.0"
			owner = ROOT
		}
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_armor_defence_factor = 0.03 tooltip = VIE_tt_army_armor_defence_factor }
	add_to_variable = { VIE_af_army_armor_attack_factor = 0.03 tooltip = VIE_tt_army_armor_attack_factor }
	VIE_lf_refresh = yes
}
VIE_lf_pb1_reward = {
	VIE_lf_xp_15 = yes
	add_equipment_to_stockpile = { type = artillery_equipment amount = 50 producer = VIE }
	add_tech_bonus = {
		name = VIE_lf_pb1_tech
		bonus = 1.0
		uses = 1
		category = CAT_artillery
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_artillery_attack_factor = 0.03 tooltip = VIE_tt_army_artillery_attack_factor }
	add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
	VIE_lf_refresh = yes
}
VIE_lf_pb2_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 20
	add_equipment_to_stockpile = { type = artillery_equipment amount = 50 producer = VIE }
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 100 producer = VIE }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_arty_elite } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_arty_elite }
		division_template = {
			name = "Lu doan Phao binh 45"
			regiments = {
				Arty_Bat = { x = 0 y = 0 }
				Arty_Bat = { x = 0 y = 1 }
				Arty_Bat = { x = 0 y = 2 }
				SP_Arty_Bat = { x = 1 y = 0 }
				SP_R_arty_Bat = { x = 1 y = 1 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
				L_Recce_Comp = { x = 0 y = 1 }
			}
		}
		create_unit = {
			division = "name = \\"Lu doan Phao binh Tat Thang 45\\" division_template = \\"Lu doan Phao binh 45\\" start_experience_factor = 0.8 start_equipment_factor = 1.0"
			owner = ROOT
		}
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_artillery_attack_factor = 0.03 tooltip = VIE_tt_army_artillery_attack_factor }
	add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
	VIE_lf_refresh = yes
}
VIE_lf_cb_reward = {
	VIE_lf_xp_15 = yes
	add_command_power = 20
	522 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
	673 = { add_building_construction = { type = infrastructure level = 1 instant_build = yes } }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_sapper_elite } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_sapper_elite }
		division_template = {
			name = "Lu doan Dac cong 113"
			regiments = {
				Special_Forces = { x = 0 y = 0 }
				Special_Forces = { x = 0 y = 1 }
				Special_Forces = { x = 0 y = 2 }
				Special_Forces = { x = 1 y = 0 }
				Special_Forces = { x = 1 y = 1 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
				L_Recce_Comp = { x = 0 y = 1 }
			}
		}
		create_unit = {
			division = "name = \\"Lu doan Dac cong 113\\" division_template = \\"Lu doan Dac cong 113\\" start_experience_factor = 0.9 start_equipment_factor = 1.0"
			owner = ROOT
		}
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_special_forces_cap = 0.05 tooltip = VIE_tt_special_forces_cap }
	add_to_variable = { VIE_af_terrain_penalty_reduction = 0.05 tooltip = terrain_penalty_reduction_tt }
	add_to_variable = { VIE_af_dig_in_speed_factor = 0.05 tooltip = VIE_tt_dig_in_speed_factor }
	VIE_lf_refresh = yes
}
VIE_lf_hd_reward = {
	VIE_lf_xp_25 = yes
	add_command_power = 30
	add_war_support = 0.03
	add_doctrine_cost_reduction = {
		name = VIE_lf_hd_tech
		cost_reduction = 0.5
		uses = 1
		category = land_doctrine
	}
	add_tech_bonus = {
		name = VIE_lf_hd_tech
		bonus = 1.0
		uses = 1
		category = land_doctrine
	}
	set_temp_variable = { temp_opinion = 5 }
	change_the_military_opinion = yes
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_org_factor = 0.03 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_planning_speed = 0.10 tooltip = VIE_tt_planning_speed }
	VIE_lf_refresh = yes
}
VIE_lf_cr1_reward = {
	add_command_power = 40
	VIE_lf_xp_20 = yes
	add_political_power = 30
	unlock_decision_tooltip = VIE_dec_lf_train_terrain
	unlock_decision_tooltip = VIE_dec_lf_train_urban
	unlock_decision_tooltip = VIE_dec_lf_joint_arms
	unlock_decision_tooltip = VIE_dec_lf_total_mobilization
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_org_factor = 0.025 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.03 tooltip = VIE_tt_supply_consumption_factor }
	add_to_variable = { VIE_af_max_planning = 0.10 tooltip = VIE_tt_max_planning }
	VIE_lf_refresh = yes
}
VIE_lf_fm1_reward = {
	hidden_effect = { set_country_flag = VIE_lf_mobile }
	add_ideas = VIE_mobile_doctrine_spirit
	VIE_lf_xp_20 = yes
	add_equipment_to_stockpile = { type = APC_1 amount = 50 producer = VIE }
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_speed_factor = 0.03 tooltip = VIE_tt_army_speed_factor }
	add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_conscription_factor = -0.015 tooltip = VIE_tt_conscription_factor }
	add_to_variable = { VIE_af_equipment_cost_multiplier_modifier = 0.02 tooltip = VIE_tt_equipment_cost }
	add_to_variable = { VIE_af_max_dig_in_factor = -0.02 tooltip = VIE_tt_max_dig_in_factor }
	VIE_lf_fav_discount = yes
	VIE_lf_refresh = yes
}
VIE_lf_fm2_reward = {
	VIE_lf_xp_25 = yes
	add_command_power = 25
	add_equipment_to_stockpile = { type = APC_1 amount = 60 producer = VIE }
	add_equipment_to_stockpile = { type = medium_tank_destroyer_chassis_2 amount = 20 producer = VIE }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_mobile_corps } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_mobile_corps }
		division_template = {
			name = "Cum Co dong Phiet kich"
			regiments = {
				Mech_Inf_Bat = { x = 0 y = 0 }
				Mech_Inf_Bat = { x = 0 y = 1 }
				armor_Bat = { x = 0 y = 2 }
				armor_Bat = { x = 1 y = 0 }
				SP_Arty_Bat = { x = 1 y = 1 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
				armor_Recce_Comp = { x = 0 y = 1 }
				SP_AA_Battery = { x = 0 y = 2 }
			}
		}
		create_unit = {
			division = "name = \\"Cum Co dong Chien luoc 1\\" division_template = \\"Cum Co dong Phiet kich\\" start_experience_factor = 0.8 start_equipment_factor = 1.0"
			owner = ROOT
		}
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_speed_factor = 0.03 tooltip = VIE_tt_army_speed_factor }
	add_to_variable = { VIE_af_army_attack_factor = 0.03 tooltip = VIE_tt_army_attack_factor }
	VIE_lf_refresh = yes
}
VIE_lf_fr1_reward = {
	hidden_effect = { set_country_flag = VIE_lf_regular }
	add_ideas = VIE_regular_corps_spirit
	VIE_lf_xp_25 = yes
	add_command_power = 30
	add_war_support = 0.04
	set_temp_variable = { temp_opinion = 10 }
	change_the_military_opinion = yes
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_army_defence_factor = 0.015 tooltip = VIE_tt_army_defence_factor }
	add_to_variable = { VIE_af_army_personnel_cost_multiplier_modifier = 0.02 tooltip = VIE_tt_army_personnel_cost }
	add_to_variable = { VIE_af_experience_gain_army_factor = -0.01 tooltip = VIE_tt_experience_gain_army_factor }
	VIE_lf_fav_discount = yes
	VIE_lf_refresh = yes
}
VIE_lf_fr2_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 25
	set_temp_variable = { treasury_change = 1.5 }
	modify_treasury_effect = yes
	add_equipment_to_stockpile = { type = infantry_weapons_type amount = 2000 producer = VIE }
	add_equipment_to_stockpile = { type = artillery_equipment amount = 30 producer = VIE }
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_org_factor = 0.025 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.05 tooltip = VIE_tt_supply_consumption_factor }
	VIE_lf_refresh = yes
}
VIE_lf_fd1_reward = {
	hidden_effect = { set_country_flag = VIE_lf_depth }
	add_ideas = VIE_depth_defence_spirit
	VIE_lf_xp_20 = yes
	522 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }
	519 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }
	518 = { add_building_construction = { type = bunker level = 2 instant_build = yes } }
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_max_dig_in_factor = 0.04 tooltip = VIE_tt_max_dig_in_factor }
	add_to_variable = { VIE_af_army_defence_factor = 0.025 tooltip = VIE_tt_army_defence_factor }
	add_to_variable = { VIE_af_army_speed_factor = -0.02 tooltip = VIE_tt_army_speed_factor }
	add_to_variable = { VIE_af_army_armor_attack_factor = -0.015 tooltip = VIE_tt_army_armor_attack_factor }
	VIE_lf_fav_discount = yes
	VIE_lf_refresh = yes
}
VIE_lf_fd2_reward = {
	VIE_lf_xp_15 = yes
	add_manpower = 40000
	add_equipment_to_stockpile = { type = infantry_weapons_type amount = 3000 producer = VIE }
	522 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }
	673 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_militia_elite } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_militia_elite }
		division_template = {
			name = "Su doan Dan quan Khu vuc"
			regiments = {
				L_Inf_Bat = { x = 0 y = 0 }
				L_Inf_Bat = { x = 0 y = 1 }
				L_Inf_Bat = { x = 0 y = 2 }
				L_Inf_Bat = { x = 1 y = 0 }
				L_Inf_Bat = { x = 1 y = 1 }
				L_Inf_Bat = { x = 1 y = 2 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
			}
		}
		create_unit = {
			division = "name = \\"Su doan Dan quan Khu vuc 1\\" division_template = \\"Su doan Dan quan Khu vuc\\" start_experience_factor = 0.5 start_equipment_factor = 1.0"
			owner = ROOT
		}
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_conscription_factor = 0.04 tooltip = VIE_tt_conscription_factor }
	add_to_variable = { VIE_af_dig_in_speed_factor = 0.05 tooltip = VIE_tt_dig_in_speed_factor }
	VIE_lf_refresh = yes
}
VIE_lf_ps_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 20
	unlock_decision_tooltip = VIE_dec_lf_rapid_response
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 300 producer = VIE }
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
	add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.02 tooltip = VIE_tt_supply_consumption_factor }
	add_to_variable = { VIE_af_equipment_cost_multiplier_modifier = 0.01 tooltip = VIE_tt_equipment_cost }
	VIE_lf_refresh = yes
}
VIE_lf_pt_reward = {
	VIE_lf_xp_15 = yes
	add_manpower = 40000
	unlock_decision_tooltip = VIE_dec_lf_mobilize_people
	add_equipment_to_stockpile = { type = infantry_weapons_type amount = 2000 producer = VIE }
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_conscription_factor = 0.035 tooltip = VIE_tt_conscription_factor }
	add_to_variable = { VIE_af_max_dig_in_factor = 0.02 tooltip = VIE_tt_max_dig_in_factor }
	add_to_variable = { VIE_af_army_personnel_cost_multiplier_modifier = 0.01 tooltip = VIE_tt_army_personnel_cost }
	VIE_lf_refresh = yes
}
''' + fav_discount_code + '''
VIE_lf_cr2_reward = {
	add_command_power = 50
	VIE_lf_xp_20 = yes
	add_stability = 0.03
	add_war_support = 0.03
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_planning_speed = 0.15 tooltip = VIE_tt_planning_speed }
	add_to_variable = { VIE_af_max_planning = 0.10 tooltip = VIE_tt_max_planning }
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.005 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_attack_factor = 0.015 tooltip = VIE_tt_army_attack_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_dig_in_speed_factor = 0.03 tooltip = VIE_tt_dig_in_speed_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_l1_reward = {
	VIE_lf_xp_20 = yes
	add_equipment_to_stockpile = { type = infantry_weapons_type amount = 2000 producer = VIE }
	add_equipment_to_stockpile = { type = support_equipment amount = 100 producer = VIE }
	671 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }
	672 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }
	add_tech_bonus = {
		name = VIE_lf_l1_tech
		bonus = 1.0
		uses = 1
		category = CAT_infantry_weapons
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_terrain_penalty_reduction = 0.05 tooltip = terrain_penalty_reduction_tt }
	if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_l2_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 20
	522 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }
	519 = { add_building_construction = { type = bunker level = 1 instant_build = yes } }
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 200 producer = VIE }
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_land_reinforce_rate = 0.05 tooltip = VIE_tt_land_reinforce_rate }
	if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.025 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.015 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_attack_factor = 0.02 tooltip = VIE_tt_army_attack_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_a1_reward = {
	VIE_lf_xp_20 = yes
	add_equipment_to_stockpile = { type = AA_Equipment amount = 120 producer = VIE }
	522 = { one_state_anti_air = yes }
	671 = { one_state_anti_air = yes }
	add_tech_bonus = {
		name = VIE_lf_a1_tech
		bonus = 1.0
		uses = 1
		category = CAT_anti_air
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_defence_factor = 0.03 tooltip = VIE_tt_army_defence_factor }
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_a2_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 20
	522 = { one_state_radar_station = yes }
	673 = { one_state_radar_station = yes }
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_recon_factor = 0.05 tooltip = VIE_tt_recon_factor }
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.03 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.03 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_attack_factor = 0.02 tooltip = VIE_tt_army_attack_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_y1_reward = {
	add_ideas = VIE_cyber_command_86
	VIE_lf_xp_25 = yes
	add_command_power = 25
	add_equipment_to_stockpile = { type = Air_UAV1 amount = 40 producer = VIE }
	671 = { one_state_network_infrastructure = yes }
	672 = { one_state_network_infrastructure = yes }
	add_tech_bonus = {
		name = VIE_lf_y1_tech
		bonus = 1.0
		uses = 1
		category = CAT_drones
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_recon_factor = 0.08 tooltip = VIE_tt_recon_factor }
	if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.03 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_attack_factor = 0.02 tooltip = VIE_tt_army_attack_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.02 tooltip = VIE_tt_max_dig_in_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_y2_reward = {
	VIE_lf_xp_20 = yes
	add_command_power = 25
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 150 producer = VIE }
	add_equipment_to_stockpile = { type = Air_UAV1 amount = 30 producer = VIE }
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_recon_factor = 0.10 tooltip = VIE_tt_recon_factor }
	add_to_variable = { VIE_af_planning_speed = 0.10 tooltip = VIE_tt_planning_speed }
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.03 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_attack_factor = 0.03 tooltip = VIE_tt_army_attack_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_dig_in_speed_factor = 0.03 tooltip = VIE_tt_dig_in_speed_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_mod_reward = {
	army_experience = 50
	add_command_power = 40
	add_war_support = 0.05
	set_temp_variable = { treasury_change = -2.0 }
	modify_treasury_effect = yes
	increase_military_spending = yes
	671 = { one_state_arms_factory = yes }
	set_temp_variable = { temp_opinion = 10 }
	change_the_military_opinion = yes
	add_tech_bonus = {
		name = VIE_lf_mod_tech_1
		bonus = 1.0
		uses = 1
		category = CAT_infantry_weapons
	}
	add_tech_bonus = {
		name = VIE_lf_mod_tech_2
		bonus = 1.0
		uses = 1
		category = CAT_main_battle_tanks
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.03 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.03 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.03 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_attack_factor = 0.03 tooltip = VIE_tt_army_attack_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.04 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.03 tooltip = VIE_tt_army_defence_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_cr3_reward = {
	add_command_power = 50
	army_experience = 30
	add_political_power = 50
	add_doctrine_cost_reduction = {
		name = VIE_lf_cr3_tech
		cost_reduction = 0.5
		uses = 2
		category = land_doctrine
	}
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	add_to_variable = { VIE_af_army_org_factor = 0.03 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.05 tooltip = VIE_tt_supply_consumption_factor }
	add_to_variable = { VIE_af_planning_speed = 0.15 tooltip = VIE_tt_planning_speed }
	VIE_lf_refresh = yes
}
VIE_lf_cap_reward = {
	add_ideas = VIE_vpa_modern_army_power
	army_experience = 50
	add_command_power = 50
	add_war_support = 0.08
	add_stability = 0.05
	set_temp_variable = { treasury_change = -3.0 }
	modify_treasury_effect = yes
	increase_military_spending = yes
	672 = { one_state_arms_factory = yes }
	set_temp_variable = { temp_opinion = 15 }
	change_the_military_opinion = yes
	custom_effect_tooltip = {
		localization_key = modifies_dynamic_modifier_tt
		MODIFIER = VIE_armed_forces_modifier
	}
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.04 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.04 tooltip = VIE_tt_army_defence_factor }
		add_to_variable = { VIE_af_planning_speed = 0.15 tooltip = VIE_tt_planning_speed }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.05 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_attack_factor = 0.05 tooltip = VIE_tt_army_attack_factor }
		add_to_variable = { VIE_af_army_armor_attack_factor = 0.04 tooltip = VIE_tt_army_armor_attack_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.06 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.05 tooltip = VIE_tt_army_defence_factor }
		add_to_variable = { VIE_af_conscription_factor = 0.05 tooltip = VIE_tt_conscription_factor }
	}
	VIE_lf_refresh = yes
}
'''

full_text = header + rewards_code + trailer
with open(p17_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

print('Updated VIE_md_effects_p17.txt successfully!')
