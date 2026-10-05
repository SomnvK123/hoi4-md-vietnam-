import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
import tools.test_scs_layout as tsl
import tools.analyze_military as am

compact_scs = {
    # y = 12
    'VIE_law_of_the_sea': {
        'abs': (76, 12), 'rel': 'VIE_doi_moi_continues', 'dx': -4, 'dy': 12,
        'prereqs': [], 'avail': []
    },
    # y = 13 (6 focuses: 70, 72, 74, 76, 80, 84)
    'VIE_legal_warfare': {
        'abs': (70, 13), 'rel': 'VIE_law_of_the_sea', 'dx': -6, 'dy': 1,
        'prereqs': ['VIE_law_of_the_sea'], 'avail': []
    },
    'VIE_assert_maritime_rights': {
        'abs': (72, 13), 'rel': 'VIE_law_of_the_sea', 'dx': -4, 'dy': 1,
        'prereqs': ['VIE_law_of_the_sea'], 'avail': []
    },
    'VIE_fisheries_surveillance': {
        'abs': (74, 13), 'rel': 'VIE_law_of_the_sea', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_law_of_the_sea'], 'avail': []
    },
    'VIE_maritime_militia': {
        'abs': (76, 13), 'rel': 'VIE_law_of_the_sea', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_law_of_the_sea'], 'avail': []
    },
    'VIE_peoples_defence': {
        'abs': (80, 13), 'rel': 'VIE_law_of_the_sea', 'dx': 4, 'dy': 1,
        'prereqs': ['VIE_law_of_the_sea'], 'avail': []
    },
    'VIE_scs_maritime_cooperation': {
        'abs': (84, 13), 'rel': 'VIE_law_of_the_sea', 'dx': 8, 'dy': 1,
        'prereqs': ['VIE_law_of_the_sea'], 'avail': []
    },
    # y = 14 (9 focuses: 70, 72, 74, 76, 78, 80, 82, 84, 86)
    'VIE_limited_war_doctrine': {
        'abs': (70, 14), 'rel': 'VIE_assert_maritime_rights', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_assert_maritime_rights'], 'avail': ['VIE_legal_warfare']
    },
    'VIE_paracel_ultimatum': {
        'abs': (72, 14), 'rel': 'VIE_assert_maritime_rights', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_assert_maritime_rights'], 'avail': []
    },
    'VIE_coast_guard_law': {
        'abs': (74, 14), 'rel': 'VIE_fisheries_surveillance', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_fisheries_surveillance'], 'avail': []
    },
    'VIE_spratly_fortification': {
        'abs': (76, 14), 'rel': 'VIE_maritime_militia', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_maritime_militia'], 'avail': []
    },
    'VIE_provincial_defence_zones': {
        'abs': (78, 14), 'rel': 'VIE_peoples_defence', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_peoples_defence'], 'avail': []
    },
    'VIE_force_47': {
        'abs': (80, 14), 'rel': 'VIE_peoples_defence', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_peoples_defence'], 'avail': []
    },
    'VIE_un_peacekeeping': {
        'abs': (82, 14), 'rel': 'VIE_peoples_defence', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_peoples_defence'], 'avail': []
    },
    'VIE_scs_multilateral_exercise': {
        'abs': (84, 14), 'rel': 'VIE_scs_maritime_cooperation', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_scs_maritime_cooperation'], 'avail': []
    },
    'VIE_scs_cam_ranh_port': {
        'abs': (86, 14), 'rel': 'VIE_scs_maritime_cooperation', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_scs_maritime_cooperation'], 'avail': []
    },
    # y = 15 (6 focuses: 72, 76, 78, 80, 82, 84)
    'VIE_retake_north_spratlys': {
        'abs': (72, 15), 'rel': 'VIE_paracel_ultimatum', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_paracel_ultimatum'], 'avail': []
    },
    'VIE_dk1_platforms': {
        'abs': (76, 15), 'rel': 'VIE_spratly_fortification', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_spratly_fortification'], 'avail': ['VIE_coast_guard_law']
    },
    'VIE_militia_law': {
        'abs': (78, 15), 'rel': 'VIE_provincial_defence_zones', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_provincial_defence_zones'], 'avail': []
    },
    'VIE_cyber_command': {
        'abs': (80, 15), 'rel': 'VIE_force_47', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_force_47'], 'avail': []
    },
    'VIE_four_nos_doctrine': {
        'abs': (82, 15), 'rel': 'VIE_un_peacekeeping', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_un_peacekeeping'], 'avail': []
    },
    'VIE_scs_joint_training': {
        'abs': (84, 15), 'rel': 'VIE_scs_multilateral_exercise', 'dx': 0, 'dy': 1,
        'prereqs': ['VIE_scs_multilateral_exercise'], 'avail': ['VIE_scs_cam_ranh_port']
    },
    # y = 16 (2 focuses: 70, 74)
    'VIE_retake_east_spratlys': {
        'abs': (70, 16), 'rel': 'VIE_retake_north_spratlys', 'dx': -2, 'dy': 1,
        'prereqs': ['VIE_retake_north_spratlys'], 'avail': []
    },
    'VIE_retake_south_spratlys': {
        'abs': (74, 16), 'rel': 'VIE_retake_north_spratlys', 'dx': 2, 'dy': 1,
        'prereqs': ['VIE_retake_north_spratlys'], 'avail': []
    }
}

# Verify internal
abs_map = {}
collisions = []
for fid, d in compact_scs.items():
    pos = d['abs']
    if pos in abs_map:
        collisions.append((fid, abs_map[pos], pos))
    else:
        abs_map[pos] = fid

print(f"Internal collisions: {len(collisions)}")
for c in collisions:
    print("  Collision:", c)

# Verify external collisions
ext_collisions = []
for fid, d in compact_scs.items():
    ax, ay = d['abs']
    for ext_fid, ext_f in am.focuses.items():
        if ext_fid not in compact_scs:
            if (ext_f['abs_x'], ext_f['abs_y']) == (ax, ay):
                ext_collisions.append((fid, ext_fid, (ax, ay)))

print(f"External collisions: {len(ext_collisions)}")
for ec in ext_collisions:
    print("  External collision:", ec)

# Check gaps
rows = {}
for fid, d in compact_scs.items():
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
for fid, d in compact_scs.items():
    if fid == 'VIE_law_of_the_sea': continue
    if abs(d['dx']) >= 6 or d['dy'] > 1:
        jumps.append((fid, d['rel'], d['dx'], d['dy']))

print(f"\nJumps with |dx| >= 6 or dy > 1: {len(jumps)}")
for j in jumps:
    print(f"  {j[0]:32} -> {j[1]:28} | dx={j[2]:3d}, dy={j[3]:2d}")
