---
name: md-art
description: 'Cẩm nang và quy trình sản xuất đồ họa toàn diện Millennium Dawn Vietnam: Focus icons (93x91 DDS 33.980B), Ideas/National Spirits (60x68), Decisions/Categories (33x32 TGA / 64x64 DDS), Event pictures (210x176), Portraits (156x210) và UI/BoP/MIO.'
---

# Cẩm nang Mỹ thuật & Đồ họa Toàn diện (MD Vietnam Art Pipeline)

Dùng cho mọi công việc thiết kế, tạo mới, chỉnh sửa, xuất file và tích hợp tài nguyên đồ họa trong mod:
từ icon National Focus, National Spirit (Idea), Quyết sách (Decision), ảnh Sự kiện (Event), Chân dung nhân vật (Portrait), đến Giao diện (UI, BoP, MIO, Cờ).

Tài liệu phong cách chuyên sâu: [`.claude/docs/art-style-guide/README.md`](../../docs/art-style-guide/README.md).

---

## 1. Triết lý Thiết kế Cốt lõi & Khoa học Màu sắc (Color Science)

1. **Ánh sáng 3 nguồn Chiaroscuro chuẩn Paradox:**
   - **Key Light (Nguồn chính):** Góc trên bên trái ($10$–$11$ giờ), màu vàng nắng ấm áp (`#FFF2A3` hoặc `#FFE58F`), tạo điểm sáng specular highlight rõ rệt trên kim loại/vải.
   - **Fill Light (Nguồn phụ):** Góc dưới bên phải ($4$–$5$ giờ), phản quang xanh thép hoặc đất nung lạnh (`#5D7A88`), giữ chi tiết vùng tối.
   - **Rim Light (Nguồn ven viền):** Viền sáng mỏng tách chủ thể khỏi nền giao diện tối.
2. **Kim loại tả thực (Non-Metallic Metal - NMM):**
   - Vàng đồng thau, vàng ròng, thép tôi, đá granite được vẽ chuyển sắc tương phản cao (từ nâu sẫm `#3D2608` đến vàng sáng `#FFF9A5`), không dùng màu gradient đơn điệu.
3. **Biểu tượng Văn hóa & Nhà nước Việt Nam chuẩn xác:**
   - **Quốc kỳ / Cờ Đảng:** Tỷ lệ sao vàng đúng Hiến pháp 2013 (sao $2/3$ chiều rộng cờ, tâm sao trùng tâm cờ, 5 cánh đều, hướng thẳng lên trời). Màu đỏ thắm `#DA251D`, vàng tươi `#FFDE23`.
   - **Hoa sen, Bó lúa, Đốt tre:** Tả thực gân lá, khớp đốt tre, không vẽ cách điệu hoạt hình phẳng.
4. **Không mờ nhòe — Unsharp Mask:** Mọi ảnh sau khi downscale xuống kích thước game phải được chạy bộ lọc **Unsharp Mask ($150\%-180\%$, threshold 1)** để giữ cạnh viền sắc sảo.

---

## 2. Bảng Quy chuẩn Kỹ thuật 6 Nhóm Graphic Consumer

| Consumer | Kích thước Game | Định dạng File | Yêu cầu Kỹ thuật Đặc thù | Thư mục Đích |
|---|---|---|---|---|
| **1. National Focus** | $93\times 91$ px | 32-bit BGRA DDS uncompressed | Đúng **33.980 bytes**, viền ngoài 1px Alpha=0, 3D relief nổi khối | `gfx/interface/goals/` |
| **2. National Spirit (Idea)** | $60\times 68$ px | 32-bit BGRA DDS uncompressed | Đúng **16.448 bytes**, viền alpha sạch, motif cô đọng | `gfx/interface/ideas/` |
| **3. Decision Icon** | $33\times 32$ px | 24-bit hoặc 32-bit TGA | Chuẩn TGA uncompressed không RLE, icon hành động rõ nét | `gfx/interface/decisions/` |
| **3b. Decision Category** | $64\times 64$ px | 32-bit BGRA DDS uncompressed | Đúng **16.512 bytes**, viền alpha, biểu trưng chuyên đề | `gfx/interface/decisions/` |
| **4. Event Picture** | $210\times 176$ px (hoặc $156\times 210$) | 32-bit BGRA DDS uncompressed | Cảnh hiện thực lịch sử, tỉ lệ 16:9/vignette, không dùng frame focus | `gfx/event_pictures/` |
| **5. Portrait (Leader/General)** | $156\times 210$ px (Large)<br>$38\times 51$ px (Small) | 32-bit BGRA DDS uncompressed | Chuẩn chân dung dầu Paradox, nền cờ mờ/văn phòng, đúng quân phục | `gfx/leaders/VIE/` |
| **6. UI / BoP / MIO / Trait** | Khám phá theo GUI slot | DDS/TGA tùy slot | Khảo sát đúng số frame (`noOfFrames`), state và canvas từ `.gui` | `gfx/interface/` |

---

## 3. Hướng dẫn Chi tiết Từng Module Mỹ thuật

### Module 1: National Focus Icons ($93\times 91$ px)
- **Bố cục:** Chủ thể chính (bamboo, ấn tín, tàu chiến, vũ khí, tài liệu) chiếm **80–85% diện tích**.
- **Khung (Framing):** Vòng nguyệt quế vàng, huy hiệu đá hoặc sao vàng tả thực 3D, lồng drop shadow ambient mềm mại. Tuyệt đối không vẽ khung bằng code pixel toán học hay ép nhỏ vào vòng tròn 62px.
- **DDS Codec:**
  ```python
  # Header 128 bytes + 93*91*4 bytes = 33.980 bytes
  header = b"DDS " + struct.pack(
      "<7I11I8I5I",
      124, 0x100F, 91, 93, 93 * 4, 0, 0, *([0] * 11),
      32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000, 0x1000, 0, 0, 0, 0
  )
  ```
- **Sprite:** Khai báo `GFX_focus_VIE_<stem>` trong `interface/VIE_md_focus_icons.gfx`.

### Module 2: National Spirits, Ideas & Laws ($60\times 68$ px)
- **Đặc trưng:** Diễn tả một trạng thái, tinh thần, năng lực hoặc debuff kéo dài (khác focus là một quyết sách và decision là một hành động).
- **Tránh ghi đè:** Kiểm tra kỹ `GFX_idea_<name>` để không vô tình đè lên sprite generic của Millennium Dawn.
- **Kỹ thuật:** Cắt silhouette rõ ràng, tương phản cao trên nền giao diện bảng chính phủ.

### Module 3: Decisions & Categories ($33\times 32$ px TGA & $64\times 64$ px DDS)
- **Nút Decision ($33\times 32$ px):** Thể hiện động từ/hành động tức thời (búa liềm, ký tên, bắt tay, phong tỏa, kiểm tra). Định dạng TGA uncompressed 24-bit hoặc 32-bit.
- **Category Header ($64\times 64$ px):** Đại diện cho một chiến dịch, chuyên đề hoặc ban chỉ đạo.

### Module 4: Event & News Pictures ($210\times 176$ px)
- **Đặc trưng:** Minh họa một khoảnh khắc lịch sử cụ thể, một cuộc họp cấp cao, lễ duyệt binh hoặc ký kết hiệp định.
- **Không dùng khung:** Ảnh sự kiện là khung chữ nhật tràn viền với vignette góc tối, không bao giờ dùng khung nguyệt quế hay huy hiệu của focus.

### Module 5: Portraits Chân dung ($156\times 210$ px & $38\times 51$ px)
- **Nhận diện:** Đúng người, đúng độ tuổi trong giai đoạn 2000–2026, đúng cấp bậc hàm và quân phục chuẩn của QĐNDVN/CAND/Đảng/Chính phủ.
- **Phong cách:** Sơn dầu tả thực Chiaroscuro kinh điển của Paradox (tương tự các chân dung mẫu của MD).
- **Bộ đôi:** Luôn xuất đồng thời bản Large ($156\times 210$ px) cho bảng chính phủ/quân đoàn và bản Small ($38\times 51$ px) cho icon tướng chỉ huy sư đoàn/advisor.

### Module 6: UI, BoP, MIO, Trait & Quốc kỳ
- **Khám phá trước khi vẽ:** Mở file `.gui` tương ứng trong `interface/` để đọc đúng kích thước hiển thị và số frame:
  - Nút bấm thường có 2-3 frame (bình thường, hover, click).
  - Thanh đo Balance of Power có kim chỉ và thanh nền riêng biệt.
  - Logo MIO thường là $64\times 64$ px hoặc $80\times 80$ px.

---

## 4. Quy trình Sản xuất & Kiểm tra Tự động (Pipeline)

1. **Lập Master:** Vẽ/Gen ảnh phân giải cao ($1024\times 1024$ px) trên nền tối tách biệt, chủ thể chiếm ưu thế.
2. **Cắt Alpha:** Tách nền mượt mà, tạo viền chuyển tiếp mịn (anti-aliased) và đổ bóng drop shadow.
3. **Downscale & Sharpen:** Thu nhỏ xuống kích thước game bằng thuật toán Lanczos, áp dụng Unsharp Mask để đảm bảo độ nét tuyệt đối.
4. **Biên dịch File:** Xuất đúng codec (32-bit BGRA DDS hoặc TGA uncompressed).
5. **Khai báo GFX:** Đăng ký spriteType trong các file `interface/*.gfx` tương ứng.
6. **Kiểm tra tự động:**
   ```bash
   python tools/audit_dds_and_gfx.py
   ```
   Lệnh phải trả về **0 DDS format errors, 0 missing texturefiles**.
