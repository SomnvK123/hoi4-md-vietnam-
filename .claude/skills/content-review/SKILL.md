---
name: content-review
description: 'Review nội dung mod VIE (focus, effect, decision, event, idea, loc) trong một file hoặc diff so với checklist của repo. Dùng khi người dùng muốn review trước khi merge.'
---

Review nội dung. Phạm vi: $ARGUMENTS (mặc định `git diff main...HEAD`).

Đọc skill `md-focus-standard` (mục 9 là checklist), `.claude/docs/bug-patterns.md`, `.claude/docs/conventions.md`, `.claude/docs/known-issues.md`.

Checklist (mỗi mục gắn nhãn BLOCKER hoặc NIT):
- **Tham chiếu chéo**: effect/trigger/idea/event/loc tồn tại; không bịa token MD. `/validate refs` và `/validate event`.
- **Cây focus**: toạ độ, anchor, prerequisite, vòng lặp. `/validate focus`. Gate không còn trỏ focus đã xoá.
- **Tiền và công trình**: trừ tiền qua scripted effect hoặc `modify_treasury_effect`; công trình province có `province =`;
  mọi `NNN = {` là state VIE (`/validate prov`).
- **Scope và vòng đời**: `country_exists` trước khi nhắm nước khác, cờ có nơi set/clear, không gate chết, không bypass bất khả.
- **AI**: `ai_will_do` / `ai_chance` có mặt, guard bankruptcy cho chi tiêu lớn.
- **Loc**: đủ key, đúng bản đang hiển thị (`replace/`), không mã màu lạ.
- **Cân bằng**: nếu đụng trục quân sự, chạy script `*_balance.py` tương ứng, phải in `PASS`.
- **Thiết kế**: khớp file thiết kế `VIE_*.md` của hệ thống, không phá quyết định đã chốt.

Báo theo mức nghiêm trọng, mỗi lỗi có `file:dòng`, kịch bản hỏng, và nói rõ điều gì chưa kiểm trong game.
