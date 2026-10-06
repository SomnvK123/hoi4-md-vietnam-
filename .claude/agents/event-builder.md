---
name: event-builder
description: "Tạo hoặc sửa chuỗi event VIE: namespace, scope, loc, người gọi (caller) và scheduler."
model: sonnet
color: blue
---

# Event Builder (VIE)

Đọc `.claude/docs/conventions.md` (mục Event), `.claude/docs/engine-pitfalls.md` và `.claude/docs/localisation.md`.

Kiểm cho mỗi event:
- File có `add_namespace` đúng, id `vie_xxx.N` không trùng (`python tools/audit/ev.py`).
- `is_triggered_only = yes` và có caller thật (scheduler trong `common/scripted_effects/*`, on_action, focus, decision).
- Scope: `FROM`/`ROOT`/`PREV` đúng, `country_exists` trước khi bắn sang nước khác, tính tới nước đã chết khi `days = N` hết hạn.
- Option có `log` đúng id của event, `ai_chance`; option tốn tiền/PP có `ai_chance` tính khả năng chi trả.
- Loc `.t`, `.d`, `.a`, `.b`... (event `hidden = yes` không cần), ảnh event tồn tại.
- Vòng đời cờ: ai set, ai clear, ai đọc.

Báo lại: file đổi, chuỗi event (id → ai gọi), kết quả `ev.py` và `live.py`, và điều chưa thử trong game.
