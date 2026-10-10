# -*- coding: utf-8 -*-
"""
Script xây dựng lại nhánh Hải quân Nhân dân Việt Nam theo đồ thị Hình Quả Trám (Organic Diamond Flow)
25 Focus cân xứng toán học quanh trục tâm X=212, chuẩn quy cách Millennium Dawn (PLAN China model).
"""

import re
import os

FOCUS_FILE = 'common/national_focus/VIE_md_focus.txt'
IDEAS_FILE = 'common/ideas/VIE_md_ideas_v32_navy.txt'
DECISIONS_FILE = 'common/decisions/VIE_md_decisions_navy.txt'
OPINION_FILE = 'common/opinion_modifiers/VIE_md_opinion_modifiers.txt'
LOC_FILE = 'localisation/english/replace/VIE_md_vi_military_l_english.yml'

# 1. 25 FOCUS DEFINITIONS
focus_defs = [
    # LAYER 1: ROOT (Y=2, X=212)
    {
        "id": "VIE_nav_maritime_strategy_21st",
        "icon": "GFX_focus_VIE_naval_defence_2030",
        "x": 10,
        "y": 1,
        "rel": "VIE_modernize_vpa",
        "cost": 7,
        "prereqs": [["VIE_modernize_vpa"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_maritime_strategy_21st"
\t\t\tadd_political_power = 75
\t\t\tnavy_experience = 25
\t\t\tadd_ideas = VPA_Naval_Readiness_1
\t\t\tcustom_effect_tooltip = VIE_nav_maritime_strategy_21st_tt"""
    },

    # LAYER 2: DUAL STRATEGIC BRIDGES (Y=3, X=207 & 217)
    {
        "id": "VIE_nav_russian_naval_partnership",
        "icon": "GFX_focus_VIE_naval_mro",
        "x": -5,
        "y": 1,
        "rel": "VIE_nav_maritime_strategy_21st",
        "cost": 7,
        "prereqs": [["VIE_nav_maritime_strategy_21st"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_russian_naval_partnership"
\t\t\tnavy_experience = 30
\t\t\tadd_opinion_modifier = { target = RUS modifier = VIE_naval_technical_cooperation }
\t\t\tcustom_effect_tooltip = VIE_nav_russian_naval_partnership_tt"""
    },
    {
        "id": "VIE_nav_bason_shipbuilding_core",
        "icon": "GFX_focus_VIE_ba_son_shipyards",
        "x": 5,
        "y": 1,
        "rel": "VIE_nav_maritime_strategy_21st",
        "cost": 7,
        "prereqs": [["VIE_nav_maritime_strategy_21st"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_bason_shipbuilding_core"
\t\t\tadd_ideas = VIE_naval_shipbuilding_spirit
\t\t\t520 = {
\t\t\t\tadd_extra_state_shared_building_slots = 2
\t\t\t\tadd_building_construction = {
\t\t\t\t\ttype = dockyard
\t\t\t\t\tlevel = 1
\t\t\t\t\tinstant_build = yes
\t\t\t\t}
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_bason_shipbuilding_core_tt"""
    },

    # LAYER 3: FOUR ANCHOR WEAPONS & BASES (Y=4, X=205, 209, 215, 219)
    {
        "id": "VIE_nav_kilo_submarine_procurement",
        "icon": "GFX_focus_VIE_nf_submarine_force",
        "x": -2,
        "y": 1,
        "rel": "VIE_nav_russian_naval_partnership",
        "cost": 7,
        "prereqs": [["VIE_nav_russian_naval_partnership"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_kilo_submarine_procurement"
\t\t\tnavy_experience = 30
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t\tadd_tech_bonus = {
\t\t\t\tname = VIE_sub_tech_bonus
\t\t\t\tbonus = 0.50
\t\t\t\tuses = 2
\t\t\t\tcategory = CAT_submarines
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_kilo_submarine_procurement_tt"""
    },
    {
        "id": "VIE_nav_gepard_frigate_procurement",
        "icon": "GFX_focus_VIE_nf_regional_frigates",
        "x": 2,
        "y": 1,
        "rel": "VIE_nav_russian_naval_partnership",
        "cost": 7,
        "prereqs": [["VIE_nav_russian_naval_partnership"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_gepard_frigate_procurement"
\t\t\tnavy_experience = 30
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t\tadd_tech_bonus = {
\t\t\t\tname = VIE_frigate_tech_bonus
\t\t\t\tbonus = 0.50
\t\t\t\tuses = 2
\t\t\t\tcategory = CAT_destroyers
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_gepard_frigate_procurement_tt"""
    },
    {
        "id": "VIE_nav_molniya_fast_attack_craft",
        "icon": "GFX_focus_VIE_nf_first_force",
        "x": -2,
        "y": 1,
        "rel": "VIE_nav_bason_shipbuilding_core",
        "cost": 7,
        "prereqs": [["VIE_nav_bason_shipbuilding_core"], ["VIE_nav_russian_naval_partnership"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_molniya_fast_attack_craft"
\t\t\tnavy_experience = 25
\t\t\tswap_ideas = {
\t\t\t\tremove_idea = VIE_naval_shipbuilding_spirit
\t\t\t\tadd_idea = VIE_naval_shipbuilding_spirit_2
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_molniya_fast_attack_craft_tt"""
    },
    {
        "id": "VIE_nav_cam_ranh_naval_base",
        "icon": "GFX_focus_VIE_scs_cam_ranh_port",
        "x": 2,
        "y": 1,
        "rel": "VIE_nav_bason_shipbuilding_core",
        "cost": 7,
        "prereqs": [["VIE_nav_bason_shipbuilding_core"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_cam_ranh_naval_base"
\t\t\t522 = {
\t\t\t\tadd_building_construction = {
\t\t\t\t\ttype = naval_base
\t\t\t\t\tlevel = 2
\t\t\t\t\tinstant_build = yes
\t\t\t\t\tprovince = 7288
\t\t\t\t}
\t\t\t}
\t\t\tadd_ideas = VIE_fleet_sustainment_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_cam_ranh_naval_base_tt"""
    },

    # LAYER 4: EIGHT EXPEDITIONARY SYSTEMS (Y=5, X=205, 207, 209, 211, 213, 215, 217, 219)
    {
        "id": "VIE_nav_189th_submarine_brigade",
        "icon": "GFX_focus_VIE_nf_denial_subs",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_kilo_submarine_procurement",
        "cost": 7,
        "prereqs": [["VIE_nav_kilo_submarine_procurement"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_189th_submarine_brigade"
\t\t\tnavy_experience = 25
\t\t\tadd_ideas = VIE_189th_submarine_brigade_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_189th_submarine_brigade_tt"""
    },
    {
        "id": "VIE_nav_clubs_cruise_missiles",
        "icon": "GFX_focus_VIE_nf_denial_command",
        "x": 2,
        "y": 1,
        "rel": "VIE_nav_kilo_submarine_procurement",
        "cost": 7,
        "prereqs": [["VIE_nav_kilo_submarine_procurement"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_clubs_cruise_missiles"
\t\t\tnavy_experience = 25
\t\t\tadd_tech_bonus = {
\t\t\t\tname = VIE_missile_tech_bonus
\t\t\t\tbonus = 0.50
\t\t\t\tuses = 1
\t\t\t\tcategory = CAT_naval
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_clubs_cruise_missiles_tt"""
    },
    {
        "id": "VIE_nav_162nd_frigate_brigade",
        "icon": "GFX_focus_VIE_nf_surface_force",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_gepard_frigate_procurement",
        "cost": 7,
        "prereqs": [["VIE_nav_gepard_frigate_procurement"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_162nd_frigate_brigade"
\t\t\tnavy_experience = 25
\t\t\tadd_ideas = VIE_162nd_frigate_brigade_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_162nd_frigate_brigade_tt"""
    },
    {
        "id": "VIE_nav_naval_aviation_ka28",
        "icon": "GFX_focus_VIE_nf_naval_aviation",
        "x": 2,
        "y": 1,
        "rel": "VIE_nav_gepard_frigate_procurement",
        "cost": 5,
        "prereqs": [["VIE_nav_gepard_frigate_procurement"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_naval_aviation_ka28"
\t\t\tair_experience = 20
\t\t\tnavy_experience = 15
\t\t\tadd_tech_bonus = {
\t\t\t\tname = VIE_naval_air_tech_bonus
\t\t\t\tbonus = 0.50
\t\t\t\tuses = 1
\t\t\t\tcategory = CAT_naval
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_naval_aviation_ka28_tt"""
    },
    {
        "id": "VIE_nav_uran_e_integration",
        "icon": "GFX_focus_VIE_naval_systems_integration",
        "x": -2,
        "y": 1,
        "rel": "VIE_nav_molniya_fast_attack_craft",
        "cost": 5,
        "prereqs": [["VIE_nav_molniya_fast_attack_craft"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_uran_e_integration"
\t\t\tnavy_experience = 20
\t\t\tadd_ideas = VIE_naval_weapons_integration_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_uran_e_integration_tt"""
    },
    {
        "id": "VIE_nav_domestic_patrol_craft",
        "icon": "GFX_focus_VIE_small_combatant_construction",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_molniya_fast_attack_craft",
        "cost": 5,
        "prereqs": [["VIE_nav_molniya_fast_attack_craft"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_domestic_patrol_craft"
\t\t\t522 = {
\t\t\t\tadd_extra_state_shared_building_slots = 1
\t\t\t\tadd_building_construction = {
\t\t\t\t\ttype = dockyard
\t\t\t\t\tlevel = 1
\t\t\t\t\tinstant_build = yes
\t\t\t\t}
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_domestic_patrol_craft_tt"""
    },
    {
        "id": "VIE_nav_submarine_rescue_logistics",
        "icon": "GFX_focus_VIE_nf_replenishment",
        "x": -2,
        "y": 1,
        "rel": "VIE_nav_cam_ranh_naval_base",
        "cost": 5,
        "prereqs": [["VIE_nav_cam_ranh_naval_base"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_submarine_rescue_logistics"
\t\t\tswap_ideas = {
\t\t\t\tremove_idea = VIE_fleet_sustainment_spirit
\t\t\t\tadd_idea = VIE_fleet_sustainment_spirit_2
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_submarine_rescue_logistics_tt"""
    },
    {
        "id": "VIE_nav_spratly_dk1_defense_system",
        "icon": "GFX_focus_VIE_scs_spratly_fortification",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_cam_ranh_naval_base",
        "cost": 7,
        "prereqs": [["VIE_nav_cam_ranh_naval_base"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_spratly_dk1_defense_system"
\t\t\t524 = {
\t\t\t\tadd_building_construction = {
\t\t\t\t\ttype = coastal_bunker
\t\t\t\t\tlevel = 2
\t\t\t\t\tinstant_build = yes
\t\t\t\t\tprovince = 13247
\t\t\t\t}
\t\t\t}
\t\t\tadd_ideas = VIE_island_fortress_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_spratly_dk1_defense_system_tt"""
    },

    # LAYER 5: THREE COMBINED CAPABILITY NODES (Y=6, X=207, 212, 217)
    {
        "id": "VIE_nav_integrated_undersea_warfare",
        "icon": "GFX_focus_VIE_nf_denial",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_clubs_cruise_missiles",
        "cost": 7,
        "prereqs": [["VIE_nav_189th_submarine_brigade"], ["VIE_nav_clubs_cruise_missiles"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_integrated_undersea_warfare"
\t\t\tnavy_experience = 35
\t\t\tadd_ideas = VIE_undersea_warfare_network_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_integrated_undersea_warfare_tt"""
    },
    {
        "id": "VIE_nav_bastion_a2ad_coastal_shield",
        "icon": "GFX_focus_VIE_nf_denial_defence",
        "x": 1,
        "y": 1,
        "rel": "VIE_nav_naval_aviation_ka28",
        "cost": 7,
        "prereqs": [["VIE_nav_162nd_frigate_brigade"], ["VIE_nav_uran_e_integration"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_bastion_a2ad_coastal_shield"
\t\t\tnavy_experience = 35
\t\t\tadd_ideas = VIE_coastal_a2ad_shield_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_bastion_a2ad_coastal_shield_tt"""
    },
    {
        "id": "VIE_nav_offshore_task_groups",
        "icon": "GFX_focus_VIE_nf_ocean_escort",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_submarine_rescue_logistics",
        "cost": 7,
        "prereqs": [["VIE_nav_domestic_patrol_craft"], ["VIE_nav_submarine_rescue_logistics"], ["VIE_nav_spratly_dk1_defense_system"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_offshore_task_groups"
\t\t\tnavy_experience = 35
\t\t\tswap_ideas = {
\t\t\t\tremove_idea = VPA_Naval_Readiness_1
\t\t\t\tadd_idea = VPA_Naval_Readiness_2
\t\t\t}
\t\t\tcustom_effect_tooltip = VIE_nav_offshore_task_groups_tt"""
    },

    # LAYER 6: TWO OPERATIONAL PILLARS (Y=7, X=211 & 213)
    {
        "id": "VIE_nav_c4isr_maritime_domain_awareness",
        "icon": "GFX_focus_VIE_nf_command_reform_1",
        "x": 4,
        "y": 1,
        "rel": "VIE_nav_integrated_undersea_warfare",
        "cost": 7,
        "prereqs": [["VIE_nav_integrated_undersea_warfare"], ["VIE_nav_bastion_a2ad_coastal_shield"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_c4isr_maritime_domain_awareness"
\t\t\tnavy_experience = 30
\t\t\tadd_ideas = VIE_maritime_domain_awareness_spirit_2
\t\t\tcustom_effect_tooltip = VIE_nav_c4isr_maritime_domain_awareness_tt"""
    },
    {
        "id": "VIE_nav_naval_infantry_and_sappers",
        "icon": "GFX_focus_VIE_sf_marine",
        "x": 1,
        "y": 1,
        "rel": "VIE_nav_bastion_a2ad_coastal_shield",
        "cost": 7,
        "prereqs": [["VIE_nav_bastion_a2ad_coastal_shield"], ["VIE_nav_offshore_task_groups"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_naval_infantry_and_sappers"
\t\t\tarmy_experience = 25
\t\t\tnavy_experience = 25
\t\t\tadd_ideas = VIE_marine_infantry_readiness_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_naval_infantry_and_sappers_tt"""
    },

    # LAYER 7: PRE-DOCTRINE ADVANCED PREPARATION (Y=8, X=211 & 213)
    {
        "id": "VIE_nav_subsurface_steel_wall",
        "icon": "GFX_focus_VIE_nf_operating_range",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_c4isr_maritime_domain_awareness",
        "cost": 7,
        "prereqs": [["VIE_nav_c4isr_maritime_domain_awareness"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_subsurface_steel_wall"
\t\t\tnavy_experience = 35
\t\t\tadd_ideas = VIE_subsurface_steel_wall_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_subsurface_steel_wall_tt"""
    },
    {
        "id": "VIE_nav_integrated_island_fleet_defense",
        "icon": "GFX_focus_VIE_scs_dk1_platforms",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_naval_infantry_and_sappers",
        "cost": 7,
        "prereqs": [["VIE_nav_naval_infantry_and_sappers"]],
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_integrated_island_fleet_defense"
\t\t\tnavy_experience = 35
\t\t\tadd_ideas = VIE_island_fleet_defense_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_integrated_island_fleet_defense_tt"""
    },

    # LAYER 8: TWO MUTUALLY EXCLUSIVE DOCTRINE ARCHETYPES (Y=9, X=211 & 213)
    {
        "id": "VIE_nav_doctrine_asymmetric_sea_denial",
        "icon": "GFX_focus_VIE_nf_medium_force",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_subsurface_steel_wall",
        "cost": 10,
        "prereqs": [["VIE_nav_subsurface_steel_wall"]],
        "mutex": ["VIE_nav_doctrine_active_maritime_presence"],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_doctrine_asymmetric_sea_denial"
\t\t\tnavy_experience = 50
\t\t\tadd_ideas = VIE_doctrine_asymmetric_sea_denial_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_doctrine_asymmetric_sea_denial_tt"""
    },
    {
        "id": "VIE_nav_doctrine_active_maritime_presence",
        "icon": "GFX_focus_VIE_nf_greenwater",
        "x": 0,
        "y": 1,
        "rel": "VIE_nav_integrated_island_fleet_defense",
        "cost": 10,
        "prereqs": [["VIE_nav_integrated_island_fleet_defense"]],
        "mutex": ["VIE_nav_doctrine_asymmetric_sea_denial"],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_doctrine_active_maritime_presence"
\t\t\tnavy_experience = 50
\t\t\tadd_ideas = VIE_doctrine_active_maritime_presence_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_doctrine_active_maritime_presence_tt"""
    },

    # LAYER 9: CONVERGING DIAMOND CAPSTONE (Y=10, X=212)
    {
        "id": "VIE_nav_capstone_eastern_sea_sovereignty",
        "icon": "GFX_focus_VIE_naval_defence_law",
        "x": 1,
        "y": 1,
        "rel": "VIE_nav_doctrine_asymmetric_sea_denial",
        "cost": 10,
        "prereqs": [["VIE_nav_doctrine_asymmetric_sea_denial", "VIE_nav_doctrine_active_maritime_presence"]], # OR prereq!
        "mutex": [],
        "reward": """\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nav_capstone_eastern_sea_sovereignty"
\t\t\tadd_political_power = 150
\t\t\tnavy_experience = 50
\t\t\tswap_ideas = {
\t\t\t\tremove_idea = VPA_Naval_Readiness_2
\t\t\t\tadd_idea = VPA_Naval_Readiness_3
\t\t\t}
\t\t\tadd_ideas = VIE_eastern_sea_sovereignty_capstone_spirit
\t\t\tcustom_effect_tooltip = VIE_nav_capstone_eastern_sea_sovereignty_tt"""
    }
]

def format_focus(f):
    lines = []
    lines.append("\tfocus = {")
    lines.append(f"\t\tid = {f['id']}")
    lines.append(f"\t\ticon = {f['icon']}")
    lines.append("")
    lines.append(f"\t\tx = {f['x']}")
    lines.append(f"\t\ty = {f['y']}")
    lines.append(f"\t\trelative_position_id = {f['rel']}")
    lines.append("")
    lines.append(f"\t\tcost = {f['cost']}")
    lines.append("")
    for p_group in f['prereqs']:
        if len(p_group) == 1:
            lines.append(f"\t\tprerequisite = {{ focus = {p_group[0]} }}")
        else:
            # OR group
            f_str = " ".join([f"focus = {fid}" for fid in p_group])
            lines.append(f"\t\tprerequisite = {{ {f_str} }}")
    for m in f['mutex']:
        lines.append(f"\t\tmutually_exclusive = {{ focus = {m} }}")
    lines.append("")
    lines.append("\t\tcompletion_reward = {")
    lines.append(f['reward'])
    lines.append("\t\t}")
    lines.append("\t}")
    return "\n".join(lines)

# Generate focus block
header = """\t# ======================================================================
\t# NHANH HAI QUAN NHAN DAN VIET NAM (VPN) - ORGANIC DIAMOND FLOW (25 FOCUS)
\t# Kien truc Hinh Qua Tram / Canh Buom can xung quanh truc tam X=212
\t# ======================================================================\n\n"""

focus_block_content = header + "\n\n".join([format_focus(f) for f in focus_defs])

print("Focus block generated successfully! Total length:", len(focus_block_content))
