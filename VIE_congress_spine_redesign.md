# Thiết kế lại nhánh chính trị theo chu kỳ Đại hội Đảng (2000–2026)

> Đầu vào: bản tham khảo "Báo cáo thiết kế Political Tree Việt Nam" (Đại hội = xương sống, Focus = định hướng, Decision = thực thi nghị quyết, Event = biến cố trong nhiệm kỳ), báo cáo nghiên cứu 26/9/2026, và code thật trong repo (đo ngày 26/9/2026).
> Thay thế `VIE_political_report_gap_plan.md` ở phần nhánh chính trị. Không đụng dải chế độ giả định (hàng 28–37), khối quốc phòng, và các thân kinh tế/ngoại giao, trừ ba chỗ trùng lặp ghi rõ ở mục 1.3.
>
> Nhãn: **[SỰ KIỆN]** đo được trong code hoặc có văn bản gốc · **[TIỀN ĐỀ KỊCH BẢN]** quyết định thiết kế · **[TRỪU TƯỢNG GAMEPLAY]** đơn giản hóa vì cơ chế game · **[CẦN THỬ]** chưa kiểm chứng trong game

---

## 0. Kết luận

Hướng của bản tham khảo đúng: nhánh chính trị Việt Nam nên là **một biên niên có gameplay**, không phải một cây chọn ý thức hệ. Nhưng code hiện tại đã có sẵn nửa xương sống, và bản tham khảo có một chỗ sẽ gây lỗi nếu làm đúng như viết. Sáu quyết định của báo cáo này:

1. **Đại hội = event + focus, không chỉ focus.** Sáu event Đại hội (`vie_pol.2`–`.8`) đã tồn tại, đúng ngày, và đang mang việc thay Tổng Bí thư cùng các cửa rẽ sang dải chế độ. Đại hội luôn diễn ra đúng lịch; cái người chơi quyết định là **có triển khai nghị quyết hay không**. Vì vậy mỗi mốc trên xương sống là focus **"Nghị quyết Đại hội N"**, chỉ mở khi Đại hội đã họp.
2. **Nhiệm kỳ là một cửa sổ.** Focus nghị quyết của nhiệm kỳ cũ có thể bị bỏ qua (`bypass`) khi Đại hội kế tiếp họp. Người chơi có năm năm để khai thác tinh thần và decision của nhiệm kỳ; bỏ lỡ thì mất phần thưởng nhưng không bị khóa cây.
3. **Cây xếp theo lưới: cột là mạch chính sách, hàng là nhiệm kỳ.** Năm mạch (dân chủ – Quốc hội; xây dựng Đảng; phòng chống tham nhũng; bộ máy – hành chính; pháp quyền – Hiến pháp) chạy dọc qua sáu nhiệm kỳ. Đây là cách bản tham khảo nói "không làm sáu cây riêng", thể hiện bằng tọa độ.
4. **Decision là lớp thực thi, tách khỏi hệ đẩy trục.** Thêm danh mục "Thực hiện Nghị quyết" chỉ hiện khi Đảng cầm quyền, nội dung đổi theo nhiệm kỳ. Danh mục "Xây dựng nhà nước" hiện có giữ nguyên vai trò công cụ đẩy trục cho mọi chế độ.
5. **Tham nhũng là biến quản trị, không phải phần thưởng focus.** Riêng khối chính trị hiện có **11 nấc giảm tham nhũng ròng** trên thang 10 nấc của MD. Chuyển phần lớn sang decision có thời gian chờ và có sàn.
6. **Không tạo chỉ số mới.** "Governance Capacity" và "Administrative Efficiency" của bản tham khảo ánh xạ vào trục `merit`, `size`, `checks` đã có. Không thêm thanh đo (ràng buộc STEP5: VIE đã dùng đủ 3 power balance).

Quy mô: khối chính trị đi từ **31 lên 38 focus**, thêm **19 decision**, **3 event mới**, sửa **9 event cũ**. Tổng hiệu ứng trục của khối gần như giữ nguyên (mục 8.1).

---

## 1. Hiện trạng đo được

### 1.1 Xương sống Đại hội đã có, nhưng "câm"

**[SỰ KIỆN]** Lịch trong `VIE_event_scheduler` và `_p2`:

| Event | Mốc | Ngày kích hoạt | Hiện làm gì |
|---|---|---|---|
| `vie_pol.2` | Đại hội IX | > 2001.3.31 | Thay TBT (Nông Đức Mạnh), BoP, **cửa rẽ bảo thủ** (option b) |
| `vie_pol.3` | Đại hội X | > 2006.3.31 | PP, BoP, cờ `VIE_reform_mandate` (option b) |
| `vie_pol.4` | Đại hội XI | > 2010.12.31 | Thay TBT (Nguyễn Phú Trọng), BoP |
| `vie_pol.5` | Đại hội XII | > 2015.12.31 | **Cửa rẽ lớn nhất**: option b mở nhánh Kiến tạo |
| `vie_pol.6` | Đại hội XIII | > 2020.12.31 | Xác nhận lãnh đạo theo nhánh |
| `vie_pol.7` | HNTW bất thường | > 2024.7.31 | Thay TBT (Tô Lâm) |
| `vie_pol.8` | Đại hội XIV | > 2025.12.31 | Cờ `VIE_congress14_done` |
| `vie_pol.9` | TBT kiêm CTN | > 2026.3.31 | Ngã rẽ lãnh đạo hạt nhân / tập thể |

Ngày đúng lịch sử. Nhưng các event chỉ cho PP và dịch BoP. **Chỉ một focus đọc Đại hội thật** (`era_of_rising` đọc cờ Đại hội XIV). Ba focus khác dùng `VIE_era_2011/2016/2021`, vốn là trigger theo ngày (`date > 2010.12.31`…), nên sau khi rời chế độ Đảng các mốc này vẫn "qua" dù không có Đại hội nào. Không có tinh thần theo nhiệm kỳ, không có decision gắn với nghị quyết.

### 1.2 Khối focus chính trị

**[SỰ KIỆN]** 31 focus ở cột x 20–34, hàng 1–11: 29 focus lịch sử (206 tuần) và 2 focus ngã rẽ 2026. Khối có 3 gốc tự do (`grassroots_democracy`, `anti_corruption_steering`, `rule_of_law_state`), nên thứ tự nhiệm kỳ không được thể hiện: người chơi năm 2001 có thể làm `anti_corruption_steering` (lập năm 2006).

Tổng hiệu ứng của 29 focus lịch sử:

| Trục | size | merit | decent | checks | market | civil | mob |
|---|---|---|---|---|---|---|---|
| Tổng | −12 | +23 | +3 | +10 | +3 | −3 | +1 |

Tham nhũng: **11 nấc giảm ròng** (12 focus giảm, `decentralization` tăng 1). VIE khởi đầu ở `corruption_level_08` (STEP6), nên chỉ riêng khối này đủ đưa về `level_01`. Đây là lỗi cân bằng thật, độc lập với việc thiết kế lại.

Hàng 10–27 ở cột 16–44 **trống**, trừ hai capstone. Xương sống dài hơn đặt được mà không đụng khối khác.

### 1.3 Ba chỗ trùng lặp

| Focus chính trị | Trùng với | Xử lý |
|---|---|---|
| `VIE_resolution_57_68` (> 2025.5.31, market +2) | NQ 57 = `VIE_science_breakthrough` (thân KHCN). NQ 68 = `VIE_private_sector_engine` (thân kinh tế) | **Giữ ID, đổi nội dung thành NQ 66** (đổi mới xây dựng và thi hành pháp luật, 30/4/2025). Đây là nghị quyết thể chế duy nhất của "bộ tứ" chưa có |
| `VIE_constitution_2013` (focus) | Hiến pháp do Quốc hội thông qua ngày 28/11/2013, không chờ người chơi | **Giữ ID, đổi vai trò thành "Thi hành Hiến pháp 2013"** (các luật tổ chức bộ máy 2014–2015). Việc thông qua trở thành event mới |
| `VIE_merge_ministries`, `VIE_provincial_merger`, `VIE_two_tier_local_gov` | Ba focus khóa ngày nằm gọn trong 7 tháng (2024.12.31 → 2025.6.30), cùng lúc `vie_pol.16`/`.17` | **Chuyển thành chuỗi decision** xen với hai event đã có (mục 6.4) |

### 1.4 Event bản tham khảo yêu cầu: đã có và còn thiếu

| Bản tham khảo | Hiện trạng |
|---|---|
| Đại hội IX–XIV, chuyển tiếp 2024 | **Có** (`vie_pol.2`–`.8`) |
| Cải tổ bộ máy 2024–2025 | **Có** (`vie_pol.16` 2024.11, `vie_pol.17` 2025.5) |
| COVID-19 | **Có** (`vie_soc.6`). Không đưa vào nhánh chính trị, đúng khuyến nghị của bản tham khảo |
| Hiến pháp 2013 có hiệu lực | **Thiếu.** Mới có `vie_pol.15` (Kiến nghị 72, đầu 2013) |
| Biến động Chủ tịch nước 2018 | **Thiếu** |
| Bầu cử Quốc hội khóa XVI (15/3/2026) | **Thiếu.** `vie_pol.14` có các lần 2002, 2007, 2011, 2016, 2021 nhưng không có 2026 |
| Cương lĩnh 2011, NQ TW4 khóa XI | **Thiếu** (mới có `vie_pol.11` HNTW6 tháng 10/2012) |

---

## 2. Đánh giá bản tham khảo

| Đề xuất của bản tham khảo | Quyết định | Lý do |
|---|---|---|
| Sáu Đại hội IX–XIV làm xương sống | **Theo** | Đúng nhịp thay đổi đường lối, đúng mẫu hình "chu kỳ Đại hội" của báo cáo nghiên cứu |
| Đại hội là Major Focus | **Sửa: event + focus "Nghị quyết Đại hội N"** | Nếu chỉ là focus, người chơi có thể trì hoãn hoặc không bao giờ bấm, trong khi event Đại hội vẫn thay TBT và mở cửa rẽ theo ngày. Hai thứ lệch nhau. Tách "sự kiện đã xảy ra" (event) khỏi "hành động của chính phủ" (focus) là nguyên tắc đã dùng suốt mod |
| Congress Spirit mỗi nhiệm kỳ | **Theo, thêm biến thể** | Tinh thần do focus nghị quyết trao, bị gỡ khi Đại hội kế tiếp họp. Ở IX và XII, tinh thần có biến thể theo option đã chọn trong event Đại hội, nên cửa rẽ có hệ quả thấy được |
| Một danh mục decision "Thực hiện Nghị quyết", đổi nội dung theo nhiệm kỳ | **Theo** | Làm được bằng một biến `VIE_congress_term` |
| Decision có chi phí, thời gian, hiệu ứng muộn | **Theo** | Dùng `days_remove` + `remove_effect` của HOI4. Mod chưa dùng cơ chế này: **[CẦN THỬ]** |
| Hiến pháp 2013 là event, không phải focus | **Theo một nửa** | Việc thông qua là event. Focus cũ giữ ID và đổi thành việc thi hành, để không mất decision đang gắn vào nó và không làm hỏng save |
| Tinh gọn bộ máy dưới Đại hội XII | **Theo** | NQ 18/19 ban hành 25/10/2017, thuộc nhiệm kỳ XII. Code hiện khóa `streamline_apparatus` tới 2021 là sai mốc |
| Cải tổ 2025 là chuỗi decision ↔ event | **Theo** | Mục 6.4 |
| Chỉ số Governance Capacity, Administrative Efficiency | **Không làm** | Ánh xạ: năng lực quản trị → `merit`; hiệu quả hành chính → `size` âm cùng luật bộ máy của MD; kiểm soát quyền lực → `checks` |
| Focus cuối "Ổn định bộ máy nhiệm kỳ mới" | **Không làm** | Không có hiệu ứng riêng. `VIE_era_of_rising` đã đóng vai trò "bước vào giai đoạn phát triển mới"; bầu cử khóa XVI và `vie_pol.9` là hai event khép lại |
| COVID-19 có decision riêng | **Không làm ở nhánh này** | Thuộc thân xã hội (`vie_soc.6`) |
| Tham nhũng là biến, không phải ideology | **Theo** | Mục 7 |

Bổ sung ngoài bản tham khảo:

- **Chế độ không phải Đảng cầm quyền.** Khi `VIE_party_rule_active` sai, focus nghị quyết tự bypass. Các focus chủ đề (cải cách hành chính, kiểm toán, pháp quyền…) vẫn đi được, vì đó là chức năng nhà nước chứ không phải của Đảng. Hiện nay các focus này đi được nhờ gốc tự do; thiết kế mới phải giữ tính chất đó.
- **Catch-up mode.** Khi phe thắng nội chiến tiếp quản dòng VIE, event Đại hội không bắn nhưng scheduler vẫn đặt cờ `VIE_sched_congress_N`. Vì vậy mọi điều kiện của xương sống đọc **cờ scheduler**, không đọc cờ do event đặt.

---

## 3. Kiến trúc

```text
LỚP            VAI TRÒ                              CƠ CHẾ HOI4
─────────────  ───────────────────────────────────  ──────────────────────────────────────────
Scheduler      Đại hội họp đúng lịch                 VIE_sched_congress_N + biến VIE_congress_term
Event          Đại hội; biến cố trong nhiệm kỳ       vie_pol.* (đã có) + 3 event mới
Focus xương    "Nghị quyết Đại hội N"                available: cờ scheduler; bypass: Đại hội N+1 đã họp
  sống                                               hoặc Đảng không cầm quyền; trao tinh thần nhiệm kỳ
Focus chủ đề   Chính sách lớn của nhiệm kỳ           prerequisite: nghị quyết của nhiệm kỳ + focus trước cùng mạch
Tinh thần      Trạng thái chính trị của nhiệm kỳ     1 idea mỗi lúc; bị gỡ ở Đại hội kế tiếp
Decision       Thực thi nghị quyết                   danh mục mới; visible theo VIE_congress_term;
                                                     days_remove = độ trễ thực thi
```

### 3.1 Cờ, biến và trigger mới

| Tên | Loại | Đặt ở đâu | Dùng để |
|---|---|---|---|
| `VIE_congress_term` | biến (8…14) | `vie_pol.1` đặt 8; mỗi khối scheduler Đại hội đặt N, **kể cả catch-up** | Decision hiện theo nhiệm kỳ |
| `VIE_congress_started = { N = 12 }` | scripted trigger có tham số | file trigger mới | `has_country_flag = VIE_sched_congress_$N$` |
| `VIE_start_congress_term = { N = 12 }` | scripted effect có tham số | file effect mới | Đặt biến, gỡ tinh thần nhiệm kỳ trước. Gọi từ khối scheduler |
| `VIE_constitution_2013_adopted` | cờ | event mới `vie_pol.28` | Mở "Thi hành Hiến pháp 2013" |
| `VIE_two_tier_done` | cờ | decision cuối chuỗi 2025 | Thay prerequisite `VIE_two_tier_local_gov` ở ngã rẽ 2026 và `era_of_rising` |

Mod đã dùng scripted effect có tham số (`VIE_boost_party = { PARTY = 20 AMOUNT = 0.15 }`), nên không cần cơ chế mới.

Khối Đại hội XIII, XIV và HNTW 2024 nằm trong `VIE_md_effects_p2.txt`; IX–XII nằm trong `VIE_md_effects.txt`. **`VIE_md_effects_p10.txt` là file sinh tự động** (`gen_ev6.py`, không có trong repo) nên không sửa. Lịch mới (bầu cử khóa XVI) đặt vào scheduler part 13, file mới.

> **Đã code (pha 1 — Nền), có hai điều chỉnh.** (1) `VIE_boost_party` **không có thật trong code** — dòng 129 chỉ là một ví dụ trong comment (`# VIE_boost_party = { PARTY = 20 AMOUNT = 0.15 }`), không phải một scripted effect đang chạy. Cả repo không có scripted effect/trigger tham số nào khác đang hoạt động; `VIE_congress_started`/`VIE_start_congress_term` là **lần đầu** cơ chế `$N$` được dùng thật trong mod, không phải mở rộng một cái đã có. Không đổi cách làm vì cú pháp tham số là tính năng chuẩn của HOI4, chỉ ghi lại để không ai tưởng có tiền lệ. (2) `VIE_start_congress_term` gỡ tinh thần nhiệm kỳ trước bằng 8 khối `if = { limit = { has_idea = X } remove_ideas = X }` (kiểm tra rồi mới gỡ), không gọi `remove_ideas` trần trụi — đúng quy ước 100% các chỗ gỡ idea khác trong `VIE_md_focus.txt` đã làm vậy, dù bản thân `remove_ideas` gỡ một idea không có sẵn vốn là no-op an toàn. Đã nối `VIE_start_congress_term` vào cả 6 khối scheduler (`vie_pol.2/.3/.4/.5/.6/.8`), đặt `VIE_congress_term = 8` trong `vie_pol.1`, và thêm suy lại biến từ cờ `VIE_sched_congress_N` trong `on_startup` cho save cũ (mục 8.3). 8 idea tinh thần + 2 idea của decision (`VIE_no_district_council_idea`, `VIE_pctn_directing_committee_idea`) đã tạo, có loc. Idea `VIE_resolution_12_dev_idea` dùng `production_speed_industrial_complex_factor` thay vì gợi ý gốc — xem mục 5.

---

## 4. Cây focus

### 4.1 Bố cục lưới

Cột 28 là xương sống. Hàng tăng theo thời gian. Mỗi mạch chính sách giữ một cột nên đường nối chủ yếu thẳng đứng.

```text
x:     20        22          24             26             28              30             34
      DT-TG   DÂN CHỦ–QH   XÂY DỰNG ĐẢNG   PCTN          XƯƠNG SỐNG       BỘ MÁY–HC      PHÁP QUYỀN
y1              grassroots  mass_mobiliz.                 ★Chuẩn bị ĐH IX
y2                                                        ■NQ ĐH IX (2001)
y3    ethnic    nat.assembly                state_audit                    public_admin
y4                                          anti_corr_law                  decentralization
y5                                                        ■NQ ĐH X (2006)
y6                          ★đảng viên KTTN  anti_corr_steer.
y7                                          asset_declar.
y8                                                        ■NQ ĐH XI (2011)
y9                          ★NQ TW4 khóa XI               ★Cương lĩnh 2011                  rule_of_law
y10                         party_inspection                                               constitution_2013*
y11                                                       ■NQ ĐH XII (2016)
y12                         party_discipline                               streamline      cybersecurity
y13             cadre_acc.  clean_cadres    asset_recovery
y14                                                       ■NQ ĐH XIII (2021)
y15             peoples_ov.                 digital_anticorr               e_government    NQ 66*
y16                                                                                        inst._bottlenecks
y17                                                       ■NQ ĐH XIV (2026)
y18                                         concentration_of_power         institutional_opening
y19                                                       era_of_rising
y20                                                       party_centennial_2030
```

`■` focus nghị quyết mới · `★` focus chủ đề mới · `*` giữ ID, đổi nội dung · còn lại là focus cũ, dời tọa độ.

`three_breakthroughs` (Chiến lược 2011–2020) được **gộp vào Cương lĩnh 2011**, vì tách riêng chỉ là focus độn.

### 4.2 Xương sống: 7 focus mới

| ID | Tên | Tọa độ | Điều kiện | Bypass | Cost | Phần thưởng |
|---|---|---|---|---|---|---|
| `VIE_prepare_congress_9` | Chuẩn bị Đại hội IX | 28,1 | `has_completed_focus = VIE_doi_moi_continues` | — | 5 | PP +50. Mở hai focus di sản |
| `VIE_resolution_congress_9` | Nghị quyết Đại hội IX | 28,2 | prereq trên; `VIE_congress_started = { N = 9 }` | `OR { NOT Đảng cầm quyền; VIE_congress_started = { N = 10 } }` | 5 | Tinh thần IX |
| `VIE_resolution_congress_10` | Nghị quyết Đại hội X | 28,5 | prereq IX; `N = 10` | `N = 11` hoặc không Đảng | 5 | Tinh thần X |
| `VIE_resolution_congress_11` | Nghị quyết Đại hội XI | 28,8 | prereq X; `N = 11` | `N = 12` hoặc không Đảng | 5 | Tinh thần XI |
| `VIE_resolution_congress_12` | Nghị quyết Đại hội XII | 28,11 | prereq XI; `N = 12` | `N = 13` hoặc không Đảng | 5 | Tinh thần XII (2 biến thể) |
| `VIE_resolution_congress_13` | Nghị quyết Đại hội XIII | 28,14 | prereq XII; `N = 13` | `N = 14` hoặc không Đảng | 5 | Tinh thần XIII |
| `VIE_resolution_congress_14` | Nghị quyết Đại hội XIV | 28,17 | prereq XIII; `N = 14` | `N = 15` hoặc không Đảng | 5 | Tinh thần XIV |

Quy tắc chung **[TIỀN ĐỀ KỊCH BẢN]**:

- Focus xương sống **không cộng trục**. Chúng trao trạng thái (tinh thần) và mở decision. Như vậy hiệu ứng trục đã hiệu chuẩn ở STEP6 không đổi.
- `ai_will_do`: base 50, nhân 4 khi `VIE_ai_historical`. AI lịch sử phải lấy nghị quyết ngay khi Đại hội họp.
- Mod chưa từng dùng `bypass`. Cần kiểm tra trong game rằng focus bị bypass được tính là hoàn thành cho focus con **[CẦN THỬ]**.

### 4.3 Focus chủ đề theo nhiệm kỳ

Cột "Prerequisite mới" luôn gồm focus nghị quyết của nhiệm kỳ. Nghị quyết bị bypass vẫn tính là hoàn thành, nên chế độ không phải Đảng vẫn đi được các mạch.

**Chuyển tiếp 2000 và nhiệm kỳ IX (2001–2006)**

| Focus | Tọa độ | Prerequisite mới | Mốc lịch sử | Thay đổi so với hiện tại |
|---|---|---|---|---|
| `grassroots_democracy` | 22,1 | `prepare_congress_9` | Quy chế dân chủ cơ sở 1998, sau Thái Bình 1997 | Chỉ dời |
| `mass_mobilization` | 24,1 | `prepare_congress_9` | Công tác dân vận | Chỉ dời |
| `national_assembly_role` | 22,3 | NQ IX + `grassroots_democracy` | Quốc hội chất vấn công khai | Chỉ dời |
| `ethnic_policy` | 20,3 | NQ IX | Tây Nguyên 2001/2004, Chương trình 134 | Chỉ dời |
| `state_audit` | 26,3 | NQ IX | Luật Kiểm toán Nhà nước 6/2005 | **Bỏ prereq** `anti_corruption_law` (hai luật độc lập, cùng năm). Bỏ giảm tham nhũng |
| `anti_corruption_law` | 26,4 | NQ IX + `state_audit` | Luật PCTN 29/11/2005 | Giữ `date > 2005.6.30` |
| `public_admin_reform` | 30,3 | NQ IX | Chương trình tổng thể CCHC 2001–2010 | Giữ `date > 2001.12.31` |
| `decentralization` | 30,4 | `public_admin_reform` | NQ 08/2004/NQ-CP về phân cấp | Chỉ dời |

**Nhiệm kỳ X (2006–2011)**

| Focus | Tọa độ | Prerequisite mới | Mốc lịch sử | Thay đổi |
|---|---|---|---|---|
| ★ `VIE_party_members_private_business` — Đảng viên làm kinh tế tư nhân | 24,6 | NQ X | Quy định 15-QĐ/TW (8/2006) | **Mới.** Cost 7. BoP cải cách nhỏ; opinion `communist_cadres` −2 (dùng `change_communist_cadres_opinion` đã có). Không cộng trục |
| `anti_corruption_steering` | 26,6 | NQ X + `anti_corruption_law` | BCĐ TW PCTN do Thủ tướng đứng đầu (8/2006), sau vụ PMU18 | **Đổi từ gốc tự do** thành con của luật 2005. Bỏ giảm tham nhũng |
| `asset_declaration` | 26,7 | `anti_corruption_steering` | NĐ 37/2007 về minh bạch tài sản | Đổi cha. Bỏ giảm tham nhũng |

**Nhiệm kỳ XI (2011–2016)**

| Focus | Tọa độ | Prerequisite mới | Mốc lịch sử | Thay đổi |
|---|---|---|---|---|
| ★ `VIE_platform_2011` — Cương lĩnh 2011 và Chiến lược 2011–2020 | 28,9 | NQ XI | Cương lĩnh bổ sung, phát triển; ba đột phá chiến lược | **Mới.** Cost 7. BoP bảo thủ nhỏ, PP +50. Mở decision CCHC giai đoạn II |
| ★ `VIE_tw4_party_building` — NQ TW4 khóa XI | 24,9 | NQ XI | NQ 12-NQ/TW (1/2012), "một số vấn đề cấp bách về xây dựng Đảng" | **Mới.** Cost 7. BoP bảo thủ nhỏ. Kéo `vie_pol.11` (HNTW6, 10/2012) thành hệ quả |
| `party_inspection` | 24,10 | `tw4_party_building` | Tái lập Ban Nội chính TW; BCĐ PCTN về Bộ Chính trị (2013) | Đổi cha (trước là `party_discipline`). Bỏ giảm tham nhũng |
| `rule_of_law_state` | 34,9 | NQ XI + `national_assembly_role` | Cương lĩnh 2011 về Nhà nước pháp quyền | Bỏ `VIE_era_2011` (NQ XI thay thế) |
| `constitution_2013` → **Thi hành Hiến pháp 2013** | 34,10 | `rule_of_law_state`; available `VIE_constitution_2013_adopted` | Luật Tổ chức Quốc hội, Chính phủ, TAND 2014–2015 | **Đổi nội dung, giữ ID.** Giữ `checks +2`. Decision `VIE_relax_media_scrutiny` vẫn gắn vào |

**Nhiệm kỳ XII (2016–2021)**

| Focus | Tọa độ | Prerequisite mới | Mốc lịch sử | Thay đổi |
|---|---|---|---|---|
| `party_discipline` | 24,12 | NQ XII + `party_inspection` | NQ TW4 khóa XII (10/2016) | Đổi cha (trước là `asset_declaration`). Bỏ `VIE_era_2016`. Tham nhũng −2 → −1 |
| `streamline_apparatus` | 30,12 | NQ XII + `decentralization` | NQ 18, 19 (25/10/2017) | **Sửa mốc:** `VIE_era_2021` → `date > 2017.9.30` |
| `cybersecurity_law` | 34,12 | NQ XII + `constitution_2013` | Luật An ninh mạng 6/2018 (event `vie_pol.10`) | Chỉ dời |
| `cadre_accountability` | 22,13 | `party_discipline` | QĐ 205-QĐ/TW (9/2019) về kiểm soát quyền lực trong công tác cán bộ | Chỉ dời. Bỏ giảm tham nhũng |
| `clean_cadres` | 24,13 | `party_discipline` + `asset_recovery` | NQ 26 TW7 khóa XII (5/2018) về cán bộ cấp chiến lược | Đổi cha (bỏ `party_inspection`). Bỏ giảm tham nhũng |
| `asset_recovery` | 26,13 | `party_discipline` + `state_audit` | Luật PCTN 2018; thu hồi tài sản (event `vie_cor.8`) | Chỉ dời. Bỏ giảm tham nhũng |

**Nhiệm kỳ XIII (2021–2026)**

| Focus | Tọa độ | Prerequisite mới | Mốc lịch sử | Thay đổi |
|---|---|---|---|---|
| `peoples_oversight` | 22,15 | NQ XIII + `national_assembly_role` | Luật Thực hiện dân chủ ở cơ sở (10/11/2022) | Thêm `date > 2022.11.9` |
| `digital_anticorruption` | 26,15 | NQ XIII + `clean_cadres` | Dữ liệu kê khai tài sản, BCĐ cấp tỉnh (2022) | Giữ available `e_government` và `date > 2021.12.31` |
| `e_government` | 30,15 | NQ XIII + `streamline_apparatus` | Đề án 06 (1/2022) | Đổi cha (trước là `public_admin_reform`). Giữ available `national_digital_transformation` |
| `resolution_57_68` → **NQ 66: đổi mới xây dựng và thi hành pháp luật** | 34,15 | NQ XIII + `constitution_2013` | NQ 66-NQ/TW (30/4/2025) | **Đổi nội dung, giữ ID.** `market +2, merit +1` → `checks +1, merit +1`. Mốc `date > 2025.4.29` |
| `institutional_bottlenecks` | 34,16 | `resolution_57_68` | "Một luật sửa nhiều luật" (2025) | Chỉ dời |

Ba focus `merge_ministries`, `provincial_merger`, `two_tier_local_gov` **bị xóa khỏi cây** và chuyển thành chuỗi decision (mục 6.4). Idea của chúng (`VIE_provincial_merger_idea`, `VIE_two_tier_gov_idea`) giữ nguyên ID, được decision trao.

**Nhiệm kỳ XIV (2026–)**

| Focus | Tọa độ | Prerequisite mới | Thay đổi |
|---|---|---|---|
| `concentration_of_power` | 26,18 | NQ XIV + `OR { clean_cadres; e_government }` | Available thay `two_tier_local_gov` bằng `VIE_two_tier_done`. Giữ cờ của `vie_pol.9` và mutex |
| `institutional_opening` | 30,18 | như trên | như trên |
| `era_of_rising` | 28,19 | NQ XIV + một trong hai ngã rẽ | Bỏ prereq `two_tier_local_gov`. Giữ `VIE_fourteenth_congress_held` |
| `party_centennial_2030` | 28,20 | `era_of_rising` | Chỉ dời |

### 4.4 Tổng kết khối focus

| | Hiện tại | Sau thiết kế |
|---|---|---|
| Số focus | 31 | **38** (+7 xương sống, +3 chủ đề, −3 chuyển sang decision) |
| Tổng cost | 226 tuần | **258 tuần**, khoảng 5 năm trên 26 năm lịch sử |
| Focus gốc tự do | 3 | **1** (`prepare_congress_9`) |
| Focus nằm dưới một nghị quyết Đại hội | 1 (`era_of_rising`) | **35**: mọi focus trừ 3 focus chuyển tiếp năm 2000 |
| ID bị xóa | — | 3 |
| ID đổi nội dung | — | 2 |

> **Đã code (pha 3 — Cây), khớp gần như tuyệt đối với văn bản.** Tất cả 38 tọa độ tuyệt đối ở mục 4.2/4.3 đã được cấy đúng từng ô (đã tính lại toàn bộ chuỗi `relative_position_id` và xác nhận 0 va chạm) — hóa ra tọa độ tương đối cũ của cả hai cụm (`anti_corruption_steering` và `doi_moi_continues`) đã được chọn từ đầu rất gần với lưới mục tiêu, nên việc "dời tọa độ 28 focus" chỉ là tính lại offset, không phải rủi ro "tách cột" như đã gặp ở pha B của báo cáo kinh tế. Toàn bộ focus giờ neo thẳng vào `VIE_doi_moi_continues` (bỏ neo trung gian qua `anti_corruption_steering`, vì bản thân nó cũng phải dời sang (26,6)). Giảm tham nhũng: đúng 7 chỗ bị bỏ `decrease_corruption`, `party_discipline` giữ đúng 1 trong 2 lần gọi, ròng đúng **−3** như mục 8.2. Hai chỗ khác so với văn bản: (1) `concentration_of_power`/`institutional_opening` không thể đặt `VIE_two_tier_done` vào `prerequisite` (khối đó chỉ nhận `focus = X`, không nhận cờ) — cờ được chuyển sang `available` như văn bản đã ngụ ý qua chữ "thay". (2) `vie_pol.11` (option c, đọc `has_completed_focus = VIE_tw4_party_building`) đáng lẽ thuộc pha 2 nhưng đã dời sang đây, đúng như đã báo trước.

---

## 5. Tinh thần nhiệm kỳ

**[TIỀN ĐỀ KỊCH BẢN]** Một idea mỗi lúc. Focus nghị quyết trao; `VIE_start_congress_term` gỡ khi Đại hội kế tiếp họp. Hiệu ứng nhỏ: tinh thần để đánh dấu thời kỳ, đổi trọng tâm, và làm điều kiện cho decision. Giá trị dưới đây là điểm xuất phát để cân bằng sau khi chạy thử, chỉ dùng khóa modifier đã có trong idea của mod (`check_static.py` kiểm tra).

| Idea | Trao bởi | Trọng tâm | Modifier gợi ý |
|---|---|---|---|
| `VIE_resolution_9_idea` | NQ IX, `vie_pol.2.a` | Công nghiệp hóa, hiện đại hóa | `political_power_factor +0.05`, `production_speed_industrial_complex_factor +0.05` |
| `VIE_resolution_9_cons_idea` | NQ IX, `vie_pol.2.b` | Ổn định trước | `stability_factor +0.05`, `political_power_factor −0.05` |
| `VIE_resolution_10_idea` | NQ X | Đẩy mạnh toàn diện Đổi Mới, hội nhập | `political_power_factor +0.05`, `consumer_goods_factor −0.02` |
| `VIE_resolution_11_idea` | NQ XI | Đổi mới phương thức lãnh đạo, ba đột phá | `stability_factor +0.03`, `research_speed_factor +0.02` |
| `VIE_resolution_12_idea` | NQ XII, `vie_pol.5.a` | Xây dựng, chỉnh đốn Đảng | `stability_factor +0.05`; **cái giá** `political_power_factor −0.05` (cán bộ e ngại, xem `vie_pol.21`) |
| `VIE_resolution_12_dev_idea` | NQ XII, `vie_pol.5.b` | Chính phủ kiến tạo | ~~`production_speed_buildings_factor +0.05`~~ → `production_speed_industrial_complex_factor +0.05` (đã code, mục không có thật — xem chú thích pha 1 ở mục 3.1); **cái giá** `stability_factor −0.03` |
| `VIE_resolution_13_idea` | NQ XIII | Tinh gọn, chuyển đổi số | `political_power_factor +0.05`, `research_speed_factor +0.02` |
| `VIE_resolution_14_idea` | NQ XIV | Hoàn thiện thể chế, giai đoạn phát triển mới | `political_power_factor +0.05`, `stability_factor +0.03` |

Biến thể được chọn bằng cờ event đã có: `VIE_congress9_phieu` (IX) và `VIE_developmental_unlocked` (XII). Không cần cờ mới.

Theo `VIE_economic_branch_redesign.md`, dải Bảo vệ nền tảng và dải Nhà nước kiến tạo bị bỏ. `vie_pol.2.b` và `vie_pol.5.b` vẫn còn nhưng **không mở dải nào nữa**: hai biến thể tinh thần ở trên là toàn bộ hệ quả của chúng, tức là biến thể đường lối trong khuôn khổ Đảng.

---

## 6. Decision: "Thực hiện Nghị quyết"

### 6.1 Danh mục

```text
VIE_resolution_category
  allowed  = { original_tag = VIE }
  visible  = { VIE_party_rule_active = yes  check_variable = { VIE_congress_term > 8 } }
  priority = 95   (trên VIE_statebuilding_category)
```

Quy tắc chung:

- Decision theo nhiệm kỳ: `visible` gồm `check_variable = { VIE_congress_term = N }` và focus nghị quyết N đã xong. Đại hội kế tiếp họp thì decision chưa làm biến mất. Đó là cửa sổ nhiệm kỳ.
- `fire_only_once = yes`, trừ hai dòng xuyên nhiệm kỳ (mục 6.3).
- **Chi phí trả ngay, lợi ích đến muộn**: `complete_effect` trừ PP và cho malus tạm (`add_timed_idea`); `days_remove` là độ trễ thực thi; `remove_effect` trao lợi ích. **[CẦN THỬ]** vì mod chưa dùng `days_remove`.
- **Không cộng trục**, trừ chuỗi 2025, vốn chỉ chuyển hiệu ứng từ ba focus bị xóa sang.

### 6.2 Decision theo nhiệm kỳ

| ID | Nhiệm kỳ | Tên | PP / ngày thực thi | Hiệu ứng |
|---|---|---|---|---|
| `VIE_rn_ix_decentral` | IX | Phân cấp Trung ương – địa phương (NQ 08/2004/NQ-CP) | 50 / 180 | Ngay: ổn định −0.01. Sau: PP +50. Cần `decentralization` |
| `VIE_rn_ix_program134` | IX | Chương trình 134 hỗ trợ đồng bào dân tộc thiểu số (2004) | 50 / 365 | Ngay: ngân sách −1. Sau: ổn định +0.03; nếu `vie_pol.18` đã bắn thì +0.02 nữa |
| `VIE_rn_x_civil_servant_law` | X | Luật Cán bộ, công chức 2008 | 75 / 365 | Sau: mở decision `VIE_civil_service_examination` sớm hơn (cờ) |
| `VIE_rn_x_district_council_pilot` | X | Thí điểm không tổ chức HĐND huyện, quận, phường (NQ 26/2008/QH12) | 50 / 180 | Ngay: PP +25. Idea mới `VIE_no_district_council_idea` (`stability_factor −0.02`, `political_power_factor +0.03`) tồn tại cho tới khi decision XI gỡ nó |
| `VIE_rn_xi_confidence_vote` | XI | Lấy phiếu tín nhiệm tại Quốc hội (6/2013) | 50 / 90 | Sau: ổn định +0.02, BoP cải cách nhỏ |
| `VIE_rn_xi_local_gov_law` | XI | Luật Tổ chức chính quyền địa phương 2015 | 75 / 365 | Gỡ `VIE_no_district_council_idea`, ổn định +0.02. Chỉ hiện khi có idea đó |
| `VIE_rn_xii_power_control` | XII | Kiểm soát quyền lực trong công tác cán bộ (QĐ 205/2019) | 75 / 365 | Ngay: opinion `communist_cadres` −3. Sau: PP +50 |
| `VIE_rn_xii_merge_communes` | XII | Sắp xếp đơn vị hành chính huyện, xã (NQ 37/2018) | 100 / 540 | Ngay: timed idea `VIE_reorg_disruption` 180 ngày (đã có). Sau: ngân sách +1 |
| `VIE_rn_xiv_operate_apparatus` | XIV | Vận hành bộ máy mới | 50 / 180 | Gỡ sớm malus chuyển đổi của chuỗi 2025 |

### 6.3 Hai dòng xuyên nhiệm kỳ

Đúng như bản tham khảo đề xuất: cơ chế tiến hóa theo nhiệm kỳ thay vì xuất hiện đột ngột.

**Cải cách hành chính.** Ba giai đoạn là ba chương trình có thật.

| ID | Mở từ | Văn bản | PP / ngày | Hiệu ứng khi xong |
|---|---|---|---|---|
| `VIE_rn_par_1` | NQ IX + `public_admin_reform` | QĐ 136/2001/QĐ-TTg, CCHC 2001–2010 | 75 / 365 | ổn định +0.02, PP +25 |
| `VIE_rn_par_2` | NQ XI + `par_1` | NQ 30c/NQ-CP, CCHC 2011–2020 | 75 / 365 | như trên |
| `VIE_rn_par_3` | NQ XIII + `par_2` | NQ 76/NQ-CP, CCHC 2021–2030 | 75 / 365 | như trên, cộng giảm 1 bậc chi phí decision `VIE_streamline_administrative_org` |

**Phòng chống tham nhũng.** Chỉ hai trong năm giai đoạn giảm tham nhũng; các giai đoạn còn lại đổi cách vận hành.

| ID | Mở từ | Nội dung | PP / chờ | Hiệu ứng |
|---|---|---|---|---|
| `VIE_rn_pctn_2006` | NQ X + `anti_corruption_steering` | BCĐ TW PCTN do Chính phủ chỉ đạo | 50 / — | Timed idea "Ban Chỉ đạo TW PCTN" 730 ngày: `stability_factor +0.02`, `political_power_factor −0.03` |
| `VIE_rn_pctn_2013` | NQ XI + `party_inspection` | BCĐ chuyển về Bộ Chính trị | 100 / 730 | **Giảm 1 nấc tham nhũng**, ổn định −0.02 |
| `VIE_rn_pctn_2016` | NQ XII + `party_discipline` | "Không có vùng cấm" | 100 / 730 | **Giảm 1 nấc tham nhũng**, opinion `communist_cadres` −5 |
| `VIE_rn_pctn_2022` | NQ XIII + `digital_anticorruption` | "Tham nhũng, tiêu cực"; BCĐ cấp tỉnh | 75 / — | Gỡ idea `VIE_official_caution` (tâm lý sợ sai, xem `vie_pol.21`), tức thực hiện Kết luận 14 về bảo vệ cán bộ dám nghĩ dám làm |
| `VIE_rn_pctn_2024` | NQ XIII, sau `vie_pol.7` | Chống lãng phí | 75 / — | Ngân sách +1 |

Hai giai đoạn giảm tham nhũng chỉ dùng được khi tham nhũng còn **từ `level_06` trở lên**. Decision `VIE_anticorruption_campaign` hiện có (danh mục Xây dựng nhà nước) đổi `visible` thành `NOT = { VIE_party_rule_active = yes }`, vì dưới chế độ Đảng dòng PCTN ở trên đã thay nó.

### 6.4 Chuỗi cải tổ 2024–2025

Bản tham khảo đề xuất decision → event → decision → event. Thiết kế này đảo thành **event trước**: `vie_pol.16` và `vie_pol.17` đã được lên lịch, và mô tả của chúng là "đề án được đưa lên bàn nghị sự", tức là việc xảy ra với chính phủ. Decision là phản ứng thực thi của người chơi.

```text
[vie_pol.16] 2024.11  Đề án tinh gọn bộ máy
   a "Tiến hành ngay" → cờ VIE_streamline_go        b "Thận trọng" → cờ có hạn 180 ngày rồi mới mở
        │
        ▼
[DECISION] VIE_rn_xiii_restructure_center   Sắp xếp bộ máy Trung ương        100 PP / 90 ngày
        hiệu ứng cũ của merge_ministries: checks −1, decent −1, size −2
        │
[vie_pol.17] 2025.5   Đề án sáp nhập tỉnh, bỏ cấp huyện (NQ 60, 4/2025)
        │
        ▼
[DECISION] VIE_rn_xiii_merge_provinces       Sắp xếp đơn vị hành chính cấp tỉnh   100 PP / 60 ngày
        hiệu ứng cũ của provincial_merger: decent −2, size −2; VIE_provincial_merger_idea
        │
        ▼
[DECISION] VIE_rn_xiii_two_tier              Vận hành chính quyền địa phương hai cấp
        available date > 2025.6.30 · 50 PP / 30 ngày
        hiệu ứng cũ của two_tier_local_gov: decent −1, size −2; VIE_two_tier_gov_idea
        timed idea VIE_reorg_disruption 365 ngày (chi phí chuyển đổi) · cờ VIE_two_tier_done
        │
        ▼
[vie_pol.30] 2025.7   Chính quyền địa phương hai cấp đi vào hoạt động   (event mới, bắn từ decision)
```

Hai option của `vie_pol.16`/`.17` hiện chỉ cho PP và ổn định, không cộng trục. Vì vậy chuyển hiệu ứng trục của ba focus vào decision **không tính trùng**.

Mất mát chấp nhận: dưới chế độ không phải Đảng, chuỗi này không hiện. Hiện nay người chơi rời chế độ Đảng vẫn sáp nhập tỉnh được qua focus. Chuyển thành decision có điều kiện `OR` với chế độ khác là việc làm thêm nếu muốn giữ.

> **Đã code (pha 4 — Decision), đúng 20 decision chứ không phải 19.** Mục 0 ghi "thêm 19 decision" nhưng cộng đúng các bảng ở 6.2 (9) + 6.3 (3 CCHC + 5 PCTN) + 6.4 (3) ra 20 — đã làm đủ cả 20, không đoán bớt cái nào. `days_remove` + `remove_effect` (mục 6.1, đánh dấu `[CẦN THỬ]`) đã dùng cho 6 trong 9 decision theo nhiệm kỳ có cột "Sau:" rõ ràng; 3 decision còn lại (`rn_x_district_council_pilot`, `rn_xi_local_gov_law`, `rn_xiv_operate_apparatus`) không có "Sau:" trong văn bản nên làm hiệu ứng ngay lập tức, không trễ. Hai dòng xuyên nhiệm kỳ (CCHC, PCTN) không đóng theo cửa sổ nhiệm kỳ cứng như nhóm 6.2 — mỗi giai đoạn tự đặt cờ hoàn thành (`VIE_par1_done`, `VIE_par2_done`, ...) để giai đoạn sau đọc, đúng tinh thần "tiến hóa qua nhiều nhiệm kỳ" đã nói ở đầu mục 6.3. `VIE_rn_par_3`'s giảm chi phí decision `VIE_streamline_administrative_org` dùng cú pháp `cost = { base modifier }` — cũng là lần đầu mod dùng, đi kèm `[CẦN THỬ]`.

---

## 7. Event

### 7.1 Event đã có, xếp theo nhiệm kỳ

| Nhiệm kỳ | Event |
|---|---|
| IX | `vie_pol.2` Đại hội · `vie_pol.14` bầu cử QH 2002 · Năm Cam 2002–03 · `vie_pol.18` Tây Nguyên 2004 |
| X | `vie_pol.3` Đại hội · PMU18 · `vie_pol.14` 2007 · lạm phát 2008 · Vinashin 2010 |
| XI | `vie_pol.4` Đại hội · `vie_pol.14` 2011 · `vie_cor.1` Vinalines · `vie_pol.11` HNTW6 · `vie_pol.15` Kiến nghị 72 |
| XII | `vie_pol.5` Đại hội · `vie_pol.14` 2016 · `vie_eco.6` Formosa · `vie_cor.2`, `.3` · `vie_pol.10` An ninh mạng · `vie_alt.6` đặc khu · `vie_pol.27` Bộ luật Lao động |
| XIII | `vie_pol.6` Đại hội · `vie_pol.14` 2021 · `vie_cor.4`, `.5`, `.6` · `vie_pol.19` Cư Kuin · `vie_pol.21` sợ sai · `vie_pol.7` chuyển tiếp 2024 · `vie_pol.16`, `.17` |
| XIV | `vie_pol.8` Đại hội · bầu cử khóa XVI (mới) · `vie_pol.9` TBT kiêm CTN |

### 7.2 Event mới

| ID | Mốc | Kích hoạt | Lựa chọn |
|---|---|---|---|
| `vie_pol.28` | Hiến pháp 2013 được thông qua (28/11/2013) | Scheduler, `date > 2013.11.27`, lớp A (luôn bắn). Nội dung đổi theo lựa chọn ở `vie_pol.15` | **a** (lịch sử): giữ Điều 4; cờ `VIE_constitution_2013_adopted`; ổn định +0.02. **b** (chỉ khi `vie_pol.15` đã chọn lấy ý kiến rộng): thêm một chương về quyền con người mạnh hơn: `checks +1`, BoP cải cách vừa, cờ dùng cho G3 / `institutional_opening` |
| `vie_pol.29` | Chủ tịch nước qua đời (21/9/2018) | Scheduler, `date > 2018.9.20`, chỉ khi có `VIE_trong_third_term` | **a** (lịch sử): quyền Chủ tịch nước, rồi Quốc hội bầu TBT kiêm Chủ tịch nước (23/10/2018): PP +50, `checks −1`, cờ `VIE_dual_role_2018`. **b**: bầu một Chủ tịch nước riêng: ổn định +0.01, `factor = 0` khi `VIE_ai_historical`. `vie_pol.9` (2026) có thể đọc cờ 2018 làm tiền lệ |
| `vie_pol.30` | Chính quyền địa phương hai cấp đi vào hoạt động (1/7/2025) | Decision `VIE_rn_xiii_two_tier` | Một lựa chọn: thông báo hiệu ứng |
| (dùng lại `vie_pol.14`) | Bầu cử Quốc hội khóa XVI (15/3/2026) | Scheduler part 13, `date > 2026.3.14` | Như các lần trước |

Tất cả dùng mẫu lớp B (cooldown 45 ngày, fallback im lặng), trừ `vie_pol.28` là lớp A vì nó là điều kiện của một focus.

### 7.3 Event cũ cần sửa

| Event | Sửa |
|---|---|
| `vie_pol.1` | Đặt `VIE_congress_term = 8` |
| Khối scheduler của `vie_pol.2`, `.3`, `.4`, `.5`, `.6`, `.8` | Gọi `VIE_start_congress_term = { N = … }` ngay sau khi đặt cờ `VIE_sched_congress_N`, cả trong catch-up |
| `vie_pol.16`, `vie_pol.17` | Option đặt cờ mở decision (mục 6.4) |
| `vie_pol.11` | Thêm option phụ khi đã làm `tw4_party_building`: kỷ luật thành công một phần (khác lịch sử) |

> **Đã code (pha 2 — Event), có hai điều chỉnh.** (1) `vie_pol.16`/`.17` không thêm event mới cho nhánh "thận trọng" (hạn 180 ngày rồi mới mở decision) — thay vào đó `vie_pol.16.b` đặt hai cờ: `VIE_streamline_wait_ever` (vĩnh viễn) và `VIE_streamline_wait` (tự xóa sau 180 ngày, cú pháp `set_country_flag = { flag = X days = N }` mod đã dùng khắp nơi). Decision `VIE_rn_xiii_restructure_center` (pha 4) sẽ kiểm tra "đã từng đặt cờ NHƯNG cờ có hạn đã hết" (`has_country_flag = VIE_streamline_wait_ever` và `NOT has_country_flag = VIE_streamline_wait`) thay vì cần một event ẩn chỉ để dời lịch. `vie_pol.17` không rẽ theo lựa chọn (đúng sơ đồ mục 6.4 chỉ có một mũi tên), nên cả hai option đều đặt chung `VIE_merge_provinces_started`. (2) **Chưa sửa `vie_pol.11`** dù mục 9 liệt nó vào pha 2 — option phụ cần `has_completed_focus = VIE_tw4_party_building`, focus đó chỉ được tạo ở pha 3 (mục 4.3). Thêm tham chiếu bây giờ sẽ treo tới khi pha 3 xong. Dời việc này sang lúc tạo `tw4_party_building`. Scheduler part 13 (file mới, viết tay) nối cả 3 event mới, thêm vào `on_monthly` và `VIE_catch_up_schedule`; phát hiện thêm: `VIE_catch_up_schedule` vốn đã thiếu gọi `VIE_event_scheduler_p11`/`_p12` (lỗi có sẵn, không liên quan tới pha này, không sửa).

---

## 8. Ràng buộc phải giữ

### 8.1 Trục

| Trục | Trước (29 focus lịch sử) | Sau (focus + chuỗi 2025) | Chênh |
|---|---|---|---|
| size | −12 | −12 | 0 |
| merit | +23 | +23 | 0 |
| decent | +3 | +3 | 0 |
| checks | +10 | +11 | **+1** (NQ 66) |
| market | +3 | +1 | **−2** (bỏ NQ 68 trùng; thân kinh tế vẫn giữ) |
| civil | −3 | −3 | 0 |
| mob | +1 | +1 | 0 |

Ngoài tổng, **thời điểm** đổi ở một chỗ: `streamline_apparatus` (size −2, merit +1) chuyển từ giai đoạn 5 (2021–26) về giai đoạn 4 (2016–20) theo đúng mốc NQ 18. Phải chạy lại kiểm tra hồ sơ giai đoạn của STEP6 trong `_gen/axis_map.py` (máy local) và cập nhật ánh xạ cho 10 focus mới (trục = 0).

Event mới `vie_pol.28.b` và `vie_pol.29.a` cộng trục, nhưng chỉ ±1 và chỉ khi chọn lựa chọn ngoài lịch sử (28.b) hoặc đúng lịch sử (29.a, đã là một phần của hồ sơ 2016–20 mà STEP6 mô tả là "civil âm, checks âm").

### 8.2 Tham nhũng

| | Trước | Sau |
|---|---|---|
| Focus khối chính trị (ròng) | −11 | **−3**: `anti_corruption_law` −1, `party_discipline` −1, `digital_anticorruption` −1, `e_government` −1, `decentralization` +1 |
| Decision dòng PCTN | 0 | tối đa −2, có sàn `level_06` |
| Đích lịch sử 2026 | có thể tới `level_01` | khoảng `level_05` |

**[TIỀN ĐỀ KỊCH BẢN]** Đích `level_05` dựa trên việc Việt Nam cải thiện liên tục chỉ số CPI của Transparency International nhưng vẫn ở nhóm giữa. Toàn cây còn các nguồn giảm tham nhũng khác (event `vie_cor.*`, `vie_pol.25`, focus ngoài khối). Cần đo toàn cây trước khi chốt con số.

### 8.3 Save cũ

- Ba ID focus bị xóa: `VIE_merge_ministries`, `VIE_provincial_merger`, `VIE_two_tier_local_gov`. Save đã hoàn thành chúng giữ idea nhưng mất cờ `VIE_two_tier_done`. Thêm vào `on_startup` một dòng: nếu đã có `VIE_two_tier_gov_idea` thì đặt cờ.
- Hai ID đổi nội dung: `VIE_constitution_2013`, `VIE_resolution_57_68`. Save cũ giữ hiệu ứng đã nhận, không lỗi.
- Save đang ở giữa ván không có biến `VIE_congress_term`. Tính lại một lần trong `on_startup` từ các cờ `VIE_sched_congress_N`.

---

## 9. Kế hoạch thực hiện

Mỗi pha chạy được độc lập; sau mỗi pha phải chạy `tools/check_static.py` trên máy local (script trỏ đường dẫn game trên Windows, không chạy được trong môi trường cloud).

| Pha | Việc | File |
|---|---|---|
| **1. Nền** | Trigger, effect có tham số; biến nhiệm kỳ; 8 idea tinh thần và 2 idea của decision (`VIE_no_district_council_idea`, idea BCĐ PCTN 2006); gọi `VIE_start_congress_term` trong 6 khối scheduler; `on_startup` tính lại biến cho save cũ | `common/scripted_triggers/VIE_md_triggers_congress.txt` (mới) · `common/scripted_effects/VIE_md_effects_congress.txt` (mới) · `VIE_md_effects.txt` · `VIE_md_effects_p2.txt` · `common/ideas/VIE_md_ideas_congress.txt` (mới) · `common/on_actions/VIE_md_on_actions_startup.txt` |
| **2. Event** | `vie_pol.28`, `.29`, `.30`; sửa `vie_pol.1`, `.11`, `.16`, `.17`; scheduler part 13 (Hiến pháp 2013, Chủ tịch nước 2018, bầu cử khóa XVI) và gọi nó trong `on_monthly` | `events/VIE_md_pol.txt` · `events/VIE_md_p10.txt` (sửa event, không sửa scheduler sinh tự động) · `common/scripted_effects/VIE_md_effects_p13.txt` (mới) · `common/on_actions/VIE_md_on_actions.txt` |
| **3. Cây** | 10 focus mới; dời tọa độ 28 focus; sửa prerequisite và available theo mục 4.3; đổi nội dung 2 focus; xóa 3 focus; giảm tham nhũng theo mục 8.2 | `common/national_focus/VIE_md_focus.txt` · `_gen/axis_map.py` (local) |
| **4. Decision** | Danh mục mới; 19 decision; đổi `visible` của `VIE_anticorruption_campaign` | `common/decisions/categories/VIE_md_categories.txt` · `common/decisions/VIE_md_decisions.txt` |
| **5. Loc** | Tiếng Việt cho tất cả ở trên | `localisation/english/replace/VIE_md_vi_congress_l_english.yml` (mới, UTF-8 BOM, header `l_english:`) |
| **6. Kiểm tra** | `check_static.py` = 0 lỗi; `_gen/fix_spacing.py` và `_gen/overview.py`: không có cặp dưới 2 ô, không có con nằm trên cha; chạy lại hồ sơ trục STEP6 | local |

Pha 1 và 2 không đổi gì người chơi nhìn thấy trong cây, nên là điểm dừng an toàn để thử trong game trước khi làm pha 3.

### 9.1 Kịch bản thử trong game

1. **Đường lịch sử, AI** (`VIE_ai_historical`) chạy 2000 → 2027: đủ 6 tinh thần nối nhau; mỗi Đại hội gỡ tinh thần cũ; chuỗi 2025 hoàn tất trước 2025.12; tham nhũng cuối ván trong khoảng `level_04`–`level_06`.
2. **Người chơi bỏ qua NQ IX** tới năm 2006: focus bị bypass, nhánh X vẫn mở, không có tinh thần IX.
3. **Cửa rẽ bảo thủ ở IX** (`vie_pol.2.b`): nhận `VIE_resolution_9_cons_idea`; không mở dải nào.
4. **Cửa rẽ Kiến tạo ở XII** (`vie_pol.5.b`): nhận `VIE_resolution_12_dev_idea`; không mở dải nào.
5. **Rời chế độ Đảng năm 2010**: nghị quyết XI–XIV bypass; `rule_of_law_state`, `constitution_2013`, `e_government` vẫn làm được; danh mục "Thực hiện Nghị quyết" ẩn; `VIE_anticorruption_campaign` hiện.
6. **Catch-up** sau nội chiến: `VIE_congress_term` đúng nhiệm kỳ hiện tại.
7. **Save cũ** đã làm `two_tier_local_gov`: ngã rẽ 2026 vẫn mở.
8. **`error.log`** không có dòng `VIE` hay `vie_`.

---

## 10. Câu hỏi tác giả cần quyết

1. **Chuỗi 2025 dưới chế độ khác.** Chấp nhận mất (thiết kế hiện tại), hay giữ bản decision song song không gắn nghị quyết?
2. **Cửa sổ nhiệm kỳ cho focus chủ đề.** Thiết kế hiện chỉ cho nghị quyết hết hạn; focus chủ đề của nhiệm kỳ cũ vẫn làm muộn được. Nếu muốn áp lực thời gian mạnh hơn, có thể cho một số focus chủ đề mất phần thưởng tinh thần khi làm muộn.
3. **Đích tham nhũng 2026.** `level_05` là đề xuất. Cần đo toàn cây trước khi chốt.
4. **Đại hội XV, XVI** (`vie_pol.12`, `.13`, 2031 và 2036) nằm trong scheduler sinh tự động. Có mở rộng xương sống sang giai đoạn giả định này không, hay dừng ở XIV như bản tham khảo?
