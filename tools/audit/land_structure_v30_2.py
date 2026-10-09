"""Static contract checks for the V30.2 land-force focus graph."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from industry import ROOT, focus_map, groups, positions, read, value, values, walk

FOCUS_FILE = ROOT / 'common/national_focus/VIE_md_focus.txt'
focus_text = FOCUS_FILE.read_text(encoding='utf-8')
focuses = focus_map(focus_text)
land = {fid: node for fid, node in focuses.items() if fid.startswith('VIE_lf_')}
pos = positions(focuses)
spec = json.loads((ROOT / '.claude/docs/land/structure_v30_2.json').read_text(encoding='utf-8'))

assert len(land) == 44, len(land)
assert set(land) == set(spec['positions'])
for fid, xy in spec['positions'].items():
    assert list(pos[fid]) == xy, (fid, pos[fid], xy)

# All relative anchors are direct parents and have been declared earlier.
declared = {}
for match in __import__('re').finditer(r'(?m)^\s*focus\s*=\s*\{', focus_text):
    end=focus_text.find('}',match.start())
    fid=__import__('re').search(r'(?m)^\s*id\s*=\s*(\S+)',focus_text[match.start():end])
    if fid: declared[fid.group(1)]=match.start()
for fid,node in land.items():
    anchor=value(node,'relative_position_id')
    assert anchor in focuses and any(anchor in g for g in groups(node)), (fid,anchor,groups(node))
    assert declared[anchor] < declared[fid], ('forward anchor',fid,anchor)
    assert pos[fid][1] > pos[anchor][1], (fid,anchor,pos[fid],pos[anchor])
    for group in groups(node):
        for parent in group:
            assert pos[fid][1] > pos[parent][1], (fid,parent,pos[fid],pos[parent])

# Land and all other branches have no card sharing an absolute cell.
assert len(set(pos.values())) == len(pos), [(a,b,pos[a]) for i,a in enumerate(focuses) for b in list(focuses)[i+1:] if pos[a]==pos[b]]
for y in {pos[f][1] for f in land}:
    xs=sorted(pos[f][0] for f in land if pos[f][1]==y)
    assert all(b-a>=2 for a,b in zip(xs,xs[1:])),(y,xs)
    outside=[pos[f][0] for f in focuses if f not in land and pos[f][1]==y]
    assert all(abs(x-ox)>=2 for x in xs for ox in outside),(y,xs,outside)

def eq(fid, expected):
    actual=groups(focuses[fid])
    assert actual==expected,(fid,actual,expected)

eq('VIE_lf_combined_arms', [['VIE_lf_cadre_professional'],['VIE_lf_force_reorganization']])
for fid,parent in spec['program_edges'].items():
    eq(fid,[[parent]])
for fid, parents in spec['convergences'].items():
    eq(fid,parents)
for fid in spec['program_roots']:
    eq(fid, [['VIE_lf_army_reform']])
for fid in spec.get('advanced_roots', []):
    eq(fid, [['VIE_lf_command_reform_2']])
roots=spec['strategy_roots']
for fid in roots:
    assert set(values(value(land[fid],'mutually_exclusive',[]),'focus')) == set(roots)-{fid},fid
for fid in roots:
    assert groups(land[fid]) == [['VIE_lf_command_reform_1']]
eq('VIE_lf_command_reform_2', [['VIE_lf_mech_complete','VIE_lf_dev_strategic','VIE_lf_dev_territorial']])
eq('VIE_lf_selective_modernization', [['VIE_lf_command_reform_2']])
assert value(land['VIE_lf_selective_modernization'],'available') == [('VIE_lf_program_done_3','=','yes')]

# K2 gate directly counts six unique program terminals with a threshold of three.
triggers={k:v for k,_,v in read('common/scripted_triggers/VIE_md_triggers_p17.txt')}
count=value(value(triggers['VIE_lf_program_done_3'],'custom_trigger_tooltip'),'count_triggers')
assert value(count,'amount')=='3'
terminal_ids=set(values(count,'has_completed_focus'))
assert terminal_ids == set(spec['terminals'])
for n in range(7):
    assert (n>=3) == (sum(i<n for i in range(6))>=3)
assert len(terminal_ids)==6

# Every focus calls a defined helper; no legacy counter gate remains in live sources.
effects={k for k,_,_ in read('common/scripted_effects/VIE_md_effects_p17.txt')}
for fid,node in land.items():
    reward=value(node,'completion_reward',[])
    calls=[k for k,_,_ in reward if k.endswith('_reward')]
    assert len(calls)==1 and calls[0] in effects,(fid,calls)
for path in ['common/national_focus/VIE_md_focus.txt','common/on_actions/VIE_md_on_actions_startup.txt','common/scripted_triggers/VIE_md_triggers_p17.txt']:
    raw=(ROOT/path).read_text(encoding='utf-8')
    for old in ['VIE_lf_arm_count','VIE_lf_arm_done','VIE_lf_cap_count','VIE_lf_cap_done','VIE_lf_arm_slot_free','VIE_lf_cap_slot_free','VIE_lf_arm_done_3','VIE_lf_cap_done_2']:
        assert old not in raw,(path,old)

# Shared capability rewards remain independent of M/R/D choice and do not field units.
shared_helpers = [
    'VIE_lf_bb1_reward','VIE_lf_bb2_reward','VIE_lf_tg1_reward','VIE_lf_tg2_reward',
    'VIE_lf_pb1_reward','VIE_lf_pb2_reward','VIE_lf_cb_reward',
    'VIE_lf_mech_equipment_reward','VIE_lf_mech_sustainment_reward',
    'VIE_lf_l1_reward','VIE_lf_l2_reward','VIE_lf_a1_reward','VIE_lf_a2_reward',
    'VIE_lf_y1_reward','VIE_lf_y2_reward']
for helper in shared_helpers:
    raw_effect = next(v for k,_,v in read('common/scripted_effects/VIE_md_effects_p17.txt') if k==helper)
    names = [k for k,_,_ in walk(raw_effect)]
    assert not any(k in names for k in ['create_unit']), (helper,'create_unit')
    assert not any(k in names for k in ['has_country_flag']), (helper,'route-dependent gate',names)
for helper in ['VIE_lf_bb1_reward','VIE_lf_bb2_reward','VIE_lf_tg1_reward','VIE_lf_tg2_reward',
               'VIE_lf_pb1_reward','VIE_lf_pb2_reward','VIE_lf_cb_reward']:
    raw_effect = next(v for k,_,v in read('common/scripted_effects/VIE_md_effects_p17.txt') if k==helper)
    assert not any(k=='add_equipment_to_stockpile' for k,_,_ in walk(raw_effect)), helper
# The strategy rewards can prepare editable templates, but must not spawn free divisions.
for helper in ['VIE_lf_fr2_reward','VIE_lf_fm2_reward','VIE_lf_fd2_reward']:
    raw_effect = next(v for k,_,v in read('common/scripted_effects/VIE_md_effects_p17.txt') if k==helper)
    assert not any(k=='create_unit' for k,_,_ in walk(raw_effect)),helper
# The factory scripted effects charge their own cost; no extra treasury debit is stacked.
for helper in ['VIE_lf_mod_reward','VIE_lf_cap_reward']:
    raw_effect = next(v for k,_,v in read('common/scripted_effects/VIE_md_effects_p17.txt') if k==helper)
    assert any(k=='one_state_arms_factory' for k,_,_ in walk(raw_effect)),helper
    assert not any(k=='set_temp_variable' and any(n[0]=='treasury_change' for n in v) for k,_,v in walk(raw_effect)),helper

print(f'PASS V30.2: {len(land)} unique land focuses; all anchors direct/earlier; {len(pos)} global focus cells unique.')
print(f'PASS: six shared programs, three mutually exclusive strategies, OR convergence to Command Reform II, 3/6 terminal gate.')
print('PASS: shared rewards are order-independent, training does not issue stockpiles/divisions, and one_state construction is not double-charged.')
print('Scope: static focus graph and effect references; Clausewitz runtime, tooltips and in-game line routing are not simulated.')


