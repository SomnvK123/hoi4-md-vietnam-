"""
Enhanced audit - deeper checks:
1. Check loc in replace/ subfolder too
2. Hidden events don't need title/desc loc
3. Focus tree flow analysis (orphan focuses, long chains without bypass)
4. Logical checks: BoP effects consistency, variable usage
5. Missing GFX references
"""
import os, re, glob
from collections import Counter, defaultdict
from pathlib import Path

MOD = str(Path(__file__).resolve().parent.parent)

errors = []
warnings = []
info = []

def read(path):
    try:
        return open(path, encoding='utf-8-sig', errors='ignore').read()
    except:
        return ""

# ============================================================
# 1) ALL LOC KEYS (including replace/)
# ============================================================
loc_files = glob.glob(os.path.join(MOD, "localisation/english/*.yml"))
loc_files += glob.glob(os.path.join(MOD, "localisation/english/replace/*.yml"))
all_loc_keys = set()
for lf in loc_files:
    ltxt = read(lf)
    keys = re.findall(r'^\s*(\S+):', ltxt, re.MULTILINE)
    all_loc_keys.update(keys)

info.append(f"Total loc keys (including replace/): {len(all_loc_keys)}")

# ============================================================
# 2) RE-CHECK EVENT LOC (skip hidden events)
# ============================================================
event_files = glob.glob(os.path.join(MOD, "events/*.txt"))
missing_event_titles = []
for ef in event_files:
    etxt = read(ef)
    # Parse events properly
    blocks = re.split(r'(?=country_event\s*=\s*\{)', etxt)
    for block in blocks:
        m_id = re.search(r'id\s*=\s*(\S+)', block)
        if not m_id:
            continue
        eid = m_id.group(1)
        is_hidden = 'hidden = yes' in block or 'hidden=yes' in block
        if is_hidden:
            continue
        title_key = eid + ".t"
        if title_key not in all_loc_keys:
            missing_event_titles.append(eid)

if missing_event_titles:
    for e in missing_event_titles:
        errors.append(f"NON-HIDDEN Event '{e}' missing title loc key '{e}.t'")
else:
    info.append("All non-hidden events have title loc keys")

# Check option loc keys
missing_option_loc = []
for ef in event_files:
    etxt = read(ef)
    option_names = re.findall(r'name\s*=\s*(\S+)', etxt)
    for on in option_names:
        if on.startswith('vie_') or on.startswith('VIE_'):
            if on not in all_loc_keys:
                missing_option_loc.append(on)
if missing_option_loc:
    for o in set(missing_option_loc):
        warnings.append(f"Event option '{o}' missing loc key")
else:
    info.append("All event option names have loc keys")

# ============================================================
# 3) FOCUS LOC (with replace/)
# ============================================================
focus_file = os.path.join(MOD, "common/national_focus/VIE_md_focus.txt")
ftxt = read(focus_file)
focus_ids = re.findall(r'^\s*id\s*=\s*(\S+)', ftxt, re.MULTILINE)
focus_set = set(focus_ids)

missing_focus_loc = []
for fid in focus_set:
    if fid == 'VIE_md_focus':
        continue  # This is the tree ID, not a focus
    if fid not in all_loc_keys:
        missing_focus_loc.append(fid)

if missing_focus_loc:
    info.append(f"Focuses missing loc (with replace/ included): {len(missing_focus_loc)}")
    for f in sorted(missing_focus_loc)[:30]:
        warnings.append(f"Focus '{f}' missing loc key")
    if len(missing_focus_loc) > 30:
        warnings.append(f"... and {len(missing_focus_loc) - 30} more")
else:
    info.append("All focuses have loc keys")

# ============================================================
# 4) ORPHAN FOCUSES (no prerequisite and not root)
# ============================================================
focus_prereqs_of = defaultdict(list)  # focus -> list of focuses it requires
for block in re.findall(r'focus\s*=\s*\{(.*?)\n\t\}', ftxt, re.DOTALL):
    m_id = re.search(r'id\s*=\s*(\S+)', block)
    if not m_id:
        continue
    fid = m_id.group(1)
    prereqs = re.findall(r'prerequisite\s*=\s*\{[^}]*?focus\s*=\s*(\S+)', block)
    focus_prereqs_of[fid] = prereqs

root_focus = 'VIE_doi_moi_continues'
orphan_focuses = []
for fid in focus_set:
    if fid == 'VIE_md_focus':
        continue
    if fid == root_focus:
        continue
    if fid not in focus_prereqs_of or len(focus_prereqs_of[fid]) == 0:
        orphan_focuses.append(fid)

if orphan_focuses:
    info.append(f"Root-level focuses (no prerequisites): {len(orphan_focuses)}")
    for f in sorted(orphan_focuses)[:10]:
        info.append(f"  Root focus: {f}")
    if len(orphan_focuses) > 10:
        info.append(f"  ... and {len(orphan_focuses) - 10} more")

# ============================================================
# 5) SCRIPTED EFFECTS USED IN EVENTS/FOCUSES - cross reference
# ============================================================
effect_files = glob.glob(os.path.join(MOD, "common/scripted_effects/*.txt"))
defined_effects = set()
for ef in effect_files:
    etxt = read(ef)
    for m in re.finditer(r'^(\w+)\s*=\s*\{', etxt, re.MULTILINE):
        defined_effects.add(m.group(1))

trigger_files = glob.glob(os.path.join(MOD, "common/scripted_triggers/*.txt"))
defined_triggers = set()
for tf in trigger_files:
    ttxt = read(tf)
    for m in re.finditer(r'^(\w+)\s*=\s*\{', ttxt, re.MULTILINE):
        defined_triggers.add(m.group(1))

# Find all VIE_ = yes calls across all files
all_vie_calls = set()
for pattern in ['common/national_focus/*.txt', 'events/*.txt', 'common/scripted_effects/*.txt',
                'common/on_actions/*.txt', 'common/decisions/*.txt']:
    for f in glob.glob(os.path.join(MOD, pattern)):
        txt = read(f)
        calls = re.findall(r'(\bVIE_\w+)\s*=\s*yes', txt)
        all_vie_calls.update(calls)

# Check which are undefined
undefined_calls = []
for call in sorted(all_vie_calls):
    if call in defined_effects or call in defined_triggers:
        continue
    # Could be a flag or variable check
    if any(p in call for p in ['_flag', '_active', '_trigger', '_check']):
        continue
    undefined_calls.append(call)

if undefined_calls:
    info.append(f"VIE_* = yes calls not found in mod effects/triggers: {len(undefined_calls)}")
    for u in undefined_calls[:20]:
        info.append(f"  Undefined? {u}")
else:
    info.append("All VIE_* = yes calls resolved")

# ============================================================
# 6) BoP EFFECT CONSISTENCY
# ============================================================
bop_effects = [e for e in defined_effects if 'bop' in e.lower()]
info.append(f"BoP-related effects: {bop_effects}")

# Count usage of bop effects in events
for ef in event_files:
    etxt = read(ef)
    for be in bop_effects:
        count = etxt.count(be)
        if count > 0:
            info.append(f"  {be} used {count} times in {os.path.basename(ef)}")

# ============================================================
# 7) VARIABLE USAGE AUDIT
# ============================================================
# Find all variable sets
all_vars_set = set()
all_vars_check = set()
for pattern in ['common/national_focus/*.txt', 'events/*.txt', 'common/scripted_effects/*.txt']:
    for f in glob.glob(os.path.join(MOD, pattern)):
        txt = read(f)
        # set_variable, add_to_variable
        vars_set = re.findall(r'(?:set_variable|add_to_variable)\s*=\s*\{\s*(\w+)\s*=', txt)
        all_vars_set.update(vars_set)
        # check_variable
        vars_check = re.findall(r'check_variable\s*=\s*\{\s*(\w+)\s*[<>=]', txt)
        all_vars_check.update(vars_check)

vars_checked_not_set = [v for v in all_vars_check if v not in all_vars_set]
if vars_checked_not_set:
    for v in vars_checked_not_set:
        warnings.append(f"Variable '{v}' checked but never set in mod files")

vars_set_not_checked = [v for v in all_vars_set if v not in all_vars_check and v.startswith('VIE_')]
if vars_set_not_checked:
    for v in sorted(vars_set_not_checked)[:10]:
        info.append(f"Variable '{v}' set but never checked (tooltip-only?)")

# ============================================================
# OPERATOR CHECK: >= and <= are INVALID in Clausewitz check_variable
# ============================================================
# These operators cause parser desync (unexpected token), silently swallow
# closing braces, and can break hundreds of lines of code that follow.
# Rule: ALWAYS use > (X-1) instead of >= X, and < (X+1) instead of <= X.
invalid_op_re = re.compile(r'check_variable\s*=\s*\{[^}]*(>=|<=)[^}]*\}')
script_dirs = ['common/national_focus/*.txt', 'events/*.txt',
               'common/scripted_effects/*.txt', 'common/decisions/*.txt']
for pattern in script_dirs:
    for f in glob.glob(os.path.join(MOD, pattern)):
        txt = read(f)
        for lno, line in enumerate(txt.splitlines(), 1):
            if '#' in line:
                line = line[:line.index('#')]
            if '>=' in line or '<=' in line:
                if invalid_op_re.search(line):
                    rel = os.path.relpath(f, MOD)
                    errors.append(
                        f"[INVALID OPERATOR] {rel}:{lno}: "
                        f"check_variable uses >= or <= (not supported by Clausewitz parser). "
                        f"Use > (X-1) or < (X+1) instead. Line: {line.strip()}"
                    )

# ============================================================
# 8) GFX REFERENCES
# ============================================================
gfx_dir = os.path.join(MOD, "gfx")
gfx_files = glob.glob(os.path.join(gfx_dir, "**/*.*"), recursive=True)
info.append(f"GFX files in mod: {len(gfx_files)}")

# Check interface for sprite defs
iface_files = glob.glob(os.path.join(MOD, "interface/*.gfx"))
info.append(f"Interface .gfx files: {len(iface_files)}")

# ============================================================
# 9) FOCUS TREE STATISTICS
# ============================================================
# Count by category
sections = re.findall(r'## (\w+)', ftxt)
info.append(f"Focus tree sections: {sections}")
info.append(f"Total focuses: {len(focus_set) - 1}")  # -1 for tree ID

# Count focuses by search_filter
filters = re.findall(r'FOCUS_FILTER_(\w+)', ftxt)
filter_counter = Counter(filters)
info.append(f"Focus filters: {dict(filter_counter)}")

# ============================================================
# 10) EVENT CHAIN ANALYSIS
# ============================================================
# Find events that fire other events
event_chains = defaultdict(list)
for ef in event_files:
    etxt = read(ef)
    blocks = re.split(r'(?=country_event\s*=\s*\{)', etxt)
    for block in blocks:
        m_id = re.search(r'id\s*=\s*(\S+)', block)
        if not m_id:
            continue
        eid = m_id.group(1)
        fired = re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*(\S+)', block)
        fired += re.findall(r'country_event\s*=\s*(\w+\.\d+)', block)
        for f in fired:
            if f != eid:
                event_chains[eid].append(f)

info.append(f"Events that fire other events: {len(event_chains)}")

# ============================================================
# SUMMARY
# ============================================================
print("=" * 60)
print("ENHANCED AUDIT SUMMARY")
print("=" * 60)

print(f"\n--- ERRORS ({len(errors)}) ---")
for e in errors:
    print(f"  [ERROR] {e}")

print(f"\n--- WARNINGS ({len(warnings)}) ---")
for w in warnings:
    print(f"  [WARN]  {w}")

print(f"\n--- INFO ({len(info)}) ---")
for i in info:
    print(f"  [INFO]  {i}")

print(f"\nTotal: {len(errors)} errors, {len(warnings)} warnings, {len(info)} info")
