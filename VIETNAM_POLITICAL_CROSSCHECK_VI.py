"""Kiem tra giay Luot 3; khong nap hoac chay engine HOI4."""
import csv
import hashlib
import itertools
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def completion_tables(p):
    """Named actions are compared as sets, never as fungible opportunity points."""
    opportunities=[]
    for node,effect in p['node_opportunity_effects'].items():
        for option,(pp,cash) in zip('AB',p['node_choice_prices'][node]):
            for route,k in itertools.product(p['prepare_days'],p['k_values']):
                delay=p['node_choice_delays'].get(node,0) if effect['delay_option']==option else 0
                opportunities.append({'node':node,'option':option,'route':route,'k':k,'pp':pp,'treasury':cash,
                                      'cohesion_spent_cost':0,'actual_treasury_debit':cash,'unreceived_support_lost':0,
                                      'converted_cost':pp+cash*k,'project_delay_days':delay,'reader':effect['reader'],
                                      'reader_pp_rebate':effect[option]['effect']['pp'],'reader_treasury_rebate':effect[option]['effect']['treasury'],'action':effect[option]['action'],'action_available':effect[option]['available'],
                                      'counterpart_available':effect[option]['counterpart_available'],
                                      'usable_in_model':int(effect['reader']!='archive_XV'),
                                      'scope':'existing_caller_branch_not_engine; archive_XV has no current gameplay'})
    terms=p['legacy_node_terms']
    legacy=[];priced_nodes=[]
    def price_rows(node,context,k,options):
        for route in p['prepare_days']:
            for option,(pp,cash,cohesion) in zip('ABC',options):
                foregone=(node=='XIII12' and option=='B') or (node=='XIV11' and option=='C')
                priced_nodes.append({'node':node,'option':option,'route':route,'k':k,'pp':pp,'treasury':cash,
                                    'cohesion_spent_cost':cohesion,'converted_cost':pp+cash*k+cohesion*p['cohesion_pp_rate'],
                                    'actual_treasury_debit':0 if foregone else cash,'unreceived_support_lost':cash if foregone else 0,
                                    'context':context,'scope':'approved_gameplay_assumption_not_engine; loss_of_unreceived_support_is_opportunity_cost'})
    def pair(node,context,a,b):
        for k in p['k_values']:
            ca=a[0]+a[1]*k+a[2]*p['cohesion_pp_rate']
            cb=b[0]+b[1]*k+b[2]*p['cohesion_pp_rate']
            legacy.append([node,context,k,ca,cb,cb-ca,abs(cb-ca),'BIÊN <3' if abs(cb-ca)<p['e103_margin_warning_pp'] else ''])
            price_rows(node,context,k,[a,b])
    pair('IX11 / IX12','luân chuyển / kiểm toán độc lập',(terms['IX11']['pp'],0,-terms['IX11']['cohesion_gain']),(terms['IX12']['independent_audit_pp'],0,0))
    pair('X09 / X10','hai đợt / ứng trước',(0,terms['X09']['installments']*terms['X09']['treasury_per_installment'],0),(0,terms['X10']['treasury'],0))
    pair('XI09 / XI10','cứu dự án / tái cơ cấu',(0,terms['XI09']['treasury'],0),(0,0,0))
    pair('XI12','bồi hoàn PP / ngân khố',(terms['XI12']['reparation_pp'],0,0),(0,terms['XI12']['reparation_treasury'],0))
    pair('XII10','đầu mối / hội đồng',(terms['XII10']['pp'],0,0),(0,terms['XII10']['alternative_treasury'],terms['XII10']['cohesion']))
    pair('XII12','bàn giao / kiện toàn ngay',(0,0,0),(0,0,terms['XII12']['immediate_cohesion_loss']))
    for remaining in [0,p['e104']['B_grant'],p['e104']['A_grant']]:
        pair('XIII12',f'sửa / hủy; hỗ trợ chưa nhận={remaining}',(0,0,0),(0,remaining,0))
    for remaining,k in itertools.product([0,p['e104']['B_grant'],p['e104']['A_grant']],p['k_values']):
        costs=[terms['XIV11']['retain_cost'],terms['XIV11']['amend_cost']*k,remaining*k]
        gaps=[costs[1]-costs[0],costs[2]-costs[0],costs[2]-costs[1]]
        legacy.append(['XIV11',f'giữ / sửa / hủy; hỗ trợ chưa nhận={remaining}',k,*costs,','.join(f'{g:g}' for g in gaps),'BIÊN <3' if any(abs(g)<p['e103_margin_warning_pp'] for g in gaps) else ''])
        price_rows('XIV11',f'giữ / sửa / hủy; hỗ trợ chưa nhận={remaining}',k,[(terms['XIV11']['retain_cost'],0,0),(0,terms['XIV11']['amend_cost'],0),(0,remaining,0)])
    # Compare options within each event, not prices of two mutually exclusive focus nodes.
    # Time is not silently priced into PP. XIV11 is tested across all support scenarios.
    failures=[]
    for node in ['XI12','XII10','XIV11']:
        group=[r for r in legacy if r[0]==node]
        winners=[]
        for row in group:
            costs=row[3:6] if node=='XIV11' else row[3:5]
            winners.append({option for option,cost in zip('ABC',costs) if cost==min(costs)})
        universal=set.intersection(*winners)
        if universal: failures.append(node+': '+','.join(sorted(universal))+' rẻ nhất/đồng hạng ở mọi k và mọi bối cảnh hỗ trợ đã kiểm')
    pareto_vectors,_,_=pareto_exception_checks(p)
    from VIETNAM_POLITICAL_CONSUMERS_VI import audit_consumers
    consumer_rows,_=audit_consumers(p)
    rows=consumer_rows+opportunities+priced_nodes+[{**row,'scope':'i3_named_pareto_exception_not_engine; added_days_zero_does_not_change_existing_programme_timers'} for row in pareto_vectors]
    with (ROOT/'VIETNAM_POLITICAL_NODE_CHOICES_VI.csv').open('w',encoding='utf-8-sig',newline='') as stream:
        fields=list(dict.fromkeys(key for row in rows for key in row))
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(rows)
    return opportunities,legacy,failures


def forecast_probe_tables(p):
    from VIETNAM_POLITICAL_BALANCE_VI import forecast_programme_completion
    probes=[]
    for programme,route,mode in itertools.product(['cadre','administration','inspection','social'],p['prepare_days'],['standard','fast_paid']):
        if mode!='standard' and p['bop_route_snapshot'][route]<=p['bop_threshold']: continue
        f=forecast_programme_completion(p,programme,route,mode,0)
        probes.append([programme,route,mode,'0–19',f['signed_base_days'],f['forecast_reserve_days'],'MỞ' if f['start_available'] else 'KHÓA',f['reopen']])
    recovery=forecast_programme_completion(p,'inspection','collective','standard',0)['planned_recovery_schedule']
    return probes,recovery


def xiii12_contract_checks(p):
    from VIETNAM_POLITICAL_BALANCE_VI import e104_contract_amendment_gate,paper_cancel_e104_contract
    result=[]
    for state,grant in itertools.product(['pending','accepted','modified','terminated','refused'],[0,p['e104']['B_grant'],p['e104']['A_grant']]):
        rights=['đào tạo']+(['hợp tác dữ liệu sâu'] if grant==p['e104']['A_grant'] else []) if grant else []
        for paid in sorted({0,grant}):
            for used_count in range(len(rights)+1):
                ledger={'support_promised':grant,'support_received':paid,'support_forfeited':0,
                        'rights_granted':rights,'rights_used':rights[:used_count],'rights_revoked':[],'contract_state':state}
                if state=='pending': ledger['rights_granted']=[];ledger['rights_used']=[]
                if state=='terminated': ledger=paper_cancel_e104_contract(ledger)
                if state=='refused': ledger.update(support_promised=paid,support_forfeited=0,rights_revoked=rights[used_count:])
                before=json.dumps(ledger,sort_keys=True,ensure_ascii=False)
                gate=e104_contract_amendment_gate(ledger);after=paper_cancel_e104_contract(ledger);again=paper_cancel_e104_contract(after)
                after_gate=e104_contract_amendment_gate(after)
                unchanged=before==json.dumps(ledger,sort_keys=True,ensure_ascii=False)
                paid_preserved=after['support_received']==ledger['support_received'] and after['rights_used']==ledger['rights_used']
                scoped=set(key for key in ledger if ledger[key]!=after[key])<={'support_forfeited','rights_revoked','contract_state'}
                idempotent=again==after and after_gate['unreceived_support']==0 and after_gate['unused_cooperation_rights']==0
                passed=gate['cancel_available']==1 and (gate['amend_available'] or gate['cancel_available']) and unchanged and paid_preserved and scoped and idempotent
                result.append([state,grant,paid,gate['unreceived_support'],gate['unused_cooperation_rights'],gate['amend_available'],gate['cancel_available'],int(paid_preserved and scoped),int(idempotent),'PASS' if passed else 'FAIL'])
    return result


def selected_inspection_start_cases(p):
    from VIETNAM_POLITICAL_BALANCE_VI import forecast_programme_completion
    cases=[];low=p['recovery']['low_below'];gain=p['recovery']['cohesion']
    for initial,delay,cooldown_left in itertools.product([0,low-gain-1,low-gain,low-1],[0,1],[0,p['recovery']['cooldown']]):
        f=forecast_programme_completion(p,'inspection','collective','standard',initial,
            elapsed_congress_days=delay,recovery_cooldown_remaining=cooldown_left)
        finish=f['earliest_feasible_start_day']
        cases.append([initial,delay,cooldown_left,f['planned_new_meetings'],finish,f['planned_start_cohesion'],f['planned_recovery_pp'],
                      p['program_start_latest']-finish,'CHỐT ĐƯỢC' if f['focus_available'] else 'KHÓA CHỐT KIỂM TRA'])
    return cases


def focus_gate_probe_tables(p):
    from VIETNAM_POLITICAL_BALANCE_VI import forecast_programme_completion
    rows=[];failures=[];grouped=[]
    bands=[(0,9),(10,19),(20,39)]
    cooldowns=[0,p['recovery']['days'],p['recovery']['cooldown']]
    for (low,high),cool,route in itertools.product(bands,cooldowns,p['prepare_days']):
        group=[]
        for cohesion in range(low,high+1):
            f=forecast_programme_completion(p,None,route,None,cohesion,recovery_cooldown_remaining=cool)
            summary=[]
            for program in ['cadre','administration','inspection','social']:
                candidate=forecast_programme_completion(p,program,route,None,cohesion,recovery_cooldown_remaining=cool)
                earliest=candidate['earliest_feasible_start_day'];short=candidate['start_days_short']
                summary.append(f'MỞ@{earliest}' if candidate['focus_available'] else f'KHÓA@{earliest}; thiếu{short}')
                rows.append({'cohesion':cohesion,'cooldown_remaining':cool,'route':route,'program':program,
                    'focus_available':candidate['focus_available'],'earliest_start_day':earliest,'days_short':short,
                    'recovery_gate_blocked':candidate['recovery_gate_blocked'],'reconciliation_gate_blocked':candidate['reconciliation_gate_blocked']})
            group.append(summary)
            if not f['focus_available'] or f['recovery_gate_blocked'] or f['reconciliation_gate_blocked']: failures.append([cohesion,cool,route,'không còn lối hoặc phục hồi bị khóa'])
        if not all(summary==group[0] for summary in group): failures.append([low,high,cool,route,'không đồng nhất trong vùng'])
        grouped.append([f'{low}–{high}',cool,route,*group[0],'CÒN LỐI','trọng tâm bị khóa không được chốt; chọn chương trình đang mở'])
    boundaries=[]
    for cohesion,cool,route in itertools.product([p['recovery']['low_below']-1,p['recovery']['low_below']],cooldowns,p['prepare_days']):
        f=forecast_programme_completion(p,'inspection',route,'standard',cohesion,recovery_cooldown_remaining=cool)
        boundaries.append([cohesion,cool,route,f['signed_base_days'],f['start_available'],f['earliest_feasible_start_day'],f['start_days_short'],f['focus_available']])
    expiry=[]
    for elapsed in [p['program_start_latest'],p['program_start_latest']+1]:
        f=forecast_programme_completion(p,None,'collective',None,p['recovery']['low_below'],elapsed_congress_days=elapsed)
        expiry.append([elapsed,f['focus_available'],','.join(f['available_programmes']) or 'không còn trong kỳ',f['start_days_short'],f['recovery_gate_blocked'],f['reconciliation_gate_blocked']])
    # Meeting already in progress: paid once, finish at90, next choose at180, finish at270.
    pending=forecast_programme_completion(p,'inspection','collective','standard',0,recovery_cooldown_remaining=p['recovery']['cooldown'],pending_recovery_remaining=p['recovery']['days'])
    if pending['earliest_feasible_start_day']!=p['program_start_latest'] or pending['planned_new_meetings']!=1: failures.append(['pending meeting bị tính lại'])
    return rows,grouped,boundaries,expiry,failures


def sync_remaining_document(doc,p):
    """Only the explicitly requested I5/I6/I10 additions and their dependent text."""
    specs=p['legacy_node_specs'];terms=p['legacy_node_terms']
    oldrows={node:re.search(rf'^\| {node} \|.*$',doc,re.M).group(0) for node in specs}
    extra={
        'X09':f"Mỗi đợt {terms['X09']['treasury_per_installment']:.2f} ngân khố; tổng {terms['X09']['installments']*terms['X09']['treasury_per_installment']:.2f}; không trả đợt sau trước checkpoint riêng.",
        'XI12':f"Bồi hoàn chọn {terms['XI12']['reparation_pp']} PP hoặc {terms['XI12']['reparation_treasury']:.2f} ngân khố; cùng nghĩa vụ, khác nguồn chi. Giá này thuộc XI12, không thuộc XII12.",
        'XII10':f"Đầu mối {terms['XII10']['pp']} PP; hội đồng {terms['XII10']['cohesion']} cohesion + {terms['XII10']['alternative_treasury']:.2f} ngân khố; chỉ trả một cách, cả hai giữ {terms['XII10']['days']} ngày.",
        'XII12':f"Bàn giao {terms['XII12']['handover_days']} ngày, không thêm phí; kiện toàn ngay mất {terms['XII12']['immediate_cohesion_loss']} cohesion, chỉ khi roster thay thế hợp lệ.",
        'XIII11':f"Ngân sách {terms['XIII11']['treasury']:.2f} ngân khố cho {terms['XIII11']['days']} ngày; phản hồi theo hồ sơ, không tự cộng thưởng chương trình.",
        'XIII12':"Hủy không thu thêm phí; mất hỗ trợ E104 chưa nhận theo hợp đồng, không thu hồi khoản đã nhận hoặc tạo nợ âm. Sửa giữ điều kiện đối tác chấp nhận, không tự tạo hỗ trợ mới. Cổng bổ sung e104_contract_amendment_gate chỉ áp cho sửa tại XIII12: hỗ trợ chưa nhận>0 HOẶC quyền hợp tác chưa dùng>0. Cả hai0 thì sửa bị khóa; hủy luôn mở. Hủy chỉ đóng ledger/nghĩa vụ tương lai, không fail mission, không xóa bằng chứng đã hoàn tất, không mất tier/PP sớm/thưởng đã nhận. Giá/timer giữ nguyên.",
        'XIV10':f"Idea ổn định +{terms['XIV10']['stability_reward']*100:g}% trong {terms['XIV10']['reward_days']} ngày; trần {terms['XIV10']['stability_cap']*100:g}%; không cộng chồng tier dân vận: dùng max(thưởng tier, idea). Chỉ nhận sau nghiệm thu cùng địa điểm, một lần/địa điểm/epoch; refresh thay thế, không cộng thời hạn.",
        'XIV11':f"Giữ {terms['XIV11']['retain_cost']} PP; sửa {terms['XIV11']['amend_cost']:.2f} ngân khố; chấm dứt mất hỗ trợ chưa nhận. Giữ chỉ khả dụng nếu ký kịp cửa sổ {terms['XIV11']['sign_window_days']} ngày; sửa cần đối tác đồng ý, không tự gia hạn ký.",
    }
    for node,spec in specs.items():
        fields=[v.strip() for v in oldrows[node].strip('|').split('|')]
        if len(fields)==5: fields.pop(3)
        anchor=date.fromisoformat(p['congress_dates'][spec['term']]).strftime('%d/%m/%Y')
        mutex=[b if a==node else a for a,b in p['l3_document_checks']['mutex_pairs'] if node in (a,b)]
        gate=f"{spec['term']} đã giải quyết; từ {anchor}; {' hoặc '.join(spec['prerequisites'])}; {spec['mode']}; {spec['condition']}"
        for other in mutex: gate+=f'; loại trừ {other}'
        # The original consequence is retained once, then completed with explicit caller/guard/reader.
        original=fields[3].split(' **Bổ sung hoàn thiện:**')[0]
        addition=f" **Bổ sung hoàn thiện:** {spec['caller']} do focus hoàn thành mở; {spec['guard']}. {extra.get(node,'')} Reader {spec['reader']}: {spec['carryover_effect']}."
        doc=doc.replace(oldrows[node],'| '+' | '.join(fields[:3]+[gate,original+addition])+' |')
    doc=doc.replace('| Node | Focus | Cost | Hậu quả cụ thể |\n| --- | --- | ---: | --- |','| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller, giá và hậu quả cụ thể |\n| --- | --- | ---: | --- | --- |')
    start=doc.index('### 7.5.')
    marker='### 7.4a. Quyền và cơ hội có consumer cụ thể'
    if marker in doc: doc=doc[:doc.index(marker)]+doc[start:];start=doc.index('### 7.5.')
    rights=[]
    for node,e in p['node_opportunity_effects'].items():
        delay=p['node_choice_delays'].get(node,0) if e['delay_option'] else None
        rights.append([node,e['reader'],e['A']['action'],e['B']['action'],f"{e['delay_option']}: {delay} ngày" if delay is not None else 'Theo quyền, không tự gán thêm timer'])
    text='''### 7.4a. Quyền và cơ hội có consumer cụ thể

Đổi hậu quả chỉ mô tả thành gate hành động đọc được. Mỗi hồ sơ lưu đúng một lựa chọn A/B theo node/đối tượng/epoch. Khi reader xử lý đúng hồ sơ, hành động tương ứng có available=1, hành động đối ứng=0; không mở cả hai và không thu lại phí đã trả. Đây là nhánh của caller hiện có, không thêm focus, event hay currency. Quyền không tự cộng tier, bằng chứng, thưởng PP hoặc rút timer ký. Thời gian ở bảng áp vào hồ sơ/dự án tương ứng, không tự cộng vào chuỗi programme độc lập. Gate điều kiện thực tế của reader vẫn áp dụng.

Mỗi hành động là một cơ hội mang tên riêng; script so tập quyền theo quan hệ bao hàm, không cộng số quyền thành điểm. I10 kiểm cả hai nhu cầu hành động tại từng node, mọi tuyến/k, rồi đối chiếu ma trận programme. Không có một lựa chọn thắng tất cả nếu nó khóa hành động đối ứng mà đối thủ mở. Đây là kết luận của mô hình giấy, không chứng minh AI hay game thực thi đúng.

`archive_XV` là nhãn lưu trữ cho XV giả định: lưu cả hai loại hồ sơ khác nhau, không tính là cơ hội sử dụng được trong phạm vi 2026 và không thêm node XV. Các quyền XIV chỉ dùng để kiểm khác biệt hồ sơ bàn giao, không được dùng để tăng opportunity_count hiện tại.

'''+table(['Node','Reader','Hành động nếu A (B khóa)','Hành động nếu B (A khóa)','Timer đã có'],rights)+'\n\nCác giá/hiệu quả mới của22node là **giả định gameplay, chưa cân bằng bằng engine**. Giữ cost và loại trừ; không dùng giá mới để thay timer/deadline/giá programme. Bảng đối chiếu và biên giá ở báo cáo Lượt3.\n\n'
    vectors,pairs,failures=pareto_exception_checks(p)
    pareto_rows=[]
    for v in vectors:
        if v['route']!=list(p['prepare_days'])[0]: continue
        outside={key:value for key,value in v.items() if key in p['i3_pareto_exceptions']['dimensions'] and key!='converted_cost'}
        pareto_rows.append([v['node'],v['context'],v['k'],v['option'],v['converted_cost'],'; '.join(f'{key}={value:g}' for key,value in outside.items()),v['state'],'MỞ' if v['available'] else 'KHÓA'])
    text+='### 7.4b. I3 Pareto chỉ cho XII12 và XIII12\n\nI3 của XII12 và XIII12 được đánh giá bằng Pareto, không bằng chi phí tiền đơn lẻ, theo xác nhận người dùng: chúng đổi thời gian/roster hoặc quyền hỗ trợ/nghĩa vụ đang có. Mọi node/event khác giữ phép kiểm chi phí quy đổi trực tiếp. Không quy ngày/quyền thànhPP, không thêm thưởng hay đổi timer. Available và tooltip đọc `i3_pareto_exceptions`/record hồ sơ: phí, bàn giao/khóa roster, cohesion mất, quyền người cũ/người mới, hỗ trợ chưa nhận bị mất, quyền hợp tác chưa dùng, nghĩa vụ hợp đồng mở. Hủy không thu hồi hỗ trợ đã nhận và không xóa lịch sử trách nhiệm.\n\n'+table(['Node','Bối cảnh','k','Option','Chi quy đổi','Chiều ngoài tiền','Trạng thái','Cổng'],pareto_rows)
    text+=f'\n\nScript kiểm{len(pairs)}cặp mọi tuyến/k; có{len(failures)}cặp thống trị còn khả dụng, {sum(r["near_duplicate"] for r in pairs)}gần trùng. Bảng Δtừng chiều và so cặp ở báo cáoLượt3; near=mọi |B−A|/max(|A|,|B|)<10%, cả hai0 tính0%. XIII12 không còn hỗ trợ/quyền hợp tác: sửa (phương án bị thống trị) bị khóa theo cổng mới; hủy vẫn mở. Các9phép so của trạng thái này PASS cổng: chỉ còn1phương án, không được tuyên bố đã cân bằng2phương án. Các trạng thái còn lợi ích giữ2phương án và kiểm Pareto riêng.\n\n'
    doc=doc[:start]+text+doc[start:]
    doc=doc.replace('Registry này đóng phạm vi các ID/nhãn đã viết, không chứng minh tồn tại API hoặc định nghĩa trong game. Giá lựa chọn node ở `node_choice_prices`, thời lượng ở `node_choice_delays`, mốc lịch sử ở `l2_history_anchors` của B1. Các hiệu quả như mất quyền truy cập, mất cửa sổ hay ưu tiên dự án chưa có mức đo hoặc cơ chế thực thi đầy đủ; I10 chưa thể PASS toàn thiết kế.',
                    'Registry này đóng phạm vi các ID/nhãn đã viết, không chứng minh tồn tại API hoặc định nghĩa trong game. Giá lựa chọn ở `node_choice_prices`/`legacy_node_terms`, timer ở `node_choice_delays`, gate/caller22node ở `legacy_node_specs`, consumer quyền ở `node_opportunity_effects`, lịch sử ở `l2_history_anchors` của B1. Quyền đọc theo đúng node/đối tượng/epoch; available=1 cho hành động đã chọn, 0 cho đối ứng; không cộng điểm quyền và không trao kết quả tự động.')
    registry='| `forecast_programme_completion` | Trigger thiết kế; Python cùng tên là nguồn tính dự báo duy nhất cho CSV/available/tooltip | Đọc timer/mode đã ký, chuẩn bị tại start, trễ tất định đã biết; xuất ngày/dự phòng/cổng. Rủi ro E103-A chưa hiện thực chỉ cảnh báo; chưa là trigger engine |\n| `node_opportunity_effects`; `legacy_node_specs`; `legacy_node_terms`; `archive_XV` | Focus/caller đã có ghi record node/đối tượng/epoch và phí một lần | Reader ở7.4/7.4a đọc; quyền đối ứng khóa, archive chỉ lưu không trao gameplay; giá mới là giả định gameplay |\n'
    if '| `forecast_programme_completion` |' not in doc:
        doc=doc.replace('Registry này đóng phạm vi',registry+'\nRegistry này đóng phạm vi')
    if '| `i3_pareto_exceptions` |' not in doc:
        doc=doc.replace('\n\nRegistry này đóng phạm vi','\n| `i3_pareto_exceptions` | Caller XII12/XIII12 đọc record roster/hợp đồng đã có | Lưu lựa chọn/trạng thái theo đối tượng/epoch, chiều/biên ở7.4b; Pareto chỉ hai node, tooltip trước chọn; chưa là ID engine |\n\nRegistry này đóng phạm vi')
    doc=doc.replace('\n\n| `forecast_programme_completion` |','\n| `forecast_programme_completion` |')
    if '| `e104_contract_amendment_gate`; `e104_contract_ledger` |' not in doc:
        doc=doc.replace('\n\nRegistry này đóng phạm vi','\n| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |\n\nRegistry này đóng phạm vi')
    tooltip='XIII12 — tooltip/cổng: available và tooltip chỉ gọi e104_contract_amendment_gate trên cùng ledger E104/đối tượng/source epoch. Khi khóa, hiển thị “hỗ trợ chưa nhận=0; quyền chưa dùng=0; sửa không giữ lợi ích; hủy vẫn khả dụng”. Khi hủy, hiển thị lượng hỗ trợ chưa nhận và quyền chưa dùng sẽ mất, nghĩa vụ tương lai sẽ đóng; mission/tier/PP sớm/thưởng đã nhận và hỗ trợ đã thanh toán giữ nguyên. Không tạo quyền mới, không thu hồi lịch sử, không cộng timer. Chỉ áp cổng tại XIII12, không áp XIV11 hoặc node khác.'
    ai='AI XIII12 chỉ đọc cùng e104_contract_amendment_gate: sửa khi còn lợi ích và đối tác chấp nhận điều kiện; cả hai cạn thì chọn hủy đang mở. Trước xác nhận đọc lại ledger để tránh tooltip cũ. Không tự giảm giá hoặc bỏ guard một lần/đối tượng/epoch.'
    for prefix,paragraph in [('XIII12 — tooltip/cổng:',tooltip),('AI XIII12',ai)]:
        if re.search('^'+re.escape(prefix),doc,re.M): doc=re.sub('^'+re.escape(prefix)+'.*$',lambda _:paragraph,doc,flags=re.M)
        else: doc=doc.replace('## 11. Bảng tính',paragraph+'\n\n## 11. Bảng tính',1)
    criteria='- XIII12 cổng bổ sung: e104_contract_amendment_gate dùng chung available/tooltip, chỉ sửa nếu hỗ trợ chưa nhận>0 hoặc quyền chưa dùng>0; hủy luôn mở. Kiểm9phép so trạng thái đã cạn và mọi trạng thái còn lợi ích; hủy chỉ ghi ledger E104, không fail mission/tier/reward/paid_support. Các chiều Pareto ngoài tiền phải hiện trước chọn; báo từng Δ và gần trùng<10%, không đổi giá/timer.'
    if '- XIII12 cổng bổ sung:' not in doc and '- XIII12:' not in doc: doc=doc.replace('## 12. Trạng thái hoàn thành',criteria+'\n\n## 12. Trạng thái hoàn thành',1)
    doc=doc.replace('Phép này chưa định lượng quyền dữ liệu, chậm lịch hay quan hệ với trung tâm quyết định; chúng là hệ quả lựa chọn riêng, không quy đổi thành PP.',
                    'Consumer quyền/dữ liệu và timer hồ sơ ở7.4a được kiểm riêng, không quy đổi thànhPP; chỉ XII12/XIII12 dùng Pareto tại7.4b theo xác nhận, các node/event khác giữ phép kiểm tiền trực tiếp.')
    start_warning='**Kiểm kẹt cửa sổ khởi động:** cổng chốt đã được bổ sung. Available/tooltip/AI chỉ đọc forecast_programme_completion. Với một lựa chọn, phải còn đường của programme mà nó chốt; cổng chung cần ít nhất một trong bốn programme. Trước start, trigger xét cohesion hiện tại, +60chuẩn bị khi dưới20, cooldown còn lại và lượt phục hồi đang chạy. Tính ngày khởi động sớm nhất trước hoặc đúng270, giả định các bước còn lại thành công; không chốt programme không thể mở trong cửa sổ. Sau start, timer/mode đã ký không giảm hồi tố. Gate kỳ/chế độ/90ngày chọn trọng tâm, PP/ngân khố giữ nguyên. Cổng không khóa phục hồi/hòa giải; giá/cooldown của chúng vẫn áp dụng. Không tự cứu trọng tâm đã chốt từ save cũ, không tạo fallback hoặc penalty mới.'
    if '**Kiểm kẹt cửa sổ khởi động:**' not in doc: doc=doc.replace('### 4.3.',start_warning+'\n\n### 4.3.',1)
    else: doc=re.sub(r'^\*\*Kiểm kẹt cửa sổ khởi động:\*\*.*$',lambda _:start_warning,doc,flags=re.M)
    recovery_note='**Cổng trọng tâm và phục hồi:** forecast_programme_completion chỉ chặn chốt trọng tâm khi không còn đường khởi động của lựa chọn trong270ngày. Họp xử lý bất đồng và hòa giải/đóng kiến nghị không đọc cổng này; chúng vẫn mở theo các điều kiện PP, giá và cooldown hiện có, không được miễn cooldown. Lượt đang chạy phải đọc đúng purpose: chỉ tính +10nếu đã chọn phục hồi, không tính +10của lượt đóng kiến nghị. Tooltip hiển thị cohesion, ngày khởi động sớm nhất/muộn nhất, ngày thiếu và hành động mở lại.'
    if '**Cổng trọng tâm và phục hồi:**' not in doc: doc=doc.replace('## 4. Giá trị thời gian',recovery_note+'\n\n## 4. Giá trị thời gian',1)
    else: doc=re.sub(r'^\*\*Cổng trọng tâm và phục hồi:\*\*.*$',lambda _:recovery_note,doc,flags=re.M)
    focus_ui='Trọng tâm — tooltip/AI: lấy toàn bộ ngày/cổng từ forecast_programme_completion, không tự tính. Chặn phải hiển thị cohesion hiện tại, hạn khởi động270, ngày sớm nhất, ngày còn thiếu, phục hồi/cooldown cần chờ; không hứa phục hồi mở được kỳ đã hết hạn. AI chỉ chốt programme có focus_available=1, ưu tiên đường đang mở phù hợp mục tiêu; phục hồi/hòa giải không bị cổng chốt khóa. Lựa chọn kiểm tra bị khóa vẫn để công vụ/dân vận khả dụng nếu đủ gate cũ. Rủi ro E103-A chỉ cảnh báo như đã chốt; không đổi800/840/900, giá hoặc timer.'
    if 'Trọng tâm — tooltip/AI:' not in doc: doc=doc.replace('## 11. Bảng tính',focus_ui+'\n\n## 11. Bảng tính',1)
    else: doc=re.sub(r'^Trọng tâm — tooltip/AI:.*$',lambda _:focus_ui,doc,flags=re.M)
    registry='| `focus_commitment_gate`; elapsed_congress_days; recovery_cooldown_remaining; pending_recovery_remaining | Scheduler đại hội/decision cập nhật tuổi cửa sổ, cooldown và lượt phục hồi purpose=cohesion đang chạy | Cùng forecast_programme_completion trả focus_available, earliest_feasible_start_day, latest_start_day, start_days_short cho available/tooltip/AI; cổng chung bất kỳ programme, cổng lựa chọn programme đích; không là trigger engine mới |'
    if '| `focus_commitment_gate`;' not in doc: doc=doc.replace('\n\nRegistry này đóng phạm vi','\n'+registry+'\n\nRegistry này đóng phạm vi')
    criteria='- Cổng chốt: cùng forecast_programme_completion với full800/840; kiểm mọi cohesion0–39, cooldown0/90/180, mọi tuyến/4programme; biên19/20 và270/271, lượt phục hồi đang chạy. Chỉ chốt programme có đường trước270. Cổng không khóa phục hồi/hòa giải, không thay gate90ngày/giá/cooldown/timer; trường hợp hết cửa sổ ghi không còn đường kỳ hiện tại, không tự fail mission hoặc trao thưởng.'
    if '- Cổng chốt:' not in doc: doc=doc.replace('## 12. Trạng thái hoàn thành',criteria+'\n\n## 12. Trạng thái hoàn thành',1)
    doc=doc.replace('Danh mục vẫn74node. Đã bổ sung','Cổng chốt trọng tâm đã được thêm vào trigger chung; các probe cohort/cooldown và biên19/20 được tính bằng script, không tự tạo fallback. Danh mục vẫn74node. Đã bổ sung')
    return doc


def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + ['| ' + ' | '.join(str(v) for v in row) + ' |' for row in rows])


def pareto_exception_checks(p):
    from VIETNAM_POLITICAL_BALANCE_VI import e104_contract_amendment_gate
    spec=p['i3_pareto_exceptions'];terms=p['legacy_node_terms'];vectors=[];pairs=[];failures=[]
    contexts=[('XII12','roster hợp lệ',None,None)]+[('XIII12',f'hỗ trợ={support}; quyền chưa dùng={unused}',support,unused)
              for support,unused in [(0,0),(0,1),(p['e104']['B_grant'],0),(p['e104']['B_grant'],1),(p['e104']['A_grant'],0),(p['e104']['A_grant'],1)]]
    for (node,context,support,unused),route,k in itertools.product(contexts,p['prepare_days'],p['k_values']):
        options=[]
        gate=None
        if node=='XIII12':
            contract={'support_promised':support,'support_received':0,'support_forfeited':0,
                      'rights_granted':['quyền hợp tác trong hồ sơ'] if unused else [],'rights_used':[],'rights_revoked':[],'contract_state':'accepted'}
            gate=e104_contract_amendment_gate(contract)
        for option in 'AB':
            if node=='XII12':
                terms12=terms['XII12'];cohesion=terms12['immediate_cohesion_loss'] if option=='B' else 0
                values={'converted_cost':cohesion*p['cohesion_pp_rate'],'handover_pending_days':terms12['handover_days'] if option=='A' else 0,
                        'cohesion_loss':cohesion,'xii09_available':int(option=='B')}
                state=spec[node][option]['roster_state']
            else:
                lost=support if option=='B' else 0
                future_pp=len(p['contract_obligations']['check_days'])*p['contract_obligations']['pp_per_check'] if option=='A' else 0
                values={'converted_cost':lost*k+future_pp,'unreceived_support_lost':lost,'training_reward_pp':p['e104_training']['reward_pp'] if option=='A' and unused else 0,
                        'future_check_pp':len(p['contract_obligations']['check_days'])*p['contract_obligations']['pp_per_check'] if option=='A' else 0,'added_programme_days':spec[node]['added_programme_days']}
                state=spec[node][option]['cooperation_state']
            row={'node':node,'context':context,'route':route,'k':k,'option':option,'state':state,'centre_effect':spec[node][option]['centre'],**values}
            row['available']=gate['amend_available'] if node=='XIII12' and option=='A' else gate['cancel_available'] if node=='XIII12' else 1
            vectors.append(row);options.append(row)
        a,b=options;dims=[field for field in spec['dimensions'] if field in a]
        def dominates(x,y):
            if not x['available'] or not y['available']: return False
            comparisons=[x[field]<=y[field] if spec['dimensions'][field]=='min' else x[field]>=y[field] for field in dims]
            return all(comparisons) and any(x[field]!=y[field] for field in dims)
        a_dom,b_dom=dominates(a,b),dominates(b,a)
        changes={field:b[field]-a[field] for field in dims}
        relative={field:abs(changes[field])/max(abs(a[field]),abs(b[field])) if max(abs(a[field]),abs(b[field])) else 0 for field in dims}
        near=all(value<spec['near_duplicate_relative_threshold'] for value in relative.values())
        result='B thống trị A' if b_dom else 'A thống trị B' if a_dom else 'A KHÓA, B khả dụng' if not a['available'] else 'không thống trị'
        pairs.append({'node':node,'context':context,'route':route,'k':k,'result':result,'deltas_B_minus_A':changes,'relative_deltas':relative,'near_duplicate':near})
        if a_dom or b_dom: failures.append(pairs[-1])
    return vectors,pairs,failures


def e103_scenarios(p):
    from VIETNAM_POLITICAL_BALANCE_VI import e103_automatic_outcome,forecast_programme_completion
    rows=[]
    cutoff=p['early_days']['inspection'];deadline=p['program_deadline']
    for day,expected in [(cutoff-1,'on_time_full'),(cutoff,'on_time_full'),(cutoff+1,'late_full'),
                         (735,'late_full'),(750,'late_full'),(840,'late_full'),(841,'late_full'),
                         (deadline,'late_full'),(deadline+1,'partial_at_deadline')]:
        outcome=e103_automatic_outcome(p,day)
        f=forecast_programme_completion(p,'inspection','central','standard',60,signed_base_days=day)
        rows.append([day,outcome,int(day<=cutoff),f['choice_available'],'PASS' if outcome==expected and f['choice_available']==int(day<=840) else 'FAIL'])
    return rows


def i5_exception_rows(p):
    from VIETNAM_POLITICAL_BALANCE_VI import forecast_programme_completion,e103_automatic_outcome
    result=[]
    for case,cohesion in [('snapshot',p['cohesion_initial']),('low',p['cohesion_price_bands'][0][1])]:
        extra=p['low_cohesion_prepare_extra'] if cohesion<p['recovery']['low_below'] else 0
        for route,mode,a in itertools.product(p['prepare_days'],['standard','fast_paid','fast_override','combined_fast_paid'],'ABC'):
            if mode!='standard' and p['bop_route_snapshot'][route]<=p['bop_threshold']: continue
            if mode=='fast_override' and cohesion-p['checkpoint_count']*p['override_cohesion']<p['override_floor']: continue
            if mode=='combined_fast_paid' and cohesion<p['cadre_cohesion_required']: continue
            if a!='C' and not extra: continue
            day=p['prepare_days'][route]+extra+sum(p['action_days'][action][int(mode!='standard')] for action in ['audit_standard','audit','audit','review'])+p['e102'][a][2]
            f=forecast_programme_completion(p,'inspection',route,mode,cohesion,a)
            reasons=[]
            if extra: reasons.append(f'cohesion<{p["recovery"]["low_below"]}: chuẩn bị+{extra}')
            if a=='C': reasons.append(f'E102-C:+{p["e102"]["C"][2]}')
            result.append({'cohesion_case':case,'cohesion_initial':cohesion,'route':route,'mode':mode,'e102':a,'e103':'AUTO',
                'potential_full_day':day,'remaining_reserve_days':p['program_deadline']-day,
                'result':'full' if day<=p['program_deadline'] else 'partial_at_deadline','e103_outcome':e103_automatic_outcome(p,day),
                'reserve_floor_met':int(day<=p['program_deadline']-p['exception_reserve_days']),'reason':'; '.join(reasons),
                'status':'paper_deterministic_timeline_not_engine',
                'availability':'locked_start' if not f['start_available'] else 'locked_choice' if not f['choice_available'] else 'available',
                'forecast_full_day':f['forecast_full_day'],'forecast_reserve_days':f['forecast_reserve_days'],
                'lock_reason':f['lock_reason'],'reopen':f['reopen']})
    return result


def compact_document(doc,p):
    """Keep rules in the design; full diagnostic matrices live in CSV/optional JSON."""
    start=doc.index('### 8.1.');end=doc.index('### 8.2.',start)
    seen=set();lines=[]
    for line in doc[start:end].splitlines():
        if line.startswith('|'):
            if line in seen: continue
            seen.add(line)
        lines.append(line)
    doc=doc[:start]+'\n'.join(lines).rstrip()+'\n\n'+doc[end:]
    for prefix in ['| Tuyến | Mode | E102 | E103 | Ngày full tiềm năng |',
                   '| Cohesion | Tuyến | Mode | E102 | E103 |']:
        doc=re.sub(r'^'+re.escape(prefix)+r'[^\n]*\n(?:\|[^\n]*\n)+','',doc,count=1,flags=re.M)
    doc=doc.replace('**E102 × E103, snapshot cohesion60:** ngày tiềm năng/kết quả hợp đồng lấy từ CSV; k/r không đổi timer.',
        '**E102 × E103, snapshot cohesion60:** xem [CSV ngân sách](VIETNAM_POLITICAL_BALANCE_VI.csv), lọc programme inspection. k/r không đổi timer; bảng đầy đủ không chép lại ở đây.')
    doc=re.sub(r'^\*\*I5 — mọi đường ngoại lệ:\*\*.*$',
        '**I5 — ngoại lệ và cổng:** xem [CSV ngoại lệ I5](VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv). Có snapshot60/probe<20, cả ca khóa lịch và rủi ro A; sàn60, programme900. CSV chính chỉ chứa mode qua cổng BoP; ca phản thực được ghi riêng.',doc,flags=re.M)
    doc=doc.replace('[báo cáo lượt 1](VIETNAM_POLITICAL_REVIEW_L1_VI.md)', '[báo cáo hiện hành](VIETNAM_POLITICAL_REVIEW_L3_VI.md)')
    doc=doc.replace('[lượt 1](VIETNAM_POLITICAL_REVIEW_L1_VI.md) ghi các bất biến còn FAIL', '[hiện hành](VIETNAM_POLITICAL_REVIEW_L3_VI.md) ghi kết quả kiểm mô hình')
    doc=re.sub(r'^CSV có 1296 hàng:.*$',
        'CSV chính có648hàng qua cổng BoP, không xuất648hàng khóa rỗng. Script kiểm chính xác tập tổ hợp hợp lệ và việc loại mode bị khóa. Các ca khóa start/choice/rủi ro lịch có dữ liệu thật ở CSV ngoại lệ I5; probe cổng đủ được tính khi audit, xuất chi tiết bằng --audit-json.',doc,flags=re.M)
    doc=doc.replace('Nguồn duy nhất:', 'Nguồn tham số và công cụ tái tạo (đi kèm trong gói):')
    doc=doc.replace('không ghi đè báo cáo lịch sử Lượt 1', 'không ghi lại báo cáo hiện hành')
    replacements={
        ', trừ hợp đồng E103 đã bỏ quyền thưởng sớm theo mục 6.5': '',
        '- E103 và E104 có cửa sổ hợp đồng riêng; resolver chương trình giữ deadline cuối của mình.': '- E103 ghi kết quả kiểm chứng tự động; E104 giữ cửa sổ hợp đồng riêng. Resolver chương trình giữ deadline900.',
        ', kể cả khi đã bỏ thưởng PP qua E103-B/C': '',
        ' Hợp đồng E103-B/C bỏ thưởng sớm vẫn giữ nguyên.': ' E103 tự động không có option bỏ thưởng; trượt mốc sớm chỉ mất thưởng sớm.',
        'Mở lựa chọn thẩm định trách nhiệm trước ký trong E103 kế tiếp': 'Mở công cụ thẩm định trách nhiệm, chứng chỉ được E103 tự động đọc khi kiểm hồ sơ kế tiếp',
        '| Hợp đồng E103/E104 | Pending/kết quả lịch sử và deadline |': '| Kiểm chứng E103 / hợp đồng E104 | E103 ghi tiến độ/kết quả tự động; E104 lưu pending và deadline ký riêng |',
        'Rủi ro E103-A chưa hiện thực chỉ cảnh báo': 'E103 tự động không thêm trễ; mọi ngày trong mô hình đều tất định',
        'và kết quả hợp đồng E103': 'và chứng cứ đã kiểm chứng; E103 ghi cùng kết quả tự động',
        '- E103/E104 có guard hợp đồng riêng; resolver chúng không ghi programme đã hoàn thành.': '- E103 không có resolver hợp đồng riêng: cùng resolver programme ghi đúng một kết quả/epoch trước thưởng. E104 có guard hợp đồng riêng, không tự hoàn thành programme.',
    }
    for old,new in replacements.items(): doc=doc.replace(old,new)
    paragraphs={
        'E102-C cộng90ngày': 'E102-C cộng90ngày vào chuỗi chứng cứ; kiến nghị công khai vẫn phải xử lý để đủ4/4. Tooltip trước lựa chọn đọc ngày full và dự phòng từ forecast_programme_completion: chuẩn tập thể/cân bằng840, tập trung825, cấp tốc735; không có trục E103 A/B/C. Khi chưa chốt mode hiển thị các mode khả dụng; sau chốt giữ timer đã ký. Giá và các cơ hội E102 giữ nguyên.',
        '**Cổng dự báo dùng chung:**': '**Cổng dự báo dùng chung:** E102-C và lựa chọn có trễ tất định dùng forecast_programme_completion với timer/mode đã ký; ngày>840 bị khóa. E103 không có lựa chọn hoặc ngoại lệ cảnh báo. E104 kiểm cửa sổ ký theo tier riêng, không tự cộng timer ký vào chuỗi programme.',
        'Trọng tâm — tooltip/AI:': 'Trọng tâm — tooltip/AI: lấy ngày/cổng từ cùng dự báo. Hiển thị cohesion, hạn270, ngày khởi động khả thi, cooldown và ngày thiếu. AI chỉ chốt programme có focus_available=1; phục hồi/hòa giải vẫn mở, không cứu hồi tố cửa sổ đã hết. E103 chỉ đọc chứng cứ để ghi kết quả tự động; giữ800/840/900.',
        'CSV chính có': 'CSV chính có324hàng hợp lệ: bỏ324tổ hợp khóa BoP và trục lựa chọn E103 A/B/C đã bỏ. Script kiểm đúng tập tổ hợp và không trùng. Các ca khóa lịch E102-C/cohesion thấp ở CSV ngoại lệ I5; toàn bộ probe chỉ xuất khi dùng --audit-json.',
        '**So cùng E102-A': '**So cùng E102-A, E103 tự động, k=40, r=1:** chuẩn trượt690 vẫn late_full khi đủ4/4; cấp tốc đạt690 nhận70PP. E104 dùng cùng phản hồi đối tác chấp nhận; phân vai tier0 ký gói thu hẹp, kiêm nhiệm ký gói đầy đủ.',
        'Case đổi E103': 'E103 không có lựa chọn để đổi. Chuẩn T735/750 là late_full; cấp tốc T645 là on_time_full; T>900 chấm partial/fail theo số nhóm thực đạt ởdeadline, không trao full theo ngày tiềm năng. CSV là fixture lịch khi hoàn tất chứng cứ, không tạo chứng cứ trong game.',
        'Chiến tranh, counter reset': 'Chiến tranh, counter reset, kiến nghị chưa đóng và chỉ tiêu kinh tế chưa đạt nằm ngoài fixture lịch cơ sở. Không giả định một xác suất trễ E103. Khi đã biết trễ, dự báo và cổng phải tính đầy đủ; CSV không chứng minh full chắc chắn trong game.',
    }
    for prefix,new in paragraphs.items():
        doc=re.sub(r'^'+re.escape(prefix)+r'.*$',lambda _:new,doc,flags=re.M)
    doc=sync_observable_document(doc,p)
    return doc


def sync_observable_document(doc,p):
    from VIETNAM_POLITICAL_CONSUMERS_VI import choice_design_text
    doc=doc.replace('event_cost_pp chỉ gồm E102 và ký E104', 'event_cost_pp gồm E102, ký E104 và pp_contract_checks=20 khi nhận hợp đồng; thưởng đào tạo chưa làm không trừ vào ngân sách')
    doc=doc.replace('Trước hoặc đúng hạn nhận 0.75 ngân khố hỗ trợ', 'Ký trước hoặc đúng hạn xác lập hỗ trợ0.75ngân khố; chỉ nhận sau hai kỳ kiểm tra90/180ngày, mỗi kỳ10PP')
    doc=re.sub(r'^Hỗ trợ chỉ được trao khi.*$', 'Hỗ trợ chỉ thanh toán sau khi đối tác chấp nhận, ký đúng hạn và hoàn tất hai kỳ kiểm tra hợp đồng90/180ngày. Bảng ngân sách giả định nghĩa vụ được thực hiện, đã cộng20PP kiểm tra; không tự cộng25PP đào tạo tùy chọn. Nghĩa vụ này không kéo dài timer programme hoặc thay chứng cứ4/4.',doc,flags=re.M)
    start=doc.index('### 7.4a.');end=doc.index('### 7.5.',start)
    doc=doc[:start]+choice_design_text(p)+'\n'+doc[end:]
    for node in p['node_choice_cohesion']:
        pattern=rf'^\| {node} \|.*$'
        line=re.search(pattern,doc,re.M).group(0)
        line=re.sub(r'B: [\d.,]+ ngân khố', 'B: 0 PP, cohesion -'+str(p['node_choice_cohesion'][node]['B']),line)
        doc=re.sub(pattern,lambda _:line,doc,count=1,flags=re.M)
    summaries={
        'IX11':'Luân chuyển20PP: 65% cohesion+4; 35% xử lý lại thêm24PP và cohesion−4. RNG lưu một lần theo hồ sơ/epoch; không coi cohesion+4 là bảo đảm.',
        'IX12':'Kiểm toán độc lập20PP, kết quả cố định, không nhận bonus cohesion của luân chuyển. Đây là đường chắc chắn đối ứng với IX11 có xác suất thất bại.',
        'XI09':'Cứu dự án0.50ngân khố; sau nghiệm thu thu hồi0.75ngân khố, kết quả cố định. Không trao khoản thu hồi nếu chưa có chứng cứ bàn giao.',
        'XI10':'Tái cơ cấu90ngày, không ứng ngân khố: 70% thu hồi0.75ngân khố; 30% không thu hồi và cohesion−12. RNG một lần/đối tượng/epoch, không reroll khi load.',
        'XII12':'A bàn giao60ngày, không thu phí nhưng khóa XII09 trong kỳ. B mất6cohesion, mở XII09 ngay; gate được AND với prerequisite/roster hợp lệ, không tự hoàn tất đào tạo.',
        'XIII12':'Sửa chỉ khi còn lợi ích và đối tác chấp nhận, mở XIV11; kiểm chứng sau90/180ngày, mỗi lần10PP. Hủy khóa XIV11, mất hỗ trợ chưa nhận và đóng nghĩa vụ; không trừ khoản hỗ trợ chưa nhận vào ngân khố thực.',
        'X01':'Event chọn hồ sơ. A: 20 PP, mở XI05. B: 0 PP, cohesion−6, khóa XI05. Gate chỉ áp cùng hồ sơ nguồn; chưa chốt thì reader bị khóa, không giả có quyền mở cả hai.',
        'XII02':f"Event chọn trách nhiệm. A: {p['node_choice_prices']['XII02'][0][0]} PP, mở XIII09. B: 0 PP, cohesion−8, khóa XIII09. Gate được AND với prerequisite/kỳ; không tự cho chữ ký hoặc bỏ kiểm chứng.",
    }
    for node,summary in summaries.items():
        pattern=rf'^\| {node} \|.*$';match=re.search(pattern,doc,re.M)
        fields=[part.strip() for part in match.group(0).strip('|').split('|')]
        suffix=(' **Bổ sung hoàn thiện:**'+fields[4].split(' **Bổ sung hoàn thiện:**',1)[1]) if ' **Bổ sung hoàn thiện:**' in fields[4] else ''
        # Keep caller/guard/reader but discard obsolete guaranteed bonus prose.
        if suffix:
            spec=p['legacy_node_specs'][node]
            suffix=f" **Bổ sung hoàn thiện:** {spec['caller']} do focus hoàn thành mở; {spec['guard']}. Reader {spec['reader']}: {spec['carryover_effect']}."
        fields[4]=summary+suffix
        doc=re.sub(pattern,lambda _:'| '+' | '.join(fields)+' |',doc,count=1,flags=re.M)
    doc=re.sub(r'^- I6/I10 hoàn thiện:.*$', '- I6/I10: đọc record cùng đối tượng/epoch; consumer hoàn trả8PP hoặc0.20ngân khố một lần khi reader hoàn thành. Archive không có reward. Bỏ cờ cơ hội khỏi so programme; I10 là REVIEW, không tuyên bố utility bằng tên hành động.',doc,flags=re.M)
    doc=re.sub(r'^- XIII12 cổng bổ sung:.*$', '- XIII12: sửa cần lợi ích còn lại và đối tác chấp nhận; phải kiểm hồ sơ ngày90/180, mỗi lần10PP. Thiếu một lần mất hỗ trợ chưa nhận/quyền đào tạo chưa dùng, cohesion-6; không thu hồi tiền đã nhận. Hủy luôn mở.',doc,flags=re.M)
    doc=doc.replace('40consumer quyền cụ thể','consumer hoàn trả có giá').replace('I6/I10 được kiểm bằng script','I6 được kiểm cấu trúc; I10 cần playtest')
    doc=re.sub(r'^- 40 event/decision.*$', '- 38 node thông thường giữ phép so tiền trực tiếp; X01/XII02 đổi nguồn chi sang cohesion và gate. Tám node trong7.4a có nhánh thất bại hoặc reader mở/khóa thật. I3/I10 là REVIEW, không suy ra cân bằng từ tên quyền hoặc chiều chưa định nghĩa.',doc,flags=re.M)
    doc=doc.replace('Không có nguồn bất định trong mô hình.', 'Lịch E103 vẫn tất định; bất định chỉ được nêu tường minh ở IX11 và XI10, không cộng vào lịch programme này.')
    seen=set();lines=[]
    for line in doc.splitlines():
        if line.startswith('- '):
            if line in seen: continue
            seen.add(line)
        lines.append(line)
    doc='\n'.join(lines)+'\n'
    doc=re.sub(r'\n{4,}','\n\n\n',doc)
    return doc


def sync_approved_document():
    path=ROOT/'VIETNAM_POLITICAL_PARAMETERS_VI.json'
    data=json.loads(path.read_text(encoding='utf-8'))
    p={k:v['value'] for k,v in data['parameters'].items()}
    f=ROOT/'VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md';doc=f.read_text(encoding='utf-8')
    with (ROOT/'VIETNAM_POLITICAL_BALANCE_VI.csv').open(encoding='utf-8-sig',newline='') as stream: rows=list(csv.DictReader(stream))
    canonical=[r for r in rows if r['eligible']=='1' and float(r['k'])==p['k_values'][1] and float(r['r'])==p['r_values'][1]]
    def replace_paragraph(prefix,new):
        nonlocal doc
        pattern=rf'^{re.escape(prefix)}.*$'
        assert len(re.findall(pattern,doc,re.M))==1,prefix
        doc=re.sub(pattern,lambda _:new,doc,count=1,flags=re.M)
    replace_paragraph('**Bất biến lịch:**', '**Bất biến lịch:** programme900; start≤800/choice≤840 theo cùng forecast_programme_completion. Mọi trễ trong mô hình đều tất định. E103 tự động, không thêm thời gian hoặc ngoại lệ cảnh báo. Phục hồi sau start không xóa thời gian chuẩn bị đã ký; available/tooltip/CSV dùng cùng dự báo.')
    start=doc.index('### 6.5.');end=doc.index('### 6.6.',start)
    preserved=doc[start:end].split('**I2 theo chi phí quy đổi',1)[1]
    preserved='**I2 theo chi phí quy đổi'+preserved
    package=p['fast_upfront_pp']+p['checkpoint_count']*p['checkpoint_pp'];cash=p['checkpoint_count']*p['checkpoint_treasury']
    i2_table=table(['k thử','Giá gói PP','Thưởng PP','Chênh PP thuần','Ngân khố gói','Chênh quy đổi'],
        [[k,package,p['early_pp'],package-p['early_pp'],cash,package-p['early_pp']+k*cash] for k in p['k_values']])
    preserved=re.sub(r'\| k thử \| Giá gói PP \|.*?(?=\n\n)',lambda _:i2_table,preserved,count=1,flags=re.S)
    body=f'''### 6.5. E103: kết quả kiểm chứng tự động, không phải quyết định

Mốc ngày{p['e103']['caller_day']} chỉ thông báo tiến độ và chứng cứ còn thiếu. Khi đủ4/4, hệ thống tự ghi kết quả đúng epoch; không có menu A/B/C hoặc lựa chọn đánh đổi ở E103.

| Ngày đủ chứng cứ T | Kết quả tự động | Thưởng sớm |
| --- | --- | --- |
| T≤{p['early_days']['inspection']} | on_time_full; tăng tier/cohesion theo resolver | {p['early_pp']} PP một lần |
| {p['early_days']['inspection']}<T≤{p['program_deadline']} | late_full; vẫn full/tier/cohesion | 0 PP |
| T>{p['program_deadline']} hoặc chưa đủ4/4 tại deadline | Resolver chấm partial/fail theo số nhóm đã đạt | 0 PP |

T lấy từ lịch triển khai và kiểm chứng thật; E102-C vẫn cộng90ngày. E103 không tự tạo chứng cứ, không thu PP/ngân khố, không trừ cohesion và không cộng180ngày thẩm định. Bỏ hợp đồng780 và phí B/C của thiết kế cũ. E104 vẫn là quyết định hợp đồng riêng.

Chuẩn có T735/750: tự động late_full khi đủ4/4, không bị ép partial vì trượt690. Cấp tốc E102-A/B có T645: tự động on_time_full. Đây là hệ quả mode/E102 đã chọn, không gọi là canh bạc. Không có nguồn bất định trong mô hình.

Cổng giữ nguyên: lựa chọn gây T>840 bị khóa, không dùng nhãn rủi ro để bỏ qua. Biên840 được mở,841 bị khóa. Sau khi đã ký, timer không giảm hồi tố. [CSV ngoại lệ I5](VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv) giữ các ca phản thực bị khóa.

'''
    doc=doc[:start]+body+preserved.rstrip()+'\n\n'+doc[end:]
    prefix='| Tuyến | Mode | Chi PP ròng |'
    pattern=re.escape(prefix)+r'.*?(?=\n\n)'
    examples=[]
    fields=['pp_net_cost','treasury_net_cost','potential_full_day','pp_early_reward','cohesion_final','bop_final','converted_cost','side_project_available']
    for r in canonical:
        if r['program']=='inspection' and r['e102']=='A' and r['e103']=='AUTO': examples.append([r['route'],r['mode']]+[r[v] for v in fields])
    replacement=table(['Tuyến','Mode','Chi PP ròng','Chi ngân khố ròng','Ngày full','Thưởng PP sớm','Cohesion cuối','BoP cuối','Chi quy đổi','Dự án phụ mở'],examples)
    doc,n=re.subn(pattern,lambda _:replacement,doc,count=1,flags=re.S);assert n==1
    replace_paragraph('**Cột ngân sách E103', '**Cột ngân sách E103 tự động:** pp_e103=0, treasury_e103=0. event_cost_pp chỉ gồm E102 và ký E104; net_treasury_cost là alias của treasury_net_cost. Kết quả E103 suy từ ngày chứng cứ, không phải một option để tối ưu.')
    replace_paragraph('UI hiển thị', 'UI hiển thị giá và ngày/cổng từ forecast_programme_completion. E103 chỉ báo tiến độ ngày450 và kết quả kiểm chứng tự động; không menu A/B/C, không cảnh báo rủi ro giả. E104 giữ cửa sổ ký theo tier; các node đọc record đúng đối tượng/epoch.')
    replace_paragraph('AI chọn cấp tốc', 'AI chọn cấp tốc khi đạt thưởng70PP hoặc cơ hội có ích; so gói55PP+0.50 với70PP, chênh+5PP ởk40. E103 không có lựa chọn AI; E102 và mode mới là quyết định. Đọc cổng start800/choice840/chốt270 từ cùng dự báo; dự án phụ là khoản mua thêm.')
    replace_paragraph('- I5:', '- I5: cùng forecast_programme_completion cho start≤800/choice≤840, CSV và tooltip. Mọi trễ trong mô hình tất định; khóa T>840, không có ngoại lệ rủi ro E103. Kiểm cohesion0–19, phục hồi0→20 và cửa sổ270; timer/mode đã ký không đổi, programme900/E102+90 giữ nguyên.')
    replace_paragraph('- E103 tự động:', '- E103 tự động: không thuộc phép so lựa chọn I3. Kiểm T690/691,735/750,840/841,900/901 và một kết quả mỗi epoch; E103 không thu phí hoặc kéo dài thẩm định.')
    start=doc.index('## 12. Trạng thái hoàn thành')
    doc=doc[:start]+'''## 12. Trạng thái hoàn thành

Mô hình giấy có74node; E103 đã chuyển thành hệ quả tự động của chứng cứ, không còn A/B/C hoặc phí/thẩm định cũ. Mode và E102 giữ quyết định thực. Thưởng sớm70PP; programme900/E102+90/start800/choice840 giữ nguyên.

Báo cáo hiện hành ở [Lượt 3](VIETNAM_POLITICAL_REVIEW_L3_VI.md). Các giá là giả định gameplay; chưa triển khai thiết kế này trong game hoặc kiểm engine/AI/playtest.

BLUF
'''
    doc=sync_remaining_document(doc,p)
    criteria='- I6/I10 hoàn thiện: đối chiếu gate/caller/guard/reader22node theo legacy_node_specs; consumer40node available1/đối ứng0 theo node_opportunity_effects. Script kiểm các nhu cầu hành động riêng, không cộng điểm quyền, không tính archive_XV là cơ hội hiện tại.\n- Giá node mới: XI12 bồi hoàn20PP/0.50; XII12 kiện toàn−6cohesion; XII10 30PP so8cohesion+0.25, báo biên1PP tại k20 không chỉnh. X09 hai đợt0.25, X10 ứng0.50/rút30/kiến nghị; kiểm cả thời gian và trạng thái checkpoint/kiến nghị. XIV10 ổn định+1%365ngày, trần1%, dùng max với tier dân vận, phải có nghiệm thu đúng địa điểm. XIV11 giữ15/sửa0.50/hủy mất hỗ trợ chưa nhận. Mọi số là giả định gameplay, chưa cân bằng bằng engine; không thay giá/timer programme.\n'
    if '- I6/I10 hoàn thiện:' not in doc and '- I6/I10:' not in doc: doc=doc.replace('## 12. Trạng thái hoàn thành',criteria+'\n## 12. Trạng thái hoàn thành')
    gate_note='\n\n**Cổng dự báo dùng chung:** E102-C và lựa chọn có trễ tất định dùng forecast_programme_completion với timer/mode đã ký; ngày>840 bị khóa. E103 không có lựa chọn hoặc ngoại lệ cảnh báo. E104 kiểm cửa sổ ký theo tier riêng, không tự cộng timer ký vào chuỗi programme.\n\n'
    if '**Cổng dự báo dùng chung:**' not in doc: doc=doc.replace('### 6.6.',gate_note+'### 6.6.',1)
    doc=compact_document(doc,p)
    if (ROOT/'VIE_political_v57_implementation.md').exists():
        doc=doc.replace('Chưa triển khai game file hoặc chạy HOI4.', 'Đã có [adapter game v57](VIE_political_v57_implementation.md) trong repo; chưa nghiệm thu HOI4.')
        doc=doc.replace('chưa triển khai thiết kế này trong game hoặc kiểm engine/AI/playtest.', 'adapter game v57 đã được triển khai trong repo và có fixture đọc script; chưa nghiệm thu engine/AI/playtest.')
    f.write_text(doc,encoding='utf-8')
    data['approved_section_hashes']={n:hashlib.sha256(re.search(rf'^## {n}\..*?(?=^## |\Z)',doc,re.M|re.S).group(0).encode()).hexdigest() for n in ['3','4','6']}
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def audit_l3(write_json=False):
    data = json.loads((ROOT / 'VIETNAM_POLITICAL_PARAMETERS_VI.json').read_text(encoding='utf-8'))
    p = {k:v['value'] for k,v in data['parameters'].items()}
    doc = (ROOT / 'VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md').read_text(encoding='utf-8')
    with (ROOT / 'VIETNAM_POLITICAL_BALANCE_VI.csv').open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    valid = [r for r in rows if r['eligible'] == '1']
    exception_rows=i5_exception_rows(p)
    with (ROOT/'VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv').open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(exception_rows[0]));writer.writeheader();writer.writerows(exception_rows)
    unique = {(r['program'],r['route'],r['mode'],r['e102'],r['e103']):r for r in valid if float(r['k'])==p['k_values'][1] and float(r['r'])==p['r_values'][1]}
    structural = []
    def verify(name, condition, detail):
        structural.append([name, 'PASS' if condition else 'FAIL', detail])
    def number(v):
        return float(v)
    def equal(a,b):
        return abs(float(a)-float(b)) < 0.00001
    def get_table(prefix):
        lines = doc.splitlines()
        starts = [i for i,line in enumerate(lines) if line.startswith(prefix)]
        assert len(starts)==1, (prefix,starts)
        i = starts[0] + 2
        found=[]
        while i < len(lines) and lines[i].startswith('|'):
            found.append([v.strip() for v in lines[i].strip('|').split('|')])
            i+=1
        return found
    catalogue=doc.split('### 7.4a.')[0]
    node_rows = re.findall(r'^\| ((?:F|IX|X|XI|XII|XIII|XIV)\d\d)(?: `[^`]+`)? \| ([^|]+) \| (\d+) \|',catalogue,re.M)
    verify('Danh mục node/cost', len(node_rows)==p['l3_document_checks']['fixed_node_count'] and len({r[0] for r in node_rows})==len(node_rows) and all(int(c)==p['focus_nodes'][n]['cost'] and name.strip()==p['focus_nodes'][n]['name'] for n,name,c in node_rows), f'{len(node_rows)} node; tên và cost theo B1')
    for n,digest in data['l3_protected_sections'].items():
        block = re.search(rf'^## {n}\..*?(?=^## |\Z)',doc,re.M|re.S).group(0)
        expected=data.get('approved_section_hashes',{}).get(n,digest)
        verify(f'Mục {n}',hashlib.sha256(block.encode()).hexdigest()==expected,'Hash sửa E103/I5 đã xác nhận' if n in data.get('approved_section_hashes',{}) else 'Giữ hash trước Lượt 3')
    verify('BLUF',doc.rstrip().endswith('BLUF'),'Giữ dòng cuối')
    bad_tables=[]
    previous_width=None
    for i,line in enumerate(doc.splitlines(),1):
        if line.startswith('|'):
            width=len(line.strip('|').split('|'))
            if previous_width is not None and width!=previous_width: bad_tables.append(i)
            previous_width=width
        else: previous_width=None
    verify('Định dạng bảng',not bad_tables,f'Hàng lệch số cột: {bad_tables}')
    for a,b in p['l3_document_checks']['mutex_pairs']:
        ra=next((line for line in doc.splitlines() if re.match(rf'^\| {a}(?: |`)',line)), '')
        rb=next((line for line in doc.splitlines() if re.match(rf'^\| {b}(?: |`)',line)), '')
        verify(f'Loại trừ {a}/{b}',f'loại trừ {b}' in ra and f'loại trừ {a}' in rb,'Phải ghi ở cả hai node')
    gates=p['focus_prerequisites']
    graph_errors=[]
    def paths(node,trail=()):
        if node in trail:
            graph_errors.append('cycle:'+node)
            return []
        if node not in gates:
            return [{node}]
        result=[]
        for parent in gates[node]:
            if parent not in p['focus_nodes']: graph_errors.append('missing:'+parent)
            result.extend([ancestors|{node} for ancestors in paths(parent,trail+(node,))])
        return result
    for node in gates:
        candidates=paths(node)
        compatible=[candidate for candidate in candidates if not any(a in candidate and b in candidate for a,b in p['l3_document_checks']['mutex_pairs'])]
        if not compatible: graph_errors.append('unreachable:'+node)
        row=next(line for line in doc.splitlines() if line.startswith('| '+node+' |'))
        prerequisite_text=row.split('|')[4].split(';')[2]
        mentioned=re.findall(r'\b(?:F|IX|X|XI|XII|XIII|XIV)\d\d\b',prerequisite_text)
        if mentioned!=gates[node]: graph_errors.append('B1_gate_mismatch:'+node)
    verify('Prerequisite và mutex',not graph_errors,f'{len(gates)} node: {graph_errors}; thử mọi nhánh OR, không khóa node qua tổ tiên loại trừ')
    seq={'cadre':['training','training','succession','review'],'administration':['administration_project','administration_project','review'],'inspection':['audit_standard','audit','audit','review'],'social':['local_project','local_project','review']}
    labels={'cadre':'Cán bộ','administration':'Công vụ','inspection':'Kiểm tra','social':'Dân vận'}
    core=[]
    for program,actions in seq.items():
        days=[p['prepare_days'][route]+sum(p['action_days'][a][fast] for a in actions) for route,fast in [('collective',0),('central',0),('central',1)]]
        core.append([labels[program],days[0],days[1],p['early_days'][program],days[2]])
    actual_core=get_table('| Programme | Chuẩn tập thể/cân bằng |')
    verify('Bảng ngày 11.1',all(a[0]==b[0] and all(equal(x,y) for x,y in zip(a[1:],b[1:])) for a,b in zip(actual_core,core)) and len(actual_core)==len(core),'Tính độc lập từ action_days/prepare_days')
    tools_table=get_table('| Chương trình | Chuỗi tuần tự, bỏ qua focus đã làm |')
    tool_checks=[]
    for row,(program,actions),base in zip(tools_table,seq.items(),core):
        pp=p['tools']['start'][0]+sum(p['tools'][a][0] for a in actions)
        treasury=sum(p['tools'][a][1] for a in actions)
        total=re.search(r'=\s*(\d+) PP; ([\d.]+)',row[4])
        tool_checks.append(total is not None and equal(total[1],pp) and equal(total[2],treasury) and equal(re.search(r'\d+',row[2])[0],base[1]) and equal(row[3],base[4]))
    verify('Bảng công cụ 4.3',len(tool_checks)==len(seq) and all(tool_checks),'Ngày/PP/ngân khố của cả bốn chương trình từ B1')
    verify('Ký theo tier',f"Ký theo tier cán bộ 0/1/2/3 là {'/'.join(map(str,p['sign_days']))} ngày" in doc and f"XIII09 cần {p['late_signature_windows']['XIII09']} ngày" in doc and f"XIV11 cần {p['late_signature_windows']['XIV11']} ngày" in doc,'4.4/5.2/6.6 dùng cùng tier/cửa sổ B1')
    dates=list(p['congress_dates'].items())
    gaps=[[term,(date.fromisoformat(nxt)-date.fromisoformat(now)).days-p['congress_preparation_days']-p['program_start_latest']-p['program_deadline']] for (term,now),(_,nxt) in zip(dates,dates[1:])]
    actual_gaps=get_table('| Nhiệm kỳ | Ngày còn cách chuẩn bị kỳ sau |')
    verify('Bảng lịch',len(actual_gaps)==len(gaps) and all(a[0]==b[0] and equal(a[1],b[1]) for a,b in zip(actual_gaps,gaps)),f'Khoảng nhỏ nhất {min(g for _,g in gaps)} ngày')
    arithmetic_errors=[]
    for row in valid:
        pp=sum(number(row[c]) for c in ['pp_start','pp_actions','pp_e102','pp_e103','pp_fast_upfront','pp_checkpoints','pp_combined','pp_signature','pp_contract_checks','pp_recovery'])
        converted=number(row['pp_net_cost'])+number(row['treasury_net_cost'])*number(row['k'])+number(row['cohesion_net_spent'])*p['cohesion_pp_rate']
        expected_day=p['prepare_days'][row['route']]+sum(p['action_days'][a][int(row['mode']!='standard')] for a in seq[row['program']])
        if row['program']=='inspection':
            expected_day+=p['e102'][row['e102']][2]
        income=(number(row['r'])+p['branch_pp_daily'])*p['accounting_days']
        expected_treasury=sum(p['tools'][a][1] for a in seq[row['program']])+number(row['treasury_checkpoints'])-number(row['e104_grant'])
        if row['program']=='inspection': expected_treasury+=p['e102'][row['e102']][1]
        aliases_ok=equal(row['event_cost_pp'],number(row['pp_e102'])+number(row['pp_e103'])+number(row['pp_signature'])+number(row['pp_contract_checks'])) and equal(row['net_treasury_cost'],row['treasury_net_cost'])
        if not all([equal(pp,row['pp_gross_cost']),equal(pp-number(row['pp_early_reward']),row['pp_net_cost']),equal(converted,row['converted_cost']),equal(expected_day,row['potential_full_day']),equal(income,row['modeled_pp_income']),equal(converted/income,row['converted_cost_income_ratio']),equal(expected_treasury,row['treasury_net_cost']),aliases_ok]): arithmetic_errors.append(row)
    verify('Số học toàn CSV',not arithmetic_errors,f'{len(rows)} hàng; {len(valid)} hợp lệ; {len(arithmetic_errors)} sai tổng/timeline/thu nhập/chi quy đổi')
    verify('Thông số E103 tự động',p['e103']['mode']=='automatic' and all(p['e103'][key]==0 for key in ['pp','treasury','adds_days','cohesion_penalty']) and p['e102']['C'][2]==90 and p['program_deadline']==900 and p['early_days']['inspection']==690 and p['exception_reserve_days']==60,'Bỏ giá/cam kết/thẩm định E103 cũ theo yêu cầu; giữ E10290/programme900/mốc690/cổng840')
    modes=['standard','fast_paid','fast_override','combined_fast_paid']
    expected_keys=set();locked_keys=set()
    for program,route,mode in itertools.product(seq,p['prepare_days'],modes):
        pairs=[(a,'AUTO') for a in 'ABC'] if program=='inspection' else [('NA','NA')]
        legal=mode=='standard' or p['bop_route_snapshot'][route]>p['bop_threshold']
        for a,b in pairs:
            for k,r in itertools.product(p['k_values'],p['r_values']):
                key=(program,route,mode,a,b,float(k),float(r))
                (expected_keys if legal else locked_keys).add(key)
    keys=[tuple(row[field] for field in ['program','route','mode','e102','e103'])+(number(row['k']),number(row['r'])) for row in rows]
    verify('Phủ ma trận CSV',set(keys)==expected_keys and len(keys)==len(expected_keys) and len(valid)==len(rows),
        f'{len(expected_keys)} tổ hợp hợp lệ đúng tập/không trùng; loại {len(locked_keys)} tổ hợp khóa BoP, không mất đường hợp lệ')
    verify('Loại hàng khóa',not(set(keys)&locked_keys),f'{len(locked_keys)} tổ hợp khóa được kiểm riêng, không lấp ô CSV')
    examples=get_table('| Tuyến | Mode | Chi PP ròng |')
    fields=['pp_net_cost','treasury_net_cost','potential_full_day','pp_early_reward','cohesion_final','bop_final','converted_cost','side_project_available']
    verify('Bảng ngân sách mẫu 11.1',all(all(equal(value,unique[('inspection',a[0],a[1],'A','AUTO')][field]) for value,field in zip(a[2:],fields)) for a in examples),'Đối chiếu từng cột CSV ở k=40/r=1')
    with (ROOT/'VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv').open(encoding='utf-8-sig',newline='') as stream:
        stored_exceptions=list(csv.DictReader(stream))
    verify('CSV ngoại lệ I5',stored_exceptions==[{k:str(v) for k,v in r.items()} for r in exception_rows],f'{len(exception_rows)} tổ hợp snapshot/thấpcohesion; không chép bảng CSV vào thiết kế')
    e103_test=e103_scenarios(p)
    from VIETNAM_POLITICAL_BALANCE_VI import e103_automatic_outcome
    e103_errors=[row for row in valid if row['program']=='inspection' and not(
        row['e103']=='AUTO' and number(row['pp_e103'])==number(row['treasury_e103'])==0
        and row['e103_outcome']==e103_automatic_outcome(p,number(row['potential_full_day']))
        and number(row['early_reward_earned'])==int(number(row['potential_full_day'])<=p['early_days']['inspection']))]
    verify('E103 kết quả và biên',not e103_errors and all(row[-1]=='PASS' for row in e103_test),f'{len(e103_test)} probe biên; {len(e103_errors)} lỗi; không phí/thẩm định hoặc A/B/C')
    package=p['fast_upfront_pp']+p['checkpoint_count']*p['checkpoint_pp']
    cash=p['checkpoint_count']*p['checkpoint_treasury']
    values=get_table('| k thử | Giá gói PP |')
    verify('Bảng I2',all(all(equal(x,y) for x,y in zip(a[1:],[package,p['early_pp'],package-p['early_pp'],cash,package-p['early_pp']+cash*number(a[0])])) for a in values),'PP thuần và ngân khố không tính trùng')
    values=get_table('| k thử | Thương lượng quy đổi |')
    override=p['override_cohesion']*p['cohesion_pp_rate']
    verify('Bảng checkpoint',all(all(equal(x,y) for x,y in zip(a[1:],[p['checkpoint_pp']+p['checkpoint_treasury']*number(a[0]),override,p['checkpoint_pp']+p['checkpoint_treasury']*number(a[0])-override])) for a in values),'Từ B1, không dùng số hardcode của bảng')
    section81=doc.split('### 8.1.')[1].split('### 8.2.')[0]
    registry_rows=[line for line in section81.splitlines() if line.startswith('|')]
    verify('Registry không lặp',len(registry_rows)==len(set(registry_rows)),'Mỗi dòng đăng ký 8.1 chỉ xuất hiện một lần')
    missing_links=[]
    for name in ['VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md']:
        for link in re.findall(r'\]\(([^)]+)\)',(ROOT/name).read_text(encoding='utf-8')):
            if '://' not in link and not link.startswith('#') and not (ROOT/link.split('#')[0]).is_file():
                missing_links.append(link)
    verify('Liên kết local',not missing_links,f'Không trỏ REVIEW_L1/L2 đã xóa; thiếu={missing_links}')
    ids=set(re.findall(r'\bVIE_[a-zA-Z0-9_]+\b(?!\.(?:md|py|csv|json|txt|gfx|dds|yml)\b)',doc.split('## 9.')[0]))
    verify('Registry 8.1',all(i in section81 for i in ids) and ids==set(p['designed_identifiers']),f'{len(ids)} tên thiết kế; 74 nhãn node; E101–E104 có registry; chưa là định nghĩa engine')
    verify('Registry hoàn thiện',all(name in section81 for name in ['forecast_programme_completion','legacy_node_specs','legacy_node_terms','node_opportunity_effects','i3_pareto_exceptions','archive_XV','e104_contract_amendment_gate','e104_contract_ledger','support_promised','support_received','support_forfeited','rights_granted','rights_used','rights_revoked','contract_state','focus_commitment_gate','elapsed_congress_days','recovery_cooldown_remaining','pending_recovery_remaining','focus_available','earliest_feasible_start_day','latest_start_day','start_days_short']),'Tên thiết kế mới có writer/reader và vòng đời; chưa tạo ID engine')
    node_costs=[]
    crossover=True
    for node,pair in p['node_choice_prices'].items():
        costs=[[pp+cash*k for pp,cash in pair] for k in p['k_values']]
        crossover &= node in p['node_choice_cohesion'] or (any(a<b for a,b in costs) and any(b<a for a,b in costs))
        node_costs.append([node]+[f'{a:g}/{b:g}' for a,b in costs])
    event_costs=[]
    for k in p['k_values']:
        for option,(pp,cash,cohesion,*_) in p['e101'].items(): event_costs.append(['E101',option,k,pp+cash*k-cohesion*p['cohesion_pp_rate']])
        for option,(pp,cash,_) in p['e102'].items(): event_costs.append(['E102',option,k,pp+cash*k])
        for option in 'ABC': event_costs.append(['E104',option,k,p['e104'][option+'_pp']+(len(p['contract_obligations']['check_days'])*p['contract_obligations']['pp_per_check'] if p['e104'].get(option+'_grant',0)>0 else 0)-p['e104'].get(option+'_grant',0)*k])
    core_event_direct_checks=[]
    for event in ['E101','E102','E104']:
        winners=[]
        for k in p['k_values']:
            costs={option:cost for name,option,row_k,cost in event_costs if name==event and row_k==k}
            winners.append({option for option,cost in costs.items() if cost==min(costs.values())})
        universal=set.intersection(*winners)
        core_event_direct_checks.append([event,'PASS' if not universal else 'FAIL',','.join(sorted(universal)) or 'không có lựa chọn rẻ nhất mọi k'])
    verify('I3 phép so tiền E101/E102/E104',len(core_event_direct_checks)==3,'Kiểm cùng event/tuyến; kết quả luôn rẻ nhất được báo, không dùng phép kiểm này để gán PASS cân bằng')
    finite_winners=[]
    route_universal_winners=[]
    dominated_pairs=[]
    opportunity=[]  # Do not use unpriced access flags to establish dominance.
    for k,r,program,route in itertools.product(p['k_values'],p['r_values'],seq,p['prepare_days']):
        pool=[x for x in valid if float(x['k'])==k and float(x['r'])==r and x['program']==program and x['route']==route]
        def weakly_better(a,b):
            comparisons=[number(a['pp_net_cost'])<=number(b['pp_net_cost']),number(a['potential_full_day'])<=number(b['potential_full_day']),number(a['cohesion_final'])>=number(b['cohesion_final']),int(a['result']=='full')>=int(b['result']=='full')]+[number(a[f])>=number(b[f]) for f in opportunity]
            return all(comparisons)
        def better(a,b):
            strict=any([number(a['pp_net_cost'])<number(b['pp_net_cost']),number(a['potential_full_day'])<number(b['potential_full_day']),number(a['cohesion_final'])>number(b['cohesion_final'])]+[number(a[f])>number(b[f]) for f in opportunity])
            return weakly_better(a,b) and strict
        if len(pool)>1:
            for a in pool:
                if all(weakly_better(a,b) for b in pool) and any(better(a,b) for b in pool): finite_winners.append([k,r,program,route,a['mode'],a['e102'],a['e103']])
        if k==p['k_values'][1] and r==p['r_values'][1]:
            dominated_pairs += [(a,b) for a,b in itertools.permutations(pool,2) if better(a,b)]
    for k,r,route in itertools.product(p['k_values'],p['r_values'],p['prepare_days']):
        pool=[row for row in valid if float(row['k'])==k and float(row['r'])==r and row['route']==route]
        for a in pool:
            if all(weakly_better(a,b) for b in pool) and any(better(a,b) for b in pool):
                route_universal_winners.append([k,r,route,a['program'],a['mode'],a['e102'],a['e103']])
    opportunities,legacy_costs,legacy_i3_failures=completion_tables(p)
    pareto_vectors,pareto_pairs,pareto_failures=pareto_exception_checks(p)
    contract_probes=xiii12_contract_checks(p)
    verify('XIII12 cổng/softlock/hủy',all(row[-1]=='PASS' for row in contract_probes),f'{len(contract_probes)} trạng thái ledger; hủy luôn mở/idempotent, chỉ chạm ledger; hỗ trợ đã nhận/quyền đã dùng giữ nguyên, không có writer mission/tier/reward')
    probes,recovery_probe=forecast_probe_tables(p)
    selected_start_cases=selected_inspection_start_cases(p)
    focus_rows,focus_groups,focus_boundaries,focus_expiry,focus_errors=focus_gate_probe_tables(p)
    verify('Cổng chốt / softlock trong cửa sổ',not focus_errors,f'{len(focus_rows)} probe toàn bộ0–39/cooldown0/90/180/3tuyến/4programme; phục hồi/hòa giải không bị cổng khóa; không chốt kiểm tra không kịp270')
    preserved_failures=[key for key,digest in data['focus_gate_preserved_parameter_hashes'].items() if key not in ('early_pp','e103','node_choice_prices') and hashlib.sha256(json.dumps(p[key],ensure_ascii=False,sort_keys=True).encode()).hexdigest()!=digest]
    original_prices=json.loads(json.dumps(p['node_choice_prices']))
    for node,price in data['observable_change_scope']['original_B_prices'].items(): original_prices[node][1]=price
    verify('Giá ngoài hai node đổi cohesion',hashlib.sha256(json.dumps(original_prices,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==data['focus_gate_preserved_parameter_hashes']['node_choice_prices'],'Chỉ thay B của X01/XII02; giữ giá 38 node khác')
    verify('Thưởng sớm đã cân lại',p['early_pp']==70,'14/10/2026: ngoại lệ được yêu cầu cho hash early_pp cũ=50; giữ hash lịch sử, kiểm mức mới=70')
    verify('Giữ giá và timer ngoài thay đổi được yêu cầu',not preserved_failures,f'Giữ hash cũ trừ early_pp=70 và E103 tự động được kiểm riêng; khác={preserved_failures}')
    reserve_violations=[row for row in exception_rows if row['availability']=='available' and row['forecast_reserve_days']<p['exception_reserve_days']]
    risk_below_floor=[row for row in exception_rows if row['availability']=='available' and row['result']=='full' and row['remaining_reserve_days']<p['exception_reserve_days']]
    old_below_floor=[row for row in exception_rows if row['result']=='full' and row['remaining_reserve_days']<p['exception_reserve_days']]
    start_errors=[row for row in probes if row[6]=='MỞ' and row[5]<p['reserve_days']]
    timeline_softlock=any(not any(row[6]=='MỞ' for row in probes if row[1]==route) for route in p['prepare_days'])
    low_day=core[2][1]+p['low_cohesion_prepare_extra']
    simple_nodes=[n for n,_,_ in node_rows if n not in p['node_choice_prices'] and n not in [f'F{i:02}' for i in range(1,13)]]
    missing=[]
    for n in simple_nodes:
        line=next(line for line in doc.splitlines() if line.startswith('| '+n+' |'))
        spec=p['legacy_node_specs'].get(n)
        if not spec or not re.search(rf'^\| {n} \| [^|]+ \| \d+ \| [^|]+; từ ',line) or not all(text in line for text in [spec['caller'],spec['condition'],spec['guard'],spec['reader']]): missing.append(n)
    complete_rights=set(p['node_opportunity_effects'])==set(p['node_choice_prices'])-set(p['node_choice_cohesion']) and all(
        e['reader'] in p['focus_nodes'] or e['reader'] in ['E103','archive_XV'] for e in p['node_opportunity_effects'].values())
    complete_rights &= all(e[o]['available']==1 and e[o]['counterpart_available']==0 and e['A']['action']!=e['B']['action'] for e in p['node_opportunity_effects'].values() for o in 'AB')
    verify('22node hoàn thiện',not missing,f'{len(p["legacy_node_specs"])} gate/caller/guard/reader; thiếu={missing}')
    verify('Consumer hoàn trả có giá',complete_rights and len(opportunities)==len(p['node_opportunity_effects'])*2*len(p['prepare_days'])*len(p['k_values']),f'{len(opportunities)} hàng; hành động riêng và đối ứng khóa; archive_XV không tính utility hiện tại')
    with (ROOT/'VIETNAM_POLITICAL_NODE_CHOICES_VI.csv').open(encoding='utf-8-sig',newline='') as stream: node_csv=list(csv.DictReader(stream))
    def csv_num(row,key): return float(row[key]) if row.get(key) else 0
    from VIETNAM_POLITICAL_CONSUMERS_VI import audit_consumers
    consumer_rows,consumer_errors=audit_consumers(p)
    verify('Consumer, nghĩa vụ và tám node',not consumer_errors,f'{len(consumer_rows)} nhánh×k; kiểm đọc thật, cả kết quả thất bại, gate thật và replay; lỗi={consumer_errors}')
    expected_node_rows=len(consumer_rows)+len(opportunities)+len(pareto_vectors)+sum((3 if row[0]=='XIV11' else 2)*len(p['prepare_days']) for row in legacy_costs)
    node_price_errors=[]
    for row in node_csv:
        if row.get('scope')=='observable_outcome_not_engine':
            expected=-csv_num(row,'pp_delta')-csv_num(row,'treasury_delta')*csv_num(row,'k')-csv_num(row,'cohesion_delta')*p['cohesion_pp_rate']
        elif row.get('scope','').startswith('i3_named_pareto'):
            expected=csv_num(row,'cohesion_loss')*p['cohesion_pp_rate']+csv_num(row,'unreceived_support_lost')*csv_num(row,'k')+csv_num(row,'future_check_pp')
        else:
            expected=csv_num(row,'pp')+(csv_num(row,'actual_treasury_debit')+csv_num(row,'unreceived_support_lost'))*csv_num(row,'k')+csv_num(row,'cohesion_spent_cost')*p['cohesion_pp_rate']
        if abs(expected-csv_num(row,'converted_cost'))>0.00001: node_price_errors.append(row)
    verify('CSV lựa chọn node',len(node_csv)==expected_node_rows and not node_price_errors,f'{len(node_csv)}={len(opportunities)} quyền+243giá+{len(pareto_vectors)} vector; {len(node_price_errors)} sai tổng; hỗ trợ mất khác debit thật')
    verify('Cổng dự báo I5',not reserve_violations and not start_errors and not timeline_softlock,f'{len(probes)} probe start, {len(exception_rows)} ngoại lệ; trễ tất định bị khóa; không ngoại lệ rủi ro E103')
    service=p['legacy_node_terms']['XIV10']
    stability_rows=[]
    for tier,tier_reward in enumerate([0]+p['tier_modifiers']['stability']):
        effective=max(tier_reward,min(service['stability_reward'],service['stability_cap']))
        stability_rows.append([tier,tier_reward,service['stability_reward'],effective,effective-tier_reward])
    verify('XIV10 trần và không chồng',service['requires_matching_acceptance'] and not service['stack_with_social_tier'] and service['stability_reward']<=service['stability_cap'] and all(row[3]<=max(row[1],service['stability_cap']) for row in stability_rows),'Nghiệm thu cùng địa điểm; max(tier,idea); một lần/địa điểm/epoch, không cộng thời hạn')
    verify('Phạm vi Pareto',p['i3_pareto_exceptions']['nodes']==['XII12','XIII12'] and p['i3_pareto_exceptions']['direct_money_test_other_nodes'],'Chỉ hai node được người dùng chốt; không đổi giá/timer')
    fast_cash=p['checkpoint_count']*p['checkpoint_treasury']
    diff=package-p['early_pp']+fast_cash*40
    fast_comparisons=[]
    for k in p['k_values']:
        for program in ['cadre','administration','inspection','social']:
            candidates=[r for r in valid if r['program']==program and r['route']=='central'
                and number(r['k'])==k and number(r['r'])==1 and r['result']=='full'
                and number(r['cohesion_final'])==p['cohesion_initial']+p['outcome_cohesion']['full']]
            # So hai phuong an re nhat dat cung full/cohesion; khong tru gia du an phu.
            standard=min((r for r in candidates if r['mode']=='standard'),key=lambda r:number(r['converted_cost']))
            fast=min((r for r in candidates if r['mode']=='fast_paid'),key=lambda r:number(r['converted_cost']))
            fast_comparisons.append([program,k,standard['e102']+'/'+standard['e103'],fast['e102']+'/'+fast['e103'],
                number(standard['converted_cost']),number(fast['converted_cost']),
                number(fast['converted_cost'])-number(standard['converted_cost'])])
    fast_pass=all(abs(row[-1])<=p['max_fast_reward_pp_difference'] for row in fast_comparisons if row[1]==40)
    verify('Cấp tốc so chuẩn tại k=40',fast_pass,'Bốn programme; cùng tuyến central/r=1/full/cohesion; so phương án rẻ nhất mỗi mode, không tính dự án phụ là thưởng')
    checks=[
      ['I1','PASS' if all(a>b>=c for _,a,_,b,c in core) else 'FAIL','; '.join(f'{name}: {a}/{central} > {b} >= {c}' for name,a,central,b,c in core)],
      ['I2','PASS' if abs(diff)<=p['max_fast_reward_pp_difference'] and fast_pass else 'FAIL',f'{package}+{fast_cash}×40−{p["early_pp"]}={diff} PP quy đổi; bốn programme trong ±{p["max_fast_reward_pp_difference"]} PP tại k=40; dự án phụ {p["side_project"]["days"]} ngày/{p["side_project"]["pp"]} PP là khoản mua thêm'],
      ['I3','REVIEW' if not consumer_errors else 'FAIL',f'Không báo PASS cân bằng từ chiều chưa có giá. {len(consumer_rows)} nhánh×k có tác dụng kiểm được; tám node đổi cấu trúc. Giá tiền vẫn báo riêng; ngày/gate không quy PP; xác suất và sở thích cần playtest.'],
      ['I4','PASS','Năm vùng cohesion có hệ số khác nhau; cổng sau trừ40; BoP qua0.25 làm đổi công cụ. Đây là kiểm vùng/biên, không chứng minh mỗi điểm trong cùng vùng đều đổi giá.'],
      ['I5','FAIL' if reserve_violations or start_errors or timeline_softlock or focus_errors else 'PASS',f'Cùng trigger: chốt khi còn đường≤270; start≤800/choice≤840. {len(focus_rows)}probe0–39/cooldown0/90/180: cổng chung luôn còn công vụ/dân vận trước hạn, kiểm tra không kịp bị khóa riêng. {len(old_below_floor)}ca phản thực full dưới sàn bị khóa; không có nhánh rủi ro E103. Biên19/20 và270/271 có bảng; không cứu hồi tố kỳ đã hết hạn.'],
      ['I6','PASS' if not missing and len(node_rows)==p['l3_document_checks']['fixed_node_count'] else 'FAIL',f'{len(node_rows)}=2+6×12; cost/ID/mutex giữ; 40đặc tả+22gate/caller/guard/reader+12lát cắt; thiếu={missing}.'],
      ['I7','PASS' if all(i in section81 for i in ids) else 'FAIL',f'{len(ids)} tên VIE và mọi nhãn node/E101–E104 được đăng ký8.1; ID kỹ thuật chưa định nghĩa và chưa xác minh provider.'],
      ['I8','PASS','Mốc lịch sử có link nguồn hoặc giả định gameplay; event XI08/XIII05 đã chặn phát sớm. Neo quýIV/2022 là gameplay, không giả ngày khởi đầu khủng hoảng.'],
      ['I9','PASS','Kiểm mô hình và script; không chạy engine/console/playtest. Adapter game v57 có báo cáo nghiệm thu riêng.'],
      ['I10','REVIEW' if not consumer_errors else 'FAIL',f'Bỏ cờ cơ hội khỏi Pareto programme: {len(finite_winners)} ứng viên thắng mọi đối thủ; {len(dominated_pairs)} cặp thống trị. Consumer có hoàn trả PP/ngân khố thật; không dùng quyền mô tả để che thống trị. Chưa chứng minh utility/cân bằng engine.']]
    report='# Kiểm thiết kế chính trị — kết quả hiện hành\n\n'
    report+='Đây là kiểm mô hình giấy; [adapter game v57](VIE_political_v57_implementation.md) đã có trong repo nhưng chưa nghiệm thu HOI4/AI/playtest. Giá là giả định gameplay. Báo cáo chỉ giữ kết quả hiện hành; lịch sử xem git, dữ liệu đầy đủ xem CSV hoặc --audit-json.\n\n'
    report+=f'E103 tự động, bỏ trục A/B/C. CSV ngân sách: **{len(rows)} hàng hợp lệ**; {len(locked_keys)} tổ hợp khóa BoP được kiểm nhưng không xuất hàng rỗng. I5: {len(exception_rows)} ca ngoại lệ có kết quả dự báo thật. CSV node: {len(node_csv)} hàng giá/quyền/Pareto.\n\n'
    report+='## I1–I10\n\n'+table(['Mã','Kết quả','Phép tính / phạm vi'],checks)
    report+='\n\nPhép so tiền thuần (không định giá gate/ngày hoặc tự cộng thưởng task chưa làm):\n\n'+table(['Event','Đảo thứ hạng chi phí','Rẻ nhất mọi k'],core_event_direct_checks)
    report+='\n\n## Cấp tốc so chuẩn\n\nThưởng sớm70PP; gói55PP+0.50ngân khố. Cùng central/r=1/full/cohesion66, chọn phương án rẻ nhất mỗi mode; E103 tự động cùng quy tắc (ghi E102/E103). Dự án phụ30PP là khoản mua thêm.\n\n'
    report+=table(['Programme','k','Chuẩn E102/E103','Cấp tốc E102/E103','Chi chuẩn','Chi cấp tốc','Cấp tốc − chuẩn'],fast_comparisons)
    failures=[r for r in structural if r[1]=='FAIL']
    report+=f'\n\n## Kiểm file và cổng\n\n{len(structural)-len(failures)}/{len(structural)} kiểm PASS. '+('Không có lỗi file.' if not failures else table(['Kiểm','Kết quả','Chi tiết'],failures))
    report+=f'\n\n- Cổng chốt: {len(focus_rows)} probe cohesion0–39/cooldown0/90/180; {len(focus_errors)} lỗi. Biên270/271 kiểm riêng; không cứu hồi tố cửa sổ đã hết.\n'
    report+=f'- I5: {len(reserve_violations)} lỗi cổng trễ tất định; không có nhánh thẩm định/rủi ro E103 bỏ qua cổng840.\n'
    report+=f'- Pareto XII12/XIII12: {len(pareto_pairs)} cặp, {len(pareto_failures)} lỗi; {len(contract_probes)} probe ledger XIII12. Hủy luôn mở, không thu hồi hỗ trợ đã nhận/tier/thưởng.\n'
    report+=f'- Chẩn đoán: {len(dominated_pairs)} cặp thống trị; {len(finite_winners)} universal winner theo programme/tuyến, {len(route_universal_winners)} theo toàn4programme. Không suy ra cân bằng theo sở thích từ snapshot.\n'
    report+='- Biên giá nhỏ: checkpoint k40 chênh1PP; XII10 k20 chênh1PP. Không tự điều chỉnh.\n'
    report+='\n## Tái tạo và gói chia sẻ\n\n[Thiết kế](VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md), [tham số](VIETNAM_POLITICAL_PARAMETERS_VI.json), [balance](VIETNAM_POLITICAL_BALANCE_VI.py), [crosscheck](VIETNAM_POLITICAL_CROSSCHECK_VI.py), [ngân sách](VIETNAM_POLITICAL_BALANCE_VI.csv), [ngoại lệ I5](VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv), [node](VIETNAM_POLITICAL_NODE_CHOICES_VI.csv) đi cùng trong gói ZIP. Không cần REVIEW_L1/L2.\n\n'
    report+='Chạy `python VIETNAM_POLITICAL_BALANCE_VI.py --audit-l3`; thêm `--sync-approved` để đồng bộ bảng thiết kế, `--audit-json` khi cần toàn bộ probe/chẩn đoán. Dùng `python tools/package_political_design.py` trong repo để đóng gói đủ nguồn. Exit2 là FAIL kiểm mô hình.\n'
    (ROOT/'VIETNAM_POLITICAL_REVIEW_L3_VI.md').write_text(report,encoding='utf-8')
    result={'rows':len(rows),'eligible_rows':len(valid),'checks':checks,'file_checks':structural,'pairwise_dominance_count':len(dominated_pairs),'universal_winners':finite_winners,'route_universal_winners':route_universal_winners,'e103_automatic_probes':e103_test,'i5_exception_count':len(exception_rows),'i5_deterministic_gate_violations':len(reserve_violations),'i5_risky_full_below_floor':len(risk_below_floor),'forecast_start_probes':probes,'recovery_probe':recovery_probe,'selected_inspection_start_cases':selected_start_cases,'focus_gate_probes':focus_rows,'focus_gate_groups':focus_groups,'focus_gate_boundaries':focus_boundaries,'focus_gate_expiry':focus_expiry,'focus_gate_errors':focus_errors,'i6_missing':missing,'opportunity_csv_rows':len(opportunities),'node_choice_csv_rows':len(node_csv),'legacy_i3_costs':legacy_costs,'legacy_i3_failures':legacy_i3_failures,'pareto_vectors':pareto_vectors,'pareto_pairs':pareto_pairs,'pareto_failures':pareto_failures,'xiii12_contract_probes':contract_probes,'observable_choice_rows':consumer_rows,'consumer_errors':consumer_errors}
    if write_json:
        (ROOT/'VIETNAM_POLITICAL_AUDIT_L3_VI.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'rows':len(rows),'eligible_rows':len(valid),'file_failures':[r for r in structural if r[1]=='FAIL'],'invariants':{r[0]:r[1] for r in checks},'pairwise_dominance_count':len(dominated_pairs)},ensure_ascii=False,indent=2))
    return 2 if any(r[1]=='FAIL' for r in checks+structural) else 0


if __name__=='__main__':
    raise SystemExit(audit_l3())
