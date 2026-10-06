# Vấn đề đã biết

Danh sách tình trạng ngày **06/10/2026**, rút ra từ audit tĩnh (script `tools/audit/*` và grep). Chưa chạy trong
game. Mỗi mục ghi mức độ chắc chắn. Xoá mục khi đã sửa, và thêm mục khi phát hiện lỗi mới chưa sửa ngay.
Đừng "sửa" các mục ở phần "Không phải lỗi".

## Lỗi code (cần sửa)

Không còn lỗi code mở trong danh sách này. Đã sửa ngày 06/10/2026 (trong working tree; `prov.py` 0 lỗi, `live.py` 0 MISSING, mọi balance test PASS):
- `VIE_md_triggers_p17.txt`: sửa dead gate `VIE_lf_mobilize_gate` sang `has_completed_focus = VIE_lf_dev_territorial`.
- `VIE_md_effects_p17.txt`: 9 dòng bunker có `province =`; `VIE_lf_cb_reward` hạ tầng chuyển sang `one_state_infrastructure = yes`; `VIE_lf_ps_reward` / `VIE_lf_pt_reward` set cờ định hướng `VIE_lf_dev_strategic` / `VIE_lf_dev_territorial`.
- `VIE_md_effects_p10.txt`: `vie_news.4` kích hoạt theo `has_completed_focus = VIE_four_nos_doctrine`; `vie_alt.40` kích hoạt theo `has_idea = VIE_four_nos` (thay cờ cũ `VIE_tc_active`).
- `VIE_md_focus.txt`: hoàn thành `VIE_sez_pass_99` set cờ `VIE_sez_active`; `VIE_net_zero_2050` set cờ `VIE_air_cleaned`; `VIE_lf_arm_engineers` thêm `FOCUS_FILTER_EXPENDITURE`; unwrap 7 `if/limit` lục quân (F10) để sửa tooltip; bổ sung `FOCUS_FILTER_EXPENDITURE` cho 56 focus chi tiêu/xây dựng (F5).
- `common/ideas/`: Lưu 36 idea mồ côi vào `v16g_removed_unused_ideas.txt`, dọn khỏi `VIE_md_ideas_p2.txt` và xoá 5 file ý tưởng mồ côi (`mining`, `p3A`, `p3B`, `p3C`, `p3Q`); `live.py` IDEAS defined but never granted: 0.
- `localisation/`: Chuẩn hoá mã màu không chuẩn (`§g`, `§C`, `§O` -> `§Y`, `§R`, plain text) trên 8 file loc.
- `tools/audit/air_proc_balance.py`: sửa parser scheduler để khớp cú pháp inline scheduler thực tế, đạt `ALL PASS`.

Còn theo dõi, chưa phải lỗi: 25 decision (14 `VIE_rn_*` trong `VIE_md_decisions.txt`, 11 `VIE_dec_*` trong
`VIE_md_def_industry.txt`) có `fire_only_once = yes` cùng `days_remove`. Cả 25 đều có `remove_effect` nên là mẫu "việc có hạn,
hết hạn thì trả kết quả", coi là chủ ý. Chưa kiểm hành vi trong game; nếu thấy decision biến mất hoặc không hoàn lại đúng,
kiểm tra mẫu này trước.

## Cây focus (audit 06/10/2026, 412 focus)

Sạch: thứ tự trường, không `cost = 10` tường minh, mọi focus có log, `ai_will_do`, `search_filters` hợp lệ, mutex đối xứng,
không prerequisite mâu thuẫn mutex, không toạ độ trùng, không forward-ref, shortcut đều có loc và target tồn tại,
`modify_treasury_effect` luôn có `treasury_change` trước.

| # | Vấn đề | Mức |
|---|---|---|
| ~~F1~~ | ~~`VIE_hl_key_sectors` guard bankruptcy & can_staff_an_industrial_complex~~ (đã sửa) | Đã xong |
| ~~F2~~ | ~~Focus tốn tiền thiếu guard bankruptcy_incoming_collapse trong ai_will_do~~ (đã đủ 107/107) | Đã xong |
| F3 | Theo luật MD (cost >= 8, hoặc cost >= 5 kèm filter kinh tế/quân sự/nghiên cứu) có 341 focus cần guard, 212 chưa có (35 focus cost 10 mặc định, 177 focus cost 5 đến 7) | Chuẩn MD |
| F4 | 45 focus (`VIE_nf_*`, `VIE_airf_*`, `VIE_apm_law`, `VIE_sf_command`, `VIE_naval_defence_law`) đặt `NOT = { has_active_mission = bankruptcy_incoming_collapse }` trong `available`. MD chỉ cho đặt trong `ai_will_do` vì `available` chặn cả người chơi | Lệch chuẩn, có thể cố ý |
| ~~F5~~ | ~~`FOCUS_FILTER_EXPENDITURE` mới có 2 focus~~ (đã bổ sung đủ 107 focus tốn tiền) | Đã xong |
| F6 | 232/412 focus có `ai_will_do` phẳng (không modifier), 0 guard theo đường chính trị, 0 `ai_strategy_plans`; `VIE_ai_historical` luôn đúng | Thiết kế |
| F7 | 39 cờ do focus đặt mà không đọc ở đâu (`VIE_net_zero_champion`, `VIE_dk1_built`, `VIE_wto_talks`, `VIE_nuclear_built`...). Cờ chết hoặc trùng với trạng thái truy vấn được | Dọn |
| ~~F8~~ | ~~14 shortcut `scroll_wheel_factor = 0.60`~~ (đã chuyển sang chuẩn `0.80`) | Đã xong |
| F9 | 6 tên icon không tìm thấy trong `.gfx` của MD hay của mod: `focus_generic_military_mission` (6 focus), `focus_generic_diplomatic_treaty` (2), `focus_generic_destroyer` (2), `focus_generic_industry_2`, `focus_generic_industry_3`, `goal_generic_radar`. Có thể là sprite vanilla, chưa đối chiếu được (không có vanilla trên máy) | Cần xác minh |
| ~~F10~~ | ~~13 focus `VIE_lf_arm_*` / `VIE_lf_cap_*` bọc cả reward trong `if = { limit = { VIE_lf_arm_slot_free = yes } }`~~ (đã unwrap 7 focus) | Đã xong |
| F11 | Độ sâu prerequisite tối đa 16 (`VIE_lf_force_complete`), chuỗi lục quân dài. Nhánh khác ổn (chuỗi đơn dài nhất 5) | Thiết kế |

## Nợ nội dung

- ~~**36 idea định nghĩa mà `live.py` không thấy ai cấp**~~: đã lưu trữ vào `v16g_removed_unused_ideas.txt` và dọn sạch khỏi `common/ideas/` ngày 06/10/2026. `live.py` báo 0 idea mồ côi.
- ~~Balance of Power oligarch~~: đã xoá 06/10/2026 (`VIE_md_bop_p3.txt`, `VIE_md_effects_p3b.txt` và 17 dòng loc `VIE_oli_*`/`VIE_oligarch_balance`). `grep` không còn tham chiếu nào.
- **Loc chết**: theo `VIE_repo_health_report.md` (30/09) hơn 40% key loc không còn được tham chiếu sau khi xoá focus v9 đến v11.
  Chưa đếm lại.
- ~~**545 key loc trùng** giữa `localisation/english/` và `replace/`~~: đã xoá sạch 545 key bị ghi đè ở thư mục cha ngày 06/10/2026; bản trong `replace/` giữ nguyên vẹn 100%.
- ~~Loc còn mã màu không chuẩn~~: đã chuẩn hoá mã màu văn bản `§g`, `§C`, `§O` sang `§Y`, `§R`, plain text trên 8 file loc. Còn lại các thanh GUI `VIE_axbar_*` trong `replace/`.
- ~~Ký tự em/en-dash~~: đã chuẩn hoá toàn bộ 123 ký tự `—` và `–` sang dấu gạch ngang chuẩn `-` trên 21 file loc.
- Layout cây focus: kiểm bằng `tools/focus_layout/` và `tools/audit/audit.py` sau mỗi đợt xoá/thêm lớn.
- `common/bookmarks/blitzkrieg.txt` là bản sao file MD, cần so lại khi MD đổi phiên bản.
- ~~Hướng dẫn thiết kế `VIE_focus_coding_standards.md`~~: đã cập nhật header đồng bộ với cấu trúc submod ngày 06/10/2026.

## Lỗi của tool (không phải lỗi mod)

- `tools/check_static.py`, `tools/audit_mod.py`: hardcode đường dẫn ổ `D:` của máy tác giả.
- `prov.py` từng không báo state `671-673` (không thuộc VIE) trong scripted effect: mục "state-scope blocks" của nó đầu ra rỗng.
  Chưa rõ vì sao. Đừng coi "prov.py sạch" là bằng chứng rằng mọi state được scope đều thuộc VIE.
- `live.py` mục `DECISIONS` và `MIO` cho `used=0`: pattern chưa bắt cách mod gọi chúng, nên mục đó không kiểm được gì.
- Đã sửa 06/10/2026: `live.py` lỗi đường dẫn Windows, `live.py` báo nhầm dynamic modifier, `prov.py` crash `UnicodeEncodeError`.

## Không phải lỗi (đừng "sửa")

- Event `hidden = yes` bị `ev.py` báo "thiếu loc" (vd. `vie_air_force.51`, `vie_lf.2/.4`, `vie_naval.45`, `vie_p1b.12`).
- `audit_dds_and_gfx.py` báo `GFX_report_event_generic_*` thiếu: sprite của MD/vanilla.
- Decision `icon = <tên>` không có tiền tố `GFX_decision_`: engine tự thêm.
- `targeted_modifier = { tag = CHI }` trong idea: đúng cú pháp.
- Event ẩn tự fire lại chính nó có điều kiện dừng (`vie_naval.45` giao hàng Sigma): chủ ý.
- `custom_trigger_tooltip` không cần `hidden_trigger` bên trong.
- Scripted effect công trình của MD (`one_state_*`, `one_random_*`) đã tự trừ tiền: không trừ thêm lần hai.
