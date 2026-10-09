"""Check current land structure gates and rewards, without simulating HOI4."""
from collections import defaultdict
from copy import deepcopy
from itertools import combinations, permutations
import json
from pathlib import Path

from industry import ROOT, compare, focus_map, groups, positions, read, value, values, walk

SPEC = json.loads((ROOT / '.claude/docs/land/structure_v29.json').read_text(encoding='utf-8'))
EFFECTS = {k: v for k, _, v in read('common/scripted_effects/VIE_md_effects_p17.txt')}
TRIGGERS = {k: v for k, _, v in read('common/scripted_triggers/VIE_md_triggers_p17.txt')}
# Total dynamic-modifier budget for each route: three parallel projects, then one
# final focus. These totals equal the previous compatible reward combinations.
EXPECTED = {
    'regular': {'army_org_factor': .06, 'army_defence_factor': .015,
                'army_personnel_cost_multiplier_modifier': .02, 'experience_gain_army_factor': -.01,
                'army_speed_factor': .02, 'supply_consumption_factor': -.07,
                'equipment_cost_multiplier_modifier': .01},
    'mobile': {'army_speed_factor': .08, 'army_org_factor': .03,
               'conscription_factor': -.015, 'equipment_cost_multiplier_modifier': .03,
               'max_dig_in_factor': -.02, 'army_attack_factor': .03, 'supply_consumption_factor': -.02},
    'depth': {'max_dig_in_factor': .06, 'army_defence_factor': .025,
              'army_speed_factor': -.02, 'army_armor_attack_factor': -.015,
              'dig_in_speed_factor': .05, 'conscription_factor': .075,
              'army_personnel_cost_multiplier_modifier': .01},
}


def condition(block, s):
    def one(k, operator, v):
        if k == 'NOT': return not any(one(*n) for n in v)
        if k == 'OR': return any(one(*n) for n in v)
        if k in ('AND', 'custom_trigger_tooltip'): return condition(v, s)
        if k == 'tooltip': return True
        if k == 'has_country_flag': return v in s['flags']
        if k == 'has_completed_focus': return v in s['done']
        if k == 'has_selected_land_grand_doctrine': return s['doctrine'] == (v == 'yes')
        if k == 'check_variable':
            name, comparison, target = v[0]
            current, target = s['vars'][name], float(target)
            return {'<': current < target, '>': current > target,
                    '<=': current <= target, '>=': current >= target,
                    '=': current == target}[comparison]
        if k == 'date':
            current = tuple(map(int, s['date'].split('.')))
            target = tuple(map(int, v.split('.')))
            return compare(current, operator, target)
        if k in TRIGGERS: return condition(TRIGGERS[k], s)
        raise ValueError('Unsupported structure condition: ' + k)
    return all(one(*n) for n in block)


def apply_counter(block, variable, s):
    """Apply only the guarded counter writes from a real focus reward."""
    for k, _, v in block:
        if k == 'if' and condition(value(v, 'limit', []), s):
            apply_counter([n for n in v if n[0] != 'limit'], variable, s)
        elif k == 'hidden_effect':
            apply_counter(v, variable, s)
        elif k == 'add_to_variable':
            for name, _, amount in v:
                if name == variable:
                    s['vars'][name] += float(amount)


def effect(block, s):
    branch = None
    for k, _, v in block:
        if k in ('if', 'else_if', 'else'):
            if k == 'if': branch = False
            assert branch is not None
            if not branch and (k == 'else' or condition(value(v, 'limit', []), s)):
                effect([n for n in v if n[0] != 'limit'], s); branch = True
            continue
        branch = None
        if k == 'hidden_effect': effect(v, s)
        elif k in EFFECTS: effect(EFFECTS[k], s)
        elif k == 'set_country_flag': s['flags'].add(v)
        elif k == 'add_to_variable':
            for name, _, amount in v:
                if name != 'tooltip': s['vars'][name] += float(amount)
        elif k == 'army_experience': s['xp'] += float(v)
        elif k == 'add_mastery':
            assert value(v, 'folder') == 'land'; s['mastery'] += float(value(v, 'amount'))
        elif k == 'add_ideas': s['ideas'].add(v)
        elif k == 'division_template': s['templates'].append(value(v, 'name'))
        elif k == 'add_tech_bonus': s['research'].append(v)
        elif k in ('log', 'add_command_power', 'add_stability', 'add_war_support',
                   'set_temp_variable', 'change_the_military_opinion', 'unlock_decision_tooltip',
                   'custom_effect_tooltip', 'reduce_focus_completion_cost', 'force_update_dynamic_modifier',
                   'create_unit', 'add_equipment_to_stockpile', 'add_manpower',
                   'add_building_construction', 'modify_treasury_effect'):
            # This bounded checker evaluates modifier/XP/template contracts only.
            s['other'].append(k)
        else: raise ValueError('Unsupported structure effect: ' + k)


def can_complete(fid, s, focuses):
    node = focuses[fid]
    prerequisites = all(any(p in s['done'] for p in g) for g in groups(node))
    exclusions = any(p in s['done'] for p in values(value(node, 'mutually_exclusive', []), 'focus'))
    return prerequisites and not exclusions and condition(value(node, 'available', []), s)


def layout_metrics(pos, land):
    segments = []
    total_length = 0
    for child, node in land.items():
        for group in groups(node):
            for parent in group:
                if parent not in land:
                    continue
                px, py = pos[parent]; x, y = pos[child]
                mid = (py + y) / 2
                edge = (parent, child)
                total_length += abs(x - px) + abs(y - py)
                segments.extend((('v', px, py, mid, edge),
                                 ('h', mid, min(px, x), max(px, x), edge),
                                 ('v', x, mid, y, edge)))
    vertical = [s for s in segments if s[0] == 'v']
    horizontal = [s for s in segments if s[0] == 'h']
    crossings = 0
    for _, hy, x1, x2, edge_h in horizontal:
        for _, vx, y1, y2, edge_v in vertical:
            if edge_h[0] == edge_v[0] or edge_h[1] == edge_v[1]:
                continue
            if x1 < vx < x2 and min(y1, y2) < hy < max(y1, y2):
                crossings += 1
    return crossings, total_length


def main():
    focuses = focus_map((ROOT / 'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8'))
    pos = positions(focuses)
    land = {f: v for f, v in focuses.items() if f.startswith('VIE_lf_')}
    roots = ['VIE_lf_' + p['root'] for p in SPEC['paths']]
    terminals = ['VIE_lf_' + p['terminal'] for p in SPEC['paths']]
    assert len(land) == 38
    manifest = SPEC['layout']
    assert set(manifest) == set(land), (set(manifest) ^ set(land))
    for fid, expected in manifest.items():
        node = focuses[fid]
        assert pos[fid] == tuple(expected['position']), (fid, pos[fid], expected['position'])
        assert pos[fid][1] == expected['display_row'], fid
        assert value(node, 'relative_position_id') == expected['anchor'], fid
        assert groups(node) == expected['pre'], (fid, groups(node), expected['pre'])
        assert values(value(node, 'mutually_exclusive', []), 'focus') == expected['ex'], fid
        actual_available = json.loads(json.dumps(value(node, 'available', []) or []))
        assert actual_available == expected['available'], (fid, actual_available, expected['available'])
    expected_positions = {
        'VIE_lf_army_reform': (180, 2), 'VIE_lf_logistics_merge': (178, 3),
        'VIE_lf_basic_training': (182, 3), 'VIE_lf_combined_arms': (180, 6),
        'VIE_lf_command_reform_1': (180, 7), 'VIE_lf_command_reform_2': (180, 11),
        'VIE_lf_cap_border_urban': (174, 12), 'VIE_lf_cap_army_ad': (180, 12),
        'VIE_lf_cap_cyber_ew': (186, 12), 'VIE_lf_cap_area_control': (174, 13),
        'VIE_lf_cap_ad_coord': (180, 13), 'VIE_lf_cap_info_ops': (186, 13),
        'VIE_lf_selective_modernization': (180, 14),
        'VIE_lf_command_reform_3': (180, 15), 'VIE_lf_force_complete': (180, 16),
    }
    assert {fid: pos[fid] for fid in expected_positions} == expected_positions
    for fid, node in land.items():
        parents = {parent for group in groups(node) for parent in group}
        anchor = value(node, 'relative_position_id')
        assert anchor in parents, (fid, anchor, parents)
        assert pos[fid][1] > pos[anchor][1], (fid, anchor)
    for y in {pos[fid][1] for fid in land}:
        row_x = sorted(pos[fid][0] for fid in land if pos[fid][1] == y)
        assert all(b - a >= 2 for a, b in zip(row_x, row_x[1:])), (y, row_x)
        outsiders = [pos[fid][0] for fid in focuses if fid not in land and pos[fid][1] == y]
        assert all(abs(x - ox) >= 2 for x in row_x for ox in outsiders), (y, row_x, outsiders)
    crossings, edge_length = layout_metrics(pos, land)
    assert crossings == 0, crossings
    assert groups(focuses['VIE_lf_command_reform_2']) == [terminals]
    arm_gate = SPEC['selection_gates']['VIE_lf_combined_arms']
    arm_training = arm_gate['counted_by']
    assert (arm_gate['type'], arm_gate['required'], arm_gate['total']) == ('n_of_m', 3, 4)
    assert len(arm_training) == arm_gate['total']
    assert groups(focuses['VIE_lf_combined_arms']) == [arm_training]
    assert value(focuses['VIE_lf_combined_arms'], 'available') == [(arm_gate['trigger'], '=', 'yes')]
    assert arm_gate['available_focus'] == 'VIE_lf_combined_arms'
    assert pos['VIE_lf_arm_engineer_train'] == (186, 5)
    assert groups(focuses['VIE_lf_arm_engineer_train']) == [['VIE_lf_arm_engineers']]
    arm_orgs = ['VIE_lf_arm_infantry_org', 'VIE_lf_arm_armor_org',
                'VIE_lf_arm_arty_org', 'VIE_lf_arm_engineers']
    base_done = {'VIE_lf_army_reform', 'VIE_lf_logistics_merge', 'VIE_lf_basic_training'}
    assert not can_complete('VIE_lf_army_reform',
                            dict(done={'VIE_modernize_vpa'}, vars=defaultdict(float), date='2019.2.10'), focuses)
    assert can_complete('VIE_lf_army_reform',
                        dict(done={'VIE_modernize_vpa'}, vars=defaultdict(float), date='2019.2.11'), focuses)
    arm_routes = 0
    for selected_orgs in combinations(arm_orgs, arm_gate['slot_limit']):
        s = dict(done=base_done, flags=set(), doctrine=False, date='2026.1.1',
                 vars=defaultdict(float), xp=0, mastery=0, ideas=set(), templates=[], research=[], other=[])
        for fid in arm_orgs:
            assert can_complete(fid, s, focuses)  # slot gate allows first three
        for fid in selected_orgs:
            apply_counter(value(focuses[fid], 'completion_reward'), 'VIE_lf_arm_count', s)
            s['done'].add(fid)
        assert s['vars']['VIE_lf_arm_count'] == 3
        assert all(not can_complete(fid, s, focuses) for fid in arm_orgs if fid not in selected_orgs)
        selected_training = [fid for fid in arm_training if
                             arm_orgs[arm_training.index(fid)] in selected_orgs]
        for count in range(arm_gate['required'] + 1):
            for subset in combinations(selected_training, count):
                route = deepcopy(s)
                for fid in subset:
                    assert can_complete(fid, route, focuses)
                    apply_counter(value(focuses[fid], 'completion_reward'), 'VIE_lf_arm_done', route)
                    route['done'].add(fid)
                assert route['vars']['VIE_lf_arm_done'] == count
                assert can_complete(arm_gate['available_focus'], route, focuses) == (count >= arm_gate['required']), (subset, route['vars'])
                arm_routes += 1
    cap_gate = SPEC['selection_gates']['VIE_lf_selective_modernization']
    cap_terminals = cap_gate['counted_by']
    assert (cap_gate['type'], cap_gate['required'], cap_gate['total']) == ('n_of_m', 2, 3)
    assert len(cap_terminals) == cap_gate['total']
    assert groups(focuses['VIE_lf_selective_modernization']) == [cap_terminals]
    assert value(focuses['VIE_lf_selective_modernization'], 'available') == [(cap_gate['trigger'], '=', 'yes')]
    cap_roots = ['VIE_lf_cap_border_urban', 'VIE_lf_cap_army_ad', 'VIE_lf_cap_cyber_ew']
    cap_done = {'VIE_lf_command_reform_2'}
    cap_routes = 0
    for selected_roots in combinations(cap_roots, cap_gate['slot_limit']):
        s = dict(done=cap_done.copy(), flags=set(), doctrine=False, date='2026.1.1',
                 vars=defaultdict(float), xp=0, mastery=0, ideas=set(), templates=[], research=[], other=[])
        for fid in cap_roots:
            assert can_complete(fid, s, focuses)
        for fid in selected_roots:
            apply_counter(value(focuses[fid], 'completion_reward'), 'VIE_lf_cap_count', s)
            s['done'].add(fid)
        assert s['vars']['VIE_lf_cap_count'] == 2
        assert all(not can_complete(fid, s, focuses) for fid in cap_roots if fid not in selected_roots)
        selected_terminals = [cap_terminals[cap_roots.index(fid)] for fid in selected_roots]
        for count in range(cap_gate['required'] + 1):
            for subset in combinations(selected_terminals, count):
                route = deepcopy(s)
                for fid in subset:
                    assert can_complete(fid, route, focuses)
                    apply_counter(value(focuses[fid], 'completion_reward'), 'VIE_lf_cap_done', route)
                    route['done'].add(fid)
                assert route['vars']['VIE_lf_cap_done'] == count
                assert can_complete(cap_gate['available_focus'], route, focuses) == (count >= cap_gate['required']), (subset, route['vars'])
                cap_routes += 1
    for f, node in land.items():
        for group in groups(node):
            for parent in group: assert pos[f][1] > pos[parent][1], (f, parent)
    for r in roots:
        assert set(values(value(focuses[r], 'mutually_exclusive', []), 'focus')) == set(roots) - {r}
    for t in terminals: assert not values(value(focuses[t], 'mutually_exclusive', []), 'focus')
    results = []
    for path in SPEC['paths']:
        root = 'VIE_lf_' + path['root']
        components = ['VIE_lf_' + n[0] for n in path['nodes'][1:4]]
        terminal = 'VIE_lf_' + path['terminal']
        route_nodes = [root, *components, terminal]
        assert [pos[fid] for fid in route_nodes] == [tuple(p) for p in path['positions']]
        assert pos[root][1] == 8 and all(pos[fid][1] == 9 for fid in components)
        assert pos[terminal][1] == 10
        for doctrine in (False, True):
            s = dict(done={'VIE_lf_command_reform_1'}, flags=set(), doctrine=doctrine,
                     vars=defaultdict(float), xp=0, mastery=0, ideas=set(), templates=[], research=[], other=[])
            assert not can_complete('VIE_lf_command_reform_2', s, focuses)
            assert groups(focuses[root]) == [['VIE_lf_command_reform_1']]
            assert can_complete(root, s, focuses)
            effect(value(focuses[root], 'completion_reward'), s); s['done'].add(root)
            assert not can_complete(terminal, s, focuses)
            for fid in components:
                assert groups(focuses[fid]) == [[root]], fid
                assert can_complete(fid, s, focuses), fid
            for order_index, order in enumerate(permutations(components)):
                route = deepcopy(s)
                for i, fid in enumerate(order):
                    data = next(n for n in path['nodes'] if n[0] == fid.removeprefix('VIE_lf_'))
                    helper = 'VIE_lf_' + data[3] + '_reward'
                    assert value(focuses[fid], 'completion_reward')[-1][0] == helper
                    for name, _, _ in walk(EFFECTS[helper]):
                        assert name not in {'create_unit', 'add_equipment_to_stockpile', 'add_manpower',
                                            'add_building_construction', 'modify_treasury_effect'}, (fid, name)
                    assert can_complete(fid, route, focuses)
                    effect(value(focuses[fid], 'completion_reward'), route); route['done'].add(fid)
                    if i < 2:
                        assert not can_complete(terminal, route, focuses)
                assert groups(focuses[terminal]) == [[components[0]], [components[1]], [components[2]]]
                assert can_complete(terminal, route, focuses)
                data = next(n for n in path['nodes'] if n[0] == path['terminal'])
                helper = 'VIE_lf_' + data[3] + '_reward'
                assert value(focuses[terminal], 'completion_reward')[-1][0] == helper
                for name, _, _ in walk(EFFECTS[helper]):
                    assert name not in {'create_unit', 'add_equipment_to_stockpile', 'add_manpower',
                                        'add_building_construction', 'modify_treasury_effect'}, (terminal, name)
                for missing in components:
                    partial = deepcopy(route); partial['done'].remove(missing)
                    assert not can_complete(terminal, partial, focuses), (terminal, missing)
                effect(value(focuses[terminal], 'completion_reward'), route); route['done'].add(terminal)
                assert can_complete('VIE_lf_command_reform_2', route, focuses)
                assert not any(can_complete(r, route, focuses) for r in roots if r != root)
                got = {k.removeprefix('VIE_af_'): round(v, 6) for k, v in route['vars'].items()}
                assert got == EXPECTED[path['flag']], (path['flag'], got)
                xp = 50 if path['flag'] == 'depth' else 65
                assert (route['xp'], route['mastery']) == ((0, xp) if doctrine else (xp, 0))
                assert len(route['ideas']) == 1 and len(route['templates']) == 1
                # Guards keep the template from being redefined by repeated helper calls.
                before = len(route['templates']); effect(EFFECTS['VIE_lf_' + path['nodes'][1][3] + '_reward'], route)
                assert len(route['templates']) == before
                if not doctrine and order_index == 0: results.append((path['flag'], got, xp))
    for flag, totals, xp in results:
        print('PASS', flag, 'horizontal-route budget:', totals, 'XP/mastery:', xp)
    print(f'PASS {len(land)} focuses; horizontal sibling projects + AND terminal, direct anchors, min gap >= 2, connector crossings {crossings}, edge length {edge_length}; 3-of-4 training ({arm_routes} states), 2-of-3 capabilities ({cap_routes} states); one priority mutex, three terminals, no early C2/cross-path unlock; six doctrine routes; guarded templates')
    print('Static scope: parallel-route AND gates, variables, XP/mastery and template declarations; HOI4 runtime and full modifier stacking remain separate.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
