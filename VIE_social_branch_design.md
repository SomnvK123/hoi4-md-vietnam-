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
