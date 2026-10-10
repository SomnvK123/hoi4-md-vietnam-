# Nhánh công nghiệp Việt Nam — v31 (09/10/2026)

> Hiện hành **v32 — 10/10/2026**: focus cấp idea chính sách trực tiếp, decision nâng bậc khi bàn giao. Xem [manifest effect v32](.claude/docs/policy_rewards/v32/README.md) và [kiểm định](.claude/docs/policy_rewards/v32/validation.md). Layout, vốn, tiến độ và gate giữ nguyên; mô tả cũ chỉ nhận modifier khi bàn giao được thay bằng các bậc v32.

Triển khai trực tiếp trên `main`: 39 → 24 focus, giữ 22 ID, thêm 2 và archive 17. Game mới bắt buộc; không có migration save. Hai cặp mutex khiến tối đa 22 focus được hoàn thành trong một lượt chơi.

Baseline lúc bắt đầu: 416 focus, riêng thay đổi công nghiệp giảm tổng 15 xuống 401. Workspace có chỉnh sửa đồng thời ở Lục quân/quốc phòng; tổng cây hiện tại phải lấy từ audit, không dùng 401 như kết quả cuối. Baseline hash được giữ nguyên để phát hiện và báo riêng những thay đổi ngoài phạm vi.

## Focus và layout

Bốn vùng X124–126 / X128–130 / X132–136 / X138–142; sáu ngành có tiến độ độc lập. Tọa độ tuyệt đối trong bảng; code dùng offset với cha trực tiếp đã khai báo trước. AND là nhiều block prerequisite, OR là nhiều focus trong cùng block. Hai mutex hai chiều; Y8 trống. Công nghiệp hỗ trợ phải bàn giao trước sáu cửa ngành.

| ID (VIE_) | Tên | Cost | X,Y | Prerequisite | Điều kiện thêm |
|---|---|---:|---|---|---|
| `industrialization_strategy` | Chiến lược công nghiệp hóa quốc gia | 5 | 133,1 | (doi_moi_continues) | `date > 2001.4.30` |
| `supporting_industries` | Phát triển công nghiệp hỗ trợ | 7 | 133,2 | (industrialization_strategy) | `Không` |
| `vinashin_restructuring_sbic` | Tái cơ cấu ngành đóng tàu | 5 | 124,3 | (supporting_industries) | `VIE_ind_support_done = yes date > 2004.12.31` |
| `national_steel_program` | Chương trình công nghiệp thép quốc gia | 7 | 126,3 | (supporting_industries) | `VIE_ind_support_done = yes date > 2007.12.31` |
| `textile_garment_exports` | Công nghiệp dệt may xuất khẩu | 5 | 128,3 | (supporting_industries) | `VIE_ind_support_done = yes` |
| `domestic_automotive` | Chương trình sản xuất ô tô | 7 | 130,3 | (supporting_industries) | `VIE_ind_support_done = yes date > 2017.12.31` |
| `electronics_export_program` | Công nghiệp điện tử xuất khẩu | 5 | 134,3 | (supporting_industries) | `VIE_ind_support_done = yes date > 2007.12.31 VIE_ind_wto_ready = yes` |
| `chip_engineers` | Nền tảng nhân lực và R&D bán dẫn | 7 | 140,3 | (supporting_industries) | `VIE_ind_support_done = yes date > 2009.12.31 VIE_ind_education_ready = yes` |
| `ev_revolution_batteries` | Linh kiện, pin và điện khí hóa | 7 | 130,4 | (domestic_automotive) | `VIE_ind_auto_base_done = yes` |
| `fdi_fast_track` | Thu hút FDI nhanh | 5 | 132,4 | (electronics_export_program) | `Không` |
| `fdi_technology_screening` | Sàng lọc FDI công nghệ | 5 | 136,4 | (electronics_export_program) | `Không` |
| `chip_design_packaging_priority` | Ưu tiên thiết kế và đóng gói | 5 | 138,4 | (chip_engineers) | `Không` |
| `chip_pilot_fab_priority` | Ưu tiên chế tạo thí điểm | 5 | 142,4 | (chip_engineers) | `Không` |
| `shipbuilding_joint_ventures` | Đóng tàu dân sự và công trình biển | 7 | 124,5 | (vinashin_restructuring_sbic) | `VIE_ind_ship_governance_done = yes` |
| `hoa_phat_hrc_steel` | Thép chất lượng cao và năng lực HRC | 7 | 126,5 | (national_steel_program) | `VIE_ind_steel_base_done = yes` |
| `green_textiles` | Chuỗi giá trị dệt may và sản xuất xanh | 7 | 128,5 | (textile_garment_exports) | `VIE_ind_textile_base_done = yes VIE_ind_green_trade_ready = yes` |
| `global_auto_export` | Năng lực xuất khẩu ô tô | 7 | 130,5 | (ev_revolution_batteries) | `VIE_ind_auto_ev_done = yes VIE_ind_wto_ready = yes` |
| `apple_supply_chain` | Nội địa hóa chuỗi cung ứng điện tử | 7 | 134,5 | (fdi_fast_track OR fdi_technology_screening) | `VIE_ind_electronics_base_done = yes` |
| `chip_design` | Năng lực thiết kế chip | 7 | 138,5 | (chip_design_packaging_priority OR chip_pilot_fab_priority) | `VIE_ind_chip_workforce_done = yes` |
| `osat_packaging` | Đóng gói và kiểm thử chip | 7 | 142,5 | (chip_design_packaging_priority OR chip_pilot_fab_priority) | `VIE_ind_chip_workforce_done = yes` |
| `manufacturing_hub` | Trung tâm chế tạo điện tử | 7 | 134,6 | (apple_supply_chain) | `VIE_ind_electronics_suppliers_done = yes` |
| `semiconductor_fab` | Chế tạo chip thí điểm | 7 | 140,6 | (chip_design) AND (osat_packaging) AND (chip_engineers) | `VIE_ind_chip_ready = yes` |
| `industrial_productivity_program` | Cải cách và nâng cao năng suất công nghiệp | 7 | 133,7 | (shipbuilding_joint_ventures OR green_textiles OR hoa_phat_hrc_steel OR global_auto_export OR manufacturing_hub OR osat_packaging) | `VIE_ind_three_sectors = yes` |
| `modern_industrial_nation_2030` | Quốc gia công nghiệp hiện đại 2030 | 7 | 133,9 | (industrial_productivity_program) | `VIE_ind_capstone_ready = yes` |

Các focus mở chương trình; nhà máy, điểm, bonus và idea được cấp ở bàn giao. Các mốc công nhận không khóa 2030. Nhân lực bán dẫn mở từ 2010 cùng Luật giáo dục đại học; AI lịch sử giữ 2024, fab 2026, năng suất sau 2023 và capstone 2030.

## Vòng đời và ngân sách

Category `VIE_industry_category` dành cho original_tag VIE, hiện sau chiến lược. 17 chương trình logic, 19 decision do hai lựa chọn thép và hai thời lượng fab. Mỗi ngành và nhóm chung có slot riêng; các ngành chạy song song. Start kiểm focus/chính sách, bậc, tiền và state sở hữu/kiểm soát; trừ treasury qua MD một lần và lưu `_paid`. Finish kiểm `_running` và bậc, bàn giao một lần, dọn slot. Mất state hoàn tiền đúng khoản đã trả và cho thử lại. State đầy được công nhận nâng cấp năng lực nhưng không xây và không gọi fallback random. Helper MD dùng `skip_payment=1`, reset 0, guard slot include_locked tương ứng.

| Decision (VIE_ind_d_) | Tỷ USD chuẩn | Ngày | Công trình tối đa | Điểm |
|---|---:|---:|---|---:|
| `support` | 2 | 180 | Nâng cấp năng lực | 6 |
| `ship_governance` | 1 | 180 | Nâng cấp năng lực | 2 |
| `ship_civil` | 7.5 | 365 | dockyard 519 | 2 |
| `textile_base` | 7.5 | 365 | industrial_complex 522 | 2 |
| `textile_green` | 2 | 180 | Nâng cấp năng lực | 2 |
| `steel_foreign` | 6 | 365 | industrial_complex 521 | 2 |
| `steel_domestic` | 7.5 | 450 | industrial_complex 521 | 2 |
| `steel_hrc` | 7.5 | 365 | industrial_complex 521 | 2 |
| `auto_base` | 7.5 | 365 | industrial_complex 522 | 1 |
| `auto_ev` | 7.5 | 365 | industrial_complex 521 | 1 |
| `auto_export` | 1 | 180 | Nâng cấp năng lực | 2 |
| `electronics_base` | 7.5 | 365 | industrial_complex 522 | 2 |
| `electronics_suppliers` | 2 | 180 | Nâng cấp năng lực | 2 |
| `chip_workforce` | 2 | 365 | Nâng cấp năng lực | 1 |
| `chip_design` | 1 | 180 | Nâng cấp năng lực | 1 |
| `chip_osat` | 7.5 | 365 | industrial_complex 519 | 2 |
| `fab_design` | 15 | 720 | industrial_complex 519 | 2 |
| `fab_pilot` | 12 | 630 | industrial_complex 519 | 2 |
| `productivity` | 1 | 180 | Nâng cấp năng lực | 4 |

FDI nhanh giảm 25% điện tử nền tảng; FDI chọn lọc tốn 25 PP, thêm 2 điểm và một bonus CAT_industry 25% khi nền tảng bàn giao. Thiết kế/OSAT giảm 25% hai đợt thiết kế và OSAT, fab 15/720; ưu tiên fab giữ giá đầy đủ hai đợt này, fab 12/630. Cả hai đường mở toàn bộ năng lực. Mỗi thiết kế/OSAT cấp CAT_microchips 25%, một lần.

Tổng đủ sáu ngành và fab: 80,625–84,875 tỷ; không fab: 66,5–72 tỷ, không tính event. Tối đa 8 IC và 1 dockyard. Đây là thông số cân bằng gameplay, không phải vốn lịch sử doanh nghiệp.

## Điểm, ngành và capstone

Root 10 điểm, hỗ trợ 6, năng suất 4 = nền chung 20. Mỗi ngành đủ các đợt đóng góp 4; bất kỳ ba ngành đạt 32 mà không bắt chọn lọc FDI/fab. Chip đủ nhân lực + thiết kế + OSAT; fab là nâng cao. Điện tử cần hai đợt và focus manufacturing_hub. Năng suất cần 3/6 ngành thực tế; capstone cần năng suất đã bàn giao, vẫn đủ 3/6 và ít nhất 32 điểm. Getter trạng thái và tooltip dùng cùng trigger ngành.

Idea fab thay idea bán dẫn nền tảng; capstone thay idea năng suất. Trần: growth modifier 0,080; research speed 0,015; factory output 0,060; corporate tax 0,060; IC construction 0,090. Capstone thêm PP50/stability0,02. Không còn tăng trưởng trực tiếp hay treasury miễn phí trong focus công nghiệp và thông báo ô tô.

## Event và tích hợp

Vinashin giữ lịch 2010, risk và processed flag. Cải cách trước 2010 ghi risk di sản +2 một lần; governance bàn giao reset risk, stability+0,01, không đặt processed và không xóa debt HSR. Cải cách giảm phí bailout/prosecution/fallback xuống 1/0,5/0,75 tỷ. Immediate, option và fallback có guard chống phát lại.

`vie_ind.1` chọn vốn thép một lần; `.2` kiểm tra xuất xứ sau trung tâm điện tử theo FDI nhanh; `.3` thông báo fab. Lựa chọn thép giữ pending qua popup cooldown và catch-up. Chỉ thép FDI đã bàn giao đặt steel_complex_built; Formosa chỉ trong cửa sổ 2016, không khủng hoảng cho nội địa hay dự án muộn. `vie_auto.1` không reward; `.2` đọc EV đã bàn giao và Petrolimex, cấp một lần PP25/stability0,01. Catch-up không đầu tư hoặc bàn giao.

`VIE_innovation_nation` chỉ đổi gate semiconductor_ambition thành nhân lực/R&D đã bàn giao. Không đổi reward/prerequisite/layout. Shortcut công nghiệp giữ tên và target. Idea hỗ trợ hợp nhất cơ khí/Tier1; bỏ idea phụ trợ ô tô riêng. Localization Việt có dấu, BOM, 229 key trong file chương trình mới.

## Tài nguyên và nghiệm thu

Provider MD/base game đã được kiểm bằng sprite và texture thật. Sửa token không có provider trong nhánh: focus_generic_destroyer → naval_industry; focus_generic_industry_3 → industry3; focus_generic_diplomatic_treaty → diplomatic_treaty. Idea hỗ trợ dùng industrial_focus đã xác minh. Không tạo artwork hoặc sửa master/texture.

- [Manifest và baseline](.claude/docs/industry/v31/structure.json)
- [Mapping 17 ID bỏ](.claude/docs/industry/v31/retired_mapping.md)
- [Kiểm định và checklist runtime](.claude/docs/industry/v31/validation.md)
- [Sơ đồ sau sửa](.claude/docs/industry/v31/after.png)
- [Sơ đồ trước sửa](.claude/docs/industry/v31/before.png)
- [Drawio hai trang](.claude/docs/industry/v31/industry_v31.drawio)

Thiết kế v17 giữ tại `.claude/docs/industry/v31/v17_design_archive.md` để tra lịch sử. Không dùng thiết kế cũ làm nghiệm thu v31.
