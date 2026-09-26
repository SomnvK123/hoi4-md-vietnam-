# Tái cấu trúc nhánh kinh tế, ngã rẽ lịch sử, và bỏ sáu dải chế độ giả định

> Đầu vào: đề xuất của tác giả, qua ba vòng:
> 1. Chia kinh tế theo ngành (công nghiệp nặng, công nghiệp phụ trợ, internet, khoa học, công nghệ, tài chính – ngân hàng, thiên tai, năng lượng gồm Petrolimex và điện, hạ tầng giao thông); tách giáo dục thành nhánh riêng; Luật Doanh nghiệp chia thành doanh nghiệp nhà nước và tư nhân; bỏ sáu dải chế độ.
> 2. Y tế thành một nhánh thuộc kinh tế; đô thị hóa về hạ tầng; **đặc khu thuộc nhánh Luật Doanh nghiệp, với ngã rẽ lịch sử 2018 (thông qua luật cho thuê đất 99 năm, hoặc hoãn) là hai lựa chọn loại trừ nhau**, và phát triển mẫu ngã rẽ đó cho các thời điểm lịch sử khác.
> 3. Bốn quyết định (mục 9): sự kiện đặc khu 2018 luôn xảy ra theo ngày; Hội nhập – FDI chuyển sang cây ngoại giao; thêm ba ngã rẽ (mở rộng Hà Nội 2008, tái cơ cấu DNNN 2017, giá FIT điện mặt trời 2017); save cũ ở các chế độ bị bỏ ghi là không tương thích.
>
> Code đo ngày 26/9/2026. Đi cùng `VIE_congress_spine_redesign.md`; mục 7 ghi những gì báo cáo đó phải sửa theo.
>
> Nhãn: **[SỰ KIỆN]** đo được trong code hoặc có văn bản gốc · **[TIỀN ĐỀ KỊCH BẢN]** quyết định thiết kế · **[CẦN ĐỐI CHIẾU]** mốc cần kiểm tra lại với văn bản gốc trước khi viết loc · **[CẦN THỬ]** chưa kiểm chứng trong game

---

## 0. Kết luận

**Nhánh kinh tế cần tái cấu trúc, không cần viết lại.** Đo code thấy 9 lỗi cấu trúc (mục 1.2). Ví dụ y tế và đô thị hóa nằm dưới giáo dục; tư nhân mọc từ SCIC; thép nằm dưới công nghiệp hỗ trợ. Cả 127 focus kinh tế – xã hội hiện có xếp được vào cách chia theo ngành của tác giả; gần như tất cả giữ ID và phần thưởng, khoảng 30 focus đổi prerequisite.

**Ngã rẽ lịch sử là phần có giá trị nhất.** Tại nhiều thời điểm, lịch sử kinh tế Việt Nam thật sự đứng trước hai lựa chọn loại trừ nhau, và có tài liệu ghi lại cuộc tranh luận. Báo cáo thiết kế **9 ngã rẽ** theo cùng một mẫu (mục 3), cộng cặp điện hạt nhân đã có trong mod:

| Năm | Ngã rẽ | Nhánh | Lịch sử đã chọn |
|---|---|---|---|
| 2008 | Mở rộng Hà Nội | Hạ tầng – Đô thị | Sáp nhập Hà Tây (NQ 15/2008/QH12) |
| 2009 | Bauxite Tây Nguyên: tiếp tục hay dừng | Công nghiệp nặng | Tiếp tục thí điểm |
| 2010 | Đường sắt tốc độ cao Bắc – Nam: thông qua hay bác | Hạ tầng – Giao thông | Quốc hội bác |
| 2012 | Vàng miếng: Nhà nước độc quyền hay thị trường tự do | Tài chính | Độc quyền (NĐ 24/2012) |
| 2015 | Ngân hàng yếu kém: mua lại 0 đồng hay cho phá sản | Tài chính | Mua lại 0 đồng |
| 2017 | Tái cơ cấu DNNN: giữ tập đoàn hay thoái vốn nhanh | Doanh nghiệp – DNNN | Giữ tập đoàn, cổ phần hóa chậm (NQ 12-NQ/TW) |
| 2017 | Điện mặt trời: giá FIT ưu đãi hay đấu thầu | Năng lượng – Điện | Giá FIT ưu đãi (QĐ 11/2017) |
| 2018 | Luật Đặc khu, thuê đất tới 99 năm: thông qua hay hoãn | Doanh nghiệp – Đặc khu | Hoãn |
| 2021 | COVID-19: giữ "zero COVID" hay thích ứng an toàn | Y tế | Thích ứng an toàn (NQ 128/NQ-CP) |

Một phát hiện đi kèm: **ở bốn trong chín ngã rẽ, và ở cặp điện hạt nhân sẵn có, lựa chọn lịch sử trì hoãn hoặc đóng băng vấn đề, rồi vấn đề quay lại sau 7–14 năm** (điện hạt nhân 2016 → 2024, đường sắt tốc độ cao 2010 → 2024, vàng 2012 → 2025, ngân hàng 0 đồng 2015 → 2024, đặc khu 2018 → 2025). Mẫu thiết kế khai thác điều đó: nhánh lịch sử rẻ lúc đầu nhưng dẫn tới một focus "quay lại" đúng năm thật; nhánh giả định nhận lợi ích sớm hơn kèm rủi ro rõ ràng.

**Ngã rẽ trong nhánh lịch sử thay thế một phần vai trò của các dải chế độ bị bỏ.** Bỏ các dải Kiến tạo, Đặc khu, Tài phiệt là bỏ ba mô hình kinh tế giả định. Chín ngã rẽ trả lại lựa chọn kinh tế cho người chơi, mỗi lựa chọn đều có mốc thật và không cần đổi chế độ. Ba event của dải Đặc khu cũ được tái dùng làm hệ quả của việc thông qua luật.

**Quy mô:** nhánh kinh tế 107 → **129 focus**; Hội nhập – FDI (7 focus) chuyển sang cây ngoại giao; khối Xã hội 20 → **15 focus**; tổng 127 → **151** (+24 mới, trong đó 21 thuộc ngã rẽ). Dải chế độ giả định 106 → **30 focus**.

---

## 1. Hiện trạng đo được

### 1.1 Nhánh kinh tế – xã hội hiện nay

**[SỰ KIỆN]** 127 focus ở cột x 130–254, hàng 0–8, tổng chi phí **933 tuần**. **55 focus (43%) không có mốc năm**, trong khi khối chính trị hầu như focus nào cũng có. Về đồ thị, phần lớn kinh tế nằm trong một thành phần liên thông 101 focus, trộn chung với ngoại giao và xã hội. Chỉ có **một cặp loại trừ** trong toàn bộ nhánh kinh tế: điện hạt nhân (xây / gác lại).

### 1.2 Chín lỗi cấu trúc

| # | Lỗi | Bằng chứng |
|---|---|---|
| 1 | **Y tế, đô thị hóa, văn hóa mọc từ giáo dục** | `universal_health_insurance`, `urbanization`, `heritage_preservation` có cha là `education_reform`. Muốn làm bảo hiểm y tế phải làm cải cách giáo dục trước |
| 2 | **Tư nhân mọc từ SCIC** | `private_champions`, `household_business` có cha là `scic` (Tổng công ty Đầu tư và Kinh doanh Vốn Nhà nước) |
| 3 | **Công nghiệp nặng nằm dưới công nghiệp hỗ trợ** | `formosa_steel_complex` có cha `supporting_industries`. Thép là đầu vào của công nghiệp hỗ trợ, không phải ngược lại |
| 4 | **Chuyển đổi năng lượng nằm dưới thiên tai** | `jetp_partnership` có cha `disaster_preparedness`; `net_zero_2050` nằm dưới JETP |
| 5 | **Luật Doanh nghiệp là gốc của mọi thứ** | `enterprise_law` là cha của BTA, sàn HOSE, xuất khẩu gạo, cổ phần hóa, Luật Đầu tư |
| 6 | **Năng lượng và giao thông đan xen** | Cùng dải cột 196–214: metro Hà Nội (206) nằm giữa Petrolimex (204) và điện hạt nhân (204–206) |
| 7 | **Ba focus Đồng bằng sông Cửu Long chồng nội dung** | `mekong_climate_adaptation` (nông nghiệp), `nature_adaptation_120` và `dutch_water_model` (thiên tai) cùng mô tả cống ngăn mặn và chuyển lúa sang tôm, tức nội dung NQ 120/NQ-CP (2017) |
| 8 | **Viettel ra nước ngoài nằm dưới nhà máy wafer** | `viettel_global` (mạng viễn thông ở Lào, Campuchia, Peru… từ 2006) có cha `semiconductor_fab` |
| 9 | **Mốc năm của khoáng sản ngược** | `bauxite_tay_nguyen` cần `rare_earths` (khóa tới 2011), trong khi quyết định về bauxite là năm 2009 |

---

## 2. Cấu trúc đề xuất

### 2.1 Tổng thể

`VIE_doi_moi_continues` giữ vai trò gốc chung. Mỗi nhánh có gốc riêng cần `doi_moi_continues`. Liên kết giữa các nhánh dùng `available`, không dùng prerequisite, để không nhánh nào phải đi qua nhánh khác mới mở được.

```text
                                      TIẾP TỤC ĐỔI MỚI
                                             │
 ┌────────┬────────┬────────┬────────┬───────┴┬────────┬────────┬───────┬────────┬───────┬──────┐
DOANH    TÀI      CÔNG     NĂNG     HẠ TẦNG  Y TẾ     NÔNG     THIÊN   INTERNET CÔNG    KHOA
NGHIỆP   CHÍNH    NGHIỆP   LƯỢNG                     NGHIỆP   TAI     – SỐ     NGHỆ    HỌC
│        │        │        │        │
├ DNNN ◆ ├ Ngân   ├ Nặng ◆ ├ Dầu    ├ Giao thông ◆
├ Tư nhân│  hàng ◆├ Chế    │  khí   │  liên vùng
└ Đặc    └ Vốn,   │  tạo   ├ Petro- └ Đô thị ◆
  khu ◆    vàng ◆ └ Phụ    │  limex
                    trợ    └ Điện ◆                               ĐÍCH 2030 / 2045

 CÂY NGOẠI GIAO (cột 101–129, sát khối ngoại giao):   HỘI NHẬP – FDI
 KHỐI XÃ HỘI:   GIÁO DỤC     LAO ĐỘNG – XÃ HỘI     VĂN HÓA – DU LỊCH

 ◆ = nhánh con có ngã rẽ lịch sử (mục 3). Y tế cũng có một ngã rẽ.
```

| Nhánh | Nhánh con | Focus | Chi phí (tuần) | Ngã rẽ | Thay đổi chính |
|---|---|---|---|---|---|
| Doanh nghiệp | Luật DN · DNNN · Tư nhân · **Đặc khu** | 16 | 109 | DNNN 2017, đặc khu 2018 | Tư nhân tách khỏi SCIC; +7 focus |
| Tài chính | Ngân hàng · Vốn, vàng và thanh toán | 18 | 126 | Vàng 2012, ngân hàng 2015 | Nhận HOSE, thanh toán; +6 focus |
| Công nghiệp | Nặng · Chế tạo – ô tô · Phụ trợ | 16 | 115 | Bauxite 2009 | Đảo thứ tự nặng/phụ trợ; +đóng tàu, +dừng bauxite |
| Năng lượng | Dầu khí · Petrolimex · Điện | 22 | 170 | FIT 2017, điện hạt nhân (đã có) | Nhận Nghi Sơn, JETP, Net Zero; +Dung Quất, +đấu thầu điện mặt trời |
| Hạ tầng | Giao thông liên vùng · **Đô thị** | 13 | 101 | Hà Nội 2008, đường sắt cao tốc 2010 | Nhận đô thị hóa; metro chuyển sang Đô thị; +4 focus |
| **Y tế** | — | 7 | 48 | COVID-19 2021 | **Chuyển từ khối Xã hội sang kinh tế**; +2 focus |
| Nông nghiệp – đất đai | — | 5 | 33 | — | Gỡ chồng lấn ĐBSCL |
| Thiên tai | — | 8 | 59 | — | Trả JETP, Net Zero cho năng lượng |
| Internet – số | — | 8 | 59 | — | Nhận `viettel_global` |
| Công nghệ (bán dẫn) | — | 5 | 41 | — | Gốc là `intel_hcmc` |
| Khoa học | — | 6 | 43 | — | Giữ |
| Đích 2030/2045 | — | 5 | 41 | — | Giữ |
| **Kinh tế** | | **129** | **945** | 9 | 107 cũ − 7 sang ngoại giao + 6 chuyển về + 23 mới |
| Hội nhập – FDI | — | 7 | 52 | — | **Chuyển sang cây ngoại giao** |
| Giáo dục | — | 6 | 39 | — | Nhánh riêng; +NQ 29 |
| Lao động – xã hội | — | 4 | 31 | — | Mất gốc đô thị hóa; hai gốc mới |
| Văn hóa – du lịch | — | 5 | 34 | — | Gốc riêng |
| **Xã hội** | | **15** | **104** | 0 | 20 cũ − 6 chuyển đi + 1 mới |

Tổng: 151 focus, 1.101 tuần. Trong 9 cặp ngã rẽ người chơi chỉ lấy được một bên, nên tối đa đi được khoảng 1.040 tuần, tức 20 năm focus trên 26 năm lịch sử. Nhánh này vẫn phải cạnh tranh thời gian với chính trị, ngoại giao và quốc phòng.

Vì sao y tế thuộc kinh tế **[TIỀN ĐỀ KỊCH BẢN]**: nội dung của năm focus y tế là quỹ bảo hiểm y tế, sản xuất vắc-xin trong nước, hệ thống bệnh viện và y tế cơ sở, tức chi tiêu công và công nghiệp dược. Ngã rẽ COVID-19 năm 2021 thực chất là một quyết định kinh tế: mở cửa sản xuất hay tiếp tục giãn cách.

### 2.2 Chi tiết từng nhánh

> **Đã code (pha B), có một điều chỉnh phạm vi quan trọng.** Toàn bộ thay đổi cha/`available` dưới đây đã áp dụng (22 chỗ, cộng 1 phát hiện thêm khi thực thi: `tier1_vendor_localization` thực ra đang là con của `intel_hcmc`, không phải `supporting_industries` như văn bản ngụ ý — đã sửa đúng). **"Tách cột" (đổi tọa độ x/y) không làm**, trừ 2 focus mới. Lý do: gần như toàn bộ khối kinh tế (Công nghiệp, Năng lượng, Hạ tầng, Internet — hơn 60 focus) hiện dùng chung một `relative_position_id = VIE_north_south_expressway`, và vùng tọa độ đó đã kín gần hết (x từ -22 đến +28, y 1–7, gần như không còn khe trống). Sắp xếp lại toàn bộ 130 focus theo cột sạch đòi phải dịch chuyển rất nhiều focus KHÔNG có lỗi cấu trúc gì, chỉ để nhường chỗ — rủi ro cao mà không xác minh được trong game (sandbox này không chạy được `_gen/fix_spacing.py` hay `check_static.py`). Các focus đổi cha giữ nguyên tọa độ cũ; chỉ 2 focus mới được đặt vào khe trống thật (hàng y=1–2, chưa có ai chiếm). Đây là việc cần làm thêm bằng công cụ local của bạn, không phải lỗi bỏ sót.

Ký hiệu: **gốc** = focus gốc của nhánh (cần `doi_moi_continues`); **đổi cha** = prerequisite mới; **+năm** = thêm `available = { date > … }`; **★** = focus mới; **◆** = thuộc một ngã rẽ, chi tiết ở mục 3.

**Doanh nghiệp.** Luật Doanh nghiệp 1999 (hiệu lực 1/1/2000) là gốc, tách thành ba nhánh con.

| Nhánh con | Focus theo thứ tự | Ghi chú |
|---|---|---|
| gốc | `enterprise_law` | Chỉ giữ ba con: DNNN, Tư nhân, Đặc khu |
| DNNN | `equitization_soes` → `state_conglomerates` (+năm 2005) → `scic` (2005) → ◆ ngã rẽ tái cơ cấu 2017 → `soe_governance` (2018) | `state_conglomerates` thôi là gốc tự do. `soe_governance` đổi cha thành một trong hai bên ngã rẽ |
| Tư nhân | `investment_law_2005` → `household_business` (2020) → `private_champions` (+năm 2017, NQ 10-NQ/TW) → `private_sector_engine` (NQ 68, 2025) | **Đổi cha**: bỏ `scic` ở hai focus; `private_sector_engine` bỏ prerequisite `soe_governance` |
| **Đặc khu** | `sez_three_zones` (chuẩn bị, không bắt buộc); event 6/2018 → ◆ ngã rẽ `sez_postpone` / `sez_pass_99` → `island_special_zones` hoặc `sez_strategic_investors` | 5 focus mới. Mục 3.2 |

**Tài chính.**

| Nhánh con | Focus |
|---|---|
| Ngân hàng | **Giữ nguyên đồ thị:** gốc `state_bank_modernization`; mạch `fight_inflation` (2008) → `deposit_insurance`; mạch `restructure_banking` (2011) → `vamc` (2013) → ◆ ngã rẽ ngân hàng 0 đồng (2015) → `compulsory_transfer_2024`; hội tụ ở `cross_ownership_crackdown` |
| Vốn, vàng và thanh toán | `hose_exchange` (7/2000, **đổi cha** từ Luật DN) → `corporate_bond_reform` (2022, **đổi cha** từ `vamc`) → `market_upgrade_criteria` → `international_financial_centre` → `investment_grade`; `cashless_payments` (2016, **đổi cha** từ `internet_expansion`, vì đây là chính sách của NHNN); ◆ ngã rẽ vàng (2012) → `gold_monopoly_lifted` (2025) |

**Công nghiệp.** Thứ tự thượng nguồn → hạ nguồn: nặng cung cấp vật liệu cho phụ trợ, phụ trợ cung cấp linh kiện cho chế tạo.

| Nhánh con | Focus | Ghi chú |
|---|---|---|
| Nặng | Ba mạch gốc: thép `formosa_steel_complex` (**đổi cha**: bỏ `supporting_industries`) → `hoa_phat_hrc_steel`; khoáng sản ◆ `bauxite_tay_nguyen` / `bauxite_suspend` (2009) → `rare_earths` (**đổi cha**: bỏ `petrovietnam_expansion`); ★ `shipbuilding_vinashin` | Đảo thứ tự bauxite / đất hiếm cho đúng năm. `nghi_son_refinery` chuyển sang Năng lượng |
| Chế tạo – ô tô | gốc `samsung_partnership` (**đổi cha** từ WTO, giữ `available` WTO) → `china_plus_one` → `manufacturing_hub`; `domestic_automotive` → `ev_revolution_batteries` → `global_auto_export` | VinFast là doanh nghiệp lắp ráp; linh kiện ở phụ trợ |
| Phụ trợ | gốc `supporting_industries` → `tier1_vendor_localization`, `precision_mechanics_molds` (**đổi cha** từ thép), `integrated_auto_supplier_park` | `intel_hcmc` chuyển sang Công nghệ |

★ **`shipbuilding_vinashin` — Công nghiệp đóng tàu.** Cost 7, +năm 2005. Thưởng công nghiệp và nhà máy đóng tàu. **Cái giá:** là điều kiện để event Vinashin đổ vỡ (2010) mang hậu quả đầy đủ. Không làm focus thì event chỉ còn hậu quả nhẹ (`VIE_fb_vinashin`).

**Năng lượng.**

| Nhánh con | Focus | Ghi chú |
|---|---|---|
| Dầu khí | gốc `petrovietnam_expansion` → ★ `dung_quat_refinery` (+năm 2008, vận hành 2/2009) → `nghi_son_refinery` (2018) | Dung Quất là nhà máy lọc dầu đầu tiên, hiện chưa có |
| Petrolimex | gốc `petrolimex_downstream_network` (**đổi cha** từ PVN) → `strategic_petroleum_reserve`, `petrolimex_eneos_partnership` → `petrolimex_green_ev_hubs` | Giữ nội dung |
| Điện | gốc `son_la_dam` → `500kv_grid` → `dppa_market_reform`; `coal_power` (**đổi cha** từ PVN thành `son_la_dam`) → ◆ ngã rẽ FIT 2017 → `power_plan_8` → `offshore_wind` → `energy_security_2045`; `ninh_thuan_nuclear` → `shelve_nuclear` / `build_nuclear_plant` → `revive_nuclear`; `jetp_partnership` (**đổi cha** thành `power_plan_8`) → `net_zero_2050` | Cặp điện hạt nhân là **mẫu ngã rẽ đã có sẵn** trong mod |

**Hạ tầng.**

| Nhánh con | Focus | Ghi chú |
|---|---|---|
| Giao thông liên vùng | gốc `north_south_expressway` → `lach_huyen_port`, `cai_mep_port` → `lao_cai_haiphong_rail`, `long_thanh_airport`; ◆ ngã rẽ đường sắt tốc độ cao 2010 → `north_south_hsr` | `north_south_hsr` thêm prerequisite một trong hai bên ngã rẽ |
| **Đô thị** | gốc `urbanization` (**đổi cha** từ `education_reform`) → ◆ ngã rẽ mở rộng Hà Nội 2008 → `hanoi_metro` (2010); `hcmc_metro` (2012) (**đổi cha** từ cao tốc thành `urbanization`) | `urbanization` đổi tên thành "Định hướng phát triển hệ thống đô thị" (QĐ 445/QĐ-TTg, 4/2009) **[CẦN ĐỐI CHIẾU]**. Mốc năm để trống vì ngã rẽ Hà Nội (5/2008) nằm sau nó. Nội dung "đô thị thông minh" (2018) chuyển vào mô tả |

**Y tế.** Gốc `universal_health_insurance` (**đổi cha** từ giáo dục, +năm 2008, Luật BHYT) → `grassroots_clinics` → `hospital_decongestion`, `vaccine_production` (2021) → `preventive_health`; ◆ ngã rẽ COVID-19 (2021), prerequisite `grassroots_clinics`.

**Nông nghiệp – đất đai.** Gốc `rice_export_power` (**đổi cha** từ Luật DN) → `new_rural_development` (2010) → `high_tech_agriculture` (2015); `land_law_reform` (2013) → `mekong_climate_adaptation`. **Sửa chồng lấn:** `mekong_climate_adaptation` chỉ giữ phần chuyển đổi sản xuất (lúa chịu mặn, lúa sang tôm và trái cây), thêm `available` `nature_adaptation_120`. Phần cống ngăn mặn để lại cho `dutch_water_model`.

**Thiên tai.** Gốc `disaster_preparedness` → `military_rescue_corps` → `emergency_operations_center`; `satellite_early_warning` → `storm_resilient_islands`; `nature_adaptation_120` (+năm 2017) → `dutch_water_model` → `sustainable_mekong_delta`.

**Internet – số.** Gốc `internet_expansion` → `mobile_networks` (5G, 2023); `national_digital_transformation` (2020, **đổi cha** từ `cashless_payments`) → `digital_id` → `national_data_center` → `ai_strategy` → `digital_nation`; `viettel_global` (**đổi cha** từ `semiconductor_fab`, +năm 2006).

**Công nghệ (bán dẫn).** Gốc `intel_hcmc` (2010) → `semiconductor_ambition` → `chip_design`, `chip_engineers` → `semiconductor_fab`.

**Khoa học.** Giữ nguyên: `nafosted` → `research_universities`, `nuclear_research`, `vinasat` → `earth_observation`; `science_breakthrough` (NQ 57).

**Đích 2030/2045.** Giữ nguyên năm focus.

> **Đã code (pha F).** Rà toàn bộ ký hiệu **+năm** trong mục 2.2 và 2.4: phần lớn đã có mốc năm từ các pha trước (`shipbuilding_vinashin`, `dung_quat_refinery`, `viettel_global`, và toàn bộ mục 2.4 từ pha E). Còn đúng 4 chỗ thiếu, đã bổ sung `available = { date > … }`: `state_conglomerates` (2005, cộng thêm vào `available` đã có `has_completed_focus = VIE_wto_negotiations` chứ không thay); `private_champions` (đổi từ cờ chung `VIE_era_2011` — tức chỉ "sau 2011" — thành mốc thật NQ 10-NQ/TW, `date > 2017.6.30`); `universal_health_insurance` và `nature_adaptation_120` (cả hai trước đó không có khối `available` nào, nay có `date > 2008.12.31` và `date > 2017.11.30`). Không đụng tới các mốc năm đã có sẵn dù vài chỗ (`nghi_son_refinery`, `hanoi_metro`, `new_rural_development`…) lệch một năm so với văn bản — đó là quyết định của các pha trước, ngoài phạm vi "chỉ thêm chỗ còn thiếu" của pha F.

### 2.3 Hội nhập – FDI chuyển sang cây ngoại giao

> **Đã code (pha C).** Khác pha B, ở đây "tách cột" áp dụng được vì đây là một cụm 7 focus tự thân (đã tách khỏi Luật Doanh nghiệp bằng đổi cha), không phải phải dịch chuyển hàng chục focus không liên quan để nhường chỗ. Vị trí tuyệt đối thật: `bilateral_trade_agreement_usa` (115,1), `fdi_attraction`/`wto_negotiations`/`wto_reforms`/`export_powerhouse` (119, 2–5), `cptpp_member` (117,6), `evfta` (121,6) — đã xác nhận 0 va chạm với focus nào khác trong x101–129.

Bảy focus giữ nguyên ID, phần thưởng và thứ tự: gốc `bilateral_trade_agreement_usa` (BTA 2000, **đổi cha** từ `enterprise_law` thành `doi_moi_continues`) → `fdi_attraction` → `wto_negotiations` → `wto_reforms` → `export_powerhouse`; nhánh bên `cptpp_member`, `evfta`.

**Vị trí:** cột x 101–129, hàng 0–9. **[SỰ KIỆN]** Vùng này đang trống hoàn toàn và nằm ngay giữa khối ngoại giao (x ≤ 100) và khối kinh tế (x ≥ 130), nên các đường nối sang cả hai phía đều ngắn.

**Liên kết giữ nguyên:** `multilateral_champion` (ngoại giao) đã cần `cptpp_member` hoặc `evfta`; `samsung_partnership` (kinh tế) giữ `available` WTO; decision `VIE_negotiate_economic_pact` giữ điều kiện `wto_negotiations`. Không có tham chiếu nào bị treo vì chỉ đổi tọa độ.

`search_filters` giữ `FOCUS_FILTER_ECONOMY`, thêm `FOCUS_FILTER_POLITICAL` để người chơi lọc theo ngoại giao vẫn thấy.

### 2.4 Khối Xã hội

| Nhánh | Focus | Ghi chú |
|---|---|---|
| **Giáo dục** | gốc `education_reform` (đổi tên thành "Chiến lược phát triển giáo dục 2001–2010", QĐ 201/2001) → `english_second_language` (**đổi cha** từ `vocational_training`, +năm 2008, Đề án Ngoại ngữ quốc gia) → ★ `education_nq29` (+năm 2013) → `university_autonomy` (**đổi cha**, +năm 2014, NQ 77/NQ-CP) → `free_tuition` (2025); `vocational_training` (+năm 2014, Luật Giáo dục nghề nghiệp) | Chỉ còn nội dung giáo dục. ★ NQ 29-NQ/TW (11/2013) "Đổi mới căn bản, toàn diện giáo dục và đào tạo" |
| **Lao động – xã hội** | hai gốc `social_insurance_reform` (2015, Luật BHXH 2014) và `labor_code_2019` → hội tụ ở `population_policy` → `overseas_vietnamese` | Mất gốc `urbanization`. `labor_code_2019` đọc cờ `VIE_labor_convention_ratified` của event `vie_pol.27` để trao thêm thưởng, thay vì làm lại việc phê chuẩn ILO |
| **Văn hóa – du lịch** | gốc `heritage_preservation` (**đổi cha**) → `sea_games_bid` (2003), `visa_reform` (2023) → `cultural_industry` → `tourism_powerhouse` | Giữ |

> **Đã code (pha E), có một lỗi phát hiện khi thực thi.** Toàn bộ đổi cha/mốc năm ở dòng Giáo dục và Lao động – xã hội đã áp dụng, cộng focus mới `education_nq29` (x=-2, y=6, đặt trong cùng cụm tọa độ `education_reform`, xác nhận 0 va chạm). Phát hiện ngoài văn bản: `english_second_language` đang có `available = { has_completed_focus = VIE_free_tuition }` — một phụ thuộc ngược, vì `free_tuition` (2025) đứng sau `english_second_language` (2008) theo thời gian và không thể nào là điều kiện tiên quyết hợp lý. Đã sửa thành `available = { date > 2008.12.31 }` như các mốc năm khác trong nhánh, và tách `english_second_language` khỏi `vocational_training` để làm con trực tiếp của `education_reform`, đúng như bảng trên mô tả. Tên `education_reform` đã đổi thành "Chiến lược Phát triển Giáo dục 2001–2010" (QĐ 201/2001/QĐ-TTg) ở cả file loc gốc lẫn bản `replace/p2_b` đã có sẵn từ trước (giữ đồng bộ cả hai vì không xác minh được trong sandbox này file nào thắng khi trùng khóa). `labor_code_2019` đọc cờ `VIE_labor_convention_ratified` bằng khối `if` cộng thêm vào biến trục `VIE_ax_west`, không đổi lại logic phê chuẩn ILO của `vie_pol.27`.

---

## 3. Ngã rẽ lịch sử

### 3.1 Mẫu chung

> **Đã code (pha D), với ba điều chỉnh so với văn bản.** (1) `island_special_zones` dùng `available = { date > 2025.6.30 }` thay vì cờ `VIE_two_tier_done`, vì cờ đó thuộc thiết kế báo cáo Đại hội chưa được code. (2) Phát hiện khi thực thi: 2 chỗ sót từ pha B — `rice_export_power` chưa thật sự tách khỏi Luật DN, `nghi_son_refinery` chưa nối vào Dung Quất — đã sửa cùng đợt này. (3) Sửa lỗi cân bằng AI: các option lịch sử ban đầu viết `factor = 0` khi không chơi lịch sử (tức AI không bao giờ chọn lịch sử ở chế độ tự do), đã sửa thành `factor = 0.05` đúng quy ước đã dùng trong toàn mod (ví dụ `vie_pol.2.a`).

Mẫu lấy từ cặp điện hạt nhân đã có trong mod (`ninh_thuan_nuclear` → `build_nuclear_plant` / `shelve_nuclear` → `revive_nuclear`) và từ ý tưởng đặc khu của tác giả.

```text
[CHUẨN BỊ]   focus của chính phủ, hoặc một mốc ngày / event đã có
     │
[TRANH LUẬN] event (nếu cần): dư luận, Quốc hội. Chỉ đặt cờ và phản ứng, KHÔNG quyết định
     │
     ├──────────────────────────────┐
     ▼                              ▼
[LỊCH SỬ]                      [GIẢ ĐỊNH]
 mutually_exclusive             mutually_exclusive
 thường là "gác lại"            lợi ích đến sớm hoặc lớn hơn
 không cộng trục                cộng trục; có cơ chế rủi ro rõ ràng
     │                              │
     ▼                              ▼
[QUAY LẠI] focus khóa đúng     [HỆ QUẢ] event hoặc timed idea
 năm vấn đề trở lại thật        do focus giả định kích hoạt
```

Sáu quy tắc **[TIỀN ĐỀ KỊCH BẢN]**:

1. Hai focus của một ngã rẽ có **cùng prerequisite, cùng `available`** (mốc năm của quyết định thật, cộng cờ của event tranh luận nếu có), và `mutually_exclusive` với nhau.
2. **Bên lịch sử không cộng trục.** Hồ sơ trục đã hiệu chuẩn ở STEP6 là hồ sơ của đường lịch sử; giữ nó nguyên vẹn. Bên lịch sử dùng PP, ổn định, ngân sách.
3. **Bên giả định mang trục và mang cái giá.** Cái giá phải là cơ chế thấy được (timed idea, event trễ), không chỉ là con số trừ ngay.
4. Mô tả bên giả định mở đầu bằng "§Y[Giả định]§!". Tooltip của cả hai bên nói rõ lịch sử đã chọn gì.
5. AI: bên giả định có `modifier = { factor = 0 VIE_ai_historical = yes }`.
6. Ngã rẽ kinh tế **không cần Đảng cầm quyền**. Đây là quyết định của nhà nước dưới mọi chế độ.

### 3.2 Đặc khu 2018 (nhánh Doanh nghiệp)

**[SỰ KIỆN]** Chính phủ trình dự thảo Luật Đơn vị hành chính – kinh tế đặc biệt Vân Đồn, Bắc Vân Phong, Phú Quốc tại kỳ họp tháng 10/2017. Dự thảo có điều khoản cho thuê đất tới 99 năm với một số dự án, và cho phép người Việt Nam vào casino trong đặc khu. Điều khoản 99 năm gây phản ứng mạnh, kèm biểu tình ở nhiều tỉnh ngày 10–11/6/2018. Tháng 6/2018, Quốc hội lùi việc thông qua sang kỳ họp sau; dự luật sau đó không được đưa trở lại. Từ 1/7/2025, trong cải cách chính quyền hai cấp, "đặc khu" trở thành loại đơn vị hành chính cấp xã cho các huyện đảo (Vân Đồn, Phú Quốc, Côn Đảo và các đảo khác). **[CẦN ĐỐI CHIẾU]** danh sách đặc khu năm 2025.

**Quyết định của tác giả:** sự kiện tháng 6/2018 **luôn xảy ra theo ngày**, như lịch sử. Focus chuẩn bị không bắt buộc; làm nó thì hai bên ngã rẽ nhận thêm lợi ích.

| Bước | ID | Loại | Điều kiện | Nội dung |
|---|---|---|---|---|
| Chuẩn bị (không bắt buộc) | ★ `VIE_sez_three_zones` — Đề án ba đặc khu | focus, cost 7 | prereq `enterprise_law`; `date > 2017.9.30`; chỉ làm được trước khi ngã rẽ được quyết | PP −25. Cờ `VIE_sez_prepared`: nếu thông qua luật thì FDI của `VIE_sez_idea` mạnh hơn; nếu hoãn thì `island_special_zones` được thêm một nhà máy dân sự |
| Tranh luận | `vie_alt.6` — Dự thảo Luật Đặc khu | event (đã có, **sửa**) | scheduler D6 **giữ nguyên**: `date > 2018.5.31`, Đảng cầm quyền | Không còn quyết định luật. Hai option phản ứng với biểu tình: **a** đối thoại, tiếp thu (ổn định +0.02, PP −25); **b** giữ trật tự cứng rắn (ổn định −0.01, `civil −1`). Cả hai đặt cờ `VIE_sez_bill_debated` |
| **Lịch sử** | ★ `VIE_sez_postpone` — Hoãn Luật Đặc khu | focus, cost 5 | prereq `enterprise_law`; `VIE_sez_bill_debated`; mutex | Ổn định +0.02. Không cộng trục |
| **Giả định** | ★ `VIE_sez_pass_99` — Thông qua Luật Đặc khu (thuê đất tới 99 năm) | focus, cost 7 | như trên; mutex | `market +2`, `decent +2`, `integ +1`. Idea `VIE_sez_idea` (FDI và xây dựng tăng). Timed idea `VIE_sez_unrest_idea` 180 ngày (**đã có**). Kích hoạt `vie_alt.8` sau 365 ± 90 ngày |
| Quay lại (lịch sử) | ★ `VIE_island_special_zones` — Đặc khu trong chính quyền hai cấp | focus, cost 7 | prereq `sez_postpone`; `VIE_two_tier_done` hoặc (`date > 2025.6.30` và không Đảng cầm quyền) | Du lịch, ngân sách. Không cộng trục. Có thể kèm event Phú Quốc đăng cai APEC 2027 **[CẦN ĐỐI CHIẾU]** |
| Hệ quả (giả định) | ★ `VIE_sez_strategic_investors` — Nhà đầu tư chiến lược vào đặc khu | focus, cost 7 | prereq `sez_pass_99` | FDI tăng. Kích hoạt `vie_alt.25` (casino và tội phạm có tổ chức); sau 2 năm `vie_alt.26` (đặc khu đòi quyền tự trị) |

Dưới chế độ không phải Đảng, scheduler D6 không bắn nên không có tranh luận. Khi đó `sez_postpone` và `sez_pass_99` dùng `available` thay thế: `date > 2018.5.31` và `NOT = { VIE_party_rule_active = yes }`.

**Tái dùng ba event của dải Đặc khu cũ** thay vì xóa: `vie_alt.8` "Ai đang thuê đất đặc khu?" (đúng nỗi lo về hợp đồng 99 năm), `vie_alt.25` "Casino và tội phạm có tổ chức" (đúng điều khoản casino trong dự thảo), `vie_alt.26` "Đặc khu đòi quyền tự trị". Chỉ cần sửa dòng chú thích "opened by VIE_lb_…" và gỡ tham chiếu tới dải cũ trong option.

### 3.3 Tám ngã rẽ còn lại

| Ngã rẽ | Nhánh | Chuẩn bị / điều kiện | **Lịch sử** | **Giả định** | Quay lại / hệ quả |
|---|---|---|---|---|---|
| **Mở rộng Hà Nội 2008** | Đô thị | prereq `urbanization`; `date > 2008.4.30`. **[SỰ KIỆN]** NQ 15/2008/QH12 (29/5/2008) sáp nhập Hà Tây và một số xã vào Hà Nội từ 1/8/2008 | ★ `VIE_hanoi_expansion_2008`: sáp nhập. Thêm ô xây dựng cho state Hà Nội; timed idea `VIE_reorg_disruption` 180 ngày (**đã có**) | ★ `VIE_hanoi_keep_boundaries`: giữ địa giới. Ổn định +0.01, không xáo trộn; `decent +1` | Cả hai mở `hanoi_metro`. Không đổi bản đồ; cần kiểm tra ID state Hà Nội trong MD **[CẦN THỬ]** |
| **Bauxite Tây Nguyên 2009** | Công nghiệp nặng | prereq gốc nhánh; `date > 2009.3.31`. **[SỰ KIỆN]** Tranh luận 2008–2009, có ba thư của Đại tướng Võ Nguyên Giáp; Bộ Chính trị kết luận tiếp tục thí điểm Tân Rai, Nhân Cơ | `bauxite_tay_nguyen` (**giữ ID**, thêm mutex): tiếp tục thí điểm. Giữ phần thưởng cũ | ★ `VIE_bauxite_suspend`: dừng khai thác. Ổn định +0.02, mất sản lượng nhôm, idea môi trường nhỏ | Cả hai mở `rare_earths` |
| **Đường sắt tốc độ cao 2010** | Giao thông | prereq `north_south_expressway`; `date > 2010.4.30`. **[SỰ KIỆN]** Quốc hội bác dự án khoảng 56 tỷ USD ngày 19/6/2010 | ★ `VIE_hsr_2010_reject`: Quốc hội bác. PP +25 | ★ `VIE_hsr_2010_approve`: thông qua. Timed idea "Dự án ĐSCT đang thi công" khoảng 10 năm: ngân sách hao hụt đều (nợ công) | Lịch sử: `north_south_hsr` như cũ (`date > 2024.11.30`, NQ 172/2024/QH15). Giả định: `north_south_hsr` mở từ 2020 |
| **Vàng miếng 2012** | Tài chính | prereq `state_bank_modernization`; `date > 2012.3.31`. **[SỰ KIỆN]** NĐ 24/2012/NĐ-CP: Nhà nước độc quyền sản xuất vàng miếng | ★ `VIE_gold_monopoly_2012`: chống "vàng hóa". Ổn định +0.02 | ★ `VIE_gold_free_market`: thả nổi. `market +1`. Timed idea áp lực tỷ giá 365 ngày | Lịch sử: ★ `VIE_gold_monopoly_lifted` (`date > 2025.8.31`, bỏ độc quyền năm 2025) **[CẦN ĐỐI CHIẾU]** số nghị định |
| **Ngân hàng yếu kém 2015** | Tài chính | prereq `vamc`; `date > 2014.12.31`. **[SỰ KIỆN]** NHNN mua lại VNCB, OceanBank, GPBank giá 0 đồng (2015) | ★ `VIE_zero_dong_acquisition`: mua lại 0 đồng. Ổn định +0.02, ngân sách −1 | ★ `VIE_bank_bankruptcy`: cho phá sản có kiểm soát. `market +1`. Ổn định −0.05 và timed idea mất niềm tin tiền gửi; **giảm một nửa nếu đã làm `deposit_insurance`** | Lịch sử: ★ `VIE_compulsory_transfer_2024` (`date > 2024.9.30`): chuyển giao bắt buộc cho các ngân hàng lớn. Event `vie_alt.7` (rút tiền SCB, 10/2022) giữ nguyên, nặng hơn trên đường lịch sử |
| **Tái cơ cấu DNNN 2017** | DNNN | prereq `scic`; `date > 2017.5.31`. **[SỰ KIỆN]** NQ 12-NQ/TW (6/2017) về cơ cấu lại, đổi mới và nâng cao hiệu quả DNNN; sau đó lập Ủy ban Quản lý vốn nhà nước tại doanh nghiệp (2018) | ★ `VIE_soe_gradual_restructuring`: giữ tập đoàn, cổ phần hóa chậm. PP +25, ổn định +0.01 | ★ `VIE_soe_rapid_divestment`: thoái vốn nhanh. `market +2`; ngân sách +2 một lần (tiền bán vốn); opinion `communist_cadres` −5; ổn định −0.03; event trễ "Bán rẻ tài sản nhà nước?" sau 1 năm (mới) | Cả hai mở `soe_governance` |
| **Giá FIT điện mặt trời 2017** | Điện | prereq `coal_power`; `date > 2017.3.31`. **[SỰ KIỆN]** QĐ 11/2017/QĐ-TTg: giá mua cố định 9,35 cent/kWh; công suất tăng vọt 2019–2020, lưới truyền tải quá tải, phải cắt giảm | `solar_boom` (**giữ ID**, thêm mutex, đổi mốc từ 2018.12.31 thành 2017.3.31): giá FIT. Giữ phần thưởng cũ, thêm timed idea `VIE_grid_curtailment_idea` (mới), chỉ gỡ khi hoàn thành `500kv_grid` | ★ `VIE_solar_auction`: đấu thầu cạnh tranh. `market +1`; ít công suất mặt trời hơn, không quá tải lưới | Cả hai mở `power_plan_8` (thay prerequisite `solar_boom`) |
| **COVID-19 tháng 10/2021** | Y tế | prereq `grassroots_clinics`; `date > 2021.9.30`; cờ scheduler của `vie_soc.6` (đã có). **[SỰ KIỆN]** NQ 128/NQ-CP (11/10/2021) chuyển từ "zero COVID" sang thích ứng an toàn | ★ `VIE_covid_safe_adaptation`: thích ứng an toàn. Ổn định −0.02 ngắn hạn, tăng trưởng phục hồi | ★ `VIE_covid_zero_extend`: tiếp tục giãn cách. Ổn định +0.02; timed idea sản xuất đình trệ 180 ngày | — |

Khác biệt với dải "Giải cứu ngân hàng" bị bỏ: dải đó là chế độ tài phiệt nắm quyền; ngã rẽ 2015 là chính sách của NHNN dưới chế độ hiện hành.

Đổi mốc `solar_boom` từ 2019 về 4/2017 kéo sớm hiệu ứng trục của nó, nhưng vẫn trong cùng giai đoạn 4 (2016–2020) của hồ sơ STEP6, nên hồ sơ giai đoạn không đổi.

### 3.4 Ứng viên không chọn ở vòng này

| Ngã rẽ | Nhánh | Lý do để lại |
|---|---|---|
| Đặc khu: phương án rút thời hạn thuê đất xuống 70 năm | Đặc khu | Tác giả không chọn. Có thể thêm sau làm option thứ ba |
| Tự chủ bệnh viện công (NĐ 16/2015) | Y tế | Tác giả không chọn |

---

## 4. Bỏ sáu dải chế độ

> **Đã code (pha A).** Khi thực thi, phạm vi thật rộng hơn bảng dưới: còn **5 event lịch trình khác** bắn từ scheduler chứ không phải từ chính focus của dải (`vie_alt.9/.20/.22`, `vie_axis.1/.3`), và việc xóa file BoP đòi phải gỡ tham chiếu `VIE_oligarch_balance` khỏi `VIE_transition_regime`, trigger `VIE_collapse_pole`, và 4 effect `VIE_oli_*` (file `effects_p3b.txt` xóa hẳn vì không còn ai gọi). Đã rewire 22 focus của `round_table_talks`/`dm_*` từng đặt tọa độ tương đối vào `VIE_developmental_state` (bị xóa) sang `VIE_doi_moi_continues`, giữ nguyên vị trí tuyệt đối. `vie_alt.6/.8/.25/.26` giữ nguyên, tạm thời "ngủ" tới khi pha C nối chúng vào ngã rẽ đặc khu.

### 4.1 Dấu chân đo được

**[SỰ KIỆN]**

| Dải | Gốc | Focus | Idea | Event do focus bắn | Mở bởi | Slot đảng |
|---|---|---|---|---|---|---|
| Bảo vệ nền tảng | `defend_the_foundation` | 6 | 4 | `vie_alt.4` | `vie_pol.2.b` (Đại hội IX) hoặc BoP cứng rắn | 4 |
| Tự chủ chiến lược | `tc_strategic_autonomy` | 15 | 6 | `vie_alt.10`, `.11`, `vie_dip.18`, `vie_int.1`, `.10` | `vie_alt.1` (sau HD-981) | — |
| Nhà nước kiến tạo | `developmental_state` | 15 | 7 | — | `vie_pol.5.b` (Đại hội XII) hoặc BoP cải cách | — |
| Luật Đặc khu | `lb_sez_law` | 13 | 6 | `vie_alt.8`, `.25`, `.26` | `vie_alt.6` | 16 |
| Giải cứu ngân hàng | `ol_bailout` | 12 | 5 | `vie_alt.27`, `.28` | `vie_alt.3`, `.7`, `.9`, `vie_axis.1` | 15 |
| Hội đồng Phát triển | `wa_development_council` | 15 | 6 | `vie_alt.29`, `.30`, `vie_int.3` | `vie_alt.31`; cần `pivot_to_the_west` | 0 |
| **Tổng** | | **76** | **34** | **16** | | |

Không dải nào có prerequisite từ ngoài dải, nên xóa focus không làm treo cây khác.

### 4.2 Cách xử lý

| Thành phần | Xử lý |
|---|---|
| 76 focus, loc tương ứng | **Xóa** |
| 34 idea | **Xóa**, trừ `VIE_sez_unrest_idea` (dùng lại ở `sez_pass_99`) |
| 16 event do focus bắn | **Xóa 13.** Giữ `vie_alt.8`, `.25`, `.26` làm hệ quả của đặc khu (mục 3.2). Kiểm tra từng event trong namespace dùng chung (`vie_dip.18`, `vie_int.1`, `.3`, `.10`) không được gọi từ nơi khác |
| `vie_alt.6` Dự thảo Luật Đặc khu | **Giữ, sửa thành event tranh luận** của ngã rẽ đặc khu. Bỏ option mở dải. Scheduler D6 giữ nguyên |
| `vie_alt.1` Sau khủng hoảng giàn khoan | **Giữ** (HD-981 là thật). Bỏ option đặt `VIE_tc_unlocked` |
| `vie_alt.3` Khủng hoảng niềm tin, `vie_alt.7` Rút tiền hàng loạt | **Giữ** (vụ SCB 10/2022 là thật). Bỏ phần đặt `VIE_oligarch_unlocked` |
| `vie_alt.9` Nhà đầu tư nắm quyền chi phối; `vie_axis.1` Kiến tạo trượt thành Tài phiệt | **Xóa** (chuyển thẳng sang slot 15; cả hai đầu cạnh đều bị bỏ) |
| `vie_alt.31` Rò rỉ hồ sơ giám sát | **Đã kiểm tra: giữ.** **[SỰ KIỆN]** Event do focus `VIE_sec_cyber_sovereignty` của dải An ninh bắn, nên là nội dung của dải còn lại. Option **a** (che đậy) giữ nguyên. Option **b** (cải tổ cơ quan an ninh) bỏ cờ `VIE_wa_unlocked` và tooltip `VIE_gate_note_wa`; thay bằng `checks +1` để lựa chọn cải tổ vẫn có hệ quả |
| `vie_pol.2.b`, `vie_pol.5.b` | **Giữ làm biến thể đường lối trong Đảng**, bỏ phần mở dải (mục 7) |
| Power balance `VIE_md_bop_p3.txt` (Tập đoàn ↔ Dân chúng) | **Xóa** file và mọi lệnh dịch thanh này |
| Decision `VIE_ol_credit_squeeze`, danh mục `VIE_oligarch_category` | **Xóa** |
| Lệnh chuyển chế độ sang slot 0, 15, 16 | Xóa cùng focus/event chứa chúng. **Slot 4 giữ**: `VIE_party_rule_active` vẫn coi slot 4 là Đảng cầm quyền |
| Luật chơi AI | Bỏ option `VIE_AUTONOMY`, `VIE_FREE_ZONES` và trọng số của chúng trong `RANDOM`. `VIE_NATIONALIST` **đã rỗng từ trước** (không còn focus `np_*`/`lh_*`), bỏ luôn. Giữ `HARDLINE` (dải An ninh dùng) và `WESTERN` (ngoại giao, quốc phòng dùng) |
| Tham chiếu trong `VIE_md_effects_p3.txt`, `_axis.txt`, `_p2.txt` | Xóa đoạn riêng của dải; giữ phần dùng chung |

### 4.3 Hệ quả

Dải chế độ giả định còn **30 focus**: Dân chủ hóa (`round_table_talks`, 22) và Nhà nước An ninh (`sec_cyber_control`, 8), cộng ngã rẽ 2026 ở khối chính trị. Lựa chọn giả định về kinh tế chuyển hẳn sang **10 ngã rẽ trong nhánh lịch sử** (9 mới cộng điện hạt nhân).

---

## 5. Ràng buộc phải giữ

**Trục.** Sáu dải bị bỏ đều nằm ngoài đường lịch sử, nên hồ sơ trục lịch sử của STEP6 không đổi. Tái cấu trúc chỉ đổi prerequisite và tọa độ. Focus mới trên đường lịch sử (đóng tàu, Dung Quất, NQ 29, các bên lịch sử và focus "quay lại" của ngã rẽ) **không cộng trục**. Chỉ bên giả định của ngã rẽ cộng trục.

**Thời điểm.** Thêm mốc năm cho focus chưa có sẽ đẩy muộn một số hiệu ứng trục trong hồ sơ giai đoạn (nhiều nhất ở Giáo dục, Y tế và Thiên tai). Phải chạy lại hồ sơ STEP6 bằng `_gen/axis_map.py` trên máy local.

**Save cũ.** **Quyết định của tác giả: ghi là không tương thích.** Không thêm code chuyển đổi. Changelog của bản cập nhật ghi rõ: save đang ở chế độ Tài phiệt, Đặc khu Tự do hoặc Hội đồng Phát triển (slot 15, 16, 0) không dùng tiếp được. Save ở các chế độ khác vẫn dùng được; save đã hoàn thành `bauxite_tay_nguyen` hoặc `solar_boom` giữ nguyên vì ID được giữ.

**Tham chiếu chéo.** `check_static.py` phải trả 0 lỗi tham chiếu treo sau khi xóa 76 focus dải chế độ và 3 focus 2025 ở báo cáo Đại hội.

---

## 6. Liên kết với xương sống Đại hội

Nhánh kinh tế **không** đặt dưới các nghị quyết Đại hội, vì kinh tế là chức năng nhà nước dưới mọi chế độ. Dùng liên kết mềm: focus nghị quyết đặt cờ; focus kinh tế tương ứng nhận thêm thưởng khi có cờ (HOI4 khó đổi `cost` động **[CẦN THỬ]**).

| Nghị quyết | Focus hưởng lợi | Căn cứ |
|---|---|---|
| NQ Đại hội X | `wto_negotiations` (nay ở ngoại giao), `private_champions` | Đảng viên được làm kinh tế tư nhân; vào WTO 1/2007 |
| NQ Đại hội XI | `restructure_banking`, `equitization_soes` | HNTW3 khóa XI (10/2011): tái cơ cấu ngân hàng, DNNN, đầu tư công |
| NQ Đại hội XII | `soe_gradual_restructuring`, `soe_governance`, `private_champions` | NQ 10, 11, 12-NQ/TW (2017) |
| NQ Đại hội XIII | `science_breakthrough`, `private_sector_engine`, `university_autonomy`, `free_tuition` | NQ 57 (12/2024), NQ 68 (5/2025), NQ 71 (8/2025) |

Liên kết chéo giữa các nhánh (thay cho prerequisite):

| Focus | `available` thêm | Lý do |
|---|---|---|
| `chip_engineers` | `university_autonomy` | Đào tạo kỹ sư cần đại học tự chủ |
| `ev_revolution_batteries` | `power_plan_8` | Xe điện cần lưới điện |
| `island_special_zones` | `VIE_two_tier_done` (báo cáo Đại hội) | Đặc khu 2025 là một phần của cải cách chính quyền hai cấp |
| `bank_bankruptcy` (giảm hậu quả) | đọc `deposit_insurance` | Bảo hiểm tiền gửi giảm cú sốc phá sản |
| `solar_boom` (gỡ timed idea) | hoàn thành `500kv_grid` | Lưới truyền tải hết quá tải |

> **Đã code (pha G), có một điều chỉnh.** Không đổi `cost` động (đúng như `[CẦN THỬ]` đã cảnh báo) và cũng không dùng hiệu ứng trục cho 10 chỗ "focus hưởng lợi" — mỗi chỗ chỉ cộng `add_political_power = 25` khi `has_completed_focus = VIE_resolution_congress_N` tương ứng đã xong (riêng `private_champions` được cộng hai lần, một cho NQ X một cho NQ XII; `soe_gradual_restructuring` cộng 50 PP, đúng như mục 7 nói rõ tên). Chọn PP thay vì trục để không đụng vào hồ sơ STEP6 đã hiệu chuẩn từ pha B. Hai liên kết chéo `bank_bankruptcy`/`solar_boom` hóa ra **đã có sẵn từ pha D**, không cần làm gì thêm. Khi sửa `chip_engineers` phát hiện lỗi có sẵn: focus này có **hai khối `available` riêng biệt** — Clausewitz chỉ giữ khối sau cùng, nên điều kiện `has_completed_focus = VIE_chip_design` ở khối đầu đã bị vô hiệu từ trước, không liên quan gì tới pha này. Đã gộp lại thành một khối khi thêm liên kết `university_autonomy`, tiện tay sửa luôn. `island_special_zones` giờ dùng đúng `VIE_two_tier_done` (báo cáo Đại hội, decision `VIE_rn_xiii_two_tier`) thay cho mốc ngày tạm thời của pha D.

---

## 7. Những gì `VIE_congress_spine_redesign.md` phải sửa theo

Đã sửa trong báo cáo đó: `vie_pol.2.b` và `vie_pol.5.b` giữ lại nhưng không mở dải nào; hai biến thể tinh thần nhiệm kỳ (`VIE_resolution_9_cons_idea`, `VIE_resolution_12_dev_idea`) là toàn bộ hệ quả của chúng. Kịch bản thử 3 và 4 đã cập nhật.

Thêm hai liên kết mới: cờ `VIE_two_tier_done` (decision cuối chuỗi cải tổ 2025 trong báo cáo Đại hội) mở `island_special_zones`; focus nghị quyết Đại hội XII tăng thưởng cho `soe_gradual_restructuring`.

---

## 8. Kế hoạch thực hiện

Làm **bỏ dải trước**: giảm diện tích code trước khi tái cấu trúc, và vừa giải phóng ba event đặc khu để tái dùng.

| Pha | Việc | File chính |
|---|---|---|
| **A. Bỏ sáu dải** | Xóa 76 focus, 33 idea, 15 event (13 do focus bắn, cộng `vie_alt.9` và `vie_axis.1`), BoP Tài phiệt, decision và danh mục Tài phiệt; sửa 5 event cửa (`vie_alt.1`, `.3`, `.6`, `.7`, `.31`); sửa `vie_pol.2`, `.5`; bỏ 3 option luật chơi AI; ghi changelog về save không tương thích | `common/national_focus/VIE_md_focus.txt` · `common/ideas/VIE_md_ideas_p2.txt` · `events/VIE_md_alt.txt`, `_axis.txt`, `_p8.txt`, `_p9.txt`, `_pol.txt` · `common/bop/VIE_md_bop_p3.txt` · `common/decisions/` · `common/game_rules/VIE_md_rules.txt` · `common/on_actions/VIE_md_on_actions_startup.txt` · `common/ai_strategy/VIE_md_ai.txt` · `common/scripted_effects/VIE_md_effects_p3.txt`, `_axis.txt`, `_p2.txt` |
| **B. Tái cấu trúc kinh tế** | Đổi cha khoảng 25 focus theo mục 2.2; tách cột; chuyển y tế và đô thị hóa; focus mới đóng tàu, Dung Quất | `VIE_md_focus.txt` · event Vinashin · loc |
| **C. Hội nhập – FDI sang ngoại giao** | Dời 7 focus sang cột 101–129; BTA đổi cha; thêm search filter | `VIE_md_focus.txt` |
| **D. Ngã rẽ lịch sử** | 21 focus mới; sửa `vie_alt.6`; nối `vie_alt.8`, `.25`, `.26` vào đặc khu; thêm mutex cho `bauxite_tay_nguyen`, `solar_boom`; sửa prerequisite `north_south_hsr`, `rare_earths`, `soe_governance`, `power_plan_8`, `hanoi_metro`; 1 event mới (bán rẻ tài sản nhà nước); idea và timed idea mới | `VIE_md_focus.txt` · `events/VIE_md_alt.txt`, `_p8.txt`, `events/VIE_md_eco_p2.txt` · `common/ideas/` (file mới cho ngã rẽ) · loc |
| **E. Khối Xã hội** | Hai gốc mới cho Lao động – xã hội; focus NQ 29; gộp `labor_code_2019` với `vie_pol.27` | `VIE_md_focus.txt` · loc |
| **F. Mốc năm** | Thêm `available = { date > … }` cho các focus mang tên chương trình có năm (mục 2.2, 2.4) | `VIE_md_focus.txt` |
| **G. Liên kết mềm** | Mục 6, sau khi xương sống Đại hội đã có | `VIE_md_focus.txt` |
| **H. Kiểm tra** | `check_static.py` = 0 lỗi; `_gen/fix_spacing.py`, `_gen/overview.py`; hồ sơ trục STEP6; chạy thử trong game | local |

Loc mới đặt ở `localisation/english/replace/` (UTF-8 BOM, header `l_english:`), theo quy ước của các file `VIE_md_vi_*`.

### 8.1 Kịch bản thử trong game

1. **AI lịch sử 2000 → 2027:** chọn đúng 9 bên lịch sử; `north_south_hsr` chỉ mở sau 11/2024; `island_special_zones` mở sau 7/2025; `error.log` không có tham chiếu tới focus, idea, event đã xóa.
2. **Không làm `sez_three_zones`:** `vie_alt.6` vẫn bắn tháng 6/2018 và cặp Hoãn / Thông qua vẫn mở; không có thưởng thêm của cờ `VIE_sez_prepared`.
3. **Chọn `sez_pass_99`:** nhận `VIE_sez_unrest_idea`; khoảng một năm sau `vie_alt.8` bắn; sau `sez_strategic_investors` có `vie_alt.25` và `.26`. `sez_postpone` bị khóa.
4. **Chọn `hsr_2010_approve`:** timed idea chạy; `north_south_hsr` mở từ 2020.
5. **Chọn `bank_bankruptcy` khi đã và chưa làm `deposit_insurance`:** hậu quả chênh nhau một nửa.
6. **Chọn `solar_boom`:** timed idea quá tải lưới tồn tại tới khi làm `500kv_grid`.
7. **Chọn `vie_pol.2.b` và `vie_pol.5.b`:** không mở dải nào.
8. **Làm bảo hiểm y tế năm 2008 mà chưa làm giáo dục; làm `private_champions` mà chưa làm `scic`:** được.
9. **Hội nhập – FDI ở cột 101–129:** `multilateral_champion` và `samsung_partnership` vẫn mở như cũ.
10. **Game rule `RANDOM`:** không bao giờ chọn AI path đã bỏ.

---

## 9. Quyết định đã chốt

| Câu hỏi | Quyết định của tác giả | Ảnh hưởng tới báo cáo |
|---|---|---|
| Sự kiện đặc khu 2018 khi người chơi không làm focus chuẩn bị | **Event luôn xảy ra theo ngày** | Mục 3.2: `sez_three_zones` thành focus chuẩn bị không bắt buộc; scheduler D6 giữ nguyên |
| Nông nghiệp và Hội nhập – FDI | **Hội nhập – FDI sang cây ngoại giao**; Nông nghiệp ở lại kinh tế | Mục 2.3 |
| Thêm ngã rẽ | **Mở rộng Hà Nội 2008, tái cơ cấu DNNN 2017, giá FIT điện mặt trời 2017** | Mục 3.3; tổng 9 ngã rẽ mới |
| Save cũ ở các chế độ bị bỏ | **Ghi là không tương thích** | Mục 5; bỏ code chuyển đổi ở pha A |
| `vie_alt.31` có còn cần cho dải An ninh | Kiểm tra code: **có**, event thuộc dải An ninh | Mục 4.2: giữ event, chỉ bỏ cờ mở dải Hội đồng Phát triển |

Không còn câu hỏi mở. Bước tiếp theo là pha A.
