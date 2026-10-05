# Nhánh Ngoại giao & ASEAN — Kiến trúc & Bố cục Hàng ngang (Chuẩn hóa MD4)

> **Tài liệu thiết kế kiến trúc và chuẩn format (04/10/2026)**  
> **Áp dụng:** Tái cấu trúc và chuẩn hóa toàn bộ 33 focus Ngoại giao & ASEAN trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md), mô hình Hub-Spine của nhánh Chính trị ([Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md)), Kinh tế ([VIE_economic_spine_horizontal_architecture.md](VIE_economic_spine_horizontal_architecture.md)) và Quân sự ([VIE_military_spine_horizontal_architecture.md](VIE_military_spine_horizontal_architecture.md)).

---

## 1. Hiện trạng & Mục tiêu Chuẩn hóa

### 1.1 Vấn đề ở kiến trúc cũ (33 focus phân tán)
1. **Phân mảnh nghiêm trọng trong file (6 cụm rời rạc):** 33 focus ngoại giao bị rải rác ở 6 vị trí khác nhau trong file, bị xen ngang bởi Vệ tinh Vinasat, An ninh mạng, Xã hội thu nhập trung bình và Hạ tầng metro.
2. **Neo xa / Neo lung tung:** Quá nhiều focus neo thẳng vào gốc `VIE_asean_integration` với khoảng cách rất lớn ($dx = -14, dx = 14$), không tuân theo nguyên tắc cha-con trực tiếp.
3. **Mạng lưới dây chéo (Spaghetti links):** Nhiều focus có đa điều kiện tiên quyết (ví dụ: `VIE_indochina_solidarity` đòi cả Lào và Campuchia; `VIE_csp_network` đòi cả Ấn Độ và Hàn Quốc; `VIE_un_security_council` đòi APEC...).
4. **Lệch pha thời gian & tầng hàng:** Nhiều mốc thời gian (2000, 2006, 2013, 2023) bị xếp lẫn lộn trên các hàng không đồng nhất.

### 1.2 Giải pháp Chuẩn hóa theo Mô hình Hàng ngang
* **Quy tụ vào MỘT khối duy nhất:** Toàn bộ 33 focus được gom về vị trí gốc `VIE_asean_integration` (ngay trước nhánh Biển Đông `VIE_law_of_the_sea`).
* **Hàng ngang phân tầng lịch sử:** 
  - $y = 11$: Gốc `VIE_asean_integration`
  - $y = 12$: 5 Mốc khởi đầu của 5 Trục quan hệ đối ngoại.
  - $y = 13$: Các hiệp định và đối tác chiến lược giai đoạn 2006–2013.
  - $y = 14$: Mở rộng mạng lưới đối tác toàn diện & đa phương 2014–2020.
  - $y = 15$: Nâng tầm đối ngoại, gỡ cấm vận & đỉnh cao Ngoại giao Cây tre.
  - $y = 16$: Mốc tương lai / Cộng đồng chia sẻ tương lai 2023+.
* **Quy tắc Prerequisite vs Available:** 
  - Chỉ giữ 1 đường dọc duy nhất nối từ Cha trực tiếp trong `prerequisite = { focus = cha }`.
  - Mọi yêu cầu liên kết ngang hàng chuyển sang `available = { has_completed_focus = ... }`.
* **Khoảng cách lưới an toàn:** $\Delta x \ge 2$ tại mọi hàng, đối xứng quanh trục trung tâm $x = 48$.

---

## 2. Phân rã 5 Trục Đối ngoại & Ngoại giao

Nhánh Ngoại giao tỏa ra từ gốc chung `VIE_asean_integration` tại tọa độ $x = 48, y = 11$:

```text
                               VIE_doi_moi_continues
                                         │
                               VIE_asean_integration
                             (Hội nhập ASEAN, x=48, y=11)
                                         │
     ┌──────────────┬────────────────────┼───────────────────┬──────────────┐
  TRỤC 1         TRỤC 2               TRỤC 3              TRỤC 4         TRỤC 5
VIỆT - TRUNG   LÀO & CAMPUCHIA      TRỌNG TÂM ASEAN     VIỆT - MỸ     ĐỐI TÁC CHIẾN LƯỢC
& BIÊN GIỚI     & MÊ KÔNG            & ĐA PHƯƠNG                      & CÂY TRE
(6 focus)      (7 focus)            (5 focus)           (5 focus)     (9 focus)
 x = 34..38     x = 40..44           x = 46..50          x = 52..54    x = 56..62
```

---

## 3. Chi tiết Bố cục & Lưới Tọa độ từng Trục

### 3.1 Bảng Tọa độ & Tham chiếu 33 Focus Ngoại giao

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available (Ngang/Anh em) |
|:---:|---|:---:|---|---|---|
| **y = 11** | `VIE_asean_integration` | (48, 11) | `VIE_doi_moi_continues` (-32, 11) | - | - |
| **y = 12** | `VIE_gulf_of_tonkin` | (36, 12) | `VIE_asean_integration` (-12, 1) | `VIE_asean_integration` | `date > 2000.11.30` |
| | `VIE_special_relations_laos` | (40, 12) | `VIE_asean_integration` (-8, 1) | `VIE_asean_integration` | - |
| | `VIE_cambodia_relations` | (44, 12) | `VIE_asean_integration` (-4, 1) | `VIE_asean_integration` | - |
| | `VIE_asean_chair` | (48, 12) | `VIE_asean_integration` (0, 1) | `VIE_asean_integration` | `date > 2009.12.31` |
| | `VIE_us_engagement` | (52, 12) | `VIE_asean_integration` (4, 1) | `VIE_asean_integration` | `date > 2000.9.30` |
| | `VIE_japan_partnership` | (58, 12) | `VIE_asean_integration` (10, 1) | `VIE_asean_integration` | `date > 2005.12.31` |
| **y = 13** | `VIE_border_settlement` | (36, 13) | `VIE_gulf_of_tonkin` (0, 1) | `VIE_gulf_of_tonkin` | - |
| | `VIE_mekong_commission` | (40, 13) | `VIE_special_relations_laos` (0, 1)| `VIE_special_relations_laos` | - |
| | `VIE_cambodia_border` | (44, 13) | `VIE_cambodia_relations` (0, 1) | `VIE_cambodia_relations` | - |
| | `VIE_code_of_conduct` | (46, 13) | `VIE_asean_chair` (-2, 1) | `VIE_asean_chair` | `date > 2012.12.31` |
| | `VIE_apec_host` | (50, 13) | `VIE_asean_chair` (2, 1) | `VIE_asean_chair` | - |
| | `VIE_us_comprehensive_partnership`| (52, 13) | `VIE_us_engagement` (0, 1) | `VIE_us_engagement` | `date > 2012.12.31` |
| | `VIE_korea_partnership` | (56, 13) | `VIE_japan_partnership` (-2, 1) | `VIE_japan_partnership` | `date > 2008.12.31` |
| | `VIE_india_partnership` | (58, 13) | `VIE_japan_partnership` (0, 1) | `VIE_japan_partnership` | `date > 2006.12.31` |
| | `VIE_australia_partnership` | (60, 13) | `VIE_japan_partnership` (2, 1) | `VIE_japan_partnership` | `date > 2008.12.31` |
| | `VIE_france_eu` | (62, 13) | `VIE_japan_partnership` (4, 1) | `VIE_japan_partnership` | - |
| **y = 14** | `VIE_16_words` | (36, 14) | `VIE_border_settlement` (0, 1) | `VIE_border_settlement` | - |
| | `VIE_mekong_dams_response` | (40, 14) | `VIE_mekong_commission` (0, 1) | `VIE_mekong_commission` | `date > 2015.12.31` |
| | `VIE_funan_techo_response` | (44, 14) | `VIE_cambodia_border` (0, 1) | `VIE_cambodia_border` | `date > 2024.6.30` |
| | `VIE_un_security_council` | (48, 14) | `VIE_apec_host` (-2, 1) | `VIE_asean_chair` | `VIE_apec_host` |
| | `VIE_us_embargo_lifted` | (52, 14) | `VIE_us_comprehensive_partnership` (0, 1) | `VIE_us_comprehensive_partnership` | - |
| | `VIE_gulf_investment` | (56, 14) | `VIE_korea_partnership` (0, 1) | `VIE_korea_partnership` | - |
| | `VIE_csp_network` | (58, 14) | `VIE_india_partnership` (0, 1) | `VIE_india_partnership` | `VIE_korea_partnership`, `date > 2023.8.31` |
| | `VIE_global_south_ties` | (60, 14) | `VIE_australia_partnership` (0, 1)| `VIE_australia_partnership` | - |
| **y = 15** | `VIE_border_trade_gates` | (34, 15) | `VIE_16_words` (-2, 1) | `VIE_16_words` | - |
| | `VIE_defence_hotline` | (38, 15) | `VIE_16_words` (2, 1) | `VIE_16_words` | `date > 2011.12.31` |
| | `VIE_indochina_solidarity` | (42, 15) | `VIE_mekong_dams_response` (2, 1)| `VIE_special_relations_laos` | `VIE_cambodia_relations` |
| | `VIE_multilateral_champion` | (48, 15) | `VIE_un_security_council` (0, 1) | `VIE_un_security_council` | `date > 2021.1.1` |
| | `VIE_us_carrier_visit` | (52, 15) | `VIE_us_embargo_lifted` (0, 1) | `VIE_us_embargo_lifted` | `date > 2017.12.31` |
| | `VIE_us_tariff_deal` | (54, 15) | `VIE_us_embargo_lifted` (2, 1) | `VIE_us_embargo_lifted` | `date > 2025.7.31` |
| | `VIE_bamboo_diplomacy` | (58, 15) | `VIE_csp_network` (0, 1) | `VIE_csp_network` | - |
| **y = 16** | `VIE_shared_future` | (36, 16) | `VIE_border_trade_gates` (2, 1) | `VIE_16_words` | `border_trade_gates`, `defence_hotline`, `date > 2022.12.31` |

---

## 4. Kết quả Kiểm định Kỹ thuật (HOÀN TẤT 100%)

Mô hình đã được chạy kiểm tra tự động qua [tools/verify_full_tree_layout.py](tools/verify_full_tree_layout.py) và [tools/check_static.py](tools/check_static.py):
* **Số lượng focus:** Khớp chính xác 33 / 33 focus Ngoại giao (Tổng cây: 410 focus).
* **Xung đột nội bộ (Collisions):** **0 lỗi**.
* **Xung đột với các nhánh khác:** **0 lỗi**.
* **Vi phạm khoảng cách ($\Delta x < 2$):** **0 lỗi**.
* **Vi phạm độ sâu ($y_{child} \le y_{parent}$):** **0 lỗi**.
* **Tham chiếu tiến (`relative_position_id` forward reference):** **0 lỗi** (toàn bộ 33 focus tuân thủ nghiêm ngặt Cha khai báo trước Con trong file).
* **Trình kiểm tra tĩnh `check_static.py`:** Giữ vững baseline **90 errors, 1 warning**.

