# -*- coding: utf-8 -*-
import os

path = r'd:\SteamLibrary\steamapps\workshop\content\529340\3800047448'

mod_loc_path = os.path.join(path, 'localization', 'english', 'dvf_modifiers_l_english.yml')
dec_loc_path = os.path.join(path, 'localization', 'english', 'dvf_decisions_l_english.yml')

mod_content = """\ufeffl_english:
 # --- DVF Modifiers & Timers ---
 dvf_dai_balance_fix: "Điều chỉnh Cân bằng Đại Việt"
 dvf_tu_duc_exiled: "Tự Đức bị Phế truất"
 dvf_tu_duc_consolidated_power: "Tự Đức Củng cố Quyền lực"
 dvf_rejected_reforms_penalty: "Bế quan Tỏa cảng (Từ chối Canh tân)"
 dvf_catholic_persecution: "Bách hại Đạo Công giáo"
 dvf_post_coup_legitimacy_high: "Chính thống Tân triều (Cao)"
 dvf_post_coup_legitimacy_mid: "Chính thống Tân triều (Trung bình)"
 dvf_post_coup_legitimacy_low: "Khủng hoảng Chính thống Hậu Đảo chính"
 dvf_landowners_purged: "Thanh trừng Đại địa chủ"
 dvf_landowners_approval_penalty: "Địa chủ Bất mãn"
 dvf_landowners_partial_purge: "Hạn chế Thế lực Địa chủ"
 dvf_new_court_authority: "Uy quyền Tân Triều đình"
 dvf_reform_court_intelligentsia_approval: "Sĩ phu Ủng hộ Canh tân"
 dvf_reform_court_armed_forces_approval: "Quân đội Đồng thuận"
 dvf_coastal_fortification: "Công sự Phòng ngự Ven biển"
 dvf_cuc_co_khi_innovation: "Cục Cơ khí Canh tân"
 dvf_nguyen_tri_phuong_defense: "Phòng tuyến Nguyễn Tri Phương"
 dvf_te_cap_bat_dieu_reforms: "Biểu trần Tế cấp Bát điều"
 dvf_tay_hanh_nhat_ky: "Tây hành Nhật ký"
 dvf_du_hoc_sinh_buff: "Du học sinh Tây học"
 dvf_ty_binh_chuan_buff: "Ty Bình chuẩn Điều tiết Lương giá"
 dvf_dong_trieu_coal_buff: "Khai trường Mỏ than Đông Triều"
 dvf_first_steam_ship_buff: "Thử nghiệm Thuyền máy Hơi nước"
 dvf_hong_bao_milestone_bronze: "Cột mốc Canh tân Đồng"
 dvf_hong_bao_milestone_silver: "Cột mốc Canh tân Bạc"
 dvf_tourane_timer: "Thời hạn Đối phó Đà Nẵng"
 dvf_french_pressure_timer: "Thời hạn Áp lực Ngoại giao Pháp"
 dvf_reform_pressure_timer: "Thời hạn Yêu sách Cải cách"
"""

with open(mod_loc_path, 'w', encoding='utf-8') as f:
    f.write(mod_content)

# Append to dvf_decisions_l_english.yml
with open(dec_loc_path, 'r', encoding='utf-8-sig') as f:
    dec_text = f.read()

if 'dvf_coastal_defense_line:' not in dec_text:
    addition = """
 dvf_coastal_defense_line: "Tuyến Phòng thủ Duyên hải"
 dvf_coastal_defense_line_desc: "Xây dựng và kiên cố hóa chuỗi pháo đài, đồn lũy ven biển và các cửa sông trọng yếu (Đà Nẵng, Ba Lạt, Cần Giờ) nhằm bảo vệ bờ cõi trước các hạm đội tàu chiến phương Tây."
"""
    with open(dec_loc_path, 'a', encoding='utf-8-sig') as f:
        f.write(addition)

print("Successfully applied DVF localization fixes.")
