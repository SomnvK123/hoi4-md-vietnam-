import os, glob, re

ROOT = r'd:/HOI4Mods/md_vietnam'
os.chdir(ROOT)

# Load all loc keys
loc_keys = set()
for lf in glob.glob('localisation/english/**/*.yml', recursive=True):
    with open(lf, 'r', encoding='utf-8-sig', errors='ignore') as f:
        for line in f:
            m = re.match(r'^\s*([A-Za-z0-9_.\-]+):', line)
            if m:
                loc_keys.add(m.group(1))

print(f"Loaded {len(loc_keys)} keys from {len(glob.glob('localisation/english/**/*.yml', recursive=True))} localisation files.")

missing = []

# 1. Balance of Power (bop)
for p in glob.glob('common/bop/*.txt'):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    for m in re.finditer(r'\bid\s*=\s*(VIE_\w+)', t):
        k = m.group(1)
        if k not in loc_keys: missing.append(('bop_id', k, p))
    for m in re.finditer(r'\b(?:left_side|right_side)\s*=\s*(VIE_\w+)', t):
        k = m.group(1)
        if k not in loc_keys: missing.append(('bop_side', k, p))
    for m in re.finditer(r'\bdecision_category\s*=\s*(VIE_\w+)', t):
        k = m.group(1)
        if k not in loc_keys: missing.append(('bop_category', k, p))

# 2. Dynamic modifiers
for p in glob.glob('common/dynamic_modifiers/*.txt'):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    for m in re.finditer(r'(?m)^(\w+)\s*=\s*\{', t):
        k = m.group(1)
        if k.startswith('VIE_') and k not in loc_keys: missing.append(('dynamic_modifier', k, p))

# 3. Tooltips in all files
for p in glob.glob('common/**/*.txt', recursive=True) + glob.glob('events/*.txt'):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    # custom_trigger_tooltip
    for k in re.findall(r'custom_trigger_tooltip\s*=\s*\{\s*tooltip\s*=\s*([A-Za-z0-9_]+)', t):
        if k.startswith('VIE_') and k not in loc_keys: missing.append(('custom_trigger_tooltip', k, p))
    # custom_effect_tooltip
    for k in re.findall(r'custom_effect_tooltip\s*=\s*([A-Za-z0-9_]+)', t):
        if k.startswith('VIE_') and k not in loc_keys: missing.append(('custom_effect_tooltip', k, p))
    # tooltip = ...
    for k in re.findall(r'\btooltip\s*=\s*([A-Za-z0-9_]+)', t):
        if k.startswith('VIE_') and k not in loc_keys: missing.append(('tooltip', k, p))

# 4. Characters
for p in glob.glob('common/characters/*.txt'):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    for k in re.findall(r'name\s*=\s*([A-Za-z0-9_]+)', t):
        if k.startswith('VIE_') and k not in loc_keys: missing.append(('char_name', k, p))

# 5. Events
for p in glob.glob('events/*.txt'):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    # check options
    for k in re.findall(r'option\s*=\s*\{[^{}]*?name\s*=\s*([A-Za-z0-9_.]+)', t, re.S):
        if k not in loc_keys: missing.append(('event_option', k, p))
    for k in re.findall(r'title\s*=\s*([A-Za-z0-9_.]+)', t):
        if k not in loc_keys: missing.append(('event_title', k, p))
    for k in re.findall(r'desc\s*=\s*([A-Za-z0-9_.]+)', t):
        if k not in loc_keys: missing.append(('event_desc', k, p))

# 6. Decisions & categories
for p in glob.glob('common/decisions/**/*.txt', recursive=True):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    for k in re.findall(r'(?m)^([A-Za-z0-9_]+)\s*=\s*\{', t):
        if k.startswith('VIE_'):
            if k not in loc_keys: missing.append(('category_name', k, p))
            if (k + '_desc') not in loc_keys: missing.append(('category_desc', k + '_desc', p))
    for k in re.findall(r'(?m)^\t([A-Za-z0-9_]+)\s*=\s*\{', t):
        if k.startswith('VIE_'):
            if k not in loc_keys: missing.append(('decision_name', k, p))
            if (k + '_desc') not in loc_keys: missing.append(('decision_desc', k + '_desc', p))

# 7. GUI files
for p in glob.glob('interface/**/*.gui', recursive=True):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    for k in re.findall(r'pdx_tooltip\s*=\s*\"?([A-Za-z0-9_]+)\"?', t):
        if k.startswith('VIE_') and k not in loc_keys: missing.append(('gui_tooltip', k, p))
    for k in re.findall(r'text\s*=\s*\"([A-Za-z0-9_]+)\"', t):
        if k.startswith('VIE_') and k not in loc_keys: missing.append(('gui_text', k, p))

# 8. Scripted effects / triggers / on_actions
for p in glob.glob('common/scripted_effects/*.txt') + glob.glob('common/on_actions/*.txt'):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    for k in re.findall(r'custom_effect_tooltip\s*=\s*([A-Za-z0-9_]+)', t):
        if k.startswith('VIE_') and k not in loc_keys: missing.append(('scripted_effect_tt', k, p))

# Deduplicate
seen = set()
dedup = []
for typ, k, p in missing:
    if k not in seen:
        seen.add(k)
        dedup.append((typ, k, p))

print(f"\nTotal missing keys found: {len(dedup)}")
for typ, k, p in dedup:
    print(f"  [{typ}] {k} (from {p})")
