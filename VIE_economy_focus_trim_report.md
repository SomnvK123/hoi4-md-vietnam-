# Báo cáo: tinh gọn khối Kinh tế của cây focus VIE

> Ngày: 03/10/2026 · Trạng thái: **đề xuất, chưa sửa code**  
> Phạm vi: các nhánh dưới `VIE_doi_moi_continues` và các root kinh tế, **không gồm nhánh Hạ tầng (đã chốt, giữ nguyên)**

---

## 1. Vấn đề

Khối Kinh tế (không tính Hạ tầng) có **125 focus**, nhiều focus chỉ là **một dự án, một nhà máy hay một doanh nghiệp** (nhà ga T3, hầm Hải Vân, Dung Quất 2, chuỗi Apple, liên doanh đóng tàu...). Cây focus vì thế dài, rời rạc và lạc khỏi đúng nghĩa *national focus*: **lựa chọn chiến lược của quốc gia**.

## 2. Tiêu chí giữ một focus

Một focus chỉ nên tồn tại khi đáp ứng **ít nhất 2 trong 3**:

1. **Tầm quốc gia:** là nghị quyết, luật, chiến lược, hoặc siêu dự án mang tính biểu tượng quốc gia.
2. **Có lựa chọn hoặc bước ngoặt:** có nhánh loại trừ (⟷), hoặc mở ra cả một hướng phát triển.
3. **Có tác động gameplay riêng:** idea, cơ chế, hoặc mở khóa focus khác.

Không đạt thì xử lý như sau:

| Loại | Chuyển thành |
|---|---|
| Mốc lịch sử có ngày cụ thể (khánh thành, sự cố) | **Event** |
| Việc tùy chọn, có thể lặp lại (xây thêm, hỗ trợ doanh nghiệp) | **Decision** |
| Dự án nhỏ cùng loại | **Gộp** vào một focus, ghi tên dự án trong mô tả |

---

## 3. Đề xuất theo nhánh

### 3.1 Công nghiệp hóa – Hiện đại hóa: 35 → 21

| Giữ (16) | Gộp (5 focus mới thay cho 12 focus cũ) | Bỏ, hoặc chuyển thành event/decision (8) |
|---|---|---|
| `industrialization_strategy` | **Tự chủ thép cán nóng** ← `hoa_phat_hrc_steel` + `hoa_phat_dung_quat_2` | `vinashin_restructuring_sbic` → thêm lựa chọn vào event `vie_eco.5` |
| `nq23_industrial_policy` | **Nhà cung ứng nội địa** ← `tier1_vendor_localization` + `precision_mechanics_molds` | `shipbuilding_joint_ventures`, `offshore_wind_fabrication` → decision |
| `nq29_industrialization_2045` | **Công xưởng châu Á** ← `manufacturing_hub` + `apple_supply_chain` | `global_auto_export` → đã có event `vie_auto.1` |
| `samsung_partnership` | **Lắp ráp và đóng gói chip** ← `intel_hcmc` + `osat_packaging` | `eco_industrial_parks`, `industrial_productivity_program` → bỏ |
| `formosa_steel_complex` | **Chuỗi dệt may khép kín** ← `cptpp_yarn_forward` + `textile_dyeing_parks` + `green_textiles` | `chip_design` → gộp vào `semiconductor_ambition` |
| `shipbuilding_vinashin` | | `integrated_auto_supplier_park` → gộp vào `domestic_automotive` |
| `supporting_industries` | | |
| `china_plus_one` | | |
| `semiconductor_ambition`, `chip_engineers`, `semiconductor_fab` | | |
| `domestic_automotive`, `ev_revolution_batteries` | | |
| `textile_garment_exports`, `investment_support_fund`, `modern_industrial_nation_2030` | | |

Giữ cơ chế **Tỷ lệ nội địa hóa**, chia lại điểm cho các focus còn lại.

### 3.2 Các nhánh kinh tế khác: 90 → khoảng 63

| Nhánh | Hiện | Đề xuất | Việc chính |
|---|---|---|---|
| Năng lượng (PetroVietnam) | 22 | 16 | Gộp 4 focus Petrolimex (hạ nguồn, dự trữ, ENEOS, trạm sạc) thành **An ninh xăng dầu**. Gộp `solar_boom` / `solar_auction` thành một lựa chọn. Gộp `dppa_market_reform` vào `power_plan_8` |
| Khai khoáng (Vinacomin) | 7 | 4 | Giữ lựa chọn bauxite ⟷ và đất hiếm. Gộp Than Quảng Ninh, Núi Pháo, Thạch Khê thành **Khai khoáng chiến lược** |
| Doanh nghiệp – Thương mại | 18 | 14 | Gộp `wto_negotiations` và `wto_reforms`. Gộp `new_rural_development` và `high_tech_agriculture`. `mekong_climate_adaptation` → event |
| Ngân hàng | 17 | 13 | Giữ chuỗi xử lý nợ xấu và các lựa chọn. Gộp `deposit_insurance` vào `restructure_banking`, gộp `cashless_payments` vào `state_bank_modernization` |
| Số hóa | 12 | 8 | Gộp `mobile_3g_4g` và `mobile_networks`, gộp `digital_id` và `national_data_center`, gộp `make_in_vietnam` và `digital_tech_industry_law` |
| Khoa học (NAFOSTED) | 6 | 4 | Gộp `vinasat` và `earth_observation` thành **Chương trình vệ tinh** |
| Tầm nhìn 2045 | 8 | 4 | Gộp `green_growth` và `carbon_circular_economy`, gộp `high_income_2045` và `developed_nation_2045` |

---

## 4. Tổng kết

| | Hiện | Sau tinh gọn |
|---|---|---|
| Khối Kinh tế (không tính Hạ tầng) | 125 | **khoảng 84** |
| Cả cây | 378 | **khoảng 337** |

Không mất nội dung lịch sử: tên dự án vẫn còn trong mô tả focus gộp, hoặc trở thành event và decision.

## 5. Rủi ro khi làm

- **Cờ và tham chiếu:** một số focus bị gộp đặt cờ mà event khác đọc, như `VIE_steel_complex_built` (event Formosa) và `VIE_auto_program`. Focus gộp phải giữ lại các cờ này.
- **Điều kiện chéo:** `chip_engineers` cần `higher_education_law`, `net_zero_2050` cần `disaster_law_2013`, `capstone` cần `semiconductor_fab` hoặc xe điện. Cần cập nhật khi đổi id.
- **Loc:** xóa khóa của focus bị bỏ, viết mô tả mới cho focus gộp (liệt kê dự án con).
- **AI:** cân lại `ai_will_do`, vì focus gộp có reward lớn hơn.

## 6. Thứ tự làm đề xuất

1. Công nghiệp hóa: nhánh phình to nhất, chủ yếu do các bước gần đây.
2. Năng lượng và Khai khoáng.
3. Ngân hàng, Doanh nghiệp, Số hóa, Khoa học, Tầm nhìn 2045.

Mỗi bước chạy `standardize_focus_tree.py`, `validate_focus_tree.py`, `verify_all_loc.py`, rồi kiểm tra trong game.
