# Báo cáo Lục quân VIE — Trục 1, 2, 3

Sep 29, 2026 · @dfd

## Tóm tắt

Báo cáo gộp ba trục của lục quân VIE trong Millennium Dawn: Trục 1 (mua sắm) bằng event, Trục 2 (CNQP) bằng decision, Trục 3 (xây dựng lực lượng) bằng 30 focus và 6 decision Lục quân (mục VIII). Kịch bản lịch sử tốn 33.35bn treasury, trong đó 22.5bn là giá 3 nhà máy theo bảng chi phí của MD; Trục 3 không tốn treasury, chỉ tốn PP.

| Trục | Hình thức | Câu hỏi của trục | Đơn vị chi phí |
| --- | --- | --- | --- |
| 1. Mua sắm | 9 chuỗi event hợp đồng (6 lịch sử, 3 alt-history) | Việt Nam mua gì, từ ai, khi nào | Treasury (bn) |
| 2. CNQP Lục quân | 9 decision sản xuất trong nước, mở từ `VIE_tank_modernization` | Việt Nam tự sản xuất gì sau khi mua | Treasury (bn) |
| 3. Xây dựng lực lượng | 30 focus (người chơi đi 21–22), 6 decision Lục quân, 3 biến thể capstone | Việt Nam tổ chức, huấn luyện và sử dụng lực lượng vũ trang như thế nào | PP |

Trục 1 và 2 nối bằng 7 flag theo con đường lịch sử “mua hoặc mua license → tự sản xuất”. Trục 3 chỉ đặt cờ hướng lực lượng để chỉnh trọng số AI; không trục nào bị chặn bởi Trục 3 (mục IV).

## I. Trục 1: Mua sắm

Trục 1 thay focus `VIE_t90_tanks` bằng event, chuyển `VIE_rocket_artillery` sang Trục 2, và thêm 8 chuỗi hợp đồng khác. Kịch bản lịch sử tốn 3.10bn; chọn mọi option lớn nhất tốn 7.95bn.

### 1.1. Xử lý focus cũ

| Focus v7 | Xử lý | Lý do |
| --- | --- | --- |
| `VIE_t90_tanks` | → Event `vie_proc_army.14`–`.15` | Hợp đồng mua |
| `VIE_rocket_artillery` | → Decision D7 (Trục 2): hiện đại hóa BM-21 | Hàng nội địa; tên “ST-122” không có nguồn |
| `VIE_army_short_range_ad` | Giữ; là điều kiện của chuỗi Igla | Có xây AA building và tech. Trục 3 (#26) chỉ thêm modifier phối hợp |
| `VIE_mechanization`, `VIE_army_c4isr` | Giữ | Tổ chức, công nghệ, học thuyết. Trục 3 chỉ thêm modifier và cờ, không tạo mẫu hay cộng tech (mục 3.7) |

### 1.2. Quy ước giá

Treasury trong game (bn) = giá thực (tỷ USD) × K, với K = 5, làm tròn tới 0.05. Thiếu tiền không chặn hợp đồng: MD tự phát hành nợ.

### 1.3. Dữ kiện hợp đồng

| Hợp đồng | Đối tác | Thời gian | Số lượng | Giá thực | Nhãn |
| --- | --- | --- | --- | --- | --- |
| K9A1 Thunder | Hanwha (Hàn Quốc), G2G qua KOTRA | Đánh giá 02/2023, huấn luyện 11/2024, xác nhận 08/2025 | 20 | ≈ 250–276 triệu USD | Lịch sử |
| T-90S/SK | Nga | Ký 2016, công bố 07/2017, giao 12/2018 và 02/2019 | 64 (SK số ít), kèm xe cứu kéo BREM-1M | ≈ 250 triệu USD, vay tín dụng Nga | Lịch sử |
| License Galil ACE | IWI (Israel) | Sản xuất tại Z111 từ khoảng 2014 | — | Không công bố | Lịch sử |
| T-54M3 (mẫu thử) | Israel (nguồn ghi Elbit, IMI hoặc Rafael) | Đề nghị 2009, mẫu thử 2010; không đặt hàng loạt vì giá | 1 mẫu + bộ kit | Không công bố | Lịch sử |
| Igla (sản xuất trong nước) | Nga | Thỏa thuận 2009; Nga cấp linh kiện lắp ráp trước | Không công bố | ≈ 50 triệu USD (ước tính) | Lịch sử |
| T-72 | Ba Lan | Đồng ý 03/2005, hủy 2006 | 150 | Không công bố | Lịch sử, thất bại |
| T-54/55 | Phần Lan | 02/2005 | ≈ 70 | Không công bố | Lịch sử |
| BMP-3, TOS-1A, CAESAR | Nga, Nga, Pháp | — | — | — | Alt-history |

EXTRA (Israel) để ngoài trục này vì được dùng cho phòng thủ đảo.

### 1.4. Thiết kế event

Mọi event đặt `is_triggered_only = yes` và được đặt lịch qua ETD. Chuỗi 7–9 chỉ vào lịch khi bật rule `rule_vie_alt_procurement`.

Các event phụ thuộc focus, license hoặc ngoại giao (`.5`, `.8`, `.11`, `.14`, `.18`) có cửa sổ thời gian và thử lại, không nổ một lần duy nhất (mục 1.6).

#### Chuỗi 1: Xe tăng cũ châu Âu (2005–2006)

```
vie_proc_army.1  (ETD 2005)
  Tự động: Phần Lan chuyển giao ~70 T-54/55 → +70 T-54/55, −0.05bn
  ├─ A: Nhận lời Ba Lan: 150 T-72 cho huấn luyện, bảo dưỡng (lịch sử) → flag VIE_pl_t72_deal
  └─ B: Từ chối                                                      → đóng
vie_proc_army.2  (ETD 2006, nếu có VIE_pl_t72_deal)
  ├─ A: Hủy, dồn ngân sách cho hải quân và không quân (lịch sử) → +10 navy XP, +10 air XP; opinion POL −5
  └─ B: Giữ hợp đồng (alt-history)                              → −0.40bn (ước tính); +150 T-72, producer POL
```

#### Chuỗi 2: T-54M3, mẫu thử Israel (2009–2010)

```
vie_proc_army.5  (ETD 2009)
  Trigger: VIE_tank_modernization, ISR tồn tại
  ├─ A: Nhận mẫu thử và bộ kit, tự nâng cấp trong nước (lịch sử) → −0.05bn; flag VIE_t54m3_prototype (mở D5)
  ├─ B: Nâng cấp hàng loạt 100 xe theo gói Israel                  → −0.75bn (ước tính); không đặt flag VIE_t54m3_prototype (D5 khóa); .6 sau 1095 ngày
  └─ C: Không                                                       → đóng
vie_proc_army.6  (chỉ nhánh B): chuyển đổi 100 T-54/55 thành T-54M3; army_armor_defence_factor +2%
```

A rẻ nhưng chậm vì phải chạy D5. B nhanh nhưng đắt, đúng lý do VN từ chối gói Israel. B thay thế D5 chứ không đi cùng D5, nên không đặt cờ VIE\_t54m3\_prototype.

#### Chuỗi 3: Igla kèm quyền sản xuất (2009)

```
vie_proc_army.8  (ETD 2009)
  Trigger: VIE_army_short_range_ad, SOV tồn tại
  ├─ A: Mua kèm quyền sản xuất trong nước (lịch sử) → −0.35bn; flag VIE_igla_license (mở D9)
  ├─ B: Chỉ mua thành phẩm                          → −0.25bn
  └─ C: Không                                       → đóng
  A và B: enemy_army_bonus_air_superiority_factor −5%
```

#### Chuỗi 4: License Galil ACE (khoảng 2014)

```
vie_proc_army.11  (ETD 2013)
  Trigger: D1 đã xong, ISR tồn tại
  ├─ A: Ký license Galil ACE cho Z111 (lịch sử) → −0.10bn (ước tính); flag VIE_iwi_license (D2 còn 730 ngày)
  └─ B: Không                                   → D2 vẫn mở, 1095 ngày
```

#### Chuỗi 5: T-90S/SK (2016–2019)

```
vie_proc_army.14  (ETD 2016)
  Trigger: VIE_russian_arms_deals, SOV tồn tại, không chiến tranh với SOV
  ├─ A: 64 xe, vay tín dụng Nga (lịch sử) → nợ +1.25bn; giao 2 đợt 32 + 32 sau ~900 và ~960 ngày
  ├─ B: 128 xe                            → −2.50bn; giao sau ~900 và ~1270 ngày
  ├─ C: 32 xe                             → −0.65bn; giao 1 đợt sau ~900 ngày
  └─ D: Không mua                         → đóng
vie_proc_army.15  (giao hàng, lặp theo đợt)
  → T-90S: medium_tank_chassis_3 (NSB) / MBT_4 (non-NSB)
  → army_armor_attack_factor +5%, army_armor_defence_factor +3%; +10 army XP
  → set_country_flag = VIE_t90_purchased
```

T-90SK là bản chỉ huy, chỉ chiếm số ít, nên trong game dùng một loại equipment.

#### Chuỗi 6: K9A1 Thunder (2023–2025)

```
vie_proc_army.18  (ETD 2023; ETD 2021 nếu có VIE_155mm_study)
  Trigger: KOR tồn tại, không chiến tranh với KOR; opinion KOR chỉ chỉnh ai_chance (>75 cao, 25–75 bình thường, <25 thấp)
  ├─ A: Đánh giá (lịch sử: 02/2023) → .19 sau 900 ngày ≈ 08/2025 (365 nếu có VIE_155mm_study)
  └─ B: Không quan tâm              → đóng
vie_proc_army.19
  ├─ A: Mua 20 xe (lịch sử) → −1.30bn
  ├─ B: Mua 40 xe           → −2.60bn
  └─ C: Không mua           → đóng
vie_proc_army.20  (sau 365 ngày): giao hàng → K9A1, flag VIE_k9_purchased
vie_proc_army.21  (sau 365 ngày)
  ├─ A: Nội địa hóa bảo dưỡng và đạn → mở D8
  ├─ B: Mua đạn dẫn đường            → −0.25bn, army_artillery_attack_factor +5%
  └─ C: Giữ nguyên                   → không đổi
```

#### Chuỗi 7: BMP-3 (alt-history)

```
vie_proc_army.30  (ETD 2010)
  Trigger: rule bật, SOV tồn tại
  ├─ A: Nhận xe thử nghiệm → −0.05bn
  └─ B: Không nhận         → đóng
vie_proc_army.31  (sau 180 ngày): báo cáo — đắt so với ngân sách, phức tạp, nặng cho địa hình
vie_proc_army.32  (sau 30 ngày)
  ├─ A: Không mua, rút kinh nghiệm → +10 army XP, opinion SOV −5 (nếu SOV còn tồn tại), flag VIE_bmp3_lessons (D6 còn 1095 ngày)
  └─ B: Mua 1 tiểu đoàn (~30 xe)   → −0.50bn (ước tính); 30 BMP-3 (medium_tank_flame_chassis_2 / IFV_3)
```

#### Chuỗi 8: TOS-1A (alt-history)

```
vie_proc_army.35  (ETD 2016)
  Trigger: rule bật, SOV tồn tại
  ├─ A: Biên chế 12 xe → −0.40bn (ước tính); 12 MLRS hạng nặng; +10 army XP
  └─ B: Không          → +5 army XP
```

#### Chuỗi 9: CAESAR (alt-history)

```
vie_proc_army.38  (ETD 2015)
  Trigger: rule bật, FRA tồn tại
  ├─ A: Đàm phán       → .39 sau 180 ngày
  └─ B: Không quan tâm → đóng
vie_proc_army.39: giá cao, điều kiện chuyển giao khắt khe, chuẩn 155mm khác hệ 122/130/152mm
vie_proc_army.40  (sau 365 ngày): không ký được → opinion FRA −5 (nếu FRA còn tồn tại); flag VIE_155mm_study
```

### 1.5. Tổng kết Trục 1

| # | Chuỗi | ID | Nhãn | Số lựa chọn | Treasury (bn, K = 5) |
| --- | --- | --- | --- | --- | --- |
| 1 | Xe tăng cũ châu Âu | .1–.2 | Lịch sử | 2 + 2 | 0.05 (+0.40 nếu giữ T-72) |
| 2 | T-54M3 | .5–.6 | Lịch sử | 3 | 0.05 / 0.75 |
| 3 | Igla | .8 | Lịch sử | 3 | 0.35 / 0.25 |
| 4 | Galil ACE | .11 | Lịch sử | 2 | 0.10 |
| 5 | T-90S/SK | .14–.15 | Lịch sử | 4 | 1.25 (nợ) / 2.50 / 0.65 |
| 6 | K9A1 | .18–.21 | Lịch sử | 2 + 3 + 3 | 1.30 / 2.60 (+0.25) |
| 7 | BMP-3 | .30–.32 | Alt-history | 2 + 2 | 0.05 (+0.50 nếu mua) |
| 8 | TOS-1A | .35 | Alt-history | 2 | 0.40 |
| 9 | CAESAR | .38–.40 | Alt-history | 2 | 0 |
|  | **Tổng** |  |  | **32** | **3.10 (lịch sử) / 7.95 (tối đa)** |

### 1.6. Cửa sổ thời gian và thử lại cho event ETD

Event ETD chỉ nổ một lần: nếu tới ngày mà điều kiện chưa đạt thì chuỗi mất. Năm chuỗi phụ thuộc focus, license hoặc ngoại giao được đổi thành cửa sổ thời gian: ETD là lần thử đầu, sau đó thử lại tới hết cửa sổ. `.1`, `.2` và chuỗi 7–9 không cần cửa sổ vì điều kiện không phụ thuộc thao tác của người chơi.

| Event | Điều kiện | Cửa sổ | Gọi thêm từ | Hệ quả nếu hết cửa sổ |
| --- | --- | --- | --- | --- |
| `.5` | `VIE_tank_modernization`, ISR tồn tại | 2009–2012 | Hoàn tất `VIE_tank_modernization` | D5 khóa (thiếu `VIE_t54m3_prototype`) |
| `.8` | `VIE_army_short_range_ad`, SOV tồn tại | 2009–2013 | Hoàn tất `VIE_army_short_range_ad` | D9 khóa (thiếu `VIE_igla_license`) |
| `.11` | D1 đã xong, ISR tồn tại | 2013–2015 | Hoàn tất D1 | D2 vẫn mở, 1095 ngày |
| `.14` | `VIE_russian_arms_deals`, SOV tồn tại, không chiến tranh với SOV | 2016–2018 | Hoàn tất `VIE_russian_arms_deals` | Mất T-90; `vie_def_ind.2` không nổ |
| `.18` | KOR tồn tại, không chiến tranh với KOR | 2023–2026 (từ 2021 nếu có `VIE_155mm_study`) | Chỉ thử lại mỗi 90 ngày | Mất K9; D8 khóa |

Quy tắc:

- Điều kiện đặt trong scripted effect `VIE_try_proc_N`, không dựa vào `trigger` của event để chặn (chưa xác minh `trigger` có chặn event nhận qua `country_event` hay không). Event vẫn giữ `trigger` giống hệt để hai chỗ không lệch.
- Cờ `VIE_proc_N_fired` đặt trong `VIE_try_proc_N` ngay khi gọi event, để không nổ đôi.
- Lần thử đầu gọi từ ETD năm gốc; chuỗi chờ focus hoặc D1 gọi thêm từ phần thưởng hoàn tất của focus hoặc decision đó. Không thử trước ngày mở cửa sổ.
- Chưa đạt thì hẹn thử lại sau 90 ngày bằng event ẩn (`.90`–`.94`, mỗi chuỗi một event) cho tới hết cửa sổ. Hết cửa sổ mà chưa nổ thì chuỗi mất và hệ quả theo bảng.
- Event nổ muộn thì các mốc sau dời theo; ví dụ T-90 nổ năm 2018 thì giao khoảng 2020.

Mẫu cho `.5`; các chuỗi khác đổi điều kiện, cửa sổ và ID:

```
VIE_try_proc_5 = {
	if = {
		limit = { NOT = { has_country_flag = VIE_proc_5_fired } date > 2008.12.31 }
		if = {
			limit = { has_completed_focus = VIE_tank_modernization country_exists = ISR }
			set_country_flag = VIE_proc_5_fired
			country_event = { id = vie_proc_army.5 days = 1 }
		}
		else_if = {
			limit = { date < 2013.1.1 }
			country_event = { id = vie_proc_army.90 days = 90 }
		}
	}
}
```

`vie_proc_army.90` là event ẩn (`hidden = yes`, `is_triggered_only = yes`) chỉ gọi lại `VIE_try_proc_5 = yes` trong `immediate`.

## II. Trục 2: CNQP Lục quân

Trục 2 có 9 decision (8 cố định, D8 có điều kiện), mỗi decision gắn một sản phẩm có thật. 8 decision cố định xong sớm nhất 01/2025 và tốn 30.25bn, trong đó 22.5bn là giá 3 nhà máy.

### 2.1. Xử lý focus cũ

| Focus v7 | Xử lý | Ghi chú |
| --- | --- | --- |
| `VIE_z_factories` | → Decision D1 | Bỏ “Z189” (xưởng đóng tàu) khỏi tên |
| `VIE_licensed_rifles` | → Decision D2 | Gắn Z111 và license IWI |
| `VIE_def_industry_law` | Giữ, đổi tên thành Pháp lệnh CNQP (02/2008/PL-UBTVQH12) | `available = { date > 2008.6.30 }`; không còn là cổng mở; +1 level. Mốc theo ngày hiệu lực 01/07/2008, không theo ngày ký 26/01/2008 |
| `VIE_military_enterprises_core` / `_divest` | Giữ | Ngã rẽ loại trừ nhau, điều kiện ở 2.4 |
| `VIE_path_self_reliant_deterrence` | Giữ | Capstone, điều kiện ở 2.4 |

`VIE_missile_program` và `VIE_def_research_partnership` là nội dung liên quân chủng, giữ nguyên và không thuộc báo cáo này.

### 2.2. Decision CNQP Lục quân

Nhóm decision “CNQP Lục quân” hiện khi hoàn tất `VIE_tank_modernization`. Bảng này là nguồn duy nhất cho điều kiện và phần thưởng.

| ID | Tên (sản phẩm thật) | Yêu cầu | Mở từ | Thời gian (ngày) | Chi phí chương trình | Xây dựng (MD) | Hoàn tất (`remove_effect`) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D1 | Hiện đại hóa nhà máy Z lục quân | — | 2008.7.1 (Pháp lệnh CNQP có hiệu lực) | 1095 | 0 | 2 nhà máy = 15.0bn, trừ trực tiếp | Tech +30%/+50% `CAT_artillery`, `CAT_inf_wep`, `CAT_art_ammo`; MIO GDT +2 size, +500 funds, +2 trait |
| D2 | Súng STV (Z111) | D1 | 2017.1.1 | 730 nếu có `VIE_iwi_license`, 1095 nếu không | 0.5bn | 1 nhà máy = 7.5bn, trừ trực tiếp | 3,000 súng bộ binh; +100% `CAT_inf_wep`; MIO GDT +1 size, +250 funds, +1 trait |
| D3 | Pháo tự hành bánh lốp dòng PTH (Z751, VDI) | D1 | 2013.1.1 | 1460 | 2.0bn | — | 24 pháo tự hành (`medium_tank_artillery_chassis` / `SP_arty`); MIO GDT +1 size, +250 funds |
| D4 | Đạn pháo nội địa (122/130/152mm) | D3 | — | 730 | 1.0bn | — | `attrition` −10%; MIO GDT +1 size, +100 funds |
| D5 | T-54M nội địa (Z153; FCS Indra, ERA trong nước) | D1 + `VIE_t54m3_prototype` | 2012.1.1 | 1095 | 0.25bn | — | Chuyển đổi 100 T-54/55 thành T-54M; `army_armor_defence_factor` +2%; MIO GDT +1 size, +200 funds |
| D6 | Xe chiến đấu bộ binh XCB-01 | D1 | 2021.1.1 | 1460 (1095 nếu có `VIE_bmp3_lessons`) | 3.0bn | — | 50 XCB-01 (`medium_tank_flame_chassis_4` / `IFV_5`); `mechanized_attack_factor` +5%; flame chassis −5% build cost |
| D7 | Hiện đại hóa BM-21, đạn rocket 122mm | D1 | — | 730 | 0.5bn | — | Chuyển đổi 36 BM-21 sang bản số hóa (`medium_tank_rocket_chassis_1` / `SP_R_arty_1`); `army_artillery_attack_factor` +5%; +10 army XP; MIO GDT +1 size, +150 funds |
| D9 | Tên lửa vác vai TL-01 (Z131) | D1 + `VIE_igla_license` | 2017.1.1 | 730 | 0.5bn | — | `enemy_army_bonus_air_superiority_factor` −3%; MIO GDT +1 size, +100 funds |
| D8 | Nội địa hóa bảo dưỡng và đạn K9 | D3 + `VIE_k9_purchased` + chọn `.21` A | — | 730 | 0.5bn | — | +50% `CAT_artillery`; MIO GDT +1 size, +150 funds |

D1–D7 và D9 mỗi cái cộng +1 `VIE_def_industry_level`; D8 không cộng. Chi phí chương trình là số cân bằng, trừ D5 (100 × 0.5 triệu USD × K). Giá nhà máy (7.5bn mỗi nhà máy, theo bảng chi phí của MD) trừ trực tiếp bằng `modify_treasury_effect` khi bấm decision; nhà máy xây bằng `add_building_construction` (mục 6.2).

### 2.3. Event Trục 2

| ID | Tên | Trigger | Hiệu ứng |
| --- | --- | --- | --- |
| `vie_def_ind.1` | Triển lãm Quốc phòng quốc tế Việt Nam | ETD tháng 12 các năm 2022, 2024 và mỗi 2 năm sau đó; level ≥ 2 | MIO GDT +100 funds; +10 opinion với 2 đối tác đã mua hàng |
| `vie_def_ind.2` | Chuyển giao bảo dưỡng T-90 | `VIE_t90_purchased`, D1 đã xong | MIO GDT +150 funds; +10 army XP |
| `vie_def_ind.3` | Xuất khẩu vũ khí | Level ≥ 6, sau 2022 | +0.25bn mỗi năm; +opinion ASEAN |
| `vie_def_ind.4` | Quốc hội thông qua Luật 38/2024/QH15 | ETD 2024.6.27; đã có `VIE_def_industry_law` | Cả 4 MIO +150 funds |

### 2.4. Biến `VIE_def_industry_level` và điều kiện mở khóa

| Nguồn | Tăng |
| --- | --- |
| D1–D7, D9 (mỗi decision) | +1, tổng +8 |
| Pháp lệnh CNQP | +1 |
| Ngã rẽ Core / Divest | +2 / +1 |
| **Tối đa** | **11 (Core) hoặc 10 (Divest)** |

| Mở khóa | Điều kiện |
| --- | --- |
| Ngã rẽ Core / Divest | Level ≥ 4 |
| Capstone `path_self_reliant_deterrence` | Đã chọn ngã rẽ, level ≥ 8, Four Nos hoặc Non-alignment |
| Triển lãm | Level ≥ 2 |
| Xuất khẩu | Level ≥ 6 |

Capstone đạt được bằng cả hai ngã rẽ: Core cần Pháp lệnh + 5 decision, Divest cần Pháp lệnh + 6 decision.

Capstone đạt sớm nhất khoảng 01/2019: Core = Pháp lệnh 1 + D1, D7, D5, D3, D2 (5 decision) + Core 2 = 8; Divest = Pháp lệnh 1 + 6 decision (thêm D9) + Divest 1 = 8. Điều kiện giữ nguyên: capstone là ngưỡng đạt tự chủ, không phải CNQP đã hoàn thiện; D6 và K9 là các mốc phát triển sau đó.

### 2.5. Thời gian

| Decision | Bắt đầu sớm nhất (lịch sử) | Hoàn tất sớm nhất (lịch sử) | Thực tế = max của | Giới hạn bởi |
| --- | --- | --- | --- | --- |
| D1 | 07/2008 | 07/2011 | 2008.7.1, xong `VIE_tank_modernization`, staffing, slot nhà máy | Ngày mở |
| D7 | 07/2011 | 07/2013 | D1 xong | D1 |
| D5 | 01/2012 | 01/2015 | 2012.1.1, D1 xong, `VIE_t54m3_prototype` (chỉ từ `.5` A) | Ngày mở; cần mẫu thử T-54M3 (2009) |
| D3 | 01/2013 | 01/2017 | 2013.1.1, D1 xong | Ngày mở |
| D4 | 01/2017 | 01/2019 | D3 xong | D3 |
| D2 | 01/2017 | 01/2019 (01/2020 nếu không có license IWI) | 2017.1.1, D1 xong | Ngày mở |
| D9 | 01/2017 | 01/2019 | 2017.1.1, D1 xong, `VIE_igla_license` | Ngày mở |
| D6 | 01/2021 | 01/2025 (01/2024 nếu có `VIE_bmp3_lessons`) | 2021.1.1, D1 xong | Ngày mở |
| D8, nhánh chuẩn | khoảng 2027 | khoảng 2029 | D3 xong, `.21` A (`.18` 2023 → `.19` +900 ngày → `.20` +365 → `.21` +365) | Chuỗi K9 |
| D8, nhánh `VIE_155mm_study` | khoảng 2024 | khoảng 2026 | Như trên, `.18` từ 2021 và mỗi bước 365 ngày | Chuỗi K9 và chuỗi CAESAR (alt-history) |

Chạy tuần tự 8 decision cố định mất 22 năm. Các mốc hoàn tất khớp lịch sử: PTH khoảng 2017, STV và TL-01 năm 2019, XCB-01 năm 2025. Cột “Thực tế” là mốc dùng khi code: mọi decision đều cần D1, nên D1 trễ thì cả chuỗi trễ theo; mốc D8 còn dời muộn hơn nếu .18 nổ ở cuối cửa sổ (mục 1.6).

## III. Trục 3: Xây dựng lực lượng (bản cũ, chỉ để đối chiếu; bản chính là mục VIII)

Trục 3 có 32 focus (người chơi đi 18), 11 decision và 3 biến thể capstone; câu hỏi của trục là Việt Nam tổ chức, huấn luyện và sử dụng lực lượng vũ trang như thế nào. Tag `VIE`.

Nhãn dữ kiện: `[THẬT]` đã có nguồn công khai; `[ĐỀ XUẤT]` thiết kế của mod, chưa xác minh là thực thể có thật; `[ALT-HISTORY]` hướng rẽ giả định. Mọi con số ở mục 3.4–3.8 là mốc balance chốt bằng hệ điểm ở 3.4, không phải dữ kiện lịch sử.

### 3.1. Kiến trúc và cost

```
cai_cach_quan_doi (root)
      ├── hop_nhat_hau_can_ky_thuat ──┐
      └── chi_huy_tac_chien_hiep_dong ┤  (cần cả hai)
                                      ▼
        ┌──────────── CHỌN 1 (ME 3 chiều) ────────────┐
        A. Cân bằng     B. Cơ động     C. Toàn dân
        (5 focus)       (5 focus)      (5 focus)
        └──────────────────┬──────────────────────────┘
                           ▼  (OR: node cuối của A/B/C)
                    san_sang_tac_chien
                           ▼  (chọn 2 trong 3, giới hạn ở gốc)
     Biên giới & Đô thị │ Biển & Trời │ Mạng & Điện tử   (3 × 4 focus)
                           ▼  (cần ≥ 2 node cuối)
             luc_luong_vu_trang_hoan_chinh (capstone)
```

Trong HOI4, `cost = N` mặc định nghĩa là N tuần (N × 7 ngày).

| Đoạn | Số focus | Người chơi đi | Cost trên đường đi (tuần) |
| --- | --- | --- | --- |
| Nền tảng (gồm root) | 3 | 3 | 13 + 7 + 7 = 27 |
| Doctrine | 15 | 5 | 10 + 7 × 4 = 38 |
| Sẵn sàng tác chiến | 1 | 1 | 7 |
| Năng lực (2 lĩnh vực × 4 focus) | 12 | 8 | 2 × (10 + 7 + 7 + 7) = 62 |
| Capstone | 1 | 1 | 13 |
| **Tổng** | **32** | **18** | **147 tuần (1 029 ngày)** |

Lĩnh vực sở trường giảm 2 tuần cho gốc, nên chọn đúng sở trường thì tổng còn 145 tuần (1 015 ngày), khoảng 2,8 năm.

### 3.2. Bảng focus và prerequisite

Cost là mốc (tuần): root 13, gốc doctrine và gốc lĩnh vực 10, còn lại 7, capstone 13. Bố cục cây: nhóm nền vật chất (các focus giữ lại của Trục 1 và các focus CNQP giữ lại của Trục 2) đặt ở nhánh trên hoặc trái, Trục 3 đặt ở nhánh riêng, cả hai cùng treo dưới VIE\_modernize\_vpa. Đây chỉ là sắp xếp vị trí, không thêm prerequisite chéo; Trục 3 không phụ thuộc ngã rẽ Core/Divest hay capstone của Trục 2 (mục 3.7).

| # | ID | Tên hiển thị | Cost | Prerequisite | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 1 | `VIE_cai_cach_quan_doi` | Cải cách quân đội, tinh gọn biên chế | 13 | `VIE_modernize_vpa` | Root. `[THẬT]` Nghị quyết 05-NQ/TW về điều chỉnh tổ chức, biên chế quân đội, ghi kèm Nghị quyết 230-NQ/QUTW. Không khóa mốc năm (mục 3.10) |
| 2 | `VIE_hop_nhat_hau_can_ky_thuat` | Hợp nhất Hậu cần – Kỹ thuật | 7 | #1 | `[THẬT]` Quyết định 366/QĐ-BQP (24/1/2025), công bố 5/2/2025 |
| 3 | `VIE_chi_huy_tac_chien_hiep_dong` | Hiện đại hóa chỉ huy tác chiến hiệp đồng | 7 | #1 | `[THẬT]` nền là Bộ Tổng Tham mưu / Cục Tác chiến; `[ĐỀ XUẤT]` cơ chế hiệp đồng liên quân chủng (mục 3.10) |
|  | **Doctrine A — Quân đội cân bằng** |  |  |  |  |
| 4 | `VIE_quan_doi_can_bang` | Quân đội chính quy cân bằng | 10 | #2 AND #3 | ME với #9, #14. Đặt cờ `VIE_doctrine_balanced`; áp cái giá của A |
| 5 | `VIE_hiep_dong_binh_chung` | Hiệp đồng binh chủng | 7 | #4 | +1 `VIE_combined_arms_level` |
| 6 | `VIE_to_chuc_co_gioi_tung_buoc` | Tổ chức cơ giới hóa từng bước | 7 | #4 | Chỉ modifier tổ chức. Mẫu sư đoàn cơ giới và trang bị thuộc `VIE_mechanization` (Trục 1) |
| 7 | `VIE_hoa_luc_chi_vien_hiep_dong` | Hỏa lực chi viện hiệp đồng | 7 | #5 | Tổ chức pháo binh trong hiệp đồng |
| 8 | `VIE_he_thong_phong_ngu_khu_vuc` | Hệ thống phòng thủ khu vực | 7 | #6 AND #7 | Node cuối A; +1 `VIE_combined_arms_level` |
|  | **Doctrine B — Cơ động và phản ứng nhanh** |  |  |  |  |
| 9 | `VIE_luc_luong_phan_ung_nhanh` | Lực lượng phản ứng nhanh | 10 | #2 AND #3 | ME với #4, #14. Đặt cờ `VIE_doctrine_mobile`; áp cái giá của B |
| 10 | `VIE_thanh_lap_quan_doan_co_dong` | Thành lập cụm/quân đoàn cơ động | 7 | #9 | `[ALT-HISTORY]`. Được tạo mẫu mới (cụm cơ động), vì Trục 1 chưa có mẫu này |
| 11 | `VIE_huan_luyen_co_dong_cao` | Huấn luyện cơ động cao | 7 | #9 | Node giữa của B; chỉ modifier |
| 12 | `VIE_hiep_dong_co_dong_da_quan_chung` | Cơ động hiệp đồng đa quân chủng | 7 | #10 | Vận tải đường không, đổ bộ đường biển ở mức tổ chức |
| 13 | `VIE_danh_nhanh_thang_nhanh` | Đánh nhanh, thắng nhanh | 7 | #11 AND #12 | Node cuối B |
|  | **Doctrine C — Chiến tranh nhân dân và chiều sâu** |  |  |  |  |
| 14 | `VIE_phong_thu_chieu_sau` | Phòng thủ chiều sâu | 10 | #2 AND #3 | ME với #4, #9. Đặt cờ `VIE_doctrine_peoples`; áp cái giá của C. Thay focus People's War của v7 |
| 15 | `VIE_dan_quan_tu_ve_toan_dan` | Dân quân tự vệ toàn dân | 7 | #14 | Được tạo mẫu mới (dân quân) |
| 16 | `VIE_nguy_trang_phan_tan` | Ngụy trang và phân tán | 7 | #14 |  |
| 17 | `VIE_cong_su_dia_dao` | Công sự, địa đạo vững chắc | 7 | #15 |  |
| 18 | `VIE_phan_cong_tai_cho` | Phân cấp tác chiến tại chỗ | 7 | #16 AND #17 | Node cuối C |
|  | **Sẵn sàng tác chiến** |  |  |  |  |
| 19 | `VIE_san_sang_tac_chien` | Sẵn sàng tác chiến | 7 | #8 OR #13 OR #18 | Đặt `VIE_capability_count = 0`, `VIE_capability_done = 0`, `VIE_readiness_active`; mở decision (mục 3.6) |
|  | **Lĩnh vực 1 — Biên giới và Đô thị** |  |  |  |  |
| 20 | `VIE_tac_chien_bien_gioi_do_thi` | Tác chiến biên giới và đô thị | 10 | #19 | `available`: `VIE_capability_count < 2`. Hoàn thành: `VIE_capability_count += 1` |
| 21 | `VIE_trinh_sat_canh_gioi` | Trinh sát, cảnh giới biên giới | 7 | #20 | Không có điều kiện count |
| 22 | `VIE_chien_dau_do_thi` | Chiến đấu trong đô thị | 7 | #20 | Không có điều kiện count |
| 23 | `VIE_khong_che_dia_ban` | Khống chế địa bàn | 7 | #21 AND #22 | Node cuối; `VIE_capability_done += 1`; đặt `VIE_capability_land` |
|  | **Lĩnh vực 2 — Biển và Trời** |  |  |  |  |
| 24 | `VIE_phong_thu_bien_troi` | Phòng thủ biển và bầu trời | 10 | #19 | `available`: `VIE_capability_count < 2`. Hoàn thành: `VIE_capability_count += 1` |
| 25 | `VIE_phong_thu_bo_bien` | Phòng thủ bờ biển, chống đổ bộ | 7 | #24 | Không có điều kiện count |
| 26 | `VIE_phong_khong_khong_quan` | Phòng không – Không quân hiệp đồng | 7 | #24 | `[THẬT]` xem mục 3.10. Chỉ modifier phối hợp; AA building và tech thuộc `VIE_army_short_range_ad` (Trục 1) |
| 27 | `VIE_bao_ve_bien_dao` | Bảo vệ biển đảo tổng hợp | 7 | #25 AND #26 | Node cuối; `VIE_capability_done += 1`; đặt `VIE_capability_seaair` |
|  | **Lĩnh vực 3 — Mạng và Điện tử** |  |  |  |  |
| 28 | `VIE_tac_chien_mang_dien_tu` | Tác chiến mạng và điện tử | 10 | #19 | `available`: `VIE_capability_count < 2`. Hoàn thành: `VIE_capability_count += 1` |
| 29 | `VIE_chi_huy_so` | Chỉ huy số hiệp đồng | 7 | #28 | Không cộng planning và recon: hai modifier đó thuộc `VIE_army_c4isr` (Trục 1). Không có điều kiện count |
| 30 | `VIE_chien_tranh_thong_tin` | Chiến tranh thông tin | 7 | #28 | Không có điều kiện count |
| 31 | `VIE_tac_chien_da_mien` | Tác chiến đa miền | 7 | #29 AND #30 | Node cuối; `VIE_capability_done += 1`; đặt `VIE_capability_cyber` |
|  | **Capstone** |  |  |  |  |
| 32 | `VIE_luc_luong_vu_trang_hoan_chinh` | Hoàn thiện lực lượng vũ trang | 13 | `VIE_capability_done >= 2` | 3 biến thể (mục 3.8). Điều kiện này đã kéo theo #19 nên không cần ghi thêm |

### 3.3. Cơ chế giới hạn 2/3

- **Chỉ ba gốc có điều kiện.** `available = { check_variable = { VIE_capability_count < 2 } }` đặt ở #20, #24, #28 và không đặt ở node giữa hay node cuối; hai loại node đó đã bị chặn bởi prerequisite. Nếu node giữa cũng đòi `count < 2`, khi hai gốc xong thì node giữa của chính hai lĩnh vực đã chọn bị khóa, `VIE_capability_done` không đạt 2 và capstone không mở được.
- **`cancel_if_invalid` là chốt chặn.** Mặc định là `yes` (MD bỏ dòng này vì là mặc định). Khi chạy nhiều slot và `count` chạm 2, gốc thứ ba đang chạy tự bị hủy. Nếu tắt cơ chế này, 29,5% lượt hai slot hoàn thành cả ba gốc (mục 3.9).
- **Bảo hiểm.** Phần thưởng node cuối chỉ cộng `VIE_capability_done` nếu giá trị đang nhỏ hơn 2. Từ 3 slot trở lên, ba gốc có thể bắt đầu cùng ngày khi `count` còn bằng 0 và cùng hoàn thành; capstone vẫn đúng nhưng lĩnh vực thứ ba không cho thưởng.
- **Không dùng ME ở node cuối.** ME chỉ cho hoàn thành một node, trong khi capstone cần hai.

### 3.4. Doctrine: mechanic, cái giá, điểm yếu

Ba doctrine có ròng 11,2 · 11,2 · 11,4 điểm, lệch nhau tối đa 0,2. Doctrine B có hiệu ứng dương cao hơn vì phải trả cái giá lớn hơn.

|  | A. Cân bằng | B. Cơ động | C. Toàn dân |
| --- | --- | --- | --- |
| Mechanic | Biến nội bộ `VIE_combined_arms_level` 0–3: +1 ở #5, +1 ở #8, capstone đặt mức 3. Chỉ dùng trong Trục 3 | Mở mẫu cụm cơ động (#10) | Mở mẫu dân quân (#15). Thay focus People's War của v7 |
| Điểm mạnh | Ổn định, ít rủi ro theo mọi hướng | Phản ứng nhanh, hiệu quả cao trên mỗi đơn vị | Nhân lực và phòng thủ lãnh thổ rất mạnh |
| Cái giá (áp ở gốc doctrine, gồm mọi hiệu ứng âm) | Chi phí duy trì +5%, −3% XP lục quân (−8,0) | −5% max manpower, chi phí sản xuất +5%, −10% dig-in (−13,0) | −5% tấn công, −5% tốc độ (−8,0) |
| Điểm yếu (hệ quả của cái giá, không thêm modifier) | Không có đỉnh nổi bật | Chịu tổn thất kém khi phải phòng ngự, do dig-in thấp | Khó tác chiến ra ngoài lãnh thổ, do phạt tấn công và tốc độ |
| Tổng hiệu ứng (5 node) | +7% org, +6% hậu cần, +4% phòng thủ, +4% tốc độ, +3% tấn công | +19% tốc độ, +10% org, +3% tấn công, +6% hậu cần | +14% max manpower, +18% dig-in, +2% phòng thủ |
| Lĩnh vực sở trường | Biển & Trời | Mạng & Điện tử | Biên giới & Đô thị |

Ánh xạ modifier của cái giá: “chi phí duy trì” của A dùng modifier tiền của MD (`army_personnel_cost_multiplier_modifier` hoặc `equipment_cost_multiplier_modifier`), không dùng modifier vanilla; “chi phí sản xuất” của B dùng modifier sản xuất của vanilla.

#### Hệ điểm balance

Mỗi hiệu ứng quy ra điểm; hiệu ứng âm dùng cùng hệ số với dấu trừ. Nếu đổi hệ số, chỉ cần tính lại bảng. Tốc độ kế hoạch không có hệ số vì Trục 3 không dùng planning.

| Hiệu ứng | Điểm / +1% |
| --- | --- |
| Tấn công | 1,2 |
| Tổ chức (org), phòng thủ, XP | 1,0 |
| Max manpower | 0,6 |
| Hiệu quả hậu cần, dig-in | 0,5 |
| Tốc độ | 0,4 |
| Chi phí duy trì, chi phí sản xuất (tăng) | −1,0 |

| Doctrine | Node → hiệu ứng (điểm) | Tổng gộp | Cái giá | **Ròng** |
| --- | --- | --- | --- | --- |
| A | #4 +3% org (3,0) · #5 +2% org, +3% hậu cần (3,5) · #6 +4% tốc độ, +2% phòng thủ (3,6) · #7 +3% tấn công (3,6) · #8 +2% org, +3% hậu cần, +2% phòng thủ (5,5) | 19,2 | −8,0 | **11,2** |
| B | #9 +5% tốc độ (2,0) · #10 +8% tốc độ, +3% org (6,2) · #11 +4% org (4,0) · #12 +3% tấn công, +6% hậu cần (6,6) · #13 +6% tốc độ, +3% org (5,4) | 24,2 | −13,0 | **11,2** |
| C | #14 +8% manpower (4,8) · #15 +6% manpower (3,6) · #16 +10% dig-in (5,0) · #17 +8% dig-in (4,0) · #18 +2% phòng thủ (2,0) | 19,4 | −8,0 | **11,4** |

Chi tiết cái giá: A = +5% duy trì (−5,0) + −3% XP (−3,0). B = −5% manpower (−3,0) + 5% chi phí sản xuất (−5,0) + −10% dig-in (−5,0). C = −5% tấn công (−6,0) + −5% tốc độ (−2,0).

### 3.5. Năng lực

Mỗi lĩnh vực có 15 điểm: gốc 3, hai node giữa 3 mỗi node, node cuối 6; hiệu ứng từng node chọn theo cờ doctrine (`VIE_doctrine_balanced / mobile / peoples`). Lĩnh vực sở trường của doctrine giảm 2 tuần cost ở gốc và nhân ×1,5 mọi con số của node cuối (6 thành 9), nên được 18 điểm. Đi hai lĩnh vực được 30 điểm, thêm 3 nếu có sở trường; con số này lớn hơn doctrine (khoảng 20 điểm gộp) vì người chơi đi 8 focus thay vì 5. Vì chỉ được chọn 2 trong 3, người chơi phải cân nhắc giữa theo sở trường và bù điểm yếu.

| Node | Điểm | A. Cân bằng | B. Cơ động | C. Toàn dân |
| --- | --- | --- | --- | --- |
| **Biên giới & Đô thị** |  |  |  |  |
| #20 gốc | 3 | +3% phòng thủ | +5% tốc độ, +1% phòng thủ | +4% dig-in, +1% phòng thủ |
| #21 | 3 | +2% org, +2% dig-in | +5% tốc độ, +1% org | +6% dig-in |
| #22 | 3 | +2% phòng thủ, +2% hậu cần | +2% tấn công, +1% manpower | +3% phòng thủ |
| #23 cuối | 6 | +3% org, +3% phòng thủ | +3% tấn công, +6% tốc độ | +8% dig-in, +2% phòng thủ |
| **Biển & Trời** |  |  |  |  |
| #24 gốc | 3 | +3% org | +5% tốc độ, +1% org | +3% phòng thủ |
| #25 | 3 | +2% phòng thủ, +2% hậu cần | +2% tấn công, +1% manpower | +4% dig-in, +1% phòng thủ |
| #26 | 3 | +2% org, +2% hậu cần | +5% tốc độ, +1% org | +3% phòng thủ |
| #27 cuối | 6 | +3% org, +3% phòng thủ | +3% tấn công, +6% tốc độ | +4% phòng thủ, +4% dig-in |
| **Mạng & Điện tử** |  |  |  |  |
| #28 gốc | 3 | +3% org | +5% tốc độ, +1% org | +6% dig-in |
| #29 | 3 | +2% org, +2% hậu cần | +5% tốc độ, +1% org | +2% phòng thủ, +2% dig-in |
| #30 | 3 | +2% phòng thủ, +2% hậu cần | +2% tấn công, +1% manpower | +3% phòng thủ |
| #31 cuối | 6 | +3% org, +3% phòng thủ | +3% tấn công, +6% tốc độ | +4% phòng thủ, +4% dig-in |

Biên giới & Đô thị và Mạng & Điện tử dùng modifier lục quân (Mạng & Điện tử chỉ dùng org, hậu cần, tốc độ, phòng thủ, dig-in); Biển & Trời dùng modifier hải quân, không quân hoặc phòng thủ duyên hải tương ứng. Tên modifier cụ thể tra khi code. Biển & Trời chỉ ở mức tổ chức và học thuyết sử dụng; nếu sau này có trục riêng cho Hải quân hoặc Không quân, #24–#27 cần chuyển sang đó hoặc đánh dấu liên quân chủng (mục VII).

### 3.6. Sẵn sàng tác chiến và decision

`VIE_san_sang_tac_chien` (#19) đặt cờ `VIE_readiness_active` và mở category decision `VIE_readiness_decisions`. Tối đa 2 chương trình chạy song song; mỗi decision có cooldown (`days_re_enable`, tính từ lúc kết thúc); chi phí giảm 30% khi trùng lĩnh vực sở trường.

Decision Trục 3 chỉ tốn PP, không tốn treasury. PP và treasury là hai loại tiền riêng nên không quy đổi: Trục 1 và 2 là mua sắm và xây dựng nên tính bằng treasury (bn), Trục 3 là huấn luyện, diễn tập, động viên nên tính bằng PP. Chi phí = k × thu nhập PP hằng tháng của VIE; tính lại k khi có số thu nhập PP thực.

| Decision | Điều kiện mở | Chi phí (k) | Thời gian | Cooldown | Hiệu ứng |
| --- | --- | --- | --- | --- | --- |
| Huấn luyện tác chiến rừng núi | `readiness_active` | 0,5 | 90 ngày | 545 ngày | +10 XP lục quân; −5% phạt địa hình 180 ngày |
| Huấn luyện tác chiến đô thị | `readiness_active` | 0,5 | 90 ngày | 545 ngày | +10 XP lục quân; −5% phạt đô thị 180 ngày |
| Huấn luyện chống ngầm | Có tàu ngầm | 0,6 | 120 ngày | 545 ngày | +10 XP hải quân; +5% phát hiện 180 ngày |
| Huấn luyện BVR | Có tiêm kích đủ điều kiện | 0,6 | 120 ngày | 545 ngày | +10 XP không quân; +5% tấn công trên không 180 ngày |
| Diễn tập song phương | Quan hệ đối tác ≥ ngưỡng | 0,6 | 60 ngày | 730 ngày | +15 XP lục quân; +5 quan hệ |
| Diễn tập đa phương | Cờ do nhánh Đối ngoại đặt | 0,8 | 90 ngày | 730 ngày | +15 XP lục quân; +3 quan hệ khu vực |
| Cứu trợ thảm họa (HADR) | Sự kiện thiên tai hoặc chủ động | 0,3 | 45 ngày | 365 ngày | +5 quan hệ; +2% ổn định 90 ngày |
| Triển khai gìn giữ hòa bình | Cờ do nhánh Chính trị – Đối ngoại đặt | 0,4 | 180 ngày | 730 ngày | +10 XP lục quân; +5 quan hệ |
| Phản ứng nhanh | Capstone B hoàn thành | 0,7 | 60 ngày | 545 ngày | +20 XP lục quân; +10% tốc độ 90 ngày |
| Động viên toàn dân | Capstone C hoàn thành | 0,6 | 120 ngày | 730 ngày | +50 000 nhân lực; +5% dig-in 180 ngày |
| Tổng động viên | Doctrine C, hoặc đang có chiến tranh, hoặc căng thẳng cao | 0,9 | 90 ngày | 1 095 ngày | +200 000 nhân lực; −5% ổn định; +10% dig-in |

Tên cờ do nhánh Đối ngoại và nhánh Chính trị – Đối ngoại đặt chưa được định nghĩa; chốt khi viết các nhánh đó.

Ước tính XP theo công thức XP mỗi lần × 365 ÷ (thời gian + cooldown), giả sử lặp lại ngay khi hết cooldown: ≈ 40 XP/năm cho bảy chương trình huấn luyện và diễn tập (lục quân ≈ 29, hải quân 5,5, không quân 5,5). Chúng chiếm khoảng 375 ngày chạy mỗi năm, thấp hơn 730 ngày của hai chương trình song song nên giới hạn 2 không chặn. Doctrine B thêm decision Phản ứng nhanh, tương đương +12 XP lục quân mỗi năm.

### 3.7. Ranh giới với ba focus Trục 1 giữ lại

Trục 1 giữ `VIE_mechanization`, `VIE_army_c4isr` và `VIE_army_short_range_ad`. Để không cộng trùng, Trục 3 chỉ cho modifier và cờ; chỉ #10 và #15 được tạo mẫu mới.

| Nội dung | Chủ sở hữu | Trục 3 làm gì |
| --- | --- | --- |
| Mẫu sư đoàn cơ giới, 200 `util_vehicle` | `VIE_mechanization` (Trục 1) | #6 chỉ cho modifier tổ chức; không tạo mẫu, không cấp trang bị |
| planning, max\_planning, recon, EW, night optics | `VIE_army_c4isr` (Trục 1) | Lĩnh vực Mạng & Điện tử chỉ dùng org, hậu cần, tốc độ, phòng thủ, dig-in; không dùng planning, recon |
| AA building, tech phòng không | `VIE_army_short_range_ad` (Trục 1) | #26 chỉ cho modifier phối hợp |
| Học thuyết People's War (v7) | Doctrine C, #14–#18 | Thay focus cũ; cần gỡ focus cũ khỏi cây v7 |
| Mẫu mới mà Trục 1 chưa có | Trục 3 | #10 (cụm cơ động), #15 (dân quân) được tạo mẫu |

Bonus của ba focus Trục 1 không nằm trong ngân sách điểm Trục 3. Vì mọi doctrine đều đi được ba focus đó, việc cộng dồn không làm lệch cân bằng giữa A, B, C; nó chỉ nâng sức mạnh tuyệt đối. Trục 3 không có prerequisite chéo sang ba focus này, nên AI không bị kẹt nếu không đi chúng.

### 3.8. Capstone: 3 biến thể

`VIE_luc_luong_vu_trang_hoan_chinh` có cùng điều kiện (`VIE_capability_done >= 2`) nhưng phần thưởng chọn theo cờ doctrine. Phần thưởng chính mỗi biến thể đúng 6 điểm theo hệ số mục 3.4; cả ba đặt cờ `VIE_force_building_done`.

| Doctrine | Phần thưởng chính (6,0 điểm) | Thưởng thêm (ngoài điểm) |
| --- | --- | --- |
| A | +3% org, +3% phòng thủ toàn quân; đặt `VIE_combined_arms_level` = 3 | Giảm chi phí duy trì 2% nếu đã hoàn thành lĩnh vực sở trường |
| B | +9% tốc độ (3,6), +2% tấn công (2,4) | Mở decision Phản ứng nhanh (mục 3.6) |
| C | +5% max manpower (3,0), +6% dig-in (3,0) | Mở decision Động viên toàn dân (mục 3.6) |

### 3.9. AI và mô phỏng

**Trọng số chọn doctrine theo path** chỉ áp dụng cho base. Nhánh dân tộc chủ nghĩa nằm ở submod riêng và có phần quân sự riêng, nên trọng số của path đó đặt trong file submod. Thay `VIE_path_*` bằng cờ path thật của mod.

| Path | A | B | C |
| --- | --- | --- | --- |
| Historical | 2 | 0,5 | 3 |
| Western | 2 | 3 | 0,5 |

- **Chọn lĩnh vực.** `ai_will_do` của ba gốc lĩnh vực: `base = 1`, riêng gốc sở trường của doctrine đã chọn `base = 3`; node giữa và node cuối `base = 1`. Xác suất AI đi đúng lĩnh vực sở trường là 0,6 + 0,4 × 0,75 = 90%. AI dừng ở 2 lĩnh vực nhờ điều kiện `VIE_capability_count < 2` ở gốc.
- **Guard phá sản.** Mọi focus cost ≥ 5 có guard `factor = 0` khi `has_active_mission = bankruptcy_incoming_collapse` theo chuẩn MD. `base` vẫn ≥ 1, guard ghi đè khi phá sản: AI tạm dừng chuỗi rồi tiếp tục khi hết phá sản, không kẹt vĩnh viễn.
- **Không đặt điều kiện ngày trên đường AI.** Các mốc ngày chỉ dùng như modifier trọng số.

Mô phỏng dùng đúng bảng prerequisite và cost ở mục 3.2: mỗi lần có slot trống, AI chọn có trọng số trong các focus khả dụng; focus hoàn thành cùng ngày xử lý theo thứ tự ngẫu nhiên; `cancel_if_invalid` là mặc định; ME giữa ba gốc doctrine chặn khi gốc khác đã bắt đầu hoặc hoàn thành; bảo hiểm ở mục 3.3 có hiệu lực. Chạy 5 000 lượt cho mỗi path base và 20 000 lượt với trọng số doctrine ngẫu nhiên.

| Kiểm tra | Kết quả |
| --- | --- |
| Đồ thị prerequisite có vòng không | Không |
| 1 slot: tới capstone | 30 000 / 30 000 lượt; luôn 18 focus |
| 1 slot: tổng thời gian | 145 tuần ở khoảng 90% lượt (đi đúng sở trường), 147 tuần ở khoảng 10% |
| 2 slot: tới capstone | 30 000 / 30 000 lượt; luôn 18 focus; 102–109 tuần; trung bình 0,30 focus bị hủy mỗi lượt |
| 2 slot: rò rỉ lĩnh vực thứ ba, có `cancel_if_invalid` | 0 / 20 000 |
| 2 slot: rò rỉ, không có `cancel_if_invalid` | 5 903 / 20 000 (29,5%) |
| 3 slot | Tới capstone 100%, nhưng cả ba lĩnh vực đều hoàn thành (22 focus); thưởng lĩnh vực thứ ba bị bảo hiểm chặn |
| Chọn doctrine, 1 slot | Historical: A 37% · B 10% · C 54%. Western: A 37% · B 54% · C 9%. Ngẫu nhiên: 33% · 34% · 33% |

Mô phỏng chưa tính guard phá sản, điều kiện của `VIE_modernize_vpa`, ngày tháng và hành vi thật của AI trong MD.

### 3.10. Thời điểm và nhãn dữ kiện

- **Không khóa ngày cho #1–#3.** Từ 5/2/2025 (mốc của #2), #1–#3 được giảm cost khoảng 50% và nhân trọng số AI ×3, để thứ tự lịch sử nền vật chất trước, cải cách tổ chức sau được ưu tiên mà không khóa người chơi. Trước mốc này, localization gắn nhãn `[ALT-HISTORY: cải cách sớm]`.
- **#1.** Nghị quyết 05-NQ/TW của Bộ Chính trị được Chính phủ ghi là điều chỉnh tổ chức, biên chế quân đội giai đoạn 2025–2030, còn một số nguồn khác ghi là tổ chức Quân đội nhân dân giai đoạn 2021–2030. Bỏ mốc năm, ghi kèm Nghị quyết 230-NQ/QUTW của Quân ủy Trung ương; không ghi `[THẬT]` cho mốc thời gian cụ thể.
- **#2 (đã xác minh).** Quyết định 366/QĐ-BQP ký ngày 24/1/2025 sáp nhập Tổng cục Hậu cần và Tổng cục Kỹ thuật thành Tổng cục Hậu cần – Kỹ thuật; lễ công bố ngày 5/2/2025.
- **#3 (xác minh một phần).** Bộ Tổng Tham mưu là cơ quan tham mưu chiến lược, có nhiệm vụ chỉ đạo tác chiến, và Cục Tác chiến là một cục của Bộ Tổng Tham mưu. Không tìm thấy nguồn nào về một bộ chỉ huy tác chiến hiệp đồng liên quân chủng đang tồn tại. Localization ghi: nền là Bộ Tổng Tham mưu / Cục Tác chiến `[THẬT]`; cơ chế chỉ huy hiệp đồng liên quân chủng là `[ĐỀ XUẤT]`.
- **#10 và #12.** Cụm cơ động và cơ động đa quân chủng là hướng giả định `[ALT-HISTORY]`.
- **#26 (đã xác minh).** Quân chủng Phòng không – Không quân thành lập ngày 22/10/1963 theo Quyết định 50/QĐ của Bộ Quốc phòng, sau đó hai quân chủng tách ra rồi hợp nhất lại theo Sắc lệnh 03/L-CTN ngày 3/3/1999. Đến năm 2000, mốc bắt đầu của mod, quân chủng đã ở dạng hợp nhất, nên #26 là hiệp đồng chứ không phải một cuộc sáp nhập mới. Ghi `[THẬT]` cho hai sự kiện 1963 và 1999; ghi `[ĐỀ XUẤT]` cho cơ chế hiệp đồng cụ thể trong focus.

## IV. Liên kết ba trục

Trục 1 và 2 nối nhau bằng 7 flag có thật trong trigger; ba trong số đó tái hiện đúng con đường lịch sử “mua license → tự sản xuất” của Việt Nam. Trục 3 chỉ đặt cờ, không trục nào bị chặn bởi Trục 3.

### 4.1. Trục 1 ↔ Trục 2: liên kết bằng trigger

| Nguồn (Trục 1) | Flag | Tác động |
| --- | --- | --- |
| Mẫu thử T-54M3 (`.5` A) | `VIE_t54m3_prototype` | Điều kiện bắt buộc của D5 (T-54M nội địa) |
| Igla kèm quyền sản xuất (`.8` A) | `VIE_igla_license` | Điều kiện bắt buộc của D9 (TL-01) |
| License Galil ACE (`.11` A) | `VIE_iwi_license` | D2 (STV) còn 730 ngày thay vì 1095 |
| T-90 giao hàng (`.15`) | `VIE_t90_purchased` | Kích hoạt `vie_def_ind.2` |
| BMP-3 “rút kinh nghiệm” (`.32` A, alt) | `VIE_bmp3_lessons` | D6 (XCB-01) còn 1095 ngày |
| CAESAR thất bại (`.40`, alt) | `VIE_155mm_study` | Chuỗi K9 mở từ 2021, đánh giá còn 365 ngày |
| K9 giao hàng (`.20`) + `.21` A | `VIE_k9_purchased` | Mở D8 (cùng với D3) |

Dòng thời gian “mua trước → sản xuất sau” do lịch ETD và ngày mở decision ép, không phụ thuộc người chơi đi nhanh hay chậm.

| Giai đoạn | Trục 1 (Mua sắm) | Trục 2 (CNQP) |
| --- | --- | --- |
| 2003–2008 | — | Nghị quyết 27-NQ/TW (2003); Pháp lệnh CNQP (2008) |
| 2005–2006 | T-54/55 từ Phần Lan; T-72 Ba Lan (hủy) | — |
| 2008–2011 | Igla kèm license (2009); mẫu thử T-54M3 (2009–2010) | D1 nhà máy Z (2008–2011) |
| 2011–2015 | License Galil ACE (khoảng 2014) | D7 BM-21 (2011–2013); D5 T-54M (2012–2015) |
| 2013–2019 | T-90S/SK (ký 2016, giao 12/2018–02/2019) | D3 PTH (2013–2017); D2 STV, D9 TL-01, D4 đạn (2017–2019) |
| 2021–2029 | K9A1 (đánh giá 2023, xác nhận 2025) | D6 XCB-01 (2021–2025); D8 sau khi nhận K9 |
| Alt-history | BMP-3, TOS-1A, CAESAR | Chỉ tác động qua flag ở bảng 4.1 |

Trục 3 không dựa lịch ETD: người chơi đi 18 focus trong 145–147 tuần (mục 3.1) và không có mốc ngày nào khóa focus (mục 3.10).

### 4.2. Trục 3 → Trục 1, 2: cờ và trọng số AI

Quan hệ là quan hệ mềm: Trục 3 đặt cờ, Trục 1 và 2 không bị chặn, để AI không bị kẹt.

| Cờ / biến | Đặt bởi | Đọc bởi |
| --- | --- | --- |
| `VIE_force_regular / mobile / depth` | FR1, FM1, FD1 | Trục 3 (bảng 8.11, capstone, AI). Trục 1 và 2 chỉ để chỉnh trọng số AI (bảng dưới) |
| `VIE_dev_strategic / territorial` | PS, PT | Trục 3 (decision Phản ứng nhanh, Động viên toàn dân) |
| `VIE_command_reform_level` | CR1, CR2, CR3 | Chỉ Trục 3 (decision, AI) |
| `VIE_combined_arms_level` | HD, capstone Chính quy | Chỉ Trục 3 |
| `VIE_capability_land / ad / cyber` | L2, A2, Y2 | Trục 3 (Hiện đại hóa chọn lọc, AI). Trục 1 và 2 không đọc |
| `VIE_force_building_done` | Capstone | Nhánh Chính trị / Đối ngoại |

Việc Trục 1 và 2 có thể làm (không bắt buộc): chỉ chỉnh trọng số AI ở chuỗi và decision đã tồn tại, không đổi điều kiện mở hay hiệu ứng. Nếu bỏ bước này, Trục 1 và 2 vẫn nguyên vẹn.

| Trục | Chuỗi hoặc decision | Hướng lực lượng | Việc |
| --- | --- | --- | --- |
| Trục 1 | K9A1 (`vie_proc_army.18`–`.21`), BMP-3 (`.30`–`.32`), TOS-1A (`.35`), CAESAR (`.38`–`.40`) | Chính quy | Cộng trọng số `ai_chance` của option mua hoặc đánh giá khi có `VIE_force_regular` |
| Trục 1 | Igla (`vie_proc_army.8`) | Chiều sâu | Cộng trọng số `ai_chance` của option A (mua kèm quyền sản xuất) khi có `VIE_force_depth` |
| Trục 2 | D3 (PTH), D6 (XCB-01) | Chính quy | Cộng trọng số `ai_will_do` khi có `VIE_force_regular` |
| Trục 2 | D9 (TL-01) | Chiều sâu | Cộng trọng số `ai_will_do` khi có `VIE_force_depth` |
| Cả hai | Không có | Cơ động | Hướng Cơ động không có chuỗi hay decision tương ứng ở Trục 1, 2, nên không đọc |

### 4.3. Kịch bản theo dòng thời gian

Kịch bản lịch sử chạy từ 2000 đến khoảng 2029: Trục 1 nổ event theo lịch ETD, Trục 2 mở decision theo ngày và cờ, Trục 3 chạy theo tốc độ người chơi. Cuối mục này nêu cách xử lý hai lỗ hổng: event ETD chỉ nổ một lần và tranh chấp slot focus.

| Giai đoạn | Trục 1 (event) | Trục 2 (decision) |
| --- | --- | --- |
| 2000–2004 | Chưa có event | Hoàn tất `VIE_tank_modernization` để mở nhóm decision “CNQP Lục quân” |
| 2005–2006 | `.1` (2005): Phần Lan giao ≈ 70 T-54/55, −0.05bn; nhận lời Ba Lan 150 T-72. `.2` (2006): hủy T-72, +10 navy XP, +10 air XP | — |
| 2008–2011 | `.5` (2009): mẫu thử T-54M3, −0.05bn, cờ `VIE_t54m3_prototype`. `.8` (2009): Igla kèm quyền sản xuất, −0.35bn, cờ `VIE_igla_license` | D1 mở 2008.7.1, −15.0bn, xong sớm nhất 07/2011, `VIE_def_industry_level` +1. D7 mở sau D1 (07/2011 → 07/2013) |
| 2012–2015 | `.11` (ETD 2013): license Galil ACE ≈ 2014, −0.10bn, cờ `VIE_iwi_license` | D5 mở 2012.1.1 (cần cờ T-54M3), xong 01/2015. D3 mở 2013.1.1, xong 01/2017 |
| 2016–2019 | `.14` (2016): T-90S/SK, chọn A nợ +1.25bn; `.15` giao 12/2018 và 02/2019, cờ `VIE_t90_purchased` | D2 và D9 mở 2017.1.1, xong 01/2019 (D2 còn 730 ngày nếu có cờ IWI; D9 cần cờ Igla). D4 mở sau D3, xong 01/2019. `vie_def_ind.2` sau khi nhận T-90 |
| 2021–2029 | `.18` (2023): đánh giá K9A1; `.19` (sau 900 ngày, ≈ 08/2025): mua 20 xe, −1.30bn; `.20` (sau 365 ngày): giao, cờ `VIE_k9_purchased`; `.21` (sau 365 ngày): chọn nội địa hóa | D6 mở 2021.1.1, xong 01/2025. `vie_def_ind.1` (Triển lãm) từ 12/2022. `vie_def_ind.4` (Luật 2024) 2024.6.27. D8 khoảng 2027 → 2029 (khoảng 2024 → 2026 nếu có VIE\_155mm\_study) |
| Alt-history (rule bật) | BMP-3 `.30` (2010), CAESAR `.38` (2015), TOS-1A `.35` (2016) | Chỉ tác động qua cờ `VIE_bmp3_lessons` (D6 còn 1095 ngày) và `VIE_155mm_study` (K9 mở từ 2021) |

**Trục 3 chạy song song, không theo lịch.** Người chơi đi 21–22 focus trong 177–184 tuần (mục 8.2) và dùng PP cho các decision Lục quân sau Cải cách bộ chỉ huy I. Mốc lịch sử của N1, N3, CR2 và N2 (17/1/2022, 20/12/2022, 2/12/2023, 5/2/2025) không khóa ngày: đi trước mốc là hướng rẽ giả định, từ mốc thì giảm cost và tăng trọng số AI (mục 8.13).

#### Điều kiện vào của event và decision

| Mục | Mốc | Điều kiện |
| --- | --- | --- |
| `.1` | ETD 2005 | Không đòi focus |
| `.5` | ETD 2009, cửa sổ 2009–2012 | `VIE_tank_modernization` và ISR tồn tại |
| `.8` | ETD 2009, cửa sổ 2009–2013 | `VIE_army_short_range_ad` và SOV tồn tại |
| `.11` | ETD 2013, cửa sổ 2013–2015 | D1 đã xong và ISR tồn tại |
| `.14` | ETD 2016, cửa sổ 2016–2018 | `VIE_russian_arms_deals`, SOV tồn tại, không chiến tranh với SOV |
| `.18` | ETD 2023 (2021 nếu có `VIE_155mm_study`), cửa sổ tới 2026 | KOR tồn tại và không chiến tranh với KOR; opinion KOR chỉ chỉnh `ai_chance` |
| `.30`, `.35`, `.38` | 2010, 2016, 2015 | Rule `rule_vie_alt_procurement` bật; SOV tồn tại (`.30`, `.35`) hoặc FRA tồn tại (`.38`) |
| D1 | 2008.7.1 (`date > 2008.6.30`) | Nhóm decision hiện sau `VIE_tank_modernization`; còn slot nhà máy |
| D2 | 2017.1.1 | D1 |
| D3 | 2013.1.1 | D1 |
| D4 | Không có ngày | D3 |
| D5 | 2012.1.1 | D1 và `VIE_t54m3_prototype` (chỉ từ `.5` A) |
| D6 | 2021.1.1 | D1 |
| D7 | Không có ngày | D1 |
| D8 | Không có ngày | D3, `VIE_k9_purchased`, chọn `.21` A |
| D9 | 2017.1.1 | D1 và `VIE_igla_license` |

#### Xử lý hai lỗ hổng

1. **Event ETD chỉ nổ một lần.** Đã chốt: cửa sổ thời gian và thử lại (mục 1.6). Chuỗi chỉ mất khi hết cửa sổ mà điều kiện vẫn chưa đạt; hệ quả từng chuỗi nằm ở bảng 1.6.
2. **Tranh chấp slot focus.** Trục 3 chiếm khoảng 3,4–3,5 năm slot, trong khi `VIE_tank_modernization` và `VIE_army_short_range_ad` phải xong trước 2009 và `VIE_russian_arms_deals` trước 2016. Nếu MD chỉ có 1 slot ở giai đoạn đầu, người chơi không thể đi Trục 3 song song mà không lỡ các mốc đó; cửa sổ thử lại chỉ nới thêm 3–4 năm. Cần kiểm số slot MD (mục 7.3) trước khi chốt thứ tự.

## V. Tổng kết số liệu

Kịch bản lịch sử tốn 33.35bn treasury cho Trục 1 và 2; chọn mọi option lớn nhất tốn 38.70bn. Trong đó 22.5bn là giá 3 nhà máy theo bảng chi phí của MD. Trục 3 không tốn treasury, chỉ tốn PP.

| Chỉ số | Trục 1 | Trục 2 | Trục 3 | Cộng |
| --- | --- | --- | --- | --- |
| Focus chuyển đổi hoặc thay thế | 2 (1 sang event, 1 sang D7) | 2 (sang D1, D2) | 0 (cây dựng lại) | 4 |
| Focus giữ trong phạm vi | 3 | 4 | — | 7 |
| Focus mới | — | — | 30 (người chơi đi 21–22) | 30 |
| Chuỗi event | 9 | 4 | 0 | 13 |
| Decision | 0 | 9 (8 cố định, D8 có điều kiện) | 6 (Lục quân) | 15 |
| Treasury, kịch bản lịch sử (bn) | 3.10 | 30.25 | 0 | 33.35 |
| Treasury, tối đa (bn) | 7.95 | 30.75 | 0 | 38.70 |
| Chi phí PP mỗi decision | — | — | 0,5–0,9 × thu nhập PP hằng tháng | — |

MIO `VIE_gdt_manufacturer` nhận size và funds từ các decision và event của Trục 2 như sau:

| Nguồn | Size | Funds |
| --- | --- | --- |
| D1 | +2 | +500 |
| D2 | +1 | +250 |
| D3 | +1 | +250 |
| D4 | +1 | +100 |
| D5 | +1 | +200 |
| D7 | +1 | +150 |
| D9 | +1 | +100 |
| D8 (có điều kiện) | +1 | +150 |
| **Tổng từ decision** | **+9 (+8 không có D8)** | **+1,700 (+1,550 không có D8)** |

Funds thêm ngoài decision: Pháp lệnh CNQP +250, hợp tác nghiên cứu +200, chuyển giao bảo dưỡng T-90 +150, Luật 2024 +150, triển lãm +100 mỗi lần.

## VI. Script theo quy ước MD

Phần này theo AGENTS.md và tài liệu dev của Millennium Dawn: tab để thụt lề, ID dạng `TAG_ten`, log trong mọi option có hiệu ứng, event `is_triggered_only`.

### 6.1. Treasury, nợ và guard phá sản

- Trừ tiền: `set_temp_variable = { treasury_change = -X }` rồi `modify_treasury_effect = yes`.
- Thiếu tiền không chặn giao dịch: MD tự phát hành nợ. Vì vậy không cần ẩn option với người chơi.
- Hợp đồng vay tín dụng (T-90) ghi vào nợ bằng `modify_debt_effect` thay vì trừ treasury.
- Guard phá sản chuẩn của MD nằm trong trọng số AI.

```
option = {
	name = vie_proc_army.14.a
	log = "[GetDateText]: [Root.GetName]: event vie_proc_army.14.a"
	set_temp_variable = { debt_change = 1.25 }
	modify_debt_effect = yes
	country_event = { id = vie_proc_army.15 days = 900 random_days = 30 }
	ai_chance = {
		base = 10
		modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
	}
}
```

### 6.2. Decision có xây nhà máy

Nhà máy được xây bằng `add_building_construction` và trả tiền trực tiếp, nên giá không phụ thuộc vào việc hiệu ứng `one_state_arms_factory` của MD có tự trừ tiền hay không. Decision không dùng ID state cố định mà chọn state VIE còn slot. Phần thưởng của decision có thời hạn đặt trong `remove_effect`; `complete_effect` chạy ngay khi bấm, dùng để trừ tiền, log và đặt cờ. `can_staff_an_arms_factory` lấy từ báo cáo gốc của bạn; MD có các trigger staffing cho focus xây nhà máy.

```
VIE_dec_z_factories = {
	available = {
		date > 2008.6.30
		can_staff_an_arms_factory = yes
		any_owned_state = {
			free_building_slots = { building = arms_factory size > 0 include_locked = no }
		}
	}
	days_remove = 1095
	complete_effect = {
		log = "[GetDateText]: [Root.GetName]: Decision VIE_dec_z_factories"
		set_temp_variable = { treasury_change = -15 }
		modify_treasury_effect = yes
	}
	remove_effect = {
		random_owned_controlled_state = {
			limit = { free_building_slots = { building = arms_factory size > 0 include_locked = no } }
			add_building_construction = { type = arms_factory level = 1 instant_build = yes }
		}
		random_owned_controlled_state = {
			limit = { free_building_slots = { building = arms_factory size > 0 include_locked = no } }
			add_building_construction = { type = arms_factory level = 1 instant_build = yes }
		}
		add_to_variable = { VIE_def_industry_level = 1 }
	}
	ai_will_do = { base = 5 }
}
```

D2 dùng cùng khuôn với một nhà máy và −7.5bn. Điều kiện slot nằm trong available nên decision hiện xám và mở khi có slot, không mất vĩnh viễn; dùng custom\_trigger\_tooltip để báo thiếu slot. Mốc date > 2008.6.30 tương ứng “từ 01/07/2008”.

### 6.3. Event theo ngày (ETD) và rule alt-history

Event lịch sử được đặt lịch trong `common/scripted_effects/00_yearly_effects.txt`, trong khối năm đã có sẵn. Chuỗi có cửa sổ thử lại (mục 1.6) gọi VIE\_try\_proc\_N thay vì country\_event trực tiếp:

```
trigger_year_2016_events = {
	if = {
		limit = { country_exists = VIE }
		VIE = { VIE_try_proc_14 = yes }
	}
}
```

```
country_event = {
	id = vie_proc_army.14
	is_triggered_only = yes
	trigger = {
		has_completed_focus = VIE_russian_arms_deals
		country_exists = SOV
		NOT = { has_war_with = SOV }
	}
	# option: xem 6.1
}
```

MD không có rule riêng cho nội dung phi lịch sử; chỉ có `historic_events` và mẫu `rule_salafist_branch` trong nhóm `MD_FOCUS_TREE_RULES`. Rule mới `rule_vie_alt_procurement` (mặc định tắt) đặt trong `common/game_rules`, và chuỗi 7–9 chỉ vào lịch ETD khi rule bật:

```
rule_vie_alt_procurement = {
	name = "RULE_VIE_ALT_PROCUREMENT"
	group = "MD_FOCUS_TREE_RULES"
	default = {
		name = "VIE_ALT_OFF"
		text = "VIE_ALT_OFF_TEXT"
		desc = "VIE_ALT_OFF_DESC"
	}
	option = {
		name = "VIE_ALT_ON"
		text = "VIE_ALT_ON_TEXT"
		desc = "VIE_ALT_ON_DESC"
	}
}
```

```
trigger_year_2010_events = {
	if = {
		limit = {
			country_exists = VIE
			has_game_rule = { rule = rule_vie_alt_procurement option = VIE_ALT_ON }
		}
		VIE = { country_event = { id = vie_proc_army.30 days = 120 random_days = 60 } }
	}
}
```

Localisation (English, UTF-8 BOM): `RULE_VIE_ALT_PROCUREMENT: "Vietnam: alternate-history procurement"`, `VIE_ALT_OFF_TEXT: "Historical only"`, `VIE_ALT_OFF_DESC: "Only documented procurement events fire."`, `VIE_ALT_ON_TEXT: "Include alternate history"`, `VIE_ALT_ON_DESC: "BMP-3, TOS-1A and CAESAR chains can fire."`.

### 6.4. Decision hai biến thể thời gian

`days_remove` cố định lúc kích hoạt. D2 (license IWI) và D6 (bài học BMP-3) dùng hai decision loại trừ nhau theo flag:

```
VIE_dec_stv = {
	visible = { NOT = { has_country_flag = VIE_iwi_license } }
	available = { NOT = { has_country_flag = VIE_stv_started } }
	days_remove = 1095
	complete_effect = {
		log = "[GetDateText]: [Root.GetName]: Decision VIE_dec_stv"
		set_country_flag = VIE_stv_started
	}
	remove_effect = { VIE_stv_reward = yes }
}
VIE_dec_stv_fast = {
	visible = { has_country_flag = VIE_iwi_license }
	available = { NOT = { has_country_flag = VIE_stv_started } }
	days_remove = 730
	complete_effect = {
		log = "[GetDateText]: [Root.GetName]: Decision VIE_dec_stv_fast"
		set_country_flag = VIE_stv_started
	}
	remove_effect = { VIE_stv_reward = yes }
}
```

`VIE_stv_reward` là scripted effect chung để hai bản không lệch phần thưởng.

### 6.5. Tên equipment

File OOB NSB dùng chassis kèm `variant_name`; file non-NSB dùng ID cũ và không có variant. Mọi event trao xe cần cả hai nhánh (`has_dlc = "No Step Back"` và `else`). Nâng cấp là chuyển đổi: trừ xe cũ bằng `add_equipment_to_stockpile` với `amount` âm (cần thử trong game), rồi cộng xe mới. Nhánh non-NSB không có variant nên bù bằng một lượng xe nhỏ.

| Hệ thống | NSB | Non-NSB | Ghi chú |
| --- | --- | --- | --- |
| T-54/55, T-54M, T-54M3 | `medium_tank_chassis_0` | `MBT_1` | Thế hệ 1965 |
| T-72 (Ba Lan) | `medium_tank_chassis_1` | `MBT_2` | Thế hệ 1975 |
| T-90S | `medium_tank_chassis_3` | `MBT_4` | v7 lệch: variant chassis\_1, NSB chassis\_2 |
| BMP-3 (alt) | `medium_tank_flame_chassis_2` | `IFV_3` | IFV dùng flame chassis |
| XCB-01 | `medium_tank_flame_chassis_4` | `IFV_5` | Thế hệ 2015 |
| BM-21, TOS-1A | `medium_tank_rocket_chassis_N` | `SP_R_arty_N` | 5 tier (0–4) |
| PTH, K9A1 | `medium_tank_artillery_chassis_N` | `SP_arty_N` | 5 tier (0–4) |
| SPAA | `medium_tank_aa_chassis_N` | `SP_Anti_Air_N` | 5 tier (0–4) |
| Súng bộ binh (D2) | `infantry_weapons_type` | `infantry_weapons_type` | Token đã dùng trong `licensed_rifles` của v7 |
| MANPADS (chuỗi 3, D9) | Không cấp equipment | Không cấp equipment | Tác dụng nằm ở modifier `enemy_army_bonus_air_superiority_factor` |

Năm của từng tier pháo và MLRS nằm trong `common/units/equipment/MD_x_tank_chassis.txt`.

T-90S nên dùng module `tank_medium_cannon_2` (2A46M), `mixed_main_ammo_2`, `smoothbore_atgm_gen3` (Refleks), `reactive_armor_gen2` (Kontakt-5), `tank_composite_armor_gen2`. Mỗi module cần tech mở tương ứng trong `set_technology`.

Hai bẫy cần tránh:

- Nếu `producer = SOV`, variant T-90S phải có trong `history/countries/SOV - Russia.txt`, không phải file VIE. Kiểm tra file SOV đã có T-90S chưa trước khi tạo mới.
- Buff sản xuất cho XCB-01 viết `equipment_bonus = { medium_tank_flame_chassis = { build_cost_ic = -0.05 } }`. Buff MBT không tự áp cho IFV hay APC.

Tên modifier chiến đấu (`air_defence`, `recon`, `naval_strike_attack` và tương tự) cần đối chiếu với `resources/documentation/modifiers_documentation.md`; modifier riêng của MD nằm trong `common/modifier_definitions/`. Sau khi viết variant, chạy `python3 tools/validation/validate_history.py --strict` và `python3 tools/validation/validate_oob_units.py --strict`.

### 6.6. Focus Trục 3: giới hạn 2/3

Khung script cho cơ chế ở mục 3.3; các focus Trục 3 dùng cùng guard phá sản và log như mục 6.1. Trong HOI4, nhiều `focus` trong một khối `prerequisite` là OR (dùng cho #19), còn AND là nhiều khối `prerequisite` riêng (dùng cho node cuối).

```
focus = {
	id = VIE_tac_chien_bien_gioi_do_thi
	cost = 10
	prerequisite = { focus = VIE_san_sang_tac_chien }
	available = { check_variable = { VIE_capability_count < 2 } }
	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: focus VIE_tac_chien_bien_gioi_do_thi"
		add_to_variable = { VIE_capability_count = 1 }
	}
	ai_will_do = {
		base = 1
		modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
	}
}
focus = {
	id = VIE_khong_che_dia_ban
	cost = 7
	prerequisite = { focus = VIE_trinh_sat_canh_gioi }
	prerequisite = { focus = VIE_chien_dau_do_thi }
	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: focus VIE_khong_che_dia_ban"
		set_country_flag = VIE_capability_land
		if = {
			limit = { check_variable = { VIE_capability_done < 2 } }
			add_to_variable = { VIE_capability_done = 1 }
			# phần thưởng node cuối theo cờ doctrine (bảng 3.5) đặt trong khối này
		}
	}
}
```

Gốc lĩnh vực không đặt `cancel_if_invalid`: MD bỏ dòng này vì mặc định là `yes`.

## VII. Quyết định cho các việc còn mở

### 7.1. Trục 1 và 2: bốn việc đã có quyết định

Có thể bắt tay vào code.

| Việc | Quyết định |
| --- | --- |
| ID state cho nhà máy | D1 và D2 không dùng ID cố định mà chọn state VIE còn slot (mục 6.2). Trong bản đồ vanilla, 517, 518 và 522 là state của Úc; nếu MD giữ số này thì ID 518, 522, 523 trong v7 không phải state Việt Nam. Các focus giữ lại còn dùng ID cũ (`VIE_army_short_range_ad` ở 522 và 521); kiểm bằng lệnh `Tdebug` khi sửa file v7. |
| Giá nhà máy | Trừ trực tiếp bằng `modify_treasury_effect` khi bấm decision, xây bằng `add_building_construction`. Tổng 22.5bn không phụ thuộc hiệu ứng `one_state_arms_factory`. |
| Tên equipment | Súng bộ binh dùng `infantry_weapons_type`, token đã có trong `licensed_rifles` của v7. MANPADS không cấp equipment; tác dụng nằm ở modifier của chuỗi 3 và D9. |
| Rule alt-history | Định nghĩa, localisation và cách gọi trong ETD ở mục 6.3. |

Giá của gói T-54M3, license Galil ACE, T-72 Ba Lan và Igla chưa được công bố; bảng dùng ước tính đã ghi nhãn, chỉnh bằng hệ số K.

### 7.2. Trục 3: ba quyết định (đã xử lý ở mục VIII)

1. **Focus People's War của v7.** Đã đóng: cây được dựng lại nên không còn focus People's War của v7; hướng Chiều sâu (FD1) ở mục VIII thay thế.
2. **Số slot focus của MD.** Đã xử lý bằng thiết kế: mô phỏng 8.12 cho thấy cây tới capstone ở 1, 2 và 3 slot; từ 2 slot có thể vượt giới hạn ở node đầu nhưng phần thưởng được bảo hiểm, chỉ mất thời gian. Số slot thực của MD kiểm khi code.
3. **Hải quân và Không quân có trục riêng không.** Đã chốt là có: Lục quân không giữ Biển & Trời; sáu decision liên quân chủng chuyển ra nhóm chung (8.14).

### 7.3. Trục 3: việc còn lại khi code

- Tên modifier cụ thể theo nhóm lĩnh vực (mục 8.11).
- Hệ số k của decision theo thu nhập PP thực (mục 8.14).
- Tên cờ do nhánh Đối ngoại và nhánh Chính trị – Đối ngoại đặt (mục 8.14).
- Sáu điểm cần test trong game:
  1. `ai_will_do` có `base ≥ 1` cho mọi focus; guard phá sản ghi đè khi cần.
  2. `VIE_modernize_vpa` AI đi được (điều kiện ngày, quan hệ) trước khi vào N1.
  3. Đặt rõ `VIE_arm_count`, `VIE_arm_done`, `VIE_capability_count`, `VIE_capability_done` = 0 ở N1, dù biến chưa đặt mặc định bằng 0.
  4. Tên cờ path (`VIE_path_*`) khớp với cờ thật của mod.
  5. `cancel_if_invalid` hủy node đầu vượt giới hạn khi điều kiện là `check_variable`, và quy tắc bảo hiểm phần thưởng hoạt động đúng.
  6. Số slot focus của MD; nếu từ 3 slot trở lên, node đầu lĩnh vực thứ ba vẫn hoàn thành và chỉ tốn thời gian.

## VIII. Trục 3: Xây dựng lực lượng, chọn dần (bản chính)

Đây là bản chính của Trục 3; mục III là bản cũ, chỉ giữ để đối chiếu và lấy lại hệ điểm (3.1) cùng bảng năng lực nền (3.5). So với mục III: bỏ ME Chính quy / Toàn dân; xây con người và binh chủng trước (chọn 3 trong 4); chỉ đến First Force Structure mới có khác biệt lớn; Cải cách bộ chỉ huy lặp lại ba lần theo từng đợt hiện đại hóa; Lục quân không giữ “Biển & Trời” (thuộc Hải quân và Không quân) mà thay bằng Phòng không lục quân. Hiệu ứng từng node ở 8.11, trọng số AI và mô phỏng ở 8.12, mốc lịch sử ở 8.13, nhóm decision chung ở 8.14. Mục IX (nội dung lịch sử) đọc kèm bảng ánh xạ ở 9.10. Các con số là mốc cân bằng theo hệ điểm mục 3.1, chưa qua thử nghiệm trong game.

### 8.1. Thay đổi so với bản trước

| Bản trước | Bản chính (mục VIII) | Lý do |
| --- | --- | --- |
| Chọn hướng đào tạo Chính quy hoặc Toàn dân (ME) | Bỏ. Đào tạo sĩ quan nằm trong từng binh chủng | Hai yếu tố đi song song trong thực tế (mục 9.1) |
| 4 mô hình lực lượng, chọn ngay sau đào tạo | Một lựa chọn lớn (First Force Structure, 3 hướng) và một lựa chọn nhỏ (hướng phát triển, 2 hướng), chỉ xuất hiện sau khi đã xây con người, binh chủng và chỉ huy | Chọn muộn, có thông tin |
| Dự bị động viên là mô hình riêng | Thành một phần của hướng “Phòng thủ khu vực và dự bị” | Dự bị không thay thế quân đội chính quy |
| Ba lĩnh vực: Biên giới & Đô thị, Biển & Trời, Mạng & Điện tử | Thay Biển & Trời bằng Phòng không lục quân | Hải quân, Không quân có trục riêng; Lục quân giữ phòng không tầm thấp (Trục 1) |
| 11 decision nằm ở Trục 3 Lục quân | 6 decision Lục quân, 6 decision chuyển ra nhóm chung (8.14) | Tránh chồng ownership với Hải quân, Không quân |
| 36 focus, 164 tuần | 30 focus, 177–184 tuần (8.2) | Dài hơn vì thêm binh chủng và Cải cách bộ chỉ huy; xem rủi ro ở 8.10 |

### 8.2. Cấu trúc

```
[1 Nền tảng]  cải cách → bảo đảm hậu cần – kỹ thuật ┐
                        → đào tạo lục quân cơ bản  ┘   (cổng mềm từ nền CNQP Trục 2, mục 8.3)
                     ▼
[2 Binh chủng]  chọn 3 trong 4; chính: tổ chức → đào tạo sĩ quan, binh sĩ; phụ: chỉ đào tạo
   Bộ binh │ Tăng thiết giáp │ Pháo binh │ Công binh (phụ)
                     ▼  (đủ 3 binh chủng)
[3 Hiệp đồng binh chủng]
                     ▼
[4 Cải cách bộ chỉ huy I]  chuẩn hóa tham mưu → mở decision Lục quân
                     ▼
[5 First Force Structure]  CHỌN 1 (ME)
   Cơ động │ Chính quy (quân đoàn chủ lực) │ Chiều sâu      (mỗi hướng 2 focus)
                     ▼  (OR)
[6 Hướng phát triển]  CHỌN 1 (ME)
   Cơ động chiến lược │ Phòng thủ khu vực và dự bị
                     ▼
[7 Cải cách bộ chỉ huy II]  bộ tư lệnh cấp chiến dịch (3 biến thể theo hướng ở tầng 5)
                     ▼
[8 Năng lực]  chọn 2 trong 3: Biên giới & Đô thị │ Phòng không lục quân │ Mạng & Điện tử
                     ▼  (≥ 2 lĩnh vực)
[9 Hiện đại hóa cao]  hiện đại hóa chọn lọc → cải cách bộ chỉ huy III → capstone (3 biến thể)
```

| Tầng | Câu hỏi | Số focus | Người chơi đi | Cost trên đường đi (tuần) | Lựa chọn |
| --- | --- | --- | --- | --- | --- |
| 1. Nền tảng | Tổ chức, bảo đảm, đào tạo cơ bản | 3 | 3 | 13 + 7 + 7 = 27 | Không |
| 2. Binh chủng | Xây binh chủng nào | 7 | 5–6 | 35–42 (2–3 binh chủng chính × 14, 0–1 phụ × 7) | 3 trong 4 (giới hạn ở node đầu của mỗi binh chủng) |
| 3. Hiệp đồng binh chủng | Phối hợp các binh chủng | 1 | 1 | 7 | Không |
| 4. Cải cách bộ chỉ huy I | Chuẩn hóa tham mưu | 1 | 1 | 7 | Không |
| 5. First Force Structure | Chủ lực tổ chức theo hướng nào | 6 | 2 | 10 + 7 = 17 | 1 trong 3 (ME) |
| 6. Hướng phát triển | Đẩy hướng nào lên cao hơn | 2 | 1 | 10 | 1 trong 2 (ME) |
| 7. Cải cách bộ chỉ huy II | Bộ tư lệnh cấp chiến dịch | 1 | 1 | 10 | Không (3 biến thể) |
| 8. Năng lực | Chuyên sâu ở đâu | 6 | 4 | 2 × (10 + 7) = 34 | 2 trong 3 |
| 9. Hiện đại hóa cao | Hiện đại hóa chọn lọc, chỉ huy số, capstone | 3 | 3 | 10 + 7 + 13 = 30 | 3 biến thể |
| **Tổng** |  | **30** | **21–22** | **177–184 tuần (1 239–1 288 ngày), khoảng 3,4–3,5 năm** | Mục III: 147 tuần |

### 8.3. Cổng vào từ nền tảng Trục 2 (tùy chọn)

Nếu muốn nền vật chất đi trước, thêm vào N1 điều kiện mềm:

```
available = {
	OR = {
		check_variable = { VIE_def_industry_level > 1 }
		date > 2012.12.31
	}
}
```

Level ≥ 2 sớm nhất khoảng 07/2011 (Pháp lệnh CNQP + D1). Ngày dự phòng để không ai bị kẹt nếu chậm D1. Điều kiện này phá quy ước ở mục 3.7 (Trục 3 không đọc biến của Trục 2); không dùng ngã rẽ Core/Divest hay capstone Trục 2 làm điều kiện. Bỏ dòng này thì cây vẫn chạy với bố cục A + B đã chốt.

### 8.4. Bảng focus

Binh chủng là `[ĐỀ XUẤT]` (chưa tra danh sách binh chủng chính thức); tên và ID đều là bản nháp. Binh chủng chính: Bộ binh, Tăng thiết giáp, Pháo binh (hai node: tổ chức, đào tạo). Binh chủng phụ: Công binh (một node đào tạo, đã gộp phần tổ chức). Người chơi chọn 3 trong 4 nên luôn có ít nhất 2 binh chủng chính.

| Mã | ID | Tên hiển thị | Cost | Prerequisite | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| N1 | `VIE_cai_cach_quan_doi` | Cải cách quân đội, tinh gọn biên chế | 13 | `VIE_modernize_vpa` (+ cổng mềm 8.3) | Root. `[THẬT]` Nghị quyết 05 (17/1/2022) |
| N2 | `VIE_hien_dai_hoa_bao_dam` | Hiện đại hóa hệ thống bảo đảm hậu cần – kỹ thuật | 7 | N1 | Focus khái quát; event 5/2/2025 (hợp nhất Hậu cần – Kỹ thuật) nổ cho mọi người chơi, thưởng thêm nếu đã xong focus |
| N3 | `VIE_dao_tao_luc_quan_co_ban` | Đào tạo lục quân cơ bản | 7 | N1 | Nền đào tạo chung, không có lựa chọn |
| BB1 | `VIE_bo_binh_to_chuc` | Bộ binh: tổ chức, cơ giới hóa từng bước | 7 | N2 AND N3 | `available`: `VIE_arm_count < 3`; hoàn thành `VIE_arm_count += 1`; chỉ modifier tổ chức (mẫu cơ giới thuộc `VIE_mechanization`) |
| BB2 | `VIE_bo_binh_dao_tao` | Bộ binh: đào tạo sĩ quan, huấn luyện binh sĩ | 7 | BB1 | `VIE_arm_done += 1` |
| TG1 | `VIE_tang_thiet_giap_to_chuc` | Tăng thiết giáp: tổ chức | 7 | N2 AND N3 | Như BB1 |
| TG2 | `VIE_tang_thiet_giap_dao_tao` | Tăng thiết giáp: đào tạo sĩ quan, kíp xe | 7 | TG1 | `VIE_arm_done += 1` |
| PB1 | `VIE_phao_binh_to_chuc` | Pháo binh: tổ chức, hỏa lực chi viện | 7 | N2 AND N3 | Như BB1 |
| PB2 | `VIE_phao_binh_dao_tao` | Pháo binh: đào tạo sĩ quan, pháo thủ | 7 | PB1 | `VIE_arm_done += 1` |
| CB2 | `VIE_cong_binh_dao_tao` | Công binh: đào tạo, công binh chiến đấu | 7 | N2 AND N3 | `available`: `VIE_arm_count < 3`; hoàn thành cộng `VIE_arm_count` và `VIE_arm_done` mỗi cái 1; phần tổ chức gộp vào node này |
| HD | `VIE_hiep_dong_binh_chung` | Hiệp đồng binh chủng | 7 | `VIE_arm_done >= 3` | +1 `VIE_combined_arms_level` |
| CR1 | `VIE_cai_cach_chi_huy_1` | Cải cách bộ chỉ huy I: chuẩn hóa tham mưu | 7 | HD | `VIE_command_reform_level` = 1; mở decision Lục quân (8.7). Nền `[THẬT]`: Bộ Tổng Tham mưu, Nghị quyết 109-NQ/QUTW |
| FM1 | `VIE_luc_luong_co_dong` | Lực lượng cơ động | 10 | CR1 | ME với FR1, FD1; cờ `VIE_force_mobile`; áp cái giá |
| FM2 | `VIE_cum_co_dong` | Cụm cơ động | 7 | FM1 | Được tạo mẫu mới (cụm cơ động) |
| FR1 | `VIE_quan_doan_chu_luc` | Quân đoàn chủ lực chính quy | 10 | CR1 | ME với FM1, FD1; cờ `VIE_force_regular`; áp cái giá. Nền `[THẬT]`: Quân đoàn 12, 34 |
| FR2 | `VIE_to_chuc_quan_doan` | Tổ chức quân đoàn tinh, gọn, mạnh | 7 | FR1 |  |
| FD1 | `VIE_phong_thu_chieu_sau` | Phòng thủ chiều sâu | 10 | CR1 | ME với FM1, FR1; cờ `VIE_force_depth`; áp cái giá |
| FD2 | `VIE_dan_quan_khu_vuc_phong_thu` | Dân quân và khu vực phòng thủ | 7 | FD1 | Được tạo mẫu mới (dân quân) |
| PS | `VIE_phat_trien_co_dong_chien_luoc` | Cơ động chiến lược | 10 | FM2 OR FR2 OR FD2 | ME với PT; cờ `VIE_dev_strategic`; mở decision Phản ứng nhanh |
| PT | `VIE_phat_trien_phong_thu_khu_vuc` | Phòng thủ khu vực và dự bị | 10 | FM2 OR FR2 OR FD2 | ME với PS; cờ `VIE_dev_territorial`; mở decision Động viên toàn dân |
| CR2 | `VIE_cai_cach_chi_huy_2` | Cải cách bộ chỉ huy II: bộ tư lệnh cấp chiến dịch | 10 | PS OR PT | `VIE_command_reform_level` = 2; 3 biến thể theo cờ `VIE_force_*`. Nền `[THẬT]`: Quân đoàn 12, 34 |
| L1 | `VIE_tac_chien_bien_gioi_do_thi` | Tác chiến biên giới và đô thị | 10 | CR2 | `available`: `VIE_capability_count < 2`; hoàn thành `VIE_capability_count += 1` |
| L2 | `VIE_khong_che_dia_ban` | Khống chế địa bàn | 7 | L1 | Node cuối; `VIE_capability_done += 1` (nếu < 2); đặt `VIE_capability_land` |
| A1 | `VIE_phong_khong_luc_quan` | Phòng không lục quân và bảo vệ lực lượng | 10 | CR2 | Như L1 |
| A2 | `VIE_hiep_dong_phong_khong` | Hiệp đồng phòng không với Phòng không – Không quân | 7 | A1 | Node cuối; đặt `VIE_capability_ad`; chỉ modifier phối hợp (AA building và tech thuộc `VIE_army_short_range_ad`) |
| Y1 | `VIE_tac_chien_mang_dien_tu` | Tác chiến mạng và điện tử | 10 | CR2 | Như L1 |
| Y2 | `VIE_tac_chien_thong_tin_hiep_dong` | Tác chiến thông tin hiệp đồng | 7 | Y1 | Node cuối; đặt `VIE_capability_cyber`; không cộng planning, recon (thuộc `VIE_army_c4isr`) |
| MOD | `VIE_hien_dai_hoa_chon_loc` | Hiện đại hóa chọn lọc | 10 | `VIE_capability_done >= 2` | Phần thưởng theo hai lĩnh vực đã hoàn thành |
| CR3 | `VIE_cai_cach_chi_huy_3` | Cải cách bộ chỉ huy III: chỉ huy số hiệp đồng | 7 | MOD | `VIE_command_reform_level` = 3; chỉ org, hậu cần, tốc độ; không planning, recon |
| CAP | `VIE_luc_luong_vu_trang_hoan_chinh` | Hoàn thiện lực lượng vũ trang | 13 | CR3 | 3 biến thể theo cờ `VIE_force_*`; đặt `VIE_force_building_done` |

### 8.5. Cơ chế giới hạn và tổ hợp

- **3 trong 4 binh chủng.** Cùng cơ chế mục 3.3: `available = { check_variable = { VIE_arm_count < 3 } }` chỉ đặt ở node đầu của ba binh chủng chính và ở node duy nhất của binh chủng phụ (Công binh); node “đào tạo” của binh chủng chính chỉ cần prerequisite; `cancel_if_invalid` là chốt chặn; phần thưởng node “đào tạo” chỉ cộng `VIE_arm_done` nếu < 3; phần thưởng của node đầu (binh chủng và lĩnh vực) cũng chỉ áp nếu số đếm còn dưới giới hạn lúc hoàn thành, nên phần vượt chỉ tốn thời gian (8.12). HD cần `VIE_arm_done >= 3`.
- **2 trong 3 lĩnh vực.** Giữ nguyên mục 3.3, với `VIE_capability_count` và `VIE_capability_done`.
- **Hai ME chồng nhau.** First Force Structure (3 chiều) và hướng phát triển (2 chiều) cho 6 tổ hợp, nhưng hiệu ứng cộng theo module nên không cần bảng 6 ô.

| Tầng 5 \\ Tầng 6 | Cơ động chiến lược | Phòng thủ khu vực và dự bị |
| --- | --- | --- |
| Chính quy | Quân đoàn chủ lực cơ động chiến lược (ALT nhẹ) | **Đường gần lịch sử nhất:** quân đoàn tinh, gọn, mạnh cùng khu vực phòng thủ và dự bị |
| Cơ động | ALT: đẩy cơ động lên cực đoan | Cơ động nòng cốt có dự bị hỗ trợ |
| Chiều sâu | Hỗn hợp: chiều sâu có mũi cơ động | ALT: đẩy chiều sâu lên cực đoan |

### 8.6. Ngân sách điểm gợi ý

Theo hệ điểm mục 3.4; chưa cân bằng chính thức.

| Thành phần | Số node | Điểm | Ròng |
| --- | --- | --- | --- |
| Binh chủng | 5–6 | Binh chủng chính: tổ chức 2,0 + đào tạo 2,5 = 4,5; binh chủng phụ: một node 2,5 | 11,5–13,5 (2–3 chính, 0–1 phụ) |
| Hiệp đồng binh chủng | 1 | 3,0 | 3,0 |
| Cải cách bộ chỉ huy I | 1 | 3,0 | 3,0 |
| First Force Structure | 2 | Gộp 11,2 (Cơ động) / 9,0 (Chính quy) / 9,2 (Chiều sâu); cái giá −5,2 / −3,0 / −3,2 | 6,0 mỗi hướng |
| Hướng phát triển | 1 | Ròng 4,0, cái giá nhỏ | 4,0 |
| Cải cách bộ chỉ huy II | 1 | 3,0 (3 biến thể) | 3,0 |
| Năng lực | 4 | Mỗi lĩnh vực: gốc 3,0 + cuối 6,0 | 18,0 (+3,0 nếu đúng sở trường) |
| Hiện đại hóa chọn lọc | 1 | 3,0 | 3,0 |
| Cải cách bộ chỉ huy III | 1 | 3,0 | 3,0 |
| Capstone | 1 | 6,0 (3 biến thể như mục 3.8) | 6,0 |
| **Tổng** | 18–19 |  | **60,5–62,5 (63,5–65,5 với sở trường)**, khoảng 0,34–0,36 điểm/tuần; mục III khoảng 0,32–0,35 |

Chi tiết cái giá của First Force Structure: Cơ động = −2% max manpower (−1,2), +2% chi phí sản xuất (−2,0), −4% dig-in (−2,0); Chính quy = +2% chi phí duy trì (−2,0), −1% XP lục quân (−1,0); Chiều sâu = −2% tấn công (−2,4), −2% tốc độ (−0,8).

Lĩnh vực sở trường theo First Force Structure: Cơ động → Mạng & Điện tử; Chính quy → Phòng không lục quân; Chiều sâu → Biên giới & Đô thị. Quy tắc sở trường giữ như mục 3.5 (giảm 2 tuần cost gốc, node cuối ×1,5). Hiệu ứng năng lực dùng lại hàng gốc và hàng cuối của bảng 3.5 cho hai lĩnh vực cũ (bỏ hai node giữa nên mỗi lĩnh vực từ 15 xuống 9 điểm); Phòng không lục quân cần bảng mới.

### 8.7. Decision Lục quân

Chi phí PP theo mục 3.6 (k × thu nhập PP hằng tháng).

| Decision | Điều kiện mở |
| --- | --- |
| Huấn luyện tác chiến rừng núi | CR1 |
| Huấn luyện tác chiến đô thị | CR1 |
| Diễn tập hiệp đồng binh chủng (mới) | CR1 |
| Phản ứng nhanh | PS |
| Động viên toàn dân | PT |
| Tổng động viên | FD1, hoặc PT, hoặc đang có chiến tranh, hoặc căng thẳng cao |

Chuyển ra nhóm chung liên quân chủng (bảng ở 8.14): huấn luyện chống ngầm (Hải quân), huấn luyện BVR (Không quân), diễn tập song phương, diễn tập đa phương, cứu trợ thảm họa (HADR), gìn giữ hòa bình. Chuỗi gìn giữ hòa bình có ba bước có thật ở mục 9.2.

### 8.8. Cờ và nối với các mục khác

- `VIE_doctrine_balanced / mobile / peoples` (mục 4.2) tương ứng `VIE_force_regular / mobile / depth`; bảng trọng số AI ở mục 4.2 đổi cờ theo đó.
- `VIE_capability_seaair` đổi thành `VIE_capability_ad`.
- Biến và cờ mới: `VIE_arm_count`, `VIE_arm_done`, `VIE_command_reform_level` (0–3, nội bộ Trục 3), `VIE_dev_strategic`, `VIE_dev_territorial`.
- Cải cách bộ chỉ huy III chồng với #29 cũ và `VIE_army_c4isr` (Trục 1), nên chỉ cho org, hậu cần, tốc độ và cờ, không cộng planning, recon.

### 8.9. Lịch sử và giả định

- **Xương sống lịch sử:** N1 → N2, N3 → binh chủng → Hiệp đồng → Cải cách bộ chỉ huy I → Chính quy (Quân đoàn 12, 34) → Phòng thủ khu vực và dự bị → Cải cách bộ chỉ huy II → lĩnh vực → Hiện đại hóa chọn lọc → Cải cách bộ chỉ huy III → capstone. Các sự kiện nền ở 9.2 nổ song song; hợp nhất Hậu cần – Kỹ thuật là focus khái quát (N2) cộng event 5/2/2025.
- **Giả định** là đẩy một hướng của chính Lục quân Việt Nam lên cao hơn (các ô ALT ở 8.5), không phải chuyển thành quân đội kiểu nước khác. Hình mẫu nước ngoài chỉ nằm trong ghi chú thiết kế, không đưa vào localization.
- Airmobile chỉ đưa vào khi có trục Không quân; chưa đưa vào bản này.

### 8.10. Còn thiếu và rủi ro

- **Cost 177–184 tuần** (175–182 nếu đúng sở trường) so với 147 tuần ở mục III; mô phỏng ở 8.12 cho thấy cây chạy tới capstone ở cả 1, 2 và 3 slot, nên số slot của MD chỉ ảnh hưởng thời gian, không chặn thiết kế; vẫn cần kiểm số slot khi code.
- **Luật chọn 3 trong 4 binh chủng và Công binh là binh chủng phụ** đã chốt. Nếu muốn 4 trong 5, thêm một binh chủng thứ năm (ví dụ Thông tin liên lạc), tránh chồng với Mạng & Điện tử và `VIE_army_c4isr`.
- **Cần test trong game:** `cancel_if_invalid` với điều kiện `check_variable` ở các node đầu binh chủng và lĩnh vực; hiệu lực quy tắc bảo hiểm phần thưởng (8.12).
- **Chưa có:** tên modifier cụ thể theo từng lĩnh vực (tra khi code), localization, mô phỏng có guard phá sản và mốc ngày.
- Danh sách bốn binh chủng là đề xuất chưa tra danh sách binh chủng chính thức.

### 8.11. Hiệu ứng từng node

Điểm theo hệ số mục 3.1, sai số tối đa 0,1 điểm mỗi node. Chỉ modifier: không cộng planning, recon, tech hay mẫu (trừ FM2 và FD2 tạo mẫu). Cái giá của First Force Structure áp ở node đầu (FM1, FR1, FD1).

**Nền, binh chủng, hiệp đồng, chỉ huy I**

| Mã | Focus | Hiệu ứng | Điểm |
| --- | --- | --- | --- |
| N1–N3 | Nền tảng | Không có hiệu ứng số; N2 nhận thưởng nhỏ của event 5/2/2025 | 0 |
| BB1 | Bộ binh: tổ chức | +2% org | 2,0 |
| BB2 | Bộ binh: đào tạo | +2% phòng thủ, +1% hậu cần | 2,5 |
| TG1 | Tăng thiết giáp: tổ chức | +5% tốc độ | 2,0 |
| TG2 | Tăng thiết giáp: đào tạo | +2% tấn công | 2,4 |
| PB1 | Pháo binh: tổ chức | +4% dig-in | 2,0 |
| PB2 | Pháo binh: đào tạo | +2% tấn công pháo binh | 2,4 |
| CB | Công binh | +5% dig-in | 2,5 |
| HD | Hiệp đồng binh chủng | +3% org; +1 `VIE_combined_arms_level` | 3,0 |
| CR1 | Cải cách bộ chỉ huy I | +2% org, +2% hậu cần; mở decision Lục quân | 3,0 |

**First Force Structure và hướng phát triển**

| Mã | Focus | Hiệu ứng | Điểm |
| --- | --- | --- | --- |
| FM1 | Lực lượng cơ động | +8% tốc độ, +2% org; cái giá −2% max manpower, +2% chi phí sản xuất, −4% dig-in | Gộp 5,2; giá −5,2 |
| FM2 | Cụm cơ động | +6% tốc độ, +3% tấn công; tạo mẫu cụm cơ động | 6,0 |
| FR1 | Quân đoàn chủ lực chính quy | +3% org, +2% phòng thủ; cái giá +2% chi phí duy trì, −1% XP lục quân | Gộp 5,0; giá −3,0 |
| FR2 | Tổ chức quân đoàn tinh, gọn, mạnh | +2% org, +4% hậu cần | 4,0 |
| FD1 | Phòng thủ chiều sâu | +6% dig-in, +2% phòng thủ; cái giá −2% tấn công, −2% tốc độ | Gộp 5,0; giá −3,2 |
| FD2 | Dân quân và khu vực phòng thủ | +7% max manpower; tạo mẫu dân quân | 4,2 |
| PS | Cơ động chiến lược | +5% tốc độ, +2% org, +2% hậu cần; cái giá +1% chi phí sản xuất | Gộp 5,0; giá −1,0 |
| PT | Phòng thủ khu vực và dự bị | +5% max manpower, +4% dig-in; cái giá +1% chi phí duy trì | Gộp 5,0; giá −1,0 |

Ròng mỗi hướng First Force Structure đúng 6,0 (11,2 − 5,2; 9,0 − 3,0; 9,2 − 3,2); mỗi hướng phát triển đúng 4,0.

**Năng lực theo hướng đã chọn ở First Force Structure**

| Lĩnh vực | Node | Chính quy | Cơ động | Chiều sâu |
| --- | --- | --- | --- | --- |
| Biên giới & Đô thị | L1 gốc (3,0) | +3% phòng thủ | +5% tốc độ, +1% phòng thủ | +4% dig-in, +1% phòng thủ |
|  | L2 cuối (6,0) | +3% org, +3% phòng thủ | +3% tấn công, +6% tốc độ | +8% dig-in, +2% phòng thủ |
| Phòng không lục quân | A1 gốc (3,0) | +3% phòng thủ | +2% org, +2,5% tốc độ | +4% dig-in, +1% phòng thủ |
|  | A2 cuối (6,0) | +3% org, +3% phòng thủ | +4% org, +5% tốc độ | +4% phòng thủ, +4% dig-in |
| Mạng & Điện tử | Y1 gốc (3,0) | +3% org | +5% tốc độ, +1% org | +6% dig-in |
|  | Y2 cuối (6,0) | +3% org, +3% phòng thủ | +3% tấn công, +6% tốc độ | +4% phòng thủ, +4% dig-in |

Sở trường: Cơ động → Mạng & Điện tử; Chính quy → Phòng không lục quân; Chiều sâu → Biên giới & Đô thị. Đúng sở trường thì giảm 2 tuần cost gốc và node cuối ×1,5 (6 thành 9). Phòng không lục quân chỉ là modifier phối hợp; AA building và tech thuộc `VIE_army_short_range_ad` (Trục 1).

**Cải cách bộ chỉ huy II, hiện đại hóa chọn lọc, chỉ huy III, capstone**

| Mã | Focus | Hiệu ứng | Điểm |
| --- | --- | --- | --- |
| CR2 | Cải cách bộ chỉ huy II | Chính quy: +2% org, +1% phòng thủ. Cơ động: +2% org, +2,5% tốc độ. Chiều sâu: +2% phòng thủ, +2% dig-in | 3,0 |
| MOD | Hiện đại hóa chọn lọc | Mỗi lĩnh vực đã hoàn thành cho 1,5 điểm: Biên giới & Đô thị +3% dig-in; Phòng không lục quân +1,5% phòng thủ; Mạng & Điện tử +1,5% org | 3,0 (hai lĩnh vực) |
| CR3 | Cải cách bộ chỉ huy III | +1% org, +4% hậu cần; không cộng planning, recon | 3,0 |
| CAP | Hoàn thiện lực lượng vũ trang | Chính quy: +3% org, +3% phòng thủ, thêm −2% chi phí duy trì nếu đúng sở trường. Cơ động: +9% tốc độ, +2% tấn công. Chiều sâu: +5% max manpower, +6% dig-in | 6,0 |

### 8.12. Trọng số AI và mô phỏng

**Trọng số `ai_will_do` (base)**

| Nhóm focus | Historical | Western |
| --- | --- | --- |
| First Force Structure (Cơ động / Chính quy / Chiều sâu) | 0,5 / 3 / 2 | 3 / 2 / 0,5 |
| Hướng phát triển (Cơ động chiến lược / Phòng thủ khu vực và dự bị) | 0,5 / 3 | 3 / 1 |
| Binh chủng (Bộ binh / Tăng thiết giáp / Pháo binh / Công binh) | 3 / 3 / 3 / 1 | 3 / 3 / 3 / 1 |
| Gốc lĩnh vực | 3 nếu là sở trường của hướng đã chọn, 1 nếu không | Như Historical |
| Mọi focus khác | 1 | 1 |

Mọi focus cost ≥ 5 có guard phá sản (`factor = 0` khi `bankruptcy_incoming_collapse`) như chuẩn MD. Trọng số path dân tộc chủ nghĩa đặt ở submod. Mọi mốc ngày chỉ là modifier trọng số, không phải điều kiện.

**Kết quả mô phỏng** (4 000 lượt mỗi dòng, dùng đúng prerequisite, cost và cơ chế giới hạn ở 8.5; `cancel_if_invalid` mặc định)

| Cấu hình | Tới capstone | Tổng thời gian (tuần) | Số focus đi | Node đầu binh chủng vượt giới hạn | Node đầu lĩnh vực vượt giới hạn |
| --- | --- | --- | --- | --- | --- |
| 1 slot | 100% | 175–184, trung bình 179,3 | 21–22 | 0% | 0% |
| 2 slot, có `cancel_if_invalid` | 100% | 139 | 21–23 | 40–43% | 0% |
| 2 slot, tắt `cancel_if_invalid` | 100% | 139–146 | 21–25 | 41% | 45% |
| 3 slot | 100% | 132 | 23–24 | 0% | 100% |

- **Không có lượt nào bị kẹt** ở cả ba mức slot và cả hai path.
- **Phân bố ở 1 slot.** Historical: Chính quy 54%, Chiều sâu 37%, Cơ động 9%; Phòng thủ khu vực và dự bị 86%. Western: Cơ động 54%, Chính quy 36%, Chiều sâu 9%; Cơ động chiến lược 75%. Ngẫu nhiên: 34% / 33% / 33%. Công binh bị bỏ ở 56–58% lượt; bộ ba Bộ binh, Tăng thiết giáp, Pháo binh chiếm 57% (Historical). AI đi đúng sở trường ở 90% lượt (1–2 slot) và 100% (3 slot).
- **Vượt giới hạn ở binh chủng (từ 2 slot).** Hai node đầu có cùng cost nên có thể hoàn thành cùng ngày; `cancel_if_invalid` không kịp chặn. **Vượt giới hạn ở lĩnh vực (3 slot)** giống mục 3.3.
- **Quy tắc bảo hiểm.** Phần thưởng của node đầu (binh chủng và lĩnh vực) chỉ áp nếu số đếm còn dưới giới hạn lúc hoàn thành; khi đó phần vượt chỉ tốn thời gian (khoảng 7–10 tuần), không thêm thưởng và không làm hỏng capstone.
- Mô phỏng chưa tính guard phá sản, mốc ngày, decision và hành vi thật của AI trong MD. Thời gian ở nhiều slot chỉ là chặn dưới vì mô phỏng bỏ qua tranh chấp nguồn lực.

### 8.13. Mốc lịch sử và giảm cost

Không khóa ngày. Từ mốc, focus được giảm cost khoảng 50% và nhân trọng số AI ×3; đi trước mốc là hướng rẽ giả định, localization gắn nhãn `[ALT-HISTORY: cải cách sớm]`.

| Focus | Mốc | Nguồn |
| --- | --- | --- |
| N1 Cải cách quân đội | 17/1/2022 | Nghị quyết 05 của Bộ Chính trị (2/4/2022: Nghị quyết 230-NQ/QUTW) |
| N3 Đào tạo lục quân cơ bản | 20/12/2022 | Nghị quyết 1657-NQ/QUTW |
| CR2 Cải cách bộ chỉ huy II | 2/12/2023 | Công bố thành lập Quân đoàn 12 (Quân đoàn 34: 15/12/2024) |
| N2 Hiện đại hóa hệ thống bảo đảm | 5/2/2025 | Công bố hợp nhất Hậu cần – Kỹ thuật |

Mốc của N1 thay cho mốc 5/2/2025 ở mục 3.10 (bản cũ), vì nguồn tra được ghi rõ ngày Nghị quyết 05.

### 8.14. Nhóm decision chung (liên quân chủng)

Sáu decision dưới đây không thuộc Lục quân; đặt ở nhóm chung để Trục 3 Hải quân và Không quân dùng lại, tránh trùng lặp. XP “lục quân” ở các diễn tập đổi thành XP của quân chủng tham gia.

| Decision | Điều kiện mở | Chi phí (k) | Thời gian | Cooldown | Hiệu ứng | Chủ |
| --- | --- | --- | --- | --- | --- | --- |
| Huấn luyện chống ngầm | Có tàu ngầm | 0,6 | 120 ngày | 545 ngày | +10 XP hải quân; +5% phát hiện 180 ngày | Hải quân |
| Huấn luyện BVR | Có tiêm kích đủ điều kiện | 0,6 | 120 ngày | 545 ngày | +10 XP không quân; +5% tấn công trên không 180 ngày | Không quân |
| Diễn tập song phương | Quan hệ đối tác ≥ ngưỡng | 0,6 | 60 ngày | 730 ngày | +15 XP; +5 quan hệ | Chung |
| Diễn tập đa phương | Cờ do nhánh Đối ngoại đặt | 0,8 | 90 ngày | 730 ngày | +15 XP; +3 quan hệ khu vực | Chung |
| Cứu trợ thảm họa (HADR) | Thiên tai hoặc chủ động | 0,3 | 45 ngày | 365 ngày | +5 quan hệ; +2% ổn định 90 ngày | Chung |
| Triển khai gìn giữ hòa bình | Cờ do nhánh Chính trị – Đối ngoại đặt | 0,4 | 180 ngày | 730 ngày | +10 XP; +5 quan hệ; ba bước theo mốc thật (6/2014, 10/2018, 5/2022) | Chung |

Lục quân thêm một decision mới: **Diễn tập hiệp đồng binh chủng** (mở sau CR1): k 0,5; 90 ngày; cooldown 545 ngày; +10 XP lục quân; +2% org 90 ngày. Chi phí PP của sáu decision Lục quân vì vậy nằm trong khoảng 0,5–0,9 × thu nhập PP hằng tháng.

## IX. Nội dung Trục 3 chọn dần (lịch sử và giả định)

Lưu ý: các bảng focus 9.3–9.8 viết cho bản VIII trước (chọn hướng đào tạo rồi chọn mô hình lực lượng); đọc kèm bảng ánh xạ sang bản chính ở 9.10. Cơ sở lịch sử và bảng sự kiện nền 9.2 dùng nguyên. Nội dung cho từng tầng của bản VIII trước: nhãn dữ kiện, cơ sở và mô tả ngắn dùng làm khung localization (câu chữ là bản nháp). Số liệu hiệu ứng nằm ở mục 8.6 và mục III, không lặp lại ở đây. Nguồn mới nằm cuối báo cáo.

### 9.1. Nguyên tắc nội dung

- Nhãn như mục III: `[THẬT]` có nguồn, `[ĐỀ XUẤT]` thiết kế của mod, `[ALT-HISTORY]` hướng giả định.
- **Đường gần lịch sử nhất** là Chính quy → Phòng vệ: Sách trắng Quốc phòng 2019 khẳng định quốc phòng mang tính hòa bình và tự vệ, và quân đội đang tổ chức lại theo quân đoàn “tinh, gọn, mạnh” (Quân đoàn 12, Quân đoàn 34). **Hướng giả định** là Phản ứng nhanh theo kiểu viễn chinh (hình mẫu Trung Quốc, Hàn Quốc, chưa tra nguồn) và Dự bị động viên mở rộng; cả hai đều tùy chọn.
- Thực tế Việt Nam đi đồng thời quân đội chính quy và nền quốc phòng toàn dân, nên ME buộc chọn trọng tâm. Phần lịch sử của hướng không được chọn giữ lại bằng các sự kiện nền ở 9.2, hiệu ứng nhỏ và không đổi cân bằng.
- Thứ tự tầng là thiết kế của mod, không phải niên đại: nghị quyết đào tạo (2019, 2022) ra trước hợp nhất Hậu cần – Kỹ thuật (2025).

### 9.2. Sự kiện lịch sử nền (nổ bất kể lựa chọn)

| Mốc | Sự kiện | Nhãn | Gợi ý xử lý |
| --- | --- | --- | --- |
| 22/9/2008 | Nghị quyết 28-NQ/TW của Bộ Chính trị: xây dựng tỉnh, thành phố thành khu vực phòng thủ vững chắc | `[THẬT]` | Event nhỏ; đặt cờ mở nội dung khu vực phòng thủ (M3, V2, C3) |
| 1/7/2010 | Luật Dân quân tự vệ 2009 (43/2009/QH12, ký 23/11/2009) có hiệu lực | `[THẬT]` | Event nhỏ |
| 1/1/2014 | Luật Giáo dục quốc phòng và an ninh (30/2013/QH13, ký 19/6/2013) có hiệu lực | `[THẬT]` | Event nhỏ |
| 27/5/2014 | Trung tâm Gìn giữ hòa bình Việt Nam ra mắt; hai sĩ quan đầu tiên tới Nam Sudan | `[THẬT]` | Mở chuỗi decision gìn giữ hòa bình (9.5) |
| 10/2018 | Bệnh viện dã chiến cấp 2 số 1 triển khai tại Nam Sudan | `[THẬT]` | Bước 2 của chuỗi gìn giữ hòa bình |
| 11/2/2019 | Nghị quyết 109-NQ/QUTW về đội ngũ cán bộ, nhất là cấp chiến dịch, chiến lược | `[THẬT]` | Event nhỏ |
| 25/11/2019 | Sách trắng Quốc phòng 2019: quốc phòng hòa bình, tự vệ; chính sách “bốn không” | `[THẬT]` | Event ghi nhãn chính sách, không cộng số |
| 1/7/2020 | Luật Dân quân tự vệ 2019 (48/2019/QH14) và Luật Lực lượng dự bị động viên (53/2019/QH14) có hiệu lực; Luật DBĐV thay Pháp lệnh 1996 | `[THẬT]` | Event nhỏ; mở khung dự bị |
| 17/1/2022 | Nghị quyết 05 của Bộ Chính trị và Nghị quyết 230 của Quân ủy Trung ương (2/4/2022) về tổ chức QĐND giai đoạn 2021–2030 | `[THẬT]` | Mốc lịch sử của #1 (xem 9.9) |
| 20/12/2022 | Nghị quyết 1657-NQ/QUTW đổi mới giáo dục, đào tạo trong quân đội | `[THẬT]` | Mốc lịch sử của G0 |
| 5/2022 | Đội Công binh số 1 tới phái bộ UNISFA (Abyei) | `[THẬT]` | Bước 3 của chuỗi gìn giữ hòa bình |
| 2/12/2023 | Công bố thành lập Quân đoàn 12 từ Quân đoàn 1 và Quân đoàn 2 (QĐ 6012/QĐ-BQP, 21/11/2023) | `[THẬT]` | Event nền, +org nhẹ; nối với Q2 |
| 15/12/2024 | Công bố thành lập Quân đoàn 34 từ Quân đoàn 3 và Quân đoàn 4 (QĐ 5989/QĐ-BQP, 10/12/2024) | `[THẬT]` | Event nền, +org nhẹ; nối với Q2 |
| 5/2/2025 | Công bố hợp nhất Hậu cần – Kỹ thuật (#2) | `[THẬT]` | Đã có ở mục 3.10 |
| 1/7/2025 | Luật 98/2025/QH15 (ký 27/6/2025) sửa đổi 11 luật về quân sự, quốc phòng | `[THẬT]` | Event nhỏ |

### 9.3. Tầng 1: Nền tảng

Cổng mềm từ nền CNQP Trục 2 (mục 8.3) diễn đạt là: nền công nghiệp quốc phòng phải đủ mức trước khi cải cách tổ chức.

| # | Focus | Nhãn | Cơ sở | Nội dung |
| --- | --- | --- | --- | --- |
| 1 | Cải cách quân đội, tinh gọn biên chế | `[THẬT]` | Nghị quyết 05 (17/1/2022) và 230-NQ/QUTW (2/4/2022) về tổ chức QĐND 2021–2030; Đại hội XIII đặt mục tiêu 2025 cơ bản “tinh, gọn, mạnh” | Rà soát, điều chỉnh tổ chức; ưu tiên quân số cho đơn vị sẵn sàng chiến đấu, tuyến biên giới, biển đảo. Bộ trưởng Quốc phòng cho biết (1/2026) đã điều chỉnh trên 5.000 tổ chức |
| 2 | Hợp nhất Hậu cần – Kỹ thuật | `[THẬT]` | Quyết định 366/QĐ-BQP (24/1/2025), công bố 5/2/2025 | Sáp nhập Tổng cục Hậu cần và Tổng cục Kỹ thuật thành một đầu mối bảo đảm cho toàn quân |
| 3 | Hiện đại hóa chỉ huy tác chiến hiệp đồng | `[THẬT]` nền, `[ĐỀ XUẤT]` cơ chế | Bộ Tổng Tham mưu và Cục Tác chiến; Nghị quyết 109-NQ/QUTW (11/2/2019) về cán bộ cấp chiến dịch, chiến lược | Chuẩn hóa quy trình chỉ huy hiệp đồng; cơ chế hiệp đồng liên quân chủng là đề xuất của mod |

### 9.4. Tầng 2: Đào tạo sĩ quan

| Mã | Focus | Nhãn | Cơ sở | Nội dung |
| --- | --- | --- | --- | --- |
| G0 | Cải cách đào tạo sĩ quan | `[THẬT]` | Nghị quyết 109-NQ/QUTW (2019); Nghị quyết 1657-NQ/QUTW (20/12/2022); Chiến lược phát triển giáo dục, đào tạo trong quân đội 2021–2030, tầm nhìn 2045 | Giáo dục, đào tạo là nhiệm vụ chính trị trung tâm; mở lối rẽ giữa đào tạo chính quy và đào tạo toàn dân |
| R1 | Học viện và đào tạo chính quy | `[THẬT]` | Đề án xây dựng đội ngũ nhà giáo, cán bộ quản lý giáo dục 2023–2030 (QĐ 3525/QĐ-BQP, 3/8/2023) | Học viện, trường sĩ quan nâng chuẩn giảng viên, chương trình và cơ sở vật chất |
| R2 | Trao đổi sĩ quan, đào tạo nước ngoài | `[THẬT]` một phần, `[ĐỀ XUẤT]` | Sĩ quan phụ trách gìn giữ hòa bình học các khóa ở Úc, Anh, Mông Cổ trước 2014; Trung tâm Gìn giữ hòa bình có quyết định thành lập 4/12/2013 theo một nguồn | Mở rộng cử sĩ quan đi học và tham gia phái bộ Liên hợp quốc; danh sách nước đối tác cụ thể là đề xuất |
| R3 | Chuyên nghiệp hóa quân nhân | `[THẬT]` luật, `[ĐỀ XUẤT]` mức độ | Luật Quân nhân chuyên nghiệp, công nhân và viên chức quốc phòng 98/2015/QH13; Luật Nghĩa vụ quân sự 78/2015/QH13 | Tăng tỷ trọng quân nhân chuyên nghiệp; ngày hiệu lực tra khi code |
| M1 | Giáo dục quốc phòng – an ninh toàn dân | `[THẬT]` | Luật 30/2013/QH13 (hiệu lực 1/1/2014); Chỉ thị 12-CT/TW (3/5/2007); Ngày hội Quốc phòng toàn dân từ 1989 | Giáo dục quốc phòng và an ninh trở thành môn chính khóa và được phổ biến cho toàn dân |
| M2 | Huấn luyện tại chỗ, sĩ quan kiêm nhiệm | `[THẬT]` một phần | Luật Dân quân tự vệ 2009 và 2019 quy định đào tạo Chỉ huy trưởng Ban chỉ huy quân sự cấp xã, tập huấn chức vụ chỉ huy dân quân tự vệ. Đề nghị đổi tên thành “Huấn luyện tại chỗ, đào tạo chỉ huy quân sự cấp xã” | Huấn luyện ngay tại địa phương, không thoát ly sản xuất |
| M3 | Cán bộ dân quân và công trình phòng thủ | `[THẬT]` | Nghị quyết 28-NQ/TW (22/9/2008); Nghị định 21/2019/NĐ-CP (22/2/2019) về khu vực phòng thủ | Cán bộ địa phương và công trình phòng thủ của tỉnh, thành phố trong khu vực phòng thủ |

### 9.5. Tầng 3: Mô hình lực lượng; Sẵn sàng tác chiến

| Mã | Focus | Nhãn | Cơ sở | Nội dung |
| --- | --- | --- | --- | --- |
| Q1 | Mô hình phản ứng nhanh | `[ĐỀ XUẤT]`, `[ALT-HISTORY]` | Hình mẫu Trung Quốc, Hàn Quốc (chưa tra nguồn); nền thật là Quân đoàn 12, quân đoàn “cơ động chiến lược” đầu tiên tổ chức lại theo hướng tinh, gọn, mạnh | Ưu tiên lực lượng nhỏ, cơ động cao, sẵn sàng ngay; chấp nhận dig-in thấp và chi phí sản xuất cao |
| Q2 | Quân đoàn chủ lực cơ động (đổi tên từ “Cụm/quân đoàn cơ động”) | `[THẬT]` | Quân đoàn 12 (công bố 2/12/2023 tại Ninh Bình) và Quân đoàn 34 (công bố 15/12/2024 tại Pleiku) | Tổ chức lại quân đoàn theo hướng tinh, gọn, mạnh; trong game tạo mẫu cụm cơ động. Nhánh Q đi xa hơn thực tế ở quy mô cơ động |
| Q3 | Đánh nhanh, thắng nhanh | `[ALT-HISTORY]` | Không có nguồn; phát triển tự nhiên của Q1 và Q2 | Học thuyết tập trung ưu thế cục bộ, kết thúc chiến dịch nhanh |
| V1 | Lực lượng phòng vệ chính quy | `[THẬT]` nền, `[ĐỀ XUẤT]` hình mẫu | Sách trắng Quốc phòng 2019 (25/11/2019): quốc phòng hòa bình và tự vệ; “bốn không”; bảo vệ Tổ quốc từ sớm, từ xa | Quân đội chính quy thuần phòng thủ; hình mẫu “lực lượng phòng vệ” chỉ là gợi ý thiết kế |
| V2 | Hệ thống phòng thủ khu vực | `[THẬT]` nền | Nghị quyết 28-NQ/TW (2008); Nghị định 21/2019/NĐ-CP | Quân khu, tỉnh, thành phố phối hợp phòng thủ theo khu vực |
| V3 | Hiệp đồng binh chủng | `[ĐỀ XUẤT]` | Không có nguồn cụ thể | Bộ binh, pháo binh, thiết giáp, phòng không hiệp đồng dưới một chỉ huy; node cuối |
| C1 | Phòng thủ chiều sâu | `[THẬT]` nền | Đường lối chiến tranh nhân dân; thế trận quốc phòng toàn dân gắn với thế trận an ninh nhân dân | Phòng thủ nhiều tuyến, dựa vào địa bàn và nhân dân |
| C2 | Dân quân tự vệ toàn dân | `[THẬT]` | Luật Dân quân tự vệ 2009 và 2019: dân quân tự vệ thường trực, cơ động, rộng rãi | Tổ chức và trang bị dân quân; tạo mẫu dân quân |
| C3 | Công sự, địa đạo, phân cấp tại chỗ | `[THẬT]` nền, `[ĐỀ XUẤT]` phân cấp | Địa đạo là di sản chiến tranh; Luật Quản lý, bảo vệ công trình quốc phòng và khu quân sự 25/2023/QH15 | Công trình phòng thủ vững chắc; quyền quyết định tác chiến giao xuống cấp địa phương; node cuối |
| B1 | Dự bị động viên | `[THẬT]` nền, `[ĐỀ XUẤT]` mở rộng | Luật Lực lượng dự bị động viên 53/2019/QH14 (26/11/2019; hiệu lực 1/7/2020), thay Pháp lệnh ngày 27/8/1996 | Xây dựng lực lượng dự bị lớn, đăng ký, quản lý theo luật |
| B2 | Tổ chức lực lượng dự bị | `[THẬT]` nền | Luật 53/2019/QH14 | Biên chế đơn vị dự bị gắn với đơn vị thường trực; dùng mẫu dân quân, không cùng lúc với C2 |
| B3 | Động viên nhanh | `[ĐỀ XUẤT]` | Luật 53/2019/QH14 quy định huy động khi tổng động viên, động viên cục bộ, thiết quân luật; mức độ “nhanh” là của mod | Rút ngắn thời gian từ lệnh động viên tới sẵn sàng chiến đấu; node cuối |

**Sẵn sàng tác chiến (#19)**

- `[THẬT]` Sách trắng 2019 nêu “sẵn sàng chống chiến tranh xâm lược”; Luật 98/2025/QH15 (1/7/2025) sửa 11 luật về quân sự, quốc phòng.
- Chuỗi decision gìn giữ hòa bình theo ba bước có thật: 6/2014 sĩ quan cá nhân; 10/2018 Bệnh viện dã chiến cấp 2 số 1; 5/2022 Đội Công binh số 1. Chuỗi mở theo mốc ngày ở 9.2, không phụ thuộc lựa chọn.

### 9.6. Tầng 4: Năng lực

Đại hội XIII ưu tiên đưa phòng không, không quân, thông tin liên lạc, tác chiến điện tử, trinh sát kỹ thuật, không gian mạng và cơ yếu tiến thẳng lên hiện đại; dự thảo văn kiện Đại hội XIV nêu thêm Hải quân và Biên phòng.

| # | Focus | Nhãn | Cơ sở | Nội dung |
| --- | --- | --- | --- | --- |
| 20 | Tác chiến biên giới và đô thị | `[ĐỀ XUẤT]` | Nền: Luật Biên phòng Việt Nam 66/2020/QH14 | Kết hợp phòng thủ tuyến biên giới với chiến đấu trong đô thị lớn |
| 21 | Trinh sát, cảnh giới biên giới | `[THẬT]` nền | Luật Biên phòng 66/2020/QH14 | Mạng lưới cảnh giới, trinh sát dọc biên giới |
| 22 | Chiến đấu trong đô thị | `[ĐỀ XUẤT]` | Không có nguồn cụ thể | Tổ chức và huấn luyện chiến đấu trong thành phố |
| 23 | Khống chế địa bàn | `[ĐỀ XUẤT]` | Không có nguồn cụ thể | Kiểm soát các địa bàn then chốt; node cuối |
| 24 | Phòng thủ biển và bầu trời | `[THẬT]` nền | Đại hội XIII ưu tiên phòng không, không quân; dự thảo Đại hội XIV nêu Hải quân | Xương sống phòng thủ trên biển và trên không |
| 25 | Phòng thủ bờ biển, chống đổ bộ | `[ĐỀ XUẤT]` | Không có nguồn cụ thể | Pháo bờ, tên lửa bờ, chống đổ bộ |
| 26 | Phòng không – Không quân hiệp đồng | `[THẬT]` | Quân chủng thành lập 22/10/1963 (QĐ 50/QĐ), hợp nhất lại 3/3/1999 (Sắc lệnh 03/L-CTN); Luật Phòng không nhân dân 49/2024/QH15 | Hiệp đồng phòng không và không quân |
| 27 | Bảo vệ biển đảo tổng hợp | `[ĐỀ XUẤT]` | Nền: Hải quân là quân chủng ưu tiên | Phối hợp hải quân, không quân, bộ đội biên phòng, dân quân biển; node cuối |
| 28 | Tác chiến mạng và điện tử | `[THẬT]` nền | Đại hội XIII ưu tiên tác chiến điện tử, lực lượng không gian mạng, cơ yếu | Xây nền tảng tác chiến mạng và điện tử |
| 29 | Chỉ huy số hiệp đồng | `[ĐỀ XUẤT]` | Nền: thông tin liên lạc là lực lượng ưu tiên | Chỉ huy trên nền số, hiệp đồng thời gian thực |
| 30 | Chiến tranh thông tin | `[ĐỀ XUẤT]` | Không có nguồn cụ thể | Tác chiến thông tin và phản tuyên truyền |
| 31 | Tác chiến đa miền | `[ĐỀ XUẤT]` | Nền: dự thảo Đại hội XIV nêu tác chiến không gian mạng | Phối hợp bộ, biển, không, mạng; node cuối |

### 9.7. Tầng 5: Capstone (4 biến thể)

| Mô hình | Tên gợi ý | Nhãn | Cơ sở | Nội dung |
| --- | --- | --- | --- | --- |
| Phòng vệ | Quân đội tự vệ hiện đại | `[THẬT]` nền | Mục tiêu 2030: QĐND “cách mạng, chính quy, tinh nhuệ, hiện đại” (Đại hội XIII) | Quân đội chính quy, tinh gọn, tự vệ, hiện đại ở các lĩnh vực ưu tiên |
| Phản ứng nhanh | Lực lượng cơ động chiến lược | `[ALT-HISTORY]` | Mở rộng từ Quân đoàn 12 và Quân đoàn 34 | Lực lượng cơ động nhanh, tác chiến ngoài địa bàn cố định |
| Chiều sâu | Nền quốc phòng toàn dân | `[THẬT]` nền | Cụm “nền quốc phòng toàn dân, thế trận quốc phòng toàn dân” (Đại hội XIII) | Toàn dân tham gia bảo vệ Tổ quốc theo thế trận nhiều tầng |
| Dự bị động viên | Nền quốc phòng động viên | `[ĐỀ XUẤT]` | Mở rộng từ Luật Lực lượng dự bị động viên 2019 | Lực lượng dự bị đủ lớn và đủ nhanh để chuyển từ thời bình sang chiến tranh |

### 9.8. Tầng 6: Hiện đại hóa cao (bản nháp)

Cơ sở: Đại hội XIII đặt “một số quân chủng, binh chủng, lực lượng tiến thẳng lên hiện đại” và mục tiêu quân đội hiện đại từ 2030; Bộ trưởng Quốc phòng nói (1/2026) đã cơ bản đủ điều kiện xây dựng quân đội hiện đại trước 5 năm so với nghị quyết. Mỗi lĩnh vực năng lực đã hoàn thành mở một focus sau capstone; người chơi đi hai trong ba focus, cost 10 tuần mỗi focus, ngân sách khoảng 3,0 điểm gộp mỗi focus (chưa cân bằng chính thức).

| Focus | Điều kiện | Nhãn | Cơ sở | Nội dung |
| --- | --- | --- | --- | --- |
| Biên phòng và lực lượng địa bàn tiến thẳng lên hiện đại | Capstone và `VIE_capability_land` | `[THẬT]` nền | Dự thảo Đại hội XIV nêu Biên phòng là lực lượng ưu tiên hiện đại hóa | Hiện đại hóa lực lượng biên phòng và địa bàn |
| Hải quân và Phòng không – Không quân tiến thẳng lên hiện đại | Capstone và `VIE_capability_seaair` | `[THẬT]` nền | Đại hội XIII và dự thảo Đại hội XIV | Hiện đại hóa hải quân, phòng không, không quân |
| Tác chiến điện tử và không gian mạng tiến thẳng lên hiện đại | Capstone và `VIE_capability_cyber` | `[THẬT]` nền | Đại hội XIII: thông tin liên lạc, tác chiến điện tử, trinh sát kỹ thuật, không gian mạng, cơ yếu | Hiện đại hóa tác chiến điện tử và không gian mạng |

Tầng này chỉ cho modifier, không cộng tech hay mẫu vì trang bị thuộc Trục 1 (mục 3.7). Người chơi đi 2 focus nên tổng cost lên khoảng 184 tuần.

### 9.9. Điều cần xác minh hoặc bạn quyết

- **Mốc Nghị quyết 05.** Nguồn báo Pháp luật Việt Nam ghi Nghị quyết 05 ngày 17/1/2022 về tổ chức QĐND giai đoạn 2021–2030; mục 3.10 hiện ghi “2025–2030” theo một nguồn khác và cố ý bỏ mốc năm. Đề nghị cập nhật #1 thành `[THẬT]` với ngày 17/1/2022 và tách mốc mục B ở 3.10: #1 theo 2022, #2 theo 5/2/2025.
- **Ngày hiệu lực Luật Dân quân tự vệ 2009.** Hai nguồn ghi 1/7/2010, một dự thảo của Bộ Quốc phòng ghi 1/1/2010; bản này dùng 1/7/2010.
- **Nghị quyết 28-NQ/TW năm 2013** (Chiến lược bảo vệ Tổ quốc) có nguồn ghi ngày 25/10/2013, nguồn khác ghi 25/01/2013; chưa dùng trong bản này.
- **Hình mẫu Trung Quốc, Hàn Quốc và “lực lượng phòng vệ”** chỉ là gợi ý thiết kế, chưa tra nguồn; danh sách nước đối tác đào tạo (R2) cũng vậy.
- **Quân đoàn 12 và 34** là quân đoàn chủ lực thật, nên Q2 không còn là hướng giả định: nếu muốn giữ khác biệt giữa người chơi chọn Q và không chọn Q, cần quyết event nền cho mọi người chơi hay chỉ mở ở nhánh Q.

### 9.10. Ánh xạ sang bản chính (mục VIII)

| Nội dung ở 9.3–9.8 | Vị trí trong mục VIII |
| --- | --- |
| #1 Cải cách quân đội | N1 |
| #2 Hợp nhất Hậu cần – Kỹ thuật | N2 (focus khái quát cộng event 5/2/2025) |
| #3 Chỉ huy tác chiến hiệp đồng | CR1 (cơ sở: Bộ Tổng Tham mưu, Nghị quyết 109-NQ/QUTW) |
| G0 Cải cách đào tạo sĩ quan; R3 Chuyên nghiệp hóa quân nhân | N3 (Nghị quyết 109, 1657; Luật Quân nhân chuyên nghiệp, Luật Nghĩa vụ quân sự) |
| R1 Học viện và đào tạo chính quy | Node “đào tạo” của Bộ binh, Tăng thiết giáp, Pháo binh (BB2, TG2, PB2) |
| R2 Trao đổi sĩ quan, đào tạo nước ngoài | Nhóm decision chung (8.14): diễn tập song phương, gìn giữ hòa bình |
| M1 Giáo dục quốc phòng – an ninh toàn dân | Event nền (9.2) và nền của PT |
| M2 Huấn luyện tại chỗ; M3 Cán bộ dân quân và công trình phòng thủ | FD2 và PT |
| Q1–Q3 Phản ứng nhanh | FM1, FM2 (nền Quân đoàn 12, 34) và PS |
| V1–V3 Phòng vệ | FR1, FR2 và PT |
| C1–C3 Chiều sâu | FD1, FD2 |
| B1–B3 Dự bị động viên | PT và decision Động viên toàn dân (Luật 53/2019/QH14) |
| #20–#23 Biên giới và Đô thị | L1, L2 |
| #24, #25, #27 (Biển & Trời) | Bỏ khỏi Lục quân (thuộc Hải quân, Không quân) |
| #26 Phòng không – Không quân hiệp đồng | A2 (Hiệp đồng phòng không), với A1 Phòng không lục quân |
| #28–#31 Mạng và Điện tử | Y1, Y2 (bỏ “Tác chiến đa miền”) |
| 9.7 Capstone 4 biến thể | 3 biến thể theo FR1, FM1, FD1; Dự bị nằm trong PT |
| 9.8 Tầng 6 Hiện đại hóa cao | MOD và CR3 (mỗi lĩnh vực đã hoàn thành cho phần thưởng) |

## Nguồn

Lịch sử hợp đồng và sản phẩm (Trục 1, 2):

- [Jane's: Nga hoàn tất giao 64 T-90S/SK](https://www.janes.com/defence-news/news-detail/russia-completes-delivery-of-t-90ssk-tanks-to-vietnam) — ký 2016, giao 12/2018 và 02/2019, ≈ 250 triệu USD, tín dụng Nga
- [KED Global: Hanwha gần chốt hợp đồng K9](https://www.kedglobal.com/newsView/ked202501200011) — ≈ 276 triệu USD, 20–30 xe, đánh giá 02/2023, huấn luyện 11/2024
- [Wikipedia: trang bị Lục quân Việt Nam](https://en.wikipedia.org/wiki/List_of_equipment_of_the_Vietnam_People%27s_Ground_Forces) — K9 20 xe qua KOTRA, TL-01 tại Z131, dòng PTH, XCB-01, BM-21, T-72 Ba Lan, T-54/55 Phần Lan, STV tại Z111, Spike
- [Tank Encyclopedia: T-54M3 và T-55M3](https://tanks-encyclopedia.com/t-54m3-and-t-55m3/) — VN đề nghị mẫu thử năm 2009, mẫu thử 2010
- [Army Recognition: VN dừng gói nâng cấp của Israel](https://www.armyrecognition.com/focus-analysis-conflicts/army/analysis-defense-and-security-industry/vietnam-no-longer-considers-israeli-upgraded-t-54-55-tanks) — giá cao, VN tự làm T-54M
- [Asia Pacific Defense Journal: nâng cấp T-54B trong nước](https://www.asiapacificdefensejournal.com/2019/11/vietnam-increases-pace-on-local-upgrade.html) — Z153, bộ kit IMI
- [Wikipedia: biến thể T-54/T-55](https://en.wikipedia.org/wiki/T-54/T-55_operators_and_variants) — T-54M tại Z153, FCS Indra TIFCS-3BU
- [Defense Studies: Igla cho Việt Nam (2009)](http://defense-studies.blogspot.com/2009/06/igla-for-vietnam.html) — thỏa thuận sản xuất Igla trong nước
- [Maritime Executive (Reuters): VN đưa bệ phóng ra Trường Sa](https://maritime-executive.com/article/vietnam-moving-rocket-launchers-to-spratlys) — hệ thống EXTRA mua từ Israel
- [VOV: khí tài diễu binh 2025](https://vov.gov.vn/modern-military-equipment-mobilised-for-rehearsal-ahead-of-national-day-parade-dtnew-1103972) — XCB-01 do Tổng cục CNQP thiết kế, sản xuất
- [Asian Military Review: Việt Nam](https://www.asianmilitaryreview.com/tag/vietnam-peoples-army/) — xác nhận mua K9A1; PTH-152 ra mắt 08/2025

Văn bản pháp lý và tổ chức quân đội:

- [Thư viện Pháp luật: Pháp lệnh CNQP 02/2008/PL-UBTVQH12](https://m.thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Phap-lenh-cong-nghiep-quoc-phong-2008-02-2008-PL-UBTVQH12-62388.aspx) — ký 26/01/2008
- [Đại biểu Nhân dân: từ Nghị quyết 27-NQ/TW đến Pháp lệnh CNQP](https://daibieunhandan.vn/print/10266505.html)
- [Đại biểu Nhân dân: Luật 38/2024/QH15](https://daibieunhandan.vn/kip-thoi-thong-nhat-va-hieu-qua-10350612.html) — thông qua 27/06/2024, hiệu lực 01/07/2025
- [Báo Chính phủ: công bố Quyết định sáp nhập Tổng cục Hậu cần và Tổng cục Kỹ thuật](https://baochinhphu.vn/bo-quoc-phong-sap-nhap-tong-cuc-hau-can-va-tong-cuc-ky-thuat-10225020511244099.htm) — Trục 3 #2
- [Báo Quân đội nhân dân: tinh gọn tổ chức, biên chế công tác hậu cần – kỹ thuật](https://www.qdnd.vn/quoc-phong-an-ninh/xay-dung-quan-doi/tinh-gon-to-chuc-bien-che-thuc-hien-thang-loi-nhiem-vu-cong-tac-hau-can-ky-thuat-trong-tinh-hinh-moi-815137) — Trục 3 #1, #2
- [Đại biểu Nhân dân: Quân chủng Phòng không – Không quân, Quyết định 50/QĐ](https://daibieunhandan.vn/thu-tuong-pham-minh-chinh-phong-khong-khong-quan-viet-nam-khong-so-bat-cu-ke-thu-nao-da-ra-quan-la-chien-thang-10391202.html) — Trục 3 #26
- [Nhân Dân: Quân chủng Phòng không – Không quân, Sắc lệnh 03/L-CTN năm 1999](https://special.nhandan.vn/quan-chung-PKKQ-buoc-phat-trien-moi-cua-QDND-Viet-Nam/index.html) — Trục 3 #26

Millennium Dawn:

- [AGENTS.md](https://github.com/MillenniumDawn/Millennium-Dawn/blob/main/AGENTS.md) — quy ước event, decision, focus, guard phá sản, `cancel_if_invalid` mặc định
- [Scripted Effects Reference](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/scripted-effects-reference/) — `modify_treasury_effect`, `modify_debt_effect`, `one_state_arms_factory`, hệ thống ETD
- [Code Resources](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/code-resource/) — modifier chi phí tiền của MD (cái giá doctrine A)
- [OOB & Equipment Variants Reference](https://github.com/MillenniumDawn/Millennium-Dawn/blob/main/.claude/docs/oob-variants-reference.md) — bảng chassis ↔ ID, NSB / non-NSB, `equipment_bonus`
- [Game Rules](https://github.com/MillenniumDawn/Millennium-Dawn/blob/main/docs/src/content/tutorials/game-rules.md) — `historic_events`, `rule_salafist_branch`

Trục 3 chọn dần (mục IX):

- [Thư viện Pháp luật: Luật Dân quân tự vệ 2009 (43/2009/QH12)](https://thuvienphapluat.vn/van-ban/bo-may-hanh-chinh/luat-dan-quan-tu-ve-nam-2009-98743.aspx?temp=d) — ký 23/11/2009
- [Caselaw: Luật Dân quân tự vệ 2019 (48/2019/QH14)](https://caselaw.vn/van-ban-phap-luat/328401-luat-dan-quan-tu-ve-so-48-2019-qh14-ngay-22-11-2019-cua-quoc-hoi?en=true) — ký 22/11/2019, hiệu lực 1/7/2020
- [Thư viện Pháp luật: 11 luật thông qua ngày 20/11/2019](https://thuvienphapluat.vn/hoi-dap-phap-luat/11-luat-duoc-quoc-hoi-thong-qua-tai-ky-hop-thu-8-ngay-20-11-2019-313578.html) — Luật Lực lượng dự bị động viên 53/2019/QH14 hiệu lực 1/7/2020
- [Luật Việt Nam: văn bản hợp nhất Luật Giáo dục quốc phòng và an ninh](https://luatvietnam.vn/an-ninh-quoc-gia/van-ban-hop-nhat-140-vbhn-vpqh-nam-2025-do-van-phong-quoc-hoi-ban-hanh-hop-nhat-luat-giao-duc-quoc-phong-va-an-ninh-411072-d5.html) — 30/2013/QH13 hiệu lực 1/1/2014; Luật 98/2025/QH15
- [Báo Pháp luật: Quân đoàn 12 “tinh, gọn, mạnh”, tiến lên hiện đại](https://baophapluat.vn/quan-doan-12-tinh-gon-manh-tien-len-hien-dai-post497672.html) — Nghị quyết 05 (17/1/2022), Nghị quyết 230 (2/4/2022)
- [SGGP: công bố thành lập Quân đoàn 12](https://www.sggp.org.vn/bo-quoc-phong-cong-bo-quyet-dinh-thanh-lap-quan-doan-12-post716653.html) — QĐ 6012/QĐ-BQP, lễ công bố 2/12/2023
- [VOV: Chủ tịch nước làm việc với Quân đoàn 12](https://vov.vn/chinh-tri/chu-tich-nuoc-lam-viec-voi-don-vi-quan-doi-dau-tien-thuc-hien-tinh-gon-manh-post1186920.vov) — thành lập 21/11/2023, quân đoàn chủ lực cơ động chiến lược
- [Báo Lào Cai: công bố thành lập Quân đoàn 34](https://baolaocai.vn/dai-tuong-phan-van-giang-du-le-cong-bo-quyet-dinh-thanh-lap-quan-doan-34-post394811.html) — QĐ 5989/QĐ-BQP, lễ 15/12/2024
- [Quản lý nhà nước: xây dựng quân đội cách mạng, chính quy, tinh nhuệ, từng bước hiện đại](https://www.quanlynhanuoc.vn/?p=18852) — mục tiêu Đại hội XIII: 2025 tinh, gọn, mạnh; 2030 hiện đại
- [Hà Tĩnh: xây dựng quân đội vững mạnh nhưng không tạo gánh nặng](https://hatinh.gov.vn/vi/bai-viet/xay-dung-quan-doi-vung-manh-nhung-khong-tao-ganh-nang-cho-nen-kinh-te) — danh sách lực lượng ưu tiên tiến thẳng lên hiện đại
- [Đại biểu Nhân dân: dự thảo Văn kiện Đại hội XIV](https://daibieunhandan.vn/print/10403749.html) — ưu tiên Hải quân, Phòng không – Không quân, Tác chiến điện tử, Tác chiến không gian mạng, Biên phòng
- [Tuổi Trẻ: Bộ trưởng Quốc phòng về điều chỉnh tổ chức quân đội (1/2026)](https://tuoitre.vn/dai-tuong-phan-van-giang-co-ban-hoan-thanh-dieu-chinh-to-chuc-quan-doi-tinh-gon-manh-20260121213707528.htm)
- [Tuổi Trẻ: Sách trắng Quốc phòng 2019](https://tuoitre.vn/viet-nam-cong-bo-sach-trang-quoc-phong-2019-20191125220311349.htm) — công bố 25/11/2019; hòa bình và tự vệ
- [RFA: Sách trắng 2019 và chính sách bốn không](https://www.rfa.org/vietnamese/news/vietnamnews/vietnam-released-new-white-paper-11252019090956.html)
- [Báo Pháp luật: Cục Gìn giữ hòa bình 11 năm](https://baophapluat.vn/cuc-gin-giu-hoa-binh-viet-nam-11-nam-thuc-hien-su-menh-gin-giu-hoa-binh-lien-hop-quoc-post550047.html) — 27/5/2014, hai sĩ quan đầu tiên
- [Báo Pháp luật: hai sĩ quan tới Nam Sudan](https://baophapluat.vn/hai-si-quan-viet-nam-dang-tren-duong-toi-nam-sudan-post178569.html) — quyết định thành lập Trung tâm 4/12/2013
- [Tuổi Trẻ: hai sĩ quan Việt xuất ngoại gìn giữ hòa bình](https://tuoitre.vn/hai-si-quan-viet-xuat-ngoai-gin-giu-hoa-binh-609327.htm) — khóa học ở Úc, Anh, Mông Cổ
- [VUFO: lực lượng gìn giữ hòa bình](https://vufo.org.vn/Luc-luong-gin-giu-hoa-binh-Lan-toa-cac-gia-tri-tot-dep-cua-Viet-Nam-toi-ban-be-quoc-te-2057-97695.html?lang=vn) — Bệnh viện dã chiến (10/2018), Đội Công binh (5/2022)
- [Quản lý nhà nước: tăng cường giáo dục, đào tạo trong quân đội](https://www.quanlynhanuoc.vn/2024/01/30/tang-cuong-cong-tac-giao-duc-va-dao-tao-dap-ung-yeu-cau-nhiem-vu-xay-dung-quan-doi-trong-tinh-hinh-moi) — Nghị quyết 1657-NQ/QUTW (20/12/2022), Quyết định 3525/QĐ-BQP
- [Quản lý nhà nước: đội ngũ nhà giáo trong quân đội](https://www.quanlynhanuoc.vn/2023/01/12/xay-dung-doi-ngu-nha-giao-dap-ung-yeu-cau-doi-moi-can-ban-toan-dien-giao-duc-dao-tao-trong-quan-doi) — Nghị quyết 109-NQ/QUTW (11/2/2019), Chiến lược giáo dục, đào tạo 2021–2030
- [Báo Pháp luật: phát triển kinh tế gắn với quốc phòng, an ninh](https://baophapluat.vn/phat-trien-kinh-te-phai-gan-voi-quoc-phong-an-ninh-post129411.html) — Nghị quyết 28-NQ/TW (22/9/2008) về khu vực phòng thủ
