import re, sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Check BOM
with open('localisation/english/VIE_md_hardline_l_english.yml', 'rb') as f:
    raw = f.read()

assert raw.startswith(b'\xef\xbb\xbf'), 'BOM missing!'
text = raw.decode('utf-8-sig')

# 2. Check header and syntax
lines = text.splitlines()
assert lines[0].strip() == 'l_english:', f'First line is {lines[0]}'

keys_found = {}
for idx, line in enumerate(lines[1:], 2):
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    m = re.match(r'^([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"$', s)
    if not m:
        print(f'SYNTAX ERROR line {idx}: {s}')
        sys.exit(1)
    k, ver, val = m.group(1), m.group(2), m.group(3)
    # Check inner unescaped quotes
    temp = val.replace('\\"', '')
    if '"' in temp:
        print(f'UNESCAPED QUOTE line {idx}: {s}')
        sys.exit(1)
    keys_found[k] = val

print(f'Syntax check PASSED! Total valid keys: {len(keys_found)}')

# 3. Check hardline focus IDs
focus_ids = [
    'VIE_hl_unity_of_will',
    'VIE_hl_party_rectification',
    'VIE_hl_ideological_foundation',
    'VIE_hl_cadre_centralisation',
    'VIE_hl_state_sector_leading',
    'VIE_hl_key_sectors',
    'VIE_hl_soe_spearhead',
    'VIE_hl_selective_fdi',
    'VIE_hl_no_party_business',
    'VIE_hl_five_year_plan',
    'VIE_hl_party_leads_army',
    'VIE_hl_army_political_education',
    'VIE_hl_all_people_defence',
    'VIE_hl_party_defence_industry',
    'VIE_hl_cyber_ideology',
    'VIE_hl_school_theory',
    'VIE_hl_press_planning',
    'VIE_hl_fatherland_front',
    'VIE_hl_party_diplomacy',
    'VIE_hl_no_dependence',
    'VIE_hl_selective_partners',
    'VIE_hl_term_review',
    'VIE_hl_steadfast_renewal',
    'VIE_hl_party_state_fusion',
    'VIE_hl_handover'
]

print(f'Checking {len(focus_ids)} focuses:')
missing = []
for fid in focus_ids:
    if fid not in keys_found:
        missing.append(fid)
    else:
        print(f'  [OK] {fid} -> {keys_found[fid]}')

if missing:
    print('MISSING FOCUS KEYS:', missing)
else:
    print('ALL 25 FOCUSES ARE FULLY AND CORRECTLY LOCALIZED!')
