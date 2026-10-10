# Mapping 28 focus đã bỏ — v30

ID dưới đây có prefix `VIE_`. Đây là mapping nội dung, không phải migration save.

| ID cũ | Nội dung hiện hành |
|---|---|
| `hai_van_tunnel`, `hcmc_trung_luong_expressway`, `can_tho_bridge`, `northern_expressways` | Chương trình đường bộ và đợt nền tảng |
| `north_south_expressway_phase2` | Chương trình Bắc–Nam và mở rộng mạng |
| `ring_roads_hanoi_hcmc` | Kết nối vùng, hai đợt |
| `expressway_3000km` | Đợt 3.000 km của mạng 5.000 km; thông báo `.6` |
| `hsr_2010_reject`, `hsr_2010_approve` | Event `.4`, giữ trạng thái quyết định một lần |
| `hcmc_metro`, `urban_rail_hanoi`, `urban_rail_special_mechanism_nq188`, `metro_network_2035` | Đường sắt đô thị, hai đợt, nội dung TOD/NQ188 |
| `lach_huyen_port`, `cai_mep_port` | Cảng nước sâu quốc gia, hai đợt |
| `lao_cai_haiphong_rail` | Nâng cấp đường sắt hiện hữu |
| `hsr_partner_japan`, `hsr_partner_eu`, `hsr_partner_china` | Event `.5`, cờ đối tác và đợt HSR tương ứng |
| `hsr_groundbreaking` | Đợt HSR ban đầu; thông báo `.9` |
| `domestic_rail_industry` | Chuyển giao/nội địa hóa, đợt đào tạo |
| `aviation_market_opening` | Nội dung chính sách vốn sân bay cuối 2011 |
| `noi_bai_t2`, `tan_son_nhat_t3` | Hiện đại hóa mạng sân bay, hai đợt |
| `long_thanh_approval` | Chuẩn bị Long Thành; focus và decision xây dựng riêng |
| `dual_use_airports` | Đầu tư lưỡng dụng tùy chọn |
| `van_don_airport` | Đầu tư Vân Đồn tùy chọn với xã hội hóa |
| `infrastructure_breakthrough_nq13` | Nội dung chiến lược hạ tầng quốc gia |

Flag đối tác `VIE_hsr_partner_*` còn dùng để lưu event choice; cùng tên với focus đã bỏ không có nghĩa focus cũ vẫn tồn tại. Toàn bộ block cũ nằm trong archive ở gốc repo. Không tạo 28 decision thay thế một-một.
