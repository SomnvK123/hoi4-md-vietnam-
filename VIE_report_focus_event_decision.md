# Báo cáo: Focus tree, Event và Decision — submod Việt Nam cho Millennium Dawn

> Số liệu đo bằng script trực tiếp trên `D:\HOI4Mods\md_vietnam` (ngày 26/09/2026). Không lấy từ tài liệu kế hoạch.
> Trạng thái kiểm tra: `python tools/check_static.py` → **0 lỗi, 129 cảnh báo** (127 là cảnh báo bố cục). **Chưa chạy thử trong game** — `error.log` mới nhất là 12:42 ngày 20/09, trước gần như toàn bộ nội dung hiện tại.

---

## 1. Tóm tắt

| | Số lượng |
|---|---|
| Focus | **502** (1 cây duy nhất `VIE_md_focus`) |
| Event | **191** (179 country, 12 news) |
| Decision | **16** trong 5 danh mục |
| Idea (national spirit) | **189** |
| Power balance | 3 |
| Dynamic modifier | 2 (`VIE_armed_forces_modifier`, `VIE_state_modifier`) |
| Công ty quốc phòng (MIO) | 4 |
| Scripted effect | 60 (13 file) |
| Khóa loc (duy nhất) | 2.481 |

**Đánh giá ngắn:** nội dung dày và nhất quán về cấu trúc; phần logic (điều kiện, chuyển chế độ, tham chiếu) sạch theo kiểm tra tĩnh. Ba điểm đáng lo nhất là **bố cục cây bị chen sát** (127 cặp focus cách nhau chưa đủ 2 ô), **chưa có bằng chứng chạy thật**, và **4 focus đã bị xóa** khỏi bản đã review trước đó.

---

## 2. Focus tree

### 2.1 Quy mô và cấu thành

| Khối | Focus | Ghi chú |
|---|---|---|
| Thân lịch sử (chính trị, kinh tế, xã hội, khoa học, ngoại giao) | **210** | hàng 0–9 |
| Quốc phòng | **133** | hàng 10–26, một nhánh gốc `VIE_modernize_vpa` chia 4 cột |
| Dải chế độ giả định | **159** | hàng 28–37, 19 thành phần liên thông |

- **Chi phí:** 74 focus giá 5, 336 giá 7, 92 giá 10. Tổng **3.642 tuần ≈ 70 năm** thời gian focus, trong khi một ván 2000–2045 chỉ có 45 năm — nghĩa là người chơi **không thể lấy hết**, đây là cơ chế lựa chọn chính của cây.
- **Bộ lọc:** POLITICAL 182 · ECONOMY 173 · ARMY 80 · STABILITY 76 · RESEARCH 60 · NAVY 53 · INDUSTRY 43 · AIR 38.
- **Đồ thị:** 35 gốc (không prerequisite), 156 lá, độ sâu tối đa 11 tầng. Cây rộng và nông; giới hạn thực tế là thời gian, không phải độ sâu.
- **Khóa:** 229 focus có `available`, **127 khóa theo mốc năm**, 17 focus có `mutually_exclusive` (điện hạt nhân xây/gác, ngả Trung Quốc/ngả phương Tây, pháp lý biển/khẳng định chủ quyền, các ngã rẽ học thuyết quân sự…).
- **Chất lượng script:** 100% focus có dòng `log`, 100% có `ai_will_do`; 173 focus (34%) có modifier AI.
- **Tương tác:** 46 focus bắn event, 160 lượt `add_ideas`, 10 focus gọi `VIE_transition_regime`, 17 nút tắt (shortcut) trên đầu cây.

### 2.2 Thân lịch sử (210)

Gồm năm mảng, mỗi mảng có gốc riêng để người chơi rời Đảng vẫn đi được:

- **Chính trị – nhà nước:** chống tham nhũng, cải cách bộ máy, tinh gọn 2024–2025, Hiến pháp 2013, Luật An ninh mạng.
- **Ngoại giao:** cây tre, Mỹ (BTA → đối tác toàn diện → thuế quan), Trung Quốc (16 chữ), ASEAN/LHQ/WTO/CPTPP/EVFTA, Biển Đông.
- **Kinh tế:** tài chính – ngân hàng, công nghiệp và FDI, DNNN và tư nhân, năng lượng, hạ tầng, nông nghiệp.
- **Xã hội – khoa học:** giáo dục, y tế, môi trường, số hóa, bán dẫn.
- **Đợt bổ sung gần đây (19 focus mới):** ô tô và xe điện (`ev_revolution_batteries`, `global_auto_export`, `tier1_vendor_localization`, `integrated_auto_supplier_park`…), Petrolimex và dự trữ xăng dầu (4), ứng phó thiên tai (`emergency_operations_center`, `military_rescue_corps`, `satellite_early_warning`, `storm_resilient_islands`), đồng bằng Cửu Long (`dutch_water_model`, `nature_adaptation_120`, `sustainable_mekong_delta`), thép (`hoa_phat_hrc_steel`, `precision_mechanics_molds`), điện (`dppa_market_reform`, `jetp_partnership`).

### 2.3 Quốc phòng (133)

Một gốc `VIE_modernize_vpa` chia **bốn cột**:

| Cột | Nội dung | Điểm nhấn |
|---|---|---|
| Lục quân (24 focus) | hạ sĩ quan, quân khu, sư đoàn cơ giới, công binh–đặc công, tác chiến điện tử, C4ISR | ngã rẽ **chiến tranh nhân dân ↔ viễn chinh**; 3 mẫu sư đoàn/lữ đoàn mới |
| Hải quân (25) | 5 Vùng, Molniya, căn cứ tàu ngầm Cam Ranh, mạng đảo Trường Sa | ngã rẽ **từ chối tiếp cận ↔ viễn dương** (khu trục, tàu sân bay nhẹ — giả định) |
| Không quân (28) | sân bay kiên cố, SAM tầm xa, cảnh báo sớm, UAV, VAECO | ngã rẽ **ưu thế trên không ↔ tấn công chiều sâu** (SEAD, ALCM — giả định) |
| Công nghiệp quốc phòng + tên lửa (18) | Viettel, nhà máy Z, Ba Son, VAECO, tên lửa bờ, chuỗi hạt nhân giả định | gắn **MIO** (cần DLC Arms Against Tyranny); nhánh hạt nhân khóa DLC Götterdämmerung |

Nhánh hạt nhân cần được đối chiếu trực tiếp với trigger hiện hành. Báo cáo cũ ghi luật chơi `VIE_alt_history ≠ historical`, nhưng audit ngày 07/10/2026 xác nhận rule đó chỉ có lựa chọn mặc định, không có reader, và đã bị xoá; đừng coi điều kiện ấy là gate đang hoạt động.

### 2.4 Dải chế độ giả định (159)

19 thành phần liên thông, ánh xạ vào 12 party slot của MD:

| Nhóm | Dải | Ghi chú |
|---|---|---|
| Không đổi chế độ | Kiến tạo (15) · Tự chủ chiến lược (15) · Bàn tròn (6) | 36 focus là **lựa chọn xây dựng nhà nước / cơ chế chuyển đổi**, không phải chế độ |
| Bên trong đảng trị | Bảo thủ (6) | slot 4 |
| Độc đoán | Nhà nước An ninh (8) · Junta (8) · Hội đồng Phát triển (15) · Đoàn kết Quốc gia (6) | slot 7 / 22 / 0 / 13 |
| Vốn chiếm giữ | Tài phiệt (12) · Đặc khu Tự do (13) | slot 15 / 16 |
| Dân túy → cực hữu | Dân túy (14) → Lạc Hồng (3) | slot 20 → 21; Lạc Hồng **không vào trực tiếp được** |
| Dân chủ | 4 gói đảng cầm quyền (16) | slot 1 / 2 / 14 / 18 |
| Ngoại lệ hậu khủng hoảng | Quân chủ (10) · Xanh (9) · Công xã Công nhân (3) | slot 23 / 17 / 5 |

### 2.5 Cơ chế xuyên suốt gắn vào focus

- **Power balance (3):** Bảo thủ ↔ Cải cách (ĐCSVN), Nhà nước ↔ Đường phố (Dân túy), Tập đoàn ↔ Dân chúng (Tài phiệt). **74 focus** dịch chuyển thanh chính.
- **Hệ 9 trục xây dựng nhà nước:** `VIE_ax_size/merit/decent/checks/market/civil/integ/mob/west`, chuẩn hóa −10…+10, đọc bởi `VIE_state_modifier`. **Hơn 600 dòng cộng trục** trong focus. 10 focus gốc chế độ có cổng theo trục, hiển thị điều kiện bằng chữ Việt kèm giá trị hiện tại.
- **Luật MD:** 15 focus gọi trực tiếp luật bộ máy, cảnh sát, giáo dục, y tế, an sinh của MD (`decrease_centralization`, `increase_policing_budget`…).
- **Đánh đổi:** cải cách chất lượng bộ máy (`merit ≥ 2`) trừ 1 điểm ủng hộ của `communist_cadres` (Geddes 1994).
- **Tham nhũng:** dùng hệ `corruption_level_01…10` của MD; ~20 focus tăng/giảm.

### 2.6 Vấn đề của cây hiện tại

| Mức | Vấn đề | Chi tiết |
|---|---|---|
| **Cao** | **127 cặp focus cách nhau dưới 2 ô** | 59 ở thân lịch sử, 67 ở dải chế độ, 1 ở quốc phòng. Toàn bộ cây đã được xếp lại (483/487 focus đổi tọa độ so với bản đã review, gốc chuyển từ x=27 sang x=80). Hộp focus rộng khoảng 2 ô nên các cặp này có nguy cơ **chồng lên nhau** khi xem trong game |
| **Trung bình** | 1 focus nằm không thấp hơn cha | `VIE_semiconductor_ambition` so với `VIE_intel_hcmc` |
| **Trung bình** | **4 focus đã bị xóa** khỏi bản đã review | `VIE_forest_protection`, `VIE_hanoi_air_quality`, `VIE_plastic_waste`, `VIE_jetp` (`VIE_jetp_partnership` xuất hiện, có thể là đổi tên). Kiểm tra tĩnh không thấy tham chiếu treo, nhưng save cũ đã hoàn thành các focus này sẽ lệch |
| **Thấp** | File rác trong thư mục mod | 5 file `VIE_md_focus.txt.bak*` (~2 MB) và thư mục `scratch/` (nhiều script Python). Sẽ bị đóng gói nếu upload Workshop |
| **Thấp** | Nhiều hiệu ứng chỉ cộng | Dù đã thêm cái giá Geddes, phần lớn focus vẫn là thuần lợi ích; chỉ 17 focus loại trừ lẫn nhau trên 502 |

---

## 3. Event

### 3.1 Quy mô và phân bố

| Namespace | Số event | Chủ đề |
|---|---|---|
| `vie_alt` | 38 | các cửa rẽ chế độ, khủng hoảng dân túy, Lạc Hồng, đổi chính phủ |
| `vie_eco` | 28 | kinh tế, ngân hàng, FDI |
| `vie_pol` | 22 | Đại hội Đảng, tham nhũng, bộ máy |
| `vie_dip` | 19 | ngoại giao, Mỹ, chọn tiêm kích |
| `vie_scs` | 19 | Biển Đông: căng thẳng, Hoàng Sa, đưa ra tòa |
| `vie_soc` | 19 | xã hội, y tế, giáo dục |
| `vie_news` | 12 | tin tức (news event) |
| `vie_int` | 11 | nội chiến, tái thiết |
| `vie_cor` | 8 | chống tham nhũng |
| `vie_col` | 6 | Sụp đổ và hậu quả |
| `vie_axis` | 4 | cạnh thất bại theo trục (**mới**) |
| `vie_disaster` / `vie_auto` / `vie_petro` | 2 / 2 / 1 | bão, xe điện, xăng dầu (**mới**) |

### 3.2 Cách event chạy

- **187/191 là `is_triggered_only`** — do focus, scheduler hoặc event khác gọi. Chỉ 4 event chạy theo `mean_time_to_happen`.
- **Scheduler ba lớp (A/B/C)** gắn vào `on_monthly` chung, có chế độ bắt kịp (`VIE_catch_up`) để sau nội chiến không mất mốc lịch sử.
- **Lịch sử chạy bằng event, lựa chọn chạy bằng focus** — đúng nguyên tắc plan v6. Mỗi ngã rẽ lịch sử có option lịch sử và option giả định.
- **Lựa chọn:** tổng **366 option**; 139 event có 2 option, 33 có 1, 17 có 3. Chỉ `vie_pol.1` có 0 option (event ẩn khởi tạo).
- **AI:** 343 khối `ai_chance`, chỉ **57 (17%)** có modifier; còn lại là trọng số cố định. Không phải lỗi, nhưng AI ở các điểm rẽ D1–D8 sẽ ít nhạy với bối cảnh.
- **Tham chiếu:** không có event nào bị bỏ rơi (mọi event đều được gọi ở đâu đó hoặc chạy theo mtth).

### 3.3 Cạnh chuyển chế độ theo trục (`vie_axis`)

Bốn event mô tả những kết cục "nửa chừng" mà literature nói phổ biến hơn kết cục cực đoan:

1. **Kiến tạo trượt thành Tài phiệt** khi thị trường mở nhanh hơn năng lực bộ máy (Evans 1995).
2. **Lạc Hồng thoái hóa** thành độc đoán thông thường sau 600 ngày mất năng lượng huy động (Paxton, giai đoạn 5).
3. **Dân chủ hóa dừng ở độc đoán cạnh tranh** (Levitsky & Way).
4. **Cảnh báo khủng hoảng đa tầng** khi ổn định và trục thể chế cùng xuống thấp.

### 3.4 Vấn đề đã sửa và còn mở

**Đã sửa trong đợt rà soát:**
- Hai event gọi macro `VIE_enter_regime` không còn tồn tại → viết lại thành chuỗi `VIE_transition_regime` đầy đủ.
- Cạnh Kiến tạo → Tài phiệt kiểm tra cờ chưa từng được đặt → nay dùng `has_completed_focus`.
- Event entropy Lạc Hồng có thể bắn ngay sau khi vào → thêm cờ hạn 600 ngày.
- **`vie_disaster.1` gọi `change_military_opinion` — effect không tồn tại trong MD** (đúng là `change_the_military_opinion`, cần `the_military` đang là faction). Đã sửa trong lần chạy này.
- 3 tên tech bonus thiếu loc (`VIE_home_fighter`, `vie_alt_29_advisers`, `VIE_naval_infantry_landing`) → đã thêm.

**Còn mở:**
- Chưa event nào được chạy trong game.
- `vie_disaster.1` chỉ có 3 phương án dựa vào việc đã làm hai focus cứu hộ; người chơi không làm focus nào chỉ gặp phương án C.
- `vie_petro.1` chỉ có option "chuẩn bị tốt" khi đã làm 1 trong 2 focus; không có option trung gian.
- Sự cố đã biết: event D4, D5, D6 chỉ có ghi chú cổng trục, không chặn lựa chọn.

---

## 4. Decision

**16 quyết định trong 5 danh mục**, tất cả có thời gian chờ (`days_re_enable`) và chi phí điểm chính trị:

| Danh mục | Quyết định | Chi phí | Chờ (ngày) |
|---|---|---|---|
| **Tài phiệt** | `VIE_ol_credit_squeeze` | 75 | 180 |
| **Dân túy** | `VIE_np_restore_order` | 150 | 240 |
| **Chiến lược Biển Đông** | `VIE_scs_patrol_disputed_waters` | 50 | 180 |
| | `VIE_scs_deescalate` | 25 | 180 |
| **Sẵn sàng chiến đấu** (6) | diễn tập quân khu / hải quân / không quân | 40 mỗi cái | 365 |
| | `VIE_procurement_batch` (mua sắm bổ sung) | 25 | 730 |
| | `VIE_asean_joint_patrol` | 50 | 540 |
| | `VIE_extended_conscription` | 75 | 1.095 |
| **Xây dựng nhà nước** (6) | thi tuyển công chức cạnh tranh | 75 | 180 |
| | giao quyền thí điểm cho tỉnh | 50 | 180 |
| | tinh gọn tổ chức bộ máy | 100 | 360 |
| | nới kiểm soát nội dung | 50 | 180 |
| | siết kỷ luật nội bộ | 50 | 180 |
| | đàm phán hiệp định kinh tế | 75 | 240 |

**Đặc điểm:**
- Nhóm **Xây dựng nhà nước** là chỗ duy nhất người chơi chủ động đẩy trục ngoài dòng lịch sử; mỗi quyết định gọi `VIE_ax_normalize` và có giá (giảm ủng hộ cán bộ, giảm ổn định ngắn hạn, tăng chi thường xuyên qua luật MD).
- Nhóm **Sẵn sàng chiến đấu** cho kinh nghiệm quân sự và quyền chỉ huy, tốn PP, phù hợp cơ chế lặp lại.
- Nhóm **Biển Đông** chỉ hiện khi người chơi chọn con đường từ chối tiếp cận.
- **Thiếu:** không có decision nào cho nhánh dân chủ hóa, hạt nhân, hoặc môi trường; các quyết định của dải chế độ chỉ có 2 (Tài phiệt, Dân túy).

---

## 5. Hệ thống hỗ trợ

| Thành phần | Nội dung |
|---|---|
| **Idea (189)** | 153 trong file chính, 12 cho khối quân sự và trục (`p3A…p3Q`), 16 cho các đợt bổ sung (thiên tai, Petrolimex, công nghiệp hỗ trợ) |
| **MIO (4)** | Viettel, Tổng cục CNQP (nhà máy Z), Ba Son, VAECO; 31 trait; 6 biến thể vũ khí sao chép từ biến thể MD đang chạy |
| **Dynamic modifier (2)** | `VIE_armed_forces_modifier` (61 biến `VIE_af_*`), `VIE_state_modifier` (9 biến trục) |
| **on_actions (3)** | `on_monthly` (scheduler + chuẩn hóa trục), `on_civil_war_end`, `on_startup` |
| **Internal faction** | 3 slot của MD; `VIE_ax_faction_check` đổi faction theo ngưỡng trục và giữ đúng giới hạn 3 |
| **Tham nhũng, ngân sách** | dùng nguyên hệ MD |
| **Tích hợp DLC** | Arms Against Tyranny (MIO), No Step Back (biến thể tăng/pháo), Götterdämmerung (nhánh hạt nhân); mọi chỗ đều có nhánh `else` |

---

## 6. Kiểm tra chất lượng

| Loại | Kết quả |
|---|---|
| Cân bằng ngoặc, tham chiếu focus/idea/event/decision | **0 lỗi** |
| Modifier trong idea có trong tài liệu game hoặc MD | **0 lỗi** |
| Sprite của focus, decision, MIO | **0 lỗi** |
| Đơn vị trong `division_template` có thật | **0 lỗi** |
| Lệnh `VIE_*` chưa định nghĩa | **0 lỗi** (kiểm tra mới, đã bắt được lỗi `VIE_enter_regime`) |
| Lệnh không phải `VIE_*` chưa định nghĩa | **0 lỗi** (kiểm tra mới, đã bắt được `change_military_opinion`) |
| Tên tech bonus thiếu loc | **0 lỗi** (kiểm tra mới) |
| Bố cục | **127 cảnh báo khoảng cách + 1 cha–con sai thứ tự** |
| **Chạy trong game** | **Chưa** |

Ánh xạ trục: 360+ focus đã đối chiếu với `axis_map*.py` — 0 thiếu, 0 thừa, 0 sai giá trị; 11 cổng chế độ đều đạt được bằng tìm kiếm ngẫu nhiên trên tập focus khả dụng.

---

## 7. Khuyến nghị theo thứ tự ưu tiên

1. **Chạy một ván ngắn và gửi `error.log`.** Đây là việc duy nhất biến "đã qua kiểm tra tĩnh" thành "chạy được". Nội dung quân sự, MIO, hệ trục, thiên tai đều chưa từng được nạp.
2. **Sửa 127 cặp chen sát trong bố cục** (hoặc xác nhận bằng ảnh chụp trong game là nhìn ổn). Nếu chồng lên nhau thật thì đây là lỗi thị giác nặng nhất của cây.
3. **Xác nhận 4 focus bị xóa là cố ý**, và với `VIE_jetp` → `VIE_jetp_partnership` thì đó là đổi tên hay thay nội dung.
4. **Dọn thư mục mod:** chuyển 5 file `.bak*` và `scratch/` ra ngoài trước khi đóng gói.
5. **Bổ sung modifier AI** cho các event điểm rẽ D1–D8 nếu muốn AI đi đường lịch sử ổn định hơn (không cần làm cho cả 343 khối).
6. **Bổ sung decision** cho nhánh dân chủ hóa và môi trường nếu muốn cân bằng với nhóm quân sự (hiện 6 quyết định).
7. **Thêm phương án trung gian** cho `vie_disaster.1` và `vie_petro.1`.
