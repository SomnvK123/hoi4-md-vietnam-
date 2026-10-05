# Nhánh Biển Đông & Luật Biển — Kiến trúc & Bố cục Hàng ngang Tối ưu (Chuẩn hóa MD4)

> **Tài liệu thiết kế kiến trúc và chuẩn format (04/10/2026 - Bản Rút Gọn Spacing)**  
> **Áp dụng:** Tái cấu trúc, rút gần khoảng cách x-y và chuẩn hóa toàn bộ 24 focus Biển Đông trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md), quy hoạch thống nhất cùng nhánh Quân sự, Chính trị và Kinh tế.

---

## 1. Hiện trạng & Lý do Tối ưu Rút gần (Compaction)

### 1.1 Vấn đề ở bản bố cục ban đầu
1. **Bước nhảy ngang từ gốc quá rộng ($dx = \pm 10$):** Hàng $y = 13$ tỏa từ gốc `VIE_law_of_the_sea` $(76, 12)$ sang 2 cánh với $dx = -10$ (`legal_warfare` tại $x = 66$) và $dx = +10$ (`scs_maritime_cooperation` tại $x = 86$), tạo ra 2 đường nối kéo chéo quá dài.
2. **Khoảng trống ngang xen kẽ ở hàng $y = 14$:** Các focus hàng $y = 14$ dùng bước $\Delta x = 4$ ở một số vị trí, bỏ trống các tọa độ chẵn ($x = 72, 76$).
3. **Độ rộng chiếm dụng:** Toàn nhánh trải rộng từ $x = 66$ đến $x = 88$ (span 22).

### 1.2 Giải pháp Tối ưu Rút gần
* **Bó gọn hàng $y = 13$:** Thu hẹp từ $x = 66..86$ (span 20) về **$x = 70..84$ (span 14)**. Các bước nhảy từ gốc $76$ giảm từ $\pm 10$ xuống chỉ còn $-6 .. +8$.
* **Điền kín hàng $y = 14$:** Toàn bộ 9 focus ở hàng $y = 14$ được xếp liên tục với bước chuẩn $\Delta x = 2$ ($x = 70, 72, 74, 76, 78, 80, 82, 84, 86$), xóa bỏ hoàn toàn các lỗ thủng ngang.
* **Mọi bước nhảy từ hàng 14 xuống 15:** Đạt $dx = 0$ hoàn hảo, các focus con đứng thẳng hàng trực tiếp dưới focus cha.
* **Thu hẹp độ rộng toàn nhánh:** Giảm từ $x = 66..88$ xuống **$x = 70..86$ (span 16)**.

---

## 2. Sơ đồ Kiến trúc Tổng quan Sau Rút Gọn

```text
                               VIE_doi_moi_continues
                                         │ (dx=-4, dy=12)
                                VIE_law_of_the_sea
                            (Luật Biển VN 2012, x=76, y=12)
                                         │
        ┌───────────────┬────────────────┼────────────────┬───────────────┐
     dx = -6         dx = -4          dx = -2          dx = +4         dx = +8
      TRỤC 1          TRỤC 2           TRỤC 3           TRỤC 4          TRỤC 5
   ĐẤU TRANH       THỰC THI &       BẢO VỆ ĐẢO &       QUỐC PHÒNG      HỢP TÁC
   PHÁP LÝ &       TUẦN TRA         CHIẾN LƯỢC DK1     TOÀN DÂN &       QUỐC TẾ
  CHỦ QUYỀN       KIỂM NGƯ         (HẢI QUÂN ĐÁNH BỘ) KHÔNG GIAN MẠNG  BIỂN ĐÔNG
   (4 focus)       (3 focus)        (6 focus)          (7 focus)       (4 focus)
     x = 70..74        x = 74..76       x = 76..78         x = 78..82      x = 84..86
```

---

## 3. Bảng Tọa độ Chi tiết 24 Focus Biển Đông

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available (Ngang/Anh em/Thời gian) |
|:---:|---|:---:|---|---|---|
| **y = 12** | `VIE_law_of_the_sea` | (76, 12) | `VIE_doi_moi_continues` (-4, 12) | - | `date > 2011.12.31` |
| **y = 13** | `VIE_legal_warfare` | (70, 13) | `VIE_law_of_the_sea` (-6, 1) | `VIE_law_of_the_sea` | `date > 2016.7.31` |
| | `VIE_assert_maritime_rights` | (72, 13) | `VIE_law_of_the_sea` (-4, 1) | `VIE_law_of_the_sea` | `VIE_scs_escalated_trigger` (Loại trừ `VIE_legal_warfare`) |
| | `VIE_fisheries_surveillance` | (74, 13) | `VIE_law_of_the_sea` (-2, 1) | `VIE_law_of_the_sea` | `date > 2012.12.31` |
| | `VIE_maritime_militia` | (76, 13) | `VIE_law_of_the_sea` (0, 1) | `VIE_law_of_the_sea` | - |
| | `VIE_peoples_defence` | (80, 13) | `VIE_law_of_the_sea` (4, 1) | `VIE_law_of_the_sea` | `VIE_modernize_vpa` |
| | `VIE_scs_maritime_cooperation` | (84, 13) | `VIE_law_of_the_sea` (8, 1) | `VIE_law_of_the_sea` | `VIE_asean_integration`, `date > 2011.12.31` |
| **y = 14** | `VIE_limited_war_doctrine` | (70, 14) | `VIE_assert_maritime_rights` (-2, 1) | `VIE_assert_maritime_rights` | `VIE_legal_warfare` |
| | `VIE_paracel_ultimatum` | (72, 14) | `VIE_assert_maritime_rights` (0, 1) | `VIE_assert_maritime_rights` | `VIE_party_rule_active`, `country_exists = CHI` |
| | `VIE_coast_guard_law` | (74, 14) | `VIE_fisheries_surveillance` (0, 1) | `VIE_fisheries_surveillance` | `date > 2018.12.31` |
| | `VIE_spratly_fortification` | (76, 14) | `VIE_maritime_militia` (0, 1) | `VIE_maritime_militia` | `date > 2020.12.31` |
| | `VIE_provincial_defence_zones` | (78, 14) | `VIE_peoples_defence` (-2, 1) | `VIE_peoples_defence` | - |
| | `VIE_force_47` | (80, 14) | `VIE_peoples_defence` (0, 1) | `VIE_peoples_defence` | `date > 2017.11.30` |
| | `VIE_un_peacekeeping` | (82, 14) | `VIE_peoples_defence` (2, 1) | `VIE_peoples_defence` | `date > 2013.12.31` |
| | `VIE_scs_multilateral_exercise` | (84, 14) | `VIE_scs_maritime_cooperation` (0, 1) | `VIE_scs_maritime_cooperation` | - |
| | `VIE_scs_cam_ranh_port` | (86, 14) | `VIE_scs_maritime_cooperation` (2, 1) | `VIE_scs_maritime_cooperation` | `has_idea = VIE_four_nos` OR `VIE_non_alignment_policy` |
| **y = 15** | `VIE_retake_north_spratlys` | (72, 15) | `VIE_paracel_ultimatum` (0, 1) | `VIE_paracel_ultimatum` | `VIE_party_rule_active`, `country_exists = CHI` |
| | `VIE_dk1_platforms` | (76, 15) | `VIE_spratly_fortification` (0, 1) | `VIE_spratly_fortification` | `VIE_coast_guard_law` |
| | `VIE_militia_law` | (78, 15) | `VIE_provincial_defence_zones` (0, 1) | `VIE_provincial_defence_zones` | `date > 2019.6.30` |
| | `VIE_cyber_command` | (80, 15) | `VIE_force_47` (0, 1) | `VIE_force_47` | `date > 2017.12.31` |
| | `VIE_four_nos_doctrine` | (82, 15) | `VIE_un_peacekeeping` (0, 1) | `VIE_un_peacekeeping` | `has_idea = VIE_four_nos` |
| | `VIE_scs_joint_training` | (84, 15) | `VIE_scs_multilateral_exercise` (0, 1) | `VIE_scs_multilateral_exercise` | `VIE_scs_cam_ranh_port`, đối tác JP/IN/Kilo |
| **y = 16** | `VIE_retake_east_spratlys` | (70, 16) | `VIE_retake_north_spratlys` (-2, 1) | `VIE_retake_north_spratlys` | `VIE_party_rule_active`, `country_exists = PHI` |
| | `VIE_retake_south_spratlys` | (74, 16) | `VIE_retake_north_spratlys` (2, 1) | `VIE_retake_north_spratlys` | `VIE_party_rule_active`, `country_exists = MAY` |

---

## 4. Kết quả Kiểm định Kỹ thuật (HOÀN TẤT 100%)

Đã chạy kiểm tra tự động qua các script kiểm định mod:
* **Số lượng focus:** Khớp chính xác 24 / 24 focus Biển Đông (Tổng cây: 410 focus).
* **Xung đột nội bộ (Collisions):** **0 lỗi**.
* **Xung đột ngoại vi:** **0 lỗi** (Ngoại giao ở $x = 34..62$, Biển Đông ở $x = 70..86$, An ninh ở $x = 91..95$, Quân sự ở $x = 180..220$).
* **Lỗi tham chiếu sớm (Forward References):** **0 lỗi**.
* **Khoảng cách tối thiểu giữa các icon:** $\Delta x \ge 2$ trên toàn bộ các hàng ngang ($y = 12..16$).
* **Baseline Static Validator (`check_static.py`):** Đạt mức chuẩn **90 errors, 1 warning** (khớp baseline).
