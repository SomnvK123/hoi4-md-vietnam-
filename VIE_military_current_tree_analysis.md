# Phân tích Hiện trạng Nhánh Quân sự (VIE_modernize_vpa - 92 Focus)

Tổng số focus: **92**
Tọa độ bao quát: x = 180 .. 220, y = 1 .. 16

## Cong nghiep quoc phong (VIE_def_) (1 focuses)

| Focus ID | x (abs) | y (abs) | relative_position_id | prerequisite | available |
|---|:---:|:---:|---|---|---|
| `VIE_def_industry_law` | 182 | 3 | `VIE_lf_army_reform` | VIE_lf_army_reform | - |

## Goc & Chien luoc tong the (5 focuses)

| Focus ID | x (abs) | y (abs) | relative_position_id | prerequisite | available |
|---|:---:|:---:|---|---|---|
| `VIE_modernize_vpa` | 200 | 1 | `VIE_doi_moi_continues` | - | - |
| `VIE_military_enterprises_core` | 180 | 4 | `VIE_def_industry_law` | VIE_def_industry_law | - |
| `VIE_military_enterprises_divest` | 182 | 4 | `VIE_def_industry_law` | VIE_def_industry_law | - |
| `VIE_path_self_reliant_deterrence` | 182 | 5 | `VIE_military_enterprises_divest` | VIE_military_enterprises_divest | - |
| `VIE_small_combatant_construction` | 206 | 5 | `VIE_ba_son_shipyards` | VIE_ba_son_shipyards | - |

## Hai quan (VIE_nf_) (22 focuses)

| Focus ID | x (abs) | y (abs) | relative_position_id | prerequisite | available |
|---|:---:|:---:|---|---|---|
| `VIE_nf_training_standardization` | 200 | 2 | `VIE_modernize_vpa` | VIE_modernize_vpa | - |
| `VIE_nf_surface_force` | 198 | 3 | `VIE_nf_training_standardization` | VIE_nf_training_standardization | - |
| `VIE_nf_submarine_force` | 200 | 3 | `VIE_nf_training_standardization` | VIE_nf_training_standardization | - |
| `VIE_nf_command_reform_1` | 198 | 4 | `VIE_nf_surface_force` | VIE_nf_surface_force | VIE_nf_submarine_force |
| `VIE_nf_first_force` | 198 | 5 | `VIE_nf_command_reform_1` | VIE_nf_command_reform_1 | VIE_naval_mro |
| `VIE_nf_command_reform_2` | 198 | 6 | `VIE_nf_first_force` | VIE_nf_first_force | - |
| `VIE_nf_medium_force` | 198 | 7 | `VIE_nf_command_reform_2` | VIE_nf_command_reform_2 | - |
| `VIE_nf_operating_range` | 198 | 8 | `VIE_nf_medium_force` | VIE_nf_medium_force | - |
| `VIE_nf_denial` | 194 | 9 | `VIE_nf_operating_range` | VIE_nf_operating_range | - |
| `VIE_nf_greenwater` | 198 | 9 | `VIE_nf_operating_range` | VIE_nf_operating_range | - |
| `VIE_nf_bluewater` | 202 | 9 | `VIE_nf_operating_range` | VIE_nf_operating_range | - |
| `VIE_nf_denial_defence` | 194 | 10 | `VIE_nf_denial` | VIE_nf_denial | - |
| `VIE_nf_regional_frigates` | 196 | 10 | `VIE_nf_greenwater` | VIE_nf_greenwater | - |
| `VIE_nf_amphibious_fleet` | 200 | 10 | `VIE_nf_greenwater` | VIE_nf_greenwater | - |
| `VIE_nf_ocean_escort` | 202 | 10 | `VIE_nf_bluewater` | VIE_nf_bluewater | - |
| `VIE_nf_replenishment` | 204 | 10 | `VIE_nf_bluewater` | VIE_nf_bluewater | - |
| `VIE_nf_naval_aviation` | 206 | 10 | `VIE_nf_bluewater` | VIE_nf_bluewater | - |
| `VIE_nf_denial_subs` | 194 | 11 | `VIE_nf_denial_defence` | VIE_nf_denial_defence | - |
| `VIE_nf_lhd_program` | 198 | 11 | `VIE_nf_regional_frigates` | VIE_nf_regional_frigates | VIE_nf_amphibious_fleet |
| `VIE_nf_carrier_group` | 204 | 11 | `VIE_nf_replenishment` | VIE_nf_replenishment | VIE_nf_ocean_escort, VIE_nf_naval_aviation |
| `VIE_nf_denial_command` | 194 | 12 | `VIE_nf_denial_subs` | VIE_nf_denial_subs | - |
| `VIE_nf_regional_command` | 198 | 12 | `VIE_nf_lhd_program` | VIE_nf_lhd_program | - |

## Hai quan bo sung / Dong tau (5 focuses)

| Focus ID | x (abs) | y (abs) | relative_position_id | prerequisite | available |
|---|:---:|:---:|---|---|---|
| `VIE_naval_defence_law` | 204 | 3 | `VIE_nf_training_standardization` | VIE_nf_training_standardization | - |
| `VIE_ba_son_shipyards` | 204 | 4 | `VIE_naval_defence_law` | VIE_naval_defence_law | - |
| `VIE_naval_mro` | 202 | 5 | `VIE_ba_son_shipyards` | VIE_ba_son_shipyards | - |
| `VIE_naval_systems_integration` | 204 | 6 | `VIE_small_combatant_construction` | VIE_small_combatant_construction | VIE_naval_mro |
| `VIE_naval_defence_2030` | 204 | 7 | `VIE_naval_systems_integration` | VIE_naval_systems_integration | VIE_naval_mro, VIE_small_combatant_construction |

## Khong quan (VIE_airf_) (22 focuses)

| Focus ID | x (abs) | y (abs) | relative_position_id | prerequisite | available |
|---|:---:|:---:|---|---|---|
| `VIE_airf_training_standardization` | 214 | 2 | `VIE_modernize_vpa` | VIE_modernize_vpa | - |
| `VIE_airf_fighter_force` | 212 | 3 | `VIE_airf_training_standardization` | VIE_airf_training_standardization | - |
| `VIE_airf_sam_force` | 214 | 3 | `VIE_airf_training_standardization` | VIE_airf_training_standardization | - |
| `VIE_airf_command_reform_1` | 212 | 4 | `VIE_airf_fighter_force` | VIE_airf_fighter_force | VIE_airf_sam_force |
| `VIE_airf_first_force` | 212 | 5 | `VIE_airf_command_reform_1` | VIE_airf_command_reform_1 | - |
| `VIE_airf_command_reform_2` | 212 | 6 | `VIE_airf_first_force` | VIE_airf_first_force | - |
| `VIE_airf_medium_force` | 214 | 7 | `VIE_airf_command_reform_2` | VIE_airf_command_reform_2 | - |
| `VIE_airf_operating_range` | 214 | 8 | `VIE_airf_medium_force` | VIE_airf_medium_force | - |
| `VIE_airf_iads` | 210 | 9 | `VIE_airf_operating_range` | VIE_airf_operating_range | - |
| `VIE_airf_multirole` | 214 | 9 | `VIE_airf_operating_range` | VIE_airf_operating_range | - |
| `VIE_airf_unmanned` | 218 | 9 | `VIE_airf_operating_range` | VIE_airf_operating_range | - |
| `VIE_airf_layered_defence` | 210 | 10 | `VIE_airf_iads` | VIE_airf_iads | - |
| `VIE_airf_multirole_fleet` | 212 | 10 | `VIE_airf_multirole` | VIE_airf_multirole | - |
| `VIE_airf_sustainment` | 214 | 10 | `VIE_airf_multirole` | VIE_airf_multirole | - |
| `VIE_airf_airlift_tanker` | 216 | 10 | `VIE_airf_multirole` | VIE_airf_multirole | - |
| `VIE_airf_isr_uav` | 218 | 10 | `VIE_airf_unmanned` | VIE_airf_unmanned | - |
| `VIE_airf_datalink` | 220 | 10 | `VIE_airf_unmanned` | VIE_airf_unmanned | - |
| `VIE_airf_ew_antistealth` | 210 | 11 | `VIE_airf_layered_defence` | VIE_airf_layered_defence | - |
| `VIE_airf_multirole_wing` | 214 | 11 | `VIE_airf_multirole_fleet` | VIE_airf_multirole_fleet | VIE_airf_sustainment, VIE_airf_airlift_tanker |
| `VIE_airf_strike_uav` | 218 | 11 | `VIE_airf_isr_uav` | VIE_airf_isr_uav | - |
| `VIE_airf_iads_command` | 210 | 12 | `VIE_airf_ew_antistealth` | VIE_airf_ew_antistealth | - |
| `VIE_airf_teaming` | 218 | 12 | `VIE_airf_strike_uav` | VIE_airf_strike_uav | VIE_airf_datalink |

## Luc quan (VIE_lf_) (30 focuses)

| Focus ID | x (abs) | y (abs) | relative_position_id | prerequisite | available |
|---|:---:|:---:|---|---|---|
| `VIE_lf_army_reform` | 186 | 2 | `VIE_modernize_vpa` | VIE_modernize_vpa | - |
| `VIE_lf_logistics_merge` | 184 | 3 | `VIE_lf_army_reform` | VIE_lf_army_reform | - |
| `VIE_lf_basic_training` | 188 | 3 | `VIE_lf_army_reform` | VIE_lf_army_reform | - |
| `VIE_lf_arm_infantry_org` | 184 | 4 | `VIE_lf_logistics_merge` | VIE_lf_logistics_merge | VIE_lf_basic_training |
| `VIE_lf_arm_armor_org` | 186 | 4 | `VIE_lf_basic_training` | VIE_lf_basic_training | VIE_lf_logistics_merge |
| `VIE_lf_arm_arty_org` | 188 | 4 | `VIE_lf_basic_training` | VIE_lf_basic_training | VIE_lf_logistics_merge |
| `VIE_lf_arm_engineers` | 190 | 4 | `VIE_lf_basic_training` | VIE_lf_basic_training | VIE_lf_logistics_merge |
| `VIE_lf_arm_infantry_train` | 184 | 5 | `VIE_lf_arm_infantry_org` | VIE_lf_arm_infantry_org | - |
| `VIE_lf_arm_armor_train` | 186 | 5 | `VIE_lf_arm_armor_org` | VIE_lf_arm_armor_org | - |
| `VIE_lf_arm_arty_train` | 188 | 5 | `VIE_lf_arm_arty_org` | VIE_lf_arm_arty_org | - |
| `VIE_lf_combined_arms` | 186 | 6 | `VIE_lf_arm_armor_train` | VIE_lf_arm_armor_train | VIE_lf_arm_infantry_train, VIE_lf_arm_arty_train, VIE_lf_arm_engineers |
| `VIE_lf_command_reform_1` | 186 | 7 | `VIE_lf_combined_arms` | VIE_lf_combined_arms | - |
| `VIE_lf_fs_mobile_force` | 184 | 8 | `VIE_lf_command_reform_1` | VIE_lf_command_reform_1 | - |
| `VIE_lf_fs_main_corps` | 186 | 8 | `VIE_lf_command_reform_1` | VIE_lf_command_reform_1 | - |
| `VIE_lf_fs_depth_defence` | 188 | 8 | `VIE_lf_command_reform_1` | VIE_lf_command_reform_1 | - |
| `VIE_lf_fs_mobile_corps` | 184 | 9 | `VIE_lf_fs_mobile_force` | VIE_lf_fs_mobile_force | - |
| `VIE_lf_fs_lean_corps` | 186 | 9 | `VIE_lf_fs_main_corps` | VIE_lf_fs_main_corps | - |
| `VIE_lf_fs_militia_units` | 188 | 9 | `VIE_lf_fs_depth_defence` | VIE_lf_fs_depth_defence | - |
| `VIE_lf_dev_strategic` | 184 | 10 | `VIE_lf_fs_mobile_corps` | VIE_lf_fs_mobile_corps | - |
| `VIE_lf_dev_territorial` | 188 | 10 | `VIE_lf_fs_militia_units` | VIE_lf_fs_militia_units | - |
| `VIE_lf_command_reform_2` | 186 | 11 | `VIE_lf_dev_strategic` | VIE_lf_dev_strategic | VIE_lf_dev_territorial |
| `VIE_lf_cap_border_urban` | 184 | 12 | `VIE_lf_command_reform_2` | VIE_lf_command_reform_2 | - |
| `VIE_lf_cap_army_ad` | 186 | 12 | `VIE_lf_command_reform_2` | VIE_lf_command_reform_2 | - |
| `VIE_lf_cap_cyber_ew` | 188 | 12 | `VIE_lf_command_reform_2` | VIE_lf_command_reform_2 | - |
| `VIE_lf_cap_area_control` | 184 | 13 | `VIE_lf_cap_border_urban` | VIE_lf_cap_border_urban | - |
| `VIE_lf_cap_ad_coord` | 186 | 13 | `VIE_lf_cap_army_ad` | VIE_lf_cap_army_ad | - |
| `VIE_lf_cap_info_ops` | 188 | 13 | `VIE_lf_cap_cyber_ew` | VIE_lf_cap_cyber_ew | - |
| `VIE_lf_selective_modernization` | 186 | 14 | `VIE_lf_cap_ad_coord` | VIE_lf_cap_ad_coord | - |
| `VIE_lf_command_reform_3` | 186 | 15 | `VIE_lf_selective_modernization` | VIE_lf_selective_modernization | - |
| `VIE_lf_force_complete` | 186 | 16 | `VIE_lf_command_reform_3` | VIE_lf_command_reform_3 | - |

## Phong khong - May bay (APM) (7 focuses)

| Focus ID | x (abs) | y (abs) | relative_position_id | prerequisite | available |
|---|:---:|:---:|---|---|---|
| `VIE_apm_law` | 218 | 3 | `VIE_airf_training_standardization` | VIE_airf_training_standardization | - |
| `VIE_apm_a32` | 216 | 4 | `VIE_apm_law` | VIE_apm_law | - |
| `VIE_apm_a31` | 218 | 4 | `VIE_apm_law` | VIE_apm_law | - |
| `VIE_apm_radar` | 220 | 4 | `VIE_apm_law` | VIE_apm_law | - |
| `VIE_apm_integration` | 216 | 5 | `VIE_apm_a32` | VIE_apm_a32 | - |
| `VIE_apm_uav` | 220 | 5 | `VIE_apm_radar` | VIE_apm_radar | - |
| `VIE_apm_mature` | 218 | 6 | `VIE_apm_integration` | VIE_apm_integration | VIE_apm_uav |

