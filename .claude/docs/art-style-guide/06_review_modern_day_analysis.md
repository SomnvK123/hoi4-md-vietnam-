# Đánh giá phân tích Modern Day và bằng chứng

Ngày đối chiếu: 08/10/2026. Đối tượng: submod VIE của Millennium Dawn (MD), HOI4 1.19.*.
“Modern Day” mô tả bối cảnh hiện đại; không phải một chuẩn mỹ thuật duy nhất cho mọi mod.

## Kết luận

Phân tích người dùng gửi đúng ở hướng đơn giản hóa hình tượng, chọn vật liệu hiện đại
và dùng radar/mạch điện cho chủ đề phù hợp. Chưa có bằng chứng cho kết luận MD đã
“chuyển hoàn toàn” sang vector phẳng, cel-shading hai tone hoặc HUD neon.
Không nên thay toàn bộ nguyệt quế, lụa và tả thực bằng hexagon phát sáng.

Tài liệu cũ của VIE cũng có khẳng định quá mạnh theo chiều ngược lại: mọi tài nguyên
phải sơn dầu, tối thiểu 2.500 màu, đủ sáu lớp, cùng cấu trúc khung.
Đó là lựa chọn thiết kế hoặc chỉ số thử nghiệm, không phải yêu cầu của engine
và không thể dùng để chứng minh một icon đẹp hay tương thích với MD.

Định hướng mới: minh họa biểu trưng hiện đại, vật thể đọc rõ ở kích thước thực,
tô khối vừa phải; chọn khung và chất liệu theo nhiệm vụ của từng ô giao diện.
Các mẫu ngoại giao đã được người dùng chọn là mốc tham chiếu cho nhóm ngoại giao,
không tự động trở thành khung bắt buộc của idea, decision hoặc portrait.

## Đối chiếu từng nhận định trong văn bản gửi

| Nhận định | Đánh giá | Quy tắc áp dụng |
|---|---|---|
| MD rời hoàn toàn mỹ thuật sơn dầu/WWII | Khái quát quá mức | Đổi chủ đề, thời kỳ và vật liệu; so với tài nguyên MD cùng nhóm |
| Tối giản vật thể, ít chi tiết vụn | Hữu ích | Giữ silhouette và 1 chủ thể; xét bản xuất ở 1:1 |
| Mọi vật liệu phải sạch, carbon/titan | Chỉ phù hợp một số đề tài | Granite, vải, giấy, đồng vẫn hợp lý cho biên giới/ngoại giao |
| Radar, globe, mạch điện | Hữu ích có điều kiện | Dùng khi mang nghĩa gameplay; không thêm HUD vào mọi icon |
| Nét có độ dày đồng đều | Một lựa chọn tạo hình | Không gọi đây là quy tắc MD đã được xác minh |
| Nguyệt quế/ruy băng đã bị thay hết | Có phản ví dụ trực tiếp | Mẫu accept_treaty vẫn dùng vòng nguyệt quế |
| Cyan/neon là bảng màu bắt buộc | Chưa có cơ sở | Chọn màu theo ngành; neon là điểm nhấn có kiểm soát |
| Cel-shading hai tone là chuẩn MD | Chưa xác minh | Có thể dùng cho biểu tượng rất nhỏ; không ép chân dung/ảnh sự kiện |
| Nền đen trong prompt icon | Sai nếu xuất thành nền đen đặc | Icon rời yêu cầu alpha thật; nền tối chỉ dùng khi xem thử |
| Outer Glow 2–3 px luôn cần thiết | Không nên áp dụng mặc định | Ở decision 33×32, viền ấy chiếm nhiều diện tích; kiểm tra ở 1:1 |
| Focus phải 156×156 | Không khớp VIE | 229 DDS focus hiện có là 93×91; kế thừa ô giao diện hiện tại |
| DDS uncompressed ARGB | Có thể phù hợp | Kiểm tra header/masks; tên ARGB không thay thế kiểm tra thứ tự byte |

## Bằng chứng từ MD upstream

Đã đọc HEAD bằng Git HTTPS và tải DDS từ commit cố định:
**25b58fcfa1d962acf2c94982d341dd16959f8df4**.

- [Tài nguyên accept_treaty ở commit đã kiểm tra](https://github.com/MillenniumDawn/Millennium-Dawn/blob/25b58fcfa1d962acf2c94982d341dd16959f8df4/gfx/interface/goals/00_diplomacy/accept_treaty.dds)
- [Tải trực tiếp cùng DDS](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/25b58fcfa1d962acf2c94982d341dd16959f8df4/gfx/interface/goals/00_diplomacy/accept_treaty.dds)
- Kích thước: 85×73, RGBA, DDS RGB 32-bit, flags 0x41.
- Masks R/G/B/A: 0x00FF0000 / 0x0000FF00 / 0x000000FF / 0xFF000000.
- Dung lượng: 24.948 byte = 128 + 85×73×4.
- SHA-256: 6c88f04002418dfacfec04be24fe10fc3f4452221d9c9c1b74c7248e9ad005d9.

Ảnh có vòng lá vàng, bàn tay, giấy hiệp định, bóng khối và nền alpha.
Mẫu này bác bỏ mệnh đề “tất cả nguyệt quế đã biến mất” và “mọi focus MD là
156×156”; một mẫu không đủ xác lập bảng màu hay phong cách của toàn MD.

Các PNG ở scratch/md_samples/ là tư liệu so sánh sẵn có. Đã xem accept_treaty,
focus_BRA_jaguar_diplomacy và diplomacy; chúng có khung/họa tiết và vật thể tô khối
khác nhau. Những bản chưa có provenance không được gọi là mẫu upstream đã xác thực.
Không quét được toàn bộ cây MD qua GitHub API (HTTP 403); không tuyên bố đã
khảo sát tất cả tài nguyên MD hoặc kiểm thử trong game.

## Bằng chứng từ checkout VIE

Đếm trực tiếp bằng Pillow và đọc DDS header; không suy ra từ tên thư mục.

| Nhóm đang có | Số lượng | Canvas | Định dạng quan sát |
|---|---:|---|---|
| gfx/interface/goals | 229 | 93×91 | RGBA DDS RGB 32-bit |
| gfx/interface/ideas | 6 | 60×68 | RGBA DDS RGB 32-bit |
| gfx/interface/decisions: decision | 9 | 33×32 | RGBA TGA |
| gfx/interface/decisions: category | 1 | 52×40 | RGBA TGA |
| gfx/event_pictures | 56 | 210×176 | DDS DXT1/BC1 |
| gfx/leaders/VIE: large | 46 | 156×210 | 12 DXT1, 34 RGB 32-bit |
| gfx/leaders/VIE/small | 42 | 38×51 | RGB 32-bit |

Số lượng là ảnh chụp tại thời điểm đối chiếu; canvas là mặc định cho các slot
VIE tương ứng. Không biến số lượng này thành assertion vĩnh viễn.

TGA decision hợp lệ theo đường dẫn sprite hiện có; không đổi sang DDS chỉ vì
bảng cũ ghi “mọi thứ là DDS”. DXT1 ảnh sự kiện đang có không chứng minh engine
chỉ nhận DXT1. Việc đổi codec/kích thước cần giữ consumer và kiểm tra thực tế.

## Những lỗi trong tài liệu cũ cần bỏ

- Idea 64×64, decision 44×44, event 450×150 là ví dụ ở các UI khác,
  không phải profile đã đo của checkout này.
- Portrait 156×210 RGB 32-bit có 131.168 byte, không phải 131.200.
- Số màu độc nhất tăng theo noise và kích thước; không xác minh thẩm mỹ.
- Mean luminance 70–90 hoặc độ lệch chuẩn 50–65 phụ thuộc vùng alpha,
  phương pháp đo và nhóm mẫu; không có ngưỡng phổ quát đã chứng minh.
- 33.980 byte chỉ đúng DDS 93×91 RGB 32-bit không mipmap, không áp dụng DXT.
- Viền alpha 1 px là biện pháp xuất icon của VIE; chưa có kiểm thử chứng minh
  mọi file thiếu viền đều gây shader lỗi hoặc crash.

Quy tắc vận hành: [hệ thống mỹ thuật](07_unified_art_system.md),
[quy trình sản xuất](04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md).

