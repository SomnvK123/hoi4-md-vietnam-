# Tập 3: Ý Tưởng Thiết Kế Mỹ Thuật Chi Tiết Cho Các Nhánh Focus

> Trạng thái: thư viện concept, không là dữ liệu gameplay live hoặc quy định engine.
> Tọa độ, năm và số lượng focus phải kiểm lại trong code; vật thể/camera/khung là
> phương án để thử, không bắt buộc cho idea, decision, event hoặc portrait.
> Những ngưỡng màu/layer và tuyên bố “AAA” bên dưới không là tiêu chí nghiệm thu.
> Áp dụng [hệ thống mỹ thuật hiện hành](07_unified_art_system.md) và
> [profile kỹ thuật đã đo](04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md).

> **Mục tiêu:** Xây dựng khung hướng dẫn tạo hình (concept art blueprint) độc bản và nhất quán cho toàn bộ các nhánh trong cây mục tiêu quốc gia Việt Nam; kết hợp bộ hồ sơ chi tiết mẫu mực cho 34 tiêu điểm nhánh Ngoại giao Cây tre & Quốc tế (`VIE_asean_integration` subtree) làm chuẩn mực tiên phong cho toàn submod `md_vietnam`.  
> **Quy chuẩn mỹ thuật:** Tuyệt đối xóa bỏ mô-típ rập khuôn (hai cờ bắt chéo + vòng nguyệt quế + huy hiệu dẹt). Mỗi focus là một bức họa kỹ thuật số 3D thu nhỏ mang ngôn ngữ điện ảnh, chất cảm sơn dầu Paradox/MD, ánh sáng kịch tính Chiaroscuro và biểu tượng chính trị - lịch sử sâu sắc.

---

## 📌 PHẦN I: KHUNG NGÔN NGỮ TẠO HÌNH 6 TRỤ CỘT FOCUS TREE TOÀN MOD

Để bảo đảm tính nhận diện thống nhất và tính mỹ cảm cao cấp, mỗi trụ cột trong cây Focus Tree sở hữu một bộ nhận diện hình ảnh riêng biệt:

### 1. Trụ Cột Chính Trị & Xây Dựng Đảng (`VIE_congress_*`, `VIE_party_*`)
* **Ngôn ngữ tạo hình:** Sự tôn nghiêm, thiêng liêng và ý chí sắt đá. 
* **Vật thể biểu trưng chủ đạo:**
  - Bục tượng Chủ tịch Hồ Chí Minh bằng đồng đỏ;
  - Búa Liềm vàng ròng NMM vát cạnh 3D nổi khối trên nền sơn mài đỏ thắm;
  - Trống đồng Đông Sơn mạ vàng với hình chim Lạc bay ngược chiều kim đồng hồ;
  - Cuốn Hiến pháp và Văn kiện Đại hội Đảng bìa da gập nẹp vàng kim;
  - Ngọn đuốc lý tưởng cách mạng rực cháy ánh hào quang ấm áp.
* **Bảng màu:** Đỏ cờ `#DA251D`, đỏ son hoàng gia `#800020`, vàng kim hoàng gia `#D4AF37`, vàng champagne `#FFF8DC`.

### 2. Trụ Cột Kinh Tế & Đổi Mới Toàn Diện (`VIE_doi_moi_*`, `VIE_industry_*`, `VIE_energy_*`)
* **Ngôn ngữ tạo hình:** Sự chuyển động không ngừng, công nghiệp hiện đại và bứt phá công nghệ cao.
* **Vật thể biểu trưng chủ đạo:**
  - Bánh răng công nghiệp thép crôm đan xen bông lúa vàng trĩu hạt (liên minh công nông);
  - Tấm wafer silicon bán dẫn 7 sắc cầu vồng và bảng mạch vi điện tử nano;
  - Trụ tuabin điện gió ngoài khơi xoay tròn giữa nền trời xanh lộng gió;
  - Tuyến đường cao tốc Bắc - Nam và đoàn tàu metro hiện đại rẽ sáng ban mai;
  - Ngọn lửa khí dầu mỏ giàn khoan Bạch Hổ rực cháy trên thềm lục địa.
* **Bảng màu:** Cam công nghiệp `#E67E22`, xanh lục sinh thái `#27AE60`, xanh kính phản quang cao ốc `#2980B9`, vàng lúa `#FFCC00`.

### 3. Trụ Cột Quốc Phòng & Hiện Đại Hóa Quân Đội (`VIE_modernize_vpa`, `VIE_army_*`, `VIE_navy_*`, `VIE_air_*`)
* **Ngôn ngữ tạo hình:** Sức mạnh răn đe, kỷ luật thép, hiện đại và quả cảm.
* **Vật thể biểu trưng chủ đạo:**
  - Tháp pháo và xích tăng T-90S nghiêng góc chiến thuật;
  - Thân tàu ngầm Kilo 636 màu đen tàng hình rẽ sóng ngầm thềm lục địa;
  - Mũi tiêm kích Su-30MK2 mang cờ sao vàng rẽ mây lao vút lên bầu trời;
  - Bệ phóng tên lửa bờ Bastion-P dựng nòng kiên định hướng ra biển;
  - Quân kỳ thêu chữ vàng "Quyết Thắng" bay phấp phới trên trận địa.
* **Bảng màu:** Rêu quân phục `#3D5A3D`, xám thép vũ khí `#34495E`, đỏ tươi Quân kỳ `#DA251D`, vàng sao `#FFDE23`.

### 4. Trụ Cột An Ninh Quốc Gia & Nội Chính (`VIE_sec_*`, `VIE_security_*`)
* **Ngôn ngữ tạo hình:** Vững chắc, kỷ cương, thanh bảo kiếm và lá chắn bảo vệ chế độ.
* **Vật thể biểu trưng chủ đạo:**
  - Chiếc khiên đồng dày dặn gắn Công an hiệu nổi khối nâng đỡ thanh kiếm thép công lý;
  - Mũ kê-pi Công an Nhân dân đặt cạnh tập hồ sơ tư pháp dấu sáp đỏ;
  - Lưới dữ liệu an ninh số quốc gia với các đường viền neon phát quang bảo mật;
  - Camera giám sát và tường lửa bảo vệ không gian mạng quốc gia.
* **Bảng màu:** Đỏ thẫm công an `#900C3F`, vàng đồng phù hiệu `#D4AF37`, xanh neon an ninh mạng `#00FFFF`.

### 5. Trụ Cột Biển Đông & Chủ Quyền Lãnh Hải (`VIE_law_of_the_sea`, `VIE_scs_*`)
* **Ngôn ngữ tạo hình:** Kiên trung bất khuất trước sóng gió, tính chính nghĩa và pháp lý quốc tế.
* **Vật thể biểu trưng chủ đạo:**
  - Nhà giàn DK1 chân thép cắm sâu vào rạn san hô giữa ngàn trùng bão gió;
  - Cột mốc chủ quyền Trường Sa bằng đá san hô khắc chìm tọa độ thiêng liêng;
  - Đèn hải đăng quét chùm sáng vàng cực mạnh xua tan giông bão Biển Đông;
  - Tàu Cảnh sát biển và Kiểm ngư Việt Nam hiên ngang tuần tra bảo vệ ngư dân.
* **Bảng màu:** Xanh thẳm đại dương `#0B2545`, xanh ngọc san hô `#16A085`, trắng bọt sóng `#F0F8FF`, vàng hải đăng `#FFAA00`.

### 6. Trụ Cột Ngoại Giao & Hội Nhập Quốc Tế (`VIE_asean_integration`, 5 Trục Quan Hệ)
* **Ngôn ngữ tạo hình:** Độc lập, tự chủ, mềm dẻo nhưng kiên định, bản lĩnh Cây tre Việt Nam.
* **Chi tiết toàn diện:** Được trình bày trọn vẹn trong Phần II dưới đây như một **Đề án Chuẩn Mẫu Tiên Phong** cho toàn submod.

---

## 📌 PHẦN II: ĐỀ ÁN CHI TIẾT 34 FOCUS NHÁNH NGOẠI GIAO (BỘ CHUẨN MẪU TIÊN PHONG)

Mỗi tiêu điểm trong đề án được thiết kế độc bản theo 6 trường dữ liệu chuẩn mực:
1. **Thông tin định danh:** Mã Focus ID, Tên tiếng Việt, Tọa độ lưới & Mốc thời gian lịch sử.
2. **Ẩn dụ cốt lõi & Vật thể trung tâm (Centerpiece):** Ý niệm chủ đạo và vật thể chính thu hút thị giác.
3. **Bố cục, Góc nhìn & Chiều sâu 3D (Cinematic Perspective):** Phối cảnh camera (3/4 isometric, low-angle ngước nhìn, cận cảnh macro, toàn cảnh sa bàn).
4. **Bảng màu chủ đạo & Ánh sáng (Palette & Chiaroscuro):** Mã màu HEX chính xác, nhiệt độ màu (ấm/lạnh), nguồn sáng then chốt.
5. **Chất cảm vật liệu & Bề mặt (Materials & NMM):** Kim loại mạ vàng, đồng đúc Đông Sơn, đá hoa cương biên giới, vải lụa quốc kỳ bay trong gió, kính phản quang cao ốc.
6. **Kể chuyện 3 lớp không gian (Foreground - Midground - Background):** Phân tầng chiều sâu để đạt chuẩn 3.000+ màu sắc chuyển tiếp tự nhiên.

---

## TRỤC GỐC HUB: ĐƯỜNG LỐI ĐỐI NGOẠI TOÀN DIỆN

### Focus 1: `VIE_asean_integration` — Đường lối Đối ngoại Độc lập, Tự chủ
* **Tọa độ & Mốc lịch sử:** (48, 11) | Khởi nguyên Đại hội VII & VIII, mở rộng xuyên suốt thời kỳ Đổi Mới.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **La bàn Thiên văn Đối ngoại Bằng Vàng Ròng & Quốc huy Độc Lập**. Một chiếc la bàn cổ điển cỡ lớn bằng vàng thau đúc hoa văn mặt trời Trống đồng Đông Sơn, kim la bàn chỉ về hướng Bắc và các vì sao tự do.
* **Bố cục & Phối cảnh:** Góc nhìn nghiêng 3/4 từ trên xuống (high-angle 45 độ), chiếc la bàn đặt trên tấm bản đồ hàng hải Đông Nam Á cổ kẻ kinh vĩ tuyến dát vàng rực rỡ.
* **Bảng màu & Ánh sáng:**
  - Vàng kim hoàng gia: `#D4AF37`, `#FFDF00`, nâu bóng đồng `#4A2E00`.
  - Đỏ thắm cờ Tổ quốc: `#DA251D`, `#8B0000`.
  - Nguồn sáng: Chùm sáng thiên đỉnh chiếu thẳng vào tâm kim la bàn, tỏa hào quang hạt bụi vàng kim lấp lánh (divine sunbeam).
* **Chất cảm vật liệu:** Vàng bóng NMM phản chiếu các điểm sáng chói (specular highlights); mặt kính la bàn dày có vết lóa phản quang bầu trời xanh ngọc; viền kim loại chạm khắc hoa văn chim Lạc tinh xảo.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Vành kim loại la bàn nhô ra khỏi khung, kim chỉ hướng vát cạnh sắc nét.
  - *Trung cảnh:* Bó lúa 10 dải vàng ASEAN uốn lượn ôm trọn lấy Quốc huy Việt Nam đúc nổi ở tâm la bàn.
  - *Hậu cảnh:* Bản đồ bán đảo Đông Dương chìm mờ trong sắc xanh thẳm đại dương (`#0B2545`) với các luồng gió thương mại kẻ chỉ bạc.
* **Đột phá khác biệt:** Không dùng cờ chữ nhật đơn điệu; thay bằng la bàn thiên văn biểu trưng cho sự định hướng chiến lược vững vàng giữa biến động toàn cầu.

---

## TRỤC 1: QUAN HỆ VIỆT - TRUNG & BIÊN GIỚI PHÍA BẮC (6 FOCUS)

```text
       VIE_gulf_of_tonkin (y=12)
                │
     VIE_border_settlement (y=13)
                │
           VIE_16_words (y=14)
           ┌────┴────┐
VIE_border_trade_gates  VIE_defence_hotline (y=15)
           └────┬────┘
        VIE_shared_future (y=16)
```

### Focus 2: `VIE_gulf_of_tonkin` — Hiệp định Phân định Vịnh Bắc Bộ 2000
* **Tọa độ & Mốc lịch sử:** (36, 12) | Ký kết ngày 25/12/2000 tại Bắc Kinh; mốc son xác lập đường biên giới biển đầu tiên của Việt Nam với nước láng giềng.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Hải Đồ Phân Định Vịnh Bắc Bộ & Chiếc Thước Kẻ Song Mã Bằng Đồng Hàng Hải**. Một cuộn hải đồ da cao cấp trải rộng trên bàn gỗ lim, trên mặt nước biển in rõ nét đứt phân định ranh giới lãnh hải và vùng đánh cá chung.
* **Bố cục & Phối cảnh:** Góc nhìn xéo điện ảnh (cinematic low-angle nghiêng), chiếc com-pa đo khoảng cách hàng hải bằng đồng thau cắm mũi kim vào tọa độ đảo Bạch Long Vĩ.
* **Bảng màu & Ánh sáng:**
  - Xanh lam ngọc biển vịnh: `#004E64`, `#25A18E`, bọt sóng bạc `#E0FAFF`.
  - Đồng thau cổ: `#B8860B`, `#8C6239`.
  - Giấy da hải đồ cổ điển: `#F4ECD8`, `#C7B299`.
  - Ánh sáng: Đèn hải đăng quét ngang từ góc trái, tạo vệt sáng quét dài trên mặt sóng lấp lánh.
* **Chất cảm vật liệu:** Giấy hải đồ có độ nhám viền sờn; mặt nước biển có gợn sóng 3D; kim com-pa phản chiếu tia sáng lạnh của kim loại đã tôi luyện.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Cây com-pa hàng hải bằng đồng cắm sâu vào hải đồ, góc thước đo phản chiếu ánh đèn.
  - *Trung cảnh:* Cuộn hải đồ vẽ đường ranh giới biển 21 điểm nối liền, chiếc tàu kiểm ngư Việt Nam mũi rẽ sóng trắng xóa tuần tra hòa bình.
  - *Hậu cảnh:* Đảo ngọc Bạch Long Vĩ mờ ảo trong sương sớm cùng ngọn hải đăng sừng sững giữa bầu trời tím thẫm rạng đông.

### Focus 3: `VIE_border_settlement` — Hoàn Tất Phân Giới Cắm Mốc Biên Giới Đất Liền
* **Tọa độ & Mốc lịch sử:** (36, 13) | Hiệp ước 1999 & Hoàn tất cắm mốc 2008; dựng cột mốc số 0 và hàng ngàn cột mốc đá hoa cương.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cột Mốc Biên Giới Đá Hoa Cương Nguyên Khối Mang Quốc Huy Mạ Vàng**. Cột mốc tứ giác bằng đá granite nguyên khối vững chãi, chạm khắc chìm chữ son "VIỆT NAM" và số hiệu cột mốc, gắn Quốc huy bằng đồng đỏ mạ vàng sáng bóng.
* **Bố cục & Phối cảnh:** Góc ngước nhìn từ dưới lên (heroic low-angle), cột mốc vươn cao kiêu hãnh xé tan mây ngàn dải Trường Sơn và núi rừng Đông Bắc.
* **Bảng màu & Ánh sáng:**
  - Đá hoa cương xám hoa muối tiêu: `#7F8C8D`, `#BDC3C7`, `#2C3E50`.
  - Đỏ son quốc hiệu: `#C0392B`. Vàng kim quốc huy: `#F1C40F`.
  - Xanh ngàn đại ngàn: `#1E4620`, mây trời xanh lam nhạt `#EBF5FB`.
  - Ánh sáng: Ánh nắng bình minh rọi từ hướng Đông, đổ bóng đổ dài (hard cast shadow) của cột mốc xuống thềm cỏ biên cương.
* **Chất cảm vật liệu:** Bề mặt đá granite có độ nhám hạt khoáng thạch thô ráp, góc cạnh vát chéo sắc bén; Quốc huy đồng chạm nổi có độ bóng gương rực rỡ.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Bậc thềm đá hoa cương và khóm hoa sim tím biên thùy nở rộ bên chân mốc.
  - *Trung cảnh:* Thân cột mốc đá hoa cương sừng sững chiếm $60\%$ khung hình, khắc rõ Quốc huy và chữ Việt Nam dát vàng.
  - *Hậu cảnh:* Dãy núi đá vôi trập trùng mù sương và dải đường biên thanh bình uốn lượn quanh sườn non.

### Focus 4: `VIE_16_words` — Phương Châm 16 Chữ & Tinh Thần 4 Tốt
* **Tọa độ & Mốc lịch sử:** (36, 14) | "Láng giềng hữu nghị, hợp tác toàn diện, ổn định lâu dài, hướng tới tương lai" (1999).
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cuộn Trúc Thư Ngoại Giao Khắc Vàng & Cành Trúc Đan Xen Nhành Liễu**. Cuộn thư tịch ngoại giao sơn mài đỏ gắn nẹp ngọc bích, mở ra văn bản chạm 16 chữ vàng kim thư pháp, đặt trước nhành trúc xanh kiên cường và nhành liễu mềm mại.
* **Bố cục & Phối cảnh:** Bố cục cân xứng trang trọng (formal symmetry), hơi lệch nhẹ góc 15 độ để tạo chiều sâu thị giác.
* **Bảng màu & Ánh sáng:**
  - Đỏ sơn mài hoàng cung: `#800020`, đỏ tươi `#B22222`.
  - Xanh ngọc bích phù điêu: `#00A86B`, xanh cẩm thạch `#2E8B57`.
  - Nhũ vàng thư pháp: `#FFD700`, `#DAA520`.
  - Ánh sáng: Ánh nến hoặc đèn lồng nghi lễ màu vàng ấm tỏa rộng, tạo vầng hào quang ấm áp bao quanh văn tự.
* **Chất cảm vật liệu:** Nước sơn mài bóng loáng như gương phản chiếu ánh sáng; ngọc bích trong mờ đục (subsurface scattering); mực nhũ vàng đắp nổi trên nền gấm tơ tằm.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Cây bút lông cán trúc bịt bạc và nghiên mực nghiên đá hoa sen nghi thức.
  - *Trung cảnh:* Bức hoành thư sơn mài khắc nổi các ký tự 16 chữ dát vàng lấp lánh.
  - *Hậu cảnh:* Cây cầu đá Hữu Nghị mờ ảo nối liền hai bờ non nước trong sương mai thanh bình.

### Focus 5: `VIE_border_trade_gates` — Mở Rộng Cửa Khẩu & Thương Mại Biên Mậu
* **Tọa độ & Mốc lịch sử:** (34, 15) | Hiện đại hóa Cửa khẩu Quốc tế Hữu Nghị, Tân Thanh, Móng Cái, Lào Cai; thông quan điện tử.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cổng Vòm Cửa Khẩu Quốc Tế Hiện Đại & Dòng Xe Container Logistics Thông Quan**. Kiến trúc cổng vòm cửa khẩu uy nghi bằng thép và kính cường lực, bên trên gắn Quốc huy và biển tên Cửa khẩu Quốc tế Hữu Nghị rực sáng.
* **Bố cục & Phối cảnh:** Phối cảnh một điểm tụ (one-point perspective) nhìn từ làn đường kiểm soát thông quan hướng ra chân trời biên mậu.
* **Bảng màu & Ánh sáng:**
  - Thép xanh công nghiệp: `#34495E`, kính xanh phản quang `#5DADE2`.
  - Đèn tín hiệu thông quan xanh lá: `#2ECC71`.
  - Cam rực container hàng hóa: `#E67E22`, vàng xe tải `#F39C12`.
  - Ánh sáng: Đèn pha cao áp chiếu sáng rực rỡ kết hợp ánh hoàng hôn ngũ sắc trên đỉnh đèo.
* **Chất cảm vật liệu:** Kim loại khung giàn không gian bóng loáng; mặt đường nhựa bê tông có vạch sơn phản quang vàng trắng sắc nét; kính tòa nhà cửa khẩu phản chiếu mây trời.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Rào chắn barie thông quan tự động bằng kim loại màu đỏ trắng, cảm biến mã vạch phát tia laser xanh.
  - *Trung cảnh:* Cổng vòm Cửa khẩu Quốc tế bằng đá hoa cương kết hợp kính hiện đại, đoàn xe vận tải container nối dài tấp nập.
  - *Hậu cảnh:* Dãy núi biên ải xanh thẫm và bầu trời rực sáng đèn đêm của trung tâm logistics cửa khẩu.

### Focus 6: `VIE_defence_hotline` — Đường Dây Nóng Quốc Phòng & Tránh Va Chạm
* **Tọa độ & Mốc lịch sử:** (38, 15) | Ký kết thiết lập đường dây liên lạc trực tiếp giữa Bộ Quốc phòng hai nước (2011) nhằm kiểm soát khủng hoảng trên biển.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Thiết Bị Điện Thoại Mật Mã Quân Sự Bọc Vàng & Tín Hiệu Sóng Radar Tần Số Cao**. Một chiếc máy điện thoại chỉ huy quân sự màu đỏ son với ống nghe mạ crôm sáng loáng, bên cạnh là màn hình radar hiển thị đường sóng âm xanh neon bảo mật.
* **Bố cục & Phối cảnh:** Góc chụp cận cảnh macro nghiêng 45 độ đặt trên bàn tác chiến hải quân bằng gỗ gụ sẫm màu.
* **Bảng màu & Ánh sáng:**
  - Đỏ quân sự bảo mật: `#990000`, đỏ thắm bóng bẩy `#CC0000`.
  - Xanh neon radar bảo mật: `#00FFCC`, `#0099FF`.
  - Kim loại crôm lạnh: `#D5D8DC`, xám thép `#2C3E50`.
  - Ánh sáng: Màn hình điện tử hắt ánh sáng xanh lục huỳnh quang lên ống nghe màu đỏ, tạo độ tương phản bổ túc (complementary contrast) cực mạnh.
* **Chất cảm vật liệu:** Vỏ nhựa điện thoại bóng kiểu sơn tĩnh điện cao cấp; ống nghe có dây xoắn đàn hồi bằng cao su đen; kim loại phím bấm số mạ vàng có đèn nền LED.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Khóa mật mã quân sự bằng đồng cắm trên bảng điều khiển tác chiến.
  - *Trung cảnh:* Chiếc điện thoại đường dây nóng chỉ huy với ống nghe màu đỏ nhấc bổng khỏi giá, màn hình sóng xung điện thoại xanh lục.
  - *Hậu cảnh:* Tấm hải đồ tác chiến mờ tối với các tuyến tuần tra chung song phương an toàn trên Vịnh.

### Focus 7: `VIE_shared_future` — Cộng Đồng Chia Sẻ Tương Lai & Đột Phá Song Phương
* **Tọa độ & Mốc lịch sử:** (36, 16) | Tuyên bố chung nâng tầm quan hệ đối tác chiến lược toàn diện, xây dựng Cộng đồng chia sẻ tương lai Việt Nam - Trung Quốc (2023).
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cầu Dây Văng Hữu Nghị Tương Lai & Hai Búp Sen Giao Thoa Ánh Hào Quang**. Một cây cầu dây văng hiện đại vĩ đại bắc qua dòng sông biên giới, trụ tháp hình hai búp sen vươn lên đỡ lấy quả cầu ánh sáng pha lê tương lai.
* **Bố cục & Phối cảnh:** Phối cảnh góc siêu rộng từ mặt nước ngước nhìn lên nhịp cầu kỳ vĩ (wide low-angle perspective).
* **Bảng màu & Ánh sáng:**
  - Ánh sáng tương lai: Vàng kim `#FFD700`, lam ngọc điện tử `#00FFFF`, tím hoàng hôn `#4A154B`.
  - Trắng bê tông dự ứng lực: `#F8F9F9`, dây văng thép bạc `#BDC3C7`.
  - Nguồn sáng: Ánh hoàng hôn vàng cam ấm áp hòa quyện hệ thống đèn LED nghệ thuật nhiều tầng trên thân cầu.
* **Chất cảm vật liệu:** Cáp thép dây văng căng tràn lực căng cơ học; mặt nước sông phẳng lặng phản chiếu lung linh dải ánh sáng; kính pha lê trên đỉnh trụ tháp phát quang huyền ảo.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Lan can tàu tuần tra nghi lễ với dải băng khánh thành bằng lụa đỏ thắm viền tua rua vàng.
  - *Trung cảnh:* Cây cầu dây văng hiện đại lộng lẫy với tuyến tàu cao tốc xuyên biên giới đang lướt nhanh về phía trước.
  - *Hậu cảnh:* Thành phố tương lai xanh hai bên bờ sông với các tòa nhà thông minh vươn lên giữa ráng chiều rực rỡ.

---

## TRỤC 2: LÁNG GIỀNG ĐÔNG DƯƠNG & SINH THÁI MÊ KÔNG (7 FOCUS)

```text
VIE_special_relations_laos (y=12)      VIE_cambodia_relations (y=12)
           │                                      │
VIE_mekong_commission (y=13)           VIE_cambodia_border (y=13)
           │                                      │
VIE_mekong_dams_response (y=14)        VIE_funan_techo_response (y=14)
           └──────────────────┬───────────────────┘
                    VIE_indochina_solidarity (y=15)
                              │
                    VIE_indochina_federation (Alternative)
```

### Focus 8: `VIE_special_relations_laos` — Quan Hệ Đặc Biệt Việt Nam - Lào
* **Tọa độ & Mốc lịch sử:** (40, 12) | "Mối quan hệ hữu nghị vĩ đại, đoàn kết đặc biệt, thủy chung son sắt" xây đắp từ kháng chiến đến hòa bình dựng xây.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Tháp Vàng Pha That Luang Đan Lồng Đài Sen Vàng & Nhành Hoa Champa**. Bảo tháp linh thiêng mạ vàng Pha That Luang của xứ Triệu Voi đặt song song cùng Đài hoa sen đá cẩm thạch Việt Nam, quấn quýt nhành hoa Champa (hoa Chăm-pa trắng nhụy vàng) ngát hương.
* **Bố cục & Phối cảnh:** Góc nhìn chính diện trang nghiêm với chiều sâu 3 lớp (formal perspective with layered depth).
* **Bảng màu & Ánh sáng:**
  - Vàng tháp Phật giáo: `#FFB800`, `#E59866`.
  - Trắng tinh khôi hoa Champa: `#FDEDEC`, nhụy vàng `#F4D03F`.
  - Xanh Trường Sơn Tây: `#196F3D`. Đỏ thắm cờ hữu nghị: `#C0392B`.
  - Ánh sáng: Nắng sớm rực rỡ chiếu nghiêng qua tháp vàng, tạo hiệu ứng phát quang bụi vàng (golden dust volumetric rays).
* **Chất cảm vật liệu:** Vàng dát lá trên đỉnh tháp có độ lồi lõm thủ công mỹ nghệ; cánh hoa Champa mềm mại nhung mượt; cẩm thạch đài sen mát lạnh.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Cành hoa Champa trắng muốt kết cùng nhành hoa sen hồng trên chiếc khay bạc chạm nổi hoa văn truyền thống.
  - *Trung cảnh:* Đỉnh tháp Pha That Luang tráng lệ vươn cao bên cạnh tượng đài hữu nghị Việt - Lào bằng đồng đỏ.
  - *Hậu cảnh:* Dãy núi Trường Sơn hùng vĩ - nơi che chở cho hai dân tộc qua bao thăng trầm khói lửa.

### Focus 9: `VIE_cambodia_relations` — Quan Hệ Láng Giềng Hữu Nghị Việt Nam - Campuchia
* **Tọa độ & Mốc lịch sử:** (44, 12) | "Láng giềng tốt đẹp, hữu nghị truyền thống, hợp tác toàn diện, bền vững lâu dài".
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Quần Thể Tháp Đá Angkor Wat Cổ Kính Bên Dòng Sông Mê Kông Hòa Bình**. Kiến trúc 5 ngọn tháp hoa sen bằng đá sa thạch của Angkor phản chiếu trên mặt nước sông Mê Kông, được bao bọc bởi vòng nguyệt quế hoa lúa vàng và dải lụa hữu nghị.
* **Bố cục & Phối cảnh:** Góc nhìn 3/4 từ mép nước bờ sông hướng sang quần thể đền đá cổ.
* **Bảng màu & Ánh sáng:**
  - Sa thạch rêu phong: `#7D6608`, `#935116`, xám đá cổ `#5D6D7E`.
  - Vàng đất Chùa Tháp: `#F5B041`. Xanh dòng phù sa: `#2980B9`, `#1F618D`.
  - Ánh sáng: Bình minh màu cam đỏ rực rỡ ló rạng sau lưng các tháp đá, tạo bóng ngược (silhouette) huyền ảo pha vệt sáng vàng kim mép tháp.
* **Chất cảm vật liệu:** Đá sa thạch cổ có vân chạm nổi Apsara tinh tế; mặt nước sông Mekong lấp loáng gợn sóng phù sa đỏ ngầu mỡ màu; dải lụa hữu nghị mềm mại như tơ Khmer.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Thuyền hoa đăng nghi lễ truyền thống trôi êm đềm với ngọn nến hoa sen thắp sáng.
  - *Trung cảnh:* Những ngọn tháp vĩ đại của đền cổ vươn cao bên cạnh cầu dây văng hữu nghị mới khánh thành.
  - *Hậu cảnh:* Bầu trời rạng đông mênh mang soi bóng đôi bờ sông Mê Kông xanh mát bóng thốt nốt.

### Focus 10: `VIE_mekong_commission` — Ủy Hội Sông Mê Kông Quốc Tế (MRC)
* **Tọa độ & Mốc lịch sử:** (40, 13) | Hiệp định Mê Kông 1995; điều phối chia sẻ nguồn nước, bảo vệ sinh thái đồng bằng sông Cửu Long.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Biểu Trưng Dòng Nước Mê Kông 4 Nhánh Vươn Lên & Bàn Tay Nâng Niu Bát Nước Sinh Mệnh**. Dòng nước xanh lam uốn lượn hình chữ S cách điệu thành 4 luồng sóng ôm trọn hạt ngọc phù sa màu hổ phách, đặt trên đĩa cân bằng thủy văn quốc tế.
* **Bố cục & Phối cảnh:** Bố cục hình tròn hài hòa (circular focal composition), tâm điểm là khối cầu nước thủy tinh phản chiếu hệ sinh thái sông.
* **Bảng màu & Ánh sáng:**
  - Xanh lam ngọc bích nước sông: `#3498DB`, xanh lục rêu sinh thái `#27AE60`.
  - Vàng phù sa đồng bằng: `#E59866`, `#D35400`.
  - Ánh sáng: Luồng ánh sáng xuyên thấu (translucent caustics) khúc xạ qua khối nước pha lê lấp lánh như kim cương.
* **Chất cảm vật liệu:** Khối chất lỏng trong suốt khúc xạ ánh sáng; vành hợp kim nhôm đo mực nước tráng men trắng bóng; hạt phù sa có vân lấp lánh như đá mắt hổ.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Thước đo cao trình thủy văn bằng kim loại không gỉ cắm sâu vào dòng nước cuộn trào.
  - *Trung cảnh:* Biểu trưng dòng nước Mê Kông cách điệu thành quả cầu pha lê lơ lửng, chứa đựng hình bóng cá tra dầu và rừng ngập mặn.
  - *Hậu cảnh:* Vùng châu thổ Cửu Long mênh mông 9 nhánh sông đổ ra biển Đông xanh ngắt.

### Focus 11: `VIE_cambodia_border` — Phân Giới Cắm Mốc Biên Giới Việt Nam - Campuchia
* **Tọa độ & Mốc lịch sử:** (44, 13) | Hoàn thành phân giới cắm mốc $84\%$ đường biên trên đất liền (2019-2020); cắm mốc mỏ vẹt Tây Ninh, An Giang, Kiên Giang.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cột Mốc Biên Giới Số Hiệu 275 Bằng Đá Granite & Bản Đồ Địa Hình Tỷ Lệ 1:25.000**. Cột mốc biên cương hai mặt khắc song ngữ Việt - Khmer, đặt trang trọng trên tấm bản đồ địa hình phân giới cắm mốc có dấu sáp niêm phong đỏ của hai chính phủ.
* **Bố cục & Phối cảnh:** Góc chụp cận cảnh 3D đặt chéo góc 30 độ, tôn vinh độ chính xác và tính pháp lý quốc tế bất khả xâm phạm.
* **Bảng màu & Ánh sáng:**
  - Đá hoa cương xám tro: `#616A6B`, `#95A5A6`.
  - Mực đỏ son dấu sáp: `#900C3F`, ruy băng xanh hoàng gia Campuchia: `#1B4F72`.
  - Vàng đồng thau Quốc huy: `#D4AC0D`.
  - Ánh sáng: Ánh nắng nhiệt đới Tây Nam Bộ rực rỡ, chiếu rõ từng nét khắc chữ chìm sâu trên mặt đá.
* **Chất cảm vật liệu:** Độ hạt của bề mặt đá granite được đánh bóng nhẵn ở thân và để thô ở chân đế; dấu sáp niêm phong có vết nứt tự nhiên của sáp ong hoàng gia; bản đồ vẽ trên giấy can kỹ thuật cao cấp.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Kính lúp đo đạc trắc địa quang học bằng đồng đặt trên bản đồ cắm mốc.
  - *Trung cảnh:* Thân cột mốc biên giới sừng sững cắm vững chắc giữa đường biên giới hòa bình phát triển.
  - *Hậu cảnh:* Cánh đồng lúa vàng óng ả trải dài tít tắp qua biên giới của nông dân hai nước cùng canh tác.

### Focus 12: `VIE_mekong_dams_response` — Ứng Phó Thủy Điện Thượng Nguồn Mê Kông
* **Tọa độ & Mốc lịch sử:** (40, 14) | Đấu tranh ngoại giao, vận động chia sẻ dữ liệu thủy văn các đập Lan Thương / Xayaburi / Don Sahong; chủ động thích ứng hạn mặn.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cánh Đập Thủy Điện Khổng Lồ Bê Tông Chắn Nước & Chiếc Cảm Biến Cảnh Báo Mực Nước Khẩn Cấp**. Một bức tường đập bê tông xám ngắt chặn đứng dòng nước, đối lập với bàn tay công nghệ Việt Nam cầm thiết bị viễn thám vệ tinh đo mực nước sông rực sáng.
* **Bố cục & Phối cảnh:** Phối cảnh đối chọi gay gắt (dramatic split composition): Phía trên là khối đập bê tông đồ sộ, phía dưới là dòng chảy đồng bằng nứt nẻ được bảo vệ bởi lá chắn công nghệ xanh.
* **Bảng màu & Ánh sáng:**
  - Xám lạnh bê tông đập: `#34495E`, `#2C3E50`.
  - Đỏ cam cảnh báo nguy cơ: `#E74C3C`, `#D35400`.
  - Xanh lục sinh thái bảo vệ: `#27AE60`.
  - Ánh sáng: Ánh sáng lạnh lẽo từ bầu trời xám xịt phản chiếu trên mặt nước hồ thủy điện, đối lập ánh đèn quét radar kiểm soát của Việt Nam.
* **Chất cảm vật liệu:** Bê tông cốt thép nứt rạn và rêu phong; kim loại van xả đáy khổng lồ rỉ sét; màn hình thiết bị viễn thám hiển thị ảnh nhiệt vệ tinh sáng rực.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Màn hình tablet tác chiến hiển thị biểu đồ dòng chảy lưu vực và dự báo xâm nhập mặn.
  - *Trung cảnh:* Bức tường đập thủy điện thượng nguồn sừng sững với các cửa xả nước tung bọt trắng xóa.
  - *Hậu cảnh:* Vùng đồng bằng Cửu Long đang kiên cường xây đập ngọt hóa và hồ trữ nước ngọt bảo vệ vựa lúa.

### Focus 13: `VIE_funan_techo_response` — Ứng Phó Kênh Đào Phù Nam Techo
* **Tọa độ & Mốc lịch sử:** (44, 14) | Vận động cung cấp báo cáo đánh giá tác động môi trường (EIA), đối thoại ngoại giao khoa học, bảo đảm an ninh sinh thái đồng bằng sông Tiền và sông Hậu (2024+).
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Sa Bàn Kênh Đào Cắt Đôi Dòng Nước & Kính Trắc Địa Khoa Học Giám Sát Lưu Vực**. Một sa bàn địa hình 3D mô phỏng tuyến kênh đào nhân tạo cắt qua đồng bằng, bên trên là ống kính máy đo đạc trắc địa laser của các nhà khoa học Việt Nam chiếu tia phân tích thủy động lực học.
* **Bố cục & Phối cảnh:** Góc nhìn từ trên cao xuống 3/4 (isometric 3D satellite view) như một phòng nghiên cứu chiến lược quốc gia.
* **Bảng màu & Ánh sáng:**
  - Nâu đất lòng kênh đào: `#6E2C00`, `#A04000`.
  - Xanh lục bảo vệ dòng sông: `#1E8449`, lam phù sa `#2E86C1`.
  - Đỏ tia laser trắc địa: `#FF0000`, vàng kim báo cáo quốc tế `#F4D03F`.
  - Ánh sáng: Tia laser quét đỏ chéo qua mô hình kênh đào, tạo bóng đổ cắt gọt địa hình sắc lạnh.
* **Chất cảm vật liệu:** Sa bàn đất nặn và nhựa polymer có độ mịn địa hình cao; thấu kính trắc địa bằng thủy tinh quang học phản quang tím; tập hồ sơ báo cáo khoa học gáy xoắn bạc.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Kính ngắm trắc địa điện tử phóng to vào tọa độ cửa van tiếp nước của kênh đào.
  - *Trung cảnh:* Mô hình tuyến kênh đào nhân tạo thẳng tắp rẽ nước từ sông Bassac ra vịnh Thái Lan.
  - *Hậu cảnh:* Vùng đất ngập nước Tràm Chim và sông Tiền sông Hậu cần được bảo toàn dòng chảy sinh mệnh.

### Focus 14: `VIE_indochina_solidarity` — Khối Đoàn Kết Ba Nước Đông Dương
* **Tọa độ & Mốc lịch sử:** (42, 15) | Liên minh Tam giác phát triển Việt Nam - Lào - Campuchia (CLV), hội nghị cấp cao ba thủ tướng, gắn kết an ninh - kinh tế keo sơn.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Ngọn Đuốc Đồng Ba Ngọn Lửa Vàng & Chiếc Khiên Đồng Tam Giác Phát Triển**. Một chiếc khiên bằng đồng đỏ đúc hoa văn truyền thống Đông Dương, trên bề mặt chạm nổi bản đồ ba nước gắn kết, nâng đỡ ngọn đuốc đồng tỏa ba luồng lửa đỏ vàng rực rỡ tượng trưng cho ba quốc gia anh em.
* **Bố cục & Phối cảnh:** Bố cục tam giác vững chãi như bàn thạch (triangular monumental composition), góc nhìn ngước nhìn oai vệ từ chân bệ tượng đài.
* **Bảng màu & Ánh sáng:**
  - Đồng đỏ cổ xưa: `#B87333`, đồng thau vàng `#D4AF37`.
  - Lửa đỏ cam cách mạng: `#FF4500`, `#FFA500`, vàng lửa rực `#FFFF99`.
  - Xanh lam hòa bình ngọc bích: `#1B4F72`.
  - Ánh sáng: Ngọn lửa bốc cháy dữ dội tỏa ánh sáng cam ấm rực rỡ, chiếu sáng toàn bộ khiên đồng và đẩy lùi bóng tối xung quanh.
* **Chất cảm vật liệu:** Đồng đúc nguyên khối có các vết patina xanh đồng cổ kính ở kẽ rãnh hoa văn; ngọn lửa có độ trong mờ uyển chuyển và đốm tàn lửa bay lơ lửng.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Bệ đá hoa cương nguyên khối khắc phù điêu bông lúa và hoa Champa, hoa sen kết đoàn.
  - *Trung cảnh:* Chiếc khiên đồng tam giác và ngọn đuốc ba đốm lửa bừng sáng kiêu hùng chiếm trung tâm.
  - *Hậu cảnh:* Dãy Trường Sơn hùng vĩ nối liền ba dải đất nước dưới bầu trời hòa bình rực rỡ ráng mây vàng.

### Focus 14b (Alternative): `VIE_indochina_federation` — Liên Bang Đông Dương (Kịch Bản Mở Rộng)
* **Tọa độ & Mốc lịch sử:** (42, 16) | Lựa chọn chính trị giả định / Tái lập không gian chiến lược thống nhất ba nước.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Vương Miện Liên Bang Ba Ngôi Sao Vàng & Thanh Kiếm Hòa Bình Đặt Ngang Bản Đồ Tam Quốc**. Một ấn tín hoàng kim mang biểu tượng ba ngôi sao vàng trên nền men đỏ thắm, bao bọc bởi vòng cung hoa lúa ba nhánh và dải quốc kỳ thống nhất.
* **Bố cục & Phối cảnh:** Bố cục vương quyền chính trực (regal heraldic composition), góc nhìn trực diện trang nghiêm của một bản tuyên ngôn lập quốc.
* **Bảng màu & Ánh sáng:**
  - Đỏ hoàng gia đế chế: `#4A0E17`, `#78281F`.
  - Vàng kim vương giả: `#FFD700`, bạch kim `#E5E7E9`.
  - Ánh sáng: Vầng hào quang thánh thiện (halo radiance) tỏa từ tâm ấn tín ra bốn góc biểu tượng.
* **Chất cảm vật liệu:** Vàng ròng đúc dày chạm trổ hoa văn tinh xảo; men sứ đỏ bóng loáng; thanh kiếm thép tôi luyện sắc lạnh không tì vết.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Cuộn chỉ chiếu liên bang bằng giấy lụa viền nhũ vàng mở rộng trên bàn hội nghị.
  - *Trung cảnh:* Ấn tín liên bang đồ sộ với phù hiệu ba nước hợp nhất làm một thể thống nhất hùng cường.
  - *Hậu cảnh:* Bản đồ bán đảo Đông Dương thống nhất màu sắc vươn mình ra biển lớn Thái Bình Dương.

---

## TRỤC 3: TRỌNG TÂM ASEAN & NGOẠI GIAO ĐA PHƯƠNG (5 FOCUS)

```text
               VIE_asean_chair (y=12)
           ┌──────────┴──────────┐
VIE_code_of_conduct (y=13)   VIE_apec_host (y=13)
                                 │
                     VIE_un_security_council (y=14)
                                 │
                     VIE_multilateral_champion (y=15)
```

### Focus 15: `VIE_asean_chair` — Năm Chủ Tịch ASEAN (2010 & 2020)
* **Tọa độ & Mốc lịch sử:** (48, 12) | Đảm nhiệm xuất sắc vai trò Chủ tịch Hiệp hội các quốc gia Đông Nam Á; chủ đề "Hướng tới Cộng đồng ASEAN: Từ tầm nhìn đến hành động" (2010) và "Gắn kết và Chủ động thích ứng" (2020).
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Búa Điều Hành Bằng Gỗ Mun Bịt Vàng Của Chủ Tịch Hội Nghị & Bó Lúa Vàng ASEAN 10 Dải**. Chiếc búa gõ khai mạc nghi lễ (gavel) bằng gỗ mun quý cẩn xà cừ và nẹp vàng chạm hoa sen, đặt trên đế gõ tròn bằng đồng, bên cạnh là biểu trưng bó lúa vàng ASEAN rực rỡ.
* **Bố cục & Phối cảnh:** Góc nhìn cận cảnh 3/4 từ vị trí Chủ tịch bàn nghị sự (presidential gavel perspective).
* **Bảng màu & Ánh sáng:**
  - Xanh lam ASEAN chính thức: `#003399`, xanh da trời `#0066CC`.
  - Vàng bó lúa ASEAN: `#FFCC00`, `#E6B800`.
  - Gỗ mun đen nhánh cẩn xà cừ: `#1C1C1C`, lóng lánh xà cừ ngũ sắc `#E8DAEF`.
  - Ánh sáng: Đèn rọi sân khấu trung tâm hội nghị chiếu tập trung vào chiếc búa vàng, phản chiếu lấp lánh trên bề mặt sơn bóng gỗ mun.
* **Chất cảm vật liệu:** Gỗ mun tiện tròn láng bóng không tì vết; dải nẹp vàng mạ gương phản chiếu các lá cờ thành viên; biểu trưng bó lúa dập nổi kim loại sơn tĩnh điện cao cấp.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Đế gõ tròn bằng đồng sáng bóng với micro cổ ngỗng của Chủ tịch hội nghị.
  - *Trung cảnh:* Chiếc búa quyền uy của Chủ tịch ASEAN đặt chéo góc, nổi bật biểu trưng 10 dải lúa vàng đoàn kết.
  - *Hậu cảnh:* Khán phòng Trung tâm Hội nghị Quốc gia với hàng cờ 10 nước thành viên bay trong ánh đèn rực rỡ.

### Focus 16: `VIE_code_of_conduct` — Thúc Đẩy Bộ Quy Tắc Ứng Xử Ở Biển Đông (COC)
* **Tọa độ & Mốc lịch sử:** (46, 13) | Đấu tranh kiên trì xây dựng Bộ Quy tắc COC thực chất, hiệu lực, ràng buộc pháp lý dựa trên UNCLOS 1982; bảo đảm tự do hàng hải Biển Đông.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cuộn Văn Kiện Pháp Lý COC Đóng Bằng Da Hải Quân & Ngọn Hải Đăng Trường Sa Giữa Sóng Gió**. Bản thảo văn kiện pháp lý bìa da xanh thẫm in chữ vàng UNCLOS 1982, bên cạnh là ngọn hải đăng sừng sững trên nền đá san hô, phát ra chùm sáng xuyên thủng bão tố Biển Đông.
* **Bố cục & Phối cảnh:** Góc phối cảnh kịch tính (dramatic storm perspective): Nửa trái là ánh sáng pháp lý vững như bàn thạch, nửa phải là sóng biển dâng trào thử thách bản lĩnh.
* **Bảng màu & Ánh sáng:**
  - Xanh thẳm Biển Đông: `#0B2545`, xanh ngọc sóng biển `#134074`.
  - Vàng chùm đèn hải đăng: `#FFDE23`, `#FFAA00`.
  - Trắng bọt sóng bạc: `#EEF4F8`.
  - Ánh sáng: Ngọn hải đăng quét chùm sáng vàng cực mạnh chiếu rọi vào văn kiện COC, xua tan những đám mây giông xám xịt.
* **Chất cảm vật liệu:** Da thuộc xanh hải quân dập nổi chữ mạ vàng; thấu kính quang học Fresnel của đèn hải đăng bằng thủy tinh khúc xạ sắc sảo; bọt sóng biển tung tóe sinh động.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Cây bút ký mạ vàng và con dấu pháp lý bằng đồng đỏ khắc chữ "UNCLOS 1982".
  - *Trung cảnh:* Bản hiệp ước COC mở trang cam kết hòa bình, nâng đỡ bởi bệ đá ngọn hải đăng Trường Sa.
  - *Hậu cảnh:* Vùng biển trời Tổ quốc mênh mông với những cánh hải âu chao lượn trên nền rạng đông hòa bình.

### Focus 17: `VIE_apec_host` — Đăng Cai Năm APEC Việt Nam (2006 & 2017)
* **Tọa độ & Mốc lịch sử:** (50, 13) | Đăng cai APEC Hà Nội 2006 và APEC Đà Nẵng 2017; quy tụ lãnh đạo 21 nền kinh tế lớn nhất hành tinh; định hình thương mại tự do Châu Á - Thái Bình Dương.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Quả Địa Cầu Vành Đai Thái Bình Dương 21 Tia Nắng & Áo Dài Lụa Tơ Tằm Ngoại Giao**. Biểu trưng APEC cách điệu hình 21 tia nắng vươn lên thành vòng xoay năng động quanh vành đai Thái Bình Dương, kết hợp dải lụa tơ tằm Vạn Phúc màu vàng hoàng yến mang họa tiết gốm Chu Đậu.
* **Bố cục & Phối cảnh:** Bố cục chuyển động xoáy tròn động lực (dynamic vortex composition), toát lên tinh thần hội nhập kinh tế toàn cầu mạnh mẽ.
* **Bảng màu & Ánh sáng:**
  - Vàng hoàng yến tơ tằm: `#F4D03F`, `#D4AC0D`.
  - Xanh dương Thái Bình Dương: `#1B4F72`, `#2E86C1`.
  - Đỏ gốm Chu Đậu: `#922B21`.
  - Ánh sáng: 21 tia sáng phát quang từ tâm quả cầu tỏa ra xung quanh như pháo hoa rực rỡ chào đón các nguyên thủ quốc gia.
* **Chất cảm vật liệu:** Lụa tơ tằm mềm mại óng ả với các nếp gấp sóng sánh; kim loại biểu trưng APEC mạ crôm bóng loáng; bục gỗ tếch cao cấp nơi diễn ra lễ chụp ảnh chung của các nhà lãnh đạo.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Dải lụa tơ tằm nghi lễ dập hoa văn truyền thống uốn lượn mềm mại quanh góc khung hình.
  - *Trung cảnh:* Biểu trưng APEC 21 tia sáng dát vàng xoay quanh quả cầu địa giới Thái Bình Dương lấp lánh.
  - *Hậu cảnh:* Cầu Rồng Đà Nẵng rực sáng phun lửa trên dòng sông Hàn lung linh ánh đèn đón chào bạn bè quốc tế.

### Focus 18: `VIE_un_security_council` — Ủy Viên Không Thường Trực Hội Đồng Bảo An LHQ
* **Tọa độ & Mốc lịch sử:** (48, 14) | Hai nhiệm kỳ lịch sử 2008-2009 và 2020-2021 (trúng cử với số phiếu kỷ lục 192/193); đóng góp cho hòa bình và an ninh quốc tế.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Chiếc Ghế Ủy Viên Hội Đồng Bảo An Bọc Nhung Xanh & Cành Ô Liu Hòa Bình Quấn Quanh Huy Hiệu LHQ**. Biểu tượng cành ô liu hòa bình bằng vàng ròng nâng đỡ chiếc khiên Liên Hợp Quốc, đặt trang trọng bên cạnh bảng tên vị trí quốc gia "VIET NAM" bằng đồng sáng loáng trên bàn tròn phòng họp Đại hội đồng.
* **Bố cục & Phối cảnh:** Phối cảnh ghế đại biểu nhìn chéo góc từ phòng họp Hội đồng Bảo an tại New York (diplomatic chamber perspective).
* **Bảng màu & Ánh sáng:**
  - Xanh lam Liên Hợp Quốc chuẩn: `#5B92E5`, `#418AB3`.
  - Vàng cành ô liu hòa bình: `#FFD700`, `#E5C158`.
  - Đồng thau bảng tên: `#C5A059`. Vải nỉ nhung phòng họp: `#2C3E50`.
  - Ánh sáng: Chùm đèn trần mái vòm nổi tiếng của phòng họp HĐBA rọi thẳng xuống bảng tên VIET NAM, tạo độ lóa kim loại trang nghiêm tột bậc.
* **Chất cảm vật liệu:** Bảng tên kim loại đồng thau xước mờ cao cấp; nhành lá ô liu chạm khắc vàng tỉ mỉ từng đường gân lá; vách tường gỗ óc chó của khán phòng HĐBA sang trọng.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Bảng tên quốc gia "VIET NAM" bằng đồng thau và chiếc tai nghe phiên dịch đa ngữ.
  - *Trung cảnh:* Biểu trưng cành ô liu vàng ròng ôm trọn quả địa cầu Liên Hợp Quốc phát sáng rực rỡ.
  - *Hậu cảnh:* Bức bích họa nổi tiếng của Per Krohg trên tường phòng họp HĐBA tái hiện sự hồi sinh của nhân loại sau chiến tranh.

### Focus 19: `VIE_multilateral_champion` — Ngọn Cờ Đầu Ngoại Giao Đa Phương & Hòa Giải Quốc Tế
* **Tọa độ & Mốc lịch sử:** (48, 15) | Đỉnh cao vị thế Việt Nam: Đăng cai Thượng đỉnh Mỹ - Triều Hà Nội 2019, phái cử lực lượng gìn giữ hòa bình LHQ (Mũ nồi xanh), tham gia định hình luật chơi quốc tế.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Mũ Nồi Xanh Gìn Giữ Hòa Bình LHQ Mang Quốc Huy Việt Nam & Bồ Câu Trắng Ngậm Nhành Tre Xanh**. Chiếc mũ nồi xanh biểu tượng của lực lượng gìn giữ hòa bình Liên Hợp Quốc gắn huy hiệu Quốc kỳ Việt Nam, bên cạnh chú chim bồ câu trắng tung cánh bay lên, miệng ngậm nhành tre ngà biểu trưng cho hòa bình và chính nghĩa.
* **Bố cục & Phối cảnh:** Góc nhìn ngước cao hào hùng (epic upward perspective), chim bồ câu vút bay từ bàn tay che chở lên vòm trời bao la.
* **Bảng màu & Ánh sáng:**
  - Xanh lam Mũ nồi xanh LHQ: `#0080FF`, `#0059B3`.
  - Trắng tinh khiết bồ câu hòa bình: `#FFFFFF`, bóng xám lông vũ `#D5D8DC`.
  - Xanh tre ngà: `#2E7D32`, nhành tre măng `#7CB342`.
  - Ánh sáng: Ánh bình minh vàng rực chan hòa từ đỉnh trời, tạo viền sáng hào quang (rim lighting) bao quanh đôi cánh chim bồ câu trắng.
* **Chất cảm vật liệu:** Vải nỉ dạ của mũ nồi có độ sần tự nhiên; huy hiệu đồng mạ vàng dập nổi sắc nét; từng sợi lông vũ của cánh chim bồ câu mềm mại tung bay trong gió.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Chiếc mũ nồi xanh Liên Hợp Quốc đặt nghiêng trang trọng bên cạnh cuốn sổ tay điều ước quốc tế.
  - *Trung cảnh:* Chim bồ câu trắng tung cánh sải rộng đón ánh bình minh, ngậm nhành tre xanh vươn mình.
  - *Hậu cảnh:* Quả địa cầu pha lê tỏa sáng với những con đường hòa bình kết nối Việt Nam tới năm châu bốn biển.

---

## TRỤC 4: TRỤC QUAN HỆ ĐỐI NGOẠI VIỆT - MỸ (5 FOCUS)

```text
       VIE_us_engagement (y=12)
                │
VIE_us_comprehensive_partnership (y=13)
                │
     VIE_us_embargo_lifted (y=14)
           ┌────┴────┐
VIE_us_carrier_visit  VIE_us_tariff_deal (y=15)
```

### Focus 20: `VIE_us_engagement` — Bình Thường Hóa Quan Hệ & Khép Lại Quá Khứ (1995 – 2000)
* **Tọa độ & Mốc lịch sử:** (52, 12) | Tuyên bố bình thường hóa 1995, chuyến thăm lịch sử của Tổng thống Bill Clinton 2000, ký kết Hiệp định Thương mại Song phương BTA.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cái Bắt Tay Hữu Nghị Lịch Sử Vượt Thái Bình Dương & Chiếc Cầu Nối Hòa Giải**. Hai bàn tay mạnh mẽ bắt chặt lấy nhau qua mặt biển Thái Bình Dương, cổ tay một bên mang huy hiệu Cờ đỏ sao vàng Việt Nam, một bên mang huy hiệu Cờ Hoa Kỳ, đặt trước nhịp cầu dây văng nối hai bờ đại dương.
* **Bố cục & Phối cảnh:** Bố cục cận cảnh ngang tầm mắt (eye-level close-up hero shot), hai bàn tay siết chặt chiếm trọn vị trí trung tâm thể hiện lòng tin chiến lược bắt đầu đâm chồi.
* **Bảng màu & Ánh sáng:**
  - Đỏ tươi cờ Việt Nam: `#DA251D`, vàng sao `#FFDE23`.
  - Xanh hải quân cờ Mỹ: `#0A3161`, đỏ cờ Mỹ `#B31942`.
  - Ánh sáng rạng đông đại dương: `#F39C12`, `#F1C40F`.
  - Ánh sáng: Nắng sớm xuyên qua màn sương mù chiến tranh, chiếu sáng rực rỡ cái bắt tay hòa giải của hai cựu thù trở thành bạn hữu.
* **Chất cảm vật liệu:** Cúc tay áo vest ngoại giao bằng sừng cẩn xà cừ; huy hiệu cài áo bằng kim loại đúc nổi; sóng biển Thái Bình Dương nhấp nhô bên dưới.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Cây bút máy ký kết hiệp định thương mại song phương mạ vàng Parker.
  - *Trung cảnh:* Hai bàn tay đan chặt khỏe khoắn trong cái bắt tay ngoại giao lịch sử làm thay đổi cục diện thế giới.
  - *Hậu cảnh:* Tấm hải đồ nối liền Hà Nội và Washington qua Thái Bình Dương rực sáng trong ánh bình minh mới.

### Focus 21: `VIE_us_comprehensive_partnership` — Xác Lập Đối Tác Toàn Diện Việt - Mỹ (2013)
* **Tọa độ & Mốc lịch sử:** (52, 13) | Tuyên bố chung tại Nhà Trắng giữa Chủ tịch nước Trương Tấn Sang và Tổng thống Barack Obama tháng 7/2013: Tôn trọng độc lập, chủ quyền, toàn vẹn lãnh thổ và thể chế chính trị của nhau.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Hai Trụ Cột Đối Tác Bằng Đá Cẩm Thạch & Bản Tuyên Bố Chung Mang Dấu Triện Song Phương**. Hai cột trụ đá cẩm thạch trắng phong cách tân cổ điển và hoa sen đỡ lấy mái vòm đối tác chiến lược, ở giữa là tấm bia đồng khắc nguyên tắc vàng: "Tôn trọng thể chế chính trị của nhau".
* **Bố cục & Phối cảnh:** Góc nhìn chính diện từ tiền sảnh Nhà Trắng và Phủ Chủ tịch (monumental architectural perspective).
* **Bảng màu & Ánh sáng:**
  - Trắng cẩm thạch tân cổ điển: `#F4F6F7`, xám bóng `#BDC3C7`.
  - Vàng đồng thau bia tuyên bố: `#D4AF37`, `#9A7D0A`.
  - Xanh navy ngoại giao: `#1A252F`.
  - Ánh sáng: Đèn chùm đại sảnh chiếu rọi đa hướng, tạo các vệt phản quang thanh lịch trên cột đá và nền gạch hoa văn.
* **Chất cảm vật liệu:** Đá cẩm thạch Carrara được đánh bóng loáng phản chiếu ánh đèn; chữ khắc chìm trên bia đồng đổ sơn đen trang nghiêm.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Cặp ly rượu vang nghi lễ pha lê Bohemia dùng trong tiệc chiêu đãi quốc yến.
  - *Trung cảnh:* Hai cột trụ cẩm thạch vững chãi nâng đỡ tấm bia đồng Đối tác Toàn diện 2013.
  - *Hậu cảnh:* Hình bóng Nhà Trắng và Tòa nhà Quốc hội Việt Nam lồng ghép trang trọng trong khung cảnh hòa bình.

### Focus 22: `VIE_us_embargo_lifted` — Dỡ Bỏ Hoàn Toàn Cấm Vận Vũ Khí Sát Thương (2016)
* **Tọa độ & Mốc lịch sử:** (52, 14) | Tổng thống Barack Obama tuyên bố dỡ bỏ hoàn toàn cấm vận vũ khí sát thương đối với Việt Nam trong chuyến thăm Hà Nội tháng 5/2016; bình thường hóa hoàn toàn quan hệ song phương.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Ổ Khóa Xiềng Xích Bị Chặt Đứt Bằng Lưỡi Gươm Công Lý & Cánh Cửa Kho Vũ Khí Hiện Đại Mở Toang**. Một sợi xích sắt dày phong tỏa cấm vận bị cắt đứt làm đôi, các mắt xích vỡ vụn bắn ra tia lửa, để lộ phía sau là bầu trời tự do và những cánh máy bay tuần thám biển hiện đại.
* **Bố cục & Phối cảnh:** Góc chụp hành động bùng nổ (high-impact explosive action perspective), khoảnh khắc mắt xích bị bẻ gãy đập thẳng vào mắt người xem.
* **Bảng màu & Ánh sáng:**
  - Thép xám xích sắt rỉ sét: `#566573`, rỉ sắt `#78281F`.
  - Tia lửa cam vàng bùng nổ: `#FF5722`, `#FFC107`, trắng chói `#FFFFFF`.
  - Xanh lam tự do bầu trời: `#2980B9`, `#85C1E9`.
  - Ánh sáng: Luồng sáng chói lòa từ vết cắt kim loại tỏa ra như tia hồ quang hàn điện, chiếu sáng bừng toàn bộ khung cảnh u ám.
* **Chất cảm vật liệu:** Kim loại xích sắt có vân rỉ sét thô ráp bị gãy vụn; bề mặt thép sáng bóng của thiết bị quốc phòng thế hệ mới bên trong; tia lửa hàn phát sáng chói lọi.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Hai đầu mắt xích sắt dày bị cắt đứt văng ra hai bên, bắn ra các tàn lửa cam đỏ rực rỡ.
  - *Trung cảnh:* Cánh cửa thép bảo vệ mở toang, đón nhận ánh sáng bình minh hòa bình.
  - *Hậu cảnh:* Bầu trời trong xanh với biên đội tuần thám biển sải cánh bảo vệ chủ quyền biển đảo.

### Focus 23: `VIE_us_carrier_visit` — Siêu Hàng Không Mẫu Hạm Hoa Kỳ Thăm Đà Nẵng
* **Tọa độ & Mốc lịch sử:** (52, 15) | Các chuyến thăm lịch sử của tàu sân bay USS Carl Vinson (2018), USS Theodore Roosevelt (2020), USS Ronald Reagan (2023) đến Cảng Tiên Sa, Đà Nẵng.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Siêu Hàng Không Mẫu Hạm Hạt Nhân Lớp Nimitz Cập Cảng Tiên Sa & Tàu Cảnh Sát Biển Việt Nam Dẫn Luồng**. Mũi tàu sân bay khổng lồ màu xám chiến hạm với sàn đáp vĩ đại rẽ sóng tiến vào Vịnh Đà Nẵng, bên mạn tàu là tàu tuần tra hiện đại của Cảnh sát Biển Việt Nam mang Cờ đỏ sao vàng dẫn luồng nghi lễ.
* **Bố cục & Phối cảnh:** Góc nhìn ngước thấp cực kỳ hùng vĩ từ mặt nước biển (heroic sea-level upward shot), lột tả quy mô choáng ngợp của siêu hạm giữa non nước Ngũ Hành Sơn.
* **Bảng màu & Ánh sáng:**
  - Xám chiến hạm hải quân: `#5D6D7E`, `#34495E`.
  - Xanh biếc nước biển Vịnh Đà Nẵng: `#1B4F72`, bọt sóng trắng `#EBF5FB`.
  - Đỏ cam cứu sinh tàu Cảnh sát biển: `#E74C3C`, cờ đỏ sao vàng rực sáng `#DA251D`.
  - Ánh sáng: Ánh nắng trưa nhiệt đới rực rỡ chiếu trên thân thép tàu chiến, tạo vệt bóng đổ đổ dài trên mặt vịnh xanh trong vắt.
* **Chất cảm vật liệu:** Vỏ thép giáp dày đặc của thân tàu sân bay có vết muối biển phong trần; sàn đáp bằng vật liệu chống trượt màu đen nhám; mặt nước biển trong vắt gợn sóng nhấp nhô.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Mũi tàu Cảnh sát biển Việt Nam mang cờ Tổ quốc phấp phới hiên ngang dẫn đường vào cảng.
  - *Trung cảnh:* Thân tàu sân bay hạt nhân khổng lồ với tháp chỉ huy đồ sộ và các máy bay xếp hàng ngay ngắn trên sàn đáp.
  - *Hậu cảnh:* Bán đảo Sơn Trà và núi non Ngũ Hành Sơn xanh ngắt dưới mây trời Đà Nẵng yên bình.

### Focus 24: `VIE_us_tariff_deal` — Thỏa Thuận Biểu Thuế Ưu Đãi & Kinh Tế Thị Trường
* **Tọa độ & Mốc lịch sử:** (54, 15) | Đàm phán công nhận quy chế kinh tế thị trường, thỏa thuận khung thương mại và đầu tư (TIFA), ngăn chặn áp thuế trừng phạt, giữ vững xuất siêu hàng chục tỷ USD.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cán Cân Thương Mại Vàng Ròng Cân Bằng & Chiếc Khiên Miễn Trừ Thuế Quan Bảo Hộ Hàng Hóa**. Chiếc cân công lý thương mại bằng vàng ròng đạt trạng thái cân bằng tuyệt đối giữa thỏi vàng dự trữ và thùng hàng hóa xuất khẩu công nghệ cao (Made in Vietnam), che chở bởi chiếc khiên hiệp định khắc biểu trưng đại bàng và rồng vàng.
* **Bố cục & Phối cảnh:** Bố cục cân bằng động học (dynamic equilibrium composition), góc nhìn 3/4 từ trên xuống làm nổi bật sự ổn định tài chính bền vững.
* **Bảng màu & Ánh sáng:**
  - Vàng kim thỏi vàng & cán cân: `#F1C40F`, `#B7950B`.
  - Xanh lục đồng đô-la & tăng trưởng: `#27AE60`, xanh két `#1E8449`.
  - Bạc thép của thùng hàng container: `#BDC3C7`.
  - Ánh sáng: Ánh sáng trường quay tài chính chuyên nghiệp, tạo các đường viền sáng sắc nét trên đĩa cân và khối kim loại quý.
* **Chất cảm vật liệu:** Vàng ròng đúc thỏi có độ bóng gương siêu thực; thùng hàng container bằng hợp kim nhôm dập sóng gân guốc; con dấu hải quan bằng sáp đỏ nổi bật.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Con dấu hải quan "0% TARIFF EXEMPTED" bằng đồng đỏ đóng trên vận đơn quốc tế.
  - *Trung cảnh:* Chiếc cân vàng ròng cân bằng hoàn hảo giữa hàng hóa công nghệ cao Việt Nam và đồng tiền thanh toán thương mại quốc tế.
  - *Hậu cảnh:* Cảng biển nước sâu quốc tế Cái Mép - Thị Vải tấp nập những siêu tàu chở hàng vươn khơi sang bờ Tây nước Mỹ.

---

## TRỤC 5: ĐỐI TÁC CHIẾN LƯỢC TOÀN DIỆN & NGOẠI GIAO CÂY TRE (9 FOCUS)

```text
VIE_japan_partnership (y=12)
           │
           ├────────────────────────┬────────────────────────┐
VIE_korea_partnership (y=13)  VIE_india_partnership (y=13) VIE_australia_partnership (y=13)  VIE_france_eu (y=13)
           │                        │                        │
VIE_gulf_investment (y=14)   VIE_csp_network (y=14)    VIE_global_south_ties (y=14)
                                    │
                         VIE_bamboo_diplomacy (y=15) [CAPSTONE]
```

### Focus 25: `VIE_japan_partnership` — Đối Tác Chiến Lược Sâu Rộng Việt - Nhật
* **Tọa độ & Mốc lịch sử:** (58, 12) | Nguồn vốn ODA lớn nhất, cầu Nhật Tân, hầm Hải Vân, đường sắt đô thị, hợp tác công nghiệp hóa và an ninh hàng hải.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cầu Nhật Tân Dây Văng Lung Linh Bên Rừng Hoa Anh Đào & Cành Mai Vàng Giao Duyên**. Cây cầu dây văng 5 trụ tháp biểu tượng hữu nghị bắc qua sông Hồng rực sáng trong đêm, bao quanh bởi nhành hoa Anh đào (Sakura) hồng phấn Nhật Bản đan cài duyên dáng cùng nhành hoa Mai vàng phương Nam.
* **Bố cục & Phối cảnh:** Phối cảnh đêm lung linh huyền ảo (atmospheric nightscape with depth), góc máy ngắm qua nhành hoa Anh đào nhìn về phía cầu dây văng rực rỡ.
* **Bảng màu & Ánh sáng:**
  - Hồng phấn hoa anh đào: `#FADBD8`, `#F1948A`.
  - Vàng mai vàng phương Nam: `#F7DC6F`, `#F4D03F`.
  - Xanh tím than đêm sông Hồng: `#1B2631`, đèn LED cầu ngũ sắc `#E74C3C`, `#3498DB`, `#2ECC71`.
  - Ánh sáng: Hệ thống chiếu sáng mỹ thuật LED hiện đại của cầu Nhật Tân phản chiếu rực rỡ trên mặt nước sông Hồng êm đềm.
* **Chất cảm vật liệu:** Cánh hoa anh đào mỏng manh e ấp; dây văng thép cầu căng tràn sức sống hiện đại; mặt nước sông Hồng phản chiếu ánh sáng lung linh như dát ngọc.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Nhành hoa Sakura hồng tươi đan cài nhành hoa Mai vàng rực khoe sắc bên góc khung hình.
  - *Trung cảnh:* Cây cầu Nhật Tân 5 trụ tháp vươn cao kiêu hãnh với luồng xe cộ hối hả qua lại.
  - *Hậu cảnh:* Ngọn núi Phú Sĩ tuyết phủ mờ ảo hòa quyện cùng hình bóng tháp Rùa Hà Nội trong vầng trăng hữu nghị.

### Focus 26: `VIE_korea_partnership` — Đối Tác Hợp Tác Chiến Lược Việt - Hàn
* **Tọa độ & Mốc lịch sử:** (56, 13) | Nhà đầu tư FDI lớn nhất (Samsung, LG, Hyundai), trung tâm sản xuất thiết bị công nghệ cao, bán dẫn và giao lưu nhân dân sâu sắc.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Tấm Wafer Vi Mạch Bán Dẫn Khắc Bản Đồ Công Nghệ & Hoa Trống Đồng Hòa Quyện Biểu Tượng Thái Cực (Taegeuk)**. Tấm wafer silicon bán dẫn tròn óng ánh 7 sắc cầu vồng, trên bề mặt chạm khắc các mạch điện tử nano hình Trống đồng Đông Sơn và biểu tượng vòng tròn âm dương đỏ - xanh Taegeuk của Hàn Quốc.
* **Bố cục & Phối cảnh:** Góc chụp macro công nghệ cao (high-tech macro futuristic shot), tấm wafer silicon nghiêng 45 độ đón chùm tia laser quang khắc cực tím.
* **Bảng màu & Ánh sáng:**
  - Bảy sắc cầu vồng wafer silicon: `#5DADE2`, `#AF7AC5`, `#58D68D`, `#F4D03F`.
  - Đỏ âm dương Taegeuk: `#C0392B`, xanh dương Taegeuk: `#1F618D`.
  - Ánh sáng laser quang khắc UV: Tím neon `#8E44AD` và xanh điện tử `#00FFFF`.
  - Ánh sáng: Chùm tia laser quang khắc chiếu thẳng góc vào tâm chip bán dẫn, tạo hiệu ứng phát quang rực rỡ trên các vi mạch nano.
* **Chất cảm vật liệu:** Silicon tinh khiết đánh bóng gương phản chiếu màu sắc giao thoa quang học; dây vi mạch nano mạ vàng óng ánh; bàn nâng robot phòng sạch bằng thép không gỉ.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Cánh tay robot tự động của phòng sạch công nghệ cao đang kẹp tấm vi mạch bán dẫn.
  - *Trung cảnh:* Tấm wafer vi mạch silicon khắc họa biểu tượng đối tác công nghệ chiến lược Việt - Hàn tỏa sáng.
  - *Hậu cảnh:* Tổ hợp công nghệ cao Bắc Ninh / Thái Nguyên / Hải Phòng hiện đại rực sáng đèn đêm sản xuất.

### Focus 27: `VIE_india_partnership` — Đối Tác Chiến Lược Toàn Diện Việt - Ấn
* **Tọa độ & Mốc lịch sử:** (58, 13) | Hợp tác quốc phòng chiến lược (tên lửa BrahMos, tàu tuần tra, radar), thăm dò dầu khí thềm lục địa Biển Đông, gắn kết Phật giáo và văn minh Chăm-pa.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Bánh Xe Pháp Luân Ashoka Bằng Đồng Cổ Đặt Cạnh Bệ Phóng Tên Lửa Siêu Thanh BrahMos**. Bánh xe luân hồi Ashoka Chakra 24 nan hoa bằng đồng đúc đặt uy nghiêm trước bệ phóng tên lửa hành trình bờ đối hạm siêu âm BrahMos, phía sau là tháp Chàm Mỹ Sơn cổ kính linh thiêng.
* **Bố cục & Phối cảnh:** Bố cục kết hợp giữa chiều sâu tâm linh lịch sử và sức mạnh răn đe quốc phòng hiện đại (heritage & deterrent perspective).
* **Bảng màu & Ánh sáng:**
  - Nâu đỏ gạch nung tháp Chàm: `#A93226`, `#922B21`.
  - Đồng cổ bánh xe Ashoka: `#7D6608`, vàng đồng `#B7950B`.
  - Xám quân sự ống phóng tên lửa: `#2C3E50`. Xanh hải quân Ấn Độ Dương: `#1B4F72`.
  - Ánh sáng: Ánh hoàng hôn vàng đỏ rực rỡ chiếu rọi qua nan hoa bánh xe Ashoka, đổ bóng uy dũng xuống bãi phóng tên lửa hướng ra Biển Đông.
* **Chất cảm vật liệu:** Gạch nung tháp cổ không mạch vữa có độ thô nhám ngàn năm; đồng thau đúc cổ có vết chạm khắc thủ công; composite ống phóng tên lửa quân sự hiện đại.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Bánh xe Ashoka Chakra bằng đồng mạ vàng xoay nhẹ, tỏa ra năng lượng hòa bình và công lý.
  - *Trung cảnh:* Bệ phóng tên lửa bờ đối hạm BrahMos hướng nòng kiêu hãnh bảo vệ chủ quyền thềm lục địa.
  - *Hậu cảnh:* Tháp cổ Mỹ Sơn trầm mặc soi bóng bên dòng sông Thu Bồn nối ra biển lớn.

### Focus 28: `VIE_australia_partnership` — Đối Tác Chiến Lược Toàn Diện Việt - Úc
* **Tọa độ & Mốc lịch sử:** (60, 13) | Nâng cấp Đối tác Chiến lược Toàn diện 2024; hợp tác giáo dục, khoáng sản thiết yếu, chuyển dịch năng lượng xanh và an ninh hàng hải.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Chòm Sao Nam Thập Tự Rực Sáng Bên Ngọn Hải Đăng & Máy Bay Tuần Thám Biển P-8A Poseidon**. Chòm sao Nam Thập Tự (Southern Cross) bằng bạc lấp lánh trên vòm trời đêm phương Nam, soi rọi phi cơ tuần thám biển P-8A đang bay lượn hộ tống tàu nghiên cứu hải dương học xanh.
* **Bố cục & Phối cảnh:** Góc nhìn ngước bầu trời đêm đại dương bao la (celestial oceanic perspective), tôn vinh sự kết nối hai đại dương Ấn Độ Dương - Thái Bình Dương.
* **Bảng màu & Ánh sáng:**
  - Xanh thẳm bầu trời đêm Nam Bán Cầu: `#0B132B`, `#1C2541`.
  - Bạc sáng tinh tú chòm sao: `#FFFFFF`, ánh hào quang bạc `#E0E1DD`.
  - Xanh lá cây lục bảo năng lượng xanh: `#2EC4B6`.
  - Ánh sáng: 5 ngôi sao của chòm Nam Thập Tự phát sáng lấp lánh như kim cương, phản chiếu ánh sáng lân tinh trên mặt nước đại dương.
* **Chất cảm vật liệu:** Bạc nguyên chất của các ngôi sao dập nổi; kim loại thân máy bay tuần thám có độ bóng mờ hàng không chuyên dụng; nước biển đêm sâu thẳm huyền bí.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* La bàn hải quân mạ bạc khắc họa bản đồ Ấn Độ Dương - Thái Bình Dương.
  - *Trung cảnh:* Máy bay tuần thám biển tầm xa sải cánh dũng mãnh bảo vệ tự do hàng hải.
  - *Hậu cảnh:* Chòm sao Nam Thập Tự rực sáng dẫn đường trên nền trời phương Nam tĩnh mịch.

### Focus 29: `VIE_france_eu` — Ngoại Giao Việt - Pháp & Hiệp Định Thương Mại Tự Do EVFTA
* **Tọa độ & Mốc lịch sử:** (62, 13) | Ký kết EVFTA & EVIPA 2019-2020; đối tác thương mại hàng đầu châu Âu; nâng cấp Đối tác Chiến lược Toàn diện với Pháp 2024; giao thoa văn hóa - kiến trúc Pháp - Việt.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cổng Khải Hoàn Môn Cẩm Thạch & Nhà Hát Lớn Hà Nội Lồng Ghép Dưới Vòng Ngôi Sao Vàng EU**. Cổng vòm kiến trúc kinh điển phong cách Pháp giao thoa với Nhà Hát Lớn Hà Nội, phía trên là vòng tròn 12 ngôi sao vàng Liên minh Châu Âu ôm trọn bản đồ Việt Nam và dòng chữ EVFTA.
* **Bố cục & Phối cảnh:** Bố cục kiến trúc tráng lệ hoa lệ (grand neoclassical architectural composition), góc nhìn 3/4 ngước lên tôn vinh sự tinh tế và bề thế.
* **Bảng màu & Ánh sáng:**
  - Vàng kim ngôi sao EU: `#FFCC00`, xanh lam cờ Châu Âu: `#003399`.
  - Vàng hoàng yến kiến trúc Pháp Hà Nội: `#F4D03F`, `#D4AC0D`.
  - Trắng đá vôi Khải Hoàn Môn: `#EAEDED`.
  - Ánh sáng: Ánh hoàng hôn châu Âu thanh lịch vàng ấm hòa quyện với ánh đèn trang trí rực rỡ của Nhà Hát Lớn.
* **Chất cảm vật liệu:** Vữa gai vàng đặc trưng của các công trình kiến trúc Pháp cổ tại Hà Nội; đá vôi Paris chạm trổ phù điêu tinh xảo; các ngôi sao kim loại vàng rực rỡ.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Bút lông ký kết văn kiện hiệp định thương mại tự do và con dấu sáp vàng châu Âu.
  - *Trung cảnh:* Vòm cổng kiến trúc giao thoa Pháp - Việt tráng lệ với 12 ngôi sao vàng EU tỏa sáng.
  - *Hậu cảnh:* Tháp Eiffel Paris mờ ảo trong sương chiều nối liền với Cầu Long Biên lịch sử trăm năm.

### Focus 30: `VIE_gulf_investment` — Dòng Vốn Đầu Tư Vùng Vịnh & Trung Đông
* **Tọa độ & Mốc lịch sử:** (56, 14) | Thu hút các quỹ đầu tư quốc gia hùng mạnh (ADIA, PIF, QIA); hiệp định CEPA với UAE; đầu tư cảng biển nước sâu, trung tâm dữ liệu, bất động sản và hóa dầu.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Tòa Tháp Tài Chính Hiện Đại Vươn Cao & Chiếc Thuyền Buồm Dhow Ả Rập Rẽ Sóng Vàng**. Một tòa tháp chọc trời kiến trúc kính và thép tương lai vươn thẳng lên trời cao, chân tháp là chiếc thuyền buồm Dhow truyền thống vùng Vịnh chở đầy rương vàng đầu tư tiến vào bến cảng Việt Nam.
* **Bố cục & Phối cảnh:** Góc nhìn ngước chọc trời (extreme upward skyscraper perspective), thể hiện dòng vốn khổng lồ hàng tỷ USD đang đổ bộ vào hạ tầng kinh tế.
* **Bảng màu & Ánh sáng:**
  - Vàng sa mạc và kim tiền: `#D4AF37`, `#F39C12`, `#B7950B`.
  - Xanh ngọc bích vịnh Ba Tư: `#00A86B`, `#117864`.
  - Xanh kính phản quang cao ốc: `#5DADE2`, `#2E86C1`.
  - Ánh sáng: Nắng vàng sa mạc rực rỡ phản chiếu lóa mắt trên các mặt kính cường lực của tòa cao ốc tài chính.
* **Chất cảm vật liệu:** Kính phản quang tòa nhà cao tầng có độ trong suốt và phản chiếu mây bay; gỗ tếch đóng thuyền buồm phong sương; vàng ròng trong các rương kho báu đầu tư lấp lánh.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Chiếc ấn tín mạ vàng chạm khắc hoa văn thư pháp Ả Rập đóng trên hợp đồng đầu tư hạ tầng tỷ USD.
  - *Trung cảnh:* Tòa tháp trung tâm tài chính quốc tế vươn cao với kiến trúc kính xanh lộng lẫy.
  - *Hậu cảnh:* Cảng cẩu giàn container hiện đại đón những siêu tàu dầu và hàng hóa xuyên lục địa cập bến.

### Focus 31: `VIE_global_south_ties` — Thắt Chặt Gắn Kết Với Nam Bán Cầu (Global South)
* **Tọa độ & Mốc lịch sử:** (60, 14) | Mạng lưới viễn thông Viettel tại Châu Phi và Mỹ Latinh; xuất khẩu gạo bảo đảm an ninh lương thực; tình đoàn kết phong trào Không Liên Kết (NAM) và Cuba anh em.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Cột Tháp Viễn Thông Phát Sóng 5G Vươn Cao Giữa Bình Nguyên Châu Phi & Bông Lúa Vàng Việt Nam Cứu Đói**. Một cột ăng-ten trạm phát sóng viễn thông hiện đại phát ra các vòng sóng vô tuyến màu xanh ngọc lan tỏa khắp thảo nguyên, bên dưới là bàn tay người nông dân nâng niu bó lúa vàng Việt Nam trĩu hạt.
* **Bố cục & Phối cảnh:** Góc nhìn bao quát thảo nguyên bao la (panoramic savanna perspective), kết hợp công nghệ viễn thông hiện đại và tình nghĩa thủy chung quốc tế.
* **Bảng màu & Ánh sáng:**
  - Nâu đất đỏ châu Phi: `#A04000`, vàng cỏ xavan `#D4AC0D`.
  - Xanh sóng vô tuyến viễn thông: `#00E5FF`, `#0091EA`.
  - Vàng óng lúa chín Việt Nam: `#FFD700`, đỏ thắm cờ hữu nghị `#C0392B`.
  - Ánh sáng: Ánh hoàng hôn xavan rực đỏ hùng vĩ, vầng thái dương khổng lồ lặn sau bóng cây bao-báp và tháp ăng-ten.
* **Chất cảm vật liệu:** Thép giàn không gian mạ kẽm của cột phát sóng viễn thông; hạt lúa căng tròn bóng mẩy; đất đỏ bazan nứt nẻ được tưới mát bởi tình bạn quốc tế.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Bàn tay siết chặt đầy tình nghĩa giữa công nhân kỹ thuật Việt Nam và người dân bản địa châu Phi.
  - *Trung cảnh:* Tháp phát sóng viễn thông công nghệ cao phát ra các luồng sóng dữ liệu kết nối toàn cầu.
  - *Hậu cảnh:* Vùng thảo nguyên bao la với cây bao-báp cổ thụ và cánh đồng lúa xanh tốt vươn mình dưới nắng mới.

### Focus 32: `VIE_csp_network` — Mạng Lưới Đối Tác Chiến Lược Toàn Diện Toàn Cầu
* **Tọa độ & Mốc lịch sử:** (58, 14) | Thiết lập mạng lưới Đối tác Chiến lược Toàn diện (CSP) với tất cả 5 nước Thường trực HĐBA LHQ và các cường quốc hàng đầu (Trung, Nga, Ấn, Hàn, Mỹ, Nhật, Úc, Pháp...); vị thế đan xen lợi ích vững như bàn thạch.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Quả Cầu Địa Cầu Bằng Pha Lê Khắc Mạng Lưới Kinh Tuyến Vàng Nối Các Thủ Đô & Quốc Huy Việt Nam Làm Trung Tâm Tỏa Sáng**. Quả địa cầu pha lê trong suốt với các luồng sáng vàng kim kết nối Hà Nội tới Washington, Bắc Kinh, Moscow, Tokyo, New Delhi, Seoul, Canberra, Paris, London...
* **Bố cục & Phối cảnh:** Bố cục trung tâm vũ trụ ngoại giao (geopolitical nucleus composition), quả cầu pha lê chiếm trọn trung tâm với các luồng sáng laser tỏa ra tứ phía.
* **Bảng màu & Ánh sáng:**
  - Xanh ngọc bích đại dương pha lê: `#0E6655`, `#16A085`.
  - Vàng kim các mạng lưới kết nối: `#FFD700`, `#F39C12`.
  - Đỏ son quốc huy trung tâm: `#900C3F`.
  - Ánh sáng: Tâm quả cầu tại tọa độ Việt Nam phát ra chùm sáng đa sắc cực mạnh, chiếu sáng các nút giao mạng lưới trên toàn cầu.
* **Chất cảm vật liệu:** Pha lê quang học khúc xạ ánh sáng đa chiều; đường dây cáp quang kết nối bằng vàng sáng bóng; đế nâng đỡ quả cầu bằng đá thạch anh đen tuyền.
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Vành kim loại xích đạo của giá đỡ quả cầu khắc tên các thủ đô đối tác chiến lược bằng chữ mạ vàng.
  - *Trung cảnh:* Quả cầu pha lê địa chính trị với mạng lưới ánh sáng CSP đan xen chằng chịt bảo vệ lợi ích quốc gia.
  - *Hậu cảnh:* Bản đồ thế giới chiếu chìm trong không gian vũ trụ sâu thẳm lấp lánh các vì sao hòa bình.

### Focus 33: `VIE_bamboo_diplomacy` — Bản Lĩnh Ngoại Giao Cây Tre Việt Nam (CAPSTONE FOCUS)
* **Tọa độ & Mốc lịch sử:** (58, 15) | Đỉnh cao tư tưởng đối ngoại thời đại Hồ Chí Minh: **"Gốc vững, thân chắc, cành uyển chuyển"** — Kiên định về nguyên tắc, linh hoạt về sách lược, đứng vững trước mọi cơn bão địa chính trị.
* **Ẩn dụ cốt lõi & Vật thể trung tâm:** **Khóm Tre Ngà Đại Thụ Bằng Vàng Ròng & Ngọc Bích Đứng Sừng Sững Giữa Cơn Bão Địa Chính Trị Toàn Cầu**. Khóm tre ngà Việt Nam với bộ rễ cắm sâu nghìn năm vào lòng đất mẹ (đá hoa cương nguyên khối), thân tre dẻo dai kết thành lũy thép, cành lá xanh biếc uyển chuyển uốn lượn theo chiều gió bão nhưng không bao giờ gãy đổ, nâng niu Quốc kỳ Cờ đỏ sao vàng trên đỉnh ngọn tre cao vút.
* **Bố cục & Phối cảnh:** Góc nhìn ngước nhìn vĩ đại từ chân gốc tre lên đỉnh trời cao (epic vertical low-angle shot), lột tả khí phách hiên ngang, dẻo dai bất khuất của dân tộc Việt Nam trước phong ba thời đại.
* **Bảng màu & Ánh sáng:**
  - Xanh ngọc bích lá tre và thân tre non: `#1E8449`, `#27AE60`, xanh lục thẫm `#145A32`.
  - Vàng ngà thân tre già và rễ tre: `#F4D03F`, `#D4AC0D`, vàng kim rực rỡ `#FFD700`.
  - Đỏ rực cờ Tổ quốc đỉnh tre: `#DA251D`, sao vàng `#FFDE23`.
  - Xám đen bão tố địa chính trị: `#2C3E50`, `#1B2631`.
  - Ánh sáng: Một luồng sáng thiên đỉnh thần thánh (heavenly spotlight) rẽ toang mây đen bão tố, chiếu thẳng xuống khóm tre ngà, làm bừng sáng từng giọt sương mai đọng trên lá tre lấp lánh như kim cương.
* **Chất cảm vật liệu:** Thân tre có các đốt tre vàng óng ả với thớ gỗ dẻo dai phản chiếu ánh sáng tự nhiên; rễ tre bện chặt như dây cáp đồng cổ thụ cắm sâu vào tảng đá granite biên cương; lá tre mềm mại như lụa nhưng sắc bén như gươm bảo vệ độc lập; mây bão cuồn cuộn có độ sâu thể tích 3D (volumetric storm clouds).
* **Kể chuyện 3 lớp không gian:**
  - *Tiền cảnh:* Bộ rễ tre đại thụ cuồn cuộn bện chặt bám sâu vào khối đá hoa cương biên giới khắc dòng chữ "Độc lập - Tự chủ - Tự cường".
  - *Trung cảnh:* Thân khóm tre kết đoàn thành lũy vững chãi, cành lá uốn cong mềm mại đón gió bão nhưng giữ vững tâm trục thẳng đứng kiên định.
  - *Hậu cảnh:* Những cơn sóng gió bão táp sấm sét địa chính trị gầm thét dữ dội ở hai bên rìa, nhưng bị đẩy lùi trước ánh bình minh rạng rỡ phía sau khóm tre Việt Nam.
* **Ý nghĩa đỉnh cao:** Đây là biểu tượng tối thượng của toàn bộ nhánh ngoại giao. Xóa bỏ hoàn toàn định kiến về những hình vẽ phẳng thô sơ; mang lại một kiệt tác hội họa kỹ thuật số thể hiện trọn vẹn hồn cốt dân tộc, tư tưởng lớn của Chủ tịch Hồ Chí Minh và bản lĩnh ngoại giao Việt Nam trong kỷ nguyên vươn mình.

---

## 4. Bảng Tổng Hợp Thông Số Thiết Kế 34 Focus

| STT | Focus ID | Tên Tiêu Điểm | Vật Thể Trung Tâm (Centerpiece) | Tông Màu Chủ Đạo | Bố Cục Không Gian |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **01** | `VIE_asean_integration` | Đường lối Đối ngoại | La bàn thiên văn vàng & Bó lúa ASEAN | Vàng kim / Đỏ thắm / Xanh ngọc | 3/4 Isometric 45° |
| **02** | `VIE_gulf_of_tonkin` | Phân định Vịnh Bắc Bộ | Hải đồ da vịnh & Com-pa đồng hàng hải | Xanh biển / Đồng thau / Bạc sóng | Xéo điện ảnh low-angle |
| **03** | `VIE_border_settlement` | Phân giới Cắm mốc Đất liền | Cột mốc đá hoa cương gắn Quốc huy vàng | Xám granite / Đỏ son / Vàng kim | Low-angle ngước nhìn |
| **04** | `VIE_16_words` | Phương châm 16 chữ | Thư tịch sơn mài đỏ dát vàng & Cành trúc | Đỏ sơn mài / Nhũ vàng / Ngọc bích | Cân xứng trang trọng 15° |
| **05** | `VIE_border_trade_gates` | Cửa khẩu Thương mại | Cổng vòm Hữu Nghị & Đoàn xe container | Thép xanh / Cam rực / Kính phản quang | Một điểm tụ perspective |
| **06** | `VIE_defence_hotline` | Đường dây nóng Quốc phòng | Điện thoại mật mã đỏ & Sóng radar xanh | Đỏ son bảo mật / Xanh neon / Crôm | Cận cảnh macro 45° |
| **07** | `VIE_shared_future` | Cộng đồng Chia sẻ Tương lai | Cầu dây văng tương lai & Hai búp sen | Lam ngọc / Vàng kim / Trắng dự ứng lực | Siêu rộng từ mặt nước |
| **08** | `VIE_special_relations_laos` | Quan hệ Đặc biệt Việt - Lào | Tháp vàng Pha That Luang & Hoa Champa | Vàng tháp / Trắng hoa / Xanh Trường Sơn | Chính diện 3 lớp sâu |
| **09** | `VIE_cambodia_relations` | Quan hệ Việt Nam - Campuchia | Tháp đá Angkor Wat & Dòng sông Mê Kông | Sa thạch / Nâu phù sa / Vàng Chùa Tháp | 3/4 bờ sông Angkor |
| **10** | `VIE_mekong_commission` | Ủy hội Sông Mê Kông | Quả cầu nước pha lê & Bàn tay sinh thái | Xanh lam ngọc / Vàng phù sa / Nhôm trắng | Bố cục tròn circular |
| **11** | `VIE_cambodia_border` | Cắm mốc Biên giới Campuchia | Cột mốc 275 & Bản đồ dấu sáp đỏ | Xám tro / Đỏ dấu sáp / Đồng thau | Chéo góc 30° cận cảnh |
| **12** | `VIE_mekong_dams_response` | Ứng phó Đập Thượng nguồn | Bức tường đập bê tông & Tablet viễn thám | Xám bê tông / Đỏ cảnh báo / Xanh lục | Đối chọi split-view |
| **13** | `VIE_funan_techo_response` | Ứng phó Kênh Phù Nam Techo | Sa bàn kênh đào 3D & Kính ngắm laser | Nâu đất / Xanh sông / Đỏ tia laser | Isometric viễn thám |
| **14** | `VIE_indochina_solidarity` | Đoàn kết Đông Dương | Khiên đồng tam giác & Đuốc ba ngọn lửa | Đồng đỏ cổ / Lửa cam vàng / Xanh núi | Tam giác vững chãi |
| **14b**| `VIE_indochina_federation` | Liên bang Đông Dương | Vương miện ba ngôi sao & Kiếm hòa bình | Đỏ hoàng gia / Vàng kim / Bạch kim | Vương quyền chính trực |
| **15** | `VIE_asean_chair` | Năm Chủ tịch ASEAN | Búa điều hành gỗ mun & 10 dải lúa vàng | Xanh ASEAN / Vàng lúa / Đen xà cừ | Cận cảnh bàn chủ tịch |
| **16** | `VIE_code_of_conduct` | Bộ Quy tắc Ứng xử Biển Đông | Văn bản da COC & Hải đăng Trường Sa | Xanh Biển Đông / Vàng quét đèn / Bọt sóng | Bão tố kịch tính |
| **17** | `VIE_apec_host` | Đăng cai APEC | Địa cầu 21 tia sáng & Lụa tơ tằm vàng | Vàng hoàng yến / Xanh Thái Bình Dương | Xoáy tròn động lực |
| **18** | `VIE_un_security_council` | Ủy viên HĐBA LHQ | Ghế bọc nhung HĐBA & Cành ô liu vàng | Xanh UN / Vàng ô liu / Đồng bảng tên | Khán phòng ngoại giao |
| **19** | `VIE_multilateral_champion` | Quốc gia Đa phương Uy tín | Mũ nồi xanh LHQ & Bồ câu ngậm nhành tre | Xanh mũ nồi / Trắng bồ câu / Xanh tre ngà | Ngước cao hào hùng |
| **20** | `VIE_us_engagement` | Bình thường hóa Việt - Mỹ | Bắt tay vượt đại dương & Cầu nối hòa giải | Đỏ cờ VN / Xanh navy Mỹ / Vàng bình minh | Ngang tầm mắt hero shot |
| **21** | `VIE_us_comprehensive_partnership`| Đối tác Toàn diện với Mỹ | Hai cột trụ cẩm thạch & Bia đồng tuyên bố | Trắng cẩm thạch / Vàng bia đồng / Xanh nỉ | Chính diện tiền sảnh |
| **22** | `VIE_us_embargo_lifted` | Dỡ bỏ Cấm vận Vũ khí | Xiềng xích sắt bị chặt đứt & Cửa thép mở | Xám xích rỉ / Tia lửa cam chói / Xanh trời | Hành động bùng nổ |
| **23** | `VIE_us_carrier_visit` | Tàu sân bay Mỹ ở Đà Nẵng | Siêu hàng không mẫu hạm & Tàu CSB dẫn luồng | Xám chiến hạm / Xanh biển Đà Nẵng / Đỏ cờ | Mặt nước ngước nhìn |
| **24** | `VIE_us_tariff_deal` | Khung Thuế quan với Mỹ | Cân vàng thương mại & Khiên miễn thuế | Vàng thỏi / Xanh đô-la / Bạc container | Cân bằng động học 3/4 |
| **25** | `VIE_japan_partnership` | Đối tác Chiến lược Nhật Bản | Cầu Nhật Tân đêm & Hoa Anh đào đan Mai | Hồng sakura / Vàng mai / Xanh tím than | Đêm lung linh lãng mạn |
| **26** | `VIE_korea_partnership` | Đối tác Chiến lược Hàn Quốc | Wafer bán dẫn 7 sắc & Trống đồng Taegeuk | 7 sắc silicon / Đỏ xanh Taegeuk / Tím UV | Macro công nghệ cao 45° |
| **27** | `VIE_india_partnership` | Đối tác Chiến lược Ấn Độ | Bánh xe Ashoka Chakra & Tên lửa BrahMos | Nâu tháp Chàm / Vàng đồng / Xám quân sự | Di sản kết hợp răn đe |
| **28** | `VIE_australia_partnership` | Đối tác Chiến lược Úc | Chòm sao Nam Thập Tự bạc & Máy bay P-8A | Xanh đêm Nam Cực / Bạc sao / Xanh ngọc | Vòm trời đêm đại dương |
| **29** | `VIE_france_eu` | Pháp & Liên minh Châu Âu | Khải Hoàn Môn & 12 ngôi sao vàng EU | Vàng sao EU / Xanh Châu Âu / Vàng Hà Nội | Cổ điển tân cổ điển |
| **30** | `VIE_gulf_investment` | Vốn từ Vùng Vịnh | Tháp tài chính chọc trời & Thuyền Dhow vàng | Vàng kim tiền / Xanh vịnh / Xanh cao ốc | Ngước chọc trời cao |
| **31** | `VIE_global_south_ties` | Thắt chặt Nam Bán Cầu | Tháp phát sóng 5G Viettel & Thảo nguyên Phi | Đất đỏ xavan / Xanh sóng 5G / Vàng lúa chín | Toàn cảnh thảo nguyên |
| **32** | `VIE_csp_network` | Mạng lưới Đối tác Toàn diện | Địa cầu pha lê khắc mạng lưới vàng CSP | Xanh pha lê / Vàng mạng lưới / Đỏ quốc huy | Tâm điểm địa chính trị |
| **33** | `VIE_bamboo_diplomacy` | Bản Lĩnh Ngoại Giao Cây Tre | Khóm tre ngà bão tố & Cờ đỏ sao vàng đỉnh | Xanh ngọc tre / Vàng ngà / Đỏ sao vàng | Ngước nhìn vĩ đại epic |

---

*Chuyển sang đọc [Tập 4: Giải Pháp Công Nghệ & Quy Trình Sản Xuất Mỹ Thuật](./04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md) để tìm hiểu quy trình kỹ thuật chuyển hóa các ý tưởng này thành tài nguyên game DDS chuẩn xác.*
