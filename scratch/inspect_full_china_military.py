import re

file_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\common\national_focus\05_china.txt'
with open(file_path, encoding='utf-8', errors='replace') as f:
    text = f.read()

parts = re.split(r'\n\tfocus = \{', text)

target_focuses = {}
for p in parts[1:]:
    fid = re.search(r'id\s*=\s*(\w+)', p)
    if not fid: continue
    fid = fid.group(1)
    
    fprereqs = re.findall(r'focus\s*=\s*(\w+)', re.search(r'prerequisite\s*=\s*\{([^}]*)\}', p).group(1)) if re.search(r'prerequisite\s*=\s*\{([^}]*)\}', p) else []
    target_focuses[fid] = {'prereqs': fprereqs, 'full': p}

# Trace parent of CHI_informatized_local_wars
cur = 'CHI_informatized_local_wars'
print("Chain leading to CHI_informatized_local_wars:")
while cur in target_focuses and target_focuses[cur]['prereqs']:
    print(f" <- {cur}")
    cur = target_focuses[cur]['prereqs'][0]
print(f"Root: {cur}")

# Check if ANY focus in China tree has prereqs referencing any of Great Wall, Iron Fist, Sharp Blade focuses
all_archetype_focuses = {
    'CHI_the_great_wall', 'CHI_peoples_armed_police_integration', 'CHI_strategic_reserve_system', 'CHI_active_defense_doctrine', 'CHI_underground_great_wall',
    'CHI_the_iron_fist', 'CHI_ztz99_rollout', 'CHI_heavy_combined_arms_brigade', 'CHI_zbd_mechanisation', 'CHI_long_range_firepower',
    'CHI_the_sharp_blade', 'CHI_type_15_light_tank', 'CHI_special_operations_forces', 'CHI_army_aviation_corps', 'CHI_rapid_reaction_corps'
}

downstream = {}
for fid, data in target_focuses.items():
    if fid not in all_archetype_focuses and fid != 'CHI_informatized_local_wars':
        for p in data['prereqs']:
            if p in all_archetype_focuses:
                downstream[fid] = p

print("\nFocuses outside the 3 archetypes that depend on them:")
print(downstream)

# Check what Navy and Air Force branches look like
print("\n--- NAVAL BRANCH ROOTS & MUTEXES ---")
for fid, data in target_focuses.items():
    if any(k in fid.lower() for k in ['plan_', 'navy', 'naval', 'carrier', 'submarine']):
        mutex = re.findall(r'focus\s*=\s*(\w+)', re.search(r'mutually_exclusive\s*=\s*\{([^}]*)\}', data['full']).group(1)) if re.search(r'mutually_exclusive\s*=\s*\{([^}]*)\}', data['full']) else []
        if mutex:
            print(f"Naval Mutex: {fid} vs {mutex}")

print("\n--- AIR FORCE BRANCH ROOTS & MUTEXES ---")
for fid, data in target_focuses.items():
    if any(k in fid.lower() for k in ['plaaf', 'air_force', 'fighter', 'stealth']):
        mutex = re.findall(r'focus\s*=\s*(\w+)', re.search(r'mutually_exclusive\s*=\s*\{([^}]*)\}', data['full']).group(1)) if re.search(r'mutually_exclusive\s*=\s*\{([^}]*)\}', data['full']) else []
        if mutex:
            print(f"Air Mutex: {fid} vs {mutex}")
