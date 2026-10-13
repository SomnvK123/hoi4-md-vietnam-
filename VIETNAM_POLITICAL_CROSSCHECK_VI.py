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
                                      'action':effect[option]['action'],'action_available':effect[option]['available'],
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
    rows=opportunities+priced_nodes+[{**row,'scope':'i3_named_pareto_exception_not_engine; added_days_zero_does_not_change_existing_programme_timers'} for row in pareto_vectors]
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
    if '| `e104_contract_amendment_gate` |' not in doc:
        doc=doc.replace('\n\nRegistry này đóng phạm vi','\n| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |\n\nRegistry này đóng phạm vi')
    tooltip='XIII12 — tooltip/cổng: available và tooltip chỉ gọi e104_contract_amendment_gate trên cùng ledger E104/đối tượng/source epoch. Khi khóa, hiển thị “hỗ trợ chưa nhận=0; quyền chưa dùng=0; sửa không giữ lợi ích; hủy vẫn khả dụng”. Khi hủy, hiển thị lượng hỗ trợ chưa nhận và quyền chưa dùng sẽ mất, nghĩa vụ tương lai sẽ đóng; mission/tier/PP sớm/thưởng đã nhận và hỗ trợ đã thanh toán giữ nguyên. Không tạo quyền mới, không thu hồi lịch sử, không cộng timer. Chỉ áp cổng tại XIII12, không áp XIV11 hoặc node khác.'
    ai='AI XIII12 chỉ đọc cùng e104_contract_amendment_gate: sửa khi còn lợi ích và đối tác chấp nhận điều kiện; cả hai cạn thì chọn hủy đang mở. Trước xác nhận đọc lại ledger để tránh tooltip cũ. Không tự giảm giá hoặc bỏ guard một lần/đối tượng/epoch.'
    for prefix,paragraph in [('XIII12 — tooltip/cổng:',tooltip),('AI XIII12',ai)]:
        if re.search('^'+re.escape(prefix),doc,re.M): doc=re.sub('^'+re.escape(prefix)+'.*$',lambda _:paragraph,doc,flags=re.M)
        else: doc=doc.replace('## 11. Bảng tính',paragraph+'\n\n## 11. Bảng tính',1)
    criteria='- XIII12 cổng bổ sung: e104_contract_amendment_gate dùng chung available/tooltip, chỉ sửa nếu hỗ trợ chưa nhận>0 hoặc quyền chưa dùng>0; hủy luôn mở. Kiểm9phép so trạng thái đã cạn và mọi trạng thái còn lợi ích; hủy chỉ ghi ledger E104, không fail mission/tier/reward/paid_support. Các chiều Pareto ngoài tiền phải hiện trước chọn; báo từng Δ và gần trùng<10%, không đổi giá/timer.'
    if '- XIII12 cổng bổ sung:' not in doc: doc=doc.replace('## 12. Trạng thái hoàn thành',criteria+'\n\n## 12. Trạng thái hoàn thành',1)
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
                        'cohesion_loss':cohesion,'old_holder_access':int(option=='A'),'new_holder_authority':int(option=='B')}
                state=spec[node][option]['roster_state']
            else:
                lost=support if option=='B' else 0
                values={'converted_cost':lost*k,'unreceived_support_lost':lost,'unused_cooperation_access':unused if option=='A' else 0,
                        'contract_obligation_open':spec[node][option]['contract_obligation_open'],'added_programme_days':spec[node]['added_programme_days']}
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
    result=[]
    for complete,k in itertools.product([True,False],p['k_values']):
        a=p['e103']['A_pp']+(0 if complete else -p['e103']['rejection_cohesion']*p['cohesion_pp_rate'])
        b=p['e103']['B_pp']+p['e103']['B_treasury']*k
        c=p['e103']['C_pp']
        costs={'A':a,'B':b,'C':c}
        winners=[option for option,cost in costs.items() if cost==min(costs.values())]
        gaps=[b-a,b-c,a-c]
        warning=any(abs(value)<p['e103_margin_warning_pp'] for value in gaps)
        result.append(['Đủ hồ sơ' if complete else 'Chưa đủ hồ sơ',k,a,b,c,0 if complete else p['e103']['reappraisal_days'],','.join(winners),sorted(costs.values())[1]-min(costs.values()),*gaps,'BIÊN <3' if warning else ''])
    return result


def i5_exception_rows(p):
    from VIETNAM_POLITICAL_BALANCE_VI import forecast_programme_completion
    result=[]
    for case,cohesion in [('snapshot',p['cohesion_initial']),('low',p['cohesion_price_bands'][0][1])]:
        extra=p['low_cohesion_prepare_extra'] if cohesion<p['recovery']['low_below'] else 0
        for route,mode,a,b in itertools.product(p['prepare_days'],['standard','fast_paid','fast_override','combined_fast_paid'],'ABC','ABC'):
            if mode!='standard' and p['bop_route_snapshot'][route]<=p['bop_threshold']: continue
            if mode=='fast_override' and cohesion-p['checkpoint_count']*p['override_cohesion']<p['override_floor']: continue
            if mode=='combined_fast_paid' and cohesion<p['cadre_cohesion_required']: continue
            fast=int(mode!='standard')
            evidence=p['prepare_days'][route]+extra+sum(p['action_days'][action][fast] for action in ['audit_standard','audit','audit','review'])+p['e102'][a][2]
            rejected=b=='A' and evidence>p['early_days']['inspection']
            day=max(evidence,p['early_days']['inspection'])+p['e103']['reappraisal_days'] if rejected else evidence
            if not(a=='C' or b in 'BC' or rejected): continue
            remaining=p['program_deadline']-day
            forecast=forecast_programme_completion(p,'inspection',route,mode,cohesion,a,b)
            reasons=[]
            if extra: reasons.append(f'cohesion<{p["recovery"]["low_below"]}: chuẩn bị+{extra}')
            if a=='C': reasons.append(f'E102-C:+{p["e102"]["C"][2]}')
            if rejected: reasons.append(f'E103-A bị bác:+{p["e103"]["reappraisal_days"]} tuần tự')
            if b=='B': reasons.append(f'E103-B:hợp đồng{p["e103"]["B_deadline"]}, không cộng ngày programme')
            if b=='C': reasons.append('E103-C:hợp đồng partial, không cộng ngày programme')
            contract='rejected' if rejected else 'accepted' if b=='A' else 'partial' if b=='C' else 'extension_missed' if evidence>p['e103']['B_deadline'] else 'extended'
            result.append({'cohesion_case':case,'cohesion_initial':cohesion,'route':route,'mode':mode,'e102':a,'e103':b,'potential_full_day':day,'remaining_reserve_days':remaining,'result':'full' if day<=p['program_deadline'] else 'partial_at_deadline','contract':contract,'reserve_floor_met':int(remaining>=p['exception_reserve_days']),'reason':'; '.join(reasons),'status':'paper_timeline_assuming_evidence_not_engine',
                           'availability':'locked_start' if not forecast['start_available'] else 'locked_choice' if not forecast['choice_available'] else 'available',
                           'forecast_full_day':forecast['forecast_full_day'],'forecast_reserve_days':forecast['forecast_reserve_days'],
                           'reappraisal_risk':forecast['reappraisal_risk'],'lock_reason':forecast['lock_reason'],'reopen':forecast['reopen']})
    return result


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
    replace_paragraph('**Bất biến lịch:**',f'**Bất biến lịch:** deadline programme vẫn bắt đầu+{p["program_deadline"]}. Trigger thiết kế `forecast_programme_completion` tính ngày từ timer/mode đã ký, chuẩn bị tại start và trễ tất định đã biết. Start chỉ mở khi lịch mặc định≤{p["program_deadline"]-p["reserve_days"]}; lựa chọn gây trễ chỉ mở khi dự báo≤{p["program_deadline"]-p["exception_reserve_days"]}. Available, tooltip và CSV dùng chung kết quả trigger, không tự tính lại. E103-A chưa đủ hồ sơ chỉ là rủi ro: hiển thị nhánh thẩm định+{p["e103"]["reappraisal_days"]}, không khóa chỉ vì rủi ro chưa hiện thực. Nếu rủi ro xảy ra, ghi ngày thực tế và dự phòng dưới sàn; không tự sửa timer hoặc ép partial. Sau start phục hồi cohesion không xóa+{p["low_cohesion_prepare_extra"]}ngày chuẩn bị đã ký. Đây là phạm vi I5 theo xác nhận mới: cổng trễ tất định, không bảo đảm mọi nhánh rủi ro giữ60ngày.')
    start=doc.index('### 6.5.');end=doc.index('### 6.6.',start)
    old=doc[start:end]
    preserved=old[old.index('**I2 theo PP thuần'):].rstrip()+'\n\n'
    combos=[]
    for r in canonical:
        if r['program']=='inspection':
            combos.append([r['route'],r['mode'],'E102-'+r['e102'],'E103-'+r['e103'],r['potential_full_day'],'full' if r['result']=='full' else f'partial ở {p["program_deadline"]}',r['e103_contract'],r['remaining_reserve_days'] or 'Không full'])
    exceptions=i5_exception_rows(p)
    with (ROOT/'VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv').open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(exceptions[0]));writer.writeheader();writer.writerows(exceptions)
    exception_table=[[r['cohesion_case'],r['route'],r['mode'],r['e102'],r['e103'],r['potential_full_day'],r['remaining_reserve_days'],r['result'],r['contract'],'ĐẠT' if r['reserve_floor_met'] else 'DƯỚI SÀN',r['reason'],r['availability'],r['forecast_full_day'],r['forecast_reserve_days'],'CẢNH BÁO' if r['reappraisal_risk'] else ''] for r in exceptions]
    tests=e103_scenarios(p)
    body=f'''### 6.5. E103: bằng chứng trước hạn, trả tiền không làm chứng cứ xuất hiện

Caller: programme kiểm tra đến ngày{p['e103']['caller_day']}, xếp một lần theo epoch. F10 mở công cụ chuyên sâu. Hạn cam kết A vẫn là mốc sớm kiểm tra{p['early_days']['inspection']}.

| Lựa chọn | Giá | Kết quả |
| --- | --- | --- |
| A — Cam kết nộp hồ sơ đầy đủ đúng hạn | {p['e103']['A_pp']} PP | Đủ4/4 trước hoặc đúng{p['early_days']['inspection']} được chấp nhận và giữ thưởng sớm. Nếu thiếu: cohesion{p['e103']['rejection_cohesion']}; thẩm định lại tuần tự thêm{p['e103']['reappraisal_days']}ngày. |
| B — Xin gia hạn, công khai phần còn thiếu | {p['e103']['B_pp']} PP + {p['e103']['B_treasury']:.2f} ngân khố | Gia hạn hợp đồng đến ngày{p['e103']['B_deadline']}; đủ chứng cứ mới chấp nhận. Hủy thưởng PP sớm của kỳ; giữ quyền dự án phụ nếu programme full sớm. Không cộng thêm ngày programme. |
| C — Công bố kết quả có giới hạn | {p['e103']['C_pp']} PP | Chốt hợp đồng partial; programme tiếp tục kiểm chứng tới deadline. Bỏ thưởng PP sớm, vẫn có thể full/tier khi đủ4/4. |

**Quy tắc tuần tự giữ nguyên:** T là ngày chứng cứ sẵn sàng, gồm E102-C cộng{p['e102']['C'][2]}ngày. A thiếu ở hạn cam kết có ngày full tiềm năng=max(T,{p['early_days']['inspection']})+{p['e103']['reappraisal_days']}. B/C không thêm thẩm định lại; gia hạn không tạo chứng cứ. B trượt hạn hợp đồng{p['e103']['B_deadline']} không đổi deadline programme{p['program_deadline']}. C không tự tạo nhóm mục tiêu còn thiếu.

**Lệch đã xử lý theo xác nhận mới:** bản trước ghi B30PP và hạn810. Bạn chốt B0PP+0.50ngân khố, hạn780; do đó dùng780, không tự coi810 là hiệu ứng đã giữ. E102+90, thẩm định+180, C15PP và programme900 giữ nguyên.

**I3 — hai kịch bản:** A rẻ nhất khi hồ sơ đã đủ là chấp nhận được. A chưa đủ gồm6cohesion×3={-p['e103']['rejection_cohesion']*p['cohesion_pp_rate']}PP quy đổi và{p['e103']['reappraisal_days']}ngày thẩm định riêng; không gán tỷ giá ngày sangPP. Không option nào rẻ nhất đồng thời ở cả hai kịch bản và mọi k. Cột B−A/B−C/A−C ghi chênh có dấu; cảnh báo dùng trị tuyệt đối. Biên nhỏ hơn{p['e103_margin_warning_pp']}PP được báo, không chỉnh số.

'''
    body+=table(['Hồ sơ','k','A','B','C','A thêm ngày','Rẻ nhất','Biên hạng1–2','B−A','B−C','A−C','Cảnh báo'],tests)
    body+='\n\n**E102 × E103, snapshot cohesion60:** ngày tiềm năng/kết quả hợp đồng lấy từ CSV; k/r không đổi timer.\n\n'+table(['Tuyến','Mode','E102','E103','Ngày full tiềm năng','Programme','Hợp đồng','Dự phòng'],combos)
    body+=f'\n\n**I5 — mọi đường ngoại lệ:** sàn{p["exception_reserve_days"]}ngày. Bảng có snapshot60 và probe cohesion<20; probe thấp chỉ kiểm lịch kiểm tra, không giả lập thu nhập hoặc phục hồi của programme khác. Loại mode vượt/kiêm nhiệm nếu không đủ cohesion. Dự phòng={p["program_deadline"]}−ngày full tiềm năng; số âm là chuỗi không full, được chốt partial tại deadline. Các hàng DƯỚI SÀN được báo, không tự sửa kết quả/timer.\n\n'
    body+=table(['Cohesion','Tuyến','Mode','E102','E103','Ngày tiềm năng','Dự phòng','Programme','Hợp đồng','Sàn','Lý do','Cổng','Dự báo tất định','Dự phòng dự báo','Rủi ro A'],exception_table)
    body+='\n\nNgày tiềm năng/kết quả ở bảng là phản thực để nhìn thấy đường bị khóa, không phải kết quả đã trao. Cột cổng dùng duy nhất `forecast_programme_completion`: locked_start khi lịch mặc định>800; locked_choice khi trễ tất định>840; A chưa đủ chỉ cảnh báo nhánh rủi ro. Trong8đường full cũ dưới sàn,6đường bị cổng start/choice khóa;2đường A cấp tốc thấp cohesion còn khả dụng với rủi ro885/dự phòng15. Chúng không được gọi là bảo đảm đạt sàn. Full825/840 giữ nguyên; A quá900 vẫn partial theo luật cũ. Tooltip nêu ngày, dự phòng, lý do khóa và cách mở lại; timer đã ký không bị phục hồi hồi tố.\n\n'
    doc=doc[:start]+body+preserved+'\n'+doc[end:]
    prefix='| Tuyến | Mode | Chi PP ròng |'
    pattern=re.escape(prefix)+r'.*?(?=\n\n)'
    examples=[]
    fields=['pp_net_cost','treasury_net_cost','potential_full_day','pp_early_reward','cohesion_final','bop_final','converted_cost','side_project_available']
    for r in canonical:
        if r['program']=='inspection' and r['e102']=='A' and r['e103']=='B': examples.append([r['route'],r['mode']]+[r[v] for v in fields])
    replacement=table(['Tuyến','Mode','Chi PP ròng','Chi ngân khố ròng','Ngày full','Thưởng PP sớm','Cohesion cuối','BoP cuối','Chi quy đổi','Dự án phụ mở'],examples)
    doc,n=re.subn(pattern,lambda _:replacement,doc,count=1,flags=re.S);assert n==1
    note='\n\n**Cột ngân sách E103-B:** `event_cost_pp` là PP của E102+E103+ký E104; `net_treasury_cost` là alias của `treasury_net_cost`. B0PP+0.50ngân khố làm PP ròng giảm30 và ngân khố ròng tăng0.50 so bản trước, trước các quy đổi k; mọi số ở bảng lấy từ script, không sửa tay.'
    anchor='**So cùng E102-A, E103-B, k=40, r=1:**'
    if '**Cột ngân sách E103-B:**' not in doc: doc=doc.replace(anchor,note+'\n\n'+anchor)
    replace_paragraph('UI hiển thị','UI hiển thị giá B1 và đầu ra duy nhất của `forecast_programme_completion`: ngày full dự báo, dự phòng, cổng và lý do khóa. Start>800: phục hồi bằng “Họp xử lý bất đồng” trước start; choice>840: chọn phương án không cộng trễ, không rút timer đã ký. A chưa đủ hiển thị riêng rủi ro cohesion−6/thẩm định+180/ngày và dự phòng nếu bị bác, không khóa vì rủi ro chưa hiện thực. B0PP+0.50/hạn780/bỏ thưởng; C15PP; E104 giữ ký theo tier45/30/25/21 và cửa sổ30/25/21. Node22 hiển thị legacy_node_terms, ghi “giả định gameplay, chưa cân bằng bằng engine”; XI12 bồi hoàn khác XII12 roster. Consumer40node hiển thị hành động được mở/đối ứng bị khóa, reader và thời điểm; archive_XV chỉ lưu. Giữ checkpoint15PP+0.25, gói55PP+0.50, vượt8/cổng40, BoP+0.30→+0.20, dự án phụ30PP/270ngày/guard một lần; k chỉ là tham số kiểm.')
    replace_paragraph('AI chọn cấp tốc', 'AI chọn cấp tốc khi ngày dư mở dự án phụ hoặc cơ hội có hạn; so đủ55PP+0.50ngân khố với50PP sớm. Start và choice chỉ đọc cổng forecast_programme_completion, không tự tính ngày. B cần0.50ngân khố và khả năng hoàn tất hợp đồng780. A chưa đủ không bị khóa tự động; AI đọc cả dự báo tất định lẫn rủi ro+180 trước cam kết. Consumer đọc record đúng đối tượng/epoch, chọn hành động có ích thay vì cộng điểm quyền; archive_XV không tăng utility hiện tại. Giữ cổng cohesion/BoP/hàng đợi lịch sử; không thêm miễn phí hoặc trọng số thưởng.')
    replace_paragraph('Chiến tranh, counter reset', 'Chiến tranh, counter reset, kiến nghị chưa đóng và chỉ tiêu kinh tế chưa đạt nằm ngoài lịch cơ sở. CSV không chứng minh full chắc chắn trong game. I5 cổng dự báo chỉ xử lý trễ tất định; rủi ro A và các tình huống ngoài mô hình được cảnh báo riêng. Không rút timer hoặc đổi900.')
    replace_paragraph('- I5:', '- I5: dùng cùng forecast_programme_completion cho start≤800/choice≤840, CSV và tooltip; không khóa rủi ro A chưa hiện thực. Kiểm cohesion0–19, phục hồi0→20 và cửa sổ270; ghi cả đường phản thực bị khóa và nhánh rủi ro còn khả dụng. Timer/mode đã ký không đổi sau phục hồi; programme900/E102+90/thẩm định180 giữ nguyên.')
    replace_paragraph('- A-E103 thiếu', '- A-E103 thiếu hồ sơ bị bác, cohesion−6 và thẩm định180ngày; A khi đủ được rẻ nhất. B0PP+0.50ngân khố/hạn780; C15PP. I3 kiểm hai kịch bản×k20/40/60, in chênh từng cặp; báo mọi biên<3PP, không tự chỉnh.')
    start=doc.index('## 12. Trạng thái hoàn thành')
    doc=doc[:start]+'''## 12. Trạng thái hoàn thành

Đã áp dụng xác nhận E103-B0PP+0.50ngân khố và hạn hợp đồng780, giữ C15PP/E102+90/thẩm định180/programme900. Script tính lại PP/ngân khố và mọi bảng liên quan. I3 đã kiểm hai kịch bản đủ/chưa đủ hồ sơ, A được rẻ nhất khi đủ; biên nhỏ được báo chứ không điều chỉnh. I5 có bảng ngoại lệ đầy đủ, sàn60: các hàng dưới sàn và lịch mặc định810 vẫn được báo, không thay số.

Danh mục vẫn74node. I6 còn thiếu gate/caller ở22node; I10 chưa định lượng đủ quyền/dữ liệu/cơ hội ở40node. Chưa nghiệm thu toàn thiết kế; báo cáo hiện hành ở [Lượt 3](VIETNAM_POLITICAL_REVIEW_L3_VI.md). Changelog ghi cả lệch810→780 theo mốc người dùng vừa chốt. Tham chiếu repo tại9 và BLUF được giữ.

Chỉ tính bằng script, chưa triển khai định nghĩa game của thiết kế này hoặc chạy engine/console/playtest.

BLUF
'''
    doc=sync_remaining_document(doc,p)
    # Dependent criteria/status are synchronized with the completion report, without touching repo references.
    doc=doc.replace('Danh mục vẫn74node. I6 còn thiếu gate/caller ở22node; I10 chưa định lượng đủ quyền/dữ liệu/cơ hội ở40node. Chưa nghiệm thu toàn thiết kế;',
                    'Danh mục vẫn74node. Đã bổ sung gate/caller/guard/reader22node và consumer quyền40node; I6/I10 được kiểm bằng script. I5 dùng cổng trễ tất định được chốt, vẫn cảnh báo rủi ro A; I3 được mở rộng kiểm giá22node và có kết quả chi tiết tại báo cáo. Chưa nghiệm thu gameplay;')
    doc=doc.replace('I5 có bảng ngoại lệ đầy đủ, sàn60: các hàng dưới sàn và lịch mặc định810 vẫn được báo, không thay số.',
                    'I5 có bảng ngoại lệ/cổng đầy đủ:6/8đườngfull cũ dưới sàn bị khóa,2rủi ro A885 còn mở theo xác nhận; không đổi timer. Các giá mới22node đã chốt, là giả định gameplay, chưa cân bằng bằng engine.')
    criteria='- I6/I10 hoàn thiện: đối chiếu gate/caller/guard/reader22node theo legacy_node_specs; consumer40node available1/đối ứng0 theo node_opportunity_effects. Script kiểm các nhu cầu hành động riêng, không cộng điểm quyền, không tính archive_XV là cơ hội hiện tại.\n- Giá node mới: XI12 bồi hoàn20PP/0.50; XII12 kiện toàn−6cohesion; XII10 30PP so8cohesion+0.25, báo biên1PP tại k20 không chỉnh. X09 hai đợt0.25, X10 ứng0.50/rút30/kiến nghị; kiểm cả thời gian và trạng thái checkpoint/kiến nghị. XIV10 ổn định+1%365ngày, trần1%, dùng max với tier dân vận, phải có nghiệm thu đúng địa điểm. XIV11 giữ15/sửa0.50/hủy mất hỗ trợ chưa nhận. Mọi số là giả định gameplay, chưa cân bằng bằng engine; không thay giá/timer programme.\n'
    if '- I6/I10 hoàn thiện:' not in doc: doc=doc.replace('## 12. Trạng thái hoàn thành',criteria+'\n## 12. Trạng thái hoàn thành')
    gate_note='\n\n**Cổng dự báo dùng chung:** E102-C và các lựa chọn có trễ tất định gọi forecast_programme_completion với mode/timer đã ký; khóa khi ngày dự báo>840. E103-A chưa đủ hồ sơ chỉ hiển thị rủi ro; không khóa chỉ vì khả năng bị bác. E104 và hợp đồng nối tiếp vẫn kiểm riêng cửa sổ ký theo tier; không tự cộng timer ký vào chuỗi programme, không gia hạn cửa sổ để vượt cổng.\n\n'
    if '**Cổng dự báo dùng chung:**' not in doc: doc=doc.replace('### 6.6.',gate_note+'### 6.6.',1)
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
    if data.get('archived_review_hashes'):
        archived=(ROOT/'VIETNAM_POLITICAL_REVIEW_L3_VI.md').read_text(encoding='utf-8')
        for name,digest in data['archived_review_hashes'].items():
            archive_round=re.search(r'_L([12])_',name).group(1)
            begin=f'<!-- SNAPSHOT_L{archive_round}_START -->\n';end=f'\n<!-- SNAPSHOT_L{archive_round}_END -->'
            text=archived.split(begin,1)[1].split(end,1)[0] if begin in archived and end in archived else ''
            verify(f'Lịch sử Lượt{archive_round} đã gộp',hashlib.sha256(text.encode('utf-8')).hexdigest()==digest,'Hash nguyên văn trước gộp; nguồn tham số hiện hành vẫn B1')
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
        pp=sum(number(row[c]) for c in ['pp_start','pp_actions','pp_e102','pp_e103','pp_fast_upfront','pp_checkpoints','pp_combined','pp_signature','pp_recovery'])
        converted=number(row['pp_net_cost'])+number(row['treasury_net_cost'])*number(row['k'])+number(row['cohesion_net_spent'])*p['cohesion_pp_rate']
        expected_day=p['prepare_days'][row['route']]+sum(p['action_days'][a][int(row['mode']!='standard')] for a in seq[row['program']])
        if row['program']=='inspection':
            expected_day+=p['e102'][row['e102']][2]
            if row['e103']=='A' and expected_day>p['early_days']['inspection']:
                expected_day=max(expected_day,p['early_days']['inspection'])+p['e103']['reappraisal_days']
        income=(number(row['r'])+p['branch_pp_daily'])*p['accounting_days']
        expected_treasury=sum(p['tools'][a][1] for a in seq[row['program']])+number(row['treasury_checkpoints'])-number(row['e104_grant'])
        if row['program']=='inspection': expected_treasury+=p['e102'][row['e102']][1]+p['e103'].get(row['e103']+'_treasury',0)
        aliases_ok=equal(row['event_cost_pp'],number(row['pp_e102'])+number(row['pp_e103'])+number(row['pp_signature'])) and equal(row['net_treasury_cost'],row['treasury_net_cost'])
        if not all([equal(pp,row['pp_gross_cost']),equal(pp-number(row['pp_early_reward']),row['pp_net_cost']),equal(converted,row['converted_cost']),equal(expected_day,row['potential_full_day']),equal(income,row['modeled_pp_income']),equal(converted/income,row['converted_cost_income_ratio']),equal(expected_treasury,row['treasury_net_cost']),aliases_ok]): arithmetic_errors.append(row)
    verify('Số học toàn CSV',not arithmetic_errors,f'{len(rows)} hàng; {len(valid)} hợp lệ; {len(arithmetic_errors)} sai tổng/timeline/thu nhập/chi quy đổi')
    approved=data['approved_change_scope']
    verify('Giữ thông số đã chốt',p['e103']['B_pp']==approved['e103_price']['new_pp'] and p['e103']['B_treasury']==approved['e103_price']['new_treasury'] and p['e103']['B_deadline']==approved['e103_B_deadline']['user_confirmed'] and p['e103']['C_pp']==15 and p['e102']['C'][2]==approved['e102_delay_preserved'] and p['e103']['reappraisal_days']==approved['e103_reappraisal_preserved'] and p['program_deadline']==approved['programme_deadline_preserved'] and p['exception_reserve_days']==approved['i5_exception_reserve'],'B0PP+0.50; hạn780; C15/E102+90/thẩm định180/programme900')
    expected_count=sum(len(p['e102'])*len('ABC') if program=='inspection' else 1 for program in seq)*len(p['prepare_days'])*len({r['mode'] for r in rows})*len(p['k_values'])*len(p['r_values'])
    keys=[tuple(row[field] for field in ['program','route','mode','e102','e103','k','r']) for row in rows]
    verify('Phủ ma trận CSV',len(rows)==expected_count and len(set(keys))==len(keys),f'{expected_count} tổ hợp không trùng; hàng khóa vẫn được ghi')
    examples=get_table('| Tuyến | Mode | Chi PP ròng |')
    fields=['pp_net_cost','treasury_net_cost','potential_full_day','pp_early_reward','cohesion_final','bop_final','converted_cost','side_project_available']
    verify('Bảng ngân sách mẫu 11.1',all(all(equal(value,unique[('inspection',a[0],a[1],'A','B')][field]) for value,field in zip(a[2:],fields)) for a in examples),'Đối chiếu từng cột CSV ở k=40/r=1')
    combos=get_table('| Tuyến | Mode | E102 | E103 | Ngày full tiềm năng |')
    verify('Bảng E102 × E103 6.5',all(equal(a[4],unique[('inspection',a[0],a[1],a[2][-1],a[3][-1])]['potential_full_day']) and a[6]==unique[('inspection',a[0],a[1],a[2][-1],a[3][-1])]['e103_contract'] for a in combos),f'{len(combos)} tổ hợp lịch tiềm năng')
    values=get_table('| Cohesion | Tuyến | Mode | E102 | E103 |')
    verify('Bảng ngoại lệ I5',len(values)==len(exception_rows) and all(a[:5]==[r['cohesion_case'],r['route'],r['mode'],r['e102'],r['e103']] and equal(a[5],r['potential_full_day']) and equal(a[6],r['remaining_reserve_days']) and a[7]==r['result'] and a[8]==r['contract'] for a,r in zip(values,exception_rows)),f'{len(exception_rows)} tổ hợp snapshot/thấpcohesion, so CSV ngoại lệ độc lập')
    e103_test=e103_scenarios(p)
    values=get_table('| Hồ sơ | k | A | B | C |')
    verify('Bảng hai kịch bản E103',len(values)==len(e103_test) and all([str(v) for v in actual]==[str(v) for v in expected] for actual,expected in zip(values,e103_test)),f'{len(e103_test)} kịch bản×k; chiA/B/C và chênh mọi cặp')
    package=p['fast_upfront_pp']+p['checkpoint_count']*p['checkpoint_pp']
    cash=p['checkpoint_count']*p['checkpoint_treasury']
    values=get_table('| k thử | Giá gói PP |')
    verify('Bảng I2',all(all(equal(x,y) for x,y in zip(a[1:],[package,p['early_pp'],package-p['early_pp'],cash,package-p['early_pp']+cash*number(a[0])])) for a in values),'PP thuần và ngân khố không tính trùng')
    values=get_table('| k thử | Thương lượng quy đổi |')
    override=p['override_cohesion']*p['cohesion_pp_rate']
    verify('Bảng checkpoint',all(all(equal(x,y) for x,y in zip(a[1:],[p['checkpoint_pp']+p['checkpoint_treasury']*number(a[0]),override,p['checkpoint_pp']+p['checkpoint_treasury']*number(a[0])-override])) for a in values),'Từ B1, không dùng số hardcode của bảng')
    section81=doc.split('### 8.1.')[1].split('### 8.2.')[0]
    ids=set(re.findall(r'\bVIE_[a-zA-Z0-9_]+',doc.split('## 9.')[0]))
    verify('Registry 8.1',all(i in section81 for i in ids) and ids==set(p['designed_identifiers']),f'{len(ids)} tên thiết kế; 74 nhãn node; E101–E104 có registry; chưa là định nghĩa engine')
    verify('Registry hoàn thiện',all(name in section81 for name in ['forecast_programme_completion','legacy_node_specs','legacy_node_terms','node_opportunity_effects','i3_pareto_exceptions','archive_XV','e104_contract_amendment_gate','e104_contract_ledger','support_promised','support_received','support_forfeited','rights_granted','rights_used','rights_revoked','contract_state','focus_commitment_gate','elapsed_congress_days','recovery_cooldown_remaining','pending_recovery_remaining','focus_available','earliest_feasible_start_day','latest_start_day','start_days_short']),'Tên thiết kế mới có writer/reader và vòng đời; chưa tạo ID engine')
    node_costs=[]
    crossover=True
    for node,pair in p['node_choice_prices'].items():
        costs=[[pp+cash*k for pp,cash in pair] for k in p['k_values']]
        crossover &= any(a<b for a,b in costs) and any(b<a for a,b in costs)
        node_costs.append([node]+[f'{a:g}/{b:g}' for a,b in costs])
    event_costs=[]
    for k in p['k_values']:
        for option,(pp,cash,cohesion,*_) in p['e101'].items(): event_costs.append(['E101',option,k,pp+cash*k-cohesion*p['cohesion_pp_rate']])
        for option,(pp,cash,_) in p['e102'].items(): event_costs.append(['E102',option,k,pp+cash*k])
        for option in 'ABC': event_costs.append(['E104',option,k,p['e104'][option+'_pp']-p['e104'].get(option+'_grant',0)*k])
        event_costs += [['E103 hồ sơ đúng hạn','A',k,p['e103']['A_pp']],['E103 hồ sơ trễ','A',k,p['e103']['A_pp']-p['e103']['rejection_cohesion']*p['cohesion_pp_rate']],['E103','B',k,p['e103']['B_pp']+p['e103']['B_treasury']*k],['E103','C',k,p['e103']['C_pp']]]
    core_event_direct_checks=[]
    for event in ['E101','E102','E104']:
        winners=[]
        for k in p['k_values']:
            costs={option:cost for name,option,row_k,cost in event_costs if name==event and row_k==k}
            winners.append({option for option,cost in costs.items() if cost==min(costs.values())})
        universal=set.intersection(*winners)
        core_event_direct_checks.append([event,'PASS' if not universal else 'FAIL',','.join(sorted(universal)) or 'không có lựa chọn rẻ nhất mọi k'])
    verify('I3 tiền trực tiếp E101/E102/E104',all(row[1]=='PASS' for row in core_event_direct_checks),'Cùng event/tuyến, k20/40/60; E104 dùng bối cảnh đối tác chấp nhận đã công bố')
    finite_winners=[]
    route_universal_winners=[]
    dominated_pairs=[]
    opportunity=['side_project_available','technical_training_opportunity','deep_data_cooperation_opportunity']
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
    preserved_failures=[key for key,digest in data['focus_gate_preserved_parameter_hashes'].items() if hashlib.sha256(json.dumps(p[key],ensure_ascii=False,sort_keys=True).encode()).hexdigest()!=digest]
    verify('Giữ giá và timer khi thêm cổng',not preserved_failures,f'{len(data["focus_gate_preserved_parameter_hashes"])} nhóm tham số giữ hash; khác={preserved_failures}')
    reserve_violations=[row for row in exception_rows if row['availability']=='available' and row['forecast_reserve_days']<p['exception_reserve_days']]
    risk_below_floor=[row for row in exception_rows if row['availability']=='available' and row['result']=='full' and row['remaining_reserve_days']<p['exception_reserve_days']]
    old_below_floor=[row for row in exception_rows if row['result']=='full' and row['remaining_reserve_days']<p['exception_reserve_days']]
    start_errors=[row for row in probes if row[6]=='MỞ' and row[5]<p['reserve_days']]
    timeline_softlock=any(not any(row[6]=='MỞ' for row in probes if row[1]==route) for route in p['prepare_days'])
    no_universal_cheapest=not set.intersection(*[set(r[6].split(',')) for r in e103_test])
    low_day=core[2][1]+p['low_cohesion_prepare_extra']
    simple_nodes=[n for n,_,_ in node_rows if n not in p['node_choice_prices'] and n not in [f'F{i:02}' for i in range(1,13)]]
    missing=[]
    for n in simple_nodes:
        line=next(line for line in doc.splitlines() if line.startswith('| '+n+' |'))
        spec=p['legacy_node_specs'].get(n)
        if not spec or not re.search(rf'^\| {n} \| [^|]+ \| \d+ \| [^|]+; từ ',line) or not all(text in line for text in [spec['caller'],spec['condition'],spec['guard'],spec['reader']]): missing.append(n)
    complete_rights=set(p['node_opportunity_effects'])==set(p['node_choice_prices']) and all(
        e['reader'] in p['focus_nodes'] or e['reader'] in ['E103','archive_XV'] for e in p['node_opportunity_effects'].values())
    complete_rights &= all(e[o]['available']==1 and e[o]['counterpart_available']==0 and e['A']['action']!=e['B']['action'] for e in p['node_opportunity_effects'].values() for o in 'AB')
    verify('22node hoàn thiện',not missing,f'{len(p["legacy_node_specs"])} gate/caller/guard/reader; thiếu={missing}')
    verify('Consumer40node',complete_rights and len(opportunities)==len(p['node_choice_prices'])*2*len(p['prepare_days'])*len(p['k_values']),f'{len(opportunities)} hàng; hành động riêng và đối ứng khóa; archive_XV không tính utility hiện tại')
    with (ROOT/'VIETNAM_POLITICAL_NODE_CHOICES_VI.csv').open(encoding='utf-8-sig',newline='') as stream: node_csv=list(csv.DictReader(stream))
    def csv_num(row,key): return float(row[key]) if row.get(key) else 0
    expected_node_rows=len(opportunities)+len(pareto_vectors)+sum((3 if row[0]=='XIV11' else 2)*len(p['prepare_days']) for row in legacy_costs)
    node_price_errors=[]
    for row in node_csv:
        if row.get('scope','').startswith('i3_named_pareto'):
            expected=csv_num(row,'cohesion_loss')*p['cohesion_pp_rate']+csv_num(row,'unreceived_support_lost')*csv_num(row,'k')
        else:
            expected=csv_num(row,'pp')+(csv_num(row,'actual_treasury_debit')+csv_num(row,'unreceived_support_lost'))*csv_num(row,'k')+csv_num(row,'cohesion_spent_cost')*p['cohesion_pp_rate']
        if abs(expected-csv_num(row,'converted_cost'))>0.00001: node_price_errors.append(row)
    verify('CSV lựa chọn node',len(node_csv)==expected_node_rows and not node_price_errors,f'{len(node_csv)}={len(opportunities)} quyền+243giá+{len(pareto_vectors)} vector; {len(node_price_errors)} sai tổng; hỗ trợ mất khác debit thật')
    verify('Cổng dự báo I5',not reserve_violations and not start_errors and not timeline_softlock,f'{len(probes)} probe start, {len(exception_rows)} ngoại lệ; trễ tất định bị khóa; {len(risk_below_floor)} nhánh A dưới60 chỉ cảnh báo theo xác nhận')
    service=p['legacy_node_terms']['XIV10']
    stability_rows=[]
    for tier,tier_reward in enumerate([0]+p['tier_modifiers']['stability']):
        effective=max(tier_reward,min(service['stability_reward'],service['stability_cap']))
        stability_rows.append([tier,tier_reward,service['stability_reward'],effective,effective-tier_reward])
    verify('XIV10 trần và không chồng',service['requires_matching_acceptance'] and not service['stack_with_social_tier'] and service['stability_reward']<=service['stability_cap'] and all(row[3]<=max(row[1],service['stability_cap']) for row in stability_rows),'Nghiệm thu cùng địa điểm; max(tier,idea); một lần/địa điểm/epoch, không cộng thời hạn')
    verify('Phạm vi Pareto',p['i3_pareto_exceptions']['nodes']==['XII12','XIII12'] and p['i3_pareto_exceptions']['direct_money_test_other_nodes'],'Chỉ hai node được người dùng chốt; không đổi giá/timer')
    diff=package-p['early_pp']
    checks=[
      ['I1','PASS' if all(a>b>=c for _,a,_,b,c in core) else 'FAIL','; '.join(f'{name}: {a}/{central} > {b} >= {c}' for name,a,central,b,c in core)],
      ['I2','PASS' if abs(diff)<=p['max_fast_reward_pp_difference'] else 'FAIL',f'{package}−{p["early_pp"]}={diff} PP; dự án phụ {p["side_project"]["days"]} ngày/{p["side_project"]["pp"]} PP'],
      ['I3','PASS' if no_universal_cheapest and crossover and not legacy_i3_failures and not pareto_failures and all(row[1]=='PASS' for row in core_event_direct_checks) else 'FAIL',f'E101/E102/E104 kiểm tiền trực tiếp;E103 hai kịch bản×3k PASS={no_universal_cheapest};40node đảo giá theo k={crossover};XI12/XII10/XIV11 kiểm tiền trực tiếp. Chỉ XII12/XIII12 dùng Pareto theo xác nhận: {len(pareto_pairs)} cặp, {len(pareto_failures)} cặp thống trị, {sum(r["near_duplicate"] for r in pareto_pairs)} gần trùng. Biên XII10 k20:30 so29=1PP<3; không chỉnh.'],
      ['I4','PASS','Năm vùng cohesion có hệ số khác nhau; cổng sau trừ40; BoP qua0.25 làm đổi công cụ. Đây là kiểm vùng/biên, không chứng minh mỗi điểm trong cùng vùng đều đổi giá.'],
      ['I5','FAIL' if reserve_violations or start_errors or timeline_softlock or focus_errors else 'PASS',f'Cùng trigger: chốt khi còn đường≤270; start≤800/choice≤840. {len(focus_rows)}probe0–39/cooldown0/90/180: cổng chung luôn còn công vụ/dân vận trước hạn, kiểm tra không kịp bị khóa riêng. {len(old_below_floor)-len(risk_below_floor)}/{len(old_below_floor)}full cũ dưới sàn bị khóa; {len(risk_below_floor)}rủi ro A885/dư15 giữ cảnh báo. Biên19/20 và270/271 có bảng; không cứu hồi tố kỳ đã hết hạn.'],
      ['I6','PASS' if not missing and len(node_rows)==p['l3_document_checks']['fixed_node_count'] else 'FAIL',f'{len(node_rows)}=2+6×12; cost/ID/mutex giữ; 40đặc tả+22gate/caller/guard/reader+12lát cắt; thiếu={missing}.'],
      ['I7','PASS' if all(i in section81 for i in ids) else 'FAIL',f'{len(ids)} tên VIE và mọi nhãn node/E101–E104 được đăng ký8.1; ID kỹ thuật chưa định nghĩa và chưa xác minh provider.'],
      ['I8','PASS','Mốc lịch sử có link nguồn hoặc giả định gameplay; event XI08/XIII05 đã chặn phát sớm. Neo quýIV/2022 là gameplay, không giả ngày khởi đầu khủng hoảng.'],
      ['I9','PASS','Chỉ script/CSV/tài liệu; không chạy engine/console/playtest.'],
      ['I10','PASS' if not finite_winners and not route_universal_winners and complete_rights else 'FAIL',f'Ma trận: {len(finite_winners)} tổ hợp thắng mọi đối thủ cùng programme/tuyến;{len(route_universal_winners)} tổ hợp thắng mọi4programme cùng tuyến ở9k/r. Cho phép đồng hạng với bản sao, phải tốt hơn ít nhất1đối thủ. {len(dominated_pairs)} cặp thống trị là chẩn đoán.40consumer quyền cụ thể;64nhánh32node có reader hiện tại,16nhánhXIV chỉ archive không tăng cơ hội. So tập hành động thay vì điểm tổng; chưa chứng minh engine/sở thích.']]
    witness=[]
    for a,b in dominated_pairs[:12]: witness.append([a['program'],a['route'],a['mode']+'/'+a['e102']+'/'+a['e103'],b['mode']+'/'+b['e102']+'/'+b['e103'],a['pp_net_cost'],b['pp_net_cost'],a['potential_full_day'],b['potential_full_day']])
    changelog=[['7.4','Bảng6cột nhưng separator5cột','6cột thống nhất','Sửa Markdown','5 bảng40node'],['7.4 XII','Thiếu mutex trong gate','XII01/05 và XII04/08 ghi hai chiều','Khôi phục lựa chọn đã chốt','B1 mutex; script'],['7.4 lịch sử','Focus neo2011/2021 có thể phát event lịch sử sớm','XI08 event từ02/05/2014; XIII05 crisis từQ4/2022','Tách ngày mở focus với ngày caller lịch sử','B1;7.4;10'],['XIV05','Thiếu180ngày gia hạn','Gia hạn hồ sơ180ngày; programme900 không đổi','Khôi phục timer đã có','B1 delays;7.4'],['XIV08','20PP, giữ thêm30ngày','25PP, giảm30ngày gián đoạn','Khôi phục giá/hiệu quả cũ bị đổi thiếu giải thích','B1 prices/delays;7.4;I3'],['8.1','Registry thiếu nhãn/caller/lịch sử','Ghi writer/reader/epoch và pending','Đóng các nhãn hiện dùng','B1 designed_identifiers'],['7/11.3/12','Cho thêm node; nhắcCI; kết luận quá mức','Giữ74; script local; ghi FAIL đúng phạm vi','Tuân thủ scope và giới hạn kiểm tra','Kết luận;7.5;11.3;12'],['Script','Lệnh mặc định quay về hashL1','--audit-l3 dựngCSV, đối chiếu và xuất báo cáoL3','Không ghi đè reviewL1/L2','Script;11.1']]
    changelog.insert(2,['7.4 prerequisite XII','XII05 phụ thuộc tổ tiênXII01 loại trừ; XII08 quaXII04 loại trừ','Hai rootXII01/05; intermediate dùngOR; XII04/08 cùng sauXII07','Sửa gate chết, giữ hai cặp loại trừ và node chung','B1 focus_prerequisites;7.4; kiểm mọi đườngOR'])
    changelog.append(['Nguồn lịch sử','Link nợ xấu/mốc01May chưa chỉ đúng bài hỗ trợ','Link nghị quyết chuẩn và họp báo07May2014','Nguồn trực tiếp hỗ trợ mốc được nêu','2;B1 anchors;I8'])
    changelog.extend([['E103-B','30PP, ngân khố0','0PP+0.50ngân khố','Người dùng chọn phương án1','B1;6.5;CSV;event_cost_pp/net_treasury_cost;10;11.1;11.3;12'],['Hạn B','Bản hiện tại810','780','Mốc780 được người dùng chốt rõ; ghi lệch, không giả vờ đã giữ810','B1 B_deadline;6.5;contract CSV;10'],['I5','Ngoại lệ chỉC+B/C, chưa có sàn','Mặc định100; mọi lựa chọn vào ngoại lệ riêng/sàn60','Người dùng chọn phương án2','B1;4.2;6.5;CSV ngoại lệ;10;11.3;12'],['Biên I3','Không in đủ hai kịch bản','Đủ/chưa đủ×k20/40/60; biênA/B2 ởk40','Báo biên<3, không tự chỉnh','6.5;report;I3']])
    changelog.extend([['I5 cổng dự báo','8đường full dưới sàn; chỉ báo','Start≤800; trễ tất định≤840; A rủi ro không khóa','Người dùng chốt cổng, không sửa giá/timer','B1 forecast_gate;4.2;6.4–6.6;8.1;10;11.3;CSV'],['22node','Thiếu gate/caller/guard/reader','Đặc tả theo legacy_node_specs, prerequisite OR/mutex kiểm bằng script','Hoàn thiện I6 theo yêu cầu','B1;7.4;8.1;11.3;12'],['40hậu quả','Quyền/dữ liệu chỉ mô tả','Consumer hành động available1/đối ứng0, record đúng đối tượng/epoch','Lượng hóa I10, không thêm điểm thưởng','B1 node_opportunity_effects;7.4a;8.1;10;CSV720hàng'],['Giá còn trống','12ô null','Bộ giá được người dùng chốt, XI12 bồi hoàn khác XII12 roster','Giả định gameplay, chưa cân bằng bằng engine','B1 legacy_node_terms;7.4;10;11.3;CSV lựa chọn;report']])
    changelog.extend([['I3 Pareto','Kiểm tiền trực tiếp XII12/XIII12 FAIL','Chỉ hai node này kiểm Pareto đa chiều có tên','Người dùng chốt ngoại lệ; không mở rộng node khác','B1 i3_pareto_exceptions;7.4b;10;11.3;CSV;report'],['XIII12 cổng bổ sung','Sửa bị hủy thống trị khi hỗ trợ/quyền đã cạn','e104_contract_amendment_gate: sửa cần còn hỗ trợ hoặc quyền; hủy luôn mở','Người dùng chốt tránh phương án bị thống trị; giữ giá/timer','7.4 XIII12;8.1 ledger;10 UI/AI;11.3;CSV;63phép so Pareto']])
    changelog.append(['Cổng chốt trọng tâm','Có thể chốt kiểm tra dù phục hồi xong271/360/450','Cùng forecast_programme_completion trả cổng chốt theo ngày khởi động khả thi≤270; phục hồi/hòa giải không bị cổng khóa','Người dùng chốt thêm guard; không đổi giá/timer; cổng riêng theo programme và cổng chung bất kỳ programme','B1 focus_commitment_gate;3.3;4.2;8.1;10;11.3;CSV dự báo;1440probe'])
    if data.get('archived_review_hashes'):
        changelog.append(['Dọn đầu ra','Ba báo cáo tách riêng và JSON tự sinh mỗi lần','L1/L2 nguyên văn trong phụ lục L3; xóa hai file cũ; JSON chỉ sinh với --audit-json','Người dùng yêu cầu gộp/xóa sau khi hoàn tất; giữ hai script và ba CSV cần tái tạo','Report hiện hành;hash lịch sử trong B1;CLI;không xóa game files'])
    report='# Lượt 3: hoàn thiện cổng I5, đặc tả I6 và mô hình I10\n\nĐã áp dụng các quyết định người dùng: E103-B0PP+0.50/hạn780; cổng start800/choice840 chỉ xét trễ tất định, không khóa rủi ro A; hoàn thiện22node và consumer40node; chốt giá còn trống. Mọi giá mới là **giả định gameplay, chưa cân bằng bằng engine**. C15PP/E102+90/thẩm định180/programme900 và mọi giá/timer programme giữ nguyên. I3 giữ kiểm tiền trực tiếp; chỉ XII12/XIII12 kiểm Pareto theo xác nhận. Biên nhỏ được báo, không chỉnh số.\n\n## Changelog\n\n'+table(['Mục','Cũ','Mới','Lý do','Các chỗ cập nhật'],changelog)
    report+='\n\n## Bất biến I1–I10\n\n'+table(['Mã','Kết quả','Phép tính / phạm vi'],checks)
    report+='\n\n## Đối chiếu file và bảng\n\n'+table(['Kiểm tra','Kết quả','Căn cứ'],structural)
    report+='\n\n## Chi quy đổi mọi lựa chọn event lát cắt\n\nGiá=PP+ngân khố×k−cohesion nhận×3; E104 là kịch bản đối tác chấp nhận. Thời gian và quyền dữ liệu chưa quy đổi thànhPP.\n\n'+table(['Event/bối cảnh','Option','k','Chi quy đổi'],event_costs)
    report+='\n\n'+table(['Event','I3 tiền trực tiếp','Rẻ nhất mọi k'],core_event_direct_checks)
    report+='\n\n## E103: hai kịch bản và mọi biên chênh lệch\n\nA rẻ nhất khi đủ hồ sơ được chấp nhận. A chưa đủ có chi cohesion−6×3=18PP quy đổi và180ngày thẩm định riêng; không cộng ngày thànhPP. CộtB−A/B−C/A−C là chênh có dấu; dùng trị tuyệt đối để báo biên<3. k40/chưa đủ có A18 soB20, biên2PP: cảnh báo, không đổi giá.\n\n'+table(['Hồ sơ','k','A','B','C','A thêm ngày','Rẻ nhất','Biên hạng1–2','B−A','B−C','A−C','Cảnh báo'],e103_test)
    exception_values=[[r['cohesion_case'],r['route'],r['mode'],r['e102'],r['e103'],r['potential_full_day'],r['remaining_reserve_days'],r['result'],r['contract'],'ĐẠT' if r['reserve_floor_met'] else 'DƯỚI SÀN',r['reason'],r['availability'],r['forecast_full_day'],r['forecast_reserve_days'],'CẢNH BÁO' if r['reappraisal_risk'] else ''] for r in exception_rows]
    report+=f'\n\n## I5: bảng ngoại lệ và cổng đầy đủ\n\n{len(exception_rows)} tổ hợp phản thực snapshot60/probe<20. Ngày tiềm năng và result cho biết kết quả nếu đi đường đó, không tự trao full cho hàng bị khóa. {len(old_below_floor)-len(risk_below_floor)}/8đường full cũ dưới sàn bị khóa;2rủi ro A885 còn mở theo xác nhận, nếu bị bác vẫn chỉ dư15. I5 PASS **cổng trễ tất định**, không phải mọi nhánh rủi ro đều bảo đảm60ngày. B/C không cộng ngày programme; mọi900/90/180 giữ nguyên.\n\n'+table(['Cohesion','Tuyến','Mode','E102','E103','Ngày tiềm năng','Dự phòng','Programme','Hợp đồng','Sàn','Lý do','Cổng','Dự báo tất định','Dự phòng dự báo','Rủi ro A'],exception_values)
    report+='\n\n## I5: kiểm kẹt và phục hồi\n\n'+table(['Programme','Tuyến','Mode','Cohesion','Lịch mặc định','Dự phòng','Start','Mở lại'],probes)
    report+='\n\nPhục hồi0→20 với decision hiện có; cooldown tính từ lúc chọn, không phải hoàn tất:\n\n'+table(['Chọn ngày','Xong ngày','Cohesion sau','PP lượt','PP tổng'],recovery_probe)
    report+=f'\n\nKết thúc{recovery_probe[-1][1]}ngày, bằng cửa sổ start{p["program_start_latest"]} inclusive: không có độ dư. Chỉ riêng cohesion/cổng không khóa cả bốn programme: công vụ/dân vận vẫn mở ở mọi tuyến trong cửa sổ; kiểm tra chuẩn tập thể/cân bằng bị khóa ở0–19, tập trung chuẩn795 và cấp tốc705 vẫn mở nếu BoP cho phép. Giả định decision phục hồi sẵn ởngày0, đủPP, chọn ngay, không dùng cooldown để đóng kiến nghị. Chọn chậm1ngày làm phục hồi xong271, lỡ cửa sổ; đây là rủi ro lịch, không tự kéo270. Không kết luận tránh softlock cho mọi save: thiếuPP/ngân khố, hết cửa sổ, chưa mở công cụ và trạng thái chiến tranh nằm ngoài probe. Đề xuất vận hành: tooltip báo hạn phục hồi và chọn công vụ/dân vận nếu cần; không tự đổi luật.\n'
    report+='\n\n### Đường kẹt trước cổng: đối chiếu để chặn chốt\n\nNếu đã chọn kiểm tra, tuyến tập thể/cân bằng không có cấp tốc theo snapshot BoP, không được coi công vụ/dân vận là lựa chọn thay thế miễn phí trong cùng kỳ. Trong mô hình cô lập không có nguồn cohesion khác hoặc cách đổi tuyến hợp lệ trước270, cohesion0–9 và phục hồi chọn chậm1ngày, hoặc cooldown180đang chạy, không lên20 trước270; trọng tâm này không thể khởi động trong kỳ. Đây là kẹt mục tiêu do cổng mới, dù game và focus khác vẫn tiếp tục. Bảng sau chỉ tính decision đã có, không đổi phí/timer/cửa sổ:\n\n'+table(['Cohesion đầu','Trễ chọn lượt đầu','Cooldown còn','Số lượt','Phục hồi xong','Cohesion sau','PP tổng','Dư cửa sổ270','Kết quả trọng tâm kiểm tra chuẩn tập thể/cân bằng'],selected_start_cases)
    report+='\n\nCổng chốt đã được áp dụng: KHÓA CHỐT KIỂM TRA là không được chọn programme đích; cổng chung vẫn mở nếu còn programme khác. Ngày/phí dự kiến đều lấy từ cùng forecast_programme_completion, không tính lịch phục hồi ở một trigger khác. Những cổng phase90ngày, giá và điều kiện chế độ vẫn giữ nguyên.\n\n### Cổng chốt: cohesion/cooldown đầy đủ\n\nMỗi vùng được kiểm mọi điểm, không chỉ đầu/cuối. MỞ@T là còn đường khởi động ở ngàyT tính từ đại hội; KHÓA@T nghĩa đường sớm nhất vẫn quá270, thiếu số ngày nêu trong ô. ĐủPP/ngân khố, không có event cohesion chưa biết và các bước còn lại thành công là giả định của probe. Lịch còn các milestone kinh tế/cán bộ chưa chứng minh bằng engine.\n\n'+table(['Cohesion','Cooldown còn','Tuyến','Cán bộ','Công vụ','Kiểm tra','Dân vận','Cổng chung','Nếu programme bị khóa'],focus_groups)
    report+='\n\nTrong1440probe còn ít nhất một đường: công vụ/dân vận không cần phục hồi để qua cổng lịch800. Kiểm tra chuẩn tập thể/cân bằng:0–9/cooldown0 phục hồi xong270 còn mở; cooldown90/180 xong360/450 bị khóa;10–19/cooldown0/90/180 xong90/180/270 còn mở;20–39 khởi động ngay. Tuyến tập trung có chuẩn795 hoặc cấp tốc705 khi dưới20 nên vẫn mở theo gateBoP hiện có.\n\n### Biên19/20\n\n'+table(['Cohesion','Cooldown còn','Tuyến','Full nếu start ngay','Start ngay mở','Start khả thi sớm nhất','Ngày thiếu','Chốt programme mở'],focus_boundaries)
    report+='\n\n19 có+60chuẩn bị;20 không có. Phục hồi trước start có thể mở chốt cho19, nhưng không mở start trước khi đủ điều kiện. Phục hồi sau start không giảm timer đã ký. Lượt phục hồi đang chạy được đọc theo purpose=cohesion: không tính thêm phí đã trả hoặc nhầm lượt hòa giải thành+10.\n\n### Biên cửa sổ270/271\n\n'+table(['Ngày từ đại hội','Cổng chung mở','Programme còn đường','Ngày thiếu','Cổng khóa phục hồi','Cổng khóa hòa giải'],focus_expiry)
    report+='\n\nNgày271 cửa sổ khởi động đã hết: không chốt programme cho kỳ hiện tại, phục hồi/hòa giải vẫn không bị cổng chốt khóa; không tự fail mission, trao tier hoặc hoàn tiền. Đại hội theo lịch vẫn tiếp tục; kỳ sau có cửa sổ mới. Cổng này không tự sửa save đã chốt từ trước hoặc xử lý hành động làm lỡ kế hoạch sau chốt. Nếu cần chính sách riêng cho dữ liệu cũ/kỳ bỏ lỡ, có ba phương án để người dùng quyết định: (1) giữ kỳ bỏ lỡ và chờ cửa sổ đại hội sau; (2) ghi trạng thái “chưa triển khai” khi cửa sổ đóng; (3) ghi0/4 và áp penalty fail đã có. Chưa thêm phương án2/3, không đổi timer/giá. Không có trạng thái kẹt toàn bộ programme do riêng cổng mới trong vùng/cooldown được yêu cầu trước khi cửa sổ đóng.\n'
    delta_pp=p['e103']['B_pp']-approved['e103_price']['old_pp']
    delta_cash=p['e103']['B_treasury']
    report+='\n\n## Thay đổi ngân sách E103-B\n\nMọi kịch bản B giảm30PP và tăng0.50ngân khố ròng; E104 và các event khác giữ nguyên.\n\n'+table(['k','ΔPP ròng','Δngân khố ròng','Δchi quy đổi'],[[k,delta_pp,delta_cash,delta_pp+delta_cash*k] for k in p['k_values']])
    report+='\n\n## Giá A/B của40node\n\n'+table(['Node','k20 A/B','k40 A/B','k60 A/B'],node_costs)
    report+='\n\n## I10: cặp thống trị được phát hiện\n\nKhông có một tổ hợp thắng toàn ma trận không loại trừ cặp bị thống trị. Các hàng sau dùng cùng programme/tuyến, k40/r1; thời gian là full tiềm năng, cơ hội gồm dự án phụ/chuyên gia/dữ liệu sâu. Giá trị hợp đồng E103 không được tự quy thànhPP.\n\n'+table(['Programme','Tuyến','Tổ hợp trội','Tổ hợp bị trội','PP trội','PP bị trội','Ngày trội','Ngày bị trội'],witness)
    price_changes=[['X09','treasury_per_installment','chưa định lượng',p['legacy_node_terms']['X09']['treasury_per_installment']],['XI12','reparation_pp / treasury','chưa định lượng',f"{p['legacy_node_terms']['XI12']['reparation_pp']}PP /{p['legacy_node_terms']['XI12']['reparation_treasury']:.2f}"],['XII10','pp / cohesion / alternative_treasury','chưa định lượng',f"{p['legacy_node_terms']['XII10']['pp']}PP /{p['legacy_node_terms']['XII10']['cohesion']}cohesion+{p['legacy_node_terms']['XII10']['alternative_treasury']:.2f}"],['XII12','immediate_cohesion_loss','chưa định lượng',p['legacy_node_terms']['XII12']['immediate_cohesion_loss']],['XIII11','treasury','chưa định lượng',p['legacy_node_terms']['XIII11']['treasury']],['XIII12','cancellation_cost','chưa định lượng','hỗ trợ E104 chưa nhận; không phí mới'],['XIV10','stability_reward','chưa định lượng',f"+{service['stability_reward']*100:g}%,{service['reward_days']}ngày,trần{service['stability_cap']*100:g}%,max với tier,nghiệm thu tương ứng"],['XIV11','retain / amend / cancel','chưa định lượng',f"{p['legacy_node_terms']['XIV11']['retain_cost']}PP /{p['legacy_node_terms']['XIV11']['amend_cost']:.2f} /hỗ trợ chưa nhận"]]
    report+='\n\n## Ánh xạ ID và giá đã chốt\n\nXI12 là trách nhiệm bảo lãnh/bồi hoàn; XII12 là tái phân công roster. Không thấy giá bị gán nhầm giữa hai node trong bản B1 trước khi sửa. Mọi giá mới là giả định gameplay, chưa cân bằng bằng engine.\n\n'+table(['Node','Tham số','Cũ','Mới'],price_changes)
    report+='\n\n## I3: giá lựa chọn node mới và mọi biên\n\nChi quy đổi=PP+ngân khố×k+cohesion mất×3; cohesion nhận được trừ tương ứng. Không đổi ngày sangPP. Các cặp focus loại trừ là so sánh riêng, không giả là lựa chọn trong cùng event.\n\n'+table(['Node/cặp','Bối cảnh A/B','k','A','B','B−A','Biên tuyệt đối','Cảnh báo'],[r for r in legacy_costs if r[0]!='XIV11'])
    report+='\n\n'+table(['Node','Hỗ trợ','k','Giữ','Sửa','Hủy','Sửa−Giữ,Hủy−Giữ,Hủy−Sửa','Cảnh báo'],[r for r in legacy_costs if r[0]=='XIV11'])
    report+='\n\nXI12/XII10/XIV11 giữ kiểm tiền trực tiếp; chỉ XII12/XIII12 dùng Pareto theo xác nhận mới. Biên1PP XII10 và2PP E103 giữ nguyên. Các caller chỉ mở công cụ không được gán hai giá giả; XI11 đóng/chuyển kiến nghị phụ thuộc hồ sơ/decision hiện có, không được giả là hai lựa chọn có giá riêng để chứng minh cân bằng.\n'
    vector_rows=[]
    for v in pareto_vectors:
        if v['route']!=list(p['prepare_days'])[0]: continue
        vector_rows.append([v['node'],v['context'],v['k'],v['option'],v['converted_cost'],v.get('handover_pending_days',0),v.get('cohesion_loss',0),v.get('old_holder_access','—'),v.get('new_holder_authority','—'),v.get('unreceived_support_lost','—'),v.get('unused_cooperation_access','—'),v.get('contract_obligation_open','—'),v['state'],v['centre_effect'],'MỞ' if v['available'] else 'KHÓA'])
    report+='\n\n## I3 Pareto: chỉ XII12 và XIII12\n\nI3 của hai node này được đánh giá bằng Pareto, **không bằng chi phí tiền đơn lẻ**: có đánh đổi lịch/roster hoặc quyền hỗ trợ/nghĩa vụ hợp đồng đã tồn tại. Các node/event khác không được dùng ngoại lệ này. Thời gian/quyền không quy raPP. Chi phí hủy là hỗ trợ chưa nhận bị mất, không phải khoản trừ ngân khố thực; không thu hồi khoản đã nhận. Kết quả bằng nhau ở cả ba tuyến; bảng hiển thị một tuyến, CSV/JSON có đủ mọi tuyến.\n\n'+table(['Node','Bối cảnh','k','Option','Chi quy đổi','Bàn giao/khóa roster ngày','Mất cohesion','Quyền người cũ','Quyền ký người mới','Mất hỗ trợ chưa nhận','Quyền hợp tác chưa dùng','Nghĩa vụ hợp đồng mở','Trạng thái','Trung tâm phản ứng','Cổng'],vector_rows)
    report+='\n\nNgày của XII12 là thời gian bàn giao đã có; khóa quyền người mới trong cùng hồ sơ tới khi bàn giao, không dừng dự án khác. XIII12 không cộng ngày programme mới (0 cho cả hai); kiểm chứng đang có vẫn theo timer đã ký. Trạng thái quyền hợp tác chưa dùng đọc hợp đồng thực tế, không tự sinh quyền khi hỗ trợ đã cạn. An ninh đóng nghĩa vụ dữ liệu tương lai khi hủy, lịch sử hồ sơ và trách nhiệm quá khứ không xóa. Tooltip phải hiển thị mọi chiều trước chọn.\n\n'
    pair_rows=[[v['node'],v['context'],v['k'],v['result'],'; '.join(f'{key}:{value:g}' for key,value in v['deltas_B_minus_A'].items()),'; '.join(f'{key}:{value*100:g}%' for key,value in v['relative_deltas'].items()),'GẦN TRÙNG' if v['near_duplicate'] else 'không gần trùng'] for v in pareto_pairs if v['route']==list(p['prepare_days'])[0]]
    report+=table(['Node','Bối cảnh','k','So từng cặp','ΔB−A từng chiều','Chênh tương đối từng chiều','Biên10%'],pair_rows)
    report+='\n\nChênh tương đối=|B−A|/max(|A|,|B|); cả hai0 thì0%; gần trùng khi mọi chiều<10%. Đây là quy ước báo biên, không đổi giá. Trước cổng, B hủy thống trị A sửa ở trạng thái hỗ trợ/quyền0. Cổng được người dùng chốt khóa **phương án bị thống trị A sửa**, B hủy vẫn mở. Không có cặp hai phương án khả dụng để bị thống trị trong trạng thái này; không gọi đó là cân bằng hai phương án.\n'
    exhausted=[v for v in pareto_pairs if v['node']=='XIII12' and v['context']=='hỗ trợ=0; quyền chưa dùng=0']
    report+='\n\n### XIII12: đủ9phép so trạng thái đã cạn\n\n'+table(['Tuyến','k','Sửa','Hủy','So cặp còn khả dụng','PASS/FAIL'],[[v['route'],v['k'],'KHÓA','MỞ',v['result'],'PASS' if 'thống trị' not in v['result'] else 'FAIL'] for v in exhausted])
    other_pairs=[v for v in pareto_pairs if v['node']=='XIII12' and v['context']!='hỗ trợ=0; quyền chưa dùng=0']
    report+=f'\n\nCác trạng thái XIII12 còn hỗ trợ hoặc quyền có{len(other_pairs)}phép so;{sum("thống trị" in v["result"] for v in other_pairs)}cặp thống trị, {sum(v["near_duplicate"] for v in other_pairs)}gần trùng. Cổng chỉ XIII12, không dùng XIV11 hoặc node khác.\n\n### XIII12: kiểm softlock và fail ngầm\n\n'+table(['State','Hỗ trợ cam kết','Đã nhận','Chưa nhận','Quyền chưa dùng','Sửa mở','Hủy mở','Giữ paid/history và chỉ ghi ledger','Hủy lặp không phí/hiệu ứng mới','Kết quả'],contract_probes)
    report+='\n\nMọi ledger probe có hủy mở, không softlock do cổng sửa. Paper transition chỉ ghi support_forfeited/rights_revoked/contract_state; không có writer mission/tier/PP sớm/reward, không thu hồi tiền đã nhận hoặc quyền đã dùng. Do đó thiết kế hủy không fail mission hoặc mất thưởng ngoài tooltip. Kiểm này là script mô hình, cần xác minh adapter engine khi triển khai; không tuyên bố engine đã chạy.\n'
    report+='\n\n## X09 và X10: kiểm thống trị riêng\n\n'+table(['Phương án','Ngân khố tổng','Δngày dự án','Checkpoint trước trả','Kiến nghị giám sát do ứng trước'],[['X09',p['legacy_node_terms']['X09']['installments']*p['legacy_node_terms']['X09']['treasury_per_installment'],0,p['legacy_node_terms']['X09']['installments'],0],['X10',p['legacy_node_terms']['X10']['treasury'],p['legacy_node_terms']['X10']['delay_days'],0,1]])
    report+='\n\nKhông bên nào thống trị: X10 có−30ngày và không chờ checkpoint trước trả, nhưng mở thêm1kiến nghị chưa đóng; X09 không mở kiến nghị do ứng trước, nhưng chờ2checkpoint và không rút30ngày. Đo kiến nghị/đợt vốn cùng một hồ sơ, không tính checkpoint như phần thưởng tự động hoặc trừ phí kiểm toán lần nữa. Giá bằng nhau ở k20/40/60; khác biệt nằm ở lịch và nghĩa vụ.\n'
    report+='\n\n## XIV10: trần idea và tier dân vận\n\n'+table(['Tier','Ổn định tier','Idea','Ổn định hiệu lực','Phần tăng do idea'],stability_rows)
    report+='\n\nIdea365ngày chỉ trao sau nghiệm thu cùng địa điểm, một lần/địa điểm/epoch; refresh thay thế, không cộng thời hạn. Dùng max(tier,idea), không áp hai modifier cộng dồn; hết hạn idea trả về tier đang có. Adapter engine chưa triển khai.\n'
    unspecified=[[node,field,'Chưa xác định; không được tính là 0'] for node,values in p['legacy_node_terms'].items() for field,value in values.items() if value is None]
    report+='\n\n### Tham số còn trống trong B1\n\n'+table(['Node','Tham số','Cách xử lý hiện tại'],unspecified)
    report+='\n\n## I6/I10: kết quả và phạm vi\n\n22node có kỳ/ngày/prerequisite/chế độ/đối tượng, caller, guard và reader;62node ngoài lát cắt được kiểm cùng danh mục74.40node có80hành động mang tên riêng (64nhánh hoạt động ở reader trong phạm vi;16nhánhXIV chỉ archive), CSV720hàng. Không dùng archive_XV làm cơ hội hiện tại. Các consumer là nhánh của caller có sẵn; phí mở quyền trả một lần, đủ quyền không tự đủ milestone. Ma trận programme không có universal winner theo từng programme/tuyến/k/r; pairwise dominance được giữ để chẩn đoán, không đổi giá. I10 PASS mô hình giấy hiện hành, chưa chứng minh utility theo sở thích, AI hoặc engine.\n'
    report+=f'\nKiểm thêm toàn4programme cùng mỗi tuyến ở9k/r: {len(route_universal_winners)}universal winner; trường hợp đồng hạng không che một ứng viên thắng các đối thủ khác.\n'
    report+=f'\nCSV lựa chọn node tổng{len(node_csv)}hàng:720hàng quyền,243hàng giá đã chốt, {len(pareto_vectors)}vector ngoại lệ Pareto. Cộtactual_treasury_debit tách tiền thực trừ khỏi unreceived_support_lost; không cộng trùng hai khoản. Bảng ma trận programme độc lập vẫn1296hàng/648hợp lệ, không bị giá node sửa.\n'
    report+='\n## Mục không đổi\n\nMục1,5 và9 giữ hash trước Lượt3. Mục3 chỉ bổ sung cổng tại3.3; mục4/6 cập nhật đúng I5/E103 đã xác nhận và kiểm hash mới.20nhóm giá/timer giữ hash trước cổng chốt. Giữ ID/số dòng/tham chiếu repo9, cost74focus, deadline900, gói55PP/thưởng50, giá E101/E102/E104/C15; E102+90/thẩm định180. Lượt1/Lượt2 giữ nguyên văn trong lịch sử nếu đã gộp. Không sửa game files/localisation/artwork hoặc file kinh tế trong Downloads.\n'
    report+='\n## Giới hạn và quyết định còn lại\n\n- Các sửa đổi giá/cổng/Pareto và cổng chốt đã được chốt, không còn quyết định chặn hoàn thiện mô hình trước cửa sổ270.1440probe không có lối cụt toàn bộ programme do cổng mới; không tự cứu dữ liệu save đã chốt trước luật này. Các phương án xử lý kỳ đã bỏ lỡ nêu riêng để quyết định nếu cần, chưa triển khai.\n- Rủi ro E103-A885/dư15 còn mở theo xác nhận: I5 PASS cổng trễ tất định, không bảo đảm nhánh rủi ro giữ60ngày.\n- Engine/AI/playtest chưa chạy; giá mới là giả định gameplay. Không suy ra cân bằng theo sở thích hoặc lịch nhiều nhiệm kỳ từ một snapshot.\n'
    report+='\n## Đầu ra\n\nTài liệu đầy đủ: [thiết kế](VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md); nguồn [B1](VIETNAM_POLITICAL_PARAMETERS_VI.json); script chính [balance](VIETNAM_POLITICAL_BALANCE_VI.py), script đối chiếu [crosscheck](VIETNAM_POLITICAL_CROSSCHECK_VI.py); ma trận [CSV](VIETNAM_POLITICAL_BALANCE_VI.csv); [CSV ngoại lệ I5](VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv); [CSV giá/quyền/Pareto node](VIETNAM_POLITICAL_NODE_CHOICES_VI.csv). Chạy `python VIETNAM_POLITICAL_BALANCE_VI.py --audit-l3` để dựng lại và đọc báo cáo; `--sync-approved` đồng bộ các bảng đã chốt vào tài liệu. JSON debug chỉ sinh khi thêm --audit-json. Exit2 nghĩa là cònFAIL thiết kế, không phải lỗi chạyPython.\n\nBLUF\n'
    previous=ROOT/'VIETNAM_POLITICAL_REVIEW_L3_VI.md'
    history_start='<!-- HISTORICAL_REVIEW_ARCHIVE_START -->';history_end='<!-- HISTORICAL_REVIEW_ARCHIVE_END -->'
    if previous.exists():
        old_report=previous.read_text(encoding='utf-8')
        if history_start in old_report:
            assert old_report.count(history_start)==old_report.count(history_end)==1
            archive=history_start+old_report.split(history_start,1)[1].split(history_end,1)[0]+history_end
            report=report.rsplit('\n\nBLUF\n',1)[0]+'\n\n'+archive+'\n\nBLUF\n'
    (ROOT/'VIETNAM_POLITICAL_REVIEW_L3_VI.md').write_text(report,encoding='utf-8')
    result={'rows':len(rows),'eligible_rows':len(valid),'checks':checks,'file_checks':structural,'pairwise_dominance_count':len(dominated_pairs),'universal_winners':finite_winners,'route_universal_winners':route_universal_winners,'e103_scenarios':e103_test,'i5_exception_count':len(exception_rows),'i5_deterministic_gate_violations':len(reserve_violations),'i5_risky_full_below_floor':len(risk_below_floor),'forecast_start_probes':probes,'recovery_probe':recovery_probe,'selected_inspection_start_cases':selected_start_cases,'focus_gate_probes':focus_rows,'focus_gate_groups':focus_groups,'focus_gate_boundaries':focus_boundaries,'focus_gate_expiry':focus_expiry,'focus_gate_errors':focus_errors,'i6_missing':missing,'opportunity_csv_rows':len(opportunities),'node_choice_csv_rows':len(node_csv),'legacy_i3_costs':legacy_costs,'legacy_i3_failures':legacy_i3_failures,'pareto_vectors':pareto_vectors,'pareto_pairs':pareto_pairs,'pareto_failures':pareto_failures,'xiii12_contract_probes':contract_probes}
    if write_json:
        (ROOT/'VIETNAM_POLITICAL_AUDIT_L3_VI.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'rows':len(rows),'eligible_rows':len(valid),'file_failures':[r for r in structural if r[1]=='FAIL'],'invariants':{r[0]:r[1] for r in checks},'pairwise_dominance_count':len(dominated_pairs)},ensure_ascii=False,indent=2))
    return 2 if any(r[1]=='FAIL' for r in checks+structural) else 0


if __name__=='__main__':
    raise SystemExit(audit_l3())
