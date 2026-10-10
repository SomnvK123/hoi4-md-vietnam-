# -*- coding: utf-8 -*-
loc_file = 'localisation/english/replace/VIE_md_vi_military_l_english.yml'
with open(loc_file, 'r', encoding='utf-8') as f:
    text = f.read()

missing_idea_loc = """
  # Naval Readiness & Base Spirits
  VPA_Naval_Readiness_1:0 "Sẵn sàng Chiến đấu Hải quân Cấp 1"
  VPA_Naval_Readiness_1_desc:0 "Các hải đội ven bờ bước đầu củng cố kỷ luật thao diễn và nâng cao mức độ sẵn sàng trực ban bảo vệ chủ quyền."
  VPA_Naval_Readiness_2:0 "Sẵn sàng Chiến đấu Hải quân Cấp 2"
  VPA_Naval_Readiness_2_desc:0 "Nâng cấp năng lực hiệp đồng tác chiến biên đội, mở rộng tuần tra tác chiến thường trực trên các vùng biển trọng điểm."
  VPA_Naval_Readiness_3:0 "Sẵn sàng Chiến đấu Toàn diện Hải quân Cấp 3"
  VPA_Naval_Readiness_3_desc:0 "Quân chủng Hải quân làm chủ khí tài hiện đại, hiệp đồng tác chiến ngầm - mặt nước - không hải đạt chuẩn tối ưu."

  VIE_naval_shipbuilding_spirit:0 "Năng lực Đóng tàu Quân sự Ba Son"
  VIE_naval_shipbuilding_spirit_desc:0 "Đẩy mạnh công nghiệp đóng mới và sửa chữa tàu chiến vỏ thép tại Tổng công ty Ba Son và nhà máy X51."
  VIE_naval_shipbuilding_spirit_2:0 "Tổ hợp Đóng tàu Chiến lược Ba Son"
  VIE_naval_shipbuilding_spirit_2_desc:0 "Làm chủ hoàn toàn dây chuyền đóng tàu tên lửa cao tốc và tích hợp vũ khí khí tài phức tạp trong nước."

  VIE_fleet_sustainment_spirit:0 "Bảo đảm Hậu cần Quân cảng Cam Ranh"
  VIE_fleet_sustainment_spirit_desc:0 "Thiết lập căn cứ bảo đảm kỹ thuật, nhiên liệu và hậu cần nước sâu cho các biên đội tàu chiến Vùng 4."
  VIE_fleet_sustainment_spirit_2:0 "Hệ thống Tiếp vận Hạm đội Biển xa"
  VIE_fleet_sustainment_spirit_2_desc:0 "Đội ngũ tàu tìm kiếm cứu nạn tàu ngầm và vận tải đa năng bảo đảm hải trình tác chiến xa bờ dài ngày."

  VIE_maritime_domain_awareness_spirit_2:0 "Hệ thống Nhận thức Không gian Biển Tích hợp"
  VIE_maritime_domain_awareness_spirit_2_desc:0 "Mạng lưới kết nối radar bờ, vệ tinh trinh sát và cảm biến hạm đội cung cấp bức tranh tác chiến thời gian thực."
"""

with open(loc_file, 'w', encoding='utf-8') as f:
    f.write(text.rstrip() + "\n" + missing_idea_loc.strip() + "\n")

print("Added missing idea loc keys successfully.")
