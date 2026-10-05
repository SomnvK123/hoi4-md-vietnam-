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
    
    # check available for date or prereqs
    avail_m = re.search(r'available\s*=\s*\{([^}]*)\}', body)
    avail = avail_m.group(1).strip() if avail_m else ""
    date_m = re.search(r'date\s*>\s*([0-9\.]+)', avail)
    date_req = date_m.group(1) if date_m else ""

    foci[fid] = {
        'rel': rel,
        'dx': x,
        'dy': y,
        'prs': all_prs,
        'line': text[:m.start()].count('\n') + 1,
        'date': date_req,
        'body': body
    }

# Compute absolute coordinates
def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited or fid not in foci: return (0, 0)
    visited.add(fid)
    d = foci[fid]
    if not d['rel']:
        return (d['dx'], d['dy'])
    px, py = get_abs(d['rel'], visited)
    return (px + d['dx'], py + d['dy'])

# Let's find all focuses connected to VIE_infrastructure_development
infra_visited = set(['VIE_infrastructure_development'])
changed = True
while changed:
    changed = False
    for fid, d in foci.items():
        if fid in infra_visited: continue
        if d['rel'] in infra_visited or any(p in infra_visited for p in d['prs']):
            infra_visited.add(fid)
            changed = True

print(f"Total focuses connected to VIE_infrastructure_development: {len(infra_visited)}")
for fid in sorted(infra_visited, key=lambda f: foci[f]['line']):
    d = foci[fid]
    ax, ay = get_abs(fid)
    rel_str = f"{d['rel']}({d['dx']},{d['dy']})" if d['rel'] else "ROOT"
    print(f"Line {d['line']:5d} | {fid:38} | abs=({ax:3d},{ay:2d}) | rel={rel_str:35} | pr={str(d['prs']):35} | {d['date']}")

# Also let's check what other focuses exist in the tree that are not in Politics, Economy, Military, Diplomacy, SCS
print("\n=== FOCUSES NOT IN KNOWN SUBTREES ===")
# List all subtrees
subtrees = {
    'VIE_party_central_committee': 'Politics',
    'VIE_doi_moi_continues': 'Economic Root',
    'VIE_asean_integration': 'Diplomacy',
    'VIE_law_of_the_sea': 'SCS',
    'VIE_modernize_vpa': 'Military',
    'VIE_infrastructure_development': 'Infra',
}
