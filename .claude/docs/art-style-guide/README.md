# Quy Chuẩn Mỹ Thuật, Phong Cách Hoạt Họa & Thiết Kế Đồ Họa Toàn Diện Submod Millennium Dawn Vietnam

> **Phiên bản:** 2.0 — Chuẩn Hóa Toàn Diện Submod (Tháng 10/2026)  
> **Phạm vi áp dụng:** Toàn bộ hệ thống đồ họa của Mod `md_vietnam`: National Focus Goal Icons (toàn bộ các nhánh), National Spirits / Ideas, Decisions, Events Pictures, Leader Portraits và GFX giao diện.  
> **Tài liệu tham chiếu:** [VIE_focus_coding_standards.md](../../../VIE_focus_coding_standards.md), [VIE_diplomacy_spine_horizontal_architecture.md](../../../VIE_diplomacy_spine_horizontal_architecture.md), [Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](../../../Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md), [CLAUDE.md](../../CLAUDE.md).

---

## 📌 Mục Lục Chỉ Dẫn Hệ Thống Tài Liệu (Master Index)

Bộ hồ sơ nghiên cứu và thiết kế mỹ thuật được phân bổ thành 4 tập chuyên khảo toàn diện, đóng vai trò là "Kinh thánh Mỹ thuật" (Art Bible) định hướng cho mọi nghệ sĩ và nhà phát triển:

| Tập Tài Liệu | Nội Dung Trọng Tâm & Phạm Vi Phủ | Liên Kết Trực Tiếp |
| :--- | :--- | :--- |
| **Tập 1: Phân Tích Phong Cách Hoạt Họa Game Gốc** | Khảo cứu kỹ thuật hội họa sơn dầu kỹ thuật số (painterly digital oil), ánh sáng kịch tính Chiaroscuro 3 nguồn sáng, chất cảm vật liệu kim loại phi ảnh thực (NMM), giải phẫu bảng màu Paradox/MD. Phân tích định lượng: game chuẩn sở hữu **3.000 – 4.200 màu sắc**, chứng minh vì sao vẽ phẳng 24 màu vector bị loại bỏ. | [01_hoi4_md_art_style_analysis.md](./01_hoi4_md_art_style_analysis.md) |
| **Tập 2: Ngôn Ngữ Thị Giác Tranh Cổ Động & Hệ Biểu Trưng Việt Nam** | Khảo cứu mỹ thuật tranh cổ động chính luận cách mạng, quy chuẩn thiêng liêng tuyệt đối cho Quốc kỳ Cờ Đỏ Sao Vàng, Đảng kỳ Búa Liềm, Quân kỳ Quyết Thắng, Công an hiệu, biểu trưng công nông binh, văn hóa lúa nước, hoa sen, chim bồ câu, cây tre, bánh răng công nghiệp và vi mạch chuyển đổi số. | [02_vietnamese_propaganda_and_symbolic_art.md](./02_vietnamese_propaganda_and_symbolic_art.md) |
| **Tập 3: Ý Tưởng Thiết Kế Mỹ Thuật Chi Tiết Các Nhánh Focus** | Khung ngôn ngữ tạo hình cho 6 trụ cột của submod: (1) Chính trị & Xây dựng Đảng, (2) Kinh tế & Đổi Mới, (3) Quốc phòng & Quân đội, (4) An ninh & Nội chính, (5) Biển Đông & Hải đảo, (6) Ngoại giao & Hội nhập Quốc tế. Kèm theo Đề án Concept Art Blueprint chi tiết mẫu mực cho 34 Focus Ngoại giao. | [03_concept_thiet_ke_icon_cac_nhanh.md](./03_concept_thiet_ke_icon_cac_nhanh.md) |
| **Tập 4: Giải Pháp Công Nghệ & Quy Trình Sản Xuất Mỹ Thuật AAA** | Quy trình sản xuất 6 bước chuẩn công nghiệp (Value Sketch, Asset Base, Digital Painting, 6-Layer Engine Depth, Noise Dithering, DDS Compilation 32-bit BGRA uncompressed 33.980 bytes). Quy chuẩn kích thước và thông số cho Goals, Ideas, Decisions, Events, Portraits và bảng tiêu chí kiểm định QA. | [04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md](./04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md) |
| **Tập 5: Khảo Cứu Giải Phẫu Khung (Focus Frames) & Kỹ Thuật Đóng Khung** | Khảo cứu chuyên sâu cấu trúc 5 thành phần của khung Focus HOI4/MD (Đỉnh 3 sao, vành nguyệt quế/bông lúa NMM, đế huy hiệu sao đỏ, tia phát quang, gờ viền trong). Bảng phân loại 5 họ khung theo từng nhánh và kỹ thuật cắt mask tròn lồng khung trên nền trong suốt. | [05_nghien_cuu_va_thiet_ke_khung_focus.md](./05_nghien_cuu_va_thiet_ke_khung_focus.md) |

---

## 1. Triết Lý Mỹ Thuật Toàn Diện Của Submod (Artistic Vision)

Submod `md_vietnam` tái hiện lịch sử hiện đại của Việt Nam từ năm 2000 đến nay và tương lai 2030+. Mỹ thuật của submod không đơn thuần là hình ảnh minh họa cho gameplay, mà phải là **một bảo tàng trực quan sống động**, kết tinh giữa:
1. **Chất Thép Cách Mạng & Hồn Cốt Dân Tộc**: Khí phách kiên cường, hào hùng của tranh cổ động Việt Nam, thấm đượm truyền thống lịch sử ngàn năm dựng nước và giữ nước.
2. **Khát Vọng Vươn Mình Của Đất Nước Đổi Mới**: Hình tượng công nghiệp hóa, hiện đại hóa, công nghệ cao, thành phố thông minh, chuyển đổi số và vị thế quốc tế ngày càng nâng cao.
3. **Chuẩn Mực Đồ Họa Cao Cấp (AAA) Của Paradox & Millennium Dawn**: Chiều sâu thị giác 3D, ánh sáng điện ảnh, chất cảm sơn dầu kỹ thuật số dày dặn, tương phản sắc sảo, hoàn toàn đoạn tuyệt với phong cách vẽ clip-art phẳng, đục và thô sơ.

---

## 2. Bản Đồ 6 Trụ Cột Đồ Họa Của Cây Focus Tree Toàn Mod

Mọi icon trong cây Focus Tree của Việt Nam đều phải tuân thủ nghiêm ngặt ngôn ngữ thị giác riêng biệt của từng nhánh:

```text
                               CÂY MỤC TIÊU QUỐC GIA VIỆT NAM (VIE)
                                                 │
        ┌───────────────────┬────────────────────┼───────────────────┬───────────────────┐
     NHÁNH 1             NHÁNH 2              NHÁNH 3             NHÁNH 4             NHÁNH 5 & 6
  CHÍNH TRỊ & ĐẢNG     KINH TẾ ĐỔI MỚI      QUỐC PHÒNG & QĐ     AN NINH NỘI CHÍNH   NGOẠI GIAO & BIỂN ĐÔNG
  - Sắc đỏ - vàng son  - Cam công nghiệp    - Xanh rêu lính     - Đỏ thẫm khiên     - Xanh lam ngọc bích
  - Búa liềm mạ vàng   - Vàng lúa & tiền tệ - Thép xám vũ khí   - Thanh kiếm thép   - La bàn thiên văn
  - Trống đồng, đài sen- Kính cao ốc, chip  - Quân kỳ Quyết thắng- Khiên chắn radar  - Cột mốc & Tre ngà
```

### 2.1 Nhánh 1: Chính trị, Tư tưởng & Xây dựng Đảng (`VIE_congress_*`, `VIE_party_*`)
* **Tông màu chủ đạo:** Đỏ cờ thắm (`#DA251D`), đỏ son hoàng cung (`#800020`), vàng kim NMM (`#FFD700`, `#C5A059`).
* **Vật liệu & Biểu tượng:** Búa Liềm vàng rực nổi khối 3D; hoa văn Trống đồng Đông Sơn; bục tượng Bác Hồ bằng đồng đỏ; Quốc huy và Hiến pháp bìa da dập nổi chữ vàng; ngọn đuốc lý tưởng cách mạng soi đường.
* **Cảm xúc thị giác:** Trang nghiêm, thiêng liêng, kiên định, kỷ cương, mang tầm vóc lịch sử của Đảng Cộng sản Việt Nam.

### 2.2 Nhánh 2: Kinh tế & Đổi Mới Toàn Diện (`VIE_doi_moi_*`, `VIE_industry_*`, `VIE_energy_*`)
* **Tông màu chủ đạo:** Vàng lúa chín (`#FFCC00`), cam công nghiệp (`#E67E22`), xanh lục tăng trưởng xanh (`#27AE60`), xanh kính cao ốc (`#2980B9`).
* **Vật liệu & Biểu tượng:** Bánh răng công nghiệp mạ crôm; tấm wafer silicon bán dẫn 7 sắc cầu vồng; cánh đồng lúa trĩu hạt; đập thủy điện hùng vĩ; tuabin điện gió ngoài khơi; đường cao tốc Bắc - Nam và tuyến metro hiện đại.
* **Cảm xúc thị giác:** Năng động, bứt phá, trù phú, công nghệ cao, phản ánh sức sống mãnh liệt của nền kinh tế thị trường định hướng XHCN.

### 2.3 Nhánh 3: Quốc phòng & Hiện Đại Hóa Quân Đội (`VIE_modernize_vpa`, `VIE_army_*`, `VIE_navy_*`, `VIE_air_*`)
* **Tông màu chủ đạo:** Xanh ô liu / rêu quân phục (`#3D5A3D`), xám thép chiến hạm (`#34495E`), xanh da trời PK-KQ (`#1A5276`), đỏ sao vàng Quân kỳ (`#DA251D`).
* **Vật liệu & Biểu tượng:** Thép súng giáp tôi luyện; nòng pháo tăng T-90S; cánh tiêm kích Su-30MK2 rẽ mây; mũi tàu hộ vệ tên lửa Gepard và tàu ngầm Kilo 636 rẽ sóng ngầm; bệ phóng tên lửa bờ Bastion-P; Quân kỳ thêu chữ vàng "Quyết Thắng".
* **Cảm xúc thị giác:** Đanh thép, kỷ luật, quả cảm, tinh nhuệ, hiện đại, sẵn sàng đập tan mọi kẻ thù xâm phạm bờ cõi.

### 2.4 Nhánh 4: An ninh Quốc gia & Nội Chính (`VIE_sec_*`, `VIE_security_*`)
* **Tông màu chủ đạo:** Đỏ thẫm công an (`#900C3F`), vàng đồng Công an hiệu (`#D4AF37`), xanh điện tử không gian mạng (`#00FFFF`, `#0066CC`).
* **Vật liệu & Biểu tượng:** Thanh kiếm thép công lý và chiếc khiên đồng bảo vệ trật tự an toàn xã hội; Công an hiệu gắn trên mũ kê-pi trang nghiêm; lưới dữ liệu số quốc gia (VNeID/Big Data) bảo mật an ninh mạng; dấu sáp đỏ pháp luật.
* **Cảm xúc thị giác:** Thép gai, sắc bén, vững chãi, trung thành vô hạn với Tổ quốc, bảo vệ cuộc sống bình yên của nhân dân.

### 2.5 Nhánh 5: Ngoại giao Đa phương & Cây Tre Việt Nam (`VIE_asean_integration`, 5 trục đối ngoại)
* **Tông màu chủ đạo:** Xanh lam hòa bình ngọc bích (`#0B2545`, `#003399`), vàng kim bang giao (`#FFD700`), xanh ngọc tre ngà (`#1E8449`).
* **Vật liệu & Biểu tượng:** La bàn thiên văn bằng vàng; bó lúa 10 dải ASEAN; cột mốc biên cương đá granite; bắt tay hòa giải vượt đại dương; bồ câu trắng ngậm cành tre; quả địa cầu pha lê đối tác chiến lược toàn diện; khóm tre ngà hiên ngang trước bão tố.
* **Cảm xúc thị giác:** Hòa hiếu, tinh tế, đa phương hóa, bản lĩnh kiên cường, dẻo dai, "gốc vững, thân chắc, cành uyển chuyển".

### 2.6 Nhánh 6: Biển Đông & Chủ Quyền Biển Đảo (`VIE_law_of_the_sea`, `VIE_scs_*`)
* **Tông màu chủ đạo:** Xanh thẳm đại dương (`#0B2545`), xanh ngọc san hô (`#16A085`), trắng bọt sóng biển (`#F0F8FF`), vàng đèn hải đăng (`#FFAA00`).
* **Vật liệu & Biểu tượng:** Nhà giàn DK1 sừng sững giữa ngàn trùng sóng gió; ngọn hải đăng Trường Sa quét sáng đêm đen; tàu tuần tra Cảnh sát biển & Kiểm ngư mang Cờ đỏ sao vàng rẽ sóng; cột mốc chủ quyền Trường Sa / Hoàng Sa khắc đá san hô.
* **Cảm xúc thị giác:** Kiên cường, bất khuất, linh thiêng, giữ trọn từng tấc biển thiêng liêng của Tổ quốc.

---

## 3. Hệ Sinh Thái Đồ Họa Phụ Trợ (Supporting GFX Ecosystem)

Chuẩn mỹ thuật này áp dụng đồng bộ cho toàn bộ hệ thống tài nguyên đồ họa của submod:

| Loại Tài Nguyên | Kích Thước Pixel | Định Dạng File Chuẩn | Đặc Tính Mỹ Thuật |
| :--- | :---: | :---: | :--- |
| **National Focus Icons** | $93 \times 91$ px | 32-bit BGRA DDS ($33.980$ bytes) | Đầy đủ 6 lớp chiều sâu, Chiaroscuro 3 nguồn sáng, NMM kim loại, viền alpha 1px sạch. |
| **National Spirits / Ideas** | $64 \times 64$ px | 32-bit BGRA DDS ($16.512$ bytes) | Biểu tượng cô đọng (emblematic), mảng miếng khúc chiết, tương phản cực mạnh để đọc rõ ở kích thước nhỏ. |
| **Decision / Category Icons** | $44 \times 44$ hoặc $64 \times 64$ px | 32-bit BGRA DDS | Tối giản, hình tượng đường viền phát quang vàng mỏng, nhận diện nhanh chức năng gameplay. |
| **Event Pictures** | $450 \times 150$ hoặc $500 \times 200$ px | DXT5 hoặc 32-bit BGRA DDS | Bức tranh điện ảnh phong cảnh hoặc sự kiện lịch sử, ánh sáng kịch tính, chân thực và xúc động. |
| **Leader Portraits** | $156 \times 210$ px | 32-bit BGRA DDS ($131.200$ bytes) | Chân dung hội họa tả thực phong cách Paradox (oil painting portrait), thần thái cương nghị, ánh sáng studio lịch sử. |

---

## 4. Tóm Tắt Quy Chuẩn Bắt Buộc (Hard Rules)

1. **Tuyệt đối cấm dùng hình học phẳng thô sơ (No Flat Clip-Art)**: Mọi icon phải có cọ chuyển sắc sơn dầu, đổ bóng tiếp xúc (AO), ánh sáng viền (Rim Light), đạt tối thiểu **$\ge 2.500$ màu sắc**.
2. **Tuyệt đối trung thực với Quốc kỳ, Đảng kỳ và Quân kỳ**:
   - Quốc kỳ: Nền đỏ `#DA251D`, sao vàng 5 cánh `#FFDE23` (đỉnh sao chỉ góc $90^\circ$ thẳng đứng), tỷ lệ $2:3$, hiệu ứng sóng vải 3D tự nhiên. Không bao giờ dùng cờ có sọc ngang sai quy chuẩn.
   - Đảng kỳ: Búa thép đan Liềm lúa màu vàng kim trên nền đỏ thắm.
   - Quân kỳ: Cờ đỏ sao vàng có dòng chữ thêu "Quyết Thắng" bằng chỉ vàng viền góc trên bên trái.
3. **Tuyệt đối cấm bố cục rập khuôn (No Cookie-Cutter)**: Không dùng đi dùng lại mẫu "2 lá cờ chéo + vòng nguyệt quế tròn". Mỗi icon phải có một vật thể trung tâm (centerpiece) độc bản mang câu chuyện lịch sử riêng.
4. **Chuẩn kỹ thuật file DDS**: Luôn xuất đúng chuẩn 32-bit BGRA uncompressed với viền Alpha 1px trong suốt bao quanh để tránh lỗi tràn viền shader trong game.

---

*Bắt đầu nghiên cứu kỹ thuật từ [Tập 1: Phân Tích Phong Cách Hoạt Họa Game Gốc](./01_hoi4_md_art_style_analysis.md).*
