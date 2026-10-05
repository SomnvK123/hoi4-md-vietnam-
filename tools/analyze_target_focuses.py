import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

target_fids = [
    'VIE_vinasat',
    'VIE_sec_cyber_control', 'VIE_sec_surveillance_network', 'VIE_sec_security_economy',
    'VIE_upper_middle_income', 'VIE_green_growth', 'VIE_innovation_nation', 'VIE_carbon_circular_economy',
    'VIE_productivity_leap', 'VIE_ageing_society', 'VIE_high_income_2045', 'VIE_developed_nation_2045',
    'VIE_sci_digital_root', 'VIE_internet_expansion', 'VIE_mobile_3g_4g', 'VIE_mobile_networks',
    'VIE_submarine_cables', 'VIE_national_digital_transformation', 'VIE_ai_strategy', 'VIE_digital_id',
    'VIE_national_data_center', 'VIE_digital_nation', 'VIE_viettel_global', 'VIE_make_in_vietnam',
    'VIE_digital_tech_industry_law', 'VIE_nafosted', 'VIE_research_universities', 'VIE_earth_observation',
    'VIE_nuclear_research', 'VIE_science_breakthrough',
    'VIE_sec_public_order', 'VIE_sec_cyber_sovereignty', 'VIE_sec_loyalty_vetting', 'VIE_sec_border_control',
    'VIE_sec_managed_opening'
]

pattern = re.compile(r'\bfocus\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_]+)(.*?)(?=\n\tfocus\s*=\s*\{|\Z)', re.DOTALL)
foci = {}
for m in pattern.finditer(text):
    fid = m.group(1)
    body = m.group(2)
    rel_m = re.search(r'relative_position_id\s*=\s*([a-zA-Z0-9_]+)', body)
    rel = rel_m.group(1) if rel_m else None
    x_m = re.search(r'\bx\s*=\s*(-?\d+)', body)
    x = int(x_m.group(1)) if x_m else 0
    y_m = re.search(r'\by\s*=\s*(-?\d+)', body)
    y = int(y_m.group(1)) if y_m else 0
    all_prs = []
    for pr_blk in re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', body):
        all_prs.extend(re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pr_blk))
    avail_m = re.search(r'available\s*=\s*\{([^}]*)\}', body)
    avail = avail_m.group(1).strip() if avail_m else ""
    date_m = re.search(r'date\s*>\s*([0-9\.]+)', avail)
    date_req = date_m.group(1) if date_m else ""
    foci[fid] = {'rel': rel, 'dx': x, 'dy': y, 'prs': all_prs, 'date': date_req, 'avail': avail}

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited or fid not in foci: return (0, 0)
    visited.add(fid)
    d = foci[fid]
    if not d['rel']: return (d['dx'], d['dy'])
    px, py = get_abs(d['rel'], visited)
    return (px + d['dx'], py + d['dy'])

print(f"Total target focuses: {len(target_fids)}")

for fid in target_fids:
    d = foci[fid]
    ax, ay = get_abs(fid)
    print(f"{fid:35} | abs=({ax:3d},{ay:2d}) | rel={str(d['rel']):30} | pr={str(d['prs']):35} | date={d['date']}")
