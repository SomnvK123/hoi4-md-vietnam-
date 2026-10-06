---
name: loc-check
description: 'Kiểm loc của focus, decision, event, idea, tooltip đã thêm hoặc đổi: thiếu key, key trùng với replace/, mã màu, getter. Dùng khi vừa thêm nội dung mới hoặc người dùng gọi /loc-check.'
---

Kiểm loc cho nội dung vừa thêm/đổi. Phạm vi: $ARGUMENTS (mặc định: các file đổi trong `git diff` và `git status`).

1. Chạy `python tools/audit_loc_errors.py` và `python tools/verify_all_loc.py` (đặt `PYTHONIOENCODING=utf-8`).
2. Với mỗi id/key mới: có `VIE_<id>` và `_desc` (focus, idea), `.t/.d/.a` (event hiển thị), `VIE_tt_*` cho tooltip tuỳ chỉnh.
   Event `hidden = yes` không cần loc.
3. Với mỗi key định nghĩa trong file thường: grep key đó trong `localisation/english/replace/`. Nếu có thì bản `replace/` mới là
   bản hiển thị. Báo key trùng giữa hai thư mục và chỗ nào đang thắng.
4. Với chuỗi vừa sửa: BOM + `l_english:` ở dòng đầu, thụt 1 dấu cách, escape `\"`, `§` luôn đóng `§!`, chỉ dùng
   `§Y/§G/§R/§W`, getter đúng hoa thường, không `TODO`/`...`/em dash.
5. Số liệu trong chuỗi khớp effect thật.

Báo danh sách `file:dòng — vấn đề`, nói rõ lỗi mới do thay đổi này khác với nợ cũ trong `.claude/docs/known-issues.md`.
