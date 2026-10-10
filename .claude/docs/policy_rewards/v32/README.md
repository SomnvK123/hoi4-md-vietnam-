# Effect chính sách trực tiếp — v32 (10/10/2026)

24 focus công nghiệp và 22 focus hạ tầng nhận reward trực tiếp. 35 idea mới gồm 19 công nghiệp và 16 hạ tầng. Mỗi nhóm chỉ tồn tại một bậc; bàn giao thay bậc chính sách bằng năng lực hoàn chỉnh. Game mới bắt buộc.

## Manifest modifier và điều kiện

Giá trị là đóng góp của nhóm, không cộng thêm lên bậc cũ. Cảng/logistics chỉ tồn tại riêng trước đa phương thức. Tỷ lệ là modifier MD, không phải GDP.

| Nhánh / nhóm | Bậc | Idea | Điều kiện | Modifier |
|---|---:|---|---|---|
| ind/support | 1 | `VIE_ind_policy_support_1_idea` | `has_country_flag = VIE_ind_policy_supporting_industries_adopted` | country_productivity_growth_modifier=0.004, industrial_capacity_factory=0.005, corporate_tax_income_multiplier_modifier=0.005 |
| ind/support | 2 | `VIE_ind_supporting_capacity_idea` | `has_country_flag = VIE_ind_support_done` | country_productivity_growth_modifier=0.016, industrial_capacity_factory=0.02, corporate_tax_income_multiplier_modifier=0.02 |
| ind/steel | 1 | `VIE_ind_policy_steel_1_idea` | `has_country_flag = VIE_ind_policy_national_steel_program_adopted` | production_speed_industrial_complex_factor=0.0075, production_speed_infrastructure_factor=0.005, production_speed_arms_factory_factor=0.005 |
| ind/steel | 2 | `VIE_ind_policy_steel_2_idea` | `has_country_flag = VIE_ind_policy_hoa_phat_hrc_steel_adopted` | production_speed_industrial_complex_factor=0.015, production_speed_infrastructure_factor=0.01, production_speed_arms_factory_factor=0.01 |
| ind/steel | 3 | `VIE_hrc_steel_self_reliance` | `has_country_flag = VIE_ind_steel_hrc_done` | production_speed_industrial_complex_factor=0.03, production_speed_infrastructure_factor=0.02, production_speed_arms_factory_factor=0.02 |
| ind/ship | 1 | `VIE_ind_policy_ship_1_idea` | `has_country_flag = VIE_ind_policy_vinashin_restructuring_sbic_adopted` | production_speed_dockyard_factor=0.02 |
| ind/ship | 2 | `VIE_ind_policy_ship_2_idea` | `has_country_flag = VIE_ind_policy_shipbuilding_joint_ventures_adopted` | production_speed_dockyard_factor=0.04 |
| ind/ship | 3 | `VIE_ind_policy_ship_3_idea` | `VIE_ind_ship_ready = yes` | production_speed_dockyard_factor=0.05 |
| ind/textile | 1 | `VIE_ind_policy_textile_1_idea` | `has_country_flag = VIE_ind_policy_textile_garment_exports_adopted` | consumer_goods_factor=-0.00125, trade_opinion_factor=0.0025 |
| ind/textile | 2 | `VIE_ind_policy_textile_2_idea` | `has_country_flag = VIE_ind_policy_green_textiles_adopted` | consumer_goods_factor=-0.0025, trade_opinion_factor=0.005 |
| ind/textile | 3 | `VIE_textile_supply_chain_idea` | `has_country_flag = VIE_ind_textile_green_done` | consumer_goods_factor=-0.005, trade_opinion_factor=0.01 |
| ind/ev | 1 | `VIE_ind_policy_ev_1_idea` | `has_country_flag = VIE_ind_policy_domestic_automotive_adopted` | country_productivity_growth_modifier=0.004, industrial_capacity_factory=0.005, fuel_cost=-0.0075 |
| ind/ev | 2 | `VIE_ind_policy_ev_2_idea` | `has_country_flag = VIE_ind_policy_ev_revolution_batteries_adopted` | country_productivity_growth_modifier=0.008, industrial_capacity_factory=0.01, fuel_cost=-0.015 |
| ind/ev | 3 | `VIE_ev_mobility_idea` | `has_country_flag = VIE_ind_auto_ev_done` | country_productivity_growth_modifier=0.016, industrial_capacity_factory=0.02, fuel_cost=-0.03 |
| ind/auto_export | 1 | `VIE_ind_policy_auto_export_1_idea` | `has_country_flag = VIE_ind_policy_global_auto_export_adopted` | country_productivity_growth_modifier=0.002, corporate_tax_income_multiplier_modifier=0.005, stability_factor=0.0025, foreign_influence_defense_modifier=0.0125 |
| ind/auto_export | 2 | `VIE_global_brand_recognition` | `has_country_flag = VIE_ind_auto_export_done` | country_productivity_growth_modifier=0.008, corporate_tax_income_multiplier_modifier=0.02, stability_factor=0.01, foreign_influence_defense_modifier=0.05 |
| ind/electronics | 1 | `VIE_ind_policy_electronics_1_idea` | `has_country_flag = VIE_ind_policy_electronics_export_program_adopted` | country_productivity_growth_modifier=0.004, corporate_tax_income_multiplier_modifier=0.005 |
| ind/electronics | 2 | `VIE_ind_policy_electronics_2_idea` | `has_country_flag = VIE_ind_policy_apple_supply_chain_adopted` | country_productivity_growth_modifier=0.008, corporate_tax_income_multiplier_modifier=0.01 |
| ind/electronics | 3 | `VIE_manufacturing_hub_idea` | `has_country_flag = VIE_ind_policy_manufacturing_hub_adopted` | country_productivity_growth_modifier=0.016, corporate_tax_income_multiplier_modifier=0.02 |
| ind/chip | 1 | `VIE_ind_policy_chip_1_idea` | `check_variable = { VIE_ind_policy_chip_rank > 0 }` | country_productivity_growth_modifier=0.001, research_speed_factor=0.00125 |
| ind/chip | 2 | `VIE_ind_policy_chip_2_idea` | `check_variable = { VIE_ind_policy_chip_rank > 1 }` | country_productivity_growth_modifier=0.002, research_speed_factor=0.0025 |
| ind/chip | 3 | `VIE_ind_policy_chip_3_idea` | `check_variable = { VIE_ind_policy_chip_rank > 2 }` | country_productivity_growth_modifier=0.003, research_speed_factor=0.00375 |
| ind/chip | 4 | `VIE_ind_policy_chip_4_idea` | `check_variable = { VIE_ind_policy_chip_rank > 3 }` | country_productivity_growth_modifier=0.004, research_speed_factor=0.005 |
| ind/chip | 5 | `VIE_semiconductor_idea` | `VIE_ind_chip_ready = yes` | country_productivity_growth_modifier=0.008, research_speed_factor=0.01 |
| ind/chip | 6 | `VIE_ind_policy_chip_6_idea` | `has_country_flag = VIE_ind_policy_semiconductor_fab_adopted` | country_productivity_growth_modifier=0.01, research_speed_factor=0.0125 |
| ind/chip | 7 | `VIE_chip_sector_idea` | `has_country_flag = VIE_ind_chip_fab_done` | country_productivity_growth_modifier=0.012, research_speed_factor=0.015 |
| ind/productivity | 1 | `VIE_ind_policy_productivity_1_idea` | `has_country_flag = VIE_ind_policy_industrial_productivity_program_adopted` | country_productivity_growth_modifier=0.002, production_speed_industrial_complex_factor=0.01 |
| ind/productivity | 2 | `VIE_industrialization_2045_idea` | `has_country_flag = VIE_ind_productivity_done` | country_productivity_growth_modifier=0.008, production_speed_industrial_complex_factor=0.04 |
| ind/productivity | 3 | `VIE_modern_industrial_nation_idea` | `has_country_flag = VIE_ind_policy_modern_industrial_nation_2030_adopted` | country_productivity_growth_modifier=0.012, production_speed_industrial_complex_factor=0.06, industrial_capacity_factory=0.02 |
| infra/road | 1 | `VIE_infra_policy_road_1_idea` | `has_country_flag = VIE_infra_policy_transport_strategy_2004_adopted` | country_productivity_growth_modifier=0.004, production_speed_infrastructure_factor=0.025 |
| infra/road | 2 | `VIE_infra_policy_road_2_idea` | `has_country_flag = VIE_infra_policy_north_south_expressway_adopted` | country_productivity_growth_modifier=0.008, production_speed_infrastructure_factor=0.05 |
| infra/road | 3 | `VIE_expressway_idea` | `check_variable = { VIE_expressway_km > 999 }` | production_speed_infrastructure_factor=0.1, country_productivity_growth_modifier=0.016 |
| infra/road | 4 | `VIE_infra_policy_road_4_idea` | `has_country_flag = VIE_infra_policy_expressway_regional_links_adopted` | country_productivity_growth_modifier=0.02, production_speed_infrastructure_factor=0.125 |
| infra/road | 5 | `VIE_infra_policy_road_5_idea` | `has_country_flag = VIE_infra_policy_expressway_5000km_2030_adopted` | country_productivity_growth_modifier=0.022, production_speed_infrastructure_factor=0.14 |
| infra/road | 6 | `VIE_expressway_idea_2` | `check_variable = { VIE_expressway_km > 2999 }` | production_speed_infrastructure_factor=0.15, country_productivity_growth_modifier=0.024 |
| infra/road | 7 | `VIE_expressway_idea_3` | `check_variable = { VIE_expressway_km > 4999 }` | production_speed_infrastructure_factor=0.2, country_productivity_growth_modifier=0.032 |
| infra/rail | 1 | `VIE_infra_policy_rail_1_idea` | `check_variable = { VIE_infra_policy_rail_rank > 0 }` | country_productivity_growth_modifier=0.002, research_speed_factor=0.0025 |
| infra/rail | 2 | `VIE_infra_policy_rail_2_idea` | `check_variable = { VIE_infra_policy_rail_rank > 1 }` | country_productivity_growth_modifier=0.003, research_speed_factor=0.00375 |
| infra/rail | 3 | `VIE_infra_policy_rail_3_idea` | `check_variable = { VIE_infra_policy_rail_rank > 2 }` | country_productivity_growth_modifier=0.004, research_speed_factor=0.005 |
| infra/rail | 4 | `VIE_infra_policy_rail_4_idea` | `check_variable = { VIE_infra_policy_rail_rank > 3 }` | country_productivity_growth_modifier=0.005, research_speed_factor=0.00625 |
| infra/rail | 5 | `VIE_infra_policy_rail_5_idea` | `check_variable = { VIE_infra_policy_rail_rank > 4 }` | country_productivity_growth_modifier=0.006, research_speed_factor=0.0075 |
| infra/rail | 6 | `VIE_modern_rail_idea` | `has_country_flag = VIE_infra_policy_modern_rail_network_adopted` | country_productivity_growth_modifier=0.008, research_speed_factor=0.01 |
| infra/ports | 1 | `VIE_infra_policy_ports_1_idea` | `has_country_flag = VIE_infra_policy_national_deepwater_ports_adopted` | country_productivity_growth_modifier=0.004, trade_opinion_factor=0.00525 |
| infra/ports | 2 | `VIE_ports_idea` | `has_country_flag = VIE_infra_ports_done` | country_productivity_growth_modifier=0.012, trade_opinion_factor=0.01575 |
| infra/logistics | 1 | `VIE_infra_policy_logistics_1_idea` | `has_country_flag = VIE_infra_policy_logistics_strategy_adopted` | trade_opinion_factor=0.00525, country_productivity_growth_modifier=0.002 |
| infra/logistics | 2 | `VIE_logistics_idea` | `has_country_flag = VIE_infra_logistics_done` | trade_opinion_factor=0.01575, country_productivity_growth_modifier=0.006 |
| infra/multimodal | 1 | `VIE_infra_policy_multimodal_1_idea` | `has_country_flag = VIE_infra_policy_multimodal_transport_adopted` | country_productivity_growth_modifier=0.021, trade_opinion_factor=0.03675 |
| infra/multimodal | 2 | `VIE_multimodal_idea` | `has_country_flag = VIE_infra_multimodal_done` | country_productivity_growth_modifier=0.024, trade_opinion_factor=0.042 |
| infra/air | 1 | `VIE_infra_policy_air_1_idea` | `has_country_flag = VIE_infra_policy_airport_master_plan_adopted` | country_productivity_growth_modifier=0.004, trade_opinion_factor=0.00525 |
| infra/air | 2 | `VIE_infra_policy_air_2_idea` | `has_country_flag = VIE_infra_policy_airport_network_2030_adopted` | country_productivity_growth_modifier=0.008, trade_opinion_factor=0.0105 |
| infra/air | 3 | `VIE_infra_policy_air_3_idea` | `has_country_flag = VIE_infra_air_network_done` | country_productivity_growth_modifier=0.012, trade_opinion_factor=0.01575 |
| infra/air | 4 | `VIE_infra_policy_air_4_idea` | `has_country_flag = VIE_infra_policy_long_thanh_airport_adopted` | country_productivity_growth_modifier=0.014, trade_opinion_factor=0.018375 |
| infra/air | 5 | `VIE_airport_network_idea` | `has_country_flag = VIE_infra_long_thanh_done` | country_productivity_growth_modifier=0.016, trade_opinion_factor=0.021 |

## Hợp đồng effect

- Guard nhận một lần cho 46 focus; mutex chặn phương án đối lập. Đặt cờ chính sách trước refresh, không phụ thuộc thời điểm engine cập nhật completed focus.
- Refresh chỉ gỡ idea thuộc nhóm và có has_idea guard. Chỉ thêm bậc chưa có, giữ bậc cao nhất. Không đụng debt dùng chung và không chạy refresh mỗi tháng.
- Finish giữ nguyên tiền/công trình/điểm/research bonus/event/cleanup; thay phần chọn idea bằng helper chung. Refund giữ chính sách nhưng không nâng năng lực bàn giao.
- Giữ toàn bộ ID/cost/icon/layout/gate/AI, 17 chương trình công nghiệp và 26 định nghĩa decision hạ tầng. Không PP đại trà, treasury miễn phí hay research bonus mới.
- Trần công nghiệp: growth .080 / research .015 / output .060 / corporate tax .060 / IC speed .090; dockyard speed bổ sung .05. Hạ tầng: growth .088 / trade .073 / road infrastructure speed .20.
- Tooltip Nhận ngay / Mở đầu tư / Sau bàn giao ghi modifier, tiền/thời gian và kết quả từng đợt. Picture tái sử dụng, không artwork mới.

## Kiểm định

`python tools/audit/policy_rewards.py` đọc script thật, kiểm baseline mới và hợp đồng đầu tư, 46 reward, bậc/guard/trần, 64 tổ hợp và 20 bộ ba công nghiệp, 16 tổ hợp hạ tầng, 8/12 đường vốn và các lifecycle/event cũ. Baseline v30/v31 giữ nguyên; v32 chụp trạng thái workspace ngay trước lần bổ sung này.

`python tools/audit/policy_assets.py <MD directory>` xác minh toàn bộ 35 consumer idea, texture/sprite và modifier có bằng chứng MD, xuất ảnh native không sửa nguồn.

[Nghiệm thu và checklist runtime](validation.md) · [Manifest](structure.json) · [Baseline bất biến](baseline.json) · [Picture native](reused_ideas_native.png)
