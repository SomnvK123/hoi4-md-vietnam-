import re
from pathlib import Path

# Paths
FOCUS_FILE = Path('common/national_focus/VIE_md_focus.txt')
TRIGGERS_FILE = Path('common/scripted_triggers/VIE_md_triggers_hardline.txt')
EFFECTS_FILE = Path('common/scripted_effects/VIE_md_effects_hardline.txt')
LOC_FILE = Path('localisation/english/VIE_md_hardline_l_english.yml')

OLD_21_FOCUSES = set([
    'VIE_hl_soe_first',
    'VIE_hl_party_rectification',
    'VIE_hl_vpa_supreme',
    'VIE_hl_icp_legacy',
    'VIE_hl_curb_private_capital',
    'VIE_hl_central_inspection',
    'VIE_hl_ideological_commissars',
    'VIE_hl_viet_lao_special_integration',
    'VIE_hl_five_year_plan',
    'VIE_hl_national_firewall',
    'VIE_hl_defense_self_reliance',
    'VIE_hl_cambodia_revolutionary_front',
    'VIE_hl_strategic_resources',
    'VIE_hl_revolutionary_tribunals',
    'VIE_hl_peoples_war_doctrine',
    'VIE_hl_indochinese_consultative_congress',
    'VIE_hl_socialist_industrialization',
    'VIE_hl_iron_discipline_state',
    'VIE_hl_vietnam_shield',
    'VIE_hl_indochinese_socialist_union',
    'VIE_hl_unbreakable_fortress',
])

def find_all_focuses(text):
    focuses = []
    for m in re.finditer(r'\n[ \t]*focus\s*=\s*\{', text):
        st = m.end()
        d = 1
        i = st
        while d > 0 and i < len(text):
            if text[i] == '{': d += 1
            elif text[i] == '}': d -= 1
            i += 1
        body = text[st:i-1]
        fid_m = re.search(r'\bid\s*=\s*(\w+)', body)
        if fid_m:
            fid = fid_m.group(1)
            line_start = m.start()
            end_pos = i
            while end_pos < len(text) and text[end_pos] in ' \t\r\n':
                end_pos += 1
            focuses.append({
                'id': fid,
                'start': line_start,
                'end': end_pos,
                'body': body
            })
    return focuses

print("--- Step 1: Finding and cutting 21 old focuses from VIE_md_focus.txt ---")
focus_text = FOCUS_FILE.read_text(encoding='utf-8')
parsed_focuses = find_all_focuses(focus_text)

to_remove = [f for f in parsed_focuses if f['id'] in OLD_21_FOCUSES]
print(f"Found {len(to_remove)} of {len(OLD_21_FOCUSES)} old focuses to remove:")
for f in to_remove:
    print(f"  Removing {f['id']} (chars {f['start']}..{f['end']})")

assert len(to_remove) == 21, f"Expected 21 focuses to remove, found {len(to_remove)}"

# Remove in reverse order of start position so indices remain valid
for f in sorted(to_remove, key=lambda x: x['start'], reverse=True):
    focus_text = focus_text[:f['start']] + focus_text[f['end']:]

print("--- Step 2: Updating external references in VIE_md_focus.txt ---")
# 1. Shortcut
focus_text = focus_text.replace('target = VIE_hl_soe_first', 'target = VIE_hl_unity_of_will')

# 2. Congress 14 options exclusions and era of rising
focus_text = re.sub(
    r'mutually_exclusive\s*=\s*\{\s*focus\s*=\s*VIE_institutional_opening\s+focus\s*=\s*VIE_hl_unbreakable_fortress\s*\}',
    'mutually_exclusive = { focus = VIE_institutional_opening }',
    focus_text
)
focus_text = re.sub(
    r'mutually_exclusive\s*=\s*\{\s*focus\s*=\s*VIE_concentration_of_power\s+focus\s*=\s*VIE_hl_unbreakable_fortress\s*\}',
    'mutually_exclusive = { focus = VIE_concentration_of_power }',
    focus_text
)
focus_text = re.sub(
    r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_concentration_of_power\s+focus\s*=\s*VIE_institutional_opening\s+focus\s*=\s*VIE_hl_unbreakable_fortress\s*\}',
    'prerequisite = { focus = VIE_concentration_of_power focus = VIE_institutional_opening }',
    focus_text
)

# 3. Old hl focus checks in economic / other focuses
focus_text = re.sub(
    r'NOT\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_hl_curb_private_capital\s*\}',
    'NOT = { has_completed_focus = VIE_hl_no_party_business }',
    focus_text
)
focus_text = re.sub(
    r'NOT\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_hl_soe_first\s*\}',
    'NOT = { has_completed_focus = VIE_hl_state_sector_leading }',
    focus_text
)
focus_text = re.sub(
    r'NOT\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_hl_iron_discipline_state\s*\}',
    'NOT = { has_completed_focus = VIE_hl_party_state_fusion }',
    focus_text
)

print("--- Step 3: Generating 25 new Hardline focuses ---")
NEW_HARDLINE_SECTION = """
	#############################################################
	## CON ĐƯỜNG KIÊN ĐỊNH (CPV HARDLINE - RULING PARTY 4)
	## Cây độc lập hoàn toàn, 25 focus (H0 -> X3)
	## Bố cục 4 trụ song song + trục trung tâm (Y=23..31, X=6..22)
	#############################################################

	# H0: Gốc cây Kiên định
	focus = {
		id = VIE_hl_unity_of_will
		icon = legislative_palace

		x = 0
		y = 2
		relative_position_id = VIE_party_centennial_2030

		cost = 5

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_unity_of_will"
			add_political_power = 50
			VIE_bop_conservative_small = yes
			if = {
				limit = { NOT = { check_variable = { VIE_rp > 0 } } }
				set_variable = { VIE_rp = 20 }
			}
			VIE_hl_update_pressure_idea = yes
		}

		ai_will_do = { base = 100 }
	}

	# H1: Chỉnh đốn Đảng
	focus = {
		id = VIE_hl_party_rectification
		icon = Generic_Political_Purge

		x = 0
		y = 1
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_unity_of_will }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_rectification"
			add_stability = 0.02
			decrease_corruption = yes
			set_temp_variable = { temp_opinion = 3 }
			change_communist_cadres_opinion = yes
			set_temp_variable = { temp_opinion = -4 }
			change_industrial_conglomerates_opinion = yes
			add_timed_idea = { idea = VIE_official_caution days = 365 }
			if = {
				limit = { has_completed_focus = VIE_clean_cadres }
				set_temp_variable = { VIE_rp_add = 4 }
				custom_effect_tooltip = VIE_hl_rp_p4_tt
			}
			else = {
				set_temp_variable = { VIE_rp_add = 6 }
				custom_effect_tooltip = VIE_hl_rp_p6_tt
			}
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# H2: Bảo vệ nền tảng tư tưởng
	focus = {
		id = VIE_hl_ideological_foundation
		icon = propaganda

		x = -4
		y = 1
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_unity_of_will }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_ideological_foundation"
			add_political_power = 50
			add_ideas = VIE_hl_ideology_work_idea
			set_temp_variable = { VIE_rp_add = 4 }
			custom_effect_tooltip = VIE_hl_rp_p4_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# H3: Thống nhất quản lý cán bộ
	focus = {
		id = VIE_hl_cadre_centralisation
		icon = communist_purge

		x = 0
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_rectification }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_cadre_centralisation"
			VIE_bop_conservative_small = yes
			if = {
				limit = { has_completed_focus = VIE_decentralization }
				set_temp_variable = { VIE_rp_add = 7 }
				custom_effect_tooltip = VIE_hl_rp_p7_tt
			}
			else = {
				set_temp_variable = { VIE_rp_add = 4 }
				custom_effect_tooltip = VIE_hl_rp_p4_tt
			}
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A1: Kinh tế nhà nước chủ đạo
	focus = {
		id = VIE_hl_state_sector_leading
		icon = focus_generic_central_planning

		x = -4
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_rectification }

		search_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
			NOT = { has_completed_focus = VIE_soe_rapid_divestment }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_state_sector_leading"
			set_temp_variable = { treasury_change = 2 }
			modify_treasury_effect = yes
			add_ideas = VIE_hl_state_leading_idea
			add_timed_idea = { idea = VIE_hl_state_transition_idea days = 730 }
			set_temp_variable = { temp_opinion = 4 }
			change_communist_cadres_opinion = yes
			set_temp_variable = { temp_opinion = -4 }
			change_industrial_conglomerates_opinion = yes
			if = {
				limit = { has_completed_focus = VIE_state_conglomerates }
				add_political_power = 25
			}
			set_temp_variable = { VIE_rp_add = 4 }
			custom_effect_tooltip = VIE_hl_rp_p4_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A2: Danh mục ngành then chốt
	focus = {
		id = VIE_hl_key_sectors
		icon = economic_civil_industry

		x = -4
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_state_sector_leading }

		search_filters = { FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
			NOT = { has_country_flag = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_key_sectors"
			one_state_industrial_complex = yes
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A3: Tập đoàn đầu tàu
	focus = {
		id = VIE_hl_soe_spearhead
		icon = economic_prosperity

		x = -2
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_state_sector_leading }

		search_filters = { FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_soe_spearhead"
			increase_economic_growth = yes
			add_timed_idea = { idea = VIE_hl_soe_spearhead_idea days = 730 }
			add_to_variable = { var = VIE_vinashin_risk value = 2 }
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A4: Kiểm soát dòng vốn, FDI
	focus = {
		id = VIE_hl_selective_fdi
		icon = asian_investment

		x = -2
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_key_sectors }

		search_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_selective_fdi"
			add_stability = 0.01
			add_political_power = 25
			set_temp_variable = { treasury_change = -2 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_hl_fdi_slowdown_idea days = 365 }
			if = { limit = { country_exists = USA } add_opinion_modifier = { target = USA modifier = small_decrease } }
			if = { limit = { country_exists = JAP } add_opinion_modifier = { target = JAP modifier = small_decrease } }
			if = { limit = { country_exists = KOR } add_opinion_modifier = { target = KOR modifier = small_decrease } }
			set_temp_variable = { VIE_rp_add = 6 }
			custom_effect_tooltip = VIE_hl_rp_p6_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A5: Đảng viên không làm kinh tế tư nhân
	focus = {
		id = VIE_hl_no_party_business
		icon = anti_corruption

		x = -6
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_rectification }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
			NOT = { has_completed_focus = VIE_private_champions }
			NOT = { has_completed_focus = VIE_private_sector_engine }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_no_party_business"
			VIE_bop_conservative_small = yes
			set_temp_variable = { temp_opinion = 3 }
			change_communist_cadres_opinion = yes
			set_temp_variable = { temp_opinion = -5 }
			change_industrial_conglomerates_opinion = yes
			set_temp_variable = { VIE_rp_add = 5 }
			custom_effect_tooltip = VIE_hl_rp_p5_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 40
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A6: Kế hoạch định hướng 5 năm
	focus = {
		id = VIE_hl_five_year_plan
		icon = five_year_plan

		x = -4
		y = 5
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_soe_spearhead focus = VIE_hl_selective_fdi }

		search_filters = { FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_five_year_plan"
			set_temp_variable = { treasury_change = 3 }
			modify_treasury_effect = yes
			add_ideas = VIE_hl_planning_idea
			set_temp_variable = { VIE_rp_add = 3 }
			custom_effect_tooltip = VIE_hl_rp_p3_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# B1: Đảng lãnh đạo tuyệt đối quân đội
	focus = {
		id = VIE_hl_party_leads_army
		icon = GFX_focus_generic_military_mission

		x = 4
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_unity_of_will }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
			has_completed_focus = VIE_modernize_vpa
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_leads_army"
			set_temp_variable = { temp_opinion = 3 }
			change_the_military_opinion = yes
			VIE_bop_conservative_small = yes
			add_ideas = VIE_hl_army_party_work_idea
			army_experience = 10
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# B2: Giáo dục chính trị LLVT
	focus = {
		id = VIE_hl_army_political_education
		icon = GFX_focus_generic_military_mission

		x = 4
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 5

		prerequisite = { focus = VIE_hl_party_leads_army }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_WAR_SUPPORT }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_army_political_education"
			add_war_support = 0.03
			army_experience = 10
			set_temp_variable = { treasury_change = -1 }
			modify_treasury_effect = yes
			set_temp_variable = { VIE_rp_add = 1 }
			custom_effect_tooltip = VIE_hl_rp_p1_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 50 }
	}

	# B3: Thế trận quốc phòng toàn dân
	focus = {
		id = VIE_hl_all_people_defence
		icon = GFX_focus_generic_military_mission

		x = 4
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_leads_army }

		search_filters = { FOCUS_FILTER_ARMY }

		available = {
			VIE_hl_in_power = yes
			has_completed_focus = VIE_peoples_defence
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_all_people_defence"
			add_ideas = VIE_hl_all_people_defence_idea
			set_temp_variable = { VIE_rp_add = 3 }
			custom_effect_tooltip = VIE_hl_rp_p3_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 50 }
	}

	# B4: CN Quốc phòng do Đảng chỉ đạo
	focus = {
		id = VIE_hl_party_defence_industry
		icon = GFX_focus_generic_military_mission

		x = 4
		y = 5
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_army_political_education }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_defence_industry"
			if = {
				limit = { has_completed_focus = VIE_military_enterprises_core }
				add_to_variable = { var = VIE_def_industry_level value = 1 }
			}
			else_if = {
				limit = { has_completed_focus = VIE_military_enterprises_divest }
				add_political_power = 50
				add_stability = 0.01
			}
			else = {
				add_political_power = 25
			}
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 60 }
	}

	# C1: Bảo vệ nền tảng tư tưởng không gian mạng
	focus = {
		id = VIE_hl_cyber_ideology
		icon = army_cyberwar

		x = -8
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_ideological_foundation }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_cyber_ideology"
			add_ideas = VIE_hl_cyber_content_idea
			if = { limit = { country_exists = USA } add_opinion_modifier = { target = USA modifier = small_decrease } }
			set_temp_variable = { VIE_rp_add = 7 }
			custom_effect_tooltip = VIE_hl_rp_p7_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# C2: Giáo dục lý luận chính trị
	focus = {
		id = VIE_hl_school_theory
		icon = GFX_focus_AFG_education_reform

		x = -8
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_ideological_foundation }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_school_theory"
			add_stability = 0.02
			set_temp_variable = { temp_opinion = 2 }
			change_communist_cadres_opinion = yes
			add_timed_idea = { idea = VIE_hl_school_theory_idea days = 730 }
			set_temp_variable = { VIE_rp_add = 3 }
			custom_effect_tooltip = VIE_hl_rp_p3_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# C3: Quy hoạch báo chí
	focus = {
		id = VIE_hl_press_planning
		icon = sov_free_media

		x = -8
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 5

		prerequisite = { focus = VIE_hl_cyber_ideology }

		search_filters = { FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_press_planning"
			add_political_power = 50
			if = { limit = { country_exists = USA } add_opinion_modifier = { target = USA modifier = small_decrease } }
			if = { limit = { country_exists = FRA } add_opinion_modifier = { target = FRA modifier = small_decrease } }
			set_temp_variable = { VIE_rp_add = 6 }
			custom_effect_tooltip = VIE_hl_rp_p6_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# C4: Mặt trận Tổ quốc và Đoàn thể
	focus = {
		id = VIE_hl_fatherland_front
		icon = treaty2

		x = 0
		y = 6
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_school_theory focus = VIE_hl_cadre_centralisation }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_fatherland_front"
			set_temp_variable = { temp_opinion = 4 }
			change_farmers_opinion = yes
			add_stability = 0.02
			set_temp_variable = { VIE_rp_add = -4 }
			custom_effect_tooltip = VIE_hl_rp_m4_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 3 check_variable = { VIE_rp > 55 } }
		}
	}

	# D1: Đối ngoại Đảng
	focus = {
		id = VIE_hl_party_diplomacy
		icon = diplomatic_treaty

		x = 8
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_unity_of_will }

		search_filters = { FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_diplomacy"
			add_political_power = 50
			if = { limit = { country_exists = LAO } add_opinion_modifier = { target = LAO modifier = large_increase } }
			if = { limit = { country_exists = CHI } add_opinion_modifier = { target = CHI modifier = large_increase } }
			if = { limit = { country_exists = CUB } add_opinion_modifier = { target = CUB modifier = large_increase } }
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 50 }
	}

	# D2: Hợp tác không lệ thuộc
	focus = {
		id = VIE_hl_no_dependence
		icon = diplomacy

		x = 8
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_diplomacy }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_WAR_SUPPORT }

		available = {
			VIE_hl_in_power = yes
			has_completed_focus = VIE_four_nos_doctrine
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_no_dependence"
			add_war_support = 0.03
			add_stability = 0.01
			hidden_effect = { set_country_flag = VIE_hl_sovereignty_line }
			if = { limit = { country_exists = CHI } add_opinion_modifier = { target = CHI modifier = small_decrease } }
		}

		ai_will_do = { base = 60 }
	}

	# D3: Đối tác chiến lược chọn lọc
	focus = {
		id = VIE_hl_selective_partners
		icon = treaty2

		x = 8
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_no_dependence }

		search_filters = { FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
			OR = {
				has_completed_focus = VIE_japan_partnership
				has_completed_focus = VIE_india_partnership
				has_completed_focus = VIE_korea_partnership
			}
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_selective_partners"
			if = { limit = { country_exists = JAP } add_opinion_modifier = { target = JAP modifier = large_increase } }
			if = { limit = { country_exists = RAJ } add_opinion_modifier = { target = RAJ modifier = large_increase } }
			if = { limit = { country_exists = KOR } add_opinion_modifier = { target = KOR modifier = large_increase } }
			set_temp_variable = { temp_opinion = -2 }
			change_communist_cadres_opinion = yes
			VIE_bop_reform_small = yes
			set_temp_variable = { VIE_rp_add = -10 }
			custom_effect_tooltip = VIE_hl_rp_m10_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 3 check_variable = { VIE_rp > 55 } }
		}
	}

	# E1: Tổng kết nhiệm kỳ
	focus = {
		id = VIE_hl_term_review
		icon = legislative_palace

		x = 0
		y = 7
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_cadre_centralisation }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
			VIE_hl_pillars_three = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_term_review"
			add_political_power = 100
			add_stability = 0.03
			hidden_effect = { set_country_flag = VIE_hl_e1_done }
			country_event = { id = vie_hl.5 days = 3 }
		}

		ai_will_do = { base = 100 }
	}

	# X1: Kiên định mục tiêu, đổi mới phương thức
	focus = {
		id = VIE_hl_steadfast_renewal
		icon = economic_prosperity2

		x = -4
		y = 8
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_term_review }

		mutually_exclusive = { focus = VIE_hl_party_state_fusion focus = VIE_hl_handover }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
			custom_trigger_tooltip = {
				tooltip = VIE_hl_rp_below_80_tt
				check_variable = { VIE_rp < 80 }
			}
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_steadfast_renewal"
			increase_economic_growth = yes
			add_ideas = VIE_hl_controlled_renewal_idea
			set_temp_variable = { temp_opinion = -3 }
			change_communist_cadres_opinion = yes
			if = {
				limit = { has_country_flag = VIE_bop_active }
				set_power_balance = { id = VIE_party_balance set_value = -0.3 }
			}
			set_temp_variable = { VIE_rp_add = -25 }
			custom_effect_tooltip = VIE_hl_rp_m25_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 60 }
	}

	# X2: Nhất thể hóa
	focus = {
		id = VIE_hl_party_state_fusion
		icon = legislative_palace

		x = 0
		y = 8
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_term_review }

		mutually_exclusive = { focus = VIE_hl_steadfast_renewal focus = VIE_hl_handover }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
			VIE_hl_pillars_all = yes
			has_completed_focus = VIE_hl_press_planning
			VIE_bop_is_hardline = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_state_fusion"
			add_political_power = 150
			add_stability = 0.05
			add_ideas = VIE_hl_fusion_idea
			hidden_effect = { set_country_flag = VIE_hl_fusion_done }
			set_temp_variable = { VIE_rp_add = 8 }
			custom_effect_tooltip = VIE_hl_rp_p8_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 20
			modifier = { factor = 0 check_variable = { VIE_rp > 69 } }
		}
	}

	# X3: Bàn giao đường lối
	focus = {
		id = VIE_hl_handover
		icon = election2

		x = 4
		y = 8
		relative_position_id = VIE_hl_unity_of_will

		cost = 5

		prerequisite = { focus = VIE_hl_term_review }

		mutually_exclusive = { focus = VIE_hl_steadfast_renewal focus = VIE_hl_party_state_fusion }

		search_filters = { FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
			custom_trigger_tooltip = {
				tooltip = VIE_hl_rp_below_56_tt
				check_variable = { VIE_rp < 56 }
			}
			NOT = { has_idea = VIE_hl_self_reliance_idea }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_handover"
			custom_effect_tooltip = VIE_hl_handover_tt
			hidden_effect = {
				set_temp_variable = { rul_party_temp = 19 }
				set_temp_variable = { VIE_hl_keep_legacy = 1 }
				VIE_transition_regime = yes
				if = {
					limit = { has_country_flag = VIE_bop_active }
					set_power_balance = { id = VIE_party_balance set_value = -0.3 }
				}
				set_country_flag = { flag = VIE_hardline_retired value = 1 days = 3650 }
			}
			add_political_power = 100
			add_stability = 0.05
		}

		ai_will_do = { base = 20 }
	}
"""

# Insert right after VIE_party_centennial_2030 block
centennial_idx = focus_text.find('id = VIE_party_centennial_2030')
if centennial_idx == -1:
    raise ValueError("VIE_party_centennial_2030 not found!")

# Find end of VIE_party_centennial_2030 focus block
pos = centennial_idx
brace = 0
found_first_brace = False
while pos < len(focus_text):
    if focus_text[pos] == '{':
        brace += 1
        found_first_brace = True
    elif focus_text[pos] == '}':
        brace -= 1
        if found_first_brace and brace == 0:
            pos += 1
            break
    pos += 1

focus_text = focus_text[:pos] + "\n" + NEW_HARDLINE_SECTION + "\n" + focus_text[pos:]
FOCUS_FILE.write_text(focus_text, encoding='utf-8')
print("VIE_md_focus.txt successfully updated!")

print("--- Step 4: Updating VIE_md_triggers_hardline.txt ---")
trig_text = TRIGGERS_FILE.read_text(encoding='utf-8')
trig_text = re.sub(
    r'VIE_hl_pillars_three\s*=\s*\{[\s\S]*?custom_trigger_tooltip\s*=\s*\{\s*tooltip\s*=\s*VIE_hl_pillars_three_tt\s*count_triggers\s*=\s*\{\s*amount\s*=\s*3[\s\S]*?\}\s*\}\s*\}',
    '''VIE_hl_pillars_three = {
	custom_trigger_tooltip = {
		tooltip = VIE_hl_pillars_three_tt
		count_triggers = {
			amount = 3
			has_completed_focus = VIE_hl_five_year_plan
			has_completed_focus = VIE_hl_party_defence_industry
			has_completed_focus = VIE_hl_fatherland_front
			has_completed_focus = VIE_hl_no_dependence
		}
	}
}''',
    trig_text
)

trig_text = re.sub(
    r'VIE_hl_pillars_all\s*=\s*\{[\s\S]*?custom_trigger_tooltip\s*=\s*\{\s*tooltip\s*=\s*VIE_hl_pillars_all_tt[\s\S]*?\}\s*\}',
    '''VIE_hl_pillars_all = {
	custom_trigger_tooltip = {
		tooltip = VIE_hl_pillars_all_tt
		has_completed_focus = VIE_hl_five_year_plan
		has_completed_focus = VIE_hl_party_defence_industry
		has_completed_focus = VIE_hl_fatherland_front
		has_completed_focus = VIE_hl_no_dependence
	}
}''',
    trig_text
)
TRIGGERS_FILE.write_text(trig_text, encoding='utf-8')
print("VIE_md_triggers_hardline.txt successfully updated!")

print("--- Step 5: Updating VIE_md_effects_hardline.txt ---")
eff_text = EFFECTS_FILE.read_text(encoding='utf-8')
eff_text = eff_text.replace('has_completed_focus = VIE_hl_curb_private_capital', 'has_completed_focus = VIE_hl_selective_fdi')
eff_text = eff_text.replace('has_completed_focus = VIE_hl_national_firewall', 'has_completed_focus = VIE_hl_cyber_ideology')
eff_text = eff_text.replace('has_completed_focus = VIE_hl_icp_legacy', 'has_completed_focus = VIE_hl_party_diplomacy')
eff_text = eff_text.replace('has_completed_focus = VIE_hl_socialist_industrialization', 'has_completed_focus = VIE_hl_five_year_plan')
EFFECTS_FILE.write_text(eff_text, encoding='utf-8')
print("VIE_md_effects_hardline.txt successfully updated!")

print("--- Step 6: Updating Localization in VIE_md_hardline_l_english.yml ---")
loc_text = LOC_FILE.read_text(encoding='utf-8-sig')

NEW_FOCUS_LOCS = """
 # ============================================================
 # CON DUONG KIEN DINH - 25 FOCUSES (MODEL B / V3)
 # ============================================================
 VIE_hl_unity_of_will:0 "Thống nhất Ý chí & Giữ vững Bản lĩnh"
 VIE_hl_unity_of_will_desc:0 "Khẳng định lập trường kiên định của Đảng Cộng sản Việt Nam, củng cố sự thống nhất ý chí và hành động trong toàn Đảng, toàn quân và toàn dân."

 VIE_hl_party_rectification:0 "Chỉnh đốn Đảng & Lập trường Giai cấp"
 VIE_hl_party_rectification_desc:0 "Triển khai đợt sinh hoạt chính trị sâu rộng trong toàn Đảng; kiên quyết loại bỏ các phần tử cơ hội, dao động tư tưởng, giữ vững bản chất cách mạng của giai cấp công nhân."

 VIE_hl_ideological_foundation:0 "Bảo vệ Nền tảng Tư tưởng của Đảng"
 VIE_hl_ideological_foundation_desc:0 "Tăng nguồn lực cho Ban Tuyên giáo và hệ thống Học viện Chính trị; kiên định chủ nghĩa Mác - Lênin và tư tưởng Hồ Chí Minh là kim chỉ nam cho mọi hành động."

 VIE_hl_cadre_centralisation:0 "Thống nhất Quản lý Cán bộ"
 VIE_hl_cadre_centralisation_desc:0 "Tăng cường sự kiểm soát tập trung của Trung ương đối với việc quy hoạch, bổ nhiệm và quản lý cán bộ chủ chốt, thu hẹp quyền tự quyết phân tán ở các địa phương."

 VIE_hl_state_sector_leading:0 "Kinh tế Nhà nước giữ Vai trò Chủ đạo"
 VIE_hl_state_sector_leading_desc:0 "Khẳng định kinh tế nhà nước giữ vai trò chủ đạo tuyệt đối trong nền kinh tế quốc dân. Đình chỉ quá trình thoái vốn ồ ạt các tập đoàn chiến lược."

 VIE_hl_key_sectors:0 "Danh mục Ngành Then chốt"
 VIE_hl_key_sectors_desc:0 "Năng lượng, ngân hàng, viễn thông, khoáng sản và quốc phòng: Nhà nước nắm quyền chi phối tuyệt đối, bảo đảm an ninh kinh tế quốc gia."

 VIE_hl_soe_spearhead:0 "Tập đoàn Nhà nước làm Đầu tàu"
 VIE_hl_soe_spearhead_desc:0 "Giao trọng trách cho các tập đoàn tổng công ty nhà nước dẫn dắt các đại dự án hạ tầng, công nghiệp nặng và phát triển công nghệ cao."

 VIE_hl_selective_fdi:0 "Kiểm soát Dòng vốn & Thu hút FDI Chọn lọc"
 VIE_hl_selective_fdi_desc:0 "Thiết lập hàng rào kiểm soát chặt chẽ các dòng vốn đầu tư gián tiếp và dòng vốn đầu cơ, chỉ ưu tiên dự án FDI chuyển giao công nghệ thực chất."

 VIE_hl_no_party_business:0 "Đảng viên không làm Kinh tế Tư nhân"
 VIE_hl_no_party_business_desc:0 "Bác bỏ việc đảng viên tham gia làm kinh tế tư nhân nhằm trục lợi; ngăn chặn các nhóm tư bản lũng đoạn chi phối chính sách của Đảng và Nhà nước."

 VIE_hl_five_year_plan:0 "Kế hoạch Định hướng 5 năm"
 VIE_hl_five_year_plan_desc:0 "Tập trung nguồn vốn và tài nguyên quốc gia vào các mục tiêu kế hoạch hóa trung hạn, bảo đảm phát triển đồng bộ và có định hướng."

 VIE_hl_party_leads_army:0 "Đảng Lãnh đạo Tuyệt đối Lực lượng Vũ trang"
 VIE_hl_party_leads_army_desc:0 "Tái khẳng định nguyên tắc Đảng lãnh đạo tuyệt đối, trực tiếp về mọi mặt đối với Quân đội nhân dân và Công an nhân dân qua Quân ủy Trung ương."

 VIE_hl_army_political_education:0 "Giáo dục Chính trị trong Quân đội"
 VIE_hl_army_political_education_desc:0 "Tăng cường thời lượng và chất lượng công tác giáo dục chính trị, bồi dưỡng bản lĩnh cách mạng cho cán bộ, chiến sĩ toàn quân."

 VIE_hl_all_people_defence:0 "Thế trận Toàn dân gắn với Đảng Cơ sở"
 VIE_hl_all_people_defence_desc:0 "Xây dựng thế trận quốc phòng toàn dân và an ninh nhân dân vững chắc, lấy tổ chức Đảng và Mặt trận ở cơ sở làm hạt nhân lãnh đạo."

 VIE_hl_party_defence_industry:0 "Công nghiệp Quốc phòng do Đảng Chỉ đạo"
 VIE_hl_party_defence_industry_desc:0 "Đầu tư đồng bộ cho hệ thống các nhà máy công nghiệp quốc phòng, làm chủ dây chuyền sản xuất vũ khí bộ binh, đạn dược và khí tài hiện đại."

 VIE_hl_cyber_ideology:0 "Bảo vệ Tư tưởng trên Không gian Mạng"
 VIE_hl_cyber_ideology_desc:0 "Chủ động đấu tranh phản bác các quan điểm sai trái, thù địch trên nền tảng số; bảo đảm chủ quyền thông tin và an ninh tư tưởng quốc gia."

 VIE_hl_school_theory:0 "Giáo dục Lý luận Chính trị trong Nhà trường"
 VIE_hl_school_theory_desc:0 "Đưa chương trình giáo dục lý luận chính trị Mác - Lênin và tư tưởng Hồ Chí Minh trở thành trụ cột trong hệ thống giáo dục quốc dân."

 VIE_hl_press_planning:0 "Quy hoạch Báo chí & Truyền thông"
 VIE_hl_press_planning_desc:0 "Rà soát, sắp xếp lại toàn diện các cơ quan báo chí, xuất bản theo quy hoạch định hướng; kiên quyết xử lý tình trạng 'tư nhân hóa' báo chí."

 VIE_hl_fatherland_front:0 "Mặt trận Tổ quốc & Các Đoàn thể Chính trị - Xã hội"
 VIE_hl_fatherland_front_desc:0 "Phát huy tối đa vai trò của Mặt trận Tổ quốc, Công đoàn, Hội Nông dân và Đoàn Thanh niên trong việc tập hợp quần chúng và phản biện xã hội."

 VIE_hl_party_diplomacy:0 "Đẩy mạnh Quan hệ Đối ngoại Đảng"
 VIE_hl_party_diplomacy_desc:0 "Tăng cường quan hệ gắn bó, thủy chung với các đảng cộng sản, đảng công nhân và các lực lượng cánh tả anh em trên thế giới, đặc biệt là Lào, Trung Quốc và Cuba."

 VIE_hl_no_dependence:0 "Hợp tác nhưng Không Lệ thuộc"
 VIE_hl_no_dependence_desc:0 "Khẳng định sự gần gũi về ý thức hệ không đồng nghĩa với nhượng bộ về chủ quyền lãnh thổ; kiên quyết bảo vệ toàn vẹn chủ quyền biển đảo."

 VIE_hl_selective_partners:0 "Đối tác Chiến lược Chọn lọc"
 VIE_hl_selective_partners_desc:0 "Mở rộng quan hệ hợp tác kinh tế, kỹ thuật và an ninh với các đối tác chủ chốt trong khu vực châu Á trên nguyên tắc tôn trọng độc lập chủ quyền."

 VIE_hl_term_review:0 "Tổng kết Nhiệm kỳ & Định hướng Chặng mới"
 VIE_hl_term_review_desc:0 "Hội nghị Trung ương tổ chức tổng kết toàn diện những thành tựu và bài học kinh nghiệm trong quá trình thực hiện đường lối Kiên định, chuẩn bị bước vào giai đoạn mới."

 VIE_hl_steadfast_renewal:0 "Kiên định Mục tiêu, Đổi mới Phương thức"
 VIE_hl_steadfast_renewal_desc:0 "Giữ vững định hướng xã hội chủ nghĩa, mở rộng không gian sáng tạo cho khu vực kinh tế tư nhân và tiếp tục chủ động hội nhập quốc tế sâu rộng."

 VIE_hl_party_state_fusion:0 "Nhất thể hóa Lãnh đạo Đảng & Quản lý Nhà nước"
 VIE_hl_party_state_fusion_desc:0 "Hợp nhất các chức danh lãnh đạo Đảng và chính quyền ở các cấp; tinh gọn triệt để bộ máy, tập trung quyền lực cao độ để hiện đại hóa đất nước."

 VIE_hl_handover:0 "Bàn giao Đường lối"
 VIE_hl_handover_desc:0 "Hoàn thành thắng lợi giai đoạn chấn chỉnh kỷ cương và củng cố nền tảng; bàn giao quyền lãnh đạo trở lại cho đường lối Đổi mới chính thống."
"""

if "VIE_hl_cadre_centralisation:0" not in loc_text:
    loc_text += "\n" + NEW_FOCUS_LOCS + "\n"
    LOC_FILE.write_text(loc_text, encoding='utf-8-sig')
    print("VIE_md_hardline_l_english.yml successfully updated!")
else:
    print("Localization keys already present.")

print("All updates applied successfully!")
