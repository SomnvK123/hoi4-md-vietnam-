# Đánh giá & Rà soát Nhánh Chính trị Lịch sử — Millennium Dawn

> **Tài liệu tổng hợp đánh giá & kế hoạch code (08/10/2026)**  
> Hợp nhất các bản đánh giá kế hoạch tái cấu trúc và rà soát đối chiếu khoảng trống sự kiện.

## Mục lục
1. [Phần 1: Đánh giá và Bản cải tiến Kế hoạch Tái cấu trúc Nhánh Chính trị Lịch sử](#phần-1-đánh-giá-và-bản-cải-tiến-kế-hoạch-tái-cấu-trúc-nhánh-chính-trị-lịch-sử)
2. [Phần 2: Kế hoạch Code — Đối chiếu Nền tảng Lịch sử với Code Hiện tại](#phần-2-kế-hoạch-code--đối-chiếu-nền-tảng-lịch-sử-với-code-hiện-tại)

---

## Phần 1: Đánh giá và Bản cải tiến Kế hoạch Tái cấu trúc Nhánh Chính trị Lịch sử

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

---

## Phần 2: Kế hoạch Code — Đối chiếu Nền tảng Lịch sử với Code Hiện tại

# Kế hoạch code: đối chiếu "Báo cáo nghiên cứu — Nền tảng lịch sử cho Political Focus Tree VIE" với code hiện tại

> **Đã thay thế** bởi `VIE_congress_spine_redesign.md`. Mục 3.2 của tài liệu này sai một phần: 4 trên 7 event được đề xuất đã có sẵn dưới ID khác (đất đai `vie_pol.20`, Formosa `vie_eco.6`, dự luật đặc khu `vie_alt.6`, Luật An ninh mạng `vie_pol.10`). Bộ luật Lao động 2019 đã được code thành `vie_pol.27`. Luật Thực hiện dân chủ ở cơ sở 2022 được xử lý bằng mốc ngày của `peoples_oversight` trong thiết kế mới. Phản ứng về bauxite Tây Nguyên 2009 chưa làm (`vie_pol.18` là bất ổn 2004, khác chủ đề).

> Input: báo cáo nghiên cứu 26/9/2026 (Tầng 0–4, phân tích SIA, đề xuất H1/H2...). Đây **không phải** kế hoạch đầu tiên cho nhánh chính trị — nó đến **sau** `VIE_regime_taxonomy_step1_2.md` → `VIE_three_families_step3.md` → `VIE_technocracy_capacity_step4.md` → `VIE_statebuilding_framework_step5.md` → `VIE_doimoi_backbone_step6.md` → `VIE_branch_mapping_step7.md` → `VIE_transition_graph_step8.md` → `VIE_implementation_plan_step9.md` → `VIE_political_branch_plan_review.md` → `VIE_nationalism_branch_research_report.md` → `VIE_report_focus_event_decision.md` (audit hiện trạng, 26/9/2026, **502 focus / 191 event / 16 decision**, đã có tree chính trị 210 focus thân lịch sử + 159 focus dải chế độ giả định).
>
> Việc của tài liệu này: **không thiết kế lại từ đầu**. Đối chiếu từng đề xuất của báo cáo mới với code thật, đánh dấu cái gì **đã có** (đừng code lại), cái gì **thiếu thật** (code thêm), và gộp phần thiếu vào đúng chỗ trong backlog ưu tiên đã có ở `VIE_report_focus_event_decision.md` §7.
>
> Nhãn: **[ĐÃ CÓ]** · **[THIẾU — LÀM THÊM]** · **[CỐ Ý KHÔNG LÀM]** · **[CẦN XÁC MINH TRONG GAME]**

---

## 1. Kết luận ngắn

Khoảng **80–90% nội dung** báo cáo mới (Tầng 0 di sản, Tầng 1 xương sống Đại hội, phần lớn Tầng 2, khung 7 trục thay "Coup Risk", H1/H2 alt-history) **đã được code**, thường còn chi tiết hơn báo cáo đề xuất. Đây là dấu hiệu tốt — hai quá trình nghiên cứu độc lập hội tụ về cùng kiến trúc.

Phần thực sự thiếu là hẹp và cụ thể:

1. **7 event lịch sử thuộc "áp lực từ dưới lên"** (mục 6.6 của báo cáo) chưa tồn tại dưới dạng event — đây là input duy nhất đáng code mới từ báo cáo này.
2. **1 focus ngoại giao thiếu 1 target** (EU vào thang CSP).
3. **1 việc kiểm tra anachronism** (đối chiếu ngày tháng, không phải code).
4. Phần còn lại của báo cáo (H1, H2a/H2b, tầng 3 G1/G2/G3, thang đối tác, "Bốn không") đã có, có khi kỹn hơn.

**Ưu tiên thật sự cao hơn cả 4 việc trên** vẫn là backlog đã có sẵn ở `VIE_report_focus_event_decision.md` §7 (chưa chạy thử trong game, 127 cặp focus chen sát, 4 focus bị xóa cần xác nhận, dọn `.bak`). Mục 5 dưới đây xếp việc mới vào đúng vị trí trong backlog đó, không tạo backlog song song.

---

## 2. Đối chiếu Tầng 0–4 của báo cáo với code

| Đề xuất của báo cáo | Trạng thái | Bằng chứng |
|---|---|---|
| Tầng 0 di sản (Đổi Mới, Hiến pháp 1992, "không liên minh") | **[ĐÃ CÓ]** | STEP6: `VIE_doi_moi_continues` là gốc khởi tạo 7 trục bằng giá trị 2000, không phải focus chơi lại quá khứ — đúng nguyên tắc mục 9.6 của báo cáo mới |
| Tầng 1 xương sống chu kỳ Đại hội (IX→XIV) | **[ĐÃ CÓ]**, nhưng **ẩn trong hiệu ứng, không phải node riêng** | STEP6 mục 3: 5 giai đoạn (2000–06, 07–10, 11–15, 16–20, 21–26) đã đối chiếu hiệu ứng trục với đúng 82/14/13/19/26 focus mỗi giai đoạn. Đại hội XIV (2026) là flag `VIE_fourteenth_congress_held` gắn trong `VIE_era_of_rising`, không phải focus riêng |
| Nghị quyết là đơn vị chính sách, có độ trễ | **[ĐÃ CÓ]** | `resolution_57_68`, `institutional_bottlenecks`, `public_admin_reform`, `e_government`, `cybersecurity_law` đều tồn tại là focus riêng (đã bị một bản kế hoạch cũ bỏ sót, `political_branch_plan_review.md` §2 đã bắt lỗi đó) |
| Coup Risk kiểu Thái Lan → thay bằng thước đo phù hợp VN | **[ĐÃ CÓ]**, đúng như báo cáo đề xuất ở mục 4.2 | STEP5: không thêm thanh mới, dùng `VIE_state_modifier` (7→9 trục) + 3 power balance sẵn có của MD. Không có "coup risk" giả tạo |
| Đảng cầm quyền không đổi → gắn nhánh với "đường lối hiện hành" thay vì "ruling party" | **[ĐÃ CÓ]**, đúng cơ chế báo cáo đề xuất ở mục 5.2 | STEP7: chữ ký trục theo dải chế độ, không theo đảng; `VIE_political_branch_plan_review.md` §3.1 sửa đúng lỗi "gắn nhánh với cờ tĩnh thay vì trạng thái thực" mà PR #4362 của Thái Lan mắc phải |
| Thang đối tác ngoại giao (CSP/SR) | **[ĐÃ CÓ]**, thiếu 1 target | `VIE_csp_network` cộng `VIE_ax_integ`/`VIE_ax_west`, tạo opinion modifier `VIE_strategic_partnership` với US/JAP/KOR/RAJ (Ấn Độ). **Thiếu EU** (đối tác CLTD thứ 15, 29/1/2026) — xem mục 3.1 |
| "Bốn không" là ràng buộc hệ thống lên ngoại giao/quân sự | **[ĐÃ CÓ]** | `VIE_four_nos_doctrine` tồn tại; nhánh hạt nhân trong quốc phòng đòi rõ "không còn Bốn Không" làm điều kiện (theo `VIE_report_focus_event_decision.md` §2.3) — đúng cách báo cáo mới mô tả đây là trần của mọi nhánh (mục 8.2) |
| Tầng 3 G1/G2/G3 (biến thể đường lối, không phải phe) | **[ĐÃ CÓ]** | Gia đình A/B/C của `VIE_three_families_step3.md`, chữ ký trục xác nhận ở STEP7 (developmental_state = "kiến tạo rồi dân chủ hóa", đúng Slater & Wong mà báo cáo mới cũng trích) |
| Tầng 4 H1 đa nguyên có kiểm soát | **[ĐÃ CÓ]** | 4 gói `dm_*` (22 focus, dân chủ hóa qua round-table) trong dải chế độ giả định, đúng điều kiện "chỉ mở khi hội tụ khủng hoảng" mà báo cáo mới yêu cầu ở mục 6.9 |
| Tầng 4 H2a chủ quyền trong chế độ | **[ĐÃ CÓ]**, và **đã tốt hơn báo cáo mới đề xuất** | `VIE_nationalism_branch_research_report.md` đã thay thế hoàn toàn nhánh `VIE_np_*`/`VIE_lh_*` cũ bằng 4 trụ cột đúng tinh thần "chủ nghĩa dân tộc phòng thủ, khẳng định chủ quyền" — báo cáo mới mục 6.9 H2a mô tả lại đúng thứ đã redesign. **Không làm lại.** |
| Tầng 4 H2b dân tộc chủ nghĩa ngoài chế độ | **[CỐ Ý KHÔNG LÀM]**, đúng khuyến nghị "rất thấp khả thi" của báo cáo mới | Nationalism report đã loại bỏ hướng cực hữu/thanh trừng sắc tộc, giữ đúng cảnh báo mục 9.13 của báo cáo mới |
| Nhánh phục hồi lãnh thổ kiểu Greater Thailand | **[CỐ Ý KHÔNG LÀM]** | Không có trong code, đúng khuyến nghị mục 4.3/9.8 |
| Phục hồi VNCH/quân chủ | **[CỐ Ý KHÔNG LÀM]** | Không có trong code, đúng mục 9.14 |
| Capstone neo 2030/2045 | **[ĐÃ CÓ]** | `VIE_ninh_thuan_nuclear`... không liên quan; capstone thật là `party_centennial_2030` (2030) — tồn tại, và theo `political_branch_plan_review.md` §4.3 đã có kế hoạch nâng cấp bằng `swap_ideas` thay vì thêm focus độn |

**Kết luận mục 2:** không cần hành động thiết kế mới cho Tầng 0, 1, 3, 4. Phần đáng làm nằm ở Tầng 2E (áp lực xã hội) — mục 3 dưới đây.

---

## 3. Phần thiếu thật — cụ thể để code

### 3.1 EU vào thang đối tác chiến lược toàn diện (nhỏ)

**Báo cáo nói gì [S]:** EU trở thành đối tác CLTD thứ 15 ngày 29/1/2026 (mục 8.3, dòng cuối bảng 7.2).

**Code hiện tại:** `VIE_csp_network` (`common/national_focus/VIE_md_focus.txt`, khoảng dòng chứa `id = VIE_csp_network`) cộng opinion modifier `VIE_strategic_partnership` cho USA/JAP/KOR/RAJ, `available = { date > 2023.8.31 has_completed_focus = VIE_us_comprehensive_partnership }`. Không có EU (mã quốc gia MD cho EU — kiểm tra xem MD có tag `EUR`/siêu quốc gia hay chỉ có các nước thành viên riêng lẻ trước khi code, vì HOI4 gốc không có "EU" như một country tag chơi được).

**Việc cần làm:**
- Kiểm tra trong `common/countries` hoặc tag list của MD xem có tồn tại một thực thể ngoại giao đại diện EU (nhiều mod dùng opinion với từng nước lớn EU thay vì một tag EU). Nếu không có tag EU, **bỏ qua việc này** — không bịa tag.
- Nếu có, thêm 1 dòng `add_opinion_modifier`/`reverse_add_opinion_modifier` vào đúng focus `VIE_csp_network`, hoặc thêm focus con nhỏ `VIE_eu_csp_2026` (cost 5, `available = { date > 2026.1.28 }`, prerequisite `VIE_csp_network`) nếu muốn giữ mốc ngày riêng.
- Độ ưu tiên: **thấp**. Đây là chi tiết trang trí, không phải cấu trúc.

### 3.2 Bảy event "áp lực từ dưới lên" (mục 6.6 báo cáo) — đây là phần đáng code nhất

**Vấn đề đã xác nhận bằng grep:** namespace `vie_pol` hiện có 13 event (1–9, 23–26), namespace `vie_soc` có 19 event xã hội, nhưng **không event nào** khớp các mốc: Tiên Lãng/Văn Giang (đất đai 2012), Formosa hậu quả chính trị (2016, khác với focus kinh tế `VIE_formosa_steel_complex` đã có), biểu tình dự luật đặc khu + Luật An ninh mạng (6/2018), Bộ luật Lao động 2019 + phê chuẩn ILO 98/105 (điều kiện CPTPP/EVFTA), Luật Thực hiện dân chủ ở cơ sở (2022).

**Vì sao đáng code:** báo cáo mới đúng khi nói đây là "tương đương chức năng của Coup Risk" — nguồn rủi ro ổn định thật của Việt Nam. Code hiện tại đã có cơ chế nhận (7–9 trục, đặc biệt `civil`, `checks`, BoP cải cách/bảo thủ) nhưng **thiếu input lịch sử** đẩy vào cơ chế đó. Đây không phải lỗ hổng kiến trúc — là thiếu nội dung.

**Nguyên tắc thiết kế (giữ đúng nguyên tắc đã có trong mod, không thêm thanh mới):**
- Đây là "sự kiện xảy ra VỚI chính phủ" → **event, không phải focus** (đúng phân loại mục 3.4 của chính báo cáo, và đúng cách `vie_pol`/`vie_scs` hiện tại vận hành: "lịch sử chạy bằng event, lựa chọn chạy bằng focus").
- Mỗi event ghi trục bằng `add_to_variable = { VIE_ax_xxx = ± }` rồi `VIE_ax_normalize = yes` (đúng mẫu đã dùng ở `vie_pol.23-26`), **không** tạo track/modifier mới.
- Không cho lựa chọn "miễn phí" — mỗi option có ít nhất 1 cái giá, theo đúng phê bình đã có ở `political_branch_plan_review.md` §3.5.

**Danh sách 7 event đề xuất, namespace tiếp nối `vie_pol.27` trở đi (namespace đang dừng ở `.26`):**

| ID | Tên | Kích hoạt (`trigger`/mtth) | Option A (lịch sử/nhượng bộ) | Option B (cứng rắn) |
|---|---|---|---|---|
| `vie_pol.27` | Tranh chấp đất đai Tiên Lãng – Văn Giang | `date > 2012.1.1`, ngẫu nhiên trong cửa sổ 2012–2013, chỉ bắn nếu chưa có `VIE_land_law_2013_flag` | Cưỡng chế theo kế hoạch: ổn định −0.02, `VIE_ax_civil −1` | Đối thoại, dừng cưỡng chế: PP −25, `VIE_ax_checks +1` |
| `vie_pol.28` | Bauxite Tây Nguyên: phản ứng của giới trí thức | gắn `has_completed_focus = VIE_bauxite_tay_nguyen`, mtth ngắn sau đó | Giữ dự án, không phản hồi thư kiến nghị: `VIE_ax_civil −1` | Công khai báo cáo tác động môi trường: ổn định +0.01, chi phí dự án nhẹ |
| `vie_pol.29` | Formosa: bồi thường và biểu tình (hậu quả chính trị của `VIE_formosa_steel_complex`) | `has_completed_focus = VIE_formosa_steel_complex`, `date > 2016.4.1` | Bồi thường nhanh, hạn chế biểu tình: `VIE_ax_civil −1`, ổn định +0.01 | Cho phép biểu tình giám sát môi trường: `VIE_ax_checks +1`, quan hệ Đài Loan (chủ đầu tư Formosa) −nhẹ |
| `vie_pol.30` | Biểu tình phản đối dự luật đặc khu (6/2018) | `date = 2018.6.10 ± vài ngày`, độc lập focus (đây là sự kiện đã xảy ra dù người chơi làm gì — đúng nguyên tắc "hệ thống tự kích hoạt" mục 4.1 của báo cáo) | **Hoãn dự luật (lịch sử):** ổn định +0.02, PP −30, uy tín đường lối hiện hành −nhẹ | **Giữ nguyên dự luật (phản thực tế):** `VIE_ax_civil −1`, ổn định −0.03, `VIE_ax_checks −1` |
| `vie_pol.31` | Luật An ninh mạng: phạm vi áp dụng | gắn ngay sau `vie_pol.30`, hoặc `has_completed_focus = VIE_cybersecurity_law` nếu tồn tại làm focus riêng | Áp dụng đầy đủ: `VIE_ax_civil −1`, FDI công nghệ −nhẹ (nếu có modifier FDI công nghệ, dùng chung với `VIE_fdi_attraction`) | Áp dụng có ngoại lệ cho big tech: `VIE_ax_west +1`, `VIE_ax_civil` không đổi |
| `vie_pol.32` | Bộ luật Lao động 2019 và phê chuẩn ILO | `has_completed_focus = VIE_cptpp_member` HOẶC gần `VIE_evfta`, `date > 2019.11.1` — nên đặt làm **điều kiện `available` ngược của chính hai focus đó** nếu chưa có, theo đúng mục 8.1(b) báo cáo: hội nhập đòi điều kiện thể chế | Phê chuẩn đầy đủ (lịch sử, cần cho EVFTA): `VIE_ax_checks +1`, Tổng Liên đoàn Lao động phản ứng nhẹ (opinion nội bộ nếu MD có cơ chế công đoàn, nếu không thì bỏ) | Trì hoãn: EVFTA/CPTPP bị treo (thêm điều kiện chặn ở chính hai focus đó nếu muốn ràng buộc cứng) |
| `vie_pol.33` | Luật Thực hiện dân chủ ở cơ sở (2022): kênh xả áp lực | gắn sau chuỗi trên, `date > 2022.11.1` | Thực thi nghiêm: `VIE_ax_checks +1`, `VIE_ax_civil` không đổi | Hình thức, ít thực chất: không đổi trục, chỉ +PP nhỏ (mô phỏng "xả áp lực giả") |

**Ghi chú kỹ thuật bắt buộc trước khi code (để không lặp lỗi mà `political_branch_plan_review.md` đã bắt được ở kế hoạch trước):**
1. Kiểm tra `VIE_ax_civil`, `VIE_ax_checks`, `VIE_ax_west` là đúng tên biến trong `common/dynamic_modifiers/VIE_md_state_modifier.txt` trước khi dùng (báo cáo trên liệt kê 9 biến `VIE_ax_*`, chưa liệt kê hết — đọc file thật, đừng đoán tên).
2. Mọi thay đổi trục qua `add_to_variable` phải theo sau bằng gọi chuẩn hóa `VIE_ax_normalize` đúng cú pháp đang dùng ở `vie_pol.23-26` (xem `events/VIE_md_pol.txt` dòng quanh 332–428 làm mẫu).
3. Đặt event trong `events/VIE_md_pol.txt` (namespace `vie_pol` đã khai báo ở đó), **không** tạo file event mới, để không phải khai báo namespace lần nữa.
4. Loc tiếng Việt đặt ở `localisation/english/replace/*_l_english.yml` theo đúng quy ước đã ghi trong `political_branch_plan_review.md` §3.6 (không phải `localisation/VIE_md_l_english.yml` gốc).
5. `ai_chance` cho mỗi event: dùng `factor` cố định trước (khớp thực trạng "chỉ 17% event có modifier theo ngữ cảnh" ghi ở `VIE_report_focus_event_decision.md` §3.2) — không bắt buộc phải làm AI-aware ngay, nhưng nếu làm thì việc này gộp chung với khuyến nghị #5 của backlog đã có ("bổ sung modifier AI cho D1–D8").
6. Sau khi thêm, chạy `python tools/check_static.py` — phải vẫn ra 0 lỗi.

### 3.3 QA: audit anachronism theo mục 9 báo cáo mới (không phải code, là rà soát)

Báo cáo liệt kê các mốc thuật ngữ chính xác (mục 9.12): "kinh tế thị trường định hướng XHCN" chỉ từ 2001, "ngoại giao cây tre" chỉ từ 2021 (dù khái niệm groundwork có sớm hơn), "Kỷ nguyên vươn mình" chỉ từ cuối 2024, "Bốn không" chỉ từ 2019.

**Việc cần làm:** grep tên các idea/loc string chứa các cụm trên trong `common/ideas/*.txt` và các file `localisation/**/*.txt|yml` có tham chiếu, đối chiếu `available`/ngày mở khóa của focus mang các idea đó. Đây là việc kiểm tra 30 phút, không phải thiết kế lại. Không có bằng chứng hiện tại cho thấy có lỗi (vd. `VIE_bamboo_diplomacy` đã tồn tại như một focus riêng, hợp lý nếu khóa theo ngày ≥ 2021 — cần xác nhận `available` thật của nó).

---

## 4. Việc KHÔNG làm (để tránh phá vỡ kiến trúc đã ổn định)

- **Không** thêm power balance/thước đo mới cho "bức xúc xã hội" — dùng 7–9 trục sẵn có (`civil`, `checks` là đại diện đúng nhất), đúng ràng buộc kỹ thuật đã xác lập ở STEP5 (tối đa 3 power balance, VIE đã dùng đủ 3).
- **Không** tách `resolution_57_68` thành 4 focus riêng theo đúng cấu trúc "mỗi nghị quyết một node" của báo cáo mới — vi phạm nguyên tắc "một nhánh, một spirit, nâng cấp dần" đã thống nhất ở `political_branch_plan_review.md` §4.1.3, và số lượng focus thân lịch sử (210) đã đủ dày.
- **Không** làm lại nhánh dân tộc chủ nghĩa (H2a/H2b) — đã có bản redesign riêng, tốt hơn đề xuất của báo cáo này.
- **Không** thêm focus Đại hội IX/X/XI/XIII làm node riêng cho "đẹp lịch sử" — STEP6 đã quyết định giữ Đại hội là điểm đọc trục ẩn trong các focus liên quan, không phải node trang trí, và việc thêm 4 focus không hiệu ứng riêng sẽ chỉ làm cây dày thêm mà không đổi gameplay — đúng cảnh báo "focus độn" mà `political_branch_plan_review.md` đã tự phê bình và sửa.

---

## 5. Thứ tự thực hiện thật (gộp vào backlog đã có, không tạo backlog riêng)

Đây là backlog `VIE_report_focus_event_decision.md` §7, chèn 2 việc mới của báo cáo này vào đúng vị trí ưu tiên:

| # | Việc | Nguồn | File |
|---|---|---|---|
| 1 | Chạy một ván ngắn, gửi `error.log` | backlog cũ, vẫn P0 | — |
| 2 | Sửa 127 cặp focus chen sát trong bố cục | backlog cũ | `common/national_focus/VIE_md_focus.txt` |
| 3 | Xác nhận 4 focus bị xóa là cố ý (`VIE_forest_protection`, `VIE_hanoi_air_quality`, `VIE_plastic_waste`, `VIE_jetp`→`VIE_jetp_partnership`) | backlog cũ | — |
| 4 | Dọn `.bak*` và `scratch/` trước khi đóng gói | backlog cũ | thư mục gốc |
| 5 | **Thêm 7 event `vie_pol.27–33`** (mục 3.2 ở trên) | báo cáo mới | `events/VIE_md_pol.txt` |
| 6 | Loc tiếng Việt cho 7 event trên | báo cáo mới | `localisation/english/replace/` |
| 7 | Rà anachronism thuật ngữ (mục 3.3) | báo cáo mới | grep, không sửa trừ khi thấy lỗi |
| 8 | Bổ sung modifier AI cho event điểm rẽ D1–D8 **và** `vie_pol.27–33` cùng lúc | backlog cũ + báo cáo mới gộp chung | `events/VIE_md_pol.txt` |
| 9 | Bổ sung decision cho nhánh dân chủ hóa/môi trường nếu muốn cân bằng | backlog cũ | `common/decisions/VIE_md_decisions.txt` |
| 10 | Thêm phương án trung gian `vie_disaster.1`, `vie_petro.1` | backlog cũ | events tương ứng |
| 11 | (Tùy chọn, ưu tiên thấp) EU vào `VIE_csp_network` — chỉ nếu MD có tag đại diện EU | báo cáo mới, mục 3.1 | `common/national_focus/VIE_md_focus.txt` |
| 12 | Chạy lại `python tools/check_static.py`, phải vẫn 0 lỗi | cả hai | — |

**Việc 5–7 và 11 là phần thật sự mới từ báo cáo vừa nhận.** Việc 1–4, 8–10 đã được xác định độc lập trước khi báo cáo này tới và có mức ưu tiên kỹ thuật cao hơn (chặn chạy thử game thật).
