"""Static checks for md_vietnam (replaces the lost check_py.py). Run from anywhere:  python3 tools/check_static.py
Checks: brace balance, focus ids/prerequisites/exclusions/has_completed_focus, idea references, scripted effect calls,
event ids, decision categories, localisation keys, focus grid (same cell, neighbours closer than 2, children above parents),
modifier keys used by the mod's ideas exist in Millennium Dawn."""
import re,glob,os,sys,collections
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
MD='D:/SteamLibrary/steamapps/workshop/content/394360/2777392649'
os.chdir(ROOT)
err=[];warn=[]
def rd(p): return open(p,encoding='utf-8-sig').read()
def strip(t):
    t=re.sub(r'#[^\n]*','',t); return re.sub(r'"[^"\n]*"','""',t)
txts=[p for p in glob.glob('common/**/*.txt',recursive=True)+glob.glob('events/*.txt')]
for p in txts:
    t=strip(rd(p))
    if t.count('{')!=t.count('}'): err.append('unbalanced braces: %s (%d/%d)'%(p,t.count('{'),t.count('}')))
# ---- focus
F='common/national_focus/VIE_md_focus.txt'; text=rd(F)
fs={}
for m in re.finditer(r'\n\tfocus\s*=\s*\{',text):
    st=m.end();d=1;i=st
    while d: d+={'{':1,'}':-1}.get(text[i],0);i+=1
    b=text[st:i-1]; fid=re.search(r'\bid\s*=\s*(\w+)',b).group(1)
    if fid in fs: err.append('duplicate focus '+fid)
    x=int(re.search(r'\n\t\tx\s*=\s*(-?\d+)',b).group(1));y=int(re.search(r'\n\t\ty\s*=\s*(-?\d+)',b).group(1))
    r=re.search(r'relative_position_id\s*=\s*(\w+)',b)
    pre=[f for g in re.findall(r'prerequisite\s*=\s*\{([^}]*)\}',b) for f in re.findall(r'focus\s*=\s*(\w+)',g)]
    fs[fid]=dict(x=x,y=y,rel=r.group(1) if r else None,pre=pre,body=b)
memo={}
def ab(f):
    if f in memo: return memo[f]
    d=fs[f]; a=(d['x'],d['y']) if d['rel'] is None else (d['x']+ab(d['rel'])[0],d['y']+ab(d['rel'])[1]); memo[f]=a; return a
pos={f:ab(f) for f in fs}
for f,d in fs.items():
    for p in d['pre']:
        if p not in fs: err.append('%s: prerequisite %s missing'%(f,p))
        elif pos[p][1]>=pos[f][1]: warn.append('%s is not below its prerequisite %s'%(f,p))
    if d['rel'] and d['rel'] not in fs: err.append('%s: relative_position_id %s missing'%(f,d['rel']))
refs=set()
for p in txts:
    t=rd(p)
    refs|=set(re.findall(r'has_completed_focus\s*=\s*(\w+)',t))
    for g in re.findall(r'mutually_exclusive\s*=\s*\{([^}]*)\}',t): refs|=set(re.findall(r'focus\s*=\s*(\w+)',g))
    for g in re.findall(r'reduce_focus_completion_cost\s*=\s*\{\s*focus\s*=\s*(\{[^}]*\}|\w+)',t): refs|=set(re.findall(r'\w+',g))
refs={r for r in refs if r.startswith('VIE_')}
for r in sorted(refs-set(fs)): err.append('focus referenced but not defined: '+r)
cell=collections.defaultdict(list)
for f,p in pos.items(): cell[p].append(f)
for p,v in cell.items():
    if len(v)>1: err.append('same cell %s: %s'%(p,v))
rows=collections.defaultdict(list)
for f,(x,y) in pos.items(): rows[y].append((x,f))
for y,l in rows.items():
    l.sort()
    for (a,fa),(b,fb) in zip(l,l[1:]):
        if b-a<2: warn.append('neighbours closer than 2: %s %s'%(fa,fb))
# ---- ideas
ideas=set()
for p in glob.glob('common/ideas/*.txt'):
    for m in re.finditer(r'\n\t\t(\w+)\s*=\s*\{',rd(p)): ideas.add(m.group(1))
used=set()
for p in txts:
    if 'common/ideas' in p.replace('\\','/'): continue
    t=rd(p)
    for k in ('add_ideas','has_idea','remove_ideas'): used|=set(re.findall(r'\b%s\s*=\s*(VIE_\w+)'%k,t))
    for g in re.findall(r'swap_ideas\s*=\s*\{([^}]*)\}',t): used|=set(re.findall(r'(?:add_idea|remove_idea)\s*=\s*(VIE_\w+)',g))
for i in sorted(used-ideas): err.append('idea used but not defined: '+i)
# ---- modifier keys of the mod's ideas: the game's own documentation (country/all scopes) or MD definitions
doc=open('D:/SteamLibrary/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md',encoding='utf-8').read()
known=set(re.findall(r'(?m)^## (\w+)',doc))
for p in glob.glob(MD+'/common/modifier_definitions/*.txt'):
    known|=set(re.findall(r'(?m)^(\w+)\s*=\s*\{',open(p,encoding='utf-8-sig',errors='ignore').read()))
mdideas=''
for p in glob.glob(MD+'/common/ideas/*.txt')+glob.glob(MD+'/common/dynamic_modifiers/*.txt'): mdideas+=open(p,encoding='utf-8-sig',errors='ignore').read()
keys=set()
for p in glob.glob('common/ideas/*.txt'):
    for blk in re.findall(r'\bmodifier\s*=\s*\{([^}]*)\}',rd(p)): keys|=set(re.findall(r'(\w+)\s*=',blk))
for k in sorted(keys):
    if k in known: continue
    if re.match(r'production_speed_\w+_factor$',k): continue          # generated per building type
    if k.endswith('_mastery_gain_factor') and re.search(re.escape(k)+r'\s*=',mdideas): continue   # doctrine-track factors used by MD in ideas
    err.append('modifier key unknown to the game: '+k)
# ---- country tags used as targets
tags=set()
for p in glob.glob(MD+'/common/country_tags/*.txt'): tags|=set(re.findall(r'(?m)^([A-Z0-9]{3})\s*=',open(p,encoding='utf-8-sig',errors='ignore').read()))
for p in txts:
    for t in set(re.findall(r'\b(?:target|tag|producer|creator)\s*=\s*([A-Z]{3})\b',rd(p))):
        if t not in tags: err.append('%s: country tag %s does not exist'%(p,t))
# ---- scripted effects / triggers
defs=set()
for p in glob.glob('common/scripted_effects/*.txt')+glob.glob('common/scripted_triggers/*.txt'):
    defs|=set(re.findall(r'(?m)^(\w+)\s*=\s*\{',rd(p)))
calls=set()
for p in txts:
    calls|=set(re.findall(r'\b(VIE_\w+)\s*=\s*yes',rd(p)))
for c in sorted(calls-defs): err.append('scripted effect/trigger called but not defined: '+c)
# ---- events
evs=set()
for p in glob.glob('events/*.txt'): evs|=set(re.findall(r'\bid\s*=\s*(vie_\w+\.\d+)',rd(p)))
called=set()
for p in txts: called|=set(re.findall(r'country_event\s*=\s*\{\s*id\s*=\s*(vie_\w+\.\d+)',rd(p)))|set(re.findall(r'news_event\s*=\s*\{\s*id\s*=\s*(vie_\w+\.\d+)',rd(p)))
for e in sorted(called-evs): err.append('event fired but not defined: '+e)
# ---- decisions
cats=set(re.findall(r'(?m)^(\w+)\s*=\s*\{',rd('common/decisions/categories/VIE_md_categories.txt')))
for m in re.finditer(r'(?m)^(VIE_\w+_category)\s*=\s*\{',rd('common/decisions/VIE_md_decisions.txt')):
    if m.group(1) not in cats: err.append('decision category missing: '+m.group(1))
# ---- localisation
loc={}
for p in glob.glob('localisation/english/**/*.yml',recursive=True):
    for l in rd(p).split('\n'):
        m=re.match(r'\s*([\w.\-@]+):\d*\s+"',l)
        if m: loc.setdefault(m.group(1),[]).append(p)
for f in fs:
    for k in (f,f+'_desc'):
        if k not in loc: err.append('missing loc: '+k)
for i in ideas:
    if i.endswith('_idea') or i in used or i.startswith('VIE_'):
        for k in (i,i+'_desc'):
            if k not in loc: warn.append('missing loc: '+k)
for e in evs:
    if e in ('vie_pol.1',): continue
    for k in (e+'.t',e+'.d'):
        if k not in loc: err.append('missing loc: '+k)
decs=re.findall(r'(?m)^\t(VIE_\w+)\s*=\s*\{',rd('common/decisions/VIE_md_decisions.txt'))
for d in decs:
    for k in (d,d+'_desc'):
        if k not in loc: err.append('missing loc: '+k)

# ---- dynamic modifiers and their tooltips
dyn_defs={};dyn_keys=set()
for p in glob.glob('common/dynamic_modifiers/*.txt'):
    t=rd(p)
    for m in re.finditer(r'(?m)^(\w+)\s*=\s*\{',t):
        dyn_defs[m.group(1)]=p
    for k,v in re.findall(r'(?m)^	(\w+)\s*=\s*(VIE_\w+)\s*$',t):
        dyn_keys.add(v)
        if k not in known: err.append('dynamic modifier key unknown to the game: '+k)
for p in txts:
    t=rd(p)
    for m in re.findall(r'add_dynamic_modifier\s*=\s*\{\s*modifier\s*=\s*(\w+)',t):
        if m.startswith('VIE_') and m not in dyn_defs: err.append('dynamic modifier used but not defined: '+m)
    for v in set(re.findall(r'add_to_variable\s*=\s*\{\s*(VIE_af_\w+)',t)):
        if v not in dyn_keys: err.append('variable %s is not read by any dynamic modifier'%v)
mdloc=set()
for p in glob.glob(MD+'/localisation/english/*.yml')+glob.glob('D:/SteamLibrary/steamapps/common/Hearts of Iron IV/localisation/english/*.yml'):
    for l in open(p,encoding='utf-8-sig',errors='ignore'):
        m=re.match(r'\s*([\w.\-@]+):\d*\s+"',l)
        if m: mdloc.add(m.group(1))
for p in txts:
    for tt in set(re.findall(r'tooltip\s*=\s*(\w+_tt)\b',rd(p))):
        if tt not in loc and tt not in mdloc: err.append('tooltip key without loc: '+tt)
for d in dyn_defs:
    if d not in loc: err.append('missing loc for dynamic modifier: '+d)

# ---- state-building 9-axis checks (Batch 7)
axes = ['size', 'merit', 'decent', 'checks', 'market', 'civil', 'integ', 'mob', 'west']
for ax in axes:
    for k in [f'VIE_ax_{ax}', f'VIE_ax_{ax}_tt', f'VIE_ax_{ax}_pole_pos', f'VIE_ax_{ax}_pole_neg']:
        if k not in loc: err.append('missing axis loc key: ' + k)

for p in txts:
    for tt in set(re.findall(r'custom_trigger_tooltip\s*=\s*\{\s*tooltip\s*=\s*(\w+)', rd(p))):
        if tt not in loc and tt not in mdloc: err.append('custom_trigger_tooltip key without loc: ' + tt)

known_vars = {'ruling_party', 'rul_party_temp', 'treasury', 'stability', 'has_war',
              'Communist', 'Autocracy_leader', 'Monarchist_leader', 'Nat_Autocracy_leader',
              'Nat_Fascism_leader', 'Nat_Populism_leader', 'Neutral_Autocracy_leader',
              'Neutral_Libertarian_leader', 'Neutral_conservatism_leader', 'Neutral_green_leader',
              'Western_Autocracy_leader', 'anarchist_communism_leader', 'conservatism_leader',
              'liberalism_leader', 'neutral_Social_leader', 'oligarchism_leader', 'socialism_leader'}
mod_vars = set()
for p in txts:
    t = rd(p)
    for v in re.findall(r'(?:set_variable|add_to_variable|set_temp_variable|divide_variable|multiply_variable|clamp_variable|round_variable)\s*=\s*\{\s*(?:var\s*=\s*)?(\w+)', t):
        mod_vars.add(v)
    for v in re.findall(r'round_variable\s*=\s*(\w+)', t):
        mod_vars.add(v)
for p in txts:
    for m in re.findall(r'check_variable\s*=\s*\{\s*(?:var\s*=\s*)?(\w+)', rd(p)):
        if m not in known_vars and m not in mod_vars:
            err.append('%s: check_variable references unknown variable %s' % (p, m))

mdeff = set()
for p in glob.glob(MD + '/common/scripted_effects/*.txt'):
    mdeff |= set(re.findall(r'(?m)^(\w+)\s*=', open(p, encoding='utf-8-sig', errors='ignore').read()))
for p in txts:
    for eff in re.findall(r'\b((?:increase|decrease)_\w+)\s*=\s*yes', rd(p)):
        if eff not in mdeff: err.append('%s: unknown effect %s' % (p, eff))
    for eff in re.findall(r'\b(change_expected_\w+_spending)\s*=\s*yes', rd(p)):
        if eff not in mdeff: err.append('%s: unknown spending effect %s' % (p, eff))

# ---- military industrial organizations (MIO)
mios={};mio_traits=set();mio_txt=''
for p in glob.glob('common/military_industrial_organization/organizations/*.txt'):
    t=rd(p); mio_txt+=t
    for m in re.finditer(r'(?m)^(\w+) = \{',t): mios[m.group(1)]=p
    mio_traits|=set(re.findall(r'(?m)^\t\ttoken = (\w+)',t))
eqgroups=set();eqtypes=set();cats=set()
for q in glob.glob(MD+'/common/equipment_groups/*.txt'): eqgroups|=set(re.findall(r'(?m)^(\w+) = \{',rd(q)))
for q in glob.glob(MD+'/common/units/equipment/**/*.txt',recursive=True): eqtypes|=set(re.findall(r'(?m)^\t(\w+) = \{',rd(q)))
for q in glob.glob(MD+'/common/technology_tags/*.txt'): cats|=set(re.findall(r'\bCAT_\w+',rd(q)))
for blk in re.findall(r'equipment_type = \{([^}]*)\}',mio_txt):
    for tok in blk.split():
        if tok not in eqtypes and tok not in eqgroups and not tok.startswith('mio_cat') and tok not in ('submarine','carrier','helicopter_operator','convoy'): err.append('MIO equipment_type unknown: '+tok)
for blk in re.findall(r'research_categories = \{([^}]*)\}',mio_txt):
    for tok in blk.split():
        if tok not in cats: err.append('MIO research category unknown: '+tok)
okf={'token','name','icon','position','relative_position_id','all_parents','any_parent','parent','mutually_exclusive',
     'equipment_bonus','production_bonus','organization_modifier','limit_to_equipment_type','special_trait_background','on_complete','ai_will_do','available','visible'}
for m in re.finditer(r'(?m)^\ttrait = \{',mio_txt):
    i=m.end();d=1
    while d: d+={'{':1,'}':-1}.get(mio_txt[i],0);i+=1
    for f in set(re.findall(r'(?m)^\t\t(\w+)\s*=',mio_txt[m.end():i-1])):
        if f not in okf: err.append('MIO trait field not supported: '+f)
for blk in re.findall(r'(?:all_parents|any_parent|mutually_exclusive) = \{([^}]*)\}',mio_txt)+re.findall(r'relative_position_id = (\w+)',mio_txt):
    for tok in blk.split():
        if tok.startswith('VIE_') and tok not in mio_traits: err.append('MIO trait reference missing: '+tok)
for nm in set(re.findall(r'(?m)^\t?\t?name = (VIE_\w+)',mio_txt))|set(mios):
    if nm not in loc: err.append('missing loc for MIO entry: '+nm)
for p in txts:
    for m in set(re.findall(r'mio:(\w+)',rd(p)))|set(re.findall(r'unlock_mio_trait_tooltip = (\w+)',rd(p))):
        if m.startswith('VIE_') and m not in mios and m not in mio_traits: err.append('MIO reference missing: '+m)
sprites=set()
for q in glob.glob(MD+'/interface/**/*.gfx',recursive=True)+glob.glob('D:/SteamLibrary/steamapps/common/Hearts of Iron IV/interface/**/*.gfx',recursive=True)+glob.glob('interface/**/*.gfx',recursive=True):
    sprites|=set(re.findall(r'name = "(\w+)"',open(q,encoding='utf-8-sig',errors='ignore').read()))
used=set()
for p in glob.glob('common/decisions/*.txt')+glob.glob('common/military_industrial_organization/organizations/*.txt')+glob.glob('common/ideas/*.txt'):
    used|=set(re.findall(r'icon = (GFX_\w+)',rd(p)))
for g in sorted(used-sprites): err.append('sprite missing: '+g)
# ---- focus icons must be defined sprites; division template subunits must exist
for fid,fd in fs.items():
    ic=re.search(r'\n\t\ticon = (\w+)',fd['body'])
    if ic and ic.group(1) not in sprites: err.append('focus icon sprite missing: %s (%s)'%(ic.group(1),fid))
subs=set()
for q in glob.glob(MD+'/common/units/*.txt'): subs|=set(re.findall(r'(?m)^\s{1,2}(\w+) = \{',rd(q)))
for p in txts:
    for blk in re.findall(r'division_template = \{(.*?)\n\s*\}\n',rd(p),re.S):
        for u in re.findall(r'(\w+) = \{ x = \d+ y = \d+ \}',blk):
            if u not in subs: err.append('division_template unknown subunit: '+u)
# ---- political axis (abs x < 12, rows 0..9): every POLITICAL-filter focus should move the BoP unless it is a neutral foreign-policy / sovereignty step
BOP_EXEMPT = set('VIE_@'.replace('@', n) for n in '''doi_moi_continues ethnic_policy era_of_rising border_trade_gates border_settlement gulf_of_tonkin australia_partnership india_partnership
japan_partnership korea_partnership france_eu gulf_investment global_south_ties csp_network bamboo_diplomacy indo_pacific_partner pivot_to_the_west
accept_chinese_influence defence_hotline asean_chair un_security_council asean_integration indochina_solidarity indochina_federation apec_host special_relations_laos
mekong_commission mekong_dams_response funan_techo_response cambodia_relations cambodia_border cptpp_member wto_reforms law_of_the_sea legal_warfare assert_maritime_rights
code_of_conduct paracel_ultimatum multilateral_champion'''.split())
for fid_, fd_ in fs.items():
    X_, Y_ = ab(fid_)
    if Y_ <= 9 and X_ < 12 and 'FOCUS_FILTER_POLITICAL' in fd_['body'] and 'VIE_bop_' not in fd_['body'] and fid_ not in BOP_EXEMPT:
        warn.append('political focus without a BoP move: ' + fid_)
# ---- every VIE_* effect/trigger call must be defined (catches lost macros such as VIE_enter_regime)
defd = set()
for d_ in ('common/scripted_effects', 'common/scripted_triggers'):
    for q_ in glob.glob(d_ + '/*.txt') + glob.glob(MD + '/' + d_ + '/*.txt'):
        defd |= set(re.findall(r'(?m)^(\w+)\s*=\s*\{', open(q_, encoding='utf-8-sig', errors='ignore').read()))
calls = collections.defaultdict(set)
for p_ in glob.glob('events/*.txt') + glob.glob('common/national_focus/*.txt') + glob.glob('common/on_actions/*.txt') + glob.glob('common/scripted_effects/*.txt'):
    for m_ in re.finditer(r'(?m)^\t{2,}(VIE_\w+)\s*=\s*(yes|no|\{)', open(p_, encoding='utf-8-sig', errors='ignore').read()):
        calls[m_.group(1)].add(p_)
for p_ in glob.glob('common/decisions/*.txt'):
    for m_ in re.finditer(r'(?m)^\t{3,}(VIE_\w+)\s*=\s*(yes|no|\{)', open(p_, encoding='utf-8-sig', errors='ignore').read()):
        calls[m_.group(1)].add(p_)
for n_, ps_ in sorted(calls.items()):
    if n_ not in defd and n_ not in set():
        err.append('undefined scripted effect/trigger call: %s (%s)' % (n_, sorted(ps_)[0]))
# ---- every add_tech_bonus name needs a loc key (otherwise the raw key shows in the tooltip)
for p_ in glob.glob('common/national_focus/*.txt') + glob.glob('events/*.txt') + glob.glob('common/decisions/*.txt'):
    for m_ in re.finditer(r'add_tech_bonus\s*=\s*\{(.*?)\}', open(p_, encoding='utf-8-sig', errors='ignore').read(), re.S):
        n_ = re.search(r'name\s*=\s*(\w+)', m_.group(1))
        if n_ and n_.group(1) not in loc and n_.group(1) not in mdloc:
            err.append('add_tech_bonus name without loc: ' + n_.group(1))
# ---- engine-agnostic: every `name = yes` effect/trigger call in events/decisions must be a defined scripted effect/trigger (mod, MD) or a known engine keyword
known_kw = set('instant_build always yes no fire_only_once'.split())
defd2 = set(defd)
for p_ in glob.glob('events/*.txt') + glob.glob('common/decisions/*.txt'):
    for m_ in re.finditer(r'(?m)^\t{2,}([a-z][a-z_0-9]+)\s*=\s*yes\s*$', open(p_, encoding='utf-8-sig', errors='ignore').read()):
        n_ = m_.group(1)
        if n_ in defd2 or n_ in known_kw or n_.startswith(('has_', 'is_')): continue
        err.append('unknown effect/trigger call: %s (%s)' % (n_, p_))
# ---- script .txt files must NOT start with a UTF-8 BOM (engine: 'Unexpected token: <BOM>ideas', whole file ignored); .yml must have one
for p_ in glob.glob('common/**/*.txt', recursive=True) + glob.glob('events/*.txt') + glob.glob('interface/*.gfx') + glob.glob('gfx/**/*.gfx', recursive=True):
    if open(p_, 'rb').read(3) == bytes([0xEF, 0xBB, 0xBF]): err.append('BOM in script file: ' + p_)
dup=[k for k,v in loc.items() if len(v)>1]
if dup: warn.append('duplicate loc keys: %s'%dup[:10])
print('focus',len(fs),'ideas',len(ideas),'events',len(evs),'loc keys',len(loc))
for w in warn: print('WARN',w)
for e in err: print('ERROR',e)
print('%d errors, %d warnings'%(len(err),len(warn)))
sys.exit(1 if err else 0)
