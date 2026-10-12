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
DYNAMIC = {k:v for k,op,v,line in load('common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt')}


class State:
    def __init__(self, year=2026, money=50):
        self.focuses = set()
        self.flags = set()
        self.flag_dates = {}
        self.clock = 0
        self.ideas = set()
        self.variables = {'treasury': money, 'VIE_catch_up': 0, 'skip_payment': 0}
        self.variables.update({'num_ships_with_type@corvette':2, 'num_ships_with_type@attack_submarine':1})
        self.doctrines = set()
        self.dynamic_modifiers = {'VIE_armed_forces_modifier'}
        self.command_power = 0
        self.doctrine_discounts = []
        self.year = year
        self.month = self.day = 1
        self.research = []
        self.events = []
        self.special_projects = set()
        self.xp = self.mastery = self.dockyards = 0
        self.has_coast = True
        self.doctrine = False
        self.technologies = {tech for ship in SPEC['ship_contracts'].values() for tech in ship['technologies']}
        self.base_level = self.yard_level = 1
        self.variants = {}
        self.ships = []
        self.variant_creations = 0
        self.state_scope = None
        self.effect_stack = []
        self.states = {sid: dict(owned=True, controlled=True, coastal=True,
                                rd=0, rd_capacity=True, slots=2, slot_growth=True,
                                dockyard=1, base=4, slot_grants=0)
                       for sid in (519, 522, 521)}

    def scoped_condition(self, block, sid):
        previous = self.state_scope
        self.state_scope = sid
        try: return self.condition(block)
        finally: self.state_scope = previous

    def scoped_apply(self, block, sid):
        previous = self.state_scope
        self.state_scope = sid
        try: self.apply(block)
        finally: self.state_scope = previous

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
            elif k == 'has_doctrine': result = v in self.doctrines
            elif k == 'is_special_project_completed': result = v.removeprefix('sp:') in self.special_projects
            elif k == 'custom_trigger_tooltip': result = self.condition([n for n in v if n[0]!='tooltip'])
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
            elif k == 'ROOT': result = self.scoped_condition(v, None)
            elif k.isdigit(): result = self.scoped_condition(v, int(k))
            elif k == 'any_owned_state':
                result = any(st['owned'] and self.scoped_condition(v, sid)
                             for sid, st in self.states.items())
            elif k == 'is_owned_by': result = self.states[self.state_scope]['owned']
            elif k == 'is_controlled_by': result = self.states[self.state_scope]['controlled']
            elif k == 'is_coastal': result = self.has_coast and self.states[self.state_scope]['coastal']
            elif k == 'free_building_slots':
                st = self.states[self.state_scope]
                result = self.has_coast and (st['base'] < 10 if value(v,'building')=='naval_base' else st['slots'] > 0)
            elif k == 'can_construct_building':
                assert v == 'naval_facility', (k,v)
                st = self.states[self.state_scope]
                result = self.has_coast and st['rd_capacity'] and st['rd'] == 0
            elif k == 'naval_facility': result = self.states[self.state_scope]['rd'] > float(v)
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
            elif k == 'swap_ideas':
                rem = value(v, 'remove_idea')
                add = value(v, 'add_idea')
                if rem: self.ideas.discard(rem)
                if add: self.ideas.add(add)
            elif k == 'add_timed_idea': self.ideas.add(value(v, 'idea'))
            elif k == 'set_temp_variable':
                for var, _, number, _ in v: self.variables[var] = float(number)
            elif k == 'add_to_variable':
                for var, _, number, _ in v: self.variables[var] = self.variables.get(var,0)+float(number)
            elif k == 'add_command_power': self.command_power += float(v)
            elif k == 'add_doctrine_cost_reduction':
                self.doctrine_discounts.append((value(v,'name'),float(value(v,'cost_reduction')),int(value(v,'uses'))))
            elif k == 'add_dynamic_modifier': self.dynamic_modifiers.add(value(v,'modifier'))
            elif k == 'modify_treasury_effect': self.variables['treasury'] += self.variables['treasury_change']
            elif k == 'add_tech_bonus': self.research.append((value(v, 'name'), value(v, 'category'), float(value(v, 'bonus'))))
            elif k == 'country_event': self.events.append(value(v, 'id'))
            elif k == 'create_equipment_variant':
                name=value(v,'name');hull=value(v,'type')
                assert hull in self.technologies,'unresearched variant hull'
                self.variants[name]=(hull,{key:module for key,op,module,line in value(v,'modules')})
                self.variant_creations += 1
            elif k == 'create_ship':
                name=value(v,'equipment_variant');hull=value(v,'type')
                assert name in self.variants and self.variants[name][0]==hull,'unresolved ship variant'
                assert self.has_coast and self.base_level>0,'delivery without controlled base'
                self.ships.extend([(hull,name)]*int(value(v,'amount',1)))
            elif k == 'navy_experience': self.xp += float(v)
            elif k == 'add_mastery': self.mastery += float(value(v, 'amount'))
            elif k == 'random_owned_controlled_state':
                for sid,st in self.states.items():
                    if st['owned'] and st['controlled'] and self.scoped_condition(value(v,'limit',[]),sid):
                        self.scoped_apply([n for n in v if n[0]!='limit'],sid)
                        break
            elif k == 'ROOT': self.scoped_apply(v,None)
            elif k == 'construct_building_in_random_province':
                assert value(v,'naval_facility')=='1' and self.state_scope is not None
                st=self.states[self.state_scope]
                assert st['rd_capacity'] and st['rd']==0
                st['rd']=1
            elif k == 'add_extra_state_shared_building_slots':
                # Legacy focuses outside I01-I07 remain outside the construction fixture.
                if not self.effect_stack or '_subsidy_apply' not in self.effect_stack[-1]: continue
                st=self.states[self.state_scope]
                st['slot_grants']+=int(v)
                if st['slot_growth']:st['slots']+=int(v)
            elif k == 'add_building_construction':
                if not self.effect_stack or '_subsidy_apply' not in self.effect_stack[-1]: continue
                assert value(v,'instant_build')=='yes'
                st=self.states[self.state_scope]
                if value(v,'type')=='dockyard':
                    assert st['slots']>0
                    st['dockyard']+=int(value(v,'level'));st['slots']-=int(value(v,'level'))
                    self.dockyards+=int(value(v,'level'))
                else:
                    assert value(v,'type')=='naval_base' and value(v,'province')=='10309' and self.state_scope==521
                    assert st['base']<10
                    st['base']+=int(value(v,'level'))
            elif k == 'one_state_dockyard':
                self.dockyards += 1
                if not self.variables.get('skip_payment'): self.variables['treasury'] -= 7.5
            elif k in ('log', 'custom_effect_tooltip', 'add_stability', 'unlock_decision_tooltip', 'unlock_decision_category_tooltip', 'air_experience', 'army_experience', 'add_equipment_to_stockpile', 'force_update_dynamic_modifier'): pass
            elif k.isdigit(): self.scoped_apply(v,int(k))
            elif k in EFFECTS:
                self.effect_stack.append(k)
                try: self.apply(EFFECTS[k])
                finally: self.effect_stack.pop()
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

    def acknowledge(self, event_id, option=0):
        self.apply([n for n in values(EVENTS[event_id],'option')[option] if n[0] not in ('name','ai_chance')])

    def modifier_totals(self):
        totals = {}
        for idea in self.ideas:
            for k,op,v,line in value(IDEAS[idea],'modifier',[]):
                totals[k] = totals.get(k,0)+float(v)
        for name in self.dynamic_modifiers:
            block=DYNAMIC[name]
            if not self.condition(value(block,'enable',[])): continue
            for k,op,v,line in block:
                if k in ('icon','enable','remove_trigger'): continue
                actual=self.variables.get(v,0) if v.startswith('VIE_') else float(v)
                totals[k]=totals.get(k,0)+actual
        return totals


checks = 0
def check(condition, message):
    global checks
    assert condition, message
    checks += 1
    print('PASS ', message)


def prepare_blueprint(state, key):
    ship=SPEC['ship_contracts'][key]
    stem='VIE_nav35_'+key
    state.focuses.add('VIE_nav35_'+ship['focus'])
    state.flags.add(stem+'_offered')
    state.states[519]['rd']=1
    if ship['project']:
        state.flags.add('VIE_nav35_'+ship['project']+'_done')
    elif ship.get('special_project'):
        state.special_projects.add(ship['special_project'].removeprefix('sp:'))
    else:
        state.flags.update({'VIE_nav35_design_done','VIE_nav35_integration_done'})
    state.apply(EFFECTS[stem+'_blueprint_finalize'])


def complete_blue_support(state):
    if 'VIE_nav35_B05' in state.focuses and 'VIE_nav35_blue_support_done' not in state.flags:
        state.apply(EFFECTS['VIE_nav35_blue_support_start'])
        state.clock += 365
        state.apply(EFFECTS['VIE_nav35_blue_support_finish'])


def graph_tests():
    check(len([k for k in FOCUSES if k.startswith('VIE_nav35_')]) == 47, 'exactly 47 V35 focuses')
    for n in SPEC['nodes']:
        block = FOCUSES[n['id']]
        expected = [frozenset({'VIE_nav35_'+n['parent']})] if n['parent'] else []
        if n['code'] == 'N00': expected += [frozenset({'VIE_modernize_vpa'})]
        if n['any']: expected += [frozenset('VIE_nav35_'+d for d in n['any'])]
        if n['all']: expected += [frozenset({'VIE_nav35_'+d}) for d in n['all']]
        actual = [frozenset(values(g,'focus')) for g in values(block,'prerequisite')]
        check(set(actual) == set(expected), n['code']+' AND/OR matches design')
        avail_focuses = {v for k, op, v, line in value(block, 'available', []) if k == 'has_completed_focus'}
        check(avail_focuses == set(), n['code']+' gates in available')
        mutex = set(itertools.chain.from_iterable(values(g,'focus') for g in values(block,'mutually_exclusive')))
        check(mutex == {'VIE_nav35_'+d for d in n['mutex']}, n['code']+' mutex matches design')
        # Free military development (no hard date locks): verify prerequisites open the focus
        s = State(2000)
        s.focuses.update(v for group in values(block, 'prerequisite') for v in values(group, 'focus'))
        s.focuses.update('VIE_nav35_' + d for d in n['all'])
        if n['code']=='B03':s.flags.add('VIE_nav35_blue_support_done')
        check(s.can_focus(n['id']), n['code'] + ' opens with prerequisites satisfied')
    for route, year in [('PG', 2014), ('PB', 2015)]:
        s = State(year)
        s.focuses.add('VIE_modernize_vpa')
        base_excluded = {'I07', 'L03'}
        excluded = base_excluded | ({'B00', 'B01', 'B02', 'B03', 'B04', 'B05'} if route == 'PG' else {'G00', 'G01', 'G02', 'G03', 'G04', 'G05'})
        for n in SPEC['nodes']:
            if route=='PB':complete_blue_support(s)
            if n['code'] not in excluded and s.can_focus(n['id']): s.finish_focus(n['code'])
        check('VIE_nav35_F02' in s.focuses, route + ' reaches F02 by ' + str(year) + ' without I07/L03')
        check('VIE_nav35_I07' not in s.focuses, route + ' does not require 2026 project')
        routeideas = [i for i in s.ideas if i.startswith(('VPA_Integrated', 'VPA_Fleet', 'VPA_Multirole', 'VPA_Greenwater', 'VPA_Bluewater', 'VIE_nav_capstone'))]
        check(len(routeideas) == 1 and routeideas[0].startswith('VIE_nav_capstone'), route + ' final replaces all starter/capstone route ideas')
        before = copy.deepcopy(s.__dict__)
        for _ in range(3): s.apply(EFFECTS['VIE_nav35_refresh'])
        check(s.__dict__ == before, route + ' repeated refresh has zero side effects')
    s = State(2026); s.focuses = {'VIE_nav35_T02'}
    check(not s.can_focus('VIE_nav35_T04'), 'T04 blocks when T03 missing')
    s.focuses = {'VIE_nav35_P06'}
    check(not s.can_focus('VIE_nav35_F01'), 'F01 still requires a Greenwater/Bluewater capstone with P06')
    s.focuses.add('VIE_nav35_G03')
    check(s.can_focus('VIE_nav35_F01'), 'F01 opens with P06 and G03')
    s.focuses = {'VIE_nav35_P06', 'VIE_nav35_B03'}
    check(s.can_focus('VIE_nav35_F01'), 'F01 opens with P06 and B03')
    s.focuses = {'VIE_nav35_G03', 'VIE_nav35_B03'}
    check(not s.can_focus('VIE_nav35_F01'), 'F01 requires P06 even with both route capstones')
    s = State(2000); s.focuses = {'VIE_nav35_F01'}
    check(s.can_focus('VIE_nav35_F02'), 'F02 opens with F01 alone')
    s.focuses.update({'VIE_nav35_S03','VIE_nav35_L04'})
    check(s.can_focus('VIE_nav35_F02'), 'S03 and L04 remain optional for F02')
    s = State(2000); s.focuses = {'VIE_nav35_I05', 'VIE_nav35_I06'}
    check(s.can_focus('VIE_nav35_I07'), 'I07 opens when I05 and I06 satisfied')
    s = State(2026); s.focuses = {'VIE_nav35_I07'}
    check(s.can_focus('VIE_nav35_I08'), 'I08 is an optional direct successor to I07')
    s = State(2026); s.focuses = {'VIE_nav35_F01'}
    check(s.can_focus('VIE_nav35_F02'), 'F02 remains independent of optional I08, S03 and L04')


def project_tests():
    for p in SPEC['projects']:
        key=p['key']; stem='VIE_nav35_'+key; cost=p['cost']
        s=State(2026,cost-0.01)
        s.focuses={'VIE_nav35_'+p['focus']}
        if key in SPEC['ship_contracts']:prepare_blueprint(s,key)
        s.apply(EFFECTS[stem+'_start'])
        check(stem+'_running' not in s.flags and s.variables['treasury']==cost-0.01,key+' cannot spend insufficient treasury')
        s.variables['treasury']=cost
        s.apply(EFFECTS[stem+'_start'])
        check(stem+'_running' in s.flags and abs(s.variables['treasury'])<1e-8,key+' pays once at start')
        before=copy.deepcopy(s.__dict__)
        s.apply(EFFECTS[stem+'_start'])
        check(before==s.__dict__,key+' duplicate start is inert')
        if key in SPEC['ship_contracts'] or key=='blue_support':s.clock+=p['days']
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
    for route, excluded in [('PG',{'B00','B01','B02','B03','B04','B05'}),
                            ('PB',{'G00','G01','G02','G03','G04','G05'})]:
        s=State(2026,100);s.focuses.add('VIE_modernize_vpa')
        for n in SPEC['nodes']:
            if route=='PB':complete_blue_support(s)
            if n['code'] not in excluded and s.can_focus(n['id']):s.finish_focus(n['code'])
        for p in SPEC['projects']:
            if p['focus'] not in excluded:
                if p['key'] in SPEC['ship_contracts']:
                    ship=SPEC['ship_contracts'][p['key']]
                    s.acknowledge('vie_nav35.'+str(ship['offer']))
                    s.apply(EFFECTS['VIE_nav35_'+p['key']+'_blueprint_finalize'])
                s.apply(EFFECTS['VIE_nav35_'+p['key']+'_start'])
                if p['key'] in SPEC['ship_contracts']:s.clock+=p['days']
                s.apply(EFFECTS['VIE_nav35_'+p['key']+'_finish'])
        totals=s.modifier_totals()
        check(totals.get('navy_org',0)<=14,route+' 2026 total naval organization <= 14')
        check(totals.get('navy_org_factor',0)<=.50+1e-9,route+' 2026 organization factor <= 50%, reported separately from organization points')
        check(totals.get('navy_max_range_factor',0)<=.34+1e-9,route+' 2026 total range <= 34% including dynamic modifiers')
        if route=='B':check(abs(totals.get('navy_max_range_factor',0)-.34)<1e-9,'Bluewater complete range budget equals 34%')
        check(totals.get('industrial_capacity_dockyard',0)<=.20+1e-9,route+' 2026 dockyard output <= 20% including naval projects')
        check(s.xp+s.mastery<=450,route+' one-time XP/mastery <= 450')
        names=[r[0] for r in s.research]
        check(len(names)==len(set(names)),route+' research rewards have unique names')
    group=('VPA_Fleet_Development_Priority','VPA_Multirole_Task_Groups','VPA_Greenwater_Doctrine_1','VPA_Greenwater_Doctrine_Capstone','VPA_Bluewater_Doctrine_1','VPA_Bluewater_Doctrine_Capstone','VIE_nav_capstone_master_of_seas','VIE_nav_capstone_ocean_surge')
    for k in group:
        mods=value(IDEAS[k],'modifier')
        actual=float(value(mods,'navy_personnel_cost_multiplier_modifier'))
        expected=.25 if ('Bluewater' in k or 'ocean' in k) else (.10 if ('Greenwater' in k or 'master' in k) else .05)
        check(actual==expected,k+' upkeep matches economic tier')


def route_development_tests():
    def coordinates(fid):
        block=FOCUSES[fid]
        parent=value(block,'relative_position_id')
        px,py=coordinates(parent) if parent else (0,0)
        return px+int(value(block,'x',0)),py+int(value(block,'y',0))
    for node in SPEC['nodes']:
        check(coordinates(node['id'])==(node['x'],node['y']),node['code']+' live coordinates match absolute spec')
    target_positions={'G00':(206,8),'G01':(205,9),'G04':(207,9),'G02':(205,10),'G05':(207,10),'G03':(206,11),
                      'B00':(212,8),'B01':(211,9),'B04':(213,9),'B02':(211,10),'B05':(213,10),'B03':(212,11),
                      'F01':(209,12),'F02':(209,13)}
    for code,expected in target_positions.items():
        check(coordinates('VIE_nav35_'+code)==expected,code+' matches approved V35.4 position')
    check(value(FOCUSES['VIE_nav35_F01'],'relative_position_id')=='VIE_nav35_G03','F01 uses approved direct prerequisite anchor G03')
    surface_types=('corvette','stealth_corvette','frigate','stealth_frigate','heavy_frigate','destroyer','stealth_destroyer','screen_destroyer')
    for typ in surface_types:
        s=State();s.variables['num_ships_with_type@corvette']=0;s.variables['num_ships_with_type@'+typ]=1
        check(not s.condition(TRIGGERS['VIE_nav35_two_surface_ships']),typ+' single hull cannot satisfy two-surface gate')
        s.variables['num_ships_with_type@'+typ]=2
        check(s.condition(TRIGGERS['VIE_nav35_two_surface_ships']),typ+' two hulls satisfy surface gate')
    for a,b in itertools.combinations(surface_types,2):
        s=State();s.variables['num_ships_with_type@corvette']=0
        s.variables['num_ships_with_type@'+a]=s.variables['num_ships_with_type@'+b]=1
        check(s.condition(TRIGGERS['VIE_nav35_two_surface_ships']),'mixed surface pair '+a+'/'+b)
    for route in ('G','B'):
        other='B' if route=='G' else 'G'
        s=State();s.focuses.add('VIE_nav35_H02')
        check(not s.can_focus('VIE_nav35_'+route+'01'),route+' branch waits for its doctrine root')
        s.finish_focus(route+'00')
        check(not s.can_focus('VIE_nav35_'+other+'00'),route+' root locks opposing doctrine root')
        check(s.can_focus('VIE_nav35_'+route+'01') and s.can_focus('VIE_nav35_'+route+'04'),route+' root opens both parallel columns')
        check(('VPA_Greenwater_Doctrine_1' if route=='G' else 'VPA_Bluewater_Doctrine_1') in s.ideas,route+' root applies its starter doctrine profile')
        check(('VPA_Bluewater_Doctrine_1' if route=='G' else 'VPA_Greenwater_Doctrine_1') not in s.ideas,route+' root does not apply opposing doctrine profile')
        for doctrine in (False,True):
            for order in itertools.permutations(('01','02','04','05')):
                if order.index('01')>order.index('02') or order.index('04')>order.index('05'):continue
                s=State();s.doctrine=doctrine;s.focuses.add('VIE_nav35_H02');s.finish_focus(route+'00')
                for suffix in order:
                    code=route+suffix
                    check(s.can_focus('VIE_nav35_'+code),code+' valid column order '+str(order))
                    s.finish_focus(code)
                    before=copy.deepcopy(s.__dict__);s.apply(EFFECTS['VIE_nav_reward_'+code.lower()+'_effect'])
                    check(s.__dict__==before,code+' complete reward cannot repeat')
                if route=='B':complete_blue_support(s)
                check(s.can_focus('VIE_nav35_'+route+'03'),route+' capstone accepts both completed columns')
                s.finish_focus(route+'03')
                check((s.mastery,s.xp)==((40,0) if doctrine else (0,40)),route+' total 40 mastery/XP '+str(order))
                check(s.command_power==75,route+' total 75 CP '+str(order))
                check(len(s.doctrine_discounts)==1 and s.doctrine_discounts[0][1:]==(.35,1),route+' grants one doctrine discount')
                for missing in (route+'02',route+'05'):
                    s.focuses.remove('VIE_nav35_'+missing)
                    check(not s.can_focus('VIE_nav35_'+route+'03'),route+' capstone blocks missing '+missing)
                    s.focuses.add('VIE_nav35_'+missing)
                before=copy.deepcopy(s.__dict__)
                s.apply(EFFECTS['VIE_nav_reward_'+route.lower()+'03_effect']);s.apply(EFFECTS['VIE_nav35_refresh'])
                check(s.__dict__==before,route+' capstone reward and refresh are idempotent')
    for route in ('G','B'):
        s=State();s.focuses.update({'VIE_nav35_'+route+'02','VIE_nav35_'+route+'05'});s.flags.add('VIE_nav35_blue_support_done')
        fid='VIE_nav35_'+route+'03'
        if route=='B':
            s.flags.remove('VIE_nav35_blue_support_done')
            check(not s.can_focus(fid),'Bluewater certification blocks unfinished support investment')
            s.flags.add('VIE_nav35_blue_support_done')
        check(value(FOCUSES[fid],'cancel_if_invalid')=='yes' and value(FOCUSES[fid],'continue_if_invalid')=='no',route+' cancels active certification when readiness is lost')
        for var in ('num_ships_with_type@corvette','num_ships_with_type@attack_submarine'):
            original=s.variables[var];s.variables[var]=0
            check(not s.can_focus(fid),route+' certification blocks missing '+var)
            s.variables[var]=original
        s.base_level=0;check(not s.can_focus(fid),route+' certification blocks missing base');s.base_level=1
        for st in s.states.values():st['controlled']=False
        check(not s.can_focus(fid),route+' certification blocks uncontrolled base')
        for st in s.states.values():st['controlled']=True
        s.variables['num_ships_with_type@corvette']=1
        check(not s.can_focus(fid),route+' certification blocks only one surface ship')
        s.variables['num_ships_with_type@stealth_frigate']=1
        check(s.can_focus(fid),route+' certification accepts two different surface classes')
        s.variables['num_ships_with_type@corvette']=0;s.variables['num_ships_with_type@stealth_frigate']=0
        s.variables['num_ships_with_type@patrol_boat']=2;s.variables['num_ships_with_type@carrier']=1
        check(not s.can_focus(fid),route+' excludes patrol boats and carriers from two-surface requirement')
    s=State();s.finish_focus('B02')
    check(s.events.count('vie_nav35.14')==1,'B02 queues one research choice event')
    for option,category in ((0,'CAT_frigates'),(1,'CAT_aircraft_carriers')):
        t=copy.deepcopy(s);t.acknowledge('vie_nav35.14',option)
        check(t.research==[('VIE_nav35_B02_research',category,.25)],'B02 research choice '+category+' once')
        before=copy.deepcopy(t.__dict__)
        t.acknowledge('vie_nav35.14',1-option);t.acknowledge('vie_nav35.14',option);t.apply(EFFECTS['VIE_nav35_blue_research_offer'])
        check(t.__dict__==before,'B02 replay cannot change or add research choice')
    s.variables['num_ships_with_type@helicopter_operator']=1
    check(s.modifier_totals().get('sortie_efficiency',0)==0,'helicopter operator alone gives no carrier bonus')
    s.variables['num_ships_with_type@carrier']=1
    check(s.modifier_totals().get('sortie_efficiency',0)==0,'carrier without carrier_operations gives no bonus')
    s.doctrines.add('carrier_operations')
    check(s.modifier_totals().get('sortie_efficiency',0)==.06 and s.modifier_totals().get('navy_carrier_air_targetting_factor',0)==.03,'carrier and doctrine enable exact aviation layer')
    s.variables['num_ships_with_type@carrier']=0
    check(s.modifier_totals().get('sortie_efficiency',0)==0,'lost carrier disables aviation layer')
    s.variables['num_ships_with_type@carrier']=1
    before=copy.deepcopy(s.__dict__);s.modifier_totals();s.apply(EFFECTS['VIE_nav35_refresh'])
    check(s.__dict__==before,'restoring carrier cannot replay rewards')
    s.variables['VIE_af_navy_max_range_factor']=.05
    check(s.modifier_totals()['navy_max_range_factor']==.05,'balance includes variable-backed dynamic modifiers')


def blue_support_tests():
    for field in ('base_level','yard_level'):
        s=State(money=8);s.focuses.add('VIE_nav35_B05');setattr(s,field,0)
        s.apply(EFFECTS['VIE_nav35_blue_support_start'])
        check(s.variables['treasury']==8 and not s.flags,'support does not pay without '+field)
    s=State(money=7.99);s.focuses.add('VIE_nav35_B05');s.apply(EFFECTS['VIE_nav35_blue_support_start'])
    check(s.variables['treasury']==7.99 and not s.flags,'support blocks treasury 7.99')
    s.variables['treasury']=8;s.apply(EFFECTS['VIE_nav35_blue_support_start'])
    check(s.variables['treasury']==0,'support signs at exactly 8bn')
    started=s.flag_dates['VIE_nav35_blue_support_running']
    s.clock=364;s.apply(EFFECTS['VIE_nav35_blue_support_finish'])
    check('VIE_nav35_blue_support_done' not in s.flags and 'VIE_nav35_blue_support_idea' not in s.ideas,'support has no operating reward on day 364')
    s.clock=365;s.base_level=0;s.apply(EFFECTS['VIE_nav35_blue_support_finish'])
    check('VIE_nav35_blue_support_ready' in s.flags and 'VIE_nav35_blue_support_done' not in s.flags,'support waits for base at maturity')
    s.variables['treasury']=20;before=copy.deepcopy(s.__dict__)
    s.apply(EFFECTS['VIE_nav35_blue_support_start']);s.apply(EFFECTS['VIE_nav35_blue_support_finish'])
    check(s.__dict__==before,'pending support cannot repay or restart clock')
    s.base_level=1;s.yard_level=0;s.apply(EFFECTS['VIE_nav35_blue_support_finish'])
    check('VIE_nav35_blue_support_done' not in s.flags,'pending support still requires shipyard')
    restored=copy.deepcopy(s);restored.yard_level=1;restored.apply(EFFECTS['VIE_nav35_scheduler'])
    check('VIE_nav35_blue_support_done' in restored.flags and restored.variables['treasury']==20,'saved pending support recovers with no additional payment')
    before=copy.deepcopy(restored.__dict__);restored.apply(EFFECTS['VIE_nav35_blue_support_finish']);restored.apply(EFFECTS['VIE_nav35_scheduler'])
    check(restored.__dict__==before,'support repeated scheduler cannot duplicate operating reward')
    check(restored.modifier_totals().get('navy_max_range_factor',0)==.05,'support only grants 5% range')
    normal=State(money=8);normal.focuses.add('VIE_nav35_B05');normal.apply(EFFECTS['VIE_nav35_blue_support_start']);normal.clock=365
    normal.apply(EFFECTS['VIE_nav35_blue_support_finish'])
    check('VIE_nav35_blue_support_done' in normal.flags,'support with intact sites operates exactly on day 365')
    unowned=State(money=8);unowned.focuses.add('VIE_nav35_B05')
    for st in unowned.states.values():st['owned']=False
    unowned.apply(EFFECTS['VIE_nav35_blue_support_start'])
    check(unowned.variables['treasury']==8 and not unowned.flags,'support cannot pay without owned coastal sites')
    s=State();s.focuses.add('VIE_nav35_B02');check(not s.condition(TRIGGERS['VIE_nav35_blue_support_can_start']),'B02 no longer opens support investment')


def industry_tests():
    for target in (519,522,521):
        s=State(money=8)
        for sid in s.states:s.states[sid]['rd_capacity']=sid==target
        check(s.can_focus('VIE_nav35_I01') is False,'I01 still requires its parent')
        s.focuses.add('VIE_nav35_N00')
        check(s.can_focus('VIE_nav35_I01'),'I01 accepts 8bn and R&D site '+str(target))
        s.finish_focus('I01')
        check(s.variables['treasury']==0 and s.states[target]['rd']==1,'R&D builds once at eligible state '+str(target)+' for 8bn')
        before=copy.deepcopy(s.__dict__);s.apply(EFFECTS['VIE_nav35_rd_apply'])
        check(before==s.__dict__,'R&D cannot repeat '+str(target))
    s=State(money=8);s.finish_focus('I01')
    check(s.states[519]['rd']==1 and s.states[522]['rd']==0,'R&D uses Southern Vietnam first')
    s=State(money=8);s.states[519]['rd_capacity']=False;s.finish_focus('I01')
    check(s.states[522]['rd']==1,'R&D falls back to Red River Delta before Central Vietnam')
    for failure in ('money','site'):
        s=State(money=8);s.focuses.add('VIE_nav35_N00')
        check(s.can_focus('VIE_nav35_I01'),'I01 initially available before '+failure+' loss')
        if failure=='money':s.variables['treasury']=7.99
        else:
            for st in s.states.values():st['rd_capacity']=False
        before=s.variables['treasury'];s.finish_focus('I01')
        check(s.variables['treasury']==before and not any(st['rd'] for st in s.states.values()) and 'VIE_nav35_rd_pending' in s.flags,'lost '+failure+' defers R&D without charge')
        s.variables['treasury']=8;s.states[519]['rd_capacity']=True;s.apply(EFFECTS['VIE_nav35_rd_apply'])
        check(s.variables['treasury']==0 and 'VIE_nav35_rd_done' in s.flags and 'VIE_nav35_rd_pending' not in s.flags,'restored '+failure+' can settle pending R&D once')
    s=State(money=7.99);s.focuses.add('VIE_nav35_N00')
    check(not s.can_focus('VIE_nav35_I01'),'I01 blocks starting below 8bn')
    s=State(money=20)
    for c in ('I01','I02','I03','I05'):s.finish_focus(c)
    check(s.dockyards==4 and s.variables['treasury']==12,'four subsidized dockyards are free; only R&D charges 8bn')
    check([s.states[sid]['slot_grants'] for sid in (519,522,521)]==[2,1,1],'Ba Son gets two slots, Hong Ha and Song Thu one each')
    before=copy.deepcopy(s.__dict__);s.apply(EFFECTS['VIE_nav35_subsidies_refresh'])
    check(before==s.__dict__,'subsidized yards/slots cannot repeat')
    for key,definition in SPEC['industry_additions']['subsidies'].items():
        sid=definition['state'];stem='VIE_nav35_'+key+'_subsidy'
        for loss in ('owned','controlled'):
            s=State();s.states[sid][loss]=False;s.finish_focus(definition['focus'])
            check(stem+'_pending' in s.flags and stem+'_done' not in s.flags,key+' subsidy waits for '+loss)
            s.states[sid][loss]=True;s.apply(EFFECTS[stem+'_apply'])
            check(stem+'_done' in s.flags and stem+'_pending' not in s.flags,key+' subsidy recovers '+loss+' at original location')
    s=State();s.states[522].update(slots=0,slot_growth=False);s.finish_focus('I03')
    check('VIE_nav35_i03_subsidy_pending' in s.flags and s.dockyards==0,'state cap defers Hong Ha dockyard')
    s.apply(EFFECTS['VIE_nav35_subsidies_refresh']);s.apply(EFFECTS['VIE_nav35_subsidies_refresh'])
    check(s.states[522]['slot_grants']==1,'blocked dockyard cannot repeat slot grants')
    s.states[522]['slots']=1;s.apply(EFFECTS['VIE_nav35_subsidies_refresh'])
    check(s.dockyards==1 and s.states[522]['slot_grants']==1,'released slot completes original subsidy once')
    s=State();s.states[521]['base']=10;s.finish_focus('I07')
    check(s.states[521]['base']==10 and 'VIE_nav35_i07_subsidy_pending' in s.flags,'Da Nang naval base respects province cap')
    s.states[521]['base']=9;s.apply(EFFECTS['VIE_nav35_subsidies_refresh'])
    check(s.states[521]['base']==10 and 'VIE_nav35_i07_subsidy_done' in s.flags,'Da Nang subsidy uses state 521 province 10309 once')


def frigate_tests():
    # All first-ship contracts run through the same guarded lifecycle.
    for key,ship in SPEC['ship_contracts'].items():
        stem='VIE_nav35_'+key;s=State(money=10)
        if ship['project']:
            s.focuses.add('VIE_nav35_'+ship['focus'])
            project='VIE_nav35_'+ship['project']
            s.apply(EFFECTS[project+'_start']);s.clock+=ship['days']
            s.apply(EFFECTS[project+'_finish'])
        else:s.finish_focus(ship['focus'])
        event='vie_nav35.'+str(ship['offer'])
        check(s.events.count(event)==1 and stem+'_offered' not in s.flags,key+' queues approval before contract opens')
        check(not s.condition(TRIGGERS[stem+'_can_start']),key+' cannot sign before approval/blueprint')
        s.acknowledge(event)
        check(stem+'_offered' in s.flags,key+' approval opens blueprint/contract without ship')
        if ship.get('special_project'):
            missing=copy.deepcopy(s);missing.states[519]['rd']=1
            check(not missing.condition(TRIGGERS[stem+'_blueprint_can_finalize']),key+' blueprint decision stays locked before Special Project completion')
        dependencies=(['VIE_nav35_'+ship['project']+'_done'] if ship['project'] else
                      [] if ship.get('special_project') else ['VIE_nav35_design_done','VIE_nav35_integration_done'])
        s.flags.update(dependencies)
        before=copy.deepcopy(s.__dict__);s.apply(EFFECTS[stem+'_blueprint_finalize'])
        check(before==s.__dict__,key+' blueprint blocks missing controlled R&D')
        s.states[519]['rd']=1
        if ship.get('special_project'):
            s.special_projects.add(ship['special_project'].removeprefix('sp:'))
            missing=copy.deepcopy(s);missing.special_projects.remove(ship['special_project'].removeprefix('sp:'));missing.apply(EFFECTS[stem+'_blueprint_finalize'])
            check(not missing.variants,key+' blueprint requires completed '+ship['special_project'])
            missing=copy.deepcopy(s);missing.technologies.remove(ship['hull']);missing.apply(EFFECTS[stem+'_blueprint_finalize'])
            check(not missing.variants,key+' blueprint requires unlocked stealth hull tech')
        for dependency in dependencies:
            missing=copy.deepcopy(s);missing.flags.remove(dependency);missing.apply(EFFECTS[stem+'_blueprint_finalize'])
            check(not missing.variants,key+' blueprint requires '+dependency)
        for tech in ship['technologies']:
            missing=copy.deepcopy(s);missing.technologies.remove(tech);missing.apply(EFFECTS[stem+'_blueprint_finalize'])
            check(not missing.variants,key+' blueprint blocks missing '+tech)
        money=s.variables['treasury'];s.apply(EFFECTS[stem+'_blueprint_finalize'])
        check(s.variant_creations==1 and not s.ships and s.variables['treasury']==money,key+' finalizes one usable variant before signing for no additional charge')
        check(s.variants[ship['name']]==(ship['hull'],ship['modules']),key+' blueprint matches frozen module configuration')
        before=copy.deepcopy(s.__dict__);s.apply(EFFECTS[stem+'_blueprint_finalize']);s.acknowledge(event);s.apply(EFFECTS[stem+'_offer'])
        check(before==s.__dict__,key+' blueprint and approval replays are inert')
        for field in ('base_level','yard_level'):
            missing=copy.deepcopy(s);setattr(missing,field,0);missing.apply(EFFECTS[stem+'_start'])
            check(stem+'_running' not in missing.flags and missing.variables['treasury']==money,key+' signing requires '+field)
        for tech in ship['technologies']:
            missing=copy.deepcopy(s);missing.technologies.remove(tech);missing.apply(EFFECTS[stem+'_start'])
            check(stem+'_running' not in missing.flags and missing.variables['treasury']==money,key+' signing requires '+tech)
        if ship.get('special_project'):
            missing=copy.deepcopy(s);missing.special_projects.remove(ship['special_project'].removeprefix('sp:'));missing.apply(EFFECTS[stem+'_start'])
            check(stem+'_running' not in missing.flags and missing.variables['treasury']==money,key+' signing requires completed '+ship['special_project'])
        s.apply(EFFECTS[stem+'_start']);paid=money-ship['cost'];start=s.flag_dates[stem+'_running']
        check(abs(s.variables['treasury']-paid)<1e-8 and not s.ships,key+' signing pays the specified price once')
        before=copy.deepcopy(s.__dict__);s.apply(EFFECTS[stem+'_start'])
        check(before==s.__dict__,key+' signing again cannot extend timer or charge')
        s.clock=start+ship['days']-1;s.apply(EFFECTS[stem+'_finish'])
        check(not s.ships and stem+'_running' in s.flags,key+' cannot deliver one day before maturity')
        mature=copy.deepcopy(s);mature.clock+=1;mature.apply(EFFECTS[stem+'_finish'])
        check(mature.ships==[(ship['hull'],ship['name'])] and mature.variant_creations==1,key+' saved running state delivers one ship at maturity without creating blueprint again')
        before=copy.deepcopy(mature.__dict__)
        for _ in range(3):
            mature.apply(EFFECTS[stem+'_finish']);mature.apply(EFFECTS[stem+'_deliver']);mature.apply(EFFECTS[stem+'_start']);mature.acknowledge('vie_nav35.'+str(ship['delivery']))
        check(before==mature.__dict__,key+' repeated finish/delivery/event cannot grant another ship or charge')
        for field in ('base_level','yard_level'):
            pending=copy.deepcopy(s);setattr(pending,field,0);pending.clock+=1;pending.apply(EFFECTS[stem+'_finish'])
            check(not pending.ships and stem+'_ready' in pending.flags and stem+'_running' not in pending.flags,key+' lost '+field+' waits after maturity')
            pending.apply(EFFECTS['VIE_nav35_scheduler'])
            check(not pending.ships and abs(pending.variables['treasury']-paid)<1e-8,key+' monthly retry with lost '+field+' has no charge/ship')
            setattr(pending,field,1);pending.apply(EFFECTS['VIE_nav35_scheduler'])
            check(len(pending.ships)==1 and pending.variant_creations==1,key+' restores '+field+' and delivers once')
        pending=copy.deepcopy(s);pending.clock+=1;pending.technologies.remove(ship['hull']);pending.apply(EFFECTS[stem+'_finish'])
        check(not pending.ships and stem+'_ready' in pending.flags,key+' missing hull at delivery stays pending')
        pending.technologies.add(ship['hull']);pending.apply(EFFECTS['VIE_nav35_scheduler'])
        check(len(pending.ships)==1,key+' delivery recovers technology without charging')
        if ship.get('special_project'):
            pending=copy.deepcopy(s);pending.clock+=1;pending.special_projects.remove(ship['special_project'].removeprefix('sp:'));pending.apply(EFFECTS[stem+'_finish'])
            check(not pending.ships and stem+'_ready' in pending.flags,key+' missing Special Project at maturity waits')
            pending.apply(EFFECTS['VIE_nav35_scheduler'])
            check(not pending.ships and pending.variables['treasury']==paid,key+' scheduler does not deliver or charge without Special Project')
            pending.special_projects.add(ship['special_project'].removeprefix('sp:'));pending.apply(EFFECTS['VIE_nav35_scheduler'])
            check(len(pending.ships)==1,key+' restoring Special Project enables one delayed delivery')
        recovered=copy.deepcopy(s);recovered.clock=start+ship['days']+5;recovered.apply(EFFECTS['VIE_nav35_scheduler'])
        check(len(recovered.ships)==1,key+' monthly scheduler recovers missed callback')
        bad=State();bad.acknowledge(event)
        check(stem+'_offered' not in bad.flags,key+' manual approval without prerequisites cannot unlock')
    for first,second in itertools.permutations(SPEC['ship_contracts'],2):
        s=State()
        prepare_blueprint(s,first);prepare_blueprint(s,second)
        s.apply(EFFECTS['VIE_nav35_'+first+'_start']);money=s.variables['treasury']
        s.apply(EFFECTS['VIE_nav35_'+second+'_start'])
        check('VIE_nav35_'+second+'_running' not in s.flags and s.variables['treasury']==money,first+' prevents overlapping '+second)
    tt=SPEC['ship_contracts']['tt400_ship']
    check(tt['hull']=='corvette_hull_2' and not any('missile' in module for module in tt['modules'].values()),'TT400 uses corvette hull with no missile modules')
    check('has_doctrine' not in str(TRIGGERS['VIE_nav35_tt400_ship_blueprint_can_finalize']) and 'patrol_boat' not in str(TRIGGERS['VIE_nav35_tt400_ship_technology_ready']),'TT400 does not impose Jeune Ecole/patrol-hull gate')


def industry_provider_tests(md):
    md=Path(md)
    equipment=value(load(md/'common/units/equipment/MD_mtg_ships.txt'),'equipments')
    modules=value(load(md/'common/units/equipment/modules/MD_ship_modules.txt'),'equipment_modules')
    technologies={}
    for path in (md/'common/technologies').glob('*.txt'):
        for key,op,block,line in value(load(path),'technologies',[]):technologies[key]=block
    categories={k for tech in technologies.values() if isinstance(tech,list) for group in values(tech,'categories') for k,_,_,_ in group}
    for category in ('CAT_naval_sonar','CAT_attack_submarines','CAT_frigates','CAT_aircraft_carriers'):
        check(category in categories,'V35.4 research category provider '+category)
    subdoctrines=load(md/'common/doctrines/subdoctrines/sea/naval.txt')
    check(value(subdoctrines,'carrier_operations') is not None,'V35.4 carrier_operations exists')
    units=value(load(md/'common/units/MD_naval_units.txt'),'sub_units')
    for unit in ('corvette','stealth_corvette','frigate','stealth_frigate','heavy_frigate','destroyer','stealth_destroyer','screen_destroyer','attack_submarine','carrier'):
        check(value(units,unit) is not None,'V35.4 fleet unit provider '+unit)
    sprites='\n'.join(p.read_text(encoding='utf-8-sig') for p in (md/'interface').glob('*.gfx'))
    check('GFX_idea_navy_strengthened' in sprites,'V35.4 dynamic modifier icon provider')
    event_picture=value(EVENTS['vie_nav35.14'],'picture')
    blocks=re.findall(r'spriteType\s*=\s*\{([^}]+)\}',sprites)
    picture_block=next((b for b in blocks if re.search(r'name\s*=\s*"'+re.escape(event_picture)+r'"',b)),None)
    check(picture_block is not None,'V35.4 research event picture provider')
    texture=re.search(r'texturefile\s*=\s*"([^"]+)"',picture_block)
    check(texture is not None and (md/texture[1]).is_file(),'V35.4 research event picture texture exists')
    for key,ship in SPEC['ship_contracts'].items():
        archetype=value(value(equipment,ship['hull']),'archetype')
        check(archetype in ('corvette','frigate','stealth_frigate'),key+' hull provider exists')
        slots=value(value(equipment,archetype),'module_slots');unlocked=set();counts={}
        for tech in ship['technologies']:
            check(tech in technologies,key+' tech provider '+tech)
            for group in values(technologies[tech],'enable_equipment_modules'):unlocked.update(k for k,_,_,_ in group)
        for slot,module in ship['modules'].items():
            slotdef=value(slots,slot);check(slotdef is not None,key+' slot provider '+slot)
            if module=='empty':
                check(value(slotdef,'required','no')!='yes',key+' required slot is populated '+slot)
                continue
            mod=value(modules,module);check(mod is not None and module in unlocked,key+' module unlocked by required technologies '+module)
            category=value(mod,'category');allowed={k for k,_,_,_ in value(slotdef,'allowed_module_categories')}
            check(category in allowed or slot=='fixed_ship_missile_ammo_slot' and not allowed,key+' compatible slot '+slot)
            counts[category]=counts.get(category,0)+1
        for limit in values(value(equipment,archetype),'module_count_limit'):
            check(counts.get(value(limit,'category'),0)<int(value(limit,'count')),key+' module count cap '+value(limit,'category'))
    buildings=value(load(md/'common/buildings/00_buildings.txt'),'buildings')
    check(value(buildings,'naval_facility') is not None,'naval_facility is a real MD building')
    naval_projects=load(md/'common/special_projects/projects/naval_projects.txt')
    stealth_project=value(naval_projects,'sp_stealth_frigate')
    check(stealth_project is not None,'MD stealth frigate special project exists')
    check(any(k=='has_tech' and v=='frigate_hull_4' for k,_,v,_ in value(value(stealth_project,'available'),'FROM')),'MD special project requires frigate_hull_4')
    project_effects=value(value(stealth_project,'project_output'),'country_effects')
    project_techs=value(project_effects,'set_technology')
    check(any(k=='stealth_frigate_hull_1' for k,_,_,_ in project_techs),'MD special project unlocks stealth_frigate_hull_1')
    for sid in (519,522,521):
        path=next((md/'history/states').glob(str(sid)+'-*.txt'))
        state=value(load(path),'state');check(value(value(state,'history'),'owner')=='VIE','R&D/subsidy state belongs to VIE '+str(sid))
    central=value(load(next((md/'history/states').glob('521-*.txt'))),'state')
    check(any(k=='10309' for k,_,_,_ in value(value(central,'history'),'buildings')),'Da Nang province 10309 belongs to state 521 and has a base')


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
    if args.game and not args.md:parser.error('--game requires --md')
    graph_tests();project_tests();timing_tests();route_development_tests();blue_support_tests();industry_tests();frigate_tests()
    if args.md:industry_provider_tests(args.md)
    if args.md and args.game:provider_tests(args.md,args.game)
    print(f'ALL PASS: {checks} static scenarios. In-game runtime NOT RUN.')
