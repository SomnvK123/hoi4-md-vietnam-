import os, re, glob

ROOT = r'd:/HOI4Mods/md_vietnam'
os.chdir(ROOT)

# 1. Load all localisation keys and their values
loc_files = glob.glob('localisation/english/**/*.yml', recursive=True)
loc_data = {} # key -> (file, val)
all_keys = set()

for lf in loc_files:
    with open(lf, 'r', encoding='utf-8-sig', errors='ignore') as f:
        for idx, line in enumerate(f, 1):
            m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(\d*)\s*\"(.*)\"\s*$', line)
            if m:
                k = m.group(1)
                v = m.group(3)
                all_keys.add(k)
                # If in replace/, it overrides
                if 'replace' in lf or k not in loc_data:
                    loc_data[k] = (lf, v)

print(f"Total localisation files: {len(loc_files)}")
print(f"Total unique keys: {len(all_keys)}")

# 2. Check Ideas
ideas = set()
for p in glob.glob('common/ideas/*.txt'):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        t = f.read()
    # Match ideas under country = { ... } or similar
    matches = re.findall(r'\n\t\t([A-Za-z0-9_]+)\s*=\s*\{', t)
    for m in matches:
        if m.startswith('VIE_'):
            ideas.add(m)

missing_ideas = []
for i in sorted(ideas):
    if i not in all_keys:
        missing_ideas.append((i, 'name'))
    if f"{i}_desc" not in all_keys:
        missing_ideas.append((f"{i}_desc", 'desc'))

print(f"\n--- IDEAS CHECK ({len(ideas)} ideas) ---")
print(f"Missing idea keys: {len(missing_ideas)}")
for k, t in missing_ideas[:20]:
    print(f"  Missing {t}: {k}")

# 3. Check Events (titles, descs, options)
missing_events = []
event_files = glob.glob('events/*.txt')
for ep in event_files:
    with open(ep, 'r', encoding='utf-8-sig', errors='ignore') as f:
        text = f.read()
    # Event ids
    for ev_m in re.finditer(r'(country_event|news_event)\s*=\s*\{([^}]*)\}', text):
        blk = ev_m.group(2)
        eid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_.]+)', blk)
        if not eid: continue
        eid = eid.group(1)
        # title
        tm = re.search(r'\btitle\s*=\s*([a-zA-Z0-9_.]+)', blk)
        if tm:
            tk = tm.group(1)
            if tk not in all_keys: missing_events.append((ep, tk, 'event_title'))
        # desc
        dm = re.search(r'\bdesc\s*=\s*([a-zA-Z0-9_.]+)', blk)
        if dm:
            dk = dm.group(1)
            if dk not in all_keys: missing_events.append((ep, dk, 'event_desc'))
        # options
        for opt in re.findall(r'option\s*=\s*\{[^{}]*name\s*=\s*([a-zA-Z0-9_.]+)', blk):
            if opt not in all_keys: missing_events.append((ep, opt, 'event_option'))

print(f"\n--- EVENTS CHECK ---")
print(f"Missing event keys: {len(missing_events)}")
for ep, k, t in missing_events[:20]:
    print(f"  [{ep}] Missing {t}: {k}")

# 4. Check Decisions
missing_decisions = []
for dp in glob.glob('common/decisions/**/*.txt', recursive=True):
    with open(dp, 'r', encoding='utf-8-sig', errors='ignore') as f:
        text = f.read()
    # categories
    for cat in re.findall(r'(?m)^(VIE_[A-Za-z0-9_]+)\s*=\s*\{', text):
        if cat not in all_keys: missing_decisions.append((dp, cat, 'category_name'))
        if f"{cat}_desc" not in all_keys: missing_decisions.append((dp, f"{cat}_desc", 'category_desc'))
    # decisions inside categories
    for dec in re.findall(r'(?m)^\t(VIE_[A-Za-z0-9_]+)\s*=\s*\{', text):
        if dec not in all_keys: missing_decisions.append((dp, dec, 'decision_name'))
        if f"{dec}_desc" not in all_keys: missing_decisions.append((dp, f"{dec}_desc", 'decision_desc'))

print(f"\n--- DECISIONS CHECK ---")
print(f"Missing decision keys: {len(missing_decisions)}")
for dp, k, t in missing_decisions[:20]:
    print(f"  [{dp}] Missing {t}: {k}")

# 5. Check Tooltips and Dynamic Modifiers
missing_tooltips = []
for p in glob.glob('common/**/*.txt', recursive=True) + glob.glob('events/*.txt'):
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as f:
        text = f.read()
    for tt in re.findall(r'\btooltip\s*=\s*(VIE_[A-Za-z0-9_]+)', text):
        if tt not in all_keys: missing_tooltips.append((p, tt, 'tooltip'))
    for tt in re.findall(r'custom_trigger_tooltip\s*=\s*\{\s*tooltip\s*=\s*(VIE_[A-Za-z0-9_]+)', text):
        if tt not in all_keys: missing_tooltips.append((p, tt, 'custom_trigger_tooltip'))
    for tt in re.findall(r'custom_effect_tooltip\s*=\s*(VIE_[A-Za-z0-9_]+)', text):
        if tt not in all_keys: missing_tooltips.append((p, tt, 'custom_effect_tooltip'))

print(f"\n--- TOOLTIPS CHECK ---")
print(f"Missing tooltips: {len(missing_tooltips)}")
for p, k, t in missing_tooltips[:20]:
    print(f"  [{p}] Missing {t}: {k}")

# 6. Check for English strings in keys that start with VIE_
english_looking = []
english_indicators = [
    r'\bthe\b', r'\band\b', r'\bwith\b', r'\bfor\b', r'\bfrom\b', r'\bthat\b',
    r'\bthis\b', r'\bwill\b', r'\bThe\b', r'\bThis\b', r'\bWe\b', r'\bOur\b'
]
vietnamese_diacritics = set("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ")

for k, (f, v) in loc_data.items():
    if k.startswith('VIE_') or k.startswith('vie_'):
        # Check if value has NO vietnamese diacritics and has english indicator words
        has_vn = any(c in vietnamese_diacritics for c in v)
        if not has_vn and len(v.split()) > 3:
            for ind in english_indicators:
                if re.search(ind, v, re.IGNORECASE):
                    english_looking.append((k, f, v))
                    break

print(f"\n--- UNTRANSLATED (ENGLISH) STRINGS CHECK ---")
print(f"Total English-looking VIE_ keys: {len(english_looking)}")
for k, f, v in english_looking[:30]:
    print(f"  {k} in {f}:\n    \"{v}\"")
