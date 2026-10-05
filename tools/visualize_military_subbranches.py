import sys, os
sys.path.insert(0, os.path.abspath("."))
from tools.test_military_layout import military_layout

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return (0, 0)
    visited.add(fid)
    d = military_layout[fid]
    if d['rel'] == 'VIE_doi_moi_continues':
        return (80 + d['dx'], 0 + d['dy'])
    px, py = get_abs(d['rel'], visited)
    return (px + d['dx'], py + d['dy'])

abs_coords = {fid: get_abs(fid) for fid in military_layout}

# Divide by 3 sub-branches:
# 1. Army: starts with VIE_lf_ or VIE_def_industry_law or VIE_military_enterprises_ or VIE_path_self_reliant_deterrence
# 2. Navy: starts with VIE_nf_ or VIE_ba_son_ or VIE_naval_
# 3. Air Force: starts with VIE_airf_ or VIE_apm_

army_fids = [f for f in military_layout if f.startswith('VIE_lf_') or f.startswith('VIE_military_enterprises_') or f in ['VIE_def_industry_law', 'VIE_path_self_reliant_deterrence']]
navy_fids = [f for f in military_layout if f.startswith('VIE_nf_') or f.startswith('VIE_naval_') or f == 'VIE_ba_son_shipyards']
air_fids = [f for f in military_layout if f.startswith('VIE_airf_') or f.startswith('VIE_apm_')]

print(f"Army focuses: {len(army_fids)}")
print(f"Navy focuses: {len(navy_fids)}")
print(f"Air Force focuses: {len(air_fids)}")

def print_subbranch(name, fids):
    print(f"\n=================== {name} ({len(fids)} focuses) ===================")
    rows = {}
    for f in fids:
        x, y = abs_coords[f]
        rows.setdefault(y, []).append((x, f))
    for y in sorted(rows.keys()):
        r = sorted(rows[y])
        f_str = ", ".join([f"{f}({x}, rel={military_layout[f]['rel']}: dx={military_layout[f]['dx']}, dy={military_layout[f]['dy']})" for x, f in r])
        print(f"y={y:2d}: {f_str}")

print_subbranch("ARMY (LUC QUAN)", army_fids)
print_subbranch("NAVY (HAI QUAN)", navy_fids)
print_subbranch("AIR FORCE (PK-KQ & APM)", air_fids)
