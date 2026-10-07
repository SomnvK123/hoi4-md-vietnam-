# Tập 1: Nghiên Cứu Phong Cách Hoạt Họa & Kỹ Thuật Hội Họa Trong Vanilla HOI4 và Millennium Dawn

> **Mục tiêu:** Giải phẫu khoa học kỹ thuật lên màu, nghệ thuật ánh sáng, cấu trúc chất cảm và bảng màu tiêu chuẩn trong các icon tiêu điểm (Focus Icons), ý niệm quốc gia (National Spirits / Ideas), quyết sách (Decisions) và tranh sự kiện (Events) của Hearts of Iron IV và bản mod Millennium Dawn; chỉ rõ nguyên nhân vì sao việc vẽ hình học thô sơ (code primitives) bị xem là "xấu quá xấu" và xác lập chuẩn mực mỹ thuật cao cấp cho toàn bộ submod `md_vietnam`.

---

## 1. Giải Phẫu Phong Cách Đồ Họa Paradox Interactive (Vanilla HOI4)

### 1.1 Bản chất phong cách: "Tranh Sơn Dầu Kỹ Thuật Số Giàu Tính Điêu Khắc" (Sculptural Digital Oil)
Các họa sĩ của Paradox Interactive không thiết kế icon như những biểu tượng phẳng (flat icons) hay logo vector tối giản trên web. Mỗi biểu tượng focus trong HOI4 thực chất là một **bức tranh sơn dầu thu nhỏ có kích thước thực tế chỉ $93 \times 91$ hoặc $100 \times 88$ pixel**, nhưng tạo ra ảo giác thị giác của một **phù điêu 3D (3D relief)** hoặc một tác phẩm nghệ thuật hiện thực anh hùng ca (heroic realism).

Các đặc trưng kỹ thuật không thể nhầm lẫn:
1. **Kỹ thuật Non-Metallic Metal (NMM)**:
   - Khi thể hiện kim loại (vàng, đồng thau, thép, bạc), họa sĩ Paradox **không bao giờ dùng một màu vàng phẳng (như `#FFFF00`)** hay dùng các bộ lọc gradient tuyến tính đơn giản.
   - Thay vào đó, họ mô phỏng phản xạ kim loại bằng cọ vẽ: Đặt một mảng màu bóng tối sâu thẳm (nâu cháy/umber đậm) ngay sát cạnh một mảng màu sáng rực (vàng champagne/trắng ngà). Sự chuyển đổi sắc độ đột ngột và dứt khoát này đánh lừa não bộ nhận diện đó là bề mặt kim loại sáng bóng có độ phản quang cao.
2. **Kỹ thuật Chiaroscuro (Tương phản sáng - tối kịch tính)**:
   - **Nguồn sáng chính (Key Light)**: Thường chiếu xiên từ góc trên bên trái ($10:30$ hoặc $11:00$) với góc nghiêng khoảng $45^\circ$, mang nhiệt độ màu ấm áp (Warm Gold / Sunlight).
   - **Bóng đổ môi trường (Ambient Occlusion)**: Các góc khuất, kẽ nứt, dưới chân các chi tiết luôn có các mảng bóng tối rất đậm, tạo chiều sâu như được tạc từ đá hoặc đúc từ kim loại đặc.
   - **Nguồn sáng phản xạ (Rim / Bounce Light)**: Chiếu ngược từ góc dưới bên phải với nhiệt độ màu lạnh (Cool Cyan / Slate Gray / Navy) để tách vật thể ra khỏi nền tối của giao diện game.
3. **Độ mềm của nét cọ (Painterly Brushstrokes)**:
   - Các đường viền không bao giờ là đường vẽ pixel cứng ngắc (aliased hard edges). Mọi đường nét đều có độ chuyển tiếp quang học mềm mại (sub-pixel anti-aliasing) giống như nét cọ lông vuốt nhẹ trên mặt vải toan.

---

## 2. Phong Cách Hoạt Họa Millennium Dawn (MD) – Bước Chuyển Vào Thế Kỷ 21

Nếu như Vanilla HOI4 mang nặng âm hưởng tranh áp phích Thế chiến thứ Hai, thì Millennium Dawn đã nâng tầm phong cách này sang **ngôn ngữ hình ảnh địa chính trị hiện đại thế kỷ 21**:

| Yếu Tố Thị Giác | Vanilla HOI4 (Thế chiến II) | Millennium Dawn (Thế kỷ 21) |
| :--- | :--- | :--- |
| **Vật liệu chủ đạo** | Thép rèn, gỗ mộc, vải bạt thô, giấy công văn ố vàng, huy chương đồng cũ. | Hợp kim titan, kính phản quang, sợi carbon, đá hoa cương đánh bóng, vi mạch silicon, gốm sứ cao cấp, lụa nghi lễ dệt kim tuyến. |
| **Bối cảnh & Vật thể** | Pháo hạng nặng, xe tăng thô ráp, nhà máy ống khói, cờ chiến hào. | Siêu tàu sân bay, tiêm kích tàng hình, màn hình radar quét tọa độ, tháp viễn thông 5G, tòa nhà chọc trời, hội trường LHQ. |
| **Huy hiệu & Phù hiệu** | Khiên hiệp sĩ, đại bàng đế chế, búa liềm công nông đơn sơ. | Huân huy chương tinh xảo, ngôi sao đa giác giác cạnh 3D (faceted 3D stars), dải ruy băng lụa cao cấp, con dấu sáp niêm phong hoàng gia. |
| **Độ bão hòa màu** | Trầm, ám màu đất (earthy), ngả vàng nâu sepia của thời chiến. | Tương phản sắc nét: Nền màu xanh thẫm/navy/xám chì điện ảnh làm nổi bật các sắc đỏ cờ, vàng kim và xanh ngọc bích rực rỡ. |

---

## 3. Phân Tích Định Lượng: Vì Sao Vẽ Bằng Code Hình Học Bị Đánh Giá "Quá Xấu"?

Để hiểu nguyên nhân khoa học của lời phê bình *"xấu quá xấu"*, chúng tôi đã sử dụng các công cụ thị giác phân tích và đo lường trực tiếp các file ảnh trong thư mục game gốc so với các file vẽ bằng hình học tự động:

```
[BẢNG SO SÁNH DỮ LIỆU ĐO LƯỜNG ĐỊNH LƯỢNG]

┌──────────────────────────────────────┬────────────────┬────────────────┬────────────────────────┐
│ Tập Tin Icon                         │ Độ Sáng Trung  │ Độ Tương Phản  │ Số Lượng Màu Sắc       │
│                                      │ Bình (Lumin.)  │ (Std. Dev.)    │ Chuyển Đổi (Unique)    │
├──────────────────────────────────────┼────────────────┼────────────────┼────────────────────────┤
│ 00_organizations/asean_mutual_trade  │ 94.6           │ 68.2           │ 3.726 màu (Rất phong phú)│
│ 00_diplomacy/accept_treaty (MD)      │ 77.8           │ 62.0           │ 3.083 màu (Rất phong phú)│
│ focus_generic_concessions (Vanilla)  │ 81.9           │ 67.4           │ 3.245 màu (Rất phong phú)│
├──────────────────────────────────────┼────────────────┼────────────────┼────────────────────────┤
│ border_settlement (Vẽ code cũ)       │ 114.9 (Quá sáng)│ 74.7           │ 24 màu (CỰC KỲ NGHÈO)  │
│ bamboo_diplomacy (Vẽ code cũ)        │ 125.4 (Quá sáng)│ 81.6           │ 46 màu (CỰC KỲ NGHÈO)  │
└──────────────────────────────────────┴────────────────┴────────────────┴────────────────────────┘
```

### 3 Điểm Tử Huyệt Khiến Icon Cũ Thất Bại:
1. **Thiếu hoàn toàn chuyển sắc (Color Gradient Deficiency)**:
   - Một icon của game chuẩn có **hơn 3.000 màu sắc khác nhau** vì mỗi đường cong đều có hàng trăm sắc thái trung gian chuyển từ sáng sang tối, tạo cảm giác mượt mà, bóng bẩy và sống động.
   - Icon vẽ bằng lệnh hình học chỉ có **24 đến 46 màu phẳng**! Nó giống hệt như một bức tranh tô màu bằng thùng sơn Paint (Paint Bucket Fill) năm 1995: Mảng đỏ phẳng lỳ, mảng xám phẳng lỳ, viền đen sắc cạnh thô lỗ.
2. **Hiện tượng "Cháy sáng & Rợ màu" (Over-saturation & High Luminance)**:
   - Các icon chuẩn có độ sáng trung bình khoảng $70 - 90$, giúp icon hòa nhập tự nhiên vào giao diện kim loại tối màu của Hearts of Iron IV.
   - Icon cũ có độ sáng vọt lên $> 115 - 125$, dùng màu vàng `#FFFF00` chói lọi và màu đỏ cờ nguyên chất không đổ bóng, khiến icon trông như một miếng sticker hoạt hình dán đè lên giao diện nghiêm túc của game.
3. **Mất khối 3D (Lack of Form and Volume)**:
   - Một cột mốc biên giới thật có độ gồ ghề của đá granite, có bóng đổ của góc cạnh, có bụi đất bám dưới chân đế.
   - Icon cũ chỉ là hai hình đa giác xám úp vào nhau tạo thành hình chữ nhật nhạt nhẽo, trông như một thanh xà phòng hoặc viên gạch xám không hồn.

---

## 4. Khoa Học Bảng Màu Chuẩn (Color Science & Palette Architecture)

Để đạt chất lượng hội họa đỉnh cao, mọi chi tiết trên icon phải được xây dựng dựa trên các dải màu chuyển sắc chuyên nghiệp (Professional Gamut):

### 4.1 Bảng màu Vàng Kim / Đồng Thau Hoàng Gia (Royal Gold / Brass Palette)
*Tuyệt đối cấm dùng màu vàng đơn sắc `#FFFF00`.*

```
[BÓNG TỐI SÂU]                  [SẮC ĐỘ CHÍNH]                 [ÁNH SÁNG PHẢN QUANG]
#2D1D08 (Nâu cháy bóng tối) ──> #8B5A00 (Hổ phách đậm) ──> #D4AF37 (Vàng kim hoàng gia) ──> #FFF8DC (Vàng Champagne) ──> #FFFFFF (Điểm lóe sáng)
```
- **Deep Shadow (`#2D1D08`)**: Dùng cho các kẽ lá nguyệt quế, viền dưới chân phù hiệu, rãnh chạm khắc.
- **Midtone (`#D4AF37` / `#C5A059`)**: Chiếm 60% diện tích kim loại, tạo cảm giác vàng đúc nguyên khối.
- **Specular Highlight (`#FFF8DC` / `#FFFFFF`)**: Chỉ chiếm 5% diện tích tại các đỉnh sao, gờ nổi, tạo điểm bắt sáng chói chang.

### 4.2 Bảng màu Đỏ Thắm Quốc Gia & Lụa Nghi Lễ (Crimson National Red Palette)
*Tuyệt đối cấm dùng màu đỏ cờ phẳng không đổ bóng.*

```
[BÓNG ĐỔ SÂU]                   [ĐỎ HUYẾT DỤ]                  [ĐỎ THẮM QUỐC GIA]              [ÁNH CAM VÀNG VIỀN]
#420B0B (Đỏ rượu bóng tối) ──> #7A1414 (Đỏ huyết dụ) ──> #DA251D (Đỏ thắm Quốc kỳ) ──> #FF5722 (Phản quang ấm) ──> #FFD700 (Viền kim tuyến)
```
- **Nền cờ & Quốc huy**: Tâm cờ là sắc đỏ thắm rực rỡ `#DA251D`, nhưng tại các nếp gấp uốn lượn của vải cờ chuyển dần về `#7A1414` và `#420B0B`, trên sống lưng nếp gấp đón sáng ánh lên sắc cam ấm `#FF5722`.

### 4.3 Bảng màu Đá Hoa Cương Biên Cương (Granite & Stone Palette)
- **Granite Highlight (`#F0F2F5`)**: Mặt trước cột mốc đón ánh nắng ban mai.
- **Granite Midtone (`#C8CDD5`)**: Thân đá granite xám sáng có hạt khoáng sản li ti.
- **Granite Shadow (`#78808A`)**: Mặt nghiêng và chân đế cột mốc.
- **Creep Shadow (`#383D45`)**: Đường rãnh phân giới và khe chân bệ đá.

### 4.4 Bảng màu Nước Sông Mê Kông & Biển Khơi (Hydrological Emerald & Ocean Navy)
- **Deep Navy (`#122A4A`)**: Vùng nước sâu Vịnh Bắc Bộ và Thái Bình Dương.
- **Emerald Cyan (`#1E8276` / `#48C9B0`)**: Dòng chảy sông Mê Kông phù sa màu ngọc bích.
- **Foam Highlight (`#D4F6FF`)**: Bọt sóng trắng xóa chân đập thủy điện và mũi tàu tuần tra rẽ sóng.

### 4.5 Bảng màu Quân Sự & Thép Khí Tài (VPA Military Olive & Armored Steel Palette)
- **Rêu quân phục QĐNDVN (`#2E4A2E` / `#3D5A3D`)**: Màu áo lính và ngụy trang rừng nhiệt đới.
- **Thép giáp nòng pháo (`#1A202C` ──> `#4A5568` ──> `#CBD5E0`)**: Thân xe tăng T-90, nòng pháo và tiêm kích Su-30.
- **Lửa đạn pháo / Động cơ phản lực (`#FF4500` ──> `#FFD700`)**: Điểm bắt lửa phản lực và luồng phóng tên lửa.

### 4.6 Bảng màu Công Nghiệp Đổi Mới & Vi Mạch (High-Tech Silicon & Industrial Palette)
- **Cam công nghiệp & Hạ tầng (`#D35400` / `#E67E22`)**: Cần cẩu bến cảng, máy móc công trường cao tốc.
- **Xanh lục tăng trưởng (`#27AE60` / `#2ECC71`)**: Kinh tế xanh, chuyển dịch năng lượng tái tạo.
- **Giao thoa quang học Silicon Wafer (`#5DADE2`, `#AF7AC5`, `#58D68D`, `#F4D03F`)**: Bảy sắc cầu vồng của vi mạch bán dẫn.

### 4.7 Bảng màu An Ninh Trật Tự & An Ninh Mạng (Security Shield & Cyber Neon Palette)
- **Đỏ thẫm Công an (`#78281F` / `#900C3F`)**: Khiên an ninh trật tự, bìa hồ sơ tư pháp.
- **Vàng đồng Công an hiệu (`#B7950B` / `#D4AF37`)**: Phù hiệu CAND đúc nổi trên khiên thép.
- **Xanh Neon Không gian mạng (`#00FFFF` / `#0080FF`)**: Luồng dữ liệu số, an ninh mạng và tường lửa quốc gia.

---

## 5. Quy Chuẩn Bố Cục Không Gian 3D (Z-Depth Layer Hierarchy)

Mỗi icon tiêu điểm phải được cấu trúc thành **6 lớp không gian có chiều sâu phân cấp rõ rệt**:

```text
[LỚP 6] VIỀN BẢO VỆ ALPHA (1px viền ngoài cùng luôn có Alpha = 0 chống xước giao diện)
  │
[LỚP 5] ĐIỂM SÁNG TỐI CAO (Crowning Highlight: Ngôi sao vàng 3D, ánh nắng ban mai, tia chớp)
  │
[LỚP 4] CHI TIẾT CÂU CHUYỆN (Storytelling Foreground: Cờ bay, triện son, compa, thước ngắm, barie)
  │
[LỚP 3] HÌNH TƯỢNG TRUNG TÂM (Iconic Centerpiece: Tháp đá Angkor, Cổng Hữu Nghị, Khóm tre, Tàu sân bay)
  │
[LỚP 2] KHUNG NỀN HUÂN CHƯƠNG (Framing Element: Vòng nguyệt quế vàng, khiên thép, dải lụa danh dự)
  │
[LỚP 1] BẦU KHÔNG KHÍ HẬU CẢNH (Atmospheric Backdrop: Sương mù Trường Sơn, biển xanh, bầu trời rực rỡ)
  │
[LỚP 0] BÓNG ĐỔ MÔI TRƯỜNG (Ambient Occlusion Drop Shadow: Gaussian Blur R=1.8, Opacity 75%)
```

Nhờ cấu trúc 6 lớp này, khi nhìn ở bất kỳ kích thước nào trong cây focus tree của Hearts of Iron IV, icon sẽ luôn nổi bật, có chiều sâu không gian ba chiều mạnh mẽ và không bao giờ bị chìm vào nền xám của giao diện game.

---

*Chuyển sang đọc [Tập 2: Ngôn Ngữ Thị Giác Tranh Cổ Động & Biểu Trưng Việt Nam](./02_vietnamese_propaganda_and_symbolic_art.md) để khảo cứu kho tàng biểu tượng văn hóa và đối ngoại nước nhà.*
