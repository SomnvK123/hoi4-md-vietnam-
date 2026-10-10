"""Bounded scenarios executing the live infrastructure PDX, not a HOI4 emulator.

Unknown evaluated tokens fail. Reads the actual MD construction/treasury helpers;
UI, engine decision timers, civil-war lineage and AI still require in-game QA.
Run from any directory with Python 3.10+; no third-party dependencies.
"""
from copy import deepcopy
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys

from industry import ROOT, read, parse, value, values, walk, focus_map, positions, groups, compare

EFFECTS = {k:v for k,_,v in read('common/scripted_effects/VIE_infra_effects.txt')}
TRIGGERS = {k:v for k,_,v in read('common/scripted_triggers/VIE_infra_triggers.txt')}
DECISIONS = {k:v for k,_,v in value(read('common/decisions/VIE_infra_decisions.txt'), 'VIE_infrastructure_category')}
EVENTS = {value(b,'id'):b for b in values(read('events/VIE_infra_events.txt'),'country_event')}
FOCUS_TEXT = (ROOT/'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8-sig')
FOCUSES = focus_map(FOCUS_TEXT)
MANIFEST = json.loads((ROOT/'.claude/docs/infrastructure/structure.json').read_text(encoding='utf-8'))
IDS = {f['id'] for f in MANIFEST['focuses']}
BASELINE = json.loads((ROOT/'.claude/docs/infrastructure/baseline.json').read_text())
# The repository's MD snapshots provide portable verified helper definitions.
MD = {}
for file in ('00_scripted_effects.txt','00_budget_effects.txt'):
    MD.update({k:v for k,_,v in read('tools/audit/md_ref/'+file)})
STATES = {518,519,520,521,522,523,524}
ROAD_IDEAS = {'VIE_expressway_idea','VIE_expressway_idea_2','VIE_expressway_idea_3'}


def state():
    return dict(variables={'treasury':1000},temps={},flags={},completed=set(),ideas={},owned=set(STATES),
                controlled=set(STATES),countries={'JAP','CHI','GER','FRA'},capacity={},buildings={},
                now=0,date='2027.1.1',historical=True,bankrupt=False,pp=0,stability=0,
                charges=[],bonus=[],queue=[],active={},native_calls=[])


def number(x,s):
    try:return float(x)
    except ValueError:
        return s['temps'].get(x,s['variables'].get(x,0))


def condition(block,s,scope=None):
    def one(k,op,v):
        if k in ('tooltip','localization_key'):return True
        if k in ('AND','custom_trigger_tooltip'):return condition(v,s,scope)
        if k=='OR':return any(one(*item) for item in v)
        if k=='NOT':return not condition(v,s,scope)
        if k=='count_triggers':return sum(one(*item) for item in v if item[0]!='amount')>=int(value(v,'amount'))
        if k=='check_variable':return all(compare(number(a,s),o,number(b,s)) for a,o,b in v if a!='tooltip')
        if k=='has_completed_focus':return v in s['completed']
        if k=='has_country_flag':return v in s['flags']
        if k=='has_idea':return v in s['ideas']
        if k=='owns_state':return int(v) in s['owned']
        if k=='controls_state':return int(v) in s['controlled']
        if k=='is_owned_by':assert v=='ROOT';return scope in s['owned']
        if k=='is_controlled_by':assert v=='ROOT';return scope in s['controlled']
        if k=='free_building_slots':return s['capacity'].get((scope,value(v,'building')),5)>0
        if k=='country_exists':return v in s['countries']
        if k=='original_tag':return v=='VIE'
        if k=='VIE_ai_historical':return s['historical']==(v=='yes')
        if k=='has_active_mission':
            assert v=='bankruptcy_incoming_collapse';return s['bankrupt']
        if k=='has_active_mission':assert v=='bankruptcy_incoming_collapse';return s['bankrupt']
        if k=='date':return compare(tuple(map(int,s['date'].split('.'))),op,tuple(map(int,v.split('.'))))
        if k=='always':return v=='yes'
        if k in TRIGGERS:return condition(TRIGGERS[k],s,scope)==(v=='yes')
        raise ValueError('Unsupported trigger: '+k)
    return all(one(*item) for item in block)


def apply(block,s,scope=None):
    taken=None
    for k,op,v in block:
        if k in ('if','else_if','else'):
            if k=='if':taken=False
            if k=='else':execute=not taken
            else:execute=(not taken) and condition(value(v,'limit',[]),s,scope)
            if execute:
                taken=True
                apply([item for item in v if item[0]!='limit'],s,scope)
            continue
        taken=None
        if k in ('log','custom_effect_tooltip','name','trigger','ai_chance'):continue
        if k=='hidden_effect':apply(v,s,scope)
        elif k in ('set_variable','set_temp_variable','add_to_variable','multiply_temp_variable'):
            data=s['temps'] if 'temp' in k else s['variables']
            for var,_,val in v:
                if var=='tooltip':continue
                n=number(val,s)
                if k.startswith('set'):data[var]=n
                elif k.startswith('add'):data[var]=data.get(var,0)+n
                else:data[var]=data.get(var,0)*n
        elif k=='clear_variable':s['variables'].pop(v,None)
        elif k=='clamp_variable':
            var=value(v,'var');s['variables'][var]=max(number(value(v,'min'),s),min(number(value(v,'max'),s),s['variables'].get(var,0)))
        elif k=='set_country_flag':
            if isinstance(v,list):s['flags'][value(v,'flag')]=s['now']+int(value(v,'days'))
            else:s['flags'][v]=None
        elif k=='clr_country_flag':s['flags'].pop(v,None)
        elif k in ('add_ideas','remove_ideas'):
            if k=='add_ideas':s['ideas'][v]=None
            else:s['ideas'].pop(v,None)
        elif k=='add_timed_idea':s['ideas'][value(v,'idea')]=int(value(v,'days'))
        elif k=='add_political_power':s['pp']+=number(v,s)
        elif k=='add_stability':s['stability']+=number(v,s)
        elif k=='add_tech_bonus':s['bonus'].append(dict(name=value(v,'name'),category=value(v,'category'),uses=int(value(v,'uses')),bonus=float(value(v,'bonus'))))
        elif k in ('add_opinion_modifier','reverse_add_opinion_modifier'):
            assert value(v,'target') in s['countries'],'opinion effect targets nonexistent country'
        elif k=='country_event':s['queue'].append(value(v,'id'))
        elif k=='CONTROLLER':
            assert scope in s['controlled'];apply(v,s,None)
        elif k=='add_building_construction':
            assert scope in s['owned'] and scope in s['controlled']
            key=(scope,value(v,'type'));assert s['capacity'].get(key,5)>0
            s['buildings'][key]=s['buildings'].get(key,0)+int(value(v,'level'))
            s['capacity'][key]=s['capacity'].get(key,5)-int(value(v,'level'))
        elif k=='modify_treasury_effect':
            before=s['variables']['treasury'];apply(MD[k],s,scope)
            s['charges'].append(s['variables']['treasury']-before)
        elif k in ('one_state_infrastructure','one_state_air_base'):apply(MD[k],s,scope)
        elif k in EFFECTS:apply(EFFECTS[k],s,scope)
        elif k in ('VIE_ax_init','VIE_ax_normalize','change_industrial_conglomerates_opinion','change_farmers_opinion','change_the_military_opinion','update_money_dirty_variable','VIE_fb_none'):
            # Verified upstream/submod APIs; their separate mechanics are outside these scenarios.
            s['native_calls'].append(k)
        elif k.isdigit():apply(v,s,int(k))
        else:raise ValueError('Unsupported effect: '+k)


def unlock(fid,s):
    b=FOCUSES[fid]
    assert all(any(parent in s['completed'] for parent in group) for group in groups(b)),fid+' prerequisite'
    assert condition(value(b,'available',[]),s),fid+' available'
    assert not any(mx in s['completed'] for group in values(b,'mutually_exclusive') for mx in values(group,'focus'))
    s['completed'].add(fid);apply(value(b,'completion_reward'),s)


def start(ident,s):
    assert condition(value(DECISIONS[ident],'available'),s),ident+' unavailable'
    apply(value(DECISIONS[ident],'complete_effect'),s)
    s['active'][ident]=s['now']+int(value(DECISIONS[ident],'days_remove'))


def advance(s,days):
    s['now']+=days
    s['flags']={k:v for k,v in s['flags'].items() if v is None or v>s['now']}
    for ident,end in list(s['active'].items()):
        if end<=s['now']:
            del s['active'][ident]
            apply(value(DECISIONS[ident],'remove_effect'),s)


def invest(key,s):
    ident='VIE_infra_d_'+key
    before=s['variables']['treasury']
    start(ident,s)
    paid=before-s['variables']['treasury'];assert paid>0
    advance(s,int(value(DECISIONS[ident],'days_remove')))
    assert s['variables']['treasury']==before-paid,'charged again on delivery'
    snap=deepcopy(s)
    apply(value(DECISIONS[ident],'remove_effect'),s)
    assert s==snap,'duplicate delivery mutated state'
    return paid


def choose(event,letter,s):
    b=next(b for b in values(EVENTS[event],'option') if value(b,'name')==event+'.'+letter)
    assert condition(value(b,'trigger',[]),s),'ineligible event option'
    apply(b,s)


def ready(s):return condition(TRIGGERS['VIE_infra_three_programs_ready'],s)


def preservation_checks():
    live={}
    for m in re.finditer(r'(?m)^\tfocus = \{',FOCUS_TEXT):
        end=m.end();depth=1
        while depth:depth+=(FOCUS_TEXT[end]=='{')-(FOCUS_TEXT[end]=='}');end+=1
        b=FOCUS_TEXT[m.start():end];fid=re.search(r'\bid = (\w+)',b).group(1)
        if fid not in IDS:live[fid]=hashlib.sha256(b.encode()).hexdigest()
    changed=[fid for fid in set(live)|set(BASELINE['unrelated_focus_hashes'])
             if live.get(fid)!=BASELINE['unrelated_focus_hashes'].get(fid)]
    assert not changed,'outside-infrastructure baseline changed: '+', '.join(sorted(changed))
    print('PASS preservation: 394 unrelated blocks unchanged from captured baseline')


def graph_checks():
    assert len(IDS)==22 and len(BASELINE['removed'])==28
    assert not IDS.intersection(BASELINE['removed'])
    assert len(FOCUSES)==BASELINE['old_count']-22
    xy=positions(FOCUSES);order=list(FOCUSES)
    for f in MANIFEST['focuses']:
        fid=f['id'];b=FOCUSES[fid]
        assert xy[fid]==tuple(f['xy']) and groups(b)==f['pre']
        anchor=value(b,'relative_position_id')
        assert order.index(anchor)<order.index(fid)
        assert any(anchor in group for group in groups(b))
        for group in groups(b):
            for parent in group:assert xy[parent][1]<xy[fid][1]
        assert value(b,'cost') in ('5','7') and value(b,'icon')
        for group in values(b,'mutually_exclusive'):
            for peer in values(group,'focus'):
                assert any(fid in values(g,'focus') for g in values(FOCUSES[peer],'mutually_exclusive'))
    for a,b in itertools.combinations(FOCUSES,2):
        if a in IDS or b in IDS:
            assert xy[a][1]!=xy[b][1] or abs(xy[a][0]-xy[b][0])>=2
    assert all(f['targets']==[] or set(f['targets'])<=STATES for f in MANIFEST['projects'])
    # Actual state snapshot owners, not the inaccurate whitelist in older documentation.
    for target in set(s for p in MANIFEST['projects'] for s in p['targets']):
        path=next((ROOT/'tools/audit/md_ref').glob(str(target)+'-*'))
        assert re.search(r'owner = VIE\b',path.read_text(encoding='utf-8-sig'))
    for b in DECISIONS.values():
        assert value(b,'fire_only_once') is None and value(b,'cost')=='0'
        assert value(b,'days_remove') and value(b,'remove_effect')
    assert 'increase_economic_growth' not in (ROOT/'common/scripted_effects/VIE_infra_effects.txt').read_text()
    assert not any(k=='add_building_construction' for b in EFFECTS.values() for k,_,_ in walk(b))
    for helper in ('one_state_infrastructure','one_state_air_base'):
        assert any(k=='check_variable' and value(v,'skip_payment')=='1' for k,_,v in walk(MD[helper]) if isinstance(v,list))
    print('PASS graph: 22 nodes, 28 archived, direct anchors, symmetric mutex, mainland states')


def capstone_checks():
    terminals=['VIE_expressway_5000km_2030','VIE_modern_rail_network','VIE_multimodal_transport','VIE_long_thanh_airport']
    for bits in itertools.product((False,True),repeat=4):
        s=state()
        if bits[0]:s['completed'].add(terminals[0]);s['variables']['VIE_expressway_km']=5000
        if bits[1]:s['completed'].add(terminals[1]);s['flags']['VIE_infra_rail_network_ready']=None
        if bits[2]:s['completed'].add(terminals[2]);s['flags']['VIE_infra_multimodal_done']=None
        if bits[3]:s['completed'].add(terminals[3]);s['flags']['VIE_infra_long_thanh_done']=None
        assert ready(s)==(sum(bits)>=3)
        if sum(bits)>=3:unlock('VIE_synchronized_infrastructure_2030',s)
    s=state();s['completed'].update(terminals)
    assert not ready(s),'focus completion alone granted capstone'
    print('PASS capstone: all 16 combinations; actual delivery required')


def routes():
    totals={}
    for bot,private,partner in itertools.product((False,True),(False,True),('japan','eu','china')):
        s=state();s['completed'].add('VIE_doi_moi_continues')
        def u(slug):unlock('VIE_'+slug,s)
        u('infrastructure_development');u('transport_strategy_2004')
        u('expressway_bot' if bot else 'expressway_public_investment')
        invest('road_foundation_1',s);u('north_south_expressway');invest('road_spine_1',s)
        u('expressway_regional_links');invest('road_regions_1',s);invest('road_regions_2',s)
        u('expressway_5000km_2030');invest('road_3000_1',s)
        for i in range(1,5):invest('road_5000_'+str(i),s)
        assert s['variables']['VIE_expressway_km']==5000
        assert s['ideas'].keys() & ROAD_IDEAS=={'VIE_expressway_idea_3'}
        u('railway_national_program');u('reunification_line_upgrade');invest('rail_upgrade_1',s)
        u('urban_rail_program');invest('metro_1',s);invest('metro_2',s)
        u('north_south_hsr');choose('vie_infra.5',dict(japan='a',eu='b',china='c')[partner],s)
        # Replaying another valid option cannot change the partner or axes.
        axes={k:v for k,v in s['variables'].items() if k.startswith('VIE_ax_')}
        choose('vie_infra.5','b' if partner!='eu' else 'a',s)
        assert axes=={k:v for k,v in s['variables'].items() if k.startswith('VIE_ax_')}
        u('rail_technology_transfer');invest('rail_training_1',s);invest('hsr_'+partner+'_1',s)
        assert len(s['bonus'])==1 and s['bonus'][0]['bonus']==dict(japan=.5,eu=.4,china=.3)[partner]
        u('modern_rail_network')
        u('national_deepwater_ports');invest('ports_1',s);invest('ports_2',s)
        u('logistics_strategy');invest('logistics_1',s);u('multimodal_transport');invest('multimodal_1',s)
        assert 'VIE_multimodal_idea' in s['ideas'] and not s['ideas'].keys() & {'VIE_ports_idea','VIE_logistics_idea'}
        u('airport_master_plan');u('socialized_airports' if private else 'acv_monopoly')
        u('airport_network_2030');invest('air_modern_1',s);invest('air_modern_2',s)
        u('long_thanh_airport');invest('long_thanh_prepare_1',s);invest('long_thanh_1',s)
        assert ready(s);u('synchronized_infrastructure_2030')
        assert not any(kind=='air_base' for (_,kind) in s['buildings'])
        expected=(35.875 if bot else 45.5)+7+7+1+1+dict(japan=10.5,eu=9.5,china=7.5)[partner]+14+(9.875 if private else 12.5)
        assert abs(1000-s['variables']['treasury']-expected)<1e-8,(bot,private,partner,expected,s['variables']['treasury'])
        assert (s['ideas'].get('VIE_state_debt_overhang')==1825)==(partner=='china')
        totals[f'{bot}/{private}/{partner}']=expected
    assert totals['False/False/japan']==98.5 and totals['True/True/china']==83.25
    print('PASS routes: 12 funding/partner combinations, exact budgets 83.25..98.5, exclusive ideas, civilian airports')


def edge_checks():
    s=state();s['completed'].update(IDS)
    ident='VIE_infra_d_road_foundation_1'
    # No money / equality boundary / no double click.
    s['variables']['treasury']=6.999;assert not condition(value(DECISIONS[ident],'available'),s)
    s['variables']['treasury']=7;assert condition(value(DECISIONS[ident],'available'),s)
    start(ident,s);assert s['variables']['treasury']==0
    before=deepcopy(s);apply(EFFECTS[ident+'_start'],s);assert before==s
    # Same sector blocked, different sector still allowed when solvent.
    s['variables']['treasury']=100;s['flags']['VIE_infra_road_foundation_done']=None
    assert not condition(TRIGGERS['VIE_infra_d_road_spine_1_can_start'],s)
    assert condition(TRIGGERS['VIE_infra_d_ports_1_can_start'],s)
    start('VIE_infra_d_ports_1',s);assert len(s['active'])==2
    # Lost owner refunds exactly once, no progress or foreign construction.
    s['owned'].remove(521);before_money=s['variables']['treasury'];advance(s,180)
    assert s['variables']['treasury']==before_money+7 and s['variables'].get('VIE_expressway_km',0)==0
    assert not s['flags'].keys() & {'VIE_infra_road_busy',ident+'_running'}
    s['owned'].add(521);assert condition(TRIGGERS[ident+'_can_start'],s)
    # A state still owned but occupied must also prevent handover and refund.
    s=state();s['completed'].update(IDS);start(ident,s);s['controlled'].remove(518)
    advance(s,180);assert s['variables']['treasury']==1000 and not s['buildings']
    # A separate branch's completion cannot free this branch early.
    s=state();s['completed'].update(IDS);start(ident,s);start('VIE_infra_d_ports_1',s)
    advance(s,180);assert 'VIE_infra_ports_busy' in s['flags']
    advance(s,185);assert 'VIE_infra_ports_busy' not in s['flags']
    # Capped state never calls the MD fallback or bills again.
    s=state();s['completed'].update(IDS);s['capacity']={(521,'infrastructure'):0,(518,'infrastructure'):0}
    invest('road_foundation_1',s)
    assert not s['buildings'] and s['variables']['VIE_expressway_km']==400 and s['temps']['skip_payment']==0
    # Reload the fixture's persistent state midway through the live decision duration.
    s=state();s['completed'].update(IDS);start(ident,s);advance(s,90)
    encoded=json.dumps(s,default=lambda x:sorted(x))
    restored=json.loads(encoded)
    for key in ('completed','owned','controlled','countries'):restored[key]=set(restored[key])
    advance(restored,89);assert restored['variables'].get('VIE_expressway_km',0)==0
    advance(restored,1);assert restored['variables']['VIE_expressway_km']==400
    assert restored['variables']['treasury']==993
    # Exact km idea boundaries, repeated refresh is idempotent.
    for km,wanted in [(999,set()),(1000,{'VIE_expressway_idea'}),(2999,{'VIE_expressway_idea'}),(3000,{'VIE_expressway_idea_2'}),(4999,{'VIE_expressway_idea_2'}),(5000,{'VIE_expressway_idea_3'})]:
        s=state();s['variables']['VIE_expressway_km']=km;apply(EFFECTS['VIE_infra_refresh_roads'],s)
        assert s['ideas'].keys() & ROAD_IDEAS==wanted
        before=deepcopy(s);apply(EFFECTS['VIE_infra_refresh_roads'],s);assert before==s
    # Early HSR access and debt; China must not replace ten years with five.
    s=state();s['completed'].update(IDS);s['date']='2012.1.1';choose('vie_infra.4','b',s)
    choose('vie_infra.5','c',s);s['flags']['VIE_infra_rail_training_done']=None
    invest('hsr_china_1',s);assert s['ideas']['VIE_state_debt_overhang']==3650
    s=state();s['completed'].update(IDS);s['date']='2026.11.30';s['flags'].update(VIE_hsr_partner_japan=None,VIE_infra_rail_training_done=None)
    assert not condition(TRIGGERS['VIE_infra_d_hsr_japan_1_can_start'],s)
    s['date']='2026.12.1';assert condition(TRIGGERS['VIE_infra_d_hsr_japan_1_can_start'],s)
    # Each necessary delivery independently locks the integrated railway focus.
    flags={'VIE_infra_'+x for x in ['rail_upgrade_done','metro_done','rail_training_done','hsr_launch_done']}
    for missing in flags:
        s=state();s['flags'].update({x:None for x in flags-{missing}})
        assert not condition(TRIGGERS['VIE_infra_rail_network_gate'],s)
    # Optional projects and their separate prices/capstone independence.
    s=state();s['completed'].update(IDS);assert not condition(TRIGGERS['VIE_infra_d_van_don_1_can_start'],s)
    s['flags']['VIE_infra_air_private']=None
    assert invest('van_don_1',s)==2.625
    assert invest('dual_use_1',s)==3 and s['buildings'][(521,'air_base')]==1
    print('PASS lifecycle: treasury equality, double click/delivery, branch slots, loss/refund/retry, cap, reload fixture, km boundaries, early debt, optional projects')


def scheduler_checks():
    s=state();s['flags']['VIE_infra_partner_pending']=None
    s['flags']['VIE_popup_cd']=100;s['variables']['VIE_catch_up']=1
    before=deepcopy(s);apply(EFFECTS['VIE_event_scheduler_infra'],s)
    assert s['variables']['treasury']==before['variables']['treasury'] and not s['queue']
    s['variables']['VIE_catch_up']=0;apply(EFFECTS['VIE_event_scheduler_infra'],s)
    assert not s['queue'] and 'VIE_infra_partner_pending' in s['flags']
    advance(s,100);apply(EFFECTS['VIE_event_scheduler_infra'],s)
    assert s['queue']==['vie_infra.5']
    before=deepcopy(s);apply(EFFECTS['VIE_event_scheduler_infra'],s);assert before==s
    # Countries disappear between queueing and resolving: wait, preserve request.
    s['countries'].clear();choose('vie_infra.5','d',s)
    assert 'VIE_infra_partner_pending' in s['flags'] and 'VIE_infra_partner_resolved' not in s['flags']
    advance(s,45);apply(EFFECTS['VIE_event_scheduler_infra'],s);assert s['queue']==['vie_infra.5']
    s['countries'].add('JAP');apply(EFFECTS['VIE_event_scheduler_infra'],s)
    assert s['queue']==['vie_infra.5','vie_infra.5'];choose('vie_infra.5','a',s)
    assert 'VIE_hsr_partner_japan' in s['flags']
    # Mandatory choice is not silently dropped after six months.
    s=state();s['completed'].add('VIE_railway_national_program');s['date']='2011.1.1';s['flags']['VIE_popup_cd']=1000
    apply(EFFECTS['VIE_event_scheduler_infra'],s);assert 'VIE_infra_vote_resolved' not in s['flags']
    advance(s,1000);apply(EFFECTS['VIE_event_scheduler_infra'],s);assert 'vie_infra.4' in s['queue']
    choose('vie_infra.4','a',s);before=deepcopy(s);choose('vie_infra.4','b',s);assert before==s
    # Notice options never deliver rewards, even replayed.
    for num in range(6,10):
        s=state();before=s['variables']['treasury'];choose('vie_infra.'+str(num),'a',s)
        assert s['variables']['treasury']==before and s['pp']==0 and not s['ideas']
    # Missing partner rechecked inside choice effect, not just option visibility.
    s=state();s['countries'].clear()
    option=next(b for b in values(EVENTS['vie_infra.5'],'option') if value(b,'name')=='vie_infra.5.a')
    apply(option,s);assert 'VIE_infra_partner_resolved' not in s['flags']
    print('PASS scheduler: catch-up, cooldown queue, disappearance/retry, duplicate options, reward-free notifications')


def balance_checks():
    ideas={}
    for file in ('VIE_md_ideas_p2.txt','VIE_infra_ideas.txt'):
        ideas.update({k:v for k,_,v in value(value(read('common/ideas/'+file),'ideas'),'country')})
    chosen=['VIE_expressway_idea_3','VIE_modern_rail_idea','VIE_multimodal_idea','VIE_airport_network_idea','VIE_synchronized_infra_idea']
    def total(mod):return sum(float(value(value(ideas[k],'modifier'),mod,'0')) for k in chosen)
    assert abs(total('country_productivity_growth_modifier')-.088)<1e-9
    assert abs(total('trade_opinion_factor')-.073)<1e-9
    assert abs(total('production_speed_infrastructure_factor')-.2)<1e-9
    # Every new consumer has exactly one active localised title/description.
    loc={}
    for path in (ROOT/'localisation').rglob('*.yml'):
        for key in re.findall(r'^\s*([\w.]+):\d',path.read_text(encoding='utf-8-sig'),re.M):loc[key]=loc.get(key,0)+1
    for key in IDS | set(DECISIONS) | {'VIE_modern_rail_idea','VIE_multimodal_idea','VIE_infrastructure_category'}:
        assert loc.get(key)==1 and loc.get(key+'_desc')==1,(key,loc.get(key),loc.get(key+'_desc'))
    for key in BASELINE['removed']:assert not loc.get(key) and not loc.get(key+'_desc')
    scripted=values(read('common/scripted_localisation/VIE_infra_loc.txt'),'defined_text')
    assert len(scripted)==4
    for b in scripted:
        for text in values(b,'text'):assert loc.get(value(text,'localization_key'))==1
    print('PASS balance/loc: growth .088, trade .073, construction .20; unique active titles/descriptions, retired focus loc removed')


def ai_checks():
    def weight(block,s):
        result=float(value(block,'base'))
        for modifier in values(block,'modifier'):
            if condition([item for item in modifier if item[0]!='factor'],s):
                result*=float(value(modifier,'factor'))
        return result
    s=state()
    assert weight(value(FOCUSES['VIE_expressway_bot'],'ai_will_do'),s)==0
    assert weight(value(FOCUSES['VIE_expressway_public_investment'],'ai_will_do'),s)>0
    assert weight(value(FOCUSES['VIE_acv_monopoly'],'ai_will_do'),s)==0
    assert weight(value(FOCUSES['VIE_socialized_airports'],'ai_will_do'),s)>0
    vote=next(b for b in values(EVENTS['vie_infra.4'],'option') if value(b,'name')=='vie_infra.4.b')
    assert weight(value(vote,'ai_chance'),s)==0
    for option,expected in zip(values(EVENTS['vie_infra.5'],'option')[:3],(50,50,40)):
        assert weight(value(option,'ai_chance'),s)==expected
    s['bankrupt']=True
    for decision in DECISIONS.values():assert weight(value(decision,'ai_will_do'),s)==0
    # Bankruptcy is AI behaviour, not an extra player can_start restriction.
    s['completed'].add('VIE_transport_strategy_2004')
    assert condition(TRIGGERS['VIE_infra_d_road_foundation_1_can_start'],s)
    print('PASS AI script weights: historical policies/vote, 50/50/40 partners, bankruptcy guard outside player gates')


def main():
    graph_checks();capstone_checks();routes();edge_checks();scheduler_checks();balance_checks();ai_checks();preservation_checks()
    print('ALL INFRASTRUCTURE SCENARIOS PASS (bounded script evaluation; not in-game validation)')


if __name__=='__main__':main()
