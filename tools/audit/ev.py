import re,os,collections
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
ARCH={'v10_removed_nationalist_focuses.txt','v11_removed_military_all_subbranches.txt','v11_removed_military_other_focuses.txt'}
def read(p):
    return open(p,encoding='utf-8',errors='replace').read()
def strip(t): return '\n'.join(l[:l.find('#')] if '#' in l else l for l in t.split('\n'))
live={}
for dp,ds,fns in os.walk(ROOT):
    if '.git' in dp: continue
    for fn in fns:
        rel=os.path.relpath(os.path.join(dp,fn),ROOT)
        if rel in ARCH or rel.endswith('.bak'): continue
        if fn.endswith(('.txt','.mod','.gfx')): live[rel]=read(os.path.join(dp,fn))
# event ids + namespaces
ids={}; ns=collections.defaultdict(list)
for p,t in live.items():
    if not p.startswith('events'): continue
    tt=strip(t)
    # chi lay id cua country_event / news_event; bo qua 'id =' cua set_power_balance,
    # create_faction, ... (tranh duong tinh gia nhu VIE_party_balance)
    for m in re.finditer(r'(?:country_event|news_event)\s*=\s*\{\s*\n\s*id\s*=\s*([a-zA-Z_0-9\.]+)',tt):
        ids.setdefault(m.group(1),[]).append(p)
    for m in re.finditer(r'add_namespace\s*=\s*([a-z_0-9]+)',tt): ns[m.group(1)].append(p)
print('namespaces declared:',dict(ns))
print('event ids:',len(ids))
dup={k:v for k,v in ids.items() if len(v)>1}
print('DUPLICATE event ids:',dup)
# events with no namespace in their file
byfile=collections.defaultdict(set)
for e,ps in ids.items():
    for p in ps: byfile[p].add(e)
for p,evs in byfile.items():
    tt=strip(live[p])
    has_ns='add_namespace' in tt
    pref={e.split('.')[0] for e in evs}
    print(f'  {p}: {len(evs)} events, prefixes={sorted(pref)}, add_namespace={has_ns}')
# references to each event id anywhere (excluding its own definition line)
refs=collections.Counter()
for p,t in live.items():
    tt=strip(t)
    for e in ids:
        # count occurrences beyond definition
        c=len(re.findall(r'\b'+re.escape(e)+r'\b',tt))
        if p in ids[e]: c-=1
        if c>0: refs[e]+=c
never=[e for e in sorted(ids) if refs[e]==0]
print(f'\nEVENTS never referenced anywhere (defined only): {len(never)}')
print(never)
# event files' loc coverage
loc=set()
for dp,ds,fns in os.walk(os.path.join(ROOT,'localisation')):
    for fn in fns:
        if fn.endswith('.yml'):
            for m in re.finditer(r'^\s*([A-Za-z_0-9\.\:]+)\s*:\s*\d',read(os.path.join(dp,fn)),re.M): loc.add(m.group(1))
# hidden = yes event khong can title/desc (engine tu chon option dau neu co)
hidden=set()
for p,t in live.items():
    if not p.startswith('events'): continue
    tt=strip(t)
    # lay 400 ky tu sau id de tim 'hidden = yes'; khong can khop dau } vi
    # immediate/options co nhieu } long nhau, khop som se hut hidden event
    for m in re.finditer(r'(?:country_event|news_event)\s*=\s*\{\s*\n\s*id\s*=\s*([a-zA-Z_0-9\.]+)([\s\S]{0,400})',tt):
        if 'hidden = yes' in m.group(2): hidden.add(m.group(1))
noloc=[e for e in sorted(ids) if e not in hidden and (e+'.t' not in loc and e+'.d' not in loc and e+'.a' not in loc)]
print(f'\nEVENTS missing title/desc/option loc: {len(noloc)}  (hidden events excluded: {len(hidden)})')
print(noloc)
