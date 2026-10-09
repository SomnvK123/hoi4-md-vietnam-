> **PK-KQ v19 (09/10/2026):** không quân hiện có 33 focus, một hàng lựa chọn sau củng cố và ba cụm chuyên ngành mở ngang. [Kiến trúc hiện hành](VIE_air_force_documentation.md), [sơ đồ/kiểm định](.claude/docs/air/validation.md). Các mô tả PK-KQ v18 phía dưới là lịch sử.

# Kiến trúc & Quy chuẩn Bố cục Hàng ngang Focus Tree Việt Nam (MD4)

> **Tài liệu tổng hợp kiến trúc hệ thống (08/10/2026)**  
> Hợp nhất toàn bộ 8 trục nhánh kiến trúc hàng ngang trong cây Focus Quốc gia VIE_md_focus.txt.

## Mục lục
1. [Nhánh Quân sự](#nhánh-quân-sự)
2. [Nhánh Chính trị & Hệ thống Đại hội Đảng](#nhánh-chính-trị--hệ-thống-đại-hội-đảng)
3. [Nhánh Kinh tế](#nhánh-kinh-tế)
4. [Nhánh Kết cấu Hạ tầng & Giao thông](#nhánh-kết-cấu-hạ-tầng--giao-thông)
5. [Nhánh Khoa học số, Công nghệ & Xã hội 2045](#nhánh-khoa-học-số-công-nghệ--xã-hội-2045)
6. [Nhánh Ngoại giao & ASEAN](#nhánh-ngoại-giao--asean)
7. [Nhánh Biển Đông & Luật Biển](#nhánh-biển-đông--luật-biển)
8. [Nhánh An ninh Nội địa & Không gian mạng](#nhánh-an-ninh-nội-địa--không-gian-mạng)

---
## Nhánh Quân sự

# Nhánh Quân sự — Kiến trúc & Bố cục Hàng ngang Tối ưu (Chuẩn hóa MD4)

> **Cập nhật PK-KQ v18 — 08/10/2026:** phần kiến trúc không quân bên dưới là lịch sử. Bản hiện hành có 36 focus, hai cụm lực lượng/công nghiệp dưới root không quân chung, năm tầng lực lượng, cơ cấu tác chiến trên focus, ba cụm năng lực cùng tồn tại. [Thiết kế hiện hành](VIE_air_force_documentation.md), [sơ đồ và kiểm định](.claude/docs/air/validation.md). Chưa nghiệm thu trong HOI4. Quy tắc nén bỏ mọi hàng trống/giấu phụ thuộc hoặc mutex cả cụm của bản cũ không áp dụng cho PK-KQ v18.


> **Tài liệu thiết kế kiến trúc và chuẩn format (04/10/2026 - Bản Rút Gọn Spacing)**  
> **Áp dụng:** Tái cấu trúc, rút gần khoảng cách x-y và chuẩn hóa toàn bộ 92 focus Quân sự trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md), mô hình Hub-Spine của nhánh Chính trị ([Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md)) và nhánh Kinh tế ([VIE_economic_spine_horizontal_architecture.md](VIE_economic_spine_horizontal_architecture.md)).

---

## 1. Hiện trạng & Lý do Tối ưu Rút gần (Compaction)

### 1.1 Vấn đề ở bản bố cục ban đầu
1. **Khoảng cách gốc quá xa (dx quá lớn):** Focus gốc `VIE_modernize_vpa` (x=210) vươn sang Lục quân `VIE_lf_army_reform` với $dx = -26$, và vươn sang Không quân `VIE_airf_training_standardization` với $dx = +22$, tạo ra 2 đường nối kéo dài vắt ngang màn hình.
2. **Khoảng trống dọc (dy = 2 sinh ra hàng rỗng):**
   - Hải quân: `VIE_nf_command_reform_1` (y=4) nối xuống `VIE_nf_first_force` (y=6) với $dy = 2$, bỏ trống hàng y=5 ở cột Hải quân.
   - APM (Phòng không): `VIE_apm_a32` và `VIE_apm_radar` (y=4) nhảy xuống `VIE_apm_integration` và `VIE_apm_uav` (y=6) với $dy = 2$, tiếp tục nhảy xuống `VIE_apm_mature` (y=8) với $dy = 2$, tạo ra các lỗ hổng tại y=5 và y=7.
3. **Các bước nhảy ngang nội bộ lớn ($|dx| \ge 6..8$):**
   - Lục quân: `VIE_lf_army_reform` sang `VIE_def_industry_law` ($dx = -8$), `VIE_lf_basic_training` sang `VIE_lf_arm_engineers` ($dx = +8$).
   - Hải quân: `VIE_nf_training_standardization` sang `VIE_nf_surface_force` ($dx = -6$), `VIE_nf_operating_range` sang `VIE_nf_bluewater` ($dx = +8$), `VIE_nf_bluewater` sang `VIE_nf_naval_aviation` ($dx = +6$).
   - Không quân: `VIE_airf_training_standardization` sang `VIE_airf_fighter_force` ($dx = -6$), `VIE_apm_law` sang `VIE_apm_radar` ($dx = +6$), `VIE_airf_operating_range` sang `VIE_airf_unmanned` ($dx = +6$).
4. **Độ rộng chiếm dụng quá lớn:** Nhánh trải từ $x = 174$ đến $x = 244$ (rộng 70 đơn vị), giữa các quân chủng có nhiều khoảng trống 10–18 ô.

### 1.2 Giải pháp Tối ưu Rút gần
* **Thu hẹp tổng chiều ngang:** Giảm từ 70 cột ($x = 174..244$) xuống còn **40 cột ($x = 180..220$)**, tiết kiệm 30 cột (giảm 43% độ choán ngang).
* **Đưa gốc về đối xứng hoàn hảo:** Đặt `VIE_modernize_vpa` tại $(200, 1)$ ngay trên Hải quân:
  - Sang Lục quân: $dx = -14$ (giảm từ $-26$).
  - Sang Hải quân: $dx = 0$ (trục trung tâm).
  - Sang Không quân: $dx = +14$ (giảm từ $+22$).
  - Đối xứng gương hoàn hảo $|-14| = |+14|$.
* **Xóa bỏ 100% bước nhảy dọc rỗng ($dy = 2 \to dy = 1$):**
  - Hải quân: Đưa `VIE_nf_first_force` lên $y = 5$ (ngang hàng với Ba Son Shipyards), liên kết $dy = 1$.
  - APM: Đưa `VIE_apm_integration` & `VIE_apm_uav` lên $y = 5$, và `VIE_apm_mature` lên $y = 6$. Toàn bộ APM kết thúc gọn gàng tại $y = 6$.
* **Triệt tiêu các bước nhảy ngang lớn nội bộ:** Mọi bước nhảy bên trong 3 quân chủng đều rút về $|dx| \le 4$ (đa số là $dx \in \{-2, 0, 2\}$).
* **Khoảng cách phân cách giữa 3 quân chủng:**
  - Lục quân ($x = 180..190$) cách Hải quân ($x = 194..206$) đúng **4 ô**.
  - Hải quân ($x = 194..206$) cách Không quân ($x = 210..220$) đúng **4 ô**.

---

## 2. Sơ đồ Kiến trúc Tổng quan Sau Rút Gọn

```text
                                VIE_doi_moi_continues
                                          │ (dx=120, dy=1)
                                  VIE_modernize_vpa
                              (Hiện đại hóa QĐNDVN, x=200, y=1)
                                          │
          ┌───────────────────────────────┼───────────────────────────────┐
       dx = -14                        dx = 0                          dx = +14
       TRỤC 1                          TRỤC 2                          TRỤC 3
      LỤC QUÂN                        HẢI QUÂN                      PHÒNG KHÔNG
   & CNQP LỤC QUÂN               & ĐÓNG TÀU BA SON                 - KHÔNG QUÂN
    (34 focuses)                    (28 focuses)                    (29 focuses)
    x = 180..190                    x = 194..206                    x = 210..220
    (Tâm x = 186)                   (Tâm x = 200)                   (Tâm x = 214)
          │                               │                               │
   ◄── Cách 4 ô ──►                ◄── Cách 4 ô ──►
```

---

## 3. Bảng Tọa độ Chi tiết Từng Trục

### 3.1 TRỤC 1: Lục quân Nhân dân & CNQP Lục quân (34 focus)
* **Vùng tọa độ:** $x = 180 .. 190$ (Tâm $x = 186$)
* **Gốc trục:** `VIE_lf_army_reform` ($x = 186, y = 2$).

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available (Ngang/Anh em) |
|:---:|---|:---:|---|---|---|
| **y = 2** | `VIE_lf_army_reform` | (186, 2) | `VIE_modernize_vpa` (-14, 1) | `VIE_modernize_vpa` | - |
| **y = 3** | `VIE_def_industry_law` | (182, 3) | `VIE_lf_army_reform` (-4, 1) | `VIE_lf_army_reform` | - |
| | `VIE_lf_logistics_merge` | (184, 3) | `VIE_lf_army_reform` (-2, 1) | `VIE_lf_army_reform` | - |
| | `VIE_lf_basic_training` | (188, 3) | `VIE_lf_army_reform` (2, 1) | `VIE_lf_army_reform` | - |
| **y = 4** | `VIE_military_enterprises_core` | (180, 4) | `VIE_def_industry_law` (-2, 1) | `VIE_def_industry_law` | - |
| | `VIE_military_enterprises_divest`| (182, 4) | `VIE_def_industry_law` (0, 1) | `VIE_def_industry_law` | - |
| | `VIE_lf_arm_infantry_org` | (184, 4) | `VIE_lf_logistics_merge` (0, 1) | `VIE_lf_logistics_merge` | `VIE_lf_basic_training` |
| | `VIE_lf_arm_armor_org` | (186, 4) | `VIE_lf_basic_training` (-2, 1) | `VIE_lf_basic_training` | `VIE_lf_logistics_merge` |
| | `VIE_lf_arm_arty_org` | (188, 4) | `VIE_lf_basic_training` (0, 1) | `VIE_lf_basic_training` | `VIE_lf_logistics_merge` |
| | `VIE_lf_arm_engineers` | (190, 4) | `VIE_lf_basic_training` (2, 1) | `VIE_lf_basic_training` | `VIE_lf_logistics_merge` |
| **y = 5** | `VIE_path_self_reliant_deterrence`| (182, 5) | `VIE_military_enterprises_divest` (0, 1) | `VIE_military_enterprises_divest` | - |
| | `VIE_lf_arm_infantry_train` | (184, 5) | `VIE_lf_arm_infantry_org` (0, 1) | `VIE_lf_arm_infantry_org` | - |
| | `VIE_lf_arm_armor_train` | (186, 5) | `VIE_lf_arm_armor_org` (0, 1) | `VIE_lf_arm_armor_org` | - |
| | `VIE_lf_arm_arty_train` | (188, 5) | `VIE_lf_arm_arty_org` (0, 1) | `VIE_lf_arm_arty_org` | - |
| **y = 6** | `VIE_lf_combined_arms` | (186, 6) | `VIE_lf_arm_armor_train` (0, 1) | `VIE_lf_arm_armor_train` | `infantry_train`, `arty_train`, `engineers` |
| **y = 7** | `VIE_lf_command_reform_1` | (186, 7) | `VIE_lf_combined_arms` (0, 1) | `VIE_lf_combined_arms` | - |
| **y = 8** | `VIE_lf_fs_mobile_force` | (184, 8) | `VIE_lf_command_reform_1` (-2, 1) | `VIE_lf_command_reform_1` | - |
| | `VIE_lf_fs_main_corps` | (186, 8) | `VIE_lf_command_reform_1` (0, 1) | `VIE_lf_command_reform_1` | - |
| | `VIE_lf_fs_depth_defence` | (188, 8) | `VIE_lf_command_reform_1` (2, 1) | `VIE_lf_command_reform_1` | - |
| **y = 9** | `VIE_lf_fs_mobile_corps` | (184, 9) | `VIE_lf_fs_mobile_force` (0, 1) | `VIE_lf_fs_mobile_force` | - |
| | `VIE_lf_fs_lean_corps` | (186, 9) | `VIE_lf_fs_main_corps` (0, 1) | `VIE_lf_fs_main_corps` | - |
| | `VIE_lf_fs_militia_units` | (188, 9) | `VIE_lf_fs_depth_defence` (0, 1) | `VIE_lf_fs_depth_defence` | - |
| **y = 10** | `VIE_lf_dev_strategic` | (184, 10) | `VIE_lf_fs_mobile_corps` (0, 1) | `VIE_lf_fs_mobile_corps` | - |
| | `VIE_lf_dev_territorial` | (188, 10) | `VIE_lf_fs_militia_units` (0, 1) | `VIE_lf_fs_militia_units` | - |
| **y = 11** | `VIE_lf_command_reform_2` | (186, 11) | `VIE_lf_dev_strategic` (2, 1) | `VIE_lf_dev_strategic` | `VIE_lf_dev_territorial` |
| **y = 12** | `VIE_lf_cap_border_urban` | (184, 12) | `VIE_lf_command_reform_2` (-2, 1) | `VIE_lf_command_reform_2` | - |
| | `VIE_lf_cap_army_ad` | (186, 12) | `VIE_lf_command_reform_2` (0, 1) | `VIE_lf_command_reform_2` | - |
| | `VIE_lf_cap_cyber_ew` | (188, 12) | `VIE_lf_command_reform_2` (2, 1) | `VIE_lf_command_reform_2` | - |
| **y = 13** | `VIE_lf_cap_area_control` | (184, 13) | `VIE_lf_cap_border_urban` (0, 1) | `VIE_lf_cap_border_urban` | - |
| | `VIE_lf_cap_ad_coord` | (186, 13) | `VIE_lf_cap_army_ad` (0, 1) | `VIE_lf_cap_army_ad` | - |
| | `VIE_lf_cap_info_ops` | (188, 13) | `VIE_lf_cap_cyber_ew` (0, 1) | `VIE_lf_cap_cyber_ew` | - |
| **y = 14** | `VIE_lf_selective_modernization`| (186, 14) | `VIE_lf_cap_ad_coord` (0, 1) | `VIE_lf_cap_ad_coord` | - |
| **y = 15** | `VIE_lf_command_reform_3` | (186, 15) | `VIE_lf_selective_modernization` (0, 1)| `VIE_lf_selective_modernization` | - |
| **y = 16** | `VIE_lf_force_complete` | (186, 16) | `VIE_lf_command_reform_3` (0, 1) | `VIE_lf_command_reform_3` | - |

---

### 3.2 TRỤC 2: Hải quân Nhân dân & Đóng tàu Ba Son (28 focus)
* **Vùng tọa độ:** $x = 194 .. 206$ (Tâm $x = 200$)
* **Gốc trục:** `VIE_nf_training_standardization` ($x = 200, y = 2$).

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available (Ngang/Anh em) |
|:---:|---|:---:|---|---|---|
| **y = 2** | `VIE_nf_training_standardization` | (200, 2) | `VIE_modernize_vpa` (0, 1) | `VIE_modernize_vpa` | - |
| **y = 3** | `VIE_nf_surface_force` | (198, 3) | `VIE_nf_training_standardization` (-2, 1) | `VIE_nf_training_standardization` | - |
| | `VIE_nf_submarine_force` | (200, 3) | `VIE_nf_training_standardization` (0, 1) | `VIE_nf_training_standardization` | - |
| | `VIE_naval_defence_law` | (204, 3) | `VIE_nf_training_standardization` (4, 1) | `VIE_nf_training_standardization` | - |
| **y = 4** | `VIE_nf_command_reform_1` | (198, 4) | `VIE_nf_surface_force` (0, 1) | `VIE_nf_surface_force` | `VIE_nf_submarine_force` |
| | `VIE_ba_son_shipyards` | (204, 4) | `VIE_naval_defence_law` (0, 1) | `VIE_naval_defence_law` | - |
| **y = 5** | `VIE_nf_first_force` | (198, 5) | `VIE_nf_command_reform_1` (0, 1) | `VIE_nf_command_reform_1` | `VIE_naval_mro` |
| | `VIE_naval_mro` | (202, 5) | `VIE_ba_son_shipyards` (-2, 1) | `VIE_ba_son_shipyards` | - |
| | `VIE_small_combatant_construction`| (206, 5) | `VIE_ba_son_shipyards` (2, 1) | `VIE_ba_son_shipyards` | - |
| **y = 6** | `VIE_nf_command_reform_2` | (198, 6) | `VIE_nf_first_force` (0, 1) | `VIE_nf_first_force` | - |
| | `VIE_naval_systems_integration` | (204, 6) | `VIE_small_combatant_construction` (-2, 1)| `VIE_small_combatant_construction` | `VIE_naval_mro` |
| **y = 7** | `VIE_nf_medium_force` | (198, 7) | `VIE_nf_command_reform_2` (0, 1) | `VIE_nf_command_reform_2` | - |
| | `VIE_naval_defence_2030` | (204, 7) | `VIE_naval_systems_integration` (0, 1) | `VIE_naval_systems_integration` | `naval_mro`, `small_combatant` |
| **y = 8** | `VIE_nf_operating_range` | (198, 8) | `VIE_nf_medium_force` (0, 1) | `VIE_nf_medium_force` | - |
| **y = 9** | `VIE_nf_denial` | (194, 9) | `VIE_nf_operating_range` (-4, 1) | `VIE_nf_operating_range` | - |
| | `VIE_nf_greenwater` | (198, 9) | `VIE_nf_operating_range` (0, 1) | `VIE_nf_operating_range` | - |
| | `VIE_nf_bluewater` | (202, 9) | `VIE_nf_operating_range` (4, 1) | `VIE_nf_operating_range` | - |
| **y = 10** | `VIE_nf_denial_defence` | (194, 10) | `VIE_nf_denial` (0, 1) | `VIE_nf_denial` | - |
| | `VIE_nf_regional_frigates` | (196, 10) | `VIE_nf_greenwater` (-2, 1) | `VIE_nf_greenwater` | - |
| | `VIE_nf_amphibious_fleet` | (200, 10) | `VIE_nf_greenwater` (2, 1) | `VIE_nf_greenwater` | - |
| | `VIE_nf_ocean_escort` | (202, 10) | `VIE_nf_bluewater` (0, 1) | `VIE_nf_bluewater` | - |
| | `VIE_nf_replenishment` | (204, 10) | `VIE_nf_bluewater` (2, 1) | `VIE_nf_bluewater` | - |
| | `VIE_nf_naval_aviation` | (206, 10) | `VIE_nf_bluewater` (4, 1) | `VIE_nf_bluewater` | - |
| **y = 11** | `VIE_nf_denial_subs` | (194, 11) | `VIE_nf_denial_defence` (0, 1) | `VIE_nf_denial_defence` | - |
| | `VIE_nf_lhd_program` | (198, 11) | `VIE_nf_regional_frigates` (2, 1) | `VIE_nf_regional_frigates` | `VIE_nf_amphibious_fleet` |
| | `VIE_nf_carrier_group` | (204, 11) | `VIE_nf_replenishment` (0, 1) | `VIE_nf_replenishment` | `ocean_escort`, `naval_aviation` |
| **y = 12** | `VIE_nf_denial_command` | (194, 12) | `VIE_nf_denial_subs` (0, 1) | `VIE_nf_denial_subs` | - |
| | `VIE_nf_regional_command` | (198, 12) | `VIE_nf_lhd_program` (0, 1) | `VIE_nf_lhd_program` | - |

---

### 3.3 TRỤC 3: Phòng không - Không quân & APM (29 focus)
* **Vùng tọa độ:** $x = 210 .. 220$ (Tâm $x = 214$)
* **Gốc trục:** `VIE_airf_training_standardization` ($x = 214, y = 2$).

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available (Ngang/Anh em) |
|:---:|---|:---:|---|---|---|
| **y = 2** | `VIE_airf_training_standardization`| (214, 2) | `VIE_modernize_vpa` (14, 1) | `VIE_modernize_vpa` | - |
| **y = 3** | `VIE_airf_fighter_force` | (212, 3) | `VIE_airf_training_standardization` (-2, 1)| `VIE_airf_training_standardization` | - |
| | `VIE_airf_sam_force` | (214, 3) | `VIE_airf_training_standardization` (0, 1) | `VIE_airf_training_standardization` | - |
| | `VIE_apm_law` | (218, 3) | `VIE_airf_training_standardization` (4, 1) | `VIE_airf_training_standardization` | - |
| **y = 4** | `VIE_airf_command_reform_1` | (212, 4) | `VIE_airf_fighter_force` (0, 1) | `VIE_airf_fighter_force` | `VIE_airf_sam_force` |
| | `VIE_apm_a32` | (216, 4) | `VIE_apm_law` (-2, 1) | `VIE_apm_law` | - |
| | `VIE_apm_a31` | (218, 4) | `VIE_apm_law` (0, 1) | `VIE_apm_law` | - |
| | `VIE_apm_radar` | (220, 4) | `VIE_apm_law` (2, 1) | `VIE_apm_law` | - |
| **y = 5** | `VIE_airf_first_force` | (212, 5) | `VIE_airf_command_reform_1` (0, 1) | `VIE_airf_command_reform_1` | - |
| | `VIE_apm_integration` | (216, 5) | `VIE_apm_a32` (0, 1) | `VIE_apm_a32` | - |
| | `VIE_apm_uav` | (220, 5) | `VIE_apm_radar` (0, 1) | `VIE_apm_radar` | - |
| **y = 6** | `VIE_airf_command_reform_2` | (212, 6) | `VIE_airf_first_force` (0, 1) | `VIE_airf_first_force` | - |
| | `VIE_apm_mature` | (218, 6) | `VIE_apm_integration` (2, 1) | `VIE_apm_integration` | `VIE_apm_uav` |
| **y = 7** | `VIE_airf_medium_force` | (214, 7) | `VIE_airf_command_reform_2` (2, 1) | `VIE_airf_command_reform_2` | - |
| **y = 8** | `VIE_airf_operating_range` | (214, 8) | `VIE_airf_medium_force` (0, 1) | `VIE_airf_medium_force` | - |
| **y = 9** | `VIE_airf_iads` | (210, 9) | `VIE_airf_operating_range` (-4, 1) | `VIE_airf_operating_range` | - |
| | `VIE_airf_multirole` | (214, 9) | `VIE_airf_operating_range` (0, 1) | `VIE_airf_operating_range` | - |
| | `VIE_airf_unmanned` | (218, 9) | `VIE_airf_operating_range` (4, 1) | `VIE_airf_operating_range` | - |
| **y = 10** | `VIE_airf_layered_defence` | (210, 10) | `VIE_airf_iads` (0, 1) | `VIE_airf_iads` | - |
| | `VIE_airf_multirole_fleet` | (212, 10) | `VIE_airf_multirole` (-2, 1) | `VIE_airf_multirole` | - |
| | `VIE_airf_sustainment` | (214, 10) | `VIE_airf_multirole` (0, 1) | `VIE_airf_multirole` | - |
| | `VIE_airf_airlift_tanker` | (216, 10) | `VIE_airf_multirole` (2, 1) | `VIE_airf_multirole` | - |
| | `VIE_airf_isr_uav` | (218, 10) | `VIE_airf_unmanned` (0, 1) | `VIE_airf_unmanned` | - |
| | `VIE_airf_datalink` | (220, 10) | `VIE_airf_unmanned` (2, 1) | `VIE_airf_unmanned` | - |
| **y = 11** | `VIE_airf_ew_antistealth` | (210, 11) | `VIE_airf_layered_defence` (0, 1) | `VIE_airf_layered_defence` | - |
| | `VIE_airf_multirole_wing` | (214, 11) | `VIE_airf_multirole_fleet` (2, 1) | `VIE_airf_multirole_fleet` | `sustainment`, `airlift_tanker` |
| | `VIE_airf_strike_uav` | (218, 11) | `VIE_airf_isr_uav` (0, 1) | `VIE_airf_isr_uav` | - |
| **y = 12** | `VIE_airf_iads_command` | (210, 12) | `VIE_airf_ew_antistealth` (0, 1) | `VIE_airf_ew_antistealth` | - |
| | `VIE_airf_teaming` | (218, 12) | `VIE_airf_strike_uav` (0, 1) | `VIE_airf_strike_uav` | `VIE_airf_datalink` |

---

## 4. Bảng So sánh Trước và Sau Rút Gọn

| Chỉ số / Đặc tính | Trước Rút Gọn | Sau Rút Gọn (Compacted) | Hiệu quả Đạt được |
|---|:---:|:---:|---|
| **Dải tọa độ X toàn nhánh** | $174 .. 244$ | **$180 .. 220$** | **Rút gọn 30 cột (giảm 43%)** |
| **Khoảng vươn từ gốc VPA sang Lục quân** | $dx = -26$ | **$dx = -14$** | Giảm gần 50% độ dài đường nối |
| **Khoảng vươn từ gốc VPA sang Không quân** | $dx = +22$ | **$dx = +14$** | Đối xứng hoàn hảo với Lục quân ($|-14| = |+14|$) |
| **Khoảng cách giữa các Quân chủng** | Trống 10–18 ô | **Đồng đều 4 ô** | Cây gắn kết, không bị cảm giác rời rạc |
| **Hàng rỗng dọc ($dy = 2$)** | 4 focus | **0 focus (100% $dy = 1$)** | Xóa sạch các lỗ thủng dọc ở Hải quân và APM |
| **Số focus có bước nhảy $|dx| \ge 6$** | 17 focus | **Chỉ còn 2 focus cánh gốc ($dx = \pm 14$)** | Triệt tiêu toàn bộ 15 cú nhảy ngang dị thường |
| **Nội bộ 3 quân chủng** | Nhiều bước nhảy $6..8$ | **Mọi $|dx| \le 4$ (đa số $0..2$)** | Dòng liên kết thẳng đứng, dễ đọc, mạch lạc |
| **Tầng kết thúc Hải quân** | $y = 13$ | **$y = 12$** | Rút ngắn 1 tầng do nâng $y=5$ |
| **Tầng kết thúc APM** | $y = 8$ | **$y = 6$** | Rút ngắn 2 tầng, khép kín hoàn chỉnh |

---

## 5. Kết quả Kiểm định Kỹ thuật (HOÀN TẤT 100%)

Đã chạy kiểm tra tự động qua các script kiểm định mod:
* **Số lượng focus:** Khớp chính xác 92 / 92 focus quân sự (Tổng cây: 410 focus).
* **Xung đột nội bộ (Collisions):** **0 lỗi**.
* **Xung đột với các nhánh khác:** **0 lỗi**.
* **Vi phạm khoảng cách ($\Delta x < 2$):** **0 lỗi**.
* **Tham chiếu tiến (`relative_position_id` forward reference):** **0 lỗi** (toàn bộ file tuân thủ nghiêm ngặt Cha khai báo trước Con).
* **Vi phạm độ sâu ($y_{child} \le y_{parent}$):** **0 lỗi**.
* **Gameplay & Logic:** Giữ nguyên 100% triggers, completion rewards, AI weights, search filters, icons, và available conditions.
* **Trình kiểm tra tĩnh `check_static.py`:** Đạt chuẩn **90 errors, 1 warning** (khớp baseline).

---

## Nhánh Chính trị & Hệ thống Đại hội Đảng

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

---

## Nhánh Kinh tế

# Nhánh Kinh tế — Kiến trúc & Bố cục Hàng ngang (Chuẩn hóa theo Cột Chính trị)

> **Tài liệu thiết kế kiến trúc và chuẩn format (05/10/2026)**  
> **Áp dụng:** Tái cấu trúc toàn bộ khối Kinh tế trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md) và mô hình Hub-Spine của nhánh Chính trị ([Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md)).

> **Cập nhật 08/10/2026:** Nhánh công nghiệp dùng [thiết kế v17](VIE_industry_branch_redesign.md). Quy tắc hub hai hàng và chuyển mọi phụ thuộc nội bộ sang `available` trong tài liệu này không còn áp dụng cho nhánh công nghiệp. Các phần khác giữ phạm vi hiện tại.

---

## 0. Vấn đề của nhánh Kinh tế cũ & Giải pháp chuẩn hóa

| Vấn đề ở kiến trúc cũ | Giải pháp theo Chuẩn "Hàng ngang" Chính trị |
|---|---|
| **Chuỗi dọc quá sâu (4–8 tầng):** Nhánh đâm thẳng xuống dưới gây dài cây, khó bao quát, người chơi phải cuộn màn hình liên tục. | **Quy tắc Hub 2 hàng:** Mỗi mốc (Hub) quản lý một tầng chính sách. Mọi focus triển khai nằm trên **MỘT hàng ngang ngay dưới mốc (`dy = 1`)**, mốc kế tiếp nằm ở `dy = 2`. |
| **Đường nối chéo chằng chịt (Spaghetti links):** Các focus phụ thuộc lẫn nhau giữa các ngành (ví dụ: bán dẫn cần giáo dục, thép cần phụ trợ, JETP cần thiên tai) kéo dây chéo qua cả màn hình. | **Quy tắc Prerequisite vs Available:** Tuyệt đối chỉ dùng `prerequisite` cho liên kết Cha $\rightarrow$ Con dọc. Mọi phụ thuộc ngang hàng (anh em) hoặc chéo ngành chuyển 100% sang `available = { has_completed_focus = ... }`. |
| **Neo xa / Neo lung tung:** Nhiều focus neo vào một gốc xa (như `doi_moi_continues` x=80) hoặc neo chéo hàng làm lệch lưới tọa độ. | **Neo cha trực tiếp (`relative_position_id = cha`):** Khai báo cha trước, con sau. Con nằm tại $x = 0$ (thẳng dưới) hoặc $\pm 2, \pm 4$ quanh cha. |
| **Ô quá sát nhau hoặc đè ô:** Không đồng nhất khoảng cách $\Delta x$. | **Chuẩn lưới $\Delta x \ge 2$:** Khoảng cách tối thiểu giữa 2 focus cùng hàng là 2 ô, căn giữa đối xứng quanh mốc Hub. |
| **Lẫn lộn tầm vĩ mô với dự án cụ thể:** Quá nhiều focus tiểu dự án (hầm, trạm, liên doanh). | **Gộp & tinh gọn (theo Báo cáo Tinh gọn 03/10/2026):** Giữ lại các luật, nghị quyết, chiến lược quốc gia và ngã rẽ lịch sử; dự án nhỏ chuyển thành mô tả hoặc decision. |

---

## 1. Phân rã 4 Trục chức năng của Khối Kinh tế

Nhánh Kinh tế phân bố bên phải nhánh Chính trị, tỏa ra từ gốc chung `VIE_doi_moi_continues` (hoặc các Hub cấp 1 độc lập) thành **4 Trục chiến lược**:

```text
                               VIE_doi_moi_continues
                                         │
        ┌───────────────────┬────────────┴───────┬───────────────────┐
      TRỤC 1              TRỤC 2               TRỤC 3              TRỤC 4
  DOANH NGHIỆP        TÀI CHÍNH &          NĂNG LƯỢNG &        CÔNG NGHIỆP HÓA
   & THƯƠNG MẠI        NGÂN HÀNG            TÀI NGUYÊN           & CÔNG NGHỆ
   (Luật DN 2000)    (NHNN & DNNN)        (PVN & Vinacomin)     (CNH-HĐH ĐH IX)
```

*(Lưu ý: Khối **Kết cấu Hạ tầng** `VIE_infrastructure_development` đã được chuẩn hóa riêng theo tài liệu [VIE_infrastructure_branch_design.md](VIE_infrastructure_branch_design.md) nên đứng độc lập bên cạnh).*

---

## 2. Chi tiết Kiến trúc & Bố cục từng Trục

### 2.1 TRỤC 1: Doanh nghiệp, Thương mại & Thị trường vốn
* **Gốc (Hub 1):** `VIE_enterprise_law` (Luật Doanh nghiệp 2000 - cột mốc mở cửa kinh tế tư nhân).

#### Cấu trúc Hub & Hàng ngang:
1. **Hàng 1 (Nền tảng mở cửa, dy = 1 dưới `enterprise_law`):**
   * `VIE_equitization_soes` (Cổ phần hóa DNNN đợt 1, $dx = -3$)
   * `VIE_investment_law_2005` (Luật Đầu tư 2005 - Mốc Hub kinh tế tư nhân, $dx = -1$)
   * `VIE_bilateral_trade_agreement_usa` (Hiệp định BTA Việt - Mỹ, $dx = 1$)
   * `VIE_rice_export_power` (Nông nghiệp hàng hóa & xuất khẩu gạo, $dx = 3$)
2. **Hàng 2 (Kinh tế tư nhân & Nông thôn mới, dy = 1 dưới `investment_law_2005` & `rice_export_power`):**
   * Dưới `investment_law_2005`:
     * `VIE_household_business` (Kinh tế hộ cá thể, $dx = -2$)
     * `VIE_private_champions` (Tập đoàn tư nhân lớn, $dx = 0$)
     * `VIE_private_sector_engine` (Động lực kinh tế tư nhân - NQ 10, $dx = 2$, cần `available = private_champions`)
   * Dưới `rice_export_power`:
     * `VIE_new_rural_development` (Nông thôn mới, $dx = -1$)
     * `VIE_land_law_reform` (Sửa đổi Luật Đất đai, $dx = 1$)
3. **Hàng 3 (Hội nhập toàn cầu & FDI, dy = 1 dưới mốc `fdi_attraction`):**
   * **Mốc Hub:** `VIE_fdi_attraction` (Thu hút FDI thế hệ mới)
   * **Hàng con ngang:**
     * `VIE_wto_negotiations` (Gia nhập WTO, $dx = -3$)
     * `VIE_wto_reforms` (Cải cách hậu WTO, $dx = -1$, cần `available = wto_negotiations`)
     * `VIE_cptpp_member` (Hiệp định CPTPP, $dx = 1$)
     * `VIE_evfta` (Hiệp định EVFTA, $dx = 3$)
4. **Hàng 4 (Ngã rẽ Đặc khu kinh tế 2018, dy = 1 dưới `sez_three_zones`):**
   * **Mốc Hub:** `VIE_sez_three_zones` (Đề án 3 Đặc khu: Vân Đồn, Bắc Vân Phong, Phú Quốc)
   * **Ngã rẽ loại trừ nhau:**
     * `VIE_sez_postpone` (Hoãn luật theo nguyện vọng dư luận — *Lịch sử*, $dx = -2$)
     * `VIE_sez_pass_99` (Thông qua ưu đãi thuê đất 99 năm — *Giả định*, $dx = 2$)
   * **Hàng tiếp nối (dy = 1 dưới mỗi lựa chọn):**
     * Dưới `sez_postpone`: `VIE_island_special_zones` (Khu kinh tế ven biển chọn lọc)
     * Dưới `sez_pass_99`: `VIE_sez_strategic_investors` (Thu hút đại bàng tài phiệt)

---

### 2.2 TRỤC 2: Tài chính, Ngân hàng & Sở hữu Nhà nước
* **Gốc (Hub 2):** `VIE_state_bank_modernization` (Hiện đại hóa Ngân hàng Nhà nước).

#### Cấu trúc Hub & Hàng ngang:
1. **Hàng 1 (Điều hành tiền tệ & Thị trường vốn, dy = 1 dưới `state_bank_modernization`):**
   * `VIE_cashless_payments` (Thanh toán không dùng tiền mặt, $dx = -4$)
   * `VIE_hose_exchange` (Sàn chứng khoán HOSE, $dx = -2$)
   * `VIE_corporate_bond_reform` (Thị trường trái phiếu doanh nghiệp, $dx = 0$)
   * `VIE_fight_inflation` (Kiềm chế lạm phát vĩ mô, $dx = 2$)
   * Ngã rẽ Vàng 2012 (loại trừ nhau):
     * `VIE_gold_monopoly_2012` (Nghị định 24 - Độc quyền vàng miếng SJC — *Lịch sử*, $dx = 4$)
     * `VIE_gold_free_market` (Thị trường vàng tự do — *Giả định*, $dx = 6$)
2. **Hàng 2 (Sở hữu Nhà nước & Tái cơ cấu DNNN, dy = 1 dưới `state_conglomerates`):**
   * **Mốc Hub:** `VIE_state_conglomerates` (Tập đoàn kinh tế Nhà nước)
   * **Hàng con:**
     * `VIE_scic` (Thành lập Tổng công ty Đầu tư và Kinh doanh Vốn Nhà nước SCIC, $dx = -2$)
     * Ngã rẽ Cổ phần hóa 2017:
       * `VIE_soe_gradual_restructuring` (Cổ phần hóa thận trọng, giữ vai trò chủ đạo — *Lịch sử*, $dx = 0$)
       * `VIE_soe_rapid_divestment` (Thoái vốn nhanh, tư nhân hóa triệt để — *Giả định*, $dx = 2$)
     * `VIE_soe_governance` (Quản trị DNNN theo chuẩn OECD, $dx = 4$)
3. **Hàng 3 (Tái cơ cấu hệ thống Ngân hàng & Xử lý Nợ xấu, dy = 1 dưới `restructure_banking`):**
   * **Mốc Hub:** `VIE_restructure_banking` (Đề án cơ cấu lại hệ thống các TCTD)
   * **Hàng con ngang:**
     * `VIE_vamc` (Thành lập Công ty VAMC - Mua bán nợ xấu, $dx = -3$)
     * `VIE_cross_ownership_crackdown` (Chống sở hữu chéo ngân hàng, $dx = -1$)
     * Ngã rẽ Ngân hàng 0 đồng 2015:
       * `VIE_zero_dong_acquisition` (Mua lại bắt buộc 0 đồng — *Lịch sử*, $dx = 1$)
       * `VIE_bank_bankruptcy` (Cho phép ngân hàng phá sản theo thị trường — *Giả định*, $dx = 3$)
     * `VIE_compulsory_transfer_2024` (Chuyển giao bắt buộc ngân hàng yếu kém 2024, dy=1 dưới `zero_dong_acquisition`)
4. **Hàng 4 (Đích đến hội tụ Tài chính, dy = 2):**
   * `VIE_international_financial_centre` (Trung tâm Tài chính Quốc tế TP.HCM / Đà Nẵng, $dx = -2$)
   * `VIE_investment_grade` (Đạt mức xếp hạng tín nhiệm đầu tư Baa3/BBB, $dx = 2$)

---

### 2.3 TRỤC 3: Năng lượng & Tài nguyên Khoáng sản
* **Hai Hub cấp 1:** `VIE_vinacomin_founding` (Khoáng sản/Vinacomin) và `VIE_petrovietnam_expansion` (Dầu khí/Điện/PVN).

#### Cấu trúc Hub & Hàng ngang:
1. **Khối Khoáng sản (Dưới `vinacomin_founding`):**
   * Ngã rẽ Bauxite Tây Nguyên 2009:
     * `VIE_bauxite_tay_nguyen` (Tiếp tục khai thác bauxite — *Lịch sử*, $dx = -2$)
     * `VIE_bauxite_suspend` (Dừng dự án vì môi trường & an ninh — *Giả định*, $dx = 2$)
   * Hàng tài nguyên chiến lược (dy = 1):
     * `VIE_rare_earths` (Khai thác đất hiếm, $dx = -3$)
     * `VIE_than_quang_ninh` (Than Quảng Ninh - An ninh năng lượng, $dx = -1$)
     * `VIE_nui_phao_tungsten` (Vonfram Núi Pháo, $dx = 1$)
     * `VIE_thach_khe_mine_start` (Quặng sắt Thạch Khê, $dx = 3$)
2. **Khối Dầu khí & Lọc hóa dầu (Dưới `petrovietnam_expansion`):**
   * Hàng hạ nguồn & chế biến (dy = 1):
     * `VIE_dung_quat_refinery` (Nhà máy Lọc dầu Dung Quất, $dx = -3$)
     * `VIE_nghi_son_refinery` (Lọc hóa dầu Nghi Sơn, $dx = -1$)
     * `VIE_petrolimex_downstream_network` (Mạng lưới phân phối xăng dầu Petrolimex, $dx = 1$)
     * `VIE_strategic_petroleum_reserve` (Dự trữ xăng dầu quốc gia, $dx = 3$)
3. **Khối Lưới điện & Năng lượng tái tạo (Dưới `son_la_dam` & `power_plan_8`):**
   * `VIE_son_la_dam` (Thủy điện Sơn La) $\rightarrow$ Hàng 1 (dy = 1): `VIE_500kv_grid` (Mạch 500kV), `VIE_coal_power` (Nhiệt điện than).
   * **Mốc Hub:** `VIE_power_plan_8` (Quy hoạch Điện VIII) $\rightarrow$ Hàng 2 (dy = 1):
     * Ngã rẽ Điện mặt trời: `VIE_solar_boom` (Giá FIT ưu đãi) ⟷ `VIE_solar_auction` (Đấu thầu giá điện)
     * Ngã rẽ Điện hạt nhân Ninh Thuận: `VIE_shelve_nuclear` (Tạm dừng 2016 — *Lịch sử*) ⟷ `VIE_build_nuclear_plant` (Quyết tâm xây dựng)
     * `VIE_revive_nuclear` (Khởi động lại điện hạt nhân 2024, dy = 1 dưới `shelve_nuclear`)
     * `VIE_offshore_wind` (Điện gió ngoài khơi)
     * `VIE_dppa_market_reform` (Cơ chế mua bán điện trực tiếp DPPA)
   * **Hội tụ Capstone Năng lượng (dy = 2):**
     * `VIE_jetp_partnership` (Quan hệ đối tác chuyển dịch năng lượng bình đẳng JETP)
     * `VIE_net_zero_2050` (Cam kết phát thải ròng bằng 0 - COP26)

---

### 2.4 TRỤC 4: Công nghiệp hóa và công nghệ — v17

Thiết kế hiện hành: [VIE_industry_branch_redesign.md](VIE_industry_branch_redesign.md).
Nhánh có 39 focus (35 ID cũ và 4 chính sách mới), x=124..140, y=1..9.

- Formosa, Hòa Phát, Samsung, Intel và công nghiệp hỗ trợ có lối vào độc lập.
- Đóng tàu, dệt may, thép, ô tô và điện tử phát triển song song.
- Trung tâm chế tạo cần phụ trợ AND (Samsung OR China+1).
- China+1 có cặp lựa chọn FDI; Apple cần một lựa chọn và trung tâm chế tạo.
- Bán dẫn có cặp lựa chọn hỗ trợ; thiết kế, đóng gói, đào tạo cùng mở sau một lựa chọn.
  Fab thử nghiệm yêu cầu đủ cả ba, hai đường có tổng hỗ trợ bằng nhau.
- NQ23 dẫn đến NQ29; quỹ đầu tư và năng suất song song, không buộc khu công nghiệp
  sinh thái hoặc quỹ hỗ trợ thành điều kiện của toàn bộ chính sách.
- Đích cuối cần năng suất, ≥45 điểm nội địa hóa và ≥3/6 nhóm; không khóa năm với
  người chơi, không bắt buộc bán dẫn hoặc xe điện.

Quan hệ nội bộ hiện trên cây bằng prerequisite AND/OR. `available` dành cho điều
kiện ngoài nhánh, ngày của dự án có tên, cờ xử lý sự kiện và ngưỡng năng lực.

---

## 3. Bảng Ánh xạ Chuyển đổi: Prerequisite $\rightarrow$ Available (Cắt đường nối rối)

Bảng lịch sử dưới đây áp dụng cho các nhánh chưa tái thiết kế. Công nghiệp v17 dùng prerequisite cho phụ thuộc nội bộ; chỉ giữ điều kiện ngoài nhánh trong `available`:

| Focus | Cha trực tiếp (`prerequisite`) | Điều kiện logic chuyển sang `available = {}` |
|---|---|---|
| `VIE_fdi_attraction` | `VIE_bilateral_trade_agreement_usa` | `available = { has_completed_focus = VIE_equitization_soes }` (thay vì 2 prerequisite kéo chéo) |
| `VIE_wto_reforms` | `VIE_fdi_attraction` | `available = { has_completed_focus = VIE_wto_negotiations }` |
| `VIE_chip_engineers` | OR hai focus ưu tiên bán dẫn (v17) | `available = { has_completed_focus = VIE_higher_education_law }` (cắt dây chéo sang nhánh Giáo dục) |
| `VIE_net_zero_2050` | `VIE_power_plan_8` | `available = { has_completed_focus = VIE_jetp_partnership }` |
| `VIE_cptpp_member` | `VIE_fdi_attraction` | `available = { date > 2018.1.1 }` |
| `VIE_evfta` | `VIE_fdi_attraction` | `available = { date > 2020.6.30 }` |
| `VIE_tier1_vendor_localization` (v17) | `VIE_supporting_industries` | Không cần Samsung; không còn khóa năm |
| `VIE_semiconductor_ambition` (v17) | `VIE_intel_hcmc` | Không còn khóa năm của người chơi |
| `VIE_revive_nuclear` | `VIE_shelve_nuclear` | `available = { date > 2024.1.1 has_completed_focus = VIE_power_plan_8 }` |

---

## 4. Danh sách Các Cặp Ngã rẽ Lịch sử (Loại trừ nhau)

Tất cả các ngã rẽ đều sử dụng `mutually_exclusive = { focus = ... }` và đặt trên cùng một hàng ($dy = 1$ dưới Hub chung):

1. **Bauxite Tây Nguyên 2009:** `VIE_bauxite_tay_nguyen` $\longleftrightarrow$ `VIE_bauxite_suspend` (Cha: `VIE_vinacomin_founding`).
2. **Thị trường Vàng 2012:** `VIE_gold_monopoly_2012` $\longleftrightarrow$ `VIE_gold_free_market` (Cha: `VIE_state_bank_modernization`).
3. **Ngân hàng 0 đồng 2015:** `VIE_zero_dong_acquisition` $\longleftrightarrow$ `VIE_bank_bankruptcy` (Cha: `VIE_restructure_banking`).
4. **Tái cơ cấu DNNN 2017:** `VIE_soe_gradual_restructuring` $\longleftrightarrow$ `VIE_soe_rapid_divestment` (Cha: `VIE_state_conglomerates`).
5. **Giá điện mặt trời 2017:** `VIE_solar_boom` $\longleftrightarrow$ `VIE_solar_auction` (Cha: `VIE_power_plan_8`).
6. **Đặc khu kinh tế 2018:** `VIE_sez_postpone` $\longleftrightarrow$ `VIE_sez_pass_99` (Cha: `VIE_sez_three_zones`).
7. **Điện hạt nhân Ninh Thuận:** `VIE_shelve_nuclear` $\longleftrightarrow$ `VIE_build_nuclear_plant` (Cha: `VIE_ninh_thuan_nuclear`).
8. **Chiến lược FDI v17:** `VIE_fdi_fast_track` $\longleftrightarrow$ `VIE_fdi_technology_screening` (Cha: `VIE_china_plus_one`).
9. **Hỗ trợ bán dẫn v17:** `VIE_chip_design_packaging_priority` $\longleftrightarrow$ `VIE_chip_pilot_fab_priority` (Cha: `VIE_semiconductor_ambition`).

---

## 5. Quy chuẩn Format Code một Focus Block mẫu

Mỗi focus trong nhánh Kinh tế khi áp dụng vào code phải tuân thủ nghiêm ngặt định dạng chuẩn MD4:

```pdx
focus = {
	id = VIE_equitization_soes
	icon = economic_privatisation

	x = -3
	y = 1
	relative_position_id = VIE_enterprise_law

	cost = 7

	prerequisite = { focus = VIE_enterprise_law }

	search_filters = { FOCUS_FILTER_ECONOMY }

	available = {
		date > 2001.1.1
	}

	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: Focus VIE_equitization_soes"
		increase_economic_growth = yes
		add_political_power = 50
		VIE_bop_reform_small = yes
	}

	ai_will_do = { base = 80 }
}
```

---

## 6. Trạng thái Triển khai Code vào `VIE_md_focus.txt` (HOÀN TẤT 100%)

Toàn bộ 4 Trục Kinh tế (110 focus) đã được chuyển đổi hoàn toàn sang chuẩn Bố cục Hàng ngang:

* [x] **Trục 1:** Doanh nghiệp, Thương mại & Thị trường vốn (`VIE_enterprise_law`): 23 focus (x = 27..39, y = 1..8).
* [x] **Trục 2:** Tài chính, Ngân hàng & Sở hữu Nhà nước (`VIE_state_bank_modernization`): 23 focus (x = 45..65, y = 1..6).
* [x] **Trục 3:** Năng lượng & Tài nguyên Khoáng sản (`VIE_vinacomin_founding` & `VIE_petrovietnam_expansion`): 29 focus (x = 102..122, y = 1..7).
* [x] **Trục 4:** Công nghiệp hóa – Hiện đại hóa & Công nghệ cao (`VIE_industrialization_strategy`): 35 focus (x = 124..140, y = 1..7).

### Kết quả kiểm định kỹ thuật (04/10/2026):
* **Forward references (`relative_position_id`):** 0 lỗi (toàn bộ file tuân thủ nghiêm ngặt Cha khai báo trước Con).
* **Đè ô / Xung đột tọa độ (Collisions):** 0 lỗi (toàn bộ 410 focus của cây mod có tọa độ tuyệt đối phân biệt duy nhất).
* **Khoảng cách hàng ngang:** $\Delta x \ge 2$ tại mọi hàng, 0 vi phạm khoảng cách.
* **Đường nối chéo (Spaghetti):** 0 đường chéo (chuyển toàn bộ phụ thuộc chéo/ngang sang `available = { has_completed_focus = ... }`).
* **Trình kiểm tra tĩnh `check_static.py`:** Baseline giữ vững 90 errors, 4 warnings (đã giải quyết triệt để cảnh báo `WARN VIE_intel_hcmc`).

---

## Nhánh Kết cấu Hạ tầng & Giao thông

# Nhánh Kết cấu Hạ tầng & Giao thông — Kiến trúc & Bố cục Hàng ngang Tối ưu (Chuẩn hóa MD4)

> **Tài liệu thiết kế kiến trúc và chuẩn format (04/10/2026 - Bản Rút Gọn Spacing)**  
> **Áp dụng:** Tái cấu trúc, rút gần khoảng cách x-y và chuẩn hóa toàn bộ 44 focus Hạ tầng & Giao thông trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md), quy hoạch thống nhất cùng nhánh Quân sự, Chính trị và Kinh tế.

---

## 1. Hiện trạng & Lý do Tối ưu Rút gần (Compaction)

### 1.1 Vấn đề ở bản bố cục ban đầu
1. **Bước nhảy dọc quá lớn ($dy = 5$):** `VIE_airport_master_plan` đặt tại hàng $y = 6$ nhưng neo trực tiếp về `VIE_infrastructure_development` (hàng $y = 1$) với $dy = 5$, tạo ra đường liên kết vắt dọc qua 5 tầng trống.
2. **Khoảng cách ngang quá rộng ($dx = -16, -12$):** Hàng $y = 2$ tỏa từ gốc $(82, 1)$ sang Cảng biển với $dx = -16$ (`cai_mep_port`) và $dx = -12$ (`lach_huyen_port`).
3. **Bước nhảy ngang ở nhánh Metro và Sân bay:** `urban_rail_hanoi` nhảy $dx = 10$, `tan_son_nhat_t3` nhảy $dx = 8$.
4. **Hàng rỗng ở chốt hạ:** `VIE_synchronized_infrastructure_2030` đặt ở $y = 10$ với $dy = 2$ từ $y = 8$, để trống hàng $y = 9$.

### 1.2 Giải pháp Tối ưu Rút gần
* **Rút gọn toàn bộ nhánh về $y = 1 .. 9$:** Toàn bộ 44 focus kết thúc ở $y = 9$ thay vì $y = 10$.
* **Triệt tiêu $dy = 5$ tại `airport_master_plan`:** Neo về `VIE_hsr_groundbreaking` tại hàng $y = 5$ với $dx = 0, dy = 1$.
* **Triệt tiêu $dy = 2$ tại `synchronized_infrastructure_2030`:** Đưa lên hàng $y = 9$ ngay dưới `expressway_5000km_2030` (hàng $y = 8$) với $dy = 1$.
* **Thu hẹp độ rộng toàn nhánh:** Giảm từ span 32 ($x = 66..98$) xuống **span 22 ($x = 68..90$)**.
* **Đưa các bước nhảy ngang về $\le 4$:** Đa số các liên kết là $dx \in \{-2, 0, 2\}$.

---

## 2. Sơ đồ Kiến trúc Tổng quan Sau Rút Gọn

```text
                                VIE_doi_moi_continues
                                          │ (dx=0, dy=1)
                           VIE_infrastructure_development
                            (Phát triển Hạ tầng, x=80, y=1)
                                          │
       ┌──────────────────┬───────────────┴───────────────┬──────────────────┐
    TRỤC 1             TRỤC 2                          TRỤC 3             TRỤC 4
 CẢNG BIỂN &        ĐƯỜNG BỘ CAO TỐC &             ĐƯỜNG SẮT CAO TỐC   ĐƯỜNG SẮT ĐÔ THỊ
  LOGISTICS             CẦU HẦM                       & MẠNG LƯỚI ĐS       (METRO)
  (3 focus)            (14 focus)                       (10 focus)         (4 focus)
  x = 68..70           x = 70..76                       x = 78..82        x = 86..90
                                          │
                                       TRỤC 5
                                  CẢNG HÀNG KHÔNG &
                                 HÀNG KHÔNG DÂN DỤNG
                                      (11 focus)
                                      x = 78..84
                                          │
                                        CHỐT HẠ
                          HẠ TẦNG ĐỒNG BỘ 2030 (x=74, y=9)
```

---

## 3. Bảng Tọa độ Chi tiết 44 Focus

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available (Ngang/Anh em/Thời gian) |
|:---:|---|:---:|---|---|---|
| **y = 1** | `VIE_infrastructure_development` | (80, 1) | `VIE_doi_moi_continues` (0, 1) | `VIE_doi_moi_continues` | - |
| **y = 2** | `VIE_cai_mep_port` | (68, 2) | `VIE_infrastructure_development` (-12, 1) | `VIE_infrastructure_development` | `date > 2010.12.31` |
| | `VIE_lach_huyen_port` | (70, 2) | `VIE_infrastructure_development` (-10, 1) | `VIE_infrastructure_development` | `date > 2014.12.31` |
| | `VIE_transport_strategy_2004` | (72, 2) | `VIE_infrastructure_development` (-8, 1) | `VIE_infrastructure_development` | `date > 2004.12.9` |
| | `VIE_infrastructure_breakthrough_nq13` | (76, 2) | `VIE_infrastructure_development` (-4, 1) | `VIE_infrastructure_development` | `date > 2011.12.31` |
| | `VIE_hsr_2010_reject` | (78, 2) | `VIE_infrastructure_development` (-2, 1) | `VIE_infrastructure_development` | `date > 2010.4.30` |
| | `VIE_hsr_2010_approve` | (82, 2) | `VIE_infrastructure_development` (2, 1) | `VIE_infrastructure_development` | `date > 2010.4.30` |
| | `VIE_reunification_line_upgrade` | (86, 2) | `VIE_infrastructure_development` (6, 1) | `VIE_infrastructure_development` | `date > 2009.12.31` |
| **y = 3** | `VIE_logistics_strategy` | (70, 3) | `VIE_lach_huyen_port` (0, 1) | `VIE_lach_huyen_port` | `VIE_cai_mep_port`, `date > 2017.7.31` |
| | `VIE_hai_van_tunnel` | (72, 3) | `VIE_transport_strategy_2004` (0, 1) | `VIE_transport_strategy_2004` | `date > 2005.5.31` |
| | `VIE_hcmc_trung_luong_expressway` | (74, 3) | `VIE_transport_strategy_2004` (2, 1) | `VIE_transport_strategy_2004` | `date > 2010.2.2` |
| | `VIE_can_tho_bridge` | (76, 3) | `VIE_transport_strategy_2004` (4, 1) | `VIE_transport_strategy_2004` | `date > 2010.4.23` |
| | `VIE_north_south_hsr` | (80, 3) | `VIE_hsr_2010_reject` (2, 1) | `VIE_hsr_2010_reject` OR `VIE_hsr_2010_approve` | `date > 2024.11.30` |
| | `VIE_lao_cai_haiphong_rail` | (86, 3) | `VIE_reunification_line_upgrade` (0, 1) | `VIE_reunification_line_upgrade` | `date > 2025.11.30` |
| | `VIE_hcmc_metro` | (88, 3) | `VIE_reunification_line_upgrade` (2, 1) | `VIE_reunification_line_upgrade` | `date > 2012.12.31` |
| | `VIE_urban_rail_hanoi` | (90, 3) | `VIE_reunification_line_upgrade` (4, 1) | `VIE_reunification_line_upgrade` | `date > 2021.10.31` |
| **y = 4** | `VIE_northern_expressways` | (72, 4) | `VIE_hcmc_trung_luong_expressway` (-2, 1) | `VIE_hcmc_trung_luong_expressway` | `date > 2015.12.4` |
| | `VIE_north_south_expressway` | (74, 4) | `VIE_hcmc_trung_luong_expressway` (0, 1) | `VIE_hcmc_trung_luong_expressway` | `date > 2017.11.21` |
| | `VIE_hsr_partner_japan` | (78, 4) | `VIE_north_south_hsr` (-2, 1) | `VIE_north_south_hsr` | - |
| | `VIE_hsr_partner_eu` | (80, 4) | `VIE_north_south_hsr` (0, 1) | `VIE_north_south_hsr` | - |
| | `VIE_hsr_partner_china` | (82, 4) | `VIE_north_south_hsr` (2, 1) | `VIE_north_south_hsr` | - |
| | `VIE_domestic_rail_industry` | (86, 4) | `VIE_lao_cai_haiphong_rail` (0, 1) | `VIE_lao_cai_haiphong_rail` | `date > 2025.11.30` |
| | `VIE_urban_rail_special_mechanism_nq188` | (90, 4) | `VIE_urban_rail_hanoi` (0, 1) | `VIE_urban_rail_hanoi` | `VIE_hcmc_metro`, `date > 2025.2.28` |
| **y = 5** | `VIE_expressway_regional_links` | (70, 5) | `VIE_northern_expressways` (-2, 1) | `VIE_northern_expressways` | `date > 2018.12.31` |
| | `VIE_expressway_bot` | (72, 5) | `VIE_north_south_expressway` (-2, 1) | `VIE_north_south_expressway` | `date > 2019.12.31` |
| | `VIE_expressway_public_investment` | (74, 5) | `VIE_north_south_expressway` (0, 1) | `VIE_north_south_expressway` | `date > 2019.12.31` |
| | `VIE_hsr_groundbreaking` | (80, 5) | `VIE_hsr_partner_eu` (0, 1) | `VIE_hsr_partner_japan` OR `EU` OR `China` | `date > 2026.11.30` |
| | `VIE_metro_network_2035` | (90, 5) | `VIE_urban_rail_special_mechanism_nq188` (0, 1) | `VIE_urban_rail_special_mechanism_nq188` | `date > 2028.12.31` |
| **y = 6** | `VIE_north_south_expressway_phase2` | (72, 6) | `VIE_expressway_bot` (0, 1) | `VIE_expressway_bot` | `VIE_expressway_public_investment`, `date > 2022.1.10` |
| | `VIE_airport_master_plan` | (80, 6) | `VIE_hsr_groundbreaking` (0, 1) | - | `VIE_infrastructure_development`, `date > 2008.12.31` |
| **y = 7** | `VIE_ring_roads_hanoi_hcmc` | (70, 7) | `VIE_north_south_expressway_phase2` (-2, 1) | `VIE_north_south_expressway_phase2` | `date > 2022.6.15` |
| | `VIE_expressway_3000km` | (74, 7) | `VIE_north_south_expressway_phase2` (2, 1) | `VIE_north_south_expressway_phase2` | `VIE_expressway_regional_links`, `date > 2025.11.30` |
| | `VIE_aviation_market_opening` | (78, 7) | `VIE_airport_master_plan` (-2, 1) | `VIE_airport_master_plan` | `date > 2011.12.24` |
| | `VIE_noi_bai_t2` | (80, 7) | `VIE_airport_master_plan` (0, 1) | `VIE_airport_master_plan` | `date > 2014.12.31` |
| | `VIE_long_thanh_approval` | (82, 7) | `VIE_airport_master_plan` (2, 1) | `VIE_airport_master_plan` | `date > 2015.6.30` |
| | `VIE_tan_son_nhat_t3` | (84, 7) | `VIE_airport_master_plan` (4, 1) | `VIE_airport_master_plan` | `date > 2025.4.18` |
| **y = 8** | `VIE_expressway_5000km_2030` | (74, 8) | `VIE_expressway_3000km` (0, 1) | `VIE_expressway_3000km` | `date > 2026.6.30` |
| | `VIE_socialized_airports` | (78, 8) | `VIE_aviation_market_opening` (0, 1) | `VIE_aviation_market_opening` | `date > 2017.12.31` |
| | `VIE_acv_monopoly` | (80, 8) | `VIE_aviation_market_opening` (2, 1) | `VIE_aviation_market_opening` | `date > 2017.12.31` |
| | `VIE_long_thanh_airport` | (82, 8) | `VIE_long_thanh_approval` (0, 1) | `VIE_long_thanh_approval` | `date > 2025.12.18` |
| | `VIE_dual_use_airports` | (84, 8) | `VIE_tan_son_nhat_t3` (0, 1) | `VIE_airport_master_plan` | `VIE_tan_son_nhat_t3` |
| **y = 9** | `VIE_synchronized_infrastructure_2030` | (74, 9) | `VIE_expressway_5000km_2030` (0, 1) | `VIE_expressway_5000km_2030` | `VIE_long_thanh_airport`, `date > 2029.12.31` |
| | `VIE_van_don_airport` | (78, 9) | `VIE_socialized_airports` (0, 1) | `VIE_socialized_airports` | `date > 2018.12.31` |
| | `VIE_airport_network_2030` | (80, 9) | `VIE_acv_monopoly` (0, 1) | `VIE_acv_monopoly` | `VIE_socialized_airports`, `date > 2023.5.31` |

---

## 4. Kết quả Kiểm định Kỹ thuật (HOÀN TẤT 100%)

Đã chạy kiểm tra tự động qua các script kiểm định mod:
* **Số lượng focus:** Khớp chính xác 44 / 44 focus Hạ tầng (Tổng cây: 410 focus).
* **Xung đột nội bộ (Collisions):** **0 lỗi**.
* **Xung đột ngoại vi:** **0 lỗi**.
* **Vi phạm khoảng cách ($\Delta x < 2$):** **0 lỗi**.
* **Tham chiếu tiến (`relative_position_id` forward reference):** **0 lỗi**.
* **Vi phạm độ sâu ($y_{child} \le y_{parent}$):** **0 lỗi**.
* **Trình kiểm tra tĩnh `check_static.py`:** Đạt chuẩn **90 errors, 1 warning** (khớp baseline).

---

## Nhánh Khoa học số, Công nghệ & Xã hội 2045

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

---

## Nhánh Ngoại giao & ASEAN

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

---

## Nhánh Biển Đông & Luật Biển

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

---

## Nhánh An ninh Nội địa & Không gian mạng

# Nhánh An ninh Nội địa & Kiểm soát Không gian mạng — Kiến trúc & Bố cục Hàng ngang (Chuẩn hóa MD4)

> **CẬP NHẬT QUAN TRỌNG (05/10/2026):**  
> Nhánh An ninh Nội địa (`VIE_sec_*`) đã được **SÁP NHẬP TOÀN DIỆN** vào cây focus **Con đường Kiên định** (CPV Hardline, `ruling_party = 4`).  
> - **Lý do:** Khắc phục xung đột ID đảng (`ruling_party = 7` Autocracy vs `4` Communist-State), giải quyết triệt để sự trùng lặp về mục tiêu chính trị, và tích hợp cơ chế Áp lực cải cách (`VIE_rp`).  
> - **Khối độc lập tại x=93:** Đã được dỡ bỏ khỏi file `VIE_md_focus.txt`.  
> - **Quy hoạch 30 focus hợp nhất:**  
>   + Giữ lại **5 focus An ninh chuyên biệt** ghép nối trực tiếp vào các trụ của Hardline: `VIE_sec_public_order` (18, 14), `VIE_sec_border_control` (18, 15), `VIE_sec_surveillance_network` (4, 15), `VIE_sec_cyber_sovereignty` (4, 16), `VIE_sec_state_data_center` (12, 16).  
>   + Gộp **6 focus An ninh trùng lặp** vào các focus song sinh của Hardline (`VIE_sec_security_state` $\rightarrow$ `VIE_hl_unity_of_will`; `VIE_sec_cyber_control` $\rightarrow$ `VIE_hl_cyber_ideology`; `VIE_sec_loyalty_vetting` $\rightarrow$ `VIE_hl_party_rectification`; `VIE_sec_security_economy` $\rightarrow$ `VIE_hl_selective_fdi`; `VIE_sec_ideological_education` $\rightarrow$ `VIE_hl_school_theory`; `VIE_sec_managed_opening` $\rightarrow$ `VIE_hl_steadfast_renewal`).  
> - Chi tiết kiến trúc mới xem tại [Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md).

---

> **Tài liệu lịch sử thiết kế kiến trúc (04/10/2026 - Lưu trữ tham khảo):**  
> **Áp dụng:** Từng chuẩn hóa 8 focus An ninh Nội địa (`VIE_sec_*`) tại tọa độ x=93 trước khi sáp nhập vào Hardline.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md).

---

## 1. Hiện trạng & Mục tiêu Chuẩn hóa

### 1.1 Vấn đề trước khi chuẩn hóa
1. **Phân mảnh trong file:** 8 focus an ninh bị xé làm 2 cụm: 3 focus đầu (`VIE_sec_cyber_control`, `VIE_sec_surveillance_network`, `VIE_sec_security_economy`) đặt trước Khoa học số, còn 5 focus sau (`VIE_sec_public_order`, `VIE_sec_cyber_sovereignty`, `VIE_sec_loyalty_vetting`, `VIE_sec_border_control`, `VIE_sec_managed_opening`) đặt sau Khoa học số.
2. **Khoảng cách và kết nối:** Cần đồng bộ hóa để đảm bảo toàn bộ các bước nhảy $dy = 1$, $\Delta x \ge 2$, và không có bất kỳ khoảng trống hay dây chéo nào.

### 1.2 Giải pháp Chuẩn hóa
* **Hợp nhất một khối duy nhất:** Toàn bộ 8 focus được gom thành 1 khối duy nhất đặt ngay trước khối Khoa học số 2045.
* **Bố cục Kim tự tháp ngược đối xứng hoàn hảo:**
  - Hàng $y = 13$: Gốc `VIE_sec_cyber_control` tại tọa độ $(93, 13)$.
  - Hàng $y = 14$: 3 trụ cột an ninh: Giám sát $(91)$, Trật tự xã hội $(93)$, Kinh tế an ninh $(95)$.
  - Hàng $y = 15$: 3 mũi nhọn chuyên sâu: Chủ quyền số $(91)$, Thẩm tra lòng trung thành $(93)$, Kiểm soát biên giới $(95)$.
  - Hàng $y = 16$: Mốc chốt mở cửa có quản lý: `VIE_sec_managed_opening` tại trung tâm $(93)$.
* **Toàn bộ $dy = 1$:** 100% các bước chuyển đều liền kề 1 hàng, không có khoảng cách trống.

---

## 2. Bản đồ Cấu trúc & Tọa độ

```text
                           VIE_sec_cyber_control
                         (Kiểm soát Không gian mạng)
                                (x=93, y=13)
                                      │
              ┌───────────────────────┼───────────────────────┐
   VIE_sec_surveillance_network  VIE_sec_public_order   VIE_sec_security_economy
       (Mạng lưới Giám sát)       (Trật tự Công cộng)       (Kinh tế An ninh)
           (x=91, y=14)              (x=93, y=14)              (x=95, y=14)
              │                           │                         │
   VIE_sec_cyber_sovereignty     VIE_sec_loyalty_vetting    VIE_sec_border_control
        (Chủ quyền Số)           (Thẩm tra Lòng trung thành)   (Kiểm soát Biên giới)
           (x=91, y=15)              (x=93, y=15)              (x=95, y=15)
              └───────────────────────────┬─────────────────────────┘
                                   VIE_sec_managed_opening
                                    (Mở cửa có Quản lý)
                                       (x=93, y=16)
```

---

## 3. Bảng Tọa độ & Tham chiếu Chi tiết

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available |
|:---:|---|:---:|---|---|---|
| **y = 13** | `VIE_sec_cyber_control` | (93, 13) | `VIE_doi_moi_continues` (13, 13) | - | `VIE_cybersecurity_law`, ruling_party = 7 / flag |
| **y = 14** | `VIE_sec_surveillance_network` | (91, 14) | `VIE_sec_cyber_control` (-2, 1) | `VIE_sec_cyber_control` | - |
| | `VIE_sec_public_order` | (93, 14) | `VIE_sec_cyber_control` (0, 1) | `VIE_sec_cyber_control` | - |
| | `VIE_sec_security_economy` | (95, 14) | `VIE_sec_cyber_control` (2, 1) | `VIE_sec_cyber_control` | - |
| **y = 15** | `VIE_sec_cyber_sovereignty` | (91, 15) | `VIE_sec_surveillance_network` (0, 1) | `VIE_sec_surveillance_network` | - |
| | `VIE_sec_loyalty_vetting` | (93, 15) | `VIE_sec_public_order` (0, 1) | `VIE_sec_public_order` | - |
| | `VIE_sec_border_control` | (95, 15) | `VIE_sec_security_economy` (0, 1) | `VIE_sec_security_economy` | - |
| **y = 16** | `VIE_sec_managed_opening` | (93, 16) | `VIE_sec_loyalty_vetting` (0, 1) | `VIE_sec_loyalty_vetting`, `VIE_sec_cyber_sovereignty` | - |

---

## 4. Kết quả Kiểm định Kỹ thuật (HOÀN TẤT 100%)

* **Số lượng focus:** Khớp chính xác 8 / 8 focus An ninh (Tổng cây: 410 focus).
* **Xung đột nội bộ (Collisions):** **0 lỗi**.
* **Tham chiếu tiến (`relative_position_id` forward reference):** **0 lỗi**.
* **Độ lệch dọc ($dy$):** 100% các liên kết đạt chuẩn $dy = 1$.
* **Khoảng cách ngang ($\Delta x$):** Đạt chuẩn $\Delta x = 2$ giữa các cột kề nhau.
* **Trình kiểm tra tĩnh `check_static.py`:** Giữ vững baseline **90 errors, 1 warning**.