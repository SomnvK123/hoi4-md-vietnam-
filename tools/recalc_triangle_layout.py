"""
tools/recalc_triangle_layout.py
Comprehensive script to recalculate and apply the Millennium Dawn
symmetrical Triangle / Pyramid / Diamond layout for all 487 focuses
in VIE_md_focus.txt.
"""

import os
import re
import sys
from collections import Counter
try:
    from tools.layout_applier import apply_layout_to_text
except ImportError:
    from layout_applier import apply_layout_to_text

MOD_ROOT = r"d:\HOI4Mods\md_vietnam"
FOCUS_FILE = os.path.join(MOD_ROOT, r"common\national_focus\VIE_md_focus.txt")

def parse_focus_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    focuses = []
    for m in re.finditer(r'\bfocus\s*=\s*\{', content):
        start_idx = m.start()
        brace_count = 0
        end_idx = start_idx
        for i in range(m.end() - 1, len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx = i + 1
                    break
        block_text = content[start_idx:end_idx]
        
        id_m = re.search(r'id\s*=\s*(\S+)', block_text)
        if not id_m: continue
        fid = id_m.group(1)
        x_m = re.search(r'\bx\s*=\s*(-?\d+)', block_text)
        y_m = re.search(r'\by\s*=\s*(-?\d+)', block_text)
        rel_m = re.search(r'\brelative_position_id\s*=\s*(\S+)', block_text)
        prereqs = re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', block_text)
        p_list = []
        for p in prereqs:
            p_list.extend(re.findall(r'focus\s*=\s*(\S+)', p))
        mut = re.findall(r'mutually_exclusive\s*=\s*\{([^}]+)\}', block_text)
        m_list = []
        for m in mut:
            m_list.extend(re.findall(r'focus\s*=\s*(\S+)', m))
        
        focuses.append({
            'id': fid,
            'start': start_idx,
            'end': end_idx,
            'old_x': int(x_m.group(1)) if x_m else 0,
            'old_y': int(y_m.group(1)) if y_m else 0,
            'old_rel': rel_m.group(1) if rel_m else None,
            'prereqs': p_list,
            'mut': m_list,
            'text': block_text
        })
    return content, focuses

def build_master_layout():
    """
    Defines the global placement of each module and local triangle coordinates for each focus.
    Returns: dict mapping fid -> {'rel': anchor_fid_or_None, 'x': local_x, 'y': local_y}
    """
    layout = {}

    # ROOT FOCUS
    layout['VIE_doi_moi_continues'] = {'rel': None, 'x': 80, 'y': 0}

    # -------------------------------------------------------------------------
    # MODULE 1: POLITICAL DIAMOND (26 focuses)
    # Anchor: VIE_anti_corruption_steering at abs (14, 1) relative to ROOT (dx = -66, dy = 1)
    # -------------------------------------------------------------------------
    layout['VIE_anti_corruption_steering'] = {'rel': 'VIE_doi_moi_continues', 'x': -66, 'y': 1}
    
    pol_rel = {
        # Left Wing (Grassroots)
        'VIE_grassroots_democracy': (-3, 1),
        'VIE_ethnic_policy': (-4, 2),
        'VIE_national_assembly_role': (-3, 2),
        'VIE_mass_mobilization': (-2, 2),
        # Center Spine (Anti-corruption & Party discipline)
        'VIE_anti_corruption_law': (-1, 1),
        'VIE_asset_declaration': (-2, 3),
        'VIE_state_audit': (-1, 3),
        'VIE_party_discipline': (-2, 4),
        'VIE_party_inspection': (-2, 5),
        'VIE_asset_recovery': (-1, 5),
        'VIE_clean_cadres': (-1, 6),
        # Right Wing (Public Admin & Rule of Law)
        'VIE_public_admin_reform': (1, 1),
        'VIE_decentralization': (1, 3),
        'VIE_e_government': (2, 3),
        'VIE_streamline_apparatus': (1, 4),
        'VIE_rule_of_law_state': (3, 2),
        'VIE_constitution_2013': (3, 3),
        'VIE_cybersecurity_law': (3, 4),
        'VIE_merge_ministries': (1, 5),
        'VIE_resolution_57_68': (2, 5),
        'VIE_provincial_merger': (1, 6),
        'VIE_institutional_bottlenecks': (2, 6),
        'VIE_two_tier_local_gov': (1, 7),
        # Capstone Convergence
        'VIE_era_of_rising': (0, 8),
        'VIE_party_centennial_2030': (0, 9),
    }
    for fid, (x, y) in pol_rel.items():
        layout[fid] = {'rel': 'VIE_anti_corruption_steering', 'x': x, 'y': y}

    # -------------------------------------------------------------------------
    # MODULE 2: EAST SEA DIAMOND (18 focuses)
    # Anchor: VIE_law_of_the_sea at abs (26, 1) relative to ROOT (dx = -54, dy = 1)
    # -------------------------------------------------------------------------
    layout['VIE_law_of_the_sea'] = {'rel': 'VIE_doi_moi_continues', 'x': -54, 'y': 1}

    sea_rel = {
        'VIE_maritime_militia': (-2, 1),
        'VIE_dk1_platforms': (-2, 2),
        'VIE_spratly_fortification': (-3, 3),
        'VIE_assert_maritime_rights': (-1, 3),
        'VIE_limited_war_doctrine': (-2, 4),
        'VIE_paracel_ultimatum': (-2, 5),
        'VIE_legal_warfare': (2, 1),
        'VIE_fisheries_surveillance': (0, 1),
        'VIE_coast_guard_law': (0, 2),
        'VIE_code_of_conduct': (2, 2),
        'VIE_peoples_defence': (2, 3),
        'VIE_provincial_defence_zones': (0, 4),
        'VIE_militia_law': (0, 5),
        'VIE_force_47': (2, 4),
        'VIE_cyber_command': (2, 5),
        'VIE_un_peacekeeping': (4, 4),
        'VIE_four_nos_doctrine': (0, 6),
    }
    for fid, (x, y) in sea_rel.items():
        layout[fid] = {'rel': 'VIE_law_of_the_sea', 'x': x, 'y': y}

    # -------------------------------------------------------------------------
    # MODULE 3: DIPLOMACY DIAMOND (39 focuses)
    # Anchor: VIE_asean_integration at abs (44, 1) relative to ROOT (dx = -36, dy = 1)
    # -------------------------------------------------------------------------
    layout['VIE_asean_integration'] = {'rel': 'VIE_doi_moi_continues', 'x': -36, 'y': 1}

    dip_rel = {
        'VIE_asean_chair': (-1, 1),
        'VIE_apec_host': (1, 1),
        'VIE_un_security_council': (0, 2),
        'VIE_bamboo_diplomacy': (0, 6),
        'VIE_global_south_ties': (0, 7),
        'VIE_multilateral_champion': (0, 8),
        # Western / Pacific Partnerships Wing
        'VIE_us_engagement': (-3, 1),
        'VIE_us_comprehensive_partnership': (-3, 2),
        'VIE_defence_hotline': (-4, 2),
        'VIE_japan_partnership': (-5, 2),
        'VIE_korea_partnership': (-5, 3),
        'VIE_france_eu': (-6, 3),
        'VIE_us_embargo_lifted': (-3, 3),
        'VIE_us_carrier_visit': (-3, 4),
        'VIE_us_tariff_deal': (-4, 4),
        'VIE_australia_partnership': (-5, 4),
        'VIE_india_partnership': (-6, 4),
        'VIE_csp_network': (-5, 5),
        'VIE_gulf_investment': (-6, 5),
        'VIE_pivot_to_the_west': (-3, 5),
        'VIE_military_cooperation_usa': (-3, 6),
        'VIE_indo_pacific_partner': (-3, 7),
        # Eastern / Neighbors Wing
        'VIE_border_settlement': (3, 1),
        'VIE_gulf_of_tonkin': (3, 2),
        'VIE_16_words': (4, 2),
        'VIE_border_trade_gates': (3, 3),
        'VIE_shared_future': (4, 3),
        'VIE_accept_chinese_influence': (3, 4),
        'VIE_join_bri': (4, 5),
        'VIE_socialist_bloc': (3, 6),
        # Indochina
        'VIE_special_relations_laos': (5, 2),
        'VIE_cambodia_relations': (6, 2),
        'VIE_cambodia_border': (6, 3),
        'VIE_mekong_commission': (5, 3),
        'VIE_mekong_dams_response': (5, 4),
        'VIE_funan_techo_response': (6, 4),
        'VIE_indochina_solidarity': (5, 5),
        'VIE_indochina_federation': (6, 6),
    }
    for fid, (x, y) in dip_rel.items():
        layout[fid] = {'rel': 'VIE_asean_integration', 'x': x, 'y': y}

    # -------------------------------------------------------------------------
    # MODULE 4: ECONOMY & INFRASTRUCTURE TRI-PYRAMID (112 focuses)
    # Positioned around VIE_doi_moi_continues at abs (80, 0)
    # -------------------------------------------------------------------------
    
    # Sub-pyramid 4.1: Institutions & Trade (dx in [-18..-6])
    layout['VIE_enterprise_law'] = {'rel': 'VIE_doi_moi_continues', 'x': -12, 'y': 1}
    trade_rel = {
        'VIE_bilateral_trade_agreement_usa': (-3, 1),
        'VIE_equitization_soes': (-1, 1),
        'VIE_investment_law_2005': (0, 1),
        'VIE_hose_exchange': (2, 1),
        'VIE_fdi_attraction': (-1, 2),
        'VIE_rice_export_power': (2, 2),
        'VIE_wto_negotiations': (-1, 3),
        'VIE_new_rural_development': (1, 3),
        'VIE_land_law_reform': (3, 3),
        'VIE_samsung_partnership': (-2, 4),
        'VIE_wto_reforms': (-1, 4),
        'VIE_high_tech_agriculture': (1, 4),
        'VIE_mekong_climate_adaptation': (3, 4),
        'VIE_export_powerhouse': (-1, 5),
        'VIE_cptpp_member': (-2, 6),
        'VIE_evfta': (0, 6),
    }
    for fid, (x, y) in trade_rel.items():
        layout[fid] = {'rel': 'VIE_enterprise_law', 'x': x, 'y': y}

    # Sub-pyramid 4.2: Banking & Finance & SOEs (dx in [-5..+5])
    layout['VIE_state_bank_modernization'] = {'rel': 'VIE_doi_moi_continues', 'x': -3, 'y': 1}
    bank_rel = {
        'VIE_fight_inflation': (-1, 1),
        'VIE_restructure_banking': (1, 1),
        'VIE_state_conglomerates': (3, 1),
        'VIE_deposit_insurance': (-1, 2),
        'VIE_vamc': (1, 2),
        'VIE_scic': (3, 2),
        'VIE_cross_ownership_crackdown': (-1, 3),
        'VIE_corporate_bond_reform': (1, 3),
        'VIE_soe_governance': (3, 3),
        'VIE_private_champions': (4, 3),
        'VIE_market_upgrade_criteria': (0, 4),
        'VIE_household_business': (3, 4),
        'VIE_international_financial_centre': (0, 5),
        'VIE_private_sector_engine': (3, 5),
        'VIE_investment_grade': (0, 6),
    }
    for fid, (x, y) in bank_rel.items():
        layout[fid] = {'rel': 'VIE_state_bank_modernization', 'x': x, 'y': y}

    # Sub-pyramid 4.3: Social, Education, Health, Culture (dx in [7..17])
    layout['VIE_education_reform'] = {'rel': 'VIE_doi_moi_continues', 'x': 8, 'y': 1}
    soc_rel = {
        # Education
        'VIE_university_autonomy': (-2, 1),
        'VIE_vocational_training': (-1, 1),
        'VIE_free_tuition': (-2, 2),
        'VIE_english_second_language': (-1, 2),
        # Health
        'VIE_universal_health_insurance': (0, 1),
        'VIE_grassroots_clinics': (0, 2),
        'VIE_vaccine_production': (-1, 3),
        'VIE_hospital_decongestion': (0, 3),
        'VIE_preventive_health': (0, 4),
        # Urban & Labor
        'VIE_urbanization': (2, 1),
        'VIE_labor_code_2019': (1, 2),
        'VIE_social_insurance_reform': (2, 2),
        'VIE_population_policy': (2, 3),
        'VIE_overseas_vietnamese': (2, 4),
        # Culture & Tourism
        'VIE_heritage_preservation': (4, 1),
        'VIE_visa_reform': (3, 2),
        'VIE_sea_games_bid': (4, 2),
        'VIE_cultural_industry': (4, 3),
        'VIE_tourism_powerhouse': (4, 4),
    }
    for fid, (x, y) in soc_rel.items():
        layout[fid] = {'rel': 'VIE_education_reform', 'x': x, 'y': y}

    # Sub-pyramid 4.4: Infrastructure, Energy & Digital Tech (dx in [20..42])
    layout['VIE_north_south_expressway'] = {'rel': 'VIE_doi_moi_continues', 'x': 25, 'y': 1}
    infra_rel = {
        # Transport
        'VIE_hanoi_metro': (-2, 1),
        'VIE_hcmc_metro': (-1, 1),
        'VIE_lach_huyen_port': (1, 1),
        'VIE_cai_mep_port': (2, 1),
        'VIE_long_thanh_airport': (-1, 2),
        'VIE_lao_cai_haiphong_rail': (1, 2),
        'VIE_north_south_hsr': (0, 3),
        # Energy, Power & Grid
        'VIE_petrovietnam_expansion': (-5, 1),
        'VIE_son_la_dam': (-6, 2),
        'VIE_500kv_grid': (-6, 3),
        'VIE_dppa_market_reform': (-6, 4),
        'VIE_coal_power': (-4, 2),
        'VIE_nghi_son_refinery': (-4, 3),
        'VIE_rare_earths': (-7, 2),
        'VIE_bauxite_tay_nguyen': (-7, 3),
        'VIE_solar_boom': (-5, 3),
        'VIE_power_plan_8': (-5, 4),
        'VIE_offshore_wind': (-5, 5),
        'VIE_energy_security_2045': (-5, 6),
        # Petrolimex Downstream & Green Hubs
        'VIE_petrolimex_downstream_network': (-3, 2),
        'VIE_strategic_petroleum_reserve': (-1, 4),
        'VIE_petrolimex_eneos_partnership': (2, 4),
        'VIE_petrolimex_green_ev_hubs': (0, 5),
        # Nuclear
        'VIE_ninh_thuan_nuclear': (-3, 3),
        'VIE_shelve_nuclear': (-3, 4),
        'VIE_build_nuclear_plant': (-3, 5),
        'VIE_revive_nuclear': (-2, 5),
        # Environment & Disaster Pillars
        'VIE_disaster_preparedness': (-8, 1),
        'VIE_military_rescue_corps': (-11, 2),
        'VIE_emergency_operations_center': (-11, 3),
        'VIE_dutch_water_model': (-9, 2),
        'VIE_nature_adaptation_120': (-8, 2),
        'VIE_sustainable_mekong_delta': (-9, 3),
        'VIE_satellite_early_warning': (-10, 4),
        'VIE_storm_resilient_islands': (-10, 5),
        'VIE_jetp_partnership': (-8, 4),
        'VIE_net_zero_2050': (-8, 5),
        # Supporting Industries & Metallurgy
        'VIE_supporting_industries': (4, 1),
        'VIE_formosa_steel_complex': (3, 2),
        'VIE_hoa_phat_hrc_steel': (3, 3),
        'VIE_precision_mechanics_molds': (3, 4),
        # Electronics & Supply Chain
        'VIE_intel_hcmc': (4, 2),
        'VIE_tier1_vendor_localization': (4, 3),
        'VIE_china_plus_one': (5, 2),
        'VIE_manufacturing_hub': (5, 3),
        # Automotive & EV Revolution
        'VIE_domestic_automotive': (6, 2),
        'VIE_integrated_auto_supplier_park': (6, 3),
        'VIE_ev_revolution_batteries': (6, 4),
        'VIE_global_auto_export': (6, 5),
        # Internet & Digital
        'VIE_internet_expansion': (8, 1),
        'VIE_mobile_networks': (7, 2),
        'VIE_cashless_payments': (8, 2),
        'VIE_national_digital_transformation': (8, 3),
        'VIE_digital_id': (8, 4),
        'VIE_national_data_center': (8, 5),
        'VIE_ai_strategy': (8, 6),
        'VIE_digital_nation': (7, 7),
        # Semiconductor
        'VIE_semiconductor_ambition': (10, 1),
        'VIE_chip_design': (10, 2),
        'VIE_chip_engineers': (11, 2),
        'VIE_semiconductor_fab': (10, 3),
        'VIE_viettel_global': (10, 4),
        # Science & Space
        'VIE_nafosted': (13, 1),
        'VIE_research_universities': (13, 2),
        'VIE_vinasat': (14, 2),
        'VIE_nuclear_research': (13, 3),
        'VIE_earth_observation': (14, 3),
        'VIE_science_breakthrough': (13, 4),
    }
    for fid, (x, y) in infra_rel.items():
        layout[fid] = {'rel': 'VIE_north_south_expressway', 'x': x, 'y': y}

    # -------------------------------------------------------------------------
    # SECTION 11: MEGA-CAPSTONES 2045 (TÁCH RIÊNG ĐỘC LẬP - ĐỂ RIÊNG)
    # Tách riêng khỏi 10 trụ cột kinh tế chính, đặt tại phân khu riêng biệt
    # -------------------------------------------------------------------------
    layout['VIE_upper_middle_income'] = {'rel': 'VIE_doi_moi_continues', 'x': 46, 'y': 1}
    layout['VIE_green_growth'] = {'rel': 'VIE_upper_middle_income', 'x': -1, 'y': 1}
    layout['VIE_innovation_nation'] = {'rel': 'VIE_upper_middle_income', 'x': 1, 'y': 1}
    layout['VIE_high_income_2045'] = {'rel': 'VIE_upper_middle_income', 'x': 0, 'y': 2}
    layout['VIE_developed_nation_2045'] = {'rel': 'VIE_upper_middle_income', 'x': 0, 'y': 3}

    # -------------------------------------------------------------------------
    # MODULE 5: MILITARY UNIFIED 4-COLUMN ARCHITECTURE (132 focuses)
    # Ref: VIE_focus_tree_military.png & manual_layout.py
    # Apex: VIE_modernize_vpa at (96, 10) relative to ROOT (dx = 16, dy = 10)
    # Four unified vertical columns:
    # 1. Army (Lục quân)           - Head: VIE_tank_modernization (X=52, Y=11)
    # 2. Navy (Hải quân)           - Head: VIE_navy_modernization (X=86, Y=11)
    # 3. Air Force (Không quân)    - Head: VIE_air_force_modernization (X=108, Y=11)
    # 4. Defence Industry & Missiles - Head: VIE_viettel_military_tech (X=139, Y=11)
    # -------------------------------------------------------------------------
    ROOT_ROW = 10
    HEADS = {1: 'VIE_tank_modernization', 2: 'VIE_navy_modernization', 3: 'VIE_air_force_modernization', 4: 'VIE_viettel_military_tech'}
    V = 'VIE_'
    
    try:
        from tools.manual_layout import MAN, CENTRES
    except ImportError:
        from manual_layout import MAN, CENTRES

    vpa_x = round(sum(CENTRES[c] + MAN[c][h.replace('VIE_', '')][0] for c, h in HEADS.items()) / 4)
    layout['VIE_modernize_vpa'] = {'rel': 'VIE_doi_moi_continues', 'x': vpa_x - 80, 'y': ROOT_ROW}

    for c, mp in MAN.items():
        head_fid = HEADS[c]
        head_key = head_fid.replace('VIE_', '')
        head_abs_x = CENTRES[c] + mp[head_key][0]
        head_abs_y = ROOT_ROW + mp[head_key][1]
        
        layout[head_fid] = {'rel': 'VIE_modernize_vpa', 'x': head_abs_x - vpa_x, 'y': head_abs_y - ROOT_ROW}
        
        for k, (lx, r) in mp.items():
            fid = V + k
            if fid == head_fid: continue
            abs_x = CENTRES[c] + lx
            abs_y = ROOT_ROW + r
            layout[fid] = {'rel': head_fid, 'x': abs_x - head_abs_x, 'y': abs_y - head_abs_y}

    # JOIN: VIE_defence_strategy_review
    layout['VIE_defence_strategy_review'] = {'rel': 'VIE_modernize_vpa', 'x': 0, 'y': 5}

    # -------------------------------------------------------------------------
    # MODULE 6: ALTERNATIVE REGIMES (159 focuses)
    # Layer 3: Y in [28..37]
    # -------------------------------------------------------------------------

    # 6.1 Developmental State & Pluralism
    layout['VIE_developmental_state'] = {'rel': 'VIE_doi_moi_continues', 'x': -5, 'y': 28}
    dev_rel = {
        'VIE_technocrat_cabinet': (-2, 1),
        'VIE_intra_party_elections': (0, 1),
        'VIE_press_relaxation': (2, 1),
        'VIE_environmental_accountability': (4, 1),
        'VIE_meritocratic_service': (-2, 2),
        'VIE_judicial_reform': (0, 2),
        'VIE_front_coalition': (2, 2),
        'VIE_performance_legitimacy': (-2, 3),
        'VIE_vetted_elections': (0, 3),
        'VIE_singapore_model': (-2, 4),
        # Transition & Pluralism
        'VIE_round_table_talks': (2, 3),
        'VIE_revive_democratic_party': (1, 4),
        'VIE_revive_socialist_party': (3, 4),
        'VIE_loyal_opposition': (2, 4),
        'VIE_legalize_parties': (2, 5),
        'VIE_new_constitution': (0, 5),
        'VIE_managed_pluralism': (1, 6),
        'VIE_first_free_election': (2, 6),
        'VIE_consolidate_democracy': (2, 7),
        'VIE_dm_truth_reconciliation': (1, 7),
        # 4 Post-election Parties
        'VIE_dm_lib_market_opening': (-3, 8),
        'VIE_dm_lib_independent_anticorruption': (-4, 9),
        'VIE_dm_lib_free_trade': (-3, 9),
        'VIE_dm_lib_eu_alignment': (-2, 9),
        'VIE_dm_soc_welfare_state': (-1, 8),
        'VIE_dm_soc_labor_rights': (-1, 9),
        'VIE_dm_soc_public_healthcare': (0, 9),
        'VIE_dm_soc_progressive_tax': (1, 9),
        'VIE_dm_con_fiscal_discipline': (2, 8),
        'VIE_dm_con_us_alignment': (2, 9),
        'VIE_dm_con_community_institutions': (3, 9),
        'VIE_dm_con_strong_defense': (4, 9),
        'VIE_dm_tra_cultural_heritage': (5, 8),
        'VIE_dm_tra_religious_freedom': (5, 9),
        'VIE_dm_tra_rural_first': (6, 9),
        'VIE_dm_tra_balanced_neutrality': (7, 9),
    }
    for fid, (x, y) in dev_rel.items():
        layout[fid] = {'rel': 'VIE_developmental_state', 'x': x, 'y': y}

    # 6.2 CPV Orthodoxy & Tech Autonomy (Apex: VIE_defend_the_foundation, dx = -35 from ROOT)
    layout['VIE_defend_the_foundation'] = {'rel': 'VIE_doi_moi_continues', 'x': -35, 'y': 28}
    orth_rel = {
        'VIE_anti_peaceful_evolution': (-2, 1),
        'VIE_state_sector_leading': (0, 1),
        'VIE_self_reliance': (2, 1),
        'VIE_nationalize_foreign_assets': (0, 2),
        'VIE_ideological_fortress': (2, 2),
        # Tech Autonomy
        'VIE_tc_strategic_autonomy': (5, 0),
        'VIE_tc_decouple_supply': (4, 1),
        'VIE_tc_self_management': (5, 1),
        'VIE_tc_russia_india_axis': (6, 1),
        'VIE_tc_global_south': (5, 2),
        'VIE_tc_import_substitution': (4, 3),
        'VIE_tc_nonaligned_summit': (5, 3),
        'VIE_tc_workers_councils': (6, 3),
        'VIE_tc_armed_neutrality': (7, 3),
        'VIE_tc_arms_diversification': (8, 3),
        'VIE_tc_asean_bloc': (4, 4),
        'VIE_tc_market_socialism': (5, 4),
        'VIE_tc_rare_earth_leverage': (6, 4),
        'VIE_tc_mekong_leadership': (5, 5),
        'VIE_tc_eastern_yugoslavia': (6, 5),
    }
    for fid, (x, y) in orth_rel.items():
        layout[fid] = {'rel': 'VIE_defend_the_foundation', 'x': x, 'y': y}

    # 6.3 Nationalist, Junta & Security (Apex: VIE_np_street_mandate, dx = 18 from ROOT)
    layout['VIE_np_street_mandate'] = {'rel': 'VIE_doi_moi_continues', 'x': 18, 'y': 28}
    np_rel = {
        'VIE_np_boycott': (-2, 1),
        'VIE_np_maritime_militia_mass': (0, 1),
        'VIE_np_purge_collaborators': (2, 1),
        'VIE_np_institutionalize': (-1, 2),
        'VIE_np_paracel_campaign': (1, 2),
        'VIE_np_national_goods': (-2, 3),
        'VIE_np_youth_brigades': (0, 3),
        'VIE_np_fishermen_protection': (1, 3),
        'VIE_np_veterans_council': (2, 3),
        'VIE_np_patriotic_media': (-1, 4),
        'VIE_np_sovereignty_referendum': (0, 4),
        'VIE_np_nationalist_economy': (2, 4),
        'VIE_np_nation_first': (0, 5),
        # Junta
        'VIE_national_salvation_council': (5, 0),
        'VIE_jn_purge_party': (4, 1),
        'VIE_martial_law': (5, 1),
        'VIE_military_economy': (6, 1),
        'VIE_jn_border_mobilization': (7, 1),
        'VIE_jn_constitutional_roadmap': (5, 2),
        'VIE_jn_military_technocrats': (6, 2),
        'VIE_restore_civilian_rule': (5, 3),
        # Security State
        'VIE_sec_cyber_control': (10, 0),
        'VIE_sec_surveillance_network': (9, 1),
        'VIE_sec_public_order': (10, 1),
        'VIE_sec_security_economy': (11, 1),
        'VIE_sec_cyber_sovereignty': (9, 2),
        'VIE_sec_loyalty_vetting': (10, 2),
        'VIE_sec_border_control': (11, 2),
        'VIE_sec_managed_opening': (10, 3),
    }
    for fid, (x, y) in np_rel.items():
        layout[fid] = {'rel': 'VIE_np_street_mandate', 'x': x, 'y': y}

    # 6.4 SEZ, Oligarch, East Asian wa, Royal, Green, Ethnic, Commune (Apex: VIE_lb_sez_law, dx = 38 from ROOT)
    layout['VIE_lb_sez_law'] = {'rel': 'VIE_doi_moi_continues', 'x': 38, 'y': 28}
    sp_rel = {
        # SEZ
        'VIE_lb_99_year_leases': (-2, 1),
        'VIE_lb_common_law_courts': (0, 1),
        'VIE_lb_flat_tax': (2, 1),
        'VIE_lb_expand_zones': (0, 2),
        'VIE_lb_van_don': (-2, 3),
        'VIE_lb_bac_van_phong': (-1, 3),
        'VIE_lb_phu_quoc': (0, 3),
        'VIE_lb_charter_state': (1, 3),
        'VIE_lb_free_port': (2, 3),
        'VIE_lb_casino_resorts': (-1, 4),
        'VIE_lb_sovereignty_safeguards': (0, 4),
        'VIE_lb_digital_assets': (2, 4),
        # Oligarchy
        'VIE_ol_bailout': (5, 0),
        'VIE_ol_conglomerate_council': (4, 1),
        'VIE_ol_media_ownership': (5, 1),
        'VIE_ol_real_estate_boom': (6, 1),
        'VIE_ol_reform_from_within': (5, 2),
        'VIE_ol_bank_capture': (4, 3),
        'VIE_ol_land_bank': (5, 3),
        'VIE_ol_political_donations': (6, 3),
        'VIE_ol_private_security': (7, 3),
        'VIE_ol_offshore_wealth': (5, 4),
        'VIE_ol_golden_visa': (6, 4),
        'VIE_ol_tycoon_diplomacy': (5, 5),
        # East Asian wa
        'VIE_wa_development_council': (10, 0),
        'VIE_wa_five_year_plans': (9, 1),
        'VIE_wa_us_alliance': (10, 1),
        'VIE_wa_national_champions': (11, 1),
        'VIE_wa_export_drive': (12, 1),
        'VIE_wa_japan_capital': (9, 2),
        'VIE_wa_heavy_industry': (10, 2),
        'VIE_wa_suppress_labor': (11, 2),
        'VIE_wa_cam_ranh_access': (8, 3),
        'VIE_wa_technical_education': (9, 3),
        'VIE_wa_korea_partnership': (10, 3),
        'VIE_wa_new_countryside': (11, 3),
        'VIE_wa_anti_corruption_purge': (12, 3),
        'VIE_wa_economic_miracle': (10, 4),
        'VIE_wa_prepare_transition': (11, 4),
        # Caretaker
        'VIE_ng_technocratic_caretaker': (15, 0),
        'VIE_ng_reconciliation': (14, 1),
        'VIE_ng_ceasefire': (15, 1),
        'VIE_ng_election_roadmap': (16, 1),
        'VIE_ng_economic_stabilization': (15, 2),
        'VIE_ng_handover': (15, 3),
        # Monarchy
        'VIE_mn_recall_royal_house': (19, 0),
        'VIE_mn_two_heirs': (18, 1),
        'VIE_mn_diaspora_reconciliation': (19, 1),
        'VIE_mn_constitutional_monarchy': (18, 2),
        'VIE_mn_imperial_heritage': (19, 2),
        'VIE_mn_hue_conference': (18, 3),
        'VIE_mn_royal_charter': (19, 3),
        'VIE_mn_royal_diplomacy': (20, 3),
        'VIE_mn_crown_as_mediator': (19, 4),
        'VIE_mn_parliamentary_monarchy': (19, 5),
        # Green Coalition
        'VIE_gr_green_coalition': (23, 0),
        'VIE_gr_environmental_law': (22, 1),
        'VIE_gr_polluter_pays': (23, 1),
        'VIE_gr_save_mekong': (24, 1),
        'VIE_gr_coal_phaseout': (22, 2),
        'VIE_gr_reforestation': (23, 2),
        'VIE_gr_green_cities': (24, 2),
        'VIE_gr_climate_diplomacy': (23, 3),
        'VIE_gr_green_transition': (23, 4),
        # Ethnic Nationalism & Workers Commune
        'VIE_lh_ethnic_nationalism': (26, 0),
        'VIE_lh_total_mobilization': (26, 1),
        'VIE_lh_awakening': (26, 2),
        'VIE_wk_workers_commune': (28, 0),
        'VIE_wk_factory_councils': (28, 1),
        'VIE_wk_federation_of_communes': (28, 2),
    }
    for fid, (x, y) in sp_rel.items():
        layout[fid] = {'rel': 'VIE_lb_sez_law', 'x': x, 'y': y}

    return layout

def validate_layout(focuses, layout):
    file_fids = set(f['id'] for f in focuses)
    layout_fids = set(layout.keys())
    
    missing = file_fids - layout_fids
    extra = layout_fids - file_fids
    
    if missing:
        print(f"ERROR: Missing focuses ({len(missing)}): {missing}")
        return False
    if extra:
        print(f"ERROR: Extra focuses ({len(extra)}): {extra}")
        return False
        
    def get_abs(fid, visited=None):
        if visited is None: visited = set()
        if fid in visited: return 0, 0
        visited.add(fid)
        info = layout.get(fid)
        if not info: return 0, 0
        if not info['rel']: return info['x'], info['y']
        rx, ry = get_abs(info['rel'], visited)
        return rx + info['x'], ry + info['y']
    
    abs_coords = {}
    for fid in layout_fids:
        abs_coords[fid] = get_abs(fid)
    
    c = Counter(abs_coords.values())
    dups = [coord for coord, count in c.items() if count > 1]
    if dups:
        print(f"\nERROR: COLLISIONS DETECTED ({len(dups)}):")
        for d in dups:
            clashing = [fid for fid, coord in abs_coords.items() if coord == d]
            print(f"  Coord {d}: {clashing}")
        return False
        
    xs = [coord[0] for coord in abs_coords.values()]
    ys = [coord[1] for coord in abs_coords.values()]
    print(f"\nLAYOUT IS 100% VALID!")
    print(f"Total Focuses: {len(layout_fids)} / {len(file_fids)}")
    print(f"Collisions: 0")
    print(f"Absolute X span: {min(xs)} to {max(xs)} (width: {max(xs) - min(xs) + 1})")
    print(f"Absolute Y span: {min(ys)} to {max(ys)} (depth: {max(ys) - min(ys) + 1})")
    return True

def apply_and_save():
    content, focuses = parse_focus_file(FOCUS_FILE)
    layout = build_master_layout()
    if not validate_layout(focuses, layout):
        print("Cannot apply: layout validation failed.")
        sys.exit(1)
        
    new_content = apply_layout_to_text(content, layout)
    
    with open(FOCUS_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully wrote new layout to {FOCUS_FILE}")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--apply':
        apply_and_save()
    else:
        content, focuses = parse_focus_file(FOCUS_FILE)
        layout = build_master_layout()
        validate_layout(focuses, layout)
