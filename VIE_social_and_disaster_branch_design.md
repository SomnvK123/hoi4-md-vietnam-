# Thiết kế Mở rộng: Nhánh Phát triển Xã hội & Thiên tai Khí hậu

> **Tài liệu nghiên cứu & thiết kế mở rộng (08/10/2026)**  
> Hợp nhất 2 tài liệu thiết kế nhánh Xã hội (Giáo dục, Y tế, An sinh) và nhánh Thiên tai & Khí hậu.

## Mục lục
1. [Phần 1: Nhánh Phát triển Xã hội & Chiến lược Giáo dục](#phần-1-nhánh-phát-triển-xã-hội--chiến-lược-giáo-dục)
2. [Phần 2: Nhánh Thiên tai & Khí hậu](#phần-2-nhánh-thiên-tai--khí-hậu)

---

## Phần 1: Nhánh Phát triển Xã hội & Chiến lược Giáo dục

# VIE — Tách nhánh "Chiến lược giáo dục": root Phát triển Xã hội + root Thiên tai & Khí hậu

> ⚠️ **Đã thay đổi (03/10/2026):** theo quyết định mới, 6 focus giáo dục và 8 focus thiên tai đã bị **xóa khỏi nhánh Kinh tế**, cùng 20 focus y tế / an sinh / văn hóa / đô thị còn lại của cụm cũ và các idea, event liên quan; chỉ còn 4 focus luật trong phần Chính trị (`VIE_higher_education_law`, `VIE_education_law_2019`, `VIE_disaster_law_2013`, `VIE_civil_defense_law_2023`) dưới `VIE_constitution_2013`. Tài liệu này giữ lại làm tham khảo cho thiết kế mở rộng sau, không còn phản ánh trạng thái cây hiện tại.

> Trạng thái: **đề xuất thiết kế**, chưa code. Ngày: 03/10/2026  
> Phạm vi: `VIE_education_reform` và 33 focus con trong `common/national_focus/VIE_md_focus.txt`

---

## 1. Chẩn đoán

`VIE_education_reform` ("Chiến lược giáo dục 2001–2010") hiện là con của `VIE_doi_moi_continues`. Dưới nó có **34 focus thuộc 6 chủ đề**, không chủ đề nào liên quan tới giáo dục ngoài chính nó:

| Chủ đề | Số focus | Focus hiện có |
|---|---|---|
| Giáo dục | 6 | education_reform, english_second_language, education_nq29, university_autonomy, free_tuition, vocational_training |
| Y tế | 7 | universal_health_insurance, grassroots_clinics, vaccine_production, hospital_decongestion, preventive_health, covid_zero_extend ⟷ covid_safe_adaptation |
| An sinh, lao động, dân số | 4 | social_insurance_reform, labor_code_2019, population_policy, overseas_vietnamese |
| Văn hóa, thể thao, du lịch | 5 | heritage_preservation, sea_games_bid, visa_reform, cultural_industry, tourism_powerhouse |
| Đô thị | 4 | urbanization, hanoi_expansion_2008 ⟷ hanoi_keep_boundaries, hanoi_metro |
| Thiên tai, khí hậu | 8 | disaster_preparedness, military_rescue_corps, emergency_operations_center, dutch_water_model ⟷ nature_adaptation_120, sustainable_mekong_delta, satellite_early_warning, storm_resilient_islands |

Hệ quả:
- Bảo hiểm y tế (2009), Bộ luật Lao động (2019) hay Phòng chống thiên tai (2013) đều phải chờ "Chiến lược giáo dục". Về logic lịch sử, chúng không phụ thuộc vào nhau.
- `VIE_doi_moi_continues` có 10 nhánh con, một nửa trong số đó không phải kinh tế.
- Filter tìm kiếm của cụm này gần như chỉ là `STABILITY`, nên người chơi khó lọc.

### Lỗi phát hiện kèm (sửa trong lúc tách)

| # | Focus | Lỗi |
|---|---|---|
| L1 | `VIE_hanoi_metro` | Xây infra ở **522** (TP.HCM). Hà Nội là **519** |
| L2 | `VIE_urbanization` | Gọi `add_building_construction` trực tiếp trong `every_owned_state`, sai chuẩn mục 6 (phải dùng `one_state_infrastructure`) |
| L3 | `VIE_hcmc_metro` | Là root mồ côi, không có prerequisite |
| L4 | `VIE_mekong_climate_adaptation` (nhánh nông nghiệp) | Trùng chủ đề với `nature_adaptation_120` và `sustainable_mekong_delta` |
| L5 | `VIE_overseas_vietnamese` | Là focus ngoại giao (bắn `vie_dip.19`) nhưng đang nằm dưới Bộ luật Lao động |

---

## 2. Phương án đề xuất

Tách thành **1 root mới** và **2 phần chuyển đi**:

```
TRƯỚC                                   SAU
doi_moi_continues                       doi_moi_continues (chỉ còn kinh tế)
 └─ education_reform (34 focus)         │
                                        ROOT MỚI  VIE_social_development  "Phát triển Xã hội"
                                         ├─ Giáo dục & Đào tạo      (6 cũ + 5 mới)
                                         ├─ Y tế                     (7 cũ + 4 mới)
                                         ├─ An sinh – Lao động – Dân số (3 cũ + 5 mới)
                                         └─ Văn hóa – Thể thao – Du lịch (5 cũ + 4 mới)

                                        ROOT MỚI  VIE_disaster_preparedness "Thiên tai & Khí hậu"
                                         └─ 6 nhánh, 8 focus cũ + 24 mới (xem tài liệu riêng)

                                        HẠ TẦNG (north_south_expressway)
                                         └─ urbanization → hà nội ⟷ → hanoi_metro / hcmc_metro

                                        NGOẠI GIAO
                                         └─ overseas_vietnamese
```

Lý do chọn phương án này:
- MD đã có sẵn 3 hệ thống ngân sách xã hội: `increase_education_budget`, `increase_healthcare_budget`, `increase_social_spending` và các `change_expected_*_spending`. Một root riêng giúp cả 3 trục này dùng chung một chỗ.
- Thiên tai và khí hậu là chủ đề an ninh, có cả lực lượng cứu hộ quân đội và radar, lại nối với các event `vie_soc.3` và `vie_disaster.*`. Gộp vào Xã hội sẽ lại thành một nhánh lẫn lộn.
- Đô thị và Metro thuộc hạ tầng. `hcmc_metro` đang mồ côi ở x=176, ngay cạnh cụm cao tốc, nên gom về đó là tự nhiên.

Root mới theo chuẩn mục 10.1: không có prerequisite, guard bằng `VIE_ax_init` và `VIE_ax_initialized`, có thêm shortcut `VIE_social_shortcut`.

---

## 3. Root Xã hội — chi tiết

Ký hiệu: **[cũ]** giữ nguyên reward, chỉ đổi prerequisite và vị trí. **[mới]** là focus thêm mới. Mốc thời gian là điều kiện `available`.

### 3.0 Root

| Focus | Mốc | Nội dung |
|---|---|---|
| **[mới]** `VIE_social_development` "Phát triển Xã hội" | 2001 | Root. Init trục ax và cho +PP nhỏ. Mở 4 nhánh |

### 3.1 Giáo dục & Đào tạo

```
social_development
 └─ education_reform [cũ, 2001]
     ├─ preschool_universal_5 [mới, 2010]
     ├─ english_second_language [cũ, 2008]
     │   └─ education_nq29 [cũ, 2013]
     │       ├─ general_curriculum_2018 [mới, 2018]
     │       │   ├─ textbooks_multi_set ⟷ textbooks_unified [mới, 2025]
     │       └─ university_autonomy [cũ, 2015]
     │           └─ free_tuition [cũ, 2025]
     │               └─ education_breakthrough_nq71 [mới, 2025, capstone]
     ├─ vocational_training [cũ, 2015]
     └─ border_boarding_schools [mới, 2025]  (nối ethnic_policy)
```

| Focus mới | Cơ sở lịch sử | Reward gợi ý |
|---|---|---|
| `preschool_universal_5` | QĐ 239/QĐ-TTg (2/2010): phổ cập mầm non 5 tuổi | `increase_education_budget`, +stability nhỏ, `VIE_ax_size +1` |
| `general_curriculum_2018` | Chương trình GDPT 2018, triển khai từ lớp 1 năm học 2020–21 (NQ 88/2014/QH13) | tech bonus `CAT_computing_tech`, `VIE_ax_merit +1` |
| `textbooks_multi_set` ⟷ `textbooks_unified` | Tranh luận "một chương trình nhiều bộ sách" và "bộ SGK thống nhất toàn quốc", được NQ 71 chốt theo hướng thống nhất | multi: `ax_market +1`, `ax_decent +1`. unified: `ax_checks +1`, +stability, giảm chi phí cho gia đình (`treasury −1`) |
| `border_boarding_schools` | Chủ trương xây trường nội trú liên cấp ở các xã biên giới đất liền (2025) | `treasury −2`, +stability, opinion `farmers +3`. Yêu cầu `has_completed_focus = VIE_ethnic_policy` |
| `education_breakthrough_nq71` | NQ 71-NQ/TW (8/2025) về đột phá phát triển giáo dục & đào tạo | Idea capstone thay `VIE_education_idea` (research speed). Yêu cầu NQ29 và free_tuition |

### 3.2 Y tế

```
social_development
 └─ universal_health_insurance [cũ, 2009]
     ├─ doctor_rotation_1816 [mới, 2008]
     │   └─ grassroots_clinics [cũ]
     │       ├─ hospital_decongestion [cũ, 2013]
     │       │   └─ health_nq20 [mới, 2017]
     │       │       └─ preventive_health [cũ]
     │       ├─ vaccine_production [cũ, 2021]
     │       └─ covid_zero_extend ⟷ covid_safe_adaptation [cũ, 10/2021]
     ├─ medical_examination_law_2023 [mới, 2023]
     │   └─ electronic_health_records [mới, 2024]  (nối digital_id)
     └─ health_breakthrough_nq72 [mới, 2025, capstone]
```

| Focus mới | Cơ sở lịch sử | Reward gợi ý |
|---|---|---|
| `doctor_rotation_1816` | Đề án 1816 (QĐ 1816/QĐ-BYT, 5/2008): luân phiên bác sĩ tuyến trên về tuyến dưới | `ax_decent +1`, opinion `farmers +3` |
| `health_nq20` | NQ 20-NQ/TW (10/2017) về bảo vệ, chăm sóc và nâng cao sức khỏe nhân dân | `increase_healthcare_budget`, `change_expected_health_spending` |
| `medical_examination_law_2023` | Luật Khám bệnh, chữa bệnh 2023 (hiệu lực 2024) | `ax_checks +1`, +stability |
| `electronic_health_records` | Sổ sức khỏe điện tử tích hợp VNeID | Yêu cầu `VIE_digital_id`. Tech bonus `CAT_computing_tech` |
| `health_breakthrough_nq72` | NQ 72-NQ/TW (9/2025): lộ trình miễn viện phí cơ bản, khám sức khỏe định kỳ miễn phí | `treasury −5`, idea capstone. **Cần bankruptcy guard** |

### 3.3 An sinh – Lao động – Dân số

```
social_development
 └─ social_insurance_reform [cũ, 2014]
     ├─ labor_code_2019 [cũ, 2019]
     │   ├─ wage_reform_2024 [mới, 7/2024]
     │   └─ employment_law_2025 [mới, 2025]
     ├─ social_insurance_law_2024 [mới, 7/2025]
     ├─ sustainable_poverty_reduction [mới, 2021]
     │   ├─ social_housing_million [mới, 2023]
     │   └─ eliminate_temporary_housing [mới, 10/2024]
     └─ population_policy [cũ, 2025]  → nối sang ageing_society (đã có)
```

| Focus mới | Cơ sở lịch sử | Reward gợi ý |
|---|---|---|
| `wage_reform_2024` | NQ 27-NQ/TW (2018). Cải cách tiền lương từ 1/7/2024, lương cơ sở 1,8 lên 2,34 triệu | `treasury −3`, +stability, opinion `communist_cadres +5`. **Cần guard** |
| `employment_law_2025` | Luật Việc làm 2025 (bảo hiểm thất nghiệp mở rộng) | `increase_social_spending`, `ax_size +1` |
| `social_insurance_law_2024` | Luật BHXH 2024: giảm số năm đóng tối thiểu từ 20 xuống 15, hiệu lực 7/2025 | `change_expected_social_spending`, +stability |
| `sustainable_poverty_reduction` | Chương trình MTQG giảm nghèo bền vững 2021–2025 | opinion `farmers +5`, `increase_economic_growth` |
| `social_housing_million` | Đề án 1 triệu căn nhà ở xã hội (QĐ 338/QĐ-TTg, 4/2023) | `519/522 one_state_infrastructure`, opinion `industrial_conglomerates +3` |
| `eliminate_temporary_housing` | Phong trào xóa nhà tạm, nhà dột nát trên cả nước (phát động 10/2024) | +stability 0.03, +PP. Bắn event nhỏ khi hoàn thành |

Ghi chú: `population_policy` hiện chỉ cho +2% stability và +50 PP. Nên chỉnh loc thành "Bãi bỏ giới hạn hai con" (Pháp lệnh Dân số sửa đổi, 6/2025) và cho mở `VIE_ageing_society`.

### 3.4 Văn hóa – Thể thao – Du lịch

```
social_development
 └─ heritage_preservation [cũ]
     ├─ culture_people_nq33 [mới, 2014]
     │   ├─ national_culture_conference [mới, 11/2021]
     │   │   └─ cultural_industry [cũ]
     │   │       └─ tourism_powerhouse [cũ]
     │   └─ belief_religion_law [mới, 2016]
     ├─ sea_games_bid [cũ]
     │   └─ asiad_2019_host ⟷ asiad_2019_withdraw [mới, 2014]
     └─ visa_reform [cũ, 2023]
```

| Focus mới | Cơ sở lịch sử | Reward gợi ý |
|---|---|---|
| `culture_people_nq33` | NQ 33-NQ/TW (6/2014) về xây dựng văn hóa, con người Việt Nam | +stability, `ax_checks +1` |
| `national_culture_conference` | Hội nghị Văn hóa toàn quốc (11/2021) | +PP, idea nhỏ |
| `belief_religion_law` | Luật Tín ngưỡng, tôn giáo 2016 (hiệu lực 2018) | +stability, `ax_integ +1` (quan hệ Vatican, Hoa Kỳ). Nối `vie_dip` |
| `asiad_2019_host` ⟷ `asiad_2019_withdraw` | Việt Nam được trao ASIAD 18 (2012) rồi rút lui (4/2014) vì chi phí | host: `treasury −6`, +stability, +PP, có rủi ro event. withdraw: `treasury +1`, `ax_checks +1`. Đây là một lựa chọn "what-if" có thật |

---

## 4. Phần chuyển đi

### 4.1 Đô thị sang nhánh Hạ tầng

```
north_south_expressway
 └─ urbanization [cũ, sửa L2]
     ├─ hanoi_expansion_2008 ⟷ hanoi_keep_boundaries [cũ]
     │   └─ hanoi_metro [cũ, sửa L1: 522 → 519]
     └─ hcmc_metro [cũ, sửa L3: thêm prerequisite urbanization]
```

### 4.2 Thiên tai & khí hậu thành root riêng

Đã chốt: làm root riêng và phát triển thành một nội dung đầy đủ. Thiết kế chi tiết nằm ở [VIE_disaster_climate_design.md](VIE_disaster_climate_design.md).

### 4.3 Người Việt ở nước ngoài sang Ngoại giao

`overseas_vietnamese` đổi prerequisite sang một focus trong nhánh `VIE_asean_integration`, ví dụ ngay sau quan hệ với Hoa Kỳ.

---

## 5. Tổng kết số lượng

| | Trước | Sau |
|---|---|---|
| Root Phát triển Xã hội | — | 21 cũ + 23 mới (gồm root) = 44 |
| Sang Hạ tầng | — | 4 (+ hcmc_metro hết mồ côi) |
| Root Thiên tai & Khí hậu | 8 (nằm trong cụm) | 8 cũ + 24 mới = 32 (xóa `mekong_climate_adaptation`) |
| Sang Ngoại giao | — | 1 |
| Tổng cây | 357 | 403 |

---

## 6. Kế hoạch triển khai

1. **Bước 1 (không đổi gameplay):** đổi prerequisite và relative_position_id để tách 3 khối, sửa L1–L3 và L5. Chạy `validate_focus_tree.py` (forward-ref, orphan).
2. **Bước 2:** thêm root `VIE_social_development` và shortcut, sửa loc `population_policy`.
3. **Bước 3:** thêm 22 focus mới theo từng nhánh. Mỗi nhánh gồm loc VI, idea nếu có, và ai_will_do kèm guard khi chi tiền từ 5 bn trở lên.
4. **Bước 4:** layout lại (gap rule ở mục 7.1), chạy `standardize_focus_tree.py` và validator, rồi test trong game.

### Cần xác minh trước khi code

- Số và ngày chính xác của các văn bản 2025 (NQ 71, NQ 72, Luật Việc làm 2025, chủ trương trường nội trú biên giới).
- Reward của `VIE_mekong_climate_adaptation` để quyết định gộp hay xóa (L4).
- Các idea mới cần thêm vào `common/ideas/` mà không vượt trần modifier của trục ax (xem `tools/audit/nf_balance.py`).

---

## Phần 2: Nhánh Thiên tai & Khí hậu

# VIE — Root "Thiên tai & Khí hậu"

> ⚠️ **Đã thay đổi (03/10/2026):** theo quyết định mới, 6 focus giáo dục và 8 focus thiên tai đã bị **xóa khỏi nhánh Kinh tế**, cùng 20 focus y tế / an sinh / văn hóa / đô thị còn lại của cụm cũ và các idea, event liên quan; chỉ còn 4 focus luật trong phần Chính trị (`VIE_higher_education_law`, `VIE_education_law_2019`, `VIE_disaster_law_2013`, `VIE_civil_defense_law_2023`) dưới `VIE_constitution_2013`. Tài liệu này giữ lại làm tham khảo cho thiết kế mở rộng sau, không còn phản ánh trạng thái cây hiện tại.

> Trạng thái: **đề xuất thiết kế**, chưa code. Ngày: 03/10/2026  
> Liên quan: [VIE_social_branch_design.md](VIE_social_branch_design.md) (mục 4.2)

---

## 1. Hiện trạng

### 1.1 Đang có

| Loại | Nội dung |
|---|---|
| Focus | 8 focus dưới `VIE_disaster_preparedness`, cộng `VIE_mekong_climate_adaptation` nằm lạc ở nhánh nông nghiệp |
| Idea | `VIE_disaster_prep_idea` (stability +0.7%), `VIE_military_rescue_idea`, `VIE_dutch_engineering_idea`, `VIE_nature_adaptation_idea`, `VIE_mekong_granary_idea`, timed idea `VIE_salinity_emergency`, `VIE_nature_transition` |
| Event | `vie_soc.3` lũ miền Trung (ngẫu nhiên), `vie_soc.4` hạn mặn 2016, `vie_soc.5` hạn mặn 2020, `vie_soc.7` bão Yagi 2024 (`events/VIE_md_soc.txt`). `vie_disaster.1` siêu bão (MTTH), `vie_disaster.2` hạn mặn 2016 (`events/VIE_disaster_events.txt`) |

### 1.2 Vấn đề

| # | Vấn đề |
|---|---|
| T1 | **Event trùng nhau:** `vie_disaster.2` và `vie_soc.4` đều là hạn mặn ĐBSCL 2016. `vie_disaster.1` (siêu bão ngẫu nhiên) chồng lên `vie_soc.3` và `vie_soc.7` |
| T2 | **Ba cờ được đặt nhưng không ở đâu đọc:** `VIE_72h_early_warning_active`, `VIE_civil_defense_network_active`, `VIE_spratly_storm_shelter_ready`. Các focus Radar 72h, Sở Chỉ huy và Công sự chịu bão vì thế không có tác dụng thật lên thiên tai |
| T3 | Tác dụng giảm thiệt hại chỉ là bật/tắt theo một cờ (`VIE_disaster_prepared` hoặc `VIE_mekong_adapted`). Làm thêm focus không giúp chống chịu tốt hơn |
| T4 | `VIE_disaster_prep_idea` chỉ cho +0.7% stability, yếu so với cost 7 |
| T5 | `VIE_storm_resilient_islands` gọi `add_building_construction` trực tiếp (naval_base, bunker), dù đã tự trừ 3 bn |

---

## 2. Ý tưởng cốt lõi: chỉ số "Năng lực chống chịu"

Thêm một biến **`VIE_resilience`** (0–100), hiển thị bằng tooltip giống trục `VIE_ax_*`.

- **Tăng** khi hoàn thành focus trong root này (+3 đến +8 mỗi focus) và một số decision.
- **Giảm** từ từ khi bỏ ngân sách (decision quỹ PCTT hết hạn) và sau mỗi trận thiên tai lớn (−5, hạ tầng bị tàn phá).
- **Dùng:** mọi event thiên tai gọi chung một scripted effect `VIE_disaster_damage_effect` với `base_damage`. Thiệt hại thực tế bằng `base_damage × (1 − VIE_resilience / 140)`, nên ở mức tối đa vẫn còn khoảng 30% thiệt hại. Thiệt hại gồm treasury, stability và một timed idea tái thiết.

Ba cờ đang bị bỏ quên (T2) được dùng lại như sau:

| Cờ | Tác dụng mới |
|---|---|
| `VIE_72h_early_warning_active` | Bão lớn có **event cảnh báo trước** (`vie_disaster.10`), mở 3–7 ngày cho decision "Sơ tán khẩn cấp". Không có cờ này thì bão đổ bộ luôn, không có cảnh báo |
| `VIE_civil_defense_network_active` | Mở category decision "Ứng phó khẩn cấp" ngay khi có thiên tai, không phải chờ event |
| `VIE_spratly_storm_shelter_ready` | Event bão trên biển không làm mất tàu cá / tàu kiểm ngư ở Trường Sa. Nối với nhánh Biển Đông |

Hai cờ cũ `VIE_disaster_prepared` và `VIE_mekong_adapted` vẫn giữ để không làm vỡ event hiện có. Sau đó chuyển dần sang kiểm tra `VIE_resilience`.

---

## 3. Cây focus — 6 nhánh

Ký hiệu: **[cũ]** giữ reward, chỉ đổi vị trí/prerequisite. **[mới]** là focus thêm. **R+n** là cộng `VIE_resilience`.

```
VIE_disaster_preparedness  "Luật Phòng chống thiên tai" [cũ → ROOT, 2013]
 ├─ A. Thể chế & Chỉ huy
 ├─ B. Cứu hộ – Cứu nạn
 ├─ C. Cảnh báo sớm
 ├─ D. Đồng bằng sông Cửu Long
 ├─ E. Miền núi & Miền Trung
 └─ F. Môi trường
                     └──► climate_resilient_nation [mới, capstone]
```

Root mới: không có prerequisite, guard `VIE_ax_init`, shortcut `VIE_disaster_shortcut`. Mốc 2013 giữ nguyên (Luật PCTT số 33/2013/QH13), nên trước 2013 cả root đứng chờ. **Đề xuất** cho root mở từ 2001 với tên "Chương trình phòng chống thiên tai" và để 2013 là focus con `disaster_law_2013`. Như vậy bão và lũ năm 2000–2012 cũng có việc để làm.

### A. Thể chế & Chỉ huy

```
disaster_preparedness
 └─ disaster_fund [mới, 2014]
     └─ national_steering_committee [mới]
         └─ emergency_operations_center [cũ]
             └─ civil_defense_law_2023 [mới, 7/2024]
```

| Focus | Cơ sở | Reward gợi ý |
|---|---|---|
| `disaster_fund` | Quỹ Phòng chống thiên tai (NĐ 94/2014/NĐ-CP) | Mở decision "Giải ngân Quỹ PCTT". R+5. `treasury −1` |
| `national_steering_committee` | Ban Chỉ đạo Trung ương / Quốc gia về PCTT | R+3, +PP. `ax_checks +1` |
| `civil_defense_law_2023` | Luật Phòng thủ dân sự 2023 (hiệu lực 7/2024) | R+8, idea `VIE_civil_defense_idea` (thay `VIE_disaster_prep_idea`, sửa T4) |

### B. Cứu hộ – Cứu nạn

```
disaster_preparedness
 └─ military_rescue_corps [cũ]
     ├─ four_on_the_spot [mới]
     │   └─ commune_response_teams [mới]
     └─ rescue_aviation [mới]
         └─ international_rescue [mới, 2/2023]
```

| Focus | Cơ sở | Reward gợi ý |
|---|---|---|
| `four_on_the_spot` | Phương châm "4 tại chỗ": chỉ huy, lực lượng, vật tư, hậu cần tại chỗ | R+5, opinion `farmers +3`, `ax_decent +1` |
| `commune_response_teams` | Lực lượng xung kích PCTT cấp xã | R+4, `add_manpower` nhỏ, +stability |
| `rescue_aviation` | Trực thăng cứu hộ của Không quân, phục vụ vùng bị chia cắt | R+4. Nối nhánh Không quân (`VIE_airf_*`) nếu đã có |
| `international_rescue` | Việt Nam cử đội cứu hộ sang Thổ Nhĩ Kỳ sau động đất (2/2023), tham gia AADMER / AHA Centre | `ax_integ +1`, opinion cải thiện với TUR và các nước ASEAN, +PP |

### C. Cảnh báo sớm

```
disaster_preparedness
 └─ hydromet_law_2015 [mới]
     └─ satellite_early_warning [cũ]  ── đặt VIE_72h_early_warning_active
         ├─ vnredsat [mới, 5/2013]
         ├─ cell_broadcast_alerts [mới, 2024]
         └─ storm_resilient_islands [cũ, sửa T5]
```

| Focus | Cơ sở | Reward gợi ý |
|---|---|---|
| `hydromet_law_2015` | Luật Khí tượng thủy văn 2015 | R+3, tech bonus nhỏ `CAT_computing_tech` |
| `vnredsat` | Vệ tinh quan sát Trái Đất VNREDSat-1 (phóng 5/2013) | R+4. Nối nhánh khoa học (Viện Hàn lâm, Trung tâm Vũ trụ) |
| `cell_broadcast_alerts` | Tin nhắn cảnh báo thiên tai gửi đến mọi thuê bao di động trong vùng ảnh hưởng | R+5. Yêu cầu `VIE_internet_expansion` hoặc 4G. Kéo dài thời gian sơ tán trong event cảnh báo |

### D. Đồng bằng sông Cửu Long

Giữ cặp lựa chọn cũ làm trục chính: **công trình kiểu Hà Lan** ⟷ **thuận thiên (NQ 120)**.

```
disaster_preparedness
 └─ mekong_delta_plan_2013 [mới, 2013]
     ├─ dutch_water_model [cũ]  ⟷  nature_adaptation_120 [cũ, 11/2017]
     │   └─ cai_lon_cai_be_sluice [mới]      └─ rice_shrimp_transition [mới]
     ├─ groundwater_law_2023 [mới]
     └─ sustainable_mekong_delta [cũ, OR của 2 nhánh]
         └─ one_million_ha_rice [mới, 11/2023]
```

| Focus | Cơ sở | Reward gợi ý |
|---|---|---|
| `mekong_delta_plan_2013` | Kế hoạch Đồng bằng sông Cửu Long (hợp tác Việt Nam – Hà Lan, 2013) | Đặt `VIE_mekong_adapted` (thay `mekong_climate_adaptation`). R+3 |
| `cai_lon_cai_be_sluice` | Hệ thống thủy lợi Cái Lớn – Cái Bé chống xâm nhập mặn | `518 one_state_infrastructure`, `treasury −3`, R+6. Hạn mặn giảm mạnh, nhưng opinion `farmers −2` |
| `rice_shrimp_transition` | Chuyển đổi lúa – tôm và lúa – thủy sản theo NQ 120 | R+5, opinion `farmers +5`, `increase_economic_growth` |
| `groundwater_law_2023` | Luật Tài nguyên nước 2023, hạn chế khai thác nước ngầm (sụt lún) | R+4, `ax_checks +1`. Opinion `industrial_conglomerates −2` |
| `one_million_ha_rice` | Đề án 1 triệu ha lúa chất lượng cao, phát thải thấp (QĐ 1490/QĐ-TTg, 11/2023) | Tăng idea `VIE_mekong_granary_idea`. Nối `VIE_rice_export_power` |

Xử lý `VIE_mekong_climate_adaptation`: xóa khỏi nhánh nông nghiệp, chuyển cờ `VIE_mekong_adapted` sang `mekong_delta_plan_2013`. Nhờ vậy event hạn mặn 2016 (`vie_soc.4`) có thể được giảm nhẹ nếu người chơi làm sớm. Lịch sử thì không làm kịp, và chính hạn mặn 2016 là lý do ra NQ 120 năm 2017.

### E. Miền núi & Miền Trung

```
disaster_preparedness
 └─ landslide_hazard_mapping [mới]
     ├─ reservoir_interlinked_operation [mới, 2020]
     ├─ highrisk_resettlement [mới, 2024]
     └─ billion_trees [mới, 2021]
```

| Focus | Cơ sở | Reward gợi ý |
|---|---|---|
| `landslide_hazard_mapping` | Bản đồ phân vùng nguy cơ lũ quét, sạt lở miền núi | R+4, tech bonus nhỏ |
| `reservoir_interlinked_operation` | Quy trình vận hành liên hồ chứa, siết thủy điện nhỏ sau lũ lịch sử miền Trung 10/2020 (Rào Trăng 3) | R+5. Opinion `industrial_conglomerates −3`. Nối nhánh điện (power_plan_8) |
| `highrisk_resettlement` | Di dời dân khỏi vùng sạt lở; tái thiết Làng Nủ (Lào Cai) sau bão Yagi 9/2024 | `treasury −2`, R+4, +stability. Có thể là phần thưởng của event `vie_soc.7` |
| `billion_trees` | Đề án trồng 1 tỷ cây xanh 2021–2025 (QĐ 524/QĐ-TTg), gồm rừng phòng hộ và rừng ngập mặn ven biển | R+5, `ax_integ +1`. Nối `VIE_net_zero_2050` |

### F. Môi trường

```
disaster_preparedness
 └─ formosa_crisis_response  ⟷  formosa_quiet_settlement [mới, 4/2016]
     └─ environment_law_2020 [mới]
         └─ air_quality_action [mới]
```

| Focus | Cơ sở | Reward gợi ý |
|---|---|---|
| `formosa_crisis_response` | Sự cố môi trường biển miền Trung do Formosa Hà Tĩnh (4/2016). Công ty nhận lỗi và bồi thường 500 triệu USD | `treasury +2` (bồi thường), +stability, `ax_checks +1`. Opinion `industrial_conglomerates −3` |
| `formosa_quiet_settlement` | Phương án "what-if": xử lý kín để giữ FDI | `ax_market +1`, nhưng −stability và tạo timed idea bất ổn ven biển miền Trung |
| `environment_law_2020` | Luật Bảo vệ môi trường 2020 (EPR, phân loại rác) | R+3, idea nhỏ `consumer_goods_factor` |
| `air_quality_action` | Ô nhiễm không khí Hà Nội, lộ trình hạn chế xe máy | +stability, opinion `farmers −1`. Nối metro bên nhánh Hạ tầng |

Cặp Formosa yêu cầu `VIE_formosa_steel_complex` (nhánh công nghiệp) đã hoàn thành. Như vậy hai nhánh có liên hệ nhân quả.

### Capstone

| Focus | Yêu cầu | Reward |
|---|---|---|
| `climate_resilient_nation` "Quốc gia chống chịu khí hậu" | `civil_defense_law_2023` + `sustainable_mekong_delta` + `VIE_resilience > 59` | Idea `VIE_climate_resilient_idea`: stability, giảm `consumer_goods_factor`. Nối `VIE_developed_nation_2045` |

---

## 4. Event & Decision

### 4.1 Gom event (sửa T1)

| Giữ | Gộp / xóa |
|---|---|
| `vie_soc.3` lũ miền Trung (ngẫu nhiên) | `vie_disaster.1` → đổi thành event **bão ngẫu nhiên** mùa bão (7–11), đi qua `VIE_disaster_damage_effect` |
| `vie_soc.4`, `vie_soc.5` hạn mặn 2016 / 2020 | **Xóa** `vie_disaster.2` (trùng `vie_soc.4`) |
| `vie_soc.7` bão Yagi 2024 | Thêm hệ quả lũ quét Làng Nủ, mở `highrisk_resettlement` |

Event mới đề xuất:

| ID | Nội dung | Mốc |
|---|---|---|
| `vie_disaster.10` | Cảnh báo bão 72h (chỉ khi có cờ cảnh báo): chọn sơ tán (−PP, −treasury nhỏ, thiệt hại −40%) hoặc chờ | trước mỗi bão lớn |
| `vie_disaster.11` | Bão Damrey (11/2017), trùng APEC Đà Nẵng | 11/2017 |
| `vie_disaster.12` | Chuỗi lũ lịch sử miền Trung, sạt lở Rào Trăng 3 | 10/2020 |
| `vie_disaster.13` | Sự cố Formosa: cá chết hàng loạt ven biển miền Trung (kích hoạt cặp focus F) | 4/2016 |
| `vie_disaster.14` | Đoàn cứu hộ Việt Nam sang Thổ Nhĩ Kỳ (khi có `international_rescue`) | 2/2023 |

### 4.2 Category decision "Ứng phó Thiên tai"

Mở khi có `disaster_fund`. Category hiện ngay khi đang có thiên tai nếu có `VIE_civil_defense_network_active`.

| Decision | Chi phí | Tác dụng |
|---|---|---|
| Giải ngân Quỹ PCTT | 25 PP | −1 bn, timed idea tái thiết nhanh 90 ngày |
| Huy động quân đội cứu hộ | 50 PP, cần `military_rescue_corps` | Giảm thiệt hại trận hiện tại, opinion `the_military +3` |
| Sơ tán khẩn cấp | 30 PP | Chỉ hiện trong cửa sổ cảnh báo của `vie_disaster.10` |
| Kêu gọi viện trợ quốc tế | 0 PP | +treasury nhỏ, `ax_integ +1`. Tăng phụ thuộc nhẹ |
| Duy trì ngân sách PCTT (bật/tắt) | −0.2 bn mỗi tháng | Chặn `VIE_resilience` giảm theo thời gian |

---

## 5. Cân bằng & kỹ thuật

- **Tổng R** từ toàn bộ focus khoảng 90–100, decision giúp duy trì. Capstone yêu cầu R > 59, tức cần khoảng 2/3 cây.
- **Biến:** thêm `VIE_resilience` vào `VIE_ax_init`, tooltip `VIE_resilience_tt`, dùng cùng mẫu `add_to_variable` + `tooltip`. Chặn trần bằng `clamp_variable` (0–100).
- **Treasury:** focus chi từ 5 bn trở lên phải có bankruptcy guard. Focus xây dựng dùng `one_state_*` (sửa T5 ở `storm_resilient_islands`: bỏ bunker, chỉ giữ naval_base kèm phí).
- **Filter:** `FOCUS_FILTER_STABILITY` + `FOCUS_FILTER_INFRASTRUCTURE` / `FOCUS_FILTER_ENVIRONMENT` / `FOCUS_FILTER_EXPENDITURE` cho đúng chuẩn MD (xem `search-filters.md`).
- **AI:** ưu tiên A, B, C (base 60–70). Cặp D và cặp F cho `VIE_ai_historical = yes` theo đúng lịch sử: D chọn NQ 120, F chọn crisis_response.

---

## 6. Thứ tự làm

| Bước | Nội dung | Ước lượng |
|---|---|---|
| 1 | Tách 8 focus thành root riêng, chuyển `mekong_climate_adaptation`, sửa T1 (xóa `vie_disaster.2`) và T5. Không đổi gameplay khác | nhỏ |
| 2 | Thêm `VIE_resilience` và `VIE_disaster_damage_effect`, nối 4 event hiện có vào effect này, dùng lại 3 cờ (T2–T3) | vừa |
| 3 | Thêm focus nhánh A, B, C (11 focus) | vừa |
| 4 | Thêm nhánh D, E (8 focus) | vừa |
| 5 | Thêm nhánh F, capstone, event 10–14, category decision | lớn |
| 6 | Loc VI, idea, layout, chạy `standardize_focus_tree.py` + validator, test trong game | vừa |

### Cần xác minh trước khi viết loc

- Số hiệu và năm: NĐ 94/2014 (Quỹ PCTT), tên gọi và thời điểm thành lập Ban Chỉ đạo Quốc gia PCTT, năm khánh thành cống Cái Lớn – Cái Bé, thời điểm triển khai cảnh báo qua di động trên toàn quốc.
- Mốc đổi tên root (2001 hay 2013) ảnh hưởng tới event `vie_disaster.1` (`date > 2013.9.1`).
