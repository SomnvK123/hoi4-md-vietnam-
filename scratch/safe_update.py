from pathlib import Path
import re

ROOT = Path("d:/HOI4Mods/md_vietnam")
focus_file = ROOT / "common/national_focus/VIE_md_focus.txt"
text = focus_file.read_text(encoding="utf-8-sig")

# 1. Update T04
old_t04 = """\t# T04: Yak-130 - Chuyen loai nang cao (252, 5)
\tfocus = {
\t\tid = VIE_air8_t04_yak130_advanced_trainer
\t\ticon = GFX_focus_VIE_airf_fighter_force

\t\tx = 0
\t\ty = 2
\t\trelative_position_id = VIE_air8_t01_academy_reform

\t\tcost = 5

\t\tprerequisite = { focus = VIE_air8_t01_academy_reform }"""

new_t04 = """\t# T04: Yak-130 - Chuyen loai nang cao (252, 5)
\tfocus = {
\t\tid = VIE_air8_t04_yak130_advanced_trainer
\t\ticon = GFX_focus_VIE_airf_fighter_force

\t\tx = 2
\t\ty = 1
\t\trelative_position_id = VIE_air8_t02_t6c_basic_trainer

\t\tcost = 5

\t\tprerequisite = { focus = VIE_air8_t02_t6c_basic_trainer }
\t\tprerequisite = { focus = VIE_air8_t03_l39ng_jet_trainer }"""

assert old_t04 in text, "old_t04 not found in text!"
text = text.replace(old_t04, new_t04, 1)

# 2. Update R01
old_r01 = """\t# R01: Cai cach so chi huy va dan duong (244, 6)
\tfocus = {
\t\tid = VIE_air8_r01_c2_guidance_reform
\t\ticon = GFX_focus_VIE_airf_command_reform_1

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_air8_f03_su30mk2_fleet_expansion

\t\tcost = 7

\t\tprerequisite = { focus = VIE_air8_p03_multitier_sam }
\t\tprerequisite = { focus = VIE_air8_f03_su30mk2_fleet_expansion }
\t\tprerequisite = {
\t\t\tfocus = VIE_air8_t03_l39ng_jet_trainer
\t\t\tfocus = VIE_air8_t04_yak130_advanced_trainer
\t\t}"""

new_r01 = """\t# R01: Cai cach so chi huy va dan duong (244, 6)
\tfocus = {
\t\tid = VIE_air8_r01_c2_guidance_reform
\t\ticon = GFX_focus_VIE_airf_command_reform_1

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_air8_f03_su30mk2_fleet_expansion

\t\tcost = 7

\t\tprerequisite = { focus = VIE_air8_p03_multitier_sam }
\t\tprerequisite = { focus = VIE_air8_f03_su30mk2_fleet_expansion }
\t\tprerequisite = { focus = VIE_air8_t04_yak130_advanced_trainer }"""

assert old_r01 in text, "old_r01 not found in text!"
text = text.replace(old_r01, new_r01, 1)

# 3. Add R03 after C06
c06_marker = """\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_air8_c06_networked_pkkq_battlespace"
\t\t\tVIE_air_xp_25 = yes
\t\t\tswap_ideas = {
\t\t\t\tremove_idea = VIE_air8_spirit_integrated_c4isr
\t\t\t\tadd_idea = VIE_air8_spirit_digital_air_network
\t\t\t}
\t\t}

\t\tai_will_do = { base = 50 }
\t}"""

r03_block = """\n\n\t# R03: Lam chu bau troi To quoc (244, 13) - Capstone Toi hau PK-KQ
\tfocus = {
\t\tid = VIE_air8_r03_master_of_the_skies
\t\ticon = GFX_focus_VIE_airf_multirole_fleet

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_air8_b06_agile_multirole_air_force

\t\tcost = 10

\t\tprerequisite = {
\t\t\tfocus = VIE_air8_a06_multilayer_sky_shield
\t\t\tfocus = VIE_air8_b06_agile_multirole_air_force
\t\t\tfocus = VIE_air8_c06_networked_pkkq_battlespace
\t\t}

\t\tsearch_filters = { FOCUS_FILTER_AIR FOCUS_FILTER_MILITARY FOCUS_FILTER_POLITICAL }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_air8_r03_master_of_the_skies"
\t\t\tVIE_air_xp_25 = yes
\t\t\tadd_political_power = 50
\t\t\tadd_command_power = 25
\t\t\tadd_ideas = VIE_air8_spirit_master_of_the_skies
\t\t\tcustom_effect_tooltip = { localization_key = modifies_dynamic_modifier_tt MODIFIER = VIE_armed_forces_modifier }
\t\t\tadd_to_variable = { VIE_af_air_superiority_efficiency = 0.03 tooltip = air_superiority_efficiency_tt }
\t\t\tadd_to_variable = { VIE_af_air_range_factor = 0.03 tooltip = air_range_factor_tt }
\t\t\tadd_to_variable = { VIE_af_air_home_defence_factor = 0.02 tooltip = air_home_defence_factor_tt }
\t\t\tadd_to_variable = { VIE_af_air_mission_efficiency = 0.02 tooltip = air_mission_efficiency_tt }
\t\t\tadd_to_variable = { VIE_af_air_ace_generation_chance_factor = 0.02 tooltip = air_ace_generation_chance_factor_tt }
\t\t}

\t\tai_will_do = { base = 100 }
\t}"""

assert c06_marker in text, "c06_marker not found in text!"
text = text.replace(c06_marker, c06_marker + r03_block, 1)

# 4. Update Missile focuses coordinates to compact (x: -5,-3,-1,1,3,5; y=1)
msl_changes = [
    # M00
    ("id = VIE_msl_national_program\n\t\ticon = GFX_focus_VIE_nf_command_reform_2\n\n\t\tx = 82\n\t\ty = 1\n\t\trelative_position_id = VIE_modernize_vpa",
     "id = VIE_msl_national_program\n\t\ticon = GFX_focus_VIE_nf_command_reform_2\n\n\t\tx = 78\n\t\ty = 1\n\t\trelative_position_id = VIE_modernize_vpa"),
    # M01
    ("id = VIE_msl_scud_b_maintenance\n\t\ticon = GFX_focus_VIE_nf_denial_defence\n\n\t\tx = -15\n\t\ty = 2",
     "id = VIE_msl_scud_b_maintenance\n\t\ticon = GFX_focus_VIE_nf_denial_defence\n\n\t\tx = -5\n\t\ty = 1"),
    # M02
    ("id = VIE_msl_redut_maintenance\n\t\ticon = GFX_focus_VIE_nf_denial_defence\n\n\t\tx = -11\n\t\ty = 2",
     "id = VIE_msl_redut_maintenance\n\t\ticon = GFX_focus_VIE_nf_denial_defence\n\n\t\tx = -3\n\t\ty = 1"),
    # M03
    ("id = VIE_msl_rubezh_maintenance\n\t\ticon = GFX_focus_VIE_nf_denial_defence\n\n\t\tx = -7\n\t\ty = 2",
     "id = VIE_msl_rubezh_maintenance\n\t\ticon = GFX_focus_VIE_nf_denial_defence\n\n\t\tx = -1\n\t\ty = 1"),
    # M05
    ("id = VIE_msl_vcm01_program\n\t\ticon = GFX_focus_VIE_research_universities\n\n\t\tx = 7\n\t\ty = 2",
     "id = VIE_msl_vcm01_program\n\t\ticon = GFX_focus_VIE_research_universities\n\n\t\tx = 1\n\t\ty = 1"),
    # M06
    ("id = VIE_msl_vsm01a_song_hong\n\t\ticon = GFX_focus_VIE_research_universities\n\n\t\tx = 11\n\t\ty = 2",
     "id = VIE_msl_vsm01a_song_hong\n\t\ticon = GFX_focus_VIE_research_universities\n\n\t\tx = 3\n\t\ty = 1"),
    # M07
    ("id = VIE_msl_vcs01_truong_son\n\t\ticon = GFX_focus_VIE_research_universities\n\n\t\tx = 15\n\t\ty = 2",
     "id = VIE_msl_vcs01_truong_son\n\t\ticon = GFX_focus_VIE_research_universities\n\n\t\tx = 5\n\t\ty = 1"),
    # M04
    ("id = VIE_msl_technical_autonomy\n\t\ticon = GFX_focus_VIE_nf_command_reform_2\n\n\t\tx = 0\n\t\ty = 2",
     "id = VIE_msl_technical_autonomy\n\t\ticon = GFX_focus_VIE_nf_command_reform_2\n\n\t\tx = 0\n\t\ty = 1"),
    # M08
    ("id = VIE_msl_cruise_missile_industry\n\t\ticon = GFX_focus_VIE_def_industry_law\n\n\t\tx = 0\n\t\ty = 2",
     "id = VIE_msl_cruise_missile_industry\n\t\ticon = GFX_focus_VIE_def_industry_law\n\n\t\tx = 0\n\t\ty = 1"),
    # M09
    ("id = VIE_msl_national_capability\n\t\ticon = GFX_focus_VIE_nf_command_reform_2\n\n\t\tx = 11\n\t\ty = 2",
     "id = VIE_msl_national_capability\n\t\ticon = GFX_focus_VIE_nf_command_reform_2\n\n\t\tx = 3\n\t\ty = 1"),
]

for old, new in msl_changes:
    assert old in text, f"Missile block not found: {old[:50]}"
    text = text.replace(old, new, 1)

focus_file.write_text(text, encoding="utf-8")
print("All focus replacements executed successfully!")
