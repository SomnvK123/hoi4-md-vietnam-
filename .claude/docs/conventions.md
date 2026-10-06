# Quy ước viết nội dung

Chuẩn chi tiết cho cây focus (thứ tự trường, thang cost, bố cục hàng ngang, trigger đảng cầm quyền,
tooltip) nằm ở `VIE_focus_coding_standards.md` ở gốc repo. File đó là nguồn chính, tài liệu này chỉ
tóm tắt và bổ sung phần ngoài focus. Lưu ý: header của file đó còn nhắc `.claude/docs/focus-tree-reference.md`
và `tools/validation/...` của MD upstream, những file này không còn ở repo này.

## Focus

- Id `VIE_<slug>`, snake_case. Neo `relative_position_id` vào một prerequisite của chính nó, anchor khai
  báo **trước** con trong file.
- Thứ tự trường: `id, icon, x/y, relative_position_id, cost, allow_branch, prerequisite/mutually_exclusive,
  will_lead_to_war_with, search_filters, available/bypass/cancel, completion_reward/select_effect, ai_will_do`.
  `ai_will_do` luôn cuối.
- `cost`: bỏ nếu 10 (mặc định). Dùng 5 cho focus chuẩn bị, 7 cho focus hành động. 16 chỉ cho
  `VIE_spratly_fortification`. Cost là thời gian, không phải tiền.
- Mỗi focus có `log = "[GetDateText]: [Root.GetName]: Focus VIE_<slug>"` làm dòng đầu của reward, và reward
  có ít nhất một effect thật. Block chỉ có log thì bỏ.
- `search_filters` bắt buộc, 1 dòng, 1 đến 2 filter chung (xem danh sách trong `VIE_focus_coding_standards.md`
  mục 4). Dùng `FOCUS_FILTER_MILITARY_LAWS` và `FOCUS_FILTER_AIRCRAFT`, không dùng alias cũ
  `FOCUS_FILTER_MILITARY` / `FOCUS_FILTER_AIR`.
- Tối đa 5 hiệu ứng vĩnh viễn mỗi focus; bonus thêm dùng timed idea.
- Không có block rỗng (`available = { }`, `mutually_exclusive = { }`), không bypass gắn với `available = { always = no }`.
- Điều kiện đảng cầm quyền dùng trigger gốc của MD (`<slug>_are_in_power`, `<slug>_are_in_coalition`) hoặc
  trigger bọc của mod (`VIE_hl_in_power`, `VIE_party_rule_active`). Không dùng `check_variable = { ruling_party = N }`.
- Focus bắn event sang nước khác hoặc tạo wargoal: có `country_exists = TAG` và tooltip kết quả
  (`TT_IF_THEY_ACCEPT` kiểu MD), và `will_lead_to_war_with = TAG` nếu dẫn tới chiến tranh.

## Tiền và công trình

- Focus/decision tốn tiền thật (từ ~5 tỷ trở lên) thêm `FOCUS_FILTER_EXPENDITURE` và guard trong `ai_will_do`:
  `modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }`. Focus xây nhà máy thêm
  `can_staff_an_industrial_complex` (mẫu có sẵn trong cây focus).
- Công trình qua scripted effect của MD (đã tự trừ tiền, đừng trừ lần hai): `one_state_industrial_complex`,
  `one_state_arms_factory`, `one_state_dockyard`, `one_state_infrastructure`, `one_state_anti_air`,
  `one_state_air_base`, `one_state_radar_station`, `one_random_*`.
- Công trình MD không có sẵn effect (bunker, coastal_bunker, naval_base): `add_building_construction` thô
  **phải có `province = N`**, và trừ tiền thủ công bằng
  `set_temp_variable = { treasury_change = -N }` + `modify_treasury_effect = yes`.
  Province phải thuộc đúng state đang scope (kiểm bằng `tools/audit/prov.py`).
- Số liệu giá tham chiếu (đã dùng ở v7): IC/AF/dockyard -7.5 tỷ, infra -3.5, AA -3.25, air base -3.0,
  radar -1.75, bunker ~1 tỷ/cấp, naval_base ~3.25 tỷ/cấp.

## Scripted effect

- Tên `VIE_<hệ thống>_<việc>`, đặt trong file `VIE_md_effects_<chủ đề>.txt` của hệ thống đó. Reward của
  focus là một effect riêng `VIE_<prefix>_<id>_reward`, focus chỉ gọi nó (`VIE_lf_cb_reward = yes`).
- Mọi effect gọi phải có định nghĩa. Một định nghĩa trùng tên ở hai file thì cái sau ghi đè im lặng.
- Biến modifier lực lượng (`VIE_af_*`) cộng bằng `add_to_variable = { VIE_af_x = v tooltip = VIE_tt_x }` rồi
  gọi `VIE_<xx>_refresh = yes` để cập nhật dynamic modifier. Không tự nhân đôi cùng lúc cộng biến và
  cộng modifier thật.
- Biến chưa set đọc là 0, đừng khởi tạo 0 ở startup. Chỉ reset khi chu kỳ yêu cầu.
- Cờ và biến phải có vòng đời rõ: ai set, ai clear, ai đọc. Cờ chỉ được đọc mà không ai set là gate chết.

## Decision

- Trong `common/decisions/<file>`, category ở `categories/VIE_md_categories.txt` phải có `visible`/gate
  đạt được.
- `cost` là PP (không phải tiền). `days_remove` phải đi cùng `remove_effect` nếu trạng thái cần được hoàn
  lại. Tránh `fire_only_once = yes` cùng `days_remove` nếu không cần: engine xử lý không nhất quán,
  kiểm từng decision (xem known-issues).
- Decision có `complete_effect` bắn event sang nước khác: `visible`/`available` có `country_exists` cho
  nước đó, và log dòng đầu.

## Event

- `is_triggered_only = yes`, có caller. Không viết event MTTH mở.
- Id khớp namespace của file; mỗi file có `add_namespace`. Option log đúng id của chính nó
  (`log = "[GetDateText]: [This.GetName]: Event vie_xxx.N.a executed"`).
- Event hiển thị cần `.t`, `.d`, và `.a`/`.b`... cho option. Event `hidden = yes` không cần loc.
- Event gửi sang nước khác dùng guard `country_exists`, và tính tới việc nước đó đã chết khi `days = N` hết hạn.
- Tự fire lại chính nó (`vie_naval.45` kiểu giao hàng lặp) phải có điều kiện dừng rõ ràng.
- Ảnh event: kiểm sprite tồn tại trong `interface/VIE_md_event_pictures.gfx` hoặc là sprite MD/vanilla có thật.

## Idea

- `original_tag = VIE` trong `allowed`, không dùng `tag =` (vỡ khi nội chiến). `targeted_modifier = { tag = X }`
  là cú pháp riêng, dùng `tag` là đúng.
- Tên idea `name = X` dùng cặp loc `X` và `X_desc`. Đừng để focus/decision khác dùng cùng key `X`.
- Idea định nghĩa mà không ai cấp là rác: thêm nguồn cấp hoặc xoá cả idea và loc.

## Khi xoá nội dung

Theo mẫu v9 → v11: ghi vào file `vN_removed_*.txt` ở gốc repo (không được game nạp), re-point mọi gate
`has_completed_focus` trỏ focus đã xoá sang cờ hoặc focus còn sống, xoá loc chết đi cùng, ghi dòng `## vN`.
Sau đó chạy `audit.py` và `live.py`.
