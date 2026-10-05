# Con đường Kiên định (bản 2)

Nội dung cây focus khi CPV Hardline (Communist-State, `ruling_party = 4`) cầm quyền.
Tài liệu nội dung, chưa code. Bản 2, 04/10/2026. Thay thế bản nháp 1.

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

## 8. Bố cục

Đã đo lưới thật bằng cách cộng dồn `relative_position_id`. Cây hiện có 379 focus, chạy từ x 6 đến 234, y 0 đến 19, chỉ có một gốc (`VIE_doi_moi_continues` ở (80,0)). Không có x âm, nên vị trí "x −85" ở bản 1 là sai.

Cột chính trị của CPV mặc định đã được thiết kế lại (x 4–22, y 1–23: mỗi Đại hội một hàng, các focus "thông qua" ngay dưới, rồi tới Đại hội kế tiếp). Khối Con đường Kiên định vì vậy nằm ở **x 16–29, y 25–32**, ngay dưới cột đó.

Tọa độ tuyệt đối đề xuất. H0 neo vào `VIE_doi_moi_continues` với `x = -57, y = 25` (tuyệt đối (23,25)), các focus khác neo vào H0. Bảng dưới ghi y của bản đầu; cộng thêm 14 để ra y thực tế.

| y | Focus (x) |
|---|---|
| 11 | H0 (23) |
| 12 | H1 (18), B1 (22), H2 (26), D1 (30) |
| 13 | A1 (16), A5 (18), H3 (20), B2 (22), C1 (24), C2 (26), D2 (30) |
| 14 | A2 (16), A3 (18), B3 (22), C3 (24), D3 (30) |
| 15 | A4 (16), B4 (22), C4 (26) |
| 16 | A6 (17) |
| 17 | E1 (23) |
| 18 | X1 (19), X2 (23), X3 (27) |

Cột: trụ A ở x 16–18, trụ B ở x 22, trụ C ở x 24–26, trụ D ở x 30. Khoảng cách ngang tối thiểu là 2, đúng yêu cầu của `tools/check_static.py`. Phải chạy lại script này sau khi code để chắc không đè ô.

`search_filters`: POLITICAL, STABILITY, ECONOMY, ARMY (đã có).

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
