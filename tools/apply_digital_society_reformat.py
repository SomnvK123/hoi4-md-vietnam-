import re
import sys, os
sys.path.append(os.path.dirname(__file__))
from test_digital_society_layout import DIGITAL_SOCIETY_LAYOUT

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Verify all 27 focuses exist
focus_blocks = {}
pattern = re.compile(r'(\tfocus\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_]+)\b.*?\n\t\})', re.DOTALL)
for m in pattern.finditer(text):
    fid = m.group(2)
    if fid in DIGITAL_SOCIETY_LAYOUT:
        focus_blocks[fid] = m.group(1)

print(f"Total mapped: {len(DIGITAL_SOCIETY_LAYOUT)}, Found in text: {len(focus_blocks)}")
missing = set(DIGITAL_SOCIETY_LAYOUT.keys()) - set(focus_blocks.keys())
if missing:
    print("MISSING IN TEXT:", missing)
    sys.exit(1)

# Generate topological order
in_degree = {}
for fid, cfg in DIGITAL_SOCIETY_LAYOUT.items():
    deps = []
    if cfg['rel'] in DIGITAL_SOCIETY_LAYOUT:
        deps.append(cfg['rel'])
    for p in cfg['prereqs']:
        if p in DIGITAL_SOCIETY_LAYOUT and p not in deps:
            deps.append(p)
    in_degree[fid] = deps

order = []
visited = set()
while len(visited) < len(DIGITAL_SOCIETY_LAYOUT):
    ready = [f for f, deps in in_degree.items() if f not in visited and all(d in visited for d in deps)]
    ready.sort(key=lambda f: (DIGITAL_SOCIETY_LAYOUT[f]['abs'][1], DIGITAL_SOCIETY_LAYOUT[f]['abs'][0]))
    for f in ready:
        visited.add(f)
        order.append(f)
        break

print(f"Topological order: {len(order)} focuses")

def reformat_block(fid):
    block = focus_blocks[fid]
    layout = DIGITAL_SOCIETY_LAYOUT[fid]

    # Extract icon
    icon_m = re.search(r'\bicon\s*=\s*([^\s\n\}]+)', block)
    icon_str = icon_m.group(1) if icon_m else ""

    # Extract cost
    cost_m = re.search(r'\bcost\s*=\s*(\d+)', block)
    cost_str = cost_m.group(1) if cost_m else "10"

    # Extract mutually_exclusive
    me_m = re.search(r'\bmutually_exclusive\s*=\s*\{([^}]+)\}', block)
    me_str = me_m.group(1).strip() if me_m else ""

    # Extract search_filters
    filters_m = re.search(r'\bsearch_filters\s*=\s*\{([^}]+)\}', block)
    filters_str = filters_m.group(1).strip() if filters_m else ""

    # Extract available body
    avail_body = ""
    avail_m = re.search(r'\bavailable\s*=\s*\{', block)
    if avail_m:
        a_start = avail_m.end() - 1
        a_depth = 0
        for j in range(a_start, len(block)):
            if block[j] == '{':
                a_depth += 1
            elif block[j] == '}':
                a_depth -= 1
                if a_depth == 0:
                    avail_body = block[a_start+1:j].strip()
                    break

    # Add required siblings to available
    for req in layout['avail']:
        if "has_completed_focus" in req or "date >" in req:
            if req not in avail_body:
                avail_body = (req + "\n\t\t" + avail_body).strip()
        else:
            sib_line = f"has_completed_focus = {req}"
            if sib_line not in avail_body:
                avail_body = (sib_line + "\n\t\t" + avail_body).strip()

    # Extract completion_reward block
    reward_block = ""
    rew_m = re.search(r'\bcompletion_reward\s*=\s*\{', block)
    if rew_m:
        r_start = rew_m.start()
        r_depth = 0
        for j in range(r_start, len(block)):
            if block[j] == '{':
                r_depth += 1
            elif block[j] == '}':
                r_depth -= 1
                if r_depth == 0:
                    reward_block = block[r_start:j+1].strip()
                    break

    # Extract ai_will_do block
    ai_block = ""
    ai_m = re.search(r'\bai_will_do\s*=\s*\{', block)
    if ai_m:
        ai_start = ai_m.start()
        ai_depth = 0
        for j in range(ai_start, len(block)):
            if block[j] == '{':
                ai_depth += 1
            elif block[j] == '}':
                ai_depth -= 1
                if ai_depth == 0:
                    ai_block = block[ai_start:j+1].strip()
                    break

    # Extract any select_effect, bypass, etc. if present
    extra_blocks = []
    for tag in ['select_effect', 'bypass']:
        tag_m = re.search(r'\b' + tag + r'\s*=\s*\{', block)
        if tag_m:
            t_start = tag_m.start()
            t_depth = 0
            for j in range(t_start, len(block)):
                if block[j] == '{':
                    t_depth += 1
                elif block[j] == '}':
                    t_depth -= 1
                    if t_depth == 0:
                        extra_blocks.append(block[t_start:j+1].strip())
                        break

    # Format new focus block
    lines = ["\tfocus = {", f"\t\tid = {fid}"]
    if icon_str:
        lines.append(f"\t\ticon = {icon_str}")
    lines.append("")
    lines.append(f"\t\tx = {layout['dx']}")
    lines.append(f"\t\ty = {layout['dy']}")
    lines.append(f"\t\trelative_position_id = {layout['rel']}")
    lines.append("")
    if cost_str != "10": # MD convention
        lines.append(f"\t\tcost = {cost_str}")
        lines.append("")
    if layout['prereqs']:
        if len(layout['prereqs']) == 1:
            lines.append(f"\t\tprerequisite = {{ focus = {layout['prereqs'][0]} }}")
        else:
            pr_inner = " ".join([f"focus = {p}" for p in layout['prereqs']])
            lines.append(f"\t\tprerequisite = {{ {pr_inner} }}")
    if me_str:
        lines.append(f"\t\tmutually_exclusive = {{ {me_str} }}")
    if filters_str:
        lines.append(f"\t\tsearch_filters = {{ {filters_str} }}")
    lines.append("")
    if avail_body:
        lines.append("\t\tavailable = {")
        for ab_line in avail_body.splitlines():
            lines.append(f"\t\t\t{ab_line.strip()}")
        lines.append("\t\t}")
        lines.append("")
    for eb in extra_blocks:
        lines.append("\t\t" + eb.replace("\n", "\n\t\t"))
        lines.append("")
    if reward_block:
        lines.append("\t\t" + reward_block.replace("\n", "\n\t\t"))
        lines.append("")
    if ai_block:
        lines.append("\t\t" + ai_block.replace("\n", "\n\t\t"))
    lines.append("\t}")
    return "\n".join(lines)

# Assemble new consolidated code
header = """\t#############################################################
\t## KHOA HOC SO, CONG NGHE & XA HOI 2045 (27 FOCUS)
\t## Chuan hoa hang ngang theo mo hinh Chinh tri (VIE_focus_coding_standards.md 7.3)
\t#############################################################"""

new_blocks = [reformat_block(fid) for fid in order]
consolidated_code = header + "\n\n" + "\n\n".join(new_blocks)
print(f"Generated consolidated code length: {len(consolidated_code)}")

# Find spans in text
spans = []
for fid in DIGITAL_SOCIETY_LAYOUT:
    m = re.search(r'\tfocus\s*=\s*\{\s*id\s*=\s*' + fid + r'\b', text)
    if not m:
        print(f"Failed to find {fid}")
        sys.exit(1)
    start = m.start()
    depth = 0
    end = -1
    for i in range(start, len(text)):
        if text[i] == '{': depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    spans.append((start, end, fid))

spans.sort(key=lambda s: s[0])
print(f"Found {len(spans)} spans in text.")

# Group into clusters
clusters = []
curr = [spans[0]]
for s in spans[1:]:
    if s[0] - curr[-1][1] < 500:
        curr.append(s)
    else:
        clusters.append(curr)
        curr = [s]
clusters.append(curr)

print(f"Found {len(clusters)} clusters:")
for i, c in enumerate(clusters, 1):
    print(f"  Cluster {i}: {len(c)} focuses, from char {c[0][0]} ({c[0][2]}) to {c[-1][1]} ({c[-1][2]})")

# Cluster 1 is VIE_vinasat (single focus at line 11036)
# Cluster 2 is Society (8 focuses at line 11220)
# Cluster 3 is Science/Digital (18 focuses at line 11533)
# We remove Cluster 3, remove Cluster 2, and remove Cluster 1.
# Where do we insert the consolidated block?
# At Cluster 2's position! (Right after VIE_sec_security_economy, before VIE_sec_public_order)
# Or at Cluster 1's position?
# If we insert at Cluster 2:
# We delete Cluster 3 (highest start index first)
# Then replace Cluster 2 with consolidated_code
# Then delete Cluster 1

modified = text
# 1. Delete Cluster 3
c3 = clusters[2]
modified = modified[:c3[0][0]] + modified[c3[-1][1]:]
print("Deleted Cluster 3.")

# 2. Replace Cluster 2 with consolidated_code
c2 = clusters[1]
modified = modified[:c2[0][0]] + consolidated_code + modified[c2[-1][1]:]
print("Replaced Cluster 2 with consolidated code.")

# 3. Delete Cluster 1 (VIE_vinasat)
c1 = clusters[0]
modified = modified[:c1[0][0]] + modified[c1[-1][1]:]
print("Deleted Cluster 1 (VIE_vinasat).")

with open('scratch_new_focus.txt', 'w', encoding='utf-8') as f:
    f.write(modified)

print("Wrote scratch_new_focus.txt.")

# Validation of scratch_new_focus.txt
new_pattern = re.compile(r'\bfocus\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_]+)(.*?)(?=\n\tfocus\s*=\s*\{|\Z)', re.DOTALL)
new_foci = {}
for m in new_pattern.finditer(modified):
    fid = m.group(1)
    body = m.group(2)
    rel_m = re.search(r'relative_position_id\s*=\s*([a-zA-Z0-9_]+)', body)
    rel = rel_m.group(1) if rel_m else None
    x_m = re.search(r'\bx\s*=\s*(-?\d+)', body)
    x = int(x_m.group(1)) if x_m else 0
    y_m = re.search(r'\by\s*=\s*(-?\d+)', body)
    y = int(y_m.group(1)) if y_m else 0
    new_foci[fid] = {'rel': rel, 'dx': x, 'dy': y}

print(f"Total focuses in parsed final file: {len(new_foci)} (expected 410)")

# Check forward references
seen = set()
fwd_refs = []
for fid in new_foci:
    rel = new_foci[fid]['rel']
    if rel and rel not in seen and rel in new_foci:
        fwd_refs.append((fid, rel))
    seen.add(fid)

print(f"Forward references in final file: {len(fwd_refs)}")
if fwd_refs:
    for fr in fwd_refs[:5]:
        print(f"  {fr[0]} references {fr[1]} before definition")

# Check collisions
def get_final_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited or fid not in new_foci: return (0, 0)
    visited.add(fid)
    d = new_foci[fid]
    if not d['rel']: return (d['dx'], d['dy'])
    px, py = get_final_abs(d['rel'], visited)
    return (px + d['dx'], py + d['dy'])

final_coords = {}
for fid in new_foci:
    final_coords[fid] = get_final_abs(fid)

by_c = {}
for fid, c in final_coords.items():
    by_c.setdefault(c, []).append(fid)

coll = {c: fs for c, fs in by_c.items() if len(fs) > 1}
print(f"Collisions in final file: {len(coll)}")
if coll:
    for c, fs in coll.items():
        print(f"  Collision at {c}: {fs}")
