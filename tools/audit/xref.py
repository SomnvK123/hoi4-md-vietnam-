import re, os, glob, collections, json
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
def read(p):
    with open(p,encoding='utf-8',errors='replace') as f: return f.read()
def strip_comments(t):
    return '\n'.join(l[:l.find('#')] if '#' in l else l for l in t.split('\n'))

files={}
for dirpath,dirs,fns in os.walk(ROOT):
    if '.git' in dirpath: continue
    for fn in fns:
        if fn.endswith(('.txt','.mod','.yml')):
            p=os.path.join(dirpath,fn)
            files[p]=read(p)

# ---------- collect DEFINITIONS ----------
defined={'idea':set(),'effect':set(),'trigger':set(),'event':set(),'decision':set(),
         'dec_cat':set(),'dyn_mod':set(),'opinion':set(),'game_rule':set(),'rule_opt':set(),
         'bop':set(),'bop_side':set(),'bop_range':set(),'mio':set(),'char':set(),'loc':set(),'gfx':set()}

def blocks(t, key, depth=None):
    """yield (name, body_text, line) for `name = {` blocks whose key context matches"""
    pass

# --- ideas: files in common/ideas; structure ideas = { <slot> = { NAME = { ... } } }
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'common','ideas')): continue
    tt=strip_comments(t)
    # idea names = blocks at depth 3 with picture/modifier etc.  Heuristic: lines with 3 tabs then NAME = {
    for m in re.finditer(r'^\t{3}([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M):
        defined['idea'].add(m.group(1))
    for m in re.finditer(r'^\t{2}([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M):
        defined['idea'].add(m.group(1))

# --- scripted effects
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'common','scripted_effects')): continue
    tt=strip_comments(t)
    for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['effect'].add(m.group(1))
# --- scripted triggers
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'common','scripted_triggers')): continue
    tt=strip_comments(t)
    for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['trigger'].add(m.group(1))
# --- decisions + categories
for p,t in files.items():
    if p.startswith(os.path.join(ROOT,'common','decisions','categories')):
        tt=strip_comments(t)
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['dec_cat'].add(m.group(1))
    elif p.startswith(os.path.join(ROOT,'common','decisions')):
        tt=strip_comments(t)
        cur=None
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{|^\t([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M):
            if m.group(1): cur=m.group(1); defined['dec_cat'].add(cur)
            else: defined['decision'].add(m.group(2))
# --- events
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'events')): continue
    tt=strip_comments(t)
    for m in re.finditer(r'^\s*id\s*=\s*([A-Za-z_0-9\.]+)', tt, re.M): defined['event'].add(m.group(1))
# --- dynamic modifiers
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'common','dynamic_modifiers')): continue
    tt=strip_comments(t)
    for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['dyn_mod'].add(m.group(1))
# --- opinion modifiers
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'common','opinion_modifiers')): continue
    tt=strip_comments(t)
    for m in re.finditer(r'^\t([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['opinion'].add(m.group(1))
# --- game rules
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'common','game_rules')): continue
    tt=strip_comments(t)
    for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['game_rule'].add(m.group(1))
    for m in re.finditer(r'^\t([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['rule_opt'].add(m.group(1))
# --- bop
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'common','bop')): continue
    tt=strip_comments(t)
    for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['bop'].add(m.group(1))
# --- MIO
for p,t in files.items():
    if 'military_industrial_organization' not in p: continue
    tt=strip_comments(t)
    for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{', tt, re.M): defined['mio'].add(m.group(1))
# --- localisation keys
for p,t in files.items():
    if not p.startswith(os.path.join(ROOT,'localisation')): continue
    for m in re.finditer(r'^\s*([A-Za-z_0-9\.\:]+)\s*:\s*\d', t, re.M): defined['loc'].add(m.group(1))
# --- gfx sprites
for dirpath,dirs,fns in os.walk(os.path.join(ROOT,'interface')):
    for fn in fns:
        if fn.endswith('.gfx'):
            tt=read(os.path.join(dirpath,fn))
            for m in re.finditer(r'name\s*=\s*"?([A-Za-z_0-9\./]+)"?', tt): defined['gfx'].add(m.group(1))

for k,v in defined.items(): print(f'defined {k}: {len(v)}')
json.dump({k:sorted(v) for k,v in defined.items()}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'defined.json'),'w'), indent=0)

# ---------- collect USAGE ----------
usage=collections.defaultdict(lambda: collections.defaultdict(list))
VIE=re.compile(r'\b(VIE_[A-Za-z_0-9]+)\b')
CALL_PATTERNS={
 'idea':      [r'\bhas_idea\s*=\s*(VIE_[A-Za-z_0-9]+)', r'\badd_ideas\s*=\s*(VIE_[A-Za-z_0-9]+)',
               r'\bremove_idea\s*=\s*(VIE_[A-Za-z_0-9]+)', r'\bswap_ideas\s*=\s*\{[^}]*?idea\s*=\s*(VIE_[A-Za-z_0-9]+)',
               r'\bremove_ideas\s*=\s*(VIE_[A-Za-z_0-9]+)', r'\badd_timed_idea\s*=\s*\{\s*idea\s*=\s*(VIE_[A-Za-z_0-9]+)'],
 'effect':    [r'^\s*(VIE_[A-Za-z_0-9]+)\s*=\s*yes\s*$'],
 'event':     [r'\bcountry_event\s*=\s*\{?\s*id\s*=\s*([a-z_0-9\.]+)', r'\bcountry_event\s*=\s*([a-z_0-9\.]+)',
               r'\bnews_event\s*=\s*\{?\s*id\s*=\s*([a-z_0-9\.]+)', r'\bid\s*=\s*(vie_[a-z_0-9\.]+)'],
 'decision':  [r'\bactivate_decision\s*=\s*(VIE_[A-Za-z_0-9]+)', r'\bhas_active_decision\s*=\s*(VIE_[A-Za-z_0-9]+)',
               r'\bremove_decision\s*=\s*(VIE_[A-Za-z_0-9]+)', r'\bhas_decision\s*=\s*(VIE_[A-Za-z_0-9]+)'],
 'dyn_mod':   [r'\badd_dynamic_modifier\s*=\s*\{\s*modifier\s*=\s*(VIE_[A-Za-z_0-9]+)', r'\bremove_dynamic_modifier\s*=\s*(VIE_[A-Za-z_0-9]+)'],
 'opinion':   [r'\badd_opinion_modifier\s*=\s*\{\s*target\s*=\s*[A-Z]+\s+modifier\s*=\s*(VIE_[A-Za-z_0-9]+)',
               r'\bremove_opinion\s*=\s*\{\s*target\s*=\s*[A-Z]+\s+modifier\s*=\s*(VIE_[A-Za-z_0-9]+)'],
 'game_rule': [r'\brule\s*=\s*(VIE_[A-Za-z_0-9]+)', r'\boption\s*=\s*(VIE_[A-Za-z_0-9]+)'],
}
for p,t in files.items():
    if p.startswith(os.path.join(ROOT,'localisation')): continue
    tt=strip_comments(t)
    rel=os.path.relpath(p,ROOT)
    for kind,pats in CALL_PATTERNS.items():
        for pat in pats:
            for m in re.finditer(pat, tt, re.M):
                name=m.group(1)
                if name=='fire_only_once': continue
                line=tt[:m.start()].count('\n')+1
                usage[kind][name].append((rel,line))

def report(kind, defkey, label):
    d=defined[defkey]
    used=usage.get(kind,{})
    miss={k:v for k,v in used.items() if k not in d}
    unused={k for k in d if k not in used and kind!='event'}
    print(f'\n=== [{label}] used={len(used)}  defined={len(d)}  MISSING DEF={len(miss)} ===')
    for k,v in sorted(miss.items()):
        locs=', '.join(f'{f}:{l}' for f,l in v[:4])
        print(f'  !! {k}  <- {locs}')
    return miss

miss={}
miss['idea']=report('idea','idea','IDEAS')
miss['effect']=report('effect','effect','SCRIPTED EFFECT CALLS (name = yes)')
miss['decision']=report('decision','decision','DECISIONS')
miss['dyn_mod']=report('dyn_mod','dyn_mod','DYNAMIC MODIFIERS')
miss['game_rule']=report('game_rule','game_rule','GAME RULES/OPTIONS')
# events
ev_used=usage.get('event',{})
ev_miss={k:v for k,v in ev_used.items() if k.startswith('vie_') and k not in defined['event']}
print(f'\n=== [EVENTS] fired-but-undefined: {len(ev_miss)} ===')
for k,v in sorted(ev_miss.items()):
    print(f'  !! {k} <- '+', '.join(f'{f}:{l}' for f,l in v[:4]))
json.dump({k:{kk:[list(x) for x in vv] for kk,vv in v.items()} for k,v in miss.items() if isinstance(v,dict)}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'missing.json'),'w'), indent=1, default=str)
