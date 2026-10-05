import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
import tools.test_scs_layout as tsl

with open("common/national_focus/VIE_md_focus.txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern = re.compile(r'(\tfocus\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_]+)\b.*?\n\t\})', re.DOTALL)
foci = {}
for m in pattern.finditer(text):
    fid = m.group(2)
    body = m.group(1)
    all_prs = []
    for pr_blk in re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', body):
        all_prs.extend(re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pr_blk))
    avail_m = re.search(r'available\s*=\s*\{([^}]*)\}', body)
    avail = avail_m.group(1).strip() if avail_m else ""
    avail = re.sub(r'\s+', ' ', avail)
    foci[fid] = {'prs': all_prs, 'avail': avail}

# In test_scs_layout, how is it defined? Let's check keys
print("Keys in tsl:", [k for k in dir(tsl) if not k.startswith('_')])

# Let's read the 24 SCS focuses from file:
scs_fids = [
    'VIE_law_of_the_sea',
    'VIE_legal_warfare', 'VIE_assert_maritime_rights', 'VIE_fisheries_surveillance', 'VIE_maritime_militia', 'VIE_peoples_defence', 'VIE_scs_maritime_cooperation',
    'VIE_limited_war_doctrine', 'VIE_paracel_ultimatum', 'VIE_coast_guard_law', 'VIE_spratly_fortification', 'VIE_provincial_defence_zones', 'VIE_force_47', 'VIE_un_peacekeeping', 'VIE_scs_multilateral_exercise', 'VIE_scs_cam_ranh_port',
    'VIE_retake_north_spratlys', 'VIE_dk1_platforms', 'VIE_militia_law', 'VIE_cyber_command', 'VIE_four_nos_doctrine', 'VIE_scs_joint_training',
    'VIE_retake_east_spratlys', 'VIE_retake_south_spratlys'
]

print(f"Total SCS focuses to inspect: {len(scs_fids)}")

for fid in scs_fids:
    m = re.search(r'focus\s*=\s*\{\s*id\s*=\s*' + fid + r'\b.*?\n\t\}', text, re.DOTALL)
    if m:
        b = m.group(0)
        x_m = re.search(r'^\s*x\s*=\s*(-?\d+)', b, re.MULTILINE)
        y_m = re.search(r'^\s*y\s*=\s*(-?\d+)', b, re.MULTILINE)
        rel_m = re.search(r'^\s*relative_position_id\s*=\s*([a-zA-Z0-9_]+)', b, re.MULTILINE)
        x = int(x_m.group(1)) if x_m else 0
        y = int(y_m.group(1)) if y_m else 0
        rel = rel_m.group(1) if rel_m else ""
        pr = foci[fid]['prs']
        av = foci[fid]['avail']
        print(f"{fid:32} | x={x:3d}, y={y:2d}, rel={rel:28} | pr={str(pr):35} | av={av[:35]}")
