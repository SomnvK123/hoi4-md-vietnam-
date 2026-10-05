import sys, os
sys.path.insert(0, os.path.abspath("."))
import re
import tools.analyze_military as am

# Compact Military Layout (Chuẩn Hàng ngang Tối ưu Spacing)
# Root: VIE_modernize_vpa (200, 1) -> dx=-14 (Army), dx=0 (Navy), dx=+14 (Air Force)
# Army: x = 180 .. 190 (center 186)
# Navy: x = 194 .. 206 (center 200)
# Air Force: x = 210 .. 220 (center 214..215)
# Gaps between services: exactly 4 units (190 to 194, 206 to 210)
# All dy = 1 (no empty rows in Navy or APM)
# All sub-branch internal |dx| <= 4 (mostly 0 or 2)

military_layout = {
    # ROOT
    "VIE_modernize_vpa": {
        "rel": "VIE_doi_moi_continues", "dx": 120, "dy": 1, # abs (200, 1)
        "prereqs": [], "avail": []
    },

    # =========================================================
    # TRUC 1: LUC QUAN & CNQP LUC QUAN (34 focuses)
    # Zone: x = 180 .. 190 (center 186)
    # =========================================================
    # y = 2
    "VIE_lf_army_reform": {
        "rel": "VIE_modernize_vpa", "dx": -14, "dy": 1, # abs (186, 2)
        "prereqs": ["VIE_modernize_vpa"], "avail": []
    },
    # y = 3 (3 focuses: 182, 184, 188)
    "VIE_def_industry_law": {
        "rel": "VIE_lf_army_reform", "dx": -4, "dy": 1, # abs (182, 3)
        "prereqs": ["VIE_lf_army_reform"], "avail": []
    },
    "VIE_lf_logistics_merge": {
        "rel": "VIE_lf_army_reform", "dx": -2, "dy": 1, # abs (184, 3)
        "prereqs": ["VIE_lf_army_reform"], "avail": []
    },
    "VIE_lf_basic_training": {
        "rel": "VIE_lf_army_reform", "dx": 2, "dy": 1, # abs (188, 3)
        "prereqs": ["VIE_lf_army_reform"], "avail": []
    },
    # y = 4 (6 focuses: 180, 182, 184, 186, 188, 190)
    "VIE_military_enterprises_core": {
        "rel": "VIE_def_industry_law", "dx": -2, "dy": 1, # abs (180, 4)
        "prereqs": ["VIE_def_industry_law"], "avail": []
    },
    "VIE_military_enterprises_divest": {
        "rel": "VIE_def_industry_law", "dx": 0, "dy": 1, # abs (182, 4)
        "prereqs": ["VIE_def_industry_law"], "avail": []
    },
    "VIE_lf_arm_infantry_org": {
        "rel": "VIE_lf_logistics_merge", "dx": 0, "dy": 1, # abs (184, 4)
        "prereqs": ["VIE_lf_logistics_merge"], "avail": ["VIE_lf_basic_training"]
    },
    "VIE_lf_arm_armor_org": {
        "rel": "VIE_lf_basic_training", "dx": -2, "dy": 1, # abs (186, 4)
        "prereqs": ["VIE_lf_basic_training"], "avail": ["VIE_lf_logistics_merge"]
    },
    "VIE_lf_arm_arty_org": {
        "rel": "VIE_lf_basic_training", "dx": 0, "dy": 1, # abs (188, 4)
        "prereqs": ["VIE_lf_basic_training"], "avail": ["VIE_lf_logistics_merge"]
    },
    "VIE_lf_arm_engineers": {
        "rel": "VIE_lf_basic_training", "dx": 2, "dy": 1, # abs (190, 4)
        "prereqs": ["VIE_lf_basic_training"], "avail": ["VIE_lf_logistics_merge"]
    },
    # y = 5 (4 focuses: 182, 184, 186, 188)
    "VIE_path_self_reliant_deterrence": {
        "rel": "VIE_military_enterprises_divest", "dx": 0, "dy": 1, # abs (182, 5)
        "prereqs": ["VIE_military_enterprises_divest"], "avail": []
    },
    "VIE_lf_arm_infantry_train": {
        "rel": "VIE_lf_arm_infantry_org", "dx": 0, "dy": 1, # abs (184, 5)
        "prereqs": ["VIE_lf_arm_infantry_org"], "avail": []
    },
    "VIE_lf_arm_armor_train": {
        "rel": "VIE_lf_arm_armor_org", "dx": 0, "dy": 1, # abs (186, 5)
        "prereqs": ["VIE_lf_arm_armor_org"], "avail": []
    },
    "VIE_lf_arm_arty_train": {
        "rel": "VIE_lf_arm_arty_org", "dx": 0, "dy": 1, # abs (188, 5)
        "prereqs": ["VIE_lf_arm_arty_org"], "avail": []
    },
    # y = 6 (1 focus: 186)
    "VIE_lf_combined_arms": {
        "rel": "VIE_lf_arm_armor_train", "dx": 0, "dy": 1, # abs (186, 6)
        "prereqs": ["VIE_lf_arm_armor_train"], "avail": ["VIE_lf_arm_infantry_train", "VIE_lf_arm_arty_train", "VIE_lf_arm_engineers"]
    },
    # y = 7 (1 focus: 186)
    "VIE_lf_command_reform_1": {
        "rel": "VIE_lf_combined_arms", "dx": 0, "dy": 1, # abs (186, 7)
        "prereqs": ["VIE_lf_combined_arms"], "avail": []
    },
    # y = 8 (3 focuses: 184, 186, 188)
    "VIE_lf_fs_mobile_force": {
        "rel": "VIE_lf_command_reform_1", "dx": -2, "dy": 1, # abs (184, 8)
        "prereqs": ["VIE_lf_command_reform_1"], "avail": []
    },
    "VIE_lf_fs_main_corps": {
        "rel": "VIE_lf_command_reform_1", "dx": 0, "dy": 1, # abs (186, 8)
        "prereqs": ["VIE_lf_command_reform_1"], "avail": []
    },
    "VIE_lf_fs_depth_defence": {
        "rel": "VIE_lf_command_reform_1", "dx": 2, "dy": 1, # abs (188, 8)
        "prereqs": ["VIE_lf_command_reform_1"], "avail": []
    },
    # y = 9 (3 focuses: 184, 186, 188)
    "VIE_lf_fs_mobile_corps": {
        "rel": "VIE_lf_fs_mobile_force", "dx": 0, "dy": 1, # abs (184, 9)
        "prereqs": ["VIE_lf_fs_mobile_force"], "avail": []
    },
    "VIE_lf_fs_lean_corps": {
        "rel": "VIE_lf_fs_main_corps", "dx": 0, "dy": 1, # abs (186, 9)
        "prereqs": ["VIE_lf_fs_main_corps"], "avail": []
    },
    "VIE_lf_fs_militia_units": {
        "rel": "VIE_lf_fs_depth_defence", "dx": 0, "dy": 1, # abs (188, 9)
        "prereqs": ["VIE_lf_fs_depth_defence"], "avail": []
    },
    # y = 10 (2 focuses: 184, 188)
    "VIE_lf_dev_strategic": {
        "rel": "VIE_lf_fs_mobile_corps", "dx": 0, "dy": 1, # abs (184, 10)
        "prereqs": ["VIE_lf_fs_mobile_corps"], "avail": []
    },
    "VIE_lf_dev_territorial": {
        "rel": "VIE_lf_fs_militia_units", "dx": 0, "dy": 1, # abs (188, 10)
        "prereqs": ["VIE_lf_fs_militia_units"], "avail": []
    },
    # y = 11 (1 focus: 186)
    "VIE_lf_command_reform_2": {
        "rel": "VIE_lf_dev_strategic", "dx": 2, "dy": 1, # abs (186, 11)
        "prereqs": ["VIE_lf_dev_strategic"], "avail": ["VIE_lf_dev_territorial"]
    },
    # y = 12 (3 focuses: 184, 186, 188)
    "VIE_lf_cap_border_urban": {
        "rel": "VIE_lf_command_reform_2", "dx": -2, "dy": 1, # abs (184, 12)
        "prereqs": ["VIE_lf_command_reform_2"], "avail": []
    },
    "VIE_lf_cap_army_ad": {
        "rel": "VIE_lf_command_reform_2", "dx": 0, "dy": 1, # abs (186, 12)
        "prereqs": ["VIE_lf_command_reform_2"], "avail": []
    },
    "VIE_lf_cap_cyber_ew": {
        "rel": "VIE_lf_command_reform_2", "dx": 2, "dy": 1, # abs (188, 12)
        "prereqs": ["VIE_lf_command_reform_2"], "avail": []
    },
    # y = 13 (3 focuses: 184, 186, 188)
    "VIE_lf_cap_area_control": {
        "rel": "VIE_lf_cap_border_urban", "dx": 0, "dy": 1, # abs (184, 13)
        "prereqs": ["VIE_lf_cap_border_urban"], "avail": []
    },
    "VIE_lf_cap_ad_coord": {
        "rel": "VIE_lf_cap_army_ad", "dx": 0, "dy": 1, # abs (186, 13)
        "prereqs": ["VIE_lf_cap_army_ad"], "avail": []
    },
    "VIE_lf_cap_info_ops": {
        "rel": "VIE_lf_cap_cyber_ew", "dx": 0, "dy": 1, # abs (188, 13)
        "prereqs": ["VIE_lf_cap_cyber_ew"], "avail": []
    },
    # y = 14 (1 focus: 186)
    "VIE_lf_selective_modernization": {
        "rel": "VIE_lf_cap_ad_coord", "dx": 0, "dy": 1, # abs (186, 14)
        "prereqs": ["VIE_lf_cap_ad_coord"], "avail": []
    },
    # y = 15 (1 focus: 186)
    "VIE_lf_command_reform_3": {
        "rel": "VIE_lf_selective_modernization", "dx": 0, "dy": 1, # abs (186, 15)
        "prereqs": ["VIE_lf_selective_modernization"], "avail": []
    },
    # y = 16 (1 focus: 186)
    "VIE_lf_force_complete": {
        "rel": "VIE_lf_command_reform_3", "dx": 0, "dy": 1, # abs (186, 16)
        "prereqs": ["VIE_lf_command_reform_3"], "avail": []
    },

    # =========================================================
    # TRUC 2: HAI QUAN & DONG TAU BA SON (28 focuses)
    # Zone: x = 194 .. 206 (center 200)
    # =========================================================
    # y = 2
    "VIE_nf_training_standardization": {
        "rel": "VIE_modernize_vpa", "dx": 0, "dy": 1, # abs (200, 2)
        "prereqs": ["VIE_modernize_vpa"], "avail": []
    },
    # y = 3 (3 focuses: 198, 200, 204)
    "VIE_nf_surface_force": {
        "rel": "VIE_nf_training_standardization", "dx": -2, "dy": 1, # abs (198, 3)
        "prereqs": ["VIE_nf_training_standardization"], "avail": []
    },
    "VIE_nf_submarine_force": {
        "rel": "VIE_nf_training_standardization", "dx": 0, "dy": 1, # abs (200, 3)
        "prereqs": ["VIE_nf_training_standardization"], "avail": []
    },
    "VIE_naval_defence_law": {
        "rel": "VIE_nf_training_standardization", "dx": 4, "dy": 1, # abs (204, 3)
        "prereqs": ["VIE_nf_training_standardization"], "avail": []
    },
    # y = 4 (2 focuses: 198, 204)
    "VIE_nf_command_reform_1": {
        "rel": "VIE_nf_surface_force", "dx": 0, "dy": 1, # abs (198, 4)
        "prereqs": ["VIE_nf_surface_force"], "avail": ["VIE_nf_submarine_force"]
    },
    "VIE_ba_son_shipyards": {
        "rel": "VIE_naval_defence_law", "dx": 0, "dy": 1, # abs (204, 4)
        "prereqs": ["VIE_naval_defence_law"], "avail": []
    },
    # y = 5 (3 focuses: 198, 202, 206) - NO EMPTY HOLE! first_force at y=5!
    "VIE_nf_first_force": {
        "rel": "VIE_nf_command_reform_1", "dx": 0, "dy": 1, # abs (198, 5)
        "prereqs": ["VIE_nf_command_reform_1"], "avail": ["VIE_naval_mro"]
    },
    "VIE_naval_mro": {
        "rel": "VIE_ba_son_shipyards", "dx": -2, "dy": 1, # abs (202, 5)
        "prereqs": ["VIE_ba_son_shipyards"], "avail": []
    },
    "VIE_small_combatant_construction": {
        "rel": "VIE_ba_son_shipyards", "dx": 2, "dy": 1, # abs (206, 5)
        "prereqs": ["VIE_ba_son_shipyards"], "avail": []
    },
    # y = 6 (2 focuses: 198, 204)
    "VIE_nf_command_reform_2": {
        "rel": "VIE_nf_first_force", "dx": 0, "dy": 1, # abs (198, 6)
        "prereqs": ["VIE_nf_first_force"], "avail": []
    },
    "VIE_naval_systems_integration": {
        "rel": "VIE_small_combatant_construction", "dx": -2, "dy": 1, # abs (204, 6)
        "prereqs": ["VIE_small_combatant_construction"], "avail": ["VIE_naval_mro"]
    },
    # y = 7 (2 focuses: 198, 204)
    "VIE_nf_medium_force": {
        "rel": "VIE_nf_command_reform_2", "dx": 0, "dy": 1, # abs (198, 7)
        "prereqs": ["VIE_nf_command_reform_2"], "avail": []
    },
    "VIE_naval_defence_2030": {
        "rel": "VIE_naval_systems_integration", "dx": 0, "dy": 1, # abs (204, 7)
        "prereqs": ["VIE_naval_systems_integration"], "avail": ["VIE_naval_mro", "VIE_small_combatant_construction"]
    },
    # y = 8 (1 focus: 198)
    "VIE_nf_operating_range": {
        "rel": "VIE_nf_medium_force", "dx": 0, "dy": 1, # abs (198, 8)
        "prereqs": ["VIE_nf_medium_force"], "avail": []
    },
    # y = 9 (3 focuses: 194, 198, 202)
    "VIE_nf_denial": {
        "rel": "VIE_nf_operating_range", "dx": -4, "dy": 1, # abs (194, 9)
        "prereqs": ["VIE_nf_operating_range"], "avail": []
    },
    "VIE_nf_greenwater": {
        "rel": "VIE_nf_operating_range", "dx": 0, "dy": 1, # abs (198, 9)
        "prereqs": ["VIE_nf_operating_range"], "avail": []
    },
    "VIE_nf_bluewater": {
        "rel": "VIE_nf_operating_range", "dx": 4, "dy": 1, # abs (202, 9)
        "prereqs": ["VIE_nf_operating_range"], "avail": []
    },
    # y = 10 (6 focuses: 194, 196, 200, 202, 204, 206)
    "VIE_nf_denial_defence": {
        "rel": "VIE_nf_denial", "dx": 0, "dy": 1, # abs (194, 10)
        "prereqs": ["VIE_nf_denial"], "avail": []
    },
    "VIE_nf_regional_frigates": {
        "rel": "VIE_nf_greenwater", "dx": -2, "dy": 1, # abs (196, 10)
        "prereqs": ["VIE_nf_greenwater"], "avail": []
    },
    "VIE_nf_amphibious_fleet": {
        "rel": "VIE_nf_greenwater", "dx": 2, "dy": 1, # abs (200, 10)
        "prereqs": ["VIE_nf_greenwater"], "avail": []
    },
    "VIE_nf_ocean_escort": {
        "rel": "VIE_nf_bluewater", "dx": 0, "dy": 1, # abs (202, 10)
        "prereqs": ["VIE_nf_bluewater"], "avail": []
    },
    "VIE_nf_replenishment": {
        "rel": "VIE_nf_bluewater", "dx": 2, "dy": 1, # abs (204, 10)
        "prereqs": ["VIE_nf_bluewater"], "avail": []
    },
    "VIE_nf_naval_aviation": {
        "rel": "VIE_nf_bluewater", "dx": 4, "dy": 1, # abs (206, 10)
        "prereqs": ["VIE_nf_bluewater"], "avail": []
    },
    # y = 11 (3 focuses: 194, 198, 204)
    "VIE_nf_denial_subs": {
        "rel": "VIE_nf_denial_defence", "dx": 0, "dy": 1, # abs (194, 11)
        "prereqs": ["VIE_nf_denial_defence"], "avail": []
    },
    "VIE_nf_lhd_program": {
        "rel": "VIE_nf_regional_frigates", "dx": 2, "dy": 1, # abs (198, 11)
        "prereqs": ["VIE_nf_regional_frigates"], "avail": ["VIE_nf_amphibious_fleet"]
    },
    "VIE_nf_carrier_group": {
        "rel": "VIE_nf_replenishment", "dx": 0, "dy": 1, # abs (204, 11)
        "prereqs": ["VIE_nf_replenishment"], "avail": ["VIE_nf_ocean_escort", "VIE_nf_naval_aviation"]
    },
    # y = 12 (2 focuses: 194, 198)
    "VIE_nf_denial_command": {
        "rel": "VIE_nf_denial_subs", "dx": 0, "dy": 1, # abs (194, 12)
        "prereqs": ["VIE_nf_denial_subs"], "avail": []
    },
    "VIE_nf_regional_command": {
        "rel": "VIE_nf_lhd_program", "dx": 0, "dy": 1, # abs (198, 12)
        "prereqs": ["VIE_nf_lhd_program"], "avail": []
    },

    # =========================================================
    # TRUC 3: PHONG KHONG - KHONG QUAN & APM (29 focuses)
    # Zone: x = 210 .. 220 (center 214..215)
    # =========================================================
    # y = 2
    "VIE_airf_training_standardization": {
        "rel": "VIE_modernize_vpa", "dx": 14, "dy": 1, # abs (214, 2)
        "prereqs": ["VIE_modernize_vpa"], "avail": []
    },
    # y = 3 (3 focuses: 212, 214, 218)
    "VIE_airf_fighter_force": {
        "rel": "VIE_airf_training_standardization", "dx": -2, "dy": 1, # abs (212, 3)
        "prereqs": ["VIE_airf_training_standardization"], "avail": []
    },
    "VIE_airf_sam_force": {
        "rel": "VIE_airf_training_standardization", "dx": 0, "dy": 1, # abs (214, 3)
        "prereqs": ["VIE_airf_training_standardization"], "avail": []
    },
    "VIE_apm_law": {
        "rel": "VIE_airf_training_standardization", "dx": 4, "dy": 1, # abs (218, 3)
        "prereqs": ["VIE_airf_training_standardization"], "avail": []
    },
    # y = 4 (4 focuses: 212, 216, 218, 220)
    "VIE_airf_command_reform_1": {
        "rel": "VIE_airf_fighter_force", "dx": 0, "dy": 1, # abs (212, 4)
        "prereqs": ["VIE_airf_fighter_force"], "avail": ["VIE_airf_sam_force"]
    },
    "VIE_apm_a32": {
        "rel": "VIE_apm_law", "dx": -2, "dy": 1, # abs (216, 4)
        "prereqs": ["VIE_apm_law"], "avail": []
    },
    "VIE_apm_a31": {
        "rel": "VIE_apm_law", "dx": 0, "dy": 1, # abs (218, 4)
        "prereqs": ["VIE_apm_law"], "avail": []
    },
    "VIE_apm_radar": {
        "rel": "VIE_apm_law", "dx": 2, "dy": 1, # abs (220, 4)
        "prereqs": ["VIE_apm_law"], "avail": []
    },
    # y = 5 (3 focuses: 212, 216, 220) - NO EMPTY HOLES! integration & uav at y=5!
    "VIE_airf_first_force": {
        "rel": "VIE_airf_command_reform_1", "dx": 0, "dy": 1, # abs (212, 5)
        "prereqs": ["VIE_airf_command_reform_1"], "avail": []
    },
    "VIE_apm_integration": {
        "rel": "VIE_apm_a32", "dx": 0, "dy": 1, # abs (216, 5)
        "prereqs": ["VIE_apm_a32"], "avail": []
    },
    "VIE_apm_uav": {
        "rel": "VIE_apm_radar", "dx": 0, "dy": 1, # abs (220, 5)
        "prereqs": ["VIE_apm_radar"], "avail": []
    },
    # y = 6 (2 focuses: 212, 218) - apm_mature at y=6!
    "VIE_airf_command_reform_2": {
        "rel": "VIE_airf_first_force", "dx": 0, "dy": 1, # abs (212, 6)
        "prereqs": ["VIE_airf_first_force"], "avail": []
    },
    "VIE_apm_mature": {
        "rel": "VIE_apm_integration", "dx": 2, "dy": 1, # abs (218, 6)
        "prereqs": ["VIE_apm_integration"], "avail": ["VIE_apm_uav"]
    },
    # y = 7 (1 focus: 214)
    "VIE_airf_medium_force": {
        "rel": "VIE_airf_command_reform_2", "dx": 2, "dy": 1, # abs (214, 7)
        "prereqs": ["VIE_airf_command_reform_2"], "avail": []
    },
    # y = 8 (1 focus: 214)
    "VIE_airf_operating_range": {
        "rel": "VIE_airf_medium_force", "dx": 0, "dy": 1, # abs (214, 8)
        "prereqs": ["VIE_airf_medium_force"], "avail": []
    },
    # y = 9 (3 focuses: 210, 214, 218)
    "VIE_airf_iads": {
        "rel": "VIE_airf_operating_range", "dx": -4, "dy": 1, # abs (210, 9)
        "prereqs": ["VIE_airf_operating_range"], "avail": []
    },
    "VIE_airf_multirole": {
        "rel": "VIE_airf_operating_range", "dx": 0, "dy": 1, # abs (214, 9)
        "prereqs": ["VIE_airf_operating_range"], "avail": []
    },
    "VIE_airf_unmanned": {
        "rel": "VIE_airf_operating_range", "dx": 4, "dy": 1, # abs (218, 9)
        "prereqs": ["VIE_airf_operating_range"], "avail": []
    },
    # y = 10 (6 focuses: 210, 212, 214, 216, 218, 220)
    "VIE_airf_layered_defence": {
        "rel": "VIE_airf_iads", "dx": 0, "dy": 1, # abs (210, 10)
        "prereqs": ["VIE_airf_iads"], "avail": []
    },
    "VIE_airf_multirole_fleet": {
        "rel": "VIE_airf_multirole", "dx": -2, "dy": 1, # abs (212, 10)
        "prereqs": ["VIE_airf_multirole"], "avail": []
    },
    "VIE_airf_sustainment": {
        "rel": "VIE_airf_multirole", "dx": 0, "dy": 1, # abs (214, 10)
        "prereqs": ["VIE_airf_multirole"], "avail": []
    },
    "VIE_airf_airlift_tanker": {
        "rel": "VIE_airf_multirole", "dx": 2, "dy": 1, # abs (216, 10)
        "prereqs": ["VIE_airf_multirole"], "avail": []
    },
    "VIE_airf_isr_uav": {
        "rel": "VIE_airf_unmanned", "dx": 0, "dy": 1, # abs (218, 10)
        "prereqs": ["VIE_airf_unmanned"], "avail": []
    },
    "VIE_airf_datalink": {
        "rel": "VIE_airf_unmanned", "dx": 2, "dy": 1, # abs (220, 10)
        "prereqs": ["VIE_airf_unmanned"], "avail": []
    },
    # y = 11 (3 focuses: 210, 214, 218)
    "VIE_airf_ew_antistealth": {
        "rel": "VIE_airf_layered_defence", "dx": 0, "dy": 1, # abs (210, 11)
        "prereqs": ["VIE_airf_layered_defence"], "avail": []
    },
    "VIE_airf_multirole_wing": {
        "rel": "VIE_airf_multirole_fleet", "dx": 2, "dy": 1, # abs (214, 11)
        "prereqs": ["VIE_airf_multirole_fleet"], "avail": ["VIE_airf_sustainment", "VIE_airf_airlift_tanker"]
    },
    "VIE_airf_strike_uav": {
        "rel": "VIE_airf_isr_uav", "dx": 0, "dy": 1, # abs (218, 11)
        "prereqs": ["VIE_airf_isr_uav"], "avail": []
    },
    # y = 12 (2 focuses: 210, 218)
    "VIE_airf_iads_command": {
        "rel": "VIE_airf_ew_antistealth", "dx": 0, "dy": 1, # abs (210, 12)
        "prereqs": ["VIE_airf_ew_antistealth"], "avail": []
    },
    "VIE_airf_teaming": {
        "rel": "VIE_airf_strike_uav", "dx": 0, "dy": 1, # abs (218, 12)
        "prereqs": ["VIE_airf_strike_uav"], "avail": ["VIE_airf_datalink"]
    }
}

abs_coords = {}
def get_abs_pos(fid, visited=None):
    if visited is None:
        visited = set()
    if fid in visited:
        return (0, 0)
    visited.add(fid)
    entry = military_layout[fid]
    parent = entry["rel"]
    if parent == "VIE_doi_moi_continues":
        return (80 + entry["dx"], 0 + entry["dy"])
    px, py = get_abs_pos(parent, visited)
    return (px + entry["dx"], py + entry["dy"])

for fid in military_layout:
    abs_coords[fid] = get_abs_pos(fid)

if __name__ == "__main__":
    print(f"Total mapped focuses: {len(abs_coords)} (expected 92)")
    
    # Internal collisions
    coord_map = {}
    collisions = []
    for fid, (ax, ay) in abs_coords.items():
        if (ax, ay) in coord_map:
            collisions.append((fid, coord_map[(ax, ay)], (ax, ay)))
        else:
            coord_map[(ax, ay)] = fid

    print(f"Collisions within military: {len(collisions)}")
    for c in collisions:
        print("  Collision:", c)

    # External collisions
    external_collisions = []
    for fid, (ax, ay) in abs_coords.items():
        for ext_fid, ext_f in am.focuses.items():
            if ext_fid not in military_layout:
                if (ext_f['abs_x'], ext_f['abs_y']) == (ax, ay):
                    external_collisions.append((fid, ext_fid, (ax, ay)))

    print(f"Collisions with non-military: {len(external_collisions)}")
    for c in external_collisions:
        print("  External collision:", c)

    # Gap violations
    rows = {}
    for fid, (ax, ay) in abs_coords.items():
        rows.setdefault(ay, []).append((ax, fid))

    gap_violations = []
    print("\n=== COMPACT ROWS ===")
    for y in sorted(rows.keys()):
        items = sorted(rows[y], key=lambda x: x[0])
        row_str = ", ".join([f"{fid}(x={ax})" for ax, fid in items])
        print(f"Row y={y:2} ({len(items):2} focuses): {row_str}")
        for k in range(len(items) - 1):
            dx = items[k+1][0] - items[k][0]
            if dx < 2:
                gap_violations.append((items[k][1], items[k+1][1], y, dx))

    print(f"\nGap violations (dx < 2): {len(gap_violations)}")
    for g in gap_violations:
        print("  Gap violation:", g)

    # Prerequisite y_child > y_parent check
    prereq_violations = []
    for fid, entry in military_layout.items():
        ax, ay = abs_coords[fid]
        for p in entry["prereqs"]:
            if p in abs_coords:
                p_ax, p_ay = abs_coords[p]
                if ay <= p_ay:
                    prereq_violations.append((fid, p, ay, p_ay))

    print(f"Prerequisite y_child <= y_parent violations: {len(prereq_violations)}")
    for pv in prereq_violations:
        print("  Prereq violation:", pv)
