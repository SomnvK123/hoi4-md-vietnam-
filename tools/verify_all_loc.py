import os
import re

loc_dir = 'localisation/english'
files = []
for root, _, filenames in os.walk(loc_dir):
    for f in filenames:
        if f.endswith('.yml') or f.endswith('.yaml'):
            rel_path = os.path.relpath(os.path.join(root, f), loc_dir)
            files.append((rel_path, os.path.join(root, f)))

print(f"Checking {len(files)} localisation files in {loc_dir} (recursive):")
all_keys = set()
errors = []

for rel_p, p in sorted(files):
    fname = os.path.basename(p)
    # HOI4 requirement: must end with _l_english.yml
    if not fname.endswith('_l_english.yml'):
        errors.append(f"{rel_p}: Filename DOES NOT end with '_l_english.yml' (HOI4 will ignore it!)")
        
    with open(p, 'rb') as raw:
        b = raw.read(3)
        has_bom = (b == b'\xef\xbb\xbf')
    if not has_bom:
        errors.append(f"{rel_p}: missing UTF-8 BOM")
        
    with open(p, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()
        
    first_line = lines[0].strip() if lines else ""
    if first_line != 'l_english:':
        errors.append(f"{rel_p}: first line is '{first_line}', expected 'l_english:'")
        
    file_keys = 0
    for idx, line in enumerate(lines, 1):
        m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(\d*)\s*\"(.*)\"\s*$', line)
        if m:
            key = m.group(1)
            all_keys.add(key)
            file_keys += 1
        elif line.strip() and not line.strip().startswith('#') and line.strip() != 'l_english:':
            errors.append(f"{rel_p}:{idx}: malformed line -> {line.strip()}")
            
    print(f"  {rel_p:45s}: OK ({file_keys} keys)")

print(f"\nTotal unique keys loaded: {len(all_keys)}")
if errors:
    print(f"\nFound {len(errors)} errors:")
    for err in errors:
        print(f"  ERROR: {err}")
else:
    print("\nAll localisation files passed with ZERO errors!")

# Now check focus tree keys
focus_file = 'common/national_focus/VIE_md_focus.txt'
with open(focus_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Only match focus ids inside focus = { ... }
focus_blocks = re.findall(r'focus\s*=\s*\{([^{}]*?id\s*=\s*([A-Za-z0-9_]+))', text)
focus_ids = [m[1] for m in focus_blocks if m[1].startswith('VIE_') and m[1] != 'VIE_md_focus']

missing_focus = []
missing_desc = []
for fid in set(focus_ids):
    if fid not in all_keys:
        missing_focus.append(fid)
    if f"{fid}_desc" not in all_keys:
        missing_desc.append(f"{fid}_desc")

print(f"\nFocus tree check: {len(set(focus_ids))} focuses found.")
print(f"Missing focus name keys: {len(missing_focus)}")
print(f"Missing focus desc keys: {len(missing_desc)}")
if missing_focus:
    print("  Sample missing focus:", missing_focus[:5])
if missing_desc:
    print("  Sample missing desc:", missing_desc[:5])
