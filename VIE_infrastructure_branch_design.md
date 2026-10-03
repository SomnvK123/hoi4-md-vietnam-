# VIE — Nhánh "Phát triển Kết cấu Hạ tầng"

> Trạng thái: **Bước 1 đã code (03/10/2026)**: root, 4 nhánh, sửa H4–H5, đổi shortcut. H3 (thay `add_building_construction` bằng `one_state_infrastructure`) để sang Bước 2 vì đổi chi phí. **Bước 2 đã code (03/10/2026): nhánh A đầy đủ (12 focus mới), biến `VIE_expressway_km`, sửa H3, event `vie_infra.1`–`.2`.** **Bước 3 đã code (03/10/2026): nhánh B đường sắt (9 focus mới, 3 lựa chọn đối tác HSR loại trừ nhau).** `north_south_hsr` chỉ còn là phê duyệt chủ trương (−1 bn); phần xây dựng chuyển sang `hsr_groundbreaking`. `hcmc_metro` và `lao_cai_haiphong_rail` dưới `reunification_line_upgrade`. **Bước 4 đã code (03/10/2026): nhánh C hàng không (10 focus mới, event `vie_infra.3` qua `VIE_event_scheduler_infra`).** **Bước 5 đã code (03/10/2026): `infrastructure_breakthrough_nq13` (độc lập, không khóa dự án nào), `logistics_strategy` (nhánh D), capstone `synchronized_infrastructure_2030` (cần 5.000 km cao tốc + khởi công HSR + Long Thành), 2 idea mới.** Nhánh Hạ tầng đã triển khai đủ 5 bước; phần còn lại là test trong game và tra nguồn số liệu. Nhánh C đặt ở dưới root (y 10–16) vì phía phải đã bị cụm đường sắt đô thị và cụm năng lượng chiếm. Khác thiết kế gốc ở mục 4: thêm `expressway_regional_links` (800 km) để tổng km đạt được mốc 3.000; `north_south_expressway` yêu cầu `hcmc_trung_luong_expressway`; mốc 3.000 km yêu cầu km > 2599 rồi cộng 300 khi hoàn thành. Ngày: 03/10/2026  
> Phạm vi: thay cụm 9 focus đang treo dưới `VIE_north_south_expressway` bằng một root Hạ tầng có 3 nhánh chính (Đường bộ, Đường sắt, Hàng không) và 1 nhánh phụ (Cảng biển).

---

## 1. Hiện trạng

### 1.1 Chín focus đang có

| Focus | Mốc | Reward chính | Ghi chú |
|---|---|---|---|
| `north_south_expressway` Đường cao tốc Bắc – Nam | 2011 (`VIE_era_2011`) | `VIE_expressway_idea`, infra +1 **mọi state**, −3 bn | Đang là root của cụm |
| `lach_huyen_port` Cảng Lạch Huyện | 2015 | 522 infra, tăng trưởng | |
| `cai_mep_port` Cảng Cái Mép – Thị Vải | 2011 | `VIE_ports_idea`, 519 infra | |
| `lao_cai_haiphong_rail` Lào Cai – Hà Nội – Hải Phòng | 12/2025 | 523 infra, quan hệ với CHI | Con của Lạch Huyện |
| `long_thanh_airport` Sân bay Long Thành | 6/2025 | 519 infra, tăng trưởng | Đòi `hcmc_metro` |
| `hsr_2010_reject` ⟷ `hsr_2010_approve` | 2010 | reject: +25 PP. approve: nợ công 10 năm | Lựa chọn lịch sử (QH bác 19/6/2010) |
| `north_south_hsr` Đường sắt tốc độ cao Bắc – Nam | 12/2024 hoặc ngay sau approve | infra +1 **mọi state**, −4 bn | |
| `hcmc_metro` Metro TP.HCM | 2013 | 519 infra | Không có prerequisite |

### 1.2 Vấn đề

| # | Vấn đề |
|---|---|
| H1 | **Root mở từ 2011**, nên 2001–2010 không có gì để làm. Trong khi đó giai đoạn này có Hầm Hải Vân (2005), cao tốc TP.HCM – Trung Lương (2010), cầu Cần Thơ (2010) |
| H2 | **Lẫn chủ đề:** cảng biển, sân bay, đường sắt, metro đều nằm chung dưới "cao tốc". Không có trục rõ ràng cho từng loại hạ tầng |
| H3 | `north_south_expressway` và `north_south_hsr` gọi `add_building_construction` trực tiếp trên mọi state. Sai chuẩn của mod (mục 6): phải dùng `one_state_infrastructure` |
| H4 | `long_thanh_airport` yêu cầu `hcmc_metro`. Về thực tế, hai dự án không phụ thuộc nhau |
| H5 | `hcmc_metro` không có prerequisite (root mồ côi) |
| H6 | Mỗi dự án chỉ cho 1 cấp infra ở 1 state, nên không cảm nhận được quy mô (654 km hay 3.000 km cao tốc trông như nhau) |

Đã sửa ngay khi rà (03/10/2026): `hcmc_metro` còn yêu cầu `VIE_urbanization`, và `VIE_ageing_society` còn yêu cầu `VIE_population_policy`. Cả hai focus kia đã bị xóa ở bước trước, gây soft-lock nên đã gỡ hai điều kiện đó.

---

## 2. Khung mới

```
VIE_infrastructure_development  "Phát triển Kết cấu Hạ tầng"  [ROOT, 2001]
 │
 ├─ A. ĐƯỜNG BỘ – CAO TỐC      (cao tốc Bắc – Nam là xương sống)
 ├─ B. ĐƯỜNG SẮT               (Thống Nhất → đô thị → tốc độ cao → liên vận)
 ├─ C. HÀNG KHÔNG              (nhà ga, sân bay lớn, hãng bay)
 └─ D. CẢNG BIỂN & LOGISTICS   (nhánh phụ, giữ 2 cảng cũ)
          │
          └──► infrastructure_breakthrough_nq13  (mid-game, 1/2012)
                    └──► synchronized_infrastructure_2030  [capstone]
```

- **Root** `VIE_infrastructure_development` (2001): không có prerequisite, guard `VIE_ax_init` giống các root khác. Đổi shortcut `VIE_roads_shortcut` thành `VIE_infrastructure_shortcut`.
- **Mốc giữa:** `infrastructure_breakthrough_nq13`, theo **NQ 13-NQ/TW (1/2012)** về xây dựng kết cấu hạ tầng đồng bộ. Hạ tầng là 1 trong **3 đột phá chiến lược** của Đại hội XI (2011). Focus này mở các dự án lớn sau 2012 và là chỗ tự nhiên cho `VIE_era_2011`.
- **Vị trí:** đặt root ở x=130, y=1 (chỗ cao tốc đang đứng). Bốn nhánh xòe ra trong vùng x 116–146 vừa trống sau khi xóa cụm giáo dục và y tế.

---

## 3. Cơ chế: "km cao tốc" và nguồn vốn

### 3.1 Biến `VIE_expressway_km`

Mỗi dự án cao tốc cộng số km gần đúng với thực tế. Biến hiển thị qua tooltip, cùng mẫu với trục `VIE_ax_*`.

| Mốc | Tổng km (xấp xỉ) | Dùng để |
|---|---|---|
| Sau GĐ1 Bắc – Nam (2020) | ~1.200 | Mở GĐ2 |
| Sau GĐ2 (2025) | **~3.000** (mục tiêu Đại hội XIII) | Mở `idea` hạ tầng cấp 2 |
| Capstone (2030) | **~5.000** | Yêu cầu của `synchronized_infrastructure_2030` |

Như vậy người chơi thấy rõ quy mô (sửa H6). Capstone cũng có điều kiện đo được, không chỉ "đã làm focus X".

### 3.2 Nguồn vốn — lựa chọn có hệ quả

| Kênh | Tác dụng | Gắn với |
|---|---|---|
| **Đầu tư công** | Tốn treasury trực tiếp, nhanh, ít tranh cãi | `ax_decent −1` (trung ương ôm việc) |
| **BOT / PPP** | Rẻ cho ngân sách nhưng có rủi ro event "trạm thu phí" | `ax_market +1`, opinion `industrial_conglomerates +` |
| **ODA Nhật Bản** | Lãi thấp, chậm, cần quan hệ tốt | opinion JAP, `ax_west +1` |
| **Vốn vay Trung Quốc** | Nhanh, rủi ro chậm tiến độ / đội vốn | opinion CHI, `ax_integ` / rủi ro event |

Các dự án lớn (cầu, metro, sân bay) có điều kiện hoặc reward khác nhau theo kênh vốn mà người chơi đã chọn qua cờ (`VIE_infra_funding_*`).

---

## 4. Nhánh A — Đường bộ – Cao tốc

```
infrastructure_development
 └─ transport_strategy_2004 [mới, 2004]
     ├─ hai_van_tunnel [mới, 6/2005]
     ├─ hcmc_trung_luong_expressway [mới, 2/2010]
     │   └─ northern_expressways [mới, 2014–2015]
     └─ can_tho_bridge [mới, 4/2010]
            ⇓ (sau NQ 13)
 north_south_expressway_phase1 [cũ, đổi tên, 2017]
  └─ bot_vs_public_investment:  expressway_bot  ⟷  expressway_public_investment [mới, 2020]
      └─ north_south_expressway_phase2 [mới, 2022]
          ├─ ring_roads_hanoi_hcmc [mới, 2022]
          └─ expressway_3000km [mới, 12/2025]
              └─ expressway_5000km_2030 [mới]
```

| Focus | Cơ sở lịch sử | Reward gợi ý |
|---|---|---|
| `transport_strategy_2004` | Chiến lược phát triển GTVT đến 2020 (2004) | +PP, mở nhánh |
| `hai_van_tunnel` | Hầm đường bộ Hải Vân, dài nhất Đông Nam Á lúc khánh thành (6/2005, ODA Nhật) | 521 infra, opinion JAP |
| `hcmc_trung_luong_expressway` | Tuyến cao tốc đầu tiên của Việt Nam (2/2010) | 519 infra, km +40 |
| `northern_expressways` | Nội Bài – Lào Cai (9/2014), Hà Nội – Hải Phòng (12/2015) | 522 + 523 infra, km +350 |
| `can_tho_bridge` | Cầu Cần Thơ (4/2010). Sự cố sập nhịp dẫn 9/2007 làm 54 người chết | 518 infra. **Event** sập nhịp 2007 nếu đang làm focus |
| `north_south_expressway_phase1` (đổi từ `north_south_expressway`) | NQ 52/2017/QH14: 11 dự án, ~654 km | `VIE_expressway_idea`, km +650, sửa H3 (dùng `one_state_infrastructure` cho 521/519) |
| `expressway_bot` ⟷ `expressway_public_investment` | Năm 2020 Quốc hội chuyển 3 dự án BOT sang đầu tư công vì không hút được nhà đầu tư. Bối cảnh: khủng hoảng "trạm BOT đặt nhầm chỗ" Cai Lậy (2017) | BOT: −1 bn, `ax_market +1`, rủi ro event thu phí. Công: −4 bn, `ax_decent −1`, +stability |
| `north_south_expressway_phase2` | NQ 44/2022/QH15: 12 dự án, ~729 km | km +730, −4 bn, **cần bankruptcy guard** |
| `ring_roads_hanoi_hcmc` | Vành đai 4 Hà Nội và Vành đai 3 TP.HCM (2022) | 522 + 519 infra, tăng trưởng |
| `expressway_3000km` | Mục tiêu 3.000 km cao tốc cuối 2025 | Yêu cầu `VIE_expressway_km > 2999`. Nâng `VIE_expressway_idea` lên cấp 2 |
| `expressway_5000km_2030` | Mục tiêu ~5.000 km năm 2030 | Yêu cầu km > 4999, idea cấp 3 |

**Event đi kèm:** `vie_infra.1` sập nhịp dẫn cầu Cần Thơ (2007), `vie_infra.2` khủng hoảng trạm BOT Cai Lậy (2017, chỉ khi chọn BOT).

---

## 5. Nhánh B — Đường sắt

```
infrastructure_development
 └─ reunification_line_upgrade [mới]
     ├─ hsr_2010_reject ⟷ hsr_2010_approve [cũ]
     │       └─ north_south_hsr_nq172 [cũ, đổi tên, 11/2024]
     │           └─ hsr_technology_partner: JAP ⟷ EU ⟷ CHI [mới]
     │               └─ hsr_groundbreaking [mới]
     ├─ urban_rail_hanoi (Cát Linh – Hà Đông) [mới, 11/2021]
     │   └─ urban_rail_special_mechanism_nq188 [mới, 2025]
     │       └─ metro_network_2035 [mới]
     ├─ hcmc_metro [cũ, sửa H5: prerequisite urban rail]
     └─ lao_cai_haiphong_rail [cũ, chuyển sang đây, 12/2025]
         └─ domestic_rail_industry [mới]
```

| Focus | Cơ sở lịch sử | Reward gợi ý |
|---|---|---|
| `reunification_line_upgrade` | Nâng cấp đường sắt Thống Nhất (khổ 1 m), cải tạo cầu, hầm yếu | 521 infra, +PP |
| `north_south_hsr_nq172` (đổi tên `north_south_hsr`) | NQ 172/2024/QH15 (11/2024): 1.541 km, 350 km/h, ~67 tỷ USD | Giữ nhánh lựa chọn 2010. Chỉ phê duyệt chủ trương: −1 bn, mở bước tiếp. Sửa H3 |
| `hsr_technology_partner_*` (3 lựa chọn) | Việt Nam đặt điều kiện chuyển giao công nghệ khi chọn đối tác | JAP: opinion JAP, `ax_west +1`, chậm hơn (thêm cost). EU: cân bằng. CHI: rẻ, nhanh, opinion CHI, `ax_integ`, rủi ro nợ |
| `hsr_groundbreaking` | Mục tiêu khởi công cuối 2026 | −5 bn, `VIE_state_debt_overhang` ngắn nếu vay. **Guard**. Tất cả state ven biển +1 infra qua `one_state_infrastructure` |
| `urban_rail_hanoi` | Metro Cát Linh – Hà Đông (11/2021, vốn vay TQ, chậm tiến độ và đội vốn). Nhổn – ga Hà Nội (đoạn trên cao 8/2024) | 522 infra, +stability. Nếu kênh vốn là CHI thì có event đội vốn |
| `hcmc_metro` | Metro số 1 Bến Thành – Suối Tiên (khai thác 12/2024, ODA Nhật) | Giữ reward, thêm prerequisite `urban_rail_hanoi` hoặc `reunification_line_upgrade` |
| `urban_rail_special_mechanism_nq188` | NQ 188/2025/QH15: cơ chế đặc thù phát triển mạng lưới đường sắt đô thị Hà Nội và TP.HCM (mô hình TOD) | 522 + 519 infra, `ax_decent +1` |
| `metro_network_2035` | Mục tiêu hoàn thành mạng metro hai thành phố | −5 bn, **guard**, idea đô thị |
| `lao_cai_haiphong_rail` | NQ 187/2025/QH15: tuyến khổ tiêu chuẩn kết nối Trung Quốc, khởi công 12/2025 | Giữ reward cũ, chuyển prerequisite sang nhánh đường sắt |
| `domestic_rail_industry` | Mục tiêu nội địa hóa toa xe, đầu máy và hạ tầng đường sắt | Nối sang `VIE_supporting_industries` (nhánh công nghiệp). Tech bonus |

---

## 6. Nhánh C — Hàng không

```
infrastructure_development
 └─ airport_master_plan [mới, 2008]
     ├─ noi_bai_t2 [mới, 1/2015]
     │   └─ aviation_market_opening [mới, 12/2011]
     │       └─ socialized_airports ⟷ acv_monopoly [mới, 2018]
     │           └─ van_don_airport [mới, 12/2018] (chỉ nhánh xã hội hóa)
     ├─ long_thanh_approval [mới, 6/2015]
     │   └─ long_thanh_airport [cũ, sửa H4]
     ├─ tan_son_nhat_t3 [mới, 4/2025]
     ├─ dual_use_airports [mới]  (nối nhánh Không quân)
     └─ airport_network_2030 [mới, 6/2023]
```

| Focus | Cơ sở lịch sử | Reward gợi ý |
|---|---|---|
| `airport_master_plan` | Quy hoạch phát triển GTVT hàng không (2008) | +PP, mở nhánh |
| `noi_bai_t2` | Nhà ga T2 Nội Bài (1/2015, ODA Nhật) | `522 one_state_air_base`, opinion JAP |
| `aviation_market_opening` | Vietjet bay chuyến đầu tiên (12/2011): hãng tư nhân phá thế độc quyền | `ax_market +1`, tăng trưởng |
| `socialized_airports` ⟷ `acv_monopoly` | Tranh luận xã hội hóa đầu tư cảng hàng không, hay giữ ACV quản lý | Xã hội hóa: `ax_market +1`, mở Vân Đồn. ACV: `ax_decent −1`, treasury +1 (cổ tức) |
| `van_don_airport` | Sân bay Vân Đồn: sân bay đầu tiên do tư nhân đầu tư (12/2018) | `523 one_state_air_base`, opinion `industrial_conglomerates +3` |
| `long_thanh_approval` | NQ 94/2015/QH13: chủ trương đầu tư Long Thành. Giai đoạn 1 khởi công 1/2021 | −2 bn, mở `long_thanh_airport` |
| `long_thanh_airport` | Mục tiêu đưa vào khai thác 2026 | Sửa H4: prerequisite là `long_thanh_approval`, bỏ điều kiện `hcmc_metro`. Thêm `519 one_state_air_base` |
| `tan_son_nhat_t3` | Nhà ga T3 Tân Sơn Nhất (4/2025) | `519 one_state_air_base`, +stability |
| `dual_use_airports` | Sân bay lưỡng dụng dân sự – quân sự (Phan Thiết, Chu Lai) | Air base ở 521. Nối nhánh `VIE_airf_*` |
| `airport_network_2030` | QĐ 648/QĐ-TTg (6/2023): quy hoạch 30 cảng hàng không đến 2030 | Idea hàng không: tăng trưởng, `trade_opinion_factor` |

**Event đi kèm:** `vie_infra.3` Vietnam Airlines kiệt quệ vì COVID-19 (2020): giải cứu bằng ngân sách hay để thị trường tự xử lý.

---

## 7. Nhánh D — Cảng biển & Logistics (phụ)

Giữ 2 cảng cũ để không mất nội dung. Chuyển ra khỏi cao tốc thành một nhánh ngắn.

```
infrastructure_development
 ├─ cai_mep_port [cũ, 2011]
 └─ lach_huyen_port [cũ, 2015]
     └─ logistics_strategy [mới]
```

| Focus | Cơ sở | Reward gợi ý |
|---|---|---|
| `logistics_strategy` | Chiến lược phát triển dịch vụ logistics (giảm chi phí logistics/GDP) | Idea nhỏ `trade_opinion_factor`. Nối `VIE_cai_mep_port` |

---

## 8. Capstone

| Focus | Yêu cầu | Reward |
|---|---|---|
| `infrastructure_breakthrough_nq13` | Root + 1 focus mỗi nhánh A/B/C, date > 1/2012 | Mở các dự án lớn sau 2012 (GĐ1 cao tốc, NQ 172, Long Thành) |
| `synchronized_infrastructure_2030` "Hạ tầng đồng bộ" | `expressway_5000km_2030` + `hsr_groundbreaking` + `long_thanh_airport` | Idea capstone: `production_speed_infrastructure_factor`, `country_productivity_growth_modifier`. Nối `VIE_developed_nation_2045` |

---

## 9. Số liệu & kỹ thuật

### 9.1 Số focus

| Nhánh | Cũ giữ lại | Mới | Tổng |
|---|---|---|---|
| Root + mốc NQ 13 + capstone | — | 3 | 3 |
| A. Đường bộ | 1 | 11 | 12 |
| B. Đường sắt | 5 | 7 (gồm 3 lựa chọn đối tác) | 12 |
| C. Hàng không | 1 | 10 | 11 |
| D. Cảng biển | 2 | 1 | 3 |
| **Tổng** | **9** | **32** | **41** |

Cây tăng từ 327 lên khoảng 359 focus.

### 9.2 State dùng cho xây dựng

Đã đối chiếu với tên file `history/states/` trong repo MD:

| State | Vùng | Dùng cho |
|---|---|---|
| **522** | Đồng bằng sông Hồng (Hà Nội, thủ đô) | Nội Bài, metro Hà Nội, Vành đai 4, Lạch Huyện |
| **519** | Nam Bộ (TP.HCM, Đông Nam Bộ, Nha Trang) | Long Thành, Tân Sơn Nhất, metro TP.HCM, Cái Mép, Vành đai 3 |
| **521** | Trung Bộ | Hầm Hải Vân, đường sắt Thống Nhất, sân bay lưỡng dụng |
| **518** | ĐBSCL | Cầu Cần Thơ, cao tốc Cần Thơ – Cà Mau |
| **523** | Đông Bắc (Lào Cai, Hạ Long) | Nội Bài – Lào Cai, Vân Đồn, đường sắt Lào Cai |

`VIE_focus_coding_standards.md` (mục 7.3) từng ghi ngược 519 và 522. Bảng đó đã được sửa.

### 9.3 Quy tắc

- Mọi xây dựng dùng `one_state_infrastructure` (3,5 bn) và `one_state_air_base` (2,5 bn). Không gọi `add_building_construction` trực tiếp (sửa H3).
- Focus chi từ 5 bn trở lên phải có `has_active_mission = bankruptcy_incoming_collapse` trong `ai_will_do`.
- Filter: `FOCUS_FILTER_INFRASTRUCTURE` + `FOCUS_FILTER_ECONOMY`. Thêm `FOCUS_FILTER_EXPENDITURE` cho dự án lớn.
- AI lịch sử (`VIE_ai_historical = yes`): chọn `hsr_2010_reject`, `expressway_public_investment` (sau 2020), `socialized_airports`. Đối tác đường sắt cao tốc: để AI chọn theo trục quan hệ.
- Cần kiểm tra MD có bật building `railway` / `supply_node` không. Nếu có, nhánh B có thể xây đường ray thật thay vì chỉ cộng infra.

---

## 10. Thứ tự triển khai

| Bước | Nội dung | Đổi gameplay? |
|---|---|---|
| 1 | Tạo root, chuyển 9 focus cũ vào 4 nhánh, sửa H3–H5, đổi shortcut | Ít (chỉ sửa lỗi) |
| 2 | Thêm `VIE_expressway_km`, nhánh A đầy đủ, event Cần Thơ và BOT | Có |
| 3 | Nhánh B (đường sắt), lựa chọn đối tác HSR | Có |
| 4 | Nhánh C (hàng không), event Vietnam Airlines | Có |
| 5 | Capstone, idea, loc VI, layout, chạy `standardize_focus_tree.py` + validator, test trong game | — |

### Cần xác minh trước khi viết loc

- Số km chính xác của từng giai đoạn cao tốc và tổng km thực tế cuối 2025.
- Số hiệu NQ 52/2017, NQ 44/2022, NQ 172/2024, NQ 187/2025, NQ 188/2025, NQ 94/2015, QĐ 648/2023, và năm chính xác của Chiến lược GTVT (2004).
- Mốc khai thác thương mại Long Thành và tiến độ khởi công đường sắt tốc độ cao.
- Danh sách 3 dự án BOT được chuyển sang đầu tư công năm 2020.

## 11. Đã tra nguồn (03/10/2026)

Các số hiệu và mốc ở mục 4–6 đã được đối chiếu với nguồn báo chí và văn bản chính thức, rồi cập nhật vào loc và điều kiện `available`. Các điểm đã sửa so với bản thiết kế:

- TP.HCM – Trung Lương dài khoảng 62 km (không phải 40 km), nên `VIE_expressway_km` cộng 62.
- Sập nhịp dẫn cầu Cần Thơ (26/9/2007) làm 55 người chết (không phải 54).
- NQ 44/2022/QH15 thông qua ngày 11/1/2022. NQ 56 và 57/2022/QH15 (vành đai) thông qua ngày 16/6/2022. NQ 52/2017/QH14 thông qua ngày 22/11/2017: `north_south_expressway` giờ mở từ 22/11/2017 thay vì 2011.
- Chiến lược GTVT là QĐ 206/2004/QĐ-TTg (10/12/2004).
- Long Thành đón chuyến bay đầu ngày 19/12/2025, khai thác thương mại năm 2026.
- QĐ 648/QĐ-TTg (7/6/2023): 30 cảng hàng không đến 2030 (không phải "hơn 30").
