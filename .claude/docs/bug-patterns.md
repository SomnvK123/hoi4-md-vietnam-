# Bug patterns

Pattern grep được để quét toàn repo, và câu hỏi phản biện để kiểm một diff. Bẫy engine chi tiết ở
[engine-pitfalls.md](engine-pitfalls.md).

## Pattern quét được

Chạy bằng Grep trên `common/` và `events/`. Mỗi kết quả phải đọc ngữ cảnh trước khi kết luận là lỗi.

- `add_building_construction` với `type = bunker | coastal_bunker | naval_base | land_fort` mà không có
  `province =` (công trình province bị bỏ qua hoặc báo lỗi). Công trình cấp state (`infrastructure`,
  `industrial_complex`...) không cần province nhưng phải trừ tiền.
- `add_building_construction` thô cho nhà máy/hạ tầng thay vì `one_state_*` / `one_random_*` (không trừ tiền).
- `NNN = { ... }` với state không thuộc VIE (VIE: 518-524, 526, 801, 802, 813, 816). Mọi số state khác phải
  xác minh chủ sở hữu 2000 (`prov.py`).
- `swap_ideas` có `remove_idea` trùng `add_idea`, hoặc `remove_idea` không khớp `limit`.
- Event option `name =` trỏ sang id event khác, hoặc option trùng tên trong một event.
- `else_if` có `limit` giống `if` liền trước (không bao giờ chạy tới).
- `tag =` thay `original_tag =` trong `allowed` của idea/decision (vỡ khi nội chiến). `targeted_modifier = { tag = }` đúng.
- `set_cosmetic_tag = original_tag` (đúng là `drop_cosmetic_tag = yes`).
- `country_event` / scope vào TAG mà không có `country_exists` (nước đó có thể đã biến mất).
- Biến cộng dồn hằng tháng mà không reset trước.
- `for_each_scope_loop` lặp mảng chỉ số (đúng là `for_each_loop`).
- Nút scripted GUI có `trigger` mà không có `effects`.
- `has_idea` / `add_ideas` / `remove_ideas` sai hoa thường (im lặng thất bại).
- Scripted effect/trigger định nghĩa hai lần (bản sau ghi đè bản trước).
- Marker merge conflict (`<<<<<<<`, `=======`, `>>>>>>>`).
- `dirty = global.date` hoặc `global.num_days` (vẽ lại GUI mỗi tick).
- Cờ chỉ được `has_country_flag` mà không có `set_country_flag` ở đâu (gate chết). Ngược lại cờ set mà không đọc.
- Loc key dùng trong `custom_*_tooltip` mà không có định nghĩa (script `live.py` bắt).

## Câu hỏi phản biện cho mỗi khối thay đổi

**Tồn tại và scope**
- Scope vào một TAG, hoặc ban thưởng cho nước khác: có `country_exists` không? Nước đó có thể đã chết lúc effect chạy.
- Scope vào `var:target`: đã guard `check_variable = { var:target > 0 }`? Biến chưa set đọc 0.
- `FROM` trong decision/focus không nhắm mục tiêu: nó rơi về `ROOT`. Nếu code giả định `FROM` là nước khác thì tự nhắm chính mình.

**Thời điểm và chuyển trạng thái**
- `available = { always = no }` cùng `bypass`: bypass có thực sự đạt được không? Nếu không, người chơi khoá cứng vĩnh viễn.
- Gate dựa trên một focus đã bị xoá ở v9 đến v11: phải đã re-point sang cờ hoặc focus còn sống.
- `days_remove` không có `remove_effect` đi kèm: hiệu ứng hết hạn mà không hoàn lại.
- `fire_only_once` + `days_remove` trên một decision: kiểm hành vi mong muốn.
- Event fire sang nước khác với `days = N`: nếu nước đó chết hoặc đang chiến tranh với ROOT lúc hết hạn thì sao?
- Event tự fire lại chính nó: có điều kiện dừng không?

**Biến và mảng**
- Chia cho biến: đã clamp hoặc guard `> 0`?
- Chỉ số mảng động `array^i`: `i` có bị chặn không?
- Biến đọc trước khi ghi ở một nhánh thực thi nào đó?
- `add_stability` / `add_war_support` ngoài `-1.0 .. 1.0` bị cắt im lặng.
- Hai biến `VIE_af_*` cộng cùng một lượng cho hai mục đích khác nhau (đã chạm trần modifier chưa; xem
  `tools/audit/*_balance.py`)?

**Hai chiều với người chơi**
- Hiệu ứng vĩnh viễn lên nước khác không qua event (không cho người chơi quyết định)?
- `will_lead_to_war_with = TAG` mà không có wargoal thật trong reward (tooltip nói dối), và ngược lại focus dẫn tới
  chiến tranh mà thiếu `will_lead_to_war_with`.

**Nội dung**
- Core hay công trình được cấp miễn phí? Công trình phải trừ tiền (xem conventions).
- Số liệu trong loc có khớp effect không?
- Một tooltip hiện ra có đủ thông tin (reward không bọc hết trong `if`/`limit`, gate cờ bọc `custom_trigger_tooltip`)?
