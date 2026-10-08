---
name: md-portrait-art
description: 'Tạo/sửa chân dung leader, commander và advisor VIE từ tư liệu nhận dạng, đúng tuổi/chức vụ/quân phục, với large/small export và đường dẫn portraits đúng consumer.'
---

# Mỹ thuật Portrait / Advisor

Đọc [md-art](../md-art/SKILL.md). Đọc character definition và giai đoạn tuyển/retire.
Portrait phục vụ nhận diện một người; không dùng mặt generic để báo đã tái hiện người thật.

## Profile và likeness

Profile large đang có: 156×210; small: 38×51.
Large trộn DXT1 và RGB32; small hiện có RGB32.
Đọc đúng file mục tiêu và slot army/civilian/advisor, không ép codec đồng loạt.
Các silhouette do build_vie_placeholder_portraits.py tạo là placeholder, không
nguồn xác nhận khuôn mặt; ghi rõ khi dùng chúng.

Tìm tư liệu hợp lệ theo tên, năm, chức vụ; kiểm đường chân tóc, cấu trúc mặt,
tuổi, kính, nét đặc trưng, uniform và insignia.
Giữ likeness khi chuyển phong cách; không trẻ hóa/tăng huân chương hoặc thêm
cấp hàm sai thời kỳ. Cờ và lãnh đạo khác không được lẫn vào background.
Thiếu tư liệu chính xác: hoàn thành brief/reference độc lập rồi yêu cầu nguồn
còn thiếu; không bịa từ tên người.

## Tạo ảnh và bố cục

Phong cách chân dung biên tập có tô khối, bớt photo noise, background giản dị
khớp board. Khuôn mặt/ánh mắt là điểm nổi bật, vai và ngực vừa đủ nhận chức vụ.
Khung focus, sao đỉnh, HUD, badge neon không phù hợp portrait thông thường.
Prompt nêu người, năm/tuổi, reference thực tế, framing, costume verified và ánh sáng.
Không dùng “anh hùng ca” để làm biến đổi danh tính.

Tạo large master có khoảng thở đầu/vai. Small là crop riêng ưu tiên mặt,
không chỉ ép toàn khung large vào 38×51 nếu khiến mặt quá nhỏ.
Small và large phải cùng người/giai đoạn/palette.

## Export, mapping, QA

Lưu source, prompt và quyền sử dụng; theo đường dẫn gfx/leaders/VIE/ và small/.
RGB32 156×210 không mipmap: 131.168 byte; 38×51: 7.880 byte.
Đó không phải dung lượng của DXT1 hoặc TGA.

Character có thể trỏ đường dẫn trực tiếp trong portraits/army hoặc
portraits/civilian, với field large và small. Copy cú pháp thật từ block tương ứng.
Advisor có thể dùng sprite riêng; tra thực tế, đừng giả định cần GFX_focus_*.

Xác nhận cả hai file và mapping character; audit DDS/path không thay thế
kiểm likeness. Không chạy silhouette builder lên các chân dung đã hoàn thiện.
Xem 156×210 và 38×51 ở 1:1; kiểm mặt/tóc/cổ/rìa crop.
Khi có game: recruitment/advisor/leader panel theo đúng năm và role.
Báo thiếu tư liệu hoặc placeholder một cách rõ ràng.

