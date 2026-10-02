"""Generator for Truc 1B (Program Engine): chuong trinh mua sam alt-history cua hai quan.

Thiet ke: VIE_naval_truc3_review_and_plan.md (A6, 5.5, 5.6). Script, event, Decision, idea, scripted loc va
loc deu sinh tu bang PROGRAMS duoi day, vi create_ship / create_equipment_variant / ten co/bien la literal.
Chay tu goc repo:

    python tools/gen_p1b.py

Them mot chuong trinh = them mot dong vao PROGRAMS (va ENABLED) roi chay lai. Cac file sinh co dong dau
"GENERATED" - khong sua tay.
"""
from __future__ import annotations

import os
import sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

LOC_MULT = {0: '1', 1: '1.15', 2: '1.3'}
LEAD_MULT = {0: 1.0, 1: 1.2, 2: 1.4}
SPACING_DAYS = 240   # 8 thang giua hai tau

ENABLED = ['corvette', 'frigate_med', 'asw_frigate', 'ssk_reg', 'bastion2', 'amphib', 'destroyer', 'carrier', 'ssn']   # buoc 6; buoc 7 them phan con lai

# Moi chuong trinh. Truong:
#  n: ma so (hidden delivery event = vie_p1b.(10+n))     key: tien to bien/co (VIE_p1b_<key>_*)
#  name: ten hien thi                                      desc: mo ta Decision
#  hull / variant / modules / role_icon: variant VIE tu tao (allow_without_tech = yes, mau HOL_military.077)
#  techs: tech cap luc ky                                  unit: ty USD / tau (nhap khau)
#  q: (min, giua, max) so luong                            lead: thang toi tau dau
#  partners: doi tac nhap khau (quoc gia ton tai & khong chien tranh)
#  hyb / dom: dieu kien Truc 2 cho hybrid / noi dia (None = khong mo)
#  focus / date: loi vao Decision                           sb / integ: exp Truc 2 moi tau (nhan 0 / 0,5 / 1 theo muc)
#  counter: bo dem lop (tuy chon)                          names: ten tau placeholder
PROGRAMS = {
    'corvette': dict(
        n=1, name='Hộ vệ hạm nhẹ', desc='Đặt đóng hộ vệ hạm nhẹ cho các biên đội ven bờ và vùng đặc quyền kinh tế.',
        hull='corvette_hull_4', variant='VIE Corvette Class', role_icon=2,
        modules=[
            ('fixed_ship_engine_slot', 'module_light_surface_diesel_power_2'),
            ('fixed_ship_fire_control_system_slot', 'module_digital_integrated_fire_control'),
            ('fixed_ship_radar_slot', 'module_radar_4'),
            ('fixed_ship_auxillary_slot', 'module_torpedoes_3'),
            ('fixed_ship_battery_slot', 'module_76mm_gun_3'),
            ('front_1_custom_slot', 'module_naval_missile_mount_quad'),
            ('rear_1_custom_slot', 'module_light_helipad_2'),
            ('fixed_ship_missile_ammo_slot', 'module_naval_ammo_balanced_4'),
        ],
        techs=['corvette_hull_4'], unit=0.40, q=(2, 4, 6), lead=30, partners=['HOL', 'SOV'],
        hyb=['check_variable = { VIE_var_small_combatant_tier > 0 }', 'check_variable = { VIE_var_ba_son_tier > 0 }'],
        dom=['check_variable = { VIE_var_small_combatant_tier > 1 }', 'check_variable = { VIE_var_ba_son_tier > 1 }'],
        focus='VIE_nf_medium_force', date='2015.12.31', sb=3, integ=0,
        names=['Hộ vệ hạm 1', 'Hộ vệ hạm 2', 'Hộ vệ hạm 3', 'Hộ vệ hạm 4', 'Hộ vệ hạm 5', 'Hộ vệ hạm 6'],
    ),
    'frigate_med': dict(
        n=2, name='Khinh hạm cỡ trung', desc='Đặt đóng khinh hạm cỡ trung có sàn trực thăng và phòng không tầm trung.',
        hull='frigate_hull_4', variant='VIE Frigate Class', role_icon=2,
        modules=[
            ('fixed_ship_engine_slot', 'module_light_surface_diesel_power_2'),
            ('fixed_ship_fire_control_system_slot', 'module_digital_integrated_fire_control'),
            ('fixed_ship_radar_slot', 'module_radar_4'),
            ('fixed_ship_auxillary_slot_2', 'module_naval_vls_cells_16'),
            ('fixed_ship_auxillary_slot_1', 'module_naval_vls_cells_16'),
            ('fixed_ship_auxillary_slot', 'module_chain_gun'),
            ('fixed_ship_battery_slot', 'module_76mm_gun_3'),
            ('front_1_custom_slot', 'module_naval_missile_mount_quad'),
            ('rear_1_custom_slot', 'module_light_helipad_1'),
            ('fixed_ship_missile_ammo_slot', 'module_naval_ammo_balanced_2'),
        ],
        techs=['frigate_hull_4'], unit=0.45, q=(2, 3, 4), lead=40, partners=['HOL', 'KOR'],
        hyb=['check_variable = { VIE_var_ba_son_tier > 0 }'],
        dom=['check_variable = { VIE_var_integration_tier > 0 }', 'check_variable = { VIE_var_ba_son_tier > 1 }'],
        focus='VIE_nf_medium_force', date='2017.12.31', sb=3, integ=2,
        names=['Khinh hạm 1', 'Khinh hạm 2', 'Khinh hạm 3', 'Khinh hạm 4'],
    ),
    'asw_frigate': dict(
        n=3, name='Khinh hạm chống ngầm', desc='Đặt đóng khinh hạm chống ngầm cơ động với sonar kéo, ngư lôi và trực thăng săn ngầm.',
        hull='frigate_hull_4', variant='VIE ASW Frigate Class', role_icon=2,
        modules=[
            ('fixed_ship_engine_slot', 'module_light_surface_diesel_power_2'),
            ('fixed_ship_fire_control_system_slot', 'module_digital_integrated_fire_control'),
            ('fixed_ship_radar_slot', 'module_sonar_4'),
            ('fixed_ship_auxillary_slot_2', 'module_torpedoes_3'),
            ('fixed_ship_auxillary_slot_1', 'module_naval_vls_cells_16'),
            ('fixed_ship_auxillary_slot', 'module_chain_gun'),
            ('fixed_ship_battery_slot', 'module_76mm_gun_3'),
            ('front_1_custom_slot', 'module_naval_missile_mount_quad'),
            ('rear_1_custom_slot', 'module_light_helipad_1'),
            ('fixed_ship_missile_ammo_slot', 'module_naval_ammo_balanced_2'),
        ],
        techs=['frigate_hull_4'], unit=0.50, q=(2, 3, 4), lead=40, partners=['HOL', 'SOV'],
        hyb=['check_variable = { VIE_var_ba_son_tier > 0 }'],
        dom=['check_variable = { VIE_var_integration_tier > 0 }'],
        focus='VIE_nf_medium_force', date='2017.12.31', sb=3, integ=2,
        names=['Khinh hạm chống ngầm 1', 'Khinh hạm chống ngầm 2', 'Khinh hạm chống ngầm 3', 'Khinh hạm chống ngầm 4'],
    ),
    'ssk_reg': dict(
        n=4, name='Tàu ngầm tấn công khu vực', desc='Đặt đóng tàu ngầm diesel-điện tấn công khu vực, bổ sung cho đội Kilo.',
        hull='attack_submarine_hull_4', variant='VIE Regional SSK Class', role_icon=14,
        modules=[
            ('fixed_ship_engine_slot', 'module_sub_diesel_electric_power3'),
            ('fixed_ship_radar_slot', 'module_sonar_5'),
            ('fixed_ship_auxillary_slot_3', 'module_torpedoes_3'),
            ('fixed_ship_auxillary_slot_2', 'module_sub_esm_2'),
            ('fixed_ship_auxillary_slot_1', 'module_minelaying'),
            ('fixed_ship_auxillary_slot', 'module_torpedoes_3'),
            ('fixed_ship_battery_slot', 'module_anti_ship_torpedoes_3'),
        ],
        techs=['attack_submarine_hull_4'], unit=0.55, q=(2, 3, 4), lead=54, partners=['SOV'],
        hyb=['check_variable = { VIE_var_ba_son_tier > 2 }', 'check_variable = { VIE_var_integration_tier > 1 }', 'VIE_naval_has_sub_mro = yes'],
        dom=None,
        focus='VIE_nf_medium_force', date='2019.12.31', sb=4, integ=3,
        extra=[('VIE_p1b_d2_done_tt', 'has_country_flag = VIE_nf_d2_done'),
               ('VIE_p1b_p4_branch_tt', 'OR = {\n\thas_completed_focus = VIE_nf_denial_subs\n\thas_completed_focus = VIE_nf_regional_frigates\n}')],
        names=['Tàu ngầm khu vực 1', 'Tàu ngầm khu vực 2', 'Tàu ngầm khu vực 3', 'Tàu ngầm khu vực 4'],
    ),
    'bastion2': dict(
        n=6, kind='coastal', name='Bastion-P mở rộng', desc='Đặt thêm tổ hợp tên lửa bờ Bastion-P để mở rộng phòng thủ ven bờ. Chỉ nhập khẩu.',
        techs=[], unit=0.15, q=(1, 2, 3), lead=18, partners=['SOV'], hyb=None, dom=None,
        focus='VIE_nf_denial_defence', date=None, sb=0, integ=0,
    ),
    'amphib': dict(
        n=7, name='Tàu đổ bộ trực thăng', desc='Đặt đóng tàu đổ bộ trực thăng (LHD) cho hạm đội đổ bộ.',
        hull='helicopter_operator_hull_3', variant='VIE Amphibious Class', role_icon=2,
        modules=[
            ('fixed_ship_engine_slot', 'module_surface_diesel_power_1'),
            ('fixed_ship_fire_control_system_slot', 'module_digital_integrated_fire_control'),
            ('fixed_ship_radar_slot', 'module_radar_4'),
            ('fixed_ship_auxillary_slot_3', 'module_fuel_tank'),
            ('fixed_ship_auxillary_slot_2', 'module_chain_gun'),
            ('fixed_ship_auxillary_slot', 'module_chain_gun'),
            ('fixed_ship_battery_slot', 'module_light_flight_deck_1'),
            ('front_1_custom_slot', 'module_helipads_2'),
            ('mid_1_custom_slot', 'module_helipads_2'),
            ('rear_1_custom_slot', 'module_helipads_2'),
        ],
        techs=['helicopter_operator_hull_3'], unit=0.60, q=(1, 1, 2), lead=54, partners=['KOR', 'FRA'],
        hyb=['check_variable = { VIE_var_ba_son_tier > 1 }'],
        dom=['check_variable = { VIE_var_ba_son_tier > 2 }'],
        focus='VIE_nf_lhd_program', date='2021.12.31', sb=4, integ=2,
        names=['Tàu đổ bộ trực thăng 1', 'Tàu đổ bộ trực thăng 2'],
    ),
    'destroyer': dict(
        n=8, name='Khu trục hạm', desc='Đặt đóng khu trục hạm phòng không tầm xa cho hạm đội viễn dương.',
        hull='destroyer_hull_4', variant='VIE Destroyer Class', role_icon=2,
        modules=[
            ('fixed_ship_engine_slot', 'module_surface_diesel_power_3'),
            ('fixed_ship_fire_control_system_slot', 'module_advanced_integrated_missile_radar_control'),
            ('fixed_ship_radar_slot', 'module_radar_4'),
            ('fixed_ship_auxillary_slot_3', 'module_ciws_3'),
            ('fixed_ship_auxillary_slot_2', 'module_torpedoes_3'),
            ('fixed_ship_auxillary_slot', 'module_naval_vls_cells_16'),
            ('fixed_ship_battery_slot', 'module_76mm_gun_3'),
            ('front_1_custom_slot', 'module_naval_missile_mount_quad'),
            ('mid_1_custom_slot', 'module_ram_3'),
            ('mid_2_custom_slot', 'module_ciws_3'),
            ('rear_1_custom_slot', 'module_light_helipad_2'),
            ('fixed_ship_missile_ammo_slot', 'module_naval_ammo_balanced_4'),
        ],
        techs=['destroyer_hull_4'], unit=0.70, q=(2, 2, 3), lead=48, partners=['RAJ', 'KOR'],
        hyb=['check_variable = { VIE_var_integration_tier > 0 }', 'check_variable = { VIE_var_ba_son_tier > 1 }'],
        dom=['check_variable = { VIE_var_integration_tier > 1 }', 'check_variable = { VIE_var_ba_son_tier > 2 }'],
        focus='VIE_nf_ocean_escort', date='2023.12.31', sb=4, integ=3, counter='VIE_var_hulls_destroyer',
        names=['Khu trục hạm 1', 'Khu trục hạm 2', 'Khu trục hạm 3'],
    ),
    'carrier': dict(
        n=10, name='Tàu sân bay hạng nhẹ', desc='Đặt đóng tàu sân bay hạng nhẹ cho nhóm tác chiến viễn dương.',
        hull='carrier_hull_3', variant='VIE Light Carrier Class', role_icon=2,
        modules=[
            ('fixed_ship_engine_slot', 'module_surface_diesel_power_3'),
            ('fixed_ship_fire_control_system_slot', 'module_advanced_integrated_missile_radar_control'),
            ('fixed_ship_radar_slot', 'module_radar_4'),
            ('fixed_ship_auxillary_slot_2', 'module_ciws_3'),
            ('fixed_ship_auxillary_slot_1', 'module_ram_3'),
            ('fixed_ship_auxillary_slot', 'module_esm_1'),
            ('fixed_ship_flight_deck', 'module_flight_deck_4'),
            ('front_1_custom_slot', 'module_ram_3'),
            ('front_2_custom_slot', 'module_ciws_3'),
            ('mid_1_custom_slot', 'module_helipads_3'),
            ('rear_1_custom_slot', 'module_naval_adl_3'),
            ('rear_2_custom_slot', 'module_ciws_3'),
        ],
        techs=['carrier_hull_3'], unit=2.70, q=(1, 1, 1), lead=84, partners=['RAJ'],
        hyb=['has_country_flag = VIE_cap_mature_naval_industry'], dom=None,
        focus='VIE_nf_naval_aviation', date='2027.12.31', sb=6, integ=4, counter='VIE_var_hulls_carrier',
        names=['Tàu sân bay hạng nhẹ'],
    ),
    'ssn': dict(
        n=11, name='Tàu ngầm hạt nhân', desc='Đặt đóng tàu ngầm hạt nhân tấn công, chương trình lớn nhất của hạm đội.',
        hull='attack_submarine_hull_5', variant='VIE SSN Class', role_icon=14,
        modules=[
            ('fixed_ship_engine_slot', 'module_sub_early_reactor_power'),
            ('fixed_ship_radar_slot', 'module_sonar_5'),
            ('fixed_ship_auxillary_slot_3', 'module_torpedoes_3'),
            ('fixed_ship_auxillary_slot_2', 'module_sub_esm_2'),
            ('fixed_ship_auxillary_slot_1', 'module_minelaying'),
            ('fixed_ship_auxillary_slot', 'module_torpedoes_3'),
            ('fixed_ship_battery_slot', 'module_anti_ship_torpedoes_3'),
        ],
        techs=['attack_submarine_hull_5', 'tech_nuclear_power_systems_1'], unit=2.00, q=(1, 1, 2), lead=96, partners=['SOV'],
        hyb=['has_country_flag = VIE_cap_mature_naval_industry'], dom=None,
        focus='VIE_nf_carrier_group', date='2029.12.31', sb=6, integ=6,
        extra=[('VIE_p1b_nuclear_tt', 'VIE_naval_has_nuclear_tech = yes')],
        names=['Tàu ngầm hạt nhân 1', 'Tàu ngầm hạt nhân 2'],
    ),
}

HEADER = '# GENERATED by tools/gen_p1b.py from the PROGRAMS table - do not edit by hand.\n# Thiet ke: VIE_naval_truc3_review_and_plan.md (A6, 5.5, 5.6).\n\n'


def fmt(x: float) -> str:
    return ('%g' % x)


def partner_expr(partners: list[str], indent: str) -> str:
    inner = ''.join('%s\tAND = {\n%s\t\tcountry_exists = %s\n%s\t\tNOT = { has_war_with = %s }\n%s\t}\n' % (indent, indent, t, indent, t, indent) for t in partners)
    return '%sOR = {\n%s%s}\n' % (indent, inner, indent)


def conds(cs: list[str], indent: str) -> str:
    return ''.join('%s%s\n' % (indent, c) for c in cs)


def prog(k):
    return PROGRAMS[k]


# ------------------------------------------------------------------ scripted effects
def gen_effects() -> str:
    o = HEADER
    o += '''# ---- Chi phi (ty USD) vao bien tam VIE_naval_cost: so tau x gia/tau x he so noi dia hoa (1,0 / 1,15 / 1,3) ----
VIE_p1b_cost = {
	set_temp_variable = { VIE_naval_cost = VIE_p1b_qty }
	multiply_temp_variable = { VIE_naval_cost = VIE_p1b_unit }
	if = {
		limit = { check_variable = { VIE_p1b_loc = 1 } }
		multiply_temp_variable = { VIE_naval_cost = 1.15 }
	}
	else_if = {
		limit = { check_variable = { VIE_p1b_loc = 2 } }
		multiply_temp_variable = { VIE_naval_cost = 1.3 }
	}
	# P1 (ho ve han nhe) hybrid/noi dia la tau chien dau co nho: he so Decision 3 cua Truc 2 (0,8-0,9) ap dung
	# nhu voi Molniya pha 2 cua Truc 1. Nhap khau khong duoc giam.
	if = {
		limit = {
			check_variable = { VIE_p1b_cur = 1 }
			check_variable = { VIE_p1b_loc > 0 }
			check_variable = { VIE_small_combatant_cost_mult > 0 }
		}
		multiply_temp_variable = { VIE_naval_cost = VIE_small_combatant_cost_mult }
	}
}

# ---- Funding Gate (A5): dung VIE_naval_can_fund cua Truc 1. Truot -> event .3 ----
VIE_p1b_funding_check = {
	VIE_p1b_cost = yes
	if = {
		limit = { VIE_naval_can_fund = yes }
		VIE_p1b_contract = yes
	}
	else = {
		country_event = { id = vie_p1b.3 }
	}
}

# ---- Tra tien: ngan kho hoac vay (no = chi phi x 1,1 neu co VIE_p1b_use_debt) ----
VIE_p1b_pay = {
	VIE_p1b_cost = yes
	if = {
		limit = { has_country_flag = VIE_p1b_use_debt }
		set_temp_variable = { debt_change = VIE_naval_cost }
		multiply_temp_variable = { debt_change = 1.1 }
		modify_debt_effect = yes
		clr_country_flag = VIE_p1b_use_debt
	}
	else = {
		set_temp_variable = { treasury_change = VIE_naval_cost }
		multiply_temp_variable = { treasury_change = -1 }
		modify_treasury_effect = yes
	}
}

'''
    # dispatchers
    o += '# ---- Dispatch theo VIE_p1b_cur ----\nVIE_p1b_contract = {\n'
    first = True
    for k in ENABLED:
        o += '\t%s = {\n\t\tlimit = { check_variable = { VIE_p1b_cur = %d } }\n\t\tVIE_p1b_contract_%s = yes\n\t}\n' % ('if' if first else 'else_if', prog(k)['n'], k)
        first = False
    o += '}\n\nVIE_p1b_cancel = {\n'
    first = True
    for k in ENABLED:
        o += '\t%s = {\n\t\tlimit = { check_variable = { VIE_p1b_cur = %d } }\n\t\tset_country_flag = VIE_p1b_%s_cancelled\n\t}\n' % ('if' if first else 'else_if', prog(k)['n'], k)
        first = False
    o += '}\n\n'

    for k in ENABLED:
        p = prog(k)
        n = p['n']
        coastal = p.get('kind') == 'coastal'
        o += '########################################################################\n# P%d %s (%s)\n########################################################################\n' % (n, p['name'], k)
        # load
        o += 'VIE_p1b_load_%s = {\n' % k
        o += '\tset_variable = { VIE_p1b_cur = %d }\n\tset_variable = { VIE_p1b_unit = %s }\n' % (n, fmt(p['unit']))
        for i, q in enumerate(p['q']):
            o += '\tset_variable = { VIE_p1b_q%d = %d }\n' % (i + 1, q)
        o += '\tset_variable = { VIE_p1b_qty = 0 }\n\tset_variable = { VIE_p1b_loc = 0 }\n'
        o += '\tset_variable = { VIE_p1b_ok_import = 0 }\n\tset_variable = { VIE_p1b_ok_hybrid = 0 }\n\tset_variable = { VIE_p1b_ok_domestic = 0 }\n'
        o += '\tif = {\n\t\tlimit = {\n' + partner_expr(p['partners'], '\t\t\t') + '\t\t}\n\t\tset_variable = { VIE_p1b_ok_import = 1 }\n\t}\n'
        if p['hyb']:
            o += '\tif = {\n\t\tlimit = {\n' + conds(p['hyb'], '\t\t\t') + '\t\t}\n\t\tset_variable = { VIE_p1b_ok_hybrid = 1 }\n\t}\n'
        if p['dom']:
            o += '\tif = {\n\t\tlimit = {\n' + conds(p['dom'], '\t\t\t') + '\t\t}\n\t\tset_variable = { VIE_p1b_ok_domestic = 1 }\n\t}\n'
        o += '}\n\n'
        # variant (khong co cho he thong bo)
        if not coastal:
          o += 'VIE_p1b_ensure_variant_%s = {\n\tif = {\n\t\tlimit = { NOT = { has_country_flag = VIE_p1b_variant_%s_done } }\n\t\tset_country_flag = VIE_p1b_variant_%s_done\n' % (k, k, k)
          o += '\t\tcreate_equipment_variant = {\n\t\t\tname = "%s"\n\t\t\ttype = %s\n\t\t\tallow_without_tech = yes\n\t\t\tparent_version = 0\n\t\t\trole_icon_index = %d\n\t\t\tmodules = {\n' % (p['variant'], p['hull'], p['role_icon'])
          for s_, m_ in p['modules']:
            o += '\t\t\t\t%s = %s\n' % (s_, m_)
          o += '\t\t\t}\n\t\t}\n\t}\n}\n\n'
        # contract
        lead = p['lead'] * 30
        days = {m: int(round(lead * LEAD_MULT[m])) for m in (0, 1, 2)}
        o += 'VIE_p1b_contract_%s = {\n' % k
        o += '\tset_country_flag = VIE_p1b_%s_contracted\n' % k
        o += '\tset_variable = { VIE_p1b_%s_qty_ordered = VIE_p1b_qty }\n\tset_variable = { VIE_p1b_%s_qty_delivered = 0 }\n\tset_variable = { VIE_p1b_%s_localization = VIE_p1b_loc }\n' % (k, k, k)
        o += '\tVIE_p1b_pay = yes\n'
        if p['techs']:
            o += '\tset_technology = { %s }\n' % ' '.join('%s = 1' % t for t in p['techs'])
        if not coastal:
            o += '\tVIE_p1b_ensure_variant_%s = yes\n' % k
        o += '\tVIE_p1b_program_start = yes\n'
        o += '\tset_temp_variable = { VIE_p1b_days = %d }\n' % days[0]   # bien tam dat ngoai if
        o += '\tif = {\n\t\tlimit = { check_variable = { VIE_p1b_loc = 1 } }\n\t\tset_temp_variable = { VIE_p1b_days = %d }\n\t}\n' % days[1]
        o += '\tif = {\n\t\tlimit = { check_variable = { VIE_p1b_loc = 2 } }\n\t\tset_temp_variable = { VIE_p1b_days = %d }\n\t}\n' % days[2]
        o += '\tset_temp_variable = { VIE_p1b_total = VIE_p1b_qty }\n\tadd_to_temp_variable = { VIE_p1b_total = -1 }\n\tmultiply_temp_variable = { VIE_p1b_total = %d }\n\tadd_to_temp_variable = { VIE_p1b_total = VIE_p1b_days }\n' % SPACING_DAYS
        o += '\tadd_timed_idea = { idea = VIE_p1b_prog_%s days = VIE_p1b_total }\n' % k
        o += '\tcountry_event = { id = vie_p1b.%d days = VIE_p1b_days }\n}\n\n' % (10 + n)
        # deliver
        o += 'VIE_p1b_deliver_%s = {\n' % k
        if not coastal:
            o += '\tVIE_p1b_ensure_variant_%s = yes\n' % k
        names = p['names'] if not coastal else []
        if coastal:
            o += '\tset_variable = { VIE_bastion_site = VIE_p1b_%s_qty_delivered }\n\tadd_to_variable = { VIE_bastion_site = 1 }\n\tVIE_naval_bastion_site = yes\n' % k
        for i, nm in enumerate(names):
            kw = 'if' if i == 0 else ('else_if' if i < len(names) - 1 else 'else')
            ship = 'create_ship = { type = %s equipment_variant = "%s" creator = VIE name = "%s" }' % (p['hull'], p['variant'], nm)
            if kw == 'else':
                o += '\telse = {\n\t\t%s\n\t}\n' % ship
            else:
                o += '\t%s = {\n\t\tlimit = { check_variable = { VIE_p1b_%s_qty_delivered = %d } }\n\t\t%s\n\t}\n' % (kw, k, i, ship)
        o += '\tadd_to_variable = { VIE_p1b_%s_qty_delivered = 1 }\n' % k
        if not coastal:
            o += '\tadd_to_variable = { VIE_var_hulls_delivered = 1 }\n'
        if p.get('counter'):
            o += '\tadd_to_variable = { %s = 1 }\n' % p['counter']
        for amount, helper in ((p['sb'], 'VIE_nav_add_shipbuilding_exp'), (p['integ'], 'VIE_nav_add_integration_exp')):
            if not amount:
                continue
            o += '\tif = {\n\t\tlimit = { check_variable = { VIE_p1b_%s_localization = 2 } }\n\t\tset_temp_variable = { VIE_nav_exp_gain = %s }\n\t\t%s = yes\n\t}\n' % (k, fmt(amount), helper)
            o += '\telse_if = {\n\t\tlimit = { check_variable = { VIE_p1b_%s_localization = 1 } }\n\t\tset_temp_variable = { VIE_nav_exp_gain = %s }\n\t\t%s = yes\n\t}\n' % (k, fmt(amount / 2), helper)
        o += '\tif = {\n\t\tlimit = { check_variable = { VIE_p1b_%s_qty_delivered < VIE_p1b_%s_qty_ordered } }\n\t\tcountry_event = { id = vie_p1b.%d days = %d }\n\t}\n\telse = {\n\t\tVIE_p1b_program_end = yes\n\t}\n}\n\n' % (k, k, 10 + n, SPACING_DAYS)
    return o


# ------------------------------------------------------------------ events
def gen_events() -> str:
    o = 'add_namespace = vie_p1b\n\n' + HEADER
    o += '''# Truc 1B - Program Engine. Event dung chung doc VIE_p1b_cur (ma chuong trinh) va cac bien VIE_p1b_*
# do VIE_p1b_load_<p> nap khi bam Decision. Khong co cua so lich su, khong event tu kich.
#   .1 so luong   .2 muc noi dia hoa   .3 thieu von   .11+ giao hang an (10 + ma chuong trinh)
# Cac event .1-.3 do nguoi choi bam Decision nen khong di qua VIE_popup_cd.

# .1  So luong
country_event = {
	id = vie_p1b.1
	title = vie_p1b.1.t
	desc = vie_p1b.1.d
	picture = GFX_report_event_generic_read_write
	is_triggered_only = yes

	option = {
		name = vie_p1b.1.a
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.1.a executed"
		set_variable = { VIE_p1b_qty = VIE_p1b_q1 }
		country_event = { id = vie_p1b.2 }
		ai_chance = { base = 60 }
	}

	option = {
		name = vie_p1b.1.b
		trigger = { check_variable = { VIE_p1b_q2 > VIE_p1b_q1 } }
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.1.b executed"
		set_variable = { VIE_p1b_qty = VIE_p1b_q2 }
		country_event = { id = vie_p1b.2 }
		ai_chance = { base = 30 }
	}

	option = {
		name = vie_p1b.1.c
		trigger = { check_variable = { VIE_p1b_q3 > VIE_p1b_q2 } }
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.1.c executed"
		set_variable = { VIE_p1b_qty = VIE_p1b_q3 }
		country_event = { id = vie_p1b.2 }
		ai_chance = { base = 10 }
	}
}

# .2  Muc noi dia hoa. Chuoi tu .1, mien VIE_popup_cd
country_event = {
	id = vie_p1b.2
	title = vie_p1b.2.t
	desc = vie_p1b.2.d
	picture = GFX_report_event_generic_read_write
	is_triggered_only = yes

	# A - Nhap khau: x1,0, giao dung han, khong co kinh nghiem cho Truc 2
	option = {
		name = vie_p1b.2.a
		trigger = { check_variable = { VIE_p1b_ok_import = 1 } }
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.2.a executed"
		set_variable = { VIE_p1b_loc = 0 }
		VIE_p1b_funding_check = yes
		ai_chance = { base = 60 }
	}

	# B - Hybrid: x1,15, giao cham hon 20%, 50% kinh nghiem
	option = {
		name = vie_p1b.2.b
		trigger = { check_variable = { VIE_p1b_ok_hybrid = 1 } }
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.2.b executed"
		set_variable = { VIE_p1b_loc = 1 }
		VIE_p1b_funding_check = yes
		ai_chance = { base = 30 }
	}

	# C - Noi dia: x1,3, giao cham hon 40%, 100% kinh nghiem
	option = {
		name = vie_p1b.2.c
		trigger = { check_variable = { VIE_p1b_ok_domestic = 1 } }
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.2.c executed"
		set_variable = { VIE_p1b_loc = 2 }
		VIE_p1b_funding_check = yes
		ai_chance = { base = 10 }
	}
}

# .3  Thieu von (Funding Gate truot)
country_event = {
	id = vie_p1b.3
	title = vie_p1b.3.t
	desc = vie_p1b.3.d
	picture = GFX_report_event_generic_read_write
	is_triggered_only = yes

	# A - Cat quy mo con muc toi thieu va kiem tra lai
	option = {
		name = vie_p1b.3.a
		trigger = { check_variable = { VIE_p1b_qty > VIE_p1b_q1 } }
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.3.a executed"
		set_variable = { VIE_p1b_qty = VIE_p1b_q1 }
		VIE_p1b_funding_check = yes
		ai_chance = { base = 50 }
	}

	# B - Vay no (x1,1)
	option = {
		name = vie_p1b.3.b
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.3.b executed"
		set_country_flag = VIE_p1b_use_debt
		VIE_p1b_contract = yes
		ai_chance = {
			base = 5
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
			modifier = { factor = 0 ai_has_high_deficit = yes }
		}
	}

	# C - Hoan: khong mat gi, bam lai Decision sau
	option = {
		name = vie_p1b.3.c
		ai_chance = { base = 30 }
	}

	# D - Huy chuong trinh
	option = {
		name = vie_p1b.3.d_cancel
		log = "[GetDateText]: [This.GetName]: Event vie_p1b.3.d_cancel executed"
		VIE_p1b_cancel = yes
		ai_chance = { base = 5 }
	}
}

'''
    for k in ENABLED:
        n = prog(k)['n']
        o += '# .%d  Giao hang an: %s\ncountry_event = {\n\tid = vie_p1b.%d\n\thidden = yes\n\tis_triggered_only = yes\n\n\timmediate = {\n\t\tlog = "[GetDateText]: [This.GetName]: Event vie_p1b.%d (VIE_p1b_deliver_%s)"\n\t\tVIE_p1b_deliver_%s = yes\n\t}\n}\n\n' % (10 + n, prog(k)['name'], 10 + n, 10 + n, k, k)
    return o


# ------------------------------------------------------------------ decisions
def gen_decisions() -> str:
    o = HEADER + 'VIE_naval_program_category = {\n'
    for k in ENABLED:
        p = prog(k)
        o += '\tVIE_p1b_%s = {\n\t\ticon = GFX_decision_generic_form_nation\n\t\tcost = 50\n\n' % k
        o += '\t\tvisible = {\n\t\t\thas_completed_focus = %s\n\t\t\tNOT = { has_country_flag = VIE_p1b_%s_contracted }\n\t\t\tNOT = { has_country_flag = VIE_p1b_%s_cancelled }\n\t\t}\n' % (p['focus'], k, k)
        o += '\t\tavailable = {\n'
        if p.get('date'):
            o += '\t\t\tdate > %s\n' % p['date']
        for tt, block in p.get('extra', []):
            o += '\t\t\tcustom_trigger_tooltip = {\n\t\t\t\ttooltip = %s\n' % tt
            o += ''.join('\t\t\t\t%s\n' % ln for ln in block.split('\n'))
            o += '\t\t\t}\n'
        o += '\t\t\tcustom_trigger_tooltip = {\n\t\t\t\ttooltip = VIE_p1b_slot_tt\n\t\t\t\tVIE_p1b_slot_free = yes\n\t\t\t}\n'
        o += '\t\t\tcustom_trigger_tooltip = {\n\t\t\t\ttooltip = VIE_p1b_path_tt\n\t\t\t\tOR = {\n'
        # explicit, simple layout
        for t in p['partners']:
            o += '\t\t\t\t\tAND = {\n\t\t\t\t\t\tcountry_exists = %s\n\t\t\t\t\t\tNOT = { has_war_with = %s }\n\t\t\t\t\t}\n' % (t, t)
        if p['hyb']:
            o += '\t\t\t\t\tAND = {\n' + conds(p['hyb'], '\t\t\t\t\t\t') + '\t\t\t\t\t}\n'
        o += '\t\t\t\t}\n\t\t\t}\n\t\t}\n\n'
        o += '\t\tcomplete_effect = {\n\t\t\tlog = "[GetDateText]: [Root.GetName]: Decision VIE_p1b_%s"\n\t\t\tVIE_p1b_load_%s = yes\n\t\t\tcountry_event = { id = vie_p1b.1 }\n\t\t}\n\n' % (k, k)
        o += '\t\tai_will_do = {\n\t\t\tbase = 20\n\t\t\tmodifier = { factor = 0 NOT = { VIE_ai_free = yes } }\n\t\t\tmodifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }\n\t\t\tmodifier = { factor = 0 ai_has_high_deficit = yes }\n\t\t}\n\t}\n\n'
    o = o.rstrip('\n') + '\n}\n'
    return o


# ------------------------------------------------------------------ ideas
def gen_ideas() -> str:
    o = HEADER + 'ideas = {\n\tcountry = {\n\n'
    for k in ENABLED:
        o += '''		VIE_p1b_prog_%s = {
			picture = army_planning
			allowed = { always = no }
			allowed_civil_war = { always = no }
			cancel_if_invalid = no

			modifier = {
				experience_gain_navy_factor = 0.01
			}
		}

''' % k
    o = o.rstrip('\n') + '\n\t}\n}\n'
    return o


# ------------------------------------------------------------------ scripted loc + loc
def gen_sloc() -> str:
    o = HEADER + 'defined_text = {\n\tname = VIE_p1b_name\n'
    for k in ENABLED:
        o += '\ttext = {\n\t\ttrigger = { check_variable = { VIE_p1b_cur = %d } }\n\t\tlocalization_key = VIE_p1b_name_%s\n\t}\n' % (prog(k)['n'], k)
    o += '}\n'
    return o


def gen_loc() -> str:
    L = ['l_english:', ' # GENERATED by tools/gen_p1b.py - khong sua tay.']
    L += [
        ' VIE_naval_program_category:0 "Chương trình Mua sắm Hải quân"',
        ' VIE_naval_program_category_desc:0 "Các chương trình đặt đóng tàu chiến theo hướng phát triển lực lượng. Mỗi chương trình chọn số lượng và mức nội địa hóa; tiền được trừ khi ký hợp đồng.\\n\\n§YChương trình đang chạy:§! [?VIE_var_procurement_1b_active|0] / 2"',
        ' VIE_p1b_slot_tt:0 "Đang chạy ít hơn §Y2§! chương trình mua sắm"',
        ' VIE_p1b_d2_done_tt:0 "Đã hoàn tất huấn luyện lực lượng tàu ngầm"',
        ' VIE_p1b_p4_branch_tt:0 "Đã hoàn tất §YLực lượng Tàu ngầm Ngăn chặn§! hoặc §YKhinh hạm Viễn hành§!"',
        ' VIE_p1b_nuclear_tt:0 "Có nền tảng công nghệ hạt nhân (§YNghiên cứu Hạt nhân§!)"',
        ' VIE_p1b_path_tt:0 "Có ít nhất một đường mua sắm: đối tác nhập khẩu hoặc năng lực công nghiệp trong nước"',
        ' vie_p1b.1.t:0 "[GetVIE_p1b_name]: số lượng"',
        ' vie_p1b.1.d:0 "Cần quyết định số tàu đặt đóng. Giá nhập khẩu khoảng §Y[?VIE_p1b_unit|2]§! tỷ USD mỗi tàu; đường hybrid đắt hơn 15%, đường nội địa đắt hơn 30%."',
        ' vie_p1b.1.a:0 "[?VIE_p1b_q1|0] tàu"',
        ' vie_p1b.1.b:0 "[?VIE_p1b_q2|0] tàu"',
        ' vie_p1b.1.c:0 "[?VIE_p1b_q3|0] tàu"',
        ' vie_p1b.2.t:0 "[GetVIE_p1b_name]: mức nội địa hóa"',
        ' vie_p1b.2.d:0 "Đặt §Y[?VIE_p1b_qty|0]§! tàu. Nhập khẩu là đường rẻ và nhanh nhất nhưng không giúp công nghiệp trong nước. Hybrid và nội địa đắt hơn, giao chậm hơn nhưng cộng kinh nghiệm cho ngành đóng tàu."',
        ' vie_p1b.2.a:0 "Nhập khẩu: giá ×1,0, giao đúng hạn"',
        ' vie_p1b.2.b:0 "Hybrid: giá ×1,15, giao chậm hơn 20%, một nửa kinh nghiệm"',
        ' vie_p1b.2.c:0 "Nội địa: giá ×1,3, giao chậm hơn 40%, toàn bộ kinh nghiệm"',
        ' vie_p1b.3.t:0 "[GetVIE_p1b_name]: thiếu vốn"',
        ' vie_p1b.3.d:0 "Ngân khố không đủ để ký hợp đồng ở quy mô và mức nội địa hóa đã chọn. Có thể cắt quy mô, vay nợ với lãi cao hơn 10%, hoãn để quay lại sau, hoặc hủy chương trình."',
        ' vie_p1b.3.a:0 "Cắt quy mô về mức tối thiểu"',
        ' vie_p1b.3.b:0 "Vay nợ để ký hợp đồng (nợ ×1,1)"',
        ' vie_p1b.3.c:0 "Hoãn lại"',
        ' vie_p1b.3.d_cancel:0 "Hủy chương trình"',
    ]
    for k in ENABLED:
        p = prog(k)
        L.append(' VIE_p1b_%s:0 "%s"' % (k, p['name']))
        L.append(' VIE_p1b_%s_desc:0 "%s\\n\\n§gGiá nhập khẩu khoảng %s tỷ USD mỗi tàu.§!"' % (k, p['desc'], ('%g' % p['unit']).replace('.', ',')))
        L.append(' VIE_p1b_name_%s:0 "%s"' % (k, p['name']))
        L.append(' VIE_p1b_prog_%s:0 "Chương trình %s đang thực hiện"' % (k, p['name'].lower()))
        L.append(' VIE_p1b_prog_%s_desc:0 "Hợp đồng đã ký. Tàu được giao lần lượt theo tiến độ."' % k)
    return '\n'.join(L) + '\n'


OUT = [
    ('common/scripted_effects/VIE_md_effects_p1b.txt', gen_effects, 'utf-8'),
    ('events/VIE_p1b.txt', gen_events, 'utf-8'),
    ('common/decisions/VIE_md_p1b_decisions.txt', gen_decisions, 'utf-8'),
    ('common/ideas/VIE_md_ideas_p1b.txt', gen_ideas, 'utf-8'),
    ('common/scripted_localisation/VIE_md_p1b_loc.txt', gen_sloc, 'utf-8'),
    ('localisation/english/VIE_md_events_p1b_l_english.yml', gen_loc, 'utf-8-sig'),
]

if __name__ == '__main__':
    for path, fn, enc in OUT:
        open(path, 'w', encoding=enc, newline='').write(fn())
        print('wrote', path)
