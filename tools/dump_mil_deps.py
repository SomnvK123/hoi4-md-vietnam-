import sys, os, re
sys.path.insert(0, os.path.abspath("."))
from tools.test_military_layout import military_layout

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

print("=== ALL 92 FOCUSES WITH CURRENT POS & REL ===")
for fid in military_layout:
    entry = military_layout[fid]
    pr = foci.get(fid, {}).get('prs', [])
    av = foci.get(fid, {}).get('avail', '')
    ax, ay = abs_coords[fid]
    rel = entry['rel']
    dx, dy = entry['dx'], entry['dy']
    print(f"{fid:35} | abs=({ax:3d},{ay:2d}) | rel={rel:30} | dx={dx:3d}, dy={dy:2d} | pr={str(pr):32} | av={av[:35]}")
