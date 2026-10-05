import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

file_path = "common/national_focus/VIE_md_focus.txt"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Parse all focus blocks
pos = 0
blocks = []
focus_map = {}
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
                block_content = text[start:i+1]
                id_m = re.search(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', block_content, re.MULTILINE)
                if id_m:
                    fid = id_m.group(1)
                    focus_map[fid] = {
                        'id': fid,
                        'start': start,
                        'end': i+1,
                        'block': block_content
                    }
                    blocks.append(fid)
                pos = i + 1
                break
        i += 1
    else:
        break

print(f"Total focus blocks parsed: {len(blocks)}")

# Define the 9 compacting edits
mods = {
    'VIE_fdi_attraction': {
        'x': 0, 'y': 1, 'rel': 'VIE_household_business'
    },
    'VIE_sez_three_zones': {
        'x': 0, 'y': 1, 'rel': 'VIE_cptpp_member'
    },
    'VIE_shared_future': {
        'x': 2, 'y': 1, 'rel': 'VIE_border_trade_gates'
    },
    'VIE_indochina_solidarity': {
        'x': 2, 'y': 1, 'rel': 'VIE_mekong_dams_response'
    },
    'VIE_un_security_council': {
        'x': -2, 'y': 1, 'rel': 'VIE_apec_host'
    },
    'VIE_hl_all_people_defence': {
        'x': -2, 'y': 1, 'rel': 'VIE_hl_army_political_education'
    },
    'VIE_hl_party_defence_industry': {
        'x': 0, 'y': 1, 'rel': 'VIE_hl_army_political_education'
    },
    'VIE_hl_fatherland_front': {
        'x': 0, 'y': 1, 'rel': 'VIE_hl_school_theory'
    },
    'VIE_hl_indochina_union': {
        'x': 1, 'y': 1, 'rel': 'VIE_hl_vientiane_ultimatum'
    },
}

def update_block_coords(block, new_x, new_y, new_rel):
    # replace x
    block = re.sub(r'^\s*x\s*=\s*-?\d+', f'\t\tx = {new_x}', block, flags=re.MULTILINE)
    # replace y
    block = re.sub(r'^\s*y\s*=\s*-?\d+', f'\t\ty = {new_y}', block, flags=re.MULTILINE)
    # replace relative_position_id
    if new_rel:
        if re.search(r'^\s*relative_position_id\s*=', block, flags=re.MULTILINE):
            block = re.sub(r'^\s*relative_position_id\s*=\s*[a-zA-Z0-9_]+', f'\t\trelative_position_id = {new_rel}', block, flags=re.MULTILINE)
        else:
            # add relative_position_id after y
            block = re.sub(r'(^\s*y\s*=\s*-?\d+)', r'\1\n\t\trelative_position_id = ' + new_rel, block, flags=re.MULTILINE)
    return block

# Modify blocks
for fid, m in mods.items():
    if fid in focus_map:
        old_blk = focus_map[fid]['block']
        new_blk = update_block_coords(old_blk, m['x'], m['y'], m['rel'])
        focus_map[fid]['block'] = new_blk
        print(f"Updated {fid}: x={m['x']}, y={m['y']}, rel={m['rel']}")

# Reconstruct file with unified Security block
# Security focus order:
sec_order = [
    'VIE_sec_cyber_control',
    'VIE_sec_surveillance_network',
    'VIE_sec_public_order',
    'VIE_sec_security_economy',
    'VIE_sec_cyber_sovereignty',
    'VIE_sec_loyalty_vetting',
    'VIE_sec_border_control',
    'VIE_sec_managed_opening'
]

sec_header = """	#############################################################
	## AN NINH NOI DIA & KIEM SOAT KHONG GIAN MANG (8 FOCUS)
	## Chuan hoa hang ngang theo mo hinh Chinh tri (Rule 7.3)
	## Root: VIE_sec_cyber_control (abs: 93, 13)
	## Hang 14: surveillance_network (-2), public_order (0), security_economy (+2)
	## Hang 15: cyber_sovereignty (91), loyalty_vetting (93), border_control (95)
	## Hang 16: managed_opening (93)
	#############################################################
"""

# Extract the unified security blocks text
sec_blocks_text = sec_header + "\n\n".join([focus_map[sf]['block'] for sf in sec_order]) + "\n\n"

# In the text, we have:
# Section 1: up to VIE_sec_cyber_control start
# Section 2: between VIE_sec_security_economy end and VIE_sec_public_order start (Science & Tech)
# Section 3: after VIE_sec_managed_opening end

s1_end = focus_map['VIE_sec_cyber_control']['start']
s2_start = focus_map['VIE_sec_security_economy']['end']
s2_end = focus_map['VIE_sec_public_order']['start']
s3_start = focus_map['VIE_sec_managed_opening']['end']

# Let's clean up any comments between s2_end and s3_start
# s2 contains the Science & Tech block
sci_block = text[s2_start:s2_end]
# clean any leftover sec headers in sci_block if any
sci_block = sci_block.strip() + "\n\n"

# Check what precedes s1_end
prefix = text[:s1_end]
# Check what follows s3_start
suffix = text[s3_start:]

# Put security blocks at s1_end, followed by sci_block, then suffix
new_text = prefix + sec_blocks_text + sci_block + suffix

# Also apply the individual mods to new_text for any focuses that were outside security
# Note: focus_map blocks for non-security focuses were modified in focus_map, but let's replace their blocks in new_text
for fid, m in mods.items():
    if not fid.startswith('VIE_sec_'):
        old_orig = text[focus_map[fid]['start']:focus_map[fid]['end']]
        new_blk = focus_map[fid]['block']
        if old_orig in new_text:
            new_text = new_text.replace(old_orig, new_blk, 1)
            print(f"Replaced non-sec block in text: {fid}")
        else:
            print(f"WARNING: old block not found in text for {fid}")

# Write to file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Applied compacting and unified security blocks successfully!")
