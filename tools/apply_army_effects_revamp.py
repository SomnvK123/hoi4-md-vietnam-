# -*- coding: utf-8 -*-
import os

with open('common/scripted_effects/VIE_md_effects_p17.txt', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "VIE_lf_n1_reward = {"
end_marker = "hidden_effect = { set_country_flag = VIE_lf_done }\n\tVIE_lf_refresh = yes\n}"

p_start = text.find(start_marker)
if p_start == -1:
    raise ValueError("start_marker not found!")

p_end = text.find(end_marker, p_start)
if p_end == -1:
    raise ValueError("end_marker not found!")
p_end += len(end_marker)

new_rewards = """VIE_lf_n1_reward = {
	add_political_power = 50
	VIE_lf_xp_20 = yes
	add_ideas = VIE_military_streamlining
}
VIE_lf_n2_reward = {
	add_command_power = 25
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 350 producer = VIE }
	add_tech_bonus = {
		name = VIE_lf_n2_tech
		bonus = 1.0
		uses = 1
		category = CAT_util
	}
}
VIE_lf_n3_reward = {
	VIE_lf_xp_20 = yes
	add_tech_bonus = {
		name = VIE_lf_n3_tech
		bonus = 1.0
		uses = 1
		category = land_doctrine
	}
}
VIE_lf_bb1_reward = {
	add_to_variable = { VIE_af_army_org_factor = 0.025 tooltip = VIE_tt_army_org_factor }
	add_tech_bonus = {
		name = VIE_lf_bb1_tech
		bonus = 1.0
		uses = 1
		category = CAT_infantry_weapons
	}
	if = {
		limit = { has_dlc = "Arms Against Tyranny" }
		mio:VIE_gdt_manufacturer = { add_mio_funds = 150 }
	}
	VIE_lf_refresh = yes
}
VIE_lf_bb2_reward = {
	add_to_variable = { VIE_af_army_defence_factor = 0.025 tooltip = VIE_tt_army_defence_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.02 tooltip = VIE_tt_supply_consumption_factor }
	add_equipment_to_stockpile = { type = infantry_weapons_type amount = 2500 producer = VIE }
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
	}
	VIE_lf_refresh = yes
}
VIE_lf_tg1_reward = {
	add_to_variable = { VIE_af_army_speed_factor = 0.03 tooltip = VIE_tt_army_speed_factor }
	add_tech_bonus = {
		name = VIE_lf_tg1_tech
		bonus = 1.0
		uses = 1
		category = CAT_main_battle_tanks
	}
	if = {
		limit = { has_dlc = "Arms Against Tyranny" }
		mio:VIE_gdt_manufacturer = { add_mio_funds = 150 }
	}
	VIE_lf_refresh = yes
}
VIE_lf_tg2_reward = {
	add_to_variable = { VIE_af_army_attack_factor = 0.025 tooltip = VIE_tt_army_attack_factor }
	add_to_variable = { VIE_af_army_armor_attack_factor = 0.03 tooltip = VIE_tt_army_armor_attack_factor }
	add_equipment_to_stockpile = { type = APC_1 amount = 60 producer = VIE }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_armor_bde } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_armor_bde }
		division_template = {
			name = "Lu doan Tang - Thiet giap 201"
			regiments = {
				armor_Bat = { x = 0 y = 0 }
				armor_Bat = { x = 0 y = 1 }
				armor_Bat = { x = 0 y = 2 }
				Mech_Inf_Bat = { x = 1 y = 0 }
				Mech_Inf_Bat = { x = 1 y = 1 }
				SP_Arty_Bat = { x = 2 y = 0 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
				armor_Recce_Comp = { x = 0 y = 1 }
				SP_AA_Battery = { x = 0 y = 2 }
			}
		}
	}
	VIE_lf_refresh = yes
}
VIE_lf_pb1_reward = {
	add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
	add_to_variable = { VIE_af_army_artillery_attack_factor = 0.03 tooltip = VIE_tt_army_artillery_attack_factor }
	add_tech_bonus = {
		name = VIE_lf_pb1_tech
		bonus = 1.0
		uses = 1
		category = CAT_artillery
	}
	VIE_lf_refresh = yes
}
VIE_lf_pb2_reward = {
	add_to_variable = { VIE_af_army_artillery_attack_factor = 0.035 tooltip = VIE_tt_army_artillery_attack_factor }
	add_equipment_to_stockpile = { type = artillery_equipment amount = 40 producer = VIE }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_arty_bde } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_arty_bde }
		division_template = {
			name = "Lu doan Phao binh 45"
			regiments = {
				Arty_Bat = { x = 0 y = 0 }
				Arty_Bat = { x = 0 y = 1 }
				Arty_Bat = { x = 0 y = 2 }
				Arty_Bat = { x = 1 y = 0 }
				Arty_Bat = { x = 1 y = 1 }
				SP_R_arty_Bat = { x = 2 y = 0 }
				SP_R_arty_Bat = { x = 2 y = 1 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
				L_Recce_Comp = { x = 0 y = 1 }
				Arty_Battery = { x = 0 y = 2 }
			}
		}
	}
	VIE_lf_refresh = yes
}
VIE_lf_cb_reward = {
	add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
	add_to_variable = { VIE_af_dig_in_speed_factor = 0.05 tooltip = VIE_tt_dig_in_speed_factor }
	522 = {
		add_building_construction = {
			type = bunker
			level = 2
			instant_build = yes
			province = {
				all_provinces = yes
				limit_to_border = yes
			}
		}
	}
	add_equipment_to_stockpile = { type = support_equipment amount = 150 producer = VIE }
	VIE_lf_refresh = yes
}
VIE_lf_hd_reward = {
	add_to_variable = { VIE_af_army_org_factor = 0.03 tooltip = VIE_tt_army_org_factor }
	VIE_lf_xp_20 = yes
	add_tech_bonus = {
		name = VIE_lf_hd_tech
		bonus = 1.0
		uses = 1
		category = land_doctrine
	}
	VIE_lf_refresh = yes
}
VIE_lf_cr1_reward = {
	add_to_variable = { VIE_af_army_org_factor = 0.025 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.03 tooltip = VIE_tt_supply_consumption_factor }
	add_command_power = 30
	VIE_lf_refresh = yes
}
VIE_lf_fm1_reward = {
	hidden_effect = { set_country_flag = VIE_lf_mobile }
	add_ideas = VIE_mobile_doctrine_spirit
	add_to_variable = { VIE_af_army_speed_factor = 0.03 tooltip = VIE_tt_army_speed_factor }
	add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_conscription_factor = -0.015 tooltip = VIE_tt_conscription_factor }
	add_to_variable = { VIE_af_equipment_cost_multiplier_modifier = 0.02 tooltip = VIE_tt_equipment_cost }
	add_to_variable = { VIE_af_max_dig_in_factor = -0.02 tooltip = VIE_tt_max_dig_in_factor }
	VIE_lf_fav_discount = yes
	VIE_lf_refresh = yes
}
VIE_lf_fm2_reward = {
	add_to_variable = { VIE_af_army_speed_factor = 0.025 tooltip = VIE_tt_army_speed_factor }
	add_to_variable = { VIE_af_army_attack_factor = 0.02 tooltip = VIE_tt_army_attack_factor }
	add_equipment_to_stockpile = { type = APC_1 amount = 50 producer = VIE }
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 100 producer = VIE }
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_mobile } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_mobile }
		division_template = {
			name = "Cum Co dong"
			regiments = {
				armor_Bat = { x = 0 y = 0 }
				armor_Bat = { x = 0 y = 1 }
				Mech_Inf_Bat = { x = 1 y = 0 }
				Mech_Inf_Bat = { x = 1 y = 1 }
				Mech_Inf_Bat = { x = 1 y = 2 }
				Mech_Inf_Bat = { x = 2 y = 0 }
				SP_Arty_Bat = { x = 2 y = 1 }
				SP_Arty_Bat = { x = 2 y = 2 }
			}
			regimental_support = {
				armor_Recce_Comp = { x = 0 y = 0 }
			}
			support = {
				SP_AA_Battery = { x = 0 y = 0 }
			}
		}
	}
	VIE_lf_refresh = yes
}
VIE_lf_fr1_reward = {
	hidden_effect = { set_country_flag = VIE_lf_regular }
	add_ideas = VIE_regular_corps_spirit
	add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_army_defence_factor = 0.015 tooltip = VIE_tt_army_defence_factor }
	add_to_variable = { VIE_af_army_personnel_cost_multiplier_modifier = 0.02 tooltip = VIE_tt_army_personnel_cost }
	add_to_variable = { VIE_af_experience_gain_army_factor = -0.01 tooltip = VIE_tt_experience_gain_army_factor }
	VIE_lf_fav_discount = yes
	VIE_lf_refresh = yes
}
VIE_lf_fr2_reward = {
	add_to_variable = { VIE_af_army_org_factor = 0.025 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.05 tooltip = VIE_tt_supply_consumption_factor }
	add_equipment_to_stockpile = { type = infantry_weapons_type amount = 1500 producer = VIE }
	add_equipment_to_stockpile = { type = artillery_equipment amount = 30 producer = VIE }
	VIE_lf_refresh = yes
}
VIE_lf_fd1_reward = {
	hidden_effect = { set_country_flag = VIE_lf_depth }
	add_ideas = VIE_depth_defence_spirit
	519 = {
		add_building_construction = {
			type = bunker
			level = 1
			instant_build = yes
			province = { all_provinces = yes limit_to_border = yes }
		}
	}
	518 = {
		add_building_construction = {
			type = bunker
			level = 1
			instant_build = yes
			province = { all_provinces = yes limit_to_border = yes }
		}
	}
	add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
	add_to_variable = { VIE_af_army_defence_factor = 0.015 tooltip = VIE_tt_army_defence_factor }
	add_to_variable = { VIE_af_army_attack_factor = -0.015 tooltip = VIE_tt_army_attack_factor }
	add_to_variable = { VIE_af_army_speed_factor = -0.01 tooltip = VIE_tt_army_speed_factor }
	VIE_lf_fav_discount = yes
	VIE_lf_refresh = yes
}
VIE_lf_fd2_reward = {
	add_to_variable = { VIE_af_conscription_factor = 0.05 tooltip = VIE_tt_conscription_factor }
	add_manpower = 50000
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_militia } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_militia }
		division_template = {
			name = "Dan quan Khu vuc"
			regiments = {
				L_Inf_Bat = { x = 0 y = 0 }
				L_Inf_Bat = { x = 0 y = 1 }
				L_Inf_Bat = { x = 0 y = 2 }
				L_Inf_Bat = { x = 1 y = 0 }
				L_Inf_Bat = { x = 1 y = 1 }
				L_Inf_Bat = { x = 1 y = 2 }
			}
		}
	}
	VIE_lf_refresh = yes
}
VIE_lf_ps_reward = {
	add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
	add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.02 tooltip = VIE_tt_supply_consumption_factor }
	add_to_variable = { VIE_af_equipment_cost_multiplier_modifier = 0.01 tooltip = VIE_tt_equipment_cost }
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 250 producer = VIE }
	VIE_lf_refresh = yes
}
VIE_lf_pt_reward = {
	hidden_effect = { set_country_flag = VIE_lf_dev_territorial }
	add_to_variable = { VIE_af_conscription_factor = 0.035 tooltip = VIE_tt_conscription_factor }
	add_to_variable = { VIE_af_max_dig_in_factor = 0.02 tooltip = VIE_tt_max_dig_in_factor }
	add_to_variable = { VIE_af_army_personnel_cost_multiplier_modifier = 0.01 tooltip = VIE_tt_army_personnel_cost }
	add_manpower = 30000
	VIE_lf_refresh = yes
}
VIE_lf_cr2_reward = {
	add_command_power = 40
	add_to_variable = { VIE_af_planning_speed = 0.15 tooltip = VIE_tt_planning_speed }
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.005 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_speed_factor = 0.01 tooltip = VIE_tt_army_speed_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_army_defence_factor = 0.015 tooltip = VIE_tt_army_defence_factor }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.01 tooltip = VIE_tt_max_dig_in_factor }
	}
	VIE_lf_refresh = yes
}

# Giam 14 ngay cost goc linh vuc so truong (muc 5.4 / G6).
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

VIE_lf_l1_reward = {
	522 = {
		add_building_construction = {
			type = bunker
			level = 1
			instant_build = yes
			province = { all_provinces = yes limit_to_border = yes }
		}
	}
	add_tech_bonus = {
		name = VIE_lf_l1_tech
		bonus = 1.0
		uses = 1
		category = CAT_infantry_weapons
	}
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.005 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.02 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.005 tooltip = VIE_tt_army_defence_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_l2_reward = {
	if = {
		limit = { NOT = { has_country_flag = VIE_lf_tpl_dac_cong } }
		hidden_effect = { set_country_flag = VIE_lf_tpl_dac_cong }
		division_template = {
			name = "Lu doan Dac cong 113"
			regiments = {
				Special_Forces = { x = 0 y = 0 }
				Special_Forces = { x = 0 y = 1 }
				Special_Forces = { x = 0 y = 2 }
				Special_Forces = { x = 1 y = 0 }
				Special_Forces = { x = 1 y = 1 }
				Special_Forces = { x = 1 y = 2 }
			}
			support = {
				Combat_engineer_company = { x = 0 y = 0 }
				L_Recce_Comp = { x = 0 y = 1 }
			}
		}
	}
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_attack_factor = 0.02 tooltip = VIE_tt_army_attack_factor }
		add_to_variable = { VIE_af_army_speed_factor = 0.025 tooltip = VIE_tt_army_speed_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.06 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.025 tooltip = VIE_tt_army_defence_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_a1_reward = {
	add_equipment_to_stockpile = { type = AA_Equipment amount = 100 producer = VIE }
	add_tech_bonus = {
		name = VIE_lf_a1_tech
		bonus = 1.0
		uses = 1
		category = CAT_anti_air
	}
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_speed_factor = 0.01 tooltip = VIE_tt_army_speed_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.02 tooltip = VIE_tt_max_dig_in_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.005 tooltip = VIE_tt_army_defence_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_a2_reward = {
	one_state_radar_station = yes
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.03 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.03 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_org_factor = 0.03 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_army_defence_factor = 0.03 tooltip = VIE_tt_army_defence_factor }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.02 tooltip = VIE_tt_max_dig_in_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_y1_reward = {
	add_ideas = VIE_cyber_command_86
	add_tech_bonus = {
		name = VIE_lf_y1_tech
		bonus = 1.0
		uses = 1
		category = CAT_drones
	}
	if = {
		limit = { has_dlc = "Arms Against Tyranny" }
		mio:VIE_viettel_manufacturer = { add_mio_funds = 200 }
	}
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.02 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_org_factor = 0.005 tooltip = VIE_tt_army_org_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_y2_reward = {
	add_to_variable = { VIE_af_recon_factor = 0.10 tooltip = VIE_tt_recon_factor }
	add_equipment_to_stockpile = { type = util_vehicle_type amount = 100 producer = VIE }
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_attack_factor = 0.03 tooltip = VIE_tt_army_attack_factor }
		add_to_variable = { VIE_af_army_speed_factor = 0.04 tooltip = VIE_tt_army_speed_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_army_defence_factor = 0.03 tooltip = VIE_tt_army_defence_factor }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.02 tooltip = VIE_tt_max_dig_in_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_mod_reward = {
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
	if = {
		limit = { has_completed_focus = VIE_lf_cap_area_control }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.015 tooltip = VIE_tt_max_dig_in_factor }
	}
	if = {
		limit = { has_completed_focus = VIE_lf_cap_ad_coord }
		add_to_variable = { VIE_af_army_defence_factor = 0.01 tooltip = VIE_tt_army_defence_factor }
	}
	if = {
		limit = { has_completed_focus = VIE_lf_cap_info_ops }
		add_to_variable = { VIE_af_army_org_factor = 0.01 tooltip = VIE_tt_army_org_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_cr3_reward = {
	add_command_power = 50
	add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
	add_to_variable = { VIE_af_supply_consumption_factor = -0.04 tooltip = VIE_tt_supply_consumption_factor }
	VIE_lf_refresh = yes
}
VIE_lf_cap_reward = {
	add_ideas = VIE_vpa_modern_army_power
	add_political_power = 100
	VIE_lf_xp_20 = yes
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.02 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.02 tooltip = VIE_tt_army_defence_factor }
		if = {
			limit = { has_completed_focus = VIE_lf_cap_ad_coord }
			add_to_variable = { VIE_af_army_personnel_cost_multiplier_modifier = -0.02 tooltip = VIE_tt_army_personnel_cost }
		}
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_speed_factor = 0.035 tooltip = VIE_tt_army_speed_factor }
		add_to_variable = { VIE_af_army_attack_factor = 0.015 tooltip = VIE_tt_army_attack_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_conscription_factor = 0.035 tooltip = VIE_tt_conscription_factor }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.03 tooltip = VIE_tt_max_dig_in_factor }
	}
	hidden_effect = { set_country_flag = VIE_lf_done }
	VIE_lf_refresh = yes
}"""

updated_text = text[:p_start] + new_rewards + text[p_end:]

with open('common/scripted_effects/VIE_md_effects_p17.txt', 'w', encoding='utf-8') as f:
    f.write(updated_text)

# Also remove duplicate loc from replace/ directory
replace_loc = 'localisation/english/replace/VIE_army_revamp_l_english.yml'
if os.path.exists(replace_loc):
    os.remove(replace_loc)
    print("Removed duplicate replace file:", replace_loc)

print("Updated VIE_md_effects_p17.txt with valid subunits and restored fav_discount!")
