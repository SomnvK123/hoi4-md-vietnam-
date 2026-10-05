# Layout configuration for Khoa hoc so, Cong nghe & Xa hoi (27 focuses)
# 19 Digital & Science focuses + 8 Society & Sustainable Development focuses

DIGITAL_SOCIETY_LAYOUT = {
    # ==========================================
    # NHANH KHOA HOC CONG NGHE SO & VIEN THONG (19 FOCUS)
    # Root: VIE_sci_digital_root (x=156, y=1)
    # ==========================================
    # y = 1
    'VIE_sci_digital_root': {
        'abs': (156, 1), 'rel': 'VIE_doi_moi_continues', 'dx': 76, 'dy': 1,
        'prereqs': [], 'avail': ['date > 2005.12.31']
    },

    # y = 2
    'VIE_internet_expansion': {
        'abs': (152, 2), 'rel': 'VIE_sci_digital_root', 'dx': -4, 'dy': 1,
        'prereqs': ['VIE_sci_digital_root'], 'avail': ['date > 2005.12.31']
    },
    'VIE_nafosted': {
        'abs': (160, 2), 'rel': 'VIE_sci_digital_root', 'dx': 4, 'dy': 1,
        'prereqs': ['VIE_sci_digital_root'], 'avail': ['date > 2007.12.31']
    },

    # y = 3
    'VIE_mobile_3g_4g': {
        'abs': (146, 3), 'rel': 'VIE_internet_expansion', 'dx': -6, 'dy': 1,
        'prereqs': ['VIE_internet_expansion'], 'avail': ['date > 2009.8.31']
    },
    'VIE_national_digital_transformation': {
        'abs': (152, 3), 'rel': 'VIE_internet_expansion', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_internet_expansion'], 'avail': ['date > 2019.12.31']
    },
    'VIE_viettel_global': {
        'abs': (156, 3), 'rel': 'VIE_internet_expansion', 'dx': 4, 'dy': 1,
        'prereqs': ['VIE_internet_expansion'], 'avail': ['date > 2005.12.31']
    },
    'VIE_research_universities': {
        'abs': (158, 3), 'rel': 'VIE_nafosted', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_nafosted'], 'avail': []
    },
    'VIE_vinasat': {
        'abs': (162, 3), 'rel': 'VIE_nafosted', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_nafosted'], 'avail': ['date > 2007.12.31']
    },

    # y = 4
    'VIE_mobile_networks': {
        'abs': (144, 4), 'rel': 'VIE_mobile_3g_4g', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_mobile_3g_4g'], 'avail': ['date > 2023.12.31']
    },
    'VIE_submarine_cables': {
        'abs': (148, 4), 'rel': 'VIE_mobile_3g_4g', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_mobile_3g_4g'], 'avail': ['date > 2013.12.31']
    },
    'VIE_digital_id': {
        'abs': (152, 4), 'rel': 'VIE_national_digital_transformation', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_national_digital_transformation'], 'avail': ['date > 2022.12.31']
    },
    'VIE_ai_strategy': {
        'abs': (154, 4), 'rel': 'VIE_national_digital_transformation', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_national_digital_transformation'], 'avail': ['date > 2020.12.31']
    },
    'VIE_make_in_vietnam': {
        'abs': (156, 4), 'rel': 'VIE_viettel_global', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_viettel_global'], 'avail': ['date > 2019.5.31']
    },
    'VIE_nuclear_research': {
        'abs': (158, 4), 'rel': 'VIE_research_universities', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_nafosted'], 'avail': []
    },
    'VIE_earth_observation': {
        'abs': (162, 4), 'rel': 'VIE_vinasat', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_vinasat'], 'avail': ['date > 2012.12.31']
    },

    # y = 5
    'VIE_national_data_center': {
        'abs': (152, 5), 'rel': 'VIE_digital_id', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_digital_id'], 'avail': ['date > 2024.11.30']
    },
    'VIE_digital_tech_industry_law': {
        'abs': (156, 5), 'rel': 'VIE_make_in_vietnam', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_make_in_vietnam'], 'avail': ['date > 2025.6.30']
    },
    'VIE_science_breakthrough': {
        'abs': (160, 5), 'rel': 'VIE_nuclear_research', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_research_universities'], 'avail': ['date > 2024.11.30']
    },

    # y = 6 (Diem hoi tu Cong nghe so)
    'VIE_digital_nation': {
        'abs': (152, 6), 'rel': 'VIE_national_data_center', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_national_data_center'], 'avail': ['VIE_mobile_networks', 'VIE_ai_strategy']
    },

    # ==========================================
    # NHANH PHAT TRIEN BEN VUNG & XA HOI 2045 (8 FOCUS)
    # Root: VIE_upper_middle_income (x=166, y=1)
    # ==========================================
    # y = 1
    'VIE_upper_middle_income': {
        'abs': (166, 1), 'rel': 'VIE_doi_moi_continues', 'dx': 86, 'dy': 1,
        'prereqs': [], 'avail': ['date > 2029.12.31']
    },

    # y = 2
    'VIE_green_growth': {
        'abs': (164, 2), 'rel': 'VIE_upper_middle_income', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_upper_middle_income'], 'avail': []
    },
    'VIE_innovation_nation': {
        'abs': (168, 2), 'rel': 'VIE_upper_middle_income', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_upper_middle_income'], 'avail': []
    },
    'VIE_ageing_society': {
        'abs': (170, 2), 'rel': 'VIE_upper_middle_income', 'dx': 4, 'dy': 1,
        'prereqs': ['VIE_upper_middle_income'], 'avail': ['date > 2032.12.31']
    },

    # y = 3
    'VIE_carbon_circular_economy': {
        'abs': (164, 3), 'rel': 'VIE_green_growth', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_green_growth'], 'avail': ['date > 2027.12.31']
    },
    'VIE_productivity_leap': {
        'abs': (168, 3), 'rel': 'VIE_innovation_nation', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_innovation_nation'], 'avail': ['date > 2033.12.31']
    },

    # y = 4
    'VIE_high_income_2045': {
        'abs': (166, 4), 'rel': 'VIE_carbon_circular_economy', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_carbon_circular_economy'], 'avail': ['VIE_productivity_leap', 'date > 2039.12.31']
    },

    # y = 5
    'VIE_developed_nation_2045': {
        'abs': (166, 5), 'rel': 'VIE_high_income_2045', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_high_income_2045'], 'avail': ['VIE_ageing_society', 'date > 2044.12.31']
    }
}

if __name__ == '__main__':
    print(f"Total mapped focuses: {len(DIGITAL_SOCIETY_LAYOUT)} (expected 27)")

    # Verify calculated coords match abs
    def calc_pos(fid, visited=None):
        if visited is None: visited = set()
        if fid in visited: return (0, 0)
        visited.add(fid)
        cfg = DIGITAL_SOCIETY_LAYOUT[fid]
        rel = cfg['rel']
        if rel == 'VIE_doi_moi_continues':
            return (80 + cfg['dx'], 0 + cfg['dy'])
        px, py = calc_pos(rel, visited)
        return (px + cfg['dx'], py + cfg['dy'])

    mismatches = []
    for fid, cfg in DIGITAL_SOCIETY_LAYOUT.items():
        cx, cy = calc_pos(fid)
        ax, ay = cfg['abs']
        if (cx, cy) != (ax, ay):
            mismatches.append((fid, (cx, cy), (ax, ay)))
    if mismatches:
        print("COORDINATE MISMATCHES:")
        for m in mismatches:
            print(f"  {m[0]}: calc {m[1]} != abs {m[2]}")
    else:
        print("All 27 relative coordinates match absolute coordinates perfectly!")

    # Check internal collisions
    by_pos = {}
    for fid, cfg in DIGITAL_SOCIETY_LAYOUT.items():
        by_pos.setdefault(cfg['abs'], []).append(fid)
    collisions = {pos: fs for pos, fs in by_pos.items() if len(fs) > 1}
    print("Collisions within branch:", len(collisions))

    # Check spacing
    rows = {}
    for fid, cfg in DIGITAL_SOCIETY_LAYOUT.items():
        rows.setdefault(cfg['abs'][1], []).append((cfg['abs'][0], fid))
    gap_violations = []
    for y in sorted(rows.keys()):
        r = sorted(rows[y])
        print(f"Row y={y:2d} ({len(r):2d} focuses): " + ", ".join([f"{f}(x={x})" for x, f in r]))
        for i in range(len(r) - 1):
            if r[i+1][0] - r[i][0] < 2:
                gap_violations.append((y, r[i][1], r[i+1][1], r[i+1][0] - r[i][0]))
    print("Gap violations (dx < 2):", len(gap_violations))

    # Check external collisions with other branches
    import sys, os
    sys.path.append(os.path.dirname(__file__))
    from analyze_target_focuses import foci, get_abs
    ext_coords = {}
    for fid in foci:
        if fid not in DIGITAL_SOCIETY_LAYOUT:
            ext_coords[fid] = get_abs(fid)
    ext_collisions = {}
    for fid, cfg in DIGITAL_SOCIETY_LAYOUT.items():
        pos = cfg['abs']
        colliders = [ef for ef, epos in ext_coords.items() if epos == pos]
        if colliders:
            ext_collisions[fid] = (pos, colliders)
    print("Collisions with external focuses:", len(ext_collisions))
    if ext_collisions:
        for f, (pos, col) in ext_collisions.items():
            print(f"  {f} at {pos} collides with {col}")

    # Generate topological file order
    in_degree = {}
    for fid, cfg in DIGITAL_SOCIETY_LAYOUT.items():
        deps = []
        if cfg['rel'] in DIGITAL_SOCIETY_LAYOUT:
            deps.append(cfg['rel'])
        for p in cfg['prereqs']:
            if p in DIGITAL_SOCIETY_LAYOUT and p not in deps:
                deps.append(p)
        in_degree[fid] = deps

    order = []
    visited_fids = set()
    while len(visited_fids) < len(DIGITAL_SOCIETY_LAYOUT):
        ready = [f for f, deps in in_degree.items() if f not in visited_fids and all(d in visited_fids for d in deps)]
        ready.sort(key=lambda f: (DIGITAL_SOCIETY_LAYOUT[f]['abs'][1], DIGITAL_SOCIETY_LAYOUT[f]['abs'][0]))
        for f in ready:
            visited_fids.add(f)
            order.append(f)
            break

    print(f"\nTopological file order generated: {len(order)} focuses")
    for i, f in enumerate(order, 1):
        cfg = DIGITAL_SOCIETY_LAYOUT[f]
        print(f"  {i:2d}. {f:38} | y={cfg['abs'][1]:2d}, x={cfg['abs'][0]:2d} | rel={cfg['rel']}")
