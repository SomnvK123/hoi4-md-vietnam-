---
name: md-event-art
description: 'Tạo ảnh event/news cho VIE theo cảnh hiện đại và năm lịch sử, canvas consumer thực tế, mapping picture và codec DDS; không dùng frame focus.'
---

# Mỹ thuật Event / News Picture

Đọc [md-art](../md-art/SKILL.md). Tìm event ID, title, desc, options và picture.
Ảnh cần minh họa một thời điểm/hành động; không biến thành huy hiệu của branch.

## Profile và tư liệu

VIE hiện có 56 DDS 210×176 DXT1/BC1 ở gfx/event_pictures/.
tools/build_vie_event_pictures.py và các export hiện tại cùng profile này.
Không tự dùng panorama 450×150/500×200 chỉ vì prompt gọi “cinematic”.
News hoặc GUI khác có thể khác: tra texture/slot của consumer ấy trước.

Khớp năm, địa điểm, khí tài, quân phục, nhân vật và cờ. Phân biệt ảnh tư liệu có
license với cảnh AI diễn giải. Không gọi cảnh AI là ảnh chụp sự kiện thật.
Tư liệu chưa đủ nhận diện nhân vật: chọn cảnh môi trường/khí tài hợp lệ
hoặc ghi rõ concept, không bịa likeness từ tên.

## Bố cục và prompt

Một focal point và một hành động: đoàn tàu bàn giao, cuộc gặp, cảng hoạt động,
lực lượng ứng cứu. Tiền cảnh/midground/background có thể hữu ích,
không bắt buộc sáu layer.
Giữ chủ thể trong vùng an toàn để crop; hậu cảnh phục vụ bối cảnh.
Tránh caption, chữ bị bịa, frame vàng, HUD/hex ngoài đề tài.
Không ép mọi ảnh thành góc heroic hoặc ánh bình minh.

Prompt: “editorial historical illustration of <event>, <place/year>,
<verified subjects>, restrained modern materials, one clear focal action,
composition readable at 210x176, subdued background, no emblem frame,
no captions, opaque scene”. Thêm reference và chọn sắc độ khớp board.
transparent_background=false cho cảnh kín khi consumer dùng kiểu đó.

## Xuất và tích hợp

Lưu master/provenance ở assets/event_pictures/raw/, preview PNG ở png/.
Xuất gfx/event_pictures/<stem>.dds và đăng ký sprite riêng
GFX_VIE_report_event_<stem> trong interface/VIE_md_event_pictures.gfx.
Event picture thường dùng full sprite; tra code live trước khi gán.

Giữ BC1 như asset mục tiêu nếu encoder đã kiểm hỗ trợ. BC1 có palette nén,
không phải alpha mềm 8-bit. Cảnh kín nên opaque; xem lại banding/block artifacts.
Nếu cần RGBA/RGB32 không nén cho ảnh mới, dùng header hợp lệ, ghi thay đổi codec
và kiểm consumer; không nói mọi DDS khác 33.980 byte đều lỗi.
Không chạy builder tải/build hàng loạt để thay một ảnh nếu nó viết lại .gfx.

Kiểm canvas, ratio/crop, path và event picture mapping.
Chạy python3 tools/audit_dds_and_gfx.py; các GFX_report_event_generic_* có thể
được MD/base game cung cấp, không tự xóa các reference ấy.
Trong game: gọi đúng event trên bản save thử, kiểm popup/news slot,
đọc title/options không bị frame/ảnh lấn. Không coi exit=0 là gameplay pass.

