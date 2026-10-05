import re
from pathlib import Path

FOCUS_FILE = Path('common/national_focus/VIE_md_focus.txt')
content = FOCUS_FILE.read_text(encoding='utf-8')

# Parse all focus blocks in current file
def parse_focus_blocks(text):
    blocks = {}
    pos = 0
    while True:
        m = re.search(r'(?m)^\t?focus\s*=\s*\{', text[pos:])
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
print(f"Extracted {len(blocks)} focus blocks from current file.")

def extract_field(blk, field_name):
    m = re.search(r'(?m)^\t+' + field_name + r'\s*=\s*(\S+)', blk)
    return m.group(1) if m else None

def extract_block(blk, block_name):
    m = re.search(r'(?m)^\t+' + block_name + r'\s*=\s*\{', blk)
    if not m: return None
    start = m.start()
    brace = 1
    i = m.end()
    while i < len(blk) and brace > 0:
        if blk[i] == '{': brace += 1
        elif blk[i] == '}': brace -= 1
        i += 1
    return blk[start:i]

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
    raw_filters = extract_block(raw_blk, 'search_filters')
    raw_avail = extract_block(raw_blk, 'available')
    raw_bypass = extract_block(raw_blk, 'bypass')
    raw_reward = extract_block(raw_blk, 'completion_reward')
    raw_ai = extract_block(raw_blk, 'ai_will_do')
    
    lines = ["\tfocus = {", f"\t\tid = {fid}", f"\t\ticon = {icon}", "", f"\t\tx = {x}", f"\t\ty = {y}"]
    if rel:
        lines.append(f"\t\trelative_position_id = {rel}")
    lines.append("")
    lines.append(f"\t\tcost = {cost}")
    lines.append("")
    
    if prereqs is not None:
        if len(prereqs) == 0:
            pass
        elif len(prereqs) == 1:
            lines.append(f"\t\tprerequisite = {{ focus = {prereqs[0]} }}")
        else:
            p_str = " ".join(f"focus = {p}" for p in prereqs)
            lines.append(f"\t\tprerequisite = {{ {p_str} }}")
    else:
        raw_pre = re.findall(r'(?m)^\t+prerequisite\s*=\s*\{[^}]*\}', raw_blk)
        for p in raw_pre:
            lines.append(f"\t{p.strip()}")
            
    if mx is not None:
        if len(mx) > 0:
            mx_str = " ".join(f"focus = {m}" for m in mx)
            lines.append(f"\t\tmutually_exclusive = {{ {mx_str} }}")
    else:
        raw_mx = extract_block(raw_blk, 'mutually_exclusive')
        if raw_mx:
            lines.append(f"\t\t{raw_mx.strip()}")
            
    lines.append("")
    if raw_filters:
        f_tokens = re.findall(r'FOCUS_FILTER_\w+', raw_filters)
        if f_tokens:
            lines.append(f"\t\tsearch_filters = {{ {' '.join(f_tokens)} }}")
            lines.append("")
            
    if 'avail' in spec:
        lines.append("\t\tavailable = {")
        for av in spec['avail']:
            lines.append(f"\t\t\t{av}")
        lines.append("\t\t}")
    elif raw_avail:
        av_lines = raw_avail.strip().splitlines()
        lines.append("\t\tavailable = {")
        for al in av_lines[1:-1]:
            lines.append(f"\t\t{al.strip()}")
        lines.append("\t\t}")
        
    if 'bypass' in spec:
        lines.append("\t\tbypass = {")
        for bp in spec['bypass']:
            lines.append(f"\t\t\t{bp}")
        lines.append("\t\t}")
    elif raw_bypass:
        bp_lines = raw_bypass.strip().splitlines()
        lines.append("\t\tbypass = {")
        for bl in bp_lines[1:-1]:
            lines.append(f"\t\t{bl.strip()}")
        lines.append("\t\t}")
        
    lines.append("")
    if raw_reward:
        rew_lines = raw_reward.strip().splitlines()
        lines.append("\t\tcompletion_reward = {")
        for rl in rew_lines[1:-1]:
            lines.append(f"\t\t{rl.strip()}")
        lines.append("\t\t}")
        
    lines.append("")
    if raw_ai:
        ai_lines = raw_ai.strip().splitlines()
        lines.append("\t\tai_will_do = {")
        for ail in ai_lines[1:-1]:
            lines.append(f"\t\t{ail.strip()}")
        lines.append("\t\t}")
    else:
        lines.append("\t\tai_will_do = { base = 50 }")
        
    lines.append("\t}")
    return "\n".join(lines)

# 42 Political focuses strictly without any hardline focuses
political_elements = [
    # GỐC CÂY
    ('VIE_prepare_congress_9', {
        'x': 14, 'y': 1, 'rel': None,
        'cost': 5,
        'prereqs': [],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_party_rule_active_tt VIE_party_rule_active = yes }',
            'NOT = { has_country_flag = VIE_resolution_congress_9_done }'
        ]
    }),
    ('VIE_grassroots_democracy', {
        'x': -2, 'y': 1, 'rel': 'VIE_prepare_congress_9',
        'cost': 5,
        'prereqs': ['VIE_prepare_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_party_rule_active_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_prepare_congress_9'
        ]
    }),
    ('VIE_mass_mobilization', {
        'x': 2, 'y': 1, 'rel': 'VIE_prepare_congress_9',
        'cost': 5,
        'prereqs': ['VIE_prepare_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_party_rule_active_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_prepare_congress_9'
        ]
    }),

    # ĐẠI HỘI IX (2001 - 2006)
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI IX (2001 - 2006)\n\t#############################################################"),
    ('VIE_resolution_congress_9', {
        'x': 0, 'y': 2, 'rel': 'VIE_prepare_congress_9',
        'cost': 5,
        'prereqs': ['VIE_prepare_congress_9'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_resolution_congress_9_done', '}']
    }),
    # Nhiệm kỳ IX: Nghị quyết chung (Y = 4)
    ("COMMENT", "\t# --- NHIỆM KỲ IX: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_ethnic_policy', {
        'x': -4, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_9']
    }),
    ('VIE_state_audit', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_9']
    }),
    ('VIE_anti_corruption_law', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_9']
    }),
    ('VIE_national_assembly_role', {
        'x': 4, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_9']
    }),
    ('VIE_public_admin_reform', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_9']
    }),
    ('VIE_decentralization', {
        'x': 8, 'y': 1, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_9',
            'has_completed_focus = VIE_public_admin_reform'
        ]
    }),

    # ĐẠI HỘI X (2006 - 2011)
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI X (2006 - 2011)\n\t#############################################################"),
    ('VIE_resolution_congress_10', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_9',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_9'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_11', '}']
    }),
    # Nhiệm kỳ X: Nghị quyết chung (Y = 7, 8)
    ("COMMENT", "\t# --- NHIỆM KỲ X: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_anti_corruption_steering', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_10'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_10']
    }),
    ('VIE_asset_declaration', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_10'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_10']
    }),
    ('VIE_party_members_private_business', {
        'x': 4, 'y': 2, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_10'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_10',
            'NOT = { has_completed_focus = VIE_hl_no_party_business }'
        ]
    }),

    # ĐẠI HỘI XI (2011 - 2016)
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI XI (2011 - 2016)\n\t#############################################################"),
    ('VIE_resolution_congress_11', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_10',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_10'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_12', '}']
    }),
    # Nhiệm kỳ XI: Nghị quyết chung (Y = 10)
    ("COMMENT", "\t# --- NHIỆM KỲ XI: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_tw4_party_building', {
        'x': -4, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_11']
    }),
    ('VIE_party_inspection', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_11']
    }),
    ('VIE_platform_2011', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_11']
    }),
    ('VIE_rule_of_law_state', {
        'x': 4, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_11']
    }),
    ('VIE_constitution_2013', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_11']
    }),
    ('VIE_disaster_law_2013', {
        'x': 8, 'y': 1, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_11'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_11']
    }),

    # ĐẠI HỘI XII (2016 - 2021)
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI XII (2016 - 2021)\n\t#############################################################"),
    ('VIE_resolution_congress_12', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_11',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_11'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_13', '}']
    }),
    # Nhiệm kỳ XII: Nghị quyết chung (Y = 13)
    ("COMMENT", "\t# --- NHIỆM KỲ XII: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_streamline_apparatus', {
        'x': -4, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_12']
    }),
    ('VIE_cybersecurity_law', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_12']
    }),
    ('VIE_party_discipline', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_12']
    }),
    ('VIE_cadre_accountability', {
        'x': 4, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_12']
    }),
    ('VIE_asset_recovery', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_12']
    }),
    ('VIE_clean_cadres', {
        'x': 8, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_12']
    }),
    ('VIE_higher_education_law', {
        'x': 10, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_12']
    }),
    ('VIE_education_law_2019', {
        'x': 12, 'y': 1, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_12']
    }),

    # ĐẠI HỘI XIII (2021 - 2026)
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI XIII (2021 - 2026)\n\t#############################################################"),
    ('VIE_resolution_congress_13', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_12',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_12'],
        'bypass': ['OR = {', '\tNOT = { VIE_party_rule_active = yes }', '\thas_country_flag = VIE_sched_congress_14', '}']
    }),
    # Nhiệm kỳ XIII: Nghị quyết chung (Y = 16)
    ("COMMENT", "\t# --- NHIỆM KỲ XIII: CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI) ---"),
    ('VIE_digital_anticorruption', {
        'x': -4, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_13']
    }),
    ('VIE_e_government', {
        'x': -2, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_13']
    }),
    ('VIE_peoples_oversight', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_13']
    }),
    ('VIE_resolution_57_68', {
        'x': 4, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_13']
    }),
    ('VIE_institutional_bottlenecks', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_13']
    }),
    ('VIE_civil_defense_law_2023', {
        'x': 8, 'y': 1, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': ['custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }', 'has_completed_focus = VIE_resolution_congress_13']
    }),

    # ĐẠI HỘI XIV (2026+)
    ("COMMENT", "\t#############################################################\n\t## ĐẠI HỘI XIV (2026+)\n\t#############################################################"),
    ('VIE_resolution_congress_14', {
        'x': 0, 'y': 3, 'rel': 'VIE_resolution_congress_13',
        'cost': 5,
        'prereqs': ['VIE_resolution_congress_13'],
        'avail': [
            'custom_trigger_tooltip = { tooltip = VIE_party_rule_active_tt VIE_party_rule_active = yes }',
            'has_completed_focus = VIE_resolution_congress_13',
            'date > 2026.1.1'
        ]
    }),
    # Định hướng chính trị ĐH XIV (Y = 19)
    ("COMMENT", "\t# --- LỰA CHỌN ĐỊNH HƯỚNG CHÍNH TRỊ ĐẠI HỘI XIV ---"),
    ('VIE_concentration_of_power', {
        'x': 2, 'y': 1, 'rel': 'VIE_resolution_congress_14',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_14'],
        'mutually_exclusive': ['VIE_institutional_opening'],
        'avail': [
            'NOT = { VIE_hl_in_power = yes }',
            'has_completed_focus = VIE_resolution_congress_14',
            'custom_trigger_tooltip = { tooltip = VIE_flag_VIE_two_tier_done_tt has_country_flag = VIE_two_tier_done }'
        ]
    }),
    ('VIE_institutional_opening', {
        'x': 6, 'y': 1, 'rel': 'VIE_resolution_congress_14',
        'cost': 7,
        'prereqs': ['VIE_resolution_congress_14'],
        'mutually_exclusive': ['VIE_concentration_of_power'],
        'avail': [
            'NOT = { VIE_hl_in_power = yes }',
            'has_completed_focus = VIE_resolution_congress_14',
            'custom_trigger_tooltip = { tooltip = VIE_flag_VIE_two_tier_done_tt has_country_flag = VIE_two_tier_done }'
        ]
    }),

    # ĐỈNH CAO DÂN TỘC & ĐẢNG (Y = 20, 21)
    ("COMMENT", "\t# --- ĐỈNH CAO DÂN TỘC & ĐẢNG (DÙNG CHUNG) ---"),
    ('VIE_era_of_rising', {
        'x': 0, 'y': 2, 'rel': 'VIE_resolution_congress_14',
        'cost': 5,
        'prereqs': ['VIE_concentration_of_power', 'VIE_institutional_opening'],
        'avail': ['date > 2026.1.15']
    }),
    ('VIE_party_centennial_2030', {
        'x': 0, 'y': 1, 'rel': 'VIE_era_of_rising',
        'cost': 5,
        'prereqs': ['VIE_era_of_rising'],
        'avail': ['date > 2029.12.31']
    }),
]

print("--- Building Clean 42-Focus Political Tree ---")
formatted_political_blocks = []
for item in political_elements:
    if item[0] == "COMMENT":
        formatted_political_blocks.append(item[1])
    else:
        fid, spec = item
        raw_blk = blocks[fid]
        clean_blk = build_clean_focus(fid, spec, raw_blk)
        formatted_political_blocks.append(clean_blk)

unified_political_section = "\n\n".join(formatted_political_blocks)

# Replace the old political section in content (from prepare_congress_9 to party_centennial_2030)
m_start = re.search(r'(?m)^\t?focus\s*=\s*\{\s*\n\t+id\s*=\s*VIE_prepare_congress_9\b', content)
m_end = re.search(r'(?m)^\t?focus\s*=\s*\{\s*\n\t+id\s*=\s*VIE_party_centennial_2030\b', content)

start_idx = m_start.start()
depth = 1
i = content.find('{', m_end.start()) + 1
while i < len(content) and depth > 0:
    if content[i] == '{': depth += 1
    elif content[i] == '}': depth -= 1
    i += 1
end_idx = i

# Remove ghost duplicates of political focuses that might exist further down in the file
new_content = content[:start_idx] + unified_political_section + content[end_idx:]

# 42 IDs to remove from the rest of the file if duplicated
pol_ids = set([item[0] for item in political_elements if item[0] != "COMMENT"])
# Find any duplicate occurrences after start_idx + len(unified_political_section)
tail_part = new_content[start_idx + len(unified_political_section):]
parsed_tail = parse_focus_blocks(tail_part)
duplicates = [f for f in parsed_tail if f in pol_ids and f != 'VIE_party_centennial_2030']
print(f"Duplicate political focuses found in tail: {len(duplicates)}")
for dup in duplicates:
    # Remove block
    p = re.search(r'(?m)^\t?focus\s*=\s*\{\s*\n\t+id\s*=\s*' + re.escape(dup) + r'\b', tail_part)
    if p:
        d = 1
        pos = p.end()
        while d > 0 and pos < len(tail_part):
            if tail_part[pos] == '{': d += 1
            elif tail_part[pos] == '}': d -= 1
            pos += 1
        while pos < len(tail_part) and tail_part[pos] in ' \t\r\n': pos += 1
        tail_part = tail_part[:p.start()] + tail_part[pos:]

new_content = new_content[:start_idx + len(unified_political_section)] + tail_part

print("--- Updating external references in other focuses ---")
new_content = new_content.replace('target = VIE_hl_soe_first', 'target = VIE_hl_unity_of_will')
new_content = re.sub(
    r'NOT\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_hl_curb_private_capital\s*\}',
    'NOT = { has_completed_focus = VIE_hl_no_party_business }',
    new_content
)
new_content = re.sub(
    r'NOT\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_hl_soe_first\s*\}',
    'NOT = { has_completed_focus = VIE_hl_state_sector_leading }',
    new_content
)
new_content = re.sub(
    r'NOT\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_hl_iron_discipline_state\s*\}',
    'NOT = { has_completed_focus = VIE_hl_party_state_fusion }',
    new_content
)

print("--- Appending 25 New Hardline Focuses right below party_centennial_2030 ---")
NEW_HARDLINE_SECTION = """
	#############################################################
	## CON ĐƯỜNG KIÊN ĐỊNH (CPV HARDLINE - RULING PARTY 4)
	## Cây độc lập hoàn toàn, 25 focus (H0 -> X3)
	## Bố cục 4 trụ song song + trục trung tâm (Y=23..31, X=6..22)
	#############################################################

	# H0: Gốc cây Kiên định
	focus = {
		id = VIE_hl_unity_of_will
		icon = legislative_palace

		x = 0
		y = 2
		relative_position_id = VIE_party_centennial_2030

		cost = 5

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_unity_of_will"
			add_political_power = 50
			VIE_bop_conservative_small = yes
			if = {
				limit = { NOT = { check_variable = { VIE_rp > 0 } } }
				set_variable = { VIE_rp = 20 }
			}
			VIE_hl_update_pressure_idea = yes
		}

		ai_will_do = { base = 100 }
	}

	# H1: Chỉnh đốn Đảng
	focus = {
		id = VIE_hl_party_rectification
		icon = Generic_Political_Purge

		x = 0
		y = 1
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_unity_of_will }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_rectification"
			add_stability = 0.02
			decrease_corruption = yes
			set_temp_variable = { temp_opinion = 3 }
			change_communist_cadres_opinion = yes
			set_temp_variable = { temp_opinion = -4 }
			change_industrial_conglomerates_opinion = yes
			add_timed_idea = { idea = VIE_official_caution days = 365 }
			if = {
				limit = { has_completed_focus = VIE_clean_cadres }
				set_temp_variable = { VIE_rp_add = 4 }
				custom_effect_tooltip = VIE_hl_rp_p4_tt
			}
			else = {
				set_temp_variable = { VIE_rp_add = 6 }
				custom_effect_tooltip = VIE_hl_rp_p6_tt
			}
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# H2: Bảo vệ nền tảng tư tưởng
	focus = {
		id = VIE_hl_ideological_foundation
		icon = propaganda

		x = -4
		y = 1
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_unity_of_will }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_ideological_foundation"
			add_political_power = 50
			add_ideas = VIE_hl_ideology_work_idea
			set_temp_variable = { VIE_rp_add = 4 }
			custom_effect_tooltip = VIE_hl_rp_p4_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# H3: Thống nhất quản lý cán bộ
	focus = {
		id = VIE_hl_cadre_centralisation
		icon = communist_purge

		x = 0
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_rectification }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_cadre_centralisation"
			VIE_bop_conservative_small = yes
			if = {
				limit = { has_completed_focus = VIE_decentralization }
				set_temp_variable = { VIE_rp_add = 7 }
				custom_effect_tooltip = VIE_hl_rp_p7_tt
			}
			else = {
				set_temp_variable = { VIE_rp_add = 4 }
				custom_effect_tooltip = VIE_hl_rp_p4_tt
			}
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A1: Kinh tế nhà nước chủ đạo
	focus = {
		id = VIE_hl_state_sector_leading
		icon = focus_generic_central_planning

		x = -4
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_rectification }

		search_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
			NOT = { has_completed_focus = VIE_soe_rapid_divestment }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_state_sector_leading"
			set_temp_variable = { treasury_change = 2 }
			modify_treasury_effect = yes
			add_ideas = VIE_hl_state_leading_idea
			add_timed_idea = { idea = VIE_hl_state_transition_idea days = 730 }
			set_temp_variable = { temp_opinion = 4 }
			change_communist_cadres_opinion = yes
			set_temp_variable = { temp_opinion = -4 }
			change_industrial_conglomerates_opinion = yes
			if = {
				limit = { has_completed_focus = VIE_state_conglomerates }
				add_political_power = 25
			}
			set_temp_variable = { VIE_rp_add = 4 }
			custom_effect_tooltip = VIE_hl_rp_p4_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A2: Danh mục ngành then chốt
	focus = {
		id = VIE_hl_key_sectors
		icon = economic_civil_industry

		x = -4
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_state_sector_leading }

		search_filters = { FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
			NOT = { has_country_flag = bankruptcy_incoming_collapse }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_key_sectors"
			one_state_industrial_complex = yes
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A3: Tập đoàn đầu tàu
	focus = {
		id = VIE_hl_soe_spearhead
		icon = economic_prosperity

		x = -2
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_state_sector_leading }

		search_filters = { FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_soe_spearhead"
			increase_economic_growth = yes
			add_timed_idea = { idea = VIE_hl_soe_spearhead_idea days = 730 }
			add_to_variable = { var = VIE_vinashin_risk value = 2 }
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A4: Kiểm soát dòng vốn, FDI
	focus = {
		id = VIE_hl_selective_fdi
		icon = asian_investment

		x = -2
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_key_sectors }

		search_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_selective_fdi"
			add_stability = 0.01
			add_political_power = 25
			set_temp_variable = { treasury_change = -2 }
			modify_treasury_effect = yes
			add_timed_idea = { idea = VIE_hl_fdi_slowdown_idea days = 365 }
			if = { limit = { country_exists = USA } add_opinion_modifier = { target = USA modifier = small_decrease } }
			if = { limit = { country_exists = JAP } add_opinion_modifier = { target = JAP modifier = small_decrease } }
			if = { limit = { country_exists = KOR } add_opinion_modifier = { target = KOR modifier = small_decrease } }
			set_temp_variable = { VIE_rp_add = 6 }
			custom_effect_tooltip = VIE_hl_rp_p6_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A5: Đảng viên không làm kinh tế tư nhân
	focus = {
		id = VIE_hl_no_party_business
		icon = anti_corruption

		x = -6
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_rectification }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
			NOT = { has_completed_focus = VIE_private_champions }
			NOT = { has_completed_focus = VIE_private_sector_engine }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_no_party_business"
			VIE_bop_conservative_small = yes
			set_temp_variable = { temp_opinion = 3 }
			change_communist_cadres_opinion = yes
			set_temp_variable = { temp_opinion = -5 }
			change_industrial_conglomerates_opinion = yes
			set_temp_variable = { VIE_rp_add = 5 }
			custom_effect_tooltip = VIE_hl_rp_p5_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 40
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# A6: Kế hoạch định hướng 5 năm
	focus = {
		id = VIE_hl_five_year_plan
		icon = five_year_plan

		x = -4
		y = 5
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_soe_spearhead focus = VIE_hl_selective_fdi }

		search_filters = { FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_five_year_plan"
			set_temp_variable = { treasury_change = 3 }
			modify_treasury_effect = yes
			add_ideas = VIE_hl_planning_idea
			set_temp_variable = { VIE_rp_add = 3 }
			custom_effect_tooltip = VIE_hl_rp_p3_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 60
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# B1: Đảng lãnh đạo tuyệt đối quân đội
	focus = {
		id = VIE_hl_party_leads_army
		icon = GFX_focus_generic_military_mission

		x = 4
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_unity_of_will }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
			has_completed_focus = VIE_modernize_vpa
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_leads_army"
			set_temp_variable = { temp_opinion = 3 }
			change_the_military_opinion = yes
			VIE_bop_conservative_small = yes
			add_ideas = VIE_hl_army_party_work_idea
			army_experience = 10
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# B2: Giáo dục chính trị LLVT
	focus = {
		id = VIE_hl_army_political_education
		icon = GFX_focus_generic_military_mission

		x = 4
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 5

		prerequisite = { focus = VIE_hl_party_leads_army }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_WAR_SUPPORT }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_army_political_education"
			add_war_support = 0.03
			army_experience = 10
			set_temp_variable = { treasury_change = -1 }
			modify_treasury_effect = yes
			set_temp_variable = { VIE_rp_add = 1 }
			custom_effect_tooltip = VIE_hl_rp_p1_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 50 }
	}

	# B3: Thế trận quốc phòng toàn dân
	focus = {
		id = VIE_hl_all_people_defence
		icon = GFX_focus_generic_military_mission

		x = 4
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_leads_army }

		search_filters = { FOCUS_FILTER_ARMY }

		available = {
			VIE_hl_in_power = yes
			has_completed_focus = VIE_peoples_defence
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_all_people_defence"
			add_ideas = VIE_hl_all_people_defence_idea
			set_temp_variable = { VIE_rp_add = 3 }
			custom_effect_tooltip = VIE_hl_rp_p3_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 50 }
	}

	# B4: CN Quốc phòng do Đảng chỉ đạo
	focus = {
		id = VIE_hl_party_defence_industry
		icon = GFX_focus_generic_military_mission

		x = 4
		y = 5
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_army_political_education }

		search_filters = { FOCUS_FILTER_ARMY FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_defence_industry"
			if = {
				limit = { has_completed_focus = VIE_military_enterprises_core }
				add_to_variable = { var = VIE_def_industry_level value = 1 }
			}
			else_if = {
				limit = { has_completed_focus = VIE_military_enterprises_divest }
				add_political_power = 50
				add_stability = 0.01
			}
			else = {
				add_political_power = 25
			}
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 60 }
	}

	# C1: Bảo vệ nền tảng tư tưởng không gian mạng
	focus = {
		id = VIE_hl_cyber_ideology
		icon = army_cyberwar

		x = -8
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_ideological_foundation }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_cyber_ideology"
			add_ideas = VIE_hl_cyber_content_idea
			if = { limit = { country_exists = USA } add_opinion_modifier = { target = USA modifier = small_decrease } }
			set_temp_variable = { VIE_rp_add = 7 }
			custom_effect_tooltip = VIE_hl_rp_p7_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# C2: Giáo dục lý luận chính trị
	focus = {
		id = VIE_hl_school_theory
		icon = GFX_focus_AFG_education_reform

		x = -8
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_ideological_foundation }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_school_theory"
			add_stability = 0.02
			set_temp_variable = { temp_opinion = 2 }
			change_communist_cadres_opinion = yes
			add_timed_idea = { idea = VIE_hl_school_theory_idea days = 730 }
			set_temp_variable = { VIE_rp_add = 3 }
			custom_effect_tooltip = VIE_hl_rp_p3_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# C3: Quy hoạch báo chí
	focus = {
		id = VIE_hl_press_planning
		icon = sov_free_media

		x = -8
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 5

		prerequisite = { focus = VIE_hl_cyber_ideology }

		search_filters = { FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_press_planning"
			add_political_power = 50
			if = { limit = { country_exists = USA } add_opinion_modifier = { target = USA modifier = small_decrease } }
			if = { limit = { country_exists = FRA } add_opinion_modifier = { target = FRA modifier = small_decrease } }
			set_temp_variable = { VIE_rp_add = 6 }
			custom_effect_tooltip = VIE_hl_rp_p6_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0.3 check_variable = { VIE_rp > 55 } }
		}
	}

	# C4: Mặt trận Tổ quốc và Đoàn thể
	focus = {
		id = VIE_hl_fatherland_front
		icon = treaty2

		x = 0
		y = 6
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_school_theory focus = VIE_hl_cadre_centralisation }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_fatherland_front"
			set_temp_variable = { temp_opinion = 4 }
			change_farmers_opinion = yes
			add_stability = 0.02
			set_temp_variable = { VIE_rp_add = -4 }
			custom_effect_tooltip = VIE_hl_rp_m4_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 3 check_variable = { VIE_rp > 55 } }
		}
	}

	# D1: Đối ngoại Đảng
	focus = {
		id = VIE_hl_party_diplomacy
		icon = diplomatic_treaty

		x = 8
		y = 2
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_unity_of_will }

		search_filters = { FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_diplomacy"
			add_political_power = 50
			if = { limit = { country_exists = LAO } add_opinion_modifier = { target = LAO modifier = large_increase } }
			if = { limit = { country_exists = CHI } add_opinion_modifier = { target = CHI modifier = large_increase } }
			if = { limit = { country_exists = CUB } add_opinion_modifier = { target = CUB modifier = large_increase } }
			set_temp_variable = { VIE_rp_add = 2 }
			custom_effect_tooltip = VIE_hl_rp_p2_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 50 }
	}

	# D2: Hợp tác không lệ thuộc
	focus = {
		id = VIE_hl_no_dependence
		icon = diplomacy

		x = 8
		y = 3
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_party_diplomacy }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_WAR_SUPPORT }

		available = {
			VIE_hl_in_power = yes
			has_completed_focus = VIE_four_nos_doctrine
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_no_dependence"
			add_war_support = 0.03
			add_stability = 0.01
			hidden_effect = { set_country_flag = VIE_hl_sovereignty_line }
			if = { limit = { country_exists = CHI } add_opinion_modifier = { target = CHI modifier = small_decrease } }
		}

		ai_will_do = { base = 60 }
	}

	# D3: Đối tác chiến lược chọn lọc
	focus = {
		id = VIE_hl_selective_partners
		icon = treaty2

		x = 8
		y = 4
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_no_dependence }

		search_filters = { FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
			OR = {
				has_completed_focus = VIE_japan_partnership
				has_completed_focus = VIE_india_partnership
				has_completed_focus = VIE_korea_partnership
			}
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_selective_partners"
			if = { limit = { country_exists = JAP } add_opinion_modifier = { target = JAP modifier = large_increase } }
			if = { limit = { country_exists = RAJ } add_opinion_modifier = { target = RAJ modifier = large_increase } }
			if = { limit = { country_exists = KOR } add_opinion_modifier = { target = KOR modifier = large_increase } }
			set_temp_variable = { temp_opinion = -2 }
			change_communist_cadres_opinion = yes
			VIE_bop_reform_small = yes
			set_temp_variable = { VIE_rp_add = -10 }
			custom_effect_tooltip = VIE_hl_rp_m10_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 3 check_variable = { VIE_rp > 55 } }
		}
	}

	# E1: Tổng kết nhiệm kỳ
	focus = {
		id = VIE_hl_term_review
		icon = legislative_palace

		x = 0
		y = 7
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_cadre_centralisation }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
			VIE_hl_pillars_three = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_term_review"
			add_political_power = 100
			add_stability = 0.03
			hidden_effect = { set_country_flag = VIE_hl_e1_done }
			country_event = { id = vie_hl.5 days = 3 }
		}

		ai_will_do = { base = 100 }
	}

	# X1: Kiên định mục tiêu, đổi mới phương thức
	focus = {
		id = VIE_hl_steadfast_renewal
		icon = economic_prosperity2

		x = -4
		y = 8
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_term_review }

		mutually_exclusive = { focus = VIE_hl_party_state_fusion focus = VIE_hl_handover }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_ECONOMY }

		available = {
			VIE_hl_in_power = yes
			custom_trigger_tooltip = {
				tooltip = VIE_hl_rp_below_80_tt
				check_variable = { VIE_rp < 80 }
			}
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_steadfast_renewal"
			increase_economic_growth = yes
			add_ideas = VIE_hl_controlled_renewal_idea
			set_temp_variable = { temp_opinion = -3 }
			change_communist_cadres_opinion = yes
			if = {
				limit = { has_country_flag = VIE_bop_active }
				set_power_balance = { id = VIE_party_balance set_value = -0.3 }
			}
			set_temp_variable = { VIE_rp_add = -25 }
			custom_effect_tooltip = VIE_hl_rp_m25_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = { base = 60 }
	}

	# X2: Nhất thể hóa
	focus = {
		id = VIE_hl_party_state_fusion
		icon = legislative_palace

		x = 0
		y = 8
		relative_position_id = VIE_hl_unity_of_will

		cost = 7

		prerequisite = { focus = VIE_hl_term_review }

		mutually_exclusive = { focus = VIE_hl_steadfast_renewal focus = VIE_hl_handover }

		search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }

		available = {
			VIE_hl_in_power = yes
			VIE_hl_pillars_all = yes
			has_completed_focus = VIE_hl_press_planning
			VIE_bop_is_hardline = yes
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_state_fusion"
			add_political_power = 150
			add_stability = 0.05
			add_ideas = VIE_hl_fusion_idea
			hidden_effect = { set_country_flag = VIE_hl_fusion_done }
			set_temp_variable = { VIE_rp_add = 8 }
			custom_effect_tooltip = VIE_hl_rp_p8_tt
			VIE_hl_add_pressure = yes
		}

		ai_will_do = {
			base = 20
			modifier = { factor = 0 check_variable = { VIE_rp > 69 } }
		}
	}

	# X3: Bàn giao đường lối
	focus = {
		id = VIE_hl_handover
		icon = election2

		x = 4
		y = 8
		relative_position_id = VIE_hl_unity_of_will

		cost = 5

		prerequisite = { focus = VIE_hl_term_review }

		mutually_exclusive = { focus = VIE_hl_steadfast_renewal focus = VIE_hl_party_state_fusion }

		search_filters = { FOCUS_FILTER_POLITICAL }

		available = {
			VIE_hl_in_power = yes
			custom_trigger_tooltip = {
				tooltip = VIE_hl_rp_below_56_tt
				check_variable = { VIE_rp < 56 }
			}
			NOT = { has_idea = VIE_hl_self_reliance_idea }
		}

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_handover"
			custom_effect_tooltip = VIE_hl_handover_tt
			hidden_effect = {
				set_temp_variable = { rul_party_temp = 19 }
				set_temp_variable = { VIE_hl_keep_legacy = 1 }
				VIE_transition_regime = yes
				if = {
					limit = { has_country_flag = VIE_bop_active }
					set_power_balance = { id = VIE_party_balance set_value = -0.3 }
				}
				set_country_flag = { flag = VIE_hardline_retired value = 1 days = 3650 }
			}
			add_political_power = 100
			add_stability = 0.05
		}

		ai_will_do = { base = 20 }
	}
"""

centennial_idx = new_content.find('id = VIE_party_centennial_2030')
pos = centennial_idx
brace = 0
found_first_brace = False
while pos < len(new_content):
    if new_content[pos] == '{':
        brace += 1
        found_first_brace = True
    elif new_content[pos] == '}':
        brace -= 1
        if found_first_brace and brace == 0:
            pos += 1
            break
    pos += 1

new_content = new_content[:pos] + "\n" + NEW_HARDLINE_SECTION + "\n" + new_content[pos:]
FOCUS_FILE.write_text(new_content, encoding='utf-8')
print("VIE_md_focus.txt successfully rewritten and structured!")
