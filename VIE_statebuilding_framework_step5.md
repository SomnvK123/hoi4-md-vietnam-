# Bước 5: Khung xây dựng nhà nước bên trong "Đổi Mới tiếp tục"

> Tiếp theo STEP 1–2 (`VIE_regime_taxonomy_step1_2.md`), STEP 3 (`VIE_three_families_step3.md`), STEP 4 (`VIE_technocracy_capacity_step4.md`).
> **Chưa** vẽ transition graph cuối (STEP 6–8), **chưa** đề xuất sửa từng focus (STEP 9).
>
> Nhãn: **[SỰ KIỆN]** · **[HỌC THUẬT]** · **[TIỀN ĐỀ KỊCH BẢN]** · **[TRỪU TƯỢNG GAMEPLAY]**

---

## 0. Ràng buộc kỹ thuật đã kiểm chứng trước khi thiết kế

**[SỰ KIỆN]** Ba con số quyết định hình dạng của thiết kế này:

| Câu hỏi | Kết quả đo trong MD 1.19 | Hệ quả |
|---|---|---|
| Một nước được bao nhiêu power balance? | **Tối đa 3** (Ba Lan). Phần lớn có 1. **VIE đã có 3** rồi | **Không thêm thanh nào.** Bảy trục không thể là bảy thanh |
| Dynamic modifier có đắt không? | **Trung Quốc có 37**, cái lớn nhất đọc 42 biến | **Rẻ.** Đây là cơ chế mang chính |
| Submod đã dùng hệ luật của MD chưa? | **0 lần** trên 7 họ luật | Nối vào là gần như miễn phí |

**[TIỀN ĐỀ KỊCH BẢN] Quyết định kiến trúc:** khung xây dựng nhà nước chạy bằng **một dynamic modifier `VIE_state_modifier`** đọc khoảng 20 biến, **cộng** các họ luật sẵn có của MD, **cộng** internal factions. Không thêm power balance. Đây đúng mẫu `VIE_armed_forces_modifier` đã chạy được trong mod (61 biến, 1 modifier).

---

## 1. Nguyên tắc chọn trục

Một trục chỉ được vào khung nếu thỏa cả bốn:

1. **Có trong literature** như một chiều biến thiên thật của nhà nước, không phải một nhãn ý thức hệ
2. **Có đánh đổi được ghi nhận** — cả hai cực đều có cái giá, không có cực nào thuần lợi
3. **Độc lập với các trục khác** — không phải cách nói khác của một trục đã có
4. **Có cơ chế MD mang được**, hoặc chỉ cần một biến mới

Trục bị loại vì vi phạm nguyên tắc 3: "kỹ trị ↔ quan liêu" (đó là trục 2 nói cách khác), "phát triển ↔ phúc lợi" (đó là hệ quả ngân sách của trục 5), "dân tộc ↔ quốc tế" (đó là trục 7).

---

## 2. Bảy trục

### T1 — Quy mô bộ máy: tinh gọn ↔ mở rộng

| | |
|---|---|
| **Cơ sở** | Besley & Persson (2011): năng lực nhà nước là **khoản đầu tư** — tốn trước, sinh lợi sau |
| **Đánh đổi** | Bộ máy lớn: ra quyết định và thực thi nhanh hơn, nhưng **tốn ngân sách** và **chậm xây dựng**. Bộ máy nhỏ: rẻ, nhưng thiếu người thực thi |
| **Cơ chế mang** | **`bureau_law` 1–5 của MD, sẵn có.** VIE khởi đầu `bureau_03`. Ở mức 5: `political_power_gain = 1.0`, `production_speed_buildings_factor = -0.2` |
| **Cần thêm gì** | Không. Chỉ cần focus gọi đổi luật |
| **Việt Nam thật** | Cải cách 2024–2025 đẩy trục này về phía **tinh gọn**: 22 bộ → 17, bỏ 86% tổng cục, mục tiêu giảm 400.000 người |

### T2 — Chất lượng bộ máy: bảo trợ ↔ năng lực

| | |
|---|---|
| **Cơ sở** | Evans & Rauch (1999), *ASR* 64(5): thang **Weber hóa** = tuyển theo năng lực + lộ trình sự nghiệp dự đoán được, tương quan có ý nghĩa với tăng trưởng |
| **Đánh đổi** | **Geddes (1994), *Politician's Dilemma*:** cải cách công vụ **tước đi nguồn lực chính để mua liên minh** của người cầm quyền. Trọng dụng nhân tài làm tăng năng lực nhưng **giảm khả năng giữ đoàn kết nội bộ** |
| **Bằng chứng Việt Nam** | **[SỰ KIỆN]** Dù số tỉnh giảm 46%, ghế địa phương trong BCH TƯ chỉ giảm ~10% — Đảng chọn giữ cơ cấu bảo trợ. ISEAS 2025/14 nêu rủi ro "giữ người kém, mất người giỏi", dẫn tới "chính quyền do những người kém năng lực nhất điều hành" |
| **Cơ chế mang** | **Biến mới duy nhất của toàn khung:** `VIE_merit` (âm = bảo trợ, dương = năng lực). Đọc bởi `VIE_state_modifier` |
| **Vì sao phải mới** | `bureau_law` đo *nhiều hay ít*, `corruption_level` đo *hệ quả*. Không cái nào đo *cách tuyển người* |

### T3 — Tổ chức lãnh thổ: tập trung ↔ phân cấp

| | |
|---|---|
| **Cơ sở** | Treisman (2007), *The Architecture of Government*; Bardhan (2002), *Journal of Economic Perspectives* 16(4) |
| **Đánh đổi** | Phân cấp: chính sách **hợp với địa phương hơn**, nhưng **vấn đề phối hợp** và **nguy cơ bị nhóm lợi ích địa phương bắt cóc**. Tập trung: chính sách đồng nhất và nhanh, nhưng **mù thông tin địa phương** |
| **Bằng chứng Việt Nam** | **[SỰ KIỆN]** PCI và PAPI tồn tại được chính vì **63 tỉnh quản trị rất khác nhau** — biến thiên địa phương là sự thật đo được ở Việt Nam, không phải giả định |
| **Nghịch lý cần thể hiện** | Sáp nhập tỉnh và bỏ cấp huyện **vừa** phân cấp (cấp xã mạnh hơn) **vừa** tập trung (ít đầu mối tỉnh hơn). Đây là hai hiệu ứng ngược chiều trên cùng một cải cách, nên cho cả hai |
| **Cơ chế mang** | Biến `VIE_decentral` trong `VIE_state_modifier` |

### T4 — Quyền lực: hành pháp mạnh ↔ ràng buộc mạnh

| | |
|---|---|
| **Cơ sở** | O'Donnell (1998), "Horizontal Accountability in New Democracies"; Svolik (2012), *The Politics of Authoritarian Rule* về chia sẻ quyền lực trong chế độ độc đoán |
| **Đánh đổi** | **[SỰ KIỆN]** ISEAS 2026/29 phát biểu chính xác đánh đổi này về Việt Nam hiện nay: hệ thống yếu kiểm soát ngang "có thể đẩy nhanh sáng kiến từ trên xuống, nhưng khó xử lý đánh đổi, khó tiếp thu phản hồi và khó duy trì liên minh rộng", đồng thời **kém thích ứng với cú sốc bên ngoài** |
| **Nói gọn** | **Tốc độ chính sách đổi lấy khả năng sửa sai** |
| **Cơ chế mang** | Biến `VIE_checks`. **Không** dùng `VIE_party_balance` — thanh đó là Bảo thủ ↔ Cải cách, một chiều khác |
| **Lưu ý** | Theo Mann, đây là **quyền lực chuyên chế**, khác với T1+T2 là **quyền lực hạ tầng**. Hợp nhất TBT–Chủ tịch nước tăng cái này, không tăng cái kia |

### T5 — Kinh tế: nhà nước dẫn dắt ↔ thị trường dẫn dắt

| | |
|---|---|
| **Cơ sở** | Johnson (1982), Amsden (1989), Wade (1990); Kornai (1986), "The Soft Budget Constraint", *Kyklos* 39(1) |
| **Đánh đổi** | Nhà nước dẫn dắt: xây được ngành chiến lược mà thị trường không rót vốn, nhưng **ràng buộc ngân sách mềm** — doanh nghiệp nhà nước biết sẽ được cứu nên không kỷ luật. Thị trường dẫn dắt: hiệu quả, nhưng **đầu tư dưới mức** vào ngành chiến lược |
| **Cơ chế của Amsden phải có** | **Có đi có lại**: trợ cấp đổi lấy chỉ tiêu thành tích kiểm chứng được. Không đạt thì mất. Đây là thứ phân biệt chính sách công nghiệp thành công với bảo hộ thất bại |
| **Cơ chế mang** | Biến `VIE_state_econ` + luật kinh tế MD + `treasury` |
| **Việt Nam thật** | Vinashin 2010 là ca ràng buộc ngân sách mềm điển hình; Nghị quyết 68 (2025) đẩy về phía thị trường |

### T6 — An ninh: cưỡng chế ↔ quyền dân sự

| | |
|---|---|
| **Cơ sở** | Greitens (2016), *Dictators and their Secret Police* |
| **Đánh đổi (rất đặc thù, đáng làm)** | Bộ máy an ninh **chống đảo chính** được tối ưu bằng phân mảnh và chồng chéo — hiệu quả chống tinh hoa, **kém chống biểu tình quần chúng**. Bộ máy **chống nổi dậy** được tối ưu bằng tập trung và thâm nhập xã hội — hiệu quả chống quần chúng, **tạo ra một cơ quan đủ mạnh để tự đảo chính** |
| **Cơ chế mang** | **`police_law` 1–5 của MD, sẵn có** (VIE khởi đầu **police_05, cao nhất**) + `military_law` + biến `VIE_civil_liberties` |
| **Việt Nam thật** | **[SỰ KIỆN]** Bộ Công an ~8% BCH TƯ, quân đội ~18%, cộng 26%. Giải thể 705 công an cấp huyện là chuyển từ phân mảnh sang tập trung |

### T7 — Đối ngoại: hội nhập ↔ tự chủ

| | |
|---|---|
| **Cơ sở** | Kuik (2008), "The Essence of Hedging"; Levitsky & Way (2010) về **linkage** |
| **Đánh đổi kép** | Hedging **tốn ở cả hai đầu**: không được bảo đảm an ninh của liên minh, cũng không được ưu đãi của phụ thuộc. Hội nhập sâu: tăng trưởng và công nghệ, nhưng **linkage tạo áp lực thể chế** — Levitsky & Way cho thấy linkage dự báo dân chủ hóa mạnh hơn sức ép |
| **Phân biệt phải có trong game** | **Linkage ≠ alignment.** FTA, du học, kiều hối, chuỗi cung ứng → đẩy về phía dân chủ hóa. Hiệp ước quân sự → **không** |
| **Cơ chế mang** | Biến `VIE_integration` + ý tưởng Ba/Bốn Không sẵn có + cặp loại trừ `VIE_accept_chinese_influence` ↔ `VIE_pivot_to_the_west` đã có |

---

## 3. Ba đại lượng phái sinh — người chơi không chọn trực tiếp

**[TIỀN ĐỀ KỊCH BẢN]** Đây là chỗ khung này khác một bảng thanh trượt: ba thứ sau **được tính ra** từ bảy trục, và chúng là thứ quyết định nhánh chế độ nào mở.

### P1 — Tự chủ gắn kết (Evans)

```
VIE_embedded_autonomy = f( T2 chất lượng bộ máy , faction doanh nghiệp , corruption_level )
```

| Tự chủ | Gắn kết | Kết quả | Dải trong mod |
|---|---|---|---|
| Cao | Cao | **Nhà nước kiến tạo** | `developmental_state` |
| Cao | Thấp | Nhà nước xa rời, chính sách sai thông tin | — |
| Thấp | Cao | **Bị bắt cóc → tài phiệt** | `ol_*` |
| Thấp | Thấp | Nhà nước ăn cướp | Collapse |

**[HỌC THUẬT]** Đây là kết luận quan trọng nhất của STEP 4 thành cơ chế: **tài phiệt không phải một chế độ tách rời, nó là nhà nước kiến tạo mất tự chủ.**

### P2 — Huy động quần chúng

```
VIE_mobilization = f( T4 ràng buộc , T6 quyền dân sự , căng thẳng Biển Đông , tính chính danh )
```

**[HỌC THUẬT]** Đây là biến **phân biệt Family A với Family B** theo Linz: chế độ độc đoán giải huy động, chế độ hướng phát xít huy động. Mod hiện **chỉ có nó bên trong chế độ Dân túy** qua `VIE_populist_balance`. Nó phải tồn tại ở mọi chế độ, nếu không cửa Lạc Hồng không có cơ sở.

### P3 — Cấu trúc tinh hoa → internal factions

**[SỰ KIỆN]** MD có **23 faction**, VIE dùng **3**. Cấu trúc tinh hoa không nên là một thanh, nó nên **hiện ra** dưới dạng faction được thêm vào khi cấu hình đạt ngưỡng:

| Cấu hình | Faction MD được thêm |
|---|---|
| T5 lệch thị trường + T2 thấp + tham nhũng cao | `oligarchs` |
| T6 lệch cưỡng chế | `intelligence_community` |
| T6 lệch cưỡng chế qua ngả quân đội | `the_military` |
| T5 lệch thị trường + T7 hội nhập | `small_medium_business_owners` |
| T4 mở ràng buộc + T5 lệch nhà nước | `labour_unions` |
| T5 vô địch quốc gia kiểu Đông Á | `chaebols` |
| Công nghiệp quốc phòng sâu | `defense_industry` |

**[HỌC THUẬT]** Đúng với Winters (2011): đầu sỏ là **kết quả của động lực bảo vệ của cải**, không phải một chính sách được chọn.

---

## 4. Cơ chế: ba tầng, không có hệ thống mới

| Tầng | Nội dung | Có sẵn? |
|---|---|---|
| **Luật MD** | `bureau_law` (T1), `police_law` + `military_law` (T6), `tax_rate` (ngân sách), `education_law`/`health_law`/`social_law` (khế ước xã hội) | **Có, chưa dùng** |
| **Dynamic modifier** | `VIE_state_modifier` đọc ~20 biến `VIE_st_*`, đúng mẫu `VIE_armed_forces_modifier` | Mẫu **đã chạy** trong mod |
| **Internal faction** | 7 faction mới thêm theo ngưỡng cấu hình | **Có trong MD, chưa dùng** |

**Không thêm:** power balance mới (MD tối đa 3, VIE đã có 3), GUI mới, hệ tham nhũng riêng, cây focus thứ hai.

**[TRỪU TƯỢNG GAMEPLAY]** Bảy trục hiển thị cho người chơi dưới dạng **một mục trong danh sách modifier quốc gia**, giống hệt cách "Quân đội Nhân dân Việt Nam" hiện ra bây giờ. Mỗi trục là một dòng, giá trị đổi khi hoàn thành focus.

---

## 5. Đổi Mới là xương sống: focus lịch sử đẩy trục

**[TIỀN ĐỀ KỊCH BẢN] Đây là điểm mấu chốt của toàn thiết kế.** Không thêm 50 focus "xây dựng nhà nước" mới. Thay vào đó, **195 focus lịch sử sẵn có trở thành cơ chế xây dựng nhà nước.**

Ví dụ, dùng ID đã code:

| Focus đã có | T1 quy mô | T2 năng lực | T3 phân cấp | T4 ràng buộc | T5 kinh tế | T6 an ninh | T7 đối ngoại |
|---|---|---|---|---|---|---|---|
| `VIE_public_admin_reform` | − | **+** | | | | | |
| `VIE_decentralization` | | | **+** | + | | | |
| `VIE_two_tier_local_gov` | **−** | | **+ và −** | | | | |
| `VIE_merge_ministries` | **−** | | − | − | | | |
| `VIE_e_government` | − | **+** | | + | | | |
| `VIE_asset_declaration` | | **+** | | + | | | |
| `VIE_national_assembly_role` | | | | **+** | | | |
| `VIE_rule_of_law_state` | | + | | **+** | | | |
| `VIE_equitization_soes` | | | | | **+ thị trường** | | |
| `VIE_state_conglomerates` | | | | | **+ nhà nước** | | |
| `VIE_private_sector_engine` | | | | | **+ thị trường** | | |
| `VIE_cybersecurity_law` | | | | − | | **+ cưỡng chế** | |
| `VIE_force_47` | | | | − | | **+ cưỡng chế** | |
| `VIE_press_relaxation` | | | | + | | **+ dân sự** | |
| `VIE_wto_negotiations` | | | | | + thị trường | | **+ hội nhập** |
| `VIE_cptpp_member`, `VIE_evfta` | | | | | | | **+ hội nhập** |
| `VIE_self_reliance` | | | | | + nhà nước | | **+ tự chủ** |
| `VIE_tc_import_substitution` | | | | | + nhà nước | | **+ tự chủ** |

**Hệ quả:** người chơi **không bấm một nút "chọn mô hình nhà nước"**. Họ chơi lịch sử, và đến năm 2015 nhìn lại thì thấy mình đã xây ra một nhà nước cụ thể. Đó là điều bạn mô tả ở mục VII.

**[SỰ KIỆN]** Việc này cũng vá khiếm khuyết lớn nhất của cây: hiện **92% focus thân lịch sử không có đánh đổi nào**. Gắn trục vào chúng là cách rẻ nhất để sửa.

---

## 6. Cấu hình → mô hình nhà nước

**[TIỀN ĐỀ KỊCH BẢN]** Bảy trục không sinh ra 2⁷ kịch bản. Literature chỉ công nhận một số **cấu hình ổn định**, và chỉ những cấu hình đó có tên:

| Mô hình | T1 | T2 | T3 | T4 | T5 | T6 | T7 | Dải trong mod |
|---|---|---|---|---|---|---|---|---|
| **Nhà nước kiến tạo** | vừa | **cao** | tập trung | thấp | nhà nước | vừa | hội nhập | `developmental_state` |
| **Kiến tạo dân chủ** | vừa | **cao** | vừa | **cao** | vừa | dân sự | hội nhập | `dm_*` sau kiến tạo |
| **Nhà nước an ninh** | lớn | thấp | tập trung | **rất thấp** | nhà nước | **cưỡng chế** | tự chủ | `sec_*` |
| **Tài phiệt** | nhỏ | **rất thấp** | phân cấp | thấp | thị trường | vừa | hội nhập | `ol_*` |
| **Độc tài phát triển** | vừa | cao | tập trung | **rất thấp** | nhà nước | cưỡng chế | **hội nhập, ngả Tây** | `wa_*` |
| **Chiến tranh nhân dân** | vừa | vừa | **phân cấp** | vừa | nhà nước | **huy động** | **tự chủ** | `tc_*` + `path_peoples_war` |
| **Dân túy** | lớn | thấp | tập trung | rất thấp | nhà nước | **huy động** | tự chủ | `np_*` |

**[HỌC THUẬT]** Cột T2 là cột phân biệt rõ nhất: kiến tạo và tài phiệt khác nhau **chủ yếu ở chất lượng bộ máy**, không ở ý thức hệ. Đó là luận điểm Evans, và nó thành một con số trong game.

---

## 7. Điều kiện mở nhánh: từ cờ sang cấu hình

**[SỰ KIỆN]** Hiện nay nhánh mở bằng cờ do event đặt: `VIE_developmental_unlocked`, `VIE_tc_unlocked`, `VIE_oligarch_unlocked`…

**[TIỀN ĐỀ KỊCH BẢN]** Đề xuất: **giữ cờ làm điều kiện cần, thêm cấu hình làm điều kiện đủ.** Cửa event vẫn mở cơ hội; nhưng đi được hay không phụ thuộc vào nhà nước bạn đã xây.

| Nhánh | Điều kiện hiện tại | Điều kiện đề xuất thêm | Cơ sở |
|---|---|---|---|
| `developmental_state` | `VIE_bop_is_reformist` | T2 trên ngưỡng **+ đe dọa bên ngoài + khan hiếm nguồn lực** | Doner, Ritchie & Slater (2005): kiến tạo **bị ép ra đời** |
| `ol_*` Tài phiệt | cờ từ khủng hoảng ngân hàng | T2 **dưới** ngưỡng + tham nhũng cao + faction `oligarchs` đã có | Evans: mất tự chủ |
| `sec_*` An ninh | cờ từ khủng hoảng | T6 lệch cưỡng chế + T4 rất thấp | Greitens |
| `np_*` Dân túy | cờ từ HD-981 | **P2 huy động** trên ngưỡng | Mudde |
| `lh_*` Lạc Hồng | đang ở Dân túy | **thêm hai** trong: khủng hoảng chính danh, tinh hoa ly khai, rạn độc quyền bạo lực | Paxton giai đoạn 3, Mann |
| `managed_pluralism` → Dân chủ | `VIE_press_relaxation` | **T2 cao + tăng trưởng tốt** = nhượng bộ từ thế mạnh | Slater & Wong (2013) |
| Dân chủ qua Collapse | stability sụp | không cần cấu hình, nhưng **hệ quả xấu hơn** | O'Donnell & Schmitter: replacement bất ổn hơn transformation |

**[HỌC THUẬT]** Dòng áp chót và dòng cuối là chỗ quan trọng nhất: **hai lối vào dân chủ phải có hệ quả khác nhau.** Hiện mod có cả hai nhưng đối xử như nhau.

---

## 8. Ngân sách công việc

| Việc | Khối lượng | Ghi chú |
|---|---|---|
| `VIE_state_modifier` + ~20 biến | 1 file mới | Đúng mẫu `VIE_md_dynamic_modifiers.txt` đã có |
| Loc cho các biến | ~20 khóa | Mẫu `VIE_tt_*` đã có |
| Gắn trục vào focus lịch sử | **~120 trên 195 focus** | Script, đúng cách đã làm với 34 focus BoP |
| Nối `bureau_law` / `police_law` | ~12 focus | Cần thử `swap_ideas` với luật MD trước |
| Thêm faction theo ngưỡng | 7 faction, qua scheduler | Cần kiểm giới hạn số faction của MD |
| Ba đại lượng phái sinh | scripted effect tính lại hằng tháng | Scheduler đã có |
| Đổi điều kiện mở nhánh | ~16 gốc dải | Thêm `available`, không xóa cờ |
| Kiểm tra tĩnh | mở rộng `check_static.py` | Mọi biến `VIE_st_*` phải có trong modifier và có loc |

**Không đụng tới:** 487 ID focus, cấu trúc `VIE_md_focus`, dải chế độ, nhánh quân sự.

---

## 9. Những gì khung này cố ý KHÔNG làm

1. **Không thêm power balance.** MD tối đa 3, VIE đã dùng hết.
2. **Không biến trục thành ý thức hệ.** Không có "chế độ kỹ trị", "chế độ phân cấp".
3. **Không gắn cứng quân sự vào chế độ.** Theo yêu cầu mục XIII của bạn: một nhà nước dân chủ vẫn chọn được phòng thủ lãnh thổ, một nhà nước dân tộc chủ nghĩa vẫn chọn được từ chối biển. Nhánh quân sự nối vào **T3 (phân cấp → dân quân), T5 (nhà nước → công nghiệp quốc phòng), T7 (tự chủ → nội địa hóa)**, không nối vào chế độ.
4. **Không thêm focus mới cho phần lõi.** Focus lịch sử sẵn có làm nhiệm vụ này.
5. **Không xóa focus nào** vì phân loại thay đổi.
6. **Không cho trục nào chỉ toàn lợi.** Nếu một trục không tìm được cái giá trong literature thì loại trục đó.

---

## 10. Khoảng trống cần kiểm chứng trước khi code

1. **Đổi luật MD bằng focus có sạch không.** `bureau_01…05` có `available` gắn với `budget_law_parliament_change_allowed` và `bureau_decrease_blocked`. Phải thử `swap_ideas` trong `completion_reward` xem có bị chặn không, hay phải dùng effect riêng của MD.
2. **Giới hạn số internal faction cùng lúc** của MD — chưa biết. Quyết định P3 phụ thuộc vào con số này.
3. **Ngưỡng cho từng trục.** Hiện tôi mới có hướng, chưa có số. Nên lấy mốc từ PAPI 2011 và 2024 cho T2, PCI cho T3.
4. **`corruption_level` đã tác động lên PP và ngân sách như thế nào** — phải biết để T2 không cộng dồn hai lần.
5. **Quan hệ dân sự – quân sự Việt Nam** — vẫn nợ từ STEP 3, cần cho T6.
6. **Hiển thị.** 20 dòng trong một modifier có quá dài không — cần xem trong game. Nếu dài, gộp thành 7 dòng tóm tắt bằng `custom_modifier_tooltip`.

---

## Nguồn mới dùng ở bước này

Besley & Persson (2011) *Pillars of Prosperity*; Evans & Rauch (1999) *ASR* 64(5); **Geddes (1994) *Politician's Dilemma: Building State Capacity in Latin America***; Treisman (2007) *The Architecture of Government*; Bardhan (2002) *JEP* 16(4); O'Donnell (1998) *Journal of Democracy* 9(3); Svolik (2012) *The Politics of Authoritarian Rule*; **Kornai (1986) "The Soft Budget Constraint", *Kyklos* 39(1)**; Greitens (2016) *Dictators and their Secret Police*; Kuik (2008) *Contemporary Southeast Asia* 30(2); Levitsky & Way (2010) *Competitive Authoritarianism*; Evans (1995) *Embedded Autonomy*; Winters (2011) *Oligarchy*; Doner, Ritchie & Slater (2005) *International Organization* 59(2); Slater & Wong (2013) *Perspectives on Politics* 11(3); Mann (1984) *EJS* 25(2).

Dữ liệu Việt Nam: [ISEAS Perspective 2025/14](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-14-vietnams-bureaucratic-reforms-opportunities-and-challenges-in-the-era-of-national-rise-by-nguyen-khac-giang/) · [ISEAS Perspective 2026/29](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2026-29-vietnams-reconfigured-leadership-personnel-and-power-in-the-new-era-by-nguyen-khac-giang/) · [PAPI](https://papi.org.vn/eng/) · [PCI/PAPI – Malesky, Duke](https://sites.duke.edu/malesky/governance-indices/).

Cơ chế MD đọc trực tiếp: `common/bop/*.txt` (tối đa 3/nước), `common/dynamic_modifiers/99_CHI_*.txt` (37 modifier), `common/ideas/AA_law_budget.txt`, `common/ideas/AA_law_internal_factions.txt` (23 faction).
