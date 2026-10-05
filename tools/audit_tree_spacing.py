import sys, os, re
sys.path.insert(0, os.path.abspath("."))

with open("common/national_focus/VIE_md_focus.txt", "r", encoding="utf-8") as f:
    text = f.read()

pos = 0
focuses = {}
focus_list = []
while True:
    m = re.search(r'\bfocus\s*=\s*\{', text[pos:])
    if not m:
        break
    start = pos + m.start()
    depth = 0
    i = pos + m.end() - 1
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                block = text[start:i+1]
                id_m = re.search(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', block, re.MULTILINE)
                x_m = re.search(r'^\s*x\s*=\s*(-?\d+)', block, re.MULTILINE)
                y_m = re.search(r'^\s*y\s*=\s*(-?\d+)', block, re.MULTILINE)
                rel_m = re.search(r'^\s*relative_position_id\s*=\s*([a-zA-Z0-9_]+)', block, re.MULTILINE)
                prereqs = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_]+)\s*\}', block)
                if id_m:
                    fid = id_m.group(1)
                    f_data = {
                        'id': fid,
                        'x': int(x_m.group(1)) if x_m else 0,
                        'y': int(y_m.group(1)) if y_m else 0,
                        'rel': rel_m.group(1) if rel_m else None,
                        'prereqs': prereqs,
                        'order': len(focus_list)
                    }
                    focuses[fid] = f_data
                    focus_list.append(f_data)
                pos = i + 1
                break
        i += 1
    else:
        break

print(f"Total focuses parsed: {len(focuses)}")

abs_coords = {}
def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return (0, 0)
    visited.add(fid)
    f = focuses[fid]
    if not f['rel']: return (f['x'], f['y'])
    if f['rel'] not in focuses: return (f['x'], f['y'])
    px, py = get_abs(f['rel'], visited)
    return (px + f['x'], py + f['y'])

for fid in focuses:
    abs_coords[fid] = get_abs(fid)

# Categorize focuses into major branches:
# 1. Chinh tri (Dang & Nha nuoc + Con duong Kien dinh)
# 2. Kinh te (4 Truc cong nghiep, nong nghiep, tai chinh, ...)
# 3. Quan su (VPA: Luc quan, Hai quan, PK-KQ)
# 4. Ngoai giao & ASEAN
# 5. Bien Dong & Luat Bien (SCS)
# 6. Ket cau Ha tang & Giao thong (Infra)
# 7. Khoa hoc so, Cong nghe & Xa hoi (Digital / Sci / Society)
# 8. An ninh Noi dia (VIE_sec_*)

def get_branch(fid):
    if fid.startswith('VIE_sec_'): return "An ninh Nội địa"
    if fid.startswith('VIE_dip_') or fid.startswith('VIE_asean_') or fid in ['VIE_bdf_bamboo_diplomacy']: return "Ngoại giao & ASEAN"
    if fid.startswith('VIE_scs_') or fid.startswith('VIE_maritime_') or fid in ['VIE_law_of_the_sea_2012', 'VIE_fisheries_surveillance_force']: return "Biển Đông & SCS"
    if fid.startswith('VIE_infra_') or fid.startswith('VIE_hwy_') or fid.startswith('VIE_rail_') or fid.startswith('VIE_port_') or fid.startswith('VIE_aviation_') or fid.startswith('VIE_logistics_') or fid.startswith('VIE_energy_') or fid in ['VIE_grid_modernization', 'VIE_north_south_backbone']: return "Hạ tầng & Giao thông"
    if fid.startswith('VIE_sci_') or fid.startswith('VIE_digital_') or fid.startswith('VIE_soc_') or fid in ['VIE_internet_expansion', 'VIE_national_digital_transformation', 'VIE_digital_id', 'VIE_national_data_center', 'VIE_digital_nation', 'VIE_ai_strategy', 'VIE_make_in_vietnam', 'VIE_digital_tech_industry_law', 'VIE_research_universities', 'VIE_nuclear_research', 'VIE_nafosted', 'VIE_science_breakthrough', 'VIE_vinasat', 'VIE_earth_observation', 'VIE_green_growth', 'VIE_carbon_circular_economy', 'VIE_upper_middle_income', 'VIE_high_income_2045', 'VIE_developed_nation_2045', 'VIE_innovation_nation', 'VIE_productivity_leap', 'VIE_ageing_society', 'VIE_mobile_networks', 'VIE_mobile_3g_4g', 'VIE_submarine_cables', 'VIE_domestic_automotive', 'VIE_integrated_auto_supplier_park', 'VIE_ev_revolution_batteries', 'VIE_global_auto_export', 'VIE_viettel_global']: return "Khoa học số & Xã hội"
    if fid.startswith('VIE_lf_') or fid.startswith('VIE_nf_') or fid.startswith('VIE_airf_') or fid.startswith('VIE_apm_') or fid.startswith('VIE_naval_') or fid.startswith('VIE_military_') or fid in ['VIE_modernize_vpa', 'VIE_def_industry_law', 'VIE_ba_son_shipyards', 'VIE_small_combatant_construction', 'VIE_path_self_reliant_deterrence']: return "Quân sự"
    if fid.startswith('VIE_pol_') or fid.startswith('VIE_party_') or fid.startswith('VIE_anti_corruption_') or fid.startswith('VIE_state_') or fid.startswith('VIE_soviet_') or fid.startswith('VIE_marxist_') or fid.startswith('VIE_socialist_') or fid.startswith('VIE_discipline_') or fid.startswith('VIE_personnel_') or fid.startswith('VIE_ideology_') or fid.startswith('VIE_rule_of_law_') or fid.startswith('VIE_vcp_') or fid in ['VIE_doi_moi_continues', 'VIE_socialist_rule_of_law', 'VIE_streamline_the_state', 'VIE_cpv_monopoly_confirmed', 'VIE_anti_corruption_intensified', 'VIE_party_building_cadre_work', 'VIE_discipline_inspection_supervision', 'VIE_centralize_power_general_secretary', 'VIE_collective_leadership_tradition', 'VIE_party_state_cadre_streamlining', 'VIE_anticorruption_furnace', 'VIE_anticorruption_clean_governance', 'VIE_anticorruption_cadre_resignation', 'VIE_anticorruption_institutionalize', 'VIE_personnel_discipline_consolidation', 'VIE_ideological_purity_work', 'VIE_cadre_planning_central_committee', 'VIE_resolutions_on_party_building', 'VIE_power_supervision_mechanism', 'VIE_strengthen_inspection_commission', 'VIE_special_supervision_teams', 'VIE_internal_political_security', 'VIE_anti_degradation_campaign', 'VIE_party_rectification_central_resolution']: return "Chính trị"
    return "Kinh tế"

branches = {}
for fid, f in focuses.items():
    b = get_branch(fid)
    branches.setdefault(b, []).append(fid)

print("\n=== FOCUSES PER BRANCH ===")
for b, fids in branches.items():
    xs = [abs_coords[f][0] for f in fids]
    ys = [abs_coords[f][1] for f in fids]
    print(f"{b:25} | count={len(fids):3d} | x=[{min(xs):3d} .. {max(xs):3d}] (span={max(xs)-min(xs):2d}) | y=[{min(ys):2d} .. {max(ys):2d}]")

# Audit large dx, dy, and row voids in each branch
print("\n=== AUDIT LARGE JUMPS (|dx| >= 6 or dy > 1) ACROSS ALL BRANCHES ===")
for b, fids in branches.items():
    b_jumps = []
    for fid in fids:
        f = focuses[fid]
        dx, dy = f['x'], f['y']
        # If rel is root or doi_moi_continues, large dx might be bridge
        if abs(dx) >= 6 or dy > 1:
            b_jumps.append((fid, f['rel'], dx, dy, abs_coords[fid]))
    print(f"\n--- {b} ({len(b_jumps)} jumps) ---")
    for j in b_jumps:
        print(f"  {j[0]:35} -> rel={str(j[1]):30} | dx={j[2]:3d}, dy={j[3]:2d} | abs={j[4]}")
