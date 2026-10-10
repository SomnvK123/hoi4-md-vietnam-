"""Read live V35 scripts and test gates, transactions and idempotent rewards.

This limited interpreter is a static fixture, not the HOI4 engine. Unknown
statements fail closed instead of silently treating them as supported.
Run: python tools/audit/naval_scenarios.py
"""
from __future__ import annotations

import ast
import argparse
import copy
import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = json.loads((Path(__file__).with_name('naval_v35_spec.json')).read_text(encoding='utf-8'))
# Reuse the repository parser without executing audit.py's reporting/file writes.
source = ast.parse((ROOT / 'tools/audit/audit.py').read_text(encoding='utf-8'))
namespace = {}
ast_functions = [n for n in source.body if isinstance(n, ast.FunctionDef) and n.name in ('tokenize', 'parse')]
exec(compile(ast.Module(body=ast_functions, type_ignores=[]), 'audit_parser', 'exec'), namespace)


def load(path):
    text = (ROOT / path).read_text(encoding='utf-8-sig')
    # Remove comments outside quoted strings; preserve localisation/log tokens.
    clean = []
    for line in text.splitlines():
        quoted = False
        for i, char in enumerate(line):
            if char == '"' and (i == 0 or line[i-1] != '\\'):
                quoted = not quoted
            if char == '#' and not quoted:
                line = line[:i]
                break
        clean.append(line)
    return namespace['parse'](namespace['tokenize']('\n'.join(clean)))


def values(block, key):
    return [v for k, op, v, line in block if k == key]


def value(block, key, default=None):
    return next(iter(values(block, key)), default)


FOCUSES = {value(v, 'id'): v for v in values(load('common/national_focus/VIE_md_focus.txt')[0][2], 'focus')}
EFFECTS = {k: v for k, op, v, line in load('common/scripted_effects/VIE_md_effects.txt')}
TRIGGERS = {k: v for k, op, v, line in load('common/scripted_triggers/VIE_md_triggers.txt')}
IDEAS = {k: v for k, op, v, line in value(load('common/ideas/VIE_md_ideas.txt'), 'ideas')
         if k == 'country' for k, op, v, line in v}
DECISIONS = {k: v for k, op, v, line in value(load('common/decisions/VIE_md_decisions.txt'), 'VIE_naval_procurement_category')}
EVENTS = {value(v,'id'):v for v in values(load('events/VIE_md_events.txt'),'country_event')}


class State:
    def __init__(self, year=2026, money=50):
        self.focuses = set()
        self.flags = set()
        self.flag_dates = {}
        self.clock = 0
        self.ideas = set()
        self.variables = {'treasury': money, 'VIE_catch_up': 0, 'skip_payment': 0}
        self.year = year
        self.month = self.day = 1
        self.research = []
        self.events = []
        self.xp = self.mastery = self.dockyards = 0
        self.has_coast = True
        self.doctrine = False
        self.technologies = set(SPEC['ship_blueprint']['technologies'])
        self.base_level = self.yard_level = 1
        self.variants = {}
        self.ships = []

    def condition(self, block, mode='AND'):
        results = []
        for k, op, v, line in block:
            if k in ('AND', 'OR', 'NOT'):
                result = self.condition(v, 'OR' if k == 'OR' else 'AND')
                if k == 'NOT': result = not result
            elif k == 'has_completed_focus': result = v in self.focuses
            elif k == 'has_country_flag':
                if isinstance(v,list):
                    target=value(v,'flag')
                    days=next((int(number) for name,compare,number,_ in v if name=='days'),0)
                    result=target in self.flags and self.clock-self.flag_dates.get(target,self.clock)>days
                else:result = v in self.flags
            elif k == 'has_tech': result = v in self.technologies
            elif k == 'has_idea': result = v in self.ideas
            elif k == 'check_variable':
                comparisons = []
                for var, compare, number, _ in v:
                    actual = self.variables.get(var, 0)
                    expected = float(number)
                    comparisons.append({'=': actual == expected, '>': actual > expected,
                                        '<': actual < expected, '>=': actual >= expected,
                                        '<=': actual <= expected}[compare])
                result = all(comparisons)
            elif k == 'date':
                when = tuple(int(x) for x in v.split('.'))
                now = (self.year, self.month, self.day)
                result = now > when if op == '>' else now < when
            elif k == 'original_tag': result = v == 'VIE'
            elif k == 'is_ai': result = v == 'no'
            elif k == 'has_selected_naval_grand_doctrine': result = self.doctrine
            elif k in ('any_owned_state',): result = self.has_coast and self.condition(v)
            elif k in ('is_controlled_by', 'is_coastal', 'free_building_slots'): result = self.has_coast
            elif k == 'naval_base': result = self.base_level>float(v)
            elif k == 'dockyard': result = self.yard_level>float(v)
            elif k in TRIGGERS and k.startswith('VIE_nav35_'): result = self.condition(TRIGGERS[k])
            else: raise AssertionError(f'Unsupported trigger {k}:{line}')
            results.append(result)
        return any(results) if mode == 'OR' else all(results)

    def apply(self, block):
        selected = False
        for k, op, v, line in block:
            if k == 'if':
                selected = self.condition(value(v, 'limit', []))
                if selected: self.apply([n for n in v if n[0] != 'limit'])
            elif k == 'else_if':
                if not selected and self.condition(value(v, 'limit', [])):
                    selected = True
                    self.apply([n for n in v if n[0] != 'limit'])
            elif k == 'else':
                if not selected: self.apply(v)
                selected = True
            elif k in ('hidden_effect',): self.apply(v)
            elif k == 'set_country_flag': self.flags.add(v);self.flag_dates[v]=self.clock
            elif k == 'clr_country_flag': self.flags.discard(v);self.flag_dates.pop(v,None)
            elif k == 'add_ideas': self.ideas.add(v)
            elif k == 'remove_ideas': self.ideas.discard(v)
            elif k == 'add_timed_idea': self.ideas.add(value(v, 'idea'))
            elif k == 'set_temp_variable':
                for var, _, number, _ in v: self.variables[var] = float(number)
            elif k == 'modify_treasury_effect': self.variables['treasury'] += self.variables['treasury_change']
            elif k == 'add_tech_bonus': self.research.append((value(v, 'name'), value(v, 'category'), float(value(v, 'bonus'))))
            elif k == 'country_event': self.events.append(value(v, 'id'))
            elif k == 'create_equipment_variant':
                name=value(v,'name');hull=value(v,'type')
                assert hull in self.technologies,'unresearched variant hull'
                self.variants[name]=(hull,{key:module for key,op,module,line in value(v,'modules')})
            elif k == 'create_ship':
                name=value(v,'equipment_variant');hull=value(v,'type')
                assert name in self.variants and self.variants[name][0]==hull,'unresolved ship variant'
                assert self.has_coast and self.base_level>0,'delivery without controlled base'
                self.ships.extend([(hull,name)]*int(value(v,'amount',1)))
            elif k == 'navy_experience': self.xp += float(v)
            elif k == 'add_mastery': self.mastery += float(value(v, 'amount'))
            elif k == 'random_owned_controlled_state':
                if self.has_coast and self.condition(value(v, 'limit', [])):
                    self.apply([n for n in v if n[0] != 'limit'])
            elif k == 'one_state_dockyard':
                self.dockyards += 1
                if not self.variables.get('skip_payment'): self.variables['treasury'] -= 7.5
            elif k in ('log', 'custom_effect_tooltip', 'add_command_power', 'add_stability'): pass
            elif k in EFFECTS: self.apply(EFFECTS[k])
            else: raise AssertionError(f'Unsupported effect {k}:{line}')

    def can_focus(self, fid):
        block = FOCUSES[fid]
        for group in values(block, 'prerequisite'):
            if not any(v in self.focuses for v in values(group, 'focus')): return False
        for group in values(block, 'mutually_exclusive'):
            if any(v in self.focuses for v in values(group, 'focus')): return False
        return self.condition(value(block, 'available', []))

    def finish_focus(self, code):
        fid = 'VIE_nav35_' + code
        self.focuses.add(fid)
        self.apply(value(FOCUSES[fid], 'completion_reward'))

    def acknowledge(self, event_id):
        self.apply([n for n in value(EVENTS[event_id],'option') if n[0] not in ('name','ai_chance')])


checks = 0
def check(condition, message):
    global checks
    assert condition, message
    checks += 1
    print('PASS ', message)


def graph_tests():
    check(len([k for k in FOCUSES if k.startswith('VIE_nav35_')]) == 40, 'exactly 40 V35 focuses')
    for n in SPEC['nodes']:
        block = FOCUSES[n['id']]
        deps = list(dict.fromkeys(([n['parent']] if n['parent'] else []) + n['all']))
        expected = [frozenset({'VIE_nav35_'+d}) for d in deps]
        if n['code'] == 'N00': expected += [frozenset({'VIE_modernize_vpa'})]
        if n['any']: expected += [frozenset('VIE_nav35_'+d for d in n['any'])]
        actual = [frozenset(values(g,'focus')) for g in values(block,'prerequisite')]
        check(set(actual) == set(expected), n['code']+' AND/OR matches design')
        mutex = set(itertools.chain.from_iterable(values(g,'focus') for g in values(block,'mutually_exclusive')))
        check(mutex == {'VIE_nav35_'+d for d in n['mutex']}, n['code']+' mutex matches design')
        declared_year=int(n['year'])
        if declared_year>2000:
            s=State(declared_year-1);s.focuses.update(v for group in values(block,'prerequisite') for v in values(group,'focus'))
            check(not s.can_focus(n['id']),n['code']+' cannot open before stated year')
            s.year=declared_year
            check(s.can_focus(n['id']),n['code']+' opens at stated year with prerequisites satisfied')
    for route,year in [('P',2011),('G',2014),('B',2015)]:
        s=State(year)
        s.focuses.add('VIE_modernize_vpa')
        excluded = ({'H01','H02','G01','G02','G03','B01','B02','B03'} if route == 'P'
                    else {'P01','P02','P03','P04','P05','P06'} | ({'B01','B02','B03'} if route == 'G' else {'G01','G02','G03'}))
        for n in SPEC['nodes']:
            if n['code'] not in excluded and s.can_focus(n['id']): s.finish_focus(n['code'])
        check('VIE_nav35_F02' in s.focuses, route+' reaches F02 by '+str(year)+' without I07/L03')
        check('VIE_nav35_I07' not in s.focuses, route+' does not require 2026 project')
        routeideas=[i for i in s.ideas if i.startswith(('VPA_Integrated','VPA_Fleet','VPA_Multirole','VPA_Greenwater','VPA_Bluewater','VIE_nav_capstone'))]
        check(len(routeideas)==1 and routeideas[0].startswith('VIE_nav_capstone'),route+' final replaces all starter/capstone route ideas')
        before=copy.deepcopy(s.__dict__)
        for _ in range(3): s.apply(EFFECTS['VIE_nav35_refresh'])
        check(s.__dict__==before,route+' repeated refresh has zero side effects')
    s=State(2026);s.focuses={'VIE_nav35_T02'}
    check(not s.can_focus('VIE_nav35_T04'), 'T04 blocks when T03 missing')
    for c in ('P06','G03','B03'):
        s.focuses={'VIE_nav35_'+c}
        check(s.can_focus('VIE_nav35_F01'),'F01 accepts '+c+' independently')
    s=State(2000);s.focuses={'VIE_nav35_F01','VIE_nav35_S03'}
    check(not s.can_focus('VIE_nav35_F02'),'F02 requires L04 explicitly')
    s=State(2025);s.focuses={'VIE_nav35_I05','VIE_nav35_I06'}
    check(not s.can_focus('VIE_nav35_I07'),'I07 cannot start before 2026')


def project_tests():
    for p in SPEC['projects']:
        key=p['key']; stem='VIE_nav35_'+key; cost=p['cost']
        s=State(2026,cost-0.01)
        s.focuses={'VIE_nav35_'+p['focus']}
        if key=='asw_frigate':s.flags.add('VIE_nav35_asw_frigate_offered')
        s.apply(EFFECTS[stem+'_start'])
        check(stem+'_running' not in s.flags and s.variables['treasury']==cost-0.01,key+' cannot spend insufficient treasury')
        s.variables['treasury']=cost
        s.apply(EFFECTS[stem+'_start'])
        check(stem+'_running' in s.flags and abs(s.variables['treasury'])<1e-8,key+' pays once at start')
        before=copy.deepcopy(s.__dict__)
        s.apply(EFFECTS[stem+'_start'])
        check(before==s.__dict__,key+' duplicate start is inert')
        if key=='asw_frigate':s.clock+=1095
        s.apply(EFFECTS[stem+'_finish'])
        check(stem+'_done' in s.flags and stem+'_running' not in s.flags,key+' finishes and clears running state')
        before=copy.deepcopy(s.__dict__)
        s.apply(EFFECTS[stem+'_finish']);s.apply(EFFECTS[stem+'_start'])
        check(before==s.__dict__,key+' duplicate finish/restart cannot reward or charge')
        check(int(value(DECISIONS[stem+'_program'],'days_remove'))==p['days'],key+' duration matches spec')
    s=State()
    s.focuses={'VIE_nav35_I01'};s.has_coast=False
    s.apply(EFFECTS['VIE_nav35_dockyard_start'])
    check(s.dockyards==0 and s.variables['treasury']==50,'no coast/slots: dockyard has no charge or construction')
    for doctrine in (False,True):
        s=State();s.doctrine=doctrine;s.apply(EFFECTS['VIE_nav_xp_15'])
        check((s.mastery,s.xp)==((15,0) if doctrine else (0,15)),'naval XP/mastery branch '+str(doctrine))


def timing_tests():
    s=State(2000);s.finish_focus('T01')
    check('VIE_nav35_regions_done' not in s.flags,'regional bonus waits until 2009')
    s.year=2009;s.apply(EFFECTS['VIE_nav35_scheduler'])
    check('VIE_nav35_regions_done' in s.flags,'monthly scheduler grants 2009 regional bonus')
    before=copy.deepcopy(s.__dict__);s.apply(EFFECTS['VIE_nav35_scheduler'])
    check(before==s.__dict__,'regional milestone cannot repeat')
    s=State(2026);s.variables['VIE_catch_up']=1;s.finish_focus('I06')
    check('VIE_nav35_integration_2022_done' in s.flags and 'VIE_nav35_integration_2025_done' in s.flags,'late focus/catch-up receives both integration milestones')
    check(not s.events,'late milestones do not flood popup queue')
    s=State(2026);s.focuses={'VIE_nav35_I07'};s.month=10;s.day=4
    s.apply(EFFECTS['VIE_nav35_scheduler'])
    check('VIE_nav35_asw_2026_milestone_recorded' not in s.flags,'keel news waits until 5 October 2026')
    s.day=5;s.apply(EFFECTS['VIE_nav35_scheduler'])
    check('vie_nav35.7' in s.events and 'VIE_nav35_asw_frigate_done' not in s.flags,'keel news does not complete funded gameplay project')
    before=copy.deepcopy(s.__dict__);s.apply(EFFECTS['VIE_nav35_scheduler'])
    check(before==s.__dict__,'keel news cannot repeat')
    for order in [('S02','S03'),('S03','S02')]:
        s=State()
        for c in order:s.finish_focus(c)
        check('VPA_Maritime_MDA_4' in s.ideas and 'VIE_nav35_joint_picture_idea' in s.ideas,'optional aviation bonus in either focus order '+str(order))
    for order in (('G02','project'),('project','G02')):
        s=State()
        for c in order:
            if c=='project':s.flags.add('VIE_nav35_asw_frigate_done');s.apply(EFFECTS['VIE_nav35_refresh'])
            else:s.finish_focus(c)
        check('VIE_nav35_domestic_asw_support_idea' in s.ideas,'G02 optional ASW result in either order '+str(order))
    for order in (('L04','project'),('project','L04')):
        s=State()
        for c in order:
            if c=='project':s.flags.add('VIE_nav35_vt_done');s.apply(EFFECTS['VIE_nav35_refresh'])
            else:s.finish_focus(c)
        check('VIE_nav35_rescue_range_idea' in s.ideas,'L04 transport bonus in either order '+str(order))
    for route, excluded in [('P',{'H01','H02','G01','G02','G03','B01','B02','B03'}),
                            ('G',{'P01','P02','P03','P04','P05','P06','B01','B02','B03'}),
                            ('B',{'P01','P02','P03','P04','P05','P06','G01','G02','G03'})]:
        s=State(2026,100);s.focuses.add('VIE_modernize_vpa')
        for n in SPEC['nodes']:
            if n['code'] not in excluded and s.can_focus(n['id']):s.finish_focus(n['code'])
        for p in SPEC['projects']:
            if p['focus'] not in excluded:
                if p['key']=='asw_frigate':s.acknowledge('vie_nav35.5')
                s.apply(EFFECTS['VIE_nav35_'+p['key']+'_start'])
                if p['key']=='asw_frigate':s.clock+=1095
                s.apply(EFFECTS['VIE_nav35_'+p['key']+'_finish'])
        totals={}
        for idea in s.ideas:
            for k,op,v,line in value(IDEAS[idea],'modifier',[]):totals[k]=totals.get(k,0)+float(v)
        check(totals.get('navy_org',0)<=14,route+' 2026 total naval organization <= 14')
        check(totals.get('navy_max_range_factor',0)<=.34,route+' 2026 total range <= 34%')
        check(totals.get('industrial_capacity_dockyard',0)<=.20,route+' 2026 dockyard output <= 20% including naval projects')
        check(s.xp+s.mastery<=450,route+' one-time XP/mastery <= 450')
        names=[r[0] for r in s.research]
        check(len(names)==len(set(names)),route+' research rewards have unique names')
    group=('VPA_Fleet_Development_Priority','VPA_Multirole_Task_Groups','VPA_Greenwater_Doctrine_1','VPA_Greenwater_Doctrine_Capstone','VPA_Bluewater_Doctrine_1','VPA_Bluewater_Doctrine_Capstone','VIE_nav_capstone_master_of_seas','VIE_nav_capstone_ocean_surge')
    for k in group:
        mods=value(IDEAS[k],'modifier')
        actual=float(value(mods,'navy_personnel_cost_multiplier_modifier'))
        expected=.25 if ('Bluewater' in k or 'ocean' in k) else (.10 if ('Greenwater' in k or 'master' in k) else .05)
        check(actual==expected,k+' upkeep matches economic tier')


def frigate_tests():
    stem='VIE_nav35_asw_frigate'
    def funded():
        s=State(2026,1)
        s.finish_focus('I07');s.acknowledge('vie_nav35.5')
        s.apply(EFFECTS[stem+'_start'])
        return s
    s=State(2026,1);s.finish_focus('I07')
    check(s.events.count('vie_nav35.5')==1 and stem+'_offered' not in s.flags,'I07 queues approval event before unlocking decision')
    check(not s.condition(TRIGGERS[stem+'_can_start']),'no contract before acknowledging approval event')
    s.acknowledge('vie_nav35.5')
    check(stem+'_offered' in s.flags and stem+'_offer_queued' not in s.flags,'approval event unlocks first-ship decision')
    before=copy.deepcopy(s.__dict__);s.acknowledge('vie_nav35.5');s.apply(EFFECTS[stem+'_offer'])
    check(before==s.__dict__,'replayed approval cannot queue event or duplicate unlock')
    for tech in SPEC['ship_blueprint']['technologies']:
        missing=copy.deepcopy(s);missing.technologies.remove(tech)
        missing.apply(EFFECTS[stem+'_start'])
        check(stem+'_running' not in missing.flags and missing.variables['treasury']==1,'missing '+tech+' prevents charge and construction')
    for field in ('base_level','yard_level'):
        missing=copy.deepcopy(s);setattr(missing,field,0)
        missing.apply(EFFECTS[stem+'_start'])
        check(stem+'_running' not in missing.flags and missing.variables['treasury']==1,'missing '+field+' prevents starting contract')
    s=funded();check(abs(s.variables['treasury']-.4)<1e-8 and not s.ships,'contract pays 0.6 once and grants no ship at start')
    s.clock=1094;s.apply(EFFECTS[stem+'_finish'])
    check(not s.ships and stem+'_running' in s.flags,'no delivery before 1095 elapsed days')
    saved=copy.deepcopy(s);saved.clock+=1;saved.apply(EFFECTS[stem+'_finish'])
    check(len(saved.ships)==1 and saved.ships[0]==(SPEC['ship_blueprint']['hull'],SPEC['ship_blueprint']['name']),'saved running state delivers exactly one fixed frigate at 1095 days')
    check(saved.variants[SPEC['ship_blueprint']['name']][1]==SPEC['ship_blueprint']['modules'],'delivered variant matches immutable contract blueprint')
    before=copy.deepcopy(saved.__dict__)
    for _ in range(3):
        saved.apply(EFFECTS[stem+'_finish']);saved.apply(EFFECTS[stem+'_deliver']);saved.apply(EFFECTS[stem+'_start']);saved.acknowledge('vie_nav35.6')
    check(before==saved.__dict__,'replayed completion/delivery/event cannot charge or spawn again')
    s=funded();s.base_level=0;s.clock=1095;s.apply(EFFECTS[stem+'_finish'])
    check(not s.ships and stem+'_ready' in s.flags and stem+'_running' not in s.flags,'lost base queues completed vessel without spawning')
    s.apply(EFFECTS['VIE_nav35_scheduler'])
    check(not s.ships and abs(s.variables['treasury']-.4)<1e-8,'monthly retry without base does not charge or spawn')
    s.base_level=1;s.yard_level=0;s.apply(EFFECTS['VIE_nav35_scheduler'])
    check(len(s.ships)==1 and stem+'_done' in s.flags and abs(s.variables['treasury']-.4)<1e-8,'base restored delivers paid vessel despite lost yard, without extra charge')
    s=funded();s.clock=1095;s.technologies.remove(SPEC['ship_blueprint']['hull']);s.apply(EFFECTS[stem+'_finish'])
    check(not s.ships and stem+'_ready' in s.flags,'missing delivery hull technology leaves vessel pending')
    s.technologies.add(SPEC['ship_blueprint']['hull']);s.apply(EFFECTS['VIE_nav35_scheduler'])
    check(len(s.ships)==1,'delivery resumes after technology restored')
    s=funded();s.clock=1100;s.apply(EFFECTS['VIE_nav35_scheduler'])
    check(len(s.ships)==1,'monthly recovery completes elapsed contract if timer callback missed')
    offer=State();offer.acknowledge('vie_nav35.5')
    check(stem+'_offered' not in offer.flags,'manual approval event before I07 cannot unlock program')
    check(all('asw_'+kind+'_program' not in ''.join(DECISIONS) for kind in ('design','prototype','evaluation')),'three obsolete research stages removed')


def provider_tests(md, game):
    md=Path(md);game=Path(game)
    engine=(game/'documentation/modifiers_documentation.md').read_text(encoding='utf-8-sig')
    defined_modifiers=set(re.findall(r'^## (\w+)',engine,re.M))
    for p in (md/'common/modifier_definitions').glob('*.txt'):
        defined_modifiers.update(re.findall(r'^(\w+)\s*=\s*\{',p.read_text(encoding='utf-8-sig'),re.M))
    defined_modifiers.add('production_speed_dockyard_factor')  # Engine generated building modifier.
    navytext=(ROOT/'common/ideas/VIE_md_ideas.txt').read_text(encoding='utf-8')
    navytext=navytext[navytext.index('# Hai quan V35.1'):navytext.index('# SECTION: VIE_md_ideas_p2.txt')]
    used=re.findall(r'^\s{2,}(\w+)\s*=\s*-?[\d.]+\s*$',navytext,re.M)
    check(not set(used)-defined_modifiers,'all V35 country modifiers exist in engine/MD provider')
    techs='\n'.join(p.read_text(encoding='utf-8-sig') for p in (md/'common/technologies').glob('*.txt'))
    tree=(ROOT/'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8')
    focus=tree[tree.index('# Hai quan V35.1: 40 focus'):tree.index('id = VIE_force_47')]
    effects=(ROOT/'common/scripted_effects/VIE_md_effects.txt').read_text(encoding='utf-8')
    effects=effects[effects.index('# Hai quan V35.1: ham tinh lai'):]
    usedcats=set(re.findall(r'category\s*=\s*(CAT_\w+)',focus+effects))
    check(all(re.search(r'\b'+cat+r'\b',techs) for cat in usedcats),'all V35 research categories exist in installed MD')
    interfaces='\n'.join(p.read_text(encoding='utf-8-sig',errors='replace') for base in (ROOT,md,game) for p in (base/'interface').glob('*.gfx'))
    provider_sprites=set(re.findall(r'name\s*=\s*"([^"]+)"',interfaces))
    for icon in sorted(set(SPEC['icons'].values())):
        check('GFX_focus_VIE_'+icon in provider_sprites,'sprite provider: '+icon)
    check('GFX_idea_generic_navy_bonus' in provider_sprites,'generic navy idea picture provider')
    check('GFX_report_event_military_planning' in provider_sprites,'new event picture provider')
    check('GFX_decision_generic_naval' in provider_sprites,'naval decision picture provider')
    triggertext='\n'.join(p.read_text(encoding='utf-8-sig') for p in (md/'common/scripted_triggers').glob('*.txt'))
    check(bool(re.search(r'^can_staff_an_dockyard\s*=\s*\{',triggertext,re.M)),'dockyard staffing trigger provider')
    blueprint=SPEC['ship_blueprint']
    equipment=value(load(md/'common/units/equipment/MD_mtg_ships.txt'),'equipments')
    hull=value(equipment,blueprint['hull']);check(hull is not None,'contract frigate hull exists in installed MD')
    slots=value(value(equipment,'frigate'),'module_slots')
    modules=value(load(md/'common/units/equipment/modules/MD_ship_modules.txt'),'equipment_modules')
    technologies={}
    for path in (md/'common/technologies').glob('*.txt'):
        for key,op,block,line in value(load(path),'technologies',[]):technologies[key]=block
    unlocked=set()
    for tech in blueprint['technologies']:
        check(tech in technologies,'contract technology provider: '+tech)
        for group in values(technologies[tech],'enable_equipment_modules'):
            unlocked.update(key for key,op,block,line in group)
    counts={}
    for slot,module in blueprint['modules'].items():
        slotdef=value(slots,slot);check(slotdef is not None,'contract slot provider: '+slot)
        if module=='empty':continue
        mod=value(modules,module);check(mod is not None and module in unlocked,'module exists and unlock technology required: '+module)
        category=value(mod,'category');allowed={key for key,op,block,line in value(slotdef,'allowed_module_categories')}
        # MD historical variants use the dedicated ammo slot with an empty category list.
        check(category in allowed or slot=='fixed_ship_missile_ammo_slot' and not allowed,'slot/category compatibility: '+slot)
        counts[category]=counts.get(category,0)+1
    for limit in values(value(equipment,'frigate'),'module_count_limit'):
        category=value(limit,'category');maximum=int(value(limit,'count'))
        check(counts.get(category,0)<maximum,'frigate module-count cap: '+category)


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--md');parser.add_argument('--game')
    args=parser.parse_args()
    if bool(args.md) != bool(args.game):parser.error('pass both --md and --game')
    graph_tests();project_tests();timing_tests();frigate_tests()
    if args.md:provider_tests(args.md,args.game)
    print(f'ALL PASS: {checks} static scenarios. In-game runtime NOT RUN.')
