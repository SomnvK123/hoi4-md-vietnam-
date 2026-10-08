# Tập 5: Khung focus và phân cấp giao diện

## 1. Khung phục vụ consumer

Khung tạo silhouette, phân nhóm và mức trang trọng. Một focus có thể có
frame trong ảnh, frame từ GUI, hoặc hình trần; không có bằng chứng mọi
focus MD bắt buộc đủ năm thành phần hay đúng ba sao.

VIE đã chọn hai mẫu ngoại giao có wreath/ba sao/badge đỏ. Dùng chúng để
đồng bộ nhóm ngoại giao; không áp lên mọi asset.
Trước khi thêm frame, tra .gfx và GUI nếu có để tránh khung kép.

## 2. Các thành phần có thể dùng

| Thành phần | Công dụng | Khi nên giảm/bỏ |
|---|---|---|
| Crest/sao đỉnh | mức trang trọng, trục dọc | decision/trait, khi lấn chủ thể |
| Wreath/rice leaves | ngoại giao/nhà nước, hình bao | công nghệ trần, frame GUI có sẵn |
| Bezel/vành trong | tách scene khỏi frame | glyph nhỏ, scene không có inset |
| Ribbon/medallion đáy | nhận diện nhóm, trọng lượng thị giác | khi badge làm icon nặng hơn cùng hàng |
| Sunburst/rim accents | tách silhouette | khi thành noise/glow hoặc tràn biên |

Sao đỉnh là trang trí, không quốc huy. Không gọi huy hiệu sao đỏ/ba sao là
emblem quốc gia đúng quy chuẩn khi hình chưa được đối chiếu nguồn.

## 3. Họ khung đề xuất cho VIE

| Nhóm | Gợi ý | Cần kiểm |
|---|---|---|
| Ngoại giao | vàng/brass, vòng lá hoặc rice, đỏ/jade | centerpiece rõ hơn frame |
| Chính trị | lacquer/bronze, sách/seal, crest nhẹ | không lẫn Party/National emblems |
| Quân sự | shield/thép, frame mở hoặc không frame | silhouette khí tài nổi bật |
| Kinh tế/hạ tầng | cog/bezel kỹ thuật tiết chế | không biến mọi thứ thành gear |
| Biển đảo | maritime rim/rope/anchor nếu có nghĩa | không che đảo/tàu/phao |
| Số hóa/nghiên cứu | tech bezel hoặc góc cắt nhẹ | neon cục bộ, không sci-fi tràn nhánh |

Đây là thư viện lựa chọn, không khuôn cứng. Một nhóm nên có vài silhouette
để nhận diện mục tiêu; không chỉ đổi chủ thể nhỏ trong cùng frame áp đảo.

## 4. Hai kiểu nguồn và hai cách xử lý

**Complete badge:** master đã có artwork và frame. Thu toàn badge bằng contain,
giữ tỷ lệ và khoảng thở. Hai PNG raw ngoại giao hiện có thuộc kiểu này.
Không crop tròn tâm hoặc gọi process_focus_batch.py để đóng thêm khung.

**Centerpiece riêng:** master chưa có frame. Chọn frame đã duyệt, dựng inset/mask
theo hình thật của frame, đặt artwork xuống dưới, kiểm overlap/AO và silhouette.
Không mặc định radius=31, center=(46,43) cho mọi frame hoặc mọi size.
Cắt mask mềm không thay thế cho generation/edit artwork bằng công cụ phù hợp.

“Đóng khung bằng code” chỉ là compositing/output, không tự biến frame primitive
thành painterly artwork. tools/process_focus_batch.py hiện có cách dựng khung
bằng hình học; cần xem output trước khi dùng, không coi script đó là bảo đảm
chất lượng hay chạy nó lên master đã có frame.

## 5. Tỷ lệ và vùng an toàn

Profile focus VIE 93×91. Recipe hiện dùng vùng tối đa 91×89, đặt giữa canvas,
giữ một pixel alpha ngoài cùng. Đây là chính sách xuất icon, chưa chứng minh
mọi asset thiếu border đều gây lỗi engine.

Giữ đầy đủ các đầu sao/lá/ribbon. Alpha thật bên ngoài, không matte đen/chessboard.
Mép frame có anti-alias phù hợp; kiểm nền sáng để thấy viền đen bẩn.
Không thêm blur/AO cố định 1.8 px cho mọi size: decision và category cần cách khác.

## 6. QA và giới hạn

Xem 1:1 bên cạnh 3 icon cùng nhóm. Hỏi:
- Chủ thể đọc trước hay frame đọc trước?
- Vùng vàng/đỏ và scale có tương đương không?
- Nội dung có khác đủ bằng silhouette không?
- Shine/hover có frame riêng tạo chồng viền không?
- Ba sao và chữ nhỏ có thành noise không?

Nếu chưa có game/GUI, ghi rõ chỉ kiểm texture.
Chỉ sửa pixel/frame trong phạm vi yêu cầu; không sửa focus position/reward.
[Xuất file và mapping](04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md).
