import re, os, sys, collections, json
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
ARCHIVE=('v10_removed_nationalist_focuses.txt','v30_removed_infrastructure_focuses.txt','v31_removed_industry_focuses.txt','v11_removed_military_all_subbranches.txt',
         'v11_removed_military_other_focuses.txt','common/national_focus/VIE_md_focus.txt.bak',
         'scratch/test_focus.txt')  # Non-loaded scratch copy; retain the user's file.
def read(p):
    with open(p,encoding='utf-8',errors='replace') as f: return f.read()
def strip(t): return '\n'.join(l[:l.find('#')] if '#' in l else l for l in t.split('\n'))
live={}
for dp,ds,fns in os.walk(ROOT):
    if '.git' in dp: continue
    for fn in fns:
        p=os.path.relpath(os.path.join(dp,fn),ROOT).replace(os.sep,'/')
        if p in ARCHIVE or p.endswith('.bak'): continue
        if fn.endswith(('.txt','.mod','.gfx')): live[p]=read(os.path.join(dp,fn))

# definitions
defs={'effect':set(),'trigger':set(),'idea':set(),'event':set(),'decision':set(),'dec_cat':set(),
      'dyn_mod':set(),'opinion':set(),'rule':set(),'rule_opt':set(),'bop':set(),'mio':set(),'loc':set(),'gfx':set(),'char':set(),'focus':set(),'state_mod':set()}
for p,t in live.items():
    tt=strip(t)
    if p.startswith('common/scripted_effects'):
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['effect'].add(m.group(1))
    if p.startswith('common/scripted_triggers'):
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['trigger'].add(m.group(1))
    if p.startswith('common/ideas'):
        for m in re.finditer(r'^\t{2,3}([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['idea'].add(m.group(1))
    if p.startswith('events'):
        for m in re.finditer(r'^\s*id\s*=\s*([a-zA-Z_0-9\.]+)',tt,re.M): defs['event'].add(m.group(1))
    if p.startswith('common/decisions/categories'):
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['dec_cat'].add(m.group(1))
    elif p.startswith('common/decisions'):
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{|^\t([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M):
            (defs['dec_cat'] if m.group(1) else defs['decision']).add(m.group(1) or m.group(2))
    if p.startswith('common/dynamic_modifiers'):
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['dyn_mod'].add(m.group(1))
    if p.startswith('common/opinion_modifiers'):
        for m in re.finditer(r'^\t([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['opinion'].add(m.group(1))
    if p.startswith('common/game_rules'):
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['rule'].add(m.group(1))
        for m in re.finditer(r'^\t\tname\s*=\s*([A-Za-z_0-9]+)',tt,re.M): defs['rule_opt'].add(m.group(1))
    if p.startswith('common/bop'):
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['bop'].add(m.group(1))
    if 'military_industrial_organization' in p:
        for m in re.finditer(r'^([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['mio'].add(m.group(1))
    if p.startswith('common/national_focus'):
        for m in re.finditer(r'^\t\tid\s*=\s*([A-Za-z_0-9]+)',tt,re.M): defs['focus'].add(m.group(1))
    if p.startswith('interface'):
        for m in re.finditer(r'name\s*=\s*"?([A-Za-z_0-9\./]+)',tt): defs['gfx'].add(m.group(1))
    if p.startswith('common/characters') or 'VIE_political_leaders' in p:
        for m in re.finditer(r'^\t([A-Za-z_0-9]+)\s*=\s*\{',tt,re.M): defs['char'].add(m.group(1))
for p in os.listdir(os.path.join(ROOT,'localisation','english')):
    pass
for dp,ds,fns in os.walk(os.path.join(ROOT,'localisation')):
    for fn in fns:
        if fn.endswith('.yml'):
            for m in re.finditer(r'^\s*([A-Za-z_0-9\.\:]+)\s*:\s*\d', read(os.path.join(dp,fn)), re.M):
                defs['loc'].add(m.group(1))
print('DEFS:', {k:len(v) for k,v in defs.items()})

CALLABLE = defs['effect']|defs['trigger']
usage=collections.defaultdict(lambda: collections.defaultdict(list))
PATS={
 'callable':[(r'^\s*(VIE_[A-Za-z_0-9]+)\s*=\s*yes\s*$','call')],
 'idea':[(r'\bhas_idea\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\badd_ideas\s*=\s*(VIE_[A-Za-z_0-9]+)',''),
         (r'\bremove_idea\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\bremove_ideas\s*=\s*(VIE_[A-Za-z_0-9]+)',''),
         (r'idea\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\brmb_idea\s*=\s*(VIE_[A-Za-z_0-9]+)',''),
         (r'\badd_idea\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'event':[(r'\bcountry_event\s*=\s*\{?\s*id\s*=\s*([a-z_0-9\.]+)',''),(r'\bnews_event\s*=\s*\{?\s*id\s*=\s*([a-z_0-9\.]+)',''),
          (r'\bid\s*=\s*(vie_[a-z_0-9\.]+)','')],
 'decision':[(r'\bactivate_decision\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\bhas_active_decision\s*=\s*(VIE_[A-Za-z_0-9]+)',''),
             (r'\bremove_decision\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\bhas_decision\s*=\s*(VIE_[A-Za-z_0-9]+)',''),
             (r'\bcomplete_decision\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'dec_cat':[(r'\bunlock_decision_category\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\badd_decision_category\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'dyn_mod':[(r'\b(?:add|has|remove)_dynamic_modifier\s*=\s*\{\s*modifier\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\bMODIFIER\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'opinion':[(r'modifier\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'rule':[(r'\brule\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'rule_opt':[(r'\boption\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'bop':[(r'\bpower_balance\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\bset_power_balance\s*=\s*\{\s*id\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'focus':[(r'\bhas_completed_focus\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\bunlocks_decision\s*=\s*(VIE_[A-Za-z_0-9]+)',''),
          (r'\bfocus\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\btarget\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'mio':[(r'\badd_mio\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\bmio\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\borganization\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
 'loc':[(r'tooltip\s*=\s*(VIE_[A-Za-z_0-9]+)',''),(r'\bcustom_effect_tooltip\s*=\s*(VIE_[A-Za-z_0-9]+)',''),
        (r'\bcustom_trigger_tooltip\s*=\s*\{\s*tooltip\s*=\s*(VIE_[A-Za-z_0-9]+)','')],
}
for p,t in live.items():
    if p.startswith('localisation'): continue
    tt=strip(t)
    for kind,pats in PATS.items():
        for pat,_ in pats:
            try:
                for m in re.finditer(pat,tt,re.M):
                    n=m.group(1)
                    usage[kind][n].append((p,tt[:m.start()].count('\n')+1))
            except re.error: pass

def chk(kind, defset, label, prefix=None):
    used=usage.get(kind,{})
    miss=collections.defaultdict(list)
    for n,locs in used.items():
        if prefix and not n.startswith(prefix): continue
        if n not in defset: miss[n]+=locs
    print(f'\n=== [{label}] used={len([k for k in used if not prefix or k.startswith(prefix)])} defined={len(defset)} MISSING={len(miss)} ===')
    for n,locs in sorted(miss.items()):
        print(f'  !! {n:45s} <- '+', '.join(f'{f}:{l}' for f,l in sorted(set(locs))[:5]))
    return miss

chk('callable',CALLABLE,'SCRIPTED EFFECT / TRIGGER CALLS (X = yes)')
chk('idea',defs['idea'],'IDEAS (add_ideas/has_idea/remove_idea)')
chk('decision',defs['decision'],'DECISIONS (activate/has/remove)')
chk('dec_cat',defs['dec_cat'],'DECISION CATEGORIES (unlock_decision_category)')
chk('dyn_mod',defs['dyn_mod'],'DYNAMIC MODIFIERS','VIE_')
chk('focus',defs['focus'],'FOCUS refs (has_completed_focus / shortcut target / prerequisite)')
chk('rule_opt',defs['rule_opt'],'GAME RULE OPTIONS')
chk('mio',defs['mio'],'MIO organizations')
chk('loc',defs['loc'],'LOC keys used as tooltip/custom_*_tooltip','VIE_')
ev=usage.get('event',{})
evmiss=collections.defaultdict(list)
for n,locs in ev.items():
    if n.startswith('vie_') and n not in defs['event']: evmiss[n]+=locs
print(f'\n=== [EVENTS] fired but undefined: {len(evmiss)} ===')
for n,locs in sorted(evmiss.items()): print(f'  !! {n:20s} <- '+', '.join(f'{f}:{l}' for f,l in sorted(set(locs))[:5]))

# defined-but-unused events. An event is "fired" if some OTHER event file body, a
# scripted effect, a decision or a focus references it. Chained events (.18 -> .19)
# count as fired, so exclude each event's own definition block before searching.
non_ev=' '.join(strip(t) for p,t in live.items() if not p.startswith('events'))
ev_all={p:strip(t) for p,t in live.items() if p.startswith('events')}
never=[]
for e in sorted(defs['event']):
    if not e.startswith('vie_'): continue
    if e in non_ev: continue
    # search inside events/ but skip lines that merely define the event
    hit=False
    for p,body in ev_all.items():
        for line in body.split('\n'):
            if e in line and not line.strip().startswith('id =') and not line.strip().startswith('log ='):
                hit=True; break
        if hit: break
    if not hit: never.append(e)
print(f'\n=== [EVENTS] defined but never fired anywhere (true orphans): {len(never)} ===')
print('   ', never)
# ideas defined but unused
ideatxt=' '.join(strip(t) for p,t in live.items() if not p.startswith('common/ideas'))
unidea=[i for i in sorted(defs['idea']) if i.startswith('VIE_') and i not in ideatxt]
print(f'\n=== [IDEAS] defined but never granted/referenced: {len(unidea)} ===')
print('   ', unidea)
