import sys
from pathlib import Path
sys.path.insert(0, 'tools/audit')
from industry import ROOT, focus_map, groups, positions, value, values

FOCUS_FILE = ROOT / 'common/national_focus/VIE_md_focus.txt'
raw_text = FOCUS_FILE.read_text(encoding='utf-8')
allf = focus_map(raw_text)
pos = dict(positions(allf))

pos_overrides = {}
prereq_overrides = {}

# ==========================================
# 1. NAVY
# ==========================================
prereq_overrides['VIE_naval_defence_2030'] = [['VIE_naval_systems_integration']]

# ==========================================
# 2. POLITICS
# ==========================================
pos_overrides.update({
    'VIE_party_members_private_business': (6, 4),
    'VIE_asset_declaration': (8, 4),
    'VIE_party_inspection': (8, 5),
    'VIE_party_discipline': (8, 6),
    'VIE_cadre_accountability': (6, 7),
    'VIE_asset_recovery': (8, 7),
    'VIE_clean_cadres': (8, 8),
    'VIE_concentration_of_power': (12, 9),
    'VIE_institutional_opening': (16, 9),
    'VIE_era_of_rising': (14, 10),
    'VIE_party_centennial_2030': (14, 11),
})
prereq_overrides['VIE_party_discipline'] = [['VIE_party_inspection']]

# ==========================================
# 3. ECONOMY & BANKING
# ==========================================
prereq_overrides['VIE_bilateral_trade_agreement_usa'] = [['VIE_enterprise_law']]
prereq_overrides['VIE_rice_export_power'] = []
pos_overrides['VIE_household_business'] = (40, 5)

pos_overrides.update({
    'VIE_corporate_bond_reform': (44, 3),
    'VIE_market_upgrade_criteria': (44, 4),
    'VIE_international_financial_centre': (44, 5),
    'VIE_investment_grade': (44, 6),
    'VIE_cashless_payments': (50, 2),
    'VIE_gold_monopoly_2012': (52, 4),
    'VIE_gold_free_market': (54, 4),
    'VIE_gold_monopoly_lifted': (52, 5),
    'VIE_cross_ownership_crackdown': (56, 4),
    'VIE_zero_dong_acquisition': (58, 4),
    'VIE_bank_bankruptcy': (60, 4),
    'VIE_compulsory_transfer_2024': (58, 5),
    'VIE_new_rural_development': (62, 4),
    'VIE_land_law_reform': (64, 4),
    'VIE_high_tech_agriculture': (62, 5),
    'VIE_mekong_climate_adaptation': (64, 5),
})
prereq_overrides['VIE_corporate_bond_reform'] = [['VIE_hose_exchange']]
prereq_overrides['VIE_market_upgrade_criteria'] = [['VIE_corporate_bond_reform']]
prereq_overrides['VIE_international_financial_centre'] = [['VIE_market_upgrade_criteria']]
prereq_overrides['VIE_gold_monopoly_2012'] = [['VIE_deposit_insurance']]
prereq_overrides['VIE_gold_free_market'] = [['VIE_deposit_insurance']]

# ==========================================
# 4. INFRASTRUCTURE & TRANSPORT
# ==========================================
prereq_overrides['VIE_dual_use_airports'] = [['VIE_tan_son_nhat_t3']]
prereq_overrides['VIE_expressway_3000km'] = [['VIE_north_south_expressway_phase2']]
prereq_overrides['VIE_synchronized_infrastructure_2030'] = [
    ['VIE_expressway_5000km_2030'],
    ['VIE_airport_network_2030']
]
pos_overrides['VIE_expressway_5000km_2030'] = (78, 9)

# ==========================================
# 5. ENERGY & MINING
# ==========================================
# Roots at Y=1
pos_overrides.update({
    'VIE_vinacomin_founding': (104, 1),
    'VIE_petrovietnam_expansion': (110, 1),
    'VIE_bauxite_tay_nguyen': (104, 2),
    'VIE_bauxite_suspend': (100, 2),
    'VIE_than_quang_ninh': (108, 2),
    'VIE_nui_phao_tungsten': (112, 2),
    'VIE_son_la_dam': (106, 2),
    'VIE_dung_quat_refinery': (114, 2),
    'VIE_petrolimex_downstream_network': (110, 2),
    'VIE_rare_earths': (102, 3),
    'VIE_thach_khe_mine_start': (108, 3),
    'VIE_500kv_grid': (106, 3),
    'VIE_nghi_son_refinery': (114, 3),
    'VIE_coal_power': (116, 3),
    'VIE_petrolimex_eneos_partnership': (110, 3),
    'VIE_strategic_petroleum_reserve': (110, 4),
    'VIE_dppa_market_reform': (106, 4),
    'VIE_solar_boom': (116, 4),
    'VIE_solar_auction': (118, 4),
    'VIE_ninh_thuan_nuclear': (120, 4),
    'VIE_petrolimex_green_ev_hubs': (110, 5),
    'VIE_shelve_nuclear': (120, 5),
    'VIE_build_nuclear_plant': (122, 5),
    'VIE_power_plan_8': (118, 5),
    'VIE_revive_nuclear': (120, 6),
    'VIE_jetp_partnership': (118, 6),
    'VIE_offshore_wind': (122, 6),
    'VIE_net_zero_2050': (118, 7),
    'VIE_energy_security_2045': (122, 7),
})
prereq_overrides['VIE_thach_khe_mine_start'] = [['VIE_than_quang_ninh']]
prereq_overrides['VIE_petrolimex_eneos_partnership'] = [['VIE_petrolimex_downstream_network']]
prereq_overrides['VIE_strategic_petroleum_reserve'] = [['VIE_petrolimex_eneos_partnership']]
prereq_overrides['VIE_petrolimex_green_ev_hubs'] = [['VIE_strategic_petroleum_reserve']]

# ==========================================
# 6. INDUSTRY & MANUFACTURING
# ==========================================
pos_overrides.update({
    # Col 128: Automotive
    'VIE_domestic_automotive': (128, 3),
    'VIE_integrated_auto_supplier_park': (128, 4),
    'VIE_ev_revolution_batteries': (128, 5),
    'VIE_global_auto_export': (128, 6),
    # Col 130: Heavy Steel & Metallurgy
    'VIE_tier1_vendor_localization': (130, 4),
    'VIE_fdi_fast_track': (130, 5),
    # Col 132: Supporting Industries & High-tech
    'VIE_precision_mechanics_molds': (132, 3),
    'VIE_fdi_technology_screening': (132, 4),
    'VIE_apple_supply_chain': (132, 5),
    'VIE_modern_industrial_nation_2030': (132, 6),
    # Col 134: Samsung & Manufacturing Hub
    'VIE_china_plus_one': (134, 3),
    'VIE_manufacturing_hub': (134, 4),
    # Col 136..140: Semiconductor
    'VIE_chip_design_packaging_priority': (136, 4),
    'VIE_chip_pilot_fab_priority': (138, 4),
    'VIE_chip_design': (136, 5),
    'VIE_osat_packaging': (138, 5),
    'VIE_chip_engineers': (140, 5),
    'VIE_semiconductor_fab': (138, 6),
    # Col 140..142: National Strategy
    'VIE_eco_industrial_parks': (142, 3),
    'VIE_industrial_productivity_program': (140, 4),
    'VIE_investment_support_fund': (142, 4),
})
prereq_overrides['VIE_domestic_automotive'] = [['VIE_formosa_steel_complex']]
prereq_overrides['VIE_tier1_vendor_localization'] = [['VIE_hoa_phat_dung_quat_2']]
prereq_overrides['VIE_fdi_fast_track'] = [['VIE_tier1_vendor_localization']]
prereq_overrides['VIE_precision_mechanics_molds'] = [['VIE_supporting_industries']]
prereq_overrides['VIE_fdi_technology_screening'] = [['VIE_precision_mechanics_molds']]
prereq_overrides['VIE_apple_supply_chain'] = [['VIE_fdi_technology_screening']]
prereq_overrides['VIE_china_plus_one'] = [['VIE_samsung_partnership']]
prereq_overrides['VIE_manufacturing_hub'] = [['VIE_china_plus_one']]
prereq_overrides['VIE_modern_industrial_nation_2030'] = [['VIE_apple_supply_chain']]
prereq_overrides['VIE_chip_design_packaging_priority'] = [['VIE_semiconductor_ambition']]
prereq_overrides['VIE_chip_pilot_fab_priority'] = [['VIE_semiconductor_ambition']]

# ==========================================
# 7. SCIENCE & DIGITAL
# ==========================================
prereq_overrides['VIE_nuclear_research'] = [['VIE_research_universities']]
prereq_overrides['VIE_science_breakthrough'] = [['VIE_nuclear_research']]
prereq_overrides['VIE_developed_nation_2045'] = [['VIE_high_income_2045']]

# ==========================================
# TEST
# ==========================================
test_fmap = {}
for fid, node in allf.items():
    new_node = list(node)
    if fid in prereq_overrides:
        new_node = [(k, op, v) for k, op, v in new_node if k != 'prerequisite']
        for grp in prereq_overrides[fid]:
            for p in grp:
                new_node.append(('prerequisite', '=', [('focus', '=', p)]))
    test_fmap[fid] = new_node

test_pos = dict(pos)
test_pos.update(pos_overrides)

def detect_collisions(fmap, pos_dict):
    collisions = []
    for fid, node in fmap.items():
        cx, cy = pos_dict[fid]
        for grp in groups(node):
            for p in grp:
                if p in pos_dict:
                    px, py = pos_dict[p]
                    mid_y = (py + cy) / 2.0
                    for oid, (ox, oy) in pos_dict.items():
                        if oid in (fid, p): continue
                        if px == cx:
                            if ox == px and py < oy < cy:
                                collisions.append((p, fid, oid, f'Vertical line on x={px} cuts {oid} at ({ox}, {oy})'))
                        else:
                            if ox == px and py < oy < mid_y:
                                collisions.append((p, fid, oid, f'Parent drop on x={px} cuts {oid} at ({ox}, {oy})'))
                            elif ox == px and abs(oy - mid_y) < 0.2:
                                collisions.append((p, fid, oid, f'Parent corner at y={mid_y} hits {oid} at ({ox}, {oy})'))
                            if abs(oy - mid_y) < 0.2 and (min(px, cx) < ox < max(px, cx)):
                                collisions.append((p, fid, oid, f'Horizontal seg at y={mid_y} cuts {oid} at ({ox}, {oy})'))
                            if ox == cx and mid_y < oy < cy:
                                collisions.append((p, fid, oid, f'Child lead-in on x={cx} cuts {oid} at ({ox}, {oy})'))
                            elif ox == cx and abs(oy - mid_y) < 0.2:
                                collisions.append((p, fid, oid, f'Child corner at y={mid_y} hits {oid} at ({ox}, {oy})'))
    return collisions

cols = detect_collisions(test_fmap, test_pos)
print(f"Remaining collisions: {len(cols)}")
for p, c, o, desc in cols:
    print(f"  [{p} ({test_pos[p]}) -> {c} ({test_pos[c]})]: {desc}")
