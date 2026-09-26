# Nhánh quân sự VIE — thiết kế v3 (chuyên sâu hóa)

Tổng cây: **485 focus** (từ 413); quân sự: **148** (từ 76). Kiểm tra tĩnh: 0 lỗi. Chưa chạy thử trong game.

## Khối mới (72 focus)
| Khối | Focus | Nội dung | Ngã rẽ giả định |
|---|---|---|---|
| A Lục quân | 18 | hạ sĩ quan, quân khu, sư đoàn cơ giới, công binh–đặc công, học viện, pháo tự hành, phòng không gần, hiện đại hóa xe tăng, tác chiến điện tử/mạng, quang học đêm, C4ISR, Quân đội 2030 | dân quân→công trình ngầm→biên phòng **hoặc** lữ đoàn viễn chinh→hậu cần tiền phương→lực lượng can thiệp khu vực |
| B Hải quân | 18 | 5 Vùng, học viện Nha Trang, hải quân đánh bộ 147, thủy lôi/đo đạc, cảnh sát biển, tàu tên lửa Molniya, căn cứ tàu ngầm Cam Ranh, trực thăng săn ngầm, Ba Son, radar bờ, mạng đảo Trường Sa, mở rộng tàu ngầm, Hải quân 2030 | viễn dương: khu trục hạm→tiếp tế→tàu sân bay nhẹ→hạm đội Biển Đông; từ chối biển: UUV/USV |
| C Không quân | 18 | sư đoàn PK-KQ, học viện, sân bay kiên cố, SAM tầm xa, cảnh báo sớm, VAECO, vận tải, tác chiến điện tử, tuần thám biển, UAV, trực thăng, ưu thế trên không, radar nội địa, Không quân 2030 | tấn công chiến lược: SEAD→ALCM + máy bay tầm xa→năng lực chiến lược |
| D CNQP + MIO | 10 | luật CNQP 2018, Viettel High Tech, nhà máy Z, Ba Son, VAECO, hợp tác nghiên cứu, chuỗi cung ứng, xuất khẩu, đạn dược, CNQP 2030 | — |
| E Tên lửa | 8 | tên lửa bờ nội địa, tên lửa chiến thuật, phòng thủ tên lửa, tên lửa hành trình; điện hạt nhân→ngưỡng lưỡng dụng→răn đe tối thiểu→học thuyết | chuỗi hạt nhân (DLC Götterdämmerung, special project, rule ≠ historical) |

## Cơ chế mới
- **MIO** (file `VIE_md_organizations.txt`): 4 công ty, 31 trait; focus khối D cấp `add_mio_size/funds/free_trait_picks`.
- **Biến thể vũ khí**: 6 biến thể chép 1:1 từ biến thể MD đang chạy (module đúng), gắn `design_team = mio:...`; thiếu DLC thì cộng kho hoặc bỏ qua.
- **Đơn vị thật**: 4 template mới (cơ giới, đặc công, viễn chinh, hải quân đánh bộ) + 4 sư đoàn/lữ đoàn.
- **Quyết định lặp lại**: 6 quyết định (diễn tập quân khu/hải quân/không quân, mua sắm bổ sung, tuần tra ASEAN, tuyển quân mở rộng).
- **36 biến `VIE_af_*` mới** trong `VIE_armed_forces_modifier` (tổng 61).

## Rủi ro còn lại
Ngữ nghĩa `free_trait_picks`, `start_equipment_factor` trong `create_unit`, hướng `reduce_focus_completion_cost`, module biến thể theo DLC; chưa playtest.
Generator nằm ở `D:\HOI4Mods\_gen` (ngoài mod): chạy lại `blockA/B/C/DE.py` để tái tạo.
