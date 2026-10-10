"""Bounded scenarios executing the live industry PDX, not a HOI4 emulator.

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

EFFECTS = {k:v for k,_,v in read('common/scripted_effects/VIE_industry_effects.txt')}
TRIGGERS = {k:v for k,_,v in read('common/scripted_triggers/VIE_industry_triggers.txt')}
DECISIONS = {k:v for k,_,v in value(read('common/decisions/VIE_industry_decisions.txt'), 'VIE_industry_category')}
EVENTS = {value(b,'id'):b for b in values(read('events/VIE_industry_events.txt'),'country_event')}
FOCUS_TEXT = (ROOT/'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8-sig')
FOCUSES = focus_map(FOCUS_TEXT)
MANIFEST = json.loads((ROOT/'.claude/docs/industry/v31/structure.json').read_text(encoding='utf-8'))
IDS = {f['id'] for f in MANIFEST['focuses']}
BASELINE = json.loads((ROOT/'.claude/docs/industry/v31/baseline.json').read_text())
# The repository's MD snapshots provide portable verified helper definitions.
MD = {}
for file in ('00_scripted_effects.txt','00_budget_effects.txt'):
    MD.update({k:v for k,_,v in read('tools/audit/md_ref/'+file)})
STATES = {518,519,520,521,522,523,524}



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
        if k=='is_coastal':return scope==519
        if k=='can_staff_an_industrial_complex' or k=='can_staff_an_dockyard':return s.get('staff',True)==(v=='yes')
        if k=='original_tag':return v=='VIE'
        if k=='VIE_ai_historical':return s['historical']==(v=='yes')
        if k=='has_active_mission':
            assert v=='bankruptcy_incoming_collapse';return s['bankrupt']
        if k.isdigit():return condition(v,s,int(k))
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
        elif k=='swap_ideas':
            s['ideas'].pop(value(v,'remove_idea'),None);s['ideas'][value(v,'add_idea')]=None
        elif k=='add_extra_state_shared_building_slots':
            for building in ('industrial_complex','dockyard'):
                key=(scope,building);s['capacity'][key]=s['capacity'].get(key,5)+int(v)
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
        elif k in ('one_state_industrial_complex','one_state_dockyard'):apply(MD[k],s,scope)
        elif k in EFFECTS:apply(EFFECTS[k],s,scope)
        elif k in ('VIE_ax_init','VIE_ax_normalize','change_industrial_conglomerates_opinion','change_farmers_opinion','change_the_military_opinion','update_money_dirty_variable','VIE_fb_none','change_communist_cadres_opinion','increase_corruption','VIE_bop_reform_small','VIE_bop_conservative_small'):
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


PROGRAMS={p['id']:p for p in MANIFEST['programs']}
ECO={value(b,'id'):b for b in values(read('events/VIE_md_eco_p2.txt'),'country_event')}
EVENTS.update(ECO)
EVENTS.update({value(b,'id'):b for b in values(read('events/VIE_automotive_events.txt'),'country_event')})
P2={k:v for k,_,v in read('common/scripted_effects/VIE_md_effects_p2.txt')}
EFFECTS['VIE_fb_vinashin']=P2['VIE_fb_vinashin']


def choose(ident,letter,s):
    option=next(b for b in values(EVENTS[ident],'option') if value(b,'name')==ident+'.'+letter)
    assert condition(value(option,'trigger',[]),s)
    apply(option,s)


def invest(key,s):
    ident='VIE_ind_d_'+key;before=s['variables']['treasury']
    start(ident,s);paid=before-s['variables']['treasury'];assert paid>0
    advance(s,int(value(DECISIONS[ident],'days_remove')))
    assert s['variables']['treasury']==before-paid,'Construction charged twice'
    snapshot=deepcopy(s);apply(value(DECISIONS[ident],'remove_effect'),s)
    assert s==snapshot,'Duplicate delivery'
    return paid


def base():
    s=state();s['completed']={'VIE_doi_moi_continues','VIE_wto_negotiations','VIE_higher_education_law','VIE_cptpp_member'}
    unlock('VIE_industrialization_strategy',s);unlock('VIE_supporting_industries',s);invest('support',s)
    return s


def sector(s,name,fast=False,pilot=False,foreign=False):
    if name=='ship':
        unlock('VIE_vinashin_restructuring_sbic',s);invest('ship_governance',s)
        unlock('VIE_shipbuilding_joint_ventures',s);invest('ship_civil',s)
    elif name=='textile':
        unlock('VIE_textile_garment_exports',s);invest('textile_base',s)
        unlock('VIE_green_textiles',s);invest('textile_green',s)
    elif name=='steel':
        unlock('VIE_national_steel_program',s);choose('vie_ind.1','a' if foreign else 'b',s)
        invest('steel_foreign' if foreign else 'steel_domestic',s)
        unlock('VIE_hoa_phat_hrc_steel',s);invest('steel_hrc',s)
    elif name=='auto':
        for fid,key in [('domestic_automotive','auto_base'),('ev_revolution_batteries','auto_ev'),('global_auto_export','auto_export')]:
            unlock('VIE_'+fid,s);invest(key,s)
    elif name=='electronics':
        unlock('VIE_electronics_export_program',s)
        unlock('VIE_fdi_fast_track' if fast else 'VIE_fdi_technology_screening',s)
        invest('electronics_base',s);unlock('VIE_apple_supply_chain',s);invest('electronics_suppliers',s)
        unlock('VIE_manufacturing_hub',s)
    else:
        assert name=='chip'
        unlock('VIE_chip_engineers',s);invest('chip_workforce',s)
        unlock('VIE_chip_pilot_fab_priority' if pilot else 'VIE_chip_design_packaging_priority',s)
        for fid,key in [('chip_design','chip_design'),('osat_packaging','chip_osat')]:unlock('VIE_'+fid,s);invest(key,s)
    assert condition(TRIGGERS['VIE_ind_'+name+'_ready'],s)


def graph_checks():
    assert len(IDS)==24 and len(DECISIONS)==19 and len({p['key'] for p in PROGRAMS.values()})==17
    assert len(MANIFEST['removed'])==17 and not IDS.intersection(MANIFEST['removed'])
    assert not set(MANIFEST['removed']).intersection(FOCUSES)
    xy=positions(FOCUSES);order=list(FOCUSES)
    for item in MANIFEST['focuses']:
        fid=item['id'];block=FOCUSES[fid]
        assert xy[fid]==tuple(item['xy']) and groups(block)==item['pre']
        assert value(block,'icon')==item['icon']
        anchor=value(block,'relative_position_id')
        assert anchor in set().union(*map(set,groups(block))) and order.index(anchor)<order.index(fid)
        for group in groups(block):
            for parent in group:assert xy[parent][1]<xy[fid][1]
        for other,p in xy.items():
            if other!=fid and p[1]==xy[fid][1]:assert abs(p[0]-xy[fid][0])>=2,(fid,other)
        for exclusion in values(block,'mutually_exclusive'):
            for peer in values(exclusion,'focus'):
                assert any(fid in values(b,'focus') for b in values(FOCUSES[peer],'mutually_exclusive'))
                assert xy[fid][1]==xy[peer][1]
        assert not any(k=='has_completed_focus' and v in IDS for k,_,v in walk(value(block,'available',[])))
    assert len([fid for fid in IDS if values(FOCUSES[fid],'mutually_exclusive')])==4
    for ident,decision in DECISIONS.items():
        assert not values(decision,'fire_only_once') and int(value(decision,'days_remove'))==PROGRAMS[ident]['days']
        assert value(decision,'cost')=='0'
    for directory in ('common','events'):
        for file in (ROOT/directory).rglob('*.txt'):
            text='\n'.join(line.split('#',1)[0] for line in file.read_text(encoding='utf-8-sig').splitlines())
            for retired in MANIFEST['removed']:
                assert not re.search(r'\b'+re.escape(retired)+r'\b',text),(retired,file)
    print('PASS graph: 24 focuses, 19 decisions/17 programmes, anchors/AND/OR/mutex/gaps')


def capstone_checks():
    sectors=list(MANIFEST['sectors'])
    locdefs=values(read('common/scripted_localisation/VIE_industry_loc.txt'),'defined_text')
    getter={'ship':'Ship','textile':'Textile','steel':'Steel','auto':'Auto','electronics':'Supply','chip':'Chip'}
    for bits in itertools.product((False,True),repeat=6):
        s=state();s['variables']['VIE_ind_localization']=32;s['flags']['VIE_ind_productivity_done']=None
        for key,on in zip(sectors,bits):
            if on:
                for programme in MANIFEST['sectors'][key]:s['flags']['VIE_ind_'+programme+'_done']=None
                if key=='electronics':s['completed'].add('VIE_manufacturing_hub')
            definition=next(b for b in locdefs if value(b,'name')=='VIEIndustry'+getter[key]+'Status')
            assert condition(value(values(definition,'text')[0],'trigger'),s)==on
        assert condition(TRIGGERS['VIE_ind_capstone_ready'],s)==(sum(bits)>=3)
        s['variables']['VIE_ind_localization']=31.9
        assert not condition(TRIGGERS['VIE_ind_capstone_ready'],s)
    for trio in itertools.combinations(sectors,3):
        s=base()
        for name in trio:sector(s,name,fast=True,pilot=False,foreign=False)
        assert s['variables']['VIE_ind_localization']==28,trio
        unlock('VIE_industrial_productivity_program',s)
        assert not condition(TRIGGERS['VIE_ind_capstone_ready'],s)
        invest('productivity',s);assert s['variables']['VIE_ind_localization']==32
        unlock('VIE_modern_industrial_nation_2030',s)
    s=base();s['completed'].update(IDS)
    assert not condition(TRIGGERS['VIE_ind_three_sectors'],s),'Focus unlocks counted as delivery'
    print('PASS capstone: 64 states, 20 funded triples, 31.9/32, programme delivery, no mandatory fab/screened FDI')


def routes():
    budgets=[]
    for fast,pilot,foreign in itertools.product((False,True),repeat=3):
        s=base()
        for name in MANIFEST['sectors']:sector(s,name,fast,pilot,foreign)
        unlock('VIE_industrial_productivity_program',s);invest('productivity',s)
        before_fab=1000-s['variables']['treasury']
        assert abs(before_fab-(72-(1.875 if fast else 0)-(0 if pilot else 2.125)-(1.5 if foreign else 0)))<1e-9
        unlock('VIE_semiconductor_fab',s);invest('fab_pilot' if pilot else 'fab_design',s)
        expected=87-(1.875 if fast else 0)-(3 if pilot else 2.125)-(1.5 if foreign else 0)
        assert abs(1000-s['variables']['treasury']-expected)<1e-9
        budgets.append(expected);unlock('VIE_modern_industrial_nation_2030',s)
        assert sum(v for (st,kind),v in s['buildings'].items() if kind=='industrial_complex')==8
        assert sum(v for (st,kind),v in s['buildings'].items() if kind=='dockyard')==1
        assert 'VIE_chip_sector_idea' in s['ideas'] and 'VIE_semiconductor_idea' not in s['ideas']
        assert 'VIE_modern_industrial_nation_idea' in s['ideas'] and 'VIE_industrialization_2045_idea' not in s['ideas']
        assert len(s['bonus'])==(2 if fast else 3) and all(b['bonus']==.25 and b['uses']==1 for b in s['bonus'])
    assert min(budgets)==80.625 and max(budgets)==84.875
    print('PASS routes: 8 funding combinations; budgets 80.625..84.875 / 66.5..72 without fab; 8 IC/1 dockyard; bounded bonuses')


def lifecycle_checks():
    # Every start checks money and every finish is safe against loss and caps.
    for ident,p in PROGRAMS.items():
        s=state();s['completed'].update(IDS)
        for key in MANIFEST['sectors'].values():
            for k in key:s['flags']['VIE_ind_'+k+'_done']=None
        s['flags'].update({flag:None for flag in ('VIE_fdi_technology_screening','VIE_ind_priority_design' if ident.endswith('fab_design') else 'VIE_ind_priority_fab','VIE_ind_steel_foreign' if ident.endswith('steel_foreign') else 'VIE_ind_steel_domestic')})
        s['variables']['treasury']=p['cost']-.001
        assert not condition(TRIGGERS[ident+'_can_start'],s),ident
        s['variables']['treasury']=p['cost'];start(ident,s)
        after=deepcopy(s);apply(EFFECTS[ident+'_start'],s);assert s==after
        assert not condition(TRIGGERS[ident+'_can_start'],s)
        if p['target']:
            lost_owner=deepcopy(s);lost_owner['owned'].remove(p['target']);advance(lost_owner,p['days'])
            assert lost_owner['variables']['treasury']==p['cost'] and not lost_owner['buildings']
            assert not any(k.endswith('_busy') for k in lost_owner['flags'])
            before=s['variables'].get('VIE_ind_localization',0)
            s['controlled'].remove(p['target']);advance(s,p['days'])
            assert s['variables']['treasury']==p['cost'] and s['variables'].get('VIE_ind_localization',0)==before
            assert not s['buildings'];s['controlled'].add(p['target']);assert condition(TRIGGERS[ident+'_can_start'],s)
            start(ident,s);s['capacity'][(p['target'],p['building'])]=0;advance(s,p['days'])
            assert not s['buildings'] and s['variables']['VIE_ind_'+p['key']+'_stage']==1
        else:advance(s,p['days'])
        assert s['variables']['VIE_ind_'+p['key']+'_stage']==1
        assert not condition(TRIGGERS[ident+'_can_start'],s)
        assert not any(k.endswith('_busy') for k in s['flags'])
    # Save fixture: persist actual programme timers, variables and flags in JSON.
    s=base();unlock('VIE_textile_garment_exports',s);unlock('VIE_domestic_automotive',s)
    start('VIE_ind_d_textile_base',s);start('VIE_ind_d_auto_base',s);advance(s,100)
    encoded=json.dumps({k:s[k] for k in ('variables','flags','active','now')})
    resumed=deepcopy(s);resumed.update(json.loads(encoded));advance(resumed,265)
    assert resumed['variables']['VIE_ind_textile_base_stage']==1 and resumed['variables']['VIE_ind_auto_base_stage']==1
    assert not resumed['active'] and resumed['variables']['treasury']==s['variables']['treasury']
    # Missing workforce/design/OSAT must block fab independently.
    s=base();sector(s,'chip')
    for key in ('chip_workforce','chip_design','chip_osat'):
        other=deepcopy(s);other['flags'].pop('VIE_ind_'+key+'_done');assert not condition(value(FOCUSES['VIE_semiconductor_fab'],'available'),other)
    print('PASS lifecycle: money equality/shortage, replay, sector slots, ownership/control loss/refund/retry, full states, JSON timer fixture, missing fab prerequisites')


def event_checks():
    s=base();unlock('VIE_national_steel_program',s);s['flags']['VIE_popup_cd']=s['now']+1000
    apply(EFFECTS['VIE_event_scheduler_industry'],s);assert not s['queue']
    advance(s,1000);apply(EFFECTS['VIE_event_scheduler_industry'],s);assert s['queue']==['vie_ind.1']
    choose('vie_ind.1','a',s);before=deepcopy(s);choose('vie_ind.1','b',s);assert s==before
    s=base();s['variables']['VIE_catch_up']=1;unlock('VIE_national_steel_program',s)
    apply(EFFECTS['VIE_event_scheduler_industry'],s);assert not s['queue'] and 'VIE_ind_steel_choice_pending' in s['flags']
    s['variables']['VIE_catch_up']=0;apply(EFFECTS['VIE_event_scheduler_industry'],s);assert 'vie_ind.1' in s['queue']
    for early in (False,True):
        for letter,normal,discount in [('a',3,1),('b',1,.5)]:
            s=state();s['variables']['VIE_vinashin_risk']=2
            if early:s['flags']['VIE_ind_ship_governance_done']=None;s['variables']['VIE_vinashin_risk']=0
            apply(value(ECO['vie_eco.5'],'immediate'),s)
            assert ('VIE_state_debt_overhang' in s['ideas'])==(not early)
            choose('vie_eco.5',letter,s);assert s['variables']['treasury']==1000-(discount if early else normal)
            before=deepcopy(s);choose('vie_eco.5',letter,s);apply(value(ECO['vie_eco.5'],'immediate'),s);assert s==before
        s=state()
        if early:s['flags']['VIE_ind_ship_governance_done']=None
        apply(EFFECTS['VIE_fb_vinashin'],s);assert s['variables']['treasury']==1000-(.75 if early else 2)
        snap=deepcopy(s);apply(EFFECTS['VIE_fb_vinashin'],s);assert s==snap
    # Pre-existing long HSR debt is not removed by governance.
    s=base();s['date']='2005.1.1';s['ideas']['VIE_state_debt_overhang']=3650
    unlock('VIE_vinashin_restructuring_sbic',s);assert s['variables']['VIE_vinashin_risk']==2
    invest('ship_governance',s);assert s['variables']['VIE_vinashin_risk']==0 and s['ideas']['VIE_state_debt_overhang']==3650
    assert 'VIE_vinashin_crisis_processed' not in s['flags']
    for ident in ('vie_ind.3','vie_auto.1'):
        s=state();before=s['variables']['treasury'];choose(ident,'a',s);assert s['variables']['treasury']==before and not s['ideas'] and s['pp']==0
    s=state();s['countries'].clear();choose('vie_ind.2','a',s);before=deepcopy(s);choose('vie_ind.2','a',s);assert s==before
    s=state();choose('vie_auto.2','a',s);assert s['pp']==0
    s['flags']['VIE_ind_auto_ev_done']=None;s['completed'].add('VIE_petrolimex_green_ev_hubs');choose('vie_auto.2','a',s)
    assert s['pp']==25 and s['stability']==.01;snap=deepcopy(s);choose('vie_auto.2','a',s);assert s==snap
    formosa=next(b for b in values(P2['VIE_event_scheduler_p2'],'if') if any(k=='has_country_flag' and v=='VIE_steel_complex_built' for k,_,v in walk(value(b,'limit',[]))))
    for foreign,late,expected in [(False,False,False),(True,True,False),(True,False,True)]:
        s=state();s['date']='2020.1.1' if late else '2016.5.1'
        if foreign:s['flags']['VIE_steel_complex_built']=None
        apply([('if','=',formosa)],s);assert ('vie_eco.6' in s['queue'])==expected
        if late:assert s['variables']['treasury']==1000 and s['stability']==0
    vinashin = next(b for b in values(P2['VIE_event_scheduler_p2'], 'if') if any(k=='has_country_flag' and v=='VIE_sched_vinashin' for k,_,v in walk(value(b,'limit',[]))))
    s=state();s['variables']['VIE_catch_up']=1
    apply([('if','=',vinashin)],s)
    assert s['variables']['treasury']==1000 and not s['buildings'] and not s['ideas'] and not s['queue']
    assert 'VIE_vinashin_crisis_processed' in s['flags'] and 'VIE_ind_ship_governance_done' not in s['flags']
    print('PASS events: mandatory queue/cooldown/catch-up, immutable steel, Vinashin early/late/replay/debt, Formosa window, Petrolimex, notices without rewards')


def balance_and_preservation():
    definitions={}
    for file in ('VIE_industry_ideas.txt','VIE_md_ideas_p2.txt','VIE_supporting_industries_ideas.txt'):
        definitions.update({k:v for k,_,v in value(value(read('common/ideas/'+file),'ideas'),'country')})
    chosen=['VIE_ind_supporting_capacity_idea','VIE_hrc_steel_self_reliance','VIE_textile_supply_chain_idea','VIE_ev_mobility_idea','VIE_global_brand_recognition','VIE_manufacturing_hub_idea','VIE_chip_sector_idea','VIE_modern_industrial_nation_idea']
    for modifier,expected in [('country_productivity_growth_modifier',.08),('research_speed_factor',.015),('industrial_capacity_factory',.06),('corporate_tax_income_multiplier_modifier',.06),('production_speed_industrial_complex_factor',.09)]:
        assert abs(sum(float(value(value(definitions[key],'modifier'),modifier,'0')) for key in chosen)-expected)<1e-9
    for key in MANIFEST['retired_ideas']:assert key not in definitions
    loc={}
    for p in (ROOT/'localisation').rglob('*.yml'):
        for key in re.findall(r'^\s*([\w.]+):\d',p.read_text(encoding='utf-8-sig'),re.M):loc[key]=loc.get(key,0)+1
    for key in IDS|set(DECISIONS)|set(MANIFEST['ideas'])|{'VIE_industry_category'}:assert loc.get(key)==1 and loc.get(key+'_desc')==1,key
    for key in MANIFEST['removed']:assert not loc.get(key) and not loc.get(key+'_desc')
    assert (ROOT/'localisation/english/VIE_industry_programs_l_english.yml').read_bytes().startswith(b'\xef\xbb\xbf')
    def weight(block,s):
        result=float(value(block,'base'))
        for modifier in values(block,'modifier'):
            if condition([i for i in modifier if i[0]!='factor'],s):result*=float(value(modifier,'factor'))
        return result
    s=state();assert weight(value(FOCUSES['VIE_fdi_fast_track'],'ai_will_do'),s)==0
    assert weight(value(FOCUSES['VIE_chip_pilot_fab_priority'],'ai_will_do'),s)==0
    s['bankrupt']=True
    for decision in DECISIONS.values():assert weight(value(decision,'ai_will_do'),s)==0
    s['bankrupt']=False;s['staff']=False
    for ident,p in PROGRAMS.items():
        if p['target']:
            assert weight(value(DECISIONS[ident],'ai_will_do'),s)==0
            s['capacity'][(p['target'],p['building'])]=0
            assert weight(value(DECISIONS[ident],'ai_will_do'),s)>0
            s['capacity'].clear()
    changed=[]
    live={}
    for m in re.finditer(r'(?m)^\tfocus = \{',FOCUS_TEXT):
        end=m.end();depth=1
        while depth:depth+=(FOCUS_TEXT[end]=='{')-(FOCUS_TEXT[end]=='}');end+=1
        block=FOCUS_TEXT[m.start():end];fid=re.search(r'\bid = (\w+)',block).group(1)
        live[fid]=block
    assert live['VIE_innovation_nation']==BASELINE['innovation_before'].replace('has_completed_focus = VIE_semiconductor_ambition','VIE_ind_semiconductor_foundation_ready = yes')
    for fid,digest in BASELINE['unrelated_focus_hashes'].items():
        if fid!='VIE_innovation_nation' and hashlib.sha256(live.get(fid,'').encode()).hexdigest()!=digest:changed.append(fid)
    print('PASS balance, unique BOM loc and AI weights; innovation changed only at its approved gate')
    assert not changed,'External baseline changes preserved; review separately: '+', '.join(changed)
    assert len(FOCUSES)==BASELINE['old_count']-15
    print('PASS preservation: all other focus blocks unchanged from captured live baseline')


def main():
    graph_checks();capstone_checks();routes();lifecycle_checks();event_checks();balance_and_preservation()
    print('ALL INDUSTRY V31 SCENARIOS PASS (bounded script evaluation; runtime QA still required)')


if __name__=='__main__':main()


