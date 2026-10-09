> Lịch sử v17. Hiện hành: [công nghiệp v31](v31/validation.md), [mapping bỏ focus](v31/retired_mapping.md) và [thiết kế](../../../VIE_industry_branch_redesign.md).

# Quan hệ và reward trước/sau

| Focus | Cha trước | Cha sau | Thay đổi reward |
|---|---|---|---|
| `VIE_industrialization_strategy` | (doi_moi_continues) | (doi_moi_continues) | Giữ nguyên |
| `VIE_shipbuilding_vinashin` | (industrialization_strategy) | (industrialization_strategy) | Giữ nguyên |
| `VIE_textile_garment_exports` | (industrialization_strategy) | (industrialization_strategy) | Giữ nguyên |
| `VIE_formosa_steel_complex` | (industrialization_strategy) | (industrialization_strategy) | Giữ nguyên |
| `VIE_hoa_phat_hrc_steel` | (formosa_steel_complex) | (industrialization_strategy) | Giữ nguyên |
| `VIE_supporting_industries` | (samsung_partnership) | (industrialization_strategy) | Giữ nguyên |
| `VIE_samsung_partnership` | (industrialization_strategy) | (industrialization_strategy) | Giữ nguyên |
| `VIE_intel_hcmc` | (supporting_industries) | (industrialization_strategy) | Giữ nguyên |
| `VIE_nq23_industrial_policy` | (industrialization_strategy) | (industrialization_strategy) | Giữ nguyên |
| `VIE_vinashin_restructuring_sbic` | (shipbuilding_vinashin) | (shipbuilding_vinashin) | Giữ nguyên |
| `VIE_cptpp_yarn_forward` | (textile_garment_exports) | (textile_garment_exports) | Giữ nguyên |
| `VIE_hoa_phat_dung_quat_2` | (hoa_phat_hrc_steel) | (hoa_phat_hrc_steel) | Giữ nguyên |
| `VIE_china_plus_one` | (supporting_industries) | (supporting_industries) | Bỏ lần gọi vie_ind.1; thưởng khác giữ nguyên |
| `VIE_semiconductor_ambition` | (intel_hcmc) | (intel_hcmc) | Giữ nguyên |
| `VIE_eco_industrial_parks` | (nq23_industrial_policy) | (nq23_industrial_policy) | Giữ nguyên |
| `VIE_nq29_industrialization_2045` | (eco_industrial_parks) | (nq23_industrial_policy) | Giữ nguyên |
| `VIE_shipbuilding_joint_ventures` | (vinashin_restructuring_sbic) | (vinashin_restructuring_sbic) | Giữ nguyên |
| `VIE_textile_dyeing_parks` | (cptpp_yarn_forward) | (cptpp_yarn_forward) | Giữ nguyên |
| `VIE_domestic_automotive` | (supporting_industries) | (supporting_industries) | Giữ nguyên |
| `VIE_tier1_vendor_localization` | (supporting_industries) | (supporting_industries) | Giữ nguyên |
| `VIE_precision_mechanics_molds` | (supporting_industries) | (supporting_industries) | Giữ nguyên |
| `VIE_chip_design_packaging_priority` | Mới | (semiconductor_ambition) | Focus chính sách mới; xem tài liệu thiết kế |
| `VIE_chip_pilot_fab_priority` | Mới | (semiconductor_ambition) | Focus chính sách mới; xem tài liệu thiết kế |
| `VIE_industrial_productivity_program` | (investment_support_fund) | (nq29_industrialization_2045) | Giữ nguyên |
| `VIE_investment_support_fund` | (nq29_industrialization_2045) | (nq29_industrialization_2045) | Giữ nguyên |
| `VIE_offshore_wind_fabrication` | (shipbuilding_joint_ventures) | (shipbuilding_joint_ventures) | Giữ nguyên |
| `VIE_green_textiles` | (textile_dyeing_parks) | (textile_dyeing_parks) | Giữ nguyên |
| `VIE_integrated_auto_supplier_park` | (domestic_automotive) | (domestic_automotive) | Giữ nguyên |
| `VIE_fdi_fast_track` | Mới | (china_plus_one) | Focus chính sách mới; xem tài liệu thiết kế |
| `VIE_fdi_technology_screening` | Mới | (china_plus_one) | Focus chính sách mới; xem tài liệu thiết kế |
| `VIE_manufacturing_hub` | (intel_hcmc) | (supporting_industries) AND (samsung_partnership OR china_plus_one) | Giữ nguyên |
| `VIE_ev_revolution_batteries` | (integrated_auto_supplier_park) | (integrated_auto_supplier_park) | Giữ nguyên |
| `VIE_apple_supply_chain` | (manufacturing_hub) | (manufacturing_hub) AND (fdi_fast_track OR fdi_technology_screening) | Giữ nguyên |
| `VIE_chip_design` | (semiconductor_ambition) | (chip_design_packaging_priority OR chip_pilot_fab_priority) | Giữ nguyên |
| `VIE_osat_packaging` | (semiconductor_ambition) | (chip_design_packaging_priority OR chip_pilot_fab_priority) | Giữ nguyên |
| `VIE_chip_engineers` | (semiconductor_ambition) | (chip_design_packaging_priority OR chip_pilot_fab_priority) | Giữ nguyên |
| `VIE_global_auto_export` | (ev_revolution_batteries) | (ev_revolution_batteries) | Giữ nguyên |
| `VIE_semiconductor_fab` | (chip_design) AND (osat_packaging) | (chip_design) AND (osat_packaging) AND (chip_engineers) | Bổ sung 2 tỷ khi đã chọn ưu tiên thiết kế/đóng gói |
| `VIE_modern_industrial_nation_2030` | (industrial_productivity_program) AND (semiconductor_fab OR ev_revolution_batteries) | (industrial_productivity_program) | Giữ nguyên |
