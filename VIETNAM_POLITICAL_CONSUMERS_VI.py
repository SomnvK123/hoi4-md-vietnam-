"""Paper transitions with observable outputs; this module does not install game code."""
from copy import deepcopy


def consume_node(p, state, node, option, object_id, epoch):
    """Consume a resolved record once at its real reader, granting actual PP/cash."""
    result=deepcopy(state)
    spec=p['node_opportunity_effects'][node]
    key=f'{node}/{object_id}/{epoch}'
    if result.get('records',{}).get(key)!=option:
        raise ValueError('Missing resolved record for this object and epoch')
    if key in result.get('cancelled_records',[]): raise ValueError('Cancelled work cannot receive a rebate')
    if spec['reader']=='archive_XV':
        return result
    if spec['reader'] not in result.get('completed_nodes',[]):
        raise ValueError('Reader is not completed')
    if key in result.get('consumed',[]): return result
    effect=spec[option]['effect']
    result['pp']=result.get('pp',0)+effect['pp']
    result['treasury']=result.get('treasury',0)+effect['treasury']
    result.setdefault('consumed',[]).append(key)
    return result


def resolve_choice(p, state, decision, option, object_id, epoch, roll=0):
    """Roll once per object/epoch; replay cannot reroll or charge again."""
    result=deepcopy(state);key=f'{decision}/{object_id}/{epoch}'
    if key in result.get('resolved',{}): return result
    if not 0<=roll<1: raise ValueError('Roll must be in [0,1)')
    choice=p['observable_choices'][decision][option]
    if decision=='XI09 / XI10' and key not in result.get('completed_evidence',[]):
        raise ValueError('Asset recovery requires completed project/restructuring evidence')
    if decision=='XIII12':
        from VIETNAM_POLITICAL_BALANCE_VI import e104_contract_amendment_gate,paper_cancel_e104_contract
        if 'contract' not in result: raise ValueError('No live E104 contract')
        if option=='A':
            if not result.get('partner_accepts') or not e104_contract_amendment_gate(result['contract'])['amend_available']:
                raise ValueError('Amendment requires remaining benefit and partner acceptance')
            contract=result['contract']
            contract.setdefault('check_history',[]).extend(contract.get('checks_paid',[]))
            contract['checks_paid']=[]
            contract['contract_state']='modified_active'
            contract['obligation_start_day']=result.get('day',0)
        else:
            result['contract']=paper_cancel_e104_contract(result['contract'])
    if result.get('pp',0)<choice['pp'] or result.get('treasury',0)<choice['treasury']:
        raise ValueError('Insufficient funds')
    if result.get('cohesion',60)-choice['cohesion']<40:
        raise ValueError('Cohesion would fall below 40')
    result['pp']-=choice['pp'];result['treasury']-=choice['treasury']
    result['cohesion']=result.get('cohesion',60)-choice['cohesion']
    cumulative=0
    for outcome in choice['outcomes']:
        cumulative+=outcome['probability']
        if roll<cumulative:
            result['pp']+=outcome.get('pp',0)
            result['treasury']+=outcome.get('treasury',0)
            result['cohesion']=min(100,max(0,result['cohesion']+outcome.get('cohesion',0)))
            for target,allowed in outcome.get('node_gates',{}).items():
                result.setdefault('node_gates',{})[target]=allowed
            result.setdefault('resolved',{})[key]={'option':option,'outcome':outcome['name'],'roll':roll}
            return result
    raise ValueError('Outcome probabilities must sum to 1')


def node_available(p, state, node):
    """A real reader: dynamic gates AND the normal prerequisite graph."""
    if node in state.get('completed_nodes',[]): return False
    gated={target for spec in p['observable_choices'].values() for option in 'AB'
           for outcome in spec[option]['outcomes'] for target in outcome.get('node_gates',{})}
    if node in gated and node not in state.get('node_gates',{}): return False
    if not state.get('node_gates',{}).get(node,True): return False
    parents=p['focus_prerequisites'].get(node,[])
    return not parents or any(parent in state.get('completed_nodes',[]) for parent in parents)


def advance_contract(p, ledger, day, fulfilled_checks, training_completed=False):
    """Two E104 checks charge PP once; unmet checks revoke unpaid support/unused access."""
    result=deepcopy(ledger);terms=p['contract_obligations']
    if result['contract_state']=='terminated': return result
    paid=result.setdefault('checks_paid',[])
    for due in terms['check_days']:
        if day<due or due in paid: continue
        if due not in fulfilled_checks:
            result['support_forfeited']+=max(0,result['support_promised']-result['support_received']-result['support_forfeited'])
            result['rights_revoked']=sorted(set(result['rights_revoked']) | (set(result['rights_granted'])-set(result['rights_used'])))
            result['cohesion']=max(0,result.get('cohesion',60)-terms['missed_cohesion'])
            result['contract_state']='terminated'
            return result
        if result.get('pp',0)<terms['pp_per_check']: raise ValueError('Insufficient PP for contract check')
        result['pp']-=terms['pp_per_check'];paid.append(due)
    if all(due in paid for due in terms['check_days']):
        result['support_received']=result['support_promised']-result['support_forfeited']
        if training_completed and day>=p['e104_training']['days'] and 'training' in set(result['rights_granted'])-set(result['rights_revoked'])-set(result['rights_used']):
            result['pp']+=p['e104_training']['reward_pp'];result['rights_used'].append('training')
    return result


def settle_contract(p,state,day,fulfilled_checks,training_completed=False):
    """Debit the state ledger and transfer support once, after actual checked evidence."""
    result=deepcopy(state);ledger=deepcopy(result['contract'])
    ledger['pp']=result['pp'];ledger['cohesion']=result['cohesion']
    after=advance_contract(p,ledger,day-ledger.get('obligation_start_day',0),fulfilled_checks,training_completed)
    result['pp']=after['pp'];result['cohesion']=after['cohesion']
    result['treasury']+=after['support_received']-ledger['support_received']
    result['contract']=after
    return result


def audit_consumers(p):
    errors=[];rows=[]
    for node,spec in p['node_opportunity_effects'].items():
        if spec['reader']=='archive_XV':
            for o in 'AB':
                if spec[o]['effect']!={'pp':0,'treasury':0}: errors.append(node+': archive reward')
            continue
        for option in 'AB':
            initial={'pp':0,'treasury':0,'completed_nodes':[spec['reader']], 'records':{f'{node}/obj/1':option}}
            result=consume_node(p,initial,node,option,'obj',1)
            if result==initial or consume_node(p,result,node,option,'obj',1)!=result: errors.append(node+option+': missing effect/replay')
            for wrong in [('other',1),('obj',2)]:
                try: consume_node(p,initial,node,option,*wrong);errors.append(node+': cross-object/epoch')
                except ValueError: pass
            try:
                consume_node(p,{**initial,'cancelled_records':[f'{node}/obj/1']},node,option,'obj',1)
                errors.append(node+': cancelled rebate')
            except ValueError: pass
    for decision,spec in p['observable_choices'].items():
        for option in 'AB':
            if abs(sum(o['probability'] for o in spec[option]['outcomes'])-1)>1e-9: errors.append(decision+': probability')
            cumulative=0
            for outcome in spec[option]['outcomes']:
                roll=cumulative+outcome['probability']/2;cumulative+=outcome['probability']
                before={'pp':100,'treasury':2,'cohesion':60,'completed_nodes':list(p['focus_nodes']),
                    'completed_evidence':[f'{decision}/obj/1'],'partner_accepts':True,'contract':{'support_promised':.75,'support_received':0,'support_forfeited':0,
                    'rights_granted':['training'],'rights_used':[],'rights_revoked':[],'contract_state':'accepted'}}
                # Open a consumer node that is not already completed in this fixture.
                before['completed_nodes']=[n for n in before['completed_nodes'] if n not in outcome.get('node_gates',{})]
                after=resolve_choice(p,before,decision,option,'obj',1,roll)
                if decision=='XI09 / XI10':
                    try:
                        resolve_choice(p,{**before,'completed_evidence':[]},decision,option,'obj',1,roll)
                        errors.append('asset recovery without evidence')
                    except ValueError: pass
                if resolve_choice(p,after,decision,option,'obj',1,0.999)!=after: errors.append(decision+': reroll')
                for target,allowed in outcome.get('node_gates',{}).items():
                    if target not in p['focus_nodes'] or node_available(p,after,target)!=allowed: errors.append(decision+': dead gate '+target)
                for k in p['k_values']:
                    cost=(before['pp']-after['pp'])+(before['treasury']-after['treasury'])*k+(before['cohesion']-after['cohesion'])*p['cohesion_pp_rate']
                    rows.append({'node':decision,'option':option,'outcome':outcome['name'],'probability':outcome['probability'],'k':k,
                        'converted_cost':round(cost,6),'pp_delta':after['pp']-before['pp'],'treasury_delta':after['treasury']-before['treasury'],
                        'cohesion_delta':after['cohesion']-before['cohesion'],'node_gates':str(outcome.get('node_gates',{})),
                        'scope':'observable_outcome_not_engine'})
    ledger={'pp':100,'cohesion':60,'support_promised':0.75,'support_received':0,'support_forfeited':0,
        'rights_granted':['training'],'rights_used':[],'rights_revoked':[],'contract_state':'accepted'}
    fulfilled=advance_contract(p,ledger,180,[90,180],True);failed=advance_contract(p,ledger,90,[])
    if fulfilled['pp']!=100-2*p['contract_obligations']['pp_per_check']+p['e104_training']['reward_pp'] or fulfilled['support_received']!=0.75: errors.append('contract: missing settlement')
    if advance_contract(p,fulfilled,180,[90,180],True)!=fulfilled: errors.append('contract: double reward')
    no_training=advance_contract(p,ledger,180,[90,180])
    if no_training['pp']!=80 or no_training['rights_used']: errors.append('training: free reward without evidence')
    if failed['contract_state']!='terminated' or failed['support_forfeited']!=0.75 or failed['cohesion']!=54: errors.append('contract: missing failure')
    state={'pp':100,'treasury':0,'cohesion':60,'contract':ledger,'partner_accepts':True}
    amended=resolve_choice(p,state,'XIII12','A','obj',1)
    settled=settle_contract(p,amended,180,[90,180],True)
    if settled['pp']!=105 or settled['treasury']!=.75 or settle_contract(p,settled,180,[90,180],True)!=settled: errors.append('contract: missing real debit/payment or replay')
    cancelled=resolve_choice(p,state,'XIII12','B','obj',1)
    if settle_contract(p,cancelled,180,[90,180],True)['treasury']!=0 or cancelled['contract']['support_forfeited']!=.75: errors.append('contract: cancellation still pays')
    try:
        resolve_choice(p,{**state,'partner_accepts':False},'XIII12','A','obj',1)
        errors.append('contract: ignored rejection')
    except ValueError: pass
    varied={node for spec in p['observable_choices'].values() for node in spec['nodes']}
    if varied!=set(p['observable_choices']['IX11 / IX12']['nodes']+p['observable_choices']['XI09 / XI10']['nodes']+['X01','XII02','XII12','XIII12']): errors.append('eight-node scope')
    return rows,errors


def choice_design_text(p):
    from VIETNAM_POLITICAL_BALANCE_VI import table
    rows=[]
    for node,spec in p['observable_choices'].items():
        for label in 'AB':
            option=spec[label];outcomes=[]
            for result in option['outcomes']:
                effect=[f"PP{result.get('pp',0):+g}",f"ngân khố{result.get('treasury',0):+g}",f"cohesion{result.get('cohesion',0):+g}"]
                effect += [('mở ' if allowed else 'khóa ')+target for target,allowed in result.get('node_gates',{}).items()]
                outcomes.append(f"{result['probability']*100:g}% {result['name']}: "+', '.join(effect))
            rows.append([node,label,f"{option['pp']}PP +{option['treasury']}ngân khố +{option['cohesion']}cohesion",'; '.join(outcomes)])
    text='### 7.4a. Tác dụng có giá và tám node đổi cấu trúc\n\n'
    text+='Nguồn thực thi mô hình giấy: [consumer](VIETNAM_POLITICAL_CONSUMERS_VI.py). Các tỷ lệ65/35 và70/30 là giả định gameplay. RNG lấy một lần khi giải quyết hồ sơ, lưu theo node/đối tượng/epoch; load/replay không reroll hoặc thu lại phí. Thu hồi tài sản yêu cầu chứng cứ dự án/tái cơ cấu đã hoàn tất. Thất bại là kết quả có tác dụng, không phải option biết trước sẽ thua.\n\n'
    text+=table(['Node/nhánh','Option','Chi lúc chọn','Kết quả quan sát được'],rows)
    text+='\n\nXII12-A giữ bàn giao60ngày nhưng khóa XII09 trong kỳ; B mở XII09 ngay. Node XII09 cần cả prerequisite cũ và gate này. X01 đọc tại XI05; XII02 đọc tại XIII09; XIII12 đọc tại XIV11. Gate mặc định đóng trước khi có record và được AND với prerequisite; không bỏ qua kỳ/ngày/đối tượng. Nhánh khóa không cho chọn node rồi mới fail. Một node đã hoàn thành không nhận lại reward từ gate.\n\n'
    text+='### 7.4b. Hoàn trả công việc và nghĩa vụ hợp đồng\n\n'
    text+='Các consumer còn lại hoàn trả chi phí tái sử dụng hồ sơ: A +8PP, B +0.20ngân khố khi reader hoàn thành trên cùng hồ sơ/source epoch; phí mở hồ sơ vẫn trả trước. Không nhận reader hoặc chưa đủ chứng cứ thì chưa hoàn trả. Archive XIV→XV chỉ lưu, thưởng0. Guard lưu consumed; hủy hoặc đọc sai đối tượng/epoch không tạo khoản hoàn trả. Các khoản này là giả định gameplay, không phải điểm cơ hội.\n\n'
    rebate=[]
    for node,spec in p['node_opportunity_effects'].items():
        rebate.append([node,spec['reader'],spec['A']['effect']['pp'],spec['B']['effect']['treasury']])
    text+=table(['Writer','Reader','A: PP hoàn trả','B: ngân khố hoàn trả'],rebate)
    text+='\n\nE102-A mở E104 theo hồ sơ công khai thật. Đào tạo E104 là task90ngày, cùng đối tượng/epoch, không có phí riêng; nhận25PP sau chứng cứ hoàn thành và hai kỳ kiểm tra hợp đồng. Cột training_reward_if_completed_pp chỉ là kết quả nếu thực hiện task, không cộng vào pp_net_cost trước khi hoàn tất và không dùng trong Pareto programme. Hủy hoặc thiếu kiểm tra thu hồi quyền chưa dùng; không thu hồi PP đã nhận.\n\n'
    text+='XIII12 sửa giữ hợp đồng phải kiểm hồ sơ sau90và180ngày tính từ lần sửa; mỗi lần10PP. Qua cả hai mới nhận phần hỗ trợ chưa thanh toán. Thiếu một lần: chấm dứt nghĩa vụ tương lai, mất hỗ trợ chưa nhận/quyền đào tạo chưa dùng và cohesion−6 đúng một lần. Hủy đóng nghĩa vụ ngay, mất hỗ trợ chưa nhận, khóa XIV11 cho hợp đồng này; không trừ ngân khố bằng khoản hỗ trợ chưa nhận và không thu hồi lịch sử. Nếu không còn lợi ích thì sửa bị khóa; đối tác phải chấp nhận sửa. Các chi phí tương lai chỉ ghi khi còn chưa trả, không thu hai lần khi sửa/timeout/load.\n\n'
    text+='I3 chỉ báo REVIEW: kiểm được giao dịch, gate và kết quả hai nhánh, nhưng không tuyên bố mọi chiều sở thích hoặc thời gian có tỷ giá PP. So tiền trực tiếp vẫn chỉ rõ các phương án rẻ hơn; không dùng tên hành động hoặc cờ nghĩa vụ để đổi FAIL thành PASS.\n\n'
    return text
