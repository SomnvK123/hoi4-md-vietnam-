import sys, os
sys.path.insert(0, os.path.abspath("."))
import re
import tools.test_military_layout as tml

# Topological order of the 92 focuses
ordered_fids = [
    # ROOT
    "VIE_modernize_vpa",

    # TRUC 1: LUC QUAN & CNQP LUC QUAN (34 focus)
    "VIE_lf_army_reform",
    "VIE_def_industry_law",
    "VIE_lf_logistics_merge",
    "VIE_lf_basic_training",
    "VIE_military_enterprises_core",
    "VIE_military_enterprises_divest",
    "VIE_path_self_reliant_deterrence",
    "VIE_lf_arm_infantry_org",
    "VIE_lf_arm_armor_org",
    "VIE_lf_arm_arty_org",
    "VIE_lf_arm_engineers",
    "VIE_lf_arm_infantry_train",
    "VIE_lf_arm_armor_train",
    "VIE_lf_arm_arty_train",
    "VIE_lf_combined_arms",
    "VIE_lf_command_reform_1",
    "VIE_lf_fs_mobile_force",
    "VIE_lf_fs_main_corps",
    "VIE_lf_fs_depth_defence",
    "VIE_lf_fs_mobile_corps",
    "VIE_lf_fs_lean_corps",
    "VIE_lf_fs_militia_units",
    "VIE_lf_dev_strategic",
    "VIE_lf_dev_territorial",
    "VIE_lf_command_reform_2",
    "VIE_lf_cap_border_urban",
    "VIE_lf_cap_army_ad",
    "VIE_lf_cap_cyber_ew",
    "VIE_lf_cap_area_control",
    "VIE_lf_cap_ad_coord",
    "VIE_lf_cap_info_ops",
    "VIE_lf_selective_modernization",
    "VIE_lf_command_reform_3",
    "VIE_lf_force_complete",

    # TRUC 2: HAI QUAN & DONG TAU BA SON (28 focus)
    "VIE_nf_training_standardization",
    "VIE_nf_surface_force",
    "VIE_nf_submarine_force",
    "VIE_naval_defence_law",
    "VIE_nf_command_reform_1",
    "VIE_ba_son_shipyards",
    "VIE_naval_mro",
    "VIE_small_combatant_construction",
    "VIE_nf_first_force",
    "VIE_naval_systems_integration",
    "VIE_nf_command_reform_2",
    "VIE_naval_defence_2030",
    "VIE_nf_medium_force",
    "VIE_nf_operating_range",
    "VIE_nf_denial",
    "VIE_nf_greenwater",
    "VIE_nf_bluewater",
    "VIE_nf_denial_defence",
    "VIE_nf_regional_frigates",
    "VIE_nf_amphibious_fleet",
    "VIE_nf_ocean_escort",
    "VIE_nf_replenishment",
    "VIE_nf_naval_aviation",
    "VIE_nf_denial_subs",
    "VIE_nf_lhd_program",
    "VIE_nf_carrier_group",
    "VIE_nf_denial_command",
    "VIE_nf_regional_command",

    # TRUC 3: PHONG KHONG - KHONG QUAN & APM (29 focus)
    "VIE_airf_training_standardization",
    "VIE_airf_fighter_force",
    "VIE_airf_sam_force",
    "VIE_apm_law",
    "VIE_airf_command_reform_1",
    "VIE_apm_a32",
    "VIE_apm_a31",
    "VIE_apm_radar",
    "VIE_airf_first_force",
    "VIE_airf_command_reform_2",
    "VIE_apm_integration",
    "VIE_apm_uav",
    "VIE_airf_medium_force",
    "VIE_airf_operating_range",
    "VIE_apm_mature",
    "VIE_airf_iads",
    "VIE_airf_multirole",
    "VIE_airf_unmanned",
    "VIE_airf_layered_defence",
    "VIE_airf_multirole_fleet",
    "VIE_airf_sustainment",
    "VIE_airf_airlift_tanker",
    "VIE_airf_isr_uav",
    "VIE_airf_datalink",
    "VIE_airf_ew_antistealth",
    "VIE_airf_multirole_wing",
    "VIE_airf_strike_uav",
    "VIE_airf_iads_command",
    "VIE_airf_teaming"
]

print(f"Total ordered focuses: {len(ordered_fids)}")
missing = [fid for fid in tml.military_layout if fid not in ordered_fids]
print(f"Missing from order list: {missing}")

# Verify 0 forward references in this order
order_dict = {fid: idx for idx, fid in enumerate(ordered_fids)}
fwd_refs = []
for fid in ordered_fids:
    entry = tml.military_layout[fid]
    parent = entry['rel']
    if parent in order_dict:
        if order_dict[parent] >= order_dict[fid]:
            fwd_refs.append(f"{fid} (order {order_dict[fid]}) references future {parent} (order {order_dict[parent]})")

print(f"Forward references in planned order: {len(fwd_refs)}")
for fr in fwd_refs:
    print("  ", fr)
