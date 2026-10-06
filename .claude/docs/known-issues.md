# Vấn đề đã biết

Danh sách tình trạng ngày **06/10/2026**, rút ra từ audit tĩnh (script `tools/audit/*` và grep). Chưa chạy trong
game. Mỗi mục ghi mức độ chắc chắn. Xoá mục khi đã sửa, và thêm mục khi phát hiện lỗi mới chưa sửa ngay.
Đừng "sửa" các mục ở phần "Không phải lỗi".

## Lỗi code (cần sửa)

Không còn lỗi code mở trong danh sách này. Đã sửa ngày 06/10/2026 (trong working tree, chưa commit; `prov.py` 0 lỗi,
`live.py` 0 MISSING):
- `VIE_md_effects_p17.txt`: 9 dòng bunker nay có `province =`; state `671-673` đổi sang state VIE (518-524);
  công trình bunker trừ tiền (-6, -2, -2, -2 tỷ qua `modify_treasury_effect`).
- `VIE_md_hardline_decisions.txt`: bỏ `days_remove` thừa ở `VIE_hl_extraordinary_plenum`, `VIE_hl_ultimatum_laos`,
  `VIE_hl_ultimatum_cambodia` (không có `remove_effect`).

Còn theo dõi, chưa phải lỗi: 25 decision (14 `VIE_rn_*` trong `VIE_md_decisions.txt`, 11 `VIE_dec_*` trong
`VIE_md_def_industry.txt`) có `fire_only_once = yes` cùng `days_remove`. Cả 25 đều có `remove_effect` nên là mẫu "việc có hạn,
hết hạn thì trả kết quả", coi là chủ ý. Chưa kiểm hành vi trong game; nếu thấy decision biến mất hoặc không hoàn lại đúng,
kiểm tra mẫu này trước.

## Nợ nội dung

- **36 idea định nghĩa mà `live.py` không thấy ai cấp**: `VIE_air_dominance_idea`, `VIE_bastion_idea`,
  `VIE_blue_water_idea`, `VIE_modern_*_2030_idea`, `VIE_democratic_*`, `VIE_negotiated_transition_idea`,
  `VIE_vinacomin_idea`, `VIE_rare_earth_*`, ... (danh sách đầy đủ: chạy `live.py`, mục `IDEAS defined but never granted`).
  Một số có thể được cấp qua tên ghép động, kiểm bằng grep trước khi xoá.
- **Balance of Power oligarch** (`common/bop/VIE_md_bop_p3.txt`, `VIE_md_effects_p3b.txt`): mọi effect gate bằng cờ
  `VIE_bop_oli_active`, và không có `set_country_flag` nào đặt cờ này. Mã chết cùng các key loc `VIE_oli_*`.
- **Loc chết**: theo `VIE_repo_health_report.md` (30/09) hơn 40% key loc không còn được tham chiếu sau khi xoá focus v9 đến v11.
  Chưa đếm lại.
- **545 key loc trùng** giữa `localisation/english/` và `replace/`, 444 key khác nội dung. Bản trong `replace/` thắng,
  bản thư mục cha là chữ chết. Xem [localisation.md](localisation.md).
- Loc còn mã màu `§g` (74 chỗ), `§B` (10), `§C` (2), `§O` (1), và 82 dòng có em/en dash.
- Layout cây focus: kiểm bằng `tools/focus_layout/` và `tools/audit/audit.py` sau mỗi đợt xoá/thêm lớn.
- `common/bookmarks/blitzkrieg.txt` là bản sao file MD, cần so lại khi MD đổi phiên bản.
- Hướng dẫn thiết kế `VIE_focus_coding_standards.md` còn tham chiếu `.claude/docs/focus-tree-reference.md`,
  `search-filters.md`, `tools/validation/` của MD upstream. Cần cập nhật header cho khớp.

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
