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
