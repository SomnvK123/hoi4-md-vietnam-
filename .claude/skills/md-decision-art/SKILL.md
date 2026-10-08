---
name: md-decision-art
description: 'Tạo icon decision/category cho VIE theo ô UI nhỏ, motif hành động và TGA/DDS thực tế. Không dùng badge focus hoặc giả định mọi category là 64x64.'
---

# Mỹ thuật Decision và Category

Đọc [md-art](../md-art/SKILL.md). Tách nút hành động và ô danh mục;
đọc file decision/category live, field icon và sprite trước generation.

## Profile đã đo

- Decision VIE: 9 RGBA TGA, 33×32.
- Category texture đang có: 1 RGBA TGA, 52×40.
- Category texture tồn tại không chứng minh category đó đang được code dùng.
  Kiểm live ID/consumer trước khi tạo hoặc thay.
- Chưa có GUI base game/MD trong checkout để xác nhận các slot khác.
  Với nút mới, tra slot hoặc lấy một mẫu cùng chức năng; không tự dùng 44×44.

Định dạng TGA đang dùng là hợp lệ theo sprite hiện tại. Giữ codec/đuôi path
khi thay icon; không đổi đuôi .tga thành .dds mà quên texturefile.

## Concept ở độ phân giải rất nhỏ

Một silhouette/hành động, vài mảng màu đủ tương phản. Ở 33×32, bỏ chữ, số
và quốc huy phức tạp. Không vòng lá dày, ba sao và bản đồ nền kiểu focus.
Sử dụng màu ngành, nhưng không làm decision chỉ nhận biết được qua màu.

| Hành động | Motif gợi ý |
|---|---|
| Kiểm tra/giám sát | hồ sơ + dấu kiểm |
| Luân chuyển cán bộ | thẻ người + mũi tên chuyển |
| Đầu tư/mua sắm | thùng hàng + dấu cộng |
| Đàm phán | tài liệu + liên kết hai phía |
| Phòng thủ/ứng cứu | shield hoặc phao phù hợp ngữ cảnh |

Category diễn tả ngành/tổ chức thay vì lặp động từ từng decision.
Giữ nền alpha và khoảng thở; viền glow nếu có phải kiểm ở 1:1,
không áp cố định 2–3 px vào mọi canvas.

## Tạo, mapping và kiểm

Tạo master lớn hơn với motif đơn giản, xuất final đúng slot; không render text nhỏ.
PNG source ở assets/decisions/ nếu tạo nhóm mới; export vào gfx/interface/decisions/.
Giữ RGBA khi xuất TGA; nếu đổi codec, kiểm runtime hỗ trợ và cập nhật texturefile.
Đọc lại ảnh export để kiểm alpha/canvas.

Tên hiện có: GFX_decision_VIE_<stem> hoặc GFX_decision_category_VIE_<stem>.
Đừng giả định prefix tự động: copy cách icon được dùng trong block live phù hợp.
Thêm sprite VIE riêng trong interface/VIE_md_decision_icons.gfx nếu cần,
không viết lại cả file hay sửa cost/visible/effects.

python3 tools/audit_dds_and_gfx.py kiểm path trong .gfx, nhưng không audit
header TGA hoặc mọi decision/category icon field. Kiểm các ảnh TGA bằng Pillow
và mapping bằng rg; xem toàn hàng ở kích thước thật, không chỉ master lớn.
Trong game: mở danh mục và decision tương ứng, kiểm hover/disabled nếu có.

