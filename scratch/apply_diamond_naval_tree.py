# -*- coding: utf-8 -*-
"""
apply_diamond_naval_tree.py
Thực hiện chuyển đổi toàn diện nhánh Hải quân sang chuẩn Organic Diamond Flow (25 Focus).
Cập nhật đồng thời:
1. common/national_focus/VIE_md_focus.txt
2. common/ideas/VIE_md_ideas_v32_navy.txt
3. common/decisions/VIE_md_decisions_navy.txt
4. common/opinion_modifiers/VIE_md_opinion_modifiers.txt
5. localisation/english/replace/VIE_md_vi_military_l_english.yml
"""

import re
import os
from build_diamond_navy import focus_block_content, focus_defs

FOCUS_FILE = 'common/national_focus/VIE_md_focus.txt'
IDEAS_FILE = 'common/ideas/VIE_md_ideas_v32_navy.txt'
DECISIONS_FILE = 'common/decisions/VIE_md_decisions_navy.txt'
OPINION_FILE = 'common/opinion_modifiers/VIE_md_opinion_modifiers.txt'
LOC_FILE = 'localisation/english/replace/VIE_md_vi_military_l_english.yml'

# ==============================================================================
# 1. CAP NHAT COMMON/NATIONAL_FOCUS/VIE_MD_FOCUS.TXT
# ==============================================================================
print("Step 1: Updating focus tree...")
with open(FOCUS_FILE, 'r', encoding='utf-8') as f:
    focus_text = f.read()

# Tim diem bat dau cua cum naval
# Co the bat dau bang header V32.1 hoac header moi
m1 = "# ======================================================================\n\t# NHANH HAI QUAN NHAN DAN VIET NAM V32.1 (40 FOCUS)"
m2 = "# ======================================================================\n\t# NHANH HAI QUAN NHAN DAN VIET NAM (VPN) - ORGANIC DIAMOND FLOW (25 FOCUS)"

if m1 in focus_text:
    start_cut = focus_text.find(m1)
elif m2 in focus_text:
    start_cut = focus_text.find(m2)
else:
    raise ValueError("Cannot find naval branch header in focus tree!")

end_marker = "focus = {\n\t\tid = VIE_force_47"
end_cut = focus_text.find(end_marker)

if end_cut == -1:
    raise ValueError("Cannot find end marker VIE_force_47 in focus tree!")

print(f"Bounds found: start_cut={start_cut}, end_cut={end_cut}")
new_focus_text = focus_text[:start_cut] + focus_block_content + "\n\n\t" + focus_text[end_cut:]

with open(FOCUS_FILE, 'w', encoding='utf-8') as f:
    f.write(new_focus_text)

print("Focus tree updated successfully.")

# ==============================================================================
# 2. CAP NHAT COMMON/IDEAS/VIE_MD_IDEAS_V32_NAVY.TXT
# ==============================================================================
print("Step 2: Updating naval ideas...")
ideas_content = """# ======================================================================
# Y NIEM QUOC GIA HAI QUAN NHAN DAN VIET NAM (VPN DIAMOND TREE)
# ======================================================================

ideas = {
\tcountry = {
\t\t# ------------------------------------------------------------------
\t\t# NEN TANG SAN SANG CHIEN DAU HAI QUAN (VPA_Naval_Readiness)
\t\t# ------------------------------------------------------------------
\t\tVPA_Naval_Readiness_1 = {
\t\t\tpicture = generic_navy_bonus
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_org_factor = 0.04
\t\t\t\tnaval_morale_factor = 0.04
\t\t\t}
\t\t}

\t\tVPA_Naval_Readiness_2 = {
\t\t\tpicture = generic_navy_bonus
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_org_factor = 0.08
\t\t\t\tnaval_morale_factor = 0.06
\t\t\t\texperience_gain_navy_factor = 0.06
\t\t\t\tnaval_coordination = 0.04
\t\t\t}
\t\t}

\t\tVPA_Naval_Readiness_3 = {
\t\t\tpicture = generic_navy_bonus
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_org_factor = 0.12
\t\t\t\tnaval_morale_factor = 0.10
\t\t\t\texperience_gain_navy_factor = 0.10
\t\t\t\tnaval_coordination = 0.08
\t\t\t}
\t\t}

\t\t# ------------------------------------------------------------------
\t\t# HA TANG DONG TAU BA SON
\t\t# ------------------------------------------------------------------
\t\tVIE_naval_shipbuilding_spirit = {
\t\t\tpicture = generic_coastal_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tindustrial_capacity_dockyard = 0.06
\t\t\t\tproduction_speed_dockyard_factor = 0.06
\t\t\t}
\t\t}

\t\tVIE_naval_shipbuilding_spirit_2 = {
\t\t\tpicture = generic_coastal_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tindustrial_capacity_dockyard = 0.12
\t\t\t\tproduction_speed_dockyard_factor = 0.12
\t\t\t\tnaval_speed_factor = 0.04
\t\t\t}
\t\t}

\t\t# ------------------------------------------------------------------
\t\t# HAU CAN & CAN CU CAM RANH
\t\t# ------------------------------------------------------------------
\t\tVIE_fleet_sustainment_spirit = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_max_range_factor = 0.08
\t\t\t\tnavy_fuel_consumption_factor = -0.06
\t\t\t}
\t\t}

\t\tVIE_fleet_sustainment_spirit_2 = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_max_range_factor = 0.15
\t\t\t\tnavy_fuel_consumption_factor = -0.10
\t\t\t\trepair_speed_factor = 0.10
\t\t\t}
\t\t}

\t\t# ------------------------------------------------------------------
\t\t# KHI TAI & LU DOAN CHU LUC
\t\t# ------------------------------------------------------------------
\t\tVIE_189th_submarine_brigade_spirit = {
\t\t\tpicture = generic_sea_focused_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tsub_visibility = -0.10
\t\t\t\tsubmarine_attack_factor = 0.08
\t\t\t}
\t\t}

\t\tVIE_162nd_frigate_brigade_spirit = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tscreening_efficiency = 0.10
\t\t\t\tnavy_anti_air_attack_factor = 0.08
\t\t\t}
\t\t}

\t\tVIE_naval_weapons_integration_spirit = {
\t\t\tpicture = generic_coastal_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnaval_strike_attack_factor = 0.08
\t\t\t\tnaval_torpedo_hit_chance_factor = 0.06
\t\t\t}
\t\t}

\t\tVIE_island_fortress_spirit = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tamphibious_invasion_defense = 0.15
\t\t\t}
\t\t}

\t\t# ------------------------------------------------------------------
\t\t# HE THONG HOP THANH TANG 6 & 7
\t\t# ------------------------------------------------------------------
\t\tVIE_undersea_warfare_network_spirit = {
\t\t\tpicture = generic_sea_focused_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tsubmarine_attack_factor = 0.12
\t\t\t\tsub_visibility = -0.15
\t\t\t\tnavy_submarine_detection_factor = 0.10
\t\t\t}
\t\t}

\t\tVIE_coastal_a2ad_shield_spirit = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_screen_attack_factor = 0.10
\t\t\t\tnavy_surface_detection_factor = 0.12
\t\t\t}
\t\t}

\t\tVIE_maritime_domain_awareness_spirit_2 = {
\t\t\tpicture = generic_sea_focused_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_surface_detection_factor = 0.15
\t\t\t\tnavy_submarine_detection_factor = 0.12
\t\t\t\tnaval_coordination = 0.06
\t\t\t}
\t\t}

\t\tVIE_marine_infantry_readiness_spirit = {
\t\t\tpicture = generic_volunteer_expedition_bonus
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tamphibious_invasion_defense = 0.10
\t\t\t\tinvasion_preparation = -0.15
\t\t\t}
\t\t}

\t\tVIE_subsurface_steel_wall_spirit = {
\t\t\tpicture = generic_sea_focused_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tsubmarine_attack_factor = 0.15
\t\t\t\tconvoy_raiding_efficiency_factor = 0.15
\t\t\t}
\t\t}

\t\tVIE_island_fleet_defense_spirit = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tscreening_efficiency = 0.12
\t\t\t\tnavy_max_range_factor = 0.10
\t\t\t}
\t\t}

\t\t# ------------------------------------------------------------------
\t\t# HAI HOC THUYET DOI KHANG (ARCHETYPES)
\t\t# ------------------------------------------------------------------
\t\tVIE_doctrine_asymmetric_sea_denial_spirit = {
\t\t\tpicture = generic_sea_focused_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tsubmarine_attack_factor = 0.20
\t\t\t\tsub_visibility = -0.20
\t\t\t\tconvoy_raiding_efficiency_factor = 0.20
\t\t\t\tnavy_submarine_detection_factor = 0.15
\t\t\t}
\t\t}

\t\tVIE_doctrine_active_maritime_presence_spirit = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tscreening_efficiency = 0.20
\t\t\t\tnavy_surface_detection_factor = 0.20
\t\t\t\tnavy_max_range_factor = 0.20
\t\t\t\tnavy_speed_factor = 0.08
\t\t\t}
\t\t}

\t\t# ------------------------------------------------------------------
\t\t# CAPSTONE HOI TU: CHU QUYEN BIEN DAO
\t\t# ------------------------------------------------------------------
\t\tVIE_eastern_sea_sovereignty_capstone_spirit = {
\t\t\tpicture = generic_coastal_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_org_factor = 0.15
\t\t\t\tnaval_morale_factor = 0.12
\t\t\t\tnaval_coordination = 0.10
\t\t\t\tindustrial_capacity_dockyard = 0.15
\t\t\t}
\t\t}

\t\t# ------------------------------------------------------------------
\t\t# Y NIEM TAM THOI (TIMED IDEAS TU DECISION)
\t\t# ------------------------------------------------------------------
\t\tVIE_idea_molniya_production_active = {
\t\t\tpicture = generic_coastal_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tproduction_speed_dockyard_factor = 0.15
\t\t\t}
\t\t}

\t\tVIE_idea_gepard_batch_active = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tproduction_speed_dockyard_factor = 0.15
\t\t\t\tscreening_efficiency = 0.08
\t\t\t}
\t\t}

\t\tVIE_idea_kilo_submarine_active = {
\t\t\tpicture = generic_sea_focused_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tsubmarine_attack_factor = 0.10
\t\t\t\tsub_visibility = -0.08
\t\t\t}
\t\t}

\t\tVIE_idea_domestic_corvette_active = {
\t\t\tpicture = generic_coastal_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tproduction_speed_dockyard_factor = 0.12
\t\t\t\tnaval_speed_factor = 0.05
\t\t\t}
\t\t}

\t\tVIE_idea_island_bastion_active = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tamphibious_invasion_defense = 0.20
\t\t\t}
\t\t}

\t\tVIE_idea_sea_denial_ambush_active = {
\t\t\tpicture = generic_sea_focused_navy
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tsubmarine_attack_factor = 0.15
\t\t\t\tsub_visibility = -0.12
\t\t\t}
\t\t}

\t\tVIE_idea_coastal_defense_readiness_active = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_surface_detection_factor = 0.15
\t\t\t\tnavy_screen_attack_factor = 0.10
\t\t\t}
\t\t}

\t\tVIE_idea_convoy_protection_active = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tconvoy_escort_efficiency = 0.20
\t\t\t\tscreening_efficiency = 0.10
\t\t\t}
\t\t}

\t\tVIE_idea_extended_sea_presence_active = {
\t\t\tpicture = generic_coastal_defense_ships
\t\t\tallowed = { original_tag = VIE }
\t\t\tmodifier = {
\t\t\t\tnavy_max_range_factor = 0.20
\t\t\t\tnavy_morale_factor = 0.08
\t\t\t}
\t\t}
\t}
}
"""

with open(IDEAS_FILE, 'w', encoding='utf-8') as f:
    f.write(ideas_content)

print("Naval ideas updated successfully.")

# ==============================================================================
# 3. CAP NHAT COMMON/DECISIONS/VIE_MD_DECISIONS_NAVY.TXT
# ==============================================================================
print("Step 3: Updating naval decisions...")
decisions_content = """# ======================================================================
# QUYET DINH CHIEN LUOC & DONG TAU HAI QUAN (VPN DIAMOND TREE)
# ======================================================================

VIE_military_readiness_category = {

\t# ------------------------------------------------------------------
\t# KHÍ TÀI & DỰ ÁN ĐÓNG TÀU CHỦ LỰC
\t# ------------------------------------------------------------------

\tVIE_decision_molniya_production_run = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 40

\t\tdays_remove = 180
\t\tdays_re_enable = 360

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_molniya_fast_attack_craft
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 20
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_molniya_production_run"
\t\t\tadd_command_power = -20
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t\tadd_timed_idea = { idea = VIE_idea_molniya_production_active days = 180 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}

\tVIE_decision_gepard_batch_procurement = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 50

\t\tdays_remove = 240
\t\tdays_re_enable = 360

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_gepard_frigate_procurement
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 25
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_gepard_batch_procurement"
\t\t\tadd_command_power = -25
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t\tadd_timed_idea = { idea = VIE_idea_gepard_batch_active days = 240 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}

\tVIE_decision_kilo_submarine_sustainment = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 45

\t\tdays_remove = 180
\t\tdays_re_enable = 360

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_kilo_submarine_procurement
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 20
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_kilo_submarine_sustainment"
\t\t\tadd_command_power = -20
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t\tadd_timed_idea = { idea = VIE_idea_kilo_submarine_active days = 180 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}

\tVIE_decision_domestic_corvette_lead_ship = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 50

\t\tdays_remove = 240
\t\tdays_re_enable = 360

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_domestic_patrol_craft
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 25
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_domestic_corvette_lead_ship"
\t\t\tadd_command_power = -25
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t\tadd_timed_idea = { idea = VIE_idea_domestic_corvette_active days = 240 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}

\t# ------------------------------------------------------------------
\t# PHÒNG THỦ ĐẢO & THẾ TRẬN BIỂN
\t# ------------------------------------------------------------------

\tVIE_decision_island_bastion_fortification = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 45

\t\tdays_remove = 180
\t\tdays_re_enable = 360

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_spratly_dk1_defense_system
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 20
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_island_bastion_fortification"
\t\t\tadd_command_power = -20
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t\tadd_timed_idea = { idea = VIE_idea_island_bastion_active days = 180 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}

\t# ------------------------------------------------------------------
\t# TẬP TRẬN HỌC THUYẾT & TÁC CHIẾN
\t# ------------------------------------------------------------------

\tVIE_decision_sea_denial_ambush_exercise = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 40

\t\tdays_remove = 120
\t\tdays_re_enable = 240

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_integrated_undersea_warfare
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 20
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_sea_denial_ambush_exercise"
\t\t\tadd_command_power = -20
\t\t\tnavy_experience = 15
\t\t\tadd_timed_idea = { idea = VIE_idea_sea_denial_ambush_active days = 120 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}

\tVIE_decision_coastal_defense_readiness = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 40

\t\tdays_remove = 120
\t\tdays_re_enable = 240

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_bastion_a2ad_coastal_shield
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 20
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_coastal_defense_readiness"
\t\t\tadd_command_power = -20
\t\t\tnavy_experience = 15
\t\t\tadd_timed_idea = { idea = VIE_idea_coastal_defense_readiness_active days = 120 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}

\tVIE_decision_convoy_protection_sweep = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 35

\t\tdays_remove = 120
\t\tdays_re_enable = 240

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_offshore_task_groups
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 15
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_convoy_protection_sweep"
\t\t\tadd_command_power = -15
\t\t\tnavy_experience = 15
\t\t\tadd_timed_idea = { idea = VIE_idea_convoy_protection_active days = 120 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}

\tVIE_decision_extended_sea_presence = {
\t\ticon = GFX_decision_generic_naval
\t\tcost = 40

\t\tdays_remove = 180
\t\tdays_re_enable = 360

\t\tvisible = {
\t\t\thas_completed_focus = VIE_nav_doctrine_active_maritime_presence
\t\t}

\t\tavailable = {
\t\t\tcommand_power > 20
\t\t}

\t\tcomplete_effect = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_decision_extended_sea_presence"
\t\t\tadd_command_power = -20
\t\t\tnavy_experience = 20
\t\t\tadd_timed_idea = { idea = VIE_idea_extended_sea_presence_active days = 180 }
\t\t}

\t\tai_will_do = {
\t\t\tfactor = 15
\t\t\tmodifier = { factor = 2 has_war = yes }
\t\t}
\t}
}
"""

with open(DECISIONS_FILE, 'w', encoding='utf-8') as f:
    f.write(decisions_content)

print("Naval decisions updated successfully.")

# ==============================================================================
# 4. CAP NHAT COMMON/OPINION_MODIFIERS/VIE_MD_OPINION_MODIFIERS.TXT
# ==============================================================================
print("Step 4: Updating opinion modifier...")
with open(OPINION_FILE, 'r', encoding='utf-8') as f:
    op_text = f.read()

if 'VIE_naval_technical_cooperation' not in op_text:
    idx = op_text.rfind('}')
    mod_str = """\n\tVIE_naval_technical_cooperation = {
\t\tvalue = 25
\t\tdecay = 0.1
\t}\n"""
    op_text = op_text[:idx] + mod_str + op_text[idx:]
    with open(OPINION_FILE, 'w', encoding='utf-8') as f:
        f.write(op_text)
    print("Added VIE_naval_technical_cooperation.")
else:
    print("VIE_naval_technical_cooperation already exists.")

# ==============================================================================
# 5. CAP NHAT LOCALISATION
# ==============================================================================
print("Step 5: Updating localisation...")
with open(LOC_FILE, 'r', encoding='utf-8') as f:
    loc_text = f.read()

loc_entries = """
  # ======================================================================
  # HẢI QUÂN NHÂN DÂN VIỆT NAM (ORGANIC DIAMOND FLOW - 25 FOCUS)
  # ======================================================================
  VIE_nav_maritime_strategy_21st: "Chiến lược Biển Việt Nam Thế kỷ 21"
  VIE_nav_maritime_strategy_21st_desc: "Đề ra đường lối hiện đại hóa Hải quân nhân dân Việt Nam tiến thẳng lên hiện đại, xác định biển đảo là không gian sinh tồn chiến lược và phên dậu bảo vệ Tổ quốc."
  VIE_nav_maritime_strategy_21st_tt: "§GKhởi động lộ trình hiện đại hóa hạm đội và nâng cấp năng lực tác chiến biển.§!"

  VIE_nav_russian_naval_partnership: "Hợp tác Kỹ thuật Hải quân Việt - Nga"
  VIE_nav_russian_naval_partnership_desc: "Ký kết các hiệp định hợp tác chiến lược toàn diện với Liên bang Nga về chuyển giao khí tài hải quân hiện đại, bảo đảm kỹ thuật và đào tạo kíp chiến đấu."
  VIE_nav_russian_naval_partnership_tt: "§GThiết lập cầu nối kỹ thuật mua sắm và chuyển giao công nghệ tàu ngầm và khinh hạm.§!"

  VIE_nav_bason_shipbuilding_core: "Hiện đại hóa Tổ hợp Đóng tàu Ba Son"
  VIE_nav_bason_shipbuilding_core_desc: "Đầu tư mở rộng và hiện đại hóa Tổng công ty Ba Son và các nhà máy X51, tạo nền tảng công nghiệp tự chủ sửa chữa và đóng mới tàu quân sự vỏ thép trong nước."
  VIE_nav_bason_shipbuilding_core_tt: "§GMở rộng hạ tầng xưởng đóng tàu quân sự tại Nhà Bè và TP. Hồ Chí Minh.§!"

  VIE_nav_kilo_submarine_procurement: "Đề án Hạm đội Tàu ngầm Kilo 636.1"
  VIE_nav_kilo_submarine_procurement_desc: "Ký hợp đồng lịch sử mua 6 tàu ngầm điện-diesel thế hệ 3 đề án 636.1 Varshavyanka ('Hố đen đại dương'), mở ra kỷ nguyên tác chiến ngầm bảo vệ vùng biển Việt Nam."
  VIE_nav_kilo_submarine_procurement_tt: "§GNhận thưởng nghiên cứu tàu ngầm và chuẩn bị thành lập đơn vị tác chiến ngầm.§!"

  VIE_nav_gepard_frigate_procurement: "Đề án Khinh hạm Tàng hình Gepard 3.9"
  VIE_nav_gepard_frigate_procurement_desc: "Trang bị các tàu hộ vệ tên lửa tàng hình lớp Gepard 3.9 (Đinh Tiên Hoàng, Lý Thái Tổ, Trần Hưng Đạo, Quang Trung) với khả năng tác chiến mặt nước và săn ngầm tầm xa."
  VIE_nav_gepard_frigate_procurement_tt: "§GNhận thưởng nghiên cứu khinh hạm và khu trục hạm hiện đại.§!"

  VIE_nav_molniya_fast_attack_craft: "Đóng tàu Tên lửa Tấn công nhanh Molniya"
  VIE_nav_molniya_fast_attack_craft_desc: "Tiếp nhận chuyển giao bản quyền đóng loạt tàu tên lửa tấn công nhanh Project 1241.8 Molniya trang bị 16 tên lửa Uran-E tại Nhà máy Ba Son."
  VIE_nav_molniya_fast_attack_craft_tt: "§GNâng cấp hiệu suất xưởng đóng tàu nội địa lên cấp độ 2.§!"

  VIE_nav_cam_ranh_naval_base: "Căn cứ Chiến lược Quân cảng Cam Ranh"
  VIE_nav_cam_ranh_naval_base_desc: "Xây dựng và nâng cấp Vịnh Cam Ranh thành quân cảng nước sâu hiện đại hàng đầu khu vực, căn cứ mẹ vững chắc cho hạm đội tàu ngầm và tàu mặt nước chủ lực."
  VIE_nav_cam_ranh_naval_base_tt: "§GNâng cấp quân cảng Cam Ranh và tăng cường năng lực tiếp vận hạm đội.§!"

  VIE_nav_189th_submarine_brigade: "Thành lập Lữ đoàn Tàu ngầm 189"
  VIE_nav_189th_submarine_brigade_desc: "Chính thức thành lập Lữ đoàn Tàu ngầm 189 tại Cam Ranh, làm chủ vũ khí kỹ thuật, đào tạo thủy thủ ngầm tinh nhuệ và xây dựng trung tâm huấn luyện mô phỏng hiện đại."
  VIE_nav_189th_submarine_brigade_tt: "§GTăng cường khả năng ẩn mình và sức tấn công của hạm đội tàu ngầm.§!"

  VIE_nav_clubs_cruise_missiles: "Tên lửa Hành trình Tấn công ngầm Club-S"
  VIE_nav_clubs_cruise_missiles_desc: "Trang bị đạn tên lửa hành trình diệt hạm siêu thanh 3M-54E và đạn tấn công mục tiêu mặt đất 3M-14E cho tàu ngầm Kilo, tạo năng lực răn đe chiến lược tầm xa."
  VIE_nav_clubs_cruise_missiles_tt: "§GNâng cao sức mạnh hỏa lực tên lửa hành trình của hải quân.§!"

  VIE_nav_162nd_frigate_brigade: "Lữ đoàn Tàu chiến Mặt nước 162"
  VIE_nav_162nd_frigate_brigade_desc: "Xây dựng Lữ đoàn 162 ('Lữ đoàn thép') thành nắm đấm cơ động mặt nước tinh nhuệ của Vùng 4 Hải quân, tổ chức huấn luyện tác chiến hiệp đồng bảo vệ Trường Sa."
  VIE_nav_162nd_frigate_brigade_tt: "§GTăng cường hiệu quả hộ tống và năng lực phòng không hạm đội.§!"

  VIE_nav_naval_aviation_ka28: "Không quân Hải quân & Trực thăng Săn ngầm"
  VIE_nav_naval_aviation_ka28_desc: "Biên chế các phi đội trực thăng săn ngầm Ka-28/Ka-32 cất cánh từ sàn đáp Gepard, kết hợp phi đội tuần thám biển mở rộng bán kính phát hiện mục tiêu dưới ngầm."
  VIE_nav_naval_aviation_ka28_tt: "§GNhận điểm kinh nghiệm không quân và mở rộng trinh sát săn ngầm.§!"

  VIE_nav_uran_e_integration: "Tích hợp Tên lửa Diệt hạm Uran-E & VCM-01"
  VIE_nav_uran_e_integration_desc: "Tự chủ tích hợp hệ thống điều khiển hỏa lực tên lửa Uran-E lên tàu chiến và nghiên cứu phát triển thế hệ tên lửa hành trình diệt hạm VCM-01 do Việt Nam tự chế tạo."
  VIE_nav_uran_e_integration_tt: "§GTăng cường năng lực tích hợp vũ khí và xác suất bắn trúng mục tiêu biển.§!"

  VIE_nav_domestic_patrol_craft: "Đóng mới Tàu pháo TT-400TP & Tuần tra"
  VIE_nav_domestic_patrol_craft_desc: "Đẩy mạnh dây chuyền tự thiết kế và đóng mới các tàu pháo tuần tra TT-400TP, tàu tuần tra cao tốc phục vụ tuần tra vùng biển ven bờ và cửa vịnh."
  VIE_nav_domestic_patrol_craft_tt: "§GBổ sung dockyard và tăng cường tốc độ đóng tàu tuần tra.§!"

  VIE_nav_submarine_rescue_logistics: "Tàu Cứu hộ Yết Kiêu 927 & Tiếp vận Đa năng"
  VIE_nav_submarine_rescue_logistics_desc: "Biên chế tàu tìm kiếm cứu nạn tàu ngầm đa năng 927 Yết Kiêu, cùng các tàu bệnh viện Khánh Hòa 01 và tàu vận tải Trường Sa bảo đảm cứu sinh và tiếp vận biển xa."
  VIE_nav_submarine_rescue_logistics_tt: "§GNâng cấp năng lực duy trì hạm đội lên mức tối ưu.§!"

  VIE_nav_spratly_dk1_defense_system: "Phòng thủ Quần đảo Trường Sa & Nhà giàn DK1"
  VIE_nav_spratly_dk1_defense_system_desc: "Kiên cố hóa công sự trận địa trên các đảo thuộc Quần đảo Trường Sa và hệ thống Nhà giàn DK1 trên thềm lục địa phía Nam, xây dựng âu tàu tránh trú bão và điểm tựa hậu cần."
  VIE_nav_spratly_dk1_defense_system_tt: "§GXây dựng công sự kiên cố và tăng cường phòng thủ đảo.§!"

  VIE_nav_integrated_undersea_warfare: "Mạng lưới Tác chiến Ngầm & Phục kích Biển"
  VIE_nav_integrated_undersea_warfare_desc: "Kết hợp hạm đội tàu ngầm Kilo, bãi mìn phong tỏa và tên lửa hành trình Club-S thành mạng lưới tác chiến ngầm hiệp đồng, sẵn sàng tung đòn phục kích bất ngờ."
  VIE_nav_integrated_undersea_warfare_tt: "§GTối ưu hóa đòn phục kích ngầm và khả năng phát hiện tàu ngầm đối phương.§!"

  VIE_nav_bastion_a2ad_coastal_shield: "Lưới lửa Bờ đối hải Bastion-P & Radar Bờ"
  VIE_nav_bastion_a2ad_coastal_shield_desc: "Triển khai các tổ hợp tên lửa bờ siêu thanh cơ động K-300P Bastion-P (Yakhont), Redut và mạng lưới trinh sát radar bờ nhìn vòng tạo nên chiếc ô A2/AD chống tiếp cận bờ biển."
  VIE_nav_bastion_a2ad_coastal_shield_tt: "§GThiết lập lưới lửa bờ đối hải siêu thanh bảo vệ toàn dải ven biển.§!"

  VIE_nav_offshore_task_groups: "Hải đội Tác chiến Biển xa Vùng đặc quyền"
  VIE_nav_offshore_task_groups_desc: "Hình thành các biên đội tàu hỗn hợp hộ vệ, tên lửa, cứu hộ và tiếp tế có khả năng tác chiến dài ngày và độc lập tại các vùng biển xa thuộc vùng đặc quyền kinh tế 200 hải lý."
  VIE_nav_offshore_task_groups_tt: "§GNâng cấp Sẵn sàng Chiến đấu Hải quân lên Cấp độ 2.§!"

  VIE_nav_c4isr_maritime_domain_awareness: "Hệ thống C4ISR & Nhận thức Không gian Biển"
  VIE_nav_c4isr_maritime_domain_awareness_desc: "Kết nối dữ liệu từ vệ tinh viễn thám Vinasat/VNREDSat, radar đối hải tầm xa và máy bay tuần thám biển vào hệ thống chỉ huy chỉ thị mục tiêu thời gian thực cho toàn quân chủng."
  VIE_nav_c4isr_maritime_domain_awareness_tt: "§GNâng cấp năng lực trinh sát phát hiện mặt nước và điều phối hiệp đồng hạm đội.§!"

  VIE_nav_naval_infantry_and_sappers: "Hải quân Đánh bộ & Đặc công Nước Đổ bộ Đảo"
  VIE_nav_naval_infantry_and_sappers_desc: "Hiện đại hóa Lữ đoàn 147, 101 Hải quân Đánh bộ và các đơn vị Đặc công nước tinh nhuệ, huấn luyện tác chiến đổ bộ đường biển, tái chiếm và phòng thủ đảo kiên cường."
  VIE_nav_naval_infantry_and_sappers_tt: "§GTăng cường phòng ngự đổ bộ và rút ngắn thời gian chuẩn bị tấn công đường biển.§!"

  VIE_nav_subsurface_steel_wall: "Thế trận Lũy thép Biển ngầm"
  VIE_nav_subsurface_steel_wall_desc: "Quy hoạch các vùng tuần tra phục kích ngầm bí mật, thiết lập mạng lưới cảm biến âm học đáy biển và thủy lôi thông minh bảo vệ các tuyến luồng hàng hải huyết mạch."
  VIE_nav_subsurface_steel_wall_tt: "§GHoàn thiện năng lực tác chiến ngầm trước ngưỡng cửa học thuyết chiến lược.§!"

  VIE_nav_integrated_island_fleet_defense: "Phòng thủ Đảo - Bờ - Hạm đội Liên hoàn"
  VIE_nav_integrated_island_fleet_defense_desc: "Tổ chức thế trận tác chiến liên hoàn giữa hỏa lực pháo - tên lửa trên các đảo, biên đội tàu cơ động mặt nước và các trận địa tên lửa bờ lục địa."
  VIE_nav_integrated_island_fleet_defense_tt: "§GTối đa hóa hiệu quả bảo vệ đảo và cự ly hoạt động của biên đội tàu.§!"

  VIE_nav_doctrine_asymmetric_sea_denial: "Học thuyết Khước từ Biển Bất đối xứng"
  VIE_nav_doctrine_asymmetric_sea_denial_desc: "Lựa chọn chiến lược tập trung nguồn lực vào tác chiến phi đối xứng: biến vùng biển thành tử địa đối với kẻ thù bằng đòn đánh ngầm tàng hình, mìn biển và tên lửa bờ siêu thanh."
  VIE_nav_doctrine_asymmetric_sea_denial_tt: "§G§YTẬP TRUNG HỌC THUYẾT:§! Tối đa hóa sức mạnh tàu ngầm, phục kích bí mật và cấm biển đối phương."

  VIE_nav_doctrine_active_maritime_presence: "Học thuyết Làm chủ Vùng biển Đặc quyền"
  VIE_nav_doctrine_active_maritime_presence_desc: "Lựa chọn chiến lược hiện diện chủ động: duy trì hải đội cơ động mặt nước tuần tra thường trực, làm chủ vùng biển đặc quyền kinh tế, bảo vệ tài nguyên dầu khí và tuyến giao thương quốc tế."
  VIE_nav_doctrine_active_maritime_presence_tt: "§G§YTẬP TRUNG HỌC THUYẾT:§! Tối đa hóa sức mạnh tàu mặt nước, tầm hoạt động hạm đội và hộ tống đường biển."

  VIE_nav_capstone_eastern_sea_sovereignty: "Giữ vững Chủ quyền Biển đảo Tổ quốc"
  VIE_nav_capstone_eastern_sea_sovereignty_desc: "Hội tụ tối thượng sức mạnh quốc phòng toàn dân trên biển: khẳng định chủ quyền toàn vẹn không thể tranh cãi trên thềm lục địa và hai quần đảo Hoàng Sa, Trường Sa thiêng liêng của Tổ quốc."
  VIE_nav_capstone_eastern_sea_sovereignty_tt: "§G§TĐỈNH CAO HẢI QUÂN:§! Nâng cấp Sẵn sàng Chiến đấu Hải quân lên Cấp 3 và khẳng định vững chắc chủ quyền biển đảo."

  # Ideas Localisation
  VIE_189th_submarine_brigade_spirit: "Lữ đoàn Tàu ngầm 189 'Hố đen Đại dương'"
  VIE_189th_submarine_brigade_spirit_desc: "Đơn vị tác chiến ngầm tinh nhuệ làm chủ tàu ngầm Kilo 636.1, sẵn sàng phục kích bí mật bảo vệ vùng biển."
  VIE_162nd_frigate_brigade_spirit: "Lữ đoàn Khinh hạm 162 'Hạm đội Thép'"
  VIE_162nd_frigate_brigade_spirit_desc: "Lực lượng tàu chiến mặt nước hiện đại nhất của Hải quân nhân dân Việt Nam, bảo đảm an ninh trên các tuyến biển xa."
  VIE_naval_weapons_integration_spirit: "Tích hợp Vũ khí Diệt hạm Uran-E & VCM-01"
  VIE_naval_weapons_integration_spirit_desc: "Khả năng làm chủ và tích hợp đạn tên lửa diệt hạm siêu thanh và đạn hành trình tầm xa lên tàu chiến."
  VIE_island_fortress_spirit: "Thế trận Pháo đài Trường Sa & Nhà giàn DK1"
  VIE_island_fortress_spirit_desc: "Hệ thống công sự kiên cố trên các đảo và nhà giàn bảo đảm khả năng trụ bám và phòng ngự kiên cường."
  VIE_undersea_warfare_network_spirit: "Mạng lưới Tác chiến Biển ngầm Hiệp đồng"
  VIE_undersea_warfare_network_spirit_desc: "Phối hợp giữa tàu ngầm, bãi mìn thông minh và đòn đánh tên lửa hành trình Club-S."
  VIE_coastal_a2ad_shield_spirit: "Lưới lửa Bờ đối hải Bastion-P A2/AD"
  VIE_coastal_a2ad_shield_spirit_desc: "Chiếc ô phòng thủ bờ biển tầm xa ngăn chặn mọi mưu toan tiếp cận bờ biển của hạm đội đối phương."
  VIE_marine_infantry_readiness_spirit: "Hải quân Đánh bộ Sẵn sàng Chiến đấu"
  VIE_marine_infantry_readiness_spirit_desc: "Khả năng phản ứng nhanh đổ bộ chiếm đảo và phòng ngự giữ vững hải đảo."
  VIE_subsurface_steel_wall_spirit: "Lũy thép Tác chiến Biển ngầm"
  VIE_subsurface_steel_wall_spirit_desc: "Mạng lưới phong tỏa ngầm ngăn chặn mọi sự xâm nhập dưới lòng biển."
  VIE_island_fleet_defense_spirit: "Hiệp đồng Phòng thủ Đảo - Hạm đội"
  VIE_island_fleet_defense_spirit_desc: "Thế trận liên hoàn kết hợp hỏa lực đảo và tính cơ động của hạm đội tàu chiến."
  VIE_doctrine_asymmetric_sea_denial_spirit: "Học thuyết Khước từ Biển Bất đối xứng"
  VIE_doctrine_asymmetric_sea_denial_spirit_desc: "Biến vùng biển thành vùng cấm đối với đối phương bằng sức mạnh răn đe ngầm và tên lửa siêu thanh."
  VIE_doctrine_active_maritime_presence_spirit: "Học thuyết Làm chủ Vùng biển Đặc quyền"
  VIE_doctrine_active_maritime_presence_spirit_desc: "Duy trì sự hiện diện thường trực bảo vệ các quyền chủ quyền và thềm lục địa của Việt Nam."
  VIE_eastern_sea_sovereignty_capstone_spirit: "Chủ quyền Biển đảo Thiêng liêng"
  VIE_eastern_sea_sovereignty_capstone_spirit_desc: "Khẳng định trọn vẹn chủ quyền biển đảo, thềm lục địa và lợi ích kinh tế biển của quốc gia."
  VIE_naval_technical_cooperation: "Hợp tác Kỹ thuật Hải quân Việt - Nga"
"""

# Loc cleanup: xoa sach cac key naval cu
lines = loc_text.splitlines()
cleaned_lines = []
skip = False
for line in lines:
    if "VIE_nav_redefine_naval_power:" in line or "# NHANH HAI QUAN NHAN DAN VIET NAM V32.1" in line:
        skip = True
    elif "VIE_force_47:" in line or "# Lực lượng tác chiến không gian mạng" in line:
        skip = False
    
    if not skip:
        # cung bo qua cac key cu
        if re.match(r'^\s*VIE_nav_\w+:', line):
            continue
        cleaned_lines.append(line)

new_loc_text = "\n".join(cleaned_lines) + "\n" + loc_entries

with open(LOC_FILE, 'w', encoding='utf-8') as f:
    f.write(new_loc_text)

print("Localisation updated successfully.")
