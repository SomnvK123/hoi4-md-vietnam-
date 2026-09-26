# Bước 9: Kế hoạch thi công theo batch

> Bước cuối của quy trình nghiên cứu STEP 1–9. Tiếp theo `VIE_transition_graph_step8.md`.
>
> Nhãn: **[SỰ KIỆN]** · **[TIỀN ĐỀ KỊCH BẢN]**

---

## 0. Món nợ kỹ thuật lớn nhất đã trả xong

**[SỰ KIỆN]** Câu hỏi treo từ STEP 5 — *"đổi luật MD bằng focus có sạch không"* — đã có câu trả lời bằng cách đọc code MD. **Có, và MD cung cấp sẵn API đầy đủ:**

| Họ luật | Effect tăng | Effect giảm | Báo cho hệ ngân sách |
|---|---|---|---|
| `bureau_law` | `increase_centralization = yes` | `decrease_centralization = yes` | `change_expected_bureaucracy_spending` |
| `police_law` | `increase_policing_budget = yes` | `decrease_policing_budget = yes` | `change_expected_police_spending` |
| `education_law` | `increase_education_budget = yes` | `decrease_education_budget = yes` | `change_expected_education_spending` |
| `health_law` | `increase_healthcare_budget = yes` | `decrease_healthcare_budget = yes` | `change_expected_health_spending` |
| `social_law` | `increase_social_spending = yes` | `decrease_social_spending = yes` | `change_expected_social_spending` |
| `military_law` | `increase_military_spending = yes` | `decrease_military_spending = yes` | `change_expected_defense_spending` |

Cả hai mẫu dùng đều có trong MD và đã chạy:

- **Mẫu Canada** (`05_canada.txt:5752`) — mẫu nên theo:
```
available = { NOT = { has_idea = bureau_05 } }
bypass    = { has_idea = bureau_05 }
completion_reward = {
    increase_centralization = yes
    set_temp_variable = { desire_change = 0.5 }
    change_expected_bureaucracy_spending = yes
}
```
- **Mẫu Đan Mạch** (`05_denmark.txt:4663`) — `swap_ideas` thủ công theo từng mức, dùng khi cần nhảy nhiều mức một lúc.

**Hệ quả:** phần "quyết định lặp lại" ở STEP 5 và phần nối luật ở STEP 6 **không còn bị chặn**.

---

## 1. Nguyên tắc thi công

1. **Không xóa focus, không đổi ID, không đụng cấu trúc `VIE_md_focus`.** Toàn bộ thay đổi là **thêm** vào `completion_reward` và `available`.
2. **Mọi thứ sinh bằng script từ hai file dữ liệu đã có** — `_gen/axis_map.py` và `_gen/axis_map_mil_alt.py`. Không gõ tay 370 focus.
3. **Ưu tiên cơ chế MD sẵn có.** Không thêm power balance (MD tối đa 3, VIE đã có 3). Dùng dynamic modifier, luật, internal faction.
4. **Sau mỗi batch: `python3 tools/check_static.py` phải in 0 errors**, và sao lưu vào `D:\HOI4Mods\_backup_v5`.
5. **Batch 0–2 không đổi gameplay** — chỉ đo. Có thể chạy game kiểm tra an toàn trước khi động vào luật chơi.

---

## 2. Bảy batch

### Batch 0 — Hạ tầng đo lường (không đổi gameplay)

| Việc | Chi tiết |
|---|---|
| File mới `common/dynamic_modifiers/VIE_md_state_modifier.txt` | `VIE_state_modifier` đọc 9 biến `VIE_ax_size`, `VIE_ax_merit`, `VIE_ax_decent`, `VIE_ax_checks`, `VIE_ax_market`, `VIE_ax_civil`, `VIE_ax_integ`, `VIE_ax_mob`, `VIE_ax_west` |
| Hiệu ứng thực | Mỗi trục gắn 1–2 modifier nhỏ (ví dụ `merit` → `political_power_gain` + `production_factory_efficiency_gain_factor`; `checks` → `stability_factor`; `integ` → `trade_opinion_factor`). Biên độ ±3% ở hai đầu thang |
| Khởi tạo | `VIE_doi_moi_continues` gắn modifier và đặt giá trị khởi đầu STEP 6 mục 2: size +3, merit −2, decent +1, checks −2, market −2, civil −3, integ 0 |
| Chuẩn hóa | Scripted effect `VIE_ax_normalize` tính `VIE_ax_<a>_norm = round(10 × thô / SPAN)`, SPAN theo bảng STEP 8 mục 1. Gọi từ scheduler `on_monthly` đã có |
| Loc | 9 khóa tên trục + 18 khóa tên hai cực |
| `tools/check_static.py` | Mọi biến `VIE_ax_*` phải có trong modifier và có loc |

**Rủi ro:** thấp. **Kiểm chứng:** mod nạp sạch, danh sách modifier quốc gia hiện đúng một mục mới với 9 dòng.

### Batch 1 — Gắn trục vào thân lịch sử (167 focus)

Sinh từ `_gen/axis_map.py`, chèn vào `completion_reward` ngay sau dòng `log`, đúng cách đã làm với 34 focus BoP:

```
add_to_variable = { VIE_ax_merit = 2 tooltip = VIE_ax_merit_tt }
add_to_variable = { VIE_ax_size = -1 tooltip = VIE_ax_size_tt }
```

**Rủi ro:** thấp, thuần script. **Kiểm chứng:** lấy `VIE_public_admin_reform`, giá trị `merit` phải +2 và `size` phải −1.

### Batch 2 — Gắn trục vào quân sự và dải chế độ (203 focus)

Sinh từ `_gen/axis_map_mil_alt.py`: 51 focus quân sự, 152 focus dải chế độ. Cùng cách.

**Rủi ro:** thấp. **Kiểm chứng:** vào dải `ol_*`, `merit` phải tụt mạnh; vào `np_*`, `mob` phải tăng mạnh.

### Batch 3 — Nối vào luật MD (khoảng 14 focus)

| Focus | Gọi gì |
|---|---|
| `VIE_streamline_apparatus`, `VIE_merge_ministries`, `VIE_provincial_merger`, `VIE_two_tier_local_gov` | `decrease_centralization` + `change_expected_bureaucracy_spending` (desire âm) |
| `VIE_public_admin_reform`, `VIE_e_government` | `change_expected_bureaucracy_spending` desire âm, **không** đổi mức (chúng cải thiện chất lượng, không đổi quy mô) |
| `VIE_cybersecurity_law`, `VIE_force_47`, `sec_*` | `increase_policing_budget` |
| `VIE_free_tuition`, `VIE_education_reform` | `increase_education_budget` |
| `VIE_universal_health_insurance`, `VIE_grassroots_clinics` | `increase_healthcare_budget` |
| `VIE_social_insurance_reform`, `dm_soc_welfare_state` | `increase_social_spending` |

**Rủi ro: trung bình.** Đổi luật làm tăng chi thường xuyên; nếu ngân khố không chịu nổi, hệ ngân sách MD sẽ phản ứng. **Phải chạy game thử batch này riêng**, không gộp với batch khác.

### Batch 4 — Đánh đổi: mỗi điểm trục đều có hóa đơn

**[TIỀN ĐỀ KỊCH BẢN]** Đây là batch quan trọng nhất về mặt thiết kế, vì nó sửa khiếm khuyết "92% focus không có đánh đổi".

| Trục | Cái giá | Cách code |
|---|---|---|
| `merit` tăng | Mất công cụ bảo trợ (Geddes 1994) | `set_temp_variable = { temp_opinion = -2 }` + `change_communist_cadres_opinion = yes` |
| `integ` tăng | Dễ tổn thương trước cú sốc ngoài | Modifier trong `VIE_state_modifier`; và điều kiện cho event khủng hoảng chuỗi cung ứng |
| `civil` giảm | Bộ máy an ninh tự thành mối đe dọa | Thêm faction `intelligence_community` khi qua ngưỡng |
| `market` tăng nhanh hơn `merit` | Bị bắt cóc (Evans) | **Cạnh Kiến tạo → Tài phiệt**, xem batch 5 |
| `decent` tăng | Vấn đề phối hợp | Modifier nhỏ âm vào `production_speed_buildings_factor` |

Thêm internal faction theo ngưỡng, qua scheduler: `oligarchs`, `the_military`, `intelligence_community`, `labour_unions`, `small_medium_business_owners`, `chaebols`, `defense_industry`.

**Rủi ro: trung bình cao.** **[SỰ KIỆN]** Chưa biết MD giới hạn bao nhiêu faction cùng lúc cho một nước — **phải thử trước khi code batch này**.

### Batch 5 — Điều kiện mở nhánh theo cấu hình (16 gốc dải + 4 cạnh mới)

Thêm điều kiện trục vào `available` của 16 gốc dải, theo bảng ngưỡng STEP 8 mục 4. **Giữ nguyên cờ**:

```
available = {
    has_country_flag = VIE_oligarch_unlocked
    check_variable = { VIE_ax_merit_norm < 2 }
    check_variable = { VIE_ax_market_norm > 3 }
}
```

Bốn cạnh thất bại/đảo ngược thành event mới trong `events/VIE_md_axis.txt`:
1. Kiến tạo trượt thành Tài phiệt khi `market_norm − merit_norm` vượt ngưỡng
2. Lạc Hồng thoái hóa thành độc đoán thường sau N năm không chiến tranh
3. Dân chủ hóa dừng ở độc đoán cạnh tranh
4. Sụp đổ đọc trục thay vì chỉ đọc stability

**Rủi ro: cao.** Đây là batch **đổi luật chơi**. Nếu ngưỡng sai, người chơi hoặc bị khóa hết nhánh hoặc mở hết. **Phải playtest từng nhánh.**

### Batch 6 — Quyết định lặp lại "Xây dựng nhà nước"

Danh mục mới `VIE_statebuilding_category`, theo mẫu `VIE_military_readiness_category` đã chạy. Khoảng 6 quyết định, mỗi cái đẩy một trục với chi phí và `days_re_enable`:

- Đợt thi tuyển công chức cạnh tranh — `merit +1`, tốn PP, giảm opinion cán bộ
- Giao quyền thí điểm cho tỉnh — `decent +1`
- Nâng/hạ mức luật bộ máy — gọi `increase_centralization` hoặc `decrease_centralization`
- Nới kiểm soát nội dung — `civil +1`, giảm ổn định ngắn hạn
- Siết kiểm soát nội dung — `civil −1`, tăng ổn định, giảm `checks`
- Đàm phán hiệp định mới — `integ +1`, tốn PP

**Rủi ro: thấp** (mẫu đã chạy), nhưng phụ thuộc batch 3.

### Batch 7 — Loc, tài liệu, kiểm tra

- Loc tiếng Việt cho mọi khóa mới
- Cập nhật `tools/TESTING.md`, `implementation_plan_v6.md`
- Viết `VIE_statebuilding_design_v1.md` gộp kết quả STEP 1–9
- Mở rộng `check_static.py`: mọi `VIE_ax_*` có loc; mọi điều kiện `check_variable` trỏ tới biến có thật; mọi `increase_*`/`decrease_*` là effect có trong MD
- Ghi vào memory

---

## 3. Thứ tự và phụ thuộc

```
Batch 0 ──► Batch 1 ──► Batch 2 ──┐
   │                              ├──► Batch 5 (ngưỡng) ──► Batch 7
   └──► Batch 3 ──► Batch 6       │
            └──► Batch 4 ─────────┘
```

- **Batch 0–2 an toàn**, có thể làm liền một mạch rồi chạy game một lần.
- **Batch 3 phải chạy game riêng** — nó đụng hệ ngân sách.
- **Batch 4 phải thử giới hạn faction trước.**
- **Batch 5 là batch duy nhất đổi luật chơi**, nên làm sau cùng trước phần tài liệu.

---

## 4. Khối lượng

| Batch | Focus/file đụng tới | Sinh bằng script | Cần chạy game |
|---|---|---|---|
| 0 | 3 file mới, 1 focus | một phần | có |
| 1 | 167 focus | hoàn toàn | không bắt buộc |
| 2 | 203 focus | hoàn toàn | không bắt buộc |
| 3 | ~14 focus | một phần | **bắt buộc, riêng** |
| 4 | ~40 focus + 1 scheduler | một phần | **bắt buộc** |
| 5 | 16 gốc dải + 4 event | một phần | **bắt buộc, từng nhánh** |
| 6 | 1 danh mục + 6 quyết định | tay | có |
| 7 | loc + tài liệu | một phần | không |

**Tổng: khoảng 440 focus được thêm dòng, không focus nào bị xóa hay đổi ID.**

---

## 5. Kiểm chứng

**Sau mỗi batch:**
- `python3 tools/check_static.py` in **0 errors**
- Sao lưu `D:\HOI4Mods\_backup_v5`

**Trong game, theo batch:**

| Batch | Kiểm gì |
|---|---|
| 0 | `logs/error.log` không có dòng `VIE`; danh sách modifier hiện mục mới với 9 dòng |
| 1–2 | Lấy `VIE_public_admin_reform` → `merit` +2, `size` −1. Vào dải `ol_*` → `merit` tụt mạnh |
| 3 | Lấy `VIE_streamline_apparatus` → `bureau_law` giảm một mức, chi thường xuyên giảm, ngân sách không vỡ |
| 4 | Lấy một focus chống tham nhũng → opinion `communist_cadres` giảm. Qua ngưỡng → faction mới xuất hiện |
| 5 | **Chạy đủ 11 nhánh.** Con đường lịch sử phải mở đúng 1 nhánh (Kiến tạo), 10 nhánh còn lại đóng |
| 6 | Quyết định có cooldown, đổi đúng trục |

**Phép thử tổng:** chơi một ván lịch sử tới 2026, so vân tay trục với bảng STEP 8 mục 2. Sai lệch lớn nghĩa là bảng ánh xạ cần chỉnh.

---

## 6. Những gì không làm

1. Không thêm power balance.
2. Không xóa focus, không đổi ID, không đổi `relative_position_id`.
3. Không tạo GUI riêng — bảy trục hiện trong danh sách modifier như `VIE_armed_forces_modifier` đang làm.
4. Không tự chế hệ tham nhũng, hệ ngân sách, hay hệ luật — dùng của MD.
5. Không gắn cứng quân sự vào chế độ.
6. Không đụng nhánh quân sự và dải chế độ về mặt cấu trúc, chỉ thêm dòng.

---

## 7. Rủi ro và cách giảm

| Rủi ro | Mức | Cách giảm |
|---|---|---|
| Ngưỡng sai → khóa hết hoặc mở hết nhánh | **Cao** | Batch 5 làm cuối, playtest từng nhánh, ngưỡng để trong scripted effect để chỉnh nhanh |
| Đổi luật làm vỡ ngân sách | Trung bình | Batch 3 chạy riêng; dùng mẫu Canada đi qua `change_expected_*_spending` |
| Vượt giới hạn internal faction của MD | Trung bình | **Thử trước batch 4** |
| 9 dòng modifier quá dài, khó đọc | Thấp | Gộp bằng `custom_modifier_tooltip` nếu cần |
| Bảng ánh xạ sai ở vài focus | Thấp | Phép thử tổng ở mục 5 phát hiện được |
| Nội dung quân sự và MIO **chưa từng playtest** | **Cao, đã tồn tại** | Nên chạy một ván ngắn **trước** batch 0 |

---

## 8. Món nợ còn lại sau STEP 9

| Món | Trạng thái |
|---|---|
| Thử đổi `bureau_law` bằng focus | **ĐÃ TRẢ** — mục 0 |
| Giới hạn internal faction của MD | **Chưa** — chặn batch 4 |
| Literature quan hệ dân sự – quân sự Việt Nam | **Chưa** — ngưỡng Junta `mob ≥ 9` hiện là suy ra |
| Ngưỡng cho 4 cạnh thất bại | **Chưa có số** |
| Ba điều kiện tổn thương hệ thống quy ra biến game | **Chưa** |
| Ba điều kiện cấu trúc của Lạc Hồng quy ra cách đo | **Chưa** |
| Cái giá Geddes chưa vào file dữ liệu | **Chưa** — batch 4 xử lý |
| Nội dung quân sự và MIO chưa playtest | **Chưa** — nên làm trước tiên |

---

## 9. Tóm tắt toàn bộ quy trình STEP 1–9

| Bước | Kết quả chính |
|---|---|
| 1–2 | 19 dải và 16 party slot thực ra là **6 loại tương lai**; 36 focus không đổi `ruling_party` nên không phải chế độ |
| 3 | Ba family: A cần 8 điều kiện mà Việt Nam thiếu 5; B là mặc định và A, C đều rẽ ra từ B; C có hai lối vào |
| 4 | **MD đã có sẵn hệ năng lực nhà nước, submod dùng 0 lần**; kỹ trị và nhà nước kiến tạo đều không phải chế độ |
| 5 | Bảy trục, mỗi trục một đánh đổi có nguồn; một dynamic modifier, không thêm power balance |
| 6 | 167 focus lịch sử đã ánh xạ; mô hình **tái tạo đúng hồ sơ 5 giai đoạn** Đổi Mới |
| 7 | Mỗi dải có **chữ ký trục riêng khớp literature**; dải "Kiến tạo" thực ra là dải dân chủ hóa |
| 8 | Vân tay lịch sử; ngưỡng cho 11 cạnh; **10/11 nhánh đóng** trên con đường lịch sử |
| 9 | Bảy batch, khoảng 440 focus được thêm dòng, không xóa gì |
