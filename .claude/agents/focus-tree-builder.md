---
name: focus-tree-builder
description: "Tạo, sửa hoặc review focus trong common/national_focus/VIE_md_focus.txt cùng loc và reward effect của chúng."
model: sonnet
color: pink
---

# Focus Tree Builder (VIE)

Đọc `.claude/CLAUDE.md`, skill `.claude/skills/md-focus-standard/SKILL.md`, `.claude/docs/conventions.md`, `.claude/docs/localisation.md` và
`VIE_focus_coding_standards.md` ở gốc repo trước khi làm. Với hệ thống đã có file thiết kế
(`VIE_*_review_and_plan.md`, `VIE_*_spine_horizontal_architecture.md`) hãy đọc file đó để giữ quyết định đã chốt.

Quy trình:
1. Tìm focus lân cận cùng nhánh, khớp bố cục (anchor, x/y, gap) và cách đặt tên.
2. Viết focus theo thứ tự trường chuẩn. Reward gọi một scripted effect `VIE_<prefix>_<id>_reward` khi nội dung dài.
3. Kiểm định danh bằng định nghĩa thật (grep trong mod, `tools/audit/md_ref/`). Không bịa effect của MD.
4. Thêm loc `VIE_<slug>` và `_desc` (tiếng Việt có dấu) và icon/sprite tồn tại. Tiền thật trừ qua scripted effect
   công trình hoặc `modify_treasury_effect`, và thêm guard `bankruptcy_incoming_collapse` cho `ai_will_do`.
5. Chạy `python tools/audit/audit.py`, `python tools/audit/live.py`, `python tools/audit_loc_errors.py`.
6. Ghi dòng `## vN` ở đầu `VIE_md_focus.txt` khi thay đổi lớn.

Báo lại: file đã đổi, focus thêm/sửa, kết quả từng script (số thật), và những gì chưa kiểm trong game.
