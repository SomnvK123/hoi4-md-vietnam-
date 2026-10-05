import sys, os
sys.path.insert(0, os.path.abspath("."))
import re
import tools.test_military_layout as tml
import tools.verify_military_order as vmo

with open("common/national_focus/VIE_md_focus.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Parse all focus blocks in text
focus_blocks = {}
pos = 0
while True:
    m = re.search(r'\bfocus\s*=\s*\{', text[pos:])
    if not m:
        break
    start = pos + m.start()
    depth = 0
    i = pos + m.end() - 1
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                block = text[start:i+1]
                id_m = re.search(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', block, re.MULTILINE)
                if id_m:
                    fid = id_m.group(1)
                    focus_blocks[fid] = (start, i+1, block)
                pos = i + 1
                break
        i += 1
    else:
        break

print(f"Total focus blocks parsed: {len(focus_blocks)}")

# Verify all 92 military focuses are extracted
missing = [fid for fid in vmo.ordered_fids if fid not in focus_blocks]
if missing:
    print("ERROR: missing focuses from file:", missing)
    sys.exit(1)
print("All 92 military focuses found!")

def reformat_focus(fid):
    start, end, block = focus_blocks[fid]
    layout = tml.military_layout[fid]
    
    # Extract properties
    icon_m = re.search(r'^\s*icon\s*=\s*([^\n]+)', block, re.MULTILINE)
    icon_str = icon_m.group(1).strip() if icon_m else ""
    
    cost_m = re.search(r'^\s*cost\s*=\s*([0-9.]+)', block, re.MULTILINE)
    cost_str = cost_m.group(1).strip() if cost_m else "7"
    
    filters_m = re.search(r'search_filters\s*=\s*\{([^}]+)\}', block)
    filters_str = filters_m.group(1).strip() if filters_m else ""
    
    me_m = re.search(r'mutually_exclusive\s*=\s*\{([^}]+)\}', block)
    me_str = me_m.group(1).strip() if me_m else ""

    # Extract available block body
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
    siblings_to_add = []
    for sib in layout['avail']:
        if f"has_completed_focus = {sib}" not in avail_body:
            siblings_to_add.append(sib)

    if siblings_to_add:
        sib_lines = "\n\t\t".join([f"has_completed_focus = {sib}" for sib in siblings_to_add])
        if avail_body:
            avail_body = sib_lines + "\n\t\t" + avail_body
        else:
            avail_body = sib_lines

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
        for p in layout['prereqs']:
            lines.append(f"\t\tprerequisite = {{ focus = {p} }}")
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

# Assemble output
out = []
out.append("""\t#############################################################
\t## QUAN SU - HIEN DAI HOA QUAN DOI NHAN DAN VIET NAM (92 FOCUS)
\t## Chuan hoa hang ngang theo mo hinh Chinh tri (VIE_focus_coding_standards.md 7.3)
\t#############################################################""")

# ROOT
out.append(reformat_focus("VIE_modernize_vpa"))

# TRUC 1
out.append("""\n\t#############################################################
\t## QUAN SU - TRUC 1: LUC QUAN NHAN DAN & CNQP LUC QUAN (34 FOCUS)
\t#############################################################""")
for fid in vmo.ordered_fids:
    if fid != "VIE_modernize_vpa" and fid in vmo.ordered_fids[1:35]:
        out.append(reformat_focus(fid))

# TRUC 2
out.append("""\n\t#############################################################
\t## QUAN SU - TRUC 2: HAI QUAN NHAN DAN & DONG TAU BA SON (28 FOCUS)
\t#############################################################""")
for fid in vmo.ordered_fids[35:63]:
    out.append(reformat_focus(fid))

# TRUC 3
out.append("""\n\t#############################################################
\t## QUAN SU - TRUC 3: PHONG KHONG - KHONG QUAN & APM (29 FOCUS)
\t#############################################################""")
for fid in vmo.ordered_fids[63:]:
    out.append(reformat_focus(fid))

full_military_section = "\n\n".join(out)
print(f"Generated consolidated military code: {len(full_military_section)} characters.")

# Let's test the boundaries for replacement in VIE_md_focus.txt
# Block 1 starts at "## QUAN SU" around line 6178
b1_header = text.find("## QUAN SU\n\t###############################\n\tfocus = {\n\t\tid = VIE_modernize_vpa")
if b1_header == -1:
    b1_header = text.find("id = VIE_modernize_vpa")
    # find line start of preceding comment
    b1_header = text.rfind("###############################", 0, b1_header)

print("Block 1 start at char:", b1_header)

# Block 1 ends after VIE_nf_carrier_group
carrier_block = focus_blocks["VIE_nf_carrier_group"]
b1_end = carrier_block[1]
print("Block 1 end at char:", b1_end)
print("After Block 1:", text[b1_end:b1_end+150])

# Block 2 starts at "## TRUC 3 - XAY DUNG LUC LUONG LUC QUAN" around line 10190
b2_header = text.find("## TRUC 3 - XAY DUNG LUC LUONG LUC QUAN")
if b2_header == -1:
    b2_header = text.find("id = VIE_lf_army_reform")
    b2_header = text.rfind("###############################", 0, b2_header)
print("Block 2 start at char:", b2_header)

# Block 2 ends after VIE_airf_teaming
teaming_block = focus_blocks["VIE_airf_teaming"]
b2_end = teaming_block[1]
print("Block 2 end at char:", b2_end)
print("After Block 2:", text[b2_end:b2_end+150])

# Perform replacement in memory and validate
new_text = text[:b2_header] + text[b2_end:] # remove Block 2 first (from high index to low)
new_text = new_text[:b1_header] + full_military_section + new_text[b1_end:]

print(f"Old file length: {len(text)}, New file length: {len(new_text)}")

with open("scratch_new_focus.txt", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Wrote scratch_new_focus.txt for testing.")

# Validate scratch_new_focus.txt
pos = 0
parsed_focuses = {}
parsed_list = []
while True:
    m = re.search(r'\bfocus\s*=\s*\{', new_text[pos:])
    if not m:
        break
    start = pos + m.start()
    depth = 0
    i = pos + m.end() - 1
    while i < len(new_text):
        if new_text[i] == '{':
            depth += 1
        elif new_text[i] == '}':
            depth -= 1
            if depth == 0:
                block = new_text[start:i+1]
                id_m = re.search(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', block, re.MULTILINE)
                x_m = re.search(r'^\s*x\s*=\s*(-?\d+)', block, re.MULTILINE)
                y_m = re.search(r'^\s*y\s*=\s*(-?\d+)', block, re.MULTILINE)
                rel_m = re.search(r'^\s*relative_position_id\s*=\s*([a-zA-Z0-9_]+)', block, re.MULTILINE)
                prereqs = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_]+)\s*\}', block)
                if id_m:
                    fid = id_m.group(1)
                    f_data = {
                        'id': fid,
                        'x': int(x_m.group(1)) if x_m else 0,
                        'y': int(y_m.group(1)) if y_m else 0,
                        'rel': rel_m.group(1) if rel_m else None,
                        'prereqs': prereqs,
                        'order': len(parsed_list)
                    }
                    parsed_focuses[fid] = f_data
                    parsed_list.append(f_data)
                pos = i + 1
                break
        i += 1
    else:
        break

print(f"Total focuses in new file: {len(parsed_list)} (expected 410)")

# Check forward references
fwd_refs = []
for f in parsed_list:
    if f['rel']:
        if f['rel'] not in parsed_focuses:
            fwd_refs.append(f"{f['id']} references unknown {f['rel']}")
        elif parsed_focuses[f['rel']]['order'] >= f['order']:
            fwd_refs.append(f"{f['id']} references future {f['rel']}")

print(f"Forward references in new file: {len(fwd_refs)}")
for fr in fwd_refs:
    print("  ", fr)

# Check collisions
def get_abs_coord(fid, visited=None):
    if visited is None:
        visited = set()
    if fid in visited:
        return (0, 0)
    visited.add(fid)
    f = parsed_focuses[fid]
    if not f['rel']:
        return (f['x'], f['y'])
    px, py = get_abs_coord(f['rel'], visited)
    return (px + f['x'], py + f['y'])

coord_map = {}
collisions = []
for f in parsed_list:
    pos_abs = get_abs_coord(f['id'])
    if pos_abs in coord_map:
        collisions.append((f['id'], coord_map[pos_abs], pos_abs))
    else:
        coord_map[pos_abs] = f['id']

print(f"Collisions in new file: {len(collisions)}")
for c in collisions:
    print("  ", c)

