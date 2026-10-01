# DANH SÁCH STATE CỦA VIỆT NAM TRONG MOD MILLENNIUM DAWN

> Nguồn: repo chính thức **`MillenniumDawn/Millennium-Dawn`**, nhánh `main`, thư mục `history/states/`
> (tải trực tiếp qua GitHub API ngày 2026-09-30). Tên hiển thị lấy từ
> `localisation/english/state_names_l_english.yml`, tên thành phố từ `victory_points_l_english.yml`.
> Đối chiếu với `SomnvK123/hoi4-md-vietnam-` @ `f05cfa1`.
>
> **Việt Nam có đúng 12 state: 7 state lục địa + 5 state đảo/biển tranh chấp.**
> (`capital = 522` — xem `history/countries/VIE - Vietnam.txt`)

---

## A. 7 STATE LỤC ĐỊA — VIE sở hữu & có core

| ID | Tên trong MD (hiển thị) | Tên tiếng Việt | Dân số | Category | Slots | Tài nguyên |
|---|---|---|---:|---|---:|---|
| **522** | Red River Delta | Đồng bằng sông Hồng | **18.513.105** | `state_11` (16–19tr) | 40 | dầu 7 |
| **519** | Southern Vietnam | Nam Bộ (ĐNB + duyên hải NTB) | **16.012.760** | `state_11` (16–19tr) | 40 | dầu 5, **cao su 46** |
| **518** | Mekong Delta | Đồng bằng sông Cửu Long | **14.954.590** | `state_10` (13–16tr) | 36 | dầu 6 |
| **521** | Central Vietnam | Trung Bộ (BTB + NTB) | **13.354.014** | `state_10` (13–16tr) | 36 | thép 9, tungsten 3 |
| **523** | Northern Vietnam | Đông Bắc Bộ | **6.079.352** | `state_06` (5,2–6,8tr) | 22 | thép 7, tungsten 5 |
| **520** | Vietnamese Highlands | Tây Nguyên | **5.512.695** | `state_06` (5,2–6,8tr) | 22 | **nhôm 21**, tungsten 3, **cao su 64** |
| **524** | Northwest Vietnam | Tây Bắc Bộ | **3.048.301** | `state_04` (2,5–3,8tr) | 14 | — |
| | | **TỔNG** | **77.474.817** | | | |

### Chi tiết từng state

**522 — Red River Delta / Đồng bằng sông Hồng** · `capital = 522`
- Tỉnh: `10129` Hà Nội (VP 10) · `4119` Hải Phòng (VP 5) · `1185` Nam Định (VP 1) · `4075`, `12048`, `226`
- Công trình 2000: infra 1 · internet 1 · **IC 2** · offices 1 · **air_base 8** · agriculture_district 2 · **arms_factory 1** · **naval_base 6 @4119** · fossil_powerplant 2 · composite_plant 1
- Thuỷ điện 2.040 (cao nhất cả nước) · `productivity_state_var = 815` (cao nhất)
- Terrain modifier: `terrain_hanoi` @10129, `terrain_haipong` @4119

**519 — Southern Vietnam / Nam Bộ**
- Tỉnh: `4401` TP. Hồ Chí Minh (VP 10) · `10162` Nha Trang (VP 5) · `12232` Vũng Tàu (VP 3) · `1396` Mỹ Tho · `10232` Phan Thiết · `1285` Phan Rang · `4405` Tuy Hòa · `10261`, `12204`
- Công trình 2000: infra 2 · internet 1 · **IC 3** · **air_base 6** · **naval_base 8 + naval_headquarters lv1 @4401** (cần DLC *No Compromise, No Surrender*) · fossil_powerplant 1
- `productivity_state_var = 638` · terrain: `terrain_ho_chi_minh` @4401, `terrain_nha_trang` @10162
- ⚠️ **519 gồm cả TP.HCM lẫn Nha Trang/Khánh Hòa** — đừng tưởng 519 chỉ là Đông Nam Bộ

**518 — Mekong Delta / Đồng bằng sông Cửu Long**
- Tỉnh: `12133` Cần Thơ (VP 5) · `4223` Long Xuyên (VP 5) · `4284` Rạch Giá (VP 1) · `4341` Cà Mau (VP 1) · `7303` Sóc Trăng (VP 1) · `1423` Vĩnh Long (VP 1) · `14178` Phú Quốc (VP 1) · `7331`, `12288`
- Công trình 2000: infra 1 · internet 0 · **naval_base 4 @4284 (Rạch Giá)**
- Thuỷ điện 0.546 · `productivity_state_var = 499` · terrain: `terrain_long_xuyen` @4223
- 🚩 **Province ven biển duy nhất có naval_base là `4284`.** `4223` Long Xuyên và `1423` Vĩnh Long **không giáp biển**. `14178` Phú Quốc là đảo (giáp biển).

**521 — Central Vietnam / Trung Bộ**
- Tỉnh: `4397` Vinh (VP 5) · `4379` Huế (VP 5) · `10309` Đà Nẵng (VP 5) · `4334` Quy Nhơn (VP 5) · `11936` Thanh Hóa (VP 1) · `4255` Quảng Ngãi (VP 1) · `7280` Đồng Hới (VP 1) · + 9 tỉnh không VP
- Công trình 2000: infra 1 · internet 1 · IC 1 · air_base 2 · **naval_base 4 @10309 (Đà Nẵng)** · fossil_powerplant 1
- `productivity_state_var = 603` · terrain: `terrain_vinh` @4397, `terrain_da_nang` @10309, `terrain_quy_nhon` @4334
- 🚩 **521 giáp Lào** (Thanh Hóa → Thừa Thiên-Huế) — không chỉ 520 mới giáp Lào

**523 — Northern Vietnam / Đông Bắc Bộ**
- Tỉnh: `1157` Hạ Long (VP 5) · `1073` Lào Cai (VP 5) · `9948` Lạng Sơn (VP 1) · `7093`, `7015`, `12065`, `7518`
- Công trình 2000: infra 1 · internet 0 · IC 1 · **naval_base 2 @1157 (Hạ Long)**
- `productivity_state_var = 478` · terrain: `terrain_lao_cai` @1073, `terrain_ha_long` @1157
- 🚩 **Có biển** (Hạ Long). Đây mới là state giáp Trung Quốc ở phía Đông Bắc.

**520 — Vietnamese Highlands / Tây Nguyên**
- Tỉnh: `1605` Buôn Ma Thuột (VP 3) · `4363` Pleiku (VP 1) · `7271` Đà Lạt (VP 1) · `12176` Bảo Lộc (VP 1) · + 8 tỉnh không VP
- Công trình 2000: infra 0 · internet 0 · renewable_energy_infra 1
- **Tài nguyên giàu nhất nước**: nhôm 21, cao su 64, tungsten 3 · `productivity_state_var = 410`
- 🚩 Hoàn toàn **không giáp biển**; giáp Lào và Campuchia

**524 — Northwest Vietnam / Tây Bắc Bộ**
- Tỉnh: `4529` Điện Biên Phủ (VP 1) · `12319` Sơn La (VP 1) · `10075` Yên Bái (VP 1) · `10103`, `12008`, `12075`, `214`
- Công trình 2000: infra 0 · internet 0 · IC 1 · `productivity_state_var = 395` (thấp nhất)
- 🚩 **Không giáp biển**, giáp Trung Quốc và Lào
- ⚠️ **Tên file của MD là `524-Northeast Vietnam.txt` nhưng key loc `STATE_524` = "Northwest Vietnam"** → tên người chơi thấy là **Tây Bắc**. MD đặt tên file sai.

---

## B. 5 STATE ĐẢO / BIỂN TRANH CHẤP

Tất cả đều `state_category = state_inhospitable` (**0 building slot**), `manpower = 1` (riêng 813 = 908), `buildings_max_level_factor = 1.000`.

| ID | Tên MD | Tiếng Việt | **Owner 2000** | Claim bởi | Province (đảo/đá) |
|---|---|---|---|---|---|
| **801** | Western Spratlys | Tây Trường Sa | **🇻🇳 VIE** | CHI, TAI, MAY, PHI | `11134` (đảo chính VN giữ, MD không đặt tên VP) · `11140` Storm Island (VP 2) · `11149` Collins Reef / đá Cô Lin (VP 1) · `11168` Southwest Cay / đảo Song Tử Tây (VP 1) |
| **526** | Northern Spratlys | Bắc Trường Sa | **🇨🇳 CHI** | **VIE**, TAI, MAY, PHI | `11146` Cuarteron / đá Châu Viên · `11156` Mischief / đá Vành Khăn · `11167` Subi / đá Xu Bi · `11169` Fiery Cross / đá Chữ Thập (VP 2) |
| **802** | Eastern Spratlys | Đông Trường Sa | **🇵🇭 PHI** | CHI, TAI, MAY, **VIE** | `11138` · `11150` Commodore Reef / đá Công Đo · `11165` Thitu Island / đảo Thị Tứ (VP 2) · `11171` Nanshan Island / đảo Nam Yết |
| **813** | Paracel Islands | **Hoàng Sa** | **🇨🇳 CHI** | **VIE**, TAI | `11131` Woody Island / đảo Phú Lâm (VP 2) · `14409` Robert Island / đảo Hữu Nhật (VP 1) |
| **816** | Southern Spratlys | Nam Trường Sa | **🇲🇾 MAY** | CHI, TAI, PHI, **VIE** | `11133` Swallow Reef / đá Hoa Lau (Layang-Layang) (VP 2) |

**Công trình có sẵn trên đảo (2000):**
- `801` (VIE): air_base 1 · naval_base 1 tại cả 4 province `11134/11140/11149/11168` · terrain `terrain_southwest_cay` @11168, `terrain_collins_reef` @11149
- `526` (CHI): naval_base 1 tại cả 4 province · terrain `terrain_subi_reef`, `terrain_mischief_reef`, `terrain_fiery_cross_reef`, `terrain_cuarteron_reef`
- `802` (PHI): air_base 1 · naval_base 1 ×4 · terrain `terrain_thitu_island`, `terrain_nanshan_island`, `terrain_commodore_reef`
- `813` (CHI): **naval_base 2 @11131** · air_base 1 · terrain `terrain_parcel_island` (MD viết sai chính tả "paracel")
- `816` (MAY): naval_base 1 @11133 · air_base 1 · terrain `terrain_swalow_reef`

> ✅ **Kết luận quan trọng:** Việt Nam **đã có claim sẵn từ đầu game** trên **526, 802, 813, 816** → mọi lệnh `add_state_claim` vào 4 state này là **no-op**.
> ✅ **MD main CÓ state Hoàng Sa riêng = `813`.** Không đúng như comment trong focus của bạn.

---

## C. Ánh xạ quân khu — mod của bạn dùng ĐÚNG

`common/scripted_effects/VIE_md_effects_p3.txt` chia state cho nội chiến:

| Phe nổi dậy | State | Quân khu | Khớp thực tế |
|---|---|---|---|
| party 22 (quân đội) | `524` `523` | QK1 (Tây Bắc) + QK2 (Việt Bắc) | ✅ |
| party 20 (dân tuý) | `521` `520` | QK4 (Bắc Trung Bộ) + QK5 (Tây Nguyên) | ✅ |
| party 13 (cải cách) | `519` `518` | QK7 (Đông Nam Bộ) + QK9 (ĐBSCL) | ✅ |
| Chính phủ giữ | `522` (thủ đô, QK3) + `801` (Trường Sa) | | ✅ |
| party 5 (công nhân) | `519` `524` | QK7 + QK1 | ⚠️ cặp địa lý rời rạc, không theo quân khu nào |

---

## D. 🚩 LỖI STATE/PROVINCE TRONG MOD CỦA BẠN

### D-1 · `VIE_spratly_fortification` — state 526 nhưng province của 801 (**lỗi nặng nhất**)
`common/national_focus/VIE_md_focus.txt:2339–2392`

```pdx
526 = {                                    # ← 526 = Bắc Trường Sa, OWNER = CHI
    add_building_construction = { type = coastal_bunker level = 2 instant_build = yes province = 11168 }  # 11168 thuộc 801
    add_building_construction = { type = coastal_bunker level = 1 instant_build = yes province = 11149 }  # 11149 thuộc 801
    one_state_air_base = yes
    one_state_anti_air = yes
}
526 = { one_state_radar_station = yes }
526 = { one_state_anti_air = yes }         # ← anti_air bị gọi LẦN 2 (trùng)
...
526 = { add_building_construction = { type = naval_base level = 1 instant_build = yes province = 11134 } } # 11134 thuộc 801
```
**Hậu quả:** cả 3 `add_building_construction` fail (province không thuộc state), và 4 lệnh `one_state_*` rơi vào state **Trung Quốc** đang sở hữu. Người chơi trả `cost = 16` (80 ngày) + **9,5 tỷ USD ngân khố** mà không nhận được gì.
`tools/TESTING.md:189` vẫn ghi kỳ vọng đúng: *"bunkers/air base/AA (Spratly fortification…)"* trên **801**.
**Sửa:** đổi hết `526` → **`801`** trong focus này, và xoá dòng `one_state_anti_air` trùng.

### D-2 · `VIE_dk1_platforms` — DK1 nằm ở 801, không phải 526
`common/national_focus/VIE_md_focus.txt:6871` → `526 = { one_state_radar_station = yes }`
DK1 là chuỗi nhà giàn của **Việt Nam**; `TESTING.md:189` ghi rõ *"801 radar (DK1)"*.
**Sửa:** `526` → **`801`**.

### D-3 · `VIE_storm_resilient_islands` — đổi 524 → 526 là sai hướng
`common/national_focus/VIE_md_focus.txt:7670–7687`
```pdx
# v3: 524 (Dong Bac bo, khong giap bien) -> 526 Northern Spratlys; ...
526 = { naval_base + bunker, province = { all_provinces = yes limit_to_naval_base = yes } }
```
Hai lỗi trong một comment:
1. **524 là TÂY Bắc Bộ**, không phải Đông Bắc. (Đông Bắc là **523**, và 523 **có** biển — Hạ Long.) Nhận xét "không giáp biển" cho 524 thì đúng.
2. Đích đến mới **526 thuộc Trung Quốc** → `limit_to_naval_base` sẽ khớp 4 naval_base của TQ, build fail.
**Sửa:** `526` → **`801`** (Tây Trường Sa, VIE sở hữu, có sẵn 4 naval_base → `limit_to_naval_base = yes` chạy đúng).

### D-4 · `VIE_paracel_ultimatum` — nhắm 526 thay vì 813 (Hoàng Sa)
`common/national_focus/VIE_md_focus.txt:1132–1141`
```pdx
# MD4 main khong co state Hoang Sa rieng; claim huong ve 526 (Northern Spratlys - VIE co san claim)
add_state_claim = 526
create_wargoal = { type = take_state_focus target = CHI generator = { 526 } }
```
Tiền đề **sai**: MD main **có** `history/states/813-Paracel.txt` (owner CHI, `add_claim_by = VIE`).
Hệ quả: (a) `add_state_claim = 526` là **no-op** vì VIE đã claim 526; (b) focus tên "Paracel ultimatum" nhưng wargoal lại nhắm **Bắc Trường Sa**; (c) **mâu thuẫn với chính event của bạn** — `events/VIE_md_p11.txt:80` (`vie_scs.16.b`) dùng đúng `813`.
`VIE_nationalist_regime_TDD.md:142` cũng ghi focus này *"claim 813"* — tức bản TDD và code hiện tại đang lệch nhau.
**Sửa:** `526` → **`813`** ở cả `add_state_claim` (hoặc bỏ hẳn vì đã claim sẵn) và `generator`.

### D-5 · Hai naval_base đặt ở province **không giáp biển**
| Chỗ | Code | Vấn đề | Nên dùng |
|---|---|---|---|
| `VIE_coast_guard_law` — `VIE_md_focus.txt:6812–6819` | `518 = { naval_base … province = 1423 }` | `1423` = **Vĩnh Long**, nội địa | `4284` Rạch Giá (MD đã đặt sẵn naval_base 4) hoặc `14178` Phú Quốc |
| `VIE_spratly_fortification` — `VIE_md_focus.txt:2385–2392` | `518 = { naval_base … province = 4223 }` | `4223` = **Long Xuyên** (An Giang), nội địa | `4284` Rạch Giá |

Đây đúng loại lỗi mà `TESTING.md:171` đã tự ghi nhận cho state 524: *"State 524 has no coastal province, so the old dockyard could never build."* — cùng cơ chế, chỉ khác state.

### D-6 · `VIE_provincial_defence_zones` bỏ sót biên giới Lào của 521
`common/national_focus/VIE_md_focus.txt:2208–2243`, comment ghi:
```
# (China in 523/524, Laos and Cambodia in 520)
```
Đúng nhưng **thiếu**: `521` cũng giáp Lào suốt dải Thanh Hóa → Thừa Thiên-Huế. Bunker `limit_to_border` chỉ dựng ở 523/524/520, nên toàn bộ biên giới Lào của Bắc Trung Bộ trống. (Có thể là chủ đích để tiết kiệm ngân khố −3 tỷ — nhưng nên ghi rõ.)

### D-7 · `add_state_claim = 813` trong event là no-op
`events/VIE_md_p11.txt:80` — VIE đã có claim 813 từ đầu game. Không gây lỗi, nhưng dòng lệnh thừa; `create_wargoal` ngay sau vẫn hoạt động bình thường.

### D-8 · Hai state VIE có claim nhưng mod **không dùng đến**
`802` (Đông Trường Sa, PHI giữ) và `816` (Nam Trường Sa, MAY giữ) — không xuất hiện ở bất kỳ file live nào. Kế hoạch dùng chúng (`VIE_nat_press_spratly_claim`, `generator = { 526 802 816 }`) nằm trong `v10_removed_nationalist_focuses.txt` đã archive.

### D-9 · `520` (Tây Nguyên) gần như bị bỏ phí
State giàu tài nguyên nhất nước (**nhôm 21, cao su 64**) chỉ được mod dùng đúng một lần, cho bunker biên giới (`VIE_md_focus.txt:2231`). Không có focus kinh tế/công nghiệp nào đặt vào 520.

---

## E. Bảng tra province → state → thành phố (81 province)

Dùng khi viết `add_building_construction = { … province = N }`.

| State | Province | Tên (VP loc của MD) |
|---|---|---|
| 518 | 1423 | Vinh Long *(nội địa)* |
| 518 | 4223 | Long Xuyen *(nội địa)* |
| 518 | **4284** | **Rach Gia** ⚓ *naval_base 4* |
| 518 | 4341 | Ca Mau |
| 518 | 7303 | Soc Trang |
| 518 | 7331 | — |
| 518 | 12133 | Can Tho *(nội địa)* |
| 518 | 12288 | — |
| 518 | 14178 | Phu Quoc 🏝 |
| 519 | 1396 | My Tho |
| 519 | 10261 | — |
| 519 | **4401** | **Ho Chi Minh City** ⚓ *naval_base 8 + naval HQ* |
| 519 | 12232 | Vung Tau |
| 519 | 10232 | Phan Thiet |
| 519 | 12204 | — |
| 519 | 1285 | Phan Rang |
| 519 | 10162 | Nha Trang |
| 519 | 4405 | Tuy Hoa |
| 520 | 7238 | — |
| 520 | 12176 | Bao Loc |
| 520 | 7271 | Da Lat |
| 520 | 1605 | Buon Ma Thuot |
| 520 | 12109 | — |
| 520 | 1400 | — |
| 520 | 7380 | — |
| 520 | 1328 | — |
| 520 | 4363 | Pleiku |
| 520 | 1248 | — |
| 520 | 12150 | — |
| 520 | 7347 | — |
| 521 | 1300 | — |
| 521 | 1302 | — |
| 521 | 4255 | Quang Ngai |
| 521 | 4334 | Qui Nhon |
| 521 | 4379 | Hue |
| 521 | 4397 | Vinh |
| 521 | 7229 | — |
| 521 | 7280 | Dong Hoi |
| 521 | 9988 | — |
| 521 | 10016 | — |
| 521 | 10137 | — |
| 521 | 10180 | — |
| 521 | **10309** | **Da Nang** ⚓ *naval_base 4* |
| 521 | 11909 | — |
| 521 | 11936 | Thanh Hoa |
| 521 | 12297 | — |
| 522 | 1185 | Nam Dinh |
| 522 | 4075 | — |
| 522 | **4119** | **Haiphong** ⚓ *naval_base 6* |
| 522 | **10129** | **Hanoi** 🏛 *capital* |
| 522 | 12048 | — |
| 522 | 226 | — |
| 523 | **1157** | **Ha Long** ⚓ *naval_base 2* |
| 523 | 7093 | — |
| 523 | 9948 | Lang Son |
| 523 | 7015 | — |
| 523 | 12065 | — |
| 523 | 7518 | — |
| 523 | 1073 | Lao Cai |
| 524 | 4529 | Dien Bien Phu |
| 524 | 10075 | Yen Bai |
| 524 | 10103 | — |
| 524 | 12008 | — |
| 524 | 12075 | — |
| 524 | 12319 | Son La |
| 524 | 214 | — |
| 526 🇨🇳 | 11146 | Cuarteron Reef ⚓ |
| 526 🇨🇳 | 11156 | Mischief Reef ⚓ |
| 526 🇨🇳 | 11167 | Subi Reef ⚓ |
| 526 🇨🇳 | 11169 | Fiery Cross Reef ⚓ |
| **801 🇻🇳** | 11134 | *(không tên VP)* ⚓ |
| **801 🇻🇳** | 11140 | Storm Island ⚓ |
| **801 🇻🇳** | 11149 | Collins Reef ⚓ |
| **801 🇻🇳** | 11168 | Southwest Cay ⚓ |
| 802 🇵🇭 | 11138 | — ⚓ |
| 802 🇵🇭 | 11150 | Commodore Reef ⚓ |
| 802 🇵🇭 | 11165 | Thitu Island ⚓ |
| 802 🇵🇭 | 11171 | Nanshan Island ⚓ |
| 813 🇨🇳 | 11131 | Woody Island ⚓ |
| 813 🇨🇳 | 14409 | Robert Island |
| 816 🇲🇾 | 11133 | Swallow Reef ⚓ |

⚓ = có naval_base sẵn năm 2000 → dùng được với `province = { all_provinces = yes limit_to_naval_base = yes }`

---

## F. Ghi chú khi code

1. **5 state đảo đều là `state_inhospitable` → `local_building_slots = 0`.** MD vẫn đặt air_base/naval_base được trong `history`, và `add_building_construction` có `instant_build = yes` thường vượt slot — nhưng **chưa được kiểm chứng trong game** cho state 0 slot. Nên test trước khi dựa vào.
2. **State ven biển của VIE:** `518` `519` `521` `522` `523` + `801`. **Không ven biển:** `520` `524`. → `dockyard` / `naval_base` chỉ hợp lệ ở nhóm đầu.
3. **State giáp Trung Quốc:** `523` `524` (+ `526` `813` nếu chiếm được). **Giáp Lào:** `520` `521` `524`. **Giáp Campuchia:** `518` `520`.
4. **Tên file MD ≠ tên hiển thị** ở state 524. Luôn tra `STATE_<id>` trong `state_names_l_english.yml`, đừng tin tên file.
5. Mod của bạn muốn hiện tên state bằng tiếng Việt → thêm key `STATE_518:0 "Đồng bằng sông Cửu Long"` … vào `localisation/english/replace/`. Hiện repo **chưa có** nhóm key `STATE_*` nào.
6. `map/definition.csv` và dữ liệu giáp biển nằm trong file nhị phân của MD, không đọc được từ repo — mục "nội địa / ven biển" ở trên suy ra từ VP city name + vị trí MD đặt naval_base sẵn. Nên xác nhận lại trong game bằng console: `if = { limit = { 518 = { province = 1423 } } }` hoặc mở state view.

---

*Dữ liệu thô của Millennium Dawn lưu tại `tools/audit/md_ref/` — 12 file state Việt Nam, `VIE - Vietnam.txt`, `state_names_l_english.yml`, `victory_points_l_english.yml`, cộng `history/countries/` của SOV/POL/KOR/CHI/VIE và `common/units/equipment/`. Nguồn: repo `MillenniumDawn/Millennium-Dawn` nhánh `main`, tải qua GitHub API ngày 2026-09-30.*
