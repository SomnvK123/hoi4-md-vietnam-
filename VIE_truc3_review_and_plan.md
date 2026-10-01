# REVIEW TRỤC 3 (XÂY DỰNG LỰC LƯỢNG LỤC QUÂN) + PLAN CODE

> Đầu vào: `Báo cáo Lục quân VIE — Trục 1, 2, 3.md` (29/9/2026). **Nguồn chính của Trục 3 là mục VIII**; mục III là bản cũ (32 focus), mục IX là nội dung lịch sử viết cho bản VIII trước, đọc kèm bảng ánh xạ 9.10.
> Đối chiếu với: repo @ `f3236f9` (30/9/2026, sau khi Trục 1 và 2 đã code), `tools/audit/md_ref/`, và `MillenniumDawn/Millennium-Dawn` @ `main` (đọc qua GitHub API ngày 1/10/2026).
>
> **KẾT LUẬN: Trục 3 có khung thiết kế tốt nhưng CHƯA code được nguyên văn.** Có **3 lỗi chặn**, **4 chỗ lệch so với repo hiện tại**, **8 chỗ lệch so với game/MD**, và **1 lỗi cũ của Trục 2** tôi gặp khi đọc `on_startup`. Cấu trúc (9 tầng, 30 focus, giới hạn 3/4 và 2/3, hệ điểm balance, ME ba chiều) **giữ nguyên**. Cái đổi là: tiền đề, tên modifier, thang số, cách đặt ngày, decision, event, ID. Sau khi vá, plan ở Phần 6 code được tuần tự 9 bước.

---

# PHẦN 0 — CÁCH ĐỌC VÀ NHỮNG GÌ ĐÃ KIỂM CHỨNG

**Đã kiểm chứng đúng, khỏi tra lại**

| Hạng mục | Kết quả |
|---|---|
| Số focus mục 8.2 | 3 + 7 + 1 + 1 + 6 + 2 + 1 + 6 + 3 = **30**; người chơi đi 21–22 ✅ |
| Cost trên đường đi | 27 + (35–42) + 7 + 7 + 17 + 10 + 10 + 34 + 30 = **177–184 tuần** khớp bảng 8.2 ✅ (nhưng xem G7: đề xuất hạ 2 cost) |
| Hệ điểm 8.11 | Chạy lại bằng script: BB1 2,0 · BB2 2,5 · TG1 2,0 · TG2 2,4 · CB 2,5 · FM1+FM2 gộp 11,2 · FR 9,0 · FD 9,2 · mỗi hướng ròng đúng 6,0 ✅ |
| Không có deadlock ở giới hạn 3/4 và 2/3 | Đã suy lại bằng tay: CB2 cộng cả `count` lẫn `done`; mọi tổ hợp 3 trong 4 đều đủ `done ≥ 3`; mọi cặp 2 trong 3 đều đủ `cap_done ≥ 2` ✅ |
| Mốc lịch sử | Nghị quyết 05-NQ/TW **17/1/2022**, 230-NQ/QUTW **2/4/2022** ✅ · lễ công bố Quân đoàn 12 **2/12/2023** (QĐ 21/11/2023) ✅ · Quân đoàn 34 **15/12/2024** (QĐ 10/12/2024) ✅ · Quyết định 366 ký **24/1/2025**, công bố **5/2/2025** ✅. Chưa tra lại: Nghị quyết 1657-NQ/QUTW (20/12/2022) |
| `VIE_modernize_vpa` AI đi được | `ai_will_do base = 80`, không có `available` → AI hoàn tất sớm, không chặn N1 (báo cáo 7.3 mục 2) ✅ |
| `cost` mặc định, đơn vị | MD `focus-tree-reference.md`: *"Omit defaults: cost = 10"*; `MD_defines.lua` chỉ đổi `NFocus.MAX_SAVED_FOCUS_PROGRESS = 30`, **không** đổi `FOCUS_POINT_DAYS` → 1 điểm cost = 7 ngày ✅ |
| Tên modifier tiền của MD | `army_personnel_cost_multiplier_modifier`, `equipment_cost_multiplier_modifier` có thật (`money_modifier_definitions.txt`, `color_type = bad`, `value_type = percentage`) ✅ |
| Template sư đoàn | MD đã có sẵn `Mechanized Division` cho VIE (`VIE_2000_nsb.txt`, token `Mech_Inf_Bat`, `armor_Bat`, `SP_Arty_Bat`, `SP_AA_Battery`…), NSB và non-NSB **giống hệt** ✅ |

---

# PHẦN 1 — 3 LỖI CHẶN

## B1 · 🚨 Ba focus "Trục 1 giữ lại" **không còn tồn tại** — mục 3.7 và VIII dựa vào chúng

Báo cáo 3.7 và 8.x viết: *"Trục 1 giữ `VIE_mechanization`, `VIE_army_c4isr`, `VIE_army_short_range_ad`; Trục 3 chỉ cho modifier, không tạo mẫu, không cộng planning/recon/tech"*. Cả ba đã bị v11 xoá (`v11_removed_military_all_subbranches.txt`), và Trục 1 chỉ dùng event, **không dựng lại** (Trục 2 mới dựng lại 4 focus của riêng nó). Đo trên file live: 0 kết quả cho cả ba.

**Hệ quả:**
- Các ràng buộc "Trục 3 không cộng planning/recon, AA, tech" **vẫn nên giữ** (giữ nguyên ngân sách điểm), nhưng giờ chúng không còn "chủ sở hữu" nào bù lại. `Phòng không lục quân` (A1/A2) và `Mạng & Điện tử` (Y1/Y2) chỉ là modifier thuần, không có tòa AA hay tech nào đi kèm.
- Phần "Mẫu sư đoàn cơ giới, 200 `util_vehicle`" của `VIE_mechanization` **không cần dựng lại**: MD đã có `Mechanized Division` trong OOB 2000 của VIE. BB1 "cơ giới hóa từng bước" chỉ là modifier tổ chức, đúng ý báo cáo.
- Đây là **nợ thiết kế có chủ đích**, giống `VIE_ev_t90_tanks` của Trục 1: ghi vào Q12 (mặc định: không dựng lại), không chặn code.

## B2 · 🚨 Cụm "Phòng thủ toàn dân" **đã có sẵn** trong cây focus — trùng với FD1, FD2 và 4 decision của báo cáo

Báo cáo viết cho cây v7 rồi bị v11 cắt ba quân chủng, nhưng **một cụm quân sự khác còn sống** (neo vào `VIE_law_of_the_sea`, tiền đề `VIE_modernize_vpa`):

| Focus có sẵn | Làm gì | Trùng với báo cáo |
|---|---|---|
| `VIE_peoples_defence` | `VIE_peoples_defence_idea`: +5% phòng thủ, +2% `conscription_factor`; `VIE_ax_mob +1` | **FD1** "Phòng thủ chiều sâu" |
| `VIE_provincial_defence_zones` | bunker dọc biên giới 4 state, `VIE_provincial_defence_idea` (Nghị quyết 28-NQ/TW 2008) | **FD2** "Dân quân và khu vực phòng thủ"; sự kiện nền 22/9/2008 (9.2) |
| `VIE_militia_law` (`date > 2019.6.30`) | +20 000 nhân lực, +8% `dig_in_speed`, +5% `max_dig_in` | FD2 và sự kiện nền Luật Dân quân tự vệ 2019 (9.2) |
| `VIE_un_peacekeeping` (`date > 2013.12.31`) | +10 XP, +opinion phương Tây | decision "Triển khai gìn giữ hòa bình" (8.14) và sự kiện 27/5/2014 (9.2) |
| `VIE_force_47` → `VIE_cyber_command` | `VIE_cyber_command_idea`, tech mã hoá | **Y1** "Tác chiến mạng và điện tử" |
| `VIE_military_rescue_corps` + cờ `VIE_disaster_prepared` | cứu hộ thiên tai | decision HADR (8.14) |
| `VIE_four_nos_doctrine` | đòi `VIE_militia_law` và `VIE_un_peacekeeping` | điều kiện capstone Trục 2 |

**Quyết định cần chốt (Q11).** Mặc định (a): **giữ cả hai, chấp nhận cộng dồn**, giống cách báo cáo 3.7 đã chấp nhận cộng dồn với ba focus Trục 1. Điều kiện kèm theo: FD2 đổi tên/lời mô tả để không nói lại những gì `VIE_provincial_defence_zones` và `VIE_militia_law` đã nói (FD2 tập trung vào **tổ chức đơn vị** dân quân, kèm mẫu sư đoàn mới). Con số G2 **chưa tính** cụm cũ; người chơi đi đủ cả hai sẽ có thêm khoảng +5% phòng thủ, +5% dig-in (cùng +8% tốc độ đào và +20 000 nhân lực một lần), tức dig-in ≈ 30%. Chấp nhận vì cụm cũ là lựa chọn riêng, tốn thêm 4–5 focus, và Chiều sâu đã là hướng yếu nhất về tấn công/tốc độ.
Hệ quả: các sự kiện nền 2008/2010/2014/2020 của mục 9.2 **bỏ hết** (đã có focus tương ứng), nên cũng giải được vấn đề ngân sách pop-up (G5).

## B3 · 🚨 Decision: report dùng category và thang chi phí **không tồn tại trong repo**

- Báo cáo mở category mới `VIE_readiness_decisions`. Repo **đã có** `VIE_military_readiness_category` (`visible = has_completed_focus = VIE_modernize_vpa`) với 4 decision: `VIE_exercise_military_region` (40 PP, +15 XP, cooldown 365), `VIE_procurement_batch`, `VIE_asean_joint_patrol`, `VIE_extended_conscription` (75 PP, +25 000 nhân lực, −2% ổn định, cooldown 1095).
- Báo cáo tính chi phí = k × thu nhập PP hằng tháng. Mọi decision trong repo dùng **PP nguyên** (20–75). Chưa ai đo thu nhập PP của VIE.
- Hai decision của báo cáo **chồng** decision có sẵn: "Diễn tập hiệp đồng binh chủng" ≈ `VIE_exercise_military_region`; "Động viên toàn dân"/"Tổng động viên" ≈ `VIE_extended_conscription` (nhưng gấp 8 lần nhân lực với chi phí tương đương).

**Vá:** dùng `VIE_military_readiness_category`; chi phí PP nguyên neo vào decision có sẵn (Q13); chỉnh biên độ nhân lực (G10).

---

# PHẦN 2 — 4 CHỖ LỆCH SO VỚI REPO HIỆN TẠI

## R1 · Biến chỉ ghi, không ai đọc

`VIE_combined_arms_level`, `VIE_command_reform_level` (báo cáo 4.2, 8.8: "chỉ Trục 3") và `VIE_force_building_done` (đọc bởi "nhánh Chính trị/Đối ngoại", chưa tồn tại). Review Trục 2 đã coi "cờ đặt mà không đọc là rác" (C4).
**Vá:** bỏ hai biến đầu; trạng thái đã có sẵn dưới dạng `has_completed_focus = VIE_lf_command_reform_N` (CR1/CR2/CR3). Giữ `VIE_lf_done` làm **cờ chờ có chủ đích** (như `VIE_ev_t90_tanks`), ghi rõ trong bảng cờ.

## R2 · "Tên cờ do nhánh Đối ngoại / Chính trị đặt chưa được định nghĩa" — thực ra đã có

6 decision "nhóm chung" (8.14) chờ cờ chưa tồn tại. Repo đã có sẵn trigger thật: `has_completed_focus = VIE_un_peacekeeping` (gìn giữ hòa bình), `has_completed_focus = VIE_asean_integration` (diễn tập đa phương), `VIE_disaster_prepared` (HADR), các focus `VIE_us_comprehensive_partnership` / `VIE_india_partnership` / `VIE_japan_partnership` (song phương). Xem Phụ lục A: nhóm chung tách thành bước tùy chọn, **không chặn** Trục 3.

## R3 · ID: báo cáo dùng slug tiếng Việt không dấu, repo dùng tiếng Anh

Mọi focus quân sự live: `VIE_modernize_vpa`, `VIE_def_industry_law`, `VIE_peoples_defence`… (Trục 2 cũng theo đó). Báo cáo Trục 3: `VIE_cai_cach_quan_doi`, `VIE_phong_thu_chieu_sau`…
Thêm: tiền tố `VIE_force_*` của báo cáo (cờ hướng lực lượng) **đụng** focus `VIE_force_47` và `VIE_force_47_idea` có sẵn; báo cáo hải quân (bản 2.4) cũng dùng `VIE_cap_*`, `VIE_org_*`.
**Vá:** mọi định danh Trục 3 dùng tiền tố **`VIE_lf_`** (land force), tên tiếng Anh; tên hiển thị tiếng Việt như báo cáo. Bảng ánh xạ ở mục 5.2.

## R4 · Quân đoàn 12 và 34 là **quân đoàn chủ lực cơ động chiến lược** — nhãn "ALT" ở ô Chính quy × Cơ động chiến lược là sai

Bảng 8.5 gắn ô *Chính quy × Cơ động chiến lược* là "ALT nhẹ" và chỉ ô *Chính quy × Phòng thủ khu vực* là "gần lịch sử nhất". Nhưng chính nguồn của báo cáo (VOV, Báo Hưng Yên) gọi Quân đoàn 12 và 34 là "quân đoàn chủ lực **cơ động chiến lược**", và 9.9 cũng ghi "Quân đoàn 12 và 34 là quân đoàn chủ lực thật". Lịch sử thật đi **cả hai**: quân đoàn chủ lực cơ động chiến lược **và** khu vực phòng thủ/dự bị.
**Vá:** cả hai ô Chính quy đều `[THẬT]`; AI Historical chia PS và PT ngang nhau (G3). Chỉ các ô Cơ động × * và Chiều sâu × PS còn là hướng giả định.

---

# PHẦN 3 — 8 CHỖ LỆCH SO VỚI GAME / MD

## G1 · Số slot focus: thực tế là **1**, và đã đo ra hệ quả

MD `MD_defines.lua` chỉ chỉnh một dòng `NFocus` (`MAX_SAVED_FOCUS_PROGRESS = 30`); vanilla không có modifier cộng slot. Giả định **1 slot** (chưa kiểm trong game, ghi vào checklist). Hệ quả với báo cáo:
- Mô phỏng 8.12 ở 1 slot: 175–184 tuần, luôn 21–22 focus, **0% vượt giới hạn** → toàn bộ cơ chế bảo hiểm (phần thưởng chỉ áp nếu count còn dưới giới hạn) **không bao giờ chạy** ở 1 slot.
- Vẫn giữ bảo hiểm, nhưng gom vào một scripted effect (không tốn gì thêm), và **bỏ** phần "cancel_if_invalid là chốt chặn" khỏi danh sách rủi ro: ở 1 slot chỉ cần `available` kiểm khi chọn.
- Tranh chấp slot (báo cáo 4.3, lỗ hổng 2): Trục 3 chiếm **3,3–3,4 năm** của slot duy nhất. Điều kiện kích hoạt Trục 1 (`.5`, `.8`, `.14`) đã được Trục 1 chuyển sang `VIE_modernize_vpa` nên **không còn xung đột**.

## G2 · 🚨 Kiểm tra cộng dồn: số liệu 8.11 **quá mạnh** cho một trục tổ chức

Tôi cộng toàn bộ node theo từng đường đầy đủ (3 binh chủng chính + HD + CR1 + hai node hướng + PS/PT + CR2 + hai lĩnh vực + MOD + CR3 + CAP, kể cả ×1,5 sở trường):

| Đường | Tổng theo báo cáo 8.11 |
|---|---|
| Cơ động | **tốc độ +54 đến +60%**, tổ chức +16–22%, tấn công +10–14% |
| Chiều sâu | **dig-in +40 đến +51%**, nhân lực +17%, phòng thủ +14–16% |
| Chính quy | tổ chức +25–30%, phòng thủ +17–23%, hậu cần +11% |

So với Trục 1 và 2 (T-90 +5% giáp, D5 +2%, D7/K9 +5% pháo, Igla −5% địch): mỗi node Trục 3 cùng cỡ, nhưng **18 node cộng lại** thành mức mà không ý tưởng nào của MD đạt tới (tốc độ +57% là gấp vài lần mọi bonus tốc độ phổ thông). Nguyên nhân gốc: **hệ số điểm của tốc độ (0,4) và dig-in (0,5) quá rẻ**, nên balance cho phép số % rất lớn.

**Vá (Q16, mặc định: làm):** giữ nguyên *điểm* của mọi node (nên mọi thứ cân bằng giữa các hướng giữ nguyên), đổi *hệ số* thành `W' = W / s` với `s` = tốc độ 0,4 · dig-in 0,5 · tổ chức/phòng thủ/tấn công/nhân lực 0,7 · hậu cần, XP, chi phí = 1. Giá trị mỗi node = `round(báo cáo × s, 0,5)`. Bảng cuối ở mục 5.4. Kết quả (script kiểm, nằm ở Phụ lục B):

| Đường | Tổng sau chỉnh | Trần đặt ra |
|---|---|---|
| Cơ động | tốc độ +21–25%, tổ chức +12–17%, tấn công +7–10% | tốc độ ≤ 25 |
| Chiều sâu | dig-in +20–26%, nhân lực +12%, phòng thủ +10–12% (**chưa tính** cụm cũ B2: +5% phòng thủ, +5% dig-in, +8% tốc độ đào) | dig-in ≤ 26, nhân lực ≤ 12 |
| Chính quy | tổ chức +18–21%, phòng thủ +11–16%, hậu cần −10% tiêu hao | tổ chức ≤ 21, phòng thủ ≤ 16 |

Cân bằng ròng ba hướng sau chỉnh (cặp First Force Structure): Chính quy 6,14 · Cơ động 5,79 · Chiều sâu 5,86, lệch tối đa 0,35 (báo cáo: đúng 6,0 do làm tròn; chấp nhận được).

## G3 · Trọng số AI: thang sai và tên path không có thật

- Báo cáo dùng `base` 0,5–3 và "Mọi focus khác = 1". Focus trong repo dùng **`base` 40–80** (Trục 2: 60–80; `VIE_modernize_vpa` 80). AI chọn focus theo trọng số tuyệt đối nên `base 1` khiến AI **gần như không bao giờ** đi Trục 3 khi còn việc khác.
- `VIE_path_*` ở bảng 3.9 là **tên giả**. Cờ thật (`VIE_AI_PATH_HISTORICAL/REFORM/WESTERN/HARDLINE/NATIONALIST`) đi qua trigger có sẵn: `VIE_ai_historical`, `VIE_ai_path_reformish` (Reform, Western, Free zones), `VIE_ai_path_security` (Hardline, Nationalist), `VIE_ai_free`.

**Vá:** `base 60` cho mọi node chuỗi (khớp Trục 2), `base 20` cho Công binh và gốc lĩnh vực không sở trường, `base 40` cho ba hướng và hai hướng phát triển kèm `factor` theo path. Bảng ở mục 5.6.

## G4 · Không khóa ngày là **ngoại lệ duy nhất** trong ba trục

Trục 1 dùng cửa sổ + ETD; Trục 2 khóa **hầu hết** decision và focus bằng ngày (`date > 2008.6.30`, `2012`, `2013`, `2017`, `2021`; chỉ D4, D7, D8 đi theo cờ); báo cáo hải quân có cột "Ngày" cho từng focus (T1 ≥ 2005, T6 ≥ 2012…). Trục 3 không khóa gì (mục 3.10: "Không khóa ngày cho #1–#3"), nên AI có thể làm cải cách quân đội kiểu 2022 vào năm 2002.
Mod đã có công cụ đúng cho việc này: game rule `VIE_alt_history` (historical / plausible / free), và tiền lệ trong repo: `VIE_militia_law` (`date > 2019.6.30`), `VIE_force_47` (`> 2017.11.30`), `VIE_un_peacekeeping` (`> 2013.12.31`).

**Vá (Q10, mặc định: khóa mềm):** N1 `available = VIE_lf_gate_open`, với
`VIE_lf_gate_open = OR { date > 2019.2.10 ; AND { VIE_ai_free ; date > 2012.12.31 ; VIE_def_ind_level_ge_2 } }`.
Mốc 11/2/2019 là Nghị quyết 109-NQ/QUTW (báo cáo 9.2) và `VIE_def_ind_level_ge_2` chính là "cổng mềm 8.3" của báo cáo, nhưng chỉ ở chế độ `free`. Phần còn lại của cây **không** khóa ngày thêm (chỉ đi theo N1), giữ nguyên ý "đi trước mốc dated là hướng rẽ giả định" của 8.13.

## G5 · Ngân sách pop-up: mục 9.2 làm vỡ luật ≤ 7 pop-up/năm

`tools/TESTING.md` đo trước Trục 3 và trước Trục 2: 2022 = 6, 2023 = 6, 2024 = 7; Trục 2 sau đó thêm `vie_def_ind.1` (12/2024) và `.4` (6/2024) nên 2024 đã **vượt** luật sửa lại ≤ 7/năm (cần đo lại, mục 7). Mục 9.2 liệt kê 14 sự kiện nền (2008, 2010, 2014, 2018, hai cái 2019, 2020, ba cái 2022, 2023, 2024, hai cái 2025), phần lớn là "event nhỏ".
**Vá (Q17):** bỏ tất cả sự kiện đã có focus tương ứng (B2: 2008, 2010, 2014, 2020, 2018, 2019 cờ phụ). Còn **5 event** namespace `vie_lf`: **3 có pop-up** (Nghị quyết 05 · 2022; Quân đoàn 12 · 2023; Hậu cần–Kỹ thuật · 2025) và **2 ẩn** (Nghị quyết 1657 · 12/2022; Quân đoàn 34 · 12/2024, ẩn để không tăng 2024). Bảng ở mục 5.7.

## G6 · "Giảm cost 50% từ mốc" cần một effect cụ thể

HOI4 không có cost phụ thuộc ngày. Repo đã có tiền lệ đúng: `reduce_focus_completion_cost = { focus = VIE_code_of_conduct cost = 14 }` trong `events/VIE_md_p11.txt:193`, cost gốc của focus đó là 7 (tuần), nên đơn vị của tham số **chỉ có thể là ngày** (giảm 14 ngày; nếu là tuần thì tăng cost). Dùng cùng effect trong event mốc:
`reduce_focus_completion_cost = { focus = VIE_lf_army_reform cost = 35 }` (một nửa của 10 tuần = 70 ngày).
Cũng dùng effect này cho "sở trường giảm 2 tuần cost gốc" (`cost = 14`) ngay trong phần thưởng FM1/FR1/FD1. **Test bắt buộc** (checklist mục 7).

## G7 · Cost off-grid so với repo

Phân bố cost live: 5 (57 focus), 7 (156), 10 (mặc định), cá biệt 8 và 16. Báo cáo dùng **13** cho N1 và CAP; Trục 2 capstone và gốc đều ≤ 10. **Vá (Q15):** N1 = 10, CAP = 10. Tổng đường còn **171–178 tuần** (1 197–1 246 ngày).

## G8 · Nhãn `[ALT-HISTORY: cải cách sớm]` theo ngày cần scripted localisation

Loc tĩnh không đổi theo ngày. `common/scripted_localisation/` đã có (`VIE_md_axis_bars.txt`). Thêm bốn `defined_text` (`VIE_lf_alt_n1`, `_n2`, `_n3`, `_cr2`) trả về nhãn khi `date` nhỏ hơn mốc, gọi trong `_desc` bằng `[GetVIE_lf_alt_n1]`. Tên hàm theo mẫu `VIE_AxBar_*` của repo.

---

# PHẦN 4 — NỢ CŨ TÌM THẤY KHI ĐỌC (không thuộc Trục 3, nhưng Trục 3 dùng cùng mẫu)

## X1 · ⚠️ `on_startup` đặt lại biến Trục 2 mỗi lần load save

`common/on_actions/VIE_md_on_actions_startup.txt` (khối Trục 2):
```pdx
set_variable = { VIE_def_industry_level = 0 }
set_variable = { VIE_def_ind_export_count = 0 }
```
**không có guard**. Chính file đó ghi ở đầu khối thứ nhất: *"on_startup also runs on every save load, so the flag keeps this from recruiting twice"*, và khối `VIE_congress_term` ngay dưới **tính lại** biến từ cờ vì lý do đó. Nếu `on_startup` chạy lại khi load, mỗi lần mở save giữa chừng sẽ **đặt `VIE_def_industry_level` về 0**: ngã rẽ Core/Divest (cần ≥ 4) và capstone (cần ≥ 8) khóa lại, và xuất khẩu (`VIE_def_ind_export_count`) được 5 lần nữa.
Review Trục 2 (L4) sửa đúng điều kiện "biến không khởi tạo" nhưng không nghĩ tới chiều ngược lại.
**Vá (Bước 0):** bọc bằng cờ `VIE_def_ind_vars_init`, đặt biến một lần. Trục 3 dùng cùng khuôn (`VIE_lf_vars_init`). Nếu `on_startup` thực ra không chạy lại khi load thì guard vô hại.

---

# PHẦN 5 — THIẾT KẾ SAU ĐIỀU CHỈNH

## 5.0 · Quyết định Q10–Q17

> Mặc định bên dưới là những gì plan ở Phần 6 viết theo. Đổi lựa chọn nào thì sửa đúng bước ghi chú.

| Q | Câu hỏi | Mặc định | Ảnh hưởng nếu đổi |
|---|---|---|---|
| **Q10** | N1 khóa ngày? | **Khóa mềm** (`VIE_lf_gate_open`, G4) | Bỏ khóa: sửa 1 trigger ở bước 0 |
| **Q11** | Cụm "Phòng thủ toàn dân" có sẵn (B2) | **Giữ cả hai, cộng dồn**, FD2 đổi sang tổ chức đơn vị | Muốn loại trùng: FD2 đòi `VIE_militia_law` (bước 3) |
| **Q12** | Dựng lại `VIE_mechanization`/`_c4isr`/`_short_range_ad`? | **Không**; ghi nợ (B1) | Dựng lại là trục riêng, không chặn Trục 3 |
| **Q13** | Chi phí PP | **Nguyên, neo M ≈ 70 PP/tháng** (xem 5.5) | Đo PP thật rồi đổi 6 số ở bước 5 |
| **Q14** | 6 decision "nhóm chung" | **Tách**, Phụ lục A, tùy chọn | Làm cùng lúc: thêm 4 decision ở bước 5 |
| **Q15** | Cost N1 và CAP | **10** (G7) | Giữ 13: 177–184 tuần |
| **Q16** | Chỉnh thang số (G2) | **Làm** | Bỏ: dùng nguyên bảng 8.11, chấp nhận tốc độ +57% |
| **Q17** | Bộ event | **5 event** (G5) | Làm đủ 14: vượt ngân sách pop-up |

## 5.1 · Kiến trúc (giữ nguyên báo cáo VIII)

```
VIE_modernize_vpa (đã có, abs 266,1)
 ├─ Trục 2: VIE_def_industry_law (266,2) → Core/Divest → capstone      [đã code, không đụng]
 └─ Trục 3: [1 Nền tảng] N1 → N2, N3
              [2 Binh chủng] 3 trong 4: Bộ binh │ Tăng thiết giáp │ Pháo binh │ Công binh
              [3] HD   [4] CR1 → mở 3 decision
              [5 First Force Structure] CHỌN 1 (ME 3 chiều): Cơ động │ Chính quy │ Chiều sâu  (mỗi hướng 2 focus)
              [6 Hướng phát triển] CHỌN 1 (ME): Cơ động chiến lược │ Phòng thủ khu vực và dự bị
              [7] CR2   [8 Năng lực] 2 trong 3: Biên giới & Đô thị │ Phòng không lục quân │ Mạng & Điện tử
              [9] MOD → CR3 → CAP (3 biến thể)
```
Không có prerequisite chéo sang Trục 1/2. Trục 3 **đọc** một thứ duy nhất của Trục 2: `VIE_def_ind_level_ge_2` (chỉ ở chế độ `free`, G4). Trục 3 **ghi** các cờ ở 5.3, Trục 1/2 chỉ đọc chúng trong bước tùy chọn 8 (AI).

## 5.2 · Ánh xạ mã báo cáo → ID

Prerequisite viết theo quy ước HOI4: nhiều khối `prerequisite` = AND; nhiều `focus` trong một khối = OR. "Biến" ở cột *Điều kiện* là điều kiện `available`, **luôn đi kèm** prerequisite hiển thị (R1/B-HD): mỗi focus bị gate bằng biến vẫn có ít nhất một đường kẻ từ cha.

| Mã | ID | Tên hiển thị (báo cáo) | Cost | Prerequisite | `available` (ngoài ngày) | Hoàn thành |
|---|---|---|---:|---|---|---|
| N1 | `VIE_lf_army_reform` | Cải cách quân đội, tinh gọn biên chế | 10 | `VIE_modernize_vpa` | `VIE_lf_gate_open` | `VIE_lf_n1_reward` |
| N2 | `VIE_lf_logistics_merge` | Hiện đại hóa hệ thống bảo đảm hậu cần – kỹ thuật | 7 | N1 | — | `VIE_lf_n2_reward` |
| N3 | `VIE_lf_basic_training` | Đào tạo lục quân cơ bản | 7 | N1 | — | `VIE_lf_n3_reward` |
| BB1 | `VIE_lf_arm_infantry_org` | Bộ binh: tổ chức, cơ giới hóa từng bước | 7 | N2 và N3 | `arm_count < 3` | count +1 (có guard), `VIE_lf_bb1_reward` |
| BB2 | `VIE_lf_arm_infantry_train` | Bộ binh: đào tạo sĩ quan, huấn luyện binh sĩ | 7 | BB1 | — | done +1 (có guard), `VIE_lf_bb2_reward` |
| TG1 | `VIE_lf_arm_armor_org` | Tăng thiết giáp: tổ chức | 7 | N2 và N3 | `arm_count < 3` | như BB1 |
| TG2 | `VIE_lf_arm_armor_train` | Tăng thiết giáp: đào tạo sĩ quan, kíp xe | 7 | TG1 | — | như BB2 |
| PB1 | `VIE_lf_arm_arty_org` | Pháo binh: tổ chức, hỏa lực chi viện | 7 | N2 và N3 | `arm_count < 3` | như BB1 |
| PB2 | `VIE_lf_arm_arty_train` | Pháo binh: đào tạo sĩ quan, pháo thủ | 7 | PB1 | — | như BB2 |
| CB | `VIE_lf_arm_engineers` | Công binh: đào tạo, công binh chiến đấu | 7 | N2 và N3 | `arm_count < 3` | count +1 **và** done +1 (guard), `VIE_lf_cb_reward` |
| HD | `VIE_lf_combined_arms` | Hiệp đồng binh chủng | 7 | **OR** BB2, TG2, PB2, CB | `arm_done ≥ 3` | `VIE_lf_hd_reward` |
| CR1 | `VIE_lf_command_reform_1` | Cải cách bộ chỉ huy I: chuẩn hóa tham mưu | 7 | HD | — | `VIE_lf_cr1_reward`; mở 3 decision |
| FM1 | `VIE_lf_fs_mobile_force` | Lực lượng cơ động | 10 | CR1; ME FR1, FD1 | — | cờ `VIE_lf_mobile`, giá, sở trường |
| FM2 | `VIE_lf_fs_mobile_corps` | Cụm cơ động | 7 | FM1 | — | `VIE_lf_fm2_reward` + mẫu cụm cơ động |
| FR1 | `VIE_lf_fs_main_corps` | Quân đoàn chủ lực chính quy | 10 | CR1; ME FM1, FD1 | — | cờ `VIE_lf_regular`, giá, sở trường |
| FR2 | `VIE_lf_fs_lean_corps` | Tổ chức quân đoàn tinh, gọn, mạnh | 7 | FR1 | — | `VIE_lf_fr2_reward` |
| FD1 | `VIE_lf_fs_depth_defence` | Phòng thủ chiều sâu | 10 | CR1; ME FM1, FR1 | — | cờ `VIE_lf_depth`, giá, sở trường |
| FD2 | `VIE_lf_fs_militia_units` | Tổ chức dân quân và đơn vị khu vực phòng thủ | 7 | FD1 | — | `VIE_lf_fd2_reward` + mẫu dân quân |
| PS | `VIE_lf_dev_strategic` | Cơ động chiến lược | 10 | **OR** FM2, FR2, FD2; ME PT | — | cờ `VIE_lf_dev_strategic`, giá |
| PT | `VIE_lf_dev_territorial` | Phòng thủ khu vực và dự bị | 10 | **OR** FM2, FR2, FD2; ME PS | — | cờ `VIE_lf_dev_territorial`, giá |
| CR2 | `VIE_lf_command_reform_2` | Cải cách bộ chỉ huy II: bộ tư lệnh cấp chiến dịch | 10 | **OR** PS, PT | — | `VIE_lf_cr2_reward` (theo cờ hướng) |
| L1 | `VIE_lf_cap_border_urban` | Tác chiến biên giới và đô thị | 10 | CR2 | `cap_count < 2` | cap_count +1 (guard), `VIE_lf_l1_reward` |
| L2 | `VIE_lf_cap_area_control` | Khống chế địa bàn | 7 | L1 | — | cờ `VIE_lf_cap_land`, cap_done +1 (guard), `VIE_lf_l2_reward` |
| A1 | `VIE_lf_cap_army_ad` | Phòng không lục quân và bảo vệ lực lượng | 10 | CR2 | `cap_count < 2` | như L1 |
| A2 | `VIE_lf_cap_ad_coord` | Hiệp đồng phòng không với Phòng không – Không quân | 7 | A1 | — | cờ `VIE_lf_cap_ad`, như L2 |
| Y1 | `VIE_lf_cap_cyber_ew` | Tác chiến mạng và điện tử | 10 | CR2 | `cap_count < 2` | như L1 |
| Y2 | `VIE_lf_cap_info_ops` | Tác chiến thông tin hiệp đồng | 7 | Y1 | — | cờ `VIE_lf_cap_cyber`, như L2 |
| MOD | `VIE_lf_selective_modernization` | Hiện đại hóa chọn lọc | 10 | **OR** L2, A2, Y2 | `cap_done ≥ 2` | `VIE_lf_mod_reward` (theo lĩnh vực) |
| CR3 | `VIE_lf_command_reform_3` | Cải cách bộ chỉ huy III: chỉ huy số hiệp đồng | 7 | MOD | — | `VIE_lf_cr3_reward` |
| CAP | `VIE_lf_force_complete` | Hoàn thiện lực lượng vũ trang | 10 | CR3 | — | `VIE_lf_cap_reward` (3 biến thể), cờ `VIE_lf_done` |

`arm_count/arm_done/cap_count/cap_done` là `VIE_lf_arm_count`… Chỉ **bảy** node có điều kiện `count`: BB1, TG1, PB1, CB (< 3) và L1, A1, Y1 (< 2). Node giữa và node cuối **không** đòi count (đúng 3.3: nếu đòi, hai lĩnh vực đã chọn sẽ tự khóa nhau).

## 5.3 · Biến và cờ

| Tên | Loại | Đặt bởi | Đọc bởi |
|---|---|---|---|
| `VIE_lf_arm_count`, `VIE_lf_arm_done` | biến 0–3 | node đầu / node đào tạo binh chủng, CB | `available` BB1/TG1/PB1/CB; HD |
| `VIE_lf_cap_count`, `VIE_lf_cap_done` | biến 0–2 | L1/A1/Y1; L2/A2/Y2 | `available` gốc lĩnh vực; MOD |
| `VIE_lf_mobile` / `VIE_lf_regular` / `VIE_lf_depth` | cờ | FM1 / FR1 / FD1 | CR2, năng lực, MOD, CAP, AI, decision, Trục 1/2 (bước 8) |
| `VIE_lf_dev_strategic` / `VIE_lf_dev_territorial` | cờ | PS / PT | decision Phản ứng nhanh / Động viên toàn dân |
| `VIE_lf_cap_land` / `_ad` / `_cyber` | cờ | L2 / A2 / Y2 | MOD, CAP (−2% duy trì nếu đúng sở trường) |
| `VIE_lf_done` | cờ **chờ** | CAP | **chưa ai** (nhánh Chính trị/Đối ngoại tương lai); không xoá |
| `VIE_lf_vars_init` | cờ | startup | startup |
| `VIE_lf_ms_nq05` … `_corps12`, `_corps34`, `_logistics` | cờ | event mốc | scheduler |

Sở trường **không** có cờ riêng: Cơ động → Mạng & Điện tử, Chính quy → Phòng không, Chiều sâu → Biên giới & Đô thị, suy ra từ `VIE_lf_mobile/regular/depth` (scripted trigger `VIE_lf_fav_land/_ad/_cyber`).

## 5.4 · Hiệu ứng từng node (thang đã chỉnh, Q16)

Đơn vị: % cộng vào biến `VIE_af_*`, ví dụ "+1,5" = `add_to_variable = { VIE_af_army_org_factor = 0.015 }`. Cột *Biến* ở 5.5. "Hậu cần −X" = `supply_consumption_factor −X%`. Cột **báo cáo** để đối chiếu.

**Chung mọi hướng** (điểm báo cáo, giá trị mới)

| Node | Báo cáo 8.11 | **Giá trị mới** |
|---|---|---|
| N1 | không số | +25 PP; 10 XP; đặt `VIE_lf_vars_init` nếu chưa |
| N2 | không số (+ thưởng event 5/2/2025) | +15 điểm chỉ huy |
| N3 | không số | +10 XP |
| BB1 | +2 tổ chức | +1,5 tổ chức |
| BB2 | +2 phòng thủ, +1 hậu cần | +1,5 phòng thủ, hậu cần −1 |
| TG1 | +5 tốc độ | +2 tốc độ |
| TG2 | +2 tấn công | +1,5 tấn công |
| PB1 | +4 dig-in | +2 dig-in |
| PB2 | +2 tấn công pháo | +1,5 tấn công pháo |
| CB | +5 dig-in | +2,5 dig-in |
| HD | +3 tổ chức | +2 tổ chức |
| CR1 | +2 tổ chức, +2 hậu cần; mở decision | +1,5 tổ chức, hậu cần −2 |

**First Force Structure và hướng phát triển** (cái giá áp ở node đầu)

| Node | Báo cáo | **Giá trị mới** |
|---|---|---|
| FM1 | +8 tốc độ, +2 tổ chức; giá −2 nhân lực, +2 chi phí sản xuất, −4 dig-in | +3 tốc độ, +1,5 tổ chức; giá: nhân lực −1,5, `equipment_cost` +2, dig-in −2 |
| FM2 | +6 tốc độ, +3 tấn công; mẫu | +2,5 tốc độ, +2 tấn công; mẫu cụm cơ động |
| FR1 | +3 tổ chức, +2 phòng thủ; giá +2 duy trì, −1 XP | +2 tổ chức, +1,5 phòng thủ; giá: `army_personnel_cost` +2, XP −1 |
| FR2 | +2 tổ chức, +4 hậu cần | +1,5 tổ chức, hậu cần −4 |
| FD1 | +6 dig-in, +2 phòng thủ; giá −2 tấn công, −2 tốc độ | +3 dig-in, +1,5 phòng thủ; giá: tấn công −1,5, tốc độ −1 |
| FD2 | +7 nhân lực; mẫu | +5 nhân lực; mẫu dân quân (đã bỏ phần trùng `VIE_militia_law`, B2) |
| PS | +5 tốc độ, +2 tổ chức, +2 hậu cần; giá +1 sản xuất | +2 tốc độ, +1,5 tổ chức, hậu cần −2; giá `equipment_cost` +1 |
| PT | +5 nhân lực, +4 dig-in; giá +1 duy trì | +3,5 nhân lực, +2 dig-in; giá `army_personnel_cost` +1 |

Ròng sau chỉnh (cặp FFS): Chính quy 6,14 · Cơ động 5,79 · Chiều sâu 5,86.

**Năng lực** (gốc / cuối; ô sở trường nhân 1,5 làm tròn 0,5 cho node cuối, nên ghi riêng)

| Lĩnh vực | Hướng | Gốc | Cuối | Cuối **nếu sở trường** |
|---|---|---|---|---|
| Biên giới & Đô thị (L1/L2) | Chính quy | phòng thủ +2 | tổ chức +2, phòng thủ +2 | — |
| | Cơ động | tốc độ +2, phòng thủ +0,5 | tấn công +2, tốc độ +2,5 | — |
| | **Chiều sâu (sở trường)** | dig-in +2, phòng thủ +0,5 | dig-in +4, phòng thủ +1,5 | **dig-in +6, phòng thủ +2,5** |
| Phòng không lục quân (A1/A2) | **Chính quy (sở trường)** | phòng thủ +2 | tổ chức +2, phòng thủ +2 | **tổ chức +3, phòng thủ +3** |
| | Cơ động | tổ chức +1,5, tốc độ +1 | tổ chức +3, tốc độ +2 | — |
| | Chiều sâu | dig-in +2, phòng thủ +0,5 | phòng thủ +3, dig-in +2 | — |
| Mạng & Điện tử (Y1/Y2) | Chính quy | tổ chức +2 | tổ chức +2, phòng thủ +2 | — |
| | **Cơ động (sở trường)** | tốc độ +2, tổ chức +0,5 | tấn công +2, tốc độ +2,5 | **tấn công +3, tốc độ +4** |
| | Chiều sâu | dig-in +3 | phòng thủ +3, dig-in +2 | — |

Sở trường còn giảm 14 ngày cost của gốc (`reduce_focus_completion_cost`, G6).

**CR2, MOD, CR3, CAP**

| Node | Chính quy | Cơ động | Chiều sâu |
|---|---|---|---|
| CR2 | tổ chức +1,5, phòng thủ +0,5 | tổ chức +1,5, tốc độ +1 | phòng thủ +1,5, dig-in +1 |
| CAP | tổ chức +2, phòng thủ +2; −2% `army_personnel_cost` nếu đã xong lĩnh vực sở trường (Phòng không) | tốc độ +3,5, tấn công +1,5; mở decision Phản ứng nhanh (đã mở bởi PS) | nhân lực +3,5, dig-in +3; mở decision Động viên toàn dân (đã mở bởi PT) |

| Node | Mỗi lĩnh vực đã xong (MOD) | CR3 |
|---|---|---|
| MOD | Biên giới & Đô thị: dig-in +1,5 · Phòng không: phòng thủ +1 · Mạng & Điện tử: tổ chức +1 | — |
| CR3 | — | tổ chức +1, hậu cần −3 (không cộng planning/recon) |

Các hàng "mở decision" ở CAP thực ra đã được mở sớm hơn bởi PS/PT (báo cáo 3.8 viết cho bản cũ); CAP chỉ thêm `VIE_lf_done` và phần số. Ghi rõ vào loc để người chơi không tưởng CAP mở thêm decision.

## 5.5 · Ánh xạ modifier (đã kiểm chứng với repo và MD)

| Khái niệm báo cáo | Modifier | Biến `VIE_af_*` | Trạng thái |
|---|---|---|---|
| tổ chức | `army_org_factor` | `VIE_af_army_org_factor` | có trong `VIE_armed_forces_modifier` |
| phòng thủ | `army_defence_factor` | `VIE_af_army_defence_factor` | có |
| tốc độ | `army_speed_factor` | `VIE_af_army_speed_factor` | có |
| dig-in | `max_dig_in_factor` | `VIE_af_max_dig_in_factor` | có (cụm cũ dùng thêm `dig_in_speed_factor`) |
| hậu cần | `supply_consumption_factor` (âm) | `VIE_af_supply_consumption_factor` | có |
| XP | `experience_gain_army_factor` | `VIE_af_experience_gain_army_factor` | có |
| tấn công pháo | `army_artillery_attack_factor` | `VIE_af_army_artillery_attack_factor` | có |
| **tấn công chung** | `army_attack_factor` | `VIE_af_army_attack_factor` | **thiếu, thêm** (key tooltip `VIE_tt_army_attack_factor` đã có) |
| **max manpower** | `conscription_factor` (vanilla không có "max manpower"; cụm cũ dùng đúng nó) | `VIE_af_conscription_factor` | **thiếu, thêm** |
| chi phí duy trì | `army_personnel_cost_multiplier_modifier` (MD) | `VIE_af_army_personnel_cost_multiplier_modifier` | **thiếu, thêm** |
| chi phí sản xuất | `equipment_cost_multiplier_modifier` (MD) | `VIE_af_equipment_cost_multiplier_modifier` | **thiếu, thêm** |

Mẫu ghi: `add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }`, đúng mẫu của cụm cũ (`VIE_militia_law`) và Trục 1/2 (`VIE_af_army_artillery_attack_factor`). Sáu key tooltip mới trong `localisation/english/replace/VIE_md_vi_tt_l_english.yml`: `VIE_tt_army_org_factor`, `VIE_tt_experience_gain_army_factor`, `VIE_tt_supply_consumption_factor`, `VIE_tt_conscription_factor`, `VIE_tt_army_personnel_cost`, `VIE_tt_equipment_cost`. Hai modifier chi phí MD có `color_type = bad` và đơn vị chưa kiểm trong game: ghi vào checklist.

## 5.6 · AI

`ai_will_do` mọi focus: `base` như bảng, thêm `modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }` (cùng cách Trục 2). Mốc dated: `modifier = { factor = 3 date > <mốc> }` cho N1 (> 2022.1.16), N3 (> 2022.12.19), CR2 (> 2023.12.1), N2 (> 2025.2.4).

| Nhóm | `base` | Historical (`VIE_ai_historical`) | Western/Reform (`VIE_ai_path_reformish`) | Hardline/Nationalist (`VIE_ai_path_security`) |
|---|---:|---|---|---|
| Node chuỗi chung | 60 | — | — | — |
| Công binh (CB) | 20 | — | — | — |
| FM1 Cơ động | 40 | ×0,25 | ×1,5 | ×0,25 |
| FR1 Chính quy | 40 | ×1,5 | ×1 | ×1 |
| FD1 Chiều sâu | 40 | ×1 | ×0,25 | ×1,5 |
| PS Cơ động chiến lược | 40 | ×1,5 | ×1,5 | ×0,5 |
| PT Phòng thủ khu vực và dự bị | 40 | ×1,5 | ×0,75 | ×1,5 |
| Gốc lĩnh vực sở trường (`VIE_lf_fav_*`) | 60 | | | |
| Gốc lĩnh vực không sở trường | 20 | | | |

PS và PT ngang nhau ở Historical (R4). Tỉ lệ này khác 3.9 của báo cáo (0,5 : 3) có chủ ý.

## 5.7 · Event (`namespace = vie_lf`, scheduler p17)

Ba pop-up và hai ẩn, đều `is_triggered_only`. Mỗi event: **một** scripted effect `VIE_lf_ms_*_apply` chứa phần hiệu ứng để option và fallback không lệch nhau (mẫu của Trục 2, mục 6.2). Điều kiện lịch dùng khuôn `VIE_event_scheduler_p15`: ngày → `VIE_popup_cd` → fallback im lặng sau 6 tháng.

| ID | Mốc | Loại | Nếu focus liên quan **chưa** xong | Nếu **đã** xong |
|---|---|---|---|---|
| `vie_lf.1` | 2022.1.17 Nghị quyết 05 | pop-up | N1: `reduce_focus_completion_cost` −35 ngày | +15 XP, +25 PP |
| `vie_lf.2` | 2022.12.20 Nghị quyết 1657 | **ẩn** | N3: −24 ngày | +10 XP |
| `vie_lf.3` | 2023.12.2 Quân đoàn 12 | pop-up | CR2: −35 ngày; **mọi người chơi** tổ chức +1 (`VIE_af_army_org_factor`); thêm +0,5 nếu `VIE_lf_regular` | như bên trái, không giảm cost |
| `vie_lf.4` | 2024.12.15 Quân đoàn 34 | **ẩn** | tổ chức +0,5 cho mọi người chơi | như bên trái |
| `vie_lf.5` | 2025.2.5 hợp nhất Hậu cần – Kỹ thuật | pop-up | N2: −24 ngày; hậu cần −2 cho mọi người chơi | hậu cần −2 (đã có) và +10 điểm chỉ huy |

Chiều ngược lại, event **không** phụ thuộc người chơi đã đi N1 hay chưa ("nổ cho mọi người chơi", báo cáo 8.4). Catch-up (`VIE_catch_up = 1`): chỉ đặt cờ mốc, không pop-up. Ảnh event: dùng tạm ảnh có sẵn (`GFX_VIE_report_event_vie_proc_army_14`…) cho đến khi thêm 5 mục vào `EVENTS` của `tools/build_vie_event_pictures.py`.

## 5.8 · Decision (6, trong `VIE_military_readiness_category`)

Tất cả: `icon = GFX_decision_generic_army_support`, `visible` theo focus, `available = { has_war = no }` (trừ ghi chú), `ai_will_do = { base = 10–20 ; factor 0 khi VIE_def_ind_bankrupt }`. Phần thưởng đặt trong `remove_effect` (sau `days_remove`), log đầu mỗi khối effect (chuẩn MD `decision-reference.md`).

| ID | Mở từ | PP | Thời gian | Cooldown (`days_re_enable`) | Thưởng | So với báo cáo |
|---|---|---:|---:|---:|---|---|
| `VIE_dec_lf_train_terrain` | CR1 | 35 | 90 | 545 | +10 XP; ý tưởng tạm `terrain_penalty_reduction` +5% 180 ngày | gộp "rừng núi" |
| `VIE_dec_lf_train_urban` | CR1 | 35 | 90 | 545 | +10 XP; ý tưởng tạm `urban_attack_factor` +5% 180 ngày (**kiểm tên**) | giữ |
| `VIE_dec_lf_joint_arms` | CR1 | 35 | 90 | 545 | +10 XP (+15 nếu `VIE_lf_regular` và CAP xong); tổ chức +2% 90 ngày | giữ, đọc trạng thái CR/CAP (R1) |
| `VIE_dec_lf_rapid_response` | PS | 50 | 60 | 545 | +20 XP; tốc độ +5% 90 ngày | +10% → +5% (G2) |
| `VIE_dec_lf_mobilize_people` | PT | 40 | 120 | 730 | +40 000 nhân lực; dig-in +2,5% 180 ngày | 50 000 → 40 000, +5% → +2,5% |
| `VIE_dec_lf_total_mobilization` | CR1 | 65 | 90 | 1095 | +100 000 nhân lực; −5% ổn định (`add_stability = -0.05`, một lần); dig-in +5% 180 ngày | 200 000 → 100 000 |

`VIE_dec_lf_total_mobilization` `available`: `OR { VIE_lf_depth ; VIE_lf_dev_territorial ; has_war = yes ; VIE_scs_escalated_trigger = yes }` ("căng thẳng cao" dùng trigger có thật của repo; báo cáo không nêu tên).
XP dùng đúng mẫu repo: `has_selected_land_grand_doctrine = yes → add_mastery { folder = land }`, ngược lại `army_experience` (mẫu `VIE_limited_war_doctrine`, `VIE_un_peacekeeping`); bọc thành `VIE_lf_xp_10/15/20/25` (literal, tránh nhận biến ở `add_mastery`).

Ước tính XP: ≈ 29 XP/năm từ các decision mới (báo cáo) cộng 15 XP/năm của `VIE_exercise_military_region`; trần XP của MD là 1000 nên không chạm trần.

## 5.9 · Mẫu sư đoàn (FM2, FD2)

Báo cáo 3.7 cho phép Trục 3 tạo hai mẫu mới. Token lấy từ `VIE_2000_nsb.txt` (NSB và non-NSB giống nhau):

- **Cụm cơ động** (FM2): `armor_Bat ×2` · `Mech_Inf_Bat ×4` · `SP_Arty_Bat ×2`, `support = { SP_AA_Battery }`, `regimental_support = { armor_Recce_Comp }`. Không cấp trang bị, không tạo đơn vị: chỉ `add_division_template`.
- **Dân quân khu vực** (FD2): `L_Inf_Bat ×6` (hai cột × ba hàng), không support.

Template trống không tốn gì; người chơi tự đặt sản xuất.

## 5.10 · Layout

Cả 29 focus còn lại neo vào **N1** (`relative_position_id = VIE_lf_army_reform`, khai báo trước tất cả, 0 forward-ref); N1 neo vào `VIE_modernize_vpa` với `x = 12, y = 1`, tức abs **(278, 2)**. Vùng x 215–299 trống hoàn toàn (đo: chỉ có `VIE_modernize_vpa` và 4 focus Trục 2 ở x 264–268; dải an ninh x 304–308 ở y 24–27).

| Hàng (abs y) | Focus (dx, dy so với N1 → abs x) |
|---|---|
| 2 | N1 (0,0 → 278) |
| 3 | N2 (−2,1 → 276) · N3 (+2,1 → 280) |
| 4 | BB1 (−6,2 → 272) · TG1 (−2,2 → 276) · PB1 (+2,2 → 280) · CB (+6,2 → 284) |
| 5 | BB2 (−6,3) · TG2 (−2,3) · PB2 (+2,3) |
| 6 | HD (0,4 → 278) |
| 7 | CR1 (0,5) |
| 8 | FM1 (−6,6 → 272) · FR1 (0,6 → 278) · FD1 (+6,6 → 284) |
| 9 | FM2 (−6,7) · FR2 (0,7) · FD2 (+6,7) |
| 10 | PS (−3,8 → 275) · PT (+3,8 → 281) |
| 11 | CR2 (0,9) |
| 12 | L1 (−6,10) · A1 (0,10) · Y1 (+6,10) |
| 13 | L2 (−6,11) · A2 (0,11) · Y2 (+6,11) |
| 14 | MOD (0,12) |
| 15 | CR3 (0,13) |
| 16 | CAP (0,14) |

Khoảng cách tối thiểu cùng hàng = 4 (quy tắc "gap ≥ 2"), con luôn `y >` cha. Đường kẻ CB → HD và PS/PT chéo nhau nhìn xấu nhưng đúng; `tools/audit/audit.py` không kiểm đường kẻ, nên cần mở cây trong game chỉnh bằng tay sau bước 2–4 (đã làm vậy ở Trục 2).

---

# PHẦN 6 — PLAN CODE TRỤC 3

Nhánh: `truc3-force-building` từ `main`. Mỗi bước một commit; chạy bộ kiểm tĩnh (mục 6.4) trước khi commit.

## 6.1 · File-by-file

| # | File | Việc | Ước lượng dòng |
|---:|---|---|---:|
| 1 | `common/scripted_triggers/VIE_md_triggers_p17.txt` | **MỚI**: `VIE_lf_gate_open`, `VIE_lf_arm_slot_free`, `VIE_lf_cap_slot_free`, `VIE_lf_arm_done_3`, `VIE_lf_cap_done_2`, `VIE_lf_fav_land/_ad/_cyber`, `VIE_lf_mobilize_gate` | ~70 |
| 2 | `common/scripted_effects/VIE_md_effects_p17.txt` | **MỚI**: `VIE_lf_refresh`, `VIE_lf_xp_10/15/20/25`, 30 `VIE_lf_<mã>_reward`, `VIE_lf_ms_*_apply` ×5, `VIE_lf_create_template_mobile/_militia`, `VIE_event_scheduler_p17` | ~520 |
| 3 | `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt` | thêm 4 dòng modifier (5.5) trước `# GEN:vars end` | +4 |
| 4 | `common/on_actions/VIE_md_on_actions_startup.txt` | **vá X1** + khối `VIE_lf_vars_init` | +16 |
| 5 | `common/on_actions/VIE_md_on_actions.txt` | nối `VIE_event_scheduler_p17 = yes` | +1 |
| 6 | `common/scripted_effects/VIE_md_effects_p3.txt` | nối p17 vào `VIE_catch_up_schedule` | +1 |
| 7 | `common/national_focus/VIE_md_focus.txt` | 30 focus ở cuối file, sau khối Trục 2 | ~1 050 |
| 8 | `common/ideas/VIE_md_ideas_lf.txt` | **MỚI**: 6 ý tưởng tạm (`VIE_lf_idea_terrain_drill`, `_urban_drill`, `_joint_arms`, `_rapid_response`, `_mobilized_people`, `_total_mobilization`) | ~80 |
| 9 | `common/decisions/VIE_md_decisions_lf.txt` | **MỚI**: 6 decision, khối `VIE_military_readiness_category = { }` | ~230 |
| 10 | `events/VIE_land_force.txt` | **MỚI**: `add_namespace = vie_lf` + 5 event | ~150 |
| 11 | `common/scripted_localisation/VIE_md_lf_alt.txt` | **MỚI**: 4 `defined_text` nhãn ALT | ~50 |
| 12 | `localisation/english/VIE_md_events_p17_l_english.yml` | **MỚI** (BOM): ~115 key | ~140 |
| 13 | `localisation/english/replace/VIE_md_vi_tt_l_english.yml` | +6 key `VIE_tt_*` | +6 |
| 14 | `tools/audit/lf_balance.py` | **MỚI**: bảng 5.4 + kiểm ròng + trần (Phụ lục B) | ~120 |
| 15 | `tools/TESTING.md` | thêm mục Trục 3 (mục 7 dưới đây) | +60 |
| 16 | `events/VIE_proc_army.txt`, `common/decisions/VIE_md_def_industry.txt` | **tùy chọn** (bước 8): `ai_chance` / `ai_will_do` theo cờ hướng | +20 |

## 6.2 · Thứ tự thi công (9 bước)

| Bước | Việc | Kiểm chứng |
|---|---|---|
| **0** | File 1, 3, 4, 13, 14. **Vá X1.** Thêm 4 modifier. | `live.py` 0 missing; `lf_balance.py` in đúng bảng 5.4 (ròng ba hướng ≤ 0,4 chênh, trần G2); console `effect add_to_variable = { VIE_af_conscription_factor = 0.01 }` thấy dòng trong tooltip `VIE_armed_forces_modifier` |
| **1** | File 2 (khung): `VIE_lf_refresh`, `VIE_lf_xp_*`, scheduler **rỗng** + file 5, 6 | `on_monthly` chạy không báo lỗi; `error.log` sạch |
| **2** | File 7 phần 1: N1–N3, 7 node binh chủng, HD, CR1 (12 focus) + reward tương ứng | `audit.py`: 0 dangling, 0 forward-ref, 0 cycle, 0 trùng tọa độ; chơi: N1 xám trước 11/2/2019 (plausible), mở khi `free` + level 2 |
| **3** | File 7 phần 2: FM1/FR1/FD1, FM2/FR2/FD2, PS, PT, CR2 (9 focus) + 2 mẫu sư đoàn | ME ba chiều: chọn FR1 thì FM1 và FD1 xám; PS/PT loại trừ nhau; `reduce_focus_completion_cost` −14 ngày gốc sở trường |
| **4** | File 7 phần 3: 6 node năng lực, MOD, CR3, CAP (9 focus) | Giới hạn 2/3: sau 2 gốc thì gốc thứ ba xám; MOD xám khi `cap_done < 2`; audit 30/30 |
| **5** | File 8, 9: 6 ý tưởng tạm + 6 decision | Decision hiện sau CR1/PS/PT; cooldown; ý tưởng tạm hiện 180 ngày rồi mất |
| **6** | File 10, 11, scheduler p17 đầy đủ | Event đúng ngày; `VIE_popup_cd` tôn trọng; catch-up chỉ đặt cờ; nhãn ALT đổi tại mốc |
| **7** | File 12: loc toàn bộ | `verify_all_loc.py` PASS (BOM, 0 trùng, 0 mồ côi); `ev.py` 0 thiếu loc |
| **8** | (Tùy chọn) AI soft-link Trục 1/2, bảng 6.3 | Không đổi điều kiện mở; chỉ đổi trọng số |
| **9** | File 15 + cập nhật `VIE_cross_axis_review.md` (thêm bảng cờ Trục 3) | Checklist mục 7 |

## 6.3 · Bước 8: AI soft-link (tùy chọn)

Báo cáo 4.2, chuyển sang cờ thật. Chỉ **cộng trọng số** `ai_chance` / `ai_will_do`, không đổi `visible/available`/hiệu ứng. Nếu bỏ bước này Trục 1 và 2 vẫn nguyên vẹn.

| Nơi | Hướng | Việc |
|---|---|---|
| `vie_proc_army.18` option A, `.19` option A/B, `.30` option B, `.35` option A, `.38` option A | `VIE_lf_regular` | thêm `modifier = { factor = 1.3 has_country_flag = VIE_lf_regular }` |
| `vie_proc_army.8` option A (Igla kèm quyền SX) | `VIE_lf_depth` | cùng khuôn |
| `VIE_dec_pth` (D3), `VIE_dec_xcb01`, `VIE_dec_xcb01_fast` (D6) | `VIE_lf_regular` | trong `ai_will_do` |
| `VIE_dec_tl01` (D9) | `VIE_lf_depth` | trong `ai_will_do` |

## 6.4 · Bộ kiểm tĩnh sau mỗi bước

```bash
python3 tools/verify_all_loc.py
python3 tools/audit/live.py     # 0 missing ở mọi nhóm
python3 tools/audit/ev.py       # 0 trùng, 0 orphan, 0 thiếu loc
python3 tools/audit/audit.py    # 0 dangling, 0 forward-ref, 0 cycle, 0 trùng tọa độ
python3 tools/audit/lf_balance.py
```

## 6.5 · Khung code (mẫu để bước 2–6 chép theo)

**Khởi tạo biến (bước 0), thay khối Trục 2 hiện tại**
```pdx
if = {
	limit = { NOT = { has_country_flag = VIE_def_ind_vars_init } }
	set_variable = { VIE_def_industry_level = 0 }
	set_variable = { VIE_def_ind_export_count = 0 }
	set_country_flag = VIE_def_ind_vars_init
}
if = {
	limit = { NOT = { has_country_flag = VIE_lf_vars_init } }
	set_variable = { VIE_lf_arm_count = 0 }
	set_variable = { VIE_lf_arm_done = 0 }
	set_variable = { VIE_lf_cap_count = 0 }
	set_variable = { VIE_lf_cap_done = 0 }
	set_country_flag = VIE_lf_vars_init
}
```

**Trigger cổng (file 1)**
```pdx
VIE_lf_gate_open = {
	OR = {
		date > 2019.2.10
		AND = {
			VIE_ai_free = yes
			date > 2012.12.31
			VIE_def_ind_level_ge_2 = yes
		}
	}
}
VIE_lf_fav_land  = { has_country_flag = VIE_lf_depth }
VIE_lf_fav_ad    = { has_country_flag = VIE_lf_regular }
VIE_lf_fav_cyber = { has_country_flag = VIE_lf_mobile }
```

**Focus gốc (N1) và node đầu binh chủng (file 7)**
```pdx
focus = {
	id = VIE_lf_army_reform
	icon = army_reform
	x = 12
	y = 1
	relative_position_id = VIE_modernize_vpa
	cost = 10
	prerequisite = { focus = VIE_modernize_vpa }
	search_filters = { FOCUS_FILTER_ARMY }
	available = { VIE_lf_gate_open = yes }
	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_army_reform"
		VIE_lf_n1_reward = yes
	}
	ai_will_do = {
		base = 60
		modifier = { factor = 3 date > 2022.1.16 }
		modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
	}
}

focus = {
	id = VIE_lf_arm_infantry_org
	icon = army_planning
	x = -6
	y = 2
	relative_position_id = VIE_lf_army_reform
	cost = 7
	prerequisite = { focus = VIE_lf_logistics_merge }
	prerequisite = { focus = VIE_lf_basic_training }
	search_filters = { FOCUS_FILTER_ARMY }
	available = { VIE_lf_arm_slot_free = yes }
	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_arm_infantry_org"
		if = {
			limit = { VIE_lf_arm_slot_free = yes }
			add_to_variable = { VIE_lf_arm_count = 1 }
			VIE_lf_bb1_reward = yes
		}
	}
	ai_will_do = {
		base = 60
		modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
	}
}
```
HD đòi **OR** bốn binh chủng:
```pdx
focus = {
	id = VIE_lf_combined_arms
	...
	prerequisite = {
		focus = VIE_lf_arm_infantry_train
		focus = VIE_lf_arm_armor_train
		focus = VIE_lf_arm_arty_train
		focus = VIE_lf_arm_engineers
	}
	available = { VIE_lf_arm_done_3 = yes }
```
ME ba chiều (FR1; FM1 và FD1 lặp lại đối xứng):
```pdx
	prerequisite = { focus = VIE_lf_command_reform_1 }
	mutually_exclusive = { focus = VIE_lf_fs_mobile_force focus = VIE_lf_fs_depth_defence }
```

**Phần thưởng theo cờ hướng (file 2), ví dụ CR2**
```pdx
VIE_lf_cr2_reward = {
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.005 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_speed_factor = 0.01 tooltip = VIE_tt_army_speed_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_army_defence_factor = 0.015 tooltip = VIE_tt_army_defence_factor }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.01 tooltip = VIE_tt_max_dig_in_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_refresh = { force_update_dynamic_modifier = yes }
```
Số cho từng node chép từ bảng 5.4. Dùng literal như trên (không dùng biến tạm) vì tooltip của repo đã chạy tốt với literal; ô sở trường (×1,5) viết thành nhánh `if = { limit = { VIE_lf_fav_ad = yes } ... } else = { ... }` riêng.

**Decision (file 9), ví dụ**
```pdx
VIE_military_readiness_category = {
	VIE_dec_lf_train_terrain = {
		icon = GFX_decision_generic_army_support
		cost = 35
		days_re_enable = 545
		visible = { has_completed_focus = VIE_lf_command_reform_1 }
		available = { has_war = no }
		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_dec_lf_train_terrain"
		}
		days_remove = 90
		remove_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_dec_lf_train_terrain (complete)"
			VIE_lf_xp_10 = yes
			add_timed_idea = { idea = VIE_lf_idea_terrain_drill days = 180 }
		}
		ai_will_do = {
			base = 15
			modifier = { factor = 0 VIE_def_ind_bankrupt = yes }
		}
	}
}
```

**Scheduler (file 2), ví dụ `vie_lf.3`** (cùng khuôn `VIE_event_scheduler_p15`)
```pdx
VIE_event_scheduler_p17 = {
	if = {
		limit = { NOT = { check_variable = { VIE_catch_up = 1 } } }
		if = {
			limit = {
				date > 2023.11.30
				NOT = { has_country_flag = VIE_lf_ms_corps12 }
			}
			if = {
				limit = { NOT = { has_country_flag = VIE_popup_cd } }
				set_country_flag = VIE_lf_ms_corps12
				set_country_flag = { flag = VIE_popup_cd days = 45 }
				country_event = { id = vie_lf.3 days = 3 random_days = 15 }
			}
			else_if = {
				limit = { date > 2024.5.31 }
				set_country_flag = VIE_lf_ms_corps12
				VIE_lf_ms_corps12_apply = yes
			}
		}
		# ... .1 .2 .4 .5 tương tự
	}
}
```

---

# PHẦN 7 — CHECKLIST TEST (cần máy có HOI4)

**Cấu hình và log**
- [ ] `error.log` grep `VIE_lf_`, `vie_lf`, `VIE_dec_lf_`, `reduce_focus_completion_cost`, `force_update_dynamic_modifier`, `army_personnel_cost`, `urban_attack_factor`.
- [ ] Số slot focus của MD thật = 1? (G1) Nếu ≥ 2: chạy lại bảng 8.12 và test vượt giới hạn.
- [ ] **X1**: load một save năm 2015 sau khi làm xong vài decision Trục 2: `VIE_def_industry_level` không về 0.

**Cổng và cây**
- [ ] N1 xám trước 11/2/2019 ở `plausible`/`historical`; ở `free` mở khi `VIE_def_industry_level ≥ 2` và sau 2012.
- [ ] Binh chủng: sau 3 node đầu, node đầu thứ tư xám; BB2/TG2/PB2 vẫn bấm được; HD xám đến khi `arm_done ≥ 3`; mọi tổ hợp 3/4 mở được HD (đặc biệt BB+TG+CB).
- [ ] ME ba chiều FM1/FR1/FD1 và hai chiều PS/PT; PS/PT mở được từ FM2, FR2 **hoặc** FD2.
- [ ] Lĩnh vực: sau hai gốc, gốc thứ ba xám; MOD xám khi `cap_done < 2`; chọn hai lĩnh vực bất kỳ đều ra MOD.
- [ ] Cờ sở trường: sau FR1, gốc A1 rẻ hơn 14 ngày so với gốc L1/Y1 (tooltip thời gian).

**Số và modifier**
- [ ] Tooltip `VIE_armed_forces_modifier` đổi ngay sau mỗi node (nếu không, `force_update_dynamic_modifier` có hiệu lực?).
- [ ] `army_attack_factor`, `conscription_factor` hiện dòng riêng; hai modifier chi phí MD: +2% là +2% hay ×1,02? (ảnh hưởng FM1/FR1/PS/PT).
- [ ] `reduce_focus_completion_cost cost = 35` làm N1 từ 70 xuống 35 **ngày** (G6), không phải tuần.
- [ ] Tổng cuối đường đầy đủ khớp `lf_balance.py` (tốc độ ≤ 25, dig-in ≤ 26, tổ chức ≤ 21).
- [ ] Mẫu "Cụm cơ động" và "Dân quân" xuất hiện trong bảng mẫu sư đoàn, không báo lỗi regiment.

**Decision và event**
- [ ] 6 decision nằm đúng `VIE_military_readiness_category` (khối trùng tên ở hai file có gộp không?), cạnh 4 decision cũ.
- [ ] `days_re_enable` đếm từ lúc bấm hay lúc xong? (ảnh hưởng ước tính XP/năm, mục 5.8.)
- [ ] Ý tưởng tạm biến mất sau 180 ngày; tên modifier đô thị đúng.
- [ ] Event: `event vie_lf.1` … `.5`; ngày; không hai pop-up trong 45 ngày; 2024 không có pop-up `vie_lf`; catch-up chỉ đặt cờ.
- [ ] Đo lại số pop-up 2022/2023/2024/2025 sau khi thêm (luật ≤ 7/năm).

**AI (bước 8)**
- [ ] Quan sát một ván AI (`observe`): có đi Trục 3 sau 2019, hướng chọn đúng theo path, không kẹt (`bankruptcy_incoming_collapse`).

---

# PHỤ LỤC A — 6 decision "nhóm chung" (Q14, tùy chọn)

Báo cáo 8.14 đặt ngoài Trục 3 Lục quân. Nếu làm, cổng dùng trigger **có thật** (R2), cũng vào `VIE_military_readiness_category`:

| Decision | Cổng đề xuất | Ghi chú |
|---|---|---|
| Huấn luyện chống ngầm | thuộc plan Hải quân | Cần `VIE_var_hulls_*` của báo cáo hải quân |
| Huấn luyện BVR | thuộc plan Không quân | Cần trục Không quân |
| Diễn tập song phương | `has_completed_focus = VIE_us_comprehensive_partnership` hoặc `VIE_india_partnership` hoặc `VIE_japan_partnership` | thay "quan hệ ≥ ngưỡng" chưa định nghĩa |
| Diễn tập đa phương | `has_completed_focus = VIE_asean_integration` | thay cờ chưa tồn tại |
| Cứu trợ thảm họa (HADR) | `has_country_flag = VIE_disaster_prepared` | `VIE_disaster_events.txt` đã có sự kiện thiên tai |
| Triển khai gìn giữ hòa bình | `has_completed_focus = VIE_un_peacekeeping` | focus đã có XP + opinion; decision chỉ lặp lại phần XP |

Chỉ bốn dòng cuối là việc của Lục quân/Chung; hai dòng đầu để plan Hải quân và Không quân.

---

# PHỤ LỤC B — `tools/audit/lf_balance.py` (bước 0)

Dữ liệu: bảng 5.4 (giá trị mới) và hệ số `W`, `S`. In ba thứ và **fail** nếu vượt ngưỡng:
1. điểm từng node theo `W' = W/S` so với điểm báo cáo (lệch ≤ 0,4);
2. ròng ba hướng FFS (lệch nhau ≤ 0,4);
3. tổng cộng dồn cho 9 đường (3 hướng × 3 cặp lĩnh vực) và so với trần: tốc độ ≤ 25, dig-in ≤ 26, tổ chức ≤ 21, phòng thủ ≤ 16, nhân lực ≤ 12, tấn công ≤ 10, hậu cần ≥ −10.

Kết quả tôi đã chạy (cùng dữ liệu): tốc độ tối đa 24,5 · dig-in 25,5 · tổ chức 21 · phòng thủ 15,5 · nhân lực 12 · tấn công 10 · hậu cần −10.

---

# PHỤ LỤC C — Những gì chưa kiểm chứng

| Hạng mục | Rủi ro | Cách xử lý |
|---|---|---|
| Số slot focus = 1 | trung bình | checklist mục 7; bảo hiểm count đã có |
| `on_startup` chạy lại khi load (X1) | cao nếu đúng | guard vô hại cả hai trường hợp |
| `reduce_focus_completion_cost` đơn vị ngày | trung bình | suy từ tiền lệ `VIE_code_of_conduct`; test bắt buộc |
| Đơn vị hai modifier chi phí MD | trung bình | test; đổi 4 số nếu sai |
| `urban_attack_factor` có tồn tại | thấp | thay `terrain_penalty_reduction` nếu không |
| Hai khối category trùng tên ở hai file có gộp | thấp | nếu không: chuyển 6 decision vào `VIE_md_decisions.txt` |
| `days_re_enable` bắt đầu đếm lúc nào | thấp | ảnh hưởng XP/năm |
| Nghị quyết 1657-NQ/QUTW (20/12/2022) | thấp | chưa tra lại; đổi mốc của `vie_lf.2` nếu sai |
| PP thu nhập thật của VIE (M ≈ 70) | trung bình | neo vào decision cũ; đo rồi chỉnh 6 số |

---

# NGUỒN

- Báo cáo Lục quân VIE — Trục 1, 2, 3, mục III, VIII, IX, bảng 9.10 (repo).
- Repo: `common/national_focus/VIE_md_focus.txt` (cụm `VIE_peoples_defence`, Trục 2), `common/decisions/VIE_md_decisions.txt`, `common/decisions/categories/VIE_md_categories.txt`, `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt`, `common/on_actions/VIE_md_on_actions_startup.txt`, `common/scripted_triggers/VIE_md_triggers_p4.txt` và `_p15.txt`, `common/scripted_effects/VIE_md_effects_p15.txt`, `common/ideas/VIE_md_ideas_p2.txt`, `events/VIE_md_p11.txt:193`, `tools/TESTING.md`, `tools/audit/md_ref/VIE_2000_nsb.txt`.
- Các review sẵn có: `VIE_truc1_review_and_plan.md` (A1), `VIE_truc2_review_and_plan.md` (A1, L4), `VIE_cross_axis_review.md`, báo cáo hải quân bản 2.4 (mục 2, 3.1, 11).
- MD (GitHub): [`common/defines/MD_defines.lua`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/defines/MD_defines.lua), [`.claude/docs/focus-tree-reference.md`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/.claude/docs/focus-tree-reference.md), [`.claude/docs/decision-reference.md`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/.claude/docs/decision-reference.md), [`.claude/docs/md-custom-modifiers.md`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/.claude/docs/md-custom-modifiers.md), [`common/modifier_definitions/money_modifier_definitions.txt`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/modifier_definitions/money_modifier_definitions.txt).
- Mốc lịch sử đã đối chiếu: [Báo Pháp luật VN / Chính phủ về Nghị quyết 05-NQ/TW](https://xaydungchinhsach.chinhphu.vn/co-ban-hoan-thanh-dieu-chinh-to-chuc-luc-luong-quan-doi-tinh-gon-manh-119250213160854185.htm), [Quân đoàn 12](https://xaydungchinhsach.chinhphu.vn/cong-bo-quyet-dinh-thanh-lap-quan-doan-12-quan-doan-tinh-gon-manh-dau-tien-cua-quan-doi-nhan-dan-viet-nam-119231202122003205.htm), [Quân đoàn 34](https://xaydungchinhsach.chinhphu.vn/cong-bo-quyet-dinh-thanh-lap-quan-doan-34-119241215103454169.htm), [Hậu cần – Kỹ thuật](https://dantri.com.vn/thoi-su/bo-quoc-phong-sap-nhap-tong-cuc-hau-can-va-tong-cuc-ky-thuat-20250205151535963.htm).
