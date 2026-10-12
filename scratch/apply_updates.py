import re
from pathlib import Path

ROOT = Path("d:/HOI4Mods/md_vietnam")

# 1. Update common/ideas/VIE_md_ideas.txt
ideas_path = ROOT / "common/ideas/VIE_md_ideas.txt"
ideas_txt = ideas_path.read_text(encoding="utf-8-sig")

spirit_code = """\t\tVIE_air8_spirit_master_of_the_skies = {
\t\t\tpicture = air_superiority
\t\t\tallowed = { always = no }
\t\t\tallowed_civil_war = { always = no }
\t\t\tcancel_if_invalid = no

\t\t\tmodifier = {
\t\t\t\tair_superiority_efficiency = 0.05
\t\t\t\tair_ace_generation_chance_factor = 0.05
\t\t\t\tair_accidents_factor = -0.05
\t\t\t}
\t\t}
"""

if "VIE_air8_spirit_master_of_the_skies" not in ideas_txt:
    target = "\t\tVIE_air8_spirit_aviation_industry = {"
    idx = ideas_txt.find(target)
    if idx != -1:
        # find end of VIE_air8_spirit_aviation_industry block
        end_brace = ideas_txt.find("\t\t}", idx) + len("\t\t}\n")
        ideas_txt = ideas_txt[:end_brace] + "\n" + spirit_code + ideas_txt[end_brace:]
        ideas_path.write_text(ideas_txt, encoding="utf-8")
        print("Added VIE_air8_spirit_master_of_the_skies to ideas")

# 2. Update localisation/english/replace/VIE_replace_military_l_english.yml
loc_path = ROOT / "localisation/english/replace/VIE_replace_military_l_english.yml"
loc_txt = loc_path.read_text(encoding="utf-8-sig")

loc_add = """ VIE_air8_r03_master_of_the_skies:0 "Làm chủ Bầu trời Tổ quốc"
 VIE_air8_r03_master_of_the_skies_desc:0 "Khẳng định năng lực làm chủ không phận toàn diện và tự chủ tác chiến đường không của Quân chủng Phòng không - Không quân. Từng tấc trời, từng dải mây của Tổ quốc từ biên giới đất liền đến biển đảo thiêng liêng đều được canh giữ vững chắc, bình yên."
 VIE_air8_spirit_master_of_the_skies:0 "Làm chủ Bầu trời Tổ quốc"
 VIE_air8_spirit_master_of_the_skies_desc:0 "Bộ đội Phòng không - Không quân đã hoàn tất quá trình hiện đại hóa đồng bộ về tổ chức, học thuyết và vũ khí công nghệ cao, sẵn sàng chiến đấu 24/7 và làm chủ bầu trời Tổ quốc trong mọi tình huống."
"""

if "VIE_air8_r03_master_of_the_skies" not in loc_txt:
    target_loc = " VIE_air8_i06_viettel_tactical_uav_desc:"
    idx = loc_txt.find(target_loc)
    end_line = loc_txt.find("\n", idx) + 1
    loc_txt = loc_txt[:end_line] + "\n" + loc_add + loc_txt[end_line:]
    loc_path.write_text(loc_txt, encoding="utf-8-sig")
    print("Added localisation for R03 and spirit")

# 3. Update common/national_focus/VIE_md_focus.txt
focus_path = ROOT / "common/national_focus/VIE_md_focus.txt"
focus_txt = focus_path.read_text(encoding="utf-8-sig")

# 3a. Add R03 after C06
r03_code = """
\t# R03: Lam chu bau troi To quoc (244, 13) - Capstone Toi hau PK-KQ
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
\t}
"""

if "VIE_air8_r03_master_of_the_skies" not in focus_txt:
    target_c06 = "id = VIE_air8_c06_networked_pkkq_battlespace"
    idx = focus_txt.find(target_c06)
    end_c06 = focus_txt.find("\n\t}", idx) + len("\n\t}\n")
    focus_txt = focus_txt[:end_c06] + r03_code + focus_txt[end_c06:]
    print("Added R03 focus")

# 3b. Update missile coordinates to compact (280 center, Y=2,3,4,5)
msl_replacements = {
    # M00
    r"(id = VIE_msl_national_program.*?x = )(\d+)": r"\g<1>78",
    r"(id = VIE_msl_national_program.*?y = )(\d+)": r"\g<1>1",
    # M01
    r"(id = VIE_msl_scud_b_maintenance.*?x = )([-\d]+)": r"\g<1>-5",
    r"(id = VIE_msl_scud_b_maintenance.*?y = )(\d+)": r"\g<1>1",
    # M02
    r"(id = VIE_msl_redut_maintenance.*?x = )([-\d]+)": r"\g<1>-3",
    r"(id = VIE_msl_redut_maintenance.*?y = )(\d+)": r"\g<1>1",
    # M03
    r"(id = VIE_msl_rubezh_maintenance.*?x = )([-\d]+)": r"\g<1>-1",
    r"(id = VIE_msl_rubezh_maintenance.*?y = )(\d+)": r"\g<1>1",
    # M05
    r"(id = VIE_msl_vcm01_program.*?x = )([-\d]+)": r"\g<1>1",
    r"(id = VIE_msl_vcm01_program.*?y = )(\d+)": r"\g<1>1",
    # M06
    r"(id = VIE_msl_vsm01a_song_hong.*?x = )([-\d]+)": r"\g<1>3",
    r"(id = VIE_msl_vsm01a_song_hong.*?y = )(\d+)": r"\g<1>1",
    # M07
    r"(id = VIE_msl_vcs01_truong_son.*?x = )([-\d]+)": r"\g<1>5",
    r"(id = VIE_msl_vcs01_truong_son.*?y = )(\d+)": r"\g<1>1",
    # M04
    r"(id = VIE_msl_technical_autonomy.*?x = )([-\d]+)": r"\g<1>0",
    r"(id = VIE_msl_technical_autonomy.*?y = )(\d+)": r"\g<1>1",
    # M08
    r"(id = VIE_msl_cruise_missile_industry.*?x = )([-\d]+)": r"\g<1>0",
    r"(id = VIE_msl_cruise_missile_industry.*?y = )(\d+)": r"\g<1>1",
    # M09
    r"(id = VIE_msl_national_capability.*?x = )([-\d]+)": r"\g<1>3",
    r"(id = VIE_msl_national_capability.*?y = )(\d+)": r"\g<1>1",
}

for pat, repl in msl_replacements.items():
    focus_txt = re.sub(pat, repl, focus_txt, count=1, flags=re.DOTALL)

focus_path.write_text(focus_txt, encoding="utf-8")
print("Updated focus file successfully!")
