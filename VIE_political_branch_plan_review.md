# Đánh giá và bản cải tiến: "Kế hoạch tái cấu trúc nhánh chính trị lịch sử"

> Đối chiếu từng khẳng định của kế hoạch với code thật trong `D:\HOI4Mods\md_vietnam` (26/09/2026).
> Nhãn: **[ĐÚNG]** · **[SAI]** · **[THIẾU]** · **[RỦI RO]**

---

## 1. Kết luận ngắn

**Hướng đi đúng, nhưng kế hoạch chưa làm được như đang viết.** Ba ý tưởng lõi đáng giữ:

1. Tạo **một ngã rẽ thật** ở cuối nhánh chính trị.
2. Cho mỗi hướng một **cái giá**.
3. **Mở dần decision theo focus** thay vì mở hết từ đầu.

Nhưng có **5 lỗi nặng**:

1. Ngã rẽ 2026 **trùng với event đã có** `vie_pol.9`.
2. Có **focus cha nằm dưới focus con**.
3. Kế hoạch **âm thầm đổi prerequisite** của focus cũ.
4. Capstone `era_of_rising` **mâu thuẫn** với nhánh "mở rộng giám sát".
5. **Đếm sai hiện trạng**, nên bỏ sót 7 focus.

Chi tiết và bản sửa ở dưới.

---

## 2. Đối chiếu hiện trạng

| Kế hoạch nói | Code thật | |
|---|---|---|
| Nhánh có **19 focus** | **26 focus** chính trị lịch sử. Kế hoạch bỏ sót `public_admin_reform`, `e_government`, `cybersecurity_law`, `resolution_57_68`, `institutional_bottlenecks`. Cả 5 đều **không có trong đồ thị mới** | **[SAI]** |
| Không có mutex nào trong nhánh | Đúng với 2 cột này | **[ĐÚNG]** |
| **18 focus thuần lợi**, chỉ `party_discipline` có malus | **16 focus** trừ opinion `communist_cadres` (cái giá Geddes). `streamline_apparatus` có `VIE_reorg_disruption`. `institutional_bottlenecks` trừ ổn định. **Mọi focus** đều đẩy trục và BoP | **[SAI]** |
| Hai cột không khác nhau về gameplay | Cột trái đẩy BoP **bảo thủ** và giảm tham nhũng. Cột phải đẩy BoP **cải cách** và gọi luật bộ máy của MD (`decrease_centralization`) | **[SAI một phần]** |
| **9 event** `vie_pol.1–9` chạy tự động | Namespace `vie_pol` có **22 event** (1–22) | **[SAI]** |
| Event Đại hội không gắn vào focus là **một vấn đề** | Đây là **nguyên tắc có chủ ý** của plan v6 (A2): Đại hội chạy theo ngày, lịch sử chạy bằng event. Mục "Hạn chế" của chính kế hoạch cũng giữ nguyên scheduler | **[SAI — không phải lỗi]** |
| 6 decision xây dựng nhà nước không có điều kiện | Đúng: `visible = VIE_ax_initialized`, `available = always` (trừ một cái) | **[ĐÚNG]** |
| Reward ở đỉnh mỏng | `party_centennial_2030` chỉ cho PP và BoP nhỏ | **[ĐÚNG]** |

---

## 3. Năm lỗi nặng

### 3.1 Ngã rẽ 2026 trùng với event đã có

**`vie_pol.9` "Tổng Bí thư kiêm Chủ tịch nước (4/2026)"** đã có sẵn. Nó chỉ có một lựa chọn và đặt cờ `VIE_dual_role_2026`.

Kế hoạch thêm focus `VIE_concentration_of_power` ("TBT kiêm CTN, hợp nhất quyền lực"), và focus này **làm lại đúng việc đó**. Nếu người chơi chọn nhánh đối lập `VIE_institutional_opening`, event `vie_pol.9` vẫn bắn và vẫn hợp nhất hai chức vụ. Kết quả: người chơi vừa "mở rộng giám sát" vừa có TBT kiêm Chủ tịch nước.

Theo nguyên tắc plan v6, mỗi ngã rẽ phải gắn vào **một điểm quyết định có thật**. Điểm có thật ở đây chính là `vie_pol.9`.

**Sửa:**
- Thêm lựa chọn giả định **`vie_pol.9.b` "Giữ mô hình lãnh đạo tập thể"**.
- Hai focus ngã rẽ đọc cờ do event đặt.

### 3.2 Focus cha nằm dưới focus con

Đồ thị có `TT (VIE_two_tier_local_gov, y=8) → CWAY/DWAY (y=7)`. Focus cha ở hàng 8, con ở hàng 7, nên HOI4 vẽ đường nối ngược lên.

Ngoài ra, `two_tier_local_gov` bị khóa tới năm **2025**, nên ngã rẽ 2026 phải nằm **dưới** nó, không phải trên.

Còn một lỗi tương tự: `VIE_political_trust_campaign` "y=9, con của `VIE_era_of_rising`" trong khi `era_of_rising` cũng ở y=9.

### 3.3 Âm thầm đổi prerequisite của focus cũ

Mục 4 viết "chỉ đổi tọa độ", nhưng đồ thị mới đổi cha của nhiều focus:

| Focus | Hiện tại | Kế hoạch | Hệ quả |
|---|---|---|---|
| `decentralization` | `public_admin_reform` (2001) | `constitution_2013` (khóa đến 2013) | Toàn bộ cột cải cách bộ máy **bị đẩy lùi tới 2013**. Sai lịch sử: phân cấp bắt đầu từ Chương trình tổng thể cải cách hành chính 2001–2010 |
| `rule_of_law_state` | gốc riêng | con của `national_assembly_role` | Đổi luồng mở khóa |
| `asset_recovery` | cần `state_audit` **và** `party_discipline` | chỉ `state_audit` | Nới điều kiện |
| `resolution_57_68`, `institutional_bottlenecks`, `cybersecurity_law`, `e_government`, `public_admin_reform` | có trong cây | **không có trong đồ thị** | Hoặc mồ côi, hoặc bị xóa ngầm |

Một số **cost** cũng bị đổi mà không nói, ví dụ `state_audit` 5 → 7.

### 3.4 Capstone mâu thuẫn với nhánh "mở rộng giám sát"

`VIE_era_of_rising` hiện cho **`checks −2`**. Tôi thêm hiệu ứng này dựa trên ISEAS 2026/29 để phản ánh việc hợp nhất quyền lực. Trong kế hoạch mới, **cả hai nhánh** đều dẫn tới `era_of_rising`, nên người chơi chọn "mở rộng giám sát" vẫn bị trừ ràng buộc quyền lực.

Mục "Hạn chế" ghi "không đổi reward của 19 focus cũ", nên lỗi này sẽ tồn tại.

**Sửa:** chuyển `checks −2` từ `era_of_rising` sang `VIE_concentration_of_power`.

### 3.5 Phần thưởng sai cơ chế

| Kế hoạch viết | Vấn đề | Sửa |
|---|---|---|
| "+0.05 stability/month" | Không có modifier như vậy | `stability_factor` hoặc `stability_weekly` |
| "tech bonus research_speed +3%" | Tech bonus theo **nhóm công nghệ**, không phải theo tốc độ nghiên cứu | `research_speed_factor` trong idea, hoặc `add_tech_bonus` với `CAT_computing_tech` |
| Idea tập trung quyền lực: "+10% PP, −5% consumer goods" | `consumer_goods_factor` âm là **có lợi**, nên idea này **không có malus nào** | Thêm malus thật (xem mục 4) |
| Mở rộng giám sát: "merit −1 (mất tuyển cán bộ nhanh)" | Ngược với khung lý thuyết: ràng buộc quyền lực làm **chậm chính sách**, không làm giảm chất lượng bộ máy (O'Donnell; ISEAS 2026/29) | Malus bằng `political_power_gain` âm |
| "checks −1" trong option event | Cần viết thành `add_to_variable = { VIE_ax_checks = -1 }` rồi gọi `VIE_ax_normalize` | — |
| Decision `VIE_anticorruption_campaign`: `decrease_corruption` ×2, mỗi **365 ngày**, giá 100 PP | Hệ tham nhũng của MD chỉ có 10 nấc. Làm 5 lần là từ mức 08 xuống 01 | ×1, chờ 730 ngày, chỉ dùng khi còn ≥ `corruption_level_04` |

### 3.6 Các lỗi nhỏ khác

- **Đặt sai file.** Event nên nằm ở `events/VIE_md_pol.txt` (nơi có namespace `vie_pol`), không phải `VIE_md_p5.txt`. Loc nên nằm ở `localisation/english/replace/…_l_english.yml` (tiếng Việt, BOM, header `l_english:`), không phải `localisation/VIE_md_l_english.yml`.
- **ID event nhảy số.** Namespace đang kết thúc ở `vie_pol.22`, nên dùng **23–26** thay vì 25–28.
- **Nguyên tắc 1 lệch mốc.** Nó nói ngã rẽ "tại mốc 2016", nhưng thiết kế đặt ở 2026. Ngã rẽ 2016 (Đại hội XII → nhánh Kiến tạo) **đã có** qua `VIE_developmental_unlocked`.
- **Không nhắc tới hệ trục.** Focus mới phải có hiệu ứng trục và BoP (`check_static.py` cảnh báo focus chính trị thiếu BoP), và phải được thêm vào `_gen/axis_map.py`.
- **Chưa có AI.** Đường lịch sử phải chọn tập trung quyền lực. Nhánh đối lập cần `factor = 0` khi `VIE_ai_historical`.
- **Tọa độ sai.** `party_centennial_2030` hiện nằm ở x=94, trong khi `era_of_rising` ở x=28 — đường nối dài cắt ngang cây.

---

## 4. Bản cải tiến

### 4.1 Nguyên tắc

1. **Không đổi prerequisite, cost, ID của 26 focus cũ.** Chỉ có 2 thay đổi reward, đều có lý do:
   - Chuyển `checks −2` của `era_of_rising` sang nhánh tập trung.
   - Nâng cấp `party_centennial_2030` bằng `swap_ideas`.
2. **Ngã rẽ gắn vào event có thật** `vie_pol.9` (tháng 4/2026). Focus thể hiện hệ quả của lựa chọn đó.
3. **Mỗi focus mới có trục + BoP + đúng một cái giá.**
4. **Một nhánh, một spirit, nâng cấp dần** (plan v6 B2.7). Không thêm focus độn chỉ để đủ số.

### 4.2 Ngã rẽ 2026

**Sửa `vie_pol.9`, thêm lựa chọn b:**

| Lựa chọn | Nội dung | Cờ | AI |
|---|---|---|---|
| **a — Hợp nhất (lịch sử)** | Như hiện tại | `VIE_dual_role_2026` | base 100, luôn chọn khi lịch sử |
| **b — Giữ lãnh đạo tập thể (giả định)** | Chủ tịch nước tách riêng, Quốc hội giữ quyền giám sát | `VIE_collective_leadership_2026` | `factor = 0` khi `VIE_ai_historical` |

**Hai focus ngã rẽ.** Cả hai đều **mutex với nhau**, và đều có prerequisite `OR { two_tier_local_gov, clean_cadres }` (giống điều kiện hiện tại của `era_of_rising`).

| | `VIE_concentration_of_power` — Lãnh đạo hạt nhân | `VIE_institutional_opening` — Mở rộng giám sát |
|---|---|---|
| Điều kiện | `VIE_dual_role_2026` | `VIE_collective_leadership_2026` |
| Cost | 10 | 10 |
| Trục | `checks −2` (chuyển từ `era_of_rising`), `size −1` | `checks +3`, `civil +1` |
| BoP | `VIE_bop_conservative_medium` | `VIE_bop_reform_medium` |
| Idea | `VIE_unified_leadership_idea`: +10% PP, +3% ổn định; **malus** −2% tốc độ nghiên cứu ("kém tiếp thu phản hồi", ISEAS 2026/29) | `VIE_institutional_oversight_idea`: +4% ổn định, −10% chi phí decision; **malus** −8% PP ("chính sách chậm hơn") |
| Event | `vie_pol.23` ngay; `vie_pol.25` sau 365 ± 90 ngày | `vie_pol.24` ngay; `vie_pol.26` sau 365 ± 90 ngày |

### 4.3 Ba focus mới, bỏ hai trong số sáu của kế hoạch

| Focus | Cha | Hàng | Nội dung |
|---|---|---|---|
| `VIE_cadre_accountability` — Trách nhiệm cán bộ | `party_discipline` | 6 | `decrease_corruption` ×1 (vì `party_discipline` đã ×2), `merit +1`, `checks +1`, ổn định −0.02, cán bộ −3 |
| `VIE_peoples_oversight` — Giám sát nhân dân | `grassroots_democracy` (hợp với Quy chế dân chủ cơ sở hơn `decentralization`) | 4 | `checks +2`, `decent +1`, PP −25 |
| `VIE_digital_anticorruption` — Chống tham nhũng số | `clean_cadres`, và `available` cần `VIE_e_government` (nối chéo nhánh bằng `available`, theo plan v6 B2.2) | 8 | `decrease_corruption`, `merit +1`, `civil −1` (giám sát dữ liệu), từ 2022 |

**Bỏ hai focus:**
- `VIE_political_trust_campaign`: là focus độn, chỉ có PP và ổn định, và sai vị trí.
- Không thêm focus capstone riêng. Thay vào đó **nâng `party_centennial_2030`** bằng `swap_ideas = { remove_idea = VIE_era_of_rising_idea add_idea = VIE_era_of_rising_idea_2 }`. Như vậy vẫn giải quyết được vấn đề "reward mỏng ở đỉnh", mà đúng quy tắc một spirit mỗi nhánh.

**Tổng:** 26 + 5 = **31 focus** (2 ngã rẽ + 3 focus mới).

### 4.4 Event

| ID | Tên | Kích hoạt | Lựa chọn |
|---|---|---|---|
| `vie_pol.9` **(sửa)** | TBT kiêm Chủ tịch nước | Như hiện tại | Thêm lựa chọn b (mục 4.2) |
| `vie_pol.23` | Lãnh đạo thống nhất | Focus tập trung | **A** tiến nhanh: ổn định +0.02, PP −50, `checks −1`. **B** thận trọng: PP +25 |
| `vie_pol.24` | Quốc hội mở rộng giám sát | Focus mở rộng | **A** chất vấn trực tiếp: `checks +2`, ổn định −0.03. **B** qua báo cáo: `checks +1` |
| `vie_pol.25` | Khủng hoảng nhân sự | 365 ± 90 ngày sau focus tập trung; `trigger` kiểm tra còn idea | **A** kỷ luật công khai: `decrease_corruption`, ổn định −0.02. **B** xử lý nội bộ: PP +25, cán bộ −3, **tham nhũng tăng 1** |
| `vie_pol.26` | Dư luận phản đối trên mạng xã hội | 365 ± 90 ngày sau focus mở rộng; `trigger` kiểm tra còn idea | **A** lắng nghe: ổn định +0.02, PP −25. **B** kiểm soát: ổn định −0.01, `civil −1`, `checks −1` |

Mọi thay đổi trục trong option đều theo mẫu `add_to_variable` + `VIE_ax_normalize = yes`.

### 4.5 Decision

**Gắn điều kiện cho 6 decision cũ.** Đổi `visible`; nếu muốn người chơi ở chế độ khác vẫn dùng được thì dùng `OR` với slot đảng.

| Decision | Kế hoạch đề xuất | Sửa thành | Lý do |
|---|---|---|---|
| `VIE_civil_service_examination` | `rule_of_law_state` | **`public_admin_reform`** | Thi tuyển công chức là cải cách hành chính, không phải pháp quyền |
| `VIE_provincial_pilot_program` | `decentralization` | giữ | — |
| `VIE_streamline_administrative_org` | `streamline_apparatus` | giữ | — |
| `VIE_relax_media_scrutiny` | `constitution_2013` | giữ | — |
| `VIE_strengthen_internal_discipline` | `anti_corruption_law` | **`cybersecurity_law`** | Siết kiểm soát nội dung gắn với an ninh mạng, không phải luật chống tham nhũng |
| `VIE_negotiate_economic_pact` | `rule_of_law_state` | **`wto_negotiations`** | Hiệp định kinh tế thuộc nhánh hội nhập |

**Ba decision mới**, đã cân bằng lại:

| Decision | Điều kiện | Chi phí / chờ | Tác dụng |
|---|---|---|---|
| `VIE_anticorruption_campaign` | `party_discipline`, và **không** ở `corruption_level_01…03` | 100 PP / **730 ngày** | `decrease_corruption` **×1**, ổn định −0.02, cán bộ −5 |
| `VIE_public_consultation` | `grassroots_democracy` | 50 / 180 | `checks +1`, `decent +1`, ổn định +0.01 |
| `VIE_cadre_rotation` | `clean_cadres` | 75 / 540 | `merit +1`, `decrease_corruption`, `VIE_reorg_disruption` 180 ngày |

### 4.6 Bố cục

- Giữ tọa độ của 26 focus cũ.
- Ngã rẽ đặt ở **hàng 9**, dưới `two_tier_local_gov` (hàng 8). Kéo `era_of_rising` xuống **hàng 10**, `party_centennial_2030` xuống **hàng 11** và **dời về dưới `era_of_rising`**.
- Khối quân sự nằm ở x 94–190, còn khối chính trị ở x 20–34, nên dùng hàng 10–11 không va chạm.
- Kiểm tra bằng `_gen/fix_spacing.py` và `_gen/overview.py`: 0 cặp dưới 2 ô, 0 focus con nằm trên cha.

---

## 5. Thứ tự thực hiện

| Bước | Việc | File |
|---|---|---|
| 1 | Sửa `vie_pol.9` (lựa chọn b), thêm event 23–26 | `events/VIE_md_pol.txt` |
| 2 | Thêm 2 idea ngã rẽ, và `VIE_era_of_rising_idea_2` | `common/ideas/VIE_md_ideas_p3R.txt` (file mới, theo quy ước `p3*`) |
| 3 | Thêm 5 focus mới; chuyển `checks −2` khỏi `era_of_rising`; thêm `swap_ideas` cho `party_centennial_2030`; dời 2 capstone | `common/national_focus/VIE_md_focus.txt` |
| 4 | Thêm ánh xạ trục cho 5 focus mới | `_gen/axis_map.py` |
| 5 | Sửa 6 decision cũ, thêm 3 decision mới | `common/decisions/VIE_md_decisions.txt` |
| 6 | Loc tiếng Việt | `localisation/english/replace/VIE_md_vi_pol2_l_english.yml` |
| 7 | Chạy `check_static.py` (0 lỗi); không thêm cảnh báo khoảng cách hay cha–con | — |

## 6. Kiểm chứng trong game

- **Đường lịch sử:** AI chọn `vie_pol.9.a` rồi làm `VIE_concentration_of_power`. `checks` cuối ván không đổi so với trước khi sửa, vì `−2` chỉ đổi chỗ.
- **Người chơi chọn `vie_pol.9.b`:** `VIE_concentration_of_power` bị khóa, `VIE_institutional_opening` mở. Sau khoảng 1 năm, `vie_pol.26` bắn.
- **Decision:** chiến dịch chống tham nhũng không dùng được khi đã ở `corruption_level_03`.
- **`error.log`:** không có dòng `VIE` hay `vie_`.
