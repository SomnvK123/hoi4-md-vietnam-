"""Execute a bounded subset of the LIVE land-42 scripts for regression checks.

Unknown evaluated tokens fail. Uses live effects, triggers, decisions and spirits;
MD's treasury helper is read from --md or the repository cache. Timer advancement
is a test harness, not a claim about engine scheduling/civil-war/AI behaviour.
"""
import argparse
import itertools
from copy import deepcopy
from pathlib import Path
import re
from industry import ROOT, read, parse, value, values, walk, groups, compare
from land_42_structure import load

MANIFEST, FOCUSES, RECORDS = load()
IDS = {c: n['id'] for c, n in RECORDS.items()}
EFFECTS = {k: v for k, _, v in read('common/scripted_effects/VIE_md_effects.txt') if k.startswith('VIE_lf_')}
TRIGGERS = {k: v for k, _, v in read('common/scripted_triggers/VIE_md_triggers_land_force.txt')}
DECISIONS = {k: v for k, _, v in value(read('common/decisions/VIE_md_decisions_land_force.txt'), 'VIE_military_readiness_category')}
IDEAS = {k: b for country in values(value(read('common/ideas/VIE_md_ideas_land_force.txt'), 'ideas'), 'country') for k, _, b in country}


def state(**updates):
    s = dict(completed={'VIE_modernize_vpa'}, variables={'treasury': 10.}, temps={}, flags=set(), ideas=set(),
             date='2027.1.1', original_tag='VIE', doctrine=False, nsb=False, techs=set(), bankrupt=False,
             xp=0, mastery=0, cp=0, bonus=[], native_calls=[], now=0, active={})
    s.update(updates)
    return s


def number(v, s):
    try:
        return float(v)
    except ValueError:
        return s['temps'].get(v, s['variables'].get(v, 0))


def condition(block, s):
    def one(k, op, v):
        if k in ('tooltip', 'localization_key'):
            return True
        if k in ('AND', 'custom_trigger_tooltip'):
            return condition(v, s)
        if k == 'OR':
            return any(one(*item) for item in v)
        if k == 'NOT':
            return not condition(v, s)
        if k == 'original_tag':
            return s['original_tag'] == v
        if k == 'has_completed_focus':
            return v in s['completed']
        if k == 'has_country_flag':
            return v in s['flags']
        if k == 'has_idea':
            return v in s['ideas']
        if k == 'has_active_mission':
            assert v == 'bankruptcy_incoming_collapse'
            return s['bankrupt']
        if k == 'has_dlc':
            assert v == 'No Step Back'
            return s['nsb']
        if k == 'has_tech':
            return v in s['techs']
        if k == 'has_selected_land_grand_doctrine':
            return s['doctrine'] == (v == 'yes')
        if k == 'date':
            return compare(tuple(map(int, s['date'].split('.'))), op, tuple(map(int, v.split('.'))))
        if k == 'check_variable':
            if value(v, 'var'):
                operations = {'greater_than_or_equals': '>=', 'greater_than': '>', 'equals': '=', 'less_than': '<'}
                return compare(number(value(v, 'var'), s), operations[value(v, 'compare')], number(value(v, 'value'), s))
            return all(compare(number(a, s), o, number(b, s)) for a, o, b in v if a != 'tooltip')
        if k == 'always':
            return v == 'yes'
        if k in TRIGGERS:
            return condition(TRIGGERS[k], s) == (v == 'yes')
        raise ValueError('Unsupported trigger: ' + k)
    return all(one(*item) for item in block)


def apply(block, s):
    taken = None
    for k, op, v in block:
        if k in ('if', 'else_if', 'else'):
            if k == 'if':
                taken = False
            execute = not taken and (k == 'else' or condition(value(v, 'limit', []), s))
            if execute:
                taken = True
                apply([item for item in v if item[0] != 'limit'], s)
            continue
        taken = None
        if k in ('log', 'custom_effect_tooltip', 'unlock_decision_tooltip'):
            continue
        if k == 'hidden_effect':
            apply(v, s)
        elif k in ('set_variable', 'set_temp_variable', 'add_to_variable'):
            target = s['temps'] if k == 'set_temp_variable' else s['variables']
            for var, _, val in v:
                if var == 'tooltip':
                    continue
                n = number(val, s)
                target[var] = target.get(var, 0) + n if k == 'add_to_variable' else n
        elif k == 'set_country_flag':
            assert isinstance(v, str)
            s['flags'].add(v)
        elif k == 'clr_country_flag':
            s['flags'].discard(v)
        elif k == 'add_ideas':
            assert v in IDEAS
            s['ideas'].add(v)
        elif k == 'remove_ideas':
            assert v in s['ideas'], ('Unguarded remove', v)
            s['ideas'].remove(v)
        elif k == 'army_experience':
            s['xp'] += number(v, s)
        elif k == 'add_mastery':
            assert value(v, 'folder') == 'land'
            s['mastery'] += number(value(v, 'amount'), s)
        elif k == 'add_command_power':
            s['cp'] += number(v, s)
        elif k == 'add_tech_bonus':
            s['bonus'].append(dict(name=value(v, 'name'), category=value(v, 'category'), bonus=float(value(v, 'bonus')), uses=int(value(v, 'uses'))))
        elif k in ('force_update_dynamic_modifier', 'update_money_dirty_variable'):
            s['native_calls'].append(k)
        elif k in EFFECTS:
            apply(EFFECTS[k], s)
        else:
            raise ValueError('Unsupported effect: ' + k)


def execute(code, s):
    fid, b = IDS[code], FOCUSES[IDS[code]]
    assert all(any(p in s['completed'] for p in g) for g in groups(b)), code + ' prerequisites'
    assert condition(value(b, 'available', []), s), code + ' availability'
    mutex = {p for g in values(b, 'mutually_exclusive') for p in values(g, 'focus')}
    assert not mutex & s['completed'], code + ' mutex'
    apply(value(b, 'completion_reward'), s)
    # Reward must work before its own completed_focus becomes observable.
    s['completed'].add(fid)
    snapshot = deepcopy(s)
    apply(EFFECTS[f'VIE_lf_reward_{code.lower()}_effect'], s)
    assert s == snapshot, (code, 'reward replay')
    apply(EFFECTS['VIE_lf_reconcile_ideas_effect'], s)
    assert s == snapshot, (code, 'reconciliation replay')


def complete_route(route, industry=False, industry_first=False, doctrine=False):
    s = state(doctrine=doctrine)
    common = ['L0'] + [f'D{i}' for i in range(1, 9)] + [f'B{i}' for i in range(1, 9)]
    industrial = [f'I{i}' for i in range(1, 6)]
    branch = [f'{route}{i}' for i in range(1, 7)] + ['F1', 'F2']
    codes = common + (industrial + branch if industry_first else branch + industrial) if industry else common + branch
    for c in codes:
        execute(c, s)
    return s


def totals(s):
    result = {k.removeprefix('VIE_af_'): v for k, v in s['variables'].items() if k.startswith('VIE_af_')}
    for name in s['ideas']:
        for k, _, v in value(IDEAS[name], 'modifier', []):
            result[k] = result.get(k, 0) + float(v)
    return result


def start(name, s):
    b = DECISIONS[name]
    assert condition(value(b, 'visible'), s)
    assert condition(value(b, 'available'), s)
    assert name not in s['active']
    apply(value(b, 'complete_effect'), s)
    s['active'][name] = s['now'] + int(value(b, 'days_remove'))


def advance(days, s):
    s['now'] += days
    for name, deadline in list(s['active'].items()):
        if deadline <= s['now']:
            apply(value(DECISIONS[name], 'remove_effect'), s)
            del s['active'][name]


def providers(md):
    # Definitions, not consumers, are checked against the installed provider.
    categories = {value(v, 'category') for b in EFFECTS.values() for k, _, v in walk(b) if k == 'add_tech_bonus'}
    text = '\n'.join(p.read_text(encoding='utf-8-sig') for p in (md / 'common/technologies').glob('*.txt'))
    for cat in categories:
        assert re.search(r'\b' + re.escape(cat) + r'\b', text), ('Missing category', cat)
    for tech, filename in (('mbt_tech_2', 'NSB_armor.txt'), ('IFV_4', 'armor.txt')):
        assert re.search(r'\b' + tech + r'\s*=\s*\{', (md / 'common/technologies' / filename).read_text(encoding='utf-8-sig'))
    equipment = '\n'.join(p.read_text(encoding='utf-8-sig') for p in (md / 'common/units/equipment').glob('*.txt'))
    assert re.search(r'\bmedium_tank_flame_chassis\s*=\s*\{', equipment)
    sprites = '\n'.join(p.read_text(encoding='utf-8-sig') for folder in (ROOT / 'interface', md / 'interface') for p in folder.glob('*.gfx'))
    for b in IDEAS.values():
        assert '"GFX_idea_' + value(b, 'picture') + '"' in sprites, ('Missing idea sprite', value(b, 'picture'))
    for b in DECISIONS.values():
        assert '"' + value(b, 'icon') + '"' in sprites, ('Missing decision sprite', value(b, 'icon'))
    templates = '\n'.join(p.read_text(encoding='utf-8-sig') for p in (md / 'common/ai_templates').glob('*.txt'))
    ai = read('common/ai_strategy/VIE_md_ai.txt')
    for k, _, body in ai:
        if k in ('VIE_lf_m_force_mix', 'VIE_lf_r_force_mix'):
            for strategy in values(body, 'ai_strategy'):
                role = value(strategy, 'id')
                assert re.search(r'\brole\s*=\s*' + re.escape(role) + r'\b', templates), ('Missing MD role definition', role)
    print('PASS: installed MD technology categories, two DLC gates, IFV archetype, spirit/decision sprites and force-mix roles.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--md', type=Path, help='Installed MD root; also verifies provider definitions')
    args = parser.parse_args()
    treasury = args.md / 'common/scripted_effects/00_budget_effects.txt' if args.md else ROOT / 'tools/audit/md_ref/00_budget_effects.txt'
    md_effects = dict((k, v) for k, _, v in parse(treasury.read_text(encoding='utf-8-sig')))
    EFFECTS['modify_treasury_effect'] = md_effects['modify_treasury_effect']
    if args.md:
        providers(args.md)
    assert len(DECISIONS) == 3
    forbidden = {'add_equipment_to_stockpile', 'create_equipment_variant', 'add_building_construction', 'set_grand_doctrine', 'add_manpower'}
    assert not any(k in forbidden for b in EFFECTS.values() for k, _, _ in walk(b))
    backing = dict((k, v) for k, _, v in value(read('common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt'), 'VIE_armed_forces_modifier'))
    for b in EFFECTS.values():
        for k, _, v in walk(b):
            if k == 'add_to_variable':
                for var, _, _ in v:
                    if var.startswith('VIE_af_'):
                        assert var in backing.values(), ('Missing backing modifier', var)
    written, read_flags = set(), set()
    for b in list(EFFECTS.values()) + list(TRIGGERS.values()) + list(DECISIONS.values()):
        for k, _, v in walk(b):
            if k == 'set_country_flag':
                written.add(v)
            if k == 'has_country_flag' and v.startswith('VIE_lf_'):
                read_flags.add(v)
    assert read_flags <= written, ('Dead flag gates', read_flags - written)
    for r in 'PMR':
        plain, full, reversed_order = complete_route(r), complete_route(r, True, True), complete_route(r, True, False)
        # Research bonus inventory is unordered; R4/I3/I4 legitimately register in different orders.
        comparable = deepcopy(reversed_order)
        comparable['bonus'] = sorted(comparable['bonus'], key=lambda b: b['name'])
        forward = deepcopy(full)
        forward['bonus'] = sorted(forward['bonus'], key=lambda b: b['name'])
        assert forward == comparable, (r, 'industry completion order')
        assert len([i for i in full['ideas'] if '_priority_' in i]) == 1
        assert len([i for i in full['ideas'] if '_territorial_' in i]) == 1
        t = totals(full)
        caps = {'army_org_factor': .04, 'army_defence_factor': .03, 'army_core_defence_factor': .04,
                'army_armor_attack_factor': .04, 'army_armor_defence_factor': .01, 'army_artillery_attack_factor': .02,
                'army_speed_factor': .04, 'recon_factor': .04, 'terrain_penalty_reduction': .05,
                'max_dig_in_factor': .08, 'dig_in_speed_factor': .09, 'planning_speed': .06}
        for k, cap in caps.items():
            assert t.get(k, 0) <= cap + 1e-9, (r, k, t.get(k), cap)
        assert t.get('supply_consumption_factor', 0) >= -.05 - 1e-9
        assert t.get('attrition', 0) >= -.03 - 1e-9
        assert t.get('training_time_factor', 0) >= -.05 - 1e-9
        assert t.get('army_fuel_consumption_factor', 0) <= .05 + 1e-9
        mastery = complete_route(r, True, True, doctrine=True)
        assert mastery['xp'] == 0 and mastery['mastery'] == full['xp']
        assert plain['xp'] == full['xp']
        # Include live root/territorial spirits and militia backing contributions in a separate ledger.
        legacy = {}
        old_ideas = {k: b for country in values(value(read('common/ideas/VIE_md_ideas_p2.txt'), 'ideas'), 'country') for k, _, b in country}
        for name in ('VIE_vpa_modernization_idea', 'VIE_peoples_defence_idea', 'VIE_provincial_defence_idea'):
            for k, _, v in value(old_ideas[name], 'modifier', []):
                legacy[k] = legacy.get(k, 0) + float(v)
        for k, _, v in walk(FOCUSES['VIE_militia_law']):
            if k == 'add_to_variable':
                for var, _, amount in v:
                    if var.startswith('VIE_af_'):
                        key = var.removeprefix('VIE_af_')
                        legacy[key] = legacy.get(key, 0) + float(amount)
        combined = {k: t.get(k, 0) + legacy.get(k, 0) for k in t.keys() | legacy.keys()}
        assert combined.get('army_defence_factor', 0) <= .16 + 1e-9
        assert combined.get('army_org_factor', 0) <= .08 + 1e-9
        assert combined.get('supply_consumption_factor', 0) >= -.10 - 1e-9
        assert combined.get('max_dig_in_factor', 0) <= .15 + 1e-9
        print('LEDGER', r, 'branch=', {k: round(v, 5) for k, v in sorted(t.items())})
        print('LEDGER', r, 'with live root/territorial/militia=', {k: round(v, 5) for k, v in sorted(combined.items())})
    print('PASS: routes, live reward caps, spirit replacement, replay, XP/mastery and industry order.')

    # Exercise every legal order of the actual synergy callers, including I2 before D6.
    for codes, prerequisites, expected in (
        (('I2', 'D6', 'P5'), ('I1', 'D4', 'D5', 'P3'), 'VIE_lf_material_support_idea'),
        (('I3', 'I4', 'M3'), ('I1', 'I2', 'M1'), 'VIE_lf_ifv_integration_idea'),
    ):
        outcomes = []
        for sequence in itertools.permutations(codes):
            s = state(completed={'VIE_modernize_vpa'} | {IDS[c] for c in prerequisites})
            valid = True
            for c in sequence:
                if not all(any(p in s['completed'] for p in g) for g in groups(FOCUSES[IDS[c]])):
                    valid = False
                    break
                execute(c, s)
            if valid:
                assert expected in s['ideas']
                outcomes.append((s['ideas'], s['variables'], sorted(s['bonus'], key=lambda b: b['name'])))
        assert len(outcomes) >= 3 and all(o == outcomes[0] for o in outcomes)
    print('PASS: all legal caller permutations for I2/D6/P5 and I3/I4/M3.')

    # Specific gates and dates, not just an eventual-completion model.
    for code, node in RECORDS.items():
        if node['year']:
            s = state(date=f'{node["year"] - 1}.12.31')
            assert not condition(value(FOCUSES[node['id']], 'available'), s)
            s['date'] = f'{node["year"]}.1.1'
            assert condition(value(FOCUSES[node['id']], 'available'), s)
    # Verify authored profile preferences; this checks weights, not engine selection frequencies.
    for profile, preferred in (('VIE_ai_historical_path', 'P1'), ('VIE_ai_hardline', 'M1')):
        weights = {}
        for code in ('P1', 'M1', 'R1'):
            b = value(FOCUSES[IDS[code]], 'ai_will_do')
            weight = float(value(b, 'base'))
            for modifier in values(b, 'modifier'):
                if value(modifier, profile) == 'yes':
                    weight *= float(value(modifier, 'factor'))
            weights[code] = weight
        assert max(weights, key=weights.get) == preferred, (profile, weights)
    ai = dict((k, b) for k, _, b in read('common/ai_strategy/VIE_md_ai.txt'))
    disabled = {v for k, _, v in walk(value(ai['VIE_historical_force_mix'], 'enable')) if k == 'has_completed_focus'}
    assert {IDS['M1'], IDS['R1']} <= disabled
    for code, name in (('M1', 'VIE_lf_m_force_mix'), ('R1', 'VIE_lf_r_force_mix')):
        assert value(value(ai[name], 'enable'), 'has_completed_focus') == IDS[code]
        assert value(ai[name], 'abort_when_not_enabled') == 'yes'
    foreign = state(original_tag='CHI')
    before = deepcopy(foreign)
    for c in RECORDS:
        apply(EFFECTS[f'VIE_lf_reward_{c.lower()}_effect'], foreign)
    assert foreign == before

    for nsb, tech in ((True, 'mbt_tech_2'), (False, 'IFV_4')):
        s = complete_route('M', True)
        s['nsb'] = nsb
        names = list(DECISIONS)
        stage_costs = (.6, .3, .6)
        for index, name in enumerate(names):
            decision, cost = DECISIONS[name], stage_costs[index]
            s['variables']['treasury'] = cost - .001
            assert not condition(value(decision, 'available'), s)
            before = deepcopy(s)
            apply(EFFECTS[name + '_start_effect'], s)
            assert s == before, 'failed payment changed state'
            if index == 1:
                s['variables']['treasury'] = cost
                assert not condition(value(decision, 'available'), s)
                s['techs'] = {tech}
            s['variables']['treasury'] = cost
            s['bankrupt'] = True
            assert not condition(value(decision, 'available'), s)
            s['bankrupt'] = False
            start(name, s)
            assert abs(s['variables']['treasury']) < 1e-9
            paid = deepcopy(s)
            apply(EFFECTS[name + '_start_effect'], s)
            assert s == paid, 'double payment'
            advance(int(value(decision, 'days_remove')) - 1, s)
            assert name in s['active']
            s = deepcopy(s)  # harness state survives save/load-equivalent copying
            advance(1, s)
            done = deepcopy(s)
            apply(EFFECTS[name + '_finish_effect'], s)
            assert s == done, 'finish replay'
            assert not condition(value(decision, 'available'), s)
        assert 'VIE_lf_ifv_serial_ready_idea' in s['ideas']
        bonus = value(value(IDEAS['VIE_lf_ifv_serial_ready_idea'], 'equipment_bonus'), 'medium_tank_flame_chassis')
        assert float(value(bonus, 'build_cost_ic')) == -.05
        assert value(bonus, 'instant') == 'yes'
    # No evaluation before design, no serial before I5/certification, no unpaid completion.
    s = state(completed={'VIE_modernize_vpa', IDS['I4'], IDS['I5']}, techs={'IFV_4'})
    for name, b in DECISIONS.items():
        if name != 'VIE_lf_xcb01_design_program':
            assert not condition(value(b, 'available'), s)
        before = deepcopy(s)
        apply(EFFECTS[name + '_finish_effect'], s)
        assert s == before
    s['flags'].add('VIE_lf_xcb01_evaluation_done')
    s['completed'].discard(IDS['I5'])
    assert not condition(value(DECISIONS['VIE_lf_xcb01_serial_preparation'], 'available'), s)
    print('PASS: date boundaries, foreign-country guards, exact treasury thresholds, bankruptcy, both DLC paths, ordered stages, no double payment/unpaid completion/replay.')
    print('NOT TESTED: engine timers, actual save serialization/civil wars, designer UI, production IC display, focus connectors, error.log and long-running AI. Other laws/tech/MIO/traits are outside the ledger.')


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, ValueError, KeyError) as exc:
        raise SystemExit('FAIL: ' + str(exc))
