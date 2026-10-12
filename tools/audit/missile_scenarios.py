"""Kiem gate/giao dich V5 tu script live; fixture khong thay engine HOI4.

python tools/audit/missile_scenarios.py --md <MD root> [--baseline <snapshot>]
Statement khong ho tro phai fail, khong mac dinh coi la dung.
"""
from __future__ import annotations

import argparse
import ast
import copy
import functools
import hashlib
import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = json.loads(Path(__file__).with_name('missile_v5_spec.json').read_text(encoding='utf-8'))
source = ast.parse((ROOT / 'tools/audit/audit.py').read_text(encoding='utf-8'))
ns = {}
exec(compile(ast.Module(body=[n for n in source.body if isinstance(n, ast.FunctionDef)
                             and n.name in ('tokenize', 'parse')], type_ignores=[]), 'audit_parser', 'exec'), ns)


def load(path):
    text = Path(path).read_text(encoding='utf-8-sig')
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
    return ns['parse'](ns['tokenize']('\n'.join(clean)))


def values(block, key):
    return [v for k, op, v, line in block if k == key]


def value(block, key, default=None):
    return next(iter(values(block, key)), default)


def normalize(block):
    return [(k, op, normalize(v) if isinstance(v, list) else v) for k, op, v, line in block]


def walk(block):
    for k, op, v, line in block:
        yield k, op, v, line
        if isinstance(v, list):
            yield from walk(v)


FOCUSES = {value(b, 'id'): b for b in values(value(load(ROOT/'common/national_focus/VIE_md_focus.txt'), 'focus_tree'), 'focus')}
EFFECTS = {k: v for k, op, v, line in load(ROOT/'common/scripted_effects/VIE_md_effects_missile.txt')}
TRIGGERS = {k: v for k, op, v, line in load(ROOT/'common/scripted_triggers/VIE_md_triggers_missile.txt')}
IDEAS = {k: v for k, op, v, line in value(value(load(ROOT/'common/ideas/VIE_md_missile_ideas.txt'), 'ideas'), 'country')}
DECISIONS = {k: v for k, op, v, line in value(load(ROOT/'common/decisions/VIE_md_missile_decisions.txt'), 'VIE_msl_program_category')}
CATEGORY = value(load(ROOT/'common/decisions/categories/VIE_md_missile_categories.txt'), 'VIE_msl_program_category')
EVENTS = {value(b, 'id'): b for b in values(load(ROOT/'events/VIE_md_missile_events.txt'), 'country_event')}
NODES = {n['code']: n for n in SPEC['nodes']}
COUNT = 0


def check(condition, label):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(label)


@functools.lru_cache(None)
def position(fid):
    b = FOCUSES[fid]
    parent = value(b, 'relative_position_id')
    x, y = position(parent) if parent else (0, 0)
    return x+int(value(b, 'x', 0)), y+int(value(b, 'y', 0))


class State:
    """Mo phong statement can cho V5; timer/cooldown la model, khong la engine."""
    def __init__(self, money=50, pp=1000):
        self.money, self.pp, self.day = money, pp, 0
        self.tag = 'VIE'
        self.focuses, self.flags, self.ideas, self.doctrines = set(), set(), set(), set()
        self.timed, self.active, self.cooldowns = {}, {}, {}
        self.xp = {'land': 0, 'naval': 0}
        self.mastery = {'land': 0, 'naval': 0}
        self.research, self.temp = [], {}
        self.debug, self.bankruptcy, self.historical = False, False, False
        self.year = 2000

    def condition(self, block):
        results = []
        for k, op, v, line in block:
            if k in ('tooltip', 'factor', 'base'):
                continue
            if k in ('AND', 'custom_trigger_tooltip'):
                result = self.condition(v)
            elif k == 'NOT':
                result = not self.condition(v)
            elif k == 'OR':
                result = any(self.condition([item]) for item in v)
            elif k in TRIGGERS:
                result = self.condition(TRIGGERS[k]) == (v == 'yes')
            elif k == 'always':
                result = v == 'yes'
            elif k == 'original_tag':
                result = self.tag == v
            elif k == 'has_completed_focus':
                result = v in self.focuses
            elif k == 'has_country_flag':
                result = v in self.flags
            elif k == 'has_idea':
                result = v in self.ideas
            elif k == 'has_active_mission':
                if v != 'bankruptcy_incoming_collapse':
                    raise ValueError(k+': '+str(v))
                result = self.bankruptcy
            elif k == 'check_variable':
                if value(v, 'var') != 'treasury' or value(v, 'compare') != 'greater_than_or_equals':
                    raise ValueError('Unsupported variable comparison: '+str(v))
                result = self.money >= float(value(v, 'value'))
            elif k == 'has_selected_land_grand_doctrine':
                result = ('land' in self.doctrines) == (v == 'yes')
            elif k == 'has_selected_naval_grand_doctrine':
                result = ('naval' in self.doctrines) == (v == 'yes')
            elif k == 'VIE_ai_historical_path':
                result = self.historical == (v == 'yes')
            elif k == 'is_debug':
                result = self.debug == (v == 'yes')
            elif k == 'date' and op == '<':
                result = self.year < int(v.split('.')[0])
            else:
                raise ValueError('Unsupported trigger '+k+' at '+str(line))
            results.append(result)
        return all(results)

    def execute(self, block):
        branch = None
        for k, op, v, line in block:
            if k in ('log', 'limit', 'custom_effect_tooltip', 'unlock_decision_tooltip'):
                continue
            if k == 'if':
                branch = self.condition(value(v, 'limit'))
                if branch:
                    self.execute(v)
            elif k == 'else':
                if branch is None:
                    raise ValueError('else without if')
                if not branch:
                    self.execute(v)
                branch = None
            elif k == 'hidden_effect':
                self.execute(v)
            elif k in EFFECTS:
                if v != 'yes':
                    raise ValueError('Unsupported effect argument')
                self.execute(EFFECTS[k])
            elif k == 'set_country_flag':
                self.flags.add(v)
            elif k == 'clr_country_flag':
                self.flags.discard(v)
            elif k == 'set_temp_variable':
                self.temp.update({a: float(b) for a, _, b, _ in v})
            elif k == 'modify_treasury_effect':
                if 'MD_skip_treasury_cost' not in self.flags:
                    self.money += self.temp['treasury_change']
            elif k == 'add_tech_bonus':
                self.research.append(dict(category=value(v, 'category'), bonus=float(value(v, 'bonus')), uses=int(value(v, 'uses'))))
            elif k == 'army_experience':
                self.xp['land'] += float(v)
            elif k == 'navy_experience':
                self.xp['naval'] += float(v)
            elif k == 'add_mastery':
                self.mastery[value(v, 'folder')] += float(value(v, 'amount'))
            elif k == 'add_political_power':
                self.pp += float(v)
            elif k == 'add_ideas':
                self.ideas.add(v)
            elif k == 'remove_ideas':
                self.ideas.discard(v)
            elif k == 'add_timed_idea':
                iid = value(v, 'idea')
                self.ideas.add(iid)
                self.timed[iid] = self.day+int(value(v, 'days'))
            elif k == 'country_event':
                if value(v, 'days') is not None:
                    raise ValueError('V5 callback must be immediate')
                self.execute(value(EVENTS[value(v, 'id')], 'immediate'))
            else:
                raise ValueError('Unsupported effect '+k+' at '+str(line))

    def focus_ready(self, fid):
        b = FOCUSES[fid]
        return all(any(p in self.focuses for p in values(g, 'focus')) for g in values(b, 'prerequisite')) and self.condition(value(b, 'available', []))

    def complete_focus(self, fid):
        if fid in self.focuses or not self.focus_ready(fid):
            return False
        # Reward chay truoc completed, de kiem spirit refresh khong phu thuoc flag engine.
        self.execute(value(FOCUSES[fid], 'completion_reward'))
        self.focuses.add(fid)
        return True

    def decision_ready(self, did):
        b = DECISIONS[did]
        return (self.condition(value(CATEGORY, 'allowed')) and self.condition(value(CATEGORY, 'visible'))
                and self.condition(value(b, 'visible', [])) and self.condition(value(b, 'available', []))
                and self.pp >= float(value(b, 'cost', 0)) and did not in self.active
                and self.day >= self.cooldowns.get(did, 0))

    def select(self, did):
        if not self.decision_ready(did):
            return False
        b = DECISIONS[did]
        self.pp -= float(value(b, 'cost', 0))
        self.execute(value(b, 'complete_effect'))
        if value(b, 'days_remove'):
            self.active[did] = self.day+int(value(b, 'days_remove'))
        if value(b, 'days_re_enable'):
            self.cooldowns[did] = self.day+int(value(b, 'days_re_enable'))
        return True

    def advance(self, days):
        target = self.day+days
        for did, date in sorted(list(self.active.items()), key=lambda p: p[1]):
            if date <= target:
                self.day = date
                del self.active[did]
                self.execute(value(DECISIONS[did], 'remove_effect'))
        self.day = target
        for iid, date in list(self.timed.items()):
            if date <= self.day:
                self.ideas.discard(iid)
                del self.timed[iid]

    def weight(self, block):
        result = float(value(block, 'base', 0))
        for modifier in values(block, 'modifier'):
            if self.condition(modifier):
                result *= float(value(modifier, 'factor', 1))
        return result


def node_tests():
    check(len(NODES) == 10, '10 nodes')
    actual = {fid for fid in FOCUSES if fid.startswith('VIE_msl_')}
    check(actual == {n['id'] for n in NODES.values()}, 'exact missile focus set')
    check(sum(len(values(FOCUSES[n['id']], 'prerequisite')) for n in NODES.values()) == 15, '15 AND edges')
    check({position(NODES[c]['id'])[1] for c in ('M01','M02','M03','M05','M06','M07')} == {3}, 'six programs same row')
    for n in NODES.values():
        b = FOCUSES[n['id']]
        check(position(n['id']) == tuple(n['absolute']), n['code']+' position')
        check(value(b, 'relative_position_id') == n['anchor'], n['code']+' anchor')
        check([[p] for p in n['all']] == [values(g, 'focus') for g in values(b, 'prerequisite')], n['code']+' AND groups')
        check(n['anchor'] in n['all'], n['code']+' direct anchor')
        check(int(value(b, 'cost')) == n['cost'], n['code']+' cost')
        check(value(b, 'icon') == n['icon'], n['code']+' icon')
        check(values(b, 'bypass') == [] and values(b, 'mutually_exclusive') == [], 'no bypass/mutex')
        for fid in FOCUSES:
            if fid != n['id'] and position(fid)[1] == n['absolute'][1]:
                check(abs(position(fid)[0]-n['absolute'][0]) >= 2, 'same-row gap '+n['code']+' '+fid)
    for code in ('M04','M08','M09'):
        n = NODES[code]
        for subset in itertools.product((False, True), repeat=len(n['all'])):
            for certified in (False, True):
                s = State()
                s.focuses = {f for f, present in zip(n['all'], subset) if present}
                if certified:
                    s.flags.add('VIE_msl_vcs_certified')
                check(s.focus_ready(n['id']) == (all(subset) and (code != 'M08' or certified)), 'missing gate '+code)
    s = State();s.focuses.add(NODES['M00']['id'])
    for code in ('M01','M02','M03','M05','M06','M07'):
        check(s.focus_ready(NODES[code]['id']), 'parallel '+code)


def reward_tests():
    expected_bonuses = [('CAT_missiles', .1), ('CAT_missiles', .25), ('CAT_missiles', .15), ('CAT_military_electronics', .2)]
    for land, naval in itertools.product((False, True), repeat=2):
        s = State()
        if land:s.doctrines.add('land')
        if naval:s.doctrines.add('naval')
        for n in NODES.values():
            old = s.money
            s.execute(value(FOCUSES[n['id']], 'completion_reward'))
            check(abs(old-s.money-n['treasury_cost']) < 1e-8, n['code']+' price')
            saved = copy.deepcopy(s.__dict__)
            s.execute(value(FOCUSES[n['id']], 'completion_reward'))
            check(s.__dict__ == saved, n['code']+' idempotent reward')
        check(abs(s.money-40.5) < 1e-8 and s.pp == 1020, 'focus total 9.5 and PP20')
        check(s.xp == {'land': 0 if land else 5, 'naval': 0 if naval else 10}, 'XP routing')
        check(s.mastery == {'land': 5 if land else 0, 'naval': 10 if naval else 0}, 'mastery routing')
        check([(r['category'], r['bonus']) for r in s.research] == expected_bonuses and all(r['uses']==1 for r in s.research), 'research categories/uses')
        check(s.ideas == {'VIE_msl_integrated_idea'}, 'integrated spirit exclusive')
        s.flags.discard('VIE_msl_m04_reward_applied')
        s.execute(EFFECTS['VIE_msl_m04_reward'])
        check(s.ideas == {'VIE_msl_integrated_idea'}, 'late sustainment does not stack')
    s=State();s.flags.add('MD_skip_treasury_cost')
    for n in NODES.values():s.execute(value(FOCUSES[n['id']], 'completion_reward'))
    check(s.money==50, 'MD skip-cost respected')
    s=State();s.tag='CHI'
    for n in NODES.values():s.execute(value(FOCUSES[n['id']], 'completion_reward'))
    check(s.money==50 and not s.flags and not s.ideas and not s.research, 'foreign reward guard')
    for order in itertools.permutations(('m04','m08','m09')):
        s=State()
        for code in order:s.execute(EFFECTS['VIE_msl_'+code+'_reward'])
        check(s.ideas == {'VIE_msl_integrated_idea'}, 'spirit order '+str(order))
        s.execute(EFFECTS['VIE_msl_refresh_spirits'])
        check(s.ideas == {'VIE_msl_integrated_idea'}, 'refresh idempotent')
    for iid, mods in SPEC['ideas'].items():
        check({k:float(v) for k,op,v,line in value(IDEAS[iid], 'modifier')} == mods, 'idea modifiers '+iid)


def decision_tests():
    check(len(DECISIONS)==8 and len(EVENTS)==3 and len(IDEAS)==6, 'decision/event/idea counts')
    for d in SPEC['decisions']:
        b=DECISIONS[d['id']]
        check(int(value(b, 'cost'))==d['pp'], 'decision PP '+d['id'])
        check(value(b, 'fire_only_once') is None, 'no fire_once/timer mixture')
        if d['kind']=='integration_stub':
            for debug in (False,True):
                s=State();s.debug=debug;s.flags.update(('VIE_msl_program_started','VIE_msl_vcs_certified'));s.focuses.add(NODES['M08']['id'])
                check(s.condition(value(b,'visible'))==debug, 'debug-only stub')
                before=copy.deepcopy(s.__dict__)
                check(not s.select(d['id']) and s.__dict__==before, 'stub no charge')
                s.execute(value(b,'complete_effect'))
                check(s.__dict__==before, 'stub direct call no-op')
            continue
        check(int(value(b, 'days_remove' if d['kind']=='program' else 'days_re_enable'))==d.get('duration',365), 'timer/cooldown')
        for wrong_scope, missing_focus, missing_category in ((True,False,False),(False,True,False),(False,False,True)):
            s=State();s.flags.add('VIE_msl_program_started');s.focuses.add(d['focus'])
            if d.get('previous'):s.flags.add(d['previous'])
            if wrong_scope:s.tag='CHI'
            if missing_focus:s.focuses.clear()
            if missing_category:s.flags.discard('VIE_msl_program_started')
            before=copy.deepcopy(s.__dict__)
            check(not s.select(d['id']) and s.__dict__==before,'category/scope/focus gate '+d['id'])
            if wrong_scope or missing_focus:
                s.execute(EFFECTS[d['start']])
                check(s.__dict__==before,'direct start guard '+d['id'])
        for money in (d['treasury_cost']-.00001,d['treasury_cost'],d['treasury_cost']+1):
            for pp in (d['pp']-1,d['pp']):
                s=State(money,pp);s.flags.add('VIE_msl_program_started');s.focuses.add(d['focus'])
                if d.get('previous'):s.flags.add(d['previous'])
                before=copy.deepcopy(s.__dict__)
                ok=money>=d['treasury_cost'] and pp>=d['pp']
                check(s.select(d['id'])==ok,'funds/PP gate')
                if not ok:check(s.__dict__==before,'failed click no payment')
                else:
                    check(abs(s.money-(money-d['treasury_cost']))<1e-8 and s.pp==pp-d['pp'],'single start payment')
                    before=copy.deepcopy(s.__dict__)
                    s.execute(EFFECTS[d['start']])
                    check(s.__dict__==before,'double start blocked')
                    check(not s.select(d['id']),'active duplicate click blocked')
        s=State();s.flags.add('VIE_msl_program_started');s.focuses.add(d['focus'])
        if d.get('previous'):s.flags.add(d['previous'])
        if d['kind']=='program':
            check(value(EVENTS[d['event']],'hidden')=='yes' and value(EVENTS[d['event']],'is_triggered_only')=='yes','hidden callback')
            s.execute(value(EVENTS[d['event']], 'immediate'))
            check(d['done'] not in s.flags,'callback without start blocked')
            if d['previous']:
                s.flags.discard(d['previous']);check(not s.select(d['id']),'previous certification required');s.flags.add(d['previous'])
            check(s.select(d['id']),'program starts')
            check(d['running'] in s.flags and d['done'] not in s.flags,'running before certification')
            s.advance(179);s=copy.deepcopy(s)
            check(d['done'] not in s.flags,'no early timer completion')
            old=s.money;s.advance(1)
            check(d['done'] in s.flags and d['running'] not in s.flags and s.money==old,'completion no second charge')
            saved=copy.deepcopy(s.__dict__);s.execute(value(EVENTS[d['event']],'immediate'))
            check(s.__dict__==saved,'duplicate callback no-op')
            check(not s.select(d['id']),'certified program cannot repeat')
        else:
            check(s.select(d['id']) and d['idea'] in s.ideas,'maintenance timed idea')
            check(not s.research and s.xp=={'land':0,'naval':0},'no research/instant XP farm')
            s.advance(364);check(d['idea'] in s.ideas and not s.select(d['id']),'maintenance lasts 365')
            s.advance(1);check(d['idea'] not in s.ideas and s.select(d['id']),'maintenance repeat after expiry')
            s.ideas.discard(d['idea']);check(not s.select(d['id']),'cooldown despite early idea removal')
    s=State();s.focuses.add('VIE_modernize_vpa')
    for code in ('M00','M01','M02','M03','M04','M05','M06','M07'):
        check(s.complete_focus(NODES[code]['id']),'playthrough focus '+code)
    check(not s.focus_ready(NODES['M08']['id']),'M08 before certification locked')
    for d in [d for d in SPEC['decisions'] if d['kind']=='program']:
        check(s.select(d['id']),'playthrough program '+d['id']);s.advance(180)
    check(s.complete_focus(NODES['M08']['id']) and s.complete_focus(NODES['M09']['id']),'M08/M09 reachable')
    check(abs(s.money-38.25)<1e-8 and s.pp==845 and s.day==540,'playthrough 11.75 billion,175PP,540 days')
    for d in [d for d in SPEC['decisions'] if d['kind']=='maintenance']:check(s.select(d['id']),'endgame maintenance')
    total={}
    for iid in s.ideas:
        for k,op,v,line in value(IDEAS[iid],'modifier'):total[k]=total.get(k,0)+float(v)
    check(all(abs(total[k]-expected)<1e-8 for k,expected in dict(experience_gain_army_factor=.025,experience_gain_navy_factor=.025,production_factory_efficiency_gain_factor=.025,research_speed_factor=.01).items()),'endgame modifier ceiling')


def ai_tests():
    for n in NODES.values():
        b=value(FOCUSES[n['id']],'ai_will_do');s=State()
        check(s.weight(b)>0,'focus AI enabled '+n['code'])
        s.bankruptcy=True
        check((s.weight(b)==0)==bool(n['treasury_cost']),'focus bankruptcy guard')
        s.bankruptcy=False;s.money=n['treasury_cost']-.00001
        check((s.weight(b)==0)==bool(n['treasury_cost']),'focus budget guard')
        s=State();s.historical=True
        if n['code'] in ('M05','M06','M07'):
            before=s.weight(b);s.year=2015
            check(abs(before*4-s.weight(b))<1e-8,'historical pacing only')
            s.focuses.add(NODES['M00']['id'])
            check(s.focus_ready(n['id']),'date does not lock human focus')
    for d in SPEC['decisions']:
        if d['kind']=='integration_stub':continue
        b=value(DECISIONS[d['id']],'ai_will_do');s=State();s.focuses.add(d['focus'])
        if d.get('previous'):s.flags.add(d['previous'])
        check(s.weight(b)>0,'decision AI can advance')
        s.bankruptcy=True;check(s.weight(b)==0,'decision bankruptcy guard')
    plans=dict((k,v) for k,op,v,line in load(ROOT/'common/ai_strategy_plans/VIE_strategy_plans.txt'))
    for pid in ('VIE_HISTORICAL_plan','VIE_HARDLINE_plan'):
        factors=value(plans[pid],'focus_factors')
        for n in NODES.values():check(float(value(factors,n['id']))>0,'existing AI plan covers '+n['code'])


def reference_tests(md=None):
    locpath=ROOT/'localisation/english/VIE_missile_l_english.yml'
    raw=locpath.read_bytes();check(raw.startswith(b'\xef\xbb\xbf'),'localisation BOM')
    loc=dict(re.findall(r'^ ([A-Za-z_0-9.]+):0 "([^\n]*)"$',raw.decode('utf-8-sig'),re.M))
    for iid in [n['id'] for n in NODES.values()]+list(DECISIONS)+list(IDEAS)+['VIE_msl_program_category']:
        check(iid in loc and iid+'_desc' in loc,'title/description '+iid)
    for b in list(FOCUSES[n['id']] for n in NODES.values())+list(EFFECTS.values())+list(TRIGGERS.values())+list(DECISIONS.values())+list(EVENTS.values()):
        for k,op,v,line in walk(b):
            if k in ('custom_effect_tooltip','tooltip') and isinstance(v,str):check(v in loc,'tooltip '+v)
            if k=='unlock_decision_tooltip':check(v in DECISIONS,'decision unlock '+v)
            if k.startswith('VIE_msl_') and v in ('yes','no'):check(k in EFFECTS or k in TRIGGERS,'callable '+k)
            check(k not in ('add_equipment_to_stockpile','add_building_construction'),'no unverified equipment/buildings')
    for folder in ('common/scripted_effects','common/scripted_triggers','common/decisions','common/ideas','events'):
        for p in (ROOT/folder).rglob('*missile*.txt'):
            check(not p.read_bytes().startswith(b'\xef\xbb\xbf'),'script no BOM '+str(p))
    sprites={}
    roots=[ROOT]+([Path(md)] if md else [])
    for root in reversed(roots):
        for p in (root/'interface').glob('*.gfx'):
            for b in re.findall(r'spriteType\s*=\s*\{([^}]+)\}',p.read_text(encoding='utf-8-sig')):
                name=re.search(r'name\s*=\s*"([^"\n]+)"',b);texture=re.search(r'texturefile\s*=\s*"([^"\n]+)"',b)
                if name and texture:sprites[name[1]]=(root,texture[1])
    for n in NODES.values():
        check(n['icon'] in sprites,'focus sprite '+n['icon'])
        root,texture=sprites[n['icon']];check((root/texture).is_file(),'focus texture '+texture)
    if md:
        tags=(Path(md)/'common/technology_tags/00_technology.txt').read_text(encoding='utf-8-sig')
        check(all(re.search(r'\b'+c+r'\b',tags) for c in ('CAT_missiles','CAT_military_electronics')),'MD research category definitions')
        budget=(Path(md)/'common/scripted_effects/00_budget_effects.txt').read_text(encoding='utf-8-sig')
        check(re.search(r'^modify_treasury_effect\s*=\s*\{',budget,re.M) is not None,'MD treasury effect definition')
        for b in list(DECISIONS.values())+list(IDEAS.values()):
            icon=value(b,'icon') or 'GFX_idea_'+value(b,'picture')
            check(icon in sprites,'MD consumer sprite '+icon)
            root,texture=sprites[icon];check((root/texture).is_file(),'MD consumer texture '+texture)
    else:
        print('SKIP external MD sprites/categories/treasury: supply --md for provider validation')


def regression_tests(baseline):
    baseline=Path(baseline)
    old={value(b,'id'):b for b in values(value(load(baseline/'focus.txt'),'focus_tree'),'focus')}
    check(set(FOCUSES)==set(old)|{n['id'] for n in NODES.values()},'only 10 focuses added')
    for fid,b in old.items():check(normalize(b)==normalize(FOCUSES[fid]),'existing focus preserved '+fid)
    oldplans=dict((k,v) for k,op,v,line in load(baseline/'ai.txt'))
    newplans=dict((k,v) for k,op,v,line in load(ROOT/'common/ai_strategy_plans/VIE_strategy_plans.txt'))
    for pid,b in oldplans.items():
        filtered=[]
        for k,op,v,line in newplans[pid]:
            if k=='focus_factors':v=[a for a in v if not a[0].startswith('VIE_msl_')]
            filtered.append((k,op,v,line))
        check(normalize(b)==normalize(filtered),'existing AI semantics preserved '+pid)
    hashes=json.loads((baseline/'hashes.json').read_text(encoding='utf-8'))
    allowed={'common/national_focus/VIE_md_focus.txt','common/ai_strategy_plans/VIE_strategy_plans.txt'}
    for path,digest in hashes.items():
        if path not in allowed:check(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'existing file preserved '+path)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--md',type=Path)
    parser.add_argument('--baseline',type=Path)
    args=parser.parse_args()
    for fn in (node_tests,reward_tests,decision_tests,ai_tests):
        fn();print('PASS',fn.__name__)
    reference_tests(args.md);print('PASS reference_tests')
    if args.baseline:regression_tests(args.baseline);print('PASS baseline regression')
    print(f'PASS {COUNT} assertions; file fixture only, HOI4 runtime not tested')


if __name__=='__main__':
    main()
