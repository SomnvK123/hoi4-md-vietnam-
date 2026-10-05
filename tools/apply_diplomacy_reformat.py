import sys, os
sys.path.insert(0, os.path.abspath("."))
import re
import tools.test_diplomacy_layout as tdl

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

# Verify all 33 diplomacy focuses are extracted
ordered_fids = [
    # ROOT
    "VIE_asean_integration",

    # TRUC 1: VIET - TRUNG & BIEN GIOI TREN BO (6 focus)
    "VIE_gulf_of_tonkin",
    "VIE_border_settlement",
    "VIE_16_words",
    "VIE_border_trade_gates",
    "VIE_defence_hotline",
    "VIE_shared_future",

    # TRUC 2: LAO, CAMPUCHIA & ME KONG (7 focus)
    "VIE_special_relations_laos",
    "VIE_cambodia_relations",
    "VIE_mekong_commission",
    "VIE_cambodia_border",
    "VIE_mekong_dams_response",
    "VIE_funan_techo_response",
    "VIE_indochina_solidarity",

    # TRUC 3: TRONG TAM ASEAN & DA PHUONG HOA (5 focus)
    "VIE_asean_chair",
    "VIE_code_of_conduct",
    "VIE_apec_host",
    "VIE_un_security_council",
    "VIE_multilateral_champion",

    # TRUC 4: QUAN HE VIET - MY (5 focus)
    "VIE_us_engagement",
    "VIE_us_comprehensive_partnership",
    "VIE_us_embargo_lifted",
    "VIE_us_carrier_visit",
    "VIE_us_tariff_deal",

    # TRUC 5: DOI TAC CHIEN LUOC & NGOAI GIAO CAY TRE (9 focus)
    "VIE_japan_partnership",
    "VIE_korea_partnership",
    "VIE_india_partnership",
    "VIE_australia_partnership",
    "VIE_france_eu",
    "VIE_gulf_investment",
    "VIE_csp_network",
    "VIE_global_south_ties",
    "VIE_bamboo_diplomacy"
]

print(f"Ordered focuses list: {len(ordered_fids)}")
missing = [fid for fid in ordered_fids if fid not in focus_blocks]
if missing:
    print("ERROR missing from file:", missing)
    sys.exit(1)
print("All 33 focuses found in file!")

def reformat_focus(fid):
    start, end, block = focus_blocks[fid]
    layout = tdl.diplomacy_layout[fid]
    
    icon_m = re.search(r'^\s*icon\s*=\s*([^\n]+)', block, re.MULTILINE)
    icon_str = icon_m.group(1).strip() if icon_m else ""
    
    cost_m = re.search(r'^\s*cost\s*=\s*([0-9.]+)', block, re.MULTILINE)
    cost_str = cost_m.group(1).strip() if cost_m else "5"
    
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
\t## NGOAI GIAO & ASEAN - DUONG LOI DOI NGOAI TOAN DIEN (33 FOCUS)
\t## Chuan hoa hang ngang theo mo hinh Chinh tri (VIE_focus_coding_standards.md 7.3)
\t#############################################################""")

# ROOT
out.append(reformat_focus("VIE_asean_integration"))

# TRUC 1
out.append("""\n\t#############################################################
\t## NGOAI GIAO - TRUC 1: QUAN HE VIET - TRUNG & BIEN GIOI TREN BO (6 FOCUS)
\t#############################################################""")
for fid in ordered_fids[1:7]:
    out.append(reformat_focus(fid))

# TRUC 2
out.append("""\n\t#############################################################
\t## NGOAI GIAO - TRUC 2: LAO, CAMPUCHIA & NGUON NUOC ME KONG (7 FOCUS)
\t#############################################################""")
for fid in ordered_fids[7:14]:
    out.append(reformat_focus(fid))

# TRUC 3
out.append("""\n\t#############################################################
\t## NGOAI GIAO - TRUC 3: TRONG TAM ASEAN & DA PHUONG HOA (5 FOCUS)
\t#############################################################""")
for fid in ordered_fids[14:19]:
    out.append(reformat_focus(fid))

# TRUC 4
out.append("""\n\t#############################################################
\t## NGOAI GIAO - TRUC 4: QUAN HE VIET - MY (5 FOCUS)
\t#############################################################""")
for fid in ordered_fids[19:24]:
    out.append(reformat_focus(fid))

# TRUC 5
out.append("""\n\t#############################################################
\t## NGOAI GIAO - TRUC 5: DOI TAC CHIEN LUOC & NGOAI GIAO CAY TRE (9 FOCUS)
\t#############################################################""")
for fid in ordered_fids[24:]:
    out.append(reformat_focus(fid))

full_diplomacy_section = "\n\n".join(out)
print(f"Generated consolidated diplomacy code: {len(full_diplomacy_section)} characters.")

# Now, we need to remove the other 31 focuses from their scattered locations,
# and replace Cluster 1 (VIE_asean_integration and VIE_border_settlement) with full_diplomacy_section.
# Spans of focuses to remove (excluding VIE_asean_integration and VIE_border_settlement which get replaced at Cluster 1)
spans_to_remove = []
for fid in ordered_fids:
    if fid not in ["VIE_asean_integration", "VIE_border_settlement"]:
        s, e, _ = focus_blocks[fid]
        # Include leading comments or empty lines if immediately preceding
        # Find newline before start
        line_start = text.rfind('\n', 0, s)
        if line_start != -1:
            s = line_start
        spans_to_remove.append((s, e, fid))

# Sort spans_to_remove descending by start pos
spans_to_remove.sort(key=lambda x: x[0], reverse=True)

# Replace other occurrences from bottom to top
modified_text = text
for s, e, fid in spans_to_remove:
    # Ensure we don't leave syntax errors
    modified_text = modified_text[:s] + modified_text[e:]

# Now replace Cluster 1
# Cluster 1 starts around line 5240 before VIE_asean_integration and ends after VIE_border_settlement
c1_header = modified_text.find("## CHINH TRI\n\t###############################\n\n\t## v6-fix: anchor moved above its dependents")
if c1_header == -1:
    c1_header = modified_text.find("id = VIE_asean_integration")
    c1_header = modified_text.rfind("###############################", 0, c1_header)

bs_m = re.search(r'\bfocus\s*=\s*\{\s*id\s*=\s*VIE_border_settlement\b', modified_text)
bs_start = bs_m.start()
bs_depth = 0
bs_end = bs_start
for k in range(bs_start, len(modified_text)):
    if modified_text[k] == '{':
        bs_depth += 1
    elif modified_text[k] == '}':
        bs_depth -= 1
        if bs_depth == 0:
            bs_end = k + 1
            break

c1_start = c1_header
c1_end = bs_end

print("Cluster 1 start char:", c1_start, "end char:", c1_end)
print("Before Cluster 1:", modified_text[c1_start-100:c1_start])
print("After Cluster 1:", modified_text[c1_end:c1_end+150])

final_text = modified_text[:c1_start] + full_diplomacy_section + modified_text[c1_end:]

print(f"Old file: {len(text)}, Final file: {len(final_text)}")

with open("scratch_new_focus.txt", "w", encoding="utf-8") as f:
    f.write(final_text)

print("Wrote scratch_new_focus.txt for testing.")

# Validate scratch_new_focus.txt
pos = 0
parsed_focuses = {}
parsed_list = []
while True:
    m = re.search(r'\bfocus\s*=\s*\{', final_text[pos:])
    if not m:
        break
    start = pos + m.start()
    depth = 0
    i = pos + m.end() - 1
    while i < len(final_text):
        if final_text[i] == '{':
            depth += 1
        elif final_text[i] == '}':
            depth -= 1
            if depth == 0:
                block = final_text[start:i+1]
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

print(f"Total focuses in parsed final file: {len(parsed_list)} (expected 410)")

# Check forward references
fwd_refs = []
for f in parsed_list:
    if f['rel']:
        if f['rel'] not in parsed_focuses:
            fwd_refs.append(f"{f['id']} references unknown {f['rel']}")
        elif parsed_focuses[f['rel']]['order'] >= f['order']:
            fwd_refs.append(f"{f['id']} references future {f['rel']}")

print(f"Forward references in final file: {len(fwd_refs)}")
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

print(f"Collisions in final file: {len(collisions)}")
for c in collisions:
    print("  ", c)
