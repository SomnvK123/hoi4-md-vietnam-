---
paths:
  - "events/**"
  - "common/decisions/**"
---

# Event và decision

Đọc `.claude/docs/conventions.md` (Event, Decision) và `.claude/docs/engine-pitfalls.md`. Mỗi file event có
`add_namespace`; event bắn sang nước khác cần `country_exists`; `days_remove` đi cùng `remove_effect`.
Sau khi sửa chạy `python tools/audit/ev.py`.
