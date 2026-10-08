---
name: md-ui-art
description: 'Thiết kế BoP, MIO, trait, nút UI, emblem và flag VIE bằng cách khám phá sprite/GUI slot, số frame và state; không suy đoán kích thước từ focus.'
---

# Mỹ thuật UI / BoP / MIO / Trait / Flag

Đọc [md-art](../md-art/SKILL.md). Dùng khi asset không thuộc focus, spirit,
decision, event hoặc portrait; kích thước phải được xác lập từ consumer.

## Khám phá slot trước

1. Tìm ID/code live: common/bop/, common/military_industrial_organization/,
   interface/*.gfx, *.gui và texture thực tế.
2. Xác định sprite hay path trực tiếp; kích thước hiển thị, scale, alpha,
   số frame/noOfFrames, sprite sheet, state normal/hover/disabled/selected.
3. BoP/MIO VIE đang dùng nhiều GFX_idea_generic_* / GFX_generic_mio_trait_*.
   Base game/MD không có trong checkout: reference ngoài repo chưa chứng minh
   thiếu. Tra upstream cùng version hoặc slot runtime.
4. Chưa đọc được slot: tạo brief/master có ghi “canvas chưa xác minh”;
   không xuất game-ready dựa trên 93×91 hoặc 156×156.

## Thiết kế hệ trạng thái

Cùng category giữ chiều nét, scale, hướng sáng và vùng chiếm dụng.
Trait icon chỉ một năng lực; không thu nhỏ focus scene.
BoP hai phía cần phân biệt silhouette và ý nghĩa political, không chỉ đỏ/xanh.
MIO organization emblem thể hiện ngành/tổ chức; không dùng logo đối tác khác
khi chưa có lý do gameplay.
Đọc quy ước interface trước khi thêm frame, vì GUI có thể vẽ viền.

Nút/sprite sheet cần mỗi frame đúng kích thước và thứ tự state; đừng tạo
ba file độc lập nếu consumer yêu cầu một strip.
Màu disabled không được làm glyph biến mất; selected khác hover rõ ràng.
Text quan trọng thuộc localisation/GUI, không rasterize nếu slot đang dùng text.

## Flag và logo

Flag trong gameplay không là “cờ có ánh sáng” trong một icon.
Đọc variants/size/medium/small/ideology filename từ base game/MD và consumer,
giữ hình cờ chính xác; không tự thêm canvas hoặc prefix.
Logo cần nguồn đúng và quyền dùng; tạo lại cách điệu không chứng minh tính chính thức.

## Tích hợp và kiểm

Tạo sprite có namespace VIE; liệt kê nơi sprite generic đang được dùng trước
khi thay. Không redefine generic MD để thuận tiện.
Xuất theo codec/canvas/noOfFrames đã xác minh; không rebuild toàn .gfx.
Nếu cần sửa GUI, giữ thay đổi trong ô đã được yêu cầu và kiểm cả panel.

Chạy audit hiện có cho DDS/.gfx, tự kiểm TGA/strip/state/mapping ngoài phạm vi audit.
Xem preview 1:1 cả state và hàng cùng nhóm; khi có game kiểm panel thực tế.
Lưu provenance và ghi rõ việc nào chưa kiểm vì thiếu GUI/base game.

