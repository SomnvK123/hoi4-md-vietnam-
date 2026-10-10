# Tài liệu Triển khai 3 Trục Hải quân (Quân chủng Hải quân) — Millennium Dawn

> **Cập nhật 11/10/2026:** nội dung ba trục dưới đây là tài liệu lịch sử.
> Bản live đã thay bằng 40 focus Hải quân V35.1. Xem
> [triển khai V35](VIE_naval_V35_implementation.md) cho file consolidated,
> chi phí, kết quả kiểm tra và giới hạn hiện vật; không tái tạo các fragment cũ.

> **Tài liệu tổng hợp đánh giá, nội dung & kế hoạch code (08/10/2026)**  
> Hợp nhất 4 tài liệu phân mảnh của Quân chủng Hải quân Việt Nam.

## Mục lục
1. [Phần 1: Review Trục 1 Hải quân (Mua sắm) + Plan Code](#phần-1-review-trục-1-hải-quân-mua-sắm--plan-code)
2. [Phần 2: Review Trục 2 Hải quân (CNQP) + Plan Code](#phần-2-review-trục-2-hải-quân-cnqp--plan-code)
3. [Phần 3: Review Trục 3 Hải quân (Xây dựng Lực lượng + Trục 1B) + Plan Code](#phần-3-review-trục-3-hải-quân-xây-dựng-lực-lượng--trục-1b--plan-code)
4. [Phần 4: Scripted Effects Nhánh Hải quân — Nội dung Chi tiết + Plan Code](#phần-4-scripted-effects-nhánh-hải-quân--nội-dung-chi-tiết--plan-code)

---
## Phần 1: Review Trục 1 Hải quân (Mua sắm) + Plan Code

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
| Q3 | Giá từng chương trình (tỷ USD, 3.9) | **ĐÃ CHỐT 2026-10-02**, tra nguồn: Kilo 2,0 cho 6 tàu (+0,2/tàu nếu gói hạ tầng đầy đủ = 3,2; tin cậy cao); Gepard I 0,175/tàu (cao); Gepard II 0,35/tàu (cao); Molniya p1 0,06/tàu (thấp–trung bình); Molniya p2 0,13/tàu (trung bình–cao, cả chương trình 2 + 6 tàu cùng giấy phép khoảng 1 tỷ USD); Bastion-P **0,15**/hệ thống (hợp đồng 2006 một tổ hợp = 150 triệu USD theo nguồn Nga, Syria 2007 hai tổ hợp = 300 triệu; trung bình, đã sửa từ 0,20 ngày 2026-10-03); Sigma 0,33/tàu (trung bình, dùng ở bước 5). Chi tiết và nguồn ở đầu `VIE_md_effects_naval_ships.txt` |
| Q4 | Gepard config 3 (phòng không) | Bỏ ở bản đầu (B3) |
| Q5 | Pop-up: giao hàng im lặng (Class C) như đề xuất, hay giữ 1 popup tóm tắt khi chương trình hoàn tất (Kilo đủ 6 tàu, Molniya đủ 8 tàu)? | Một popup tóm tắt cho Kilo và Molniya, tuân `VIE_popup_cd` |
| Q6 | Chữ hoa từ viết tắt (mục 18.1 #13: `mro`, `asw`, `mio` so với Code Style Guide MD) | Giữ chữ thường như các cờ hiện có trong repo (ví dụ `VIE_dec_z_factories`); chưa đối chiếu Code Style Guide của MD |

---

## Phần 2: Review Trục 2 Hải quân (CNQP) + Plan Code

# REVIEW TRỤC 2 HẢI QUÂN (CNQP) + PLAN CODE

> Đầu vào: `Báo cáo hải quân Việt Nam – 3 trục … (bản 2.4).md`, mục 2, 3.2–3.3, 5, 6, 7, 8.1, 9, 16–18 (phần Trục 2).
> Đối chiếu với repo @ working tree sau bước 0–7 của Trục 1 hải quân (`VIE_naval_truc1_review_and_plan.md`),
> Trục 2 lục quân đã code (`VIE_md_def_industry.txt`, `VIE_truc2_review_and_plan.md`) và dữ liệu MD trong `tools/audit/md_ref/`.
>
> **KẾT LUẬN: thiết kế Trục 2 hải quân (6 Focus + 5 Decision, năng lực → kinh nghiệm → trưởng thành) đúng hướng và nối
> được với Trục 1 đã code. Nhưng chưa code được nguyên bản: 4 lỗi chặn, 6 chỗ lệch so với mod/MD, 6 lỗ hổng logic
> (trong đó A4 làm hỏng lựa chọn 8 và 10 tàu của Trục 1 nếu không sửa). Bản sửa ở Phần 3–5, plan 9 bước ở Phần 6. Chưa có dòng code nào của Trục 2.**

---

# PHẦN 1 — ĐÚNG, GIỮ NGUYÊN

| Điểm | Vì sao đúng |
|---|---|
| Sáu Focus mở năng lực, năm Decision biến thành hiện thực; không Decision/Focus nào cấp tàu | Khớp Quy tắc 1–3 và code Trục 1 (tàu chỉ đến từ `VIE_event_scheduler_naval`) |
| Focus chỉ đọc: Focus tiền đề, ngày, trạng thái thế giới, năng lực nhánh khác | Cùng mẫu Trục 1 lục quân (`VIE_def_industry_law`: ngày + root) |
| Mốc 40% đặt `VIE_cap_ba_son_yard` sớm để không chặn Molniya pha 2 | Đúng nguyên tắc, và Trục 1 đã đọc cờ này ở `VIE_naval_sched_molniya_p2` |
| Không có vòng prerequisite (5 lớp một chiều) | Kiểm lại trên code Trục 1: Trục 1 chỉ đọc lớp 1 (cờ xưởng, tier) và ghi biến cho lớp 2+ |
| Giới hạn 2 chương trình CNQP chạy cùng lúc | Giữ, nhưng đổi cách đếm (xem L4) |
| Ba Son MIO dùng `add_mio_size` | Đúng bài học Trục 2 lục quân (Q8 = a: `add_mio_funds` tự lên size, không dùng cả hai) |
| Giá dockyard dùng effect của MD, MD tự trừ 7,5 tỷ | Đúng bài học A2 của Trục 2 lục quân (không trừ tay hai lần) |

---

# PHẦN 2 — 4 LỖI CHẶN

## A1 · Focus nền không tồn tại; chuỗi Focus không có chỗ treo

Báo cáo: Focus 1 `VIE_naval_defence_law` đòi `VIE_defence_industry_modernization`. Focus này **không có ở bất kỳ file nào** (live, `.bak`, `v11_removed_*`).
Cây focus live (290 focus, root quân sự duy nhất `VIE_modernize_vpa` ở toạ độ tuyệt đối (266, 1)) **không có focus hải quân nào**; `VIE_navy_modernization`, `VIE_domestic_corvettes`... đều trong `v11_removed_*.txt`.
Cũng **không** nên dùng `VIE_def_industry_law` (cổng Trục 2 lục quân) làm tiền đề: nó mở từ `date > 2008.6.30`, nên Focus 1 + 2 + milestone 146 ngày của Decision 1 sẽ đến sớm nhất đầu 2009, sát cửa sổ Molniya pha 2 (mở 2009-06) và không còn biên an toàn.
**Fix:** Focus 1 treo trực tiếp dưới `VIE_modernize_vpa` (root quân sự còn sống, cùng cổng mà Trục 1 lục quân dùng), ngày `> 2004.12.31`. Vị trí lưới xem 5.1.

## A2 · Ba cờ `VIE_ext_*` không có chủ, nên Focus 5 và Decision 4 không bao giờ mở

`VIE_ext_viettel_mil_tech`, `VIE_ext_c4isr` không được đặt ở đâu trong repo (grep: 0 kết quả live). Nhánh "Viettel / C4ISR" của v7 đã bị xoá. Chỉ `VIE_ext_naval_missile` có người đặt (Trục 1: `VIE_naval_deliver_bastion` đặt khi giao đủ Bastion).
**Fix:** không chờ nhánh khác. Định nghĩa ba **scripted trigger** trong `VIE_md_triggers_naval.txt` (một chỗ để đổi, đúng mẫu `VIE_proc_gate_*`), mặc định ánh xạ sang focus còn sống (Phần 7). Bỏ biến `VIE_var_ext_support` (xem B4).

## A3 · Ngưỡng kinh nghiệm của Decision 5 không đạt được trên đường lịch sử

Liệt kê toàn bộ 972 tổ hợp lựa chọn mang exp (script `python tools/audit/naval_balance.py`, mục 1) theo bảng 7.3 của báo cáo:

| Đường (tất cả Basic, Nga hỗ trợ, Molniya pha 2 = 6 tàu) | `shipbuilding_exp` | `mro_exp` |
|---|---:|---:|
| Định hướng Shipbuilding trước | 46 | 10 |
| Định hướng MRO trước | 34 | 22 |
| Định hướng Cân bằng | 40 | 16 |

Ngưỡng của báo cáo là `shipbuilding_exp ≥ 50` và `mro_exp ≥ 30`: **không đường Basic nào đạt** (chỉ 233/972 tổ hợp đạt, tất cả đều là đầu tư nặng). Đây là lỗi thiết kế vì đường lịch sử không có đích (Quy tắc 5).
(Bản nháp đầu của tài liệu này đề xuất 40/20 trên một phép tính trộn hai định hướng khác nhau; phép tính đúng ở bảng trên cho thấy 40/20 cũng không đạt trên đường Basic nào, nên đã bỏ.)
**Fix:** hạ còn **`shipbuilding_exp ≥ 30` và `mro_exp ≥ 15`**. Kết quả: 779/972 tổ hợp đạt (80%). Cân bằng + Basic + Molniya pha 2 đạt (40/16); MRO trước đạt; Shipbuilding trước cần nâng D2 lên Chuyên sâu (mro_exp 20). Bỏ Molniya pha 2 mà chỉ đầu tư Basic thì không đạt (22 < 30), nên nội địa hoá vẫn được thưởng. Số này là giá trị khởi điểm, cần playtest.

## A4 · Tier Ba Son đặt khi *kết thúc* Decision làm hỏng lựa chọn 8 và 10 tàu của Trục 1

Báo cáo 5.2: `VIE_var_ba_son_tier` đặt ở Event 3 (kết thúc, 12–24 tháng). Trục 1 đã code: `vie_naval.3` option B (8 tàu) và C (10 tàu) có `trigger = { check_variable = { VIE_var_ba_son_tier > 1 } }`, và event bắn ngay khi `VIE_cap_ba_son_yard` xuất hiện (mốc 40%, tức khi tier **vẫn bằng 0**). Hậu quả: hai lựa chọn không bao giờ hiện, dù người chơi đầu tư Trọng điểm.
**Fix (đề xuất):** đặt `VIE_var_ba_son_tier` **ở mốc 40%** cùng lúc với `VIE_cap_ba_son_yard`, bằng đúng mức đã chọn (1/2/3), vì báo cáo 3.3 đã nêu nguyên tắc "đầu tư Trọng điểm không làm trễ chương trình đang chờ". Phần thưởng thật (dockyard, MIO, exp mức đầu tư) vẫn trao khi kết thúc. Đổi cách khác: bắn `vie_naval.3` chậm lại sau mốc, nhưng sẽ chạm lên hạn cửa sổ 2012-12 và làm sai lịch sử.

---

# PHẦN 3 — LỆCH SO VỚI MOD VÀ MD

## B1 · Decision không có "trạng thái chờ giữa chừng"

Báo cáo 3.2 và 7.5: Decision bắt đầu rồi chuyển sang `_waiting` khi Event kế thiếu năng lực, tự tiếp tục khi đủ. HOI4 không có trạng thái này; muốn giả lập phải có cờ + polling hàng tháng, tức đúng loại biến phản chiếu mà mục 16.3 cấm.
**Fix:** cổng ở **lúc bấm**. `available` của mỗi Decision kèm `custom_trigger_tooltip` nêu đúng điều kiện còn thiếu (mẫu `VIE_dec_z_factories`). Decision đã bắt đầu thì chạy hết, không chờ. Bỏ toàn bộ cờ `_active`, `_done`, `_waiting` và biến `_progress`.

## B2 · Cách hiển thị "đang chạy"

Decision của MD/mod chỉ có hai kiểu thời gian: `days_remove` cố định hoặc mission cố định. Báo cáo cần thời lượng động (12/18/24 tháng × hệ số nguồn hỗ trợ × hướng). Trục 2 lục quân giải bằng hai Decision riêng cho hai thời lượng (`dec_stv`, `dec_stv_fast`).
**Fix cho hải quân:** Decision chỉ là **nút khởi động** (`fire_only_once`, tốn 50 PP như lục quân). Bấm xong bắn chuỗi event chọn; lựa chọn cuối trao một **timed idea** hiển thị đang chạy (`add_timed_idea`) và hẹn event ẩn hoàn tất. Hiệu ứng thật (exp, tier, MIO, dockyard) nằm ở event ẩn hoàn tất. `days = <biến>` đã được xác minh trong mã MD cho cả `country_event` lẫn `add_timed_idea` (Phần 10), nên thời lượng động dùng `set_temp_variable` rồi truyền thẳng, không cần sinh nhánh literal.

## B3 · MIO Ba Son hiện có dùng category sai (nợ cũ, ảnh hưởng thẳng Trục 2)

`VIE_md_organizations.txt:316`: `research_categories = { CAT_patrolboat CAT_corvette CAT_frigate CAT_green_water_navy CAT_naval_sonar }`.
Đối chiếu `md_ref/MD_all_CATS.json` (194 category của MD): **chỉ `CAT_naval_sonar` tồn tại**. Tên đúng: `CAT_patrol_boats`, `CAT_corvettes`, `CAT_frigates`; `CAT_green_water_navy` không có (gần nhất `CAT_surface_ships`). Đây cùng loại nợ mà `VIE_repo_health_report.md` đã ghi cho lục quân.
Tác động: `add_tech_bonus` và thưởng nghiên cứu của MIO Ba Son sẽ im lặng hỏng; mọi `add_tech_bonus` mới của Trục 2 phải dùng token đã xác minh (danh sách ở 5.4).
**Fix:** bước 0 sửa dòng 316 (và kiểm `equipment_type = { mio_cat_only_small_ships … submarine }` với MIO reference của MD, chưa kiểm được ở đây). Chưa rõ trait khởi đầu dùng `production_efficiency_gain_factor` có nằm trong bốn khoá `production_bonus` hợp lệ của MIO hải quân (báo cáo 16.1) không: cần kiểm.

## B4 · Biến `VIE_var_ext_support` là biến phản chiếu

"Số flag `VIE_ext_*` đang được đặt, tính lại mỗi tháng" là đúng cái 16.3 cấm. Focus 5 cần "ít nhất một nguồn": dùng `OR = { … }` trực tiếp. Bỏ biến và việc tính lại hàng tháng.

## B5 · Flag năng lực dư

`VIE_cap_naval_institution`, `VIE_cap_ba_son_complete`, `VIE_cap_naval_mro`, `VIE_cap_small_combatant`, `VIE_cap_integration` đều phản chiếu trạng thái đã có (`has_completed_focus`, biến tier > 0, cờ Decision hoàn tất). Theo 16.3 chỉ giữ cờ cho **chuyển tiếp** hoặc cờ **đã có người đọc**:

| Giữ | Lý do |
|---|---|
| `VIE_cap_ba_son_yard` | Trục 1 đọc (cổng Molniya pha 2, đã code) |
| `VIE_cap_mature_naval_industry` | Trục 1B đọc (P10, P11) |
| `VIE_mro_russia_dependent` | lựa chọn không thể suy ra từ biến khác |
| `VIE_nav_d1_done`, `…_d2_done`, `…_d3_done`, `…_d4_done` | HOI4 không hỏi được "Decision đã hoàn tất", mà D4 và D5 cần biết |

Mọi thứ còn lại dùng biến tier (>0 là "có năng lực") và scripted trigger.

## B6 · Quy ước mod cho file, event, decision

- Namespace riêng, chữ thường: **`vie_nav_ind`** (`events/VIE_nav_ind.txt`), không dùng chung `vie_naval` của Trục 1 (Trục 2 lục quân cũng tách `vie_def_ind`).
- Log câu đầu tiên của mỗi option/effect; option chỉ đóng cửa sổ không log (quy tắc MD). Mọi `ai_chance` của option có tốn tiền có guard `bankruptcy_incoming_collapse` (và `ai_has_high_deficit` cho option không-lịch-sử), mẫu đã áp ở Trục 1 hải quân.
- Loc: `localisation/english/VIE_md_events_nav_ind_l_english.yml` (BOM, tiếng Việt, `:0` như toàn repo).
- Ảnh event: tạo bằng `tools/build_vie_event_pictures.py`; hoặc `GFX_report_event_generic_read_write` tạm.
- Icon focus: thêm 6 mục vào `FOCI` của `tools/build_vie_focus_icons.py` (sprite `GFX_focus_VIE_<stem>`); tạm dùng icon generic của MD cho tới khi có ảnh.

---

# PHẦN 4 — LỖ HỔNG LOGIC VÀ THIẾT KẾ ĐÃ SỬA

## L1 · Orientation của Decision 1 nên chọn ở Focus 2, không ở Decision

Event 1 "chọn định hướng" của báo cáo là lựa chọn một lần, không phụ thuộc Decision. Đặt nó ở **hoàn thành Focus 2** (focus bắn event, đúng Quy tắc 6: Focus không đọc kết quả Decision, nhưng được phép *bắn* event). Hệ quả: Decision 1 chỉ còn một event chọn mức đầu tư, và định hướng đã sẵn khi bấm. Không phá Quy tắc 6 vì Focus 3 và 4 không đọc `VIE_ba_son_orientation`.

## L2 · Công thức thời lượng và chi phí cần số thật

Báo cáo chỉ có hệ số. Đề xuất thang tuyệt đối (tỷ USD; ngày). Chi phí dùng effect có sẵn của MD khi có thể, phần còn lại `modify_treasury_effect`:

| Decision | Cơ bản | Mở rộng | Trọng điểm | Cách trả |
|---|---|---|---|---|
| D1 Ba Son (365 / 548 / 730 ngày) | 7,5 | 12,0 | 18,0 | `one_state_dockyard` ×1 / ×1 + 4,5 tay / `two_state_dockyards` hoặc ×2 + 3,0 tay (MD tự trừ 7,5 mỗi cái, **không** trừ tay phần đó nữa) |
| D2 MRO (cơ sở 4,0) | ×0,8 Nga / ×1,4 tự chủ; ×1,3 toàn hạm đội | | | `modify_treasury_effect` |
| D3 Small Combatant (cơ sở 6,0) | ×1,0 | ×1,6 | ×2,4 | `modify_treasury_effect` |
| D4 Integration (cơ sở **7,0**) | bậc ×1,0 / 1,6 / 2,4; lĩnh vực Full ×1,5 | | | `modify_treasury_effect` |
| D5 Naval 2030 (cơ sở 10,0) | Limited ×1,0 | Integrated ×1,5 | High ×2,2 | `modify_treasury_effect` |

Tổng đường lịch sử Trục 2 (tất cả Basic, Nga hỗ trợ, Limited) = **33,7 tỷ**, tối đa 97,1 (mọi bậc cao nhất, hiếm gặp); cộng Trục 1 (5,45 tỷ sau khi sửa giá Bastion-P) = 39,15 tỷ (Trục 2 lục quân: 30,25). Mọi mục đều dưới p90 của chi phí event MD (26,45 tỷ; trung vị 4,0). Đây là **giá trị khởi điểm cần cân bằng**, không có nguồn lịch sử. Đo bằng `python tools/audit/naval_balance.py`.
Thời lượng D2 = mức (365/548/730) × 0,75 nếu Nga hỗ trợ, × 1,25 nếu tự chủ, × 0,85 nếu Trục 1 đã đặt `VIE_opp_sub_mro` (đủ Kilo giao). D1 và D3 chịu hệ số ±25% theo định hướng như báo cáo 5.2.

## L3 · Điều kiện nguồn tàu của Decision 2 phải đọc đúng biến của Trục 1

Báo cáo 5.3 ghi "đã giao ít nhất 1 Gepard hoặc Molniya". Trục 1 đã code:

| Cần | Biến / cờ thật trong code Trục 1 |
|---|---|
| Có tàu ngầm Kilo | `VIE_kilo_qty_delivered > 0` |
| Có tàu mặt nước | `VIE_gepard1_qty_delivered > 0` hoặc `VIE_gepard2_qty_delivered > 0` hoặc `VIE_molniya_ru_delivered > 0` hoặc `VIE_molniya_vn_qty_delivered > 0` |
| Cơ hội MRO tàu ngầm đủ bộ | `VIE_opp_sub_mro` (giảm thời lượng 15%, không phải cổng) |
| Số thân tàu cho Focus 3 | `VIE_var_hulls_delivered ≥ 4` (báo cáo ghi `hulls_operational`; Trục 1 đã đổi tên) |

Gom thành scripted trigger `VIE_naval_has_sub`, `VIE_naval_has_surface` trong file trigger để Focus/Decision/test cùng dùng.

## L4 · Bộ đếm slot `VIE_var_naval_program_active` cần chốt biên

+1 khi Decision bắt đầu, −1 khi event ẩn hoàn tất. Nếu người chơi lưu/tải giữa chừng biến vẫn đúng (biến lưu theo save). Nếu event hoàn tất bị mất (đổi tag sau nội chiến) bộ đếm kẹt ở 2 và chặn cả nhánh. **Fix:** `available` của Decision gắn thêm `OR = { check_variable = { VIE_var_naval_program_active < 2 } has_country_flag = VIE_civil_war_reset }`, và `VIE_collapse_aftermath` (đã tồn tại) reset biến về 0 khi nội chiến xong. Ghi vào checklist.

## L5 · Trục 2 phải cung cấp ngược cho Trục 1: giá Molniya pha 2 theo hệ số Decision 3

Báo cáo 5.4: Decision 3 cấp "hệ số giảm chi phí cho chương trình đóng tàu nhỏ". Trục 1 chưa đọc hệ số này. **Fix (sửa nhỏ Trục 1):** `VIE_naval_pay_molniya_p2` nhân thêm `VIE_small_combatant_cost_mult` nếu biến có giá trị > 0 (0,8–1,0), xem bước 7.

## L6 · Cổng thưởng của Trục 1 có nguồn thật từ Trục 2

Hai trigger `VIE_naval_bonus_modernization` và `VIE_naval_bonus_russian_deals` hiện mặc định `always = no`. Gợi ý: `bonus_modernization = has_completed_focus = VIE_naval_defence_law` (Focus 1 xong thì mở các lựa chọn quy mô lớn hơn của Gepard/Bastion/Sigma). `bonus_russian_deals` giữ tắt cho tới khi có focus ngoại giao Nga (không thuộc Trục 2).

---

# PHẦN 5 — THIẾT KẾ CHỐT CHO CODE

## 5.1 Sáu Focus (tọa độ tuyệt đối, tương đối từ `VIE_modernize_vpa` = (266, 1))

Vùng x 216–262 trống ở mọi hàng (kiểm bằng script layout 2026-10-02); cột quân sự hiện nằm x 264–284.

| # | Focus | Treo từ | `relative_position_id` | (x, y) tương đối → tuyệt đối | Điều kiện mở | Khi hoàn thành |
|---|---|---|---|---|---|---|
| 1 | `VIE_naval_defence_law` | root | `VIE_modernize_vpa` | (−8, 1) → (258, 2) | prerequisite `VIE_modernize_vpa`; `date > 2004.12.31`; `NOT has_active_mission = bankruptcy_incoming_collapse` | XP hải quân (hoặc mastery nếu `has_selected_naval_grand_doctrine`), `unlock_decision_category_tooltip = VIE_naval_industry_category`; đồng thời `VIE_naval_bonus_modernization` thành đúng (L6) |
| 2 | `VIE_ba_son_shipyards` | F1 | F1 | (0, 1) → (258, 3) | F1; `date > 2004.12.31` | bắn event chọn định hướng (L1), `unlock_decision_tooltip = VIE_nav_d1_ba_son` |
| 3 | `VIE_naval_mro` | F2 | F2 | (−2, 1) → (256, 4) | F2; `date > 2011.12.31`; `VIE_var_hulls_delivered ≥ 4` | `unlock_decision_tooltip = VIE_nav_d2_mro` |
| 4 | `VIE_small_combatant_construction` | F2 | F2 | (+2, 1) → (260, 4) | F2; `date > 2009.12.31` | `unlock_decision_tooltip = VIE_nav_d3_small` |
| 5 | `VIE_naval_systems_integration` | F3 **và** F4 | F3 | (+2, 1) → (258, 5) | `prerequisite` F3 và F4 (hai khối riêng = AND); `date > 2017.12.31`; ít nhất một trong `VIE_naval_has_electronics`, `VIE_naval_has_c4isr`, `VIE_naval_has_missile` | `unlock_decision_tooltip = VIE_nav_d4_integration` |
| 6 | `VIE_naval_defence_2030` | F3, F4, F5 | F5 | (0, 1) → (258, 6) | F3, F4, F5; `date > 2027.12.31` | `unlock_decision_tooltip = VIE_nav_d5_2030` |

Mọi Focus: `search_filters = { FOCUS_FILTER_NAVY FOCUS_FILTER_INDUSTRY }`, `cost = 7` (F1 và F2 `cost = 5`), `log` đầu `completion_reward`, `ai_will_do` base 90 với `date > 2004.12.31` cho F1 và F2 (AI cần Ba Son trước 2009), 60–70 cho F3–F6; mọi cái `factor = 0` khi `bankruptcy_incoming_collapse`. Chạy `python tools/audit/audit.py` kiểm lưới, không prerequisite quá dài.
Không có `FOCUS_FILTER_NAVY` thừa: filter này đã có 11 chỗ dùng trong file focus.

## 5.2 Năm Decision (category `VIE_naval_industry_category`)

Category: `allowed = { original_tag = VIE }`, `priority = 90`, `visible = { has_completed_focus = VIE_naval_defence_law }`. Mỗi Decision: `fire_only_once = yes`, `cost = 50`, `visible` theo Focus của nó, `available` có `custom_trigger_tooltip` cho từng điều kiện, `complete_effect` log đầu + tăng `VIE_var_naval_program_active` + bắn event chọn. `ai_will_do` base 100, `factor = 0` khi `bankruptcy_incoming_collapse`.

| Decision | Focus mở | `available` (cổng lúc bấm) | Chuỗi event chọn | Hoàn tất |
|---|---|---|---|---|
| D1 `VIE_nav_d1_ba_son` | F2 | `VIE_var_naval_program_active < 2` | `.2` mức đầu tư (3 lựa chọn, L2) | mốc 40% (146 / 219 / 292 ngày): đặt `VIE_cap_ba_son_yard`, `VIE_var_ba_son_tier` = mức (A4). Kết thúc: dockyard, MIO `+1/+2/+3`, exp `+5/+10/+15`, `VIE_nav_d1_done`, −1 slot |
| D2 `VIE_nav_d2_mro` | F3 | slot; `VIE_naval_has_sub` hoặc `VIE_naval_has_surface` | `.10` trọng tâm, `.11` nguồn hỗ trợ (Nga = lịch sử), `.12` mức nội địa hóa (mức sau cần `mro_exp` đủ ngưỡng) | exp `+10/+20/+30`; `VIE_var_mro_tier`; cờ `VIE_mro_russia_dependent` nếu chọn Nga (trần `mro_exp` 50); địa điểm MRO tàu ngầm ghi **Cam Ranh** trong loc |
| D3 `VIE_nav_d3_small` | F4 | slot | `.20` chuyên hoá (Tuần tra / Tốc độ cao / Đa dụng), `.21` mức sản xuất (tier 3 cần `VIE_molniya_domestic_started`, cờ Trục 1) | exp `+5…+8` rồi `+5/+10/+15`; `VIE_small_combatant_cost_mult` = 0,80 / 0,85 / 0,90 (L5); `VIE_var_small_combatant_tier`; MIO `+1` |
| D4 `VIE_nav_d4_integration` | F5 | slot; lĩnh vực cần nguồn đúng (Electronics: `VIE_naval_has_electronics` hoặc `…_c4isr`; Weapons: `VIE_naval_has_missile`; Full: một nguồn điện tử và missile, ×1,5) | `.30` lĩnh vực, `.31` mức nội địa hoá | exp `+10/+20/+30`; `VIE_var_integration_tier`; nếu đã giao Sigma thì Cân bằng cho thêm exp |
| D5 `VIE_nav_d5_2030` | F6 | slot; `shipbuilding_exp ≥ 30`, `mro_exp ≥ 15` (A3) | `.40` ưu tiên (4 lựa chọn), `.41` mức tự chủ (Limited: không thêm; Integrated: `ba_son_tier ≥ 2`; High: `ba_son_tier = 3` và `integration_tier ≥ 2`) | đặt `VIE_cap_mature_naval_industry`; không cấp tàu |

Event ẩn hoàn tất: `.61` D1 kết thúc, `.62` D2, `.63` D3, `.64` D4, `.65` D5; `.60` mốc 40% của D1. Chuỗi event chọn là event nối tiếp nên miễn `VIE_popup_cd` (do người chơi chủ động bấm Decision).
Bấm xong, `add_timed_idea` hiển thị đang chạy; hẹn event ẩn bằng `days`.

## 5.3 Quy tắc dòng chảy giữa Trục 1 và Trục 2 (hợp đồng cờ/biến, sau sửa)

| Cạnh | Hướng | Qua | Trạng thái |
|---|---|---|---|
| Ba Son → Molniya pha 2 | T2 → T1 | `VIE_cap_ba_son_yard` (mốc 40%), `VIE_var_ba_son_tier` (cũng ở mốc 40%, A4) | Trục 1 đọc rồi; Trục 2 chưa ghi |
| Molniya pha 2 → Small Combatant | T1 → T2 | `VIE_molniya_domestic_started`, `VIE_var_shipbuilding_exp` | Trục 1 ghi rồi; Trục 2 chưa đọc |
| Kilo → MRO tàu ngầm | T1 → T2 | `VIE_kilo_qty_delivered`, `VIE_opp_sub_mro` | Trục 1 ghi rồi |
| Gepard / Molniya → MRO mặt nước, Focus 3 | T1 → T2 | `…_delivered`, `VIE_var_hulls_delivered` | Trục 1 ghi rồi |
| Bastion → Weapons | T1 → T2 | `VIE_ext_naval_missile` | Trục 1 ghi rồi |
| Sigma → Integration (tuỳ chọn) | T1 → T2 | `VIE_sigma_qty_delivered`, `VIE_var_integration_exp` | Trục 1 ghi rồi; Sigma Domestic/Hybrid đã cộng `integration_exp` |
| Decision 3 → giá Molniya pha 2 | T2 → T1 | `VIE_small_combatant_cost_mult` | **Cần sửa Trục 1** (L5) |
| Focus 1 → quy mô lớn của Trục 1 | T2 → T1 | `VIE_naval_bonus_modernization` | **Cần sửa trigger** (L6) |

## 5.4 Phần thưởng và token đã kiểm chứng

Chỉ dùng token đã xác minh trong repo hoặc `md_ref`:
- **Tech bonus (`add_tech_bonus`):** `CAT_patrol_boats`, `CAT_corvettes`, `CAT_frigates`, `CAT_attack_submarines`, `CAT_naval_sonar`, `CAT_naval_electronics`, `CAT_naval_fire_control`, `CAT_naval_missiles`, `CAT_naval_radar` (đều có trong `MD_all_CATS.json`). **Không** dùng `CAT_patrolboat`, `CAT_corvette`, `CAT_frigate`, `CAT_green_water_navy`.
- **MIO:** chỉ `mio:VIE_ba_son_manufacturer = { add_mio_size = N }` qua helper `VIE_ba_son_mio_size_N` (mẫu `VIE_gdt_mio_size_N`). Không mở trait bằng script (bài học B3 của Trục 2 lục quân). Không dùng `add_mio_funds` cùng `add_mio_size`.
- **Modifier trong idea hiển thị/thưởng:** chỉ token đã xuất hiện trong repo: `experience_gain_navy_factor`, `navy_submarine_attack_factor`, `naval_speed_factor`, `naval_hit_chance`, `naval_detection`, `naval_coordination`. "Giảm chi phí duy trì hạm đội" của báo cáo **chưa có token đã kiểm**: bỏ cho tới khi xác minh token (bước 3 của plan).
- **Building:** `one_state_dockyard` và `two_state_dockyards` của MD (tự trừ tiền, `CONTROLLER`); không dùng `add_building_construction` trần cho dockyard.

---

# PHẦN 6 — PLAN CODE (9 bước, mỗi bước 1 commit)

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `VIE_md_organizations.txt` | Sửa `research_categories` của Ba Son (B3); kiểm `equipment_type`; ghi nợ nếu còn token sai | `python tools/audit/live.py` và thử MIO mở trong game, `error.log` |
| **1** | `common/scripted_triggers/VIE_md_triggers_naval.txt` | Thêm `VIE_naval_has_sub`, `VIE_naval_has_surface`, `VIE_naval_has_electronics`, `VIE_naval_has_c4isr`, `VIE_naval_has_missile` (ánh xạ Phần 7); đổi `VIE_naval_bonus_modernization` (L6) | brace; `check6.py`-kiểu quét trigger đã định nghĩa |
| **2** | `common/national_focus/VIE_md_focus.txt` + loc | Sáu Focus (5.1), reward chỉ XP + tooltip, **chưa** có event; ảnh/icon tạm | `python tools/audit/audit.py` (lưới, prerequisite); `verify_all_loc.py`; mở cây focus, thấy cột hải quân dưới root |
| **3** | `common/scripted_effects/VIE_md_effects_nav_ind.txt` | Helper: `VIE_ba_son_mio_size_1/2/3`, `VIE_nav_add_shipbuilding_exp` (kẹp 0–100), `…_mro_exp` (trần 50 nếu `VIE_mro_russia_dependent`), `…_integration_exp`, `VIE_nav_program_start/end` (slot), hàm quy đổi mức → ngày/chi phí (L2) | brace; undefined-call scan |
| **4** | `events/VIE_nav_ind.txt` (`add_namespace = vie_nav_ind`) + `common/decisions/VIE_md_nav_ind_decisions.txt` + category | **Decision 1** trọn vẹn: event định hướng (bắn từ F2), `.2` mức đầu tư, `.60` mốc 40%, `.61` kết thúc; timed idea với `days = <biến tạm>` (Phần 10) | chơi: F1 → F2 → định hướng → D1 → 146–292 ngày sau `VIE_cap_ba_son_yard` và `VIE_var_ba_son_tier` > 0; `vie_naval.3` B/C hiện khi tier ≥ 2 |
| **5** | cùng file | **Decision 3, 2** (cần dữ liệu Trục 1: `VIE_molniya_domestic_started`, các `_delivered`), exp, `VIE_small_combatant_cost_mult` | thử với console đặt biến Trục 1 |
| **6** | cùng file | **Decision 4, 5** + Sigma bonus + `VIE_cap_mature_naval_industry` | thử Focus 5–6 bằng console ngày; ngưỡng exp (A3) |
| **7** | `VIE_md_effects_naval_ships.txt` | Sửa nhỏ Trục 1: `VIE_naval_pay_molniya_p2` nhân `VIE_small_combatant_cost_mult` (L5) | ghi chú trong TESTING; thử giá |
| **8** | `common/scripted_effects/VIE_md_effects_p3.txt` (`VIE_collapse_aftermath`) | Reset `VIE_var_naval_program_active` sau nội chiến (L4); catch-up Trục 2 | checklist nội chiến |
| **9** | `localisation/english/VIE_md_events_nav_ind_l_english.yml`; `tools/TESTING.md`; `VIE_v9_flag_mapping.md`; `tools/build_vie_focus_icons.py` (6 mục `FOCI`) | Loc (BOM), mục "Naval industry" trong TESTING, bảng cờ Trục 2, ảnh/icon | `python tools/verify_all_loc.py`; `python tools/audit/ev.py` không orphan |

Ước lượng: 6 Focus, 5 Decision, khoảng 16 event (5 chuỗi chọn + 6 ẩn), ~800 dòng script, ~120 khóa loc. Nhỏ hơn báo cáo vì `_waiting`/`_active`/`_progress` bị bỏ.

---

# PHẦN 7 — ÁNH XẠ NGUỒN `VIE_ext_*` (đề xuất, A2)

Focus live, không phụ thuộc nhánh chưa xây:

| Trigger | Định nghĩa đề xuất | Ghi chú |
|---|---|---|
| `VIE_naval_has_electronics` | `OR = { has_completed_focus = VIE_semiconductor_fab has_completed_focus = VIE_chip_design }` | Điện tử bán dẫn dân sự ứng dụng quân sự (dual-use). Cần kiểm tên focus còn sống và `date` hợp lý (fab xuất hiện muộn) |
| `VIE_naval_has_c4isr` | `OR = { has_completed_focus = VIE_earth_observation has_completed_focus = VIE_vinasat }` | Vệ tinh quan sát/viễn thông. Ứng viên thay thế: `VIE_lf_cap_cyber_ew` hoặc `VIE_lf_cap_info_ops` của Trục 3 lục quân (nối chéo quân chủng, không khuyến nghị) |
| `VIE_naval_has_missile` | `has_country_flag = VIE_ext_naval_missile` | Trục 1 đặt khi giao đủ Bastion; có thể thêm nguồn ngành tên lửa sau |

Quy tắc 6(d) gốc nói "năng lực do nhánh khác sở hữu"; ở đây chủ sở hữu là focus còn sống, vẫn đúng tinh thần. Khi nhánh Viettel/C4ISR thật được xây, đổi một dòng.

---

# PHẦN 8 — CÂU HỎI ĐÃ CHỐT (2026-10-03: N1–N6 theo mặc định, N7 = Có)

| # | Câu hỏi | Mặc định |
|---|---|---|
| N1 | Focus 1 treo dưới `VIE_modernize_vpa` (A1) hay dựng một focus cổng hải quân mới (`VIE_navy_modernization` làm lại)? | **ĐÃ CHỐT:** treo thẳng dưới `VIE_modernize_vpa`; Trục 3 sau này tự dựng cổng riêng |
| N2 | Đặt `VIE_var_ba_son_tier` ở mốc 40% (A4) hay chỉ khi kết thúc? | **ĐÃ CHỐT:** mốc 40% |
| N3 | Ngưỡng Decision 5 (A3): 30 và 15 (đã tính lại), hay giữ 50 và 30 và tăng nguồn exp? | **ĐÃ CHỐT:** 30 và 15 |
| N4 | Nguồn `VIE_naval_has_electronics` / `…_c4isr` (Phần 7) | **ĐÃ CHỐT:** như bảng Phần 7 |
| N5 | Thang chi phí (L2) là giá trị tự đặt (tổng đường lịch sử 34,7 tỷ). Chấp nhận để cân bằng sau? | **ĐÃ CHỐT:** có |
| N6 | `bonus_modernization` mở bởi Focus 1 (L6), còn `bonus_russian_deals` giữ tắt? | **ĐÃ CHỐT:** có |
| N7 | Bấm Decision nay là nút khởi động + chuỗi event (B2), không còn Decision hiển thị đang chạy. Chấp nhận timed idea làm chỉ báo? | **ĐÃ CHỐT: Có** (2026-10-02) |

---

# PHẦN 9 — CHECKLIST THỬ TRONG GAME (dự kiến, đưa vào TESTING.md ở bước 9)

- [ ] `error.log`: grep `vie_nav_ind`, `VIE_nav_`, `VIE_naval_has_`, `CAT_`, `add_tech_bonus`, `add_mio_size`, `add_timed_idea`.
- [x] `days = <biến>` đã xác minh bằng mã nguồn MD (Phần 10); không cần nhánh literal. Vẫn thử một lần trong game.
- [ ] Đường lịch sử: F1 → F2 (2005) → định hướng → D1 Cơ bản: `VIE_cap_ba_son_yard` sau 146 ngày; năm 2009-06 `vie_naval.3` xuất hiện; tier = 1 nên chỉ A và E hiện. Với Mở rộng: B và C hiện (A4).
- [ ] D1 trả tiền đúng 1 lần: kiểm `treasury` trước/sau, chỉ trừ 7,5 cho dockyard và phần tay còn lại, không 15 (bài học A2 lục quân).
- [ ] D2: đủ điều kiện sau khi giao tàu đầu của Kilo; "Toàn hạm đội" yêu cầu cả hai; chọn Nga: `VIE_mro_russia_dependent` đặt và `mro_exp` kẹp ở 50.
- [ ] D3: tier 3 chỉ hiện khi `VIE_molniya_domestic_started`; sau D3, `VIE_naval_pay_molniya_p2` rẻ hơn.
- [ ] D4: Weapons cần `VIE_ext_naval_missile` (giao đủ Bastion trong Trục 1); Electronics cần `VIE_naval_has_electronics` hoặc `…_c4isr`.
- [ ] D5: Cân bằng + Basic + Molniya pha 2 mở được (40/16 so với ngưỡng 30/15); Shipbuilding trước cần D2 Chuyên sâu; kiểm ba mức tự chủ và điều kiện tier.
- [ ] Slot: bấm D2 và D3 cùng lúc, D4 phải bị chặn bởi 2/2; hoàn tất một cái thì mở lại.
- [ ] Nội chiến: `VIE_var_naval_program_active` về 0, Decision không kẹt.
- [ ] AI-only đến 2020: AI VIE có `VIE_cap_ba_son_yard` trước 2009-06 (nếu không, Molniya pha 2 mất; xem `ai_will_do` F1, F2, D1).
- [ ] Đếm pop-up: các event chọn là chuỗi do người chơi bấm Decision nên không ảnh hưởng ngân sách pop-up tự động.

---

# PHẦN 10 — KIỂM CHỨNG CHÉO VỚI MD VÀ GAME GỐC (2026-10-02)

## 10.1 `days = <biến>`: **được**, bằng chứng từ mã nguồn MD

Tải mã nguồn MD (`MillenniumDawn/Millennium-Dawn`, nhánh `main`, sparse clone `common/` và `events/`) và quét toàn bộ cú pháp `days = <tên>` (không phải số, không phải `@hằng`):

| Effect | Có biến? | Ví dụ thật trong MD |
|---|---|---|
| `add_timed_idea` | **Có** (10 chỗ) | `HKG_scripted_effects.txt:470`: `set_temp_variable = { idea_len = … }` rồi `add_timed_idea = { idea = HKG_contract_dockyard_revenue days = idea_len }`; `BOS_scripted_effects.txt:421`: `days = BOS_recovery_days` (biến quốc gia); `eu_scripted_effects.txt:1163`: `days = potef_term_temp` |
| `country_event` | **Có** | `events/United States.txt` (usa.202): `set_temp_variable = { USA_f22_next_days = { value = USA_f22_stage_base multiply = 0.6 round = yes } }` rồi `country_event = { id = usa.203 days = USA_f22_next_days }` |
| `set_country_flag` | **Có** | `CZE_scripted_effects.txt:1154`: `flag = … days = CZE_petr_pavel_mission_duration value = 1` |

Ghi chú:
- Dạng tính trước dùng khối `set_temp_variable = { tên = { value = … multiply = … round = yes } }`. Nên có `round = yes` vì số ngày phải nguyên.
- MD cũng dùng `days = @HẰNG` (hằng biên dịch, `@HOL_D66_time_tier_1`) ở nhiều nơi: đó là hằng số, không phải biến thời gian chạy; không dùng để suy ra biến.
- **Không có** ví dụ nào trong MD cho `months = <biến>`, `hours = <biến>` hay `random_days = <biến>`. Trục 2 chỉ dùng `days`, nên không ảnh hưởng.
- Wiki HOI4 (hoi4.paradoxwikis.com, Event modding) chỉ liệt kê ví dụ số, không nói rõ; bằng chứng thực tế là mã MD ở trên. Kiểm lại một lần trong game vẫn nên làm (checklist).

**Áp dụng cho Trục 2 và cả Trục 1 hải quân:** Sigma hiện chia ba nhánh `if` literal (900 / 1080 / 1260 và 1125 / 1350 / 1575 ngày) vì lúc viết chưa chắc; có thể gọn lại bằng `set_temp_variable` rồi `days = <biến>`. Không cần sửa ngay (không lỗi), ghi lại làm việc dọn tuỳ chọn.

## 10.2 Quy ước MD cho phần bấm giờ

- Ví dụ MD đặt biến tạm trong **cùng option/effect** với lệnh dùng nó (`USA_f22_next_days` đặt rồi dùng ngay): làm vậy, không truyền biến tạm qua event khác.
- Thời lượng cần lưu cho event hoàn tất thì đã biết lúc hẹn; event ẩn không cần đọc lại (dữ liệu lựa chọn nằm ở biến quốc gia `VIE_ba_son_invest`, v.v.).
- Hệ số thời lượng: `value = base multiply = 0.75 round = yes` (Nga), `1.25` (tự chủ), `0.85` (`VIE_opp_sub_mro`).

## 10.3 Con số cân bằng: kết quả `tools/audit/naval_balance.py` (PASS)

| Kiểm tra | Kết quả |
|---|---|
| Ngưỡng exp D5 | Báo cáo (50/30) không đạt trên đường Basic nào; ngưỡng mới 30/15 cho 80% tổ hợp đạt; bỏ Molniya pha 2 thì Basic không đủ |
| Chi phí | Trục 1 lịch sử 5,45 tỷ; Trục 2 lịch sử 33,7 tỷ (tối đa 97,1); tổng 39,15 tỷ; mục đơn lớn nhất 25,2 tỷ (D4 Tự chủ cao + toàn hệ thống) < p90 MD (26,45) |
| So với MD | 1807 giá trị `treasury_change = -N` trong event MD: p25 0,3; trung vị 4,0; p75 10,0; p90 26,45. Giá hải quân Trục 1 (0,06–3,2) thuộc nửa thấp, Trục 2 (3,2–22) quanh p50–p90 |
| Ngân khố VIE đầu game | `history/countries/VIE`: `treasury = 5`, `debt = 77,514`. Funding Gate Sigma (≤ 0,86 tỷ cho 2 tàu Domestic) đạt từ đầu game |
| Mốc 40% của D1 | Sớm nhất 2005-08 / 2005-10 / 2005-12 (Cơ bản / Mở rộng / Trọng điểm); Focus 1 chậm nhất 2008-06-04 vẫn kịp tier 3 trước 2009-06 |
| Dockyard | MD `one_state_dockyard` 7,5 tỷ, `two_state_dockyards` 15 tỷ (tự trừ). `gdp_total` của MD cộng GDP từ dockyard (`gdp_from_dockyards`), nên dockyard mới có hoàn vốn qua GDP |

Giới hạn của phép kiểm: MD không công bố thu nhập hàng tháng của VIE trong dữ liệu đã tải, nên chưa mô phỏng được dòng tiền theo năm; chi phí chỉ so với phân bố chi phí event của MD và ngân khố đầu game. Cần observe-run trong game để xem `treasury` thật quanh 2009–2012 (Kilo 3,2 tỷ) và 2012–2020 (D1 7,5–18 tỷ, D3, D4).

---

# TRẠNG THÁI THI CÔNG (2026-10-03)

| Bước | Trạng thái |
|---|---|
| 0 Sửa MIO Ba Son | Xong: `research_categories` đổi thành `CAT_patrol_boats CAT_corvettes CAT_frigates CAT_surface_ships CAT_naval_sonar` (đều có trong MD). Kiểm với mã MD: `equipment_type = { mio_cat_only_small_ships mio_cat_frigates mio_cat_destroyers submarine }` hợp lệ; `production_efficiency_gain_factor` hợp lệ (495 chỗ dùng trong MD), nên mối lo ở B3 về khoá của trait khởi đầu **không còn**. Nợ cũ còn lại (ngoài phạm vi): ba MIO khác của repo (Viettel, GDT, VAECO) vẫn dùng `CAT_cnc`, `CAT_inf_wep`, `CAT_heli`... |
| 1 Trigger | Xong: `VIE_naval_has_sub`, `_has_surface`, `_has_electronics`, `_has_c4isr`, `_has_missile`, `_has_ext_source`; `VIE_naval_bonus_modernization` = Focus 1 xong |
| 2 Sáu Focus | Xong: 6 focus ở (258,2) (258,3) (256,4) (260,4) (258,5) (258,6); reward chỉ XP/mastery; loc trong `VIE_md_events_nav_ind_l_english.yml`. Chưa có event định hướng và `unlock_decision_tooltip` (thuộc bước 4 vì Decision chưa tồn tại) |
| 3 Helper | Xong: `VIE_md_effects_nav_ind.txt` (MIO size 1–3, exp shipbuilding/mro/integration có kẹp, slot start/end, `VIE_nav_d1_start`, `VIE_nav_d1_finish`) |
| 4 Decision 1 | Xong: Focus 2 bắn `vie_nav_ind.1` (định hướng); Decision `VIE_nav_d1_ba_son` (50 PP, cổng slot < 2 và đã chọn định hướng) bắn `.2` (mức đầu tư); `days = <biến tạm>` cho timed idea và hai event hẹn giờ; `.60` mốc 40% đặt `VIE_cap_ba_son_yard` và `VIE_var_ba_son_tier`; `.61` xây dockyard ở state 519 (TP Hồ Chí Minh), MIO +1/+2/+3, exp +5/+10/+15, đặt `VIE_nav_d1_done`, trả slot. Chi phí: dockyard do MD tự trừ, phần còn lại trừ tay tại lúc bắt đầu; định hướng Cân bằng +15% tổng giá. Idea `VIE_nav_prog_ba_son` hiển thị đang chạy |
| 5 Decision 3 và 2 | Xong: `VIE_nav_d3_small` (cổng: Ba Son dùng được) với `.20` chuyên hóa, `.21` mức sản xuất, `.63` kết thúc; `VIE_nav_d2_mro` (cổng: đã có tàu ngầm hoặc tàu mặt nước từ Trục 1) với `.10` trọng tâm, `.11` nguồn hỗ trợ, `.12` mức nội địa hóa, `.62` kết thúc. Thời lượng D2 = gốc × nguồn (Nga 0,75, tự chủ 1,25) × định hướng (MRO trước 0,75, đóng tàu trước 1,25) × 0,85 nếu `VIE_opp_sub_mro`; D3 chịu hệ số định hướng ngược lại. Chi phí D2 = 4,0 × bậc (1/1,6/2,4) × nguồn (0,8/1,4) × 1,3 nếu toàn hạm đội. **Lệch với báo cáo:** điều kiện "mức sau cần `mro_exp` đủ ngưỡng" của D2 đổi thành "cần Ba Son đã hoàn tất" (bậc 2) và "cần thêm đầu tư Mở rộng trở lên hoặc D3 xong" (bậc 3), vì `mro_exp` chưa có nguồn nào trước D2 (định hướng Đóng tàu trước chỉ có 0) nên điều kiện theo `mro_exp` sẽ khóa vĩnh viễn hướng đó khỏi Decision 5 |
| 6 Decision 4 và 5 | Xong: `VIE_nav_d4_integration` (cổng: có một nguồn điện tử, C4ISR hoặc tên lửa) với `.30` lĩnh vực (mỗi lĩnh vực cần đúng nguồn, Full cần cả điện tử/C4ISR và tên lửa, ×1,5), `.31` mức nội địa hóa (giá gốc **7,0** × bậc), `.64` kết thúc (+10/+20/+30 exp tích hợp, +5 nếu Cân bằng và đã giao Sigma, thưởng công nghệ). `VIE_nav_d5_2030` (cổng: `shipbuilding_exp ≥ 30`, `mro_exp ≥ 15`) với `.40` ưu tiên (Đóng tàu cần D1 xong, Bảo dưỡng cần D2 xong, Tích hợp cần D4 xong, Toàn diện cần cả ba), `.41` mức tự chủ (Limited 24 tháng 10 tỷ; Integrated 30 tháng 15 tỷ cần `ba_son_tier ≥ 2`; High 36 tháng 22 tỷ cần `ba_son_tier = 3` và `integration_tier ≥ 2`), `.65` kết thúc: MIO +1/+2/+3, thưởng công nghệ theo ưu tiên, idea `VIE_nav_mature_industry_idea`, đặt `VIE_cap_mature_naval_industry`. Giá D4 đổi từ gốc 8,0 xuống 7,0 để mục đắt nhất (24 × 1,5 ở bậc cao) nằm dưới p90 của MD |
| 7 Trục 1 đọc hệ số Decision 3 | Xong: `VIE_naval_pay_molniya_p2` và phụ phí ký muộn `VIE_naval_late_start_molniya_p2` nhân thêm `VIE_small_combatant_cost_mult` (0,8–0,9) khi biến > 0 |
| 8 Nội chiến | Xong: `VIE_nav_program_recount` đếm lại slot theo các timed idea chương trình đang giữ, gọi trong `VIE_collapse_aftermath`. Tag nổi loạn thắng thì về 0; cùng tag thì giữ số chương trình còn chạy. Giới hạn đã biết: event hoàn tất đã hẹn bị mất khi đổi tag, nên chương trình của tag cũ không tự hoàn tất cho tag mới |
| 9 Tài liệu | Xong: mục "Naval industry" trong `tools/TESTING.md` (checklist ~20 mục, mục đầu tiên là kiểm `days = <biến>` trong game), bảng cờ và biến trong `VIE_v9_flag_mapping.md`, sáu mục `FOCI` trong `tools/build_vie_focus_icons.py`. Icon riêng **chưa tạo** (cần chạy `search` rồi duyệt ảnh); sáu focus giữ icon generic cho tới lúc đó |

Bước 0–9 xong về code và tài liệu; toàn bộ chưa chạy trong game.

---

# SỬA SAU RÀ SOÁT (2026-10-03)

Rà soát cả hai trục (đối chiếu mã MD `main`) tìm ra bốn lỗi, đã sửa:
1. Decision 5 có thể mở khi chưa chương trình nào xong, làm event ưu tiên `.40` không còn lựa chọn và kẹt slot: cổng thêm `VIE_nav_d1_done` (tooltip `VIE_nav_d1_done_tt`).
2. AI có thể không chọn được ở `.10` và `.30` (mọi option khả dụng trọng số 0): A, B của `.10` và B của `.30` nay có trọng số lịch sử và tự tắt khi option khác phù hợp hơn khả dụng.
3. `add_mio_size` thiếu guard `has_dlc = "Arms Against Tyranny"` như mọi chỗ MD gọi: ba helper `VIE_ba_son_mio_size_N` đã bọc. Helper `VIE_gdt_mio_size_*` của Trục 2 lục quân còn thiếu guard (nợ cũ, ngoài phạm vi).
4. Hai đoạn loc (`vie_nav_ind.1.d`, `vie_nav_ind.12.d`) mô tả sai điều kiện/hệ quả: đã sửa.

---

## Phần 3: Review Trục 3 Hải quân (Xây dựng Lực lượng + Trục 1B) + Plan Code

# REVIEW TRỤC 3 HẢI QUÂN (XÂY DỰNG LỰC LƯỢNG + TRỤC 1B) + PLAN CODE

> Đầu vào: `Báo cáo hải quân Việt Nam – 3 trục … (bản 2.4).md`, mục 10–15 (Trục 3, Program Engine 1B, template), cộng mục 2, 16–18 (quy tắc, đối chiếu MD).
> Đối chiếu với repo @ working tree sau Trục 1 và Trục 2 hải quân (`VIE_naval_truc1_review_and_plan.md`, `VIE_naval_truc2_review_and_plan.md`), Trục 3 lục quân đã code (`VIE_truc3_review_and_plan.md`, tiền tố `VIE_lf_`) và dữ liệu MD (`tools/audit/md_ref/`, bản clone MD `main`).
> Ngày: 2026-10-02. **Chưa có dòng code nào của Trục 3.**
>
> **KẾT LUẬN: khung thiết kế (8 focus chung → 3 nhánh, 4 Decision lực lượng, Program Engine cho 1B) đúng hướng và nối được với Trục 1–2 đã code. Nhưng chưa code được nguyên văn: 7 lỗi chặn, 8 chỗ lệch mod/MD, 8 lỗ hổng logic (trong đó 6 là mâu thuẫn nội bộ của báo cáo). Bản sửa ở Phần 2–5, plan 10 bước ở Phần 6, 12 câu hỏi đã gắn mặc định ở Phần 7.**

---

# PHẦN 1 — ĐÚNG, GIỮ NGUYÊN

| Điểm | Vì sao đúng |
|---|---|
| 22 node Focus = 8 chung + 4 (Denial) + 5 (Greenwater) + 5 (Bluewater); mỗi lần chơi đi 12 (Denial) hoặc 13 (Greenwater, Bluewater) | Đếm lại trong bảng 11.1 và 11.5: khớp 10.1, 11, 15.1 và 15.2 |
| Focus chỉ mở Decision và đặt mốc; việc đào tạo là Decision | Cùng mẫu Trục 2 hải quân (`unlock_decision_tooltip`) và Trục 2 lục quân |
| Quy tắc 10: Trục 3 chỉ cấp modifier vận hành, không đụng giá đóng tàu | Khớp thực tế: Trục 2 sở hữu mọi thứ về sản xuất (`VIE_small_combatant_cost_mult`, tier) |
| Quy tắc 11: không ghi `VIE_cap_*` của Trục 2 | Đúng; xem A3 cho phần còn lại của namespace |
| Nhánh Maritime Denial là nhánh lịch sử (có đích cho người chơi đi đúng lịch sử) | Khắc phục lỗi gốc "không có chỗ đi" của bản cũ |
| Hải quân đánh bộ đã gỡ khỏi Trục 3 (sang nhánh Vietnam Special Force) | Kiểm trên repo: không còn tham chiếu live nào tới `VIE_naval_infantry` |
| Chương trình 1B đi qua Decision, không có cửa sổ lịch sử, không event tự kích | Khớp Quy tắc 5; vì vậy 1B **không** tạo pop-up mới ngoài ngân sách `VIE_popup_cd` |
| Trục 3 không ghi gì vào Trục 1 ngoài một thưởng nhỏ cho Kilo (mục 14.5) | Một chiều, không vòng: xem 5.3 |

---

# PHẦN 2 — 7 LỖI CHẶN

## A1 · Focus nền `VIE_navy_modernization` và hai node Doctrine **không còn trong cây live**

Báo cáo: T1 đòi `VIE_navy_modernization`; Quy tắc 8 lấy `VIE_path_maritime_denial` và `VIE_navy_blue_water` làm lối vào hai nhánh ("cần đối chiếu v7"). Đo trên repo: cả ba (và mọi focus hải quân cũ: `VIE_naval_aviation`, `VIE_cam_ranh_base`, `VIE_navy_lhd_program`…) chỉ còn trong `v11_removed_military_all_subbranches.txt` và `.bak`. Cây focus live (296 focus) có đúng một root quân sự `VIE_modernize_vpa` (266, 1).
**Fix:** T1 treo trực tiếp dưới `VIE_modernize_vpa` (đúng điều Trục 2 hải quân đã chốt ở N1: "Trục 3 sau này tự dựng cổng riêng"). Không phụ thuộc `VIE_naval_defence_law` của Trục 2 để Trục 3 không phải chờ Ba Son. Hai node Doctrine trở thành D1/B1 mới (xem A2 về ID).

## A2 · ID của báo cáo **đụng loc chết** và đụng kiểu đặt tên của repo

`localisation/english/VIE_md_p2_l_english.yml` vẫn giữ khóa của các focus đã xóa (`VIE_navy_modernization`, `VIE_naval_aviation`, `VIE_naval_infantry`, `VIE_cam_ranh_base`, `VIE_domestic_corvettes`…). Báo cáo dùng lại `VIE_naval_aviation` (B4): sẽ trùng khóa với loc mới và làm `verify_all_loc.py` báo trùng. Ngoài ra repo đặt ID bằng tiếng Anh với tiền tố nhóm (`VIE_lf_*` cho lục quân Trục 3; `VIE_nav_*`, `VIE_naval_*` cho hải quân Trục 1–2) và báo cáo dùng `VIE_org_*`, `VIE_dec_*`, `VIE_path_*`, `VIE_force_*`, mà `VIE_force_47` đã tồn tại (cùng vấn đề R3 của Trục 3 lục quân).
**Fix:** tiền tố **`VIE_nf_`** (naval force) cho focus, Decision, cờ, biến; **`VIE_p1b_`** cho Program Engine; namespace event `vie_nav_force` và `vie_p1b`. Bảng ánh xạ ở 5.1. Kiểm trước: `VIE_nf_`, `VIE_p1b_`, `vie_nav_force`, `vie_p1b` có 0 kết quả trong repo và MD.

## A3 · Gần như mọi cờ/biến ở mục 14 là **phản chiếu trạng thái** hoặc **chỉ ghi không ai đọc**

Quy tắc của chính báo cáo (16.3) và bài học đã áp ở Trục 2 hải quân (B5) và lục quân (R1): không giữ cờ chép lại trạng thái có sẵn.

| Mục báo cáo | Vấn đề | Xử lý |
|---|---|---|
| `VIE_org_naval_training`, `VIE_path_denial/greenwater/bluewater` | = `has_completed_focus` | **Bỏ**; dùng scripted trigger |
| `VIE_dec_*_active/_done/_waiting`, `_progress` | Trạng thái chờ giữa chừng không tồn tại (xem B1); `_progress` bị 16.3 cấm | **Bỏ** hết |
| `VIE_var_surface_readiness`, `VIE_var_sub_readiness`, `VIE_var_asw_skill`, `VIE_var_fleet_organization` (0–100) | Người đọc duy nhất là "template" (mà Quy tắc 10 cấm đổi giá/hull) và Kilo (chỉ thưởng) | **Bỏ biến số**; hiệu ứng vận hành đi thẳng vào `VIE_af_*` của dynamic modifier (L1 và 5.4). Giữ mức đã chọn (`VIE_nf_surface_level`…) vì không suy ra được |
| `VIE_var_hulls_<lớp>` cho 9 lớp | Chỉ lớp `carrier` và `destroyer` có người đọc (Decision nhóm tác chiến) | Giữ **2 bộ đếm**; `amphib` giữ chỗ cho nhánh Special Force qua `VIE_ext_*` khi nó tồn tại |
| `VIE_org_first_force`, `VIE_org_*_command` | Là kết quả Decision, HOI4 không hỏi được "Decision đã xong" (cùng lý do giữ `VIE_nav_dN_done`) | **Giữ** dưới tên `VIE_nf_dN_done` |

## A4 · `VIE_var_hulls_operational` **không tồn tại**: Trục 1–2 đã code `VIE_var_hulls_delivered`

Báo cáo (T6, 14.2) đọc `VIE_var_hulls_operational ≥ 4`. Trục 1 đã đổi tên thành `VIE_var_hulls_delivered` (đếm giao hàng tích lũy, mọi tàu trừ 1B; xem review Trục 1 B7) và Focus 3 của Trục 2 đã đọc nó (`> 3`).
**Fix:** T6 đọc `VIE_var_hulls_delivered > 3`. Chương trình 1B cộng `VIE_var_hulls_delivered` **chỉ cho thân tàu chủ lực** (FAC, corvette, khinh hạm, khu trục, tàu ngầm, tàu đổ bộ, tàu sân bay), đúng ý 14.2; tàu ngầm mini và tàu tiếp tế (bị hoãn, Q5) không cộng. Ghi rõ "từng giao" trong loc, vì tàu bị chìm vẫn tính.

## A5 · `VIE_var_naval_budget_room` không tồn tại; Funding Gate của 1B phải dùng cổng đã code

Mục 12.1 bước 4 dùng `VIE_var_naval_budget_room ≥ cost`. Trục 1 đã chốt dùng thẳng ngân khố: `VIE_naval_can_fund` (`treasury > VIE_naval_cost`) và nhánh thất bại kiểu event `vie_naval.43` (cắt quy mô / vay nợ ×1,1 / hoãn / hủy). **Fix:** 1B tái dùng đúng trigger và mẫu `VIE_naval_sigma_cost` → `…_funding_check` → `…_contract`; không tạo biến mới.

## A6 · Program Engine "dữ liệu thay cho event" **không thực hiện được nguyên văn** trong script HOI4

Mục 12.1 và 13.5: "thêm tàu mới chỉ thêm một dòng bảng". Nhưng `create_ship`, `create_equipment_variant`, tên tàu, `add_tech_bonus`, tên cờ/biến đều là **literal**; Trục 1 đã phải sinh mã bằng script (`gen4.py`, `gen6.py`). Bản clone MD không có mẫu tham số hóa tên biến bằng `$X$` trong scripted effect để dựa vào.
**Fix:** kiến trúc hai tầng.
1. **Dùng chung (viết tay):** 3 event pop-up (`vie_p1b.1` số lượng, `.2` mức nội địa hóa, `.3` thiếu vốn) đọc biến `VIE_p1b_cur` (mã chương trình 1–11) và các biến cấu hình `VIE_p1b_max_qty`, `VIE_p1b_unit_cost`… do effect nạp dữ liệu đặt; Funding Gate, slot, hoàn tất.
2. **Theo chương trình (sinh bằng `tools/gen_p1b.py` từ một bảng dữ liệu):** `VIE_p1b_load_<p>` (nạp dữ liệu), `VIE_p1b_ensure_variant_<p>`, `VIE_p1b_deliver_<p>` (có `create_ship` literal), event ẩn giao hàng `vie_p1b.1x`.
Số event thực tế ≈ 12 (3 chung + 9 ẩn), không phải "khoảng 7"; số effect sinh ra ~40.

## A7 · Tàu của 1B cần **hull tech + module tech** mà VIE không có; rủi ro lớn nhất của cả Trục 3

VIE mở đầu chỉ có `corvette_hull_1` (`VIE_Vietnam.txt:51`), đã hoàn tất `sp_naval_vessel_project`. MD đặt mỗi hull là một tech cùng tên (`destroyer_hull_4`, `carrier_hull_3`…, `start_year` = năm hull) và module (`module_sub_early_reactor_power` cần `tech_nuclear_power_systems_1`, mà tech này đòi `sp_medium_naval_nuclear_engines`). Trục 1 chưa cấp tech và đã ghi "rủi ro cao nhất" vào checklist; 1B không thể lặp lại cách đó cho 9 chương trình.
**Fix:** `VIE_p1b_load_<p>` kèm `set_technology = { <hull> = 1 … }` cho hull và các tech module chính khi **ký hợp đồng** (nhập khẩu = chuyển giao công nghệ). Bậc hull chọn theo năm (5.6). Kiểm trong game mục đầu của checklist (Phần 8); nếu `set_technology` không đủ thì lùi về `add_tech_bonus` + đòi nghiên cứu.

---

# PHẦN 3 — 8 CHỖ LỆCH SO VỚI MOD VÀ MD

## B1 · Trạng thái chờ giữa chừng (`_waiting`, "Decision chờ không chiếm slot")
Cùng lỗi B1 của Trục 2: HOI4 không có trạng thái này. **Fix:** cổng ở **lúc bấm** (`available` + `custom_trigger_tooltip` nói đúng điều còn thiếu); Decision đã bắt đầu thì chạy hết. Bỏ mọi `_waiting`.

## B2 · "Decision chạy nhiều sự kiện nối tiếp 12–18 tháng" cần cấu trúc đã dùng ở Trục 2
Decision = nút khởi động (`fire_only_once`, 50 PP), bấm xong bắn chuỗi event chọn, lựa chọn cuối trao **timed idea** hiển thị đang chạy (`add_timed_idea … days = <biến tạm>`, đã xác minh với MD) và hẹn event ẩn hoàn tất. Mọi hiệu ứng thật nằm ở event ẩn hoàn tất.

## B3 · Bộ đếm slot và nội chiến
`VIE_var_force_program_active` và `VIE_var_procurement_1b_active` (cap 2) cần **đếm lại theo timed idea** sau nội chiến, đúng như `VIE_nav_program_recount` đã làm cho Trục 2 (`VIE_collapse_aftermath`). Nếu không, event hoàn tất bị mất khi đổi tag sẽ kẹt bộ đếm ở 2.

## B4 · Nơi đặt modifier vận hành đã có sẵn
`VIE_armed_forces_modifier` (dynamic modifier gắn một lần bởi `VIE_modernize_vpa`, ghi bằng `add_to_variable = { VIE_af_* … tooltip = VIE_tt_* }`) đã có 14 modifier hải quân: `experience_gain_navy_factor`, `navy_max_range_factor`, `naval_coordination`, `navy_org_factor`, `naval_detection`, `navy_submarine_attack_factor`, `naval_strike_attack_factor`, `naval_speed_factor`, `naval_invasion_capacity`, `naval_invasion_planning_bonus_speed`, `navy_anti_air_attack_factor`, `naval_mines_effect_reduction`, `mines_planting_by_fleets_factor`, `navy_submarine_defence_factor`. Trục 3 hải quân dùng lại cơ chế này; chỉ **thiếu** `navy_personnel_cost_multiplier_modifier` (token MD có thật: `common/modifier_definitions/money_modifier_definitions.txt:30`) cho đánh đổi "chi phí duy trì cao" của Extended Range (11.4). Thêm 1 dòng ngoài khối `GEN:vars`, và **8 khóa tooltip `VIE_tt_*` còn thiếu** (xem bước 0). Bỏ ý "giảm chi phí duy trì" cũ khỏi Trục 2 là đúng: nay token đã có.

## B5 · Mã nguồn tàu "nhập khẩu" nên dùng variant VIE, không dùng variant của đối tác
Báo cáo không nói; Trục 1 đã chọn `creator = SOV` cho nhập khẩu (variant có sẵn của SOV) và variant VIE cho nội địa. Với 1B, đối tác (HOL, KOR, IND…) không có variant tương ứng trong MD cho mọi hull. **Fix:** **mọi** tàu 1B dùng variant do VIE tự tạo (`create_equipment_variant` có cờ chặn trùng, mẫu `VIE_naval_ensure_variants`), `creator = VIE`. Mức nội địa hóa chỉ đổi giá, thời gian và exp.

## B6 · Hull và slot ở bảng 16.2 cần bậc theo năm, tàu ngầm mini và tàu tiếp tế không khả thi
Bậc hull đã sửa ở review Trục 1 (corvette 1–8, frigate 1–8, destroyer 1–7, attack_submarine 1–8, helicopter_operator 1–6, carrier 1–7; `year` của từng bậc ở 5.6). Tàu ngầm mini không có hull riêng; tàu tiếp tế là `support_ship_N` không có module (mở bằng `tech_landing_craft_*`). **Fix:** hoãn P5 và P9 (Q5).

## B7 · Điều kiện tàu sân bay/SSN: `VIE_ext_nuclear_tech` chưa có chủ
Mục 14.5 đề xuất cờ cho "nhánh năng lượng" chưa có. Trong cây live **đã có** `VIE_nuclear_research` (focus nghiên cứu, `CAT_nuclear`). **Fix:** trigger `VIE_naval_has_nuclear_tech = { has_completed_focus = VIE_nuclear_research }` (một chỗ để đổi), cùng mẫu `VIE_naval_has_electronics` của Trục 2. Tech reactor thật được cấp lúc ký hợp đồng (A7).

## B8 · Quy ước event/decision/loc
Namespace chữ thường; log câu đầu mỗi option (không log nếu option chỉ đóng cửa sổ); `ai_chance` option tốn tiền có guard `bankruptcy_incoming_collapse` (và `ai_has_high_deficit` cho option không lịch sử); loc `localisation/english/VIE_md_events_nav_force_l_english.yml` (BOM, tiếng Việt, `:0`); `verify_all_loc.py`, `ev.py`, `audit.py`, `live.py` sau mỗi bước; category mới `allowed = { original_tag = VIE }`; mọi focus `search_filters = { FOCUS_FILTER_NAVY }`, `log` đầu `completion_reward`, `ai_will_do` base 60 (chuỗi) hoặc 40 (mở nhánh), `factor = 0` khi `bankruptcy_incoming_collapse`.

---

# PHẦN 4 — LỖ HỔNG LOGIC (6 mâu thuẫn nội bộ của báo cáo + 2 nối trục)

| # | Vấn đề | Vị trí báo cáo | Sửa |
|---|---|---|---|
| **L1** | "Readiness" 0–100 chỉ được đọc bởi template, mà Quy tắc 10 cấm template đổi giá/hull; thành ra biến không có người dùng thật | 13.5, 14.2 | Readiness = **mức đã chọn + modifier thật** (5.4). Hiệu ứng "độ sẵn sàng" là `navy_org_factor`, `naval_coordination`, `naval_detection` |
| **L2** | T9 đòi "T7 và T8" nhưng T8 đã đòi T7 | 11.1 | T9 chỉ đòi T8 |
| **L3** | P4 đòi `VIE_org_submarine_command` ở 14.1 nhưng bảng 12.2 không có điều kiện này | 12.2 vs 14.1 | Thêm vào `available` của P4: `VIE_nf_d2_done` |
| **L4** | P4 đòi `VIE_cap_naval_mro_sub`, cờ **không tồn tại**: Trục 2 đã code `VIE_var_mro_tier`, `VIE_mro_scope` (1 tàu ngầm, 2 tàu mặt nước, 3 cả hai), `VIE_nav_d2_done` | 12.2 | Trigger `VIE_naval_has_sub_mro = { has_country_flag = VIE_nav_d2_done NOT = { check_variable = { VIE_mro_scope = 2 } } }` |
| **L5** | Decision "thành lập nhóm tác chiến tàu sân bay" (B5) **không có trong danh sách 4 Decision** ở mục 11 và mục 15.2 | 11.5 vs 15.2 | Thêm làm Decision thứ 5 (`VIE_nf_d5_carrier_group`), điều kiện 1 tàu sân bay và 2 khu trục qua `VIE_var_hulls_carrier/_destroyer`. Bảng khối lượng: 5 Decision lực lượng |
| **L6** | "Mức chuyên môn… hướng còn lại mở lại bằng Event trễ với chi phí cao hơn" **không có event nào** định nghĩa; "lệch nhánh thì giảm `fleet_organization` 12 tháng" cần biến vừa bị bỏ | 11.2, 11.4 | Chuyên môn là lựa chọn một lần; hướng kia được bù một phần bởi event Hiệp đồng số 3 (mạng chống ngầm ven bờ). Lệch nhánh = `add_timed_idea` 365 ngày trừ org/coordination, đặt ngay ở focus mở nhánh |
| **L7** | **Kilo đọc readiness của Trục 3** (14.5) nhưng Kilo (đặt ngay 2009–2010) đến **trước** khi Decision tàu ngầm kết thúc | 14.2, 14.5 | Cờ `VIE_nf_sub_prep` đặt **ngay khi bấm** Decision tàu ngầm (event `.10`, mọi lựa chọn). Trục 1 `vie_naval.21` option A: nếu có cờ thì phí gói huấn luyện 0,15 tỷ/tàu thay vì 0,2. Chi phí huấn luyện không phải chi phí đóng/trang bị, không vi phạm Quy tắc 10; vẫn không phải điều kiện (Quy tắc 5) |
| **L8** | Cơ cấu lực lượng ban đầu (T6) chỉ so với T9 để phạt lệch; không có hiệu ứng nếu đi **đúng** nhánh | 11.4 | Đi đúng nhánh (Coastal→Denial, Balanced→bất kỳ, Extended→Greenwater/Bluewater): +1 mức thưởng nhỏ ở focus mở nhánh. Đối xứng với phạt |

---

# PHẦN 5 — THIẾT KẾ CHỐT CHO CODE

## 5.1 Hai mươi hai Focus (tọa độ tuyệt đối)

Anchor: toàn bộ neo vào **T1** (`relative_position_id = VIE_nf_training_standardization`, khai báo trước tất cả); T1 neo vào `VIE_modernize_vpa` (266, 1) với `x = -26, y = 1` → abs **(240, 2)**. Vùng x 216–254 trống ở mọi hàng, vùng x ≥ 200, y ≥ 9 trống (đo bằng `layout.py` ngày 2026-10-02); Trục 2 hải quân ở x 256–260, y 2–6; lục quân Trục 3 ở x 272–284, y 2–16.

| Mã | ID | Tên hiển thị | (dx,dy) → abs | Prerequisite | Ngày / điều kiện `available` |
|---|---|---|---|---|---|
| T1 | `VIE_nf_training_standardization` | Chuẩn hóa đào tạo hải quân | gốc → (240,2) | `VIE_modernize_vpa` | `date > 2004.12.31` |
| T3 | `VIE_nf_surface_force` | Phát triển lực lượng tàu mặt nước | (−4,1) → (236,3) | T1 | `date > 2004.12.31` |
| T4 | `VIE_nf_submarine_force` | Phát triển lực lượng tàu ngầm | (+4,1) → (244,3) | T1 | `date > 2007.12.31` |
| T5 | `VIE_nf_command_reform_1` | Cải cách bộ chỉ huy hải quân I | (0,2) → (240,4) | T3 **và** T4 | `date > 2009.12.31` (cần xác minh) |
| T6 | `VIE_nf_first_force` | Cơ cấu lực lượng ban đầu | (0,3) → (240,5) | T5; **OR** {`VIE_naval_mro`, `VIE_small_combatant_construction`} | `date > 2011.12.31`; `VIE_var_hulls_delivered > 3` |
| T7 | `VIE_nf_command_reform_2` | Cải cách bộ chỉ huy hải quân II | (0,4) → (240,6) | T6 | `date > 2013.12.31` |
| T8 | `VIE_nf_medium_force` | Lực lượng hải quân trung bình | (0,5) → (240,7) | T7 | `date > 2015.12.31` |
| T9 | `VIE_nf_operating_range` | Mở rộng phạm vi hoạt động | (0,6) → (240,8) | T8 | `date > 2017.12.31` |
| D1 | `VIE_nf_denial` | Ngăn chặn biển (Maritime Denial) | (−12,7) → (228,9) | T9; loại trừ G1, B1 | — |
| D2 | `VIE_nf_denial_defence` | Phòng thủ ven bờ tích hợp | (−12,8) → (228,10) | D1 | — |
| D3 | `VIE_nf_denial_subs` | Lực lượng tàu ngầm ngăn chặn | (−12,9) → (228,11) | D2 | — |
| D4 | `VIE_nf_denial_command` | Bộ chỉ huy phòng thủ ven bờ | (−12,10) → (228,12) | D3 | — |
| G1 | `VIE_nf_greenwater` | Hải quân khu vực | (0,7) → (240,9) | T9; loại trừ D1, B1 | — |
| G2 | `VIE_nf_regional_frigates` | Khinh hạm viễn hành | (−4,8) → (236,10) | G1 | — |
| G3 | `VIE_nf_amphibious_fleet` | Hạm đội đổ bộ | (+4,8) → (244,10) | G1 | — |
| G4 | `VIE_nf_lhd_program` | Chương trình tàu đổ bộ trực thăng | (0,9) → (240,11) | G2 **và** G3 | `date > 2021.12.31` |
| G5 | `VIE_nf_regional_command` | Bộ chỉ huy hạm đội khu vực | (0,10) → (240,12) | G4 | — |
| B1 | `VIE_nf_bluewater` | Hải quân viễn dương | (+16,7) → (256,9) | T9; loại trừ D1, G1 | — |
| B2 | `VIE_nf_ocean_escort` | Chương trình hộ tống viễn dương | (+10,8) → (250,10) | B1 | `date > 2023.12.31` |
| B3 | `VIE_nf_replenishment` | Bảo đảm hậu cần hạm đội | (+16,8) → (256,10) | B1 | `date > 2021.12.31` |
| B4 | `VIE_nf_naval_aviation` | Không quân hải quân | (+22,8) → (262,10) | B1 | `date > 2027.12.31` |
| B5 | `VIE_nf_carrier_group` | Nhóm tác chiến tàu sân bay | (+16,9) → (256,11) | B2, B3, B4 (ba khối riêng = AND) | `date > 2029.12.31` |

Khoảng cách cùng hàng tối thiểu 6 (quy tắc ≥ 4 của repo); con luôn `y >` cha. Ngày cổng 1B (P1…P11) lấy từ bảng 12.2 và đặt ở **Decision**, không ở focus (Quy tắc 6). Ba ngày gốc của báo cáo chưa kiểm: Lữ đoàn 162/167 (T5), Lữ đoàn 189 (báo cáo ghi 2013, bản gốc 2011), Cơ quan quản lý đóng tàu 2005 (T1): dùng như giá trị khởi điểm, ghi vào checklist. `ai_will_do`: 60 cho chuỗi; 40 cho D1/G1/B1 với `factor` theo path (Denial ×1,5 Historical, ×0,5 Reform; Greenwater ×1,5 Reform/Western, ×0,5 Historical; Bluewater ×1 Reform, ×0,25 Historical/Security; chỉ khi `VIE_ai_free` cho G và B), nhóm 40 trở lên còn lại 60.

**Phần thưởng focus** (chỉ XP, modifier và `unlock_decision_tooltip`; helper `VIE_nf_xp_10/15/20/25` theo mẫu `VIE_lf_xp_*`, có `has_selected_naval_grand_doctrine` → `add_mastery { folder = naval }`):

| Focus | Thưởng | Mở |
|---|---|---|
| T1 | XP +15; `experience_gain_navy_factor` +5% | category `VIE_naval_force_category` (tooltip) |
| T3 | `navy_org_factor` +2% | D-A (mặt nước) |
| T4 | `navy_submarine_attack_factor` +2% | D-B (tàu ngầm) |
| T5 | `navy_org_factor` +2%, `naval_coordination` +3% | D-C (hiệp đồng) |
| T6 | XP +10 | D-D (cơ cấu ban đầu) |
| T7 | `navy_org_factor` +2%, `naval_coordination` +3% | — |
| T8 | `navy_max_range_factor` +3% | lối vào 1B: P1, P2, P3 (từ ngày) |
| T9 | `navy_max_range_factor` +5%, `naval_detection` +5% | ba nhánh |
| Nhánh | Bảng 5.4 | Bảng 5.5 |

## 5.2 Năm Decision lực lượng (category `VIE_naval_force_category`, priority 92)

Category: `allowed = { original_tag = VIE }`, `visible = { has_completed_focus = VIE_nf_training_standardization }`. Mỗi Decision: `cost = 50` PP (D-E 60), `fire_only_once = yes`, `available` có `custom_trigger_tooltip` cho slot và từng điều kiện, `complete_effect` log đầu + `VIE_nf_program_start` + bắn chuỗi event; `ai_will_do` base 100, `factor = 0` khi `bankruptcy_incoming_collapse`.

| Decision | Mở từ | `available` | Chuỗi chọn | Hoàn tất (event ẩn) |
|---|---|---|---|---|
| D-A `VIE_nf_d1_surface` | T3 | slot (`VIE_var_force_program_active < 2`) | `.1` mức (Cơ bản 0,40 tỷ / 12 tháng; Chuyên sâu 0,60 tỷ / 18 tháng); `.2` chuyên môn: **Hỏa lực** hoặc **Chống ngầm** | `.61`: `VIE_nf_surface_level` = 1/2, `VIE_nf_surface_specialty`, modifier theo 5.4, `VIE_nf_d1_done`, −1 slot |
| D-B `VIE_nf_d2_submarine` | T4 | slot | `.10` định hướng: **Lịch sử** (chuẩn bị nhân lực trước khi nhận tàu, 0,30 tỷ) hoặc **Sớm** (đắt hơn, 0,50 tỷ, thưởng ban đầu cao hơn); đặt `VIE_nf_sub_prep` ngay; `.11` mức Cơ bản/Chuyên sâu (×1,0 / ×1,5) | `.62`: `VIE_nf_sub_level`, modifier, `VIE_nf_d2_done`, −1 slot |
| D-C `VIE_nf_d3_fleet_coord` | T5 | slot; `VIE_nf_d1_done`; `VIE_nf_d2_done` | không có lựa chọn (chuỗi cố định, 0,50 tỷ, 18 tháng) | `.50` (1/3: XP + org), `.51` (2/3: phối hợp tàu ngầm – tàu mặt nước, coordination), `.63` (hết: mạng chống ngầm ven bờ), `VIE_nf_d3_done` |
| D-D `VIE_nf_d4_first_force` | T6 | slot | `.30` ba lựa chọn đặt `VIE_nf_force_priority` (1 Coastal, 2 Balanced, 3 Extended Range), 0,60 tỷ / 12 tháng | `.64`: modifier theo lựa chọn, `VIE_nf_d4_done` |
| D-E `VIE_nf_d5_carrier_group` | B5 | slot; `VIE_var_hulls_carrier > 0`; `VIE_var_hulls_destroyer > 1` | không có lựa chọn (1,0 tỷ / 18 tháng) | `.65`: org/coordination nhân theo số tàu sân bay đã giao (1 hoặc 2+), `VIE_nf_d5_done` |

Thời lượng cố định theo mức (`set_temp_variable` rồi `days = <biến>`, mẫu `VIE_nav_d1_start`). Chuỗi chọn là event nối tiếp nên miễn `VIE_popup_cd` (người chơi chủ động bấm). **Mọi lựa chọn có đánh đổi số** (Quy tắc 9): mức đầu tư (chi phí/thời gian/trần), hướng hỏa lực–chống ngầm (modifier khác nhau), Historical–Sớm (chi phí vs thưởng), ba cơ cấu lực lượng.

Hai thay đổi so với báo cáo (cả hai nhằm giữ ngân sách pop-up và bỏ trạng thái chờ): (1) chuyên môn của D-A chọn ngay ở chuỗi, không ở "Event 2" giữa chừng; (2) D-C có hai milestone ẩn thay cho ba pop-up.

## 5.3 Hợp đồng cờ/biến giữa ba trục (sau sửa)

| Cạnh | Hướng | Qua | Trạng thái |
|---|---|---|---|
| Trục 3 T1 ← lục quân root | gate | `has_completed_focus = VIE_modernize_vpa` | có sẵn |
| Trục 2 → T6 | T2 → T3 | prerequisite `VIE_naval_mro` / `VIE_small_combatant_construction`; `VIE_var_hulls_delivered > 3` | Trục 2 ghi rồi |
| Trục 2 → 1B nội địa | T2 → 1B | `VIE_var_ba_son_tier`, `VIE_var_small_combatant_tier`, `VIE_var_integration_tier`, trigger `VIE_naval_has_sub_mro`, cờ `VIE_cap_mature_naval_industry` | Trục 2 ghi rồi |
| 1B → Trục 2 | 1B → T2 | helper `VIE_nav_add_shipbuilding_exp` / `VIE_nav_add_integration_exp` (đã có, kẹp 0–100) khi hoàn tất, theo mức nội địa hóa (0% / 50% / 100% của `exp_reward`) | Dùng lại helper |
| 1B → Trục 1/2 | 1B → T1/T2 | `VIE_var_hulls_delivered` +1 mỗi thân tàu chủ lực | Dùng lại biến |
| Trục 3 → Trục 1 | T3 → T1 | `VIE_nf_sub_prep` (L7). **Đây là sửa duy nhất vào Trục 1** | Cần sửa nhỏ `vie_naval.21` |
| Trục 3 → 1B | T3 → 1B | focus T8, D1, D3, G2, G4, B2, B4, B5, `VIE_nf_d2_done`; quyền mở ghi ở `available` của Decision 1B | Mới |
| Trục 1 → Trục 3 | không | — | Trục 3 không đọc cờ Trục 1 nào |
| Trục 3 → Trục 2 | không | Trục 3 không ghi `VIE_cap_*` hay biến exp (Quy tắc 11) | Giữ |

Một chiều, không vòng: Trục 1 → Trục 2 → {Trục 3, 1B}; chỉ có hai cạnh ngược (1B → exp/hulls của Trục 2, Trục 3 → Kilo) và cả hai chỉ **cộng thưởng**, không gate.

## 5.4 Hiệu ứng modifier (thang khởi điểm, Q: cần cân bằng)

Mẫu ghi: `add_to_variable = { VIE_af_navy_org_factor = 0.02 tooltip = VIE_tt_navy_org_factor }` + `custom_effect_tooltip { localization_key = modifies_dynamic_modifier_tt MODIFIER = VIE_armed_forces_modifier }` (đúng mẫu `VIE_d4_reward`). Trần đặt ra cho **đường đầy đủ** (như G2 của Trục 3 lục quân): `navy_org_factor` ≤ +18%, `naval_coordination` ≤ +20%, `naval_detection` ≤ +15%, `navy_max_range_factor` ≤ +25%, `navy_submarine_attack_factor` ≤ +10%, `navy_submarine_defence_factor` ≤ +10%, `naval_strike_attack_factor` ≤ +10%, `experience_gain_navy_factor` ≤ +10%. `tools/audit/nf_balance.py` cộng cả ba đường và kiểm các trần này.

| Nguồn | Modifier (+ = bonus) |
|---|---|
| D-A mức 1/2 × hỏa lực | `naval_strike_attack_factor` +3% / +4,5%; `navy_org_factor` +1% / +1,5% |
| D-A mức 1/2 × chống ngầm | `navy_submarine_defence_factor` +3% / +4,5%; `naval_detection` +2% / +3% |
| D-B mức 1/2 | `navy_submarine_attack_factor` +3% / +4,5%; `naval_detection` +1% / +1,5% (định hướng Sớm: +1% thêm) |
| D-C (ba giai đoạn) | `naval_coordination` +2% +2% +2%; `navy_submarine_defence_factor` +2% (giai đoạn 3); XP +10 |
| D-D Coastal | `naval_strike_attack_factor` +2%; `navy_max_range_factor` −3% |
| D-D Balanced | `navy_org_factor` +1%, `naval_strike_attack_factor` +1%, `navy_max_range_factor` +1% |
| D-D Extended Range | `navy_max_range_factor` +4%, `navy_org_factor` +2%; `navy_personnel_cost_multiplier_modifier` +3% |
| D1 / D2 / D3 / D4 | strike +3% / mines (`mines_planting_by_fleets_factor` +10%, `naval_mines_effect_reduction` +5%) / sub attack +3% / org +3%, detection +4% |
| G1 / G2 / G3 / G4 / G5 | range +5% / range +3%, org +2% / `naval_invasion_planning_bonus_speed` +10%, `naval_invasion_capacity` +1 / `naval_invasion_capacity` +1 / org +3%, coordination +3% |
| B1 / B2 / B3 / B4 / B5 | range +5% / `navy_anti_air_attack_factor` +5% / range +3% / AA +3%, detection +4% / org +3%, coordination +5% (nhân 1,0 / 1,5 theo số tàu sân bay đã giao, qua D-E) |
| Lệch nhánh so với `force_priority` | timed idea 365 ngày: `navy_org_factor` −3%, `naval_coordination` −3% (L6) |
| Đúng nhánh | +1% `navy_org_factor` (L8) |

Không có modifier sản xuất, chi phí đóng hoặc trang bị (Quy tắc 10). `navy_personnel_cost_multiplier_modifier` là chi phí nhân sự, không phải chi phí tàu.

## 5.5 Trục 1B — Program Engine (Decision, category `VIE_naval_program_category`, priority 90)

Bảng chương trình. Ngày lấy từ báo cáo 12.2; **giá thực tế** (tỷ USD mỗi tàu, mức nhập khẩu; nguồn ở cuối tài liệu) thay cho "giá trị khởi điểm" trừu tượng; mức nội địa hóa nhân ×1,0 / ×1,15 / ×1,3 (13.2); thời gian đóng nhân ×1,0 / ×1,2 / ×1,4.

| Mã | Chương trình | Lối vào (focus + ngày) | Hull MD | Giá/tàu | Số lượng (min–max) | Đến tàu đầu (tháng) | Điều kiện nội địa (Trục 2) |
|---|---|---|---|---|---:|---:|---|
| P1 | Hộ vệ hạm nhẹ | T8, ≥ 2016 | `corvette_hull_4` | 0,40 | 2–6 | 30 | `small_combatant_tier ≥ 2` và `ba_son_tier ≥ 2` |
| P2 | Khinh hạm cỡ trung | T8, ≥ 2018 | `frigate_hull_4` | 0,45 | 2–4 | 40 | `integration_tier ≥ 1` và `ba_son_tier ≥ 2` |
| P3 | Chống ngầm cơ động | T8, ≥ 2018 | `frigate_hull_4` (variant ASW) | 0,50 | 2–4 | 40 | `integration_tier ≥ 1` |
| P4 | Tàu ngầm tấn công khu vực | T8 và (D3 hoặc G2), ≥ 2020; `VIE_nf_d2_done` | `attack_submarine_hull_4` | 0,55 | 2–4 | 54 | `ba_son_tier = 3`, `integration_tier ≥ 2`, `VIE_naval_has_sub_mro` |
| P5 | Tàu ngầm mini | — | — | — | — | — | **Hoãn** (Q5) |
| P6 | Bastion-P mở rộng | D2 | (hệ thống bờ, không phải tàu) | 0,15 | 1–3 | 18 | Chỉ nhập khẩu |
| P7 | Tàu đổ bộ trực thăng/LHD | G4, ≥ 2022 | `helicopter_operator_hull_3` | 0,60 | 1–2 | 54 | `ba_son_tier = 3` |
| P8 | Khu trục | B2, ≥ 2024 | `destroyer_hull_4` | 0,70 | 2–3 | 48 | `integration_tier ≥ 2` và `ba_son_tier = 3` |
| P9 | Tàu tiếp tế | — | — | — | — | — | **Hoãn** (Q5) |
| P10 | Tàu sân bay hạng nhẹ | B4, ≥ 2028 | `carrier_hull_3` | 2,70 | 1 | 84 | `VIE_cap_mature_naval_industry` |
| P11 | Tàu ngầm hạt nhân | B5, ≥ 2030, `VIE_naval_has_nuclear_tech` | `attack_submarine_hull_5` | 2,00 | 1–2 | 96 | `VIE_cap_mature_naval_industry` |

Tổng chi phí tối đa nếu mua mọi chương trình ở mức nội địa (×1,3): ≈ 24,5 tỷ (số lượng tối đa mỗi chương trình) trong ~14 năm; chương trình đơn lẻ lớn nhất P11 ×2 ở nội địa = 5,2 tỷ, dưới p90 chi phí event MD (26,45 tỷ; trung vị 4,0). Chi phí Decision lực lượng: D-A + D-B + D-C + D-D ≈ 1,8 tỷ (mọi mức Cơ bản, D-B Lịch sử) tới ≈ 2,45 tỷ (mọi mức Chuyên sâu, D-B Sớm), cộng D-E 1,0. Đo bằng `tools/audit/nf_balance.py`.

**Chuỗi chương trình (mỗi chương trình, dùng chung):** Decision (`available`: focus, ngày, `VIE_var_procurement_1b_active < 2`, đối tác tồn tại và không chiến tranh nếu nhập khẩu, `NOT contracted`) → `vie_p1b.1` số lượng → `vie_p1b.2` nhập khẩu / hybrid / nội địa (mức sau đòi tier Trục 2) → Funding Gate (A5; thiếu vốn → `vie_p1b.3`: cắt quy mô / vay ×1,1 / hoãn / hủy) → `VIE_p1b_contract_<p>` (trừ tiền, `set_technology`, variant, hẹn giao, timed idea hiển thị) → event ẩn giao từng chiếc mỗi 8 tháng → chiếc cuối: cộng exp Trục 2 theo mức nội địa hóa, `VIE_p1b_<p>_complete`, −1 slot. Không có cửa sổ lịch sử, không event tự kích, không `P_late`.

**Mã dữ liệu mỗi chương trình (tiền tố `VIE_p1b_<p>_`):** cờ `contracted`, `cancelled`; biến `qty_ordered`, `qty_delivered`, `localization` (0–2). Không có `_complete`, `_offered`, `_missed` (cùng lý do A3). `<p>` ∈ {`corvette`, `frigate_med`, `asw_frigate`, `ssk_reg`, `bastion2`, `amphib`, `destroyer`, `carrier`, `ssn`}.

**Đối tác nhập khẩu (mặc định, Q6):** P1, P3: HOL hoặc SOV; P2: HOL hoặc KOR; P4, P6, P11: SOV; P7: KOR hoặc FRA; P8, P10: IND. Cổng = `country_exists` và `NOT has_war_with`; nếu cả hai đối tác không còn thì chỉ mở hybrid/nội địa (nếu đủ tier) hoặc không mở.

## 5.6 Hull, tech và variant (template = cặp variant + create_ship)

Bậc hull và năm (từ `MD_mtg_ships.txt`; hull tech cùng tên với hull, `start_year` = năm):

| Lớp | Bậc → năm | Chọn cho |
|---|---|---|
| corvette | 3→1995, 4→2010, 5→2025 | P1: `corvette_hull_4` |
| frigate | 3→1995, 4→2010, 5→2025 | P2, P3: `frigate_hull_4` (Sigma/Gepard đã dùng bậc 3) |
| destroyer | 3→2005, 4→2025 | P8: `destroyer_hull_4` |
| helicopter_operator | 3→2020, 4→2045 | P7 |
| carrier | 3→2005, 4→2025 | P10: `carrier_hull_3` |
| attack_submarine | 4→2010, 5→2025 | P4: bậc 4; P11: bậc 5 |

Mỗi chương trình có `VIE_p1b_ensure_variant_<p>` (cờ chặn trùng, mẫu `VIE_naval_ensure_variants`): `type`, `parent_version`, `modules` chép từ một variant MD có sẵn của tàu thật tương đương (tìm ở bước 7 trong `history/countries/` của HOL, KOR, IND, SOV, FRA), `role_icon_index`, `icon`. P11 dùng `module_sub_early_reactor_power`; P3 là variant con của P2 (thêm module sonar kéo, ngư lôi). Tên slot phải là slot của hull đó (slot sai bị bỏ im lặng). Tên tàu: placeholder, `TODO(names)`.

## 5.7 Biến và cờ cuối cùng

| Tên | Loại | Đặt bởi | Đọc bởi |
|---|---|---|---|
| `VIE_var_force_program_active` | biến 0–2 | `VIE_nf_program_start/end`, `VIE_nf_program_recount` | `available` của 5 Decision lực lượng |
| `VIE_var_procurement_1b_active` | biến 0–2 | `VIE_p1b_program_start/end`, recount | `available` của Decision 1B |
| `VIE_nf_surface_level`, `VIE_nf_surface_specialty`, `VIE_nf_sub_level`, `VIE_nf_sub_orientation` | biến | event chọn | `.61`/`.62` (modifier), Decision 1B (hiển thị) |
| `VIE_nf_force_priority` | biến 1–3 | `.30` | focus D1/G1/B1 (L6, L8) |
| `VIE_nf_d1_done` … `VIE_nf_d5_done` | cờ | event ẩn hoàn tất | D-C, P4, D-E |
| `VIE_nf_sub_prep` | cờ | `vie_nav_force.10` | `vie_naval.21` (Kilo, chỉ thưởng) |
| `VIE_var_hulls_carrier`, `VIE_var_hulls_destroyer` | biến ≥ 0 | `VIE_p1b_deliver_carrier/_destroyer` | D-E |
| `VIE_p1b_cur`, `VIE_p1b_max_qty`, `VIE_p1b_unit_cost`, `VIE_p1b_*` tạm | biến | `VIE_p1b_load_<p>` | event chung `vie_p1b.1–.3` |
| `VIE_p1b_<p>_contracted/_cancelled`; `…_qty_ordered/_qty_delivered/_localization` | cờ/biến | engine | giao hàng, hiển thị |
| `VIE_var_hulls_delivered` | biến (đã có) | 1B +1 mỗi thân tàu chủ lực | T6, Focus 3 Trục 2 |

Trigger mới (file `VIE_md_triggers_naval_force.txt`): `VIE_nf_branch_denial/_greenwater/_bluewater` (= `has_completed_focus`), `VIE_naval_has_sub_mro`, `VIE_naval_has_nuclear_tech`, `VIE_nf_slot_free`, `VIE_p1b_slot_free`. Idea (file `VIE_md_ideas_nav_force.txt`): `VIE_nf_prog_surface/_sub/_coord/_first/_csg`, `VIE_p1b_prog_<p>`, `VIE_nf_branch_mismatch_idea` (timed 365 ngày).

## 5.8 AI

Focus: 5.1. Decision lực lượng: `ai_will_do` base 100, `factor = 0` khi `bankruptcy_incoming_collapse`; lựa chọn event: option Historical/Cơ bản có `base 90` + `add 100 VIE_ai_historical`; option khác `factor 0 NOT VIE_ai_free`, có guard bankruptcy và `ai_has_high_deficit`. Decision 1B: base 20 và chỉ khi `VIE_ai_free` (AI không đi alt-history ngoài chế độ free), cùng guard tài chính, đảm bảo tránh slot bị giữ vô ích (bài học của review rà soát hai trục trước: option AI luôn phải có đường chọn được).

---

# PHẦN 6 — PLAN CODE (10 bước, mỗi bước 1 commit, nhánh `naval-truc3-force`)

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt` (+1 dòng `navy_personnel_cost_multiplier_modifier`, ngoài `GEN`); `localisation/english/replace/VIE_md_vi_tt_l_english.yml` (+8 khóa: `VIE_tt_experience_gain_navy_factor`, `_navy_max_range_factor`, `_naval_coordination`, `_navy_org_factor`, `_naval_detection`, `_navy_submarine_attack_factor`, `_naval_strike_attack_factor`, `_navy_personnel_cost`); `tools/audit/nf_balance.py` (cộng ba đường + trần + chi phí); `common/scripted_triggers/VIE_md_triggers_naval_force.txt` | Thêm biến đổi và trigger của 5.7; số liệu của 5.4 | `nf_balance.py` PASS; brace; console `effect add_to_variable = { VIE_af_navy_org_factor = 0.01 }` thấy dòng trong tooltip |
| **1** | `common/scripted_effects/VIE_md_effects_nav_force.txt` (phần 1) | `VIE_nf_xp_10/15/20/25`, `VIE_nf_add_*` (ghi `VIE_af_*`), `VIE_nf_program_start/end`, mở rộng recount | brace; scan effect chưa định nghĩa |
| **2** | `common/national_focus/VIE_md_focus.txt` + loc | Chuỗi chung T1, T3–T9 (8 focus), reward chỉ modifier + XP + tooltip | `audit.py`: 0 dangling/forward-ref/cycle/trùng tọa độ; `layout.py`; mở cây: cột hải quân x 240 |
| **3** | cùng file | 14 focus nhánh (ME D1/G1/B1; phạt/thưởng lệch/đúng nhánh); icon generic tạm; thêm 22 mục vào `FOCI` của `tools/build_vie_focus_icons.py` | ME đúng; `audit.py` 22/22 |
| **4** | `common/decisions/VIE_md_nav_force_decisions.txt`, category (`VIE_md_categories.txt`), `common/ideas/VIE_md_ideas_nav_force.txt`, `events/VIE_nav_force.txt` (`add_namespace = vie_nav_force`) | D-A và D-B (event `.1 .2 .10 .11 .61 .62`); sửa Kilo `vie_naval.21` (L7) | chơi: T1→T3→D-A: tiền trừ, timed idea, 12/18 tháng sau modifier xuất hiện; D-B đặt `VIE_nf_sub_prep` ngay; Kilo A rẻ hơn khi có cờ |
| **5** | cùng file | D-C (`.50 .51 .63`), D-D (`.30 .64`), D-E (`.65`) | slot không vượt 2; D-C cần cả hai `_done` |
| **6** | `tools/gen_p1b.py` (bảng dữ liệu) → `common/scripted_effects/VIE_md_effects_p1b_*.txt`; `events/VIE_p1b.txt` (`vie_p1b.1–.3`, ẩn `.11–.19`); `common/decisions/VIE_md_p1b_decisions.txt` + category `VIE_naval_program_category` | Lát cắt P1, P2, P3 trước; Funding Gate dùng `VIE_naval_can_fund` | chơi đến 2016: Decision P1 hiện sau T8; hợp đồng trừ tiền; tàu đến; `error.log` không có `equipment_variant does not exist` |
| **7** | cùng file generator | P4, P6, P7, P8, P10, P11; `set_technology` hull/module (A7); chép module từ variant MD tương đương | `error.log`: grep `module`, `slot`, `hull`; mở màn hình thiết kế thấy variant; SSN có module reactor |
| **8** | `VIE_md_effects_p3.txt` (`VIE_collapse_aftermath`) | Đếm lại hai bộ đếm slot mới theo timed idea | checklist nội chiến |
| **9** | `localisation/english/VIE_md_events_nav_force_l_english.yml` (+ `VIE_md_events_p1b_l_english.yml` nếu tách); `tools/TESTING.md`; `VIE_v9_flag_mapping.md` (bảng "Truc 3 hai quan"); cập nhật báo cáo | Loc toàn bộ (BOM, `:0`); mục TESTING "Naval force" | `verify_all_loc.py`, `ev.py`, `live.py`, `audit.py`, `nf_balance.py` sạch |
| **10** | `ai_chance`/`ai_will_do` rà soát | Kiểm AI chọn được ở mọi event (bài học zero-weight) | `review.py`-kiểu quét: không option nào mọi trọng số 0 |

Ước lượng: 22 focus, 5 Decision lực lượng + 9 Decision 1B, ~24 event (12 lực lượng + 12 của 1B), ~1 700 dòng script (≈ 1 000 do generator sinh), ~330 khóa loc.

Bộ kiểm tĩnh sau mỗi bước: `python tools/verify_all_loc.py`, `tools/audit/live.py`, `ev.py`, `audit.py`, `nf_balance.py`, và các script quét cờ/biến/option (`review.py`, `check6.py` trong scratchpad của phiên Trục 2).

---

# PHẦN 7 — CÂU HỎI CẦN CHỐT (mặc định đã gắn; chỉ ghi lại khi bạn muốn đổi)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q1 | T1 treo dưới `VIE_modernize_vpa` hay sau `VIE_naval_defence_law`? | **Dưới `VIE_modernize_vpa`** (A1, N1 của Trục 2) | Sau F1: đổi prerequisite và tọa độ T1, 1 dòng |
| Q2 | Readiness 0–100 hay mức + modifier? | **Mức + modifier thật** (L1) | Giữ biến số: thêm 4 biến, nhưng cần người đọc thật |
| Q3 | Chuyên môn ở chuỗi chọn đầu thay cho "Event 2" giữa chừng? | **Có** (5.2) | Muốn event giữa chừng: thêm 1 pop-up mỗi Decision, vượt ngân sách pop-up |
| Q4 | Tiền tố `VIE_nf_` / `VIE_p1b_`; namespace `vie_nav_force` / `vie_p1b` | **Như trên** (A2) | Đổi hàng loạt trước bước 1 |
| Q5 | Hoãn P5 (tàu ngầm mini) và P9 (tàu tiếp tế)? | **Hoãn**: không có hull/slot tương ứng (B6). Focus B3 và lựa chọn "tàu ngầm mini" của D-B chỉ còn modifier | Làm P5 bằng `attack_submarine_hull_1` tối giản; P9 cần kiểm `support_ship_2` |
| Q6 | Đối tác nhập khẩu theo 5.5? | **Như bảng** | Đổi bảng dữ liệu của generator |
| Q7 | Giá thực tế của 5.5 làm mặc định? | **Có**, nguồn cuối tài liệu | Đổi một cột bảng |
| Q8 | Bậc hull của 5.6? | **Như bảng**; kiểm chỉ số thật ở bước 7 | Đổi bảng dữ liệu |
| Q9 | Cổng SSN: `VIE_nuclear_research` + cấp tech reactor khi ký? | **Có** (B7) | Đổi trigger 1 dòng |
| Q10 | Chỉ giữ 2 bộ đếm lớp (`carrier`, `destroyer`)? | **Có** (A3) | Thêm bộ đếm khi có người đọc |
| Q11 | Thưởng Kilo bằng giá gói huấn luyện 0,15 thay 0,2 tỷ khi có `VIE_nf_sub_prep`? | **Có** (L7) | Đổi số hoặc bỏ thưởng |
| Q12 | Thang modifier và trần ở 5.4 | **Giá trị khởi điểm**, cần cân bằng bằng `nf_balance.py` | Đổi số |

---

# PHẦN 8 — CHECKLIST THỬ TRONG GAME (dự kiến, đưa vào `tools/TESTING.md` ở bước 9)

- [ ] **Rủi ro cao nhất:** `set_technology = { destroyer_hull_4 = 1 }` (và hull/module khác) có đủ để `create_equipment_variant` + `create_ship` dựng được tàu cho VIE không? Có dòng "equipment_variant does not exist" nào trong `error.log`?
- [ ] Module của variant 1B có bị bỏ im lặng vì thiếu tech không (màn hình thiết kế)? SSN có module reactor?
- [ ] Cây focus: cột hải quân x 240, ba nhánh đúng chỗ, ME D1/G1/B1; đường kẻ từ T6 tới hai focus Trục 2 đọc được.
- [ ] Pop-up/năm sau khi thêm Trục 3 (chỉ các pop-up chuỗi chọn do người chơi bấm): vẫn ≤ 7 theo luật `TESTING.md`.
- [ ] D-B đặt `VIE_nf_sub_prep` ngay; Kilo (sau 2009-12) rẻ hơn 0,05 tỷ/tàu khi có cờ; không có cờ thì giữ 0,2.
- [ ] Cổng `VIE_var_hulls_delivered > 3` của T6 mở đúng sau Gepard I + Molniya trên đường lịch sử.
- [ ] Hai bộ đếm slot: bấm 2 Decision lực lượng thì Decision thứ 3 xám; sau nội chiến về đúng số timed idea đang chạy.
- [ ] 1B: Funding Gate thất bại → `vie_p1b.3` mở đủ 4 lựa chọn; vay nợ nhân 1,1; hủy không trừ tiền; giao đúng 8 tháng/tàu; chiếc cuối cộng exp cho Trục 2 và `VIE_var_hulls_delivered`.
- [ ] `navy_personnel_cost_multiplier_modifier` hiển thị và đúng dấu (MD đánh dấu `color_type = bad`; đơn vị chưa kiểm).
- [ ] Lệch nhánh so với `force_priority`: timed idea phạt 365 ngày hiện và tự mất.

---

# NGUỒN GIÁ (tỷ USD, chọn làm mặc định ở 5.5)

- Gowind 2500: ≈ 0,425/tàu (Abu Dhabi, 850 triệu cho 2 tàu, 2019); Ai Cập ≈ 0,27. [Gowind-class design](https://en.wikipedia.org/wiki/Gowind-class_design) → P1 0,40.
- Arrowhead 140 (Indonesia): 0,36/tàu theo hợp đồng 2 tàu 720 triệu. [Janes](https://www.janes.com/defence-intelligence-insights/defence-news/sea/indonesia-to-implement-arrowhead-140-design-on-iver-huitfeldt-variant-contract) → P2 0,45, P3 0,50 (thêm sonar, ngư lôi, trực thăng).
- Type 214: 0,33 (2008), tàu mới 0,5–0,7; Soryu ≈ 0,665; Scorpène ≈ 0,45. [Type 214](https://en.wikipedia.org/wiki/Type_214_submarine), [Sōryū-class](https://en.wikipedia.org/wiki/S%C5%8Dry%C5%AB-class_submarine) → P4 0,55.
- Juan Carlos I: € 462 triệu. [Wikipedia](https://en.wikipedia.org/wiki/Spanish_amphibious_assault_ship_Juan_Carlos_I) → P7 0,60.
- Kolkata ≈ 0,64–0,73; Type 052DM ≈ 0,6. [Kolkata-class](https://en.wikipedia.org/wiki/Kolkata-class_destroyer), [Type 052D](https://en.wikipedia.org/wiki/Type_052D_destroyer) → P8 0,70.
- INS Vikrant: ≈ 2,7 (₹23.000 crore). [INS Vikrant](https://en.wikipedia.org/wiki/INS_Vikrant_(2013)) → P10 2,70.
- Suffren ≈ € 1,73 tỷ (2014); Astute ≈ £ 1,5–1,65 tỷ; Virginia ≈ 4,3–4,5. [Suffren-class](https://en.wikipedia.org/wiki/Suffren-class_submarine), [Astute-class](https://en.wikipedia.org/wiki/Astute-class_submarine) → P11 2,00 (mức Suffren/Astute, không phải Virginia).
- Bastion-P 0,15/tổ hợp: giữ giá đã chốt ở Trục 1.

---

# TRẠNG THÁI THI CÔNG (2026-10-02)

Bước 0–9 đã code, chưa chạy trong game, chưa commit. Bước 10 (rà AI) làm bằng đọc: mọi option của event đều có ít nhất một lựa chọn khả dụng với trọng số dương; Decision 1B chỉ AI `VIE_ai_free` bấm.

| Bước | Trạng thái | Lệch so với plan |
|---|---|---|
| 0 | Xong: `navy_personnel_cost_multiplier_modifier`, 8 khóa `VIE_tt_*`, `nf_balance.py`, `VIE_md_triggers_naval_force.txt` | Số trong 5.4 đã chỉnh sau khi script báo vượt trần: T8 range +3%, T9 +5%, B1 +5%, B3 +3%, D-D Extended +4%, D4/B4 detect +4% |
| 1 | Xong: `VIE_md_effects_nav_force.txt` (XP, dm tooltip, slot) | — |
| 2–3 | Xong: 22 focus; `VIE_nf_branch_mismatch_idea`; 22 mục `FOCI` | — |
| 4 | Xong: D-A, D-B, 5 idea, recount (gọi trong `VIE_collapse_aftermath`), Kilo L7 | Category priority 94 (92 đã bị `VIE_def_industry_category` dùng) |
| 5 | Xong: D-C, D-D, D-E | Thưởng D-E = thêm 0,25× (1 tàu sân bay) hoặc 0,5× (từ 2) thưởng B5 |
| 6–7 | Xong: `tools/gen_p1b.py`; 9 chương trình P1–P4, P6–P8, P10, P11 | Variant dùng `allow_without_tech = yes` (mẫu `05_netherlands.txt`); hybrid đòi điều kiện Trục 2 nhẹ hơn nội địa một bậc; category 1B priority 89; P5, P9 hoãn (Q5) |
| 8 | Xong: hai hàm recount nối vào `VIE_collapse_aftermath` | Làm cùng bước 4 và 6 |
| 9 | Xong: loc, `tools/TESTING.md` (mục "Naval force and Program 1B"), bảng cờ trong `VIE_v9_flag_mapping.md` | — |

Mở: module variant P8 và P7 chưa có mẫu MD đầy đủ; bunker P6 chồng lên Bastion Trục 1; icon/ảnh event chưa tạo; ngày T5/T1 và Lữ đoàn 189 chưa xác minh.

## Cap nhat 2026-10-02: cum Luat Bien chuyen sang nhanh Bien Dong

- 10 focus (law_of_the_sea, maritime_militia, fisheries_surveillance, dk1_platforms, legal_warfare, spratly_fortification, coast_guard_law, assert_maritime_rights, paracel_ultimatum, limited_war_doctrine) gom thanh mot khoi trong `VIE_md_focus.txt`, bo `FOCUS_FILTER_NAVY`; ID, vi tri luoi, prerequisite khong doi.
- `VIE_assert_maritime_rights` mo som qua `VIE_nf_branch_denial` (Truc 3) thay cho `VIE_maritime_denial_idea` (da xoa). Chieu phu thuoc duy nhat: nang luc hai quan -> mo focus Bien Dong.
- Ngan sach modifier chung `VIE_armed_forces_modifier`: Truc 3 da cham tran coord 19.5/20 va detect 14.5/15 -> Bien Dong chi con `VIE_af_navy_max_range_factor` +0.05 (spratly_fortification); `nf_balance.py` tinh them SCS, PASS.
- 1B: doi tac `destroyer`/`carrier` doi `IND` -> `RAJ` (An Do), sinh lai file.

## Cap nhat 2026-10-02: giai doan 2 - Hop tac an ninh bien (nhanh Bien Dong)

- 4 focus moi: `VIE_scs_maritime_cooperation` (goc, sau `VIE_law_of_the_sea`), `VIE_scs_multilateral_exercise`, `VIE_scs_cam_ranh_port` (cap `VIE_cam_ranh_idea`, can Bon Khong / khong lien minh), `VIE_scs_joint_training` (can ca hai nhanh + doi tac An Do/Nhat hoac co kilo).
- Category `VIE_scs_cooperation_category` (priority 88), 5 decision (tap tran, tham cang, huan luyen chung RAJ/SOV/JAP), event `vie_scs_coop.1` / `.10`, scripted trigger `VIE_scs_pc_ok` / `VIE_scs_pc_any` / `VIE_scs_non_aligned`.
- Khong cong vao `VIE_armed_forces_modifier`; `VIE_cam_ranh_idea` experience 0.05 -> 0.01 de tong `experience_gain_navy_factor` (truc luc luong 5 + coast guard 4 + Cam Ranh 1) khop tran 10; `nf_balance.py` doc truc tiep file idea.
- MD da dat san naval_base 8 tai Nha Trang (province 10162, state 519) nen khong xay them ha tang o Cam Ranh.

---

## Phần 4: Scripted Effects Nhánh Hải quân — Nội dung Chi tiết + Plan Code

# EFFECT NHÁNH HẢI QUÂN — NỘI DUNG CHI TIẾT + PLAN CODE

> Mục tiêu: đưa effect của nhánh hải quân (Trục 2 CNQP: 6 focus; Trục 3 lực lượng: 22 focus) lên mức chi tiết của nhánh lục quân (`VIE_lf_*`, 30 focus).
> Nguồn đối chiếu: `common/scripted_effects/VIE_md_effects_p17.txt` (30 effect `VIE_lf_*_reward`), `Báo cáo Lục quân VIE — Trục 1, 2, 3.md` mục 8.11, 8.13, 8.14, `tools/audit/lf_balance.py`; phía hải quân: `common/national_focus/VIE_md_focus.txt` (dòng 2991–3910), `VIE_md_effects_nav_force.txt`, `VIE_md_effects_nav_ind.txt`, `VIE_naval_truc2/3_review_and_plan.md`, `tools/audit/nf_balance.py`.
> Ngày: 2026-10-05. **Chưa sửa dòng code nào.** Mọi con số ở Phần 2–5 đã được kiểm bằng script (Phần 6), không phải ước lượng.

---

# PHẦN 0 — HIỆN TRẠNG: HẢI QUÂN THIẾU GÌ SO VỚI LỤC QUÂN

| Hạng mục | Lục quân (đã code) | Hải quân (hiện tại) |
|---|---|---|
| Nơi đặt effect | Mỗi node một scripted effect `VIE_lf_<mã>_reward` (30 effect) | Viết thẳng trong `completion_reward` của focus, không có effect đặt tên |
| Số hiệu ứng mỗi node | 2–5 dòng: modifier, XP/PP/command power, cờ, mẫu sư đoàn, giảm cost | 1–2 dòng modifier + `VIE_nf_dm_tt`; Trục 2 chỉ có XP + tooltip |
| PP / command power | N1 +25 PP, N2 +15 CP, `VIE_def_industry_law` +50 PP… | **0 node** hải quân cấp PP hoặc CP |
| Cái giá ở node đầu hướng | FM1, FR1, FD1, PS, PT đều có 1–4 khoản âm | D1/G1/B1 không có khoản âm nào, chỉ có timed idea khi lệch nhánh |
| Hướng đã chọn đổi effect node sau | CR2, L1/L2, A1/A2, Y1/Y2, MOD, CAP đọc cờ hướng | Chỉ D1/G1/B1 đọc `VIE_nf_force_priority`; T7, các node giữa và capstone không đọc gì |
| Sở trường (cost −14 ngày, node cuối ×1,5) | `VIE_lf_fav_discount` | Không có |
| Mốc lịch sử → giảm cost focus | 5 event + `VIE_event_scheduler_p17` + catch-up sau nội chiến | 0 event mốc cho Trục 3 |
| Decision huấn luyện lặp lại | 6 decision (cooldown 545 ngày, timed idea) | 5 decision một lần; **decision "Huấn luyện chống ngầm" mà báo cáo lục quân 8.14 giao cho Hải quân chưa tồn tại** |
| Số chiều modifier | ~12 (org, phòng thủ, tấn công, tốc độ, dig-in, nhân lực, hậu cần, chi phí, XP, pháo…) | 8 chiều, trong đó 5 chiều đã ở ≥ 95% trần: coordination 19,5/20, detection 14,5/15, range 25/25, subatk 9,5/10, strike 9,5/10 |
| Công cụ cân bằng | `lf_balance.py`: điểm từng node, ròng từng hướng, trần | `nf_balance.py`: chỉ trần và tiền |

Hệ quả: nhánh hải quân hiện tại không còn chỗ trong trần để thêm modifier cũ. Hướng giải: thêm **chiều mới** (3 modifier) và effect **ngoài modifier** (PP, CP, XP, tech bonus, giảm cost), không nâng trần cũ.

Hai lỗi nhỏ tìm thấy khi đọc:
1. Dòng 2991 ghi header "TRUC 2 HAI QUAN (CNQP)" nhưng bên dưới là T1 của Trục 3 (`VIE_nf_training_standardization`) rồi mới đến 5 focus Trục 2. Chỉ cần sửa comment.
2. `VIE_naval_defence_2030` không có `cost` (dùng mặc định 10), trong khi 5 focus còn lại của Trục 2 là 5 hoặc 7. Đề xuất giữ (capstone) nhưng ghi comment cho rõ.

---

# PHẦN 1 — NGUYÊN TẮC VÀ THANG ĐIỂM

## 1.1 Sáu nguyên tắc (rút từ lục quân)

1. **Một node = một effect đặt tên** `VIE_nf_<mã>_reward` (Trục 3) hoặc `VIE_nav_f<n>_reward` (Trục 2); focus chỉ còn `log` + gọi effect.
2. **Mỗi node có hơn một loại hiệu ứng**: modifier + (XP hoặc PP hoặc CP) + (tech bonus hoặc giảm cost ở node chọn lọc).
3. **Node đầu hướng trả giá** (D1, G1, B1): khoản âm đo bằng cùng thang điểm; ròng mỗi node đầu ≈ 2,4–4,2 điểm.
4. **Hướng đã chọn đổi effect node sau**: T7 đọc `VIE_nf_force_priority` (như CR2 đọc hướng); D-D mở giảm cost 14 ngày cho node đầu nhánh khớp (như `VIE_lf_fav_discount`).
5. **Mốc lịch sử không khóa ngày** (`available` giữ nguyên `date >`): chỉ giảm cost focus chưa làm hoặc thưởng nhỏ nếu đã làm (mẫu `VIE_lf_ms*_apply`).
6. **Trục 3 chỉ cấp modifier vận hành** (Quy tắc 10) và **không ghi `VIE_cap_*`/tier của Trục 2** (Quy tắc 11). Trục 2 chỉ ghi biến exp của chính nó.

## 1.2 Ba modifier mới và thang điểm

Ba modifier bổ sung vào `VIE_armed_forces_modifier` (token đã có trong repo/MD, loc tooltip đã có sẵn trừ `naval_hit_chance`):

| Modifier | Biến `VIE_af_*` | Token có thật ở | Loc `VIE_tt_*` |
|---|---|---|---|
| `naval_hit_chance` | `VIE_af_naval_hit_chance` | `common/ideas/VIE_md_ideas_p2.txt:1188`, `tools/audit/md_ref/tech_custom_tech.txt:490` | **thiếu**, thêm |
| `navy_capital_ship_attack_factor` | `VIE_af_navy_capital_ship_attack_factor` | `common/ideas/VIE_md_ideas_p3B.txt:10` | có (`VIE_md_vi_tt_l_english.yml:20`) |
| `navy_capital_ship_defence_factor` | `VIE_af_navy_capital_ship_defence_factor` | `common/ideas/VIE_md_ideas_p3B.txt:11` | có (`:21`) |

Hai modifier đã khai báo trong dynamic modifier nhưng Trục 3 chưa dùng: `naval_speed_factor`, `naval_strike_targetting_factor` (chỉ dùng `naval_speed_factor`).

Trọng số điểm (1 điểm = +1% tổ chức): org 1,0 · coordination 1,0 · strike 1,0 · subatk 1,0 · subdef 1,0 · detection 0,8 · AA 0,8 · capital atk/def 0,8 · range 0,6 · speed 0,7 · hit chance 1,2 · mines_plant 0,2 · mines_reduction 0,5 · invasion_plan 0,3 · invasion_cap 3,0/đơn vị · XP 0,5 · chi phí nhân sự −1,0 mỗi +1%.

Trần toàn đường (v2): các trần cũ giữ nguyên (org 18, coord 20, detect 15, range 25, subatk 10, subdef 10, strike 10, exp 10); trần mới: hit 10, speed 10, capital atk 8, capital def 8, AA 12, chi phí nhân sự ròng +6.

---

# PHẦN 2 — TRỤC 3: NỘI DUNG EFFECT TỪNG FOCUS (22 NODE)

Ký hiệu: **(giữ)** = đã có trong code, không đổi; **(mới)** = thêm. Số trong ngoặc là điểm theo 1.2. Mọi modifier đi qua `add_to_variable = { VIE_af_* … tooltip = VIE_tt_* }` rồi `VIE_nf_refresh = yes`.

## 2.1 Chuỗi dùng chung (8 node)

| Mã | Focus | Modifier | Ngoài modifier | Điểm |
|---|---|---|---|---|
| T1 | `VIE_nf_training_standardization` | `experience_gain_navy` +5% (giữ); `naval_hit_chance` +1% (mới) | XP 15 (giữ); **+25 PP (mới)**; tooltip mở category (giữ) | 3,7 |
| T3 | `VIE_nf_surface_force` | `navy_org` +2% (giữ); `naval_hit_chance` +1% (mới) | **XP 10 (mới)**; mở D-A (giữ) | 3,2 |
| T4 | `VIE_nf_submarine_force` | `navy_submarine_attack` +2% (giữ); `navy_submarine_defence` +1% (mới) | **XP 10 (mới)**; mở D-B (giữ) | 3,0 |
| T5 | `VIE_nf_command_reform_1` | `navy_org` +2%, `naval_coordination` +3% (giữ) | **+15 command power (mới)**; mở D-C (giữ) | 5,0 |
| T6 | `VIE_nf_first_force` | — | XP 10 (giữ); **+10 command power (mới)**; mở D-D (giữ) | 0 |
| T7 | `VIE_nf_command_reform_2` | `navy_org` +2%, `naval_coordination` +3% (giữ); **theo hướng D-D (mới)**: Coastal `naval_hit_chance` +1,5% · Balanced `navy_org` +0,5% và hit +0,5% và speed +0,5% · Extended `naval_speed` +1,5% · chưa chọn: không thêm | **XP 10 (mới)** | 5,0 + 1,1–1,8 |
| T8 | `VIE_nf_medium_force` | `navy_max_range` +3% (giữ); `naval_speed` +1% (mới) | **XP 10 (mới)**; mở P1/P2/P3 (giữ tooltip) | 2,5 |
| T9 | `VIE_nf_operating_range` | `navy_max_range` +5%, `naval_detection` +5% (giữ) | **XP 15, +15 command power (mới)** | 7,0 |

T7 đọc `VIE_nf_force_priority` (đặt ngay lúc chọn ở `vie_nav_force.30`, không đợi 12 tháng của D-D) nên hoạt động đúng cả khi người chơi bấm D-D xong mới làm T7. Giá trị "chưa chọn" = 0 → không thưởng, không phạt.

**Giảm cost theo hướng D-D** (áp trong `VIE_nf_d4_finish`, mẫu `VIE_lf_fav_discount`): Coastal → `VIE_nf_denial` −14 ngày; Extended Range → `VIE_nf_greenwater` và `VIE_nf_bluewater` mỗi cái −14 ngày; Balanced → không giảm. Chỉ áp khi focus tương ứng chưa hoàn thành. Giữ thưởng +1% org khi đúng nhánh (L8) và phạt timed idea khi lệch nhánh (L6) như code hiện tại.

## 2.2 Nhánh Maritime Denial (lịch sử, 4 node, tổng 22,9 điểm)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---|
| D1 | `VIE_nf_denial` | `naval_strike_attack` +3% (giữ); `naval_hit_chance` +2% (mới) | XP 15 (mới); khớp/lệch nhánh (giữ) | `navy_max_range` −2% (mới) | 4,2 |
| D2 | `VIE_nf_denial_defence` | `mines_planting_by_fleets` +10%, `naval_mines_effect_reduction` +5% (giữ); `naval_hit_chance` +1% (mới) | XP 10 (mới); **tech bonus 0,25 `CAT_as_missiles` ×1 lượt (mới)**; mở Bastion-P2 (giữ) | — | 5,7 |
| D3 | `VIE_nf_denial_subs` | `navy_submarine_attack` +3% (giữ); `navy_submarine_defence` +2% (mới) | XP 10 (mới); **tech bonus 0,25 `CAT_sub`+`CAT_atk_sub` (mới)**; mở P4 (giữ) | — | 5,0 |
| D4 | `VIE_nf_denial_command` (capstone) | `navy_org` +3%, `naval_detection` +4% (giữ); `naval_hit_chance` +1,5% (mới, thay cho strike +2% vì strike đã sát trần) | **XP 25, +50 PP (mới)** | — | 8,0 |

## 2.3 Nhánh Greenwater (5 node, tổng 27,0 điểm)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---|
| G1 | `VIE_nf_greenwater` | `navy_max_range` +5% (giữ); `naval_speed` +2% (mới) | XP 15 (mới); khớp/lệch nhánh (giữ) | `navy_personnel_cost` +2% (mới) | 2,4 |
| G2 | `VIE_nf_regional_frigates` | `navy_max_range` +3%, `navy_org` +2% (giữ); `navy_anti_air_attack` +2% (mới) | XP 10 (mới); **tech bonus 0,25 `CAT_frigate` (mới)**; mở P4 (giữ) | — | 5,4 |
| G3 | `VIE_nf_amphibious_fleet` | `naval_invasion_planning_bonus_speed` +10%, `naval_invasion_capacity` +1 (giữ); `naval_speed` +1% (mới) | **+10 command power (mới)** | — | 6,7 |
| G4 | `VIE_nf_lhd_program` | `naval_invasion_capacity` +1 (giữ); `navy_anti_air_attack` +2% (mới) | XP 15 (mới); mở P7 (giữ) | — | 4,6 |
| G5 | `VIE_nf_regional_command` (capstone) | `navy_org` +3%, `naval_coordination` +3% (giữ); `naval_hit_chance` +1%, `naval_speed` +1% (mới) | **XP 25, +50 PP (mới)** | — | 7,9 |

## 2.4 Nhánh Bluewater (5 node, tổng 30,8 điểm; B5 cho thêm khi có tàu sân bay)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---|
| B1 | `VIE_nf_bluewater` | `navy_max_range` +5% (giữ); `naval_speed` +2%, `navy_capital_ship_defence` +2% (mới) | XP 15 (mới); khớp/lệch nhánh (giữ) | `navy_personnel_cost` +3% (mới) | 3,0 |
| B2 | `VIE_nf_ocean_escort` | `navy_anti_air_attack` +5% (giữ); `navy_submarine_defence` +1% (mới) | XP 10 (mới); **tech bonus 0,25 `CAT_destroyer` (mới)**; mở khu trục (giữ) | — | 5,0 |
| B3 | `VIE_nf_replenishment` | `navy_max_range` +3% (giữ); `navy_org` +2% (mới); `navy_personnel_cost` −1% (mới, hậu cần tốt hơn giảm duy trì) | XP 10 (mới) | — | 4,8 |
| B4 | `VIE_nf_naval_aviation` | `navy_anti_air_attack` +3%, `naval_detection` +4% (giữ); `naval_hit_chance` +1% (mới) | XP 15 (mới); mở tàu sân bay (giữ) | — | 6,8 |
| B5 | `VIE_nf_carrier_group` (capstone) | `navy_org` +3%, `naval_coordination` +5% (giữ); `navy_capital_ship_attack` +2%, `navy_capital_ship_defence` +2% (mới) | **XP 25, +50 PP (mới)**; mở SSN (giữ). D-E `VIE_nf_d5_finish` vẫn cộng thêm 0,25–0,5× org/coord (giữ) | — | 11,2 |

Vì sao tổng ba hướng lệch (22,9 / 27,0 / 30,8): Denial có 4 node và mua sắm rẻ nhất (8,85 tỷ), Greenwater 5 node (9,6 tỷ), Bluewater 5 node và đắt nhất (15,0 tỷ, từ `nf_balance.py` mục 4). Điểm bình quân mỗi focus 5,7 / 5,4 / 6,2 và Denial là hướng lịch sử nên không bị phạt thêm. Nếu muốn ngang nhau hơn, nâng D2 hoặc D3 thêm 1 điểm (xem Q2).

---

# PHẦN 3 — TRỤC 2 HẢI QUÂN: NỘI DUNG EFFECT TỪNG FOCUS (6 NODE)

Quy ước (giống `VIE_def_industry_law`): focus cho PP, XP và một khoản kinh nghiệm công nghiệp nhỏ; việc lớn (dockyard, MIO, tier, tech bonus lớn) vẫn thuộc Decision D1–D5. Exp cộng bằng `VIE_nav_add_*_exp` (đã có kẹp 0–100, riêng MRO kẹp 50 nếu phụ thuộc Nga). Cộng 3 điểm exp ở mỗi focus không làm đổi kết luận A3 của review Trục 2 (ngưỡng 30/15 đạt 80%); sẽ chạy lại `naval_balance.py`.

| Mã | Focus | Effect mới | Giữ nguyên |
|---|---|---|---|
| F1 | `VIE_naval_defence_law` (cost 5) | **+25 PP**; idea `VIE_nav_law_idea`: `industrial_capacity_dockyard` +3%, `experience_gain_navy` +1% | XP 15; tooltip category |
| F2 | `VIE_ba_son_shipyards` (cost 5) | **+15 PP**; `shipbuilding_exp` +3 | XP 10; unlock D1; event `vie_nav_ind.1` |
| F3 | `VIE_naval_mro` (cost 7) | **+10 PP**; `mro_exp` +3 | XP 10; unlock D2 |
| F4 | `VIE_small_combatant_construction` (cost 7) | `shipbuilding_exp` +3; `naval_speed` +2% (tàu tấn công nhanh) | XP 10; unlock D3 |
| F5 | `VIE_naval_systems_integration` (cost 7) | `integration_exp` +3; `naval_hit_chance` +1% (hệ thống điều khiển hỏa lực) | XP 15; unlock D4 |
| F6 | `VIE_naval_defence_2030` (capstone, cost mặc định 10) | **+50 PP**, `add_war_support` +3% | XP 25; unlock D5 |

Idea mới cho F1 nằm trong `common/ideas/VIE_md_ideas_nav_ind.txt` (cùng mẫu `VIE_nav_mature_industry_idea`). `industrial_capacity_dockyard` đã dùng ở 13 chỗ trong repo/MD nên token chắc chắn tồn tại.

---

# PHẦN 4 — DECISION HUẤN LUYỆN HẢI QUÂN (BỐN CÁI, LẶP LẠI ĐƯỢC)

Mẫu giống `VIE_dec_lf_*` (`VIE_md_decisions_lf.txt`): không `complete_effect`, thưởng ở `remove_effect` sau `days_remove`, `days_re_enable` làm cooldown, đặt trong category có sẵn `VIE_military_readiness_category`, `ai_will_do` base 15 với `factor 0` khi `VIE_def_ind_bankrupt = yes`. Timed idea là hiệu ứng tạm nên **không tính vào trần** (giống lục quân; tạm thời có thể vượt trần).

| Decision | Hiện khi | PP | Chạy | Cooldown | Thưởng | Ghi chú |
|---|---|---:|---:|---:|---|---|
| `VIE_dec_nf_train_asw` Huấn luyện chống ngầm | `has_completed_focus = VIE_nf_surface_force` và (`VIE_kilo_qty_delivered > 0` hoặc `VIE_nf_d2_done`) | 35 | 120 | 545 | +10 XP hải quân; `naval_detection` +5% trong 180 ngày | Đúng dòng 8.14 báo cáo lục quân, giao cho Hải quân |
| `VIE_dec_nf_train_firing` Diễn tập bắn đạn thật trên biển | `VIE_nf_surface_force` | 35 | 90 | 545 | +10 XP; `naval_hit_chance` +3% trong 180 ngày | Dùng modifier mới |
| `VIE_dec_nf_train_mines` Diễn tập thủy lôi và phòng thủ bờ | `VIE_nf_denial_defence` | 35 | 90 | 545 | +10 XP; `mines_planting_by_fleets` +10% trong 180 ngày | Chỉ nhánh Denial |
| `VIE_dec_nf_train_replenish` Diễn tập tiếp tế và hộ tống viễn dương | `VIE_nf_replenishment` | 40 | 120 | 545 | +10 XP; `navy_max_range` +5% trong 180 ngày | Chỉ nhánh Bluewater |

Cần 4 idea tạm `VIE_nf_idea_asw_drill`, `_firing_drill`, `_mines_drill`, `_replenish_drill` trong `VIE_md_ideas_nav_force.txt`.

---

# PHẦN 5 — MỐC LỊCH SỬ (BA EVENT, TÙY CHỌN)

Mẫu `VIE_lf_ms*_apply` + scheduler (không dùng `trigger_year_*` của MD). Không khóa ngày: nếu focus mục tiêu **chưa xong** → giảm cost 24 ngày; **đã xong** → thưởng nhỏ. Mỗi event còn cộng một modifier nhỏ cho mọi người chơi.

| Event | Ngày | Mốc | Focus mục tiêu | Cho mọi người chơi | Độ tin cậy ngày |
|---|---|---|---|---|---|
| `vie_nav_force.70` | 2016-03 | Khai trương Cảng quốc tế Cam Ranh | `VIE_nf_operating_range` (T9) | `navy_org` +1% | Cao (8/3/2016, đã xác minh) |
| `vie_nav_force.71` | 2018-03 | Tàu sân bay Hoa Kỳ thăm Đà Nẵng (5–9/3/2018) | không (chỉ thưởng) | +10 XP, +10 command power | Cao |
| `vie_nav_force.72` | 2023-07 | Ấn Độ trao tặng một hộ vệ hạm tên lửa cho Hải quân | `VIE_nf_ocean_escort` (B2) | `naval_hit_chance` +1% | Cao (INS Kirpan, 22/7/2023, đã xác minh) |

Event .70 và .72 là pop-up; .71 ẩn để không tăng số pop-up năm 2018 (cùng cách `vie_lf.4`). Dùng `VIE_popup_cd` giống lục quân, fallback im lặng sau 6 tháng, catch-up sau nội chiến chỉ đặt cờ. Nếu bạn chưa muốn thêm event, bỏ nguyên Phần 5; các phần còn lại không phụ thuộc nó.

Ứng viên chưa đủ nguồn nên **không đưa vào**: thành lập Lữ đoàn Tàu ngầm 189 (báo cáo hải quân ghi 2013, bản gốc 2011, đã nằm trong danh sách cần xác minh ở review Trục 3, mục 5.1).

---

# PHẦN 6 — KIỂM SỐ LIỆU

Script scratch `nf_v2_check.py` (sẽ thành `tools/audit/nf_balance.py` mục 1 ở bước 0) duyệt 144 tổ hợp đường (3 nhánh × 2 mức D-A/D-B × chuyên môn × định hướng sâu × cơ cấu D-D × có hay không Luật Biển), cộng cả Trục 2, mốc Phần 5 và idea hiện có (`VIE_coast_guard_idea`, `VIE_cam_ranh_idea`: exp +5%). Trường hợp xấu nhất:

| Modifier | Xấu nhất | Trần | | Modifier | Xấu nhất | Trần |
|---|---:|---:|---|---|---:|---:|
| org | 18,0 | 18 | | strike | 9,5 | 10 |
| coordination | 19,5 | 20 | | subatk | 9,5 | 10 |
| detection | 14,5 | 15 | | subdef | 9,5 | 10 |
| range | 25,0 | 25 | | **hit chance (mới)** | 10,0 | 10 |
| experience gain | 10,0 | 10 | | **speed (mới)** | 8,5 | 10 |
| AA | 8,0 | 12 | | capital atk / def (mới) | 3,0 / 5,0 | 8 / 8 |
| chi phí nhân sự | +5,0 | +6 | | | | |

Tất cả PASS. Hai chiều chạm trần đúng bằng (org 18,0 và hit 10,0) nên **mọi thay đổi sau này đều phải chạy lại script**; không thêm modifier cùng chiều vào mốc hoặc decision mà không giảm chỗ khác. Phần thưởng PP: tổng Trục 3 chỉ +25 (T1) +50 (capstone nhánh đã chọn) = +75 và Trục 2 +25 +15 +10 +50 = +100; so với lục quân (+25 N1, +50 `VIE_def_industry_law`, các focus Trục 2 khác) là cùng cỡ.

---

# PHẦN 7 — PLAN CODE (9 BƯỚC, MỖI BƯỚC MỘT COMMIT, NHÁNH `naval-effects-v2`)

Bước 0–3 đủ để người chơi thấy khác biệt; bước 4–6 là phần tùy chọn thêm; bước 7–8 hoàn thiện.

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt` (+3 dòng, ngoài khối `GEN:vars`); `localisation/english/replace/VIE_md_vi_tt_l_english.yml` (+`VIE_tt_naval_hit_chance`); `tools/audit/nf_balance.py` (thay hằng số bằng bảng ở Phần 2–5, thêm chiều mới) | Thêm 3 biến `VIE_af_*` và loc; cập nhật script cân bằng | `nf_balance.py` PASS; console `effect add_to_variable = { VIE_af_naval_hit_chance = 0.01 }` thấy dòng trong tooltip `VIE_armed_forces_modifier` |
| **1** | `common/scripted_effects/VIE_md_effects_nav_force.txt` | `VIE_nf_refresh`, 22 effect `VIE_nf_<mã>_reward` (T1…T9, D1…D4, G1…G5, B1…B5), `VIE_nf_fav_discount`, `VIE_nf_t7_dir` | brace; `live.py` không báo effect thiếu |
| **2** | `common/national_focus/VIE_md_focus.txt` | 22 focus Trục 3: thay `completion_reward` bằng `log` + `VIE_nf_<mã>_reward = yes`; giữ nguyên prerequisite, `available`, `ai_will_do`, tọa độ; sửa comment header dòng 2991 | `audit.py` 0 dangling/cycle/trùng tọa độ; so diff: không đổi dòng nào ngoài `completion_reward` |
| **3** | `VIE_md_effects_nav_ind.txt`, `VIE_md_ideas_nav_ind.txt`, `VIE_md_focus.txt` (6 focus Trục 2) | 6 effect `VIE_nav_f<n>_reward`, idea `VIE_nav_law_idea`; focus gọi effect | `naval_balance.py` PASS (ngưỡng exp 30/15 vẫn ≥ 75% tổ hợp đạt) |
| **4** | `VIE_nf_d4_finish` (nav_force effects), `VIE_md_ideas_nav_force.txt` | Gọi `VIE_nf_fav_discount` ở cuối D-D; kiểm đơn vị `reduce_focus_completion_cost` (ngày) cùng mục checklist lục quân | chơi: chọn Coastal ở D-D thì `VIE_nf_denial` rẻ hơn 14 ngày so với `VIE_nf_greenwater` |
| **5** | `common/decisions/VIE_md_decisions_nf_drills.txt`, `VIE_md_ideas_nav_force.txt` (+4 idea tạm) | 4 decision huấn luyện (Phần 4) | `live.py`: 0 decision/idea treo; chơi: cooldown 545 ngày, timed idea 180 ngày hiện đúng |
| **6** | `events/VIE_nav_force.txt` (+`.70 .71 .72`), `VIE_md_effects_nav_force.txt` (`VIE_nf_ms1..3_apply`, `VIE_event_scheduler_nf`), `common/on_actions/VIE_md_on_actions.txt` (+1 dòng), `VIE_md_effects_p3.txt` (catch-up) | Mốc lịch sử; dùng `VIE_popup_cd` và fallback 6 tháng | `ev.py` sạch; `debug` đặt ngày 2016-03 thấy event; catch-up không bắn event |
| **7** | `localisation/english/VIE_md_events_nav_force_l_english.yml` (BOM, `:0`), `VIE_md_events_naval_l_english.yml` nếu cần | Loc: 4 decision, 4+1 idea, 3 event (title/desc/option), tech bonus name (`VIE_nf_tb_*`), cập nhật mô tả focus ngắn gọn khi effect đổi | `verify_all_loc.py` sạch |
| **8** | `ai_will_do`, `tools/TESTING.md`, `VIE_v9_flag_mapping.md` | Rà `ai_will_do`: capstone base 60 và guard phá sản như hiện có, thêm vào TESTING mục "Naval effects v2" | `ev.py`, `audit.py`, `live.py`, `nf_balance.py`, `naval_balance.py` đều sạch |

Mẫu code cho bước 1 (theo `VIE_lf_fm1_reward` và `VIE_lf_cr2_reward`):

```
VIE_nf_refresh = { force_update_dynamic_modifier = yes }

VIE_nf_d1_reward = {
	add_to_variable = { VIE_af_naval_strike_attack_factor = 0.03 tooltip = VIE_tt_naval_strike_attack_factor }
	add_to_variable = { VIE_af_naval_hit_chance = 0.02 tooltip = VIE_tt_naval_hit_chance }
	add_to_variable = { VIE_af_navy_max_range_factor = -0.02 tooltip = VIE_tt_navy_max_range_factor }
	VIE_nf_xp_15 = yes
	# khop/lech nhanh: giu nguyen khoi if/else_if theo VIE_nf_force_priority hien co
	VIE_nf_refresh = yes
}

VIE_nf_t7_reward = {
	add_to_variable = { VIE_af_navy_org_factor = 0.02 tooltip = VIE_tt_navy_org_factor }
	add_to_variable = { VIE_af_naval_coordination = 0.03 tooltip = VIE_tt_naval_coordination }
	if = { limit = { check_variable = { VIE_nf_force_priority = 1 } }
		add_to_variable = { VIE_af_naval_hit_chance = 0.015 tooltip = VIE_tt_naval_hit_chance } }
	else_if = { limit = { check_variable = { VIE_nf_force_priority = 3 } }
		add_to_variable = { VIE_af_naval_speed_factor = 0.015 tooltip = VIE_tt_naval_speed_factor } }
	else_if = { limit = { check_variable = { VIE_nf_force_priority = 2 } }
		add_to_variable = { VIE_af_navy_org_factor = 0.005 tooltip = VIE_tt_navy_org_factor }
		add_to_variable = { VIE_af_naval_hit_chance = 0.005 tooltip = VIE_tt_naval_hit_chance }
		add_to_variable = { VIE_af_naval_speed_factor = 0.005 tooltip = VIE_tt_naval_speed_factor } }
	VIE_nf_xp_10 = yes
	VIE_nf_refresh = yes
}
```

Khối lượng ước tính: 28 effect (~330 dòng), 28 focus sửa `completion_reward` (không đổi cấu trúc), 4 decision (~100 dòng), 5 idea, 3 event + scheduler (~150 dòng), ~110 khóa loc, 1 script kiểm tra.

## Rủi ro và cách giảm

| Rủi ro | Giảm |
|---|---|
| `naval_hit_chance` hoặc `navy_capital_ship_*` bị engine từ chối khi là biến của dynamic modifier | Bước 0 kiểm bằng console ngay; nếu lỗi, đổi chiều này sang `naval_strike_attack` giảm bớt chỗ khác hoặc dùng idea tĩnh |
| `force_update_dynamic_modifier` cần hay không (comment p17 tự ghi "bỏ nếu tooltip tự cập nhật") | Test cùng lúc ở bước 0; chốt một hướng cho cả lục quân lẫn hải quân |
| Đơn vị `reduce_focus_completion_cost` (ngày hay tuần) | Đã có mục kiểm trong `tools/TESTING.md` cho lục quân; dùng chung kết quả, đừng test riêng |
| Tech bonus trùng `name` hoặc categories không tồn tại | Dùng đúng categories Trục 2 đã dùng (`CAT_sub`, `CAT_atk_sub`, `CAT_frigate`, `CAT_destroyer`, `CAT_as_missiles`); tên `VIE_nf_tb_*` duy nhất |
| Hai chiều chạm trần đúng bằng | `nf_balance.py` fail cứng khi vượt; đừng nâng trần để chữa |

---

# PHẦN 8 — CÂU HỎI CẦN CHỐT (mặc định đã gắn)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q1 | Giữ trần cũ, thêm 3 chiều mới thay vì nâng trần? | **Giữ trần, thêm chiều** | Nâng trần thì lệch với thang lục quân (25–26% mỗi chiều) |
| Q2 | Denial (22,9 điểm) thấp hơn Greenwater (27,0) và Bluewater (30,8)? | **Chấp nhận** vì rẻ nhất và là hướng lịch sử | Muốn ngang: D2 thêm `naval_hit_chance` +1% (hit đang 10,0/10 nên phải bớt ở nơi khác) |
| Q3 | Có làm Phần 5 (3 event mốc)? | **Có**, nhưng .70 và .72 cần xác minh ngày | Bỏ: bỏ bước 6, không ảnh hưởng bước khác |
| Q4 | Tech bonus ở D2, D3, G2, B2 (0,25 ×1 lượt)? | **Có** | Bỏ: bớt 4 dòng, điểm không đổi vì tech bonus không tính điểm |
| Q5 | Trục 2 hải quân cho PP và exp ở focus? | **Có** (Phần 3) | Bỏ: giữ XP + tooltip hiện tại |
| Q6 | Tướng/đô đốc hải quân? | **Ngoài phạm vi**; lục quân và không quân đã có roster (`common/characters/`), hải quân chưa có file nào | Làm riêng một task "roster đô đốc" sau bước 8 |
