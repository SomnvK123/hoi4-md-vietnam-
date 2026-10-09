# PK-KQ focus relationships and rewards v19-v24

Current tree: 37 focuses (29 retained original IDs, three structures, four readiness focuses, one integrated capstone). V24 assigns the branch to Y1-Y12: First Force needs all four Y4 readiness focuses; the three specialty roots and capstones align by column; Datalink is a UAV child and a visible Teaming prerequisite; tanker has a support row; Integrated Force retains its 2/3 capstone availability gate. The full focus tree has 424 entries, including 387 outside this branch.

| Focus | Previous parent | Current parent | Reward / gate |
|---|---|---|---|
| `VIE_airf_training_standardization` | (modernize_vpa) | (modernize_vpa) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_airf_sam_force` | (airf_training_standardization) | (airf_training_standardization) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_airf_fighter_force` | (airf_training_standardization) | (airf_training_standardization) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_apm_law` | (airf_training_standardization) | (airf_training_standardization) | Giữ reward; cụm công nghiệp mở trực tiếp từ root không quân |
| `VIE_airf_command_reform_1` | (airf_fighter_force) AND (airf_sam_force) | (airf_fighter_force) AND (airf_sam_force) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_apm_a32` | (apm_law) | (apm_law) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_apm_a31` | (apm_law) | (apm_law) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_apm_radar` | (apm_law) | (apm_law) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_airf_tactical_exercises` | Mới | (airf_command_reform_1) | v25: 10 XP/mastery; +10 CP |
| `VIE_airf_gci_radar_training` | Mới | (airf_command_reform_1) | v25: 5 XP/mastery; +0.25% air detection |
| `VIE_airf_regiment_formation` | Mới | (airf_command_reform_1) | v25: 5 XP/mastery; +5 CP; -0.5% air personnel cost modifier |
| `VIE_airf_reserve_bases` | Mới | (airf_command_reform_1) | v25: 5 XP/mastery; +1% home air defence; prepare existing bases |
| `VIE_airf_first_force` | (airf_priority_air_defence OR airf_priority_multirole OR airf_priority_networked) | (airf_tactical_exercises) AND (airf_gci_radar_training) AND (airf_regiment_formation) AND (airf_reserve_bases) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI; `VIE_airf_training_done, VIE_airf_industry_start_ready` |
| `VIE_apm_integration` | (apm_a32 OR apm_a31) AND (apm_a32 OR apm_radar) AND (apm_a31 OR apm_radar) | (apm_a32 OR apm_a31) AND (apm_a32 OR apm_radar) AND (apm_a31 OR apm_radar) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_apm_uav` | (apm_radar) | (apm_radar) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_airf_structure_territorial` | (airf_first_force) | (airf_first_force) | Giữ D4: −50 PP, −0,60 tỷ; thưởng sau 360 ngày; hàng mutex duy nhất; `VIE_airf_structure_selection_ok` |
| `VIE_airf_structure_balanced` | (airf_first_force) | (airf_first_force) | Giữ D4: −50 PP, −0,60 tỷ; thưởng sau 360 ngày; hàng mutex duy nhất; `VIE_airf_structure_selection_ok` |
| `VIE_airf_structure_long_range` | (airf_first_force) | (airf_first_force) | Giữ D4: −50 PP, −0,60 tỷ; thưởng sau 360 ngày; hàng mutex duy nhất; `VIE_airf_structure_selection_ok` |
| `VIE_airf_command_reform_2` | (airf_structure_territorial OR airf_structure_balanced OR airf_structure_long_range) | (airf_structure_territorial OR airf_structure_balanced OR airf_structure_long_range) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI; `VIE_airf_coordination_done` |
| `VIE_airf_medium_force` | (airf_structure_territorial OR airf_structure_balanced OR airf_structure_long_range) | (airf_structure_territorial OR airf_structure_balanced OR airf_structure_long_range) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI; `VIE_airf_structure_done` |
| `VIE_apm_mature` | (apm_integration) | (apm_integration) | Giữ reward; tích hợp bậc 2 AND 3/4 trụ bậc 2; không bắt UAV; `VIE_apm_mature_ok` |
| `VIE_airf_iads` | (airf_command_reform_2) | (airf_command_reform_2) | Giữ modifier/XP/PP/CP/research của v18; nhận bonus nghiên cứu chuyên ngành 25% ×1, chống lặp bonus legacy tương ứng; `VIE_airf_iads_ready` |
| `VIE_airf_multirole` | (airf_medium_force) | (airf_command_reform_2) AND (airf_medium_force) | Giữ modifier/XP/PP/CP/research của v18; nhận bonus nghiên cứu chuyên ngành 25% ×1, chống lặp bonus legacy tương ứng; `VIE_airf_fighter_industry_ready` |
| `VIE_airf_unmanned` | (airf_command_reform_2) | (airf_command_reform_2) | Giữ modifier/XP/PP/CP/research của v18; nhận bonus nghiên cứu chuyên ngành 25% ×1, chống lặp bonus legacy tương ứng; `VIE_airf_uav_start_ready` |
| `VIE_airf_layered_defence` | (airf_iads) | (airf_iads) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_layered_ready` |
| `VIE_airf_ew_antistealth` | (airf_layered_defence) | (airf_iads) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_ew_ready` |
| `VIE_airf_multirole_fleet` | (airf_multirole) | (airf_multirole) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_fighter_industry_ready` |
| `VIE_airf_operating_range` | (airf_command_reform_2) AND (airf_medium_force) | (airf_multirole) | Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI |
| `VIE_airf_sustainment` | (airf_medium_force) | (airf_multirole) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_sustainment_ready` |
| `VIE_airf_isr_uav` | (airf_unmanned) | (airf_unmanned) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_uav_isr_ready` |
| `VIE_airf_datalink` | (airf_command_reform_2) | (airf_unmanned) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_integration_focus_ready` |
| `VIE_airf_strike_uav` | (airf_isr_uav) | (airf_unmanned) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_uav_strike_ready` |
| `VIE_airf_airlift_tanker` | (airf_operating_range) | (airf_operating_range) | Giữ modifier/XP/PP/CP/research của v18 |
| `VIE_airf_iads_command` | (airf_ew_antistealth) | (airf_layered_defence) AND (airf_ew_antistealth) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_coordination_done` |
| `VIE_airf_multirole_wing` | (airf_multirole_fleet) AND (airf_sustainment) | (airf_multirole_fleet) AND (airf_sustainment) AND (airf_operating_range) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_wing_ready` |
| `VIE_airf_teaming` | (airf_datalink) AND (airf_strike_uav) | (airf_isr_uav) AND (airf_strike_uav) AND (airf_datalink) | Giữ modifier/XP/PP/CP/research của v18; `VIE_airf_teaming_ready, custom_trigger_tooltip` |
| `VIE_airf_integrated_force` | (airf_command_reform_2) AND (airf_iads_command OR airf_multirole_wing OR airf_teaming) | (airf_iads_command OR airf_multirole_wing OR airf_teaming) | Giữ +20 XP/mastery, +50 PP, +3% war support; công nghiệp + D4 + 2/3 đích; `VIE_airf_structure_done, VIE_airf_two_capstones, VIE_airf_industry_mature_ready` |
| `VIE_airf_priority_air_defence` | (airf_command_reform_1) | Đã bỏ | Bỏ hệ số giá toàn nhánh; bonus chuyển sang lối vào chuyên ngành tương ứng |
| `VIE_airf_priority_multirole` | (airf_command_reform_1) | Đã bỏ | Bỏ hệ số giá toàn nhánh; bonus chuyển sang lối vào chuyên ngành tương ứng |
| `VIE_airf_priority_networked` | (airf_command_reform_1) | Đã bỏ | Bỏ hệ số giá toàn nhánh; bonus chuyển sang lối vào chuyên ngành tương ứng |

D1–D3 và D4 giữ thưởng/PP/thời lượng. D5 có ba decision đích, dùng chung guard một lần: 60 PP, 1 tỷ, 548 ngày, thưởng 0,5/1 điểm phần trăm. Giá cơ sở và giảm giá lịch sử của chương trình giữ nguyên. Xem [thiết kế](../../../VIE_air_force_documentation.md) và [kiểm định](validation.md).
