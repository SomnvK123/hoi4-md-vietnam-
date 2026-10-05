import re
from pathlib import Path
import sys

txt = Path('common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8')
focuses = {}
for m in re.finditer(r'(?m)^\tfocus\s*=\s*\{', txt):
    start = m.start()
    brace = 1
    for i in range(m.end(), len(txt)):
        if txt[i] == '{': brace += 1
        elif txt[i] == '}':
            brace -= 1
            if brace == 0: end = i + 1; break
    block = txt[start:end]
    fid = re.search(r'\bid\s*=\s*(\S+)', block).group(1)
    xm = re.search(r'\bx\s*=\s*(-?\d+)', block)
    ym = re.search(r'\by\s*=\s*(-?\d+)', block)
    rel = re.search(r'\brelative_position_id\s*=\s*(\S+)', block)
    prereqs = []
    for pm in re.finditer(r'prerequisite\s*=\s*\{([^}]*)\}', block):
        p_fids = re.findall(r'focus\s*=\s*(\S+)', pm.group(1))
        prereqs.append(p_fids)

    focuses[fid] = {
        'id': fid,
        'x': int(xm.group(1)) if xm else 0,
        'y': int(ym.group(1)) if ym else 0,
        'rel': rel.group(1) if rel else None,
        'prereqs': prereqs
    }

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = focuses.get(fid)
    if not f or not f['rel']: return (f['x'], f['y']) if f else (0, 0)
    rx, ry = get_abs(f['rel'], visited)
    return rx + f['x'], ry + f['y']

expected_hardline = {
    # H0
    'VIE_hl_unity_of_will': (14, 12),
    # H1, H2
    'VIE_hl_party_rectification': (14, 13),
    'VIE_hl_ideological_foundation': (10, 13),
    # Row 14 (Pillars start)
    'VIE_hl_cyber_ideology': (6, 14),
    'VIE_hl_state_sector_leading': (10, 14),
    'VIE_hl_cadre_centralisation': (14, 14),
    'VIE_hl_party_leads_army': (18, 14),
    'VIE_hl_party_diplomacy': (22, 14),
    # Row 15
    'VIE_hl_school_theory': (6, 15),
    'VIE_hl_key_sectors': (10, 15),
    'VIE_hl_soe_spearhead': (12, 15),
    'VIE_hl_army_political_education': (18, 15),
    'VIE_hl_no_dependence': (22, 15),
    # Row 16
    'VIE_hl_press_planning': (6, 16),
    'VIE_hl_no_party_business': (8, 16),
    'VIE_hl_selective_fdi': (12, 16),
    'VIE_hl_all_people_defence': (18, 16),
    'VIE_hl_selective_partners': (22, 16),
    # Row 17 (Pillar enders)
    'VIE_hl_five_year_plan': (10, 17),
    'VIE_hl_party_defence_industry': (18, 17),
    # Row 18
    'VIE_hl_fatherland_front': (14, 18),
    # Row 19 (Review)
    'VIE_hl_term_review': (14, 19),
    # Row 20 (Endings)
    'VIE_hl_steadfast_renewal': (10, 20),
    'VIE_hl_party_state_fusion': (14, 20),
    'VIE_hl_handover': (18, 20),
}

expected_spine = {
    'VIE_prepare_congress_9': (14, 1),
    'VIE_resolution_congress_9': (14, 2),
    'VIE_resolution_congress_10': (14, 3),
    'VIE_resolution_congress_11': (14, 4),
    'VIE_resolution_congress_12': (14, 5),
    'VIE_resolution_congress_13': (14, 6),
    'VIE_resolution_congress_14': (14, 7),
    'VIE_era_of_rising': (14, 9),
    'VIE_party_centennial_2030': (14, 10),
}

errors = []
print("--- Checking Hardline Tree Coordinates ---")
for fid, exp in expected_hardline.items():
    if fid not in focuses:
        errors.append(f"Missing focus: {fid}")
        continue
    act = get_abs(fid)
    if act != exp:
        errors.append(f"Coord mismatch for {fid}: expected {exp}, got {act}")
    else:
        print(f"  OK: {fid} -> {act}")

print("--- Checking Congress Spine Coordinates ---")
for fid, exp in expected_spine.items():
    if fid not in focuses:
        errors.append(f"Missing focus: {fid}")
        continue
    act = get_abs(fid)
    if act != exp:
        errors.append(f"Coord mismatch for {fid}: expected {exp}, got {act}")
    else:
        print(f"  OK: {fid} -> {act}")

# Check DAG inside hardline tree
print("--- Checking Hardline Tree DAG Properties ---")
for fid in expected_hardline:
    fx, fy = get_abs(fid)
    f = focuses[fid]
    for pgroup in f['prereqs']:
        for pid in pgroup:
            if pid in expected_hardline:
                px, py = get_abs(pid)
                if py >= fy:
                    errors.append(f"DAG violation: {fid} (Y={fy}) is not strictly below {pid} (Y={py})")

# Check horizontal spacing in Hardline tree
rows = {}
for fid in expected_hardline:
    fx, fy = get_abs(fid)
    rows.setdefault(fy, []).append((fx, fid))

for y, row in sorted(rows.items()):
    row.sort()
    for i in range(len(row) - 1):
        x1, f1 = row[i]
        x2, f2 = row[i+1]
        gap = x2 - x1
        if gap < 2:
            errors.append(f"Spacing violation on Y={y}: {f1} (x={x1}) and {f2} (x={x2}) have gap {gap} < 2")

if errors:
    print(f"\nFAILED with {len(errors)} errors:")
    for err in errors:
        print("  ERROR:", err)
    sys.exit(1)
else:
    print(f"\nPASSED: All {len(expected_hardline)} Hardline focuses and {len(expected_spine)} Congress spine focuses perfectly verified!")
