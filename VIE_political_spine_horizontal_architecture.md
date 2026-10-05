# Nhánh Chính trị & Hệ thống Đại hội Đảng — Kiến trúc 2 Hàng Phân Định Dùng Chung & Riêng (Chuẩn hóa MD4)

> **Tài liệu thiết kế kiến trúc và chuẩn format (05/10/2026 - Bản Bố cục 2 Hàng Phân Tầng)**  
> **Áp dụng:** Tái cấu trúc toàn bộ 63 focus Chính trị (Xương sống Đại hội IX–XIV, Nhóm Dùng chung và Cánh Kiên định Hardline) trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md) (Quy tắc 4: chia 2 hàng khi số focus lớn) và Quy chuẩn trường [mục 2.1](VIE_focus_coding_standards.md).

---

## 1. Hiện trạng & Mục tiêu Chuẩn hóa

### 1.1 Vấn đề trước khi chuẩn hóa
1. **Thiếu trực quan giữa Dùng chung và Riêng:** Trước đây xếp Hardline bên trái ($X = 6..12$) và các focus thể chế bên phải ($X = 16..30$) cùng một hàng. Người chơi nhìn vào nhầm tưởng cánh phải chỉ dành cho CPV Đổi mới, không nhận biết được đây là các quyết sách DÙNG CHUNG cho cả 2 phái (Kiểm toán, Phòng chống tham nhũng, Cải cách hành chính, Luật pháp...).
2. **Hàng ngang quá dài (10–12 focus):** Nhồi nhét cả 4 cột Hardline và 6–8 focus dùng chung vào cùng một hàng ngang duy nhất khiến bề ngang bị kéo dài tới 24 ô, vi phạm khuyến nghị hàng tối đa 8 focus của Mục 7.3 Quy tắc 4.
3. **Thứ tự quan sát ngược:** Người chơi đọc từ trái sang phải thấy Hardline trước, Đại hội ở giữa, rồi mới đến các focus dùng chung ở bên phải.

### 1.2 Giải pháp Phân Tầng 2 Hàng Theo Nhiệm Kỳ (Chuẩn hóa Tuyệt đối)
* **Cột sống Trung tâm ($X = 14$):** Chuỗi Đại hội Đảng IX $\to$ X $\to$ XI $\to$ XII $\to$ XIII $\to$ XIV $\to$ Kỷ nguyên vươn mình $\to$ Kỷ niệm 100 năm thành lập Đảng.
* **Hàng 1 ($y = 1$ so với Đại hội): CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG CHO CẢ 2 PHÁI):**
  - Nằm ngay dưới mốc Đại hội, ôm sát trục giữa ($X = 10, 12, 16, 18, 20...$).
  - Có điều kiện mở dùng chung: `custom_trigger_tooltip = { tooltip = VIE_shared_focus_tt VIE_party_rule_active = yes }`.
  - Tooltip hiển thị rõ ràng: `§G[Nghị quyết Chung] Khả dụng cho cả Đảng viên Đổi mới và Phái Kiên định§!`.
* **Hàng 2 ($y = 2$ so với Đại hội): LỰA CHỌN RIÊNG THEO ĐƯỜNG LỐI (HARDLINE & REFORMIST):**
  - Nằm ở hàng tiếp theo ngay dưới hàng nghị quyết chung.
  - Cánh Tả ($X = 2, 4, 6, 8$): 4 cột trụ cương lĩnh độc quyền của CPV Kiên định (`VIE_hl_in_power = yes`):
    - Cột 1 ($X = 2$): Kinh tế Quốc doanh nòng cốt.
    - Cột 2 ($X = 4$): Chỉnh đốn Đảng & Kỷ luật sắt.
    - Cột 3 ($X = 6$): Đảng lãnh đạo tuyệt đối Lực lượng vũ trang.
    - Cột 4 ($X = 8$): Di sản ĐCS Đông Dương & Liên minh Cách mạng.
  - Cánh Hữu (tại Khóa X, $X = 18$): Lựa chọn riêng của Đổi mới (`VIE_party_members_private_business`, khóa chéo với Hardline).
* **Mốc Đại hội kế tiếp ($y = 3$ so với Đại hội trước):** Thẳng hàng trên cột sống trung tâm ($X = 14$).
* **Không cắt chéo dây (No Line Crossings):** Hàng 1 dùng các cột $X \ge 10$, trong khi Hardline ở Hàng 2 chiếm các cột $X \le 8$. Các dây nối từ Đại hội xuống Hardline đi qua khoảng trống hoàn toàn thông thoáng ở Hàng 1 ($X \le 8$), không che khuất hay xuyên qua bất kỳ focus nào.

---

## 2. Sơ đồ Bố cục Trực quan Mỗi Nhiệm kỳ

```text
Y               CỘT TRỤ KIÊN ĐỊNH (HARDLINE)         TRỤC ĐẠI HỘI        CÁC NGHỊ QUYẾT CHUNG (DÙNG CHUNG)
                 (X = 2, 4, 6, 8)                      (X = 14)               (X = 10, 12, 16, 18, 20...)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────
Y_hub                                               [ ĐẠI HỘI N ]
                                                          │
Y_hub + 1       (Thông thoáng, không có node)             ├────────► [Nghị quyết 1] [Nghị quyết 2] ...
                                                          │          (Hiển thị: §G[Nghị quyết Chung]§!)
Y_hub + 2       [Cột 1] [Cột 2] [Cột 3] [Cột 4] ◄─────────┤
                (Chỉ mở cho CPV Kiên định)                │
                                                          │
Y_hub + 3                                           [ ĐẠI HỘI N+1 ]
```

---

## 3. Bảng Tọa độ Tuyệt đối & Tương đối Chi tiết 63 Focus

### 3.1 Tiền đề & Khóa Đại hội IX (Y = 1 .. 5)

| Hàng (Y) | Focus ID | Tọa độ (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Phân nhóm | Available (Điều kiện mở) |
|:---:|---|:---:|---|:---:|---|
| **Y = 1** | `VIE_prepare_congress_9` | (14, 1) | `VIE_doi_moi_continues` (-66, 1) | Trục chính | - |
| **Y = 2** | `VIE_grassroots_democracy` | (12, 2) | `VIE_prepare_congress_9` (-2, 1) | Chuẩn bị | `VIE_prepare_congress_9` |
| | `VIE_mass_mobilization` | (16, 2) | `VIE_prepare_congress_9` (2, 1) | Chuẩn bị | `VIE_prepare_congress_9` |
| **Y = 3** | `VIE_resolution_congress_9` | (14, 3) | `VIE_prepare_congress_9` (0, 2) | Mốc Đại hội IX | `VIE_party_rule_active = yes`, `date > 2001.3.31` |
| **Y = 4** | `VIE_ethnic_policy` | (10, 4) | `VIE_resolution_congress_9` (-4, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_9` |
| | `VIE_state_audit` | (12, 4) | `VIE_resolution_congress_9` (-2, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_9` |
| | `VIE_anti_corruption_law` | (16, 4) | `VIE_resolution_congress_9` (2, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_state_audit`, `date > 2005.6.30` |
| | `VIE_national_assembly_role`| (18, 4) | `VIE_resolution_congress_9` (4, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_9` |
| | `VIE_public_admin_reform` | (20, 4) | `VIE_resolution_congress_9` (6, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `date > 2001.12.31` |
| | `VIE_decentralization` | (22, 4) | `VIE_resolution_congress_9` (8, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_public_admin_reform` |
| **Y = 5** | `VIE_hl_soe_first` | (2, 5) | `VIE_resolution_congress_9` (-12, 2) | **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_resolution_congress_9` |
| | `VIE_hl_party_rectification`| (4, 5) | `VIE_resolution_congress_9` (-10, 2) | **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_resolution_congress_9` |
| | `VIE_hl_vpa_supreme` | (6, 5) | `VIE_resolution_congress_9` (-8, 2) | **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_resolution_congress_9` |
| | `VIE_hl_icp_legacy` | (8, 5) | `VIE_resolution_congress_9` (-6, 2) | **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_resolution_congress_9` |

### 3.2 Khóa Đại hội X (Y = 6 .. 8)

| Hàng (Y) | Focus ID | Tọa độ (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Phân nhóm | Available (Điều kiện mở) |
|:---:|---|:---:|---|:---:|---|
| **Y = 6** | `VIE_resolution_congress_10`| (14, 6) | `VIE_resolution_congress_9` (0, 3) | Mốc Đại hội X | `VIE_party_rule_active = yes`, `date > 2006.3.31` |
| **Y = 7** | `VIE_anti_corruption_steering`|(12, 7) | `VIE_resolution_congress_10` (-2, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `VIE_anti_corruption_law` |
| | `VIE_asset_declaration` | (16, 7) | `VIE_resolution_congress_10` (2, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_anti_corruption_steering` |
| **Y = 8** | `VIE_hl_curb_private_capital`|(2, 8) | `VIE_resolution_congress_10` (-12, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_soe_first` |
| | `VIE_hl_central_inspection` | (4, 8) | `VIE_resolution_congress_10` (-10, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_party_rectification` |
| | `VIE_hl_ideological_commissars`|(6, 8)| `VIE_resolution_congress_10` (-8, 2) | **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_vpa_supreme` |
| | `VIE_hl_viet_lao_special_integration`|(8, 8)|`VIE_resolution_congress_10` (-6, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_icp_legacy` |
| | `VIE_party_members_private_business`|(18, 8)|`VIE_resolution_congress_10` (4, 2)| **Riêng Đổi mới** | `NOT = { VIE_hl_in_power = yes }`, khóa chéo Hardline |

### 3.3 Khóa Đại hội XI (Y = 9 .. 11)

| Hàng (Y) | Focus ID | Tọa độ (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Phân nhóm | Available (Điều kiện mở) |
|:---:|---|:---:|---|:---:|---|
| **Y = 9** | `VIE_resolution_congress_11`| (14, 9) | `VIE_resolution_congress_10` (0, 3) | Mốc Đại hội XI | `VIE_party_rule_active = yes`, `date > 2011.3.31` |
| **Y = 10**| `VIE_tw4_party_building` | (10, 10)| `VIE_resolution_congress_11` (-4, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_11` |
| | `VIE_party_inspection` | (12, 10)| `VIE_resolution_congress_11` (-2, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `VIE_tw4_party_building` |
| | `VIE_platform_2011` | (16, 10)| `VIE_resolution_congress_11` (2, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_11` |
| | `VIE_rule_of_law_state` | (18, 10)| `VIE_resolution_congress_11` (4, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_11` |
| | `VIE_constitution_2013` | (20, 10)| `VIE_resolution_congress_11` (6, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_rule_of_law_state`, `date > 2013` |
| | `VIE_disaster_law_2013` | (22, 10)| `VIE_resolution_congress_11` (8, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `date > 2013.6.19` |
| **Y = 11**| `VIE_hl_five_year_plan` | (2, 11) | `VIE_resolution_congress_11` (-12, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_curb_private_capital` |
| | `VIE_hl_national_firewall` | (4, 11) | `VIE_resolution_congress_11` (-10, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_central_inspection` |
| | `VIE_hl_defense_self_reliance`|(6, 11)| `VIE_resolution_congress_11` (-8, 2) | **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_ideological_commissars` |
| | `VIE_hl_cambodia_revolutionary_front`|(8, 11)|`VIE_resolution_congress_11` (-6, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_viet_lao_special_integration` |

### 3.4 Khóa Đại hội XII (Y = 12 .. 14)

| Hàng (Y) | Focus ID | Tọa độ (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Phân nhóm | Available (Điều kiện mở) |
|:---:|---|:---:|---|:---:|---|
| **Y = 12**| `VIE_resolution_congress_12`| (14, 12)| `VIE_resolution_congress_11` (0, 3) | Mốc Đại hội XII | `VIE_party_rule_active = yes`, `date > 2016.3.31` |
| **Y = 13**| `VIE_streamline_apparatus` | (10, 13)| `VIE_resolution_congress_12` (-4, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_12` |
| | `VIE_cybersecurity_law` | (12, 13)| `VIE_resolution_congress_12` (-2, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `date > 2018.6.12` |
| | `VIE_party_discipline` | (16, 13)| `VIE_resolution_congress_12` (2, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_party_inspection` |
| | `VIE_cadre_accountability` | (18, 13)| `VIE_resolution_congress_12` (4, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_party_discipline` |
| | `VIE_asset_recovery` | (20, 13)| `VIE_resolution_congress_12` (6, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_party_discipline` |
| | `VIE_clean_cadres` | (22, 13)| `VIE_resolution_congress_12` (8, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_cadre_accountability` |
| | `VIE_higher_education_law`| (24, 13)| `VIE_resolution_congress_12` (10, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `date > 2018.11.19` |
| | `VIE_education_law_2019` | (26, 13)| `VIE_resolution_congress_12` (12, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `date > 2019.6.14` |
| **Y = 14**| `VIE_hl_strategic_resources`|(2, 14) | `VIE_resolution_congress_12` (-12, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_five_year_plan` |
| | `VIE_hl_revolutionary_tribunals`|(4, 14)|`VIE_resolution_congress_12` (-10, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_national_firewall` |
| | `VIE_hl_peoples_war_doctrine`|(6, 14)| `VIE_resolution_congress_12` (-8, 2) | **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_defense_self_reliance` |
| | `VIE_hl_indochinese_consultative_congress`|(8, 14)|`VIE_resolution_congress_12` (-6, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_cambodia_revolutionary_front` |

### 3.5 Khóa Đại hội XIII (Y = 15 .. 17)

| Hàng (Y) | Focus ID | Tọa độ (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Phân nhóm | Available (Điều kiện mở) |
|:---:|---|:---:|---|:---:|---|
| **Y = 15**| `VIE_resolution_congress_13`| (14, 15)| `VIE_resolution_congress_12` (0, 3) | Mốc Đại hội XIII| `VIE_party_rule_active = yes`, `date > 2021.3.31` |
| **Y = 16**| `VIE_digital_anticorruption`|(10, 16)| `VIE_resolution_congress_13` (-4, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_13` |
| | `VIE_e_government` | (12, 16)| `VIE_resolution_congress_13` (-2, 1)| **Dùng chung** | `VIE_shared_focus_tt`, `VIE_resolution_congress_13` |
| | `VIE_peoples_oversight` | (16, 16)| `VIE_resolution_congress_13` (2, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `VIE_clean_cadres` |
| | `VIE_resolution_57_68` | (18, 16)| `VIE_resolution_congress_13` (4, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `date > 2025.4.30` |
| | `VIE_institutional_bottlenecks`|(20, 16)|`VIE_resolution_congress_13` (6, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `date > 2024.12.31` |
| | `VIE_civil_defense_law_2023`|(22, 16)| `VIE_resolution_congress_13` (8, 1) | **Dùng chung** | `VIE_shared_focus_tt`, `date > 2023.6.20` |
| **Y = 17**| `VIE_hl_socialist_industrialization`|(2, 17)|`VIE_resolution_congress_13` (-12, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_strategic_resources` |
| | `VIE_hl_iron_discipline_state`|(4, 17)| `VIE_resolution_congress_13` (-10, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_revolutionary_tribunals` |
| | `VIE_hl_vietnam_shield` | (6, 17) | `VIE_resolution_congress_13` (-8, 2) | **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_peoples_war_doctrine` |
| | `VIE_hl_indochinese_socialist_union`|(8, 17)|`VIE_resolution_congress_13` (-6, 2)| **Riêng Hardline**| `VIE_hl_in_power = yes`, `VIE_hl_indochinese_consultative_congress`|

### 3.6 Khóa Đại hội XIV & Đỉnh cao Thế kỷ (Y = 18 .. 21)

| Hàng (Y) | Focus ID | Tọa độ (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Phân nhóm | Available (Điều kiện mở) |
|:---:|---|:---:|---|:---:|---|
| **Y = 18**| `VIE_resolution_congress_14`| (14, 18)| `VIE_resolution_congress_13` (0, 3) | Mốc Đại hội XIV | `VIE_party_rule_active = yes`, `date > 2026.1.15` |
| **Y = 19**| `VIE_hl_unbreakable_fortress`|(6, 19) | `VIE_resolution_congress_14` (-8, 1)| Lựa chọn Hardline | `VIE_hl_in_power = yes`, loại trừ 2 lựa chọn Đổi mới |
| | `VIE_concentration_of_power`|(16, 19)| `VIE_resolution_congress_14` (2, 1) | Lựa chọn Đổi mới 1 | `NOT = { VIE_hl_in_power = yes }`, loại trừ 2 lựa chọn còn lại |
| | `VIE_institutional_opening` |(20, 19)| `VIE_resolution_congress_14` (6, 1) | Lựa chọn Đổi mới 2 | `NOT = { VIE_hl_in_power = yes }`, loại trừ 2 lựa chọn còn lại |
| **Y = 20**| `VIE_era_of_rising` | (14, 20)| `VIE_resolution_congress_14` (0, 2) | **Đỉnh cao Chung**| Hoàn thành 1 trong 3 lựa chọn Khóa XIV, `date > 2026.1.15` |
| **Y = 21**| `VIE_party_centennial_2030` | (14, 21)| `VIE_era_of_rising` (0, 1) | **Đỉnh cao Chung**| `VIE_era_of_rising`, `date > 2029.12.31` |

---

## 4. Kết quả Kiểm tra & Thẩm định Tính toàn vẹn

1. **Kiểm tra Tọa độ Tuyệt đối & Lưới Focus (`tools/test_hardline_layout.py`):**
   - Đã kiểm tra 63/63 focus.
   - **0 trùng tọa độ (Collisions = 0).**
   - **0 vi phạm khoảng cách ngang (Gap < 2 = 0).** Mọi focus cùng hàng đều cách nhau tối thiểu 2 ô (gap = 2 hoặc 4).
   - Chiều ngang tối đa mỗi hàng: 16 ô (từ $X = 10$ đến $X = 26$), 100% tuân thủ Mục 7.3 Quy tắc 4.
2. **Kiểm tra Toàn cục Hệ thống (`tools/check_static.py`):**
   - Baseline giữ nguyên: **90 errors, 1 warnings** (0 lỗi mới phát sinh).
   - Cân bằng ngoặc nhọn `{}` hoàn hảo: 100% tệp tin hợp lệ.
3. **Hiển thị Trực quan Trong Game (In-game Experience):**
   - Người chơi hover vào bất kỳ focus dùng chung nào đều thấy tooltip nổi bật: `§G[Nghị quyết Chung] Khả dụng cho cả Đảng viên Đổi mới và Phái Kiên định§!`.
   - Các dây liên kết (prerequisite lines) thẳng hàng tuyệt đối, không có hiện tượng dây chéo hay dây đè lên icon focus.
