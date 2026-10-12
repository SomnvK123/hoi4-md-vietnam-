# BÁO CÁO TÁI CẤU TRÚC VÀ MỞ RỘNG NHÁNH CÔNG NGHIỆP QUỐC PHÒNG LỤC QUÂN VIỆT NAM
## Vietnam Ground Forces Industrial Branch Expansion & Technical Master Plan (Millennium Dawn)

- **Dự án:** Vietnam Focus Tree — Millennium Dawn (Hearts of Iron IV 1.19.*)
- **Phạm vi:** Nhánh Công nghiệp Quốc phòng Lục quân (`VIE_lf_ind_*`)
- **Quy mô hoàn thiện:** 9 National Focus (I1 → I9)
- **Trạng thái:** **Đã hoàn thành triển khai toàn bộ vào mã nguồn mod** (Focus, Scripted Effects, Ideas, Decisions, Localisation)

---

## I. MỤC TIÊU VÀ NGUYÊN TẮC TÁI CẤU TRÚC

### 1. Bối cảnh & Hạn chế của Nhánh cũ (5 Focus)
Nhánh Công nghiệp Quốc phòng Lục quân nguyên bản có 5 focus:
1. `VIE_lf_ind_production_governance` (I1)
2. `VIE_lf_ind_precision_z131` (I2)
3. `VIE_lf_ind_armor_structures` (I3)
4. `VIE_lf_ind_xcb01_design` (I4)
5. `VIE_lf_ind_serial_ground_equipment` (I5 cũ)

**Tồn tại:**
- Chỉ có duy nhất một dự án xe chiến đấu cụ thể là IFV XCB-01.
- Thiếu vắng hoàn toàn các chương trình phát triển khí tài mặt đất quan trọng của Việt Nam: xe bọc thép chở quân nội địa (dòng XTC), xe tăng bơi lội nước thế hệ mới (dự án T-1 thay thế PT-76/K-63), pháo tự hành nội địa (PTH Series) và dự án đỉnh cao xe tăng chiến đấu chủ lực thế hệ mới (T-2 MBT).
- Focus sản xuất loạt kết thúc quá sớm (2024), thiếu tầm nhìn dài hạn đến 2030–2035.

---

### 2. Triết lý Thiết kế: "Chương trình qua Focus — Quản lý qua Decision"
Kế thừa mô hình hiện đại hóa của Millennium Dawn (nhánh PLAN Trung Quốc, Nga, Hàn Quốc):
- **National Focus** đóng vai trò là **người khởi xướng chính sách / phê duyệt chương trình cấp nhà nước**: Cung cấp ý niệm quốc gia (Idea), điểm kinh nghiệm, thưởng nghiên cứu công nghệ (Tech bonus) và mở khóa chuỗi quyết định.
- **Hệ thống Decisions** đóng vai trò là **cơ quan điều hành dự án công nghiệp**: Người chơi không nhận khí tài ngay lập tức mà phải đầu tư điểm chính trị (Political Power), thời gian và ngân sách qua từng giai đoạn:
  1. *Thiết kế kỹ thuật* (Design Program)
  2. *Thử nghiệm & Đánh giá nguyên mẫu* (Prototype Evaluation)
  3. *Chuẩn bị & Sản xuất loạt* (Serial Production)
- **Kết quả:** Tránh phình to cây focus (không bị rối màn hình), nhưng gameplay có chiều sâu chiến lược cực cao.

---

## II. KIẾN TRÚC CÂY FOCUS HOÀN CHỈNH (9 FOCUS: I1 → I9)

### 1. Sơ đồ cây nhánh (Focus Tree Layout)

```
                   [I1] Chuyển đổi công nghệ & quản trị
                     (production_governance - 2009, 190, 3)
                       ┌────────────────┴────────────────┐
                       ▼                                 ▼
             [I2] Z131 & đạn dược              [I3] Kết cấu thiết giáp
              (precision_z131, 188, 4)           (armor_structures, 192, 4)
                       │                                 │
                       ▼                                 ▼
             [I4] Chương trình XCB-01          [I5] Chương trình XTC
               (xcb01_design, 188, 5)             (xtc_program, 192, 5)
                       │                                 │
                       ▼                                 ▼
             [I7] Pháo tự hành SPG             [I6] Xe tăng bơi T-1
               (spg_program, 188, 6)             (t1_light_tank, 192, 6)
                       └────────────────┬────────────────┘
                                        ▼ (Hội tụ 2 cột)
                        [I8] Công nghiệp hóa sản xuất loạt
                          (serial_industrialization - 2029, 190, 7)
                                        ▼
                      [I9] Xe tăng chiến đấu chủ lực T-2
                           (t2_main_tank - CAPSTONE 2033, 190, 8)

          ··············· (VÙNG ĐỆM THÔNG THOÁNG: y = 9, 10) ···············

  [P1] Phòng thủ (178, 11) ◄─► [M1] Cơ giới (184, 11) ◄─► [R1] Cơ động (190, 11)
```

---

### 2. Bảng Danh Mục Chi Tiết 9 Focus

| ID Focus | Tên Focus | Icon | Cost | Tiên Quyết (Prerequisite) | Điều Kiện Mở Khóa (Gating) | Hiệu Ứng Hoàn Thành (Completion Reward) |
|:---|:---|:---|:---:|:---|:---|:---|
| **I1** `VIE_lf_ind_production_governance` | Chuyển đổi công nghệ & quản trị | `GFX_focus_VIE_lf_army_reform` | 7 | `VIE_lf_root_modern_army` | Không khóa ngày (Tự do theo chuỗi) | +20 CP, Idea quản trị, 1x 50% Tech CN, +1 Xưởng vũ khí (Hà Nội). |
| **I2** `VIE_lf_ind_precision_z131` | Cơ khí chính xác & đạn dược Z131 | `GFX_focus_VIE_lf_arm_arty_train` | 7 | I1 | Không khóa ngày (Cột trái) | +20 CP, Idea đạn dược, 1x 50% Tech đạn pháo, +1 Xưởng vũ khí (Thái Nguyên). |
| **I3** `VIE_lf_ind_armor_structures` | Chế tạo kết cấu thiết giáp | `GFX_focus_VIE_lf_arm_armor_org` | 7 | I1 | Không khóa ngày (Cột phải) | +20 CP, 1x 50% Tech IFV, +50 APC_2 vào kho. |
| **I4** `VIE_lf_ind_xcb01_design` | Chương trình XCB-01 | `GFX_focus_VIE_lf_arm_armor_train` | 7 | I2 | Tự do theo chuỗi I2 | +25 CP, Idea tích hợp IFV, 1x 50% Tech IFV, mở 2 Decisions XCB-01. |
| **I5** `VIE_lf_ind_xtc_program` *(Mới)* | Chương trình XTC (XTC-02 / XTC-03) | `GFX_focus_VIE_lf_arm_armor_org` | 7 | I3 | Tự do theo chuỗi I3 | +25 CP, Idea XTC, 1x 50% Tech Cơ giới hóa, mở 2 Decisions XTC. |
| **I6** `VIE_lf_ind_t1_light_tank` *(Mới)* | Dự án xe tăng bơi T-1 | `GFX_focus_VIE_lf_arm_armor_train` | 7 | I5 | Tự do theo chuỗi I5 | +25 CP, Idea T-1, 1x 50% Tech Thiết giáp nhẹ, mở 2 Decisions T-1. |
| **I7** `VIE_lf_ind_spg_program` *(Mới)* | Pháo tự hành nội địa | `GFX_focus_VIE_lf_arm_arty_train` | 7 | I4 | Tự do theo chuỗi I4 | +25 CP, Idea SPG, 1x 50% Tech Pháo binh, mở 2 Decisions SPG. |
| **I8** `VIE_lf_ind_serial_industrialization` | Công nghiệp hóa sản xuất loạt | `GFX_focus_VIE_lf_force_complete` | 7 | I7 + I6 (Hội tụ 2 cột) | Hoàn thành cả 2 trục I7 và I6 | +25 CP, Idea sản xuất loạt, 1x 50% Tech Giáp, +1 Xưởng vũ khí (Đà Nẵng), cấp XCB-01. |
| **I9** `VIE_lf_ind_t2_main_tank` *(Mới - Đỉnh cao)* | Xe tăng chiến đấu chủ lực T-2 | `GFX_focus_VIE_lf_arm_armor_train` | 10 | I8 | Hoàn thành I8 | +30 CP, Idea T-2 MBT, 2x 75% Tech Thiết giáp, mở trọn bộ 3 Decisions T-2. |

> **Cập nhật chuẩn MD:** Đã gỡ bỏ toàn bộ khóa thời gian cứng (`date >`) ở cả 16 focus Lục quân và 13 focus Hải quân. Tiến độ hiện đại hóa hoàn toàn do người chơi tự điều tiết thông qua năng lực kinh tế, chuỗi tiên quyết và thời gian thi công dự án trong Decisions.

---

## III. HỆ THỐNG QUYẾT ĐỊNH (DECISIONS) ĐIỀU HÀNH DỰ ÁN

Mỗi chương trình khí tài được vận hành theo chuỗi quyết định chuyên biệt với tiến trình chặt chẽ:

```mermaid
graph LR
    A[Mở Khóa qua Focus] --> B[Giai đoạn 1: Thiết kế kỹ thuật]
    B -->|Hoàn thành sau 120-180 ngày| C[Giai đoạn 2: Thử nghiệm nguyên mẫu]
    C -->|Hoàn thành sau 150-210 ngày| D[Giai đoạn 3: Sản xuất loạt]
```

### Bảng Danh Mục Quyết Định Chi Tiết

| Chương Trình | Quyết Định | Chi Phí (PP) | Thời Gian | Điều Kiện Tiên Quyết | Phần Thưởng Khi Hoàn Thành |
|:---|:---|:---:|:---:|:---|:---|
| **XCB-01** | `VIE_lf_xcb01_design_program` | 50 | 120 ngày | Hoàn thành I4 | +100% Tech IFV, cờ hoàn thành thiết kế |
| | `VIE_lf_xcb01_prototype_evaluation` | 50 | 150 ngày | Đã thiết kế xong | +75% Tech IFV, +20 IFV_2 nguyên mẫu |
| | `VIE_lf_xcb01_serial_preparation` | 75 | 180 ngày | Hoàn thành I8 | +50% Tech IFV, +40 IFV_3 vào kho |
| **XTC** | `VIE_lf_xtc02_prototype_program` | 50 | 120 ngày | Hoàn thành I5 | +100% Tech Cơ giới hóa, +40 APC_2 vào kho |
| | `VIE_lf_xtc03_upgrade_program` | 50 | 150 ngày | XTC-02 hoàn tất | +75% Tech Cơ giới hóa, +30 APC_3 vào kho |
| **T-1** | `VIE_lf_t1_design_program` | 50 | 120 ngày | Hoàn thành I6 | +100% Tech Thiết giáp nhẹ, cờ thiết kế |
| | `VIE_lf_t1_prototype_evaluation` | 50 | 150 ngày | Đã thiết kế xong | +75% Tech Thiết giáp nhẹ, +20 Light Tank vào kho |
| **SPG** | `VIE_lf_spg_design_program` | 50 | 120 ngày | Hoàn thành I7 | +100% Tech Pháo binh, cờ thiết kế |
| | `VIE_lf_spg_prototype_evaluation` | 50 | 150 ngày | Đã thiết kế xong | +75% Tech Pháo binh, +30 SP_arty_2 vào kho |
| **T-2 MBT** | `VIE_lf_t2_design_program` | 75 | 180 ngày | Hoàn thành I9 | 2x 100% Tech Thiết giáp chủ lực |
| | `VIE_lf_t2_prototype_evaluation` | 75 | 210 ngày | Đã thiết kế T-2 | +75% Tech Giáp, +10 T-2 nguyên mẫu |
| | `VIE_lf_t2_serial_production` | 100 | 365 ngày | Đánh giá đạt chuẩn | +50% Tech Giáp, +50 T-2 MBT, +2 Xưởng vũ khí (Z179) |

---

## IV. BẢN ĐẶC TẢ THIẾT KẾ KỸ THUẬT 5 DÒNG KHÍ TÀI

### 1. Bảng So Sánh Thông Số Kỹ Thuật Tổng Hợp

| Thông Số Kỹ Thuật | 1. XCB-01 (IFV) | 2. XTC-02/03 (APC) | 3. T-1 (Light Tank) | 4. SPG Nội Địa (PTH) | 5. T-2 MBT (Capstone) |
|:---|:---|:---|:---|:---|:---|
| **Thế hệ quân sự** | Gen 3 / Gen 3+ | Gen 3 (02) / Gen 3+ (03) | Gen 3 (Lội nước) | Gen 3+ (Kỹ thuật số) | **Gen 3+ / Gen 4** |
| **Chassis NSB** | `medium_tank_flame_chassis_3` | `medium_tank_amphibious_chassis_2` | `medium_tank_destroyer_chassis_2` | `medium_tank_artillery_chassis_2` | **`medium_tank_chassis_4`** |
| **Equipment non-NSB** | `IFV_6` / `IFV_7` | `APC_5` / `APC_6` | `Rec_tank_2` / `light_tank_2` | `SP_arty_2` / `SP_arty_3` | **`MBT_7` / `MBT_8`** |
| **Trọng lượng chiến đấu** | 18 – 22 tấn | 14 – 16 tấn | 18 – 20 tấn | 28 – 32 tấn | **48 – 52 tấn** |
| **Khung gầm vận động** | Bánh xích lội nước | Bánh lốp 8x8 hoặc xích nhẹ | Bánh xích 2 ống Waterjet | Bánh xích hạng nặng / 8x8 | Bánh xích chịu lực nặng |
| **Hỏa lực chính** | Pháo 30mm 2A42 | Súng máy 12.7mm / RWS | Pháo 85mm / 105mm áp lực thấp | Lựu pháo 152mm L/47 | **Pháo nòng trơn 125mm Gen 4** |
| **Hỏa lực phụ / ATGM** | 2x ATGM Kornet + PKT 7.62 | PKT 7.62 + súng phóng lựu 30mm | PKT 7.62 + 12.7mm nóc tháp | Súng máy 12.7mm tự vệ | **RWS 12.7mm CITV + PKT 7.62** |
| **Cơ cấu nạp đạn** | Tự động hộp tiếp đạn | Thủ công / nạp từ dây đạn | Bán tự động | Tự động hóa tay máy | **Ổ xoay cách ly buồng đạn** |
| **Giáp bảo vệ** | Thép cán hàn + Composite | Thép chống đạn + gốm nhẹ | Hợp kim nhôm + Thép nhẹ | Thép chống mảnh đạn | **NERA đa lớp + ERA Gen 3/4** |
| **Phòng vệ tích cực** | Ống phóng lựu đạn khói | Ống phóng đạn khói | Ống phóng đạn khói | Cảnh báo laser + đạn khói | **APS chủ động + Khói Aerosol** |
| **Điều khiển hỏa lực** | Quang điện tử + Đo xa laser | Camera quang học 360° | Ổn định 2 trục + Đo xa laser | FCS kỹ thuật số + GPS/INS | **Digital FCS + Hunter-Killer** |
| **Động cơ & Vận tốc** | Diesel 500 hp; 70 km/h (bộ) | Diesel 400 hp; 90 km/h (bộ) | Diesel 600 hp; 12 km/h (bơi) | Diesel 650 hp; 60 km/h | **Diesel 1.500 hp; 75 km/h** |

---

### 2. Thiết Kế Chi Tiết & Mã Nguồn Biến Thể (NSB Variants)

#### A. XCB-01 — Xe Chiến Đấu Bộ Binh Nội Địa
```pdx
create_equipment_variant = {
    name = "XCB-01"
    type = medium_tank_flame_chassis_3
    parent_version = 0
    modules = {
        main_armament_slot = afv_assault_gun_2
        secondary_armament_slot = afv_coax_machine_gun_2
        reload_type_slot = automatic_loading
        ammunition_load_slot = anti_infantry_main_ammo_2
        turret_type_slot = tank_base_tank_turret
        suspension_type_slot = tank_torsion_bar_suspension_medium
        armor_type_slot = afv_alum_armor_gen2
        engine_type_slot = tank_diesel_engine_gen3
        special_type_slot_1 = smoothbore_atgm_gen2
        special_type_slot_2 = smoke_launchers_2
        special_type_slot_3 = afv_troop_capacity
        special_type_slot_4 = tank_battlestation_2_thermal
        special_type_slot_5 = afv_gun_ports
    }
    upgrades = { tank_nsb_armor_upgrade = 2 tank_nsb_engine_upgrade = 2 }
    design_team = mio:VIE_gdt_manufacturer
}
```

#### B. XTC-02 / XTC-03 — Dòng Xe Thiết Giáp Chở Quân
```pdx
create_equipment_variant = {
    name = "XTC-03"
    type = medium_tank_amphibious_chassis_2
    parent_version = 0
    modules = {
        main_armament_slot = afv_machine_gun_2
        secondary_armament_slot = afv_coax_machine_gun_2
        reload_type_slot = manual_loading
        ammunition_load_slot = machine_gun_ammo_1
        turret_type_slot = tank_base_tank_turret
        suspension_type_slot = tank_wheeled_suspension_medium
        armor_type_slot = tank_steel_armor_gen2
        engine_type_slot = tank_diesel_engine_gen3
        special_type_slot_1 = smoke_launchers_2
        special_type_slot_2 = afv_troop_capacity
        special_type_slot_3 = afv_gun_ports
        special_type_slot_4 = tank_battlestation_2_thermal
        special_type_slot_5 = spaced_armor_gen2
    }
    upgrades = { tank_nsb_armor_upgrade = 3 tank_nsb_engine_upgrade = 3 }
    design_team = mio:VIE_gdt_manufacturer
}
```

#### C. T-1 — Xe Tăng Bơi Hạng Nhẹ Lội Nước
```pdx
create_equipment_variant = {
    name = "T-1"
    type = medium_tank_destroyer_chassis_2
    parent_version = 0
    modules = {
        main_armament_slot = tank_small_medium_cannon
        secondary_armament_slot = afv_coax_machine_gun_2
        reload_type_slot = manual_loading
        ammunition_load_slot = mixed_main_ammo_2
        turret_type_slot = tank_soviet_turret
        suspension_type_slot = tank_torsion_bar_suspension_light
        armor_type_slot = afv_alum_armor_gen2
        engine_type_slot = tank_diesel_engine_gen3
        special_type_slot_1 = smoke_launchers_2
        special_type_slot_2 = additional_mg
        special_type_slot_3 = smoothbore_atgm_gen2
        special_type_slot_4 = tank_battlestation_2_thermal
    }
    upgrades = { tank_nsb_armor_upgrade = 2 tank_nsb_engine_upgrade = 4 }
    design_team = mio:VIE_gdt_manufacturer
}
```

#### D. SPG Nội Địa (PTH-152M) — Pháo Tự Hành Kỹ Thuật Số
```pdx
create_equipment_variant = {
    name = "PTH-152M"
    type = medium_tank_artillery_chassis_2
    parent_version = 0
    modules = {
        main_armament_slot = art_med_gun_gen2
        secondary_armament_slot = afv_coax_machine_gun_2
        reload_type_slot = automatic_loading
        ammunition_load_slot = artillery_medium_ammo_2
        turret_type_slot = tank_base_tank_turret
        suspension_type_slot = tank_pneumatic_suspension_medium
        armor_type_slot = tank_steel_armor_gen2
        engine_type_slot = tank_diesel_engine_gen3
        special_type_slot_1 = smoke_launchers_2
        special_type_slot_2 = additional_mg
        special_type_slot_3 = laser_guided_ammo_1
        special_type_slot_4 = tank_battlestation_3
    }
    upgrades = { tank_nsb_fire_upgrade = 3 tank_nsb_engine_upgrade = 2 }
    design_team = mio:VIE_gdt_manufacturer
}
```

#### E. T-2 MBT — Xe Tăng Chiến Đấu Chủ Lực Thế Hệ Mới (Capstone 2033+)
```pdx
create_equipment_variant = {
    name = "T-2 MBT"
    type = medium_tank_chassis_4
    parent_version = 0
    modules = {
        main_armament_slot = tank_medium_cannon_3
        secondary_armament_slot = afv_coax_machine_gun_2
        reload_type_slot = automatic_loading
        ammunition_load_slot = mixed_main_ammo_2
        turret_type_slot = tank_base_tank_turret
        suspension_type_slot = tank_torsion_bar_suspension_medium
        armor_type_slot = nera_armor_gen2
        engine_type_slot = tank_diesel_engine_gen4
        special_type_slot_1 = smoke_launchers_3
        special_type_slot_2 = additional_mg
        special_type_slot_3 = smoothbore_atgm_gen3
        special_type_slot_4 = tank_battlestation_3
        special_type_slot_6 = reactive_armor_gen3
    }
    upgrades = {
        tank_nsb_armor_upgrade = 4
        tank_nsb_engine_upgrade = 4
        tank_nsb_fire_upgrade = 4
    }
    design_team = mio:VIE_gdt_manufacturer
}
```

---

## V. NHẬT KÝ THAY ĐỔI MÃ NGUỒN (CODE MODIFICATION LOG)

Toàn bộ các tệp tin trong repository đã được chỉnh sửa đồng bộ và vượt qua kiểm tra cú pháp:

1. **`common/national_focus/VIE_md_focus.txt`**
   - Đổi tên focus I5 cũ `VIE_lf_ind_serial_ground_equipment` → `VIE_lf_ind_serial_industrialization` (I8), lùi mốc thời gian sang > 2029.
   - Thêm 3 focus mới: `VIE_lf_ind_xtc_program` (I5), `VIE_lf_ind_t1_light_tank` (I6), `VIE_lf_ind_spg_program` (I7).
   - Thêm focus chốt chặn `VIE_lf_ind_t2_main_tank` (I9), mốc > 2033, cost = 10.
2. **`common/scripted_effects/VIE_md_effects.txt`**
   - Đổi `VIE_lf_reward_i5_effect` cũ → `VIE_lf_reward_i8_effect`.
   - Bổ sung các scripted effects: `VIE_lf_reward_i5_effect` (XTC), `VIE_lf_reward_i6_effect` (T-1), `VIE_lf_reward_i7_effect` (SPG), `VIE_lf_reward_i9_effect` (T-2 MBT).
3. **`common/ideas/VIE_md_ideas.txt`**
   - Thêm 4 national ideas: `VIE_lf_xtc_program_idea`, `VIE_lf_t1_light_tank_idea`, `VIE_lf_spg_program_idea`, `VIE_lf_t2_main_tank_idea`.
4. **`common/decisions/VIE_md_decisions.txt`**
   - Bổ sung 9 decisions điều hành dự án: 2 cho XTC, 2 cho T-1, 2 cho SPG, 3 cho T-2 MBT.
5. **`localisation/english/replace/VIE_replace_military_l_english.yml`**
   - Bổ sung đầy đủ chuỗi bản địa hóa tên focus, mô tả, custom tooltip, tên idea, tên decision cho toàn bộ I5 → I9.

---

## VI. KẾT LUẬN VÀ BƯỚC TIẾP THEO

Nhánh Công nghiệp Quốc phòng Lục quân đã được nâng cấp toàn diện từ khung sơ khai 5 node thành **hệ sinh thái công nghiệp quân sự 9 node** hoàn chỉnh, tái hiện chân thực các chương trình khí tài thực tế của Quân đội Nhân dân Việt Nam và mở ra tầm nhìn đến năm 2035 với siêu xe tăng T-2 MBT.
