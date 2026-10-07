# Tập 5: Khảo Cứu Giải Phẫu Khung (Focus Frames) & Kỹ Thuật Đóng Khung Huy Hiệu Paradox

> **Mục tiêu:** Nghiên cứu chuyên sâu giải phẫu cấu trúc khung (Focus Frame Anatomy) của Hearts of Iron IV và Millennium Dawn; phân tích vì sao biểu tượng focus bắt buộc phải có khung huy hiệu (heraldic badge) và vùng nền trong suốt (Alpha = 0); từ đó thiết lập bộ quy chuẩn thiết kế và giải pháp đóng khung mỹ thuật cho toàn bộ các nhánh của mod `md_vietnam`.

---

## 1. Bản Chất Của Biểu Tượng Focus: Huy Hiệu Nổi Khối, Không Phải Khối Vuông Đặc

Một trong những sai lầm phổ biến nhất khi vẽ icon cho HOI4 là coi canvas $93 \times 91$ pixel như một "khung tranh vuông" (square photo canvas) và vẽ kín mít từ góc này sang góc kia. 

Trên thực tế, trong engine Clausewitz của Paradox Interactive:
* **Background luôn là nền trong suốt (Alpha = 0)**: Icon chỉ chiếm khoảng $50\% - 65\%$ diện tích canvas, để lộ khoảng trống xung quanh.
* **Hình thức là một Phù Hiệu / Huân Chương Nổi Khối 3D (Sculpted Heraldic Badge)**: Icon được "treo" nổi bồng bềnh trên cây Focus Tree, hòa nhập hoàn hảo với các đường kẻ nhánh nối (`prerequisite lines`) và hiệu ứng quét sáng (`goal_shine_strip`).
* **Khung (Frame) đóng vai trò định hình đẳng cấp và phân loại nhánh**: Khung là ranh giới thị giác tách biệt giữa vật thể trung tâm và nền giao diện xám xịt của game, đồng thời tôn vinh tính trang trọng, quyền uy của quyết sách quốc gia.

```text
┌────────────────────────────────────────────────────────┐
│  SO SÁNH CẤU TRÚC: TRANH VUÔNG ĐẶC vs HUY HIỆU CÓ KHUNG │
├────────────────────────────┬───────────────────────────┤
│    TRANH VUÔNG ĐẶC (CŨ)    │   HUY HIỆU CÓ KHUNG (CHUẨN)│
├────────────────────────────┼───────────────────────────┤
│ - Kín đặc 100% ô 93x91     │ - Nền ngoài trong suốt 100% │
│ - Cảm giác dẹt, hình hộp   │ - Nổi khối 3D (Drop Shadow)│
│ - Che khuất đường nối cây  │ - Không che đường nối     │
│ - Thiếu tính tôn nghiêm    │ - Đẳng cấp huân huy chương│
│ - Shader quét sáng bị méo  │ - Shader quét sáng lấp lánh│
└────────────────────────────┴───────────────────────────┘
```

---

## 2. Giải Phẫu Học Cấu Trúc Khung Focus (Focus Frame Anatomy)

Một khung Focus chuẩn mực của Paradox/MD được cấu thành từ **5 thành phần giải phẫu kinh điển**:

```text
                           [1. ĐỈNH KHUNG / VƯƠNG MIỆN]
                           (Crown: 3 Ngôi Sao Vàng / Ngọn Lửa)
                                        │
           ┌────────────────────────────┼────────────────────────────┐
           ▼                                                         ▼
[4. TIA HÀO QUANG]                                            [4. TIA HÀO QUANG]
(Sunburst Rays:                                               (Sunburst Rays:
 16 tia kim cương tỏa)                                         16 tia kim cương tỏa)
           │          ┌───────────────────────────┐                  │
           │          │ 2. VÀNH KHUNG CHÍNH       │                  │
           ├─────────►│ (Main Wreath / Laurel)    │◄─────────────────┤
           │          │ Vòng nguyệt quế / Bông lúa│                  │
           │          └─────────────┬─────────────┘                  │
           │                        │                                │
           │          ┌─────────────▼─────────────┐                  │
           │          │ 5. GỜ VIỀN TRONG LÒNG KHUNG│                 │
           │          │ (Inner Bezel / Rim)       │                  │
           │          │ Nâng đỡ Centerpiece       │                  │
           │          └─────────────┬─────────────┘                  │
           │                        │                                │
           └────────────────────────┼────────────────────────────────┘
                                    │
                        [3. CHÂN KHUNG / ĐẾ HUY HIỆU]
                        (Pedestal: Huy Hiệu Sao Đỏ / Dải Lụa Nơ)
```

### 2.1 Đỉnh Khung / Vương Miện (The Crown / Crest)
* **Vị trí:** Tọa độ đỉnh ($y = 2 \dots 14$), nằm chính giữa trục đối xứng.
* **Chi tiết biểu trưng:**
  - Nhánh Nhà nước & Độc lập: **3 ngôi sao vàng năm cánh mạ vàng NMM** (ngôi sao giữa lớn nhất, hai bên nhỏ hơn), tượng trưng cho chủ quyền tối cao.
  - Nhánh Đảng & Lý tưởng: **Biểu tượng Búa Liềm** hoặc **Ngọn đuốc cách mạng**.
  - Nhánh Quốc phòng: **Ngôi sao đỏ viền vàng** hoặc **Đại bàng/Mũi giáo**.

### 2.2 Vành Khung Ôm Hai Bên (The Flanking Wreath / Mantle)
* **Vị trí:** Uốn cong hình bầu dục/elip hai bên sườn trái và phải ($x = 4 \dots 88, y = 14 \dots 78$).
* **Chi tiết biểu trưng:**
  - **Vòng Nguyệt Quế Vàng (Golden Laurel Wreath):** 10 – 12 cặp lá nguyệt quế xếp lớp chồng lên nhau, gân lá có điểm bắt sáng vàng champagne, bóng rãnh đổ màu nâu umber sâu thẳm.
  - **Bông Lúa Vàng Dân Tộc (Golden Rice Sheaf):** Các hạt lúa chín mẩy uốn cong mềm mại ôm trọn tranh tròn, tượng trưng cho nền văn minh lúa nước và ấm no.
  - **Vành Khung Bánh Răng (Industrial Cogwheel):** Các răng cưa kim loại mạ crôm/thép cho nhánh công nghiệp.

### 2.3 Chân Khung / Đế Đỡ (The Base Pedestal / Medallion)
* **Vị trí:** Tọa độ đáy ($y = 74 \dots 88$).
* **Chi tiết biểu trưng:**
  - **Huy hiệu Sao Đỏ Viền Vàng (Red-Gold Star Badge):** Một khối đa giác hoặc tròn màu đỏ thắm `#DA251D` có ngôi sao vàng dập nổi ở giữa, viền nẹp vàng sáng bóng.
  - **Nơ Lụa Danh Dự (Honor Ribbon Knot):** Dải lụa đỏ uốn lượn thắt nút ở đáy và xòe ra hai bên sườn.
  - **Tấm Bia Kim Loại Khắc Chữ (Plaque / Banner):** Tấm đồng khắc niên hiệu hoặc khẩu hiệu (như "1930 - 2030" hay "VIET NAM").

### 2.4 Tia Hào Quang Phát Quang (Radial Sunburst / Spark Rays)
* **Vị trí:** Phân bổ đối xứng xung quanh vành ngoài của vòng nguyệt quế ($8 - 16$ tia sáng).
* **Hình dáng:** Các hạt sáng hình thoi (rhombus sparks) màu vàng kim nhạt rực rỡ, tỏa tia từ tâm ra ngoài, tạo hiệu ứng phát quang linh thiêng.

### 2.5 Gờ Viền Trong Lòng Khung (Inner Bezel / Inset Ring)
* **Chức năng:** Là "mặt gương" kim loại mạ vàng hình tròn hoặc hình khiên có độ dày $2 - 3\text{ px}$.
* Mặt gờ này có rãnh bóng tối tiếp xúc (Ambient Occlusion Shadow) đổ vào bên trong, tạo cảm giác bức tranh trung tâm (Centerpiece) nằm lọt thỏm sâu bên trong mặt kính pha lê bảo vệ.

---

## 3. Bảng Phân Loại 5 Họ Khung Chuẩn Theo Từng Nhánh Mod Việt Nam

Không được dùng duy nhất 1 kiểu khung cho tất cả các nhánh để tránh nhàm chán. Mỗi trụ cột của mod sở hữu một họ khung đặc trưng:

| Họ Khung (Frame Family) | Nhánh Áp Dụng | Cấu Trúc Khung | Chất Liệu & Màu Sắc |
| :--- | :--- | :--- | :--- |
| **1. Khung Ngoại Giao & Hòa Bình (Diplomatic Wreath)** | Ngoại giao, ASEAN, Quốc tế, Hợp tác đa phương. | Vòng nguyệt quế/bông lúa vàng tròn ôm quanh, đỉnh có 3 sao vàng, đáy có huy hiệu sao đỏ. | Vàng ròng NMM (`#D4AF37`), dải lụa đỏ thắm (`#DA251D`), ngọc bích. |
| **2. Khung Chính Trị & Tư Tưởng (State & Party Crest)** | Xây dựng Đảng, Hiến pháp, Quốc hội, Tư pháp. | Khung tròn sơn mài dày nẹp chỉ vàng, đỉnh là Búa Liềm hoặc Quốc huy, đáy là bục đỏ. | Đỏ sơn mài hoàng cung (`#800020`), nhũ vàng thư pháp, đồng đỏ. |
| **3. Khung Quốc Phòng & Quân Sự (Military Shield Frame)** | Hiện đại hóa QĐNDVN, Lục quân, PK-KQ, Hải quân. | Khiên sắt góc cạnh, hai thanh kiếm hoặc nòng súng bắt chéo phía sau, đỉnh là Quân hiệu QĐNDVN. | Thép tôi luyện xám chì (`#34495E`), đồng thau, viền vàng kim tuyến. |
| **4. Khung Công Nghiệp & Đổi Mới (Tech & Industrial Cog)** | Công nghiệp, Năng lượng, Bán dẫn, Hạ tầng, Viễn thông. | Nửa vành bánh răng công nghiệp đan xen nửa vành bông lúa, viền mạch điện tử nano. | Thép crôm bóng loáng, đồng đỏ, vệt sáng xanh neon (`#00FFFF`). |
| **5. Khung Biển Đảo & Chủ Quyền (Maritime Naval Ring)** | Biển Đông, Luật biển, Trường Sa, Hoàng Sa, DK1. | Vành phao tròn hàng hải quấn dây thừng đồng thau, mỏ neo phía đáy, sóng biển ôm chân. | Đồng thau hải quân phong sương (`#B8860B`), xanh thẳm đại dương (`#0B2545`). |

---

## 4. Quy Trình Kỹ Thuật: Đóng Khung Centerpiece Chuẩn 3D

Để đưa một bức tranh trung tâm (Centerpiece vẽ sơn dầu chất lượng cao) vào khung chuẩn game:

```text
[BƯỚC 1]                   [BƯỚC 2]                   [BƯỚC 3]                   [BƯỚC 4]
Tranh Centerpiece        Cắt Mask Hình Tròn         Ghép Khung Huân Chương      Đổ Bóng Ambient Shadow
(Độ phân giải cao)   ──► Bằng Mặt Nạ Alpha      ──► Lên Phía Trên           ──► Ra Nền Trong Suốt
                                (Radius = 31px)             (Outer Laurel Wreath)       (Xuất DDS 33.980 bytes)
```

### 4.1 Chi tiết từng bước kỹ thuật
1. **Bước 1: Chuẩn bị Inset Artwork**:
   - Tranh trung tâm được vẽ ở tỷ lệ $1:1$ vuông vức với đầy đủ chi tiết chất lượng cao.
   - Thu nhỏ về kích thước lòng khung (đường kính khoảng $58 - 64\text{ px}$, tâm đặt tại $x = 46.5, y = 43$).
2. **Bước 2: Cắt mặt nạ tròn mềm (Anti-aliased Circular Inset Mask)**:
   - Sử dụng mặt nạ hình tròn có bán kính $r \approx 30.5\text{ px}$ với cạnh viền được khử răng cưa siêu mịn (smooth sub-pixel blend).
3. **Bước 3: Áp lớp Khung Huân Chương 3D (Gold Laurel Frame Overlay)**:
   - Lớp vành khung kim loại mạ vàng NMM, 3 sao trên đỉnh, dải nguyệt quế và huy hiệu sao đỏ ở chân được ép đè lên trên (Alpha Composite).
   - Khung sẽ che phủ phần viền ngoài của tranh tròn, tạo gờ kim loại nổi khối bảo vệ tranh.
4. **Bước 4: Tạo bóng đổ tiếp xúc môi trường (Ambient Occlusion Drop Shadow)**:
   - Tách kênh Alpha của toàn bộ tổ hợp (khung + tranh).
   - Đổ bóng màu đen nâu nhân tính (Gaussian Blur $R = 1.8$, độ mờ $75\%$, dịch chuyển xuống dưới $1\text{ px}$).
   - Nền bên ngoài bóng đổ giữ giá trị **Alpha = 0 hoàn toàn**.
5. **Bước 5: Xuất DDS 32-bit BGRA**:
   - Đảm bảo đúng $93 \times 91$ pixel, đúng $33.980$ bytes, 1px alpha border sạch sẽ.

---

## 5. Kết Luận & Hành Động Tiếp Theo

Khung Focus không chỉ là một phụ kiện trang trí, mà là **linh hồn cấu trúc của nghệ thuật giao diện Hearts of Iron IV**. Việc bổ sung khung huân chương chuẩn Paradox sẽ giải quyết triệt để vấn đề:
1. Chuyển hóa các bức tranh tròn từ dạng "ảnh cắt dán" thành **các huân chương phù hiệu 3D kiêu hãnh**.
2. Tạo độ trong suốt tự nhiên quanh viền icon, giúp hiển thị ăn khớp với cây Focus Tree và hiệu ứng quét sáng (`shine`).
3. Đưa chất lượng đồ họa của mod Việt Nam tiệm cận và vượt qua các bản mod hàng đầu thế giới.

---

*Cập nhật ngay quy trình kỹ thuật này vào script biên dịch `tools/process_focus_batch.py` để đóng khung cho toàn bộ các icon.*
