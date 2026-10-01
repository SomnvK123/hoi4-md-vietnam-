import re, os, glob, collections, json, sys
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
def read(p):
    with open(p, encoding='utf-8', errors='replace') as f: return f.read()
def strip_comments(t):
    return '\n'.join(l[:l.find('#')] if '#' in l else l for l in t.split('\n'))
def tokenize(t):
    toks=[]; i=0; n=len(t); line=1
    while i<n:
        c=t[i]
        if c=='\n': line+=1; i+=1; continue
        if c in ' \t\r': i+=1; continue
        if c=='{': toks.append(('{',line)); i+=1; continue
        if c=='}': toks.append(('}',line)); i+=1; continue
        if c=='=':
            if t[i+1:i+2]=='=': toks.append(('==',line)); i+=2; continue
            toks.append(('=',line)); i+=1; continue
        if c in '<>':
            if t[i+1:i+2]=='=': toks.append((c+'=',line)); i+=2; continue
            toks.append((c,line)); i+=1; continue
        if c=='"':
            j=t.find('"',i+1)
            if j<0: j=n
            toks.append(('STR',line,t[i+1:j])); i=j+1; continue
        j=i
        while j<n and t[j] not in ' \t\r\n{}=<>"': j+=1
        toks.append(('W',line,t[i:j])); i=j
    return toks

def parse(toks):
    """returns nested: list of (key, value, line) where value is str (W/STR) or list (block)."""
    pos=0
    def parse_block():
        nonlocal pos
        items=[]
        while pos<len(toks) and toks[pos][0]!='}':
            t=toks[pos]
            if t[0] in ('W','STR'):
                key=t[2]
                if pos+1<len(toks) and toks[pos+1][0] in ('=','==','<','>','<=','>='):
                    op=toks[pos+1][0]; pos+=2
                    if pos<len(toks) and toks[pos][0]=='{':
                        pos+=1; val=parse_block()
                        if pos<len(toks) and toks[pos][0]=='}': pos+=1
                    elif pos<len(toks):
                        val=(toks[pos][2] if toks[pos][0] in ('W','STR') else toks[pos][0]); pos+=1
                    else: val=None
                    items.append((key,op,val,t[1]))
                else:
                    pos+=1
                    items.append((key,'',None,t[1]))
            elif t[0]=='{':
                pos+=1; val=parse_block()
                if pos<len(toks) and toks[pos][0]=='}': pos+=1
                items.append(('<anon>','',val,t[1]))
            else:
                pos+=1
        return items
    return parse_block()

def walk(items):
    for k,op,v,l in items:
        yield k,op,v,l

ftxt=strip_comments(read(f'{ROOT}/common/national_focus/VIE_md_focus.txt'))
tree=parse(tokenize(ftxt))
# find focus_tree block
ft=None
for k,op,v,l in tree:
    if k=='focus_tree': ft=v
focus_blocks=[]
shortcuts=[]
for k,op,v,l in ft:
    if k=='focus': focus_blocks.append((v,l))
    elif k=='shortcut': shortcuts.append((v,l))
def getf(block,key):
    for k,op,v,l in block:
        if k==key: return v
    return None
focuses={}
order=[]
for b,l in focus_blocks:
    fid=getf(b,'id')
    if fid is None: continue
    if fid in focuses:
        print('DUPLICATE focus id:',fid,'line',l,'and',focuses[fid]['line'])
        continue
    focuses[fid]={'line':l,'block':b}
    order.append(fid)
print(f'FOCUSES parsed: {len(focuses)}   shortcuts: {len(shortcuts)}')
# shortcut targets
stargets=[getf(b,'target') for b,l in shortcuts]
fset=set(focuses)
for b,l in shortcuts:
    tg=getf(b,'target')
    if tg not in fset: print('  !! shortcut target missing:',tg,'line',l)
isp=getf(ft,'initial_show_position')
print('initial_show_position:',isp)

def collect_focus_names(v):
    names=[]
    def rec(x):
        if isinstance(x,list):
            for k,op,val,l in x:
                if k=='focus' and isinstance(val,str): names.append(val)
                elif isinstance(val,list): rec(val)
                elif k in ('has_completed_focus',):
                    if isinstance(val,str): names.append(val)
        return
    rec(v); return names

dang=collections.defaultdict(list)
attrs={}
for fid,info in focuses.items():
    b=info['block']
    a={'prereq':[],'anchor':None,'mx':[],'x':None,'y':None,'cost':None,'icon':None,'line':info['line'],
       'has_available':False,'has_bypass':False,'has_reward':False,'has_ai':False,'avail_focus_refs':[]}
    for k,op,v,l in b:
        if k=='prerequisite':
            for n in re.findall(r'focus\s*=\s*([A-Za-z_0-9]+)', ''): pass
            txt=json.dumps(v)
            a['prereq']+=re.findall(r'(?:^|[\s"])focus"?\s*,\s*"?\s*"?([A-Za-z_0-9]+)', txt) or []
            # robust: walk
            names=[]
            def rec(x):
                if isinstance(x,list):
                    for kk,oo,vv,ll in x:
                        if kk=='focus' and isinstance(vv,str): names.append(vv)
                        else: rec(vv)
            rec(v); a['prereq']=names
        elif k=='relative_position_id' and isinstance(v,str): a['anchor']=v
        elif k=='mutually_exclusive':
            names=[]
            def rec2(x):
                if isinstance(x,list):
                    for kk,oo,vv,ll in x:
                        if kk=='focus' and isinstance(vv,str): names.append(vv)
                        else: rec2(vv)
            rec2(v); a['mx']=names
        elif k=='x' and isinstance(v,str) and v.lstrip('-').isdigit(): a['x']=int(v)
        elif k=='y' and isinstance(v,str) and v.lstrip('-').isdigit(): a['y']=int(v)
        elif k=='cost' and isinstance(v,str): a['cost']=v
        elif k=='icon' and isinstance(v,str): a['icon']=v
        elif k=='available': a['has_available']=True
        elif k=='bypass': a['has_bypass']=True
        elif k=='completion_reward': a['has_reward']=True
        elif k=='ai_will_do': a['has_ai']=True
    # focus names referenced inside available (has_completed_focus)
    txt=json.dumps(a and b, default=str)
    a['avail_focus_refs']=sorted(set(re.findall(r'"has_completed_focus",\s*"",\s*"([A-Za-z_0-9]+)"', txt)))
    attrs[fid]=a

for fid,a in attrs.items():
    for p in a['prereq']:
        if p not in fset: dang[('prerequisite',p)].append(fid)
    if a['anchor'] and a['anchor'] not in fset: dang[('relative_position_id',a['anchor'])].append(fid)
    for m_ in a['mx']:
        if m_ not in fset: dang[('mutually_exclusive',m_)].append(fid)
print('\n=== [FOCUS] dangling prerequisite / anchor / mutually_exclusive ===')
if dang:
    for (k,t),srcs in sorted(dang.items()): print(f'  {k} -> {t}  : from {", ".join(sorted(set(srcs)))}')
else: print('  none')

coords=collections.defaultdict(list)
for fid,a in attrs.items():
    if a['x'] is not None and a['y'] is not None: coords[(a['x'],a['y'])].append(fid)
dups={k:v for k,v in coords.items() if len(v)>1}
print(f'\n=== [FOCUS] duplicate (x,y): {len(dups)} ===')
for k,v in sorted(dups.items()): print('  ',k,v)
noxy=[(f,a['line']) for f,a in attrs.items() if a['x'] is None or a['y'] is None]
print(f'\n=== [FOCUS] missing absolute x/y: {len(noxy)} ===  {noxy[:15]}')
idx={f:i for i,f in enumerate(order)}
fwd=[(f,a['anchor']) for f,a in attrs.items() if a['anchor'] and a['anchor'] in idx and idx[a['anchor']]>idx[f]]
print(f'\n=== [FOCUS] forward anchor refs (engine reads top-down -> ERROR): {len(fwd)} ===')
for f,a in fwd[:40]: print('  ',f,'-> anchor',a)
graph={f:attrs[f]['prereq'] for f in attrs}
color={}; cycles=[]
def dfs(n,stack):
    color[n]=1; stack.append(n)
    for m in graph.get(n,[]):
        if m not in graph: continue
        if color.get(m,0)==1: cycles.append(stack[stack.index(m):]+[m])
        elif color.get(m,0)==0: dfs(m,stack)
    stack.pop(); color[n]=2
sys.setrecursionlimit(20000)
for f in order:
    if color.get(f,0)==0: dfs(f,[])
print(f'\n=== [FOCUS] prerequisite cycles: {len(cycles)} ===')
for c in cycles[:10]: print('  ',' -> '.join(c))
roots=[f for f in order if not attrs[f]['prereq']]
print(f'\n=== [FOCUS] roots: {len(roots)} ===')
print('   ', roots)
noprize=[f for f in order if not attrs[f]['has_reward']]
print(f'\n=== [FOCUS] no completion_reward: {len(noprize)} === {noprize[:20]}')
noicon=[f for f in order if not attrs[f]['icon']]
print(f'=== [FOCUS] no icon: {len(noicon)} === {noicon[:20]}')
costs=collections.Counter(attrs[f]['cost'] for f in order)
print(f'=== [FOCUS] cost distribution: {dict(costs)} ===')
json.dump({'order':order,'attrs':attrs},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'focus.json'),'w'),indent=1,default=str)
