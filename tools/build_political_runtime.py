"""Build the game adapter from the reviewed political parameters; preserve other branches."""
from pathlib import Path
from datetime import date,timedelta
import json,math,re

ROOT=Path(__file__).resolve().parents[1]
P={k:v['value'] for k,v in json.loads((ROOT/'VIETNAM_POLITICAL_PARAMETERS_VI.json').read_text(encoding='utf-8'))['parameters'].items()}
LOC={};EFFECTS=[];EVENTS=['add_namespace = vie_pol_runtime'];DECISIONS=[];TRIGGERS=[]
def block_end(text,start):
    depth=0
    for match in re.finditer(r'"(?:\\.|[^"\\])*"|#[^\n]*|[{}]',text[start:]):
        token=match.group()
        if token=='{': depth+=1
        elif token=='}':
            depth-=1
            if depth==0:return start+match.end()
    raise ValueError('Unclosed block')
def replace_block(text,key,body):
    match=re.search(r'\b'+re.escape(key)+r'\s*=\s*\{',text)
    assert match,key
    return text[:match.start()]+key+' = {\n'+body+'\n}'+text[block_end(text,match.start()):]
def effect_body(text):
    body=text[text.index('{')+1:text.rfind('}')].strip()
    # Rebuild an existing guarded adapter without stacking another wrapper.
    if body.startswith('if = {') and block_end(body,0)==len(body):
        limit=re.search(r'\blimit\s*=\s*\{',body)
        if limit: body=body[block_end(body,limit.start()):body.rfind('}')].strip()
    return body
def definition(name,body): EFFECTS.append(name+' = {\n'+body+'\n}\n')
def condition(name,body): TRIGGERS.append(name+' = {\n'+body+'\n}\n')
def funds(pp=0,cash=0,cohesion=0):
    return (f'NOT = {{ political_power < {pp} }}\n' if pp else '')+(f'NOT = {{ check_variable = {{ treasury < {cash} }} }}\n' if cash else '')+(f'NOT = {{ check_variable = {{ VIE_leadership_cohesion < {40+cohesion} }} }}\n' if cohesion else '')
def money(value):return f'set_temp_variable = {{ treasury_change = {value:g} }}\nmodify_treasury_effect = yes\n' if value else ''
def cohesion(value):return f'set_temp_variable = {{ cohesion_add = {value:g} }}\nVIE_modify_cohesion = yes\n' if value else ''
def pay(pp=0,cash=0,loss=0):return (f'add_political_power = {-pp:g}\n' if pp else '')+money(-cash)+cohesion(-loss)
def guard(body,limit):return 'if = {\nlimit = { '+limit+' }\n'+body+'}\n'
def decision(name,title,desc,available,body,cost=0,visible=None,days=None,finish=''):
    LOC[name]=title;LOC[name+'_desc']=desc
    extra=f'days_remove = {days}\nremove_effect = {{\n{finish}\n}}\n' if days else ''
    DECISIONS.append(f'{name} = {{\nicon = generic_political_actions\nallowed = {{ original_tag = VIE }}\nvisible = {{ {visible or available} }}\navailable = {{ {available} }}\ncost = {cost}\ncomplete_effect = {{\n{body}\n}}\n{extra}ai_will_do = {{ base = 50 }}\n}}\n')
def event(number,title,desc,options,trigger='always = yes',hidden=False):
    name=f'vie_pol_runtime.{number}'
    if hidden:
        EVENTS.append(f'country_event = {{\nid = {name}\nhidden = yes\nis_triggered_only = yes\ntrigger = {{ {trigger} }}\nimmediate = {{\n{options}\n}}\n}}\n')
        return
    LOC[name+'.t']=title;LOC[name+'.d']=desc
    text=f'country_event = {{\nid = {name}\ntitle = {name}.t\ndesc = {name}.d\npicture = GFX_report_event_generic_read_write\nis_triggered_only = yes\ntrigger = {{ {trigger} }}\n'
    for label,caption,available,body in options:
        LOC[name+'.'+label]=caption
        text+=f'option = {{\nname = {name}.{label}\ntrigger = {{ {available} }}\n'+guard(body,trigger+' '+available)+'}\n'
    EVENTS.append(text+'}\n')

focus_path=ROOT/'common/national_focus/VIE_md_focus.txt'
tree=focus_path.read_text(encoding='utf-8-sig')
focuses={}
for match in re.finditer(r'\bfocus\s*=\s*\{',tree):
    text=tree[match.start():block_end(tree,match.start())]
    identifier=re.search(r'\bid\s*=\s*(\w+)',text).group(1)
    focuses[identifier]=text
IDS={}
for identifier in focuses:
    match=re.match(r'VIE_(ix|xiii|xiv|xii|xi|x)(\d\d)_',identifier)
    if match: IDS[match.group(1).upper()+match.group(2)]=identifier
for i,stem in enumerate(['review_public_administration','publish_responsibility_rules','consult_provincial_leaders','establish_project_command','publish_land_compensation_plan','audit_state_enterprise_guarantees','publish_term_action_plan','pilot_one_stop_service','train_successor_candidates','publish_procurement_audits','establish_grievance_hearings','review_program_delivery'],1):IDS[f'F{i:02}']='VIE_'+stem
assert set(IDS)==set(P['focus_nodes'])
def reward(node,body):
    identifier=IDS[node];text=focuses[identifier]
    focuses[identifier]=replace_block(text,'completion_reward',f'log = "[GetDateText]: [Root.GetName]: Focus {identifier}"\n'+body)
def available(node,extra):
    identifier=IDS[node];text=focuses[identifier]
    match=re.search(r'\bavailable\s*=\s*\{',text);assert match
    old=text[match.end():block_end(text,match.start())-1]
    # Idempotent: do not append the same dynamic gate on repeated generation.
    if extra.strip() not in old: focuses[identifier]=replace_block(text,'available',old+'\n'+extra)

# Clock uses a single saved, country-scoped event chain, avoiding global on_action scope.
definition('VIE_politics_runtime_init','''if = { limit = { NOT = { has_country_flag = VIE_politics_clock_running } }
VIE_init_political_system = yes
set_country_flag = VIE_politics_clock_running
country_event = { id = vie_pol_runtime.1 days = 1 }
}''')
definition('VIE_politics_new_term','''set_variable = { VIE_congress_elapsed = 0 }
add_to_variable = { VIE_programme_epoch = 1 }
clr_country_flag = VIE_programme_active
clr_country_flag = VIE_programme_selected
clr_country_flag = VIE_programme_early_full
clr_country_flag = VIE_last_programme_full
''')

# Startup cost, preparation and completion forecasts read the same snapshot.
costbody='set_variable = { VIE_programme_start_cost = 40 }\n'
for tier,discount in [(3,15),(2,10),(1,5)]:
    costbody+=('if' if tier==3 else 'else_if')+f' = {{ limit = {{ NOT = {{ check_variable = {{ VIE_tier_cadre < {tier} }} }} }} set_variable = {{ VIE_programme_start_cost = {40-discount} }} }}\n'
for idx,(lo,hi,factor) in enumerate(P['cohesion_price_bands']):
    costbody+=('if' if idx==0 else 'else_if')+f' = {{ limit = {{ NOT = {{ check_variable = {{ VIE_leadership_cohesion < {lo} }} }} check_variable = {{ VIE_leadership_cohesion < {hi+1} }} }}\n'
    for j,base in enumerate([25,30,35,40]):
        costbody+=('if' if j==0 else 'else_if')+f' = {{ limit = {{ check_variable = {{ VIE_programme_start_cost = {base} }} }} set_variable = {{ VIE_programme_start_cost = {math.ceil(base*factor)} }} }}\n'
    costbody+='}\n'
costbody+='''set_variable = { VIE_programme_prepare_days = 30 }
if = { limit = { VIE_is_central_zone = yes } set_variable = { VIE_programme_prepare_days = 15 } }
if = { limit = { check_variable = { VIE_leadership_cohesion < 20 } } add_to_variable = { VIE_programme_prepare_days = 60 } }
set_variable = { VIE_programme_forecast_standard = VIE_programme_prepare_days }
set_variable = { VIE_programme_forecast_fast = VIE_programme_prepare_days }
if = { limit = { has_country_flag = VIE_programme_inspection }
add_to_variable = { VIE_programme_forecast_standard = 720 }
add_to_variable = { VIE_programme_forecast_fast = 630 }
} else = {
add_to_variable = { VIE_programme_forecast_standard = 630 }
add_to_variable = { VIE_programme_forecast_fast = 540 }
}'''
definition('VIE_politics_forecast',guard(costbody,'NOT = { has_country_flag = VIE_programme_active }'))
condition('VIE_politics_can_select','''has_country_flag = VIE_congress_resolved
check_variable = { VIE_last_congress > 8 }
NOT = { has_country_flag = VIE_programme_active }
NOT = { has_country_flag = VIE_programme_selected }
NOT = { check_variable = { var = VIE_programme_used_term value = VIE_last_congress compare = equals } }
NOT = { check_variable = { VIE_congress_elapsed > 270 } }''')
condition('VIE_politics_can_select_inspection','''VIE_politics_can_select = yes
OR = { VIE_is_central_zone = yes NOT = { check_variable = { VIE_leadership_cohesion < 20 } } }
''')
decision('VIE_change_unstarted_programme','Đổi trọng tâm trước khởi động','Chưa thu phí khởi động thì có thể đổi trọng tâm trong cửa sổ270ngày. Không đổi chương trình đã chạy hoặc kéo dài hạn khởi động. Hồi phục gắn kết trước khi chọn kiểm tra nếu không có mode khởi động hợp lệ.','has_country_flag = VIE_programme_selected NOT = { has_country_flag = VIE_programme_active } NOT = { check_variable = { VIE_congress_elapsed > 270 } }','clr_country_flag = VIE_programme_selected\n'+''.join('clr_country_flag = VIE_programme_'+program+'\n' for program in ['cadre','admin','inspection','social']))
for mode,surcharge in [('standard',0),('fast_paid',55),('fast_override',25)]:
    budget='OR = {\n'
    for tier,base in [(0,40),(1,35),(2,30),(3,25)]:
        for lo,hi,factor in P['cohesion_price_bands']:
            budget+=f'AND = {{ check_variable = {{ VIE_tier_cadre = {tier} }} NOT = {{ check_variable = {{ VIE_leadership_cohesion < {lo} }} }} check_variable = {{ VIE_leadership_cohesion < {hi+1} }} '+funds(math.ceil(base*factor)+surcharge,.5 if mode=='fast_paid' else 0,16 if mode=='fast_override' else 0)+' }\n'
    budget+='}\n'
    forecast='VIE_programme_forecast_standard' if mode=='standard' else 'VIE_programme_forecast_fast'
    condition('VIE_politics_can_launch_'+mode,'''has_country_flag = VIE_programme_selected
NOT = { has_country_flag = VIE_programme_active }
NOT = { check_variable = { VIE_congress_elapsed > 270 } }
'''+f'NOT = {{ check_variable = {{ {forecast} > 800 }} }}\n'+('VIE_is_central_zone = yes\n' if mode!='standard' else '')+budget)
    definition('VIE_politics_begin_'+mode,'VIE_politics_forecast = yes\n'+guard(f'''VIE_politics_forecast = yes
set_temp_variable = {{ VIE_launch_charge = VIE_programme_start_cost }}
add_to_temp_variable = {{ VIE_launch_charge = {surcharge} }}
multiply_temp_variable = {{ VIE_launch_charge = -1 }}
add_political_power = VIE_launch_charge
set_country_flag = VIE_programme_active
clr_country_flag = VIE_programme_selected
set_country_flag = VIE_mode_{mode}
set_variable = {{ VIE_programme_used_term = VIE_last_congress }}
set_variable = {{ VIE_programme_elapsed = 0 }}
set_variable = {{ VIE_programme_targets_met = 0 }}
set_variable = {{ VIE_programme_step = 0 }}
set_variable = {{ VIE_programme_forecast_days = {forecast} }}
clr_country_flag = VIE_programme_job_running
clr_country_flag = VIE_programme_review_done
clr_country_flag = VIE_programme_early_full
clr_country_flag = VIE_last_programme_full
clr_country_flag = VIE_last_programme_partial
clr_country_flag = VIE_last_programme_fail
clr_country_flag = VIE_e102_choice_pending
clr_country_flag = VIE_e102_choice_resolved
clr_country_flag = VIE_e102_data_access_unlocked
clr_country_flag = VIE_e103_progress_notified
clr_country_flag = VIE_e104_offer_shown
set_variable = {{ VIE_programme_gdp_target = gdp_per_capita }}
multiply_variable = {{ VIE_programme_gdp_target = 1.04 }}
VIE_politics_read_corruption = yes
set_variable = {{ VIE_programme_corruption_baseline = VIE_corruption_current }}
'''+money(-.5 if mode=='fast_paid' else 0)+('VIE_bop_add_collective = yes\nVIE_bop_add_collective = yes\n' if mode=='fast_paid' else cohesion(-16)+'VIE_bop_add_central = yes\nVIE_bop_add_central = yes\n' if mode=='fast_override' else '')+''.join(f'clr_country_flag = VIE_mode_{other}\n' for other in ['standard','fast_paid','fast_override'] if other!=mode)+'VIE_politics_offer_e102 = yes\n','VIE_politics_can_launch_'+mode+' = yes'))

definition('VIE_politics_offer_e102',guard('set_country_flag = VIE_e102_choice_pending\nset_variable = { VIE_e102_choice_epoch = VIE_programme_epoch }\ncountry_event = { id = vie_pol.102 }\n','has_country_flag = VIE_programme_active has_country_flag = VIE_programme_inspection has_completed_focus = '+IDS['F06']+' NOT = { has_country_flag = VIE_e102_choice_pending } NOT = { has_country_flag = VIE_e102_choice_resolved }'))
definition('VIE_politics_e104_cancel','''clr_country_flag = VIE_e104_signed
clr_country_flag = VIE_e104_signing
set_country_flag = VIE_e104_terminated
set_variable = { VIE_e104_remaining_support = 0 }
clr_country_flag = VIE_e104_rights_unused
clr_country_flag = VIE_e104_training_running
clr_country_flag = VIE_e104_training_complete
clr_country_flag = VIE_e104_check1_paid
clr_country_flag = VIE_e104_check2_paid
''')
definition('VIE_politics_e104_open','''set_country_flag = VIE_e104_signed
clr_country_flag = VIE_e104_terminated
add_to_variable = { VIE_e104_contract_epoch = 1 }
set_variable = { VIE_e104_remaining_support = VIE_e104_promised_support }
set_variable = { VIE_e104_contract_elapsed = 0 }
set_country_flag = VIE_e104_rights_unused
clr_country_flag = VIE_e104_check1_paid
clr_country_flag = VIE_e104_check2_paid
clr_country_flag = VIE_e104_check1_done
clr_country_flag = VIE_e104_check2_done
clr_country_flag = VIE_e104_training_complete
clr_country_flag = VIE_e104_training_running
clr_country_flag = VIE_e104_training_rewarded
set_country_flag = VIE_e104_amendment_preapproved
''')
definition('VIE_politics_e104_sign_begin','''set_country_flag = VIE_e104_signing
set_variable = { VIE_e104_sign_remaining = VIE_e104_sign_days }
''')
definition('VIE_politics_e104_amend','''set_country_flag = VIE_e104_amended
set_variable = { VIE_XIII12_contract_epoch = VIE_e104_contract_epoch }
set_variable = { VIE_e104_contract_elapsed = 0 }
clr_country_flag = VIE_e104_check1_paid
clr_country_flag = VIE_e104_check2_paid
clr_country_flag = VIE_e104_check1_done
clr_country_flag = VIE_e104_check2_done
''')
definition('VIE_politics_e104_fail','VIE_politics_e104_cancel = yes\n'+cohesion(-6))
definition('VIE_politics_e104_tick','''if = { limit = { has_country_flag = VIE_e104_signing }
subtract_from_variable = { VIE_e104_sign_remaining = 1 }
if = { limit = { check_variable = { VIE_e104_sign_remaining < 1 } }
clr_country_flag = VIE_e104_signing
VIE_politics_e104_open = yes
}
} else_if = { limit = { has_country_flag = VIE_e104_signed NOT = { has_country_flag = VIE_e104_terminated } }
add_to_variable = { VIE_e104_contract_elapsed = 1 }
if = { limit = { NOT = { check_variable = { VIE_e104_contract_elapsed < 90 } } NOT = { has_country_flag = VIE_e104_check1_done } }
if = { limit = { has_country_flag = VIE_e104_check1_paid has_completed_focus = '''+IDS['F10']+''' }
set_country_flag = VIE_e104_check1_done
} else = { VIE_politics_e104_fail = yes }
}
if = { limit = { has_country_flag = VIE_e104_signed NOT = { check_variable = { VIE_e104_contract_elapsed < 180 } } NOT = { has_country_flag = VIE_e104_check2_done } }
if = { limit = { has_country_flag = VIE_e104_check2_paid has_country_flag = VIE_e104_check1_done }
set_country_flag = VIE_e104_check2_done
set_temp_variable = { treasury_change = VIE_e104_remaining_support }
modify_treasury_effect = yes
set_variable = { VIE_e104_remaining_support = 0 }
} else = { VIE_politics_e104_fail = yes }
}
if = { limit = { has_country_flag = VIE_e104_training_running }
add_to_variable = { VIE_e104_training_elapsed = 1 }
if = { limit = { NOT = { check_variable = { VIE_e104_training_elapsed < 90 } } }
clr_country_flag = VIE_e104_training_running
set_country_flag = VIE_e104_training_complete
}
}
if = { limit = { has_country_flag = VIE_e104_signed has_country_flag = VIE_e104_check2_done has_country_flag = VIE_e104_training_complete NOT = { has_country_flag = VIE_e104_training_rewarded } }
set_country_flag = VIE_e104_training_rewarded
clr_country_flag = VIE_e104_rights_unused
add_political_power = 25
clr_country_flag = VIE_e104_signed
}
}''')
for i,end in [(1,90),(2,180)]:
    avail=f'has_country_flag = VIE_e104_signed NOT = {{ has_country_flag = VIE_e104_terminated }} NOT = {{ has_country_flag = VIE_e104_check{i}_paid }} check_variable = {{ VIE_e104_contract_elapsed < {end} }} has_completed_focus = {IDS["F10"]}'
    if i==2:avail+=' has_country_flag = VIE_e104_check1_done'
    decision(f'VIE_e104_fund_check_{i}',f'Cấp phí kiểm chứng hợp đồng lần {i}',f'Chi10PP cho đợt kiểm chứng kết thúc ngày{end} từ lúc ký/sửa. Cần quy trình kiểm toán mua sắm công. Không cấp đủ phí trước hạn thì mất hỗ trợ chưa nhận/quyền đào tạo và gắn kết−6.',avail,f'set_country_flag = VIE_e104_check{i}_paid',cost=10,visible='has_country_flag = VIE_e104_signed')
decision('VIE_e104_training_task','Đào tạo kỹ thuật theo hợp đồng','Task90ngày. Chỉ nhận25PP một lần sau hoàn tất đào tạo và hai đợt kiểm chứng hợp đồng; hủy hợp đồng mất quyền chưa dùng.','has_country_flag = VIE_e104_signed has_country_flag = VIE_e104_rights_unused NOT = { has_country_flag = VIE_e104_terminated } NOT = { has_country_flag = VIE_e104_training_running } NOT = { has_country_flag = VIE_e104_training_complete }','set_country_flag = VIE_e104_training_running\nset_variable = { VIE_e104_training_elapsed = 0 }',visible='has_country_flag = VIE_e104_signed')
decision('VIE_e104_cancel_task','Chấm dứt hợp đồng kỹ thuật','Đóng nghĩa vụ tương lai và mất hỗ trợ chưa nhận/quyền đào tạo chưa dùng. Không thu hồi tiền hoặc thưởng đã nhận.','has_country_flag = VIE_e104_signed','VIE_politics_e104_cancel = yes')
DECISIONS[-1]=DECISIONS[-1].replace('ai_will_do = { base = 50 }','''ai_will_do = { base = 50 modifier = { factor = 0 NOT = { OR = {
AND = { check_variable = { VIE_e104_contract_elapsed > 80 } NOT = { has_country_flag = VIE_e104_check1_paid } political_power < 10 }
AND = { check_variable = { VIE_e104_contract_elapsed > 170 } NOT = { has_country_flag = VIE_e104_check2_paid } political_power < 10 }
} } } }''')

# Programme tools: an actual paid task must finish before evidence is recorded.
SEQUENCES={'cadre':['training','training','succession','review'],'admin':['administration_project','administration_project','review'],'inspection':['audit_standard','audit','audit','review'],'social':['local_project','local_project','review']}
TOOLS={'training':('Đào tạo cán bộ','F09'),'succession':('Chuẩn bị kế cận','F09'),'administration_project':('Thực hiện dự án công vụ','F08'),'audit_standard':('Ban hành chuẩn kiểm toán','F06'),'audit':('Thực hiện kiểm toán','F10'),'local_project':('Thực hiện dự án dân vận','F11'),'review':('Kiểm chứng và nghiệm thu','F12')}
definition('VIE_politics_read_corruption','set_variable = { VIE_corruption_current = 0 }\n'+''.join(('if' if level==1 else 'else_if')+f' = {{ limit = {{ has_idea = corruption_level_{level:02} }} set_variable = {{ VIE_corruption_current = {level} }} }}\n' for level in range(1,11)))
condition('VIE_politics_corruption_verified','''OR = {
AND = { check_variable = { VIE_programme_corruption_baseline = 1 } has_idea = corruption_level_01 }
AND = { check_variable = { VIE_programme_corruption_baseline > 1 } check_variable = { VIE_corruption_current > 0 } check_variable = { var = VIE_corruption_current value = VIE_programme_corruption_baseline compare = less_than } }
}''')
condition('VIE_politics_review_condition','''OR = {
AND = { has_country_flag = VIE_programme_cadre NOT = { check_variable = { VIE_leadership_cohesion < 55 } } }
AND = { has_country_flag = VIE_programme_admin NOT = { check_variable = { treasury_rate < 0 } } }
AND = { has_country_flag = VIE_programme_inspection VIE_politics_corruption_verified = yes }
has_country_flag = VIE_programme_social
}''')
condition('VIE_politics_job_can_progress','''OR = {
NOT = { has_country_flag = VIE_programme_social }
AND = { check_variable = { VIE_programme_step = 0 } owns_state = 518 controls_state = 518 }
AND = { check_variable = { VIE_programme_step = 1 } owns_state = 526 controls_state = 526 }
AND = { check_variable = { VIE_programme_step = 2 } owns_state = 518 controls_state = 518 owns_state = 526 controls_state = 526 }
}''')
targets='set_variable = { VIE_programme_targets_met = 0 }\n'
for program,tests in [
    ('cadre',[f'has_completed_focus = {IDS["F02"]}','check_variable = { VIE_programme_step > 1 }','check_variable = { VIE_programme_step > 2 }','has_country_flag = VIE_programme_review_done']),
    ('admin',[f'has_completed_focus = {IDS["F08"]}','check_variable = { VIE_programme_step > 1 }','has_country_flag = VIE_programme_review_done','has_country_flag = VIE_programme_review_done NOT = { check_variable = { treasury_rate < 0 } }']),
    ('inspection',['check_variable = { VIE_programme_step > 0 }','check_variable = { VIE_programme_step > 2 }','has_country_flag = VIE_programme_review_done','has_country_flag = VIE_programme_review_done VIE_politics_corruption_verified = yes']),
    ('social',[f'has_completed_focus = {IDS["F11"]}','check_variable = { VIE_programme_step > 1 }','has_country_flag = VIE_programme_review_done','has_country_flag = VIE_programme_review_done check_variable = { VIE_programme_gdp_target > 0 } NOT = { check_variable = { var = gdp_per_capita value = VIE_programme_gdp_target compare = less_than } }'])]:
    targets+=guard(''.join(guard('add_to_variable = { VIE_programme_targets_met = 1 }',test) for test in tests),f'has_country_flag = VIE_programme_{program}')
definition('VIE_politics_refresh_targets',guard(targets,'has_country_flag = VIE_programme_active'))
definition('VIE_politics_job_finish','''if = { limit = { has_country_flag = VIE_programme_active has_country_flag = VIE_programme_job_running check_variable = { var = VIE_programme_job_epoch value = VIE_programme_epoch compare = equals } }
clr_country_flag = VIE_programme_job_running
add_to_variable = { VIE_programme_step = 1 }
add_to_variable = { VIE_programme_targets_met = 1 }
if = { limit = { has_country_flag = VIE_programme_inspection check_variable = { VIE_programme_step = 3 } NOT = { has_idea = corruption_level_01 } }
decrease_corruption = yes
VIE_politics_read_corruption = yes
}
if = { limit = { has_country_flag = VIE_programme_job_review }
set_country_flag = VIE_programme_review_done
if = { limit = { OR = { has_country_flag = VIE_programme_admin has_country_flag = VIE_programme_social } } add_to_variable = { VIE_programme_targets_met = 1 } }
}
}''')
for program,seq in SEQUENCES.items():
    for step,tool in enumerate(seq):
        for fast in [False,True]:
            pp,cash=P['tools'][tool];days=P['action_days'][tool][int(fast)]
            limit=f'has_country_flag = VIE_programme_active has_country_flag = VIE_programme_{program} check_variable = {{ VIE_programme_step = {step} }} NOT = {{ has_country_flag = VIE_programme_job_running }} NOT = {{ check_variable = {{ var = VIE_programme_elapsed value = VIE_programme_prepare_days compare = less_than }} }} has_completed_focus = {IDS[TOOLS[tool][1]]} '+funds(pp,cash)
            limit+=(' NOT = { has_country_flag = VIE_mode_standard }' if fast else ' has_country_flag = VIE_mode_standard')
            if program=='inspection':limit+=' has_country_flag = VIE_e102_choice_resolved'
            if program=='cadre' and tool=='review':limit+=' NOT = { check_variable = { VIE_leadership_cohesion < 55 } }'
            if program=='social':
                sites=[518] if step==0 else [526] if step==1 else [518,526]
                limit+=' '+ ' '.join(f'owns_state = {site} controls_state = {site}' for site in sites)
            limit+=' NOT = { has_country_flag = VIE_programme_job_delay }'
            flag='set_country_flag' if tool=='review' else 'clr_country_flag'
            body=pay(pp,cash)+f'''set_country_flag = VIE_programme_job_running
set_variable = {{ VIE_programme_job_epoch = VIE_programme_epoch }}
set_variable = {{ VIE_programme_job_remaining = {days} }}
{flag} = VIE_programme_job_review
'''
            progress='\\nNgày chương trình: [?VIE_programme_elapsed|0]/900; chứng cứ: [?VIE_programme_targets_met|0]/4. Công việc đang chạy còn [?VIE_programme_job_remaining|0] ngày. Ngày hoàn tất theo lịch công việc: [?VIE_programme_forecast_days|0]; vẫn phải đạt chỉ tiêu gắn kết, ngân sách hoặc GDP tương ứng.'
            visibility=f'has_country_flag = VIE_programme_active has_country_flag = VIE_programme_{program} check_variable = {{ VIE_programme_step = {step} }}'+(' has_country_flag = VIE_mode_standard' if not fast else ' NOT = { has_country_flag = VIE_mode_standard }')
            decision(f'VIE_programme_{program}_{step}_{"fast" if fast else "standard"}',TOOLS[tool][0]+f' ({step+1})',f'Chi{pp}PP'+(f' và{cash}ngân khố' if cash else '')+f'; thực hiện{days}ngày. Chỉ ghi chứng cứ sau thực thi và kiểm chứng. Chờ hoặc trì hoãn không kéo dài deadline900.'+progress,limit,body,visible=visibility)

definition('VIE_politics_evaluate',guard('''if = { limit = { check_variable = { VIE_programme_targets_met > 3 } has_country_flag = VIE_programme_review_done } VIE_resolve_programme_full = yes }
else_if = { limit = { NOT = { check_variable = { VIE_programme_elapsed < 900 } } }
if = { limit = { check_variable = { VIE_programme_targets_met > 1 } } VIE_resolve_programme_partial = yes }
else = { VIE_resolve_programme_fail = yes }
}''','has_country_flag = VIE_programme_active'))
remaining='set_variable = { VIE_programme_forecast_days = VIE_programme_elapsed }\n'
remaining+='''if = { limit = { check_variable = { var = VIE_programme_elapsed value = VIE_programme_prepare_days compare = less_than } }
set_variable = { VIE_programme_forecast_days = VIE_programme_prepare_days }
}
if = { limit = { has_country_flag = VIE_programme_job_delay } add_to_variable = { VIE_programme_forecast_days = VIE_programme_delay_remaining } }
'''
for program,seq in SEQUENCES.items():
    remaining+=f'if = {{ limit = {{ has_country_flag = VIE_programme_{program} }}\n'
    for step,tool in enumerate(seq):
        remaining+=f'if = {{ limit = {{ check_variable = {{ VIE_programme_step < {step+1} }} }}\n'
        normal,fast=P['action_days'][tool]
        remaining+=f'if = {{ limit = {{ check_variable = {{ VIE_programme_step = {step} }} has_country_flag = VIE_programme_job_running }} add_to_variable = {{ VIE_programme_forecast_days = VIE_programme_job_remaining }} }}\n'
        remaining+=f'else_if = {{ limit = {{ has_country_flag = VIE_mode_standard }} add_to_variable = {{ VIE_programme_forecast_days = {normal} }} }}\nelse = {{ add_to_variable = {{ VIE_programme_forecast_days = {fast} }} }}\n}}\n'
    remaining+='}\n'
definition('VIE_politics_remaining_forecast',guard(remaining,'has_country_flag = VIE_programme_active'))
definition('VIE_politics_programme_tick','''if = { limit = { has_country_flag = VIE_programme_active }
VIE_politics_read_corruption = yes
add_to_variable = { VIE_programme_elapsed = 1 }
if = { limit = { has_country_flag = VIE_programme_job_delay check_variable = { var = VIE_programme_elapsed value = VIE_programme_prepare_days compare = greater_than } }
subtract_from_variable = { VIE_programme_delay_remaining = 1 }
if = { limit = { check_variable = { VIE_programme_delay_remaining < 1 } } clr_country_flag = VIE_programme_job_delay }
}
if = { limit = { has_country_flag = VIE_programme_job_running NOT = { has_country_flag = VIE_programme_job_delay } VIE_politics_job_can_progress = yes }
if = { limit = { has_country_flag = VIE_programme_job_review NOT = { VIE_politics_review_condition = yes } }
set_variable = { VIE_programme_job_remaining = 90 }
} else = { subtract_from_variable = { VIE_programme_job_remaining = 1 } }
if = { limit = { check_variable = { VIE_programme_job_remaining < 1 } } VIE_politics_job_finish = yes }
}
VIE_politics_read_corruption = yes
VIE_politics_refresh_targets = yes
VIE_politics_remaining_forecast = yes
VIE_politics_offer_e102 = yes
if = { limit = { has_country_flag = VIE_programme_inspection NOT = { check_variable = { VIE_programme_elapsed < 450 } } NOT = { has_country_flag = VIE_e103_progress_notified } }
set_country_flag = VIE_e103_progress_notified
country_event = { id = vie_pol.103 }
}
if = { limit = { has_country_flag = VIE_programme_inspection has_country_flag = VIE_e102_data_access_unlocked NOT = { check_variable = { VIE_programme_elapsed < 500 } } NOT = { has_country_flag = VIE_e104_offer_shown } NOT = { has_country_flag = VIE_e104_signed } }
set_country_flag = VIE_e104_offer_shown
set_variable = { VIE_e104_offer_epoch = VIE_programme_epoch }
country_event = { id = vie_pol.104 }
}
VIE_politics_evaluate = yes
}''')

# Country national dossier is the concrete object; source congress is retained.
reader_calls=[]
for node,e in P['node_opportunity_effects'].items():
    if e['reader']=='archive_XV': continue
    effect=f'VIE_politics_consume_{node}'
    a=e['A']['effect'];b=e['B']['effect']
    definition(effect,guard('''set_country_flag = VIE_consumed_'''+node+'\n'+guard(f'add_political_power = {a["pp"]}\n'+money(a['treasury']),f'has_country_flag = VIE_record_{node}_A')+'else = { '+f'add_political_power = {b["pp"]}\n'+money(b['treasury'])+' }\n',f'NOT = {{ has_country_flag = VIE_consumed_{node} }} OR = {{ has_country_flag = VIE_record_{node}_A has_country_flag = VIE_record_{node}_B }}'))

# All reviewed A/B policies use real choice events instead of a bare completion flag.
for index,(node,prices) in enumerate(P['node_choice_prices'].items(),10):
    number=index;options=[]
    for label,(pp,cash) in zip('ab',prices):
        upper=label.upper();loss=P['node_choice_cohesion'].get(node,{}).get(upper,0)
        gate=''
        if node in ['X01','XII02']:
            target='XI05' if node=='X01' else 'XIII09'
            gate=('set_country_flag' if upper=='A' else 'clr_country_flag')+f' = VIE_gate_{target}\n'
        body=pay(pp,cash,loss)+f'set_country_flag = VIE_record_{node}_{upper}\nset_country_flag = VIE_record_{node}\nclr_country_flag = VIE_pending_{node}\n'+gate
        caption=P['node_opportunity_effects'].get(node,{}).get(upper,{}).get('action',('Kiểm chứng trách nhiệm trước' if upper=='A' else 'Nhận trách nhiệm và giữ quyền điều hành'))
        options.append((label,caption+f': {pp}PP'+(f', {cash}ngân khố' if cash else '')+(f', gắn kết−{loss}' if loss else ''),funds(pp,cash,loss) or 'always = yes',guard(body,f'has_country_flag = VIE_pending_{node} NOT = {{ has_country_flag = VIE_record_{node} }} '+funds(pp,cash,loss))))
    options.append(('c','Chưa chốt, giữ hồ sơ chờ','always = yes',''))
    desc=f'Chốt phương án cho {P["focus_nodes"][node]["name"]}. Phí thu một lần, ghi lựa chọn vào hồ sơ quốc gia; reader đọc đúng hồ sơ nguồn.'
    if node in P['node_opportunity_effects']:
        e=P['node_opportunity_effects'][node]
        desc+=f' Khi hoàn thành {P["focus_nodes"].get(e["reader"],{}).get("name","hồ sơ bàn giao XV")}, cách A hoàn trả{e["A"]["effect"]["pp"]}PP, cách B hoàn trả{e["B"]["effect"]["treasury"]}ngân khố; chưa hoàn thành không nhận.'
    else:desc+=' '+('A mở XI05; B khóa XI05.' if node=='X01' else 'A mở XIII09; B khóa XIII09.')
    event(number,P['focus_nodes'][node]['name'],desc,options,f'has_country_flag = VIE_pending_{node} NOT = {{ has_country_flag = VIE_record_{node} }}')
    date_gate='date > 2022.9.30' if node=='XIII05' else ''
    reward(node,f'set_country_flag = VIE_pending_{node}\nset_variable = {{ VIE_record_{node}_source_term = VIE_last_congress }}\n'+('' if date_gate else f'country_event = {{ id = vie_pol_runtime.{number} }}'))
    if date_gate: reader_calls.append(guard(f'set_country_flag = VIE_shown_{node}\ncountry_event = {{ id = vie_pol_runtime.{number} }}',f'has_country_flag = VIE_pending_{node} NOT = {{ has_country_flag = VIE_shown_{node} }} {date_gate}'))
    decision(f'VIE_reopen_{node}',f'Chốt hồ sơ {node}','Mở lại hồ sơ đang chờ. Không thu phí khi mở; chỉ trả phí khi chọn phương án.',f'has_country_flag = VIE_pending_{node} NOT = {{ has_country_flag = VIE_record_{node} }} '+date_gate,f'country_event = {{ id = vie_pol_runtime.{number} }}')

# Eight varied nodes, with persistent random outcomes and actual subsequent focus gates.
reward('IX11',guard('add_political_power = -20\nset_country_flag = VIE_record_IX11\nrandom_list = {\n65 = { '+cohesion(4)+'set_country_flag = VIE_IX11_consensus }\n35 = { add_political_power = -24\n'+cohesion(-4)+'set_country_flag = VIE_IX11_backlash }\n}', 'NOT = { has_country_flag = VIE_record_IX11 }'))
reward('IX12',guard('add_political_power = -20\nset_country_flag = VIE_record_IX12','NOT = { has_country_flag = VIE_record_IX12 }'))
available('IX11',funds(44));available('IX12',funds(20))
for node in ['XI09','XI10']:
    reward(node,guard((money(-.5) if node=='XI09' else '')+f'set_country_flag = VIE_record_{node}\nset_country_flag = VIE_project_{node}_running\nset_variable = {{ VIE_project_{node}_elapsed = 0 }}','NOT = { has_country_flag = VIE_record_'+node+' }'))
    identifier=IDS[node];other=IDS['XI10' if node=='XI09' else 'XI09']
    if 'mutually_exclusive' not in focuses[identifier]: focuses[identifier]=focuses[identifier].replace('search_filters =',f'mutually_exclusive = {{ focus = {other} }}\nsearch_filters =',1)
    available(node,funds(0,.5) if node=='XI09' else 'always = yes')
project_tick=''
for node in ['XI09','XI10']:
    result=money(.75) if node=='XI09' else 'random_list = { 70 = { '+money(.75)+'set_country_flag = VIE_XI10_recovered } 30 = { '+cohesion(-12)+'set_country_flag = VIE_XI10_failed } }'
    project_tick+=guard(f'add_to_variable = {{ VIE_project_{node}_elapsed = 1 }}\n'+guard(f'clr_country_flag = VIE_project_{node}_running\nset_country_flag = VIE_project_{node}_evidence_done\n'+result,f'NOT = {{ check_variable = {{ VIE_project_{node}_elapsed < 90 }} }}'),f'has_country_flag = VIE_project_{node}_running NOT = {{ has_country_flag = VIE_project_{node}_evidence_done }}')
definition('VIE_politics_project_tick',project_tick)
event(60,'Phương án kiện toàn giữa kỳ','Bàn giao tuần tự không thu phí nhưng khóa đào tạo XII09 trong kỳ. Kiện toàn ngay mất6gắn kết và mở XII09; không tự hoàn tất đào tạo.',[
 ('a','Bàn giao tuần tự60ngày','always = yes','set_country_flag = VIE_record_XII12_A\nset_country_flag = VIE_record_XII12\nclr_country_flag = VIE_gate_XII09\nclr_country_flag = VIE_pending_XII12'),
 ('b','Kiện toàn ngay, mở đào tạo trách nhiệm',funds(0,0,6),cohesion(-6)+'set_country_flag = VIE_record_XII12_B\nset_country_flag = VIE_record_XII12\nset_country_flag = VIE_gate_XII09\nclr_country_flag = VIE_pending_XII12'),
 ('c','Chưa chốt','always = yes','')], 'has_country_flag = VIE_pending_XII12 NOT = { has_country_flag = VIE_record_XII12 }')
reward('XII12','set_country_flag = VIE_pending_XII12\ncountry_event = { id = vie_pol_runtime.60 }')
decision('VIE_reopen_XII12','Chốt kiện toàn giữa kỳ','Mở lại lựa chọn đang chờ.','has_country_flag = VIE_pending_XII12 NOT = { has_country_flag = VIE_record_XII12 }','country_event = { id = vie_pol_runtime.60 }')
for reader,writer in [('XI05','X01'),('XIII09','XII02'),('XII09','XII12'),('XIV11','XIII12')]:
    if reader=='XII09':
        text=focuses[IDS[reader]];match=re.search(r'\bavailable\s*=\s*\{',text)
        old=text[match.end():block_end(text,match.start())-1]
        old=re.sub(r'^\s*has_country_flag\s*=\s*VIE_gate_XII09\s*$','',old,flags=re.M)
        focuses[IDS[reader]]=replace_block(text,'available',old)
    available(reader,f'OR = {{ has_country_flag = VIE_gate_XII09 AND = {{ has_country_flag = VIE_record_XII12_A check_variable = {{ VIE_last_congress > 12 }} }} }}' if reader=='XII09' else f'has_country_flag = VIE_gate_{reader}')
    text=focuses[IDS[reader]]
    if IDS[writer] not in re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*(\w+)',text): text=text.replace('search_filters =',f'prerequisite = {{ focus = {IDS[writer]} }}\nsearch_filters =',1)
    focuses[IDS[reader]]=text
# Put XII09 below its new direct prerequisite, avoiding an invisible sibling dependency.
text=focuses[IDS['XII09']]
text=re.sub(r'relative_position_id\s*=\s*\w+','relative_position_id = '+IDS['XII12'],text)
text=re.sub(r'\bx\s*=\s*-?\d+','x = 0',text,count=1);text=re.sub(r'\by\s*=\s*-?\d+','y = 1',text,count=1)
focuses[IDS['XII09']]=text
identifier=IDS['XIII12'];text=focuses[identifier]
text=re.sub(r'VIE_e104_can_amend\s*=\s*yes','has_country_flag = VIE_e104_signed NOT = { has_country_flag = VIE_e104_terminated }',text)
focuses[identifier]=text
available('XIII12','has_country_flag = VIE_e104_signed NOT = { has_country_flag = VIE_e104_terminated }')
available('XIV11','has_country_flag = VIE_e104_signed NOT = { has_country_flag = VIE_e104_terminated } check_variable = { var = VIE_XIII12_contract_epoch value = VIE_e104_contract_epoch compare = equals }')
reward('F06','VIE_politics_offer_e102 = yes')
for node in ['F09','F10','F11']: reward(node,'set_country_flag = VIE_'+node+'_tools_ready')
reward('F12','VIE_politics_evaluate = yes')
reward('XI08','set_country_flag = VIE_pending_XI08_history')
reader_calls.append(guard('set_country_flag = VIE_shown_XI08_history\ncountry_event = { id = vie_pol.108 }','has_country_flag = VIE_pending_XI08_history NOT = { has_country_flag = VIE_shown_XI08_history } date > 2014.5.1'))
for node,e in P['node_opportunity_effects'].items():
    if e['reader']=='archive_XV': continue
    identifier=IDS[e['reader']];text=focuses[identifier]
    match=re.search(r'\bcompletion_reward\s*=\s*\{',text)
    content=text[match.end():block_end(text,match.start())-1]
    call=f'VIE_politics_consume_{node} = yes'
    if call not in content: focuses[identifier]=replace_block(text,'completion_reward',content+'\n'+call)

definition('VIE_politics_daily','''if = { limit = { has_country_flag = VIE_congress_resolved } add_to_variable = { VIE_congress_elapsed = 1 } }
VIE_politics_forecast = yes
VIE_politics_programme_tick = yes
VIE_politics_e104_tick = yes
VIE_politics_project_tick = yes
'''+ '\n'.join(reader_calls))
event(1,'','', 'VIE_politics_daily = yes\ncountry_event = { id = vie_pol_runtime.1 days = 1 }','original_tag = VIE',True)

for identifier,old in list(focuses.items()):
    if identifier==IDS['XII09']: continue
    # Replace exactly one original focus block, leaving unrelated user changes intact.
    match=re.search(r'\bfocus\s*=\s*\{\s*id\s*=\s*'+re.escape(identifier)+r'\b',tree)
    if not match: continue
    tree=tree[:match.start()]+old+tree[block_end(tree,match.start()):]
match=re.search(r'\bfocus\s*=\s*\{\s*id\s*=\s*'+re.escape(IDS['XII09'])+r'\b',tree)
tree=tree[:match.start()]+tree[block_end(tree,match.start()):]
match=re.search(r'\bfocus\s*=\s*\{\s*id\s*=\s*'+re.escape(IDS['XII12'])+r'\b',tree)
end=block_end(tree,match.start());tree=tree[:end]+'\n\n'+focuses[IDS['XII09']]+tree[end:]
if '## v57 (14/10/2026)' not in tree: tree=tree.replace('focus_tree = {','## v57 (14/10/2026): adapter chinh tri, E103 tu dong, task/cohort, E104 nghia vu, consumer va 8 node co hau qua that.\nfocus_tree = {',1)
focus_path.write_text(tree,encoding='utf-8')

# Existing IDs retain their callers; replace only their revised behaviour.
base=ROOT/'common/scripted_effects/VIE_md_effects_politics.txt';s=base.read_text(encoding='utf-8-sig')
for mode in ['standard','fast_paid','fast_override']:s=replace_block(s,'VIE_launch_programme_'+mode,'VIE_politics_begin_'+mode+' = yes')
match=re.search(r'VIE_resolve_programme_full\s*=\s*\{',s);original=s[match.start():block_end(s,match.start())]
start=original.find('\t# Thuong som');end=original.find('\t# Tang Tier',max(start,0))
early='''# Moc som tinh tu launch, E103 khong bo quyen thuong.
if = { limit = { OR = {
AND = { has_country_flag = VIE_programme_inspection NOT = { check_variable = { VIE_programme_elapsed > 690 } } }
AND = { NOT = { has_country_flag = VIE_programme_inspection } NOT = { check_variable = { VIE_programme_elapsed > 600 } } }
} }
set_country_flag = VIE_programme_early_full
add_political_power = 70
}
'''
if start>=0: original=original[:start]+early+original[end:]
body=effect_body(original)
if 'has_idea = corruption_level_01' not in body:body=body.replace('decrease_corruption = yes', 'if = { limit = { NOT = { has_idea = corruption_level_01 } } decrease_corruption = yes }')
body=body.replace('decrease_corruption = yes','log = "[GetDateText]: [Root.GetName]: Corruption evidence already verified"')
if 'set_variable = { VIE_resolved_programme_epoch = VIE_programme_epoch }' not in body: body='set_variable = { VIE_resolved_programme_epoch = VIE_programme_epoch }\n'+body
s=replace_block(s,'VIE_resolve_programme_full',guard(body,'has_country_flag = VIE_programme_active has_country_flag = VIE_programme_review_done check_variable = { VIE_programme_targets_met > 3 } NOT = { check_variable = { VIE_programme_elapsed > 900 } } NOT = { check_variable = { var = VIE_resolved_programme_epoch value = VIE_programme_epoch compare = equals } }'))
for outcome in ['partial','fail']:
    match=re.search('VIE_resolve_programme_'+outcome+r'\s*=\s*\{',s);old=s[match.start():block_end(s,match.start())];body=effect_body(old)
    if 'set_variable = { VIE_resolved_programme_epoch = VIE_programme_epoch }' not in body: body='set_variable = { VIE_resolved_programme_epoch = VIE_programme_epoch }\n'+body
    s=replace_block(s,'VIE_resolve_programme_'+outcome,guard(body,'has_country_flag = VIE_programme_active NOT = { check_variable = { var = VIE_resolved_programme_epoch value = VIE_programme_epoch compare = equals } }'))
for program in ['cadre','admin','inspection','social']:
    match=re.search('VIE_select_programme_'+program+r'\s*=\s*\{',s);old=s[match.start():block_end(s,match.start())]
    body=effect_body(old)
    if 'VIE_politics_forecast = yes' not in body:body+='\nVIE_politics_forecast = yes'
    s=replace_block(s,'VIE_select_programme_'+program,guard(body,'VIE_politics_can_select_inspection = yes' if program=='inspection' else 'VIE_politics_can_select = yes'))
for term in range(9,15):
    match=re.search(f'VIE_resolve_congress_{term}'+r'\s*=\s*\{',s);old=s[match.start():block_end(s,match.start())]
    body=old[old.index('{')+1:old.rfind('}')]
    if 'VIE_politics_new_term' not in body:body+='\nVIE_politics_new_term = yes\n'
    s=replace_block(s,f'VIE_resolve_congress_{term}',body)
base.write_text(s,encoding='utf-8')

# Extend original decisions with authoritative launch/select gates and early-only side task.
path=ROOT/'common/decisions/VIE_md_politics_decisions.txt';s=path.read_text(encoding='utf-8-sig')
for mode in ['standard','fast_paid','fast_override']:
    key='VIE_launch_mode_'+mode+'_decision';match=re.search(key+r'\s*=\s*\{',s);old=s[match.start():block_end(s,match.start())]
    revised=replace_block(old,'available','VIE_politics_can_launch_'+mode+' = yes')
    revised=re.sub(r'\bcost\s*=\s*\d+','cost = 0',revised,count=1)
    s=s[:match.start()]+revised+s[block_end(s,match.start()):]
for program in ['cadre','admin','inspection','social']:
    key='VIE_select_'+program+'_decision';match=re.search(key+r'\s*=\s*\{',s);old=s[match.start():block_end(s,match.start())]
    s=s[:match.start()]+replace_block(old,'available','VIE_politics_can_select_inspection = yes' if program=='inspection' else 'VIE_politics_can_select = yes')+s[block_end(s,match.start()):]
match=re.search('VIE_side_project_decision'+r'\s*=\s*\{',s);old=s[match.start():block_end(s,match.start())]
avail='has_country_flag = VIE_last_programme_full has_country_flag = VIE_programme_early_full NOT = { check_variable = { var = VIE_last_side_project_epoch value = VIE_programme_epoch compare = equals } } OR = {\n'
dates=list(P['congress_dates'].items())
for (term,now),(_,nxt) in zip(dates,dates[1:]):
    latest=date.fromisoformat(nxt)-timedelta(days=180+270+100)
    avail+=f'AND = {{ check_variable = {{ VIE_last_congress = {9+["IX","X","XI","XII","XIII","XIV"].index(term)} }} NOT = {{ date > {latest.year}.{latest.month}.{latest.day} }} }}\n'
avail+='}'
revised=replace_block(old,'available',avail)
revised=replace_block(revised,'remove_effect',guard('add_timed_idea = { idea = VIE_side_project_bureaucracy_idea days = 365 }','check_variable = { var = VIE_last_side_project_epoch value = VIE_programme_epoch compare = equals } has_country_flag = VIE_programme_early_full'))
s=s[:match.start()]+revised+s[block_end(s,match.start()):]
# The daily clock is authoritative; a legacy unstamped mission may not resolve a later epoch.
for key in ['VIE_term_programme_deadline_mission','VIE_review_programme_early_decision']:
    match=re.search(key+r'\s*=\s*\{',s)
    if match:s=s[:match.start()]+s[block_end(s,match.start()):]
path.write_text(s,encoding='utf-8')

triggers=ROOT/'common/scripted_triggers/VIE_md_triggers_politics.txt';s=triggers.read_text(encoding='utf-8-sig')
match=re.search(r'VIE_e104_can_amend\s*=\s*\{',s);old=s[match.start():block_end(s,match.start())]
body=effect_body(old)
if 'VIE_e104_amendment_preapproved' not in body:body+='\nhas_country_flag = VIE_e104_amendment_preapproved'
s=replace_block(s,'VIE_e104_can_amend',body);triggers.write_text(s,encoding='utf-8')

startup=ROOT/'common/on_actions/VIE_md_on_actions_startup.txt';s=startup.read_text(encoding='utf-8-sig')
if 'VIE_politics_runtime_init' not in s:s=s.replace('VIE_ax_init = yes','VIE_ax_init = yes\nVIE_politics_runtime_init = yes',1)
startup.write_text(s,encoding='utf-8')

# E103 has only an informational acknowledgement; E102/E104 get transaction guards.
path=ROOT/'events/VIE_md_politics_events.txt';s=path.read_text(encoding='utf-8-sig')
def replace_event(text,id,body):
    for match in re.finditer(r'country_event\s*=\s*\{',text):
        end=block_end(text,match.start());old=text[match.start():end]
        if re.search(r'\bid\s*=\s*'+re.escape(id)+r'\b',old):return text[:match.start()]+'country_event = {\n'+body+'\n}\n'+text[end:]
    raise ValueError(id)
header=lambda id:f'id = {id}\ntitle = {id}.t\ndesc = {id}.d\npicture = GFX_report_event_generic_read_write\nis_triggered_only = yes\n'
s=replace_event(s,'vie_pol.103',header('vie_pol.103')+'option = { name = vie_pol.103.a }')
body=header('vie_pol.102')+'trigger = { has_country_flag = VIE_e102_choice_pending }\n'
for label,(pp,cash,delay) in P['e102'].items():
    limit=f'has_country_flag = VIE_programme_active has_country_flag = VIE_e102_choice_pending check_variable = {{ var = VIE_e102_choice_epoch value = VIE_programme_epoch compare = equals }} '+funds(pp,cash)
    if delay:limit+='NOT = { check_variable = { VIE_programme_forecast_days > 750 } }'
    chosen=pay(pp,cash)+f'set_country_flag = VIE_record_E102_{label}\nset_country_flag = VIE_e102_choice_resolved\nclr_country_flag = VIE_e102_choice_pending\n'
    if label=='A':chosen+='set_country_flag = VIE_e102_data_access_unlocked\n'
    if delay:chosen+=f'add_to_variable = {{ VIE_programme_forecast_days = {delay} }}\nset_country_flag = VIE_programme_job_delay\nset_variable = {{ VIE_programme_delay_remaining = {delay} }}\nadd_timed_idea = {{ idea = VIE_e102_c_soe_construction_idea days = 365 }}\n'
    body+=f'option = {{ name = vie_pol.102.{label.lower()} trigger = {{ {limit} }}\n'+guard(chosen,limit)+'}\n'
LOC['vie_pol.102.wait']='Chưa chốt, để hồ sơ chờ'
body+='option = { name = vie_pol.102.wait }\n'
s=replace_event(s,'vie_pol.102',body)
decision('VIE_reopen_E102','Chốt phương án kiểm toán DNNN','Mở lại hồ sơ đang chờ. Phí thu khi chọn; trễ tất định vượt840 bị khóa.','has_country_flag = VIE_programme_active has_country_flag = VIE_e102_choice_pending','country_event = { id = vie_pol.102 }')
body=header('vie_pol.104')+'trigger = { has_country_flag = VIE_programme_active check_variable = { var = VIE_e104_offer_epoch value = VIE_programme_epoch compare = equals } NOT = { has_country_flag = VIE_e104_signed } }\n'
for label in ['A','B']:
    pp=P['e104'][label+'_pp'];grant=P['e104'][label+'_grant'];limit=funds(pp)+'NOT = { has_country_flag = VIE_e104_signed } has_country_flag = VIE_programme_active check_variable = { var = VIE_e104_offer_epoch value = VIE_programme_epoch compare = equals }'
    if label=='A':limit+=' OR = { NOT = { check_variable = { VIE_tier_cadre < 1 } } has_country_flag = VIE_dual_role_active }'
    limit+=' NOT = { has_country_flag = VIE_e104_signing } NOT = { has_country_flag = VIE_e104_offer_resolved }'
    sign='set_variable = { VIE_e104_sign_days = 21 }\n'
    if label=='A':sign+='''if = { limit = { has_country_flag = VIE_dual_role_active } set_variable = { VIE_e104_sign_days = 21 } }
else_if = { limit = { NOT = { check_variable = { VIE_tier_cadre < 3 } } } set_variable = { VIE_e104_sign_days = 21 } }
else_if = { limit = { check_variable = { VIE_tier_cadre = 2 } } set_variable = { VIE_e104_sign_days = 25 } }
else = { set_variable = { VIE_e104_sign_days = 30 } }
'''
    body+=f'option = {{ name = vie_pol.104.{label.lower()} trigger = {{ {limit} }}\n'+guard(pay(pp)+sign+f'set_country_flag = VIE_e104_offer_resolved\nset_variable = {{ VIE_e104_promised_support = {grant} }}\nset_country_flag = VIE_record_E104_{label}\nVIE_politics_e104_sign_begin = yes\n',limit)+'}\n'
body+='option = { name = vie_pol.104.c\n'+guard('set_country_flag = VIE_e104_refused\nset_country_flag = VIE_e104_offer_resolved','has_country_flag = VIE_programme_active NOT = { has_country_flag = VIE_e104_offer_resolved } check_variable = { var = VIE_e104_offer_epoch value = VIE_programme_epoch compare = equals }')+'}'
s=replace_event(s,'vie_pol.104',body)
body=header('vie_pol.132')+'trigger = { has_completed_focus = '+IDS['XIII12']+' NOT = { has_country_flag = VIE_record_XIII12 } }\n'
body+='option = { name = vie_pol.132.a trigger = { VIE_e104_can_amend = yes }\n'+guard('set_country_flag = VIE_record_XIII12_A\nset_country_flag = VIE_record_XIII12\nset_country_flag = VIE_gate_XIV11\nVIE_politics_e104_amend = yes','VIE_e104_can_amend = yes NOT = { has_country_flag = VIE_record_XIII12 }')+'}\n'
body+='option = { name = vie_pol.132.b\n'+guard('set_country_flag = VIE_record_XIII12_B\nset_country_flag = VIE_record_XIII12\nclr_country_flag = VIE_gate_XIV11\nVIE_politics_e104_cancel = yes','NOT = { has_country_flag = VIE_record_XIII12 }')+'}'
s=replace_event(s,'vie_pol.132',body)
# Event IDs bind the source term immutably. A popup from IX cannot use X's ledger.
for number in [102,104]:
    original=next(s[m.start():block_end(s,m.start())] for m in re.finditer(r'country_event\s*=\s*\{',s) if re.search(r'\bid\s*=\s*vie_pol\.'+str(number)+r'\b',s[m.start():block_end(s,m.start())]))
    source=original[original.index('{')+1:original.rfind('}')]
    for term in range(9,15):
        event_id=f'vie_pol.{number}' if term==9 else f'vie_pol_runtime.{number}{term}'
        fixed=re.sub(r'\bid\s*=\s*vie_pol\.'+str(number)+r'\b','id = '+event_id,source,count=1)
        match=re.search(r'\btrigger\s*=\s*\{',fixed)
        existing=fixed[match.end():block_end(fixed,match.start())-1]
        fixed=replace_block(fixed,'trigger',existing+f'\ncheck_variable = {{ VIE_last_congress = {term} }}')
        for match in list(re.finditer(r'\boption\s*=\s*\{',fixed))[::-1]:
            end=block_end(fixed,match.start());option=fixed[match.start():end]
            name=re.search(r'\bname\s*=\s*(\S+)',option).group(1)
            trigger=re.search(r'\btrigger\s*=\s*\{',option)
            if trigger:
                availability=option[trigger.end():block_end(option,trigger.start())-1]
                content=option[block_end(option,trigger.start()):option.rfind('}')]
            else:
                availability='always = yes';content=re.sub(r'\bname\s*=\s*\S+','',option[option.index('{')+1:option.rfind('}')],count=1)
            condition=f'check_variable = {{ VIE_last_congress = {term} }}'
            rebuilt=f'option = {{ name = {name}\ntrigger = {{ {availability} {condition} }}\n'+guard(content,condition)+'}'
            fixed=fixed[:match.start()]+rebuilt+fixed[end:]
        if term==9:s=replace_event(s,f'vie_pol.{number}',fixed)
        else:EVENTS.append('country_event = {\n'+fixed+'\n}\n')
    dispatch=''
    for term in range(9,15):
        event_id=f'vie_pol.{number}' if term==9 else f'vie_pol_runtime.{number}{term}'
        dispatch+=guard(f'country_event = {{ id = {event_id} }}',f'check_variable = {{ VIE_last_congress = {term} }}')
    definition(f'VIE_politics_dispatch_{number}',dispatch)
    for i,text in enumerate(EFFECTS):
        if not text.startswith(f'VIE_politics_dispatch_{number} ='):
            EFFECTS[i]=text.replace(f'country_event = {{ id = vie_pol.{number} }}',f'VIE_politics_dispatch_{number} = yes')
    if number==102:
        DECISIONS=[text.replace('country_event = { id = vie_pol.102 }','VIE_politics_dispatch_102 = yes') for text in DECISIONS]
path.write_text(s,encoding='utf-8')
original=next(s[m.start():block_end(s,m.start())] for m in re.finditer(r'country_event\s*=\s*\{',s) if re.search(r'\bid\s*=\s*vie_pol\.132\b',s[m.start():block_end(s,m.start())]))
source=original[original.index('{')+1:original.rfind('}')]
dispatch=''
for serial in range(1,7):
    event_id='vie_pol.132' if serial==1 else f'vie_pol_runtime.132{serial}'
    fixed=re.sub(r'\bid\s*=\s*vie_pol\.132\b','id = '+event_id,source,count=1)
    binding=f'check_variable = {{ VIE_e104_contract_epoch = {serial} }}'
    match=re.search(r'\btrigger\s*=\s*\{',fixed);existing=fixed[match.end():block_end(fixed,match.start())-1]
    fixed=replace_block(fixed,'trigger',existing+'\n'+binding)
    for match in list(re.finditer(r'\boption\s*=\s*\{',fixed))[::-1]:
        end=block_end(fixed,match.start());option=fixed[match.start():end];name=re.search(r'\bname\s*=\s*(\S+)',option).group(1)
        trigger=re.search(r'\btrigger\s*=\s*\{',option)
        if trigger:availability=option[trigger.end():block_end(option,trigger.start())-1];content=option[block_end(option,trigger.start()):option.rfind('}')]
        else:availability='always = yes';content=re.sub(r'\bname\s*=\s*\S+','',option[option.index('{')+1:option.rfind('}')],count=1)
        fixed=fixed[:match.start()]+f'option = {{ name = {name}\ntrigger = {{ {availability} {binding} }}\n'+guard(content,binding)+'}'+fixed[end:]
    if serial==1:s=replace_event(s,'vie_pol.132',fixed)
    else:EVENTS.append('country_event = {\n'+fixed+'\n}\n')
    dispatch+=guard(f'country_event = {{ id = {event_id} }}',binding)
definition('VIE_politics_dispatch_132',dispatch)
path.write_text(s,encoding='utf-8')
live_tree=focus_path.read_text(encoding='utf-8').replace('country_event = { id = vie_pol.132 }','VIE_politics_dispatch_132 = yes')
focus_path.write_text(live_tree,encoding='utf-8')
# New programmes may receive a new offer; old term-bound popups remain inert.
EFFECTS=[text.replace('clr_country_flag = VIE_e104_offer_shown','clr_country_flag = VIE_e104_offer_shown\nclr_country_flag = VIE_e104_offer_resolved') for text in EFFECTS]

for folder,name,content in [('common/scripted_effects','VIE_md_effects_politics_runtime.txt','\n'.join(EFFECTS)),('common/scripted_triggers','VIE_md_triggers_politics_runtime.txt','\n'.join(TRIGGERS)),('events','VIE_md_politics_runtime_events.txt','\n'.join(EVENTS)),('common/decisions','VIE_md_politics_runtime_decisions.txt','VIE_term_programmes_category = {\n'+'\n'.join(DECISIONS)+'}\n')]:
    (ROOT/folder/name).write_text('# Adapter chinh tri v57; tao boi tools/build_political_runtime.py\n'+content,encoding='utf-8')
LOC['VIE_tt_eff_launch_mode_fast_paid']='Khởi động: giá chuẩn theo tier/gắn kết cộng55PP và0.50ngân khố; BoP−0.10. Timer cấp tốc được giữ theo snapshot lúc ký.'
LOC['VIE_tt_eff_launch_mode_standard']='Khởi động chương trình900ngày. Phí chuẩn hiện tại: [?VIE_programme_start_cost|0]PP, theo tier cán bộ và gắn kết; thu một lần khi khởi động.'
LOC['VIE_tt_eff_launch_mode_fast_override']='Khởi động: giá chuẩn theo tier/gắn kết cộng25PP; gắn kết−16, BoP+0.10. Cần gắn kết sau trừ ít nhất40.'
LOC['VIE_tt_eff_review_programme_early']='Nghiệm thu đúng4/4 sau thực thi và kiểm chứng. Thưởng70PP chỉ khi hoàn tất trước/đúng600ngày, hoặc690ngày với kiểm tra. Full trễ vẫn tăng tier; tối đa một kết quả mỗi epoch.'
LOC['vie_pol.103.t']='Tiến độ kiểm chứng chương trình'
LOC['vie_pol.103.d']='Đây là thông báo tiến độ, không có cam kết hoặc phí gia hạn. Khi đủ bốn nhóm chứng cứ sau kiểm chứng, hệ thống tự chấm full; trượt mốc690 chỉ mất thưởng sớm. Deadline chương trình vẫn900ngày.'
LOC['vie_pol.103.a']='Tiếp tục thực thi và kiểm chứng'
LOC['vie_pol.104.d']='Đối tác đã chấp nhận các điều khoản và quyền sửa trong phạm vi dữ liệu đã thỏa thuận. Ký mất21/25/30ngày tùy phương án, tier và kiêm nhiệm; chỉ xác lập hỗ trợ chưa nhận. Phải cấp10PP trước mỗi đợt kiểm chứng kết thúc ngày90/180 từ lúc ký; thiếu một đợt mất hỗ trợ chưa nhận và gắn kết−6. Đào tạo90ngày nhận25PP sau hoàn tất và đủ hai đợt kiểm chứng. Hủy không thu hồi tiền đã nhận.'
LOC['vie_pol.132.d']='Sửa giữ phần lợi ích chưa nhận nhưng phải kiểm chứng lại hai đợt90/180ngày, mỗi đợt10PP; mở node rà soát hợp đồng XIV11 cho chính hợp đồng này. Hủy đóng nghĩa vụ và khóa node đó, mất hỗ trợ chưa nhận/quyền chưa dùng; không trừ khoản hỗ trợ chưa nhận khỏi ngân khố thực.'
for node,description in {
 'IX11':'Luân chuyển20PP: 65% đạt đồng thuận và gắn kết+4; 35% bị phản đối, phải chi thêm24PP và gắn kết−4. Kết quả chỉ lấy một lần, không đổi khi tải save.',
 'IX12':'Chi20PP để kiểm toán độc lập và giữ bộ máy hiện tại. Kết quả cố định, không nhận phần thưởng gắn kết của luân chuyển.',
 'XI09':'Ứng0.50ngân khố cho cứu dự án; hoàn tất90ngày thực thi và ghi chứng cứ bàn giao mới thu hồi0.75ngân khố. Không nhận lại khoản thu hồi khi tải save.',
 'XI10':'Tái cơ cấu90ngày không ứng vốn: 70% thu hồi0.75ngân khố; 30% thất bại, không thu hồi và gắn kết−12. Kết quả được lưu một lần cho dự án này.',
 'X01':'Chọn kiểm toán vốn20PP để mở xử lý nợ xấu ở kỳ XI, hoặc trả6gắn kết để giữ cách điều hành tại ngành và khóa node đó cho hồ sơ này.',
 'XII02':'Chọn thẩm định trước25PP để mở ký liên ngành ở kỳ XIII, hoặc trả8gắn kết để nhận trách nhiệm cá nhân và khóa node ký liên ngành.',
 'XII12':'Bàn giao tuần tự không thu phí nhưng khóa đào tạo trách nhiệm XII09 trong kỳ XII. Kiện toàn ngay trả6gắn kết để mở đào tạo; không tự hoàn tất đào tạo.',
 'XIII12':'Sửa hợp đồng mở rà soát ở kỳ XIV và đặt lại hai đợt kiểm chứng90/180ngày, mỗi đợt10PP. Hủy đóng nghĩa vụ, mất hỗ trợ chưa nhận và khóa node rà soát; không thu hồi lợi ích đã nhận.',
 }.items():LOC[IDS[node]+'_desc']=description
LOC={key:text.replace('epoch','kỳ chương trình').replace('snapshot','điều kiện').replace('Task','Công việc') for key,text in LOC.items()}
loc_path=ROOT/'localisation/english/VIE_md_politics_l_english.yml';loc=loc_path.read_text(encoding='utf-8-sig')
for key in list(LOC):
    if re.search(r'^ '+re.escape(key)+r':',loc,re.M):
        loc=re.sub(r'^ '+re.escape(key)+r':.*$',lambda _:' '+key+':0 "'+LOC[key].replace('"','\\"')+'"',loc,flags=re.M);LOC.pop(key)
loc_path.write_text(loc,encoding='utf-8-sig')
(ROOT/'localisation/english/VIE_md_politics_runtime_l_english.yml').write_text('l_english:\n'+'\n'.join(' '+key+':0 "'+text.replace('"','\\"')+'"' for key,text in LOC.items())+'\n',encoding='utf-8-sig')
# Canonical whitespace only in the adapter and touched political branch.
def clean(text):
    text='\n'.join(line.rstrip() for line in text.splitlines()).rstrip()+'\n'
    return re.sub(r'\n{3,}','\n\n',text)
def indent_script(text):
    result=[];depth=0
    for line in text.splitlines():
        line=line.strip()
        tokens=re.sub(r'"(?:\\.|[^"\\])*"|#[^\n]*','',line)
        leading=len(tokens)-len(tokens.lstrip('}'))
        result.append('\t'*max(0,depth-leading)+line if line else '')
        depth+=tokens.count('{')-tokens.count('}')
        assert depth>=0,'Script indentation found unbalanced braces'
    assert depth==0,'Script indentation found unbalanced braces'
    return '\n'.join(result).rstrip()+'\n'
for folder,name in [('common/scripted_effects','VIE_md_effects_politics_runtime.txt'),('common/scripted_triggers','VIE_md_triggers_politics_runtime.txt'),('events','VIE_md_politics_runtime_events.txt'),('common/decisions','VIE_md_politics_runtime_decisions.txt')]:
    target=ROOT/folder/name;target.write_text(indent_script(target.read_text(encoding='utf-8')),encoding='utf-8')
for relative in ['common/scripted_effects/VIE_md_effects_politics.txt','common/scripted_triggers/VIE_md_triggers_politics.txt',
                 'common/decisions/VIE_md_politics_decisions.txt','events/VIE_md_politics_events.txt']:
    target=ROOT/relative;target.write_text(clean(target.read_text(encoding='utf-8')),encoding='utf-8')
text=focus_path.read_text(encoding='utf-8')
start=re.search(r'\bfocus\s*=\s*\{\s*id\s*=\s*VIE_review_public_administration\b',text).start()
end=re.search(r'\bfocus\s*=\s*\{\s*id\s*=\s*VIE_asean_integration\b',text).start()
text=text[:start]+clean(text[start:end])+'\n\t'+text[end:]
focus_path.write_text(text,encoding='utf-8')
print(f'Runtime: {len(EFFECTS)} effects, {len(DECISIONS)} decisions, {len(EVENTS)-1} events; 74 political focuses retained')
