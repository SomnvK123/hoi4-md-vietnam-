# Tái cấu trúc nhánh kinh tế, tách nhánh xã hội, và bỏ sáu dải chế độ giả định

> Đầu vào: đề xuất của tác giả (chia kinh tế theo ngành: công nghiệp nặng, công nghiệp phụ trợ, internet, khoa học, công nghệ, tài chính – ngân hàng, thiên tai, năng lượng gồm Petrolimex và điện, hạ tầng giao thông; tách giáo dục thành nhánh riêng; Luật Doanh nghiệp chia thành doanh nghiệp nhà nước và tư nhân; bỏ sáu dải chế độ). Code đo ngày 26/9/2026.
> Đi cùng `VIE_congress_spine_redesign.md`. Mục 6 ghi những gì báo cáo đó phải sửa theo.
>
> Nhãn: **[SỰ KIỆN]** đo được trong code hoặc có văn bản gốc · **[TIỀN ĐỀ KỊCH BẢN]** quyết định thiết kế · **[CẦN THỬ]** chưa kiểm chứng trong game

---

## 0. Trả lời ngắn

**Có nên thiết kế lại nhánh kinh tế không? Có, nhưng là tái cấu trúc, không phải viết lại.** Việc thiết kế lại nhánh chính trị không bắt buộc phải sửa nhánh kinh tế, vì nhánh kinh tế chạy theo ngày và dùng được dưới mọi chế độ. Lý do thật để sửa nằm ở chính nhánh kinh tế: đo code thấy **9 lỗi cấu trúc** (mục 1.2). Ví dụ y tế, lao động và văn hóa đều nằm dưới focus giáo dục; khu vực tư nhân mọc ra từ SCIC, tức cơ quan quản lý vốn nhà nước; thép nằm dưới công nghiệp hỗ trợ.

Cách chia theo ngành bạn đề xuất khớp với nội dung sẵn có: **127 focus hiện tại xếp được hết vào các nhóm đó**, khoảng 95% giữ nguyên ID và phần thưởng. Việc chính là đổi gốc, đổi cha và xếp lại cột.

Ba điểm tôi đề xuất khác hoặc thêm vào danh sách của bạn:

1. **Giữ hai nhánh bạn chưa nhắc:** Nông nghiệp – đất đai (5 focus: xuất khẩu gạo, nông thôn mới, Luật Đất đai…) và Hội nhập – FDI (7 focus: BTA, WTO, CPTPP, EVFTA). Bỏ chúng là mất trục chính của kinh tế Việt Nam 2000–2026.
2. **Tách giáo dục thành nhánh riêng thì phải tách luôn y tế, lao động – xã hội và văn hóa – du lịch**, vì hiện cả bốn cùng mọc từ `education_reform`. Bốn nhánh này gộp thành khối Xã hội, mỗi nhánh một gốc.
3. **Bỏ sáu dải chế độ không có nghĩa là bỏ các event lịch sử mở ra chúng.** Dự thảo Luật Đặc khu (6/2018), làn sóng rút tiền ngân hàng, khủng hoảng giàn khoan là chuyện có thật. Chỉ bỏ lựa chọn "mở dải", giữ event.

Quy mô: nhánh kinh tế 107 → **109 focus** (+2 mới); khối Xã hội 20 → **21 focus** (+1 mới); dải chế độ 106 → **30 focus** (−76).

---

## 1. Hiện trạng đo được

### 1.1 Nhánh kinh tế – xã hội hiện nay

**[SỰ KIỆN]** 127 focus ở cột x 130–254, hàng 0–8. Tổng chi phí 1.016 tuần. **55 focus (43%) không có mốc năm**, trong khi khối chính trị hầu như focus nào cũng có. Về đồ thị, kinh tế nằm trong một thành phần liên thông khổng lồ 101 focus, trộn chung với ngoại giao và xã hội, cộng thêm bốn cụm nhỏ (DNNN – tư nhân, năng lượng, công nghiệp, đích 2045).

### 1.2 Chín lỗi cấu trúc

| # | Lỗi | Bằng chứng |
|---|---|---|
| 1 | **Xã hội mọc từ giáo dục** | `universal_health_insurance`, `urbanization`, `heritage_preservation` đều có cha là `education_reform`. Muốn làm bảo hiểm y tế phải làm cải cách giáo dục trước |
| 2 | **Tư nhân mọc từ SCIC** | `private_champions`, `household_business` có cha là `scic` (Tổng công ty Đầu tư và Kinh doanh Vốn Nhà nước) |
| 3 | **Công nghiệp nặng nằm dưới công nghiệp hỗ trợ** | `formosa_steel_complex` có cha `supporting_industries`; `hoa_phat_hrc_steel` nằm dưới Formosa. Thép là thượng nguồn của công nghiệp hỗ trợ, không phải ngược lại |
| 4 | **Chuyển đổi năng lượng nằm dưới thiên tai** | `jetp_partnership` có cha `disaster_preparedness`; `net_zero_2050` nằm dưới JETP |
| 5 | **Luật Doanh nghiệp là gốc của mọi thứ** | `enterprise_law` là cha của BTA, sàn HOSE, xuất khẩu gạo, cổ phần hóa, Luật Đầu tư. Doanh nghiệp, hội nhập, tài chính và nông nghiệp trộn vào nhau |
| 6 | **Năng lượng và giao thông đan xen** | Cùng dải cột 196–214: metro Hà Nội (206) nằm giữa Petrolimex (204) và nhà máy điện hạt nhân (204–206) |
| 7 | **Ba focus Đồng bằng sông Cửu Long chồng nội dung** | `mekong_climate_adaptation` (nông nghiệp) và `nature_adaptation_120` + `dutch_water_model` (thiên tai) cùng mô tả cống ngăn mặn và chuyển lúa sang tôm, tức nội dung NQ 120/NQ-CP (2017) |
| 8 | **Viettel ra nước ngoài nằm dưới nhà máy wafer** | `viettel_global` (mạng viễn thông ở Lào, Campuchia, Peru… từ 2006) có cha `semiconductor_fab` |
| 9 | **NQ 57 và NQ 68 có ở hai nơi** | Đã ghi ở báo cáo Đại hội: `resolution_57_68` (chính trị) trùng `science_breakthrough` và `private_sector_engine` |

---

## 2. Cấu trúc đề xuất

### 2.1 Tổng thể

`VIE_doi_moi_continues` giữ vai trò gốc chung. Mỗi nhánh có gốc riêng, cần `doi_moi_continues`. Không nhánh nào phải đi qua nhánh khác mới mở được; liên kết giữa các nhánh dùng `available` hoặc giảm chi phí (mục 5), không dùng prerequisite.

```text
                                  TIẾP TỤC ĐỔI MỚI (160,0)
                                            │
 ┌──────────┬──────────┬──────────┬─────────┼─────────┬──────────┬──────────┬──────────┬──────────┐
DOANH      HỘI NHẬP   TÀI CHÍNH  CÔNG       NĂNG      HẠ TẦNG   NÔNG       THIÊN     INTERNET   CÔNG      KHOA
NGHIỆP     – FDI                 NGHIỆP     LƯỢNG     GIAO       NGHIỆP     TAI       – SỐ       NGHỆ      HỌC
│                                │          │         THÔNG                                     (bán dẫn)
├ DNNN                ├ Ngân hàng ├ Nặng     ├ Dầu khí
└ Tư nhân             └ Vốn và    ├ Chế tạo  ├ Petrolimex
                        thanh toán│  – ô tô  └ Điện
                                  └ Phụ trợ
                                                                     ĐÍCH 2030 / 2045

 KHỐI XÃ HỘI:   GIÁO DỤC     Y TẾ     LAO ĐỘNG – XÃ HỘI     VĂN HÓA – DU LỊCH
```

| Nhánh | Nhánh con | Focus | Chi phí (tuần) | Thay đổi chính |
|---|---|---|---|---|
| Doanh nghiệp | gốc Luật DN · DNNN · Tư nhân | 9 | 60 | Tư nhân tách khỏi SCIC |
| Hội nhập – FDI | — | 7 | 52 | Tách khỏi Luật DN |
| Tài chính | Ngân hàng · Vốn và thanh toán | 12 | 84 | Nhận HOSE và thanh toán không tiền mặt |
| Công nghiệp | Nặng · Chế tạo – ô tô · Phụ trợ | 15 | 108 | Đảo thứ tự nặng/phụ trợ; Nghi Sơn chuyển sang Năng lượng; +1 focus đóng tàu |
| Năng lượng | Dầu khí · Petrolimex · Điện | 21 | 163 | Nhận Nghi Sơn, JETP và Net Zero; +1 focus lọc dầu Dung Quất |
| Hạ tầng giao thông | — | 8 | 68 | Tách cột khỏi năng lượng |
| Nông nghiệp – đất đai | — | 5 | 33 | Gỡ chồng lấn ĐBSCL |
| Thiên tai | — | 8 | 59 | Trả JETP, Net Zero cho năng lượng |
| Internet – số | — | 8 | 59 | Nhận `viettel_global` |
| Công nghệ (bán dẫn) | — | 5 | 41 | Gốc là `intel_hcmc` |
| Khoa học | — | 6 | 43 | Giữ |
| Đích 2030/2045 | — | 5 | 41 | Giữ |
| **Kinh tế** | | **109** | **811** | 107 cũ + 2 mới |
| Giáo dục | — | 6 | 39 | **Nhánh riêng**; +1 focus NQ 29 |
| Y tế | — | 5 | 34 | Gốc riêng |
| Lao động – xã hội | — | 5 | 36 | Gốc riêng |
| Văn hóa – du lịch | — | 5 | 34 | Gốc riêng |
| **Xã hội** | | **21** | **143** | 20 cũ + 1 mới |

### 2.2 Chi tiết từng nhánh

Ký hiệu: **gốc** = focus gốc của nhánh (cần `doi_moi_continues`); **đổi cha** = prerequisite mới; **+năm** = thêm `available = { date > … }`; **★** = focus mới.

**Doanh nghiệp.** Luật Doanh nghiệp 1999 (hiệu lực 1/1/2000) là gốc, tách thành hai nhánh con.

| Nhánh con | Focus theo thứ tự | Ghi chú |
|---|---|---|
| gốc | `enterprise_law` | Chỉ giữ hai con: DNNN và Tư nhân |
| DNNN | `equitization_soes` → `state_conglomerates` (+năm 2005, mô hình tập đoàn QĐ 2005–2006) → `scic` (2005) → `soe_governance` (2017) | `state_conglomerates` thôi là gốc tự do. Event Vinashin gắn với nhánh này (mục 2.2, Công nghiệp) |
| Tư nhân | `investment_law_2005` → `household_business` (2020) → `private_champions` → `private_sector_engine` (NQ 68, 2025) | **Đổi cha**: bỏ `scic`. `private_champions` +năm 2017 (NQ 10-NQ/TW về kinh tế tư nhân) |

**Hội nhập – FDI.** Gốc `bilateral_trade_agreement_usa` (BTA 2000, hiệu lực 12/2001) → `fdi_attraction` → `wto_negotiations` → `wto_reforms` → `export_powerhouse`; nhánh bên `cptpp_member`, `evfta`. BTA đổi cha từ `enterprise_law` thành `doi_moi_continues`. Có thể cân nhắc chuyển nhánh này sang cây ngoại giao; báo cáo giữ ở kinh tế vì phần thưởng chủ yếu là kinh tế.

**Tài chính.**

| Nhánh con | Focus |
|---|---|
| Ngân hàng | **Giữ nguyên đồ thị:** gốc `state_bank_modernization`; mạch `fight_inflation` (2008) → `deposit_insurance` và mạch `restructure_banking` (2011) → `vamc` (2013), hội tụ ở `cross_ownership_crackdown` |
| Vốn và thanh toán | `hose_exchange` (7/2000, **đổi cha** từ Luật DN) → `corporate_bond_reform` (2022, **đổi cha** từ `vamc`) → `market_upgrade_criteria` → `international_financial_centre` → `investment_grade`; `cashless_payments` (2016, **đổi cha** từ `internet_expansion`, vì đây là chính sách của NHNN) |

**Công nghiệp.** Thứ tự thượng nguồn → hạ nguồn: nặng cung cấp vật liệu cho phụ trợ, phụ trợ cung cấp linh kiện cho chế tạo.

| Nhánh con | Focus | Ghi chú |
|---|---|---|
| Nặng | Ba mạch gốc: thép `formosa_steel_complex` (**đổi cha**: bỏ `supporting_industries`) → `hoa_phat_hrc_steel`; khoáng sản `rare_earths` (**đổi cha**: bỏ `petrovietnam_expansion`) → `bauxite_tay_nguyen`; ★ `VIE_shipbuilding_vinashin` | `nghi_son_refinery` chuyển sang Năng lượng |
| Chế tạo – ô tô | gốc `samsung_partnership` (**đổi cha** từ WTO; cần `available` WTO) → `china_plus_one` → `manufacturing_hub`; `domestic_automotive` → `ev_revolution_batteries` → `global_auto_export` | Ô tô đặt ở chế tạo vì VinFast là doanh nghiệp lắp ráp; linh kiện nằm ở phụ trợ |
| Phụ trợ | gốc `supporting_industries` → `tier1_vendor_localization`, `precision_mechanics_molds` (**đổi cha** từ thép), `integrated_auto_supplier_park` | `intel_hcmc` chuyển sang Công nghệ |

★ **`VIE_shipbuilding_vinashin` — Công nghiệp đóng tàu.** Cost 7, +năm 2005 (Vinashin được đầu tư mạnh từ 2006). Thưởng công nghiệp và nhà máy đóng tàu. **Cái giá:** là điều kiện để event Vinashin đổ vỡ (2010) mang hậu quả đầy đủ. Không làm focus thì event chỉ còn hậu quả nhẹ. Như vậy lựa chọn của người chơi quyết định mức độ rủi ro, đúng tinh thần event đã có (`VIE_fb_vinashin`).

**Năng lượng.**

| Nhánh con | Focus | Ghi chú |
|---|---|---|
| Dầu khí | gốc `petrovietnam_expansion` → ★ `VIE_dung_quat_refinery` (2009) → `nghi_son_refinery` (2018) | Dung Quất là nhà máy lọc dầu đầu tiên của Việt Nam, hiện chưa có |
| Petrolimex | gốc `petrolimex_downstream_network` (**đổi cha** từ PVN: Petrolimex là doanh nghiệp riêng) → `strategic_petroleum_reserve`, `petrolimex_eneos_partnership` → `petrolimex_green_ev_hubs` | 4 focus, không đổi nội dung |
| Điện | gốc `son_la_dam` → `500kv_grid` → `dppa_market_reform`; `coal_power` (**đổi cha** từ PVN thành `son_la_dam`) → `solar_boom` → `power_plan_8` → `offshore_wind` → `energy_security_2045`; `ninh_thuan_nuclear` → `shelve_nuclear` / `build_nuclear_plant` → `revive_nuclear`; `jetp_partnership` → `net_zero_2050` (**đổi cha** từ thiên tai thành `power_plan_8`) | `net_zero_2050` nhận thêm OR `sustainable_mekong_delta` như cũ để thiên tai vẫn dẫn tới |

★ **`VIE_dung_quat_refinery` — Nhà máy lọc dầu Dung Quất.** Cost 7, +năm 2008 (vận hành 2/2009). Giảm phụ thuộc nhập khẩu xăng dầu; mở `nghi_son_refinery`.

**Hạ tầng giao thông.** Gốc `north_south_expressway` → `lach_huyen_port`, `cai_mep_port` → `lao_cai_haiphong_rail`, `long_thanh_airport` → `north_south_hsr`; `hanoi_metro`, `hcmc_metro`. Chỉ dời sang cột riêng, không đổi prerequisite.

**Nông nghiệp – đất đai.** Gốc `rice_export_power` (**đổi cha** từ Luật DN) → `new_rural_development` (2010) → `high_tech_agriculture` (2015); `land_law_reform` (2013) → `mekong_climate_adaptation`. **Sửa chồng lấn:** `mekong_climate_adaptation` chỉ giữ phần chuyển đổi sản xuất (lúa chịu mặn, lúa sang tôm và trái cây), cần `available` `nature_adaptation_120`. Phần cống ngăn mặn để lại cho `dutch_water_model`.

**Thiên tai.** Gốc `disaster_preparedness` → `military_rescue_corps` → `emergency_operations_center`; `satellite_early_warning` → `storm_resilient_islands`; `nature_adaptation_120` → `dutch_water_model` → `sustainable_mekong_delta`. Mất `jetp_partnership` và `net_zero_2050` (sang Năng lượng). **7/8 focus không có mốc năm**: `nature_adaptation_120` +năm 2017.

**Internet – số.** Gốc `internet_expansion` → `mobile_networks` (5G, 2023); `national_digital_transformation` (2020) → `digital_id` → `national_data_center` → `ai_strategy` → `digital_nation`; `viettel_global` (**đổi cha** từ `semiconductor_fab` thành `internet_expansion`, +năm 2006). `national_digital_transformation` đổi cha từ `cashless_payments` thành `internet_expansion`.

**Công nghệ (bán dẫn).** Gốc `intel_hcmc` (2010) → `semiconductor_ambition` → `chip_design`, `chip_engineers` → `semiconductor_fab`. `chip_engineers` nhận thêm `available` từ nhánh Giáo dục (mục 5).

**Khoa học.** Giữ nguyên: `nafosted` → `research_universities`, `nuclear_research`, `vinasat` → `earth_observation`; `science_breakthrough` (NQ 57).

**Đích 2030/2045.** Giữ nguyên: `upper_middle_income`, `green_growth`, `innovation_nation`, `high_income_2045`, `developed_nation_2045`.

### 2.3 Khối Xã hội

| Nhánh | Focus | Ghi chú |
|---|---|---|
| **Giáo dục** | gốc `education_reform` (đổi tên thành "Chiến lược phát triển giáo dục 2001–2010", QĐ 201/2001) → `english_second_language` (+năm 2008, Đề án Ngoại ngữ quốc gia QĐ 1400) → ★ `VIE_education_nq29` (+năm 2013) → `university_autonomy` (+năm 2014, NQ 77/NQ-CP) → `free_tuition` (2025); `vocational_training` (+năm 2014, Luật Giáo dục nghề nghiệp) | ★ **NQ 29-NQ/TW (11/2013) "Đổi mới căn bản, toàn diện giáo dục"**: mốc lớn nhất của giáo dục giai đoạn này, hiện chỉ có trong tên focus gốc |
| **Y tế** | gốc `universal_health_insurance` (**đổi cha** từ giáo dục) → `grassroots_clinics` → `hospital_decongestion`, `vaccine_production` → `preventive_health` | Luật BHYT 2008 (+năm 2008) |
| **Lao động – xã hội** | gốc `urbanization` (**đổi cha**) → `labor_code_2019`, `social_insurance_reform` → `population_policy` → `overseas_vietnamese` | `labor_code_2019` là focus; event `vie_pol.27` đã thêm là quyết định phê chuẩn ILO. Cần gộp: focus đọc cờ `VIE_labor_convention_ratified` thay vì làm lại việc đó |
| **Văn hóa – du lịch** | gốc `heritage_preservation` (**đổi cha**) → `sea_games_bid` (2003), `visa_reform` (2023) → `cultural_industry` → `tourism_powerhouse` | Giữ |

**Tổng sau thiết kế:** kinh tế 107 + 2 mới = **109**; xã hội 20 + 1 mới = **21**; tổng **130 focus** (127 cũ + 3 mới). Chi phí thêm 21 tuần, từ 1.016 lên 1.037 tuần (khoảng 20 năm focus cho 26 năm lịch sử, cạnh tranh với chính trị, ngoại giao và quốc phòng: người chơi vẫn phải chọn).

### 2.4 Ba lựa chọn loại trừ trong nhánh kinh tế (tùy chọn)

Bỏ các dải Kiến tạo, Đặc khu, Tài phiệt là bỏ luôn ba mô hình kinh tế thay thế duy nhất của mod. Nhánh kinh tế lịch sử hiện chỉ có một cặp loại trừ (điện hạt nhân: xây / gác lại). Nếu muốn giữ lựa chọn kinh tế mà không cần dải chế độ, có thể thêm cặp loại trừ **bên trong** nhánh lịch sử, mỗi cặp có một bên lịch sử:

| Nhánh | Lịch sử | Phương án khác | Căn cứ |
|---|---|---|---|
| DNNN | Giữ tập đoàn, cổ phần hóa chậm | Thoái vốn nhanh qua SCIC | Tranh luận thật quanh NQ 12-NQ/TW (2017) |
| Điện | Theo Quy hoạch điện VII: nhiệt điện than là trụ | Chuyển nhanh sang năng lượng tái tạo trước 2020 | Quy hoạch điện VIII (2023) chính là sự điều chỉnh này |
| Ngân hàng | NHNN mua lại ngân hàng yếu kém giá 0 đồng (2015) | Cho phá sản có kiểm soát | Luật TCTD sửa đổi 2017 đã mở khả năng phá sản |

Đây là đề xuất, **không nằm trong khối lượng chính**. Cặp thứ ba khác với dải "Giải cứu ngân hàng" bạn muốn bỏ: dải đó là chế độ tài phiệt nắm quyền, còn cặp này là chính sách của NHNN.

---

## 3. Bỏ sáu dải chế độ

### 3.1 Dấu chân đo được

**[SỰ KIỆN]**

| Dải | Gốc | Focus | Idea | Event do focus bắn | Mở bởi | Slot đảng |
|---|---|---|---|---|---|---|
| Bảo vệ nền tảng | `defend_the_foundation` | 6 | 4 | `vie_alt.4` | `vie_pol.2.b` (Đại hội IX) hoặc BoP cứng rắn | 4 |
| Tự chủ chiến lược | `tc_strategic_autonomy` | 15 | 6 | `vie_alt.10`, `.11`, `vie_dip.18`, `vie_int.1`, `.10` | `vie_alt.1` (sau giàn khoan HD-981) | — |
| Nhà nước kiến tạo | `developmental_state` | 15 | 7 | — | `vie_pol.5.b` (Đại hội XII) hoặc BoP cải cách | — |
| Luật Đặc khu | `lb_sez_law` | 13 | 6 | `vie_alt.8`, `.25`, `.26` | `vie_alt.6` (dự thảo Luật Đặc khu 2018) | 16 |
| Giải cứu ngân hàng | `ol_bailout` | 12 | 5 | `vie_alt.27`, `.28` | `vie_alt.3`, `.7`, `.9`, `vie_axis.1` | 15 |
| Hội đồng Phát triển | `wa_development_council` | 15 | 6 | `vie_alt.29`, `.30`, `vie_int.3` | `vie_alt.31`; cần `pivot_to_the_west` | 0 |
| **Tổng** | | **76** | **34** | **16** | | |

Không dải nào có prerequisite từ ngoài dải, nên xóa focus không làm treo cây khác. Nhưng dải được nối vào 5 nơi khác: event mở cửa, event Đại hội, power balance, decision và luật chơi AI.

### 3.2 Cách xử lý từng phần

| Thành phần | Xử lý |
|---|---|
| 76 focus, 34 idea và loc | **Xóa** |
| 16 event do focus bắn | **Xóa**, sau khi kiểm tra từng event không được gọi từ nơi khác (`vie_dip.18`, `vie_int.1`, `.3`, `.10` thuộc namespace dùng chung) |
| `vie_alt.1` Sau khủng hoảng giàn khoan | **Giữ event** (HD-981 là sự kiện thật). Bỏ option đặt `VIE_tc_unlocked` |
| `vie_alt.6` Dự thảo Luật Đặc khu | **Giữ event.** Lịch sử: dự luật bị hoãn sau biểu tình 6/2018. Bỏ option "thông qua luật → mở dải"; nếu muốn giữ một phương án khác lịch sử thì chỉ để lại hệ quả trực tiếp (ổn định, trục `decent`) |
| `vie_alt.3` Khủng hoảng niềm tin, `vie_alt.7` Rút tiền hàng loạt | **Giữ event** (vụ SCB 10/2022 là thật). Bỏ phần đặt `VIE_oligarch_unlocked` |
| `vie_alt.9` Nhà đầu tư nắm quyền chi phối | **Xóa** (chuyển thẳng sang slot 15) |
| `vie_axis.1` Kiến tạo trượt thành Tài phiệt | **Xóa** (cả hai đầu cạnh đều bị bỏ) |
| `vie_alt.31` Rò rỉ hồ sơ giám sát | Kiểm tra: nếu chỉ dùng để mở Hội đồng Phát triển thì xóa, nếu còn nhánh sang dải An ninh thì chỉ bỏ cờ `VIE_wa_unlocked` |
| `vie_pol.2.b`, `vie_pol.5.b` (Đại hội IX, XII) | **Giữ như biến thể đường lối trong Đảng**, bỏ phần mở dải. Xem mục 6 |
| Power balance `VIE_md_bop_p3.txt` (Tập đoàn ↔ Dân chúng) | **Xóa** cả file và mọi lệnh dịch thanh này |
| Decision `VIE_ol_credit_squeeze` và danh mục `VIE_oligarch_category` | **Xóa** |
| 4 lệnh chuyển chế độ sang slot 0, 4, 15, 16 trong focus; 2 trong event | Xóa cùng focus/event chứa chúng. **Slot 4 không bị xóa**: `VIE_party_rule_active` vẫn coi slot 4 là Đảng cầm quyền |
| Luật chơi AI | Bỏ option `VIE_AUTONOMY` và `VIE_FREE_ZONES` cùng trọng số trong `RANDOM`. `VIE_NATIONALIST` **đã rỗng từ trước** (dải `np_*`/`lh_*` không còn trong code) nên bỏ luôn. Giữ `HARDLINE` (dải An ninh dùng) và `WESTERN` (ngoại giao, quốc phòng dùng) |
| Trigger, effect riêng của các dải (`VIE_md_effects_p3.txt`, `_axis.txt`, `_p2.txt`) | Xóa đoạn tham chiếu; giữ phần dùng chung |

### 3.3 Hệ quả

Sau khi bỏ, dải chế độ giả định còn **30 focus**: Dân chủ hóa (`round_table_talks`, 22) và Nhà nước An ninh (`sec_cyber_control`, 8), cộng ngã rẽ 2026 ở khối chính trị. Không còn con đường giả định nào về mô hình kinh tế.

Đây là thay đổi lớn về tính chơi lại. Nếu sau này muốn thêm con đường giả định mới, nên thiết kế lại cả dải chế độ một lần (như đã làm với nhánh dân tộc chủ nghĩa), không vá từng dải.

---

## 4. Ràng buộc phải giữ

**Trục.** Sáu dải bị bỏ đều nằm ngoài đường lịch sử, nên hồ sơ trục lịch sử của STEP6 không đổi. Tái cấu trúc kinh tế chỉ đổi prerequisite và tọa độ; 3 focus mới không cộng trục. **Cổng trục** của các dải còn lại (Dân chủ, An ninh) không phụ thuộc các dải bị bỏ.

**Thời điểm.** Thêm mốc năm cho focus chưa có sẽ đẩy muộn một số hiệu ứng trục trong hồ sơ giai đoạn (nhiều nhất ở Giáo dục và Thiên tai). Phải chạy lại hồ sơ STEP6 bằng `_gen/axis_map.py` trên máy local.

**Save cũ.** Save đang ở một trong bốn slot bị bỏ (0, 15, 16) sẽ không còn nội dung focus cho chế độ đó. Cần một dòng trong `on_startup`: nếu `ruling_party` là 0, 15 hoặc 16 thì chuyển về chế độ Đảng qua `VIE_transition_regime`, hoặc ghi rõ trong changelog là save cũ ở các chế độ này không tương thích.

**Tham chiếu chéo.** Sau khi bỏ ba focus 2025 ở báo cáo Đại hội và 76 focus dải chế độ, `check_static.py` phải trả 0 lỗi tham chiếu treo.

---

## 5. Liên kết với xương sống Đại hội

Nhánh kinh tế **không** đặt dưới các nghị quyết Đại hội. Kinh tế là chức năng nhà nước dưới mọi chế độ và đang chạy theo ngày, nên khóa nó vào nghị quyết sẽ làm chế độ không phải Đảng mất cả nhánh.

Thay vào đó, dùng liên kết mềm: chính sách kinh tế rẻ hơn nếu nghị quyết tương ứng đã được triển khai. Kỹ thuật: `completion_reward` của focus nghị quyết đặt cờ; focus kinh tế dùng `modifier` trong `ai_will_do` và giảm `cost` qua biến. **[CẦN THỬ]**: HOI4 không cho `cost` động dễ dàng; nếu không làm được thì dùng `completion_reward` cộng thêm khi có cờ.

| Nghị quyết | Focus kinh tế hưởng lợi | Căn cứ |
|---|---|---|
| NQ Đại hội X | `wto_negotiations`, `private_champions` | Đại hội X cho đảng viên làm kinh tế tư nhân; vào WTO 1/2007 |
| NQ Đại hội XI | `restructure_banking`, `equitization_soes` | HNTW3 khóa XI (10/2011): tái cơ cấu ngân hàng, DNNN, đầu tư công |
| NQ Đại hội XII | `soe_governance`, `private_champions` | NQ 10, 11, 12-NQ/TW (6/2017) |
| NQ Đại hội XIII | `science_breakthrough`, `private_sector_engine` | NQ 57 (12/2024), NQ 68 (5/2025) |
| NQ Đại hội XIII | `university_autonomy`, `free_tuition` | NQ 71-NQ/TW (8/2025) về giáo dục và đào tạo |

Liên kết chéo giữa các nhánh (thay cho prerequisite):

| Focus | `available` thêm | Lý do |
|---|---|---|
| `chip_engineers` | `has_completed_focus = VIE_university_autonomy` | Đào tạo kỹ sư cần đại học tự chủ |
| `samsung_partnership` | `has_completed_focus = VIE_wto_negotiations` | Giữ điều kiện cũ sau khi đổi cha |
| `ev_revolution_batteries` | `has_completed_focus = VIE_power_plan_8` | Xe điện cần lưới điện |
| `labor_code_2019` | đọc cờ `VIE_labor_convention_ratified` để trao thêm thưởng | Gộp với `vie_pol.27` |

---

## 6. Những gì `VIE_congress_spine_redesign.md` phải sửa theo

| Chỗ | Hiện viết | Sửa thành |
|---|---|---|
| Mục 5, tinh thần `VIE_resolution_9_cons_idea` | Biến thể khi chọn `vie_pol.2.b`, cửa rẽ sang dải bảo thủ | Giữ biến thể, nhưng `vie_pol.2.b` **không còn mở dải**. Đó là biến thể đường lối trong Đảng: Đại hội IX nghiêng về ổn định |
| Mục 5, `VIE_resolution_12_dev_idea` | Biến thể khi chọn `vie_pol.5.b`, mở dải Kiến tạo | Giữ biến thể "Chính phủ kiến tạo" như một trọng tâm nhiệm kỳ XII. Không còn dải 15 focus đi kèm. `vie_pol.6.b` giữ nguyên |
| Mục 9.1, kịch bản thử 3 và 4 | Kiểm tra dải bảo thủ / Kiến tạo vẫn mở | Chỉ kiểm tra tinh thần biến thể |

Như vậy phương án giả định trong khuôn khổ Đảng vẫn còn, nhưng được thể hiện bằng trọng tâm nhiệm kỳ thay vì một cây riêng. Đúng hướng báo cáo nghiên cứu đã khuyến nghị: "biến thể đường lối trong khuôn khổ Đảng, không phải phe".

---

## 7. Kế hoạch thực hiện

Làm **bỏ dải trước**: giảm diện tích code trước khi tái cấu trúc, và báo cáo Đại hội phụ thuộc vào việc hai event Đại hội không còn mở dải.

| Pha | Việc | File chính |
|---|---|---|
| **A. Bỏ sáu dải** | Xóa 76 focus, 34 idea, 16 event, BoP Tài phiệt, decision và danh mục Tài phiệt; sửa 6 event cửa (mục 3.2); sửa `vie_pol.2`, `.5`; bỏ 3 option luật chơi AI; `on_startup` cho save cũ; xóa loc | `common/national_focus/VIE_md_focus.txt` · `common/ideas/VIE_md_ideas_p2.txt` · `events/VIE_md_alt.txt`, `_axis.txt`, `_p8.txt`, `_p9.txt`, `_pol.txt` · `common/bop/VIE_md_bop_p3.txt` · `common/decisions/` · `common/game_rules/VIE_md_rules.txt` · `common/on_actions/VIE_md_on_actions_startup.txt` · `common/ai_strategy/VIE_md_ai.txt` · `common/scripted_effects/VIE_md_effects_p3.txt`, `_axis.txt`, `_p2.txt` |
| **B. Tái cấu trúc kinh tế** | Đổi cha khoảng 22 focus theo mục 2.2 (khối Xã hội thêm 5 ở pha C); tách cột; 2 focus mới; gắn `vie_fb_vinashin` / event Vinashin với focus đóng tàu | `VIE_md_focus.txt` · event Vinashin · loc |
| **C. Khối Xã hội** | 4 gốc riêng; 1 focus mới NQ 29; gộp `labor_code_2019` với `vie_pol.27` | `VIE_md_focus.txt` · loc |
| **D. Mốc năm** | Thêm `available = { date > … }` cho các focus mang tên chương trình có năm (danh sách ở mục 2.2 và 2.3) | `VIE_md_focus.txt` |
| **E. Liên kết mềm** | Mục 5, sau khi xương sống Đại hội đã có (báo cáo Đại hội, pha 3) | `VIE_md_focus.txt` |
| **F. Kiểm tra** | `check_static.py` = 0 lỗi; `_gen/fix_spacing.py`, `_gen/overview.py`; hồ sơ trục STEP6; chạy thử trong game | local |

### 7.1 Kịch bản thử trong game

1. AI lịch sử 2000 → 2027: không event nào gọi tới focus, idea hoặc event đã xóa (`error.log` sạch).
2. Chọn `vie_pol.2.b` và `vie_pol.5.b`: không mở dải nào; chỉ tinh thần biến thể.
3. Event `vie_alt.6` (2018) vẫn bắn, chỉ còn các option không mở dải.
4. Làm bảo hiểm y tế năm 2008 mà chưa làm cải cách giáo dục: được.
5. Làm `private_champions` mà chưa làm `scic`: được.
6. Load một save đang ở slot 15: về chế độ Đảng (hoặc thông báo không tương thích, tùy quyết định ở mục 8).
7. Game rule `RANDOM`: không bao giờ chọn path đã bỏ.

---

## 8. Câu hỏi tác giả cần quyết

1. **Giữ Nông nghiệp và Hội nhập – FDI ở nhánh kinh tế?** Báo cáo khuyến nghị giữ. Hội nhập – FDI cũng có thể chuyển sang cây ngoại giao.
2. **Ba cặp lựa chọn loại trừ ở mục 2.4**: thêm hay không. Không thêm thì nhánh kinh tế gần như không có lựa chọn.
3. **Save cũ ở các chế độ bị bỏ**: tự chuyển về chế độ Đảng, hay chỉ ghi không tương thích?
4. **Event cửa `vie_alt.6`**: chỉ giữ option lịch sử (hoãn dự luật), hay giữ một option "thông qua" với hệ quả ngắn hạn không mở dải?
5. **`vie_alt.31`**: event này có còn cần cho dải An ninh không (cần đọc kỹ trước pha A).
