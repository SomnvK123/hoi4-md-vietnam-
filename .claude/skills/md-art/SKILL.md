---
name: md-art
description: 'Điều phối thiết kế, tạo, sửa, xuất và tích hợp mỹ thuật MD Vietnam. Dùng cho icon focus, national spirit, decision, category, ảnh event, portrait, BoP, MIO và UI; chọn skill theo consumer thực tế.'
---

# Điều phối mỹ thuật MD Vietnam

Yêu cầu: $ARGUMENTS. Đọc skill này khi làm tài nguyên hình ảnh cho mod,
kể cả yêu cầu “gen hai mẫu”, “sửa icon” hoặc “thêm vào mod”.

## 1. Đọc và phân loại

Đọc [hệ thống chung](../../docs/art-style-guide/07_unified_art_system.md),
[profile/xuất file](../../docs/art-style-guide/04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md)
và [đánh giá phong cách](../../docs/art-style-guide/06_review_modern_day_analysis.md).
Yêu cầu hiện tại của người dùng và consumer thật ưu tiên hơn mặc định tài liệu.

| Yêu cầu | Skill chuyên biệt |
|---|---|
| National focus / goals | [md-focus-art](../md-focus-art/SKILL.md) |
| National spirit / idea / law | [md-idea-art](../md-idea-art/SKILL.md) |
| Decision / category | [md-decision-art](../md-decision-art/SKILL.md) |
| Event / news picture | [md-event-art](../md-event-art/SKILL.md) |
| Leader / commander / advisor | [md-portrait-art](../md-portrait-art/SKILL.md) |
| BoP / MIO / trait / button / flag / other UI | [md-ui-art](../md-ui-art/SKILL.md) |

Đồng bộ phong cách không đồng nghĩa dùng cùng khung/kích thước.
Không áp vector HUD neon hoặc sơn dầu/ba sao lên mọi nhóm.

## 2. Xác lập công việc và consumer

- Đọc git status; giữ các thay đổi sẵn có, gồm hai icon ngoại giao đã được chọn.
- Tìm ID bằng rg trong common/, events/, interface/ và file GUI nếu có.
- Lần theo field → sprite/path → texture; đọc kích thước/mode/header ảnh mẫu.
- Với texture chung, liệt kê mọi consumer trước khi overwrite; tạo sprite VIE
  riêng nếu thay texture generic ảnh hưởng đối tượng ngoài phạm vi.
- Lập [brief](../../docs/art-style-guide/templates/asset-brief.md);
  có thể rút gọn cho một asset đơn giản, nhưng phải biết canvas/alpha/mapping.
- Thiếu slot cho UI mới: làm master/concept hữu ích, đánh dấu export chưa xác minh.
  Chỉ hỏi thông tin thật sự ngăn tiến triển; không hỏi duyệt lại bước đã được yêu cầu.

## 3. Chọn tư liệu và tạo ảnh

Chọn board 3–5 mẫu cùng loại khi làm nhóm mới/lô lớn. Với yêu cầu nhỏ và đã có
mẫu được chọn, dùng mẫu đó cộng một đối chiếu phù hợp; không ép thu thập đủ số
để trì hoãn. Ghi nguồn, commit/ngày và các đặc điểm học được.
Xem ảnh tham chiếu thực tế trước khi sửa hoặc đưa vào công cụ.

Dùng công cụ tạo/chỉnh ảnh có sẵn cho artwork. Không thay generation bằng vẽ
đa giác thủ công chỉ vì thuận tiện. Dùng Python/Pillow cho đo đạc và chuyển đổi
file theo workflow được hỗ trợ; không tự dùng nó để sửa mỹ thuật nếu công cụ
hoặc yêu cầu hiện tại quy định cách chỉnh khác.
Có thể tham chiếu vector chính xác cho cờ/logo theo công cụ hỗ trợ.

Prompt cần ghi rõ chủ thể, thời kỳ, silhouette, camera, palette, ánh sáng, frame,
alpha, canvas dự kiến, chi tiết phải đúng và điều cần tránh.
Từ khóa “Millennium Dawn style” một mình không đủ.
Không đưa suffix Midjourney như --ar vào công cụ không hỗ trợ.
Prompt templates ở [tập sản xuất](../../docs/art-style-guide/04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md).

## 4. Phân biệt sample và triển khai

Người dùng yêu cầu mẫu: tạo số mẫu được yêu cầu, hiển thị chúng, báo chưa tích hợp.
Người dùng yêu cầu thêm vào mod: tiếp tục xuất, mapping và kiểm tra; không hỏi
xác nhận lại. Không tự mở rộng từ hai icon sang thay mọi asset.

Giữ master có tên ổn định, export, prompt/provenance và [hồ sơ kiểm định](../../docs/art-style-guide/templates/asset-record.md).
Đặt trial/export tạm ngoài path game load. Không ghi đè ảnh có thay đổi chưa biết.

## 5. Kiểm và báo cáo

Kiểm file thật: canvas, alpha, codec/channel masks, mipmap/frame count, path tồn tại,
sprite không trùng và ID được dùng. Với DDS không nén, kiểm round-trip màu/alpha.
Kiểm bản 1:1 trên nền UI và so cùng nhóm; đọc rõ quan trọng hơn số màu độc nhất.
Chạy audit liên quan theo skill chuyên biệt và xem nội dung báo cáo.
Audit có thể in lỗi rồi exit=0; reference do base game/MD cung cấp phải tra upstream,
không tự xóa chỉ vì chưa có trong submod.

Chỉ báo in-game pass khi thực sự chạy game và xem đúng consumer.
Final: asset nào tạo/thay, file nào, kiểm nào đạt, hạn chế và cách xem trong game.
Không tự commit/push hay sửa gameplay ngoài phần mapping cần cho ảnh.

