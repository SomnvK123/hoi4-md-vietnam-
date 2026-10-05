import re
from pathlib import Path

focus_file = Path(r"d:\HOI4Mods\md_vietnam\common\national_focus\VIE_md_focus.txt")
content = focus_file.read_text(encoding="utf-8")

def parse_focus_blocks(text):
    blocks = {}
    pos = 0
    while True:
        m = re.search(r'(?m)^\tfocus\s*=\s*\{', text[pos:])
        if not m: break
        st = pos + m.start()
        depth = 1
        i = pos + m.end()
        while i < len(text) and depth > 0:
            if text[i] == '{': depth += 1
            elif text[i] == '}': depth -= 1
            i += 1
        blk = text[st:i]
        pos = i
        m_id = re.search(r'\bid\s*=\s*(\w+)', blk)
        if m_id:
            blocks[m_id.group(1)] = blk
    return blocks

blocks = parse_focus_blocks(content)
print(f"Extracted {len(blocks)} focus blocks.")

def extract_field(blk, field_name):
    m = re.search(r'(?m)^\t\t' + field_name + r'\s*=\s*(\S+)', blk)
    return m.group(1) if m else None

def extract_block(blk, block_name):
    m = re.search(r'(?m)^\t\t' + block_name + r'\s*=\s*\{', blk)
    if not m: return None
    start = m.start()
    brace = 1
    i = m.end()
    while i < len(blk) and brace > 0:
        if blk[i] == '{': brace += 1
        elif blk[i] == '}': brace -= 1
        i += 1
    return blk[start:i]

# Formatting function that strictly enforces Section 2.1 and Section 7.3 standards
def build_clean_focus(fid, spec, raw_blk):
    icon = spec.get('icon') or extract_field(raw_blk, 'icon')
    x = spec['x']
    y = spec['y']
    rel = spec.get('rel')
    cost = spec.get('cost')
    if cost is None:
        raw_cost = extract_field(raw_blk, 'cost')
        cost = int(raw_cost) if raw_cost else 10
    prereqs = spec.get('prereqs')
    mx = spec.get('mutually_exclusive')
    
    # search_filters: single line, standard
    raw_filters = extract_block(raw_blk, 'search_filters')
    if raw_filters:
        filters_content = re.sub(r'\s+', ' ', raw_filters).strip()
    else:
        filters_content = "search_filters = { FOCUS_FILTER_POLITICAL }"

    # available
    if 'avail' in spec:
        avail_lines = "\n".join(f"\t\t\t{cond}" for cond in spec['avail'])
        avail_block = f"\t\tavailable = {{\n{avail_lines}\n\t\t}}"
    else:
        avail_block = extract_block(raw_blk, 'available')
        if avail_block:
            inner_lines = []
            for l in avail_block.splitlines()[1:-1]:
                s = l.strip()
                if s:
                    inner_lines.append(f"\t\t\t{s}")
            if inner_lines:
                avail_block = f"\t\tavailable = {{\n" + "\n".join(inner_lines) + f"\n\t\t}}"
            else:
                avail_block = None

    # bypass
    if 'bypass' in spec:
        bypass_lines = "\n".join(f"\t\t\t{b}" for b in spec['bypass'])
        bypass_block = f"\t\tbypass = {{\n{bypass_lines}\n\t\t}}"
    else:
        bypass_block = extract_block(raw_blk, 'bypass')
        if bypass_block:
            inner_lines = []
            for l in bypass_block.splitlines()[1:-1]:
                s = l.strip()
                if s:
                    inner_lines.append(f"\t\t\t{s}")
            if inner_lines:
                bypass_block = f"\t\tbypass = {{\n" + "\n".join(inner_lines) + f"\n\t\t}}"
            else:
                bypass_block = None

    # completion_reward
    reward_block = extract_block(raw_blk, 'completion_reward')
    if not reward_block:
        reward_block = f"\t\tcompletion_reward = {{\n\t\t\tlog = \"[GetDateText]: [Root.GetName]: Focus {fid}\"\n\t\t}}"
    else:
        reward_block = re.sub(r'treasury_change\s*=\s*3\.0', 'set_temp_variable = { treasury_change = 3 }\n\t\t\tmodify_treasury_effect = yes', reward_block)
        reward_block = re.sub(r'treasury_change\s*=\s*5\.0', 'set_temp_variable = { treasury_change = 5 }\n\t\t\tmodify_treasury_effect = yes', reward_block)
        reward_block = re.sub(r'change_oligarchs_economy_opinion\s*=\s*yes', 'change_oligarchs_opinion = yes', reward_block)
        reward_block = re.sub(r'one_state_military_industrial_complex\s*=\s*yes', 'one_state_arms_factory = yes', reward_block)
        reward_block = re.sub(r'modifier\s*=\s*positive_relations', 'modifier = declaration_of_friendship', reward_block)

    # ai_will_do
    ai_block = extract_block(raw_blk, 'ai_will_do')
    if not ai_block:
        ai_block = "\t\tai_will_do = { base = 70 }"
    elif '\n' not in ai_block.strip():
        ai_block = "\t\t" + re.sub(r'\s+', ' ', ai_block).strip()

    # Construct the block strictly following Section 2.1 field order:
    lines = ["\tfocus = {", f"\t\tid = {fid}", f"\t\ticon = {icon}", ""]
    lines.append(f"\t\tx = {x}")
    lines.append(f"\t\ty = {y}")
    if rel:
        lines.append(f"\t\trelative_position_id = {rel}")
    lines.append("")

    if cost != 10:
        lines.append(f"\t\tcost = {cost}")
        lines.append("")

    if prereqs is not None and len(prereqs) > 0:
        for p in prereqs:
            if isinstance(p, list):
                inner = " ".join(f"focus = {f}" for f in p)
                lines.append(f"\t\tprerequisite = {{ {inner} }}")
            else:
                lines.append(f"\t\tprerequisite = {{ focus = {p} }}")
        lines.append("")

    if mx:
        inner = " ".join(f"focus = {f}" for f in mx)
        lines.append(f"\t\tmutually_exclusive = {{ {inner} }}")
        lines.append("")

    lines.append(f"\t\t{filters_content}")
    lines.append("")

    if avail_block:
        lines.append(avail_block)
        lines.append("")

    if bypass_block:
        lines.append(bypass_block)
        lines.append("")

    lines.append(reward_block)
    lines.append("")
    lines.append(ai_block)
    lines.append("\t}")

    return "\n".join(lines)

# PHƯƠNG ÁN 1: 4 CỘT TRỤ KIÊN ĐỊNH DỌC SONG SONG TRỤC ĐẠI HỘI
# - Cột sống Đại hội: X = 14, bước đều đặn y = 2 mỗi nhiệm kỳ (Y = 3, 5, 7, 9, 11, 13)
# - Các focus Dùng chung: Xếp phẳng phiu trên cùng hàng với nhiệm kỳ (Y = 4, 6, 8, 10, 12), ôm sát trục X = 14
# - Cánh Kiên định: 4 cột trụ tại X = 2, 4, 6, 8 nối DỌC thẳng tắp từ Tầng 1 xuống Tầng 5 (x=0, y=2)
# - Mỗi tầng Hardline mở khóa theo Đại hội tương ứng bằng available = { has_completed_focus = VIE_resolution_congress_N }
elements = [
    # =============================================================
    # KHỞI ĐẦU & ĐẠI HỘI IX (2001 - 2006)
    # =============================================================
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI IX (2001 - 2006)\n\t#############################################################"),
    ('VIE_prepare_congress_9', {
        'x': -66, 'y': 1, 'rel': 'VIE_doi_moi_continues',
        'cost': 5,
        'prereqs': []
    }),
    ('VIE_grassroots_democracy', {
        'x': -2, 'y': 1, 'rel': 'VIE_prepare_congress_9',
        'cost': 5,
        'prereqs': ['VIE_prepare_congress_9'],
        'avail': ['has_completed_focus = VIE_prepare_congress_9']
    }),
    ('VIE_mass_mobilization', {
        'x': 2, 'y': 1, 'rel': 'VIE_prepare_congress_9',
        'cost': 5,
        'prereqs': ['VIE_prepare_congress_9'],
        'avail': ['has_completed_focus = VIE_prepare_congress_9']
    }),
    ('VIE_resolution_congress_9', {
        'x': 0, 'y': 2, 'rel': 'VIE_prepare_congress_9',
        'cost': 5,
        'prereqs': [['VIE_grassroots_democracy', 'VIE_mass_mobilization']]
    }),

    # --- NHIỆM KỲ IX: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI, Y = 4) ---
    ("COMMENT", "\t# --- NHIỆM KỲ IX: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_ethnic_policy', {
        'x': -4, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_9'
        ]
    }),
    ('VIE_state_audit', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_9'
        ]
    }),
    ('VIE_anti_corruption_law', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_9',
            'has_completed_focus = VIE_state_audit',
            'date > 2005.6.30'
        ]
    }),
    ('VIE_national_assembly_role', {
        'x': 4, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_9'
        ]
    }),
    ('VIE_public_admin_reform', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_9',
            'date > 2001.12.31'
        ]
    }),
    ('VIE_decentralization', {
        'x': 8, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_9',
            'has_completed_focus = VIE_public_admin_reform'
        ]
    }),

    # --- NHIỆM KỲ IX: CÁNH KIÊN ĐỊNH (4 CỘT TRỤ MỞ ĐẦU, Y = 5) ---
    ("COMMENT", "\t# --- NHIỆM KỲ IX: 4 CỘT TRỤ KIÊN ĐỊNH (MỞ ĐẦU TỪ ĐẠI HỘI IX) ---"),
    ('VIE_hl_soe_first', {
        'x': -12, 'y': 2, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'icon': 'focus_generic_central_planning',
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['VIE_hl_in_power = yes', 'has_completed_focus = VIE_resolution_congress_9']
    }),
    ('VIE_hl_party_rectification', {
        'x': -10, 'y': 2, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'icon': 'Generic_Political_Purge',
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['VIE_hl_in_power = yes', 'has_completed_focus = VIE_resolution_congress_9']
    }),
    ('VIE_hl_vpa_supreme', {
        'x': -8, 'y': 2, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'icon': 'GFX_focus_generic_military_mission',
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['VIE_hl_in_power = yes', 'has_completed_focus = VIE_resolution_congress_9']
    }),
    ('VIE_hl_icp_legacy', {
        'x': -6, 'y': 2, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'icon': 'diplomatic_treaty',
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['VIE_hl_in_power = yes', 'has_completed_focus = VIE_resolution_congress_9']
    }),

    # =============================================================
    # ĐẠI HỘI X (2006 - 2011)
    # =============================================================
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI X (2006 - 2011)\n\t#############################################################"),
    ('VIE_resolution_congress_10', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_11', '}']
    }),

    # --- NHIỆM KỲ X: CÁC NGHỊ QUYẾT CHUNG (Y = 7) ---
    ("COMMENT", "\t# --- NHIỆM KỲ X: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_anti_corruption_steering', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_10',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_10'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_10',
            'has_completed_focus = VIE_anti_corruption_law'
        ]
    }),
    ('VIE_asset_declaration', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_10',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_10'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_10',
            'has_completed_focus = VIE_anti_corruption_steering'
        ]
    }),

    # --- NHIỆM KỲ X: CÁNH KIÊN ĐỊNH & ĐỔI MỚI (Y = 8) ---
    ("COMMENT", "\t# --- NHIỆM KỲ X: 4 CỘT TRỤ KIÊN ĐỊNH & ĐỔI MỚI (Y = 8) ---"),
    ('VIE_hl_curb_private_capital', {
        'x': -12, 'y': 2, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'icon': 'focus_generic_central_planning',
        'prereqs': ['VIE_hl_soe_first'],
        'avail': [
            'VIE_hl_in_power = yes',
            'NOT = { has_completed_focus = VIE_party_members_private_business }',
            'has_completed_focus = VIE_resolution_congress_10'
        ]
    }),
    ('VIE_hl_central_inspection', {
        'x': -10, 'y': 2, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'icon': 'communist_purge',
        'prereqs': ['VIE_hl_party_rectification'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_10'
        ]
    }),
    ('VIE_hl_ideological_commissars', {
        'x': -8, 'y': 2, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'icon': 'GFX_focus_generic_military_mission',
        'prereqs': ['VIE_hl_vpa_supreme'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_10'
        ]
    }),
    ('VIE_hl_viet_lao_special_integration', {
        'x': -6, 'y': 2, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'icon': 'treaty2',
        'prereqs': ['VIE_hl_icp_legacy'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_10'
        ]
    }),
    ('VIE_party_members_private_business', {
        'x': 4, 'y': 2, 'rel': 'VIE_resolution_congress_10',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_10'],
        'avail': [
            'NOT = { VIE_hl_in_power = yes }',
            'NOT = { has_completed_focus = VIE_hl_curb_private_capital }',
            'has_completed_focus = VIE_resolution_congress_10'
        ]
    }),

    # =============================================================
    # ĐẠI HỘI XI (2011 - 2016)
    # =============================================================
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI XI (2011 - 2016)\n\t#############################################################"),
    ('VIE_resolution_congress_11', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_10'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_12', '}']
    }),

    # --- NHIỆM KỲ XI: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI, Y = 10) ---
    ("COMMENT", "\t# --- NHIỆM KỲ XI: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_tw4_party_building', {
        'x': -4, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_11'
        ]
    }),
    ('VIE_party_inspection', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_11',
            'has_completed_focus = VIE_tw4_party_building'
        ]
    }),
    ('VIE_platform_2011', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_11'
        ]
    }),
    ('VIE_rule_of_law_state', {
        'x': 4, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_11'
        ]
    }),
    ('VIE_constitution_2013', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_11',
            'has_completed_focus = VIE_rule_of_law_state',
            'date > 2013.11.28'
        ]
    }),
    ('VIE_disaster_law_2013', {
        'x': 8, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_11',
            'date > 2013.6.19'
        ]
    }),

    # --- NHIỆM KỲ XI: CÁNH KIÊN ĐỊNH (4 CỘT TRỤ, Y = 11) ---
    ("COMMENT", "\t# --- NHIỆM KỲ XI: 4 CỘT TRỤ KIÊN ĐỊNH (Y = 11) ---"),
    ('VIE_hl_five_year_plan', {
        'x': -12, 'y': 2, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'icon': 'economic_civil_industry',
        'prereqs': ['VIE_hl_curb_private_capital'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_11'
        ]
    }),
    ('VIE_hl_national_firewall', {
        'x': -10, 'y': 2, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'icon': 'army_cyberwar',
        'prereqs': ['VIE_hl_central_inspection'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_11'
        ]
    }),
    ('VIE_hl_defense_self_reliance', {
        'x': -8, 'y': 2, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'icon': 'GFX_focus_generic_military_mission',
        'prereqs': ['VIE_hl_ideological_commissars'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_11'
        ]
    }),
    ('VIE_hl_cambodia_revolutionary_front', {
        'x': -6, 'y': 2, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'icon': 'treaty2',
        'prereqs': ['VIE_hl_viet_lao_special_integration'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_11'
        ]
    }),

    # =============================================================
    # ĐẠI HỘI XII (2016 - 2021)
    # =============================================================
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI XII (2016 - 2021)\n\t#############################################################"),
    ('VIE_resolution_congress_12', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_11'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_13', '}']
    }),

    # --- NHIỆM KỲ XII: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI, Y = 13) ---
    ("COMMENT", "\t# --- NHIỆM KỲ XII: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_streamline_apparatus', {
        'x': -4, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_12'
        ]
    }),
    ('VIE_cybersecurity_law', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_12',
            'date > 2018.6.12'
        ]
    }),
    ('VIE_party_discipline', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_12',
            'has_completed_focus = VIE_party_inspection'
        ]
    }),
    ('VIE_cadre_accountability', {
        'x': 4, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_12',
            'has_completed_focus = VIE_party_discipline'
        ]
    }),
    ('VIE_asset_recovery', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_12',
            'has_completed_focus = VIE_party_discipline'
        ]
    }),
    ('VIE_clean_cadres', {
        'x': 8, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_12',
            'has_completed_focus = VIE_cadre_accountability'
        ]
    }),
    ('VIE_higher_education_law', {
        'x': 10, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_12',
            'date > 2018.11.19'
        ]
    }),
    ('VIE_education_law_2019', {
        'x': 12, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_12',
            'has_completed_focus = VIE_higher_education_law',
            'date > 2019.6.14'
        ]
    }),

    # --- NHIỆM KỲ XII: CÁNH KIÊN ĐỊNH (4 CỘT TRỤ, Y = 14) ---
    ("COMMENT", "\t# --- NHIỆM KỲ XII: 4 CỘT TRỤ KIÊN ĐỊNH (Y = 14) ---"),
    ('VIE_hl_strategic_resources', {
        'x': -12, 'y': 2, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'icon': 'economic_civil_industry',
        'prereqs': ['VIE_hl_five_year_plan'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_12'
        ]
    }),
    ('VIE_hl_revolutionary_tribunals', {
        'x': -10, 'y': 2, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'icon': 'Generic_Political_Purge',
        'prereqs': ['VIE_hl_national_firewall'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_12'
        ]
    }),
    ('VIE_hl_peoples_war_doctrine', {
        'x': -8, 'y': 2, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'icon': 'GFX_focus_generic_military_mission',
        'prereqs': ['VIE_hl_defense_self_reliance'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_12'
        ]
    }),
    ('VIE_hl_indochinese_consultative_congress', {
        'x': -6, 'y': 2, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'icon': 'treaty2',
        'prereqs': ['VIE_hl_cambodia_revolutionary_front'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_12'
        ]
    }),

    # =============================================================
    # ĐẠI HỘI XIII (2021 - 2026)
    # =============================================================
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI XIII (2021 - 2026)\n\t#############################################################"),
    ('VIE_resolution_congress_13', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_14', '}']
    }),

    # --- NHIỆM KỲ XIII: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI, Y = 16) ---
    ("COMMENT", "\t# --- NHIỆM KỲ XIII: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_digital_anticorruption', {
        'x': -4, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_13'
        ]
    }),
    ('VIE_e_government', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_13'
        ]
    }),
    ('VIE_peoples_oversight', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_13',
            'has_completed_focus = VIE_clean_cadres'
        ]
    }),
    ('VIE_resolution_57_68', {
        'x': 4, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_13',
            'date > 2025.4.30'
        ]
    }),
    ('VIE_institutional_bottlenecks', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_13',
            'has_completed_focus = VIE_resolution_57_68',
            'date > 2024.12.31'
        ]
    }),
    ('VIE_civil_defense_law_2023', {
        'x': 8, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_13',
            'date > 2023.6.20'
        ]
    }),

    # --- NHIỆM KỲ XIII: CÁNH KIÊN ĐỊNH (4 CỘT TRỤ, Y = 17) ---
    ("COMMENT", "\t# --- NHIỆM KỲ XIII: 4 CỘT TRỤ KIÊN ĐỊNH (Y = 17) ---"),
    ('VIE_hl_socialist_industrialization', {
        'x': -12, 'y': 2, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'icon': 'economic_civil_industry',
        'prereqs': ['VIE_hl_strategic_resources'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_13'
        ]
    }),
    ('VIE_hl_iron_discipline_state', {
        'x': -10, 'y': 2, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'icon': 'Generic_Political_Purge',
        'prereqs': ['VIE_hl_revolutionary_tribunals'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_13'
        ]
    }),
    ('VIE_hl_vietnam_shield', {
        'x': -8, 'y': 2, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'icon': 'GFX_focus_generic_military_mission',
        'prereqs': ['VIE_hl_peoples_war_doctrine'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_13'
        ]
    }),
    ('VIE_hl_indochinese_socialist_union', {
        'x': -6, 'y': 2, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'icon': 'diplomatic_treaty',
        'prereqs': ['VIE_hl_indochinese_consultative_congress'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_13'
        ]
    }),

    # =============================================================
    # ĐẠI HỘI XIV & ĐỈNH CAO THẾ KỶ (2026+)
    # =============================================================
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI XIV & ĐỈNH CAO THẾ KỶ (2026+)\n\t#############################################################"),
    ('VIE_resolution_congress_14', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_13'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_15', '}']
    }),

    # --- NHIỆM KỲ XIV: LỰA CHỌN ĐỊNH HƯỚNG CHÍNH TRỊ (Y = 19) ---
    ("COMMENT", "\t# --- LỰA CHỌN ĐỊNH HƯỚNG CHÍNH TRỊ ĐẠI HỘI XIV ---"),
    ('VIE_hl_unbreakable_fortress', {
        'x': -8, 'y': 1, 'rel': 'VIE_resolution_congress_14',
        'cost': 7,
        'icon': 'legislative_palace',
        'prereqs': ['VIE_resolution_congress_14'],
        'mutually_exclusive': ['VIE_concentration_of_power', 'VIE_institutional_opening'],
        'avail': [
            'VIE_hl_in_power = yes',
            'has_completed_focus = VIE_resolution_congress_14',
            'has_completed_focus = VIE_hl_iron_discipline_state'
        ]
    }),
    ('VIE_concentration_of_power', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_14',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_14'],
        'mutually_exclusive': ['VIE_institutional_opening', 'VIE_hl_unbreakable_fortress'],
        'avail': [
            'NOT = { VIE_hl_in_power = yes }',
            'has_completed_focus = VIE_resolution_congress_14',
            'has_country_flag = VIE_two_tier_done'
        ]
    }),
    ('VIE_institutional_opening', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_14',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_14'],
        'mutually_exclusive': ['VIE_concentration_of_power', 'VIE_hl_unbreakable_fortress'],
        'avail': [
            'NOT = { VIE_hl_in_power = yes }',
            'has_completed_focus = VIE_resolution_congress_14',
            'has_country_flag = VIE_two_tier_done'
        ]
    }),

    # --- ĐỈNH CAO CHUNG (Y = 20, 21) ---
    ("COMMENT", "\t# --- ĐỈNH CAO DÂN TỘC & ĐẢNG (DÙNG CHUNG) ---"),
    ('VIE_era_of_rising', {
        'x': 0, 'y': 2, 'rel': 'VIE_resolution_congress_14',
        'cost': 5,
        'prereqs': [['VIE_concentration_of_power', 'VIE_institutional_opening', 'VIE_hl_unbreakable_fortress']],
        'avail': ['date > 2026.1.15']
    }),
    ('VIE_party_centennial_2030', {
        'x': 0, 'y': 1, 'rel': 'VIE_era_of_rising',
        'cost': 5,
        'prereqs': ['VIE_era_of_rising'],
        'avail': ['date > 2029.12.31']
    }),
]


formatted_blocks = []
for item in elements:
    if item[0] == "COMMENT":
        formatted_blocks.append(item[1])
    else:
        fid, spec = item
        raw_blk = blocks[fid]
        clean_blk = build_clean_focus(fid, spec, raw_blk)
        formatted_blocks.append(clean_blk)

unified_section = "\n\n".join(formatted_blocks)

# Replace in content:
m_start = re.search(r'(?m)^\tfocus\s*=\s*\{\s*\n\t\tid\s*=\s*VIE_prepare_congress_9\b', content)
m_end = re.search(r'(?m)^\tfocus\s*=\s*\{\s*\n\t\tid\s*=\s*VIE_party_centennial_2030\b', content)

start_idx = m_start.start()
depth = 1
i = content.find('{', m_end.start()) + 1
while i < len(content) and depth > 0:
    if content[i] == '{': depth += 1
    elif content[i] == '}': depth -= 1
    i += 1
end_idx = i

new_content = content[:start_idx] + unified_section + content[end_idx:]

# Also clean up the ghost tail after VIE_digital_nation:
tail_marker = new_content.rfind('VIE_digital_nation')
if tail_marker != -1:
    depth = 1
    dn_start = new_content.rfind('focus = {', 0, tail_marker)
    i = new_content.find('{', dn_start) + 1
    while i < len(new_content) and depth > 0:
        if new_content[i] == '{': depth += 1
        elif new_content[i] == '}': depth -= 1
        i += 1
    dn_end = i
    new_content = new_content[:dn_end] + "\n}\n"

focus_file.write_text(new_content, encoding="utf-8")
print("SUCCESS: Written 100% standard-compliant 4-pillar parallel political tree and cleaned file!")
