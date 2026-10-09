# Con đường Kiên định — Toàn văn Nội dung và Kế hoạch Triển khai (CPV Hardline)

> **Tài liệu tổng hợp toàn diện (08/10/2026)**  
> Dành cho submod Vietnam Millennium Dawn (
uling_party = 4).

## Mục lục
1. [Phần 1: Nội dung chi tiết cây Focus (Bản 2 cập nhật)](#phần-1-nội-dung-chi-tiết-cây-focus-bản-2-cập-nhật)
2. [Phần 2: Kế hoạch triển khai mã nguồn (6 giai đoạn)](#phần-2-kế-hoạch-triển-khai-mã-nguồn-6-giai-đoạn)
3. [Phụ lục: Bản nháp nội dung v1 (Lịch sử)](#phụ-lục-bản-nháp-nội-dung-v1-lịch-sử)

---


## Phần 1: Nội dung chi tiết cây Focus (Bản 2 cập nhật)

# Con đường Kiên định (bản 2)

Nội dung cây focus khi CPV Hardline (Communist-State, `ruling_party = 4`) cầm quyền.
Tài liệu nội dung, chưa code. Bản 2, 04/10/2026. Thay thế bản nháp 1.

> **Bản 4 (05/10/2026) — Hợp nhất Toàn diện Nhánh An ninh & Kiên định (30 Focuses):**
> - Giải quyết dứt điểm xung đột ID đảng (`ruling_party = 7` vs `4`) và loại bỏ hoàn toàn khối an ninh x=93 trùng lặp.
> - Hợp nhất thành một cây duy nhất gồm **30 focus**: 25 focus Hardline gốc + 5 focus An ninh chuyên biệt (`VIE_sec_public_order`, `VIE_sec_border_control`, `VIE_sec_surveillance_network`, `VIE_sec_cyber_sovereignty`, `VIE_sec_state_data_center`).
> - Gộp 6 focus An ninh song sinh: `VIE_sec_security_state` $\rightarrow$ `VIE_hl_unity_of_will`; `VIE_sec_cyber_control` $\rightarrow$ `VIE_hl_cyber_ideology`; `VIE_sec_loyalty_vetting` $\rightarrow$ `VIE_hl_party_rectification`; `VIE_sec_security_economy` $\rightarrow$ `VIE_hl_selective_fdi`; `VIE_sec_ideological_education` $\rightarrow$ `VIE_hl_school_theory`; `VIE_sec_managed_opening` $\rightarrow$ `VIE_hl_steadfast_renewal`.
> - Tích hợp toàn diện 5 Quyết định An ninh (`VIE_sec_dec_*`) với cơ chế Áp lực cải cách (`VIE_rp`).
>
> **Bản 3 (05/10/2026) — thay thế mục 2 và mục 8.** CPV Hardline không còn là khối riêng hay lên nắm quyền qua event Đại hội / decision giữa nhiệm kỳ.
> - Đại hội XIV có **ba lựa chọn loại trừ nhau** trên cùng hàng: `Tập trung quyền lực`, `Mở rộng giám sát thể chế` (hai hướng CPV ID 19) và `Giữ vững bản chất, kiên định mục tiêu` (`VIE_hl_unity_of_will`, đưa ID 4 lên cầm quyền qua `vie_hl.1`). Điều kiện: CPV ID 19 cầm quyền, BoP < −0,3, đã làm `Đội ngũ cán bộ trong sạch`, sau 30/06/2026. Toàn bộ cây Kiên định treo dưới lựa chọn này.
> - Đã xóa: lựa chọn `hl_take` ở các event Đại hội XI–XVI, `hl_keep` ở XII–XIV, decision Hội nghị Trung ương bất thường, cờ `VIE_hardline_unlocked`. Giữ `hl_keep` ở Đại hội XV, XVI.
> - **Thống nhất Đông Dương (chỉ Hardline)**, dưới trụ D: `Liên minh đặc biệt Đông Dương` (cần `Đoàn kết Đông Dương`) → `Tối hậu thư Viêng Chăn` + `Tối hậu thư Phnôm Pênh` (event `vie_hl.20`: chấp nhận thì thành chư hầu, từ chối thì `vie_hl.21` cho wargoal chư hầu) → `Thống nhất Đông Dương` (kiểm soát 7 vùng 511–517, sáp nhập chư hầu, thêm core, mở quyết định thành lập Đông Dương của MD). Focus cũ `VIE_indochina_federation` đã gộp vào chuỗi này.
> - **Thu hồi đảo (CPV ID 19 và ID 4)**, nhánh Biển Đông: `Thu hồi Hoàng Sa` (813, Trung Quốc; giữ ID `VIE_paracel_ultimatum`) → `Thu hồi Bắc Trường Sa` (526, Trung Quốc) → `Thu hồi Đông Trường Sa` (802, Philippines) và `Thu hồi Nam Trường Sa` (816, Malaysia). AI không chọn.

## 0. Thay đổi so với bản 1

| Vấn đề ở bản 1 | Sửa ở bản 2 |
|---|---|
| Chưa biết index của hardline | Đã xác nhận: `ruling_party = 4` (comment trong `VIE_md_triggers.txt`: Neutral_Communism = CPV lịch sử, Communist-State = biến thể hardline). |
| Đề xuất đóng chuỗi Đại hội | Sai với code: `VIE_party_rule_active` gồm cả 19 và 4, nên chuỗi Đại hội vẫn chạy dưới hardline. Bản 2 giữ chuỗi Đại hội, dùng nó làm cửa lên nắm quyền. |
| `VIE_transition_regime` đặt BoP về 0 | Event "Nhận quyền" phải kéo BoP về phía bảo thủ ngay sau khi gọi effect. |
| Đường C (từ nhánh an ninh) | Bỏ. `VIE_sec_cyber_control` chuyển sang đảng 7 (Autocracy), không phải 4. |
| Nhánh an ninh cướp quyền hardline | Mới phát hiện: hardline đẩy trục B xuống, có thể chạm ngưỡng `VIE_sb_B < -5` của `sec_cyber_control`, và focus đó sẽ đổi đảng sang 7. Xem mục 1.3. |
| Tổng Áp lực 70–80 không bao giờ chạm vùng Khủng hoảng 86+ | Tính lại số. Làm hết mà không xả van thì vào vùng Khủng hoảng, có xả thì ở vùng Căng thẳng. |
| Điều kiện E1 mơ hồ | Mỗi trụ có đúng một focus cuối. |
| X2 điều kiện theo trục ẩn | Đổi sang trục hiển thị `VIE_sb_B` và BoP. |
| Thay đổi trục quá nhỏ để thấy | Tính theo span chuẩn hóa thật (mục 3.3). Trục D gần như không đổi, chấp nhận vì phù hợp với ý "không chọn phe". |
| X3 "Khép cửa" mâu thuẫn với trụ D | Thay bằng "Bàn giao đường lối", tức trở về CPV chính thống. Kịch bản khép cửa chuyển thành trạng thái khủng hoảng qua event. |
| Lợi dụng: lên hardline, lấy thưởng rồi quay về | Quay về giờ là một kết cục có thiết kế (X3), có điều kiện và có giá. |
| D2 "giảm căng thẳng Biển Đông" | Mâu thuẫn với "không nhường". Bỏ, thay bằng mở lựa chọn cứng rắn không mất ổn định. |
| C2 và H3 "mất một phần bonus focus cũ" | Khó code (phải gỡ idea). Thay bằng hiệu ứng trực tiếp. |
| H1 viết như thanh trừng phe phái | Viết lại theo đúng tinh thần TW4: chống suy thoái tư tưởng, gắn với chống tham nhũng. |

## 1. Điều kiện mở cây và quan hệ với cây cũ

### 1.1 Điều kiện mở

- H0 `available`: `check_variable = { ruling_party = 4 }`. Không dùng cờ vĩnh viễn.
- Mọi focus trong cây đều có thêm điều kiện `ruling_party = 4`. Hardline mất quyền thì cả cây đóng. Focus đã làm vẫn giữ, idea riêng của cây bị gỡ (mục 1.4).
- Cây luôn hiển thị nhưng xám. Tooltip: "Cần Đường lối Kiên định cầm quyền".

### 1.2 Cây cũ khi hardline cầm quyền

| Phần cây cũ | Xử lý |
|---|---|
| Chuỗi Đại hội và nghị quyết (`VIE_resolution_congress_*`) | Vẫn chạy, vì `VIE_party_rule_active` vẫn đúng. Không cần sửa. |
| Đảng xây dựng (`party_discipline`, `cadre_accountability`, `clean_cadres`) | Vẫn mở. Nếu đã làm `clean_cadres` thì H1 được giảm 2 Áp lực. |
| Hội nhập (`evfta`, `cptpp_member`, `investment_grade`, `international_financial_centre`) | Vẫn làm được. Mỗi focus giảm 4 Áp lực nhưng làm cán bộ cộng sản −2 và BoP cải cách nhỏ. X2 khóa hai focus cuối. |
| Tư nhân (`private_champions`, `private_sector_engine`) | Loại trừ với A5, theo cả hai chiều. |
| Kinh tế nhà nước (`state_conglomerates`, `scic`, `soe_gradual_restructuring`) | Mở. A1 thưởng thêm nếu đã làm `state_conglomerates`. |
| `soe_rapid_divestment` | Khóa khi đã làm A1. |
| Quân sự (`modernize_vpa`, `peoples_defence`, `military_enterprises_*`) | Giữ nguyên, làm tiền đề cho trụ B. |

### 1.3 Va chạm với nhánh an ninh (phải sửa code cũ)

`VIE_sec_cyber_control` mở khi `VIE_sb_B < -5` và có cờ `VIE_security_unlocked`, rồi gọi `VIE_transition_regime` sang đảng 7. Cây hardline đẩy B xuống khoảng −2,5 đến −3,5, nên người chơi hardline hoàn toàn có thể chạm ngưỡng này.

**Quyết định:** dưới hardline, nhánh sec_* vẫn làm được nhưng không đổi đảng.
Trong `completion_reward` của `sec_cyber_control`, giới hạn đoạn chuyển quyền bằng `NOT = { check_variable = { ruling_party = 4 } }`. Người chơi hardline vẫn nhận idea `VIE_security_state_idea` và đi tiếp nhánh sec_*, nhưng Áp lực +10.

Lý do: hardline là "Đảng nắm tất cả", không phải công an thay Đảng. Một người chơi hardline chọn nhánh an ninh là thêm công cụ, không phải chuyển chế độ.

### 1.4 Khi hardline mất quyền

`VIE_transition_regime` sang đảng khác thì:
- Gỡ các idea riêng của cây: "Công tác tư tưởng", "Chủ đạo nhà nước", "Kế hoạch định hướng", "Công tác Đảng trong quân đội", "Thế trận toàn dân", "Nhất thể hóa", "Thời kỳ tự lực".
- Xóa biến `VIE_rp` (Áp lực cải cách).
- Trục `VIE_ax_*` giữ nguyên. Thay đổi thể chế không tự biến mất.

Cách làm: trong `VIE_transition_regime`, trước `change_ruling_party_effect`, kiểm tra `ruling_party = 4` và `rul_party_temp` khác 4 thì gọi `VIE_hl_cleanup`. Lúc đó `ruling_party` vẫn là đảng cũ nên không cần lưu biến tạm.

### 1.5 Lãnh đạo dưới hardline

Khi chuyển sang đảng 4, `set_leader_VIE` tạo lãnh đạo hư cấu "Pham Dinh Tuan" (Communist-State), có sẵn ở [VIE_political_leaders.txt:93](common/scripted_effects/VIE_political_leaders.txt#L93).

**Vấn đề:** các event Đại hội sau đó vẫn bắn vì `VIE_party_rule_active` đúng. Lựa chọn lịch sử của chúng gọi `VIE_new_leader_trong`, `_dung`, `_to_lam`, tức là dựng lại lãnh đạo thật với hệ tư tưởng Neutral_Communism trong khi đảng cầm quyền là Communist-State.

**Sửa:** mọi lựa chọn lịch sử có đổi lãnh đạo (`vie_pol.5.a/.b`, `.6.a/.b/.c`, `.7.a`, `.8.a/.b`, `.12.*`, `.13.*`) thêm `NOT = { check_variable = { ruling_party = 4 } }`. Mỗi event thêm một lựa chọn riêng cho hardline: "Đại hội khẳng định đường lối", giữ lãnh đạo, +50 PP, BoP bảo thủ nhỏ.

## 2. Đường lên nắm quyền (ngoài cây)

Mốc sớm nhất: **Đại hội XI (01/2011)**. Đại hội IX và X không có lựa chọn hardline.

### 2.1 Hai đường, hai điều kiện

Mô hình "cửa" trong `VIE_md_alt.txt` không đủ cho mốc 2011. Lý do: các cửa bảo thủ đều mở sau Đại hội XI. `vie_alt.3` bắn sau 31/05/2011, `vie_alt.1` sau HD-981 (2014), còn `vie_alt.2` chỉ có khi đã nới báo chí. Vì vậy hai đường dùng hai điều kiện khác nhau:

| | Đường A: tại Đại hội | Đường B: Hội nghị Trung ương bất thường |
|---|---|---|
| Ý nghĩa | Đại hội là nơi hợp thức để đổi đường lối, không cần khủng hoảng | Đổi đường lối giữa nhiệm kỳ, phải có khủng hoảng làm cớ |
| BoP | < −0,3 (`VIE_hl_bop_leads_conservative`) | < −0,3 |
| Cờ `VIE_hardline_unlocked` | **Không cần** | **Cần** |
| Thời điểm | Đại hội XI trở đi | Sau Đại hội XI |
| Chung | Không có `VIE_regime_changed_recently` | Như bên trái |

### 2.2 Đường A: lựa chọn tại Đại hội

Thêm lựa chọn "Giữ vững bản chất, kiên định mục tiêu" vào các event Đại hội:

| Đại hội | Event | File |
|---|---|---|
| XI (2011) | `vie_pol.4` | `events/VIE_md_pol.txt` |
| XII (2016) | `vie_pol.5` | `events/VIE_md_pol.txt` |
| XIII (2021) | `vie_pol.6` | `events/VIE_md_pol.txt` |
| XIV (2026) | `vie_pol.8` | `events/VIE_md_pol.txt` |
| XV (2031) | `vie_pol.12` | `events/VIE_md_p10.txt` |
| XVI (2036) | `vie_pol.13` | `events/VIE_md_p10.txt` |

- Trigger: `ruling_party = 19` (chưa phải hardline), `VIE_hl_bop_leads_conservative = yes` (BoP < −0,3), không có `VIE_regime_changed_recently`.
- Hiệu ứng: gọi `country_event = { id = vie_hl.1 }`.
- AI: `factor = 0` khi `VIE_ai_historical = yes`, ngược lại base 5.

Ngưỡng −0,3 (không phải −0,6) vì cộng mọi effect bảo thủ trong mod thì −0,6 không thể đạt trước 2011 (BoP khởi đầu −0,1, các event trước 2011 chỉ cho khoảng −0,3 đến −0,4). Với −0,3, người chơi nghiêng bảo thủ nhất quán trong chuỗi Đại hội IX, X và các event 2001–2010 có thể đạt trước Đại hội XI. Sau khi lên nắm quyền BoP được đặt lại −0,5.

### 2.3 Đường B: Hội nghị Trung ương bất thường (decision)

Cờ `VIE_hardline_unlocked` đặt ở các lựa chọn bảo thủ sẵn có:

| Event | Lựa chọn | Thêm |
|---|---|---|
| `vie_alt.1` (sau HD-981) | `.b` "Đảng chọn đường lối cứng rắn" | `set_country_flag = VIE_hardline_unlocked` |
| `vie_alt.3` (khủng hoảng vĩ mô) | `.b` "Trật tự trước hết" | Đặt cờ, cùng với `VIE_security_unlocked` |
| `vie_alt.7` (rút tiền ngân hàng, 2022) | `.a` "Nhà nước ra tay" | Đặt cờ chỉ khi BoP < −0,4 |

Decision `VIE_hl_extraordinary_plenum`:
- Điều kiện: `ruling_party = 19`, có cờ, `VIE_hl_bop_leads_conservative`, `has_country_flag = VIE_sched_congress_11`, không có `VIE_regime_changed_recently`.
- Giá 100 PP. Hoàn tất thì gọi `vie_hl.1`.
- Không có tỷ lệ ngẫu nhiên. Đủ điều kiện là thành công.
- Bỏ điều kiện popularity: dưới chế độ một đảng, BoP phản ánh đấu tranh nội bộ tốt hơn.

### 2.4 Event `vie_hl.1` "Nhận quyền"

1. Tăng popularity đảng 4 giống `sec_cyber_control` (`change_relative_party_popularity`, 0,15). Đặt `rul_party_temp = 4`, gọi `VIE_transition_regime = yes`.
2. Sau effect: BoP về −0,5 (transition đã đặt về 0) bằng `set_power_balance`.
3. `set_variable = { VIE_rp = 20 }`.
4. Một lựa chọn duy nhất. Tooltip báo cây "Con đường Kiên định" đã mở.

## 3. Cơ chế: Áp lực cải cách (`VIE_rp`)

### 3.1 Thang và ngưỡng

| Mức | Khoảng | Hệ quả |
|---|---|---|
| Ổn định | 0–30 | Không có. |
| Âm ỉ | 31–55 | Mở event phản ứng nhẹ (2, 3, 4). |
| Căng thẳng | 56–79 | Idea "Bất bình âm ỉ": stability −3%, tăng trưởng năng suất −1%. Mở event 5. |
| Khủng hoảng | 80–100 | Idea nặng hơn: stability −8%, tăng trưởng năng suất −3%. Bắt buộc event 7 trong 30 ngày. |

**Hiển thị: cả số lẫn tên mức**, giống cách mod đang hiện bốn trục (`-3 (Kỷ cương)`).
- Một dòng thêm vào `VIE_state_modifier_desc`: `Áp lực cải cách: 64 (Căng thẳng), khủng hoảng từ 80`.
- Dòng này là scripted localisation `VIE_HlPressureLine`, trả về chuỗi rỗng khi `ruling_party` khác 4.
- Màu theo mức: §G xanh (Ổn định), §Y vàng (Âm ỉ), §O cam (Căng thẳng), §R đỏ (Khủng hoảng).
- Mỗi focus có tooltip "Áp lực cải cách +6", nên người chơi tự tính được còn cách ngưỡng bao xa.
- Không cần GUI mới.

### 3.2 Nguồn tăng và giảm

**Tăng:** focus siết (bảng mục 4), event.
**Giảm:**
- Focus van xả: C4 (−4), D3 (−10), X1 (−25).
- Focus hội nhập cũ: −4 mỗi focus.
- Tự giảm: −1 mỗi tháng nếu không hoàn thành focus siết nào trong 120 ngày (cờ `VIE_rp_recent` có thời hạn, đặt khi làm focus siết).
- Event: lựa chọn "tiếp thu" và nhượng bộ.

**Kiểm tra tổng** (bắt đầu 20):

| Cách chơi | Áp lực khi tới E1 |
|---|---|
| Làm hết, không xả van, bác bỏ mọi event | 20 + 62 + 5–10 ≈ **87–92**: Khủng hoảng |
| Làm hết, có C4 | ≈ 78–83: biên giới Căng thẳng/Khủng hoảng |
| Làm hết, có C4 và D3 | ≈ **68–73**: Căng thẳng |
| Thêm "tiếp thu" ở event 2, hoặc làm 1–2 focus hội nhập | ≈ **50–60**: Âm ỉ, đủ điều kiện X3 |

Kết quả: người chơi phải chọn giữa siết tối đa và chịu khủng hoảng, hoặc xả van và mất điểm với cán bộ bảo thủ.

### 3.3 Tác động lên trục hiển thị (ĐÃ BỎ)

> Hệ bốn trục và mọi effect trục (`VIE_ax_*`) đã bị xóa khỏi toàn bộ focus, event và decision (05/10/2026). Các dòng "trục +/−" trong bảng focus ở mục 4 chỉ còn là ý đồ ban đầu, không còn trong code. Mục này giữ lại để tham khảo.


Đã tính theo span chuẩn hóa trong `VIE_ax_normalize`. Một đơn vị thô bằng:

| Trục thô | Span | Tác động lên trục hiển thị |
|---|---|---|
| civil −1 | 14 | B −0,71 |
| mob +1 | 12 | B −0,42 |
| checks −1 | 19 | B −0,26 |
| market −1 | 41 | C −0,24 |
| decent −1 | 24 | C −0,21 |
| merit +1 | 59 | A +0,17 |
| size +1 | 12 | A −0,42 |
| integ −1 | 98 | D −0,10 |
| west −1 | 29 | D −0,17 |

Tổng cả cây (trước kết cục), theo số ở mục 4:

| Trục | Tổng thô | Thay đổi trục hiển thị | Ý nghĩa |
|---|---|---|---|
| B Không gian Chính trị | civil −2, checks −2, mob +3 | ≈ **−3,2** | Từ "Cân bằng" xuống "Kỷ cương". Có thể chạm −6 nếu xuất phát đã thấp, xem mục 1.3. |
| C Mô hình Kinh tế | market −9, decent −2 | ≈ **−2,6** | Về vùng "Chủ đạo nhà nước". |
| A Năng lực Bộ máy | merit +3, size +2 | ≈ **−0,3** | Gần như không đổi: liêm chính hơn, nhưng bộ máy phình ra. |
| D Đối ngoại | integ −3 +1, west −1 | ≈ **−0,4** | Gần như không đổi. Đúng ý "không chọn phe". |

## 4. Danh sách focus

Ký hiệu: **AL** = Áp lực cải cách. Mọi focus có `ruling_party = 4` trong `available`. Focus tốn tiền hoặc xây công trình có guard `bankruptcy_incoming_collapse` như file hiện tại. Focus siết đặt cờ `VIE_rp_recent` 120 ngày.

### 4.1 Gốc và củng cố

**H0. Thống nhất ý chí và hành động** (5 tuần)
- *Mô tả:* Hội nghị Trung ương khẳng định giữ vững bản chất cách mạng, mở đầu nhiệm kỳ mới.
- *Điều kiện:* `ruling_party = 4`.
- *Thưởng:* +50 PP. BoP bảo thủ nhỏ. Nếu chưa có `VIE_rp` thì đặt 20.
- *Đổi lại:* Không.

**H1. Chỉnh đốn Đảng, ngăn chặn suy thoái** (7 tuần)
- *Mô tả:* Theo tinh thần TW4 khóa XII: ngăn chặn suy thoái tư tưởng, đạo đức, lối sống, "tự diễn biến", "tự chuyển hóa". Kỷ luật đi cùng chống tham nhũng.
- *Điều kiện:* H0.
- *Thưởng:* merit +1, checks −1. Stability +2%. Giảm một nấc tham nhũng. Cán bộ cộng sản +3.
- *Đổi lại:* AL +6 (+4 nếu đã làm `clean_cadres`). Tập đoàn công nghiệp −4. Idea `VIE_official_caution` 365 ngày.

**H2. Bảo vệ nền tảng tư tưởng** (7 tuần)
- *Mô tả:* Tăng nguồn lực cho Ban Tuyên giáo và hệ thống Học viện. Tinh thần Nghị quyết 35/NQ-TW.
- *Điều kiện:* H0.
- *Thưởng:* +50 PP. Idea "Công tác tư tưởng": stability +2%, drift defence +5%.
- *Đổi lại:* AL +4. civil −1.

**H3. Thống nhất quản lý cán bộ** (7 tuần)
- *Mô tả:* Trung ương quản chặt cán bộ chủ chốt, thu hẹp quyền tự quyết của địa phương.
- *Điều kiện:* H1.
- *Thưởng:* decent −2, merit +1. BoP bảo thủ nhỏ.
- *Đổi lại:* AL +4. Nếu đã làm `decentralization`: thêm AL +3 và decent −1 (đảo ngược cải cách cũ có giá).

### 4.2 Trụ A. Kinh tế (focus cuối: A6)

**A1. Kinh tế nhà nước giữ vai trò chủ đạo** (7 tuần)
- *Điều kiện:* H1.
- *Thưởng:* market −3. Ngân quỹ +2. Idea "Chủ đạo nhà nước" (stability +2%, xây công nghiệp quân sự +5%). Cán bộ cộng sản +4. Đã làm `state_conglomerates`: thêm +25 PP.
- *Đổi lại:* AL +4. Tăng trưởng năng suất −1% trong 730 ngày. Tập đoàn công nghiệp −4. Khóa `soe_rapid_divestment`.

**A2. Danh mục ngành then chốt** (7 tuần)
- *Mô tả:* Năng lượng, ngân hàng, viễn thông, quốc phòng: nhà nước nắm chi phối.
- *Điều kiện:* A1.
- *Thưởng:* Một nhà máy dân dụng ở một vùng (`one_state_industrial_complex`). market −1.
- *Đổi lại:* AL +2.

**A3. Tập đoàn nhà nước làm đầu tàu** (7 tuần)
- *Điều kiện:* A1.
- *Thưởng:* Một lần tăng trưởng. Idea "Tập đoàn đầu tàu" (tốc độ xây dựng +5%, 730 ngày).
- *Đổi lại:* AL +2. `VIE_vinashin_risk` +2.

**A4. Kiểm soát dòng vốn, FDI có chọn lọc** (7 tuần)
- *Điều kiện:* A2.
- *Thưởng:* Stability +1%. +25 PP. market −1.
- *Đổi lại:* AL +6. Ngân quỹ −2. integ −2. Idea "FDI chững lại" 365 ngày. Thiện cảm USA, JAP, KOR −10 (bọc `country_exists`).

**A5. Đảng viên không làm kinh tế tư nhân** (7 tuần)
- *Mô tả:* Đảo ngược `party_members_private_business`.
- *Điều kiện:* H1. Chưa làm `private_champions` và `private_sector_engine`. Hai focus kia cũng phải thêm điều kiện chưa làm A5.
- *Thưởng:* merit +1, market −1. BoP bảo thủ nhỏ. Cán bộ cộng sản +3.
- *Đổi lại:* AL +5. Tập đoàn công nghiệp −5.
- *Ghi chú:* Nhánh phụ, không bắt buộc cho A6.

**A6. Kế hoạch định hướng 5 năm** (7 tuần)
- *Điều kiện:* A3 và A4.
- *Thưởng:* mob +1, market −2. Ngân quỹ +3. Idea "Kế hoạch định hướng" (sản lượng nhà máy +5%, tăng trưởng năng suất −1%).
- *Đổi lại:* AL +3. size +1.

### 4.3 Trụ B. Quân – Đảng (focus cuối: B4)

**B1. Đảng lãnh đạo tuyệt đối, trực tiếp về mọi mặt đối với quân đội** (7 tuần)
- *Điều kiện:* H0 (tiền đề) và đã làm `modernize_vpa` (qua `available`, vì focus này nằm xa trên cây).
- *Thưởng:* Quân đội +3. BoP bảo thủ nhỏ. Idea "Công tác Đảng, công tác chính trị trong quân đội" (tổ chức sư đoàn hồi +5%). XP lục quân +10.
- *Đổi lại:* AL +2.

**B2. Giáo dục chính trị trong lực lượng vũ trang** (5 tuần)
- *Điều kiện:* B1.
- *Thưởng:* War support +3%. XP lục quân +10.
- *Đổi lại:* AL +1. Ngân quỹ −1.

**B3. Thế trận quốc phòng toàn dân gắn với cơ sở Đảng** (7 tuần)
- *Điều kiện:* B1 (tiền đề) và đã làm `peoples_defence` (qua `available`).
- *Thưởng:* mob +1. Idea "Thế trận toàn dân" (nhân lực có thể tuyển +3%).
- *Đổi lại:* AL +3.
- *Ghi chú:* Không bắt buộc cho B4, vì không phải người chơi nào cũng làm `peoples_defence`.

**B4. Công nghiệp quốc phòng do Đảng chỉ đạo** (7 tuần)
- *Điều kiện:* B2.
- *Thưởng:*
  - Đã làm `military_enterprises_core`: `VIE_def_industry_level` +1.
  - Đã làm `military_enterprises_divest`: đảng ủy trong doanh nghiệp quân đội đã cổ phần hóa. +50 PP, stability +1%. Không cộng cấp.
  - Chưa làm cái nào: +25 PP.
- *Đổi lại:* AL +2. market −1.
- *Ghi chú:* Bản 1 khóa B4 nếu đã divest, khiến trụ B có thể không hoàn thành được. Bản 2 không khóa.

### 4.4 Trụ C. Tư tưởng và xã hội (focus cuối: C4)

**C1. Bảo vệ nền tảng tư tưởng trên không gian mạng** (7 tuần)
- *Mô tả:* Đấu tranh với thông tin "sai trái, thù địch" trên nền tảng xuyên biên giới. Đây là lớp nội dung, không phải giám sát hàng loạt (đó là sec_*).
- *Điều kiện:* H2.
- *Thưởng:* Idea "Quản lý nội dung mạng" (drift defence +5%, stability +1%).
- *Đổi lại:* AL +7. west −1. Thiện cảm USA −5.

**C2. Giáo dục lý luận chính trị trong nhà trường** (7 tuần)
- *Điều kiện:* H2.
- *Thưởng:* Stability +2%. Cán bộ cộng sản +2.
- *Đổi lại:* AL +3. Tốc độ nghiên cứu −2% trong 730 ngày.

**C3. Quy hoạch báo chí** (5 tuần)
- *Mô tả:* Rà soát, sắp xếp lại cơ quan báo chí theo định hướng (thực tế đã có Quy hoạch báo chí 2019).
- *Điều kiện:* C1.
- *Thưởng:* +50 PP. civil −1, checks −1.
- *Đổi lại:* AL +6. Thiện cảm các nước dân chủ −5.

**C4. Phát huy vai trò Mặt trận Tổ quốc và các đoàn thể** (7 tuần)
- *Mô tả:* Mặt trận, Công đoàn, Hội Nông dân, Đoàn Thanh niên là kênh tập hợp và phản biện trong khuôn khổ.
- *Điều kiện:* C2 và H3.
- *Thưởng:* mob +1. Nông dân +4. Stability +2%. **AL −4** (van mềm).
- *Đổi lại:* size +1.

### 4.5 Trụ D. Đối ngoại (focus cuối: D2)

Không chọn phe, theo đúng tinh thần v14. Chỉ có ngoại giao giữa các đảng và một van mở có chọn lọc.

**D1. Đẩy mạnh quan hệ đối ngoại Đảng** (7 tuần)
- *Điều kiện:* H0.
- *Thưởng:* +50 PP. Thiện cảm LAO, CHI, CUB +10. integ −1.
- *Đổi lại:* AL +2.

**D2. Hợp tác nhưng không lệ thuộc** (7 tuần)
- *Mô tả:* Gần gũi ý thức hệ không thay cho lợi ích chủ quyền. Đây là cách hardline tự điều tiết mâu thuẫn: thân Bắc Kinh về tư tưởng, không nhường ở Biển Đông.
- *Điều kiện:* D1 và `four_nos_doctrine`.
- *Thưởng:* War support +3%. Stability +1%. Cờ `VIE_hl_sovereignty_line`: event 6 có lựa chọn cứng rắn không mất stability.
- *Đổi lại:* AL +0. Thiện cảm CHI −5 (lấy lại một phần của D1).

**D3. Đối tác chiến lược có chọn lọc** (7 tuần)
- *Mô tả:* Giữ quan hệ với Nhật, Ấn, Hàn: hợp tác kinh tế và an ninh trong khuôn khổ "bốn không".
- *Điều kiện:* D2 và ít nhất một trong `japan_partnership`, `india_partnership`, `korea_partnership`.
- *Thưởng:* **AL −10**. integ +1. Thiện cảm JAP, RAJ, KOR +10.
- *Đổi lại:* Cán bộ cộng sản −2. BoP cải cách nhỏ.

### 4.6 Tổng kết

**E1. Tổng kết nhiệm kỳ, định hướng chặng mới** (7 tuần)
- *Điều kiện:* H3, và ba trong bốn: A6, B4, C4, D2.
- *Thưởng:* +100 PP, stability +3%. Mở ba kết cục.
- *Đổi lại:* Gọi event 5 (Hội nghị Trung ương giữa nhiệm kỳ).

### 4.7 Ba kết cục (loại trừ nhau)

**X1. Kiên định mục tiêu, đổi mới phương thức** (7 tuần)
- *Mô tả:* Nhà nước giữ then chốt, kinh tế tư nhân và hội nhập tiếp tục trong khuôn khổ. Đây là kết cục gần thực tế nhất.
- *Điều kiện:* E1, AL < 80.
- *Thưởng:* **AL −25**. market +2, integ +2. Một lần tăng trưởng. Focus hội nhập cũ không còn phạt cán bộ. Idea "Đổi mới có kiểm soát" (stability +3%, tăng trưởng năng suất +1%).
- *Đổi lại:* Cán bộ cộng sản −3. BoP về −0,3.
- *AI:* Đây là lựa chọn mặc định.

**X2. Nhất thể hóa lãnh đạo Đảng và quản lý Nhà nước** (7 tuần)
- *Mô tả:* Nhất thể hóa chức danh (Bí thư kiêm Chủ tịch) ở mọi cấp. Hợp nhất cơ quan Đảng và cơ quan Nhà nước cùng chức năng. Bộ máy gọn hơn nhưng không còn đối trọng.
- *Điều kiện:* E1, cả bốn A6, B4, C4, D2. `VIE_sb_B <= -4`. `VIE_bop_is_hardline = yes`.
- *Thưởng:* +150 PP, stability +5%. checks −2, decent −2, **size −2** (sáp nhập làm gọn bộ máy). Idea "Nhất thể hóa" (PP +10%, stability +3%, tốc độ nghiên cứu −3%).
- *Đổi lại:* AL +8. market −2. Khóa `investment_grade` và `international_financial_centre`.
- *AI:* factor 0 khi `VIE_ai_historical = yes`.

**X3. Bàn giao đường lối** (5 tuần)
- *Mô tả:* Nhiệm kỳ củng cố được coi là hoàn thành. Đại hội trao lại đường lối cho phe chính thống. Hardline lùi về, giữ ảnh hưởng.
- *Điều kiện:* E1, AL ≤ 55, không có idea "Thời kỳ tự lực".
- *Thưởng:* Chuyển về `ruling_party = 19` qua `VIE_transition_regime`, BoP −0,3. Giữ idea "Công tác Đảng trong quân đội" và "Công tác tư tưởng" (ngoại lệ ở mục 1.4). +100 PP, stability +5%.
- *Đổi lại:* Mất cây hardline. Cờ `VIE_hardline_retired`: không lên lại được trong 10 năm.
- *Lý do:* Phản ánh đúng mô hình thực tế: một giai đoạn siết để chỉnh đốn rồi trở lại quỹ đạo. Đồng thời biến cái "lợi dụng" ở bản 1 thành một lựa chọn có thiết kế.

## 5. Sự kiện (namespace `vie_hl`)

| # | Sự kiện | Kích hoạt | Lựa chọn |
|---|---|---|---|
| 1 | Nhận quyền | Từ đường A/B | Một lựa chọn (mục 2.4). |
| 2 | Thư kiến nghị của các cựu lãnh đạo | AL ≥ 31, đã làm H1. Một lần. | **Tiếp thu:** AL −10, BoP cải cách nhỏ, cán bộ −2. **Bác bỏ:** AL +5, stability +1%. |
| 3 | Doanh nghiệp FDI tạm hoãn đầu tư | AL ≥ 40, đã làm A4 hoặc A5 | **Trấn an:** ngân quỹ −2, market +1, AL −3. **Mặc kệ:** tăng trưởng năng suất −2% trong 365 ngày. |
| 4 | Cảnh báo cam kết lao động và thương mại (EVFTA/CPTPP) | Có `evfta` hoặc `cptpp_member`, đã làm C1 hoặc C3 | **Điều chỉnh:** AL −5, civil +1. **Giữ lập trường:** thiện cảm EU và JAP −10. |
| 5 | Hội nghị Trung ương giữa nhiệm kỳ | Hoàn thành E1, hoặc AL ≥ 56 lần đầu. Mỗi lần kích hoạt cách nhau ít nhất 2 năm. | **Giữ nguyên:** không đổi. **Nới:** AL −10, BoP cải cách nhỏ. **Siết thêm:** AL +5, BoP bảo thủ nhỏ, +50 PP. |
| 6 | Phản ứng dư luận về Biển Đông | `VIE_scs_escalated_trigger`, đã làm D1 | **Có D2:** lựa chọn cứng rắn, war support +3%, AL 0. **Không có D2:** lựa chọn mềm, stability −2%, AL +5. |
| 7 | Khủng hoảng chính danh | AL ≥ 80. Bắt buộc. | **Lùi một bước:** AL −20, BoP về −0,3, cán bộ −3. **Kiên trì:** idea "Thời kỳ tự lực" 730 ngày (stability +5%, tăng trưởng năng suất −4%, thiện cảm thương mại −10%, xây nhà máy nội địa +10%), AL dừng ở 80. Hết hạn thì gọi event 8. |
| 8 | Đánh giá lại sau thời kỳ tự lực | Idea "Thời kỳ tự lực" hết hạn | **Mở lại:** AL về 50, bỏ idea. **Gia hạn:** idea thêm 365 ngày, stability −5%. Lần thứ hai bắt buộc mở lại. |

Không event nào dẫn tới bế tắc. Event 7 thay thế kết cục "Khép cửa" của bản 1: tự lực là trạng thái có thời hạn, có lối ra, không phải đích đến.

Đánh số event: dùng namespace mới `vie_hl` để không đụng `vie_alt`/`vie_pol`.

## 6. Tổng quan kết cục

| Kết cục | Ở lại cầm quyền | Được | Mất |
|---|---|---|---|
| X1 Đổi mới phương thức | Có | Áp lực thấp, tăng trưởng hồi, hội nhập tiếp tục | Cán bộ bảo thủ bất mãn |
| X2 Nhất thể hóa | Có | PP, stability cao nhất, bộ máy gọn | Khóa hướng tài chính, nghiên cứu chậm, áp lực cao |
| X3 Bàn giao | Không, về đảng 19 | Ổn định, giữ một phần di sản | Mất cây, không quay lại được 10 năm |
| (Event 7) Thời kỳ tự lực | Có | Stability ngắn hạn | Tăng trưởng, thương mại; bắt buộc mở lại |

## 7. AI

- Không có rule hướng đi (`VIE_ai_behavior` chỉ còn NO_PATH). AI chỉ lên hardline nếu event cho phép. Các lựa chọn mở cờ đều có `factor = 0` khi `VIE_ai_historical = yes`, tức là AI lịch sử sẽ không bao giờ vào nhánh này. Không cần thêm gì.
- Khi đã vào: base 50 cho các focus củng cố và trụ, nhưng `factor = 0.3` cho mọi focus siết khi AL ≥ 56, và `factor = 3` cho C4/D3. Như vậy AI tự xả van thay vì lao vào khủng hoảng.
- Kết cục: X1 base 60, X2 base 20, X3 base 20. X2 factor 0 nếu AL ≥ 70.
- Event 7: AI chọn "Lùi một bước" với 80%.

## 8. Bố cục Thực tế (Bản 4 — 30 Focus Hợp nhất)

Toàn bộ 30 focus được sắp xếp theo chuẩn lưới MD4 tuyệt đối ($dy = 1, \Delta x \ge 2$), neo gốc vào `VIE_party_centennial_2030` tại (14, 10). Gốc Hardline `VIE_hl_unity_of_will` nằm tại $(16, 12)$.

### Bảng Lưới Tọa độ Tuyệt đối (y = 12 đến 18)

| Hàng y | Tọa độ Tuyệt đối (x, y) & ID Focus |
|:---:|---|
| **y = 12** | **(16, 12)**: `VIE_hl_unity_of_will` (Gốc cây Kiên định) |
| **y = 13** | **(6, 13)**: `VIE_hl_ideological_foundation`<br>**(16, 13)**: `VIE_hl_party_rectification`<br>**(20, 13)**: `VIE_hl_party_leads_army`<br>**(24, 13)**: `VIE_hl_party_diplomacy` |
| **y = 14** | **(4, 14)**: `VIE_hl_cyber_ideology`<br>**(8, 14)**: `VIE_hl_school_theory`<br>**(12, 14)**: `VIE_hl_state_sector_leading`<br>**(16, 14)**: `VIE_hl_cadre_centralisation`<br>**(18, 14)**: `VIE_sec_public_order` *(An ninh ghép)*<br>**(20, 14)**: `VIE_hl_army_political_education`<br>**(24, 14)**: `VIE_hl_no_dependence` |
| **y = 15** | **(4, 15)**: `VIE_sec_surveillance_network` *(An ninh ghép)*<br>**(6, 15)**: `VIE_hl_press_planning`<br>**(8, 15)**: `VIE_hl_fatherland_front`<br>**(10, 15)**: `VIE_hl_key_sectors`<br>**(12, 15)**: `VIE_hl_soe_spearhead`<br>**(14, 15)**: `VIE_hl_no_party_business`<br>**(18, 15)**: `VIE_sec_border_control` *(An ninh ghép)*<br>**(20, 15)**: `VIE_hl_all_people_defence`<br>**(24, 15)**: `VIE_hl_selective_partners` |
| **y = 16** | **(4, 16)**: `VIE_sec_cyber_sovereignty` *(An ninh ghép)*<br>**(10, 16)**: `VIE_hl_selective_fdi`<br>**(12, 16)**: `VIE_sec_state_data_center` *(An ninh ghép)*<br>**(20, 16)**: `VIE_hl_party_defence_industry` |
| **y = 17** | **(12, 17)**: `VIE_hl_five_year_plan`<br>**(16, 17)**: `VIE_hl_term_review` |
| **y = 18** | **(12, 18)**: `VIE_hl_steadfast_renewal`<br>**(16, 18)**: `VIE_hl_party_state_fusion`<br>**(20, 18)**: `VIE_hl_handover` |

- **Khoảng cách ngang ($\Delta x$):** Tối thiểu 2 ô giữa các focus kề nhau trên cùng hàng.
- **Bước nhảy dọc ($dy$):** 100% đạt chuẩn $dy = 1$ (liền hàng), không đè ô, không dây chéo.
- `search_filters`: `POLITICAL`, `STABILITY`, `ECONOMY`, `ARMY`, `RESEARCH`.

## 9. Kế hoạch code

Xem file riêng [Con_duong_Kien_dinh_plan_code.md](Con_duong_Kien_dinh_plan_code.md).

## 10. Đã chốt

- Mốc sớm nhất: Đại hội XI (2011). Đại hội không cần cờ, decision giữa nhiệm kỳ cần cờ (mục 2.1).
- Áp lực cải cách hiện cả số lẫn tên mức (mục 3.1).
- X3 đặt cờ `VIE_hardline_retired` (10 năm). Đường A và B đều kiểm tra không có cờ này.
- `vie_hl.1` xóa cờ `VIE_congress_controls_leader`. Nếu sau này trở về đảng 19 thì `set_leader_VIE` tạo lãnh đạo hư cấu "phục hồi", không dựng lại lãnh đạo lịch sử.
- Ngưỡng lên nắm quyền (đường A và B) là BoP < −0,3, không phải −0,6. Chỉ X2 vẫn đòi BoP < −0,6 (`VIE_bop_is_hardline`).
- Option mới trong các event Đại hội tên là `vie_pol.N.hl_take` và `vie_pol.N.hl_keep` (tên `.c`/`.d` trùng key mô tả của event).
- B1 và B3 kiểm tra `modernize_vpa` và `peoples_defence` qua `available`, không qua `prerequisite`.
- Event phản ứng `vie_hl.2` đến `.8` do `VIE_hl_event_scheduler` gọi. Evfta, CPTPP, investment_grade, financial_centre giảm Áp lực 4 qua `VIE_hl_integration_valve`.
- Cleanup khi rời đảng 4 xóa cả cờ một lần của các event phản ứng.
- Cân bằng: các con số nhất quán với nhau và với span trục, nhưng chưa playtest.
- Hệ bốn trục đã bị bỏ: không còn effect trục trong focus nào, các trục luôn bằng 0. X2 không còn đòi `VIE_sb_B ≤ -4`; thay bằng đã làm C3 `VIE_hl_press_planning` (Quy hoạch báo chí). Cổng nhánh an ninh chỉ còn cần cờ `VIE_security_unlocked`.

---

## Phần 2: Kế hoạch triển khai mã nguồn (6 giai đoạn)

# Con đường Kiên định: kế hoạch code

Đi kèm tài liệu nội dung [Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md) (gọi tắt là "ND"). Bản 04/10/2026.

Chia 6 giai đoạn. Mỗi giai đoạn chạy được và kiểm tra được độc lập, nên có thể dừng giữa chừng mà mod không hỏng.

## 0. Quy ước

| Loại | Quy ước | Ví dụ |
|---|---|---|
| Focus | `VIE_hl_*` | `VIE_hl_unity_of_will` |
| Idea | `VIE_hl_*_idea` | `VIE_hl_ideology_work_idea` |
| Event | namespace `vie_hl` | `vie_hl.1` |
| Biến | `VIE_rp` (Áp lực cải cách) | |
| Cờ | `VIE_hl_*`, trừ `VIE_hardline_unlocked` và `VIE_hardline_retired` | `VIE_hl_rp_recent` |
| Scripted effect, trigger | `VIE_hl_*` | `VIE_hl_add_pressure` |
| Log | Mỗi `completion_reward` và mỗi option có dòng `log = "[GetDateText]: ..."` như file hiện tại | |
| Loc | Tiếng Việt, UTF-8 có BOM, như các file `.yml` khác | |

### Bảng id focus

| ND | Id | ND | Id |
|---|---|---|---|
| H0 | `VIE_hl_unity_of_will` | C1 | `VIE_hl_cyber_ideology` |
| H1 | `VIE_hl_party_rectification` | C2 | `VIE_hl_school_theory` |
| H2 | `VIE_hl_ideological_foundation` | C3 | `VIE_hl_press_planning` |
| H3 | `VIE_hl_cadre_centralisation` | C4 | `VIE_hl_fatherland_front` |
| A1 | `VIE_hl_state_sector_leading` | D1 | `VIE_hl_party_diplomacy` |
| A2 | `VIE_hl_key_sectors` | D2 | `VIE_hl_no_dependence` |
| A3 | `VIE_hl_soe_spearhead` | D3 | `VIE_hl_selective_partners` |
| A4 | `VIE_hl_selective_fdi` | E1 | `VIE_hl_term_review` |
| A5 | `VIE_hl_no_party_business` | X1 | `VIE_hl_steadfast_renewal` |
| A6 | `VIE_hl_five_year_plan` | X2 | `VIE_hl_party_state_fusion` |
| B1 | `VIE_hl_party_leads_army` | X3 | `VIE_hl_handover` |
| B2 | `VIE_hl_army_political_education` | | |
| B3 | `VIE_hl_all_people_defence` | | |
| B4 | `VIE_hl_party_defence_industry` | | |

### File mới

| File | Nội dung |
|---|---|
| `common/scripted_triggers/VIE_md_triggers_hardline.txt` | Trigger `VIE_hl_*` |
| `common/scripted_effects/VIE_md_effects_hardline.txt` | Effect `VIE_hl_*` |
| `common/ideas/VIE_md_ideas_hardline.txt` | Toàn bộ idea của nhánh |
| `common/scripted_localisation/VIE_md_hardline_loc.txt` | `VIE_HlPressureLine` |
| `common/decisions/VIE_md_hardline_decisions.txt` | Decision Hội nghị Trung ương bất thường, decision debug |
| `events/VIE_md_hardline.txt` | `vie_hl.1` đến `vie_hl.8` |
| `localisation/english/VIE_md_hardline_l_english.yml` | Toàn bộ loc của nhánh |

Focus vẫn nằm trong `common/national_focus/VIE_md_focus.txt`, vì đây là cây duy nhất và `check_static.py` chỉ đọc file này.

---

## Giai đoạn 1. Nền tảng: biến, trigger, effect, hiển thị

Mục tiêu: có Áp lực cải cách chạy được, hiện trên tooltip, chưa ai dùng tới.

### 1.1 Trigger (`VIE_md_triggers_hardline.txt`)

```
VIE_hl_in_power = {
	original_tag = VIE
	check_variable = { ruling_party = 4 }
}

# Đường A: tại Đại hội (không cần cờ)
VIE_hl_can_take_power_congress = {
	check_variable = { ruling_party = 19 }
	VIE_hl_bop_leads_conservative = yes	# BoP < -0.3 (bản đầu dùng -0.6 nhưng không đạt được trước 2011)
	NOT = { has_country_flag = VIE_regime_changed_recently }
	NOT = { has_country_flag = VIE_hardline_retired }
}

# Đường B: Hội nghị Trung ương bất thường (cần cờ)
VIE_hl_can_take_power_plenum = {
	VIE_hl_can_take_power_congress = yes
	has_country_flag = VIE_hardline_unlocked
	has_country_flag = VIE_sched_congress_11
}

VIE_hl_pillars_three = {
	custom_trigger_tooltip = {
		tooltip = VIE_hl_pillars_three_tt
		count_triggers = {
			amount = 3
			has_completed_focus = VIE_hl_five_year_plan
			has_completed_focus = VIE_hl_party_defence_industry
			has_completed_focus = VIE_hl_fatherland_front
			has_completed_focus = VIE_hl_no_dependence
		}
	}
}

VIE_hl_pillars_all = {
	has_completed_focus = VIE_hl_five_year_plan
	has_completed_focus = VIE_hl_party_defence_industry
	has_completed_focus = VIE_hl_fatherland_front
	has_completed_focus = VIE_hl_no_dependence
}
```

### 1.2 Effect (`VIE_md_effects_hardline.txt`)

| Effect | Việc làm |
|---|---|
| `VIE_hl_add_pressure` | Đọc `VIE_rp_add` (temp). Cộng vào `VIE_rp`, kẹp 0–100. Nếu dương thì đặt cờ `VIE_hl_rp_recent` 120 ngày. Gọi `VIE_hl_update_pressure_idea`. Có `custom_effect_tooltip` "Áp lực cải cách +N". |
| `VIE_hl_update_pressure_idea` | Gỡ hai idea mức. ≥ 80 thì thêm `VIE_hl_pressure_crisis_idea`, ≥ 56 thì `VIE_hl_pressure_tense_idea`. |
| `VIE_hl_monthly` | Chỉ chạy khi `VIE_hl_in_power`. Không có `VIE_hl_rp_recent` thì `VIE_rp` −1. Gọi `VIE_hl_update_pressure_idea`. Gọi các event phản ứng (giai đoạn 4). |
| `VIE_hl_take_power` | Gọi từ `vie_hl.1` (giai đoạn 2). |
| `VIE_hl_cleanup` | Gọi khi rời đảng 4. Gỡ idea, xóa `VIE_rp`. Nếu temp `VIE_hl_keep_legacy = 1` (X3) thì giữ `VIE_hl_ideology_work_idea` và `VIE_hl_army_party_work_idea`. |

Mẫu cho focus:

```
set_temp_variable = { VIE_rp_add = 6 }
VIE_hl_add_pressure = yes
```

### 1.3 Idea mức áp lực (`VIE_md_ideas_hardline.txt`)

Theo đúng mẫu `VIE_md_ideas_congress.txt` (`allowed = { always = no }`, `cancel_if_invalid = no`).

| Idea | Modifier |
|---|---|
| `VIE_hl_pressure_tense_idea` | `stability_factor = -0.03`, `country_productivity_growth_modifier = -0.01` |
| `VIE_hl_pressure_crisis_idea` | `stability_factor = -0.08`, `country_productivity_growth_modifier = -0.03` |

### 1.4 Hiển thị

- `common/scripted_localisation/VIE_md_hardline_loc.txt`: `defined_text VIE_HlPressureLine`.
  - Không phải hardline: key rỗng.
  - Bốn mức: `VIE_hl_rp_line_1` … `_4`, dạng `\n• Áp lực cải cách: §G[?VIE_rp|0]§! (Ổn định)`. Màu theo mức (§G, §Y, §O, §R). Kèm "khủng hoảng từ 80".
- Sửa `VIE_state_modifier_desc` trong [VIE_md_vi_axis_l_english.yml:3](localisation/english/replace/VIE_md_vi_axis_l_english.yml#L3): thêm `[VIE_HlPressureLine]` sau dòng "Định hướng Đối ngoại".

### 1.5 Tick tháng

[VIE_md_on_actions.txt](common/on_actions/VIE_md_on_actions.txt): thêm `VIE_hl_monthly = yes` vào danh sách scheduler, trước `VIE_ax_normalize = yes`.

### 1.6 Decision debug

Category `VIE_hl_debug_category`, `visible = { is_debug = yes }`, chỉ hiện khi chạy game với `-debug`. Gồm các decision:
- Đặt `VIE_rp` = 30 / 60 / 85.
- Ép `vie_hl.1` (lên nắm quyền ngay).

### Kiểm tra giai đoạn 1

- `python tools/check_static.py` không có lỗi mới.
- Trong game, dùng decision debug: tooltip modifier đổi số, đổi màu, idea mức xuất hiện và biến mất đúng ngưỡng. `VIE_rp` giảm 1 mỗi tháng.

---

## Giai đoạn 2. Đường lên nắm quyền

Mục tiêu: người chơi lên được hardline từ Đại hội XI, và hardline không bị nhánh khác cướp quyền.

### 2.1 Event `vie_hl.1` "Nhận quyền" và `VIE_hl_take_power`

```
VIE_hl_take_power = {
	set_temp_variable = { party_index = 4 }
	set_temp_variable = { party_popularity_increase = 0.15 }
	set_temp_variable = { temp_outlook_increase = 0.15 }
	hidden_effect = { change_relative_party_popularity = yes }
	set_temp_variable = { rul_party_temp = 4 }
	VIE_transition_regime = yes
	# transition đặt BoP = 0
	set_power_balance = { id = VIE_party_balance set_value = -0.5 }
	set_variable = { VIE_rp = 20 }
	VIE_hl_update_pressure_idea = yes
	# Lãnh đạo lịch sử không quay lại sau thời hardline
	clr_country_flag = VIE_congress_controls_leader
	clr_country_flag = VIE_trong_third_term
	clr_country_flag = VIE_to_lam_era
}
```

`set_power_balance` cần `left_side`/`right_side` giống [VIE_md_effects.txt:192-197](common/scripted_effects/VIE_md_effects.txt#L192-L197). Phải chép đủ khi code.

Việc xóa `VIE_trong_third_term` và `VIE_to_lam_era` làm các lựa chọn lịch sử ở `vie_pol.6.a`, `vie_pol.7`, `vie_pol.8.a`, `vie_pol.9` không còn hiện. Các lựa chọn dự phòng (`.6.c`, `.8.b`) sẽ thay vào.

### 2.2 Lựa chọn tại Đại hội (đường A)

| Event | File | Thêm |
|---|---|---|
| `vie_pol.4` (XI, 2011) | [VIE_md_pol.txt:112](events/VIE_md_pol.txt#L112) | Option `hl_take` (tên `.b` ở bản đầu đã trùng key mô tả event): trigger `VIE_hl_can_take_power_congress`. Gọi `country_event = { id = vie_hl.1 }`. |
| `vie_pol.5` (XII, 2016) | [VIE_md_pol.txt:137](events/VIE_md_pol.txt#L137) | Option `hl_take` như trên. Option `hl_keep` "Đại hội khẳng định đường lối Kiên định" khi `VIE_hl_in_power`. `.a` và `.b` thêm `NOT = { VIE_hl_in_power = yes }` (`.b` gọi `VIE_new_leader_dung`). |
| `vie_pol.6` (XIII, 2021) | [VIE_md_pol.txt:185](events/VIE_md_pol.txt#L185) | Option `hl_take` (lên nắm quyền), `hl_keep` (khẳng định đường lối). `.a`, `.b`, `.c` thêm `NOT = { VIE_hl_in_power = yes }`. |
| `vie_pol.7` (HNTW 2024) | [VIE_md_pol.txt:233](events/VIE_md_pol.txt#L233) | `trigger` thêm `NOT = { VIE_hl_in_power = yes }` (gọi `VIE_new_leader_to_lam`). |
| `vie_pol.8` (XIV, 2026) | [VIE_md_pol.txt:255](events/VIE_md_pol.txt#L255) | Option `hl_take` (lên nắm quyền), `hl_keep` (khẳng định). `.a`, `.b` thêm `NOT = { VIE_hl_in_power = yes }`. |
| `vie_pol.12`, `.13` (XV, XVI) | [VIE_md_p10.txt:53](events/VIE_md_p10.txt#L53) | Như `vie_pol.8`. |

AI: option lên nắm quyền có `ai_chance = { base = 5  modifier = { factor = 0 VIE_ai_historical = yes } }`.

**Lưu ý:** `gen_ev6.py` (nguồn sinh `VIE_md_effects_p10.txt`) không có trong repo lẫn lịch sử git. Tiêu đề của file đó đã đổi thành "bảo trì bằng tay" (04/10/2026), nên sửa tay `VIE_md_p10.txt` là an toàn.

### 2.3 Cờ mở khóa (đường B)

[VIE_md_alt.txt](events/VIE_md_alt.txt):
- `vie_alt.1.b` (dòng 26): thêm `set_country_flag = VIE_hardline_unlocked`.
- `vie_alt.3.b` (dòng 95): thêm như trên.
- `vie_alt.7.a` (dòng 169): thêm trong `if = { limit = { has_country_flag = VIE_bop_active power_balance_value = { id = VIE_party_balance value < -0.4 } } ... }`.

### 2.4 Decision `VIE_hl_extraordinary_plenum`

File `VIE_md_hardline_decisions.txt`, đặt trong category có sẵn `VIE_resolution_category` (hiện khi Đảng cầm quyền, [VIE_md_categories.txt:14](common/decisions/categories/VIE_md_categories.txt#L14)).

```
VIE_hl_extraordinary_plenum = {
	icon = generic_political_discourse
	allowed = { original_tag = VIE }
	visible = { has_country_flag = VIE_hardline_unlocked  check_variable = { ruling_party = 19 } }
	available = { VIE_hl_can_take_power_plenum = yes }
	cost = 100
	days_remove = 30
	fire_only_once = yes
	complete_effect = { log = ... }
	remove_effect = { country_event = { id = vie_hl.1 } }
	ai_will_do = { base = 0 }
}
```

### 2.5 Dọn dẹp khi rời đảng 4

[VIE_md_effects.txt:150](common/scripted_effects/VIE_md_effects.txt#L150) `VIE_transition_regime`, đặt trước `change_ruling_party_effect = yes` (dòng 181):

```
if = {
	limit = {
		check_variable = { ruling_party = 4 }
		NOT = { check_variable = { rul_party_temp = 4 } }
	}
	VIE_hl_cleanup = yes
}
```

### 2.6 Chặn nhánh an ninh cướp quyền

[VIE_md_focus.txt:4474](common/national_focus/VIE_md_focus.txt#L4474) `VIE_sec_cyber_control`. Sửa `limit` của khối chuyển quyền thành:

```
limit = {
	NOT = { check_variable = { ruling_party = 7 } }
	NOT = { check_variable = { ruling_party = 4 } }
}
```

Thêm nhánh `else_if` cho đảng 4: `set_temp_variable = { VIE_rp_add = 10 }` và `VIE_hl_add_pressure = yes`.

### Kiểm tra giai đoạn 2

- Ván mới, kéo BoP xuống dưới −0,3 trước 2011. Ở Đại hội XI có lựa chọn mới, chọn thì thành đảng 4, lãnh đạo "Pham Dinh Tuan", BoP −0,5, `VIE_rp` = 20.
- Ở Đại hội XII dưới hardline chỉ hiện lựa chọn "khẳng định đường lối".
- Không lên hardline, chơi tới 2016: các event Đại hội không đổi gì (kiểm tra hồi quy).
- Với AI lịch sử: không bao giờ chọn hardline.

---

## Giai đoạn 3. Cây focus (25 focus)

### 3.1 Khung chung mỗi focus

```
focus = {
	id = VIE_hl_party_rectification
	icon = ...
	x = ...  y = ...
	relative_position_id = VIE_hl_unity_of_will
	cost = 7
	prerequisite = { focus = VIE_hl_unity_of_will }
	search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }
	available = { VIE_hl_in_power = yes }
	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_rectification"
		...
		set_temp_variable = { VIE_rp_add = 6 }
		VIE_hl_add_pressure = yes
		VIE_ax_normalize = yes
	}
	ai_will_do = { ... }
}
```

- Mọi focus: `available = { VIE_hl_in_power = yes ... }`. Không dùng `allow_branch`, để cây luôn hiển thị như ND mục 1.1.
- Focus đổi trục: kết thúc bằng `VIE_ax_normalize = yes`, như `vie_alt.6.b`.
- Focus tốn ngân quỹ hoặc xây công trình: guard `bankruptcy_incoming_collapse` như các focus kinh tế hiện có.
- Vị trí: theo bảng ND mục 8. H0 neo `VIE_party_discipline` (x = 15, y = 4), các focus khác neo H0.
- Icon: dùng GFX có sẵn trong MD trước (`communist_purge`, `generic_political_reform`…), thay icon riêng sau.

### 3.2 Loại trừ

| Cặp | Cách làm |
|---|---|
| X1 / X2 / X3 | `mutually_exclusive` ba chiều. Ba focus nằm cạnh nhau nên không có đường vẽ chéo cây. |
| A5 và `private_champions`, `private_sector_engine` | Không dùng `mutually_exclusive` (hai focus kia ở xa, đường vẽ sẽ cắt ngang cây). Dùng `available` hai chiều: A5 cần `NOT = { has_completed_focus = ... }`, hai focus kia cần `NOT = { has_completed_focus = VIE_hl_no_party_business }`. |

### 3.3 Idea của cây

| Idea | Focus | Modifier |
|---|---|---|
| `VIE_hl_ideology_work_idea` | H2 | `stability_factor = 0.02`, `drift_defence_factor = 0.05` |
| `VIE_hl_state_leading_idea` | A1 | `stability_factor = 0.02`, `industrial_capacity_factory = 0.05` |
| `VIE_hl_state_transition_idea` (730 ngày) | A1 | `country_productivity_growth_modifier = -0.01` |
| `VIE_hl_soe_spearhead_idea` (730 ngày) | A3 | `production_speed_buildings_factor = 0.05` |
| `VIE_hl_fdi_slowdown_idea` (365 ngày) | A4 | `country_productivity_growth_modifier = -0.01` |
| `VIE_hl_planning_idea` | A6 | `industrial_capacity_factory = 0.05`, `country_productivity_growth_modifier = -0.01` |
| `VIE_hl_army_party_work_idea` | B1 | `army_org_regain = 0.05` |
| `VIE_hl_all_people_defence_idea` | B3 | `conscription_factor = 0.03` |
| `VIE_hl_cyber_content_idea` | C1 | `drift_defence_factor = 0.05`, `stability_factor = 0.01` |
| `VIE_hl_school_theory_idea` (730 ngày) | C2 | `research_speed_factor = -0.02` |
| `VIE_hl_controlled_renewal_idea` | X1 | `stability_factor = 0.03`, `country_productivity_growth_modifier = 0.01` |
| `VIE_hl_fusion_idea` | X2 | `political_power_factor = 0.10`, `stability_factor = 0.03`, `research_speed_factor = -0.03` |

Idea có thời hạn dùng `add_timed_idea = { idea = ... days = ... }`.
`check_static.py` kiểm tra key modifier có tồn tại trong MD, nên chạy script để bắt lỗi tên như `army_org_regain` hay `conscription_factor`.

### 3.4 Gọi thẳng effect có sẵn

| Việc | Effect hoặc biến |
|---|---|
| Thiện cảm nhóm lợi ích | `set_temp_variable = { temp_opinion = N }` rồi `change_communist_cadres_opinion`, `change_industrial_conglomerates_opinion`, `change_farmers_opinion`, `change_the_military_opinion` |
| Ngân quỹ | `set_temp_variable = { treasury_change = N }`, `modify_treasury_effect = yes` |
| Tăng trưởng | `increase_economic_growth = yes` |
| Tham nhũng | `decrease_corruption = yes` |
| Nhà máy | `one_state_industrial_complex` (theo mẫu [VIE_md_focus.txt:777](common/national_focus/VIE_md_focus.txt#L777)) |
| Công nghiệp quốc phòng | `VIE_def_industry_level` (theo mẫu [VIE_md_focus.txt:10249](common/national_focus/VIE_md_focus.txt#L10249)) |
| Vinashin | `VIE_vinashin_risk` |
| BoP | `VIE_bop_conservative_small` / `VIE_bop_reform_small` |
| Thận trọng trong bộ máy | `VIE_official_caution` (theo mẫu [VIE_md_focus.txt:2129](common/national_focus/VIE_md_focus.txt#L2129)) |

### 3.5 AI (ND mục 7)

```
ai_will_do = {
	base = 50
	modifier = { factor = 0.3  check_variable = { VIE_rp > 55 } }   # focus siết
}
```

C4, D3: `factor = 3` khi `VIE_rp > 55`. X1 base 60, X2 base 20 (`factor = 0` khi `VIE_ai_historical` hoặc `VIE_rp > 69`), X3 base 20.

### Kiểm tra giai đoạn 3

- `check_static.py`: không trùng ô, không có hàng xóm gần hơn 2, con không nằm trên cha, prerequisite và idea đều tồn tại.
- Trong game: cây hiện xám khi không phải hardline. Lên hardline bằng debug, làm hết focus, rồi đối chiếu `VIE_rp` cuối với bảng ND mục 3.2 (khoảng 82 nếu không xả van).
- Đối chiếu bốn trục hiển thị với ND mục 3.3 (B khoảng −3, C khoảng −2,6).

---

## Giai đoạn 4. Event phản ứng `vie_hl.2` đến `vie_hl.8`

Tất cả `is_triggered_only = yes`, gọi từ `VIE_hl_monthly`, theo mẫu scheduler hiện có (cờ một lần và `VIE_popup_cd` 45 ngày).

| Event | Gọi trong `VIE_hl_monthly` khi |
|---|---|
| `.2` Thư kiến nghị | `VIE_rp > 30`, có H1, chưa có cờ `VIE_hl_ev2_done` |
| `.3` FDI tạm hoãn | `VIE_rp > 39`, có A4 hoặc A5, chưa có cờ |
| `.4` Cảnh báo EVFTA/CPTPP | Có `VIE_evfta` hoặc `VIE_cptpp_member`, có C1 hoặc C3, chưa có cờ |
| `.5` HNTW giữa nhiệm kỳ | `VIE_rp > 55` lần đầu, hoặc gọi trực tiếp từ E1. Cờ chặn 730 ngày. |
| `.6` Dư luận Biển Đông | `VIE_scs_escalated_trigger`, có D1, chưa có cờ |
| `.7` Khủng hoảng chính danh | `VIE_rp > 79`, không có `VIE_hl_self_reliance_idea`. **Bỏ qua `VIE_popup_cd`** (bắt buộc). |
| `.8` Đánh giá lại | Có cờ `VIE_hl_self_reliance_running` nhưng idea đã hết hạn |

Idea `VIE_hl_self_reliance_idea` (`add_timed_idea`, 730 ngày): `stability_factor = 0.05`, `country_productivity_growth_modifier = -0.04`, `trade_opinion_factor = -0.10`, `production_speed_industrial_complex_factor = 0.10`. Khi idea này đang chạy, `VIE_hl_add_pressure` kẹp `VIE_rp` tối đa 80.

### Kiểm tra giai đoạn 4

- Debug đặt `VIE_rp` = 85: `.7` bắn trong vòng 1 tháng. Chọn "kiên trì" thì idea chạy. Rút ngắn thời hạn để test: `.8` bắn khi idea hết.
- Mỗi event có ít nhất một lựa chọn không phạt nặng (ND mục 5: không bế tắc).

---

## Giai đoạn 5. Sửa cây cũ

| Focus | Dòng | Sửa |
|---|---|---|
| `VIE_private_champions` | [2493](common/national_focus/VIE_md_focus.txt#L2493) | `available`: thêm `NOT = { has_completed_focus = VIE_hl_no_party_business }` |
| `VIE_private_sector_engine` | [7601](common/national_focus/VIE_md_focus.txt#L7601) | Như trên |
| `VIE_soe_rapid_divestment` | [7487](common/national_focus/VIE_md_focus.txt#L7487) | `available`: thêm `NOT = { has_completed_focus = VIE_hl_state_sector_leading }` |
| `VIE_investment_grade` | [5583](common/national_focus/VIE_md_focus.txt#L5583) | `available`: thêm `NOT = { has_completed_focus = VIE_hl_party_state_fusion }`. Thưởng: thêm khối van xả (bên dưới). |
| `VIE_international_financial_centre` | [5557](common/national_focus/VIE_md_focus.txt#L5557) | Như trên |
| `VIE_evfta` | [2565](common/national_focus/VIE_md_focus.txt#L2565) | Thêm khối van xả |
| `VIE_cptpp_member` | [2529](common/national_focus/VIE_md_focus.txt#L2529) | Thêm khối van xả |

Khối van xả (nên thành effect `VIE_hl_integration_valve`):

```
if = {
	limit = { VIE_hl_in_power = yes }
	set_temp_variable = { VIE_rp_add = -4 }
	VIE_hl_add_pressure = yes
	if = {
		limit = { NOT = { has_completed_focus = VIE_hl_steadfast_renewal } }
		set_temp_variable = { temp_opinion = -2 }
		change_communist_cadres_opinion = yes
		VIE_bop_reform_small = yes
	}
}
```

H1 giảm áp lực nếu đã làm `VIE_clean_cadres`. H3 thêm phạt nếu đã làm `VIE_decentralization`. B4 rẽ nhánh theo `VIE_military_enterprises_core` / `_divest` ([10230](common/national_focus/VIE_md_focus.txt#L10230), [10263](common/national_focus/VIE_md_focus.txt#L10263)). Ba việc này viết trong chính focus hardline, không sửa focus cũ.

### Kiểm tra giai đoạn 5

- Không phải hardline: bốn focus hội nhập cho đúng thưởng như cũ (hồi quy).
- Hardline: `VIE_rp` −4 mỗi focus hội nhập.

---

## Giai đoạn 6. Loc, icon, hoàn thiện

- `VIE_md_hardline_l_english.yml`: khoảng 25 focus × 2 key, 8 event (khoảng 40 key), 16 idea × 2 key, tooltip và decision. Tổng khoảng 170 key.
- Loc các option mới trong `vie_pol.*` thêm vào file loc hiện có của từng event.
- `python tools/verify_all_loc.py`: không thiếu key.
- Icon focus và ảnh event: làm sau bằng các script `tools/build_*` hiện có, nếu muốn icon riêng.
- `python tools/check_static.py` lần cuối.

## Ước lượng khối lượng

| Giai đoạn | Dòng code (ước tính) |
|---|---|
| 1. Nền tảng | khoảng 200 |
| 2. Lên nắm quyền | khoảng 200 (phần lớn là sửa file cũ) |
| 3. Cây focus | khoảng 1.000 |
| 4. Event | khoảng 400 |
| 5. Sửa cây cũ | khoảng 60 |
| 6. Loc | khoảng 170 key |

## Rủi ro đã biết

| Rủi ro | Cách xử lý |
|---|---|
| `gen_ev6.py` sinh lại `VIE_md_p10.txt` và xóa thay đổi | Script không còn trong repo; header file đã ghi "bảo trì bằng tay". Nếu bạn còn bản ở máy khác thì không chạy lại. |
| `VIE_transition_regime` đặt BoP về 0 | `VIE_hl_take_power` đặt lại −0,5 ngay sau đó. |
| Event lịch sử dựng lại lãnh đạo thật dưới hardline | Xóa cờ lịch sử trong `VIE_hl_take_power` và chặn option (mục 2.2). |
| Hardline đẩy B xuống, mở `sec_cyber_control` | Không còn chuyển đảng khi đang là đảng 4 (mục 2.6). |
| Thứ tự nạp scripted effect | Effect không có tham số nên không bị ràng buộc thứ tự. Nếu sau này thêm effect có tham số thì phải đặt trước nơi gọi, theo ghi chú trong `VIE_md_effects_axis.txt`. |
| Tên modifier sai | `check_static.py` đối chiếu với MD. |

---

## Phụ lục: Bản nháp nội dung v1 (Lịch sử)

# **Con đường Kiên định** 

Nội dung cây focus giả định khi CPV Hardline đã nắm quyền 

Tài liệu nội dung, chưa code. Dành cho submod Vietnam MD. Bản nháp 04/10/2026. 

## **0. Tóm tắt thiết kế** 

Cây này chỉ mở khi đảng cầm quyền là CPV Hardline. Người chơi không "leo thang" trong cây để lên nắm quyền; việc lên nắm quyền xảy ra ngoài cây, qua event. Cây là phần cai trị sau đó: **25 focus** , chia thành một gốc, ba focus củng cố, bốn trụ cai trị, một focus tổng kết và ba kết cục loại trừ nhau. 

Ba nguyên tắc để nhánh này không biến thành "con đường xấu" hoặc "con đường thắng": 

- **Mỗi lần siết đều có phản ứng.** Một thước đo riêng, **Áp lực cải cách** , tăng theo mức độ siết. Càng siết, event phản ứng càng nặng. 

- **Có van xả có chủ đích.** Một số focus (đối ngoại có chọn lọc, kết cục điều chỉnh) giảm áp lực, đổi lại làm cán bộ bảo thủ bất mãn. 

- **Hardline khác nhánh an ninh.** Quyền lực dựa vào tổ chức Đảng, tư tưởng và chính ủy, không dựa vào giám sát đại trà. Nhánh sec_* hiện có là lớp công an, tách biệt. 

_Các con số (giá, điểm trục, ổn định, ngân sách) là bản nháp theo thang đang dùng trong file hiện tại, cần cân bằng lại khi playtest. Tên trục VIE_ax_* tôi suy ra từ cách dùng trong file, xem mục 9._ 

## **1. Điều kiện mở cây và số phận cây cũ** 

### **1.1 Điều kiện mở** 

- Gốc của cây kiểm tra thẳng: **đảng cầm quyền hiện tại là CPV Hardline** . Không dùng cờ vĩnh viễn. Mất quyền thì cả nhánh đóng ngay, lấy lại quyền thì mở lại; focus đã hoàn thành vẫn giữ. 

- Hiển thị cây cho mọi người chơi Việt Nam nhưng chỉ chọn được khi đủ điều kiện, kèm tooltip nói rõ "cần CPV Hardline cầm quyền". 

### **1.2 Số phận cây hiện có khi hardline lên** 

|**Phần cây cũ**|**Xử lý đề xuất**|
|---|---|
|Chuỗi Đại hội và nghị quyết<br>chưa làm|Đóng, tooltip "Đường lối đã đổi". Những focus đã hoàn thành vẫn giữ<br>nguyên hiệu ứng.|
|Cụm Đảng xây dựng (kỷ luật,<br>thanh tra, clean_cadres)|Vẫn mở và được hardline khai thác thêm, vì cùng hướng.|
|Cụm hội nhập (CPTPP,<br>EVFTA, financial centre,<br>investment_grade)|Vẫn làm được nhưng mỗi focus**giảm Áp lực cải cách**và làm cán bộ<br>bảo thủ bất mãn. Đây là van xả tự nhiên.|
|Cụm tư nhân<br>(private_champions,<br>private_sector_engine)|Vẫn mở, nhưng nếu đã làm A5 thì bị khóa. Hai bên loại trừ nhau.|



|**Phần cây cũ**|**Xử lý đề xuất**|
|---|---|
|Cụm kinh tế nhà nước<br>(conglomerates, scic,<br>soe_gradual_restructuring)|Mở, và nhận bonus nhỏ nếu đã làm A1.|
|Cụm quân sự<br>(modernize_vpa,<br>peoples_defence,<br>def_industry)|Giữ nguyên. Là tiền đề cho trụ Quân – Đảng.|



## **2. Đường lên nắm quyền (nằm ngoài cây)** 

Cả ba đường đều gọi chung **một effect chuyển quyền** (VIE_transition_regime hoặc tương đương) và kết thúc bằng event "Nhận quyền" ở mục 2.4. Không có đường nào thất bại ngẫu nhiên rồi bế tắc: nếu có rủi ro thì phải có cửa thử lại. 

### **2.1 Đường A. Đại hội Đảng: phe bảo thủ thắng thế** 

- **Thời điểm:** vào các mốc Đại hội đã có trong file (sched_congress_*). 

- **Điều kiện:** trục BoP bảo thủ đang dẫn và popularity của hardline đủ ngưỡng (đề xuất ≥ 15%, hiện khoảng 9,9% trong ảnh bạn gửi). 

- **Event:** Đại hội chọn đường lối. Hai lựa chọn: "Tiếp tục Đổi mới" (kết quả như hiện nay) hoặc "Giữ vững bản chất, kiên định mục tiêu" (chuyển quyền). 

### **2.2 Đường B. Khủng hoảng và Hội nghị Trung ương bất thường** 

- **Kích hoạt:** một trong ba cú sốc: khủng hoảng ngân hàng hoặc nợ (bankruptcy_incoming_collapse, nợ Vinashin lặp lại), cú sốc thuế quan Mỹ khi trục phương Tây đang cao, hoặc khủng hoảng Biển Đông kéo dài. 

- **Event:** Hội nghị Trung ương đánh giá nguyên nhân. Hai phe tranh luận; người chơi chọn "đổ lỗi cho cải cách quá nhanh" (chuyển quyền) hoặc "điều chỉnh trong khuôn khổ cũ". 

### **2.3 Đường C. Từ nhánh an ninh (chờ xác nhận)** 

- Chỉ giữ nếu xác nhận index mà sec_cyber_control chuyển sang đúng là CPV Hardline. Nếu không, bỏ đường này để tránh nhập nhằng với Security State. 

### **2.4 Event "Nhận quyền"** 

- Đặt Áp lực cải cách về **20** . 

- Áp dụng quy tắc cây cũ ở mục 1.2. 

- Cộng popularity hardline cho khớp trạng thái đã cầm quyền, tránh quay lại ngay do bầu cử hoặc nội bộ. 

- Báo cho người chơi rõ: cây "Con đường Kiên định" đã mở. 

## **3. Cơ chế riêng: Áp lực cải cách** 

Thước đo 0–100, ẩn hoặc hiện tùy ý, đây là **biến duy nhất** nhánh này cần thêm. 

|**Mức**|**Khoảng**|**Hệ quả**|
|---|---|---|
|Ổn định|0 – 30|Không có hệ quả xấu. Một số focus củng cố đạt hiệu quả đầy<br>đủ.|
|Âm ỉ|31 – 60|Mở event phản ứng nhẹ (thư kiến nghị, doanh nghiệp rút vốn).<br>Chưa có phạt định kỳ.|
|Căng thẳng|61 – 85|Phạt ổn định nhẹ liên tục. Mở Hội nghị Trung ương bất thường.<br>Mở kết cục Khép cửa.|
|Khủng hoảng|86 – 100|Phạt tăng trưởng và ổn định. Bắt buộc event khủng hoảng, mở<br>lối thoát về điều chỉnh.|



- **Tăng:** hầu hết focus siết (xem từng focus). Một số event cũng làm tăng. 

- **Giảm:** focus mở có chọn lọc (D3, kết cục điều chỉnh), các focus hội nhập cũ, và tự giảm chậm theo thời gian khi không hoàn thành focus siết mới. 

- **Tổng ước tính:** nếu làm hết các focus siết, áp lực chạm khoảng 70–80 (đã tính van D3). Đủ để buộc người chơi chọn giữa giảm tốc và chịu khủng hoảng, mà chưa thành "chắc chắn sụp". 

## **4. Danh sách focus** 

_Ghi chú đọc: "trục" là các biến VIE_ax_* (dấu + hoặc − so với trạng thái hiện tại). "Áp lực" là Áp lực cải cách. Mọi focus tốn kém đều có guard bankruptcy_incoming_collapse giống file hiện tại._ 

## **4.1 Gốc và củng cố** 

### **H0. Thống nhất ý chí và hành động** 

Giá: 5 tuần 

**Mô tả:** Hội nghị Trung ương khẳng định "giữ vững bản chất cách mạng của Đảng". Đây là điểm mở đầu của nhiệm kỳ cai trị mới. 

**Điều kiện:** Đảng cầm quyền là CPV Hardline. 

**Thưởng:** +50 PP. Đặt Áp lực cải cách về 20 (nếu chưa). BoP bảo thủ +nhẹ. Đặt cờ cây đã mở. 

**Giá:** Không. 

### **H1. Chỉnh đốn Đảng, thanh lọc hàng ngũ** 

Giá: 7 tuần 

**Mô tả:** Tinh thần Nghị quyết TW4 khóa XII: ngăn chặn suy thoái tư tưởng, "tự diễn biến, tự chuyển hóa". Kỷ luật những cán bộ bị coi là thân cải cách hoặc nghiêng về phương Tây. **Điều kiện:** H0. 

**Thưởng:** Trục ax_merit +2, ax_checks −1. Ổn định +0.03. Giảm tham nhũng một nấc. Cán bộ cộng sản +3. 

**Giá:** Áp lực +5. Tập đoàn công nghiệp −4. Gắn ý "thận trọng trong bộ máy" 365 ngày (dùng lại ý VIE_official_caution). 

### **H2. Củng cố nền tảng tư tưởng** 

Giá: 7 tuần 

**Mô tả:** Ban Tuyên giáo và hệ thống Học viện được giao thêm nguồn lực. Mục tiêu: giữ định hướng tư tưởng trong báo chí, giáo dục và đoàn thể (tinh thần Nghị quyết 35). **Điều kiện:** H0. 

**Thưởng:** +50 PP, ổn định +0.02. Trục ax_civil −1. Ý "Công tác tư tưởng" (ổn định nhẹ, giảm tác dụng chiến dịch tuyên truyền thân phương Tây nếu cơ chế cho phép). 

**Giá:** Áp lực +5. Trục ax_integ −1. 

### **H3. Thống nhất quản lý cán bộ** 

Giá: 7 tuần 

**Mô tả:** Cán bộ chủ chốt do Trung ương quản chặt hơn, giảm quyền tự quyết của địa phương. 

**Điều kiện:** H1. 

**Thưởng:** Trục ax_decent −2 (tập quyền), ax_merit +1. BoP bảo thủ nhỏ. 

**Giá:** Áp lực +4. Nếu đã làm decentralization hoặc streamline_apparatus: mất bonus của chúng một phần. 

## **4.2 Trụ A. Kinh tế** 

### **A1. Kinh tế nhà nước giữ vai trò chủ đạo** 

Giá: 7 tuần 

**Mô tả:** Khẳng định lại thành phần kinh tế nhà nước là then chốt, đặt lại ưu tiên cho các tập đoàn và tổng công ty. 

**Điều kiện:** H1. 

**Thưởng:** Trục ax_market −3. Ngân sách +2. Ý "Chủ đạo nhà nước". Cán bộ cộng sản +4. Bonus nhỏ cho state_conglomerates nếu đã làm. 

**Giá:** Áp lực +4. Tăng trưởng giảm nhẹ (ý có thời hạn). Tập đoàn công nghiệp −4. 

### **A2. Danh mục ngành then chốt** 

Giá: 7 tuần 

**Mô tả:** Xác định rõ các ngành không nhượng: năng lượng, ngân hàng, viễn thông, quốc phòng. 

**Điều kiện:** A1. 

**Thưởng:** Xây nhà máy công nghiệp ở một đến hai vùng (dùng one_state_industrial_complex). Trục ax_market −1. 

**Giá:** Áp lực +2. Guard staff và bankruptcy như các focus xây nhà máy hiện có. 

### **A3. Tập đoàn nhà nước làm đầu tàu** 

Giá: 7 tuần 

**Mô tả:** Giao các tập đoàn nhiệm vụ dẫn dắt dự án lớn: hạ tầng, năng lượng, đóng tàu. **Điều kiện:** A1. 

**Thưởng:** Một lần tăng trưởng. Ý "Tập đoàn đầu tàu" (xây dựng nhanh hơn, nhẹ). **Giá:** Áp lực +3. Rủi ro Vinashin +2 (dùng lại biến VIE_vinashin_risk): nhắc lại tiền lệ. 

### **A4. Kiểm soát dòng vốn và FDI có chọn lọc** 

Giá: 7 tuần 

**Mô tả:** FDI vẫn được chào đón nhưng theo danh mục ưu tiên; giám sát chặt dòng vốn và chuyển giá. 

**Điều kiện:** A2. 

**Thưởng:** Ổn định +0.01. +25 PP. Giảm phụ thuộc vào các nhà đầu tư nước ngoài lớn. 

**Giá:** Áp lực +5. Ngân sách −2. Ý "FDI chững lại" 365 ngày. Thiện cảm Mỹ, Nhật, Hàn giảm nhẹ (bọc guard country_exists). 

### **A5. Đảng viên không làm kinh tế tư nhân** 

Giá: 7 tuần 

**Mô tả:** Đảo ngược tinh thần party_members_private_business: cấm đảng viên giữ chức vụ đồng thời kinh doanh tư nhân. 

**Điều kiện:** H1. Loại trừ với private_champions và private_sector_engine. 

**Thưởng:** Trục ax_merit +1, ax_market −1. BoP bảo thủ nhỏ. Cán bộ cộng sản +3. 

**Giá:** Áp lực +4. Tập đoàn công nghiệp −5. 

### **A6. Kế hoạch 5 năm phiên bản mới** 

Giá: 7 tuần 

**Mô tả:** Quay lại tư duy kế hoạch định hướng: mục tiêu sản lượng, tỷ trọng và danh mục dự án quốc gia theo nhiệm kỳ. 

**Điều kiện:** A3 và A4. 

**Thưởng:** Trục ax_mob +1, ax_market −1. Ngân sách +3. Ý "Kế hoạch định hướng". **Giá:** Áp lực +3. Trục ax_size +1 (bộ máy phình ra). 

## **4.3 Trụ B. Quân – Đảng** 

### **B1. Đảng lãnh đạo tuyệt đối, trực tiếp trong quân đội** 

Giá: 7 tuần 

**Mô tả:** Nguyên tắc hiện hành của Quân đội nhân dân được nhấn mạnh trở lại, thông qua Tổng cục Chính trị và hệ thống chính ủy. 

**Điều kiện:** H0 và đã hoàn thành modernize_vpa. 

**Thưởng:** Quân đội +3 (opinion). Trục ax_mob +1. BoP bảo thủ nhỏ. Ý "Công tác Đảng, công tác chính trị trong quân đội". Mastery hoặc XP lục quân 10. 

**Giá:** Áp lực +2. Trục ax_civil −1. 

### **B2. Giáo dục chính trị trong lực lượng vũ trang** 

Giá: 5 tuần 

**Mô tả:** Chương trình huấn luyện chính trị bắt buộc, gắn với đánh giá cán bộ chỉ huy. **Điều kiện:** B1. 

**Thưởng:** War support +0.03. Ổn định +0.01. XP lục quân 10. 

**Giá:** Áp lực +1. Ngân sách −1. 

### **B3. Phòng thủ toàn dân gắn với Đảng cơ sở** 

Giá: 7 tuần 

**Mô tả:** Mở rộng thế trận quốc phòng toàn dân, đặt tổ chức Đảng ở cấp cơ sở làm trục tổ chức lực lượng. 

**Điều kiện:** B1 và đã hoàn thành peoples_defence. 

**Thưởng:** Trục ax_mob +2, ax_decent −1. Nhân lực +. Ý "Thế trận toàn dân kiểu hardline". **Giá:** Áp lực +3. Trục ax_civil −1. 

### **B4. Công nghiệp quốc phòng do Đảng chỉ đạo** 

Giá: 7 tuần 

**Mô tả:** Gắn công nghiệp quốc phòng với kế hoạch nhà nước và kiểm soát chính trị chặt hơn. **Điều kiện:** B1 và (đã chọn military_enterprises_core, hoặc chưa chọn divest). 

**Thưởng:** Cộng 1 cấp VIE_def_industry_level (dùng lại effect có sẵn). Ổn định +0.01. 

**Giá:** Áp lực +2. Trục ax_market −1. 

## **4.4 Trụ C. Xã hội và thông tin** 

### **C1. Bảo vệ nền tảng tư tưởng trên không gian mạng** 

Giá: 7 tuần 

**Mô tả:** Kiểm soát nội dung "sai trái, thù địch" trên mạng và nền tảng xuyên biên giới. Khác nhánh an ninh: mục tiêu là nội dung và tuyên truyền, không phải giám sát hàng loạt. **Điều kiện:** H2. 

**Thưởng:** Trục ax_civil −2, ax_west −1. Ý "Quản lý nội dung mạng". Giảm tác động của các chiến dịch tuyên truyền thân phương Tây nếu cơ chế cho phép. 

**Giá:** Áp lực +6. Trục ax_integ −1. 

### **C2. Giáo dục lý luận chính trị trong nhà trường** 

Giá: 7 tuần 

**Mô tả:** Tăng thời lượng và vị thế các môn lý luận chính trị ở các bậc học. 

**Điều kiện:** H2. 

**Thưởng:** Ổn định +0.02. Ý "Giáo dục lý luận". Tăng nhẹ hỗ trợ của cán bộ. 

**Giá:** Áp lực +4. Nếu đã làm education_law_2019 hoặc higher_education_law: giảm một phần bonus nghiên cứu của chúng. 

### **C3. Quản lý báo chí và xuất bản** 

Giá: 5 tuần 

**Mô tả:** Hệ thống báo chí được rà soát lại về định hướng và quản lý thông tin. **Điều kiện:** C1. 

**Thưởng:** +25 PP. Trục ax_checks −1, ax_civil −1. 

**Giá:** Áp lực +4. Thiện cảm các nước dân chủ giảm nhẹ. 

### **C4. Phát huy Mặt trận Tổ quốc và các đoàn thể** 

Giá: 7 tuần 

**Mô tả:** Dùng Mặt trận Tổ quốc, Công đoàn, Hội Nông dân và Đoàn Thanh niên làm kênh tập hợp và phản biện trong khuôn khổ. 

#### **Điều kiện:** H3. 

**Thưởng:** Trục ax_mob +2. Nông dân +4. Ổn định +0.02. 

**Giá:** Trục ax_size +1. (Không tăng Áp lực: đây là van mềm.) 

## **4.5 Trụ D. Đối ngoại** 

_Ở v14 bạn đã gỡ các focus "chọn phe" (socialist_bloc, join_bri, pivot_to_the_west...). Trụ này cố ý không chọn phe: chỉ là ngoại giao giữa các đảng và một van mở có chọn lọc._ 

### **D1. Ngoại giao Đảng** 

Giá: 7 tuần 

**Mô tả:** Tăng cường kênh quan hệ giữa các đảng cộng sản và đảng cầm quyền ở Lào, Trung Quốc, Cuba, bên cạnh ngoại giao nhà nước. 

**Điều kiện:** H0. 

**Thưởng:** +50 PP. Thiện cảm Lào và Trung Quốc +nhẹ (dùng lại modifier có sẵn). Trục ax_integ −1. 

**Giá:** Áp lực +2. Thiện cảm Mỹ, Nhật giảm nhẹ. 

### **D2. Hợp tác nhưng không lệ thuộc** 

Giá: 7 tuần 

**Mô tả:** Đảng khẳng định hợp tác ý thức hệ không thay thế lợi ích chủ quyền. Đây là focus điều tiết căng thẳng nội tại của hardline: gần Bắc Kinh về tư tưởng, nhưng không nhường ở Biển Đông. 

**Điều kiện:** D1. 

**Thưởng:** War support +0.03. Giảm căng thẳng Biển Đông một nấc. Ổn định +0.01. Gắn cờ để event "phản ứng dân tộc chủ nghĩa" có lựa chọn. 

**Giá:** Không tăng Áp lực. Thiện cảm Trung Quốc giảm nhẹ so với D1. 

### **D3. Đối tác chiến lược có chọn lọc** 

Giá: 7 tuần 

**Mô tả:** Duy trì quan hệ với Nhật Bản, Ấn Độ, Hàn Quốc trên cơ sở "ba không" hoặc "bốn không": hợp tác kinh tế và an ninh, không liên minh quân sự. 

**Điều kiện:** D1, và đã có ít nhất một trong japan_partnership, india_partnership, korea_partnership. 

**Thưởng: Áp lực −8** (van xả). Trục ax_integ +1. Thiện cảm Nhật, Ấn, Hàn +. 

**Giá:** Cán bộ cộng sản −2. 

## **4.6 Tổng kết nhiệm kỳ** 

### **E1. Tổng kết và định hướng nhiệm kỳ mới** 

Giá: 7 tuần 

**Mô tả:** Hội nghị Trung ương tổng kết kết quả củng cố, đặt ra hướng đi cho các năm tiếp theo. Điểm hội tụ trước ngã ba cuối. 

**Điều kiện:** Đã hoàn thành đủ **ba trong bốn trụ** : A6, B3 hoặc B4, C4, D2. 

**Thưởng:** +100 PP, ổn định +0.03. Ý "Mô hình cai trị kiên định". Mở ba focus kết cục. 

**Giá:** Không. Kích hoạt event Hội nghị Trung ương bất thường (mục 5, sự kiện 4). 

## **4.7 Ba kết cục (chọn một)** 

### **X1. Kiên định có điều chỉnh** 

Giá: 7 tuần 

**Mô tả:** Giữ vững mục tiêu nhưng điều chỉnh phương thức: nhà nước giữ then chốt, kinh tế tư nhân và hội nhập tiếp tục trong khuôn khổ kiểm soát. 

**Điều kiện:** E1. Áp lực dưới 85. 

**Thưởng:** Áp lực về 30. Trục ax_market +1, ax_integ +1. Tăng trưởng nhẹ. Mở lại các focus hội nhập cũ không bị phạt. Ý "Kiên định, đổi mới có kiểm soát". 

**Giá:** Cán bộ cộng sản −3. BoP bảo thủ −nhẹ. 

### **X2. Đảng hóa toàn diện** 

Giá: 7 tuần 

**Mô tả:** Hợp nhất lãnh đạo Đảng và quản lý nhà nước ở mọi cấp, giảm không gian độc lập của các thiết chế khác. 

**Điều kiện:** E1, đã hoàn thành ít nhất ba trụ, trục ax_civil ≤ −3 và ax_checks ≤ −2. 

**Thưởng:** +150 PP. Ổn định +0.05. Trục ax_checks −2, ax_decent −2. Ý "Nhất thể hóa Đảng và Nhà nước". 

**Giá:** Áp lực +10. Trục ax_integ −2, ax_market −2. Khóa investment_grade và international_financial_centre. Phạt tăng trưởng. 

### **X3. Khép cửa** 

Giá: 7 tuần 

**Mô tả:** Thu hẹp quan hệ với bên ngoài, ưu tiên tự cung tự cấp và an ninh chế độ. Không phải con đường mong muốn; được mở như hệ quả của việc siết quá đà. 

**Điều kiện:** E1. **Áp lực ≥ 70** hoặc ASEAN/phương Tây đã phản ứng mạnh (qua event). 

**Thưởng:** Ổn định +0.06. Ý "Tự lực tự cường" (giảm phụ thuộc nhập khẩu, tăng xây dựng nhà máy nội địa). 

**Giá:** Trục ax_integ −3, ax_west −3. Thiện cảm ASEAN và phương Tây giảm. Phạt tăng trưởng nặng. Kích hoạt event lối thoát sau khoảng hai năm: "Hội nghị Trung ương đánh giá lại", cho phép chuyển về hiệu ứng của X1 (mất một phần thưởng). 

_AI: mặc định đã là hardline thì base 60–80 cho các focus củng cố và trụ. Kết cục X2 và X3: factor 0 nếu VIE_ai_historical = yes, để AI theo lịch sử không đi hướng cực đoan._ 

## **5. Sự kiện phản ứng** 

|**#**|**Sự kiện**|**Kích hoạt**|**Lựa chọn chính**|
|---|---|---|---|
|1|Thư kiến nghị của các cựu<br>cán bộ|Áp lực ≥ 30, đã làm H1|Tiếp thu: áp lực −10, ổn định −. Bác bỏ:<br>áp lực +5, ổn định +0.01.|
|2|Doanh nghiệp tư nhân rút<br>vốn|Áp lực ≥ 40, đã làm A5<br>hoặc A4|Trấn an: ngân sách −2, trục ax_market<br>+1. Mặc kệ: tăng trưởng giảm.|
|3|Cảnh báo lao động và<br>thương mại từ<br>EVFTA/CPTPP|Đã có evfta hoặc<br>cptpp_member, đã làm<br>C1 hoặc C3|Điều chỉnh: áp lực −5. Chấp nhận áp<br>lực: thiện cảm EU/Nhật giảm.|



|**#**|**Sự kiện**|**Kích hoạt**|**Lựa chọn chính**|
|---|---|---|---|
|4|Hội nghị Trung ương bất<br>thường|Hoàn thành E1, hoặc<br>áp lực ≥ 61|Ba phe: giữ nguyên, nới nhẹ, siết thêm.<br>Dẫn tới các focus X1, X2, X3.|
|5|Phản ứng dân tộc chủ<br>nghĩa về Biển Đông|Căng thẳng Biển Đông<br>cao, đã làm D1|Có D2: có lựa chọn cứng rắn. Không có<br>D2: ổn định −0.02, áp lực +5.|
|6|Khủng hoảng tăng trưởng|Áp lực ≥ 86|Bắt buộc chọn: về hướng X1 (áp lực<br>−20) hoặc kiên trì (ổn định −0.04, mở<br>X3).|



_Mọi sự kiện đều có lựa chọn và không có lựa chọn nào dẫn tới bế tắc. Sự kiện 4 có thể chỉ xuất hiện một lần._ 

## **6. Ba kết cục tóm tắt** 

|**Kết cục**|**Được**|**Mất**|
|---|---|---|
|X1 Kiên định có điều<br>chỉnh|Ổn định cao, hội nhập tiếp tục<br>trong khuôn khổ, áp lực về mức<br>thấp.|Cán bộ bảo thủ bất mãn, hiệu quả<br>hardline giảm.|
|X2 Đảng hóa toàn diện|PP và ổn định cao nhất, kiểm soát<br>chặt.|Cô lập, tăng trưởng thấp, khóa các<br>hướng tài chính.|
|X3 Khép cửa|Ổn định ngắn hạn, tự lực.|Đứt gãy ASEAN và phương Tây, tăng<br>trưởng thấp; có lối thoát nhưng mất<br>thưởng.|



## **7. Đối chiếu với cây hiện có** 

|**Focus hiện có**|**Quan hệ**|
|---|---|
|party_discipline,<br>cadre_accountability,<br>clean_cadres|Bổ sung cho H1. Có thể cho bonus nhỏ nếu đã làm trước.|
|military_enterprises_core /<br>divest|B4 chỉ mở khi chưa chọn divest.|
|peoples_defence,<br>provincial_defence_zones|Tiền đề cho B3.|
|sec_cyber_control và các sec_*|Tách biệt với C1: sec_* là lớp công an, C1 là lớp nội dung. Nếu bạn<br>muốn gộp, nên bàn lại.|
|party_members_private_busine<br>ss, private_champions,<br>private_sector_engine|Loại trừ với A5.|
|state_conglomerates, scic,<br>soe_gradual_restructuring|Nhận bonus nhỏ từ A1.|
|evfta, cptpp_member,<br>investment_grade,<br>international_financial_centre|Giảm áp lực khi hoàn thành. X2 khóa hai focus cuối.|



|**Focus hiện có**|**Quan hệ**|
|---|---|
|four_nos_doctrine,|Nền cho D2 và D3. Không tạo thêm focus chọn phe.|
|bamboo_diplomacy,||
|indochina_solidarity||



## **8. Bố cục tham khảo (khi sang bước code)** 

- Đặt khối mới ở vùng trống bên trái khối chính trị, khoảng x −85 đến −80 và y 8 đến 18, khai báo sau các anchor mà nó dựa vào để tránh forward-ref. 

- Bố cục theo trục dọc: H0 ở trên cùng, H1–H3 ở hàng thứ hai, bốn trụ chạy song song theo bốn cột, E1 hội tụ ở dưới, ba kết cục xếp ngang dưới cùng. 

- Dùng search_filters hiện có (POLITICAL, STABILITY, ECONOMY, ARMY) để không cần thêm filter mới. 

## **9. Điều cần xác nhận trước khi code** 

- **Index của CPV Hardline.** Tài liệu MD ghi index 7 là Autocracy (Emerging). Cần xem file định nghĩa party để biết gốc kiểm tra theo đảng nào. 

- **VIE_party_rule_active** phản ứng thế nào khi hardline lên. Cờ này nằm trong bypass của chuỗi Đại hội. 

- **VIE_transition_regime** còn đổi gì ngoài ruling_party (tên chính phủ, ý quốc gia, cờ). 

- **Tên trục VIE_ax_*.** Tôi suy ra: checks (kiểm soát quyền lực), merit (liêm chính, thực tài), market (thị trường), integ (hội nhập), west (hướng phương Tây), civil (tự do dân sự), mob (huy động), decent (phân quyền), size (quy mô bộ máy). Cần đối chiếu với file loc. 

- **Chiến dịch tuyên truyền** (Pro-Western, Emerging, Non-Aligned, Nationalist, Salafi trong ảnh). Chưa biết nó có hook script để H2/C1 chặn hay không. 

- **Cân bằng số liệu.** Toàn bộ điểm trục, giá, ngân sách và Áp lực cải cách ở đây chỉ là đề xuất khởi điểm. 

- **Đường C** (từ nhánh an ninh): giữ hay bỏ.