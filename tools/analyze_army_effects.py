import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Match each focus block
pattern = re.compile(r'focus\s*=\s*\{([^\{\}]*(?:\{[^\{\}]*(?:\{[^\{\}]*\}[^\{\}]*)*\}[^\{\}]*)*)\}')
focuses = pattern.findall(content)

army_focs = []
for foc in focuses:
    id_m = re.search(r'\bid\s*=\s*(VIE_lf_\w+|VIE_def_industry_law|VIE_military_enterprises_\w+|VIE_path_self_reliant_deterrence)\b', foc)
    if id_m:
        fid = id_m.group(1)
        
        cost_m = re.search(r'\bcost\s*=\s*(\d+)', foc)
        cost = cost_m.group(1) if cost_m else "10"
        
        prereq_m = re.findall(r'prerequisite\s*=\s*\{([^}]*)\}', foc)
        prereqs = [p.strip() for p in prereq_m]
        
        avail_m = re.search(r'available\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', foc)
        avail = avail_m.group(1).strip() if avail_m else 'NONE'
        
        reward_m = re.search(r'completion_reward\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', foc)
        reward = reward_m.group(1).strip() if reward_m else 'NONE'
        reward = re.sub(r'log\s*=\s*"[^"]*"', '', reward).strip()
        
        army_focs.append((fid, cost, prereqs, avail, reward))

print(f"Total army focuses found: {len(army_focs)}")
for fid, cost, prereqs, avail, rew in army_focs:
    print(f"\n==================================================")
    print(f"Focus: {fid} (cost={cost})")
    print(f"  Prerequisites: {prereqs}")
    print(f"  Available: {avail}")
    print(f"  Reward: {rew}")
