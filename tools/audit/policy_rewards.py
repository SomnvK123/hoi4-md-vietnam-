"""v32 direct reward scenarios; evaluates live scripts, not the HOI4 engine."""
from copy import deepcopy
import hashlib
import itertools
import json
from pathlib import Path
import re
import industry_scenarios as ind
import infra_scenarios as infra
from industry import ROOT, parse, value, values, walk, focus_map

OUT=ROOT/'.claude/docs/policy_rewards/v32'
MANIFEST=json.loads((OUT/'structure.json').read_text(encoding='utf-8'))
BASE=json.loads((OUT/'baseline.json').read_text(encoding='utf-8'))
ENGINES={'ind':ind,'infra':infra}
IDEAS={}
OWNED={n['id'] for groups in MANIFEST['families'].values() for nodes in groups.values() for n in nodes}|{'VIE_synchronized_infra_idea'}
for p in (ROOT/'common/ideas').glob('*.txt'):
    for group in values(value(parse(p.read_text(encoding='utf-8-sig')),'ideas',[]),'country'):
        for key,_,body in group:
            if key in OWNED:IDEAS[key]={k:float(v) for k,_,v in value(body,'modifier',[])}


def check_state(prefix,s):
    groups=MANIFEST['families'][prefix]
    for group,nodes in groups.items():
        owned=set(s['ideas'])&{n['id'] for n in nodes}
        assert len(owned)<=1,(prefix,group,owned)
        for key in owned:
            expected=next(n['modifiers'] for n in nodes if n['id']==key)
            assert IDEAS[key]==expected,(key,IDEAS[key],expected)
    if prefix=='infra':
        separate={n['id'] for g in ('ports','logistics') for n in groups[g]}
        combined={n['id'] for n in groups['multimodal']}
        assert not (set(s['ideas'])&separate and set(s['ideas'])&combined)
    owned={n['id'] for nodes in groups.values() for n in nodes}
    if prefix=='infra':owned.add('VIE_synchronized_infra_idea')
    totals={}
    for key in set(s['ideas'])&owned:
        for modifier,v in IDEAS[key].items():totals[modifier]=totals.get(modifier,0)+v
    limits={'ind':{'country_productivity_growth_modifier':.080,'research_speed_factor':.015,'industrial_capacity_factory':.060,'corporate_tax_income_multiplier_modifier':.060,'production_speed_industrial_complex_factor':.090,'production_speed_dockyard_factor':.05},
            'infra':{'country_productivity_growth_modifier':.088,'trade_opinion_factor':.073,'production_speed_infrastructure_factor':.2,'research_speed_factor':.01}}
    for k,cap in limits[prefix].items():assert totals.get(k,0)<=cap+1e-9,(prefix,k,totals.get(k),cap)


def install_observer(prefix,engine):
    original=engine.apply
    depth=0
    def observed(block,s,scope=None):
        nonlocal depth
        depth+=1
        try:original(block,s,scope)
        finally:depth-=1
        if depth==0:
            check_state(prefix,s)
            if any(k.endswith('_finish') for k,_,_ in block):
                snapshot=deepcopy(s)
                depth+=1
                try:original(block,s,scope)
                finally:depth-=1
                assert s==snapshot, prefix+' handover replay changed state'
    engine.apply=observed


def preservation():
    live_text=(ROOT/'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8')
    assert focus_map(live_text)==focus_map(BASE['focus_text']), 'Focus graph/gameplay changed outside effects'
    protected=[]
    for name,digest in BASE['protected'].items():
        p=ROOT/name
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:protected.append(name)
    assert not protected,'Concurrent/protected files changed: '+', '.join(protected)
    # Every start/payment/refund/timer contract remains byte-equivalent at AST level.
    for prefix,engine in ENGINES.items():
        owned={n['id'] for nodes in MANIFEST['families'][prefix].values() for n in nodes}
        def investment_contract(block):
            kept=[]
            for k,op,v in block:
                if k in ('VIE_ind_refresh_chip',f'VIE_{prefix}_refresh_policy_ideas'):continue
                if k in ('add_ideas','remove_ideas') and v in owned:continue
                if isinstance(v,list):
                    v=investment_contract(v)
                    if k in ('if','else_if','else') and all(a=='limit' for a,_,_ in v):continue
                kept.append((k,op,v))
            return kept
        for key,body in BASE['effects'][prefix].items():
            if key.endswith('_start') or 'scheduler' in key or 'prepaid' in key:
                assert engine.EFFECTS[key]==parse(render([(key,'=',body)]))[0][2],key
            if key.endswith('_finish'):
                previous=parse(render([(key,'=',body)]))[0][2]
                assert investment_contract(previous)==investment_contract(engine.EFFECTS[key]),key+' changed payment/refund/progress/bonus/building contract'
        assert len(engine.IDS)==(24 if prefix=='ind' else 22)
    print('PASS fresh baseline: all focus blocks, decisions, triggers, events, start costs and schedulers preserved')


def render(block):
    return '\n'.join(k+' '+op+' '+('{ '+render(v)+' }' if isinstance(v,list) else str(v)) for k,op,v in block)


def seed_ancestors(engine,fid,s,prefix):
    for group in engine.groups(engine.FOCUSES[fid]):
        parent=group[0]
        if parent in engine.IDS:
            seed_ancestors(engine,parent,s,prefix)
            s['flags'][MANIFEST['reward_flags'][parent]]=None


def direct_rewards():
    count=0
    for prefix,engine in ENGINES.items():
        for fid in MANIFEST['focuses'][prefix]:
            slug=fid.removeprefix('VIE_');key=f'VIE_{prefix}_{slug}_reward'
            s=engine.state();seed_ancestors(engine,fid,s,prefix)
            before=deepcopy(s);engine.apply(engine.EFFECTS[key],s)
            assert MANIFEST['reward_flags'][fid] in s['flags'],fid
            assert s['ideas']!=before['ideas'] or s['pp']!=before['pp'] or s['stability']!=before['stability'] or s['variables']!=before['variables'] or s['native_calls']!=before['native_calls'],fid+' has no direct benefit'
            assert not s['buildings'] and not s['bonus'],fid+' granted investment result'
            new_delivery={k for k in s['flags'] if k.endswith('_done')}-{k for k in before['flags'] if k.endswith('_done')}
            assert not new_delivery,(fid,new_delivery)
            assert s['variables'].get('VIE_expressway_km',0)==before['variables'].get('VIE_expressway_km',0)
            if prefix=='ind' and slug not in ('industrialization_strategy','fdi_technology_screening'):
                assert s['variables'].get('VIE_ind_localization',0)==before['variables'].get('VIE_ind_localization',0)
            snapshot=deepcopy(s);engine.apply(engine.EFFECTS[key],s);assert s==snapshot,fid+' replay'
            # No dependence on the engine setting completed focus before reward.
            assert fid not in s['completed']
            count+=1
        for left,right in ([('fdi_fast_track','fdi_technology_screening'),('chip_design_packaging_priority','chip_pilot_fab_priority')] if prefix=='ind' else [('expressway_bot','expressway_public_investment'),('socialized_airports','acv_monopoly')]):
            for first,second in ((left,right),(right,left)):
                s=engine.state();engine.apply(engine.EFFECTS[f'VIE_{prefix}_{first}_reward'],s)
                snapshot=deepcopy(s);engine.apply(engine.EFFECTS[f'VIE_{prefix}_{second}_reward'],s);assert s==snapshot,(first,second)
    assert count==46
    print('PASS 46 immediate rewards, no completion-order assumption, replay and four mutex pairs both directions')


def tiers():
    for prefix,engine in ENGINES.items():
        master=engine.EFFECTS[f'VIE_{prefix}_refresh_policy_ideas']
        for group,nodes in MANIFEST['families'][prefix].items():
            for node in nodes:
                s=engine.state();s['ideas'][node['id']]=None
                engine.apply(master,s);assert node['id'] in s['ideas'],(prefix,group,node['id'],'downgrade')
                snapshot=deepcopy(s);engine.apply(master,s);assert snapshot==s
    # All ordering combinations of independent research/design/OSAT policies.
    for order in itertools.permutations(('chip_design','osat_packaging')):
        s=ind.state()
        for slug in ('chip_engineers','chip_design_packaging_priority',*order):ind.apply(ind.EFFECTS['VIE_ind_'+slug+'_reward'],s)
        assert 'VIE_ind_policy_chip_4_idea' in s['ideas']
        for key in ('chip_workforce','chip_design','chip_osat'):s['flags']['VIE_ind_'+key+'_done']=None
        ind.apply(ind.EFFECTS['VIE_ind_refresh_policy_ideas'],s);assert 'VIE_semiconductor_idea' in s['ideas']
        ind.apply(ind.EFFECTS['VIE_ind_semiconductor_fab_reward'],s);assert 'VIE_ind_policy_chip_6_idea' in s['ideas']
        s['flags']['VIE_ind_chip_fab_done']=None;ind.apply(ind.EFFECTS['VIE_ind_refresh_policy_ideas'],s)
        assert 'VIE_chip_sector_idea' in s['ideas']
    for order in itertools.permutations(('urban_rail_program','north_south_hsr')):
        s=infra.state()
        for slug in ('railway_national_program','reunification_line_upgrade',*order,'rail_technology_transfer'):infra.apply(infra.EFFECTS['VIE_infra_'+slug+'_reward'],s)
        assert 'VIE_infra_policy_rail_5_idea' in s['ideas']
    s=infra.state()
    expected=[('transport_strategy_2004','VIE_infra_policy_road_1_idea'),('north_south_expressway','VIE_infra_policy_road_2_idea'),('expressway_regional_links','VIE_infra_policy_road_4_idea'),('expressway_5000km_2030','VIE_infra_policy_road_5_idea')]
    for slug,wanted in expected:
        infra.apply(infra.EFFECTS['VIE_infra_'+slug+'_reward'],s);assert wanted in s['ideas']
    for km,wanted in [(2999,'VIE_infra_policy_road_5_idea'),(3000,'VIE_expressway_idea_2'),(4999,'VIE_expressway_idea_2'),(5000,'VIE_expressway_idea_3')]:
        s['variables']['VIE_expressway_km']=km;infra.apply(infra.EFFECTS['VIE_infra_refresh_roads'],s);assert wanted in s['ideas']
    # Planning does not certify any capstone or external delivered capability.
    for prefix,engine in ENGINES.items():
        s=engine.state()
        for fid,flag in MANIFEST['reward_flags'].items():
            if fid in engine.IDS and 'modern_' not in fid and 'synchronized_' not in fid:s['flags'][flag]=None
        engine.apply(engine.EFFECTS[f'VIE_{prefix}_refresh_policy_ideas'],s)
        trigger='VIE_ind_capstone_ready' if prefix=='ind' else 'VIE_infra_three_programs_ready'
        assert not engine.condition(engine.TRIGGERS[trigger],s)
        if prefix=='ind':assert not engine.condition(engine.TRIGGERS['VIE_ind_semiconductor_foundation_ready'],s)
    print('PASS exact tiers, monotonic/idempotent refresh, research path orders, road thresholds and planning != delivery')


def refund_policy():
    s=ind.base();ind.unlock('VIE_textile_garment_exports',s);before=set(s['ideas']);ind.start('VIE_ind_d_textile_base',s)
    s['owned'].remove(522);ind.advance(s,365)
    assert set(s['ideas'])==before and 'VIE_ind_textile_base_done' not in s['flags']
    s=infra.state();s['completed'].add('VIE_doi_moi_continues');infra.unlock('VIE_infrastructure_development',s);infra.unlock('VIE_transport_strategy_2004',s)
    before=set(s['ideas']);infra.start('VIE_infra_d_road_foundation_1',s);s['controlled'].remove(518);infra.advance(s,180)
    assert set(s['ideas'])==before and s['variables'].get('VIE_expressway_km',0)==0
    print('PASS refund retains adopted policy without investment upgrade or progress')


def shared_country():
    for order in ((ind,infra),(infra,ind)):
        s=ind.state()
        for engine in order:
            prefix='ind' if engine is ind else 'infra'
            slug='industrialization_strategy' if engine is ind else 'infrastructure_development'
            engine.apply(engine.EFFECTS[f'VIE_{prefix}_{slug}_reward'],s)
        assert s['native_calls'].count('VIE_ax_init')==1 and s['pp']==50
    s=ind.base();infra.unlock('VIE_infrastructure_development',s);infra.unlock('VIE_transport_strategy_2004',s)
    ind.unlock('VIE_textile_garment_exports',s)
    ind.start('VIE_ind_d_textile_base',s);infra.start('VIE_infra_d_road_foundation_1',s)
    assert 'VIE_ind_textile_busy' in s['flags'] and 'VIE_infra_road_busy' in s['flags']
    before=s['variables']['treasury']
    infra.apply(infra.EFFECTS['VIE_infra_d_road_foundation_1_finish'],s)
    assert 'VIE_ind_textile_busy' in s['flags'] and 'VIE_infra_road_busy' not in s['flags']
    ind.apply(ind.EFFECTS['VIE_ind_d_textile_base_finish'],s)
    assert s['variables']['treasury']==before and s['variables']['VIE_expressway_km']==400
    print('PASS shared country: root initialization once, separate industry/infrastructure slots and prepaid handovers')


def localisation():
    loc={}
    for p in (ROOT/'localisation').rglob('*.yml'):
        for key,text in re.findall(r'^\s*([\w.]+):\d "(.*)"',p.read_text(encoding='utf-8-sig'),re.M):
            loc.setdefault(key,[]).append(text)
    for ident,node in MANIFEST['new_ideas'].items():
        assert len(loc.get(ident,[]))==1 and len(loc.get(ident+'_desc',[]))==1
        assert IDEAS[ident]==node['modifiers']
    for prefix,engine in ENGINES.items():
        for fid in engine.IDS:
            key='VIE_tt_'+prefix+'_policy_'+fid.removeprefix('VIE_');assert len(loc.get(key,[]))==1
            assert all(label in loc[key][0] for label in ('Nhận ngay:','Mở đầu tư:','Sau bàn giao:'))
    assert (ROOT/'localisation/english/VIE_policy_rewards_l_english.yml').read_bytes().startswith(b'\xef\xbb\xbf')
    print('PASS concrete three-part focus tooltips, 35 unique idea title/descriptions and UTF-8 BOM')


def main():
    preservation()
    for prefix,engine in ENGINES.items():install_observer(prefix,engine)
    direct_rewards();tiers();refund_policy();shared_country();localisation()
    ind.graph_checks();ind.capstone_checks();ind.routes();ind.lifecycle_checks();ind.event_checks()
    # v30 graph/total-preservation contracts are historical; v32 preservation above checks the current tree unchanged.
    infra.capstone_checks();infra.routes();infra.edge_checks();infra.scheduler_checks();infra.balance_checks();infra.ai_checks()
    print('ALL V32 POLICY SCENARIOS PASS; engine UI/timers/save-load/AI still require HOI4 QA')


if __name__=='__main__':main()
