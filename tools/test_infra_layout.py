# Proposed compact layout for all 44 Infrastructure focuses
# Format: fid: {'abs': (x, y), 'rel': anchor, 'dx': dx, 'dy': dy, 'prereqs': [...], 'avail': [...]}

INFRA_LAYOUT = {
    # === ROW y = 1 (Root) ===
    'VIE_infrastructure_development': {
        'abs': (80, 1), 'rel': 'VIE_doi_moi_continues', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_doi_moi_continues'], 'avail': []
    },

    # === ROW y = 2 (7 focuses) ===
    'VIE_cai_mep_port': {
        'abs': (68, 2), 'rel': 'VIE_infrastructure_development', 'dx': -12, 'dy': 1,
        'prereqs': ['VIE_infrastructure_development'], 'avail': []
    },
    'VIE_lach_huyen_port': {
        'abs': (70, 2), 'rel': 'VIE_infrastructure_development', 'dx': -10, 'dy': 1,
        'prereqs': ['VIE_infrastructure_development'], 'avail': []
    },
    'VIE_transport_strategy_2004': {
        'abs': (72, 2), 'rel': 'VIE_infrastructure_development', 'dx': -8, 'dy': 1,
        'prereqs': ['VIE_infrastructure_development'], 'avail': []
    },
    'VIE_infrastructure_breakthrough_nq13': {
        'abs': (76, 2), 'rel': 'VIE_infrastructure_development', 'dx': -4, 'dy': 1,
        'prereqs': ['VIE_infrastructure_development'], 'avail': []
    },
    'VIE_hsr_2010_reject': {
        'abs': (78, 2), 'rel': 'VIE_infrastructure_development', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_infrastructure_development'], 'avail': []
    },
    'VIE_hsr_2010_approve': {
        'abs': (82, 2), 'rel': 'VIE_infrastructure_development', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_infrastructure_development'], 'avail': []
    },
    'VIE_reunification_line_upgrade': {
        'abs': (86, 2), 'rel': 'VIE_infrastructure_development', 'dx': 6, 'dy': 1,
        'prereqs': ['VIE_infrastructure_development'], 'avail': []
    },

    # === ROW y = 3 (8 focuses) ===
    'VIE_logistics_strategy': {
        'abs': (70, 3), 'rel': 'VIE_lach_huyen_port', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_lach_huyen_port'], 'avail': ['VIE_cai_mep_port']
    },
    'VIE_hai_van_tunnel': {
        'abs': (72, 3), 'rel': 'VIE_transport_strategy_2004', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_transport_strategy_2004'], 'avail': []
    },
    'VIE_hcmc_trung_luong_expressway': {
        'abs': (74, 3), 'rel': 'VIE_transport_strategy_2004', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_transport_strategy_2004'], 'avail': []
    },
    'VIE_can_tho_bridge': {
        'abs': (76, 3), 'rel': 'VIE_transport_strategy_2004', 'dx': 4, 'dy': 1,
        'prereqs': ['VIE_transport_strategy_2004'], 'avail': []
    },
    'VIE_north_south_hsr': {
        'abs': (80, 3), 'rel': 'VIE_hsr_2010_reject', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_hsr_2010_reject', 'VIE_hsr_2010_approve'], 'avail': []
    },
    'VIE_lao_cai_haiphong_rail': {
        'abs': (86, 3), 'rel': 'VIE_reunification_line_upgrade', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_reunification_line_upgrade'], 'avail': []
    },
    'VIE_hcmc_metro': {
        'abs': (88, 3), 'rel': 'VIE_reunification_line_upgrade', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_reunification_line_upgrade'], 'avail': []
    },
    'VIE_urban_rail_hanoi': {
        'abs': (90, 3), 'rel': 'VIE_reunification_line_upgrade', 'dx': 4, 'dy': 1,
        'prereqs': ['VIE_reunification_line_upgrade'], 'avail': []
    },

    # === ROW y = 4 (7 focuses) ===
    'VIE_northern_expressways': {
        'abs': (72, 4), 'rel': 'VIE_hcmc_trung_luong_expressway', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_hcmc_trung_luong_expressway'], 'avail': []
    },
    'VIE_north_south_expressway': {
        'abs': (74, 4), 'rel': 'VIE_hcmc_trung_luong_expressway', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_hcmc_trung_luong_expressway'], 'avail': []
    },
    'VIE_hsr_partner_japan': {
        'abs': (78, 4), 'rel': 'VIE_north_south_hsr', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_north_south_hsr'], 'avail': []
    },
    'VIE_hsr_partner_eu': {
        'abs': (80, 4), 'rel': 'VIE_north_south_hsr', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_north_south_hsr'], 'avail': []
    },
    'VIE_hsr_partner_china': {
        'abs': (82, 4), 'rel': 'VIE_north_south_hsr', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_north_south_hsr'], 'avail': []
    },
    'VIE_domestic_rail_industry': {
        'abs': (86, 4), 'rel': 'VIE_lao_cai_haiphong_rail', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_lao_cai_haiphong_rail'], 'avail': []
    },
    'VIE_urban_rail_special_mechanism_nq188': {
        'abs': (90, 4), 'rel': 'VIE_urban_rail_hanoi', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_urban_rail_hanoi'], 'avail': ['VIE_hcmc_metro']
    },

    # === ROW y = 5 (5 focuses) ===
    'VIE_expressway_regional_links': {
        'abs': (70, 5), 'rel': 'VIE_northern_expressways', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_northern_expressways'], 'avail': []
    },
    'VIE_expressway_bot': {
        'abs': (72, 5), 'rel': 'VIE_north_south_expressway', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_north_south_expressway'], 'avail': []
    },
    'VIE_expressway_public_investment': {
        'abs': (74, 5), 'rel': 'VIE_north_south_expressway', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_north_south_expressway'], 'avail': []
    },
    'VIE_hsr_groundbreaking': {
        'abs': (80, 5), 'rel': 'VIE_hsr_partner_eu', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_hsr_partner_japan', 'VIE_hsr_partner_eu', 'VIE_hsr_partner_china'], 'avail': []
    },
    'VIE_metro_network_2035': {
        'abs': (90, 5), 'rel': 'VIE_urban_rail_special_mechanism_nq188', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_urban_rail_special_mechanism_nq188'], 'avail': []
    },

    # === ROW y = 6 (2 focuses) ===
    'VIE_north_south_expressway_phase2': {
        'abs': (72, 6), 'rel': 'VIE_expressway_bot', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_expressway_bot'], 'avail': ['VIE_expressway_public_investment']
    },
    'VIE_airport_master_plan': {
        'abs': (80, 6), 'rel': 'VIE_hsr_groundbreaking', 'dx': 0, 'dy': 1,
        'prereqs': [], 'avail': ['VIE_infrastructure_development']
    },

    # === ROW y = 7 (6 focuses) ===
    'VIE_ring_roads_hanoi_hcmc': {
        'abs': (70, 7), 'rel': 'VIE_north_south_expressway_phase2', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_north_south_expressway_phase2'], 'avail': []
    },
    'VIE_expressway_3000km': {
        'abs': (74, 7), 'rel': 'VIE_north_south_expressway_phase2', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_north_south_expressway_phase2'], 'avail': []
    },
    'VIE_aviation_market_opening': {
        'abs': (78, 7), 'rel': 'VIE_airport_master_plan', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_airport_master_plan'], 'avail': []
    },
    'VIE_noi_bai_t2': {
        'abs': (80, 7), 'rel': 'VIE_airport_master_plan', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_airport_master_plan'], 'avail': []
    },
    'VIE_long_thanh_approval': {
        'abs': (82, 7), 'rel': 'VIE_airport_master_plan', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_airport_master_plan'], 'avail': []
    },
    'VIE_tan_son_nhat_t3': {
        'abs': (84, 7), 'rel': 'VIE_airport_master_plan', 'dx': 4, 'dy': 1,
        'prereqs': ['VIE_airport_master_plan'], 'avail': []
    },

    # === ROW y = 8 (5 focuses) ===
    'VIE_expressway_5000km_2030': {
        'abs': (74, 8), 'rel': 'VIE_expressway_3000km', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_expressway_3000km'], 'avail': []
    },
    'VIE_socialized_airports': {
        'abs': (78, 8), 'rel': 'VIE_aviation_market_opening', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_aviation_market_opening'], 'avail': []
    },
    'VIE_acv_monopoly': {
        'abs': (80, 8), 'rel': 'VIE_aviation_market_opening', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_aviation_market_opening'], 'avail': []
    },
    'VIE_long_thanh_airport': {
        'abs': (82, 8), 'rel': 'VIE_long_thanh_approval', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_long_thanh_approval'], 'avail': []
    },
    'VIE_dual_use_airports': {
        'abs': (84, 8), 'rel': 'VIE_tan_son_nhat_t3', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_airport_master_plan'], 'avail': ['VIE_tan_son_nhat_t3']
    },

    # === ROW y = 9 (3 focuses) ===
    'VIE_synchronized_infrastructure_2030': {
        'abs': (74, 9), 'rel': 'VIE_expressway_5000km_2030', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_expressway_5000km_2030'], 'avail': ['VIE_long_thanh_airport']
    },
    'VIE_van_don_airport': {
        'abs': (78, 9), 'rel': 'VIE_socialized_airports', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_socialized_airports'], 'avail': []
    },
    'VIE_airport_network_2030': {
        'abs': (80, 9), 'rel': 'VIE_acv_monopoly', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_acv_monopoly'], 'avail': ['VIE_socialized_airports']
    }
}
