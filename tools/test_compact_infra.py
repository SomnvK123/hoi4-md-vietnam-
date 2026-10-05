import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
import tools.test_infra_layout as til

# Copy existing layout
compact_infra = {}
for fid, d in til.INFRA_LAYOUT.items():
    compact_infra[fid] = {
        'abs': list(d['abs']),
        'rel': d['rel'],
        'dx': d['dx'],
        'dy': d['dy'],
        'prereqs': list(d['prereqs']),
        'avail': list(d['avail'])
    }

# 1. Airport master plan: anchor to VIE_hsr_groundbreaking (82, 5) -> (86, 6) gives dx=+4, dy=1!
compact_infra['VIE_airport_master_plan']['rel'] = 'VIE_hsr_groundbreaking'
compact_infra['VIE_airport_master_plan']['dx'] = 4
compact_infra['VIE_airport_master_plan']['dy'] = 1

# 2. Synchronized infrastructure 2030: move to y=9!
# Parent is VIE_expressway_5000km_2030 (78, 8). If abs is (82, 9), dx=4, dy=1!
compact_infra['VIE_synchronized_infrastructure_2030']['abs'] = [82, 9]
compact_infra['VIE_synchronized_infrastructure_2030']['dx'] = 4
compact_infra['VIE_synchronized_infrastructure_2030']['dy'] = 1

# 3. Compact Aviation row 7:
# airport_master_plan is at (86, 6)
# Children:
# aviation_market_opening: (83, 7) -> dx = -3, or (82, 7) -> dx = -4
# noi_bai_t2: (85, 7) -> dx = -1, or (84, 7) -> dx = -2
# long_thanh_approval: (87, 7) -> dx = 1, or (88, 7) -> dx = 2
# tan_son_nhat_t3: (89, 7) -> dx = 3, or (90, 7) -> dx = 4 (reduced from dx=8!)
compact_infra['VIE_aviation_market_opening']['abs'] = [82, 7]
compact_infra['VIE_aviation_market_opening']['dx'] = -4

compact_infra['VIE_noi_bai_t2']['abs'] = [84, 7]
compact_infra['VIE_noi_bai_t2']['dx'] = -2

compact_infra['VIE_long_thanh_approval']['abs'] = [88, 7]
compact_infra['VIE_long_thanh_approval']['dx'] = 2

compact_infra['VIE_tan_son_nhat_t3']['abs'] = [90, 7]
compact_infra['VIE_tan_son_nhat_t3']['dx'] = 4

# Aviation row 8:
# under aviation_market_opening (82):
# socialized_airports: (80, 8), dx = -2
# acv_monopoly: (84, 8), dx = 2
# under long_thanh_approval (88):
# long_thanh_airport: (88, 8), dx = 0
# under tan_son_nhat_t3 (90):
# dual_use_airports: (90, 8), dx = 0
compact_infra['VIE_socialized_airports']['abs'] = [80, 8]
compact_infra['VIE_socialized_airports']['dx'] = -2

compact_infra['VIE_acv_monopoly']['abs'] = [84, 8]
compact_infra['VIE_acv_monopoly']['dx'] = 2

compact_infra['VIE_long_thanh_airport']['abs'] = [88, 8]
compact_infra['VIE_long_thanh_airport']['dx'] = 0

compact_infra['VIE_dual_use_airports']['abs'] = [90, 8]
compact_infra['VIE_dual_use_airports']['dx'] = 0

# Aviation row 9:
# van_don_airport under socialized_airports (80): (80, 9), dx = 0
# airport_network_2030 under acv_monopoly (84): (84, 9), dx = 0
# synchronized_infrastructure_2030: (86, 9) or (88, 9)
compact_infra['VIE_van_don_airport']['abs'] = [80, 9]
compact_infra['VIE_van_don_airport']['dx'] = 0

compact_infra['VIE_airport_network_2030']['abs'] = [84, 9]
compact_infra['VIE_airport_network_2030']['dx'] = 0

compact_infra['VIE_synchronized_infrastructure_2030']['abs'] = [86, 9]
compact_infra['VIE_synchronized_infrastructure_2030']['dx'] = 8 # from expressway_5000km (78, 8) -> 86 - 78 = 8, dy=1

# 4. Metro jumps:
# reunification_line_upgrade is at (88, 2)
# lao_cai_haiphong_rail: (88, 3), dx = 0 (was 90)
# hcmc_metro: (92, 3), dx = 4 (was 94, dx = 6)
# urban_rail_hanoi: (94, 3), dx = 6 (was 98, dx = 10!)
compact_infra['VIE_lao_cai_haiphong_rail']['abs'] = [88, 3]
compact_infra['VIE_lao_cai_haiphong_rail']['dx'] = 0

compact_infra['VIE_hcmc_metro']['abs'] = [92, 3]
compact_infra['VIE_hcmc_metro']['dx'] = 4

compact_infra['VIE_urban_rail_hanoi']['abs'] = [94, 3]
compact_infra['VIE_urban_rail_hanoi']['dx'] = 6

# Row 4 Metro:
# domestic_rail_industry under lao_cai_haiphong (88): (88, 4), dx = 0 (was 92)
# urban_rail_special_mechanism_nq188 under urban_rail_hanoi (94): (94, 4), dx = 0 (was 96)
compact_infra['VIE_domestic_rail_industry']['abs'] = [88, 4]
compact_infra['VIE_domestic_rail_industry']['dx'] = 0

compact_infra['VIE_urban_rail_special_mechanism_nq188']['abs'] = [94, 4]
compact_infra['VIE_urban_rail_special_mechanism_nq188']['dx'] = 0

# Row 5 Metro:
# metro_network_2035 under urban_rail_special_mechanism (94): (94, 5), dx = 0 (was 96)
compact_infra['VIE_metro_network_2035']['abs'] = [94, 5]
compact_infra['VIE_metro_network_2035']['dx'] = 0

# Check collisions and gaps
abs_map = {}
collisions = []
for fid, d in compact_infra.items():
    pos = tuple(d['abs'])
    if pos in abs_map:
        collisions.append((fid, abs_map[pos], pos))
    else:
        abs_map[pos] = fid

print(f"Internal collisions: {len(collisions)}")
for c in collisions:
    print("  Collision:", c)

rows = {}
for fid, d in compact_infra.items():
    rows.setdefault(d['abs'][1], []).append((d['abs'][0], fid))

gap_violations = []
for y in sorted(rows.keys()):
    items = sorted(rows[y])
    row_str = ", ".join([f"{fid}(x={ax})" for ax, fid in items])
    print(f"y={y:2d} ({len(items):2d}): {row_str}")
    for k in range(len(items)-1):
        if items[k+1][0] - items[k][0] < 2:
            gap_violations.append((items[k][1], items[k+1][1], y, items[k+1][0] - items[k][0]))

print(f"Gap violations: {len(gap_violations)}")

# Check jumps |dx| >= 6 or dy > 1
jumps = []
for fid, d in compact_infra.items():
    if fid == 'VIE_infrastructure_development': continue
    if abs(d['dx']) >= 6 or d['dy'] > 1:
        jumps.append((fid, d['rel'], d['dx'], d['dy']))

print(f"Jumps with |dx| >= 6 or dy > 1: {len(jumps)}")
for j in jumps:
    print(f"  {j[0]:38} -> {j[1]:30} | dx={j[2]:3d}, dy={j[3]:2d}")
