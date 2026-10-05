with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse all focus blocks properly
foci = []
idx = 0
while True:
    pos = text.find('focus = {', idx)
    if pos == -1:
        break
    start = pos + len('focus = {')
    brace_count = 1
    i = start
    while i < len(text) and brace_count > 0:
        if text[i] == '{':
            brace_count += 1
        elif text[i] == '}':
            brace_count -= 1
        i += 1
    block = text[start:i-1]
    idx = i
    
    import re
    id_m = re.search(r'\bid\s*=\s*(\w+)', block)
    if id_m:
        fid = id_m.group(1)
        if fid.startswith('VIE_lf_') or fid.startswith('VIE_def_') or fid.startswith('VIE_military_enterprises') or fid == 'VIE_path_self_reliant_deterrence':
            cost_m = re.search(r'\bcost\s*=\s*(\d+)', block)
            cost = cost_m.group(1) if cost_m else "10 (default)"
            
            rew_m = re.search(r'completion_reward\s*=\s*\{', block)
            reward_str = ""
            if rew_m:
                r_start = rew_m.end()
                r_brace = 1
                j = r_start
                while j < len(block) and r_brace > 0:
                    if block[j] == '{':
                        r_brace += 1
                    elif block[j] == '}':
                        r_brace -= 1
                    j += 1
                reward_str = block[r_start:j-1].strip()
                reward_str = re.sub(r'log\s*=\s*"[^"]*"', '', reward_str).strip()
            
            avail_m = re.search(r'available\s*=\s*\{', block)
            avail_str = ""
            if avail_m:
                a_start = avail_m.end()
                a_brace = 1
                j = a_start
                while j < len(block) and a_brace > 0:
                    if block[j] == '{':
                        a_brace += 1
                    elif block[j] == '}':
                        a_brace -= 1
                    j += 1
                avail_str = block[a_start:j-1].strip()
            
            prereqs = re.findall(r'prerequisite\s*=\s*\{([^}]*)\}', block)
            foci.append({
                'id': fid,
                'cost': cost,
                'prereqs': [p.strip() for p in prereqs],
                'avail': avail_str,
                'reward': reward_str
            })

print(f"Total parsed army focuses: {len(foci)}")
for f in foci:
    print(f"\n[{f['id']}] (cost: {f['cost']})")
    print(f"  Prereqs: {f['prereqs']}")
    print(f"  Avail: {f['avail'] if f['avail'] else 'None'}")
    print(f"  Reward: {f['reward']}")
