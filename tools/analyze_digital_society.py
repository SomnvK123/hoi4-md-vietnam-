import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

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

    foci[fid] = {
        'rel': rel, 'dx': x, 'dy': y, 'prs': all_prs,
        'line': text[:m.start()].count('\n') + 1,
        'date': date_req, 'avail': avail, 'body': body
    }

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited or fid not in foci: return (0, 0)
    visited.add(fid)
    d = foci[fid]
    if not d['rel']: return (d['dx'], d['dy'])
    px, py = get_abs(d['rel'], visited)
    return (px + d['dx'], py + d['dy'])

# The 6 completed branches:
from test_infra_layout import INFRA_LAYOUT

with open('VIE_military_spine_horizontal_architecture.md', 'r', encoding='utf-8') as f: mil_text = f.read()
mil_fids = set(re.findall(r'`(VIE_[a-zA-Z0-9_]+)`', mil_text))

with open('VIE_economic_spine_horizontal_architecture.md', 'r', encoding='utf-8') as f: eco_text = f.read()
eco_fids = set(re.findall(r'`(VIE_[a-zA-Z0-9_]+)`', eco_text))

with open('Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md', 'r', encoding='utf-8') as f: pol_text = f.read()
pol_fids = set(re.findall(r'`(VIE_[a-zA-Z0-9_]+)`', pol_text))

with open('VIE_diplomacy_spine_horizontal_architecture.md', 'r', encoding='utf-8') as f: dip_text = f.read()
dip_fids = set(re.findall(r'`(VIE_[a-zA-Z0-9_]+)`', dip_text))

with open('VIE_scs_spine_horizontal_architecture.md', 'r', encoding='utf-8') as f: scs_text = f.read()
scs_fids = set(re.findall(r'`(VIE_[a-zA-Z0-9_]+)`', scs_text))

inf_fids = set(INFRA_LAYOUT.keys())

completed = mil_fids | eco_fids | pol_fids | dip_fids | scs_fids | inf_fids
remaining = [f for f in foci if f not in completed]

print(f"Total focuses in file: {len(foci)}")
print(f"Total completed: {len(completed)}")
print(f"Total remaining: {len(remaining)}")

for fid in sorted(remaining, key=lambda f: foci[f]['line']):
    d = foci[fid]
    ax, ay = get_abs(fid)
    rel_str = f"{d['rel']}({d['dx']},{d['dy']})" if d['rel'] else "ROOT"
    print(f"Line {d['line']:5d} | {fid:36} | abs=({ax:3d},{ay:2d}) | rel={rel_str:35} | pr={str(d['prs']):35} | {d['date']}")
