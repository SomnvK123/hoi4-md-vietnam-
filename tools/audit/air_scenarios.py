"""Bounded v24 checks against actual PDX script; never a HOI4 runtime substitute.

Unknown effects/triggers fail. Queued completion events establish actual flags and
tiers in fixtures, but scopes, UI, designers and game AI need a real game session.
"""
from copy import deepcopy
from itertools import combinations, product, permutations
import json
import subprocess
from industry import ROOT, parse, read, value, values, walk, focus_map, positions, groups, compare

STRUCTURES=['VIE_airf_structure_'+s for s in ('territorial','balanced','long_range')]
RETIRED=['VIE_airf_priority_'+s for s in ('air_defence','multirole','networked')]
TERMINALS=['VIE_airf_'+s for s in ('iads_command','multirole_wing','teaming')]
TARGETS=['VIE_airf_d5_capstone','VIE_airf_d5_multirole','VIE_airf_d5_uav']
PILLARS=dict(a32=(11,12,13),a31=(21,22,23),radar=(31,32,33),integ=(41,42,43),uav=(51,52,53))
EFFECTS={};TRIGGERS={};EVENTS={}
for filename in ('VIE_md_effects_air_force.txt','VIE_md_effects_air_ind.txt','VIE_airf_policy_effects.txt'):
    EFFECTS.update({k:v for k,_,v in read('common/scripted_effects/'+filename)})
for filename in ('VIE_md_triggers_air_force.txt','VIE_md_triggers_air_ind.txt','VIE_md_triggers_air_proc.txt'):
    TRIGGERS.update({k:v for k,_,v in read('common/scripted_triggers/'+filename)})
for filename in ('VIE_air_force.txt','VIE_air_ind.txt'):
    EVENTS.update({value(b,'id'):b for b in values(read('events/'+filename),'country_event')})

def state():
    return dict(variables={},temps={},flags=set(),completed=set(),ideas={},dlc=set(),partners=set(),
                date='2000.1.1',ai=False,historical=True,doctrine=False,bankrupt=False,wars=set(),
                treasury=0,charges=0,pp=0,xp=0,mastery=0,cp=0,war=0,bonus=[],queue=[],now=0,mio=0)

def number(v,s):
    try:return float(v)
    except ValueError:
        if v.startswith('VIE_') or v=='treasury_change':return s['temps'].get(v,s['variables'].get(v,0))
        raise ValueError('Unknown variable: '+v)

def condition(block,s):
    def one(k,o,v):
        if k=='tooltip':return True
        if k in ('AND','custom_trigger_tooltip'):return condition(v,s)
        if k=='OR':return any(one(*n) for n in v)
        if k=='NOT':return not any(one(*n) for n in v)
        if k=='count_triggers':return sum(one(*n) for n in v if n[0]!='amount')>=int(value(v,'amount'))
        if k=='check_variable':return all(compare(s['variables'].get(a,0),op,number(b,s)) for a,op,b in v)
        if k=='has_completed_focus':return v in s['completed']
        if k=='has_country_flag':return v in s['flags']
        if k=='has_idea':return v in s['ideas']
        if k=='has_dlc':return v in s['dlc']
        if k=='country_exists':return v in s['partners']
        if k=='has_war_with':return v in s['wars']
        if k=='has_selected_air_grand_doctrine':return s['doctrine']==(v=='yes')
        if k=='VIE_ai_historical':return s['historical']==(v=='yes')
        if k=='is_ai':return s['ai']==(v=='yes')
        if k=='has_active_mission':
            assert v=='bankruptcy_incoming_collapse';return s['bankrupt']
        if k=='date':return compare(tuple(map(int,s['date'].split('.'))),o,tuple(map(int,v.split('.'))))
        if k=='has_political_power':return compare(s['pp'],o,number(v,s))
        if k=='always':return v=='yes'
        if k in TRIGGERS:return condition(TRIGGERS[k],s)==(v=='yes')
        raise ValueError('Unsupported trigger: '+k)
    return all(one(*n) for n in block)

def effect(block,s):
    branch=None
    for k,_,v in block:
        if k in ('if','else_if','else'):
            if k=='if':branch=False
            assert branch is not None,'Unpaired else'
            if not branch and (k=='else' or condition(value(v,'limit',[]),s)):
                effect([n for n in v if n[0]!='limit'],s);branch=True
            continue
        branch=None
        if k in ('name','trigger','ai_chance','log','custom_effect_tooltip','force_update_dynamic_modifier',
                 'VIE_ap_ensure_af_modifier','VIE_apm_mio_effects','add_to_mio_funds',
                 'unlock_decision_category_tooltip','unlock_decision_tooltip','reduce_focus_completion_cost'):continue
        if k in ('hidden_effect','mio:VIE_viettel_manufacturer'):effect(v,s)
        elif k=='add_mio_size':s['mio']+=number(v,s)
        elif k in EFFECTS:effect(EFFECTS[k],s)
        elif k in ('set_variable','add_to_variable','set_temp_variable','add_to_temp_variable','multiply_temp_variable'):
            target=s['temps'] if 'temp' in k else s['variables']
            for a,_,b in v:
                if a=='tooltip':continue
                n=number(b,s)
                target[a]=target.get(a,0)+n if k.startswith('add_to') else target.get(a,0)*n if k.startswith('multiply') else n
        elif k=='clamp_variable':
            a=value(v,'var');s['variables'][a]=max(number(value(v,'min'),s),min(number(value(v,'max'),s),s['variables'].get(a,0)))
        elif k=='round_temp_variable':s['temps'][v]=round(s['temps'][v])
        elif k=='set_country_flag':s['flags'].add(value(v,'flag') if isinstance(v,list) else v)
        elif k=='clr_country_flag':s['flags'].discard(v)
        elif k=='add_timed_idea':s['ideas'][value(v,'idea')]=s['now']+number(value(v,'days'),s)
        elif k=='country_event':s['queue'].append((s['now']+number(value(v,'days','0'),s),value(v,'id')))
        elif k=='modify_treasury_effect':s['treasury']+=s['temps']['treasury_change'];s['charges']+=1
        elif k=='add_political_power':s['pp']+=number(v,s)
        elif k=='air_experience':s['xp']+=number(v,s)
        elif k=='add_mastery':s['mastery']+=number(value(v,'amount'),s)
        elif k=='add_command_power':s['cp']+=number(v,s)
        elif k=='add_war_support':s['war']+=number(v,s)
        elif k=='add_tech_bonus':s['bonus'].append(deepcopy(v))
        else:raise ValueError('Unsupported effect: '+k)

def call(name,s):effect(EFFECTS[name],s)
def advance(s):
    while s['queue']:
        day,eid=min(s['queue']);s['queue'].remove((day,eid));s['now']=day
        s['ideas']={k:v for k,v in s['ideas'].items() if v>day}
        effect(value(EVENTS[eid],'immediate',[]),s)
def option_effect(opt,s):effect([n for n in opt if n[0] not in ('name','trigger','ai_chance')],s)
def weight(opt,s):
    if not condition(value(opt,'trigger',[]),s):return 0
    b=value(opt,'ai_chance',[]);base=float(value(b,'base','1'));multiplier=1
    for m in values(b,'modifier'):
        if condition([n for n in m if n[0] not in ('add','factor')],s):
            base+=float(value(m,'add','0'));multiplier*=float(value(m,'factor','1'))
    return base*multiplier

def scenario_options():
    tested=0
    for delivered,life,c295,sam,radar,blr in product((0,1,11,12),(False,True),(0,1),(0,1),(0,1,2),(False,True)):
        s=state();s['ai']=True
        s['variables'].update(VIE_var_air_delivered=delivered,VIE_ap_c295_qty=c295,VIE_var_sam_lr=sam,VIE_apm_radar_tier=radar)
        if life:s['flags'].add('VIE_apm_a32_su30_life')
        if blr:s['partners'].add('BLR')
        for eid,p,tier in [('12','a32',1),('13','a32',2),('21','a31',0),('23','a31',2)]:
            s['completed'].add('VIE_apm_'+p);s['variables']['VIE_apm_'+p+'_tier']=tier
            if condition(TRIGGERS['VIE_apm_'+p+'_ok'],s):
                assert any(weight(o,s)>0 for o in values(EVENTS['vie_air_ind.'+eid],'option')),(eid,s)
                tested+=1
    print('PASS real gated AI options .12/.13/.21/.23:',tested,'reachable states; no dummy option')

def run_program(s,p,tier,choice='a'):
    assert s['variables'].get('VIE_apm_'+p+'_tier',0)==tier-1
    assert condition(TRIGGERS['VIE_apm_'+p+'_ok'],s),(p,tier)
    s['flags'].add('VIE_apm_'+p+'_pending');call('VIE_apm_program_start',s)
    event=EVENTS['vie_air_ind.'+str(PILLARS[p][tier-1])]
    opt=next(o for o in values(event,'option') if value(o,'name').endswith('.'+choice))
    assert condition(value(opt,'trigger',[]),s)
    option_effect(opt,s);snapshot=deepcopy(s);option_effect(opt,s);assert s==snapshot
    advance(s);assert s['variables']['VIE_apm_'+p+'_tier']==tier and s['variables']['VIE_var_apm_active']==0
    snapshot=deepcopy(s);call('VIE_apm_'+p+'_finish',s);assert s==snapshot

def can_focus(fid,s,focuses):
    b=focuses[fid]
    return all(any(p in s['completed'] for p in g) for g in groups(b)) and condition(value(b,'available',[]),s) and not any(p in s['completed'] for p in values(value(b,'mutually_exclusive',[]),'focus'))

def main():
    focuses=focus_map((ROOT/'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8'))
    before=json.loads((ROOT/'.claude/docs/air/air_before.json').read_text(encoding='utf-8'))
    after=json.loads((ROOT/'.claude/docs/air/air_after.json').read_text(encoding='utf-8'));ids=set(after)
    assert len(before)==29 and len(ids)==37 and set(before)<=ids and not set(RETIRED)&set(focuses)
    assert groups(focuses['VIE_apm_law'])==[['VIE_airf_training_standardization']]
    assert all(groups(focuses[f])==[['VIE_airf_command_reform_1']] for f in ['VIE_airf_tactical_exercises','VIE_airf_gci_radar_training','VIE_airf_regiment_formation','VIE_airf_reserve_bases'])
    assert groups(focuses['VIE_airf_first_force'])==[['VIE_airf_tactical_exercises'],['VIE_airf_gci_radar_training'],['VIE_airf_regiment_formation'],['VIE_airf_reserve_bases']]
    old=focus_map(subprocess.check_output(['git','show','HEAD:common/national_focus/VIE_md_focus.txt'],cwd=ROOT).decode('utf-8-sig'))
    pos=positions(focuses);oldpos=positions(old);ordered=list(focuses)
    assert pos['VIE_airf_integrated_force'][0]==pos['VIE_airf_training_standardization'][0]
    assert pos['VIE_airf_command_reform_2'][0]<pos['VIE_airf_training_standardization'][0]<pos['VIE_airf_medium_force'][0]
    assert all(b==old[f] and pos[f]==oldpos[f] for f,b in focuses.items() if f not in ids)
    assert len({pos[f][1] for f in STRUCTURES})==1
    decisions=set()
    for path in (ROOT/'common/decisions').glob('*.txt'):
        for _,_,cat in parse(path.read_text(encoding='utf-8-sig')):
            if isinstance(cat,list):decisions.update(k for k,_,v in cat if isinstance(v,list))
    for f in ids:
        b=focuses[f];assert pos[f]==(after[f]['x'],after[f]['y']) and groups(b)==after[f]['pre']
        assert 210<=pos[f][0]<=236
        assert all(pos[p][1]<pos[f][1] for g in groups(b) for p in g)
        anchor=value(b,'relative_position_id');assert anchor in sum(groups(b),[]) and ordered.index(anchor)<ordered.index(f)
        available_focus_gates=[v for k,_,v in walk(value(b,'available',[])) if k=='has_completed_focus']
        assert not any(k=='date' for k,_,_ in walk(value(b,'available',[])))
        assert all(f=='VIE_airf_teaming' and v=='VIE_airf_multirole' for v in available_focus_gates)
        if f=='VIE_airf_teaming':assert set(available_focus_gates)=={'VIE_airf_multirole'}
        assert all(abs(x-pos[f][0])>=2 for other,(x,y) in pos.items() if other!=f and y==pos[f][1])
        assert set(values(value(b,'mutually_exclusive',[]),'focus'))==(set(STRUCTURES)-{f} if f in STRUCTURES else set()),f
        assert all(v in decisions for k,_,v in walk(value(b,'completion_reward',[])) if k=='unlock_decision_tooltip')
    for parent,children,terminal in [('iads',['layered_defence','ew_antistealth'],'iads_command'),('unmanned',['isr_uav','strike_uav'],'teaming')]:
        children=['VIE_airf_'+c for c in children];terminal='VIE_airf_'+terminal
        assert all(groups(focuses[c])==[['VIE_airf_'+parent]] for c in children)
        assert pos[children[0]][1]==pos[children[1]][1]<pos[terminal][1]
        assert all([c] in groups(focuses[terminal]) for c in children)
    fighter='VIE_airf_multirole'
    assert groups(focuses[fighter])==[['VIE_airf_command_reform_2'],['VIE_airf_medium_force']]
    for child in ('VIE_airf_multirole_fleet','VIE_airf_sustainment','VIE_airf_operating_range'):
        assert groups(focuses[child])==[[fighter]],child
    assert pos['VIE_airf_multirole_fleet'][1]==pos['VIE_airf_sustainment'][1]==pos['VIE_airf_operating_range'][1]
    assert groups(focuses['VIE_airf_airlift_tanker'])==[['VIE_airf_operating_range']]
    assert groups(focuses['VIE_airf_multirole_wing'])==[
        ['VIE_airf_multirole_fleet'],['VIE_airf_sustainment'],['VIE_airf_operating_range']]
    assert pos['VIE_airf_iads_command'][1]==pos['VIE_airf_multirole_wing'][1]==pos['VIE_airf_teaming'][1]
    assert pos['VIE_airf_iads']==(214,9) and pos['VIE_airf_multirole']==(220,9) and pos['VIE_airf_unmanned']==(226,9)
    assert pos['VIE_airf_datalink']==(226,10) and pos['VIE_airf_teaming']==(226,12)
    assert pos['VIE_airf_airlift_tanker']==(220,11)
    assert pos['VIE_airf_integrated_force']==(220,13)
    assert pos['VIE_airf_multirole_fleet'][0]+pos['VIE_airf_sustainment'][0]==2*pos['VIE_airf_multirole'][0]
    assert pos['VIE_airf_isr_uav'][0]+pos['VIE_airf_strike_uav'][0]==2*pos['VIE_airf_unmanned'][0]
    assert pos['VIE_airf_layered_defence'][0]+pos['VIE_airf_ew_antistealth'][0]==2*pos['VIE_airf_iads'][0]
    assert ['VIE_airf_datalink'] not in groups(focuses['VIE_airf_multirole'])
    assert groups(focuses['VIE_airf_datalink'])==[['VIE_airf_unmanned']]
    assert groups(focuses['VIE_airf_teaming'])==[['VIE_airf_isr_uav'],['VIE_airf_strike_uav'],['VIE_airf_datalink']]
    assert groups(focuses['VIE_airf_integrated_force'])==[['VIE_airf_iads_command','VIE_airf_multirole_wing','VIE_airf_teaming']]
    assert pos['VIE_airf_command_reform_2']==(218,8) and pos['VIE_airf_medium_force']==(222,8)
    assert pos['VIE_airf_first_force']==(220,6)
    assert [pos[f][0] for f in ['VIE_airf_tactical_exercises','VIE_airf_gci_radar_training','VIE_airf_regiment_formation','VIE_airf_reserve_bases']]==[214,218,222,226]
    assert all(pos[f][1]==5 for f in ['VIE_airf_tactical_exercises','VIE_airf_gci_radar_training','VIE_airf_regiment_formation','VIE_airf_reserve_bases'])
    assert pos['VIE_airf_sam_force']==(218,3) and pos['VIE_airf_fighter_force']==(222,3)
    assert all(pos[f][1]==7 for f in STRUCTURES) and all(pos[f][1]==12 for f in TERMINALS)
    for y in (9,10,11,12):
        xs=sorted(x for fid,(x,yy) in pos.items() if fid in ids and yy==y)
        assert all(b-a>=2 for a,b in zip(xs,xs[1:])),(y,xs)
    for n in range(4):
        for subset in combinations(['VIE_apm_a32','VIE_apm_a31','VIE_apm_radar'],n):
            assert all(any(p in subset for p in g) for g in groups(focuses['VIE_apm_integration']))==(n>=2)
    changed=subprocess.check_output(['git','diff','--name-only','HEAD'],cwd=ROOT).decode().splitlines()
    assert not any(p.startswith(('gfx/','interface/','assets/')) for p in changed)
    print('PASS 29 old IDs / 37 air focuses, Y1-Y12 tiers, four readiness gates, aligned SAM/fighter/UAV columns, local datalink/teaming gate, separated tanker/capstones, shared root, 387 neighbours/artwork unchanged')
    for legacy in range(4):
        s=state();s['variables']['VIE_airf_policy_priority']=legacy
        if legacy:s['flags'].add('VIE_airf_policy_selected')
        for repeat in range(2):
            for i in (1,2,3):call('VIE_airf_research_'+str(i)+'_reward',s)
        assert len(s['bonus'])==(2 if legacy else 3)
        assert all(value(b,'bonus')=='0.25' and value(b,'uses')=='1' for b in s['bonus'])
    print('PASS relocated research once; matching legacy grant not repeated')
    priced=0
    for p,evs in PILLARS.items():
        for tier,eid in enumerate(evs):
            for opt in values(EVENTS['vie_air_ind.'+str(eid)],'option'):
                for discount in (False,True):
                    base=state();base['variables'].update({'VIE_apm_'+k+'_tier':tier for k in PILLARS})
                    base['variables']['VIE_ap_pechora_scope']=2 if discount else 0
                    if discount:base['flags'].add('VIE_ap_radar_viettel_fast')
                    neutral=deepcopy(base);option_effect(opt,neutral);assert neutral['charges']==1
                    for legacy in (1,2,3):
                        test=deepcopy(base);test['variables']['VIE_airf_policy_priority']=legacy;option_effect(opt,test)
                        assert test['treasury']==neutral['treasury'] and test['charges']==1 and test['queue']==neutral['queue']
                        assert test['temps']['VIE_apm_months']==neutral['temps']['VIE_apm_months'];priced+=1
    for d,level,orientation,legacy in product((1,2),(1,2),(1,2),range(4)):
        s=state();s['variables'].update(VIE_airf_fighter_level=level,VIE_airf_sam_level=level,VIE_airf_sam_orientation=orientation,VIE_airf_policy_priority=legacy)
        call('VIE_airf_d'+str(d)+'_start',s)
        cost=(.4 if level==1 else .6) if d==1 else ((.3 if level==1 else .45) if orientation==1 else (.5 if level==1 else .75))
        assert abs(s['treasury']+cost)<1e-9 and s['charges']==1 and s['queue'][0][0]==(360 if level==1 else 540)
        snapshot=deepcopy(s);call('VIE_airf_d'+str(d)+'_start',s);assert s==snapshot
    print('PASS actual prices/timers:',priced,'industry option/legacy/discount cases, D1/D2, one charge, no global priority factor')
    for mask,integ in product(product((1,2),repeat=4),(1,2)):
        s=state();s['variables']['VIE_apm_integ_tier']=integ
        for p,n in zip(('a32','a31','radar','uav'),mask):s['variables']['VIE_apm_'+p+'_tier']=n
        assert condition(TRIGGERS['VIE_apm_mature_ok'],s)==(integ==2 and mask.count(2)>=3)
    for specialty,token in [(1,'air_superiority_efficiency'),(2,'air_cas_efficiency')]:
        s=state();s['variables']['VIE_airf_fighter_specialty']=specialty;call('VIE_airf_b2_reward',s)
        assert abs(s['variables']['VIE_af_'+token]-.015)<1e-9
    for i in range(1,6):
        s=state();snapshot=deepcopy(s);call('VIE_airf_d'+str(i)+'_finish',s);assert s==snapshot
    print('PASS exact F7 threshold, B2 conditional reward, no unsolicited completion')
    scenario_options()
    readiness=['VIE_airf_tactical_exercises','VIE_airf_gci_radar_training','VIE_airf_regiment_formation','VIE_airf_reserve_bases']
    reward_contract=[(10,10,{}),(5,0,{'VIE_af_air_detection':.0025}),
                     (5,5,{'VIE_af_airforce_personnel_cost_multiplier_modifier':-.005}),
                     (5,0,{'VIE_af_air_home_defence_factor':.01})]
    for doctrine in (False,True):
        for fid,(xp,cp,modifiers) in zip(readiness,reward_contract):
            s=state();s['doctrine']=doctrine
            effect(value(focuses[fid],'completion_reward'),s)
            assert (s['xp'],s['mastery'],s['cp'])==((0,xp,cp) if doctrine else (xp,0,cp)),fid
            assert s['variables']==modifiers,fid
            assert not s['flags'] and not s['queue'] and not s['charges'] and not s['bonus'],fid
        for order in permutations(readiness):
            s=state();s['doctrine']=doctrine
            for fid in order:effect(value(focuses[fid],'completion_reward'),s)
            assert (s['xp'],s['mastery'],s['cp'])==((0,25,15) if doctrine else (25,0,15))
            assert s['variables']=={k:v for _,_,m in reward_contract for k,v in m.items()}
    print('PASS readiness rewards: four distinct contracts, XP/mastery fallback, 48 completion orders; no unsolicited programme or equipment grant')
    paths=0
    for legacy,structure,pair,bba,aat in product(range(4),(1,2,3),((0,1),(0,2),(1,2)),(False,True),(False,True)):
        s=state();s['variables'].update(VIE_airf_fighter_level=2,VIE_airf_fighter_specialty=1,VIE_airf_sam_level=2,VIE_airf_sam_orientation=1,VIE_airf_force_priority=1,VIE_ap_c295_qty=1,VIE_airf_policy_priority=legacy)
        s['partners'].add('BLR');s['completed'].add('VIE_modernize_vpa');s['doctrine']=bba;s['pp']=100
        if bba:s['dlc'].add('By Blood Alone')
        if aat:s['dlc'].add('Arms Against Tyranny')
        def complete(fid):
            assert can_focus(fid,s,focuses),fid
            effect(value(focuses[fid],'completion_reward',[]),s);s['completed'].add(fid)
        for f in ['VIE_airf_training_standardization','VIE_airf_fighter_force','VIE_airf_sam_force','VIE_airf_command_reform_1','VIE_apm_law','VIE_apm_a32','VIE_apm_a31','VIE_apm_radar']:complete(f)
        assert not can_focus('VIE_airf_first_force',s,focuses) and not any(can_focus(f,s,focuses) for f in STRUCTURES)
        for p in ['a32','a31','radar']:
            for tier in (1,2):run_program(s,p,tier,'b' if p=='a32' and tier==2 else 'a')
        complete('VIE_apm_integration')
        for tier in (1,2):run_program(s,'integ',tier)
        for i in (1,2):call('VIE_airf_program_start',s);call('VIE_airf_d'+str(i)+'_start',s)
        advance(s);assert {'VIE_airf_d1_done','VIE_airf_d2_done'}<=s['flags']
        readiness=['VIE_airf_tactical_exercises','VIE_airf_gci_radar_training','VIE_airf_regiment_formation','VIE_airf_reserve_bases']
        for prep in readiness[:3]:complete(prep)
        assert not can_focus('VIE_airf_first_force',s,focuses)
        complete(readiness[3])
        for prep in readiness:
            missing=deepcopy(s);missing['completed'].discard(prep)
            assert not can_focus('VIE_airf_first_force',missing,focuses),prep
        complete('VIE_airf_first_force');call('VIE_airf_program_start',s);call('VIE_airf_d3_start',s);complete(STRUCTURES[structure-1])
        assert not any(can_focus(f,s,focuses) for f in STRUCTURES)
        for opt in values(EVENTS['vie_air_force.30'],'option'):option_effect(opt,s)
        assert s['variables']['VIE_airf_force_priority']==structure
        advance(s);assert {'VIE_airf_d3_done','VIE_airf_d4_done'}<=s['flags']
        for f in ['VIE_airf_command_reform_2','VIE_airf_medium_force','VIE_apm_mature']:complete(f)
        clusters=[['iads','ew_antistealth','layered_defence','iads_command'],['multirole','multirole_fleet','sustainment','operating_range','multirole_wing'],['unmanned','isr_uav','strike_uav','datalink','teaming']]
        if 2 in pair:
            complete('VIE_apm_uav')
            for tier in (1,2,3):run_program(s,'uav',tier)
        if 2 in pair and 'VIE_airf_multirole' not in s['completed']:
            complete('VIE_airf_multirole')
        for cluster in pair:
            for f in clusters[cluster]:
                if f=='teaming' and 'VIE_airf_datalink' not in s['completed']:
                    removed=deepcopy(s);removed['completed'].discard('VIE_airf_datalink');assert not can_focus('VIE_airf_teaming',removed,focuses)
                complete('VIE_airf_'+f)
        for cluster,part in [(0,'ew_antistealth'),(1,'sustainment'),(2,'isr_uav')]:
            if cluster in pair:
                removed=deepcopy(s);removed['completed'].discard('VIE_airf_'+part);assert not can_focus(TERMINALS[cluster],removed,focuses)
        if 2 in pair:
            removed=deepcopy(s);removed['completed'].discard('VIE_airf_multirole');assert not can_focus('VIE_airf_teaming',removed,focuses)
        assert 'VIE_airf_airlift_tanker' not in s['completed']
        if pair==(0,1):assert s['variables'].get('VIE_apm_uav_tier',0)==0
        complete('VIE_airf_integrated_force')
        for terminal in TERMINALS:
            removed=deepcopy(s);removed['completed'].difference_update(TERMINALS);removed['completed'].add(terminal);assert not can_focus('VIE_airf_integrated_force',removed,focuses)
        removed=deepcopy(s);removed['flags'].discard('VIE_airf_d4_done');assert not can_focus('VIE_airf_integrated_force',removed,focuses)
        removed=deepcopy(s);removed['completed'].discard('VIE_apm_mature');assert not can_focus('VIE_airf_integrated_force',removed,focuses)
        assert s['variables']['VIE_var_airf_program_active']==0;paths+=1
    print('PASS',paths,'full paths: fresh/legacy x structures x A+B/A+C/B+C x BBA x AAT; reverse parallel ordering; no tanker, A+B no UAV; invalid convergence blocked')
    decisions=value(read('common/decisions/VIE_md_air_force_decisions.txt'),'VIE_airf_category')
    for target,level in product((1,2,3),(2,3)):
        s=state();s['completed'].update(TERMINALS);s['variables'].update({'VIE_apm_'+p+'_tier':level for p in PILLARS})
        d=value(decisions,TARGETS[target-1]);assert condition(value(d,'visible'),s) and condition(value(d,'available'),s) and value(d,'cost')=='60'
        missing=deepcopy(s);missing['completed'].discard(TERMINALS[target-1]);assert not condition(value(d,'available'),missing)
        effect(value(d,'complete_effect'),s)
        assert s['variables']['VIE_airf_capstone_target']==target and s['charges']==1 and s['treasury']==-1
        assert s['queue']==[(548,'vie_air_force.65')]
        for other in TARGETS:
            d=value(decisions,other);assert not condition(value(d,'available'),s);effect(value(d,'complete_effect'),s)
        assert s['variables']['VIE_airf_capstone_target']==target and s['charges']==1
        s['variables']['VIE_airf_policy_priority']=target%3+1;advance(s)
        modifiers={k:v for k,v in s['variables'].items() if k.startswith('VIE_af_')}
        assert len(modifiers)==2 and all(abs(v-(.005 if level==2 else .01))<1e-9 for v in modifiers.values())
        assert 'VIE_af_'+['air_home_defence_factor','air_attack_factor','air_intercept_efficiency'][target-1] in modifiers
        snapshot=deepcopy(s);call('VIE_airf_d5_finish',s)
        for other in TARGETS:effect(value(value(decisions,other),'complete_effect'),s)
        assert s==snapshot
    print('PASS D5 explicit targets: correct capstone required, fixed target/cost/timer, one lifetime grant despite all three terminals, tier-3 level gate')
    decisions=value(read('common/decisions/VIE_md_air_ind_decisions.txt'),'VIE_apm_category')
    for p in PILLARS:
        b=value(decisions,'VIE_apm_d_'+p);s=state();s['completed'].update(ids);assert condition(value(b,'available'),s)
        for kind in ('pending','running'):
            locked=deepcopy(s);locked['flags'].add('VIE_apm_'+p+'_'+kind);assert not condition(value(b,'available'),locked)
            locked['variables']['VIE_var_apm_active']=1;call('VIE_apm_slot_heal',locked);assert locked['variables']['VIE_var_apm_active']==1
        s['variables']['VIE_var_apm_active']=2;assert not condition(value(b,'available'),s)
        s=state();s['date']='2050.1.1';s['flags'].add('VIE_sched_air_'+p);call('VIE_apm_'+p+'_finish',s);assert s['variables'].get('VIE_apm_'+p+'_tier',0)==0
    for i in range(1,6):
        s=state();s['flags'].add('VIE_airf_d'+str(i)+'_started');s['variables']['VIE_var_airf_program_active']=1
        call('VIE_airf_slot_heal',s);assert s['variables']['VIE_var_airf_program_active']==1
        s['flags'].add('VIE_airf_d'+str(i)+'_done');call('VIE_airf_slot_heal',s);assert s['variables']['VIE_var_airf_program_active']==0
    print('PASS pending/running/two slots, no date/scheduler/unsolicited tier grant, slot heal preserves real programmes')
    print('ALL PASS (static scenarios; HOI4 runtime unverified)')

if __name__=='__main__':main()
