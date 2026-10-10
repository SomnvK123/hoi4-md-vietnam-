import re
from pathlib import Path

FOCUS_FILE = Path('common/national_focus/VIE_md_focus.txt')
content = FOCUS_FILE.read_text(encoding='utf-8')

# 1. Strategy M replacement block
# We want:
# - VIE_lf_fs_main_corps: x = -8, relative_position_id = VIE_lf_command_reform_1
# - VIE_lf_fs_lean_corps: x = -2, relative_position_id = VIE_lf_fs_main_corps
# - VIE_lf_mech_fire_support: x = 0, relative_position_id = VIE_lf_fs_lean_corps
# - VIE_lf_mech_coordination: x = 2, relative_position_id = VIE_lf_fs_main_corps
# - VIE_lf_mech_complete: x = 2, relative_position_id = VIE_lf_mech_fire_support
#   prerequisites: mech_coordination and mech_fire_support

# Let's inspect the entire block from 'id = VIE_lf_fs_main_corps' to 'id = VIE_lf_command_reform_2'
m_start = content.find('id = VIE_lf_fs_main_corps')
# find focus = { before it
f_start = content.rfind('focus = {', 0, m_start)

# find end of VIE_lf_command_reform_2
cr2_idx = content.find('id = VIE_lf_command_reform_2')
cr2_end = content.find('\n\t}', cr2_idx) + len('\n\t}')

print(f"Replacing from index {f_start} to {cr2_end}")

new_middle_block = '''focus = {
		id = VIE_lf_fs_main_corps
		icon = GFX_focus_VIE_lf_fs_main_corps

		x = -8
		y = 1
		relative_position_id = VIE_lf_command_reform_1

		cost = 7

		mutually_exclusive = { focus = VIE_lf_fs_mobile_force focus = VIE_lf_fs_depth_defence }

		prerequisite = { focus = VIE_lf_command_reform_1 }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_fs_main_corps"
			VIE_lf_fr1_reward = yes
		}

		ai_will_do = {
			base = 40
			modifier = { factor = 1.5 VIE_ai_historical = yes }
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_fs_lean_corps
		icon = GFX_focus_VIE_lf_fs_lean_corps

		x = -2
		y = 1
		relative_position_id = VIE_lf_fs_main_corps

		cost = 5

		prerequisite = { focus = VIE_lf_fs_main_corps }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_fs_lean_corps"
			VIE_lf_fr2_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_mech_fire_support
		icon = GFX_focus_VIE_lf_arm_arty_train

		x = 0
		y = 1
		relative_position_id = VIE_lf_fs_lean_corps

		cost = 5

		prerequisite = { focus = VIE_lf_fs_lean_corps }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mech_fire_support"
			VIE_lf_mech_fire_support_reward = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_mech_coordination
		icon = GFX_focus_VIE_lf_arm_armor_train

		x = 2
		y = 1
		relative_position_id = VIE_lf_fs_main_corps

		cost = 5

		prerequisite = { focus = VIE_lf_fs_main_corps }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mech_coordination"
			VIE_lf_mech_coordination_reward = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_mech_equipment
		icon = GFX_focus_VIE_lf_arm_armor_train

		x = 0
		y = 1
		relative_position_id = VIE_lf_arm_armor_train

		cost = 7

		prerequisite = { focus = VIE_lf_arm_armor_train }
		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mech_equipment"
			VIE_lf_mech_equipment_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_mech_sustainment
		icon = GFX_focus_VIE_lf_logistics_merge

		x = 0
		y = 1
		relative_position_id = VIE_lf_arm_engineer_train

		cost = 5

		prerequisite = { focus = VIE_lf_arm_engineer_train }
		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mech_sustainment"
			VIE_lf_mech_sustainment_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_mech_complete
		icon = GFX_focus_VIE_lf_combined_arms

		x = 2
		y = 1
		relative_position_id = VIE_lf_mech_fire_support

		cost = 7

		prerequisite = { focus = VIE_lf_mech_coordination }
		prerequisite = { focus = VIE_lf_mech_fire_support }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mech_complete"
			VIE_lf_mech_complete_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_fs_mobile_force
		icon = GFX_focus_VIE_lf_fs_mobile_force

		x = 0
		y = 1
		relative_position_id = VIE_lf_command_reform_1

		cost = 7

		mutually_exclusive = { focus = VIE_lf_fs_main_corps focus = VIE_lf_fs_depth_defence }

		prerequisite = { focus = VIE_lf_command_reform_1 }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_fs_mobile_force"
			VIE_lf_fm1_reward = yes
		}

		ai_will_do = {
			base = 40
			modifier = { factor = 0.25 VIE_ai_historical = yes }
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_fs_mobile_corps
		icon = GFX_focus_VIE_lf_fs_mobile_corps

		x = -2
		y = 1
		relative_position_id = VIE_lf_fs_mobile_force

		cost = 5

		prerequisite = { focus = VIE_lf_fs_mobile_force }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_fs_mobile_corps"
			VIE_lf_fm2_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_mobile_sustainment
		icon = GFX_focus_VIE_lf_logistics_merge

		x = 0
		y = 1
		relative_position_id = VIE_lf_fs_mobile_corps

		cost = 5

		prerequisite = { focus = VIE_lf_fs_mobile_corps }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mobile_sustainment"
			VIE_lf_mobile_sustainment_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_mobile_fire_support
		icon = GFX_focus_VIE_lf_arm_arty_train

		x = 2
		y = 1
		relative_position_id = VIE_lf_fs_mobile_force

		cost = 7

		prerequisite = { focus = VIE_lf_fs_mobile_force }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_mobile_fire_support"
			VIE_lf_mobile_fire_support_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_dev_strategic
		icon = GFX_focus_VIE_lf_dev_strategic

		x = 2
		y = 1
		relative_position_id = VIE_lf_mobile_sustainment

		cost = 7

		prerequisite = { focus = VIE_lf_mobile_fire_support }
		prerequisite = { focus = VIE_lf_mobile_sustainment }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_dev_strategic"
			VIE_lf_ps_reward = yes
		}

		ai_will_do = {
			base = 40
			modifier = { factor = 1.5 VIE_ai_historical = yes }
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_fs_depth_defence
		icon = GFX_focus_VIE_lf_fs_depth_defence

		x = 8
		y = 1
		relative_position_id = VIE_lf_command_reform_1

		cost = 7

		mutually_exclusive = { focus = VIE_lf_fs_main_corps focus = VIE_lf_fs_mobile_force }

		prerequisite = { focus = VIE_lf_command_reform_1 }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_fs_depth_defence"
			VIE_lf_fd1_reward = yes
		}

		ai_will_do = {
			base = 40
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_fs_militia_units
		icon = GFX_focus_VIE_lf_fs_militia_units

		x = -2
		y = 1
		relative_position_id = VIE_lf_fs_depth_defence

		cost = 5

		prerequisite = { focus = VIE_lf_fs_depth_defence }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_fs_militia_units"
			VIE_lf_fd2_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_territorial_coordination
		icon = GFX_focus_VIE_lf_arm_engineers

		x = 2
		y = 1
		relative_position_id = VIE_lf_fs_depth_defence

		cost = 5

		prerequisite = { focus = VIE_lf_fs_depth_defence }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_territorial_coordination"
			VIE_lf_territorial_coordination_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_territorial_reserve
		icon = GFX_focus_VIE_lf_basic_training

		x = 0
		y = 2
		relative_position_id = VIE_lf_fs_depth_defence

		cost = 7

		prerequisite = { focus = VIE_lf_fs_depth_defence }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_territorial_reserve"
			VIE_lf_territorial_reserve_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_dev_territorial
		icon = GFX_focus_VIE_lf_dev_territorial

		x = 0
		y = 1
		relative_position_id = VIE_lf_territorial_reserve

		cost = 7

		prerequisite = { focus = VIE_lf_fs_militia_units }
		prerequisite = { focus = VIE_lf_territorial_reserve }
		prerequisite = { focus = VIE_lf_territorial_coordination }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_dev_territorial"
			VIE_lf_pt_reward = yes
		}

		ai_will_do = {
			base = 40
			modifier = { factor = 1.5 VIE_ai_historical = yes }
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}

	focus = {
		id = VIE_lf_command_reform_2
		icon = GFX_focus_VIE_lf_command_reform_2

		x = 0
		y = 1
		relative_position_id = VIE_lf_dev_strategic

		prerequisite = { focus = VIE_lf_mech_complete focus = VIE_lf_dev_strategic focus = VIE_lf_dev_territorial }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_command_reform_2"
			VIE_lf_cr2_reward = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 3 date > 2023.12.1 }
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}'''

content_updated = content[:f_start] + new_middle_block + content[cr2_end:]
FOCUS_FILE.write_text(content_updated, encoding='utf-8')
print("Successfully replaced middle block in VIE_md_focus.txt")
