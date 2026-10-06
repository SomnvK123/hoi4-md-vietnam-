# Bẫy engine HOI4

Những bẫy tổng quát, không riêng nước nào. Kiểm định danh thật trước khi dùng: thấy dùng ở chỗ khác
chưa phải bằng chứng. Chú ý đúng hoa thường (tên file, đơn vị) để chạy được trên Linux.

## Trigger và scope

- `NOT = { A B }` nghĩa là "không phải cả hai", không phải "không cái nào". "Không cái nào" viết
  `NOT = { OR = { A B } }` hoặc hai block `NOT` riêng. `NOR` không tồn tại.
- `threat` thang 0.0 đến 1.0: `threat > 0.40`, không phải `> 40`.
- `is_in_faction = yes/no`. Cùng phe với nước khác: `is_in_faction_with = TAG`. `add_to_faction = TAG` nhận tag.
- `tag` là tag lúc chạy (nội chiến sinh tag mới), `original_tag` giữ danh tính. Dùng `original_tag` cho mọi
  thứ giới hạn theo nước.
- `ROOT` là scope gốc, `FROM` là bên gửi event, `PREV` là scope ngay trước. Event gọi từ `on_action` hoặc
  `random_scope_in_array` không có `FROM` rõ ràng, nó rơi về nước kích hoạt. Dùng `event_target:X = { ... }`
  thay cho `target = FROM`, hoặc bắn một event ẩn định tuyến trước.
- `target =` có chấp nhận `event_target:` hay không là theo từng effect: `add_to_war`, `add_opinion_modifier`,
  `reverse_add_opinion_modifier`, `send_equipment` có; `add_relation_modifier` chỉ nhận tag cứng (vào scope
  của bên kia: `event_target:X = { add_relation_modifier = { target = ROOT ... } }`).

## Guard bắt buộc cho effect "gỡ"

Effect gỡ thứ scope không có sẽ ghi lỗi vào `error.log` và không làm gì. Ở quy mô `random_list` hay on_action
tháng, spam log tốn hiệu năng.

- `damage_building` / `remove_building`: guard bằng đúng loại công trình, ví dụ
  `limit = { fuel_silo > 0 }` hoặc `non_damaged_building_level = { building = X level > 0 }`.
  Guard bằng idea hay cờ không chứng minh được gì.
- `remove_dynamic_modifier`: guard `has_dynamic_modifier = { modifier = X }`, đặt trong đúng scope sẽ gỡ.
- `clr_country_flag` trên cờ chưa bao giờ set là vô hại, nhưng báo hiệu chưa lần theo vòng đời cờ.

## Biến và mảng

- Biến chưa set đọc 0. Biến dùng trong dynamic modifier cũng vậy, đừng khởi tạo 0 ở startup.
- Chỉ số slot bắt đầu từ 0, chỉ số type (loại) bắt đầu từ 1. Đừng nhầm. Ghi rõ trong comment của effect có tham số mảng.
- Dynamic modifier: khoá dạng chi phí xấu đi khi biến tăng (relief phải trừ); khoá dạng bonus xấu đi khi biến
  giảm (relief phải cộng). Đừng sao chép một dấu cho cả khối trộn lẫn.
- Sau khi đổi biến backing của dynamic modifier, gọi `force_update_dynamic_modifier` nếu tooltip không cập nhật.

## Thiết bị và tiền

- Chuyển trang bị giữa hai nước: `send_equipment = { type = X amount = N target = TAG }` (giữ producer, không rút quá kho).
  Đừng trừ rồi cộng stockpile riêng. `add_equipment_to_stockpile` là cho mua sắm/giao hàng đổi loại.
- Trừ tiền: `set_temp_variable = { treasury_change = -N }` rồi `modify_treasury_effect = yes`. Scripted effect
  công trình của MD đã tự trừ.
- `add_building_construction` cấp province (bunker, naval_base...) cần `province`, và province phải thuộc state đang scope.

## Focus và event

- `relative_position_id` giải theo thứ tự file: anchor khai báo trước con, nếu không là lỗi.
- Phụ thuộc giữa anh em cùng hàng: dùng `available`, không thêm prerequisite chéo (xem `VIE_focus_coding_standards.md`).
- `is_triggered_only = yes` và `fire_only_once = yes` không ngăn on_action bắn lại: guard ở `limit` của caller.
- Loc: getter sai hoa thường (`GetNamewithFlag`) render rỗng và không báo lỗi.

## Hiệu năng

- Scheduler `on_monthly` chạy cho mọi tháng: không vòng lặp trên mọi quốc gia/state nếu tránh được; hoãn việc
  nặng bằng cờ; không `dirty` đặt bằng ngày hiện tại.
- Tránh `every_country` / `every_state` trong effect gọi mỗi tháng nếu một scope cố định đủ dùng.
