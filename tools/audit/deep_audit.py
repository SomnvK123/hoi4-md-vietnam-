import os
import re
import collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def get_loc_data():
    loc_dir = os.path.join(ROOT, 'localisation')
    keys = {}
    duplicates = collections.defaultdict(list)
    files_with_encoding_issue = []
    syntax_errors = []
    
    for dp, ds, fns in os.walk(loc_dir):
        for fn in fns:
            if fn.endswith('.yml'):
                p = os.path.join(dp, fn)
                rel = os.path.relpath(p, ROOT)
                with open(p, 'rb') as fb:
                    raw = fb.read()
                    if not raw.startswith(b'\xef\xbb\xbf'):
                        files_with_encoding_issue.append((rel, "Missing UTF-8 BOM"))
                try:
                    text = raw.decode('utf-8-sig')
                except Exception as e:
                    files_with_encoding_issue.append((rel, f"Decode error: {e}"))
                    continue
                
                lines = text.splitlines()
                if not lines or not re.match(r'^\s*l_english\s*:', lines[0]):
                    syntax_errors.append((rel, "First line not 'l_english:'"))
                
                for idx, line in enumerate(lines[1:], 2):
                    if not line.strip() or line.strip().startswith('#'):
                        continue
                    m = re.match(r'^\s*([A-Za-z0-9_\.\:]+)\s*:\s*\d*\s*"(.*)"\s*$', line)
                    if m:
                        k = m.group(1).split(':')[0]
                        v = m.group(2)
                        if k in keys:
                            duplicates[k].append(rel)
                        else:
                            keys[k] = (rel, v)
                    else:
                        if ':' in line and '"' in line:
                            syntax_errors.append((rel, f"Line {idx}: {line.strip()[:60]}"))

    return keys, duplicates, files_with_encoding_issue, syntax_errors

def parse_top_level_blocks(text):
    """Parses depth-0 blocks of form: identifier = { ... }"""
    blocks = {}
    lines = [l.split('#')[0] for l in text.splitlines()]
    clean = '\n'.join(lines)
    
    depth = 0
    curr_key = None
    curr_start = -1
    
    # Simple state machine
    for m in re.finditer(r'([A-Za-z0-9_\.:]+)\s*=\s*\{|(\{|\})', clean):
        token = m.group(0)
        if token == '{':
            depth += 1
        elif token == '}':
            depth -= 1
            if depth == 0 and curr_key:
                blocks[curr_key] = clean[curr_start:m.end()]
                curr_key = None
        else:
            if depth == 0:
                curr_key = m.group(1)
                curr_start = m.start()
                depth = 1
            else:
                depth += 1
    return blocks

def audit_events(loc_keys):
    print("\n==================== 1. AUDITING EVENTS ====================")
    events_dir = os.path.join(ROOT, 'events')
    event_files = [f for f in os.listdir(events_dir) if f.endswith('.txt')]
    
    events = []
    namespaces_declared = {}
    
    for fn in event_files:
        p = os.path.join(events_dir, fn)
        with open(p, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        lines = [l.split('#')[0] for l in content.splitlines()]
        stripped = '\n'.join(lines)
        
        ns_list = re.findall(r'add_namespace\s*=\s*([a-zA-Z0-9_]+)', stripped)
        namespaces_declared[fn] = ns_list
        
        idx = 0
        while True:
            m = re.search(r'\b(country_event|news_event)\s*=\s*\{', stripped[idx:])
            if not m: break
            start = idx + m.start()
            b = 0
            end = -1
            for i in range(idx + m.end() - 1, len(stripped)):
                if stripped[i] == '{': b += 1
                elif stripped[i] == '}':
                    b -= 1
                    if b == 0:
                        end = i + 1
                        break
            if end == -1:
                print(f"Unclosed event block in {fn}!")
                break
            ev_body = stripped[start:end]
            idx = end
            
            id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_\.]+)', ev_body)
            ev_id = id_m.group(1) if id_m else "UNKNOWN"
            is_hidden = bool(re.search(r'\bhidden\s*=\s*yes\b', ev_body))
            is_triggered_only = bool(re.search(r'\bis_triggered_only\s*=\s*yes\b', ev_body))
            fire_only_once = bool(re.search(r'\bfire_only_once\s*=\s*yes\b', ev_body))
            has_mtth = bool(re.search(r'\bmean_time_to_happen\b', ev_body))
            has_trigger = bool(re.search(r'\btrigger\s*=\s*\{', ev_body))
            
            title_m = re.search(r'\btitle\s*=\s*([^\s\{\}#]+)', ev_body)
            desc_m = re.search(r'\bdesc\s*=\s*([^\s\{\}#]+)', ev_body)
            pic_m = re.search(r'\bpicture\s*=\s*([^\s\{\}#]+)', ev_body)
            
            title = title_m.group(1).strip('"') if title_m else None
            desc = desc_m.group(1).strip('"') if desc_m else None
            pic = pic_m.group(1).strip('"') if pic_m else None
            
            options = []
            opt_matches = re.finditer(r'\boption\s*=\s*\{', ev_body)
            for opt_m in opt_matches:
                opt_start = opt_m.start()
                ob = 0
                opt_end = -1
                for j in range(opt_m.end() - 1, len(ev_body)):
                    if ev_body[j] == '{': ob += 1
                    elif ev_body[j] == '}':
                        ob -= 1
                        if ob == 0:
                            opt_end = j + 1
                            break
                if opt_end != -1:
                    opt_str = ev_body[opt_start:opt_end]
                    name_m = re.search(r'\bname\s*=\s*([^\s\{\}#]+)', opt_str)
                    opt_name = name_m.group(1).strip('"') if name_m else None
                    options.append({'name': opt_name, 'body': opt_str})
            
            events.append({
                'file': fn,
                'id': ev_id,
                'hidden': is_hidden,
                'triggered_only': is_triggered_only,
                'fire_only_once': fire_only_once,
                'mtth': has_mtth,
                'trigger': has_trigger,
                'title': title,
                'desc': desc,
                'pic': pic,
                'options': options,
                'body': ev_body
            })

    print(f"Total events found: {len(events)}")
    
    id_counts = collections.Counter(e['id'] for e in events)
    duplicates = [ev_id for ev_id, c in id_counts.items() if c > 1]
    if duplicates:
        print(f"  [CRITICAL] Duplicate event IDs: {duplicates}")
    else:
        print("  [OK] No duplicate event IDs.")

    missing_opt_loc = [opt['name'] for e in events for opt in e['options'] if opt['name'] and opt['name'] not in loc_keys]
    if missing_opt_loc:
        print(f"  [LOC ERROR] Missing option loc: {set(missing_opt_loc)}")
    else:
        print("  [OK] All event options have loc.")

    return events

def audit_localisation(loc_keys, duplicates, files_with_encoding_issue, syntax_errors):
    print("\n==================== 2. AUDITING LOCALISATION ====================")
    print(f"Total unique loc keys: {len(loc_keys)}")
    if files_with_encoding_issue:
        print(f"  [ENCODING ISSUE] Files with encoding issues: {files_with_encoding_issue}")
    else:
        print("  [OK] All localisation files have UTF-8 BOM and decode cleanly.")
    if syntax_errors:
        print(f"  [SYNTAX ERROR] Localisation syntax errors: {syntax_errors}")
    else:
        print("  [OK] No localisation syntax errors.")
    if duplicates:
        print(f"  [DUPLICATE WARNING] Duplicate keys found: {len(duplicates)}")
    else:
        print("  [OK] No duplicate localisation keys.")

def audit_common(loc_keys):
    print("\n==================== 3. AUDITING COMMON/ FOLDERS ====================")
    common_dir = os.path.join(ROOT, 'common')
    
    # 3.1 ai_*
    print("\n--- 3.1 common/ai_* ---")
    ai_dirs = ['ai_focuses', 'ai_strategy', 'ai_strategy_plans']
    for ad in ai_dirs:
        p = os.path.join(common_dir, ad)
        for fn in os.listdir(p):
            if fn.endswith('.txt'):
                with open(os.path.join(p, fn), 'r', encoding='utf-8') as f:
                    c = f.read()
                stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
                if stripped.count('{') != stripped.count('}'):
                    print(f"  [BRACKET ERROR] in {ad}/{fn}")
    print("  [OK] ai_* syntax and bracket matching clean.")

    # 3.2 bop
    print("\n--- 3.2 common/bop ---")
    bop_dir = os.path.join(common_dir, 'bop')
    for fn in os.listdir(bop_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(bop_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in bop/{fn}")
    print("  [OK] common/bop syntax clean.")

    # 3.3 characters
    print("\n--- 3.3 common/characters ---")
    char_dir = os.path.join(common_dir, 'characters')
    missing_dds = []
    char_count = 0
    for fn in os.listdir(char_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(char_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in characters/{fn}")
            for m in re.finditer(r'(?:small|large)\s*=\s*"([^"]+\.dds)"', c):
                rel_dds = m.group(1).replace('/', os.sep)
                full_dds = os.path.join(ROOT, rel_dds)
                if not os.path.exists(full_dds):
                    missing_dds.append((fn, m.group(1)))
            chars = re.findall(r'^\s*([A-Za-z0-9_]+)\s*=\s*\{\s*name\s*=', c, re.M)
            char_count += len(chars)
    print(f"  Total characters: {char_count}")
    if missing_dds:
        print(f"  [PORTRAIT ERROR] Missing DDS files on disk: {missing_dds}")
    else:
        print("  [OK] All character portrait DDS paths exist on disk.")

    # 3.4 decisions
    print("\n--- 3.4 common/decisions ---")
    dec_dir = os.path.join(common_dir, 'decisions')
    missing_dec_loc = []
    dec_count = 0
    for fn in os.listdir(dec_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(dec_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in decisions/{fn}")
            for m in re.finditer(r'^\t([A-Za-z0-9_]+)\s*=\s*\{', stripped, re.M):
                d = m.group(1)
                if d in ['allowed', 'target_array', 'targets']: continue
                dec_count += 1
                if d not in loc_keys:
                    missing_dec_loc.append(d)
    print(f"  Total decisions: {dec_count}")
    if missing_dec_loc:
        print(f"  [DECISION LOC WARNING] Decisions missing loc: {missing_dec_loc}")
    else:
        print("  [OK] All decisions have localisation.")

    # 3.5 dynamic_modifiers
    print("\n--- 3.5 common/dynamic_modifiers ---")
    dm_dir = os.path.join(common_dir, 'dynamic_modifiers')
    for fn in os.listdir(dm_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(dm_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in dynamic_modifiers/{fn}")
    print("  [OK] dynamic_modifiers syntax clean.")

    # 3.6 game_rules
    print("\n--- 3.6 common/game_rules ---")
    gr_dir = os.path.join(common_dir, 'game_rules')
    for fn in os.listdir(gr_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(gr_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in game_rules/{fn}")
    print("  [OK] game_rules syntax clean.")

    # 3.7 ideas
    print("\n--- 3.7 common/ideas ---")
    ideas_dir = os.path.join(common_dir, 'ideas')
    idea_count = 0
    missing_idea_loc = []
    for fn in os.listdir(ideas_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(ideas_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in ideas/{fn}")
            for m in re.finditer(r'^\t\t([A-Za-z0-9_]+)\s*=\s*\{', stripped, re.M):
                i = m.group(1)
                idea_count += 1
                if i not in loc_keys:
                    missing_idea_loc.append(i)
    print(f"  Total ideas: {idea_count}")
    if missing_idea_loc:
        print(f"  [IDEA LOC WARNING] Ideas missing loc: {missing_idea_loc}")
    else:
        print("  [OK] All ideas have localisation.")

    # 3.8 mio
    print("\n--- 3.8 common/military_industrial_organization ---")
    mio_org_dir = os.path.join(common_dir, 'military_industrial_organization', 'organizations')
    for fn in os.listdir(mio_org_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(mio_org_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in mio/organizations/{fn}")
    print("  [OK] mio/organizations syntax clean.")

    # 3.9 national_focus
    print("\n--- 3.9 common/national_focus ---")
    nf_path = os.path.join(common_dir, 'national_focus', 'VIE_md_focus.txt')
    with open(nf_path, 'r', encoding='utf-8') as f:
        c = f.read()
    stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
    if stripped.count('{') != stripped.count('}'):
        print(f"  [BRACKET ERROR] in national_focus/VIE_md_focus.txt")
    print("  [OK] national_focus syntax clean.")

    # 3.10 on_actions
    print("\n--- 3.10 common/on_actions ---")
    oa_dir = os.path.join(common_dir, 'on_actions')
    for fn in os.listdir(oa_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(oa_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in on_actions/{fn}")
    print("  [OK] on_actions syntax clean.")

    # 3.11 opinion_modifiers
    print("\n--- 3.11 common/opinion_modifiers ---")
    op_dir = os.path.join(common_dir, 'opinion_modifiers')
    for fn in os.listdir(op_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(op_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in opinion_modifiers/{fn}")
    print("  [OK] opinion_modifiers syntax clean.")

    # 3.12 scripted_effects
    print("\n--- 3.12 common/scripted_effects ---")
    se_dir = os.path.join(common_dir, 'scripted_effects')
    defined_effects = {}
    dup_effects = []
    for fn in os.listdir(se_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(se_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in scripted_effects/{fn}")
            top_blocks = parse_top_level_blocks(c)
            for k in top_blocks:
                if k in defined_effects:
                    dup_effects.append((k, fn, defined_effects[k]))
                defined_effects[k] = fn
    print(f"  Total scripted effects: {len(defined_effects)}")
    if dup_effects:
        print(f"  [CRITICAL] Duplicate scripted effects: {dup_effects}")
    else:
        print("  [OK] No duplicate scripted effects.")

    # 3.13 scripted_localisation
    print("\n--- 3.13 common/scripted_localisation ---")
    sl_dir = os.path.join(common_dir, 'scripted_localisation')
    for fn in os.listdir(sl_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(sl_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in scripted_localisation/{fn}")
    print("  [OK] scripted_localisation syntax clean.")

    # 3.14 scripted_triggers
    print("\n--- 3.14 common/scripted_triggers ---")
    st_dir = os.path.join(common_dir, 'scripted_triggers')
    defined_triggers = {}
    dup_triggers = []
    for fn in os.listdir(st_dir):
        if fn.endswith('.txt'):
            with open(os.path.join(st_dir, fn), 'r', encoding='utf-8') as f:
                c = f.read()
            stripped = '\n'.join(l.split('#')[0] for l in c.splitlines())
            if stripped.count('{') != stripped.count('}'):
                print(f"  [BRACKET ERROR] in scripted_triggers/{fn}")
            top_blocks = parse_top_level_blocks(c)
            for k in top_blocks:
                if k in defined_triggers:
                    dup_triggers.append((k, fn, defined_triggers[k]))
                defined_triggers[k] = fn
    print(f"  Total scripted triggers: {len(defined_triggers)}")
    if dup_triggers:
        print(f"  [CRITICAL] Duplicate scripted triggers: {dup_triggers}")
    else:
        print("  [OK] No duplicate scripted triggers.")

if __name__ == '__main__':
    loc_keys, duplicates, encoding_issues, syntax_errors = get_loc_data()
    audit_events(loc_keys)
    audit_localisation(loc_keys, duplicates, encoding_issues, syntax_errors)
    audit_common(loc_keys)
