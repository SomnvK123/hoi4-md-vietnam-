# REVIEW TRỤC 1 HẢI QUÂN (MUA SẮM) + PLAN CODE

> Đầu vào: `Báo cáo hải quân Việt Nam – 3 trục … (bản 2.4).md`, mục 1–4, 7, 8, 12–13 và 16–18 (phần liên quan Trục 1).
> Đối chiếu với repo @ `e4f3215` và dữ liệu MD trong `tools/audit/md_ref/` (`SOV_Russia.txt`, `tech_naval.txt`, `VIE_Vietnam.txt`, `00_budget_effects.txt`).
> Phạm vi: chỉ Trục 1 (6 chương trình + Decision `P_late`). Trục 2/3 chỉ nhắc khi Trục 1 phải nối vào.
>
> **KẾT LUẬN: logic cốt lõi của Trục 1 (cửa sổ + retry, Historical luôn có, Sigma xác định, Molniya hai pha) ĐÚNG và giữ nguyên.
> Nhưng bản 2.4 chưa code được: có 5 lỗi chặn, 7 chỗ sai so với MD/mod, 6 lỗ hổng logic.**
> Báo cáo gốc chưa bị sửa. Bản sửa của Trục 1 nằm ở Phần 3, plan ở Phần 4.

---

# PHẦN 1 — 5 LỖI CHẶN

## A1 · Báo cáo viết cho cây focus v7, repo đang ở v11: không còn focus hải quân nào

Quét `common/national_focus/VIE_md_focus.txt` (live). Các focus báo cáo dựa vào:

| Focus | Báo cáo dùng làm | Còn sống? |
|---|---|---|
| `VIE_navy_modernization` | thưởng Trục 1 (Gepard/Bastion/Sigma lớn hơn), điều kiện T1 của Trục 3 | ❌ chỉ có trong `v11_removed_military_all_subbranches.txt` |
| `VIE_russian_arms_deals` | thưởng Trục 1 (Kilo/Molniya) | ❌ chỉ có trong `.bak` (mất từ v9) |
| `VIE_domestic_corvettes` | mục 9.1 "gỡ" | ❌ đã gỡ rồi |
| `VIE_navy_blue_water`, `VIE_path_maritime_denial` | mục 9.1 "giữ nguyên node Doctrine" | ❌ đã gỡ ở v11 |
| `VIE_defence_industry_modernization` | tiền đề Focus 1 Trục 2 | ❌ không tồn tại ở đâu |

Hệ quả cho Trục 1: không có lỗi chặn nổ, vì thiết kế đã tách Focus khỏi cổng (chỉ thưởng). Nhưng **hai điều kiện thưởng không bao giờ đúng** và mục 9.1 mô tả việc di chuyển không còn đối tượng.
Hệ quả cho Trục 2: Focus 1 không mở được, nên `VIE_cap_ba_son_yard` không bao giờ được đặt và **Molniya pha 2 chết**. Việc này nằm ngoài Trục 1 nhưng chặn lát cắt Molniya (xem Q2).

Tiền lệ trong repo: Trục 1 lục quân giải bằng một file trigger gom mọi cổng (`common/scripted_triggers/VIE_md_triggers_p14.txt`). Làm y vậy.

## A2 · Mã giao tàu cũ (`VIE_event_scheduler_p12`) còn sống và báo cáo không biết

`common/scripted_effects/VIE_md_effects_p12.txt` đang giao 4 Gepard và 6 Kilo bằng `create_ship`, gate bằng cờ `VIE_gepard_contract` / `VIE_kilo_contract`. Không còn chỗ nào đặt hai cờ này (focus đã xoá ở v11), nên hiện là mã chết. Rủi ro:

- Vi phạm Quy tắc 1 ("không nhận thiết bị hai lần") nếu có ai đặt lại cờ cũ khi Trục 1 mới đã giao.
- Ngày giao của p12 mâu thuẫn báo cáo (Kilo thứ nhất 2014-07-31 so với 2014-01-15; thứ tư 2016-01 so với 2015-06-30). Báo cáo có nguồn (mục 8.3), p12 không.
- Gán biến thể ngược: p12 cho lô 2011 dùng `"Gepard Class"` (có ngư lôi) và lô 2017 dùng `"Gepard 3.9 Class"`. Lịch sử và báo cáo là ngược lại (xem B3).
- Đã có sẵn `VIE_kilo_flotilla_idea` (+5% tấn công tàu ngầm, +3% XP hải quân) cùng loc tiếng Việt. Báo cáo không nhắc, nên tái dùng.

## A3 · Mục 16.1/17.1 chọn `on_monthly_VIE`: sai so với kiến trúc mod

`common/on_actions/VIE_md_on_actions.txt` ghi rõ lý do dùng `on_monthly` chung với `original_tag = VIE`: sau nội chiến, người thắng có thể là tag nổi loạn có `original_tag = VIE`, và `on_monthly_VIE` không chạy cho tag đó. MD cũng đã có `on_monthly_VIE` của riêng nó (`99_VIE_on_actions.txt`, bắn `vietnam.1`).

Báo cáo cũng thiếu hai thứ mà mọi scheduler p1–p17 đều có:
- `VIE_catch_up` (nội chiến xong, người thắng không được nhận Molniya 2003 hay Kilo 2009 theo kiểu bắn event, chỉ đặt cờ "đã xảy ra").
- `VIE_popup_cd` (45 ngày): `VIE_naval_monthly_pulse` ở 17.2 bắn `country_event` thẳng, không đọc cờ này.

`VIE_catch_up_schedule` (`VIE_md_effects_p3.txt:114`) cũng phải gọi scheduler hải quân; nếu quên thì người thắng nội chiến sẽ không có cờ lịch sử.

## A4 · `create_ship … creator = VIE` + variant trong `history/countries/VIE - Vietnam.txt`: không làm được

- Repo không có thư mục `history/`. Submod không ghi đè được file quốc gia của MD.
- MD `VIE - Vietnam.txt` có **0** `create_equipment_variant` (đo trong `md_ref/VIE_Vietnam.txt`; `VIE_md_effects_p14.txt:105` ghi cùng kết luận). VIE mở đầu chỉ có `corvette_hull_1`.
- Mẫu đã chạy trong repo: `create_ship = { type = … equipment_variant = "…" creator = SOV name = "…" }` (p12). Biến thể tồn tại sẵn trong MD cho SOV:

| Báo cáo | Biến thể MD (SOV) | Hull |
|---|---|---|
| Molniya | `"Molniya Class"` (obsolete = yes, vẫn dùng được qua `creator`) | `corvette_hull_2` ✅ khớp 17.3 |
| Gepard 3.9 (lô I) | `"Gepard 3.9 Class"` (không ngư lôi, 2 bệ tên lửa + CIWS) | `frigate_hull_3` |
| Gepard ASW (lô II) | `"Gepard Class"` (có `module_torpedoes_3`, VLS) | `frigate_hull_3` |
| Kilo 636 | `"Improved Kilo Class"` | `attack_submarine_hull_2` |

- **Lỗ hổng lớn hơn:** `creator = SOV` đòi `country_exists = SOV` mỗi lần `create_ship`. Cổng pha 2 của Molniya (đóng nội địa tại Ba Son) cố ý KHÔNG đòi Nga tồn tại. Nếu Nga bị thôn tính, pha 2 vẫn "mở", `create_ship` hỏng, và theo PR #4473 mà báo cáo dẫn thì **tiền bị trừ, tàu không đến**.
  Cách vá (Phần 3, mục 3.4): pha 2 dùng biến thể **do VIE tự tạo** bằng `create_equipment_variant` trong scripted effect có cờ chặn tạo trùng (mẫu T-54M ở `VIE_md_effects_p14.txt:105-118` và `p15`), module chép từ biến thể SOV ở trên.

## A5 · Giao tàu bằng pop-up làm vỡ ngân sách pop-up

Mục 17.3 mỗi tàu giao là một `country_event` có `option` (popup). Đếm theo thiết kế: Kilo 6 + Gepard 2+2 + Molniya 2+6 = **18 popup giao hàng**, chưa tính event chọn. `tools/TESTING.md` cho mục tiêu ≤ 7 pop-up/năm và đo thực tế 2012 = 8, 2014 = 8 (đã vượt). 2014–2017 sẽ có thêm 4 Kilo + 3 Molniya đúng vào các năm đó.
Mod đã có quy ước: **giao hàng là Class C (im lặng, một cờ mỗi tàu)** (`p12`, `.6` của lục quân). Event chọn mới là Class B (đọc `VIE_popup_cd`).
Event `.12` (mốc 40%) và `.13` (kết thúc) ở 17.5 cũng là popup một nút bấm vô nghĩa. Đổi thành `hidden = yes`.

---

# PHẦN 2 — 7 CHỖ SAI SO VỚI MD VÀ MOD

## B1 · Số bậc hull ở bảng 16.2 sai

Đếm từ `tech_naval.txt`: corvette 1–**8**, frigate 1–**8**, destroyer 1–**7**, attack_submarine 1–**8**, helicopter_operator 1–**6**, carrier 1–**7** (báo cáo ghi 1–6, 1–6, 1–5, 1–6, 1–4, 1–5). Không ảnh hưởng 6 chương trình Trục 1 (chỉ dùng corvette_2, frigate_3, submarine_2) nhưng ảnh hưởng 1B. Sửa bảng 16.2.

## B2 · Sigma: chọn hull luôn, đừng để mở

Gepard 3.9 (≈ 2.100 t) đã là `frigate_hull_3` trong MD; Sigma 9814 (≈ 1.950 t) cùng cỡ. **Chọn `frigate_hull_3`** (đóng mục 18.1 #10). MD không có biến thể Sigma (không có file HOL trong `md_ref`, chưa kiểm được), nên Sigma cũng cần biến thể VIE tự tạo như pha 2 Molniya.

## B3 · Cấu hình Gepard 1/2/3 chỉ khớp được 2 biến thể

MD chỉ có hai biến thể Gepard. `VIE_gepard1_config`: 1 Standard → `"Gepard 3.9 Class"`, 2 ASW → `"Gepard Class"`. **Config 3 (phòng không) không có biến thể tương ứng.** Hoặc bỏ config 3, hoặc tạo thêm biến thể VIE. Khuyến nghị bỏ ở bản đầu (ít rủi ro nhất, không có nguồn lịch sử cho nó).
Lô II (2017–18) lịch sử là Gepard ASW, tức `"Gepard Class"`.

## B4 · `VIE_var_naval_budget_room` là biến sao chép, và Funding Gate nên dùng thẳng `treasury`

MD lưu ngân khố ở biến `treasury` (`modify_treasury_effect` làm `add_to_variable = { treasury = treasury_change }`, `00_budget_effects.txt:1491`; đơn vị tỷ USD). Một biến `naval_budget_room` tính lại hàng tháng là đúng loại biến phản chiếu mà mục 16.3 đã cấm. Cổng Sigma: một scripted trigger so `treasury` với chi phí (`set_temp_variable` rồi `check_variable`).
Lưu ý convention Trục 2 (`VIE_md_def_industry.txt`): thiếu tiền KHÔNG chặn Decision vì MD tự phát hành nợ. Sigma là ngoại lệ có chủ ý (cổng xác định), nên tooltip phải nói rõ "ngân khố ≥ X tỷ".

## B5 · Hết cửa sổ mà popup bị chặn thì mất chương trình lịch sử

Mục 3.1 đặt `_missed` và mở `P_late` khi qua `window_end` mà chưa ký. Quy ước Class B của mod là: nếu popup chỉ bị `VIE_popup_cd` chặn tới hết cửa sổ thì **áp dụng kết quả lịch sử im lặng** (`VIE_fb_*`), không phạt người chơi vì lịch sự kiện dày (xem `VIE_md_effects_p14.txt:23-27`). Báo cáo không phân biệt hai nguyên nhân.
Vá: `_missed` chỉ đặt khi cổng thật sự không đạt (đối tác không tồn tại hoặc đang chiến tranh trong toàn cửa sổ); nếu cổng đạt mà chưa bắn được thì chạy `VIE_fb_naval_<p>` (ký hợp đồng lịch sử, im lặng).

## B6 · Namespace và tên

- Namespace `VIE_naval` viết hoa. Cả repo dùng chữ thường (`vie_proc_army`, `vie_pol` …). Dùng `vie_naval`.
- Tiền tố `VIE_dec_*_progress`, `_active`, `_done` (mục 7.5) đã bị 16.3 loại; giữ đúng theo 16.3.
- Log dùng `[Root.GetName]` như toàn repo (không phải `[This.GetName]`).
- Loc: `localisation/english/VIE_md_events_naval_l_english.yml` (nội dung tiếng Việt, UTF-8 **có BOM**) cộng `replace/` theo mẫu repo, kiểm bằng `tools/verify_all_loc.py`.

## B7 · `VIE_var_hulls_operational` chỉ đếm giao hàng, không phản ánh "trạng thái thế giới"

Quy tắc 6(c) gọi nó là trạng thái thế giới, nhưng nó chỉ tăng. Tàu bị chìm hoặc bị trừ vẫn tính. Đổi tên `VIE_var_hulls_delivered` và ghi rõ là đếm giao hàng (Focus 3 Trục 2 đòi "≥ 4 thân tàu từng giao", điều vẫn đúng với ý đồ). Nếu muốn đếm thật, dùng trigger đếm tàu của engine, nhưng cần thử trong game.

---

# PHẦN 3 — LỖ HỔNG LOGIC VÀ BẢN SỬA CỦA TRỤC 1

## 3.1 Giao hàng Molniya pha 1: nhánh 4 tàu chỉ nhận 2

Ở 17.2, hai điều kiện giao đều chặn `ru_delivered < 2`, nên lựa chọn alt "4 tàu" trả tiền 4 và chỉ nhận 2. Ngoài ra pulse bắn lại `VIE_naval.2` mỗi tháng nếu người chơi chưa bấm.
**Sửa:** mẫu p12, một cờ cho mỗi tàu (`VIE_molniya_s1` … `s4`), mỗi cờ có ngày giao tuyệt đối và điều kiện `VIE_molniya_ru_qty ≥ N`. Giao im lặng (Class C). Đây là cờ chuyển tiếp lịch sử hợp lệ theo 16.3.

## 3.2 Lịch giao cho đơn hàng alt chưa được định nghĩa

Báo cáo chỉ có ngày giao lịch sử cho số lượng lịch sử. Với 4 Gepard, 8 Kilo, 4 Bastion, 4 Molniya… không có ngày. **Quy tắc đề xuất:** tàu thứ N giao vào `max(ngày lịch sử của tàu N, ngày ký + lead_min)`; tàu vượt số lịch sử giao cách tàu cuối 6 tháng. Sàn "mốc lịch sử trừ 12 tháng" (mục 3.1) chỉ áp dụng cho `P_late` và đơn alt ký sớm.

## 3.3 Lịch Kilo và dữ liệu thiếu

Dùng các mốc có nguồn ở mục 8.3: tàu 1 = 2014-01-15, tàu 4 = 2015-06-30, tàu 5 = 2016-02, tàu 6 = 2017-01-20. **Tàu 2 và 3 chưa có nguồn**; tạm nội suy 2014-09 và 2015-01, ghi `# TODO(nguồn)` và thêm hàng vào bảng 8.3 khi tìm được. Bỏ ngày p12.

## 3.4 Biến thể tàu: quy tắc chọn

| Trường hợp | `creator` | Điều kiện |
|---|---|---|
| Hàng mua từ Nga (Molniya p1, Gepard I/II, Kilo) | `SOV` | `country_exists = SOV` đã nằm trong cổng ký; khi giao mà SOV mất thì dùng biến thể VIE (dưới) |
| Molniya pha 2 (Ba Son) | `VIE` | biến thể `"Molniya Class"` do VIE tự tạo |
| Sigma | `VIE` | biến thể `"Sigma Class"` tự tạo, `frigate_hull_3` |

Scripted effect `VIE_naval_ensure_variants` tạo biến thể VIE một lần (cờ chặn trùng), gọi trước mọi `create_ship creator = VIE`. Module chép từ khối SOV ở A4. **Rủi ro đã biết:** module cần tech; chưa chắc VIE mở được `module_radar_3`, `module_naval_missile_mount_quad`… Thêm vào danh sách thử (Phần 5). Nếu hỏng, lùi về giải pháp "pha 2 đòi SOV tồn tại tại thời điểm giao".

## 3.5 Bastion-P chưa nói nó làm gì trong game

HOI4 không có trang bị "hệ thống bờ". Báo cáo chỉ có biến số lượng và `VIE_bastion_deploy` mà không có hiệu ứng. Đề xuất: mỗi hệ thống giao thì xây `coastal_bunker` và `radar` ở tỉnh theo `VIE_bastion_deploy` (Bắc/Trung/Nam/phân tán), cộng dynamic modifier nhỏ, rồi đặt `VIE_ev_bastion_p_coastal_defence` (xem 3.7). Tỉnh cụ thể lấy từ MD (`10162` Cam Ranh, state 519; `10309` từng được dùng) — **phải đối chiếu `tools/audit/prov.py` trước khi dùng**.

## 3.6 Tham số "huấn luyện" của Kilo chưa có hiệu ứng thật

`VIE_kilo_training` (đầy đủ/cắt giảm) mô tả "readiness" mà HOI4 không có. Định nghĩa: đầy đủ = chi phí +X, một timed idea +XP hải quân và `submarine_attack`; cắt giảm = rẻ hơn, giao chậm 6 tháng, không có idea. Chỉ dùng modifier có thật; `VIE_kilo_flotilla_idea` giữ làm phần thưởng khi đủ 6 tàu.

## 3.7 Nối với soft-lock `VIE_paracel_ultimatum` (Q1 đã chốt (d) ở lục quân)

`VIE_proc_gate_paracel_capable` và comment ở `VIE_md_triggers_p14.txt:90-115` ghi rõ: **trục Hải quân phải đặt** `VIE_ev_kilo_submarines` và `VIE_ev_bastion_p_coastal_defence`. Báo cáo hải quân không biết hai cờ này.
Đề xuất: đặt `VIE_ev_kilo_submarines` khi tàu Kilo đầu tiên giao; đặt `VIE_ev_bastion_p_coastal_defence` khi hệ thống Bastion đầu tiên giao. Focus mở khi có tàu thật, không phải khi ký. Đây là lý do tên hai cờ phải giữ nguyên; tránh đổi tên theo quy ước `VIE_<mã>_*` của báo cáo.

## 3.8 Phần thưởng Focus của Trục 1 (giảm giá, rút ngắn giao, quy mô lớn hơn)

`VIE_navy_modernization` và `VIE_russian_arms_deals` không còn. Gom điều kiện thưởng vào hai scripted trigger trong file gate mới, mặc định `always = no`:

```pdx
VIE_naval_bonus_modernization = { always = no }   # TODO(Truc2/3): thay bằng focus thật khi có
VIE_naval_bonus_russian_deals = { always = no }
```

Các lựa chọn "quy mô lớn hơn" (Kilo 8, Gepard 4, Sigma 6…) tạm thời **ẩn** cho tới khi trigger có chủ. Đổi một dòng là xong, theo đúng mẫu `VIE_proc_gate_army_program`.

## 3.9 Chi phí: báo cáo chưa có con số tỷ USD nào

Toàn bộ chi phí ghi "cao/rẻ". Trục 1 lục quân dùng USD thật cho `modify_treasury_effect` (T-90 1,85 tỷ trừ treasury + 1,25 tỷ nợ qua `modify_debt_effect`). Làm tương tự. Nguồn báo cáo chỉ có Kilo 1,8–3,2 tỷ USD (mục 8.3); các chương trình khác **chưa có nguồn giá**. Chốt giá từng chương trình trước bước 2 (xem Q3), đừng bịa trong code.

## 3.10 Retry cần ý nghĩa rõ giữa `_offered`, `_missed`, fallback

Bảng cờ rút gọn cho Trục 1 (theo 16.3, thêm cờ fallback và cờ giao):

| Loại | Cờ |
|---|---|
| Chuyển tiếp mỗi chương trình | `VIE_<p>_offered`, `_contracted`, `_missed`, `_cancelled`; Molniya p1 thêm `_skipped`; Sigma thêm `_suspended` |
| Giao hàng (Class C) | `VIE_<p>_sN` (N = số tàu) |
| Fallback im lặng | `VIE_fb_naval_<p>` (scripted effect) |
| Biến | `VIE_<p>_qty_ordered`, `VIE_<p>_qty_delivered`, `VIE_<p>_config`, `VIE_molniya_path`, `VIE_var_hulls_delivered` |
| Bỏ | `VIE_<p>_complete` (= `qty_delivered = qty_ordered`), `VIE_var_naval_budget_room`, mọi biến `_progress` |

---

# PHẦN 4 — PLAN CODE (7 bước, mỗi bước 1 commit)

Kiến trúc: **scheduler riêng `VIE_event_scheduler_naval`**, gọi từ `on_monthly` chung với `original_tag = VIE` và từ `VIE_catch_up_schedule`; KHÔNG dùng `on_monthly_VIE`, KHÔNG đụng `trigger_year_*`.

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `common/scripted_effects/VIE_md_effects_p12.txt`, `common/on_actions/VIE_md_on_actions.txt` | Gỡ `VIE_event_scheduler_p12` và dòng gọi (giữ `VIE_kilo_flotilla_idea`). Ghi chú trong `VIE_v9_flag_mapping.md` | `python tools/audit/live.py` không báo scheduler thiếu; loc PASS |
| **1** | `common/scripted_triggers/VIE_md_triggers_naval.txt` (mới) | Gom cổng: `VIE_naval_bonus_modernization`, `VIE_naval_bonus_russian_deals` (mặc định `always = no`), `VIE_naval_can_fund` (so `treasury`); comment trạng thái Q-list như file p14 | `live.py` sạch |
| **2** | `common/scripted_effects/VIE_md_effects_naval.txt` (mới) | `VIE_naval_ensure_variants` (có cờ chặn trùng), `VIE_event_scheduler_naval` (mẫu p13: catch-up → chỉ đặt cờ; `popup_cd` trống → fire; hết cửa sổ + cổng đạt → `VIE_fb_naval_*`; cổng hỏng → `_missed`), nối vào `on_monthly` **và** `VIE_catch_up_schedule` | console `effect VIE_event_scheduler_naval = yes` không lỗi; `effect set_variable = { VIE_catch_up = 1 }` rồi chạy: không popup |
| **3** | `events/VIE_naval.txt` (mới, `add_namespace = vie_naval`) | **Lát cắt Molniya trước**: `.1` (offer pha 1), `.3` (offer pha 2), giao hàng Class C trong scheduler (cờ `s1…s4`), biến thể `"Molniya Class"` | chơi tới 2003-06: đúng 1 popup; 2007-02 và 2008-02 có tàu; `error.log` không có "equipment_variant does not exist" |
| **4** | `events/VIE_naval.txt`, `…effects_naval.txt` | Nhân bản sang Gepard I, Gepard II (gate `VIE_gepard1_qty_delivered = VIE_gepard1_qty_ordered`), Kilo (lịch 3.3, `VIE_ev_kilo_submarines`, idea đủ 6 tàu), Bastion-P (hiệu ứng 3.5, `VIE_ev_bastion_p_coastal_defence`) | `VIE_paracel_ultimatum` mở sau khi Kilo đầu tiên giao; cờ chỉ có từ lúc giao |
| **5** | `events/VIE_naval.txt` | Sigma: event offer, review 8/2013 (Historical → `_suspended`), Funding Gate, biến thể `"Sigma Class"`, 3 kết cục xác định | đường Historical: không tàu; chọn mua với `treasury` đủ: có tàu; thiếu: hiển thị tooltip rõ |
| **6** | `common/decisions/VIE_md_naval_decisions.txt` + category (mới, `allowed = { original_tag = VIE }`) | 6 Decision `P_late` (Kilo, Gepard I, Gepard II, Bastion, Molniya định tuyến theo hai pha, Sigma từ `_missed` và `_suspended`); +25% chi phí, giao chậm | chiến tranh với Nga trong cửa sổ Kilo → `_missed` → Decision hiện ra |
| **7** | `localisation/english/VIE_md_events_naval_l_english.yml` + `replace/…`; `tools/TESTING.md`; `VIE_v9_flag_mapping.md` | Loc (BOM), mục Trục 1 Hải quân trong TESTING, bảng cờ | `python tools/verify_all_loc.py` PASS; `python tools/audit/ev.py` không orphan |

Ước lượng: ~14 event Class B/C, 6 Decision, ~700 dòng script, ~120 key loc. Số event thấp hơn "24 event" của mục 9.2 vì giao hàng chuyển thành cờ Class C trong scheduler.

---

# TRẠNG THÁI THI CÔNG (2026-10-02)

Bước 0–7 xong về mặt code, chưa chạy trong game. Checklist chi tiết đã chuyển vào `tools/TESTING.md`
(mục "Naval procurement"), bảng cờ vào `VIE_v9_flag_mapping.md` (mục "Truc 1 hai quan").
Còn mở: `VIE_cap_ba_son_yard` và `VIE_var_ba_son_tier` chưa ai đặt (Trục 2), Q1/Q2/Q4/Q5/Q6 dùng mặc định,
ngày giao Kilo tàu 2–3 và Gepard II nội suy, module variant Sigma chưa đối chiếu cấu hình thật.

# PHẦN 5 — CHECKLIST THỬ TRONG GAME

- [ ] `error.log`: grep `vie_naval`, `VIE_naval`, `equipment_variant`, `create_ship`, `module`, `slot`, `frigate_hull_3`, `attack_submarine_hull_2`, `corvette_hull_2`.
- [ ] **Rủi ro cao nhất:** `create_ship` với `creator = SOV` khi VIE chưa nghiên cứu hull đó (VIE chỉ có `corvette_hull_1`): tàu có đến không? (p12 cũ chưa từng chạy trong game.)
- [ ] Biến thể VIE tự tạo (`"Molniya Class"`, `"Sigma Class"`): module có bị bỏ im lặng vì thiếu tech không? Kiểm trong màn hình thiết kế.
- [ ] Obsolete variant của SOV (`"Molniya Class"`, `"Gepard 3.9 Class"`) có dùng được cho `create_ship` không.
- [ ] Đặt `VIE_popup_cd` thủ công rồi chờ: chương trình dời sang tháng sau và, nếu hết cửa sổ, chạy fallback im lặng chứ không đặt `_missed`.
- [ ] Cho Nga biến mất trước 2009-12 (thôn tính bằng console): Kilo `_missed`, Decision `P_late` hiện; pha 2 Molniya vẫn giao nhờ biến thể VIE.
- [ ] Chiến tranh với SOV giữa cửa sổ rồi hoà: cửa sổ còn thì offer vẫn bắn.
- [ ] Nội chiến: người thắng có cờ lịch sử (`VIE_kilo_contracted` …) nhưng không nhận tàu và không popup.
- [ ] Đếm pop-up mỗi năm 2003–2017 (`tools/audit/ev.py`); mục tiêu ≤ 7, ghi lại năm vượt.
- [ ] `treasury` thực tế của VIE tại 2011-10: Funding Gate Sigma có đạt được không, hay luôn trượt?
- [ ] AI-only đến 2020: AI có Molniya p1, Gepard I, Kilo, Bastion; không có Sigma.
- [ ] Không còn cờ `VIE_gepard_contract` / `VIE_kilo_contract` ở bất kỳ file live nào.

---

# PHẦN 6 — QUYẾT ĐỊNH CẦN BẠN CHỐT (mặc định đề xuất ở đầu mỗi dòng)

| # | Câu hỏi | Mặc định đề xuất |
|---|---|---|
| Q1 | Cờ thưởng Focus của Trục 1 (A1/3.8): để `always = no` cho tới khi Trục 2/3 có focus thật, hay dùng tạm `has_completed_focus = VIE_modernize_vpa` (root quân sự còn sống)? | `always = no`: tạm ẩn tùy chọn "quy mô lớn hơn", không thưởng sai chỗ |
| Q2 | Lát cắt Molniya cần `VIE_cap_ba_son_yard`, mà Focus 1 Trục 2 không mở được (A1). Làm Trục 2 Focus 1–2 + Decision 1 trước, hay làm Molniya pha 1 trước và pha 2 sau? | Pha 1 trước (không phụ thuộc); pha 2 chờ Trục 2 |
| Q3 | Giá từng chương trình (tỷ USD, 3.9) | **ĐÃ CHỐT 2026-10-02**, tra nguồn: Kilo 2,0 cho 6 tàu (+0,2/tàu nếu gói hạ tầng đầy đủ = 3,2; tin cậy cao); Gepard I 0,175/tàu (cao); Gepard II 0,35/tàu (cao); Molniya p1 0,06/tàu (thấp); Molniya p2 0,13/tàu (trung bình); Bastion-P 0,20/hệ thống, không có giá hợp đồng VN (thấp); Sigma 0,33/tàu (trung bình, dùng ở bước 5). Chi tiết và nguồn ở đầu `VIE_md_effects_naval_ships.txt` |
| Q4 | Gepard config 3 (phòng không) | Bỏ ở bản đầu (B3) |
| Q5 | Pop-up: giao hàng im lặng (Class C) như đề xuất, hay giữ 1 popup tóm tắt khi chương trình hoàn tất (Kilo đủ 6 tàu, Molniya đủ 8 tàu)? | Một popup tóm tắt cho Kilo và Molniya, tuân `VIE_popup_cd` |
| Q6 | Chữ hoa từ viết tắt (mục 18.1 #13: `mro`, `asw`, `mio` so với Code Style Guide MD) | Giữ chữ thường như các cờ hiện có trong repo (ví dụ `VIE_dec_z_factories`); chưa đối chiếu Code Style Guide của MD |
