# Bước 1–2: Audit baseline + Taxonomy chế độ / xây dựng nhà nước

> Phạm vi: STEP 1 (audit 3 tài liệu + code thật) và STEP 2 (taxonomy). **Chưa** nghiên cứu sâu 3 family A/B/C, **chưa** đề xuất sửa focus.
> Mọi con số đều đo bằng script trên `D:\HOI4Mods\md_vietnam` ngày 2026-09-20, không phải ước lượng từ tài liệu.
>
> Nhãn dùng trong báo cáo: **[SỰ KIỆN]** = đo được trong code/file game · **[HỌC THUẬT]** = diễn giải từ literature · **[TIỀN ĐỀ KỊCH BẢN]** = giả định thiết kế · **[TRỪU TƯỢNG HÓA GAMEPLAY]** = đơn giản hóa vì cơ chế game.

---

# PHẦN I — STEP 1: AUDIT

## 1.1 Hiện trạng thật của cây (SỰ KIỆN)

| Khối | Hàng | Focus |
|---|---|---|
| Thân lịch sử (chính trị, kinh tế, xã hội, KHCN, ngoại giao) | 0–9 | **195** |
| Quốc phòng | 10–26 | **133** |
| Dải chế độ giả định | 28–37 | **159** |
| **Tổng** | | **487** |

Dải chế độ gồm **19 thành phần liên thông** (component), **20 sự kiện `vie_alt`**, **20 idea riêng**, **3 power balance**.

## 1.2 Tài liệu so với code: khớp đến mức nào

**Khớp gần như tuyệt đối về số lượng.** Đối chiếu từng dải H4/H5 của `implementation_plan_v6` với code:

| Dải (plan v6) | Plan | Code | |
|---|---|---|---|
| H4.1 Cộng sản Tự chủ `tc` | 15 | 15 | ✅ |
| H4.2 Dân túy Biển Đông `np` | 14 | 14 | ✅ |
| H4.3 Đặc khu Tự do `lb` | 13 | 13 | ✅ |
| H4.4 Tài phiệt `ol` | 12 | 12 | ✅ |
| H4.5 Hội đồng Phát triển `wa` | 15 | 15 | ✅ |
| H5.1 Nhà nước An ninh `sec` | 8 | 8 | ✅ |
| H5.2 Liên minh Xanh `gr` | 9 | 9 | ✅ |
| H5.3 Hội đồng Cứu quốc `jn` | 8 | 8 | ✅ |
| H5.4 Đoàn kết Quốc gia `ng` | 6 | 6 | ✅ |
| H5.5 Quân chủ `mn` | 10 | 10 | ✅ |
| H5.6 Dân chủ `dm` | 22 | 6 + 4×4 = 22 | ✅ |
| H5.7 Lạc Hồng `lh` | 3 | 3 | ✅ |
| H5.8 Liên minh Công nhân `wk` | 3 | 3 | ✅ |
| C6 Bảo thủ | 6 | 6 | ✅ |
| C5 Nhà nước kiến tạo + C7 Đa đảng có kiểm soát | 8 + 6 = 14 | **15** (một chuỗi duy nhất) | ⚠️ |

**Đồ thị chế độ H3 đã được code đúng như mô tả (SỰ KIỆN).** 8 "cửa" chạy bằng event đặt cờ `VIE_<x>_unlocked`; mọi chuyển chế độ đi qua `VIE_transition_regime`; Lạc Hồng **không vào trực tiếp được** — chỉ đến từ `vie_alt.15` lựa chọn b ("để phong trào cầm quyền") khi đang ở chế độ Dân túy, với `ai_chance = base 5`. Nguyên tắc "không có đường tắt tới chế độ cực đoan" đã thành code, không chỉ nằm trên giấy.

## 1.3 Bốn chỗ lệch giữa tài liệu và code

**(a) C5 và C7 đã dính làm một.** Plan v6 mô tả *Nhà nước kiến tạo* (C5, 8 focus) và *Đa đảng có kiểm soát* (C7, 6 focus) là hai nhánh riêng **trong cây chính**. Trong code chúng là **một chuỗi liên thông 15 focus nằm trong dải chế độ** (hàng 28+), gốc `VIE_developmental_state`, và chứa cả `VIE_environmental_accountability`. Nghĩa là: kiến tạo → kỹ trị → tư pháp → nới báo chí → Mặt trận → bầu cử hiệp thương → đa nguyên có quản lý đã là **một con đường liên tục**, không phải hai nhánh song song.

**(b) Ba power balance chưa code.** Plan v6 §A6 liệt kê 6 thanh; code chỉ có 3: `VIE_party_balance`, `VIE_populist_balance`, `VIE_oligarch_balance`. Thiếu: Cộng sản Tự chủ, Đặc khu Tự do, Hội đồng Phát triển.

**(c) Internal faction: kế hoạch có, code không.** Plan v6 §A5 nói `oligarchs` thêm khi vào Tài phiệt, `the_military` khi vào Junta, `labour_unions` khi vào Tự chủ/Dân chủ. **Số lần xuất hiện trong code: 0.** VIE vẫn chỉ dùng 3 faction khởi đầu của MD. Trong khi đó MD có sẵn **23 faction** (`common/ideas/AA_law_internal_factions.txt`): `oligarchs`, `the_military`, `intelligence_community`, `labour_unions`, `chaebols`, `defense_industry`, `small_medium_business_owners`, `international_bankers`, `landowners`, `the_clergy`… (SỰ KIỆN)

**(d) Không có đại lượng nào biểu diễn "năng lực nhà nước".** Cây có tham nhũng (MD), có thanh Bảo thủ↔Cải cách, có opinion 3 faction — nhưng **không có** biến, idea hay dynamic modifier nào theo dõi năng lực hành chính / chất lượng bộ máy. Đây chính là Layer 2 mà bạn muốn.

## 1.4 Phát hiện quan trọng nhất của audit: cây gần như không có đánh đổi

| Đo | Kết quả |
|---|---|
| Focus thân lịch sử | 195 |
| … có `mutually_exclusive` | **6** (3%) |
| … có bất kỳ hiệu ứng âm nào | **16** (8%) |
| Focus dải chế độ | 159 |
| … có `mutually_exclusive` | **3** (2%) |

**(SỰ KIỆN)** 92% focus thân lịch sử là thuần lợi ích, không mất gì, không loại trừ gì. Sáu focus loại trừ lẫn nhau là: điện hạt nhân xây/gác, pháp lý biển vs. khẳng định chủ quyền, ngả Trung Quốc vs. ngả phương Tây.

Đây là lý do cây hiện tại **không** cho người chơi cảm giác "xây dựng nhà nước". Người chơi không chọn kiểu nhà nước; họ lấy hết mọi thứ theo thứ tự tùy ý, rồi đến một điểm nào đó bấm một focus và **nhảy** sang một chế độ khác. Không có bước trung gian nào giữa "làm tất cả" và "đổi chế độ".

## 1.5 Trùng lặp nội dung giữa các dải (SỰ KIỆN)

Cùng một ý tưởng được viết lại ở 3–4 chỗ dưới ID khác nhau:

| Ý tưởng | Xuất hiện ở |
|---|---|
| Chính sách công nghiệp kiểu Đông Á | `wa_five_year_plans`, `wa_national_champions`, `wa_heavy_industry`, `wa_export_drive` · `developmental_state`, `singapore_model` · thân chính `VIE_private_champions`, `VIE_manufacturing_hub`, `VIE_export_powerhouse` |
| Kỹ trị / trọng dụng nhân tài | `technocrat_cabinet`, `meritocratic_service` · `ng_technocratic_caretaker` · thân chính `VIE_public_admin_reform`, `VIE_e_government`, `VIE_streamline_apparatus` |
| Chủ nghĩa dân tộc kinh tế | `tc_import_substitution`, `tc_decouple_supply`, `tc_rare_earth_leverage` · `np_national_goods`, `np_nationalist_economy` · `VIE_state_sector_leading`, `VIE_self_reliance` |
| Cải cách tư pháp / pháp quyền | `judicial_reform` · thân chính `VIE_rule_of_law_state`, `VIE_constitution_2013` |
| Tự quản của người lao động | `tc_self_management`, `tc_workers_councils` · dải `wk_workers_commune` |
| Kiểm soát lao động ↔ quyền lao động | `wa_suppress_labor` · `dm_soc_labor_rights` · thân chính `VIE_labor_code_2019` |

**Kết luận audit:** vấn đề không phải "quá nhiều chế độ". Vấn đề là **các chiều xây dựng nhà nước bị chẻ nhỏ và nhân bản vào từng chế độ**, thay vì tồn tại một lần như lựa chọn chung.

---

# PHẦN II — STEP 2: TAXONOMY

## 2.1 Tiêu chí phân loại

Trong chính trị học so sánh, **regime** (chế độ) được định nghĩa bằng **luật chơi quyết định ai nắm quyền hành pháp và quyền đó được tranh giành như thế nào** — không phải bằng nội dung chính sách.

- Linz & Stepan (1996), *Problems of Democratic Transition and Consolidation* — phân biệt regime theo đa nguyên, ý thức hệ, huy động, lãnh đạo. **[HỌC THUẬT]**
- Geddes, Wright & Frantz (2014), "Autocratic Breakdown and Regime Transitions", *Perspectives on Politics* 12(2) — chế độ độc đoán chỉ có **4 loại**: đảng trị, quân sự, cá nhân trị, quân chủ. Phân loại dựa trên **ai kiểm soát việc tuyển chọn lãnh đạo**. **[HỌC THUẬT]**
- Levitsky & Way (2010), *Competitive Authoritarianism* — bầu cử có cạnh tranh nhưng sân chơi nghiêng: một loại lai, không phải dân chủ cũng không phải độc tài khép kín. **[HỌC THUẬT]**
- Fukuyama (2013), "What Is Governance?", *Governance* 26(3) — **năng lực nhà nước** và **trách nhiệm giải trình** là hai trục độc lập; một nhà nước có thể mạnh và độc đoán, mạnh và dân chủ, yếu và dân chủ, yếu và độc đoán. **[HỌC THUẬT]**
- Hanson & Sigman (2021), "Leviathan's Latent Dimensions", *Journal of Politics* 83(4) — năng lực nhà nước gồm **3 chiều đo được**: thu ngân sách, cưỡng chế, hành chính. **[HỌC THUẬT]**

**Phép thử suy ra:** một nhánh là *regime* khi nó **đổi cách chọn người nắm quyền**. Nếu nó chỉ đổi *nhà nước làm gì* hoặc *nhà nước làm như thế nào*, nó không phải regime.

## 2.2 Phép thử tương đương có sẵn trong code (SỰ KIỆN)

Cây này đã có sẵn một phép thử khách quan: **nhánh có gọi `VIE_transition_regime` (đổi `ruling_party`) hay không.**

| Nhóm | Dải | Slot MD |
|---|---|---|
| **Đổi slot bằng focus** (10) | `defend_the_foundation` 4 · `wa_development_council` 0 · `np_street_mandate` 20 · `national_salvation_council` 22 · `sec_cyber_control` 7 · `lb_sez_law` 16 · `ol_bailout` 15 · `ng_technocratic_caretaker` 13 · `gr_green_coalition` 17 · `wk_workers_commune` 5 | 10 slot |
| **Đổi slot bằng event** (3) | Dân chủ (1/2/14/18, qua bầu cử `vie_alt`) · Quân chủ (23, qua `vie_col.7`) · Lạc Hồng (21, qua `vie_alt.15.b`) | 7 slot |
| **KHÔNG BAO GIỜ đổi slot** (3) | `developmental_state` (15) · `tc_strategic_autonomy` (15) · `round_table_talks` (6) | vẫn 19 |

**Ba dải cuối cùng — 36 focus, chiếm 23% toàn bộ nội dung giả định — không phải là chế độ.** Code đã nói điều đó từ đầu; tài liệu chỉ chưa gọi đúng tên.

## 2.3 Bảng phân loại đầy đủ

| Nhánh hiện có | Loại thực sự | Family | Cơ sở | Nên giữ? |
|---|---|---|---|---|
| **Nhà nước kiến tạo** `developmental_state` | **Mô hình quản trị + năng lực nhà nước** — không phải regime | Trong Đổi Mới | Johnson (1982), Evans (1995) "embedded autonomy", Wade (1990). Evans chứng minh nhà nước kiến tạo tồn tại ở cả Nhật (dân chủ), Hàn (độc tài rồi dân chủ), Đài Loan → **không gắn với regime nào** **[HỌC THUẬT]** | Giữ, nhưng chuyển thành lựa chọn xây dựng nhà nước |
| **Kỹ trị** `technocrat_cabinet`, `meritocratic_service` | **Phong cách cầm quyền + cách tuyển chọn tinh hoa** — không phải regime | Xuyên family | Centeno (1993) "The New Leviathan": kỹ trị là hiện tượng **hành chính–tinh hoa**, xuất hiện trong mọi loại chế độ. Bickerton & Accetti (2021) *Technopopulism* **[HỌC THUẬT]** | Giữ, đưa thành trục "bộ máy" dùng chung |
| **Bảo thủ** `defend_the_foundation` | **Phái trong nội bộ chế độ đảng trị** (đổi slot 19→4 nhưng vẫn là đảng trị) | Trong Đổi Mới | Geddes et al.: đổi phái trong đảng **không** đổi loại chế độ **[HỌC THUẬT]** | Giữ như cấu hình, không phải "chế độ khác" |
| **Đa đảng có kiểm soát** `front_coalition → managed_pluralism` | **Chế độ lai** (competitive authoritarianism) | C — tiền dân chủ | Levitsky & Way (2010) **[HỌC THUẬT]** | Giữ — đây là bước trung gian có thật |
| **Dân chủ** `round_table_talks` + 4 gói đảng | `round_table_talks` = **cơ chế chuyển đổi**; 4 gói `dm_*` = **họ đảng cầm quyền**, không phải 4 chế độ | **C** | O'Donnell & Schmitter (1986) *Transitions from Authoritarian Rule* — đàm phán bàn tròn là cơ chế, không phải chế độ **[HỌC THUẬT]** | Giữ; nhưng gọi đúng: 1 chế độ, 4 chính phủ |
| **Tự chủ** `tc_strategic_autonomy` | **Định hướng đối ngoại + mô hình kinh tế**, không đổi chế độ | **B** | Kuik (2008) "The Essence of Hedging"; Le Hong Hiep (2013); Vuving (2006) — tự chủ chiến lược là **chính sách**, không phải thể chế **[HỌC THUẬT]** | Giữ, nhưng tách: đối ngoại ≠ tự quản xí nghiệp |
| **Dân túy** `np_street_mandate` | **Ý thức hệ mỏng + phương thức huy động**, đã được cấp slot riêng | **B → A** | Mudde (2004) "The Populist Zeitgeist": dân túy là "thin-centred ideology" bám vào ý thức hệ chủ. Levitsky & Loxton (2013): dân túy là **con đường** dẫn tới độc đoán cạnh tranh **[HỌC THUẬT]** | Giữ — là bản lề giữa B và A |
| **Lạc Hồng** `lh_*` | **Điểm thoái hóa** (degeneration endpoint) | **A** | Paxton (2004) *Anatomy of Fascism*: phát xít là **quá trình 5 giai đoạn**, cần hội tụ điều kiện, không phải lựa chọn trên thực đơn. Griffin (1991); Mann (2004) **[HỌC THUẬT]** | Giữ nguyên thiết kế hiện tại — đã đúng |
| **Junta** `national_salvation_council` | **Regime thật** (military regime) | A/B tùy hướng đi | Geddes et al.: quân sự là 1 trong 4 loại độc đoán **[HỌC THUẬT]** | Giữ |
| **Nhà nước An ninh** `sec_cyber_control` | **Regime thật** (cá nhân trị/đảng trị dựa trên bộ máy cưỡng chế) nhưng nội dung phân biệt là **thiết kế bộ máy an ninh** | A | Greitens (2016) *Dictators and their Secret Police*: cấu trúc cưỡng chế biến thiên **bên trong** cùng một loại chế độ **[HỌC THUẬT]** | Giữ regime, nhưng nội dung nên dùng chung |
| **Tài phiệt** `ol_bailout` | **Cấu trúc tinh hoa** (state capture), không phải loại chế độ | Xuyên family | Winters (2011) *Oligarchy*: đầu sỏ là **chiến lược bảo vệ của cải**, tồn tại cả trong dân chủ ("civil oligarchy") **[HỌC THUẬT]** | Giữ (MD có slot), nhưng cũng nên là **trạng thái** đo được ở mọi chế độ |
| **Đặc khu Tự do** `lb_sez_law` | **Mô hình kinh tế + cấu hình lãnh thổ**, được nâng lên thành chế độ | Xuyên family | Không có "chế độ libertarian" trong literature so sánh; đặc khu là công cụ chính sách (Farole & Akinci 2011, World Bank) **[HỌC THUẬT]** | Giữ vì MD có slot, nhưng bản chất là đường dẫn tới Tài phiệt |
| **Hội đồng Phát triển** `wa_*` | **Regime thật** (độc tài phát triển) **+** mô hình kinh tế trùng với Nhà nước kiến tạo | A/B | Mô hình Park Chung-hee; Amsden (1989); Woo-Cumings (1999) **[HỌC THUẬT]** | Giữ regime; **gộp phần kinh tế** với nhánh kiến tạo |
| **Xanh** `gr_green_coalition` | **Họ đảng / định hướng chính sách**, không phải loại chế độ | Xuyên family | Đảng Xanh cầm quyền là thay đổi **chính phủ**, không phải **chế độ** **[HỌC THUẬT]** | Hạ xuống thành gói chính sách hoặc gói đảng trong C |
| **Quân chủ** `mn_*` | **Regime thật** (monarchy) | Ngoại lệ hậu sụp đổ | Geddes et al. **[HỌC THUẬT]**. Tiền lệ Campuchia 1993 là **[TƯƠNG TỰ LỊCH SỬ]**, không phải dự báo | Giữ như kết cục hiếm |
| **Đoàn kết Quốc gia** `ng_technocratic_caretaker` | **Cơ chế chuyển tiếp** (caretaker government), không phải chế độ đích | Trung gian | Chính phủ lâm thời kỹ trị là hiện tượng chuyển tiếp **[HỌC THUẬT]** | Giữ, nhưng gắn thời hạn |
| **Liên minh Công nhân** `wk_workers_commune` | **Kết cục nội chiến** | Ngoại lệ | — | Giữ 3 focus |

## 2.4 TRẢ LỜI CÂU HỎI CHÍNH

### Có bao nhiêu "loại tương lai" thật sự?

**Code hiện có 19 dải và 16 party slot. Về mặt chính trị học, đó là 6 loại tương lai, không phải 16.**

| # | Loại tương lai | Slot | Dải hiện có | Vì sao là một loại |
|---|---|---|---|---|
| 1 | **Đảng–nhà nước tiếp tục** | 19, 4 | ĐCSVN gốc · Bảo thủ · Tự chủ · Nhà nước kiến tạo · Đa đảng có kiểm soát | Cùng một chế độ đảng trị; khác nhau ở **cấu hình nhà nước**, không ở cách chọn lãnh đạo (Geddes et al.) |
| 2 | **Độc đoán không do Đảng lãnh đạo** | 22, 7, 0, 13 | Junta · An ninh · Hội đồng Phát triển · Đoàn kết Quốc gia | Khác nhau ở **ai là người bảo trợ** (quân đội / công an / liên minh phát triển / kỹ trị lâm thời) |
| 3 | **Nhà nước bị vốn chiếm giữ** | 15, 16 | Tài phiệt · Đặc khu Tự do | Winters: cùng một hiện tượng bảo vệ của cải, hai lối vào |
| 4 | **Dân chủ bầu cử** | 1, 2, 14, 18 | Bàn tròn → 4 gói đảng | Một chế độ, bốn chính phủ |
| 5 | **Dân túy → cực hữu** | 20 → 21 | Dân túy Biển Đông → Lạc Hồng | Một quỹ đạo hai giai đoạn (Mudde → Paxton) |
| 6 | **Ngoại lệ hậu khủng hoảng** | 23, 5, 17 | Quân chủ · Công xã Công nhân · Xanh | Kết cục hiếm, không phải con đường chính |

### Nhánh nào thực chất chỉ là cách xây dựng nhà nước?

**Bằng chứng trong code: ba dải không bao giờ đổi `ruling_party` (36 focus, 23% nội dung giả định).**

| Dải | Focus | Thực chất là |
|---|---|---|
| `developmental_state` (gồm cả C7) | 15 | **Mô hình quản trị** (kiến tạo) + **năng lực bộ máy** (kỹ trị, công vụ, tư pháp) + **mức độ tham gia chính trị** (báo chí, Mặt trận, bầu cử hiệp thương) |
| `tc_strategic_autonomy` | 15 | **Định hướng đối ngoại** (không liên kết, Nam bán cầu, ASEAN) + **mô hình kinh tế** (thay thế nhập khẩu, tự quản) |
| `round_table_talks` | 6 | **Cơ chế chuyển đổi**, không phải đích đến |

**Và bên trong các dải *là* chế độ, vẫn còn nội dung không phải chế độ:**

- `wa_five_year_plans`, `wa_national_champions`, `wa_heavy_industry`, `wa_export_drive`, `wa_technical_education` → **mô hình kinh tế kiến tạo**, trùng với nhánh Nhà nước kiến tạo
- `np_national_goods`, `np_nationalist_economy`, `np_boycott` → **chủ nghĩa dân tộc kinh tế**, trùng với `tc_import_substitution`
- `sec_*` phần lớn → **thiết kế bộ máy an ninh**, có thể dùng ở nhiều chế độ
- `ol_land_bank`, `ol_private_security`, `ol_offshore_wealth` → **mức độ nhà nước bị chiếm giữ**, nên là thang đo chứ không phải focus riêng của một chế độ

**Ước tính: khoảng 55–65 trong 159 focus giả định (35–40%) không phải nội dung chế độ, mà là lựa chọn xây dựng nhà nước đang bị nhân bản.**

## 2.5 Kiến trúc phân lớp: đánh giá đề xuất 6 lớp của bạn

| Lớp bạn đề xuất | Đánh giá | Cơ sở |
|---|---|---|
| L1 Political regime | **Giữ** | Geddes et al. (2014); Linz & Stepan (1996) |
| L2 State capacity | **Giữ, nhưng tách 3 chiều** thay vì thang 4 nấc: hành chính · thu ngân sách · cưỡng chế | Hanson & Sigman (2021) |
| L3 Economic model | **Giữ** | Hall & Soskice (2001); Musacchio & Lazzarini (2014) *Reinventing State Capitalism* |
| L4 Political institutions | **Gộp một phần vào L1, phần còn lại đổi tên thành "ràng buộc hành pháp / trách nhiệm giải trình ngang"** | O'Donnell (1998) "Horizontal Accountability"; trùng lặp với L1 nếu để nguyên |
| L5 Foreign-policy orientation | **Giữ** | Kuik (2008); Goh (2005); Le Hong Hiep (2013) |
| L6 Social model | **Giữ, nhưng dùng khung Đông Á** chứ không phải Esping-Andersen | Holliday (2000) "Productivist Welfare Capitalism", *Political Studies* 48(4) |

**Kết luận: 5 lớp, không phải 6.** L4 hiện tại vừa lặp L1 vừa lặp L2. Đề xuất:

1. **Chế độ** — ai chọn người cầm quyền
2. **Năng lực nhà nước** — hành chính / ngân sách / cưỡng chế
3. **Ràng buộc quyền lực** — tư pháp, Quốc hội, báo chí, phân cấp
4. **Mô hình kinh tế** — nhà nước ↔ thị trường, DNNN ↔ tư nhân, mở ↔ tự chủ
5. **Định hướng đối ngoại** — tự chủ / cân bằng / nghiêng bên nào

Lớp "mô hình xã hội" nhập vào lớp 4 (nó là hệ quả phân phối của mô hình kinh tế), trừ khi STEP 5 chứng minh nó cần đứng riêng.

**Vị trí của kỹ trị và nhà nước kiến tạo trong khung này (HỌC THUẬT):**
- **Kỹ trị** = giá trị cao ở lớp 2 (năng lực hành chính) **cộng** giá trị thấp ở lớp 3 (ít ràng buộc bầu cử). Nó **không có ô riêng ở lớp 1**. → không phải regime.
- **Nhà nước kiến tạo** = lớp 2 cao + lớp 4 "nhà nước dẫn dắt". Xuất hiện được ở lớp 1 bất kỳ: Nhật dân chủ, Hàn trước 1987 độc tài, Hàn sau 1987 dân chủ. → không phải regime.

## 2.6 Điều này có nghĩa gì cho STEP 5 (khung xây dựng nhà nước)

**(TIỀN ĐỀ KỊCH BẢN)** Nếu 5 lớp trên đúng, thì các trục lựa chọn có cơ sở học thuật là:

| Trục | Hai cực | Đánh đổi có trong literature |
|---|---|---|
| Tập trung ↔ phân cấp | Trung ương quyết ↔ tỉnh quyết | Treisman (2007) *The Architecture of Government*: phân cấp tăng đáp ứng nhưng gây vấn đề phối hợp và có thể tăng tham nhũng địa phương |
| Bộ máy theo thâm niên ↔ theo năng lực | Bổ nhiệm chính trị ↔ thi tuyển | Evans & Rauch (1999), *ASR*: tuyển theo năng lực tương quan với tăng trưởng; nhưng làm giảm công cụ bảo trợ chính trị |
| DNNN dẫn dắt ↔ tư nhân dẫn dắt | Tập đoàn nhà nước ↔ cạnh tranh | Musacchio & Lazzarini (2014): state capitalism có lợi khi thị trường vốn yếu, hại khi đã trưởng thành |
| Hành pháp mạnh ↔ ràng buộc mạnh | Quyết nhanh ↔ kiểm soát | O'Donnell (1998); tốc độ chính sách đổi lấy sai lầm không sửa được |
| Kiểm soát tham gia ↔ mở tham gia | Hiệp thương ↔ cạnh tranh | Levitsky & Way (2010): mở một phần tạo bất ổn ngắn hạn, chính danh dài hạn |
| An ninh trước ↔ quyền dân sự trước | Bộ máy cưỡng chế ↔ tự do | Greitens (2016): bộ máy an ninh mạnh chống đảo chính nhưng kém chống biểu tình và ngược lại |
| Hội nhập sâu ↔ tự chủ | Chuỗi cung ứng toàn cầu ↔ nội địa hóa | Kuik (2008): hedging có chi phí cơ hội hai đầu |

**Bảy trục này, không phải 20.** Mỗi trục có đánh đổi được ghi nhận trong literature, chứ không phải bịa ra vì gameplay.

---

# PHẦN III — VIỆC CẦN LÀM Ở CÁC BƯỚC SAU

| Bước | Nội dung | Ghi chú |
|---|---|---|
| STEP 3 | Nghiên cứu sâu 3 family A / B / C: tiền đề, kích hoạt, phản ứng của tinh hoa, phản hồi thể chế, phụ thuộc đường đi, khả năng thất bại | Chưa làm |
| STEP 4 | Kỹ trị / nhà nước kiến tạo / năng lực nhà nước — đã có kết luận sơ bộ ở §2.3, cần kiểm chứng thêm bằng literature về Việt Nam (Gainsborough 2010; London 2014; Malesky) | Một phần |
| STEP 5 | Thiết kế 7 trục xây dựng nhà nước thành cơ chế | Chưa làm |
| STEP 6–7 | Mapping vào Đổi Mới và vào 19 dải hiện có | Chưa làm |
| STEP 8–9 | Transition graph + kế hoạch code | Chưa làm |

## Khoảng trống cần kiểm chứng

1. **Số lượng internal faction tối đa của MD** — chưa rõ MD có giới hạn bao nhiêu faction cùng lúc cho một nước. Cần thử trước khi thiết kế "elite structure" dựa trên faction.
2. **Chi phí giao diện của power balance** — nếu 7 trục biến thành 7 thanh thì vượt xa những gì MD làm cho bất kỳ nước nào. Cần khảo sát nước có nhiều BoP nhất trong MD.
3. **Literature riêng về Việt Nam** cho phần "năng lực nhà nước" — tôi mới dùng lý thuyết chung; cần đối chiếu với nghiên cứu về cải cách hành chính Việt Nam (PAR Master Programme 2001–2010, 2011–2020) và PCI/PAPI.
4. **Tính khả thi của kịch bản cực hữu ở Việt Nam** — báo cáo này **chưa** đánh giá. Đó là việc của STEP 3, và phải đánh giá trung lập theo literature, không mặc định là có hoặc không.
