from pathlib import Path

# 1. Update common/national_focus/VIE_md_focus.txt
focus_path = Path('common/national_focus/VIE_md_focus.txt')
text = focus_path.read_text(encoding='utf-8')

text = text.replace('prerequisite = { focus = VIE_lf_army_reform }', 'prerequisite = { focus = VIE_modernize_vpa }')

header_idx = text.rfind('###############################', 0, text.find('id = VIE_lf_army_reform'))
idx_last = text.find('id = VIE_lf_force_complete')
end_block = text.find('\n\t}\n', idx_last) + len('\n\t}\n')

new_text = text[:header_idx] + '\t###############################\n\t## TRUC 3 - XAY DUNG LUC LUONG LUC QUAN (DA XOA - SAN SANG THIET KE MOI)\n\t###############################\n\n' + text[end_block:]
focus_path.write_text(new_text, encoding='utf-8')
print("1. Updated VIE_md_focus.txt")

# 2. Update common/decisions/VIE_md_decisions_lf.txt
dec_path = Path('common/decisions/VIE_md_decisions_lf.txt')
dec_path.write_text('# Nhánh quyết định Lục quân đã được xóa để xây dựng lại từ đầu.\n', encoding='utf-8')
print("2. Cleared VIE_md_decisions_lf.txt")

# 3. Update common/ideas/VIE_md_ideas_army_revamp.txt and VIE_md_ideas_lf.txt
Path('common/ideas/VIE_md_ideas_army_revamp.txt').write_text('# Ideas Luc quan da duoc xoa de xay dung lai tu dau.\nideas = {\n\tcountry = {\n\t}\n}\n', encoding='utf-8')
Path('common/ideas/VIE_md_ideas_lf.txt').write_text('# Ideas Luc quan da duoc xoa de xay dung lai tu dau.\nideas = {\n\tcountry = {\n\t}\n}\n', encoding='utf-8')
print("3. Cleared army ideas files")

# 4. Update events/VIE_land_force.txt
Path('events/VIE_land_force.txt').write_text('add_namespace = vie_lf\n# Su kien Luc quan da duoc xoa de xay dung lai tu dau.\n', encoding='utf-8')
print("4. Cleared events/VIE_land_force.txt")

# 5. Update common/scripted_triggers/VIE_md_triggers_p17.txt
Path('common/scripted_triggers/VIE_md_triggers_p17.txt').write_text('# Triggers Luc quan da duoc xoa de xay dung lai tu dau.\n', encoding='utf-8')
print("5. Cleared triggers_p17.txt")

# 6. Update common/scripted_effects/VIE_md_effects_p17.txt (preserve only VIE_lf_xp_* helpers for special forces)
xp_helpers = '''# Helpers tang kinh nghiem luc quan / hoc thuyet (giu lai cho Dac cong va cac nhanh khac su dung)
VIE_lf_xp_10 = {
	if = {
		limit = { has_selected_land_grand_doctrine = yes }
		add_mastery = {
			amount = 10
			folder = land
		}
	}
	else = {
		army_experience = 10
	}
}
VIE_lf_xp_15 = {
	if = {
		limit = { has_selected_land_grand_doctrine = yes }
		add_mastery = {
			amount = 15
			folder = land
		}
	}
	else = {
		army_experience = 15
	}
}
VIE_lf_xp_20 = {
	if = {
		limit = { has_selected_land_grand_doctrine = yes }
		add_mastery = {
			amount = 20
			folder = land
		}
	}
	else = {
		army_experience = 20
	}
}
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
}
VIE_lf_xp_30 = {
	if = {
		limit = { has_selected_land_grand_doctrine = yes }
		add_mastery = {
			amount = 30
			folder = land
		}
	}
	else = {
		army_experience = 30
	}
}
VIE_lf_xp_50 = {
	if = {
		limit = { has_selected_land_grand_doctrine = yes }
		add_mastery = {
			amount = 50
			folder = land
		}
	}
	else = {
		army_experience = 50
	}
}
'''
Path('common/scripted_effects/VIE_md_effects_p17.txt').write_text(xp_helpers, encoding='utf-8')
print("6. Cleaned effects_p17.txt (retained xp helpers)")

# 7. Update common/scripted_localisation/VIE_md_lf_alt.txt
Path('common/scripted_localisation/VIE_md_lf_alt.txt').write_text('# Scripted loc Luc quan da duoc xoa.\n', encoding='utf-8')
print("7. Cleared VIE_md_lf_alt.txt")

# 8. Update common/ai_strategy_plans/VIE_strategy_plans.txt
strat_path = Path('common/ai_strategy_plans/VIE_strategy_plans.txt')
strat_text = strat_path.read_text(encoding='utf-8')
strat_lines = [l for l in strat_text.splitlines() if not any(x in l for x in [
    'VIE_lf_army_reform', 'VIE_lf_fs_depth_defence', 'VIE_lf_dev_territorial',
    'VIE_lf_cap_border_urban', 'VIE_lf_cap_area_control', 'VIE_lf_selective_modernization'
])]
strat_path.write_text('\n'.join(strat_lines) + '\n', encoding='utf-8')
print("8. Updated VIE_strategy_plans.txt")

print("\nAll land forces components have been successfully cleared!")
