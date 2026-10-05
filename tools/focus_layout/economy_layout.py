"""Hand-designed layout of the ECONOMY branch (155 focuses): one block per sub-branch, parents above children,
focuses of a group 3 columns apart, sub-branches 5-6 columns apart, every block starts on its own tier (row).
Design notes (see VIE_focus_coding_standards.md 7.3):
  tier 0  the two roots of the branch: enterprise_law (market) and doi_moi_continues (state / industry)
  tier 1  sub-branch heads            tier 2.. each sub-branch grows downwards, chains stay vertical (logic unchanged)
Only POSITIONS change; prerequisites, available, rewards are untouched.
Writes <plan.json> = {focus_id: [x, y]} for apply_positions.py.   Usage: python tools/focus_layout/economy_layout.py <plan.json>
"""
import json, sys

V = 'VIE_'
P = {}


def put(name, x, y):
    assert V + name not in P, name
    P[V + name] = [x, y]


# ---- A. Market and trade (root enterprise_law) ------------------------------------------------------------
# agriculture
put('rice_export_power', 31, 1)
put('new_rural_development', 28, 2); put('land_law_reform', 34, 2)
put('high_tech_agriculture', 28, 3); put('mekong_climate_adaptation', 34, 3)
# private sector (investment law -> household business -> private champions -> engine)
put('investment_law_2005', 41, 1)
put('household_business', 41, 2); put('private_champions', 41, 3); put('private_sector_engine', 41, 4)
# capital market
put('hose_exchange', 50, 1); put('corporate_bond_reform', 50, 2); put('market_upgrade_criteria', 50, 3)
# banking and state capital (root state_bank_modernization)
put('state_bank_modernization', 65, 1)
put('cashless_payments', 56, 2); put('gold_monopoly_2012', 59, 2); put('gold_free_market', 62, 2)
put('state_conglomerates', 66, 2); put('fight_inflation', 70, 2); put('restructure_banking', 75, 2)
put('gold_monopoly_lifted', 59, 3); put('scic', 66, 3); put('deposit_insurance', 70, 3); put('vamc', 75, 3)
put('soe_rapid_divestment', 63, 4); put('soe_gradual_restructuring', 67, 4)
put('cross_ownership_crackdown', 72, 4); put('zero_dong_acquisition', 76, 4); put('bank_bankruptcy', 79, 4)
put('soe_governance', 65, 5); put('international_financial_centre', 72, 5); put('compulsory_transfer_2024', 76, 5)
put('investment_grade', 72, 6)
# trade and WTO (equitization from enterprise_law + bilateral agreement from doi_moi meet in fdi_attraction)
put('equitization_soes', 86, 1); put('bilateral_trade_agreement_usa', 92, 1)
put('fdi_attraction', 89, 2); put('wto_negotiations', 89, 3)
put('wto_reforms', 86, 4); put('cptpp_member', 89, 4); put('evfta', 92, 4)
put('export_powerhouse', 86, 5)
# special economic zones
put('sez_three_zones', 100, 1)
put('sez_postpone', 98, 2); put('sez_pass_99', 102, 2)
put('island_special_zones', 98, 3); put('sez_strategic_investors', 102, 3)
put('enterprise_law', 58, 0)

# ---- B. Infrastructure (doi_moi -> infrastructure_development) -------------------------------------------------
put('infrastructure_development', 128, 1)
put('cai_mep_port', 108, 2); put('lach_huyen_port', 112, 2); put('logistics_strategy', 110, 3)
put('transport_strategy_2004', 121, 2)
put('hai_van_tunnel', 117, 3); put('hcmc_trung_luong_expressway', 121, 3); put('can_tho_bridge', 125, 3)
put('northern_expressways', 118, 4); put('north_south_expressway', 124, 4)
put('expressway_regional_links', 118, 5); put('expressway_bot', 122, 5); put('expressway_public_investment', 126, 5)
put('north_south_expressway_phase2', 124, 6)
put('ring_roads_hanoi_hcmc', 121, 7); put('expressway_3000km', 127, 7); put('expressway_5000km_2030', 127, 8)
put('infrastructure_breakthrough_nq13', 131, 2)
put('hsr_2010_reject', 135, 2); put('hsr_2010_approve', 139, 2); put('north_south_hsr', 137, 3)
put('hsr_partner_japan', 133, 4); put('hsr_partner_eu', 137, 4); put('hsr_partner_china', 141, 4)
put('hsr_groundbreaking', 137, 5)
put('reunification_line_upgrade', 147, 2)
put('lao_cai_haiphong_rail', 144, 3); put('hcmc_metro', 147, 3); put('urban_rail_hanoi', 150, 3)
put('domestic_rail_industry', 144, 4); put('urban_rail_special_mechanism_nq188', 148, 4); put('metro_network_2035', 148, 5)
# aviation (root airport_master_plan)
put('airport_master_plan', 170, 1)
put('aviation_market_opening', 160, 2); put('noi_bai_t2', 165, 2); put('long_thanh_approval', 170, 2)
put('tan_son_nhat_t3', 175, 2); put('dual_use_airports', 180, 2)
put('socialized_airports', 157, 3); put('acv_monopoly', 163, 3); put('long_thanh_airport', 170, 3)
put('van_don_airport', 156, 4); put('airport_network_2030', 160, 4)
put('synchronized_infrastructure_2030', 148, 9)

# ---- C. Resources and energy ------------------------------------------------------------------------------------
put('vinacomin_founding', 196, 1)
put('bauxite_suspend', 188, 2); put('bauxite_tay_nguyen', 192, 2); put('than_quang_ninh', 197, 2)
put('nui_phao_tungsten', 201, 2); put('thach_khe_mine_start', 205, 2); put('rare_earths', 190, 3)
put('petrovietnam_expansion', 226, 1)
put('petrolimex_downstream_network', 216, 2)
put('strategic_petroleum_reserve', 214, 3); put('petrolimex_eneos_partnership', 219, 3); put('petrolimex_green_ev_hubs', 214, 4)
put('dung_quat_refinery', 225, 2); put('nghi_son_refinery', 225, 3)
put('son_la_dam', 236, 2)
put('500kv_grid', 232, 3); put('dppa_market_reform', 232, 4)
put('coal_power', 240, 3)
put('solar_boom', 237, 4); put('solar_auction', 241, 4); put('ninh_thuan_nuclear', 245, 4)
put('power_plan_8', 239, 5); put('shelve_nuclear', 243, 5); put('build_nuclear_plant', 247, 5)
put('jetp_partnership', 236, 6); put('offshore_wind', 240, 6); put('revive_nuclear', 243, 6)
put('net_zero_2050', 236, 7); put('energy_security_2045', 240, 7)

# ---- D. Industrialisation ---------------------------------------------------------------------------------------
put('industrialization_strategy', 278, 1)
put('shipbuilding_vinashin', 256, 2); put('vinashin_restructuring_sbic', 256, 3)
put('shipbuilding_joint_ventures', 256, 4); put('offshore_wind_fabrication', 256, 5)
put('textile_garment_exports', 262, 2); put('cptpp_yarn_forward', 262, 3)
put('textile_dyeing_parks', 262, 4); put('green_textiles', 262, 5)
put('formosa_steel_complex', 268, 2); put('hoa_phat_hrc_steel', 268, 3); put('hoa_phat_dung_quat_2', 268, 4)
put('samsung_partnership', 282, 2); put('supporting_industries', 282, 3)
put('intel_hcmc', 275, 4); put('china_plus_one', 279, 4); put('tier1_vendor_localization', 283, 4)
put('precision_mechanics_molds', 287, 4); put('domestic_automotive', 291, 4)
put('semiconductor_ambition', 272, 5); put('manufacturing_hub', 279, 5)
put('chip_design', 269, 6); put('osat_packaging', 272, 6); put('chip_engineers', 275, 6); put('apple_supply_chain', 279, 6)
put('semiconductor_fab', 271, 7)
put('integrated_auto_supplier_park', 291, 5); put('ev_revolution_batteries', 291, 6); put('global_auto_export', 291, 7)
put('nq23_industrial_policy', 300, 2); put('eco_industrial_parks', 300, 3); put('nq29_industrialization_2045', 300, 4)
put('investment_support_fund', 300, 5); put('industrial_productivity_program', 300, 6)
put('modern_industrial_nation_2030', 295, 8)
put('doi_moi_continues', 185, 0)

if __name__ == '__main__':
    out = sys.argv[1]
    json.dump(P, open(out, 'w'))
    xs = [v[0] for v in P.values()]; ys = [v[1] for v in P.values()]
    print(len(P), 'focuses; x', min(xs), max(xs), 'y', min(ys), max(ys))
