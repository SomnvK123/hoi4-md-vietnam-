# Tập 1: Phân tích phong cách HOI4 và Millennium Dawn

## 1. Điều gì đã xác minh, điều gì là lựa chọn

[Đánh giá nguồn và phân tích gửi](06_review_modern_day_analysis.md) ghi bằng chứng
upstream và inventory VIE. Tài liệu này đưa phương pháp đọc hình ảnh, không tuyên bố
toàn MD dùng một phong cách độc nhất.

Mẫu accept_treaty ở commit MD đã kiểm tra vẫn có vòng lá vàng, giấy và bàn tay tô khối.
Các mẫu tham chiếu sẵn có khác dùng globe, động vật và dải lụa.
Vì vậy “bối cảnh hiện đại” không suy ra “vector phẳng/HUD neon bắt buộc”.
Ngược lại, “game Paradox” cũng không suy ra “mọi asset phải sơn dầu chi tiết”.

Quy chuẩn mỹ thuật của VIE là quyết định nội bộ. Tách ba nhãn trong nghiên cứu:
- Đã đo: canvas, codec, header, sprite/path, pixel alpha.
- Đã quan sát: vật thể/frame/palette trong mẫu cụ thể đã xem.
- Đề xuất: cách dựng VIE; cần kiểm sample 1:1 và consumer.

Không dùng tính từ AAA, “chuẩn tuyệt đối” hoặc số màu thay cho bằng chứng.

## 2. Bốn trục độc lập của phong cách

| Trục | Hai đầu phổ | Ý nghĩa với asset |
|---|---|---|
| Mức khái quát hóa | silhouette biểu trưng ↔ tả thực chi tiết | quyết định lượng thông tin ở độ phân giải nhỏ |
| Cách tạo khối | flat/cel ↔ gradient/painterly | quyết định vật liệu và độ nổi |
| Nhận diện UI | glyph trần ↔ badge/frame | quyết định slot và vùng chiếm dụng |
| Bối cảnh | lịch sử ↔ hiện đại/alt-history | quyết định vật thể, năm, quân phục, vật liệu |

Vector là cách biểu diễn dữ liệu/hình học, không đồng nghĩa thiếu chiều sâu.
Raster có thể rất phẳng; vector có thể có gradient/phối cảnh.
Cel-shading cũng có thể phối vật liệu tả thực; từ khóa không thay thế xem ảnh.
Chọn cấu hình theo consumer: decision thiên glyph, focus thiên biểu trưng,
portrait thiên likeness, event thiên scene.

## 3. Giải phẫu một mẫu tham chiếu

Xem file alpha thật và screenshot UI nếu có, không chỉ thumbnail nền đen.

1. Chủ thể: điều người xem đọc đầu tiên là gì? Có hợp ý nghĩa gameplay không?
2. Silhouette: hình bao có khác asset cùng hàng không?
3. Scale: frame chiếm bao nhiêu so với vật thể? Có bị UI frame kép?
4. Value: vùng sáng/tối có tách chủ thể/nền ngay ở 1:1 không?
5. Material: ánh sáng gợi stone/steel/brass/fabric như thế nào?
6. Detail: phần nào biến thành noise khi downsample?
7. Palette: điểm nhấn có chức năng hay chỉ để rực?
8. Technical: canvas, alpha, codec, sprite frames/scale và path consumer.
9. Context: năm/nhánh/nguồn/commit; đã được xem in-game hay chỉ file?

Board phải chứa mẫu cùng loại. Không suy ra kích thước/UI slot từ tên “focus”.
Một icon 85×73 có thể tồn tại trong MD; VIE dùng 93×91 là quyết định profile hiện có.

## 4. Độ nổi và vật liệu ở kích thước nhỏ

Tô khối cần phân biệt mặt đón sáng, mặt nghiêng và khe tiếp xúc. Giữ nguồn sáng
chính nhất quán trong nhóm. Fill/rim light giúp silhouette nhưng không được làm
mọi viền phát sáng như hologram.

Vàng/đồng: mảng tối nâu, midtone ấm và highlight hẹp; tránh phủ trắng cả bề mặt.
Thép/titan: slate/blue-grey, sáng ở góc, không cần rỉ sét để đọc như kim loại.
Granite: một vài hạt gợi vật liệu trong master; final ưu tiên mặt phẳng và bóng khối.
Vải: nếp gấp hỗ trợ nhận diện cờ, không làm sao biến dạng.
Màn hình/radar: glow cục bộ có nguồn, không halo lan khắp frame.
Giấy: tối giản dòng chữ, góc cuộn/bóng tạo volume, không ép sepia khi đề tài hiện đại.

Không bắt buộc 3 nguồn sáng hoặc 6 layer ở mọi asset. Đó là phương án thi công,
không là cấu trúc mà DDS/engine yêu cầu.

## 5. Tối giản có chiều sâu

Tối giản tốt giữ ý nghĩa, silhouette và tương phản; bỏ ốc vít/hoa văn chữ không đọc được.
Hình học primitive có ích để blockout/mask/đo đạc; không phải thay thế cho artwork
khi người dùng yêu cầu minh họa giàu chất liệu.

Khung vàng nhiều tầng có thể đẹp ở 1.200 px nhưng lấn chủ thể ở 93×91.
So cả 1:1 và phóng lớn: bản lớn để sửa viền, bản nhỏ để đánh giá công dụng.
Đối với decision 33×32, một glyph có tô khối nhẹ có thể hiệu quả hơn scene phức tạp.

## 6. Trắc quang: chỉ dùng khi phương pháp rõ

Các con số “3.000 màu”, “mean 70–90”, “stddev 50–65” trong bản cũ chưa có
dataset/phương pháp tái lập làm chuẩn toàn mod. Bỏ chúng khỏi điều kiện pass.

Nếu cần đo cho một lô:
- Dùng cùng final canvas, vùng alpha và conversion màu.
- Ghi cách xử lý pixel alpha=0/partial alpha; background nào được composite.
- Nêu luminance là weighted RGB hay giá trị tuyến tính; không lẫn hai loại.
- Dùng kết quả để tìm outlier so với board, không tự gọi thấp/hơn là đẹp.
- Đừng thêm noise chỉ để tăng unique colors; nó có thể làm mất khả năng đọc.

Thông số kỹ thuật có thể kiểm tự động. Độ đồng bộ, nghĩa hình tượng và likeness
cần xem thực tế; màu chính xác của logo cần nguồn đáng tin.

## 7. Ứng dụng theo ngành và theo slot

[Hệ thống chung](07_unified_art_system.md) quy định palette/ngữ nghĩa.
[Tập 5](05_nghien_cuu_va_thiet_ke_khung_focus.md) nói khi dùng frame.
[Tập 4](04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md) xác lập consumer/export.

Modern day nên thể hiện trong chủ thể: mạng dữ liệu, hạ tầng, khí tài/năm hiện đại,
cơ quan và địa chính trị. Không cần đưa circuit/hex vào cột mốc biên giới.
Ngoại giao vẫn có brass/stone/fabric; semiconductor có glass/silicon/steel.
Portrait cần nhận ra người; event cần hiểu chuyện; decision cần hiểu hành động.
