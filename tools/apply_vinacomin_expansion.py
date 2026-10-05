# -*- coding: utf-8 -*-
import sys

focus_file = 'common/national_focus/VIE_md_focus.txt'
with open(focus_file, 'r', encoding='utf-8') as f:
    content = f.read()

target_start = '\tfocus = {\n\t\tid = VIE_vinacomin_founding\n'
target_end = '\t\tai_will_do = { base = 60 }\n\t}'

idx_start = content.find(target_start)
if idx_start == -1:
    print('ERROR: target_start not found!')
    sys.exit(1)

# Find the end of VIE_mining_technology_upgrade before VIE_petrovietnam_expansion
idx_next = content.find('id = VIE_petrovietnam_expansion', idx_start)
idx_end = content.rfind('\t}', idx_start, idx_next) + 2

new_block = '''\tfocus = {
\t\tid = VIE_vinacomin_founding
\t\ticon = mining

\t\tx = 24
\t\ty = 1
\t\trelative_position_id = VIE_doi_moi_continues

\t\tcost = 5

\t\tprerequisite = { focus = VIE_doi_moi_continues }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\t# [DA DOI CHIEU] TKV (Tap doan Cong nghiep Than - Khoang san VN) thanh lap theo QD 345/2005/QD-TTg, 26/12/2005.
\t\tavailable = { date > 2005.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_vinacomin_founding"
\t\t\tincrease_economic_growth = yes
\t\t\tadd_ideas = VIE_vinacomin_idea
\t\t\tset_temp_variable = { temp_opinion = 3 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t\tset_temp_variable = { treasury_change = 1 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = { base = 70 }
\t}

\tfocus = {
\t\tid = VIE_vinacomin_restructuring
\t\ticon = focus_generic_industry_investment

\t\tx = -4
\t\ty = 1
\t\trelative_position_id = VIE_vinacomin_founding

\t\tcost = 7

\t\tprerequisite = { focus = VIE_vinacomin_founding }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_POLITICAL }

\t\t# QD 2006/QD-TTg (12/12/2017) phe duyet De an tai co cau TKV giai doan 2017-2020: thoai von ngoai nganh, tinh gon bo may.
\t\tavailable = { date > 2017.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_vinacomin_restructuring"
\t\t\tdecrease_corruption = yes
\t\t\tadd_political_power = 50
\t\t\tset_temp_variable = { temp_opinion = -2 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t\tset_temp_variable = { treasury_change = 2 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = { base = 65 }
\t}

\tfocus = {
\t\tid = VIE_green_mining_transition
\t\ticon = green_projects

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_vinacomin_restructuring

\t\tcost = 7

\t\tprerequisite = { focus = VIE_vinacomin_restructuring }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_STABILITY }

\t\t# Chuyen doi xanh nganh mo theo cam ket Net Zero COP26: dong mo lo thien, hoan nguyen moi truong, phat trien ham lo sau.
\t\tavailable = { date > 2022.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_green_mining_transition"
\t\t\tadd_ideas = VIE_green_mining_idea
\t\t\tadd_stability = 0.02
\t\t\tincrease_economic_growth = yes
\t\t}

\t\tai_will_do = { base = 60 }
\t}

\tfocus = {
\t\tid = VIE_closed_pit_mine_reclamation
\t\ticon = green_world

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_green_mining_transition

\t\tcost = 7

\t\tprerequisite = { focus = VIE_green_mining_transition }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_STABILITY }

\t\t# Hoan nguyen cac moong than lo thien dong cua (Coc Sau, Deo Nai...) thanh ho canh quan sinh thai, do thi du lich xanh.
\t\tavailable = { date > 2023.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_closed_pit_mine_reclamation"
\t\t\t523 = {
\t\t\t\tone_state_infrastructure = yes
\t\t\t}
\t\t\tadd_stability = 0.03
\t\t\tdecrease_corruption = yes
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = { base = 60 }
\t}

\tfocus = {
\t\tid = VIE_bauxite_tay_nguyen
\t\ticon = economic_privatisation

\t\tx = -2
\t\ty = 1
\t\trelative_position_id = VIE_vinacomin_founding

\t\tcost = 7

\t\tprerequisite = { focus = VIE_vinacomin_founding }
\t\tmutually_exclusive = { focus = VIE_bauxite_suspend }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\tavailable = { date > 2009.3.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_bauxite_tay_nguyen"
\t\t\t520 = {
\t\t\t\tone_state_industrial_complex = yes
\t\t\t\tadd_resource = { type = aluminium amount = 4 }
\t\t\t}
\t\t\tincrease_economic_growth = yes
\t\t\tadd_stability = -0.02
\t\t\tset_temp_variable = { temp_opinion = -3 }
\t\t\tchange_farmers_opinion = yes
\t\t\tset_temp_variable = { temp_opinion = 3 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t\thidden_effect = { set_country_flag = VIE_bauxite_done }
\t\t}

\t\tai_will_do = {
\t\t\tbase = 55
\t\t\tmodifier = { factor = 0 can_staff_an_industrial_complex = no }
\t\t\tmodifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_bauxite_suspend
\t\ticon = focus_generic_court

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_vinacomin_founding

\t\tcost = 7

\t\tprerequisite = { focus = VIE_vinacomin_founding }
\t\tmutually_exclusive = { focus = VIE_bauxite_tay_nguyen }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_STABILITY }

\t\tavailable = { date > 2009.3.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_bauxite_suspend"
\t\t\tadd_stability = 0.02
\t\t\tadd_ideas = VIE_bauxite_environmental_idea
\t\t\tset_temp_variable = { temp_opinion = 3 }
\t\t\tchange_farmers_opinion = yes
\t\t\tset_temp_variable = { temp_opinion = -3 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t\tVIE_bop_reform_small = yes
\t\t\thidden_effect = { set_country_flag = VIE_bauxite_done }
\t\t}

\t\tai_will_do = {
\t\t\tbase = 5
\t\t\tmodifier = { factor = 0 VIE_ai_historical = yes }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_tay_nguyen_eco_agriculture
\t\ticon = agriculture2

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_bauxite_suspend

\t\tcost = 7

\t\tprerequisite = { focus = VIE_bauxite_suspend }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_STABILITY }

\t\t# Bao ton rung dau nguon va dat do bazan, phat trien ca phe dac san Robusta va nong san sinh thai gia tri cao.
\t\tavailable = { date > 2011.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_tay_nguyen_eco_agriculture"
\t\t\t520 = {
\t\t\t\tadd_resource = { type = rubber amount = 8 }
\t\t\t}
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { temp_opinion = 5 }
\t\t\tchange_farmers_opinion = yes
\t\t\tadd_stability = 0.02
\t\t}

\t\tai_will_do = {
\t\t\tbase = 50
\t\t\tmodifier = { factor = 0 VIE_ai_historical = yes }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_rare_earths
\t\ticon = economic_civil_industry

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_bauxite_tay_nguyen

\t\tcost = 7

\t\tprerequisite = { focus = VIE_bauxite_tay_nguyen }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_RESEARCH }

\t\tavailable = { date > 2010.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_rare_earths"
\t\t\t523 = {
\t\t\t\tadd_resource = { type = composites amount = 4 }
\t\t\t}
\t\t\tset_temp_variable = { treasury_change = -1 }
\t\t\tmodify_treasury_effect = yes
\t\t\tset_temp_variable = { temp_opinion = 2 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t\thidden_effect = { set_country_flag = VIE_rare_earths_open }
\t\t\tcountry_event = { id = vie_dip.17 days = 10 }
\t\t}

\t\tai_will_do = { base = 55 }
\t}

\tfocus = {
\t\tid = VIE_rare_earth_processing
\t\ticon = economic_blue_print

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_rare_earths

\t\tcost = 7

\t\tprerequisite = { focus = VIE_rare_earths }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_RESEARCH }

\t\t# Xay dung to hop tinh che dat hiem do tinh khiet cao phuc vu cong nghiep dien tu, ban dan va vat lieu nam cham.
\t\tavailable = { date > 2020.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_rare_earth_processing"
\t\t\t524 = {
\t\t\t\tadd_resource = { type = composites amount = 3 }
\t\t\t}
\t\t\tadd_ideas = VIE_rare_earth_processing_idea
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = { base = 60 }
\t}

\tfocus = {
\t\tid = VIE_rare_earth_magnets
\t\ticon = GFX_focus_generic_industry_3

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_rare_earth_processing

\t\tcost = 7

\t\tprerequisite = { focus = VIE_rare_earth_processing }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_RESEARCH }

\t\t# San xuat nam cham dat hiem Neodymium (NdFeB) phuc vu dong co xe dien, tuabin gio va thiet bi dien tu cao cap.
\t\tavailable = { date > 2022.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_rare_earth_magnets"
\t\t\t524 = {
\t\t\t\tone_state_industrial_complex = yes
\t\t\t}
\t\t\tadd_tech_bonus = {
\t\t\t\tname = VIE_rare_earth_magnets
\t\t\t\tbonus = 0.5
\t\t\t\tahead_reduction = 1
\t\t\t\tcategory = CAT_electronics
\t\t\t}
\t\t\tadd_ideas = VIE_rare_earth_magnets_idea
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = {
\t\t\tbase = 65
\t\t\tmodifier = { factor = 0 can_staff_an_industrial_complex = no }
\t\t\tmodifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_than_quang_ninh
\t\ticon = coal_mining

\t\tx = 2
\t\ty = 1
\t\trelative_position_id = VIE_vinacomin_founding

\t\tcost = 7

\t\tprerequisite = { focus = VIE_vinacomin_founding }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\t# Mo rong khai thac than Quang Ninh: co gioi hoa ham lo, cung ung than cho nhiet dien va cong nghiep luyen kim.
\t\tavailable = { date > 2006.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_than_quang_ninh"
\t\t\t523 = {
\t\t\t\tone_state_industrial_complex = yes
\t\t\t\tadd_resource = { type = steel amount = 2 }
\t\t\t}
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t\tset_temp_variable = { temp_opinion = 3 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t\thidden_effect = { set_country_flag = VIE_coal_mining_expanded }
\t\t}

\t\tai_will_do = {
\t\t\tbase = 60
\t\t\tmodifier = { factor = 0 can_staff_an_industrial_complex = no }
\t\t\tmodifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_thach_khe_mine_start
\t\ticon = focus_generic_improve_roads

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_than_quang_ninh

\t\tcost = 7

\t\tprerequisite = { focus = VIE_than_quang_ninh }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\t# Du an mo sat Thach Khe (Ha Tinh): cap phep dau tu 2008; cuoi 2016 Ha Tinh de xuat tam dung vi cong nghe khai thac va rui ro moi truong.
\t\t# Day la nhanh gia dinh (tiep tuc khai thac): AI theo lich su khong chon.
\t\tavailable = { date > 2016.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_thach_khe_mine_start"
\t\t\t521 = {
\t\t\t\tadd_resource = { type = steel amount = 4 }
\t\t\t}
\t\t\tincrease_economic_growth = yes
\t\t\tadd_stability = -0.02
\t\t\tset_temp_variable = { temp_opinion = -2 }
\t\t\tchange_farmers_opinion = yes
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = {
\t\t\tbase = 15
\t\t\tmodifier = { factor = 0 VIE_ai_historical = yes }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_thach_khe_steel_cluster
\t\ticon = steel_production

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_thach_khe_mine_start

\t\tcost = 7

\t\tprerequisite = { focus = VIE_thach_khe_mine_start }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\t# Xay dung to hop luyen thep gan lien voi mo sat Thach Khe va cang Vung Ang, tu chu phoi thep chat luong cao.
\t\tavailable = { date > 2019.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_thach_khe_steel_cluster"
\t\t\t521 = {
\t\t\t\tone_state_industrial_complex = yes
\t\t\t\tadd_resource = { type = steel amount = 6 }
\t\t\t}
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t\tset_temp_variable = { temp_opinion = 4 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t}

\t\tai_will_do = {
\t\t\tbase = 15
\t\t\tmodifier = { factor = 0 VIE_ai_historical = yes }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_coal_to_electricity
\t\ticon = focus_generic_electrification

\t\tx = 2
\t\ty = 1
\t\trelative_position_id = VIE_than_quang_ninh

\t\tcost = 7

\t\tprerequisite = { focus = VIE_than_quang_ninh }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\t# Xay dung cac cum nha may nhiet dien than (Mong Duong, Cam Pha...) ket noi than Quang Ninh voi luoi dien quoc gia.
\t\tavailable = {
\t\t\thas_completed_focus = VIE_son_la_dam
\t\t}

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_coal_to_electricity"
\t\t\t523 = {
\t\t\t\tone_state_industrial_complex = yes
\t\t\t}
\t\t\tadd_ideas = VIE_coal_power_idea
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = {
\t\t\tbase = 60
\t\t\tmodifier = { factor = 0 can_staff_an_industrial_complex = no }
\t\t\tmodifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_ultra_supercritical_coal
\t\ticon = focus_generic_industry_investment

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_coal_to_electricity

\t\tcost = 7

\t\tprerequisite = { focus = VIE_coal_to_electricity }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\t# Chuyen giao cong nghe nhiet dien sieu toi han USC: hieu suat vuot 45%, tiet kiem than va giam 20% phat thai.
\t\tavailable = { date > 2018.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_ultra_supercritical_coal"
\t\t\t523 = {
\t\t\t\tone_state_industrial_complex = yes
\t\t\t}
\t\t\tadd_ideas = VIE_usc_coal_power_idea
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -3 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = {
\t\t\tbase = 60
\t\t\tmodifier = { factor = 0 can_staff_an_industrial_complex = no }
\t\t\tmodifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
\t\t}
\t}

\tfocus = {
\t\tid = VIE_nui_phao_tungsten
\t\ticon = steel_production

\t\tx = 6
\t\ty = 1
\t\trelative_position_id = VIE_vinacomin_founding

\t\tcost = 7

\t\tprerequisite = { focus = VIE_vinacomin_founding }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\t# [DA DOI CHIEU] mo Nui Phao (Dai Tu, Thai Nguyen): xay dung tu giua 2011, san xuat thuong mai tu quy I/2014.
\t\tavailable = { date > 2013.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_nui_phao_tungsten"
\t\t\t523 = {
\t\t\t\tadd_resource = { type = tungsten amount = 4 }
\t\t\t}
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t\tset_temp_variable = { temp_opinion = 2 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t}

\t\tai_will_do = { base = 60 }
\t}

\tfocus = {
\t\tid = VIE_mining_technology_upgrade
\t\ticon = economic_sciencer

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_nui_phao_tungsten

\t\tcost = 7

\t\tprerequisite = { focus = VIE_nui_phao_tungsten }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_INDUSTRY }

\t\t# Hien dai hoa cong nghe khai thac, he thong dieu do tu dong hoa va quan trac dia ky thuat tai cac mo lon.
\t\tavailable = { date > 2018.12.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_mining_technology_upgrade"
\t\t\tadd_ideas = VIE_mining_tech_idea
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -2 }
\t\t\tmodify_treasury_effect = yes
\t\t}

\t\tai_will_do = { base = 60 }
\t}

\tfocus = {
\t\tid = VIE_hc_starck_acquisition
\t\ticon = economic_sciencer

\t\tx = 0
\t\ty = 1
\t\trelative_position_id = VIE_mining_technology_upgrade

\t\tcost = 7

\t\tprerequisite = { focus = VIE_mining_technology_upgrade }
\t\tsearch_filters = { FOCUS_FILTER_ECONOMY FOCUS_FILTER_RESEARCH }

\t\t# Masan High-Tech Materials mua lai mang vonfram cua H.C. Starck Duc, lam chu chuoi gia tri vat lieu cong nghe cao toan cau.
\t\tavailable = { date > 2020.5.31 }

\t\tcompletion_reward = {
\t\t\tlog = "[GetDateText]: [Root.GetName]: Focus VIE_hc_starck_acquisition"
\t\t\tincrease_economic_growth = yes
\t\t\tset_temp_variable = { treasury_change = -4 }
\t\t\tmodify_treasury_effect = yes
\t\t\tadd_ideas = VIE_hc_starck_idea
\t\t\tset_temp_variable = { temp_opinion = 3 }
\t\t\tchange_industrial_conglomerates_opinion = yes
\t\t}

\t\tai_will_do = { base = 60 }
\t}'''

updated_content = content[:idx_start] + new_block + content[idx_end:]

with open(focus_file, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(updated_content)

print('Successfully applied 18-focus Vinacomin expansion to VIE_md_focus.txt')
