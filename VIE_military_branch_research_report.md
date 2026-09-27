# BÁO CÁO NGHIÊN CỨU & ĐỀ XUẤT TÁI CẤU TRÚC TOÀN DIỆN CÂY QUÂN ĐỘI
## (VPA Military Focus Tree Redesign & Optimization Report)

> **Tình trạng:** Bản nghiên cứu định hướng & đề xuất phương án xử lý — **Chưa can thiệp code**.  
> **Mục tiêu:** Tinh giản từ 144 focus cồng kềnh, trùng lặp xuống **~70 focus tinh gọn, khoa học**, phản ánh chân thực học thuyết quân sự và bối cảnh địa chính trị thực tế của Quân đội Nhân dân Việt Nam (2000 – 2035).

---

## I. THỰC TRẠNG CÂY QUÂN ĐỘI HIỆN TẠI: VÌ SAO BỊ "QUÁ NHIỀU CHỖ THỪA, THIẾT KẾ CHƯA KHOA HỌC"?

### 1. Con số thống kê gây sốc
* Toàn bộ cây Focus của mod hiện có **409 focus**.
* Riêng nhánh Quân sự & Công nghiệp quốc phòng đang chiếm tới **144 focus** (~35.2% toàn bộ mod!).
* Mỗi focus tốn từ 5 đến 10 tuần: Người chơi cần **trên 1.000 tuần in-game (tương đương gần 20 năm cày cuốc liên tục)** chỉ để đi hết nhánh quân sự. Trong một đại mod rất nặng và chạy chậm như Millennium Dawn, điều này làm gãy hoàn toàn nhịp độ chơi (gameplay pacing).

### 2. Nguyên nhân cốt lõi gây ra tình trạng hỗn loạn
Cây quân đội hiện tại bị hình thành bởi việc **ghép nối cơ học hai lớp nội dung hoàn toàn lệch pha**:
1. **Lớp gốc (Phase 1–2, ~50 focus):** Các focus mua sắm trang bị thực tế giai đoạn 2000–2018 (mua T-90, Kilo, Gepard, Su-30, Tổ hợp Viettel, Nhà máy Z, Luật Biển, Dân quân biển, Nhà giàn DK1).
2. **Lớp tạo tự động (Auto-generated v3 via scripts `_gen/blockA/B/C/DE.py`, ~72 focus):** Một chuỗi focus tự động bơm vào từ hàng 5 đến hàng 15, cố tình vẽ ra 5 khối A (Lục quân 18), B (Hải quân 18), C (Không quân 18), D (CNQP 10), E (Tên lửa 8) với các mốc "2030" chạy song song ở dưới.

**Hậu quả:** 
Hai lớp này **chồng chéo và lặp lại nhau gần như 1:1**, tạo nên một ma trận hỗn độn: người chơi vừa nghiên cứu xong T-90 và pháo binh ở tầng trên, xuống tầng dưới lại phải nghiên cứu "Chương trình phát triển Lục quân" rồi lại nghiên cứu "Hiện đại hóa xe tăng" và "Pháo tự hành" một lần nữa!

---

## II. CHI TIẾT "CHỖ THỪA" (CÁC ĐIỂM TRÙNG LẶP & YẾU TỐ PHI THỰC TẾ)

### 1. Danh sách các cặp Focus trùng lặp 100% (Cần sáp nhập ngay)

| Lực lượng | Focus Lớp Cũ (Trùng lặp 1) | Focus Lớp Mới v3 (Trùng lặp 2) | Bản chất nội dung trùng nhau | Hướng xử lý |
|---|---|---|---|---|
| **Lục quân** | `VIE_mechanization` (Cơ giới hóa Sư đoàn BB) | `VIE_army_mech_corps` (Sư đoàn bộ binh cơ giới) | Cùng cấp trang bị xe bọc thép BMP/BTR cho sư đoàn bộ binh | **Gộp làm 1** |
| **Lục quân** | `VIE_special_forces` (Lực lượng Đặc công) | `VIE_army_combat_engineers` (Công binh và đặc công) | Cùng nâng buff Đặc công QĐNDVN | **Gộp làm 1** |
| **Lục quân** | `VIE_rocket_artillery` (Pháo binh & Phản lực) | `VIE_army_sp_artillery` (Pháo tự hành & Phản lực) | Cùng buff pháo binh BM-21/BM-30 | **Gộp làm 1** |
| **Lục quân** | `VIE_tank_modernization` + `VIE_t90_tanks` | `VIE_army_armor_modernization` (Hiện đại hóa tăng) | Đều nói về nâng cấp T-54B lên T-54M và mua T-90S | **Gộp làm 1 chuỗi 2 focus** |
| **Lục quân** | `VIE_militia_law` (Luật Dân quân Tự vệ) | `VIE_army_dan_quan_modern` (Dân quân hiện đại hóa) | Cùng nâng buff dân quân tự vệ | **Gộp làm 1** |
| **Lục quân** | `VIE_provincial_defence_zones` (KVPT Tỉnh) | `VIE_army_military_regions` (Cải tổ hệ thống Quân khu) | Cùng củng cố thế trận tác chiến địa phương | **Gộp làm 1** |
| **Hải quân** | `VIE_cam_ranh_base` (Căn cứ Cam Ranh) | `VIE_navy_sub_base` (Căn cứ tàu ngầm Cam Ranh) | Đều là công trình cầu cảng quân sự Cam Ranh | **Gộp làm 1** |
| **Hải quân** | `VIE_naval_infantry` (Hải quân Đánh bộ) | `VIE_navy_marines` (Lữ đoàn Hải quân Đánh bộ) | Cùng nâng cấp Lữ đoàn 147 / 101 HQĐB | **Gộp làm 1** |
| **Hải quân** | `VIE_domestic_corvettes` (Đóng tàu pháo/tên lửa) | `VIE_navy_missile_boats` (Tàu tên lửa Molniya) | Cùng đề cập dự án đóng tàu tên lửa lớp 1241.8 Molniya | **Gộp làm 1** |
| **Hải quân** | `VIE_kilo_submarines` (Lữ đoàn Tàu ngầm Kilo) | `VIE_navy_submarine_expansion` (Mở rộng tàu ngầm) | Cùng buff lực lượng tàu ngầm Kilo 636 | **Gộp làm 1** |
| **Hải quân** | `VIE_coast_guard_law` + `fisheries_surveillance` | `VIE_navy_coast_guard` (Cảnh sát biển & kiểm ngư) | Cùng nói về lực lượng thực thi pháp luật biển | **Gộp làm 1 chuỗi gọn** |
| **Hải quân** | `VIE_spratly_fortification` + `dk1_platforms` | `VIE_navy_island_network` (Mạng lưới đảo Trường Sa) | Cùng nói về công sự đảo và nhà giàn DK1 | **Gộp làm 1** |
| **Không quân**| `VIE_helicopter_fleet` (Hiện đại hóa trực thăng) | `VIE_air_attack_helos` (Trực thăng vũ trang Mi-8/Mi-17) | Đều là hiện đại hóa phi đội trực thăng | **Gộp làm 1** |
| **Không quân**| `VIE_integrated_air_defense` (Lưới lửa PK) | `VIE_air_layered_sam` (Phòng không nhiều tầng) | Cùng nâng buff phòng không tích hợp | **Gộp làm 1** |
| **Không quân**| `VIE_air_dominance_coast` | `VIE_air_superiority_ops` & `VIE_air_superiority_wing` | **3 focus khác nhau** cùng nói về chiếm ưu thế trên không! | **Gộp thành 1** |
| **CNQP** | `VIE_missile_program` | `VIE_msl_coastal_home` + `VIE_msl_cruise_missiles` | Cùng là tự chủ tên lửa bờ / tên lửa hành trình | **Gộp làm 1** |
| **CNQP** | `VIE_shipyards` (Mở rộng đóng tàu quân đội) | `VIE_navy_ba_son` (Nâng cấp xưởng Ba Son) | Cùng nâng năng lực đóng tàu quân sự | **Gộp làm 1** |
| **Tác chiến số**| `VIE_force_47` + `VIE_cyber_command` | `VIE_army_electronic_warfare` | Trùng với nhánh an ninh `VIE_sec_cyber_control` | **Chuẩn hóa thành 1 cụm** |

### 2. Các nhánh ảo tưởng, phi lý cần LOẠI BỎ TRIỆT ĐỂ
* **Tàu sân bay hạng nhẹ cho Việt Nam (`VIE_navy_light_carrier` & `VIE_navy_blue_destroyers`):**  
  * *Thực tế:* Việt Nam có bờ biển hình chữ S trải dài, toàn bộ Biển Đông đều nằm trong bán kính tác chiến của không quân tiêm kích trên đất liền (sân bay Phan Rang, Đà Nẵng, Phù Cát, Chu Lai, Trường Sa Lớn). Học thuyết phòng thủ của Việt Nam xác định đất liền là "tàu sân bay không bao giờ chìm". Ý tưởng đóng tàu sân bay viễn dương vừa phi thực tế về ngân sách hàng chục tỷ USD, vừa vô lý về mặt học thuyết tác chiến.
* **Vũ khí hạt nhân cho Việt Nam (`VIE_msl_nuclear_power` -> `VIE_msl_dual_use_threshold` -> `VIE_msl_minimum_deterrent` -> `VIE_msl_deterrent_doctrine`):**  
  * *Thực tế:* Việt Nam là một trong những quốc gia tiên phong ký Hiệp ước Không phổ biến vũ khí hạt nhân (NPT), Hiệp ước Cấm vũ khí hạt nhân (TPNW), và Hiệp ước Đông Nam Á không có vũ khí hạt nhân (SEANWFZ). Một nhánh gồm 4–5 focus chế tạo đầu đạn hạt nhân răn đe mà không có bối cảnh sụp đổ quan hệ quốc tế, không chịu cấm vận toàn diện của LHQ là một thiết kế viễn tưởng thô kệch, phá hỏng tính nhập vai (immersion) của Millennium Dawn.
* **Lực lượng viễn chinh hải ngoại (`VIE_army_expeditionary` -> `VIE_army_exp_hubs` -> `VIE_army_intervention_force`):**  
  * *Thực tế:* Học thuyết quốc phòng của Việt Nam là tự vệ, hòa bình, tuân thủ nguyên tắc "Bốn Không" (không tham gia liên minh quân sự, không liên kết với nước này để chống nước kia, không cho nước ngoài đặt căn cứ quân sự, không sử dụng hoặc đe dọa sử dụng vũ lực). Ý tưởng xây dựng "Lực lượng can thiệp khu vực" và lập "Căn cứ hậu cần tiền phương ở nước ngoài" là hoàn toàn ngoại lai, xa lạ với truyền thống quân sự Việt Nam.

### 3. Căn bệnh "Lạm phát Biến số Ẩn" (Modifier Variable Bloat)
* Tệp `VIE_armed_forces_modifier` bị nhét tới **61 biến số dynamic modifier** (`VIE_af_*`).
* Rất nhiều focus chỉ làm đúng một việc là cộng `+0.02` hoặc `+0.05` vào một biến vô hình mà người chơi không cảm nhận được sự thay đổi sức mạnh trên bản đồ (ví dụ: `VIE_af_acclimatization_hot_climate_gain_factor = 0.05`, `VIE_af_naval_mines_effect_reduction = 0.05`). 
* Cách thiết kế này làm loãng game: người chơi mất 7 tuần chờ đợi chỉ để nhận một dòng chỉ số nhỏ li ti thay vì nhận đơn vị quân thật, biến thể trang bị mới, công trình phòng thủ, hoặc mở khóa quyết định quân sự có chiều sâu.

---

## III. CHI TIẾT "CHỖ THIẾU" (NHỮNG KHOẢNG TRỐNG CỐT LÕI CỦA QĐND VIỆT NAM)

Mặc dù có tới 144 focus, cây hiện tại lại **bỏ quên những vấn đề sống còn và thú vị nhất** của quân sự Việt Nam giai đoạn 2000 – 2030:

```
                  ┌─────────────────────────────────────────────────────────────┐
                  │          4 KHOẢNG TRỐNG CHIẾN LƯỢC ĐANG BỊ BỎ QUÊN          │
                  └──────────────────────────────┬──────────────────────────────┘
                                                 │
         ┌───────────────────────┬───────────────┴───────────────┬───────────────────────┐
         ▼                       ▼                               ▼                       ▼
  [A2/AD BIỂN ĐÔNG]       [ĐA PHƯƠNG HÓA VŨ KHÍ]        [KINH TẾ QUÂN ĐỘI]       [TINH - GỌN - MẠNH]
  Thiếu liên hoàn:       Thiếu lựa chọn sống còn:     Thiếu bản sắc mô hình    Thiếu cải cách biên
  Tên lửa bờ + Kilo +     Hệ Nga vs Phương Tây vs      "Đội quân lao động sản   chế, giải thể cấp
  Đảo ngầm + Dân quân    Israel/Hàn Quốc vs Tự chủ    xuất" (Viettel, Tân Cảng) trung gian theo NQ05
```

### 1. Thiếu học thuyết Tác chiến Bất đối xứng (Asymmetric A2/AD) ở Biển Đông
* Đứng trước chênh lệch lực lượng hải quân lớn trong khu vực, Việt Nam không thể "đua hạm đội mặt nước kiểu đối xứng". Sức mạnh răn đe thực sự của Việt Nam nằm ở **Chiến lược Chống tiếp cận / Chống xâm nhập (A2/AD)**:
  - Khẩu đội tên lửa bờ tầm xa siêu thanh (Bastion-P, BrahMos) đặt sâu trong hang ngầm ven biển và trên các đảo.
  - Tàu ngầm Kilo 636 nằm im phục kích ở vùng biển sâu kiểm soát các eo biển và luồng hàng hải.
  - Xuồng tên lửa cao tốc Molniya / TT-400TT áp dụng chiến thuật "bầy đàn" đánh nhanh rút nhanh.
  - Thế trận đảo nổi, đảo chìm Trường Sa và nhà giàn DK1 tạo thành chuỗi trạm radar mắt thần cảnh giới sớm.
* Hiện tại cây mod chia vụn vặt các yếu tố này ra nhiều nhánh rời rạc, không tạo thành một **combo học thuyết răn đe tổng thể**.

### 2. Thiếu bài toán then chốt: Đa phương hóa Nguồn cung Vũ khí & Chống Đạo luật CAATSA
Đây là bài toán địa chính trị kịch tính nhất của Việt Nam ngoài đời thực từ 2014 đến nay, nhưng hoàn toàn vắng bóng trong mod:
* **Phương án A: Trung thành với Hệ vũ khí Nga / Đông Âu (Truyền thống)**
  - *Ưu điểm:* Rẻ, sẵn có, quen thuộc biên chế, chuyển giao công nghệ dễ dàng (Su-30, T-90, Gepard, Kilo, S-300).
  - *Hạn chế:* Rủi ro bị trừng phạt theo CAATSA sau 2018, chuỗi cung ứng linh kiện đứt gãy sau xung đột Ukraine 2022.
* **Phương án B: Đa phương hóa / Mở cửa sang Phương Tây & Đối tác mới**
  - *Lựa chọn:* Mua hệ thống phòng không SPYDER, súng Galil ACE, radar ELM từ **Israel**; máy bay tuần thám C-295, máy bay huấn luyện T-6C từ **Mỹ/Châu Âu**; pháo tự hành K9 từ **Hàn Quốc**; tên lửa BrahMos từ **Ấn Độ**.
  - *Hạn chế:* Đắt đỏ, phải mất thời gian chuyển đổi tiêu chuẩn hậu cần và huấn luyện.
* **Phương án C: Tự lực cánh sinh / Tối đa hóa Nội địa hóa (Viettel & Tổng cục CNQP)**
  - *Thành tựu thực tế:* Tự chủ sản xuất súng STV-215/380, radar cảnh giới 3D VRS-CRS, máy bay không người lái trinh sát - tấn công hạng nhẹ, và dự án tên lửa hành trình VCM-01 (bản Việt Nam của Kh-35).

### 3. Thiếu cơ chế Doanh nghiệp Quân đội làm kinh tế
* Việt Nam có đặc thù độc nhất vô nhị: Quân đội làm kinh tế để bù đắp ngân sách quốc phòng:
  - **Tập đoàn Viettel:** Cung cấp nguồn lực tài chính khổng lồ, đồng thời là mũi nhọn nghiên cứu công nghệ cao quân sự (radar, tác chiến điện tử, thông tin liên lạc C4ISR).
  - **Tổng công ty Tân Cảng Sài Gòn:** Nắm giữ phần lớn cảng biển logistics của đất nước, kết hợp quốc phòng - kinh tế.
  - **Các xưởng sửa chữa & đóng tàu (Ba Son, 189, Sông Thu):** Vừa đóng tàu thương mại, vừa đóng tàu hải cảnh và tàu chiến.
* Trong mod, mảng này hoàn toàn bị tách rời khỏi quân sự, không tạo ra sự tương tác giữa Ngân sách - Doanh thu quân đội - Chi phí quốc phòng.

### 4. Thiếu cuộc Cách mạng Tổ chức "Tinh - Gọn - Mạnh" (Nghị quyết 05/NQ-TW)
* Từ 2020 đến nay, QĐNDVN tiến hành một cuộc cải tổ cơ cấu lớn nhất lịch sử:
  - Sáp nhập Quân đoàn 1 và Quân đoàn 2 thành **Quân đoàn 12**; sáp nhập Quân đoàn 3 và Quân đoàn 4 thành **Quân đoàn 34**.
  - Giảm bớt các cơ quan trung gian, khối phục vụ, khối văn phòng để dồn biên chế cho các đơn vị chiến đấu và các lực lượng tiến thẳng lên hiện đại.
  - Hiện tại mod chỉ có một focus sơ sài `VIE_corps_restructure` mà không tạo ra hiệu ứng thay đổi cấu trúc lực lượng rõ rệt.

---

## IV. ĐỀ XUẤT MÔ HÌNH CÂY QUÂN ĐỘI TÁI CẤU TRÚC KHOA HỌC (TỪ 144 XUỐNG CÒN ~70 FOCUS)

Chúng tôi đề xuất tái tổ chức toàn bộ nhánh quân sự theo **Mô hình 4 Trụ Cột Tác Chiến + 1 Trục Nền Tảng**, với tổng số lượng khoảng **70 – 72 focus**, bố trí thành 4 cột trực quan, liên kết chặt chẽ:

```
                            [VIE_modernize_vpa]
                     HIỆN ĐẠI HÓA QUÂN ĐỘI NHÂN DÂN
                                     │
           ┌─────────────────────────┼─────────────────────────┐
           ▼                         ▼                         ▼
   TRỤ CỘT I: LỤC QUÂN       TRỤ CỘT II: HẢI QUÂN      TRỤ CỘT III: PK-KQ
  Chiến tranh Nhân dân      Phòng thủ Biển đảo A2/AD    Lưới lửa PK đa tầng
  & Binh chủng Cơ động       & Căn cứ Cam Ranh         & Ưu thế trên không
     (16 focus)                 (18 focus)                 (16 focus)
           │                         │                         │
           └─────────────────────────┼─────────────────────────┘
                                     │
                                     ▼
                        TRỤ CỘT IV: CÔNG NGHIỆP QUỐC PHÒNG
                           & ĐỐI TÁC TRANG BỊ VŨ KHÍ
                      ┌──────────────┼──────────────┐
                      ▼              ▼              ▼
                 Hệ Nga/Đ.Âu     Đa phương hóa    Tự chủ Viettel
                  (18 focus cho toàn bộ khối CNQP & Lựa chọn)
```

---

### TRỤ CỘT I: LỤC QUÂN & THẾ TRẬN CHIẾN TRANH NHÂN DÂN (16 Focus)
*Tập trung vào: Tinh gọn biên chế, cơ giới hóa, pháo binh - xe tăng, đặc công tinh nhuệ, và thế trận phòng thủ địa phương.*

1. **Gốc lực lượng:** `VIE_army_organization` (Tổ chức Lực lượng Lục quân Tinh - Gọn - Mạnh - *sáp nhập quân đoàn theo NQ 05*).
2. **Nhánh Kỹ thuật & Binh chủng:**
   * `VIE_armor_upgrade` (Hiện đại hóa T-54M & Trang bị T-90S) — *Gộp từ 3 focus tăng cũ*.
   * `VIE_mechanized_infantry` (Cơ giới hóa Sư đoàn Bộ binh chủ lực) — *Gộp `mechanization` và `mech_corps`*.
   * `VIE_artillery_modernization` (Hiện đại hóa Pháo binh & Pháo phản lực tầm xa) — *Gộp `rocket_artillery` và `sp_artillery`*.
   * `VIE_special_forces_elite` (Binh chủng Đặc công Tinh nhuệ) — *Gộp `special_forces` và `combat_engineers`*.
   * `VIE_tactical_c4isr` (Hệ thống Thông tin & Chỉ huy Tác chiến C4ISR).
   * `VIE_army_short_range_ad` (Phòng không Lục quân tầm gần bảo vệ đội hình).
3. **Nhánh Thế trận Chiến tranh Nhân dân & Phòng thủ Chiều sâu:**
   * `VIE_peoples_defence_spine` (Thế trận Quốc phòng Toàn dân) — *Gốc nhánh địa phương*.
   * `VIE_provincial_defence_zones` (Khu vực Phòng thủ Cấp tỉnh & Hệ thống Quân khu) — *Gộp quân khu và KVPT tỉnh*.
   * `VIE_militia_modernization` (Dân quân Tự vệ & Dự bị Động viên Hiện đại) — *Gộp luật DQTV và DQTV hiện đại*.
   * `VIE_underground_fortifications` (Công sự Chiến đấu & Công trình Ngầm kiên cố).
   * `VIE_border_defence_corps` (Bộ đội Biên phòng & Quản lý Đường biên).
4. **Ngã rẽ Học thuyết Tác chiến Lục quân (Chọn 1 trong 2):**
   * **Nhánh A (Phòng thủ Chiều sâu & Du kích Công nghệ cao):**
     * `VIE_asymmetric_ground_doctrine` (Học thuyết Tác chiến Phi Đối xứng trên bộ): Tận dụng địa hình rừng núi, đô thị, công sự ngầm làm tiêu hao sinh lực địch; tăng mạnh khả năng ẩn nấp, đào hào, phục kích, chống đòn không kích công nghệ cao.
     * `VIE_iron_triangle_defence` (Tam giác thép phòng ngự kiên cố).
   * **Nhánh B (Cơ động Phản công & Tác chiến Hiệp đồng):**
     * `VIE_combined_arms_doctrine` (Học thuyết Tác chiến Hiệp đồng Binh chủng Thọc sâu): Xây dựng các lữ đoàn cơ động nhanh, xe thiết giáp phối hợp hỏa lực pháo binh và trực thăng vũ trang để tung đòn phản công tiêu diệt đối phương.
     * `VIE_rapid_response_brigades` (Lữ đoàn Phản ứng Nhanh).
5. **Focus Đỉnh cao 2030:** `VIE_vpa_army_2030` (Lục quân Hiện đại 2030).

---

### TRỤ CỘT II: HẢI QUÂN & PHÒNG THỦ BIỂN ĐẢO A2/AD (20 Focus)
*Tập trung vào: Xây dựng lưới lửa răn đe trên biển bất đối xứng, kiểm soát vùng biển đặc quyền kinh tế và quần đảo Trường Sa; với ngã rẽ chiến lược quan trọng về hộ vệ hạm thế hệ mới.*

1. **Gốc lực lượng:** `VIE_naval_modernization_root` (Chương trình Hiện đại hóa Quân chủng Hải quân & 5 Vùng Hải quân).
2. **Trục Răn đe Biển Sâu & Căn cứ:**
   * `VIE_cam_ranh_naval_bastion` (Căn cứ Quân sự Cam Ranh & Hậu cần Hải quân) — *Gộp Cam Ranh base + Sub base*.
   * `VIE_kilo_submarine_fleet` (Lữ đoàn 189 Tàu ngầm Kilo 636) — *Gộp Kilo + mở rộng tàu ngầm*.
   * `VIE_asw_aviation` (Không quân Hải quân & Trực thăng Săn ngầm Ka-28/C-295 ASW) — *Gộp naval aviation + ASW helo*.
3. **Trục Mặt nước Cơ động:**
   * `VIE_gepard_frigates_procure` (Biên chế Tàu Hộ vệ Tên lửa Gepard 3.9).
   * `VIE_fast_attack_missile_craft` (Biên đội Tàu Tên lửa Tấn công Nhanh Molniya / TT-400TT) — *Gộp corvettes + Molniya*.
   * `VIE_naval_infantry_brigades` (Lữ đoàn Hải quân Đánh bộ 147/101 & Phòng thủ Điểm đảo).
4. **Trục Trận địa Biển Đảo & Thực thi Pháp luật:**
   * `VIE_spratly_fortress_network` (Củng cố Mạng lưới Phòng thủ Quần đảo Trường Sa & Nhà giàn DK1) — *Gộp Trường Sa + DK1*.
   * `VIE_maritime_militia_force` (Hải đội Dân quân Tự vệ Biển bảo vệ chủ quyền).
   * `VIE_coast_guard_and_fisheries` (Cảnh sát biển & Lực lượng Kiểm ngư) — *Gộp Luật CSB + Kiểm ngư*.
   * `VIE_coastal_surveillance_radar` (Trạm Radar Bờ & Mạng lưới Giám sát Biển Đông).
5. **Ngã rẽ Chiến lược Tác chiến Biển (Chọn 1 trong 2):**
   * **Nhánh A: Chiến lược Chống tiếp cận Bất đối xứng (Asymmetric A2/AD - Khuyến nghị Lịch sử):**
     * `VIE_bastion_coastal_missile` (Khẩu đội Tên lửa Bờ Siêu thanh Bastion-P / K-300P).
     * `VIE_smart_sea_mines_usv` (Thủy lôi Thông minh & Phương tiện Không người lái USV/UUV).
     * `VIE_active_maritime_denial` (Học thuyết Từ chối Vùng biển Hoạt động): Buff cực mạnh sát thương tên lửa bờ, tốc độ phục kích của tàu ngầm và tác chiến bầy đàn ven bờ, biến vùng đặc quyền kinh tế thành "vùng chết" đối với hạm đội xâm nhập.
   * **Nhánh B: Thương vụ Hộ vệ hạm Thế hệ Mới — Ngã rẽ SIGMA vs Nội địa (Lựa chọn Gameplay Kịch tính Nhất):**

     > **Bối cảnh thực tế:** Năm 2012–2013, Việt Nam đàm phán mua 2 tàu hộ vệ SIGMA 9814 từ Damen (Hà Lan), trị giá ~660 triệu USD. Tàu dài 98m, rộng 14m; vũ trang hybrid Tây-Nga: pháo 76mm, tên lửa MM40 Exocet Block 3 (chống hạm), VL-MICA (phòng không), radar SMART-S Mk2. Thương vụ bị đình trệ do rào cản xuất khẩu vũ khí và ngân sách. Đến tháng 8/2026, Việt Nam tự đóng tàu hộ vệ chống ngầm đa năng tại Sông Thu (Đà Nẵng) — lớn nhất và hiện đại nhất từ trước đến nay — tích hợp radar AESA, biến thể hải quân VCM-01, ngư lôi 533mm, Ka-27.

     ```
                    [VIE_next_gen_frigate_program]
                   CHƯƠNG TRÌNH HỘ VỆ HẠM THẾ HỆ MỚI
                              (prerequisite: VIE_gepard_frigates_procure)
                                        │
              ┌───────────────────────────────────────────────┐
              ▼                                               ▼
   [VIE_sigma_9814_negotiation]                [VIE_indigenous_asw_frigate]
   Đàm phán SIGMA 9814 với Damen (Hà Lan)     Tự đóng Tàu HV Chống ngầm
   • Tàu 98m × 14m, ~3.000 tấn               tại Sông Thu / Ba Son
   • Exocet MM40 Block 3 + VL-MICA            • Radar AESA nội địa (Viettel)
   • Radar SMART-S Mk2 (NATO chuẩn)           • VCM-01 biến thể hải quân
   • Chuyển giao công nghệ đóng tàu           • Ngư lôi 533mm + sàn Ka-27
   • Tăng quan hệ Hà Lan/EU/NATO              • 100% tự chủ, không CAATSA
              │                                               │
              ▼                                               ▼
   [VIE_sigma_fleet_expansion]             [VIE_song_thu_shipyard_upgrade]
   Mở rộng hạm đội SIGMA lên 4 chiếc       Nâng cấp Nhà máy Sông Thu
   (2 đóng ở NL, 2 đóng tại VN)            thành trung tâm đóng tàu chiến
              │                                               │
              └────────────────────┬──────────────────────────┘
                                   ▼
                      [VIE_modern_navy_2030]
     ```

     **Cơ chế gameplay của ngã rẽ:**

     | Tiêu chí | SIGMA 9814 (Nhánh Hà Lan) | Tàu Nội địa Sông Thu |
     |---|---|---|
     | **Chi phí focus** | 15 tuần (đàm phán + ngân sách lớn) | 10 tuần |
     | **Hiệu ứng quân sự** | +2 tàu hộ vệ 3.000 tấn, radar NATO, tên lửa Exocet | +1 tàu HV chống ngầm, +ASW bonus, unlock Ka-27 slot |
     | **Hiệu ứng ngoại giao** | `improve_relation NLD +30`, `add_to_faction EU_naval_partner` | `VIE_ax_independence +20` |
     | **Rủi ro** | Phụ thuộc chuỗi cung ứng EU; nếu quan hệ EU xấu → spare parts bị cắt | Chậm hơn, không có radar NATO |
     | **Điều kiện mở khóa** | Cần `VIE_pivot_to_the_west = yes` HOẶC quan hệ NLD > 50 | Cần `VIE_viettel_defence_complex = completed` |

6. **Focus Đỉnh cao 2030:** `VIE_modern_navy_2030` (Hải quân Tiến thẳng lên Hiện đại 2030).


---

### TRỤ CỘT III: PHÒNG KHÔNG - KHÔNG QUÂN & TÁC CHIẾN ĐA MIỀN (16 Focus)
*Tập trung vào: Lưới lửa phòng không tích hợp đa tầng, tiêm kích chiếm ưu thế trên không, tác chiến không gian mạng và UAV.*

1. **Gốc lực lượng:** `VIE_air_defence_air_force_root` (Hiện đại hóa Quân chủng PK-KQ & Sư đoàn PK-KQ).
2. **Lưới lửa Phòng không Đa tầng:**
   * `VIE_layered_air_defense` (Lưới Lửa Phòng không Tích hợp Đa tầng) — *Gộp layered SAM + integrated AD*.
   * `VIE_long_range_sam_systems` (Tổ hợp Tên lửa Phòng không Tầm xa S-300PMU1 / S-400 / SPYDER).
   * `VIE_3d_surveillance_radars` (Hệ thống Radar Cảnh giới 3D & Bắt máy bay tàng hình).
   * `VIE_hardened_airbases` (Sân bay Kiên cố & Công sự Hầm ngầm Chứa Máy bay).
3. **Không quân Tiêm kích & Đột kích:**
   * `VIE_su30_flanker_backbone` (Trung đoàn Tiêm kích Đa năng Su-30MK2 - *Trục xương sống*).
   * `VIE_future_fighter_procurement` (Lựa chọn Tiêm kích Thế hệ Mới: Su-35 / Su-57 hoặc Tiêm kích phương Tây).
   * `VIE_maritime_strike_capability` (Năng lực Tấn công Tàu mặt nước từ trên không: Kh-31A/Kh-35).
   * `VIE_tactical_air_recon` (Tuần thám Biển & Trinh sát Đường không).
   * `VIE_armed_transport_helicopters` (Phi đội Trực thăng Vũ trang & Vận tải Quân sự).
4. **Tác chiến Không gian mạng & Phương tiện Không người lái (UAV):**
   * `VIE_uav_surveillance_strike` (UAV Trinh sát & Tấn công Không người lái).
   * `VIE_air_electronic_warfare` (Tác chiến Điện tử Trên không & Gây nhiễu Chủ động).
   * `VIE_cyber_command_86` (Bộ Tư lệnh Tác chiến Không gian mạng 86 & Lực lượng 47) — *Gộp Force 47 và Cyber Command*.
5. **Ngã rẽ Học thuyết Không quân (Chọn 1 trong 2):**
   * **Nhánh A: Phòng không Ô Dù & Phản Kích Cận duyên (Air Denial & Territorial Defense):**
     * `VIE_dense_interception_umbrella` (Ô Dù Đánh Chặn Dày Đặc): Tối đa hóa hiệu suất bắn hạ của tên lửa phòng không mặt đất, ngụy trang sân bay phân tán, phục kích bằng tiêm kích tầm gần.
   * **Nhánh B: Chế áp Phòng không & Đột kích Chiều sâu (SEAD & Precision Deep Strike):**
     * `VIE_precision_standoff_strike` (Năng lực Tập kích Chính xác Tầm xa): Trang bị đạn dẫn đường tầm xa, chế áp hỏa lực phòng không đối phương (SEAD), năng lực tấn công các trung tâm chỉ huy đối phương ngoài tầm mắt.
6. **Focus Đỉnh cao 2030:** `VIE_modern_air_force_2030` (Không quân Tiến thẳng lên Hiện đại 2030).

---

### TRỤ CỘT IV: CÔNG NGHIỆP QUỐC PHÒNG & NGUỒN CUNG VŨ KHÍ (18 Focus)
*Tập trung vào: Trục ngã rẽ địa chính trị hấp dẫn nhất của mod — Tự chủ nội địa Viettel/Z vs Đối tác Nga vs Đa phương hóa Phương Tây.*

```
                                [VIE_defence_industry_root]
                              LUẬT CÔNG NGHIỆP QUỐC PHÒNG
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
   NHÁNH 1: HỆ NGA TRUYỀN THỐNG    NHÁNH 2: ĐA PHƯƠNG HÓA       NHÁNH 3: TỰ LỰC NỘI ĐỊA
   - Giữ quan hệ Moskva            - Hợp tác Israel, Ấn Độ,      - Tổ hợp Viettel High-Tech
   - Nhận nhượng quyền sản xuất      Mỹ, Pháp, Hàn Quốc          - Súng bộ binh Nhà máy Z
   - Tối ưu chi phí vũ khí         - Công nghệ cao chuẩn NATO    - Tên lửa hành trình VCM-01
         │                                 │                                 │
         └─────────────────────────────────┼─────────────────────────────────┘
                                           │
                                           ▼
                            DOANH NGHIỆP QUÂN ĐỘI LÀM KINH TẾ
                       ┌───────────────────┴───────────────────┐
                       ▼                                       ▼
            Giữ mô hình Viettel / Tân Cảng            Thoái vốn thuần túy quân sự
```

1. **Gốc CNQP:** `VIE_defence_industry_law` (Luật Công nghiệp Quốc phòng & Động viên Công nghiệp).
2. **Năng lực Cơ sở Cốt lõi:**
   * `VIE_z_factories_modernization` (Hiện đại hóa Tổ hợp Nhà máy Z: Z111, Z113, Z115, Z121).
   * `VIE_infantry_weapons_indigenous` (Tự chủ Đạn dược & Súng bộ binh thế hệ mới STV-215/380) — *Gộp licensed rifles*.
   * `VIE_military_shipyards` (Mở rộng Năng lực Đóng tàu Ba Son, Nhà máy 189, Sông Thu) — *Gộp shipyards + Ba Son*.
   * `VIE_viettel_defence_complex` (Tổ hợp Công nghệ Cao Viettel High-Tech).
3. **Ngã rẽ Nguồn Cung Vũ khí (Chọn 1 trong 3 - Trục lựa chọn lớn):**
   * **Lựa chọn 1: Tiếp tục Hợp tác Sâu rộng với Nga (Truyền thống):**
     * `VIE_russian_strategic_procurement` (Hợp đồng Khung Vũ khí Nga): Mua sắm quy mô lớn với chi phí rẻ hơn 20%, nhận chuyển giao giấy phép đóng tàu và nâng cấp tăng; chấp nhận rủi ro địa chính trị khi Nga bị bao vây.
     * `VIE_russian_maintenance_centers` (Trung tâm Bảo dưỡng Vùng cho Vũ khí Nga).
   * **Lựa chọn 2: Đa phương hóa & Tiếp cận Công nghệ Phương Tây / Đối tác Mới:**
     * `VIE_western_israeli_partnerships` (Hợp tác Quốc phòng với Israel, Ấn Độ & Phương Tây): Tiếp cận hệ thống điện tử hàng không tiên tiến, UAV cao cấp, tên lửa BrahMos, radar AESA; tăng độ thân thiện với phương Tây (`VIE_ax_west`).
     * `VIE_nato_standardization_steps` (Từng bước Tiêu chuẩn hóa Khí tài Hiện đại).
   * **Lựa chọn 3: Tối đa hóa Tự chủ Tên lửa & Công nghệ Cao (Tự lực Cánh sinh):**
     * `VIE_vcm_cruise_missile_program` (Chương trình Tên lửa Hành trình VCM-01 & Tên lửa Diệt hạm Nội địa).
     * `VIE_indigenous_radar_and_drones` (Tự chủ Sản xuất Radar 3D & UAV Tác chiến Nội địa).
4. **Cơ chế Kinh tế Quân đội (Lựa chọn Độc nhất Vô nhị của Việt Nam):**
   * **Lựa chọn A (Mô hình Quân đội Lao động Sản xuất - Lịch sử):**
     * `VIE_military_corporate_titans` (Phát triển Các Tập đoàn Doanh nghiệp Quân đội): Tận dụng lợi nhuận của Viettel, Tân Cảng Sài Gòn để tái đầu tư ngân sách mua sắm vũ khí, giảm gánh nặng ngân sách nhà nước, tăng nghiên cứu quân dụng.
   * **Lựa chọn B (Chuyên nghiệp hóa Thuần túy - Quân đội không làm kinh tế):**
     * `VIE_pure_fighting_force` (Quân đội Chuyên nghiệp, Tách biệt Kinh tế): Thoái vốn toàn bộ doanh nghiệp quân đội về cho Bộ Tài chính, tập trung 100% cán bộ vào huấn luyện sẵn sàng chiến đấu; tăng độ trong sạch (`decrease_corruption`).
5. **Focus Đỉnh cao:** `VIE_defence_export_and_expo` (Triển lãm Quốc phòng Quốc tế & Xuất khẩu Khí tài "Made in Vietnam").

---

## V. MA TRẬN SO SÁNH TRƯỚC VÀ SAU CẢI TỔ

| Tiêu chí | Cây Hiện Tại (v3 lạm phát) | Cây Đề Xuất Mới (Tối ưu hóa) | Đánh giá Thay đổi |
|---|---|---|---|
| **Tổng số Focus Quân sự** | **144 focus** | **~70 focus** | **Giảm 51%**, vừa vặn hoàn hảo trong khung thời gian 2000–2030 |
| **Số tầng (Depth)** | 15 tầng dài dằng dặc | 7–8 tầng mạch lạc | Không bị đẩy xuống đáy giao diện focus tree |
| **Mức độ Trùng lặp** | Cực kỳ cao (~45 focus lặp 1:1) | **0% trùng lặp**, mỗi focus có một vai trò riêng | Giải quyết triệt để vấn đề "chỗ thừa" |
| **Tính Thực tế & Nhập vai** | Kém (Tàu sân bay, hạt nhân, viễn chinh) | **Tuyệt đối trung thực** với học thuyết QĐNDVN | Bỏ các nhánh viễn tưởng vô lý |
| **Ngã rẽ Chiến lược** | Giả tạo, không có tác động gameplay lớn | **3 ngã rẽ lớn**: Nguồn cung (Nga vs Tây vs Tự chủ); Học thuyết (A2/AD vs Biển xa); Kinh tế quân đội | Tăng mạnh giá trị chơi lại (replayability) |
| **Hệ thống Biến số (Modifiers)** | 61 biến `VIE_af_*` rối mắt, buff li ti | Giữ lại ~15 biến cốt lõi, buff trực tiếp trang bị/đơn vị | Người chơi cảm nhận rõ sức mạnh tăng vọt |
| **Tương tác Cơ chế MD** | Nhạt nhòa | Tích hợp sâu MIO (Viettel, Ba Son, Z-factories, VAECO) & Biến thể trang bị | Khai thác trọn vẹn điểm mạnh của Millennium Dawn |

---

## VI. LỘ TRÌNH THỰC HIỆN

*(Phần này để bạn tự xây dựng và định hình lộ trình triển khai)*

---
*Báo cáo nghiên cứu đã sẵn sàng để bạn bổ sung lộ trình và định hướng bước tiếp theo.*
