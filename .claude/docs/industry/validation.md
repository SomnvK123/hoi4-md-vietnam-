> Lịch sử v17. Hiện hành: [công nghiệp v31](v31/validation.md), [mapping bỏ focus](v31/retired_mapping.md) và [thiết kế](../../../VIE_industry_branch_redesign.md).

# Kiểm định công nghiệp v17 — 08/10/2026

Thực hiện trên nhánh `codex/industry-redesign`, bằng Python runtime có sẵn.
Kết quả dưới đây là kiểm file và logic tĩnh; chưa xác nhận runtime HOI4.

## Kiểm file và logic tĩnh

| Kiểm tra | Kết quả |
|---|---|
| `tools/audit/industry.py` | ALL PASS; 39 focus, con thấp hơn mọi cha, gap ≥2, mutex hai chiều |
| `tools/audit/audit.py` | 416 focus toàn cây; 0 cạnh treo, 0 trùng ô, 0 forward anchor, 0 vòng lặp |
| `tools/audit/live.py` | MISSING=0 ở tất cả nhóm; không effect/idea/event caller thiếu định nghĩa |
| `tools/audit/ev.py` | 0 ID trùng, 0 event không được tham chiếu; 14 cảnh báo loc của event ẩn |
| `tools/audit/prov.py` | Tổng hợp lỗi 0 |
| `tools/audit_loc_errors.py` | 0 lỗi cú pháp/BOM; không focus thiếu title/desc hoặc tooltip thiếu key |
| `tools/verify_all_loc.py` | 68 file, 3595 key duy nhất; không thiếu title/desc |
| `tools/audit_dds_and_gfx.py` | 0 lỗi DDS/texture/sprite focus; 234 cảnh báo ảnh event ngoài checkout |
| Diagram.net | XML không nén, hai trang 35/39 rectangle; mọi edge có đầu/cuối là focus; đúng 2 LINK đơn |
| Localisation động | Tên focus tham chiếu tồn tại; sáu getter có định nghĩa, khớp điều kiện sáu nhóm |
| Diff ngoài nhánh | Tất cả block focus và tọa độ ngoài nhánh công nghiệp giữ nguyên |
| Reward cũ | Giữ nguyên 33/35 reward; China+1 bỏ caller cũ, fab thêm khoản hỗ trợ có điều kiện |

Các tình huống đã kiểm bằng evaluator tĩnh giới hạn trong `industry.py`:

- 64 tổ hợp của sáu nhóm: đúng ba nhóm trở lên mở capstone; nhóm mới hoàn thành
  một nửa không được tính. 44,9 điểm không đủ, 45 điểm đủ. Getter trạng thái khớp.
- Đường đóng tàu–dệt may–thép, thêm phụ trợ và cơ khí, đạt 48 điểm và đích cuối tại
  năm 2025; không hoàn thành focus chip hay xe điện.
- Cả hai lựa chọn FDI được Apple chấp nhận. Chọn trong event trước focus được
  bypass đúng phía; event tới sau focus không cộng thưởng hoặc đổi phương án.
- Cả hai ưu tiên bán dẫn mở thiết kế/OSAT/nhân lực. Thiếu nhân lực chặn fab; đủ ba
  focus thì cả hai đường được chấp nhận. Tổng hỗ trợ là -3 tỷ và một helper công
  trình tại fab; tiền công trình do MD xử lý riêng.
- Cờ scheduler Vinashin không mở SBIC. Cờ được đặt ở hai option, fallback và catch-up
  bookmark muộn. Không coi việc xếp lịch là kết quả xử lý khủng hoảng.

Evaluator từ chối trigger/effect chưa hỗ trợ; đây không phải giả lập engine,
không chứng minh thời lượng, tài chính MD, tooltip hoặc hành vi AI trong runtime.

## Cảnh báo đã đọc

- 14 event được `ev.py` báo thiếu loc đều có `hidden = yes` khi parse toàn block:
  `vie_air_force.51`, `vie_lf.2/.4`, `vie_nav_force.51/.71`,
  `vie_naval.45/.52/.54/.56`, `vie_p1b.12/.14/.17/.18/.21`.
  Script cũ chỉ tìm cờ hidden trong một cửa sổ ngắn nên bỏ sót. Không sửa các event
  ngoài phạm vi này hoặc thêm loc hiển thị cho event ẩn.
- 234 cảnh báo GFX ảnh event generic là danh sách nền đã có trước đợt này; các
  sprite do MD/base game cung cấp không nằm trong checkout submod. Không có sprite
  focus hay texture tùy chỉnh bị thiếu theo audit.
- `vie_ind.1` chỉ giữ để xử lý hàng đợi save cũ. Audit tổng quát đếm mọi tham chiếu
  event, không phân biệt định danh trong loc/log với caller. Đã kiểm trực tiếp:
  China+1 và focus mới không gọi `vie_ind.1`.

Không dùng exit code 0 làm bằng chứng duy nhất. Raw output của tám script nằm
trong [audit_logs](audit_logs/).

## Tích hợp

- Focus, scripted effects/triggers, event, scripted localisation và AI factors
  đã được tích hợp vào đường dẫn game nạp. Bốn focus mới dùng sprite hiện có.
- Key Samsung tồn tại và không bị replace ghi đè. File provider thiếu BOM đã được
  bổ sung BOM; sau sửa, toàn bộ 68 file localisation có BOM và header hợp lệ.
- Không sửa texture artwork từ đợt ngoại giao đang có trong working tree.
- Đã xuất và xem hai PNG; chữ nằm trong rectangle. Các hình là sơ đồ thiết kế từ
  tọa độ file, không phải ảnh chụp cây trong game. Routing XML/PNG được đặt riêng;
  engine HOI4 vẫn tự vẽ đường nối từ prerequisite và tọa độ.

## Kiểm trong game — chưa thực hiện

HOI4 không chạy tại thời điểm kiểm; công cụ phiên này không điều khiển được giao
diện HOI4. Chưa xác nhận đường nối engine, biểu tượng khóa, hover hay hành vi AI.

Checklist để nghiệm thu runtime trên save mới VIE 2000:

1. Mở cây VIE, kiểm gốc công nghiệp, hai cặp mutex, hội tụ Apple, fab và capstone.
   Đặc biệt xem đường dài của phụ trợ/trung tâm chế tạo và đường năng suất→đích cuối.
2. Hover điều kiện WTO/CPTPP/EVFTA/giáo dục; xác nhận tên focus được thay từ `$key$`.
3. Hover capstone với 2/3 nhóm và 44/45 điểm; kiểm sáu trạng thái ngành.
4. Lần lượt chọn hai đường FDI ở hai save; kiểm Apple và event xuất xứ. Kiểm sự kiện
   `vie_ind.1` đang chờ không cấp lại reward nếu chính sách đã được focus lựa chọn.
5. Lần lượt chọn hai ưu tiên bán dẫn ở hai save; kiểm ba prerequisites fab, khoản
   bổ sung 2 tỷ chỉ ở đường thiết kế/đóng gói và một lần thu tiền công trình MD.
6. Kiểm Vinashin trước khi event có kết quả, sau chọn option, sau fallback và tại
   bookmark muộn. Mở SBIC đúng sau ngày 21/10/2013 và có cờ xử lý.
7. Chạy AI Historical, theo dõi lựa chọn, ngày ưu tiên và ngân sách; kiểm `error.log`.

Không dùng `focus.nochecks` hoặc `focus.ignoreprerequisites` để chứng minh gate
đúng. `focus.autocomplete` chỉ dùng tăng tốc thời gian sau khi đã kiểm điều kiện.
Save mới là chuẩn; hạn chế nhận diện lựa chọn/cờ cũ được ghi trong tài liệu thiết kế.
