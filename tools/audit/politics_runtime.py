"""Execute live political script in a narrow, fail-closed fixture (not the HOI4 engine)."""
from pathlib import Path
import ast,copy,json,math,re

ROOT=Path(__file__).resolve().parents[2]
tree=ast.parse((ROOT/'tools/audit/audit.py').read_text(encoding='utf-8'))
parser={}
exec(compile(ast.Module(body=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in ['tokenize','parse']],type_ignores=[]),'pdx_parser','exec'),parser)
def parse(path):
    text=(ROOT/path).read_text(encoding='utf-8-sig')
    text=re.sub(r'"(?:\\.|[^"\\])*"|#[^\n]*',lambda m:m.group() if m.group().startswith('"') else '',text)
    return parser['parse'](parser['tokenize'](text))
def value(block,key,default=None): return next((v for k,op,v,line in block if k==key),default)
def blocks(block,key):return [v for k,op,v,line in block if k==key]
FX={};TR={};DEC={};EV={}
for name in ['VIE_md_effects_politics.txt','VIE_md_effects_politics_runtime.txt']:
    FX.update({k:v for k,op,v,line in parse('common/scripted_effects/'+name)})
for name in ['VIE_md_triggers_politics.txt','VIE_md_triggers_politics_runtime.txt']:
    TR.update({k:v for k,op,v,line in parse('common/scripted_triggers/'+name)})
for name in ['VIE_md_politics_decisions.txt','VIE_md_politics_runtime_decisions.txt']:
    for k,op,category,line in parse('common/decisions/'+name):
        DEC.update({k:v for k,op,v,line in category if isinstance(v,list)})
for name in ['VIE_md_politics_events.txt','VIE_md_politics_runtime_events.txt']:
    EV.update({value(v,'id'):v for v in blocks(parse('events/'+name),'country_event')})
FOCUS={value(v,'id'):v for v in blocks(value(parse('common/national_focus/VIE_md_focus.txt'),'focus_tree'),'focus')}
CHECKS=0
def check(test,message):
    global CHECKS
    CHECKS+=1
    if not test:raise AssertionError(message)


class State:
    def __init__(self):
        self.v={'treasury':50,'VIE_leadership_cohesion':60,'VIE_last_congress':9,'VIE_tier_cadre':0,'treasury_rate':.1,'gdp_per_capita':100}
        self.pp=2000;self.bop=.3;self.flags={'VIE_congress_resolved'};self.focuses=set(FOCUS)
        self.ideas={'corruption_level_03'};self.events=[];self.roll=0;self.external={};self.stability=0
        self.owned={518,526};self.controlled={518,526};self.now=(2001,4,20)
    def number(self,text):
        try:return float(text)
        except (TypeError,ValueError):return self.v.get(text,0)
    def compare(self,actual,op,expected):
        operations={'=':lambda:actual==expected,'equals':lambda:actual==expected,'<':lambda:actual<expected,'>':lambda:actual>expected,
            'less_than':lambda:actual<expected,'greater_than':lambda:actual>expected,'greater_than_or_equals':lambda:actual>=expected,'less_than_or_equals':lambda:actual<=expected}
        if op not in operations:raise AssertionError('Unknown comparison '+op)
        return operations[op]()
    def condition(self,block,mode='AND'):
        results=[]
        for k,op,v,line in block:
            if k in ['AND','OR','NOT']:
                result=self.condition(v,'OR' if k=='OR' else 'AND');result=not result if k=='NOT' else result
            elif k=='always':result=v=='yes'
            elif k=='original_tag':result=v=='VIE'
            elif k=='has_country_flag':result=v in self.flags
            elif k=='has_completed_focus':result=v in self.focuses
            elif k=='has_idea':result=v in self.ideas
            elif k=='owns_state':result=int(v) in self.owned
            elif k=='controls_state':result=int(v) in self.controlled
            elif k=='political_power':result=self.compare(self.pp,op,float(v))
            elif k=='date':result=self.compare(self.now,op,tuple(map(int,v.split('.'))))
            elif k=='power_balance_value':
                _,operator,number,_=next(n for n in v if n[0]=='value');result=self.compare(self.bop,operator,float(number))
            elif k=='check_variable':
                if value(v,'var'):
                    result=self.compare(self.v.get(value(v,'var'),0),value(v,'compare','equals'),self.number(value(v,'value')))
                else:result=all(self.compare(self.v.get(name,0),operator,self.number(number)) for name,operator,number,_ in v)
            elif k=='custom_trigger_tooltip':result=self.condition([n for n in v if n[0]!='tooltip'])
            elif k in TR:
                result=self.condition(TR[k]);result=not result if v=='no' else result
            else:raise AssertionError(f'Unsupported trigger {k}:{line}')
            results.append(result)
        return any(results) if mode=='OR' else all(results)
    def apply(self,block):
        selected=False
        for k,op,v,line in block:
            if k=='if':
                selected=self.condition(value(v,'limit',[]))
                if selected:self.apply([n for n in v if n[0]!='limit'])
            elif k=='else_if':
                if not selected and self.condition(value(v,'limit',[])):
                    selected=True;self.apply([n for n in v if n[0]!='limit'])
            elif k=='else':
                if not selected:self.apply(v)
                selected=True
            elif k in ['hidden_effect']:self.apply(v)
            elif k=='set_country_flag':self.flags.add(value(v,'flag') if isinstance(v,list) else v)
            elif k=='clr_country_flag':self.flags.discard(v)
            elif k in ['set_variable','set_temp_variable','add_to_variable','add_to_temp_variable','subtract_from_variable','subtract_from_temp_variable','multiply_variable','multiply_temp_variable']:
                for name,operator,number,_ in v:
                    amount=self.number(number)
                    if k.startswith('set_'):self.v[name]=amount
                    elif k.startswith('add_'):self.v[name]=self.v.get(name,0)+amount
                    elif k.startswith('subtract_'):self.v[name]=self.v.get(name,0)-amount
                    else:self.v[name]=self.v.get(name,0)*amount
            elif k=='clamp_variable':
                var=value(v,'var');self.v[var]=max(float(value(v,'min')),min(float(value(v,'max')),self.v.get(var,0)))
            elif k=='add_political_power':self.pp+=self.number(v)
            elif k=='modify_treasury_effect':self.v['treasury']+=self.v['treasury_change']
            elif k=='add_power_balance_value':self.bop=max(-1,min(1,self.bop+float(value(v,'value'))))
            elif k=='set_power_balance':self.bop=float(value(v,'set_value'))
            elif k=='random_list':
                threshold=self.roll;offset=0
                for weight,operator,result,_ in v:
                    offset+=int(weight)
                    if threshold<offset:self.apply(result);break
                else:raise AssertionError('Random outcome outside list')
            elif k=='country_event':self.events.append(value(v,'id'))
            elif k=='add_timed_idea':self.ideas.add(value(v,'idea'))
            elif k=='add_ideas':self.ideas.add(v)
            elif k=='swap_ideas':self.ideas.discard(value(v,'remove_idea'));self.ideas.add(value(v,'add_idea'))
            elif k=='add_stability':self.stability+=float(v)
            elif k=='decrease_corruption':
                self.external[k]=self.external.get(k,0)+1
                level=next(int(n[-2:]) for n in self.ideas if n.startswith('corruption_level_'))
                check(level>1,'Never call MD floor PP compensation')
                self.ideas.discard(f'corruption_level_{level:02}');self.ideas.add(f'corruption_level_{level-1:02}')
            elif k=='increase_economic_growth':self.external[k]=self.external.get(k,0)+1
            elif k in ['log','custom_effect_tooltip']:pass
            elif k in FX:self.apply(FX[k])
            else:raise AssertionError(f'Unsupported effect {k}:{line}')
    def effect(self,name):self.apply(FX[name])
    def click(self,name):
        check(self.condition(value(DEC[name],'available',[])),name+' unavailable')
        self.pp-=float(value(DEC[name],'cost',0));self.apply(value(DEC[name],'complete_effect',[]))
    def option(self,event,index):
        option=blocks(EV[event],'option')[index]
        check(self.condition(value(option,'trigger',[])),event+' option unavailable')
        self.apply([n for n in option if n[0] not in ['name','trigger']])


def programme(program,mode,choice='B',growth=True):
    state=State();state.effect('VIE_select_programme_'+program);state.effect('VIE_launch_programme_'+mode)
    if program=='inspection':state.option('vie_pol.102','ABC'.index(choice))
    for day in range(1,902):
        state.effect('VIE_politics_daily')
        if growth and day==100:state.v['gdp_per_capita']=110
        if 'VIE_programme_active' not in state.flags:return state,day
        step=int(state.v['VIE_programme_step']);name=f'VIE_programme_{program}_{step}_{"standard" if mode=="standard" else "fast"}'
        if name in DEC and state.condition(value(DEC[name],'available',[])):state.click(name)
    raise AssertionError('Programme never terminates')


def run():
    for program,normal,fast in [('cadre',645,555),('admin',645,555),('inspection',735,645),('social',645,555)]:
        standard,day=programme(program,'standard');quick,early=programme(program,'fast_paid')
        check(day==normal and early==fast,f'{program} live timer {day}/{early}')
        check('VIE_last_programme_full' in standard.flags and 'VIE_last_programme_full' in quick.flags,'full after actual work')
        check('VIE_programme_early_full' not in standard.flags and 'VIE_programme_early_full' in quick.flags,'early cutoff')
        difference=standard.pp-quick.pp+(standard.v['treasury']-quick.v['treasury'])*40
        check(math.isclose(difference,5),f'{program} live fast price {difference}')
        before=copy.deepcopy(quick.__dict__);quick.effect('VIE_resolve_programme_full');quick.effect('VIE_resolve_programme_partial')
        check(before==quick.__dict__,'Resolver replay changed completed programme')
    for mode,expected in [('standard',825),('fast_paid',735)]:
        state,day=programme('inspection',mode,'C');check(day==expected,f'E102-C delay must add full 90 days: {day}')
    state,day=programme('social','fast_paid',growth=False)
    check(day==900 and 'VIE_last_programme_partial' in state.flags,'Passive clock cannot supply GDP evidence')
    # Budget/cohesion must remain valid for all 90 review days.
    for program,variable,bad in [('cadre','VIE_leadership_cohesion',54),('admin','treasury_rate',-.1)]:
        state=State();state.flags|={'VIE_programme_active','VIE_programme_job_running','VIE_programme_job_review','VIE_programme_'+program}
        state.v.update({'VIE_programme_epoch':1,'VIE_programme_job_epoch':1,'VIE_programme_step':3 if program=='cadre' else 2,'VIE_programme_job_remaining':1,variable:bad})
        state.effect('VIE_politics_programme_tick');check(state.v['VIE_programme_job_remaining']==90,'Broken review condition resets streak')
    state=State();state.ideas={'corruption_level_01'};state.effect('VIE_select_programme_inspection');state.effect('VIE_launch_programme_fast_paid')
    check(state.v['VIE_programme_corruption_baseline']==1,'Corruption snapshot')
    state.flags|={'VIE_programme_job_running'};state.v.update({'VIE_programme_step':2,'VIE_programme_job_epoch':1})
    state.effect('VIE_politics_job_finish');check(not state.external,'Floor grants no MD compensation')
    # Exact gates: 270 inclusive, 271 closed; deterministic C total840 inclusive.
    for day in [270,271]:
        state=State();state.v['VIE_congress_elapsed']=day
        check(state.condition(TR['VIE_politics_can_select'])==(day==270),'Start window boundary')
    for forecast in [750,750.001]:
        state=State();state.flags|={'VIE_programme_active','VIE_e102_choice_pending'};state.v.update({'VIE_programme_epoch':1,'VIE_e102_choice_epoch':1,'VIE_programme_forecast_days':forecast})
        option=blocks(EV['vie_pol.102'],'option')[2]
        check(state.condition(value(option,'trigger'))==(forecast==750),'C forecast must respect840 inclusive')
    for kind,cutoff in [('admin',600),('inspection',690)]:
        for day in [cutoff,cutoff+1]:
            state=State();state.flags|={'VIE_programme_active','VIE_programme_review_done','VIE_programme_'+kind}
            state.v.update({'VIE_programme_epoch':1,'VIE_programme_targets_met':4,'VIE_programme_elapsed':day})
            before=state.pp;state.effect('VIE_resolve_programme_full')
            check(state.pp-before==(70 if day==cutoff else 0),'Inclusive early PP cutoff')
            check('VIE_last_programme_full' in state.flags,'Late full must remain full')
    state=State();state.bop=0;state.v['VIE_leadership_cohesion']=0
    state.effect('VIE_select_programme_inspection')
    check(not state.condition(TR['VIE_politics_can_launch_standard']),'Low cohesion default810 violates start800')
    for tier in range(4):
        for cohesion in [0,19,20,39,40,54,55,69,70,100]:
            state=State();state.v.update({'VIE_tier_cadre':tier,'VIE_leadership_cohesion':cohesion})
            state.effect('VIE_select_programme_admin');charge=state.v['VIE_programme_start_cost']+55
            state.pp=charge-.01;check(not state.condition(TR['VIE_politics_can_launch_fast_paid']),'No underfunded launch')
            state.pp=charge;check(state.condition(TR['VIE_politics_can_launch_fast_paid']),'Exact funding inclusive')
    state=State();state.flags|={'VIE_programme_active','VIE_programme_job_running','VIE_programme_social'}
    state.v.update({'VIE_programme_epoch':1,'VIE_programme_job_epoch':1,'VIE_programme_step':1,'VIE_programme_job_remaining':10})
    state.controlled.discard(526);state.effect('VIE_politics_programme_tick')
    check(state.v['VIE_programme_job_remaining']==10,'Occupied project site must pause work')
    # An old event cannot bind itself to the new epoch just because globals changed.
    for name in ['vie_pol.102','vie_pol.104']:
        state=State();state.v.update({'VIE_last_congress':10,'VIE_programme_epoch':2,'VIE_e102_choice_epoch':2,'VIE_e104_offer_epoch':2})
        state.flags|={'VIE_programme_active','VIE_e102_choice_pending'}
        before=copy.deepcopy(state.__dict__)
        for option in blocks(EV[name],'option'):state.apply([n for n in option if n[0] not in ['name','trigger']])
        check(before==state.__dict__,'Old IX popup cannot charge/choose for X')
    state=State();state.v['VIE_e104_contract_epoch']=2;state.flags|={'VIE_e104_signed','VIE_e104_rights_unused','VIE_e104_amendment_preapproved'}
    before=copy.deepcopy(state.__dict__)
    for option in blocks(EV['vie_pol.132'],'option'):state.apply([n for n in option if n[0] not in ['name','trigger']])
    check(before==state.__dict__,'Old contract popup cannot amend/cancel a new ledger')
    # Signing is not a payment; two actual paid checks precede support/training.
    state=State();state.flags.add('VIE_programme_active');state.v.update({'VIE_programme_epoch':1,'VIE_e104_offer_epoch':1})
    cash=state.v['treasury'];state.option('vie_pol.104',1)
    check(state.v['treasury']==cash and 'VIE_e104_signed' not in state.flags,'No immediate support/signature')
    for _ in range(21):state.effect('VIE_politics_e104_tick')
    check('VIE_e104_signed' in state.flags and state.v['VIE_e104_contract_elapsed']==0,'Frozen21day signature')
    pp=state.pp;state.click('VIE_e104_fund_check_1');state.click('VIE_e104_training_task')
    for _ in range(90):state.effect('VIE_politics_e104_tick')
    check('VIE_e104_check1_done' in state.flags and state.v['treasury']==cash,'First check is not support payment')
    state.click('VIE_e104_fund_check_2')
    for _ in range(90):state.effect('VIE_politics_e104_tick')
    check(math.isclose(state.v['treasury']-cash,.25) and state.pp-pp==5,'Two checks cost20, completed training grants25')
    before=copy.deepcopy(state.__dict__);state.effect('VIE_politics_e104_tick');check(before==state.__dict__,'Settlement/reward replay')
    state=State();state.v['VIE_e104_promised_support']=.75;state.effect('VIE_politics_e104_open')
    for _ in range(90):state.effect('VIE_politics_e104_tick')
    check('VIE_e104_terminated' in state.flags and state.v['VIE_e104_remaining_support']==0 and state.v['VIE_leadership_cohesion']==54,'Missed obligation has real consequence')
    # Both random branches are executed from live focus/task rewards.
    for roll,delta in [(64,4),(65,-4)]:
        state=State();state.roll=roll;state.apply(value(FOCUS['VIE_ix11_rotate_cadres'],'completion_reward'))
        check(state.v['VIE_leadership_cohesion']==60+delta,'65/35 boundary')
        before=copy.deepcopy(state.__dict__);state.apply(value(FOCUS['VIE_ix11_rotate_cadres'],'completion_reward'));check(before==state.__dict__,'No reroll/refund')
    for roll,success in [(69,True),(70,False)]:
        state=State();state.roll=roll;state.flags.add('VIE_project_XI10_running');state.v['VIE_project_XI10_elapsed']=89
        state.effect('VIE_politics_project_tick');check(('VIE_XI10_recovered' in state.flags)==success,'70/30 boundary')
        check(math.isclose(state.v['treasury'],50.75 if success else 50) and state.v['VIE_leadership_cohesion']==(60 if success else 48),'Observable recovery/failure')
    # Actual writer choice -> reader gate, not a utility flag; stale second popup is inert.
    event=next(name for name,block in EV.items() if value(block,'title')=='vie_pol_runtime.10.t')
    for option,opened in [(0,True),(1,False)]:
        state=State();state.v['VIE_last_congress']=11;state.flags.add('VIE_pending_X01');state.option(event,option)
        check(state.condition(value(FOCUS['VIE_xi05_real_estate_bad_debt'],'available'))==opened,'X01 gate reaches real XI05')
        before=copy.deepcopy(state.__dict__);other=blocks(EV[event],'option')[1-option]
        state.apply([n for n in other if n[0] not in ['name','trigger']]);check(before==state.__dict__,'Old popup must not rewrite choice')
    for term,opened in [(12,False),(13,True)]:
        state=State();state.v['VIE_last_congress']=term;state.flags.add('VIE_record_XII12_A')
        check(state.condition(value(FOCUS['VIE_xii09_protect_substantive_decisions'],'available'))==opened,'Sequential handover locks XII09 only for XII')
    for name,body in FX.items():
        if not name.startswith('VIE_politics_consume_'):continue
        node=name.removeprefix('VIE_politics_consume_')
        for option in ['A','B']:
            state=State();state.flags.add('VIE_record_'+node+'_'+option);pp,cash=state.pp,state.v['treasury'];state.effect(name)
            check(state.pp-pp==(8 if option=='A' else 0) and math.isclose(state.v['treasury']-cash,.2 if option=='B' else 0),'Consumer actual rebate '+node)
            before=copy.deepcopy(state.__dict__);state.effect(name);check(before==state.__dict__,'Consumer replay '+node)
        calls=sum(any(k==name for k,op,v,line in value(focus,'completion_reward',[])) for focus in FOCUS.values())
        check(calls==1,'Consumer must have exactly one real reader completion caller '+node)
    state=State();state.v.update({'VIE_programme_epoch':2,'VIE_last_side_project_epoch':1});state.flags.add('VIE_programme_early_full')
    state.apply(value(DEC['VIE_side_project_decision'],'remove_effect'))
    check('VIE_side_project_bureaucracy_idea' not in state.ideas,'Old side-project callback cannot award in a later epoch')
    state=State();state.flags.add('VIE_programme_active');state.v.update({'VIE_programme_epoch':2,'VIE_programme_job_epoch':1,'VIE_programme_step':0})
    state.flags.add('VIE_programme_job_running');state.effect('VIE_politics_job_finish');check(state.v['VIE_programme_step']==0,'Old job epoch cannot supply evidence')
    state=State();state.effect('VIE_politics_runtime_init');state.effect('VIE_politics_runtime_init');check(state.events.count('vie_pol_runtime.1')==1,'Startup/load creates one clock chain')
    check(len(blocks(EV['vie_pol.103'],'option'))==1,'E103 is informational, not A/B/C')
    print(f'PASS: {CHECKS} live-script checks; narrow fixture, not HOI4 runtime')


if __name__=='__main__':run()
