---
name: new-focus
description: 'Thêm một hoặc nhiều focus mới vào cây focus VIE kèm reward effect, loc và icon. Ví dụ: "/new-focus VIE_xyz dưới VIE_abc". Dùng khi cần tạo focus mới.'
---

Thêm focus mới vào `common/national_focus/VIE_md_focus.txt`. Yêu cầu: $ARGUMENTS

1. Đọc skill `md-focus-standard` (chuẩn MD: reward đa dạng, AI guard, tooltip) và `.claude/docs/conventions.md` (mục Focus, Tiền và công trình) và `VIE_focus_coding_standards.md`
   (thứ tự trường, bố cục hàng ngang). Hỏi lại nếu thiếu: id, cha (prerequisite), nội dung reward, điều kiện mở.
2. Tìm focus cùng nhánh, chọn `relative_position_id` là một prerequisite của focus mới, `y = 1`, x lệch anh em ±2.
   Chèn focus **sau** anchor của nó trong file.
3. Viết focus đúng thứ tự trường, `search_filters` 1 dòng, `log` ở dòng đầu reward, `ai_will_do` cuối.
   Reward dài thì viết effect `VIE_<prefix>_<id>_reward` trong `common/scripted_effects/VIE_md_effects_<chủ đề>.txt`.
4. Mọi effect/trigger/idea dùng phải tồn tại thật. Tiền trừ bằng scripted effect công trình hoặc `modify_treasury_effect`;
   chi từ ~5 tỷ thêm `FOCUS_FILTER_EXPENDITURE` và guard bankruptcy.
5. Thêm loc `VIE_<id>` và `VIE_<id>_desc` (có dấu) vào file loc của hệ thống; nếu key đã có ở `replace/`, sửa bản đó.
   Icon: dùng sprite có thật (`interface/*.gfx`) hoặc build bằng `tools/build_*_focus_icons.py`.
6. Chạy `/validate focus`, `/validate refs`, `/validate loc`. Ghi dòng `## vN (dd/mm/yyyy)` ở đầu file focus.
7. Báo: id, vị trí (x, y, anchor), file đã đổi, kết quả kiểm tra, việc còn lại để thử trong game.
