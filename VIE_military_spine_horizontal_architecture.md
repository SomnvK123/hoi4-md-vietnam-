# Nhánh Quân sự — Kiến trúc & Bố cục Hàng ngang Tối ưu (Chuẩn hóa MD4)

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
