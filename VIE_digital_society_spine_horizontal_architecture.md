# Nhánh Khoa học số, Công nghệ & Xã hội 2045 — Kiến trúc & Bố cục Hàng ngang (Chuẩn hóa MD4)

> **Tài liệu thiết kế kiến trúc và chuẩn format (04/10/2026)**  
> **Áp dụng:** Tái cấu trúc và chuẩn hóa toàn bộ 27 focus Khoa học Công nghệ số, Hạ tầng viễn thông, Đổi mới sáng tạo & Phát triển Xã hội 2045 trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md), mô hình Hub-Spine của nhánh Chính trị ([Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md)), Kinh tế ([VIE_economic_spine_horizontal_architecture.md](VIE_economic_spine_horizontal_architecture.md)), Quân sự ([VIE_military_spine_horizontal_architecture.md](VIE_military_spine_horizontal_architecture.md)), Ngoại giao ([VIE_diplomacy_spine_horizontal_architecture.md](VIE_diplomacy_spine_horizontal_architecture.md)), Biển Đông ([VIE_scs_spine_horizontal_architecture.md](VIE_scs_spine_horizontal_architecture.md)) và Hạ tầng ([VIE_infrastructure_spine_horizontal_architecture.md](VIE_infrastructure_spine_horizontal_architecture.md)).

---

## 1. Hiện trạng & Mục tiêu Chuẩn hóa

### 1.1 Vấn đề ở kiến trúc cũ (27 focus phân tán 3 cụm)
1. **Phân mảnh nghiêm trọng trong file (3 cụm tách rời):**
   - Vệ tinh `VIE_vinasat` bị đặt đơn độc ở dòng 11036 trước cụm An ninh nội địa.
   - Cụm Xã hội 2045 (8 focus) nằm ở dòng 11220–11440.
   - Cụm Khoa học số & Viễn thông (18 focus) nằm ở dòng 11533–12090.
2. **Neo xa bất thường (Anchor jumps):** `VIE_vinasat` neo thẳng vào gốc xa `VIE_doi_moi_continues` với $dx = 82, dy = 3$ dù nó là con trực tiếp của Quỹ NAFOSTED (`VIE_nafosted`).
3. **Mạng lưới đa điều kiện (Multi-prerequisites):** `VIE_digital_nation` đòi hỏi cùng lúc 3 prerequisite dọc, `VIE_high_income_2045` và `VIE_developed_nation_2045` có 2 prerequisite dọc.

### 1.2 Giải pháp Chuẩn hóa theo Mô hình Hàng ngang
* **Quy tụ vào MỘT khối duy nhất:** Toàn bộ 27 focus được gom về vị trí liền mạch tại dòng **11180–12000** trong [VIE_md_focus.txt](file:///d:/HOI4Mods/md_vietnam/common/national_focus/VIE_md_focus.txt).
* **Hàng ngang phân tầng chiến lược & công nghệ (y = 1..6):**
  - $y = 1$: 2 Gốc chiến lược: `VIE_sci_digital_root` ($x = 156$) và `VIE_upper_middle_income` ($x = 166$).
  - $y = 2$: 5 Focus nền tảng (Internet, NAFOSTED, Tăng trưởng xanh, Quốc gia đổi mới sáng tạo, Già hóa dân số).
  - $y = 3$: 7 Focus động lực (Mạng 3G/4G, Chuyển đổi số, Viettel Global, Đại học nghiên cứu, Vinasat, Kinh tế tuần hoàn, Năng suất lao động).
  - $y = 4$: 8 Focus chuyên sâu (Mạng 5G/6G, Cáp quang biển, Định danh số VNeID, Chiến lược AI, Make in Vietnam, Nghiên cứu hạt nhân, Viễn thám vệ tinh VNREDSat, Nước thu nhập cao 2045).
  - $y = 5$: 4 Focus hoàn thiện thể chế & hạ tầng lõi (Trung tâm dữ liệu quốc gia, Luật Công nghiệp công nghệ số, Đột phá khoa học, Nước phát triển 2045).
  - $y = 6$: 1 Focus đại hội tụ: `VIE_digital_nation` (Quốc gia số toàn diện).
* **Quy tắc Prerequisite vs Available:**
  - Chỉ giữ 1 đường dọc duy nhất nối từ Cha trực tiếp trong `prerequisite = { focus = cha }`.
  - Mọi yêu cầu liên kết ngang hàng chuyển sang `available = { has_completed_focus = ... }`.
* **Khoảng cách lưới an toàn:** $\Delta x \ge 2$ tại mọi hàng, phân bố từ $x = 144$ đến $x = 170$, hoàn toàn độc lập và không va chạm với Năng lượng ($x = 106..120$) hay Quân sự ($x = 174..244$).

---

## 2. Phân rã 2 Trục Lớn: Khoa học Số & Xã hội 2045

```text
                               VIE_doi_moi_continues
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 │                                               │
        VIE_sci_digital_root                         VIE_upper_middle_income
    (Khoa học & Công nghệ số, x=156, y=1)           (Phát triển Bền vững, x=166, y=1)
                 │                                               │
      ┌──────────┴──────────┐                         ┌──────────┴──────────┐
   TRỤC 1A               TRỤC 1B                   TRỤC 2A               TRỤC 2B
HẠ TẦNG VIỄN THÔNG   NGHIÊN CỨU & VŨ TRỤ       KINH TẾ TUẦN HOÀN   THU NHẬP CAO &
& CHUYỂN ĐỔI SỐ       (NAFOSTED / VINASAT)       & ĐỔI MỚI ST        NƯỚC PHÁT TRIỂN
  (13 focus)              (6 focus)                (4 focus)            (4 focus)
  x = 144..156          x = 158..162              x = 164..168         x = 166..170
```

---

## 3. Chi tiết Bố cục & Lưới Tọa độ 27 Focus

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available (Ngang/Anh em/Thời gian) |
|:---:|---|:---:|---|---|---|
| **y = 1** | `VIE_sci_digital_root` | (156, 1) | `VIE_doi_moi_continues` (76, 1) | - | `VIE_doi_moi_continues`, `date > 2005.12.31` |
| | `VIE_upper_middle_income` | (166, 1) | `VIE_doi_moi_continues` (86, 1) | - | `date > 2029.12.31` |
| **y = 2** | `VIE_internet_expansion` | (152, 2) | `VIE_sci_digital_root` (-4, 1) | `VIE_sci_digital_root` | `date > 2005.12.31` |
| | `VIE_nafosted` | (160, 2) | `VIE_sci_digital_root` (4, 1) | `VIE_sci_digital_root` | `date > 2007.12.31` |
| | `VIE_green_growth` | (164, 2) | `VIE_upper_middle_income` (-2, 1) | `VIE_upper_middle_income` | - |
| | `VIE_innovation_nation` | (168, 2) | `VIE_upper_middle_income` (2, 1) | `VIE_upper_middle_income` | - |
| | `VIE_ageing_society` | (170, 2) | `VIE_upper_middle_income` (4, 1) | `VIE_upper_middle_income` | `date > 2032.12.31` |
| **y = 3** | `VIE_mobile_3g_4g` | (146, 3) | `VIE_internet_expansion` (-6, 1) | `VIE_internet_expansion` | `date > 2009.8.31` |
| | `VIE_national_digital_transformation` | (152, 3) | `VIE_internet_expansion` (0, 1) | `VIE_internet_expansion` | `date > 2019.12.31` |
| | `VIE_viettel_global` | (156, 3) | `VIE_internet_expansion` (4, 1) | `VIE_internet_expansion` | `date > 2005.12.31` |
| | `VIE_research_universities` | (158, 3) | `VIE_nafosted` (-2, 1) | `VIE_nafosted` | - |
| | `VIE_vinasat` | (162, 3) | `VIE_nafosted` (2, 1) | `VIE_nafosted` | `date > 2007.12.31` |
| | `VIE_carbon_circular_economy` | (164, 3) | `VIE_green_growth` (0, 1) | `VIE_green_growth` | `date > 2027.12.31` |
| | `VIE_productivity_leap` | (168, 3) | `VIE_innovation_nation` (0, 1) | `VIE_innovation_nation` | `date > 2033.12.31` |
| **y = 4** | `VIE_mobile_networks` | (144, 4) | `VIE_mobile_3g_4g` (-2, 1) | `VIE_mobile_3g_4g` | `date > 2023.12.31` |
| | `VIE_submarine_cables` | (148, 4) | `VIE_mobile_3g_4g` (2, 1) | `VIE_mobile_3g_4g` | `date > 2013.12.31` |
| | `VIE_digital_id` | (152, 4) | `VIE_national_digital_transformation` (0, 1) | `VIE_national_digital_transformation` | `date > 2022.12.31` |
| | `VIE_ai_strategy` | (154, 4) | `VIE_national_digital_transformation` (2, 1) | `VIE_national_digital_transformation` | `date > 2020.12.31` |
| | `VIE_make_in_vietnam` | (156, 4) | `VIE_viettel_global` (0, 1) | `VIE_viettel_global` | `date > 2019.5.31` |
| | `VIE_nuclear_research` | (158, 4) | `VIE_research_universities` (0, 1) | `VIE_nafosted` | - |
| | `VIE_earth_observation` | (162, 4) | `VIE_vinasat` (0, 1) | `VIE_vinasat` | `date > 2012.12.31` |
| | `VIE_high_income_2045` | (166, 4) | `VIE_carbon_circular_economy` (2, 1) | `VIE_carbon_circular_economy` | `VIE_productivity_leap`, `date > 2039.12.31` |
| **y = 5** | `VIE_national_data_center` | (152, 5) | `VIE_digital_id` (0, 1) | `VIE_digital_id` | `date > 2024.11.30` |
| | `VIE_digital_tech_industry_law` | (156, 5) | `VIE_make_in_vietnam` (0, 1) | `VIE_make_in_vietnam` | `date > 2025.6.30` |
| | `VIE_science_breakthrough` | (160, 5) | `VIE_nuclear_research` (2, 1) | `VIE_research_universities` | `date > 2024.11.30` |
| | `VIE_developed_nation_2045` | (166, 5) | `VIE_high_income_2045` (0, 1) | `VIE_high_income_2045` | `VIE_ageing_society`, `date > 2044.12.31` |
| **y = 6** | `VIE_digital_nation` | (152, 6) | `VIE_national_data_center` (0, 1) | `VIE_national_data_center` | `VIE_mobile_networks`, `VIE_ai_strategy` |

---

## 4. Kết quả Kiểm định Kỹ thuật (HOÀN TẤT 100%)

Mô hình đã được chạy kiểm tra tự động qua [tools/verify_full_tree_layout.py](tools/verify_full_tree_layout.py), [tools/test_digital_society_layout.py](tools/test_digital_society_layout.py) và [tools/check_static.py](tools/check_static.py):
* **Số lượng focus:** Khớp chính xác 27 / 27 focus (Tổng cây: 410 focus).
* **Xung đột nội bộ (Collisions):** **0 lỗi**.
* **Xung đột với các nhánh khác:** **0 lỗi** (Năng lượng ở $x = 106..120$, Khoa học & Xã hội ở $x = 144..170$, Quân sự ở $x = 174..244$).
* **Lỗi tham chiếu sớm (Forward References):** **0 lỗi** (Toàn bộ 27 focus sắp xếp theo thứ tự tô-pô chuẩn: cha luôn đứng trước con).
* **Khoảng cách tối thiểu giữa các icon:** $\Delta x \ge 2$ trên toàn bộ 6 hàng ngang ($y = 1..6$).
* **Baseline Static Validator (`check_static.py`):** Duy trì chính xác **90 errors, 1 warning** (hoàn toàn không làm phát sinh lỗi mới).
