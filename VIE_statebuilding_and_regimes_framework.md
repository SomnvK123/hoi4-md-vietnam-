# Khung Xây dựng Nhà nước, Phân loại Chế độ và Lộ trình Chuyển đổi (Statebuilding & Regimes)

> **Tài liệu tổng hợp nghiên cứu & thiết kế (08/10/2026)**  
> Hợp nhất toàn bộ tiến trình nghiên cứu 9 bước thể chế, xây dựng nhà nước và các phương án thiết kế kiến trúc chính trị.

## Mục lục
1. [Bước 1–2: Audit baseline + Taxonomy chế độ / xây dựng nhà nước](#bước-12-audit-baseline--taxonomy-chế-độ--xây-dựng-nhà-nước)
2. [Bước 3: Nghiên cứu ba family giả định (A / B / C)](#bước-3-nghiên-cứu-ba-family-giả-định-a--b--c)
3. [Bước 4: Kỹ trị, nhà nước kiến tạo và năng lực nhà nước](#bước-4-kỹ-trị-nhà-nước-kiến-tạo-và-năng-lực-nhà-nước)
4. [Bước 5: Khung xây dựng nhà nước bên trong Đổi Mới tiếp tục](#bước-5-khung-xây-dựng-nhà-nước-bên-trong-đổi-mới-tiếp-tục)
5. [Bước 6: Ánh xạ khung xây dựng nhà nước vào Đổi Mới tiếp tục](#bước-6-ánh-xạ-khung-xây-dựng-nhà-nước-vào-đổi-mới-tiếp-tục)
6. [Bước 7: Ánh xạ khung vào toàn bộ nhánh hiện có](#bước-7-ánh-xạ-khung-vào-toàn-bộ-nhánh-hiện-có)
7. [Bước 8: Đồ thị chuyển chế độ với ngưỡng cụ thể](#bước-8-đồ-thị-chuyển-chế-độ-với-ngưỡng-cụ-thể)
8. [Bước 9: Kế hoạch thi công theo batch](#bước-9-kế-hoạch-thi-công-theo-batch)
9. [Phụ lục I: Thiết kế Statebuilding v1](#phụ-lục-i-thiết-kế-statebuilding-v1)
10. [Phụ lục II: Thiết kế Statebuilding 4 trục](#phụ-lục-ii-thiết-kế-statebuilding-4-trục)

---
## Bước 1–2: Audit baseline + Taxonomy chế độ / xây dựng nhà nước

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

---

## Bước 3: Nghiên cứu ba family giả định (A / B / C)

# Bước 3: Nghiên cứu ba family giả định (A / B / C)

> Tiếp theo `VIE_regime_taxonomy_step1_2.md`. **Chưa** thiết kế khung xây dựng nhà nước (STEP 5), **chưa** đề xuất sửa focus.
>
> Nhãn: **[SỰ KIỆN]** đo được hoặc có nguồn sơ cấp · **[HỌC THUẬT]** diễn giải từ literature · **[TƯƠNG TỰ LỊCH SỬ]** so sánh, không phải dự báo · **[TIỀN ĐỀ KỊCH BẢN]** giả định thiết kế · **[TRỪU TƯỢNG GAMEPLAY]** đơn giản hóa vì cơ chế game.

---

## 0. Điểm xuất phát: chế độ Việt Nam hiện nay là gì

Cả ba family đều rẽ ra **từ cùng một điểm**. Phải mô tả điểm đó chính xác trước, nếu không mọi đánh giá khả năng đều vô nghĩa.

**[SỰ KIỆN]**

| Chỉ số | Giá trị | Nguồn |
|---|---|---|
| Phân loại V-Dem | **Closed autocracy** — không có bầu cử cạnh tranh cho hành pháp | V-Dem Democracy Report 2025 |
| Phân loại Geddes/Wright/Frantz | **Party regime** (đảng trị) | GWF 2014 |
| Đại hội XIV (1/2026) | Tô Lâm nhiệm kỳ 5 năm, **hợp nhất Tổng Bí thư và Chủ tịch nước** — lần đầu sau thống nhất | ISEAS Perspective 2026/29 |
| Bộ Công an trong BCH TƯ | ~14 ghế (~8%) | ISEAS 2026/29 |
| Quân đội trong BCH TƯ | ~32 ghế (~18%) | ISEAS 2026/29 |
| An ninh + quân đội cộng lại | **26%** — ngang các đại hội trước, nhưng nắm nhiều vị trí trọng yếu hơn | ISEAS 2026/29 |
| BCH TƯ / Bộ Chính trị | 180 / 19 — **không đổi quy mô** | ISEAS 2026/29 |
| Tỷ lệ miền Bắc trong BCH TƯ | **73%**, tăng từ 66%; riêng Hưng Yên 20 người | ISEAS 2026/29 |
| Kỹ trị trong Bộ Chính trị | 3 người, có Lê Minh Hưng làm Thủ tướng | ISEAS 2026/29 |
| Tỉnh thành | 63 → **34** (6 thành phố + 28 tỉnh) | Nghị quyết 2025 |
| Chính quyền địa phương | **hai cấp**, bỏ cấp huyện, từ 1/7/2025 (NQ 203) | NQ 203/2025 |

**[HỌC THUẬT]** Ba điều quan trọng cho thiết kế:

1. **Hướng đi hiện tại là cá nhân hóa quyền lực *bên trong* chế độ đảng trị**, không phải đổi chế độ. Hợp nhất TBT–Chủ tịch nước đưa mô hình lãnh đạo từ "Tứ trụ" tập thể sang mô hình "hạt nhân" gần Trung Quốc hơn, nhưng các thiết chế tập thể chính thức vẫn còn. Theo GWF, đây là **personalization within a party regime** — một trạng thái, không phải một loại chế độ mới.
2. **Năng lực kỹ trị không bị loại bỏ.** Ba kỹ trị vào Bộ Chính trị, một người làm Thủ tướng. Đây là bằng chứng thực nghiệm cho kết luận STEP 2: kỹ trị là **cách vận hành**, không phải chế độ — nó tồn tại song song với cá nhân hóa.
3. **Cải cách hành chính không tự động tăng năng lực nhà nước.** Dù số đơn vị hành chính giảm 46%, số ghế BCH TƯ của địa phương chỉ giảm khoảng 10% — Đảng chọn giữ cơ cấu đại diện thay vì tinh gọn theo lãnh thổ. Rủi ro ISEAS nêu: hệ thống yếu kiểm soát ngang có thể **đẩy nhanh sáng kiến từ trên xuống nhưng kém trong xử lý đánh đổi, tiếp thu phản hồi và duy trì liên minh rộng**, và kém thích ứng với cú sốc bên ngoài.

**[TIỀN ĐỀ KỊCH BẢN]** Điểm số 3 là *cơ chế cốt lõi* mà cả ba family nên dùng chung: **tốc độ chính sách đổi lấy khả năng sửa sai**. Đó là một đánh đổi có nguồn, không phải bịa ra vì gameplay.

---

# FAMILY A — CỰC HỮU ĐỘC ĐOÁN

## A.1 Bảy khái niệm không được trộn lẫn

**[HỌC THUẬT]** Đây là phần bạn yêu cầu rõ nhất. Bảy khái niệm sau khác nhau ở **tiêu chí có thể kiểm chứng**, không phải ở mức độ "cực đoan".

| Khái niệm | Định nghĩa cốt lõi | Huy động quần chúng | Đảng dân quân | Bạo lực cứu chuộc | Cần dân chủ trước đó |
|---|---|---|---|---|---|
| **Chủ nghĩa dân tộc** | Đơn vị chính trị và đơn vị dân tộc nên trùng nhau (Gellner 1983) | Tùy | Không | Không | Không |
| **Chủ nghĩa dân tộc cực đoan** | Dân tộc là giá trị tối thượng, loại trừ, kèm cảm thức suy vong | Có | Không nhất thiết | Không nhất thiết | Không |
| **Dân tộc chủ nghĩa độc đoán** | Chế độ độc đoán dùng dân tộc làm nguồn chính danh | **Giải huy động** | Không | Không | Không |
| **Phát xít** | Paxton (2004) | **Có, bắt buộc** | **Có, bắt buộc** | **Có, bắt buộc** | **Thường có** |
| **Độc tài quân sự / junta** | Nhóm sĩ quan quyết định ai cầm quyền (GWF 2014) | **Giải huy động** | Không | Không | Không |
| **Độc đoán dân túy** | Mudde (2004) + Levitsky & Loxton (2013) | **Có** | Không | Không | **Có** (cần bầu cử để thắng) |
| **Cá nhân trị** | Lãnh tụ kiểm soát cả chính sách lẫn nhân sự và lực lượng an ninh (GWF) | Tùy | Không | Không | Không |

**Định nghĩa Paxton (2004), *The Anatomy of Fascism*** — vẫn là định nghĩa được trích dẫn nhiều nhất:

> một hình thức hành vi chính trị đặc trưng bởi nỗi ám ảnh về suy vong, sỉ nhục hoặc nạn nhân hóa của cộng đồng, và bởi các sùng bái bù đắp về thống nhất, sức mạnh và thuần khiết, trong đó **một đảng quần chúng gồm những chiến binh dân tộc chủ nghĩa**, hoạt động trong **sự hợp tác không dễ chịu nhưng hiệu quả với giới tinh hoa truyền thống**, **từ bỏ các quyền tự do dân chủ** và theo đuổi bằng **bạo lực cứu chuộc**, không bị ràng buộc bởi đạo đức hay pháp luật, các mục tiêu **thanh lọc bên trong và bành trướng bên ngoài**.

**[HỌC THUẬT] Điểm mấu chốt:** Paxton lập luận phát xít là **một quá trình năm giai đoạn**, không phải một học thuyết chọn được từ thực đơn:

1. hình thành phong trào
2. bén rễ trong hệ thống chính trị
3. **giành quyền lực** — chỉ xảy ra khi giới tinh hoa truyền thống mời phong trào vào để giải quyết bế tắc
4. thực thi quyền lực trong liên minh căng thẳng với nhà nước cũ
5. hoặc cấp tiến hóa, hoặc thoái hóa thành độc đoán thông thường

Griffin (1991) gọi hạt nhân thần thoại là **"chủ nghĩa dân tộc cực đoan tái sinh"** — ý niệm dân tộc chết đi rồi sống lại. Mann (2004), *Fascists*, bổ sung hai điều kiện tổ chức: **chủ nghĩa siêu việt dân tộc** và **bán quân sự hóa** — đảng phải có lực lượng vũ trang riêng ngoài nhà nước.

## A.2 Điều gì thực sự cần để một hệ thống đi tới đó

**[HỌC THUẬT]** Tổng hợp Paxton, Mann, Linz, Berman (1997), Riley (2010):

| Điều kiện | Nội dung | Vì sao cần |
|---|---|---|
| **Khủng hoảng chính danh** | Cơ sở chính danh cũ hết hiệu lực | Tạo chỗ trống cho nguồn chính danh mới |
| **Bế tắc thể chế** | Hệ thống hiện hành không ra được quyết định | Tinh hoa phải tìm lối ra ngoài hệ thống |
| **Huy động quần chúng ngoài nhà nước** | Có phong trào mà nhà nước không kiểm soát | Nguyên liệu cho đảng dân quân |
| **Cảm thức sỉ nhục dân tộc** | Mất đất, thua trận, bị áp đặt | Nội dung tình cảm của "tái sinh" |
| **Tinh hoa chịu bắt tay** | Một phần tinh hoa cũ mời phong trào vào | Paxton: **giai đoạn 3 không thể thiếu** |
| **Xã hội dân sự dày nhưng phân cực** | Berman (1997) về Weimar | Mạng lưới hội đoàn giúp phong trào lan nhanh |
| **Đổ vỡ độc quyền bạo lực** | Có lực lượng vũ trang ngoài nhà nước | Mann: bán quân sự là cấu thành |
| **Kinh tế khủng hoảng** | Thất nghiệp, lạm phát, phá sản tầng lớp trung lưu | Điều kiện thúc đẩy, **không phải điều kiện đủ** |

**[HỌC THUẬT]** Lưu ý mà literature nhấn mạnh và thiết kế game hay bỏ sót: **khủng hoảng kinh tế không đủ**. Nhiều nước khủng hoảng sâu hơn Đức và Ý mà không thành phát xít. Biến số phân biệt là **tinh hoa có mời phong trào vào hay không** (Paxton giai đoạn 3) và **phong trào có lực lượng vũ trang riêng hay không** (Mann).

## A.3 Đối chiếu với Việt Nam: cái gì có, cái gì không

**[SỰ KIỆN] + [HỌC THUẬT]** Đây là đánh giá trung lập theo tiêu chí ở A.2, không phải dự báo.

| Điều kiện | Việt Nam hiện nay | Đánh giá |
|---|---|---|
| Khủng hoảng chính danh | Chính danh dựa trên tăng trưởng và độc lập dân tộc; chưa sụp đổ | **Không có** |
| Bế tắc thể chế | Ngược lại: quyền lực đang tập trung hơn, ra quyết định nhanh hơn | **Không có** |
| Huy động quần chúng ngoài nhà nước | **Có tiền lệ thật:** 5/2014 khoảng 20.000 người ở Bình Dương, 15 nhà máy bị đốt, lan ra Hà Tĩnh và Đồng Nai; 6/2018 hàng chục nghìn người phản đối Luật Đặc khu | **Có, nhưng ngắn và bị dập** |
| Cảm thức sỉ nhục dân tộc | Hoàng Sa 1974, biên giới 1979, HD-981 2014, các vụ tàu cá | **Có, mạnh** |
| Tinh hoa chịu bắt tay | Không có dấu hiệu; Đảng xử lý biểu tình bằng **ngăn chặn**, không phải thu nạp | **Không có** |
| Xã hội dân sự dày | Hội đoàn quần chúng đều thuộc Mặt trận; xã hội dân sự độc lập nhỏ và bị hạn chế | **Không có** |
| Lực lượng vũ trang ngoài nhà nước | Dân quân tự vệ và Lực lượng 47 đều **nằm trong** bộ máy nhà nước và quân đội | **Không có** |
| Dân chủ thất bại trước đó | V-Dem: **closed autocracy** — không có bầu cử cạnh tranh để lật | **Không có** |

**[HỌC THUẬT] Một điểm ngược chiều quan trọng:** học giới cho rằng chủ nghĩa dân tộc chống Trung Quốc ở Việt Nam **không chủ yếu do Đảng tạo ra**. Nó là không gian hội tụ của bất mãn về lao động, môi trường và phát triển. Nhà nước cho phép biểu đạt khi phục vụ mục tiêu ngoại giao, rồi kiểm soát quỹ đạo của nó. Nghĩa là: **nguyên liệu huy động tồn tại thật và không thuộc về nhà nước** — đây là điều kiện duy nhất trong bảng trên mà Việt Nam có đầy đủ.

## A.4 Đánh giá khả năng: thấp, và chỉ qua một cửa duy nhất

**[HỌC THUẬT]** Theo tiêu chí Paxton–Mann, Việt Nam thiếu **năm trên tám** điều kiện, trong đó thiếu cả hai điều kiện mà literature coi là không thể thay thế (tinh hoa bắt tay, bán quân sự ngoài nhà nước).

**[TIỀN ĐỀ KỊCH BẢN]** Con đường duy nhất có cấu trúc hợp lý:

> Nhà nước **mất kiểm soát** đối với huy động dân tộc chủ nghĩa (điều kiện duy nhất đã có) → phong trào tự tổ chức và tồn tại quá một chu kỳ đàn áp → **một bộ phận tinh hoa** (an ninh, quân đội, hoặc một phái trong Đảng) chọn cưỡi lên phong trào thay vì dập nó → đảng dân quân hình thành từ các tổ chức quần chúng bị chiếm dụng.

Đây **đúng bằng** thiết kế đã code: Lạc Hồng chỉ tới từ `vie_alt.15` lựa chọn b khi đang ở chế độ Dân túy, `ai_chance = base 5`. **[SỰ KIỆN]** Thiết kế hiện tại không cần sửa về mặt cấu trúc.

**Điều cần bổ sung, không phải sửa:** hiện tại cửa này chỉ kiểm tra người chơi đang ở chế độ Dân túy. Theo literature nó nên kiểm tra thêm **ít nhất hai** trong các điều kiện: khủng hoảng chính danh đang hoạt động, một bộ phận tinh hoa đã ly khai, và độc quyền bạo lực đã rạn. Nếu không, nó vẫn là "bấm nút thành phát xít", chỉ là bấm muộn hơn một bước.

**Cần nói rõ:** đánh giá này là về **điều kiện cấu trúc**, không phải về "người Việt Nam có thể hay không thể". Điều kiện cấu trúc thay đổi được. Và literature cũng ghi nhận rất nhiều nước có đủ điều kiện mà vẫn không đi tới đó.

## A.5 Chu trình bảy bước (Family A)

| Bước | Nội dung |
|---|---|
| **1. Tiền đề** | Phong trào dân tộc chủ nghĩa tồn tại ngoài kiểm soát nhà nước + sỉ nhục dân tộc chưa được giải quyết + chính danh dựa trên tăng trưởng suy yếu |
| **2. Kích hoạt** | Một sự cố chủ quyền có thương vong, hoặc một cú sốc kinh tế trùng với một vụ nhượng bộ bị coi là bán nước |
| **3. Phản ứng tinh hoa** | Đảng chia rẽ: dập hay cưỡi. An ninh muốn dập (bảo vệ độc quyền bạo lực), một phái dân tộc chủ nghĩa muốn cưỡi (tìm chính danh mới) |
| **4. Đáp ứng thể chế** | Nếu cưỡi: tổ chức quần chúng bị chuyển công năng thành lực lượng phong trào; luật khẩn cấp; thanh trừng "kẻ thông đồng" |
| **5. Phản hồi** | Mỗi bước thanh trừng làm giảm số tinh hoa có thể quay lại, và tăng phụ thuộc của lãnh đạo vào đường phố |
| **6. Phụ thuộc đường đi** | Sau khi có lực lượng bán quân sự và thanh trừng, không quay lại được bằng thương lượng — chỉ bằng đảo chính hoặc sụp đổ |
| **7. Thất bại / đảo ngược** | Quân đội can thiệp (→ junta, đã code `vie_alt.15.a`); phong trào phân liệt; cô lập quốc tế làm kinh tế sụp; hoặc Paxton giai đoạn 5: **thoái hóa thành độc đoán thông thường** |

**[HỌC THUẬT]** Bước 7 dòng cuối là điều literature nhấn mạnh và game thường bỏ: kết cục **phổ biến nhất** của chế độ phát xít không phải chiến thắng hay sụp đổ hoành tráng, mà là **entropy** — mất năng lượng cách mạng và trở thành một chế độ độc đoán bảo thủ bình thường.

---

# FAMILY B — NHÀ NƯỚC DÂN TỘC CHỦ NGHĨA

## B.1 Các loại nationalism cần phân biệt

**[HỌC THUẬT]**

| Loại | Nội dung | Ví dụ trong literature |
|---|---|---|
| **Dân tộc công dân** | Thành viên dựa trên cư trú và luật pháp | Brubaker (1996) phê phán lưỡng phân công dân/sắc tộc là quá gọn, nhưng vẫn dùng được như hai cực |
| **Dân tộc sắc tộc** | Thành viên dựa trên nguồn gốc | Brubaker (1996) |
| **Dân tộc nhà nước** | Nhà nước chủ động xây dựng bản sắc quốc gia từ trên xuống | Singapore, Pháp thời Đệ tam Cộng hòa |
| **Dân tộc kinh tế** | Ưu tiên kiểm soát quốc gia với các nguồn lực kinh tế chiến lược | Helleiner (2002); Gerschenkron (1962) |
| **Phát triển chủ nghĩa dân tộc** | Công nghiệp hóa như dự án dân tộc | Johnson (1982); Amsden (1989); Woo-Cumings (1999) |
| **Tự chủ chiến lược** | Giữ quyền tự quyết đối ngoại, không liên minh cứng | Kuik (2008) về hedging; Le Hong Hiep (2013) về Việt Nam |
| **Dân tộc chủ nghĩa độc đoán** | Dân tộc là nguồn chính danh chính của một chế độ độc đoán | Linz (2000) |
| **Dân tộc chủ nghĩa dân túy** | Dân tộc + đối lập "nhân dân thuần khiết ↔ tinh hoa tha hóa" | Mudde (2004); Levitsky & Loxton (2013) |

## B.2 Câu hỏi then chốt: mạnh hơn mà không thành phát xít bằng cách nào

**[HỌC THUẬT]** Câu trả lời từ literature khá rõ ràng, vì các tiêu chí ở A.1 là tiêu chí **tổ chức**, không phải tiêu chí **cường độ**. Một nhà nước có thể tăng mạnh hàm lượng dân tộc chủ nghĩa mà vẫn không phải phát xít nếu giữ bốn điều:

1. **Không tạo tổ chức song song.** Nhà nước dân tộc chủ nghĩa dùng bộ máy hành chính pháp lý – thuần lý hiện có. Phát xít tạo đảng và dân quân **song song** với nhà nước rồi nuốt nó (Mann 2004).
2. **Giải huy động thay vì huy động.** Linz (2000) phân biệt chế độ độc đoán (huy động thấp, "mentalities" thay vì ý thức hệ) với chế độ toàn trị (huy động cao, ý thức hệ toàn diện). Giữ đường phố im lặng là **tiêu chí phân biệt**, không phải mức độ.
3. **Theo đuổi yêu sách bằng kênh pháp lý và ngoại giao.** Đưa ra tòa trọng tài, vận động COC, kiện cáo — khác về bản chất với "bành trướng bên ngoài" trong định nghĩa Paxton.
4. **Giữ tinh hoa kinh tế có phần trong ổn định.** Nếu thương mại và đầu tư vẫn mở, giới doanh nghiệp không có động cơ mời một phong trào cực đoan vào để bảo vệ tài sản (ngược với logic Paxton giai đoạn 3).

**[TƯƠNG TỰ LỊCH SỬ]** — so sánh, **không phải** dự báo cho Việt Nam: Pháp thời de Gaulle (tự chủ chiến lược, rút khỏi bộ chỉ huy hợp nhất NATO 1966, dân tộc kinh tế) và Ấn Độ thời Nehru–Indira (không liên kết, thay thế nhập khẩu) đều là nhà nước dân tộc chủ nghĩa mạnh mà không có bất kỳ đặc điểm tổ chức nào ở A.1.

## B.3 Thang nội bộ của Family B (bốn nấc, không phải bốn kịch bản)

**[TIỀN ĐỀ KỊCH BẢN]** Đây là **một spectrum**, không phải bốn chế độ:

| Nấc | Nội dung | Dải đã code | Đổi chế độ? |
|---|---|---|---|
| **B1 — Tự chủ chiến lược** | Nâng mức tự chủ đối ngoại và chuỗi cung ứng, vẫn hội nhập | `tc_strategic_autonomy` (15 focus) | **Không** — vẫn slot 19 |
| **B2 — Phát triển chủ nghĩa dân tộc** | Chính sách công nghiệp, vô địch quốc gia, nội địa hóa quốc phòng | `wa_*` phần kinh tế + `developmental_state` + thân chính D3/D4 | **Không** bắt buộc |
| **B3 — Dân tộc chủ nghĩa độc đoán** | Dân tộc thành nguồn chính danh chính, kiểm soát ngang yếu đi, an ninh trung tâm | `sec_*` (8) + cá nhân hóa | **Có** — slot 7 |
| **B4 — Dân tộc chủ nghĩa dân túy** | Đường phố được huy động, chính danh trực tiếp | `np_*` (14) | **Có** — slot 20 |

**B4 là bản lề sang Family A.** Mọi nấc dưới B4 đều **không** dẫn tới A theo literature, vì chúng đều giải huy động.

## B.4 Đối chiếu với Việt Nam

**[SỰ KIỆN]** Việt Nam hiện đang ở đâu đó giữa **B1 và B2**: hedging có nguyên tắc (Bốn Không), chính sách công nghiệp đang mạnh lên (Nghị quyết 57 và 68, bán dẫn, công nghiệp quốc phòng), tinh hoa kỹ trị vẫn giữ quản lý kinh tế. Việc hợp nhất TBT–Chủ tịch nước và tỷ trọng an ninh trong bộ máy là chuyển động **về phía B3**, nhưng chưa tới.

**[HỌC THUẬT]** Family B do đó là family **có khả năng cao nhất trong ba family** — nó là phần mở rộng của quỹ đạo hiện tại, không phải đứt gãy.

## B.5 Chu trình bảy bước (Family B)

| Bước | Nội dung |
|---|---|
| **1. Tiền đề** | Cạnh tranh nước lớn làm chi phí phụ thuộc tăng; năng lực công nghiệp đủ để nội địa hóa có ý nghĩa |
| **2. Kích hoạt** | Cú sốc chuỗi cung ứng, thuế quan, hoặc một sự cố chủ quyền không có thương vong |
| **3. Phản ứng tinh hoa** | Đồng thuận rộng — đây là điểm khác A: dân tộc kinh tế **không** chia rẽ tinh hoa mà gắn kết họ |
| **4. Đáp ứng thể chế** | Luật công nghiệp quốc phòng, danh mục chiến lược, sàng lọc đầu tư, dự trữ, đa dạng hóa nhà cung cấp |
| **5. Phản hồi** | Tự chủ tăng → đòn bẩy đàm phán tăng → nhưng chi phí cơ hội tích lũy (Kuik: hedging tốn cả hai đầu) |
| **6. Phụ thuộc đường đi** | Nội địa hóa sâu tạo nhóm lợi ích sống nhờ bảo hộ, khó mở lại |
| **7. Thất bại / đảo ngược** | Tăng trưởng chậm lại vì mất quy mô; hoặc leo thang sang B3/B4 khi một sự cố có thương vong xảy ra |

---

# FAMILY C — DÂN CHỦ ĐỊNH HƯỚNG PHƯƠNG TÂY

## C.1 Hai trục độc lập

**[HỌC THUẬT]** Yêu cầu quan trọng nhất của bạn ở family này: **dân chủ hóa ≠ ngả phương Tây**, và ngược lại. Đây là hai chiều trực giao:

|  | **Không liên kết / ngả Đông** | **Ngả phương Tây** |
|---|---|---|
| **Dân chủ** | Ấn Độ, Indonesia, Brazil, Nam Phi | Hàn Quốc sau 1987, Đài Loan sau 1996, Philippines |
| **Độc đoán** | Việt Nam hiện nay, Lào, Campuchia | Hàn Quốc trước 1987, Đài Loan trước 1987, các nước Vùng Vịnh |

**[SỰ KIỆN]** Mod đã code đúng điều này: `wa_development_council` (slot 0, `Western_Autocracy`) là ô **độc đoán + ngả phương Tây**, tách hẳn khỏi dải dân chủ. Đây là một quyết định thiết kế đúng cần giữ.

**[HỌC THUẬT] Nhưng có một liên hệ thật, qua một cơ chế khác:** Levitsky & Way (2010) chỉ ra biến số dự báo mạnh nhất cho việc một chế độ độc đoán cạnh tranh có dân chủ hóa hay không là **linkage** (mật độ quan hệ kinh tế, xã hội, truyền thông, giáo dục với phương Tây) — mạnh hơn cả **leverage** (sức ép). Nghĩa là: **hội nhập tạo áp lực dân chủ hóa, liên minh thì không**. Với thiết kế game, đây là phân biệt dùng được ngay: FTA, du học, kiều hối, chuỗi cung ứng đẩy về phía C; hiệp ước quân sự thì không.

## C.2 Điều kiện chuyển đổi

**[HỌC THUẬT]** Bốn tác phẩm nền:

- **O'Donnell & Schmitter (1986)**, *Transitions from Authoritarian Rule* — chuyển đổi **bắt đầu từ rạn nứt trong liên minh cầm quyền** giữa phái cứng rắn và phái mềm dẻo, không phải từ áp lực đối lập. Đối lập chỉ trở nên quan trọng **sau khi** rạn nứt đã có.
- **Przeworski (1991)**, *Democracy and the Market* — tự do hóa có hai kết cục: hoặc mở rộng độc tài, hoặc mất kiểm soát thành chuyển đổi. Thời điểm quyết định là khi đối lập có thể đe dọa một cách đáng tin.
- **Huntington (1991)**, *The Third Wave* — ba kiểu: **chuyển hóa** do tinh hoa dẫn, **thay thế** do đối lập dẫn, **chuyển vị** do thương lượng.
- **Slater & Wong (2013, 2022)**, "The Strength to Concede" và *From Development to Democracy* — **quan trọng nhất cho Việt Nam**. Ở châu Á phát triển, các đảng cầm quyền dân chủ hóa **từ thế mạnh**, khi họ tự tin còn thắng được bầu cử và muốn đổi tính chính danh lấy sự tồn tại lâu dài. Đài Loan (Quốc dân đảng), Hàn Quốc (Dân chính đảng 1987) là hai ca chuẩn.

**[HỌC THUẬT]** Hệ quả cho mod: **con đường dân chủ hóa hợp lý nhất cho Việt Nam trong literature không phải sụp đổ, mà là nhượng bộ từ thế mạnh sau một giai đoạn phát triển thành công.**

**[SỰ KIỆN]** Và đó **chính xác** là chuỗi đã code: `developmental_state → performance_legitimacy → press_relaxation → front_coalition → vetted_elections → managed_pluralism → round_table_talks → first_free_election`. Mod đã đi đúng đường Slater–Wong mà tài liệu chưa gọi tên.

## C.3 Việt Nam: bắt buộc phải qua trạm trung gian

**[SỰ KIỆN]** V-Dem xếp Việt Nam là **closed autocracy**, không phải electoral autocracy. **[HỌC THUẬT]** Trong khung V-Dem, đi từ closed autocracy tới electoral democracy phải qua electoral autocracy — tức là phải có **bầu cử đa đảng cho hành pháp trước đã**, dù không tự do và công bằng.

Nghĩa là dải `front_coalition → vetted_elections → managed_pluralism` **không phải nội dung phụ**, nó là **bước bắt buộc về lý thuyết**. Nếu người chơi đi thẳng từ ĐCSVN sang bầu cử tự do mà không qua đây, đó là một kịch bản sụp đổ, không phải kịch bản chuyển đổi — và hai thứ đó nên có hệ quả khác nhau.

## C.4 Các biến thể con (sub-variants, không phải kịch bản riêng)

**[TIỀN ĐỀ KỊCH BẢN]** Bốn gói `dm_*` đã code không phải bốn chế độ, mà là **bốn họ đảng cầm quyền** trong cùng một chế độ dân chủ — đúng như kết luận STEP 2:

| Gói đã code | Họ đảng | Định hướng đối ngoại **không** bị quy định sẵn |
|---|---|---|
| `dm_lib_*` (slot 2) | Tự do – thị trường | Có thể ngả Tây, có thể không |
| `dm_soc_*` (slot 18) | Xã hội dân chủ | Có thể ngả Tây, có thể không |
| `dm_con_*` (slot 1) | Bảo thủ – trung hữu | Có thể ngả Tây, có thể không |
| `dm_tra_*` (slot 14) | Dân tộc – truyền thống | Có thể **không** ngả Tây |

**[HỌC THUẬT]** Chỗ này là nơi nguyên tắc "dân chủ ≠ phương Tây" phải thành cơ chế: định hướng đối ngoại nên là **một lớp riêng** mà mọi chế độ đều chọn, chứ không gắn cứng vào gói đảng. Ấn Độ và Indonesia là dân chủ và không liên kết. **[SỰ KIỆN]** Hiện tại mod đã có sẵn cặp `VIE_accept_chinese_influence` ↔ `VIE_pivot_to_the_west` loại trừ nhau trên thân chính, dùng được cho mọi chế độ.

## C.5 Chu trình bảy bước (Family C)

| Bước | Nội dung |
|---|---|
| **1. Tiền đề** | Thành tích phát triển đủ để đảng cầm quyền tin mình còn thắng được; linkage với phương Tây dày (FTA, du học, kiều hối); tầng lớp trung lưu đô thị lớn |
| **2. Kích hoạt** | Một bế tắc kế nhiệm, một bê bối làm chính danh hiệu quả suy giảm, hoặc một yêu cầu từ hội nhập sâu |
| **3. Phản ứng tinh hoa** | **Rạn nứt cứng rắn ↔ mềm dẻo** (O'Donnell & Schmitter). Phái mềm dẻo tính rằng nhượng bộ có kiểm soát rẻ hơn đàn áp |
| **4. Đáp ứng thể chế** | Nới báo chí → hợp pháp hóa tổ chức trong Mặt trận → bầu cử có hiệp thương → tòa án độc lập hơn → hiến pháp mới |
| **5. Phản hồi** | Mỗi bước nới làm đối lập tổ chức tốt hơn, khiến bước sau khó đảo ngược hơn (Przeworski) |
| **6. Phụ thuộc đường đi** | Sau bầu cử tự do đầu tiên, đảo ngược đòi hỏi đảo chính công khai, tốn kém hơn nhiều |
| **7. Thất bại / đảo ngược** | Ba kiểu: **dừng lại ở độc đoán cạnh tranh** (Levitsky & Way — kết cục phổ biến nhất); **phản đòn của phái cứng rắn**; **sụp đổ kinh tế trong chuyển đổi** làm cử tri quay về độc đoán |

---

# D. QUAN HỆ GIỮA BA FAMILY

**[TIỀN ĐỀ KỊCH BẢN]** Đồ thị đúng theo literature không phải ba nhánh song song, mà là **một trục chính và hai lối rẽ có điều kiện**:

```
                    ĐỔI MỚI TIẾP TỤC  (closed autocracy, party regime)
                              │
                    ┌─────────┴─────────┐
                    │                   │
            năng lực nhà nước      chính danh dựa trên
            tăng (kỹ trị,          dân tộc tăng
            kiến tạo)                   │
                    │                   │
                    ▼                   ▼
        ┌───── B1/B2 Tự chủ + phát triển chủ nghĩa dân tộc ─────┐
        │       (KHÔNG đổi chế độ — vẫn slot 19)                │
        │                                                       │
   nhượng bộ từ                                        huy động đường phố
   thế mạnh                                            vượt kiểm soát
   (Slater & Wong)                                             │
        │                                                       ▼
        ▼                                              B4 Dân túy (slot 20)
   C  Đa đảng có kiểm soát → Dân chủ                           │
      (bắt buộc qua electoral autocracy)          ┌────────────┴────────────┐
        │                                          │                         │
        │                                   quân đội can thiệp        tinh hoa bắt tay
        ▼                                          ▼                         ▼
   dừng ở độc đoán cạnh tranh              Junta (slot 22)          A  Lạc Hồng (slot 21)
   (kết cục phổ biến nhất)                       │                         │
                                                  ▼                         ▼
                                          B3 An ninh / Hội đồng      thoái hóa thành
                                          Phát triển (7 / 0)         độc đoán thường
```

**Ba quy luật từ literature:**

1. **B là mặc định, không phải ngoại lệ.** Cả A và C đều **rẽ ra từ B**, không rẽ trực tiếp từ Đổi Mới. Tự chủ chiến lược và phát triển chủ nghĩa dân tộc là phần mở rộng của quỹ đạo hiện tại.
2. **A chỉ tới được qua B4.** Mọi nấc B khác đều giải huy động, mà giải huy động là rào chặn A theo tiêu chí Linz–Mann.
3. **C có hai lối vào với hệ quả khác nhau:** nhượng bộ từ thế mạnh (Slater & Wong — ổn định) và sụp đổ (O'Donnell–Schmitter kiểu "replacement" — bất ổn). **[SỰ KIỆN]** Mod đã có cả hai (`managed_pluralism` và `round_table_talks` sau Collapse) nhưng **chưa phân biệt hệ quả**.

---

# E. HỆ QUẢ THIẾT KẾ (chưa phải đề xuất code)

| Phát hiện | Hệ quả |
|---|---|
| Family B là mặc định, A và C rẽ ra từ B | Đổi Mới không nên rẽ thẳng ba hướng; nó nên rẽ vào **các trục xây dựng nhà nước** rồi mới phân kỳ |
| A cần điều kiện cấu trúc, không chỉ điều kiện chế độ | Cửa Lạc Hồng nên kiểm tra thêm ít nhất hai điều kiện, không chỉ "đang ở Dân túy" |
| Phân biệt huy động ↔ giải huy động là tiêu chí chia A và B | Cần **một đại lượng huy động quần chúng** — hiện chưa có. Thanh `VIE_populist_balance` (Nhà nước ↔ Đường phố) đã là đúng ý này nhưng chỉ tồn tại trong chế độ Dân túy |
| Linkage ≠ alignment (Levitsky & Way) | Hội nhập kinh tế nên đẩy về phía C; hiệp ước quân sự thì không. Hiện mod không phân biệt |
| Dân chủ hóa từ thế mạnh (Slater & Wong) | Chuỗi kiến tạo → đa nguyên có quản lý **đã đúng**; nên gọi tên và củng cố, không phải viết lại |
| Closed autocracy phải qua electoral autocracy | `vetted_elections` là bước bắt buộc, không phải trang trí; đi tắt nên bị phạt |
| Bốn gói `dm_*` không quy định đối ngoại | Định hướng đối ngoại nên là lớp riêng dùng chung cho mọi chế độ |
| Kết cục phổ biến nhất của A là entropy, của C là dừng ở độc đoán cạnh tranh | Cả hai family cần **kết cục "nửa chừng"**, không chỉ kết cục cực đoan |

---

# F. KHOẢNG TRỐNG CẦN KIỂM CHỨNG THÊM

1. **Không có đại lượng huy động quần chúng dùng chung.** Đây là biến số phân biệt A với B trong literature, và mod chưa có nó ngoài phạm vi chế độ Dân túy.
2. **Chưa đọc literature riêng về quan hệ dân sự – quân sự Việt Nam.** Thayer và Vu Tuong có công trình về vai trò chính trị của Quân đội nhân dân; cần đọc trước khi thiết kế cửa junta, vì tỷ trọng 18% BCH TƯ là con số lớn cần được diễn giải đúng.
3. **Chưa kiểm chứng phía "phản chứng" cho Family A.** Cần tìm literature về các trường hợp **có đủ điều kiện mà không thành phát xít** để cân bằng đánh giá.
4. **Số liệu linkage của Việt Nam với phương Tây** (FDI, du học sinh, kiều hối, thương mại) chưa được dùng làm căn cứ định lượng cho Family C.
5. **Chi phí giao diện** nếu biến "huy động" và "năng lực nhà nước" thành hai power balance mới — chưa khảo sát nước nào trong MD có nhiều BoP nhất.

---

## Nguồn

**Chế độ và chuyển đổi:** Linz & Stepan (1996); Linz (2000) *Totalitarian and Authoritarian Regimes*; Geddes, Wright & Frantz (2014) *Perspectives on Politics* 12(2); Levitsky & Way (2010) *Competitive Authoritarianism*; O'Donnell & Schmitter (1986); Przeworski (1991); Huntington (1991); Slater & Wong (2013) *Perspectives on Politics* 11(3) và (2022) *From Development to Democracy*.

**Phát xít và dân tộc chủ nghĩa:** Paxton (2004) *The Anatomy of Fascism*; Griffin (1991) *The Nature of Fascism*; Mann (2004) *Fascists*; Berman (1997) "Civil Society and the Collapse of the Weimar Republic" *World Politics*; Riley (2010) *The Civic Foundations of Fascism in Europe*; Gellner (1983) *Nations and Nationalism*; Brubaker (1996) *Nationalism Reframed*; Mudde (2004) "The Populist Zeitgeist" *Government and Opposition*; Levitsky & Loxton (2013) "Populism and Competitive Authoritarianism in the Andes" *Democratization*.

**Nhà nước kiến tạo và kinh tế chính trị:** Johnson (1982); Amsden (1989); Wade (1990); Evans (1995); Woo-Cumings (1999); Helleiner (2002); Gerschenkron (1962).

**Đối ngoại và Việt Nam:** Kuik (2008) "The Essence of Hedging" *Contemporary Southeast Asia*; Goh (2005); Le Hong Hiep (2013); Vuving (2006).

**Dữ liệu và think tank:** [V-Dem Democracy Report 2025](https://v-dem.net/documents/54/v-dem_dr_2025_lowres_v1.pdf); [Freedom House, Vietnam 2025](https://freedomhouse.org/country/vietnam/freedom-world/2025); [ISEAS Perspective 2026/29, Nguyen Khac Giang](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2026-29-vietnams-reconfigured-leadership-personnel-and-power-in-the-new-era-by-nguyen-khac-giang/); [ISEAS Perspective 2025/14 về cải cách bộ máy](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-14-vietnams-bureaucratic-reforms-opportunities-and-challenges-in-the-era-of-national-rise-by-nguyen-khac-giang/); [The Diplomat về Đại hội XIV](https://thediplomat.com/2026/01/vietnams-14th-national-congress-power-reform-and-the-next-political-generation/); [Oxford, *International Relations of the Asia-Pacific* về khủng hoảng giàn khoan 2014](https://academic.oup.com/irap/article/25/3/lcaf010/8380159).

---

## Bước 4: Kỹ trị, nhà nước kiến tạo và năng lực nhà nước

# Bước 4: Kỹ trị, nhà nước kiến tạo và năng lực nhà nước

> Tiếp theo `VIE_regime_taxonomy_step1_2.md` và `VIE_three_families_step3.md`. **Chưa** thiết kế khung xây dựng nhà nước (STEP 5), **chưa** đề xuất sửa focus.
>
> Nhãn: **[SỰ KIỆN]** · **[HỌC THUẬT]** · **[TƯƠNG TỰ LỊCH SỬ]** · **[TIỀN ĐỀ KỊCH BẢN]** · **[TRỪU TƯỢNG GAMEPLAY]**

---

## 0. Phát hiện quan trọng nhất của bước này

**[SỰ KIỆN]** Millennium Dawn **đã có sẵn một hệ năng lực nhà nước hoàn chỉnh**, gồm 7 họ luật có biến theo dõi, đã được khởi tạo cho Việt Nam bằng giá trị lịch sử hợp lý. Submod `md_vietnam` **chưa từng chạm vào nó một lần nào**.

| Hệ thống MD | Biến | Giá trị khởi đầu của VIE | Số lần submod dùng |
|---|---|---|---|
| Luật bộ máy hành chính | `bureau_law` | **bureau_03** (giữa) | **0** |
| Luật cảnh sát | `police_law` | **police_05** (cao nhất) | **0** |
| Luật giáo dục | `education_law` | edu_03 | **0** |
| Luật y tế | `health_law` | health_02 | **0** |
| Luật an sinh | `social_law` | social_02 | **0** |
| Luật quân sự | `military_law` | defence_02 | **0** |
| Thuế | `tax_rate`, `corporate_tax_rate` | — | **0** |
| Tham nhũng | `corruption_level_XX` | **corruption_level_08** (cao) | 39 |

Submod gọi `treasury_change` **162 lần** nhưng chưa bao giờ đụng tới một luật nào. Nghĩa là: **lớp "năng lực nhà nước" mà bạn muốn xây không cần phát minh — nó đã nằm sẵn trong MD, chỉ chưa được nối vào cây focus.**

---

## 1. Nhà nước kiến tạo thực sự là gì

**[HỌC THUẬT]**

### 1.1 Bốn công trình nền

**Johnson (1982), *MITI and the Japanese Miracle*** — đặt ra thuật ngữ. Phân biệt ba loại nhà nước: **plan-rational** (Nhật — nhà nước đặt mục tiêu thực chất cho nền kinh tế và can thiệp theo cách thuận thị trường), **plan-ideological** (Liên Xô — kế hoạch thay thế thị trường), **market-rational** (Mỹ — nhà nước chỉ đặt luật chơi). Bốn đặc điểm của nhà nước kiến tạo:
1. Một bộ máy kinh tế **nhỏ, tinh hoa, tuyển theo năng lực**
2. Một hệ thống chính trị cho bộ máy đó **không gian để hành động** — "chính trị gia trị vì, quan chức cai trị"
3. Can thiệp bằng phương pháp **thuận thị trường**
4. Có một **cơ quan đầu não** (pilot agency) điều phối

**Amsden (1989), *Asia's Next Giant*** (Hàn Quốc) — đóng góp cơ chế then chốt: **tính có đi có lại** (reciprocity). Nhà nước trợ cấp, nhưng **đổi lấy tiêu chuẩn thành tích** kiểm chứng được, chủ yếu là chỉ tiêu xuất khẩu. Doanh nghiệp không đạt thì bị cắt. Đây là thứ phân biệt chính sách công nghiệp thành công với bảo hộ thất bại.

**Wade (1990), *Governing the Market*** (Đài Loan) — nhà nước hướng đầu tư vào các ngành mà thị trường tự nó không rót vốn vào.

**Evans (1995), *Embedded Autonomy*** — đóng góp lý thuyết quyết định. Nhà nước kiến tạo cần **đồng thời hai điều kiện đối nghịch nhau**:
- **Tự chủ** — bộ máy Weber hóa, tuyển theo năng lực, có bản sắc riêng, **không bị doanh nghiệp bắt cóc**
- **Gắn kết** — mạng lưới quan hệ dày đặc với doanh nghiệp để biết thông tin thật

Và hai kiểu hỏng:

| Mất cân bằng | Kết quả | Ví dụ của Evans |
|---|---|---|
| Tự chủ nhiều, gắn kết ít | Nhà nước xa rời, chính sách sai thông tin | Ấn Độ thời kỳ đầu |
| Gắn kết nhiều, tự chủ ít | **Bị bắt cóc — tài phiệt** | Nhiều nước Mỹ Latinh |
| Không có cả hai | **Nhà nước ăn cướp** | Zaire |
| Có cả hai | Nhà nước kiến tạo | Nhật, Hàn, Đài Loan |

**[HỌC THUẬT]** Dòng thứ hai của bảng này là kết nối trực tiếp tới dải `ol_*` trong mod: **tài phiệt không phải một chế độ khác, nó là nhà nước kiến tạo mất tự chủ.** Evans coi chúng là hai điểm trên cùng một chiều.

### 1.2 Điều kiện nào sinh ra nhà nước kiến tạo

**Doner, Ritchie & Slater (2005), "Systemic Vulnerability and the Origins of Developmental States", *International Organization* 59(2)** — công trình quan trọng nhất cho thiết kế game, vì nó nói nhà nước kiến tạo **bị ép ra đời, không phải được chọn**. Ba điều kiện phải hội tụ:

1. **Mối đe dọa an ninh nghiêm trọng từ bên ngoài**
2. **Khan hiếm nguồn lực** — không có dầu, không có viện trợ vô điều kiện
3. **Nhu cầu mua sự trung thành của quần chúng** — tinh hoa cầm quyền phải cần dân ủng hộ

Khi cả ba cùng có, giới cầm quyền **không còn lựa chọn nào khác** ngoài xây dựng bộ máy có năng lực và ép doanh nghiệp làm ăn thật.

**[TIỀN ĐỀ KỊCH BẢN]** Đây là điều kiện tiên quyết có cơ sở cho nhánh kiến tạo trong mod, thay cho điều kiện hiện tại (`VIE_bop_is_reformist`). Việt Nam có điều kiện 1 (Trung Quốc) rõ ràng, điều kiện 2 một phần, điều kiện 3 tùy vào chính danh.

### 1.3 Nó có phải một chế độ không

**Không.** **[HỌC THUẬT]** Bằng chứng trong literature:

| Nước | Thời kỳ | Chế độ | Nhà nước kiến tạo? |
|---|---|---|---|
| Nhật Bản | 1955–1990 | Dân chủ suốt | **Có** |
| Hàn Quốc | 1961–1987 | Độc tài quân sự | **Có** |
| Hàn Quốc | 1987–nay | Dân chủ | **Có**, dạng biến đổi |
| Đài Loan | 1950–1996 | Độc đảng | **Có** |
| Singapore | 1965–nay | Độc đoán bầu cử | **Có** |

Cùng một mô hình kinh tế xuất hiện ở bốn cấu hình chính trị khác nhau, và tồn tại **xuyên qua** chuyển đổi dân chủ ở hai nước. Kết luận: nhà nước kiến tạo là **quan hệ nhà nước – xã hội + hình thái bộ máy + bộ công cụ chính sách**, không phải một loại chế độ.

---

## 2. Kỹ trị thực sự là gì

**[HỌC THUẬT]**

**Centeno (1993), "The New Leviathan: The Dynamics and Limits of Technocracy", *Theory and Society* 22(3)** — định nghĩa được trích dẫn nhiều nhất: sự thống trị hành chính và chính trị của một xã hội bởi **một tinh hoa nhà nước** tìm cách áp đặt **một hệ hình chính sách duy nhất, loại trừ**, dựa trên việc áp dụng các kỹ thuật duy lý công cụ.

Lập luận then chốt của Centeno, và là câu trả lời cho câu hỏi của bạn: **kỹ trị không tự sinh ra tính chính danh.** Nó luôn phải mượn chính danh từ một nguồn khác — một đảng, một lãnh tụ, một cuộc bầu cử, hoặc một cuộc khủng hoảng. Vì vậy nó **không thể là một loại chế độ**: chế độ là câu trả lời cho "ai cầm quyền và bằng quyền gì", mà kỹ trị không có câu trả lời riêng cho vế thứ hai.

**Putnam (1977)** — "tâm thế kỹ trị" là một thuộc tính **đo được của quan chức**, không phải một hình thức chính thể.

**Dargent (2015), *Technocracy and Democracy in Latin America*** — kỹ trị lên nắm quyền **trong các nền dân chủ** thông qua ủy quyền: ngân hàng trung ương độc lập, cơ quan quản lý, bộ tài chính. Nghĩa là kỹ trị hoàn toàn tương thích với dân chủ.

**Bickerton & Invernizzi Accetti (2021), *Technopopulism*** — kỹ trị và dân túy chia sẻ cùng một logic: cả hai đều viện dẫn **lợi ích chung không qua trung gian**, bỏ qua sự trung giới của đảng phái. Hai thứ có thể hợp nhất.

**[HỌC THUẬT] Kết luận:** kỹ trị là **cách tuyển chọn tinh hoa + cách biện minh chính sách**. Trên khung phân lớp, nó là giá trị cao ở **lớp năng lực** kèm giá trị thấp ở **lớp ràng buộc quyền lực**. Nó không có ô riêng ở lớp chế độ.

---

## 3. Hai thứ này có phải cùng một loại không

**Không.** Chúng trả lời hai câu hỏi khác nhau:

- **Nhà nước kiến tạo** = *nhà nước làm gì với nền kinh tế, và quan hệ với doanh nghiệp ra sao*
- **Kỹ trị** = *ai ngồi trong bộ máy, và họ viện quyền gì*

**[TƯƠNG TỰ LỊCH SỬ]** Bốn ô đều có ca thật:

|  | **Kỹ trị mạnh** | **Kỹ trị yếu** |
|---|---|---|
| **Kiến tạo mạnh** | Nhật (MITI), Singapore, Đài Loan | Hàn Quốc đầu thời Park — quân sự hóa, cá nhân hóa, nhưng vẫn có chính sách công nghiệp có đi có lại |
| **Kiến tạo yếu** | Chile thời "Chicago Boys" — kỹ trị mạnh nhưng **chống** chính sách công nghiệp; các nội các ổn định hóa kiểu IMF | Nhà nước ăn cướp (Evans) |

Ô trên bên phải và ô dưới bên trái chứng minh hai khái niệm **độc lập với nhau**. Đây là lý do không thể gộp `VIE_developmental_state` và `VIE_technocrat_cabinet` thành một thứ, mà cũng không thể tách chúng thành hai chế độ.

---

## 4. Năng lực nhà nước

**[HỌC THUẬT]**

### 4.1 Khái niệm trung tâm: quyền lực chuyên chế ≠ quyền lực hạ tầng

**Mann (1984), "The Autonomous Power of the State", *European Journal of Sociology*** — phân biệt quan trọng nhất trong toàn bộ literature này:

- **Quyền lực chuyên chế (despotic power):** tinh hoa nhà nước **có thể làm gì mà không cần thương lượng** với xã hội
- **Quyền lực hạ tầng (infrastructural power):** nhà nước **thực sự có thể thẩm thấu vào xã hội và thi hành quyết định** tới đâu

Hai thứ này **độc lập**. Một chế độ có thể chuyên chế cao mà hạ tầng yếu — ra lệnh gì cũng được nhưng không thực hiện được lệnh nào. Và ngược lại: các nhà nước Bắc Âu có quyền lực hạ tầng rất cao và quyền lực chuyên chế rất thấp.

**[HỌC THUẬT] Áp dụng cho Việt Nam:** nhà nước Việt Nam có quyền lực hạ tầng tương đối cao so với mức thu nhập — thu được thuế, làm được tổng điều tra, triển khai được tiêm chủng và dân quân tới cấp xã. Các động thái ở Đại hội XIV (hợp nhất TBT–Chủ tịch nước, an ninh nắm vị trí trọng yếu) làm tăng **quyền lực chuyên chế**. Các cải cách bộ máy nhắm vào **quyền lực hạ tầng** nhưng chưa chắc đạt được. **Đây là hai thanh khác nhau và không nên gộp.**

### 4.2 Ba chiều đo được

**Hanson & Sigman (2021), "Leviathan's Latent Dimensions: Measuring State Capacity for Comparative Political Research", *Journal of Politics* 83(4)** — phân tích nhân tố trên hàng chục chỉ số, tìm ra **ba chiều**:

1. **Khai thác (extractive)** — thu ngân sách
2. **Cưỡng chế (coercive)** — kiểm soát lãnh thổ, độc quyền bạo lực
3. **Hành chính (administrative)** — cung cấp dịch vụ, đăng ký dân cư, thực thi hợp đồng

**Fukuyama (2013), "What Is Governance?", *Governance* 26(3)** — năng lực và trách nhiệm giải trình là **hai trục trực giao**. Nhà nước có thể mạnh và độc đoán, mạnh và dân chủ, yếu và dân chủ, yếu và độc đoán.

**Evans & Rauch (1999), "Bureaucracy and Growth", *American Sociological Review* 64(5)** — phát hiện dùng được ngay: **thang Weber hóa** gồm hai thành phần, **tuyển theo năng lực** và **lộ trình sự nghiệp dự đoán được**, tương quan có ý nghĩa với tăng trưởng, kiểm soát cả GDP ban đầu lẫn vốn con người. Nghĩa là *cách tuyển người* có hiệu ứng kinh tế đo được, không chỉ là chuyện đạo đức.

**Besley & Persson (2011), *Pillars of Prosperity*** — năng lực tài khóa và năng lực pháp lý là **khoản đầu tư**: tốn chi phí trước, sinh lợi sau. Đây là cơ sở lý thuyết cho việc trong game, nâng năng lực phải **tốn tiền và tốn thời gian**, không phải bấm một cái là có.

---

## 5. Việt Nam: dữ liệu thật về cải cách bộ máy

**[SỰ KIỆN]** (ISEAS Perspective 2025/14, Nguyễn Khắc Giang)

| Chỉ số | Giá trị |
|---|---|
| Khu vực công | ~4 triệu người, **7,9% lực lượng lao động** (2023), thuộc nhóm lớn nhất Đông Nam Á |
| Bộ ngành | 22 → **17** (tính cả cơ quan thuộc Chính phủ: 30 → 22) |
| Tổng cục bị bỏ | **519 đơn vị, 86%** |
| Cục/vụ bị bỏ | **219 đơn vị, 54%** |
| Mỗi bộ phải cắt tầng trung gian | **30%** |
| Công an cấp huyện | **705 đơn vị bị giải thể** |
| Tinh giản ngay | **100.000 người trong 6 tháng** |
| Mục tiêu dài hạn | **giảm 20%, khoảng 400.000 người** |
| Chi phí | **130.000 tỷ đồng ≈ 5,1 tỷ USD = 6,4% chi ngân sách 2024** |
| Văn bản pháp luật phải sửa hoặc bỏ | **hơn 5.000**, khoảng 300 luật trong một kỳ họp |

**[HỌC THUẬT] Chẩn đoán của tác giả:** vấn đề cốt lõi **không phải số lượng biên chế** mà là **phân mảnh** — nhiều đầu mối nắm quyền, chồng lấn thẩm quyền. Nhà đầu tư phải xin **30–40 con dấu** từ các sở ngành, mất **hai đến ba năm**.

**[HỌC THUẬT] Rủi ro tác giả nêu — và đây là chất liệu đánh đổi tốt nhất trong toàn bộ nghiên cứu này:**

- Tiến độ gấp tạo lỗ hổng cho tham nhũng và **"chạy ghế"**
- Có thể **giữ lại người kém và mất người giỏi**, dẫn tới "chính quyền do những người kém năng lực nhất điều hành"
- Siêu bộ có thể **tập trung quyền quá mức** và giảm kiểm soát
- Gián đoạn chuyển tiếp làm giảm niềm tin nhà đầu tư

Nói cách khác: **một cuộc cải cách nhằm tăng năng lực nhà nước có thể làm giảm năng lực nhà nước.** Đó chính xác là kiểu đánh đổi bạn muốn, và nó có nguồn.

**[SỰ KIỆN] Đo lường sẵn có của Việt Nam:** **PAPI** (UNDP, từ 2009, cả 63 tỉnh) đo 8 chiều: *tham gia ở cấp cơ sở, công khai minh bạch, trách nhiệm giải trình với người dân, kiểm soát tham nhũng, thủ tục hành chính công, cung ứng dịch vụ công, quản trị môi trường, quản trị điện tử*. **PCI** (từ 2005) đo chất lượng điều hành kinh tế cấp tỉnh. Edmund Malesky là tác giả chính của PCI và thành viên nhóm nghiên cứu PAPI từ đầu.

**[TIỀN ĐỀ KỊCH BẢN]** Tám chiều PAPI là quá nhiều cho gameplay, nhưng chúng là **bộ khung Việt Nam chính thức** để rút gọn, thay vì tự nghĩ ra.

---

## 6. MD đã có gì, và nó mô hình hóa đúng đến đâu

**[SỰ KIỆN]** Đối chiếu ba chiều Hanson–Sigman với cơ chế MD:

| Chiều năng lực | Cơ chế MD sẵn có | VIE khởi đầu | Mô hình hóa đúng không |
|---|---|---|---|
| **Khai thác** | `tax_rate`, `corporate_tax_rate`, hệ ngân sách `treasury` | — | **Khá đúng** |
| **Cưỡng chế** | `police_law` 1–5, `military_law` | **police_05 — cao nhất** | **Đúng**, và giá trị khởi đầu hợp lý |
| **Hành chính** | `bureau_law` 1–5 | **bureau_03** | **Chỉ một nửa** — xem dưới |

**[HỌC THUẬT] Hạn chế quan trọng:** `bureau_law` của MD mô hình hóa **quy mô và chi phí** của bộ máy, không phải **chất lượng** của nó. Ở mức 5, hiệu ứng là `political_power_gain = 1.0` và `production_speed_buildings_factor = -0.2` — bộ máy to hơn thì ra quyết định chính trị nhanh hơn nhưng xây dựng chậm hơn và tốn ngân sách hơn.

Đó là chiều **"nhiều hay ít"**, không phải chiều **"tốt hay tệ"**. Thang Weber hóa của Evans & Rauch — tuyển theo năng lực và lộ trình dự đoán được — **không có đại diện nào trong MD**. Thứ gần nhất là `corruption_level_XX`, nhưng tham nhũng là **hệ quả** của chất lượng bộ máy, không phải bản thân chất lượng đó.

**[TIỀN ĐỀ KỊCH BẢN] Hệ quả:** submod cần **đúng một** đại lượng mới — chất lượng bộ máy theo nghĩa Weber — và nối vào bốn thứ đã có sẵn (`bureau_law`, `police_law`, `tax_rate`, `corruption_level`). Không cần xây cả một hệ thống năng lực nhà nước.

---

## 7. Trả lời năm câu hỏi của bạn

**1. Nhà nước kiến tạo thực sự là gì?**
Một **quan hệ nhà nước–xã hội** (tự chủ gắn kết, theo Evans) cộng một **hình thái bộ máy** (cơ quan đầu não tuyển theo năng lực, theo Johnson) cộng một **bộ công cụ chính sách** (trợ cấp có đi có lại đổi lấy thành tích xuất khẩu, theo Amsden). Nó bị ép ra đời bởi tổn thương hệ thống, chứ không được chọn tùy ý (Doner–Ritchie–Slater).

**2. Kỹ trị thực sự là gì?**
Một **cách tuyển chọn tinh hoa** và một **cách biện minh chính sách**, không tự sinh ra chính danh (Centeno). Nó luôn ký sinh vào một nguồn chính danh khác.

**3. Hai thứ này có cùng một loại không?**
**Không.** Bốn ô trong bảng 2×2 ở mục 3 đều có ca lịch sử thật. Chúng độc lập với nhau.

**4. Kỹ trị nên là gì?**
**Phong cách cầm quyền cộng mô hình năng lực nhà nước** — tức là **lớp 2 và lớp 3**, dùng được cho mọi family. **Không phải** chế độ, **không phải** nhánh con của một chế độ duy nhất.
*Bạn nghi ngờ đúng, và literature xác nhận, chứ không phải tôi chiều theo ý bạn: lập luận quyết định là của Centeno về việc kỹ trị không thể tự sinh chính danh, cộng với bằng chứng của Dargent rằng kỹ trị tồn tại bình thường trong các nền dân chủ.*
**Lưu ý:** `VIE_ng_technocratic_caretaker` trong mod là **chính phủ lâm thời kỹ trị**, một thứ khác — đó là một **cơ chế chuyển tiếp** có thời hạn, không phải kỹ trị như phong cách cầm quyền. Hai cái trùng tên nhưng khác loại.

**5. Nhà nước kiến tạo nên nằm ở đâu?**
**Ở nhiều family, nhưng với điều kiện tiên quyết và trần khác nhau.** Bằng chứng: Nhật dân chủ, Hàn và Đài độc tài rồi dân chủ, Singapore độc đoán bầu cử — cùng mô hình, bốn cấu hình chính trị.
Cụ thể cho mod:
- **Trong Đổi Mới (slot 19):** có — đây là vị trí hiện tại và nó đúng
- **Trong Family B dân tộc chủ nghĩa:** có — đó chính là "phát triển chủ nghĩa dân tộc", nấc B2
- **Trong nhánh độc đoán:** có — `wa_*` Hội đồng Phát triển là mô hình Park Chung-hee
- **Trong nhánh dân chủ:** có — Nhật và Hàn sau 1987
- **Điều kiện khác nhau:** dân chủ thì khó giữ tự chủ hơn (áp lực cử tri), độc đoán thì dễ mất gắn kết hơn (không có kênh phản hồi)

---

## 8. Cập nhật khung phân lớp sau bước 4

Khung 5 lớp ở STEP 2 vẫn đứng vững, nhưng lớp 2 cần tách đôi theo Mann:

| Lớp | Nội dung | Cơ chế MD sẵn có |
|---|---|---|
| 1. **Chế độ** | Ai chọn người cầm quyền | `ruling_party`, `VIE_transition_regime` |
| 2a. **Quyền lực hạ tầng** | Nhà nước thực thi được tới đâu | `bureau_law`, `police_law`, `tax_rate` — **chưa dùng** |
| 2b. **Chất lượng bộ máy** | Tuyển theo năng lực, dự đoán được | **Chưa có — cần thêm đúng một đại lượng** |
| 3. **Ràng buộc quyền lực** | Tư pháp, Quốc hội, báo chí, phân cấp | `VIE_party_balance` một phần |
| 4. **Mô hình kinh tế** | Nhà nước ↔ thị trường, tự chủ ↔ gắn kết | Luật kinh tế MD, `treasury` |
| 5. **Đối ngoại** | Tự chủ / cân bằng / nghiêng bên nào | Ý tưởng Ba–Bốn Không, cặp loại trừ đã có |

**[TIỀN ĐỀ KỊCH BẢN]** Lớp 2b là nơi "kỹ trị" sống. Lớp 4 là nơi "nhà nước kiến tạo" sống. Chúng gặp nhau ở **tự chủ gắn kết** của Evans: tự chủ cao mà gắn kết thấp thì thành nhà nước xa rời; gắn kết cao mà tự chủ thấp thì **thành dải `ol_*` tài phiệt**.

---

## 9. Hệ quả thiết kế

| Phát hiện | Hệ quả cho STEP 5 |
|---|---|
| MD có 7 họ luật, submod dùng 0 | Focus cải cách bộ máy nên **đổi `bureau_law`**, không chỉ cho PP. Việc này gần như miễn phí về kỹ thuật |
| `bureau_law` đo quy mô, không đo chất lượng | Cần **một** đại lượng mới duy nhất: chất lượng bộ máy kiểu Weber |
| Evans: tài phiệt = kiến tạo mất tự chủ | `ol_*` nên là **điểm cuối của một chiều đo**, không phải một chế độ tách rời |
| Doner–Ritchie–Slater: kiến tạo bị ép ra đời | Điều kiện mở nhánh kiến tạo nên là **đe dọa + khan hiếm + cần chính danh quần chúng**, không phải `VIE_bop_is_reformist` |
| Amsden: có đi có lại | Focus vô địch quốc gia nên **kèm điều kiện thành tích**, nếu không đạt thì mất — đây là đánh đổi có nguồn |
| Cải cách có thể làm giảm năng lực | Chuỗi tinh gọn bộ máy 2024–2025 nên có **rủi ro thật**, không chỉ toàn lợi ích |
| Mann: chuyên chế ≠ hạ tầng | Hợp nhất TBT–Chủ tịch nước tăng chuyên chế, **không** tăng hạ tầng. Hai thứ nên tách |
| Kỹ trị dùng được ở mọi family | `technocrat_cabinet`, `meritocratic_service` nên **thoát khỏi** dải kiến tạo và thành lựa chọn chung |
| PAPI 8 chiều | Rút gọn thành 3 chiều làm khung đo, thay vì tự nghĩ |

---

## 10. Khoảng trống cần kiểm chứng thêm

1. **Giới hạn kỹ thuật của việc đổi luật MD bằng focus.** Luật MD có `available` gắn với `budget_law_parliament_change_allowed` và chi phí PP. Cần thử xem `swap_ideas` từ `bureau_03` sang `bureau_04` trong `completion_reward` có chạy sạch không, hay phải dùng effect riêng của MD.
2. **Chi phí ngân sách.** Nâng `bureau_law` làm tăng `expected_adm_spending`. Nếu focus nâng luật mà người chơi không đủ ngân sách thì hệ thống ngân sách MD phản ứng thế nào — chưa kiểm.
3. **Literature về quan hệ dân sự – quân sự Việt Nam** vẫn chưa đọc (nợ từ STEP 3). Cần cho lớp 2a chiều cưỡng chế.
4. **Dữ liệu PAPI theo năm** chưa dùng. Nếu muốn đặt giá trị khởi đầu và mục tiêu cho đại lượng chất lượng bộ máy, nên lấy mốc từ PAPI 2011 và 2024 thay vì đoán.
5. **Cách MD tính `corruption_level` tác động lên PP và ngân sách** — cần biết để không cộng dồn hai lần với đại lượng chất lượng bộ máy mới.

---

## Nguồn

**Nhà nước kiến tạo:** Johnson (1982) *MITI and the Japanese Miracle*; Amsden (1989) *Asia's Next Giant*; Wade (1990) *Governing the Market*; Evans (1995) *Embedded Autonomy*; Woo-Cumings ed. (1999) *The Developmental State*; Doner, Ritchie & Slater (2005) *International Organization* 59(2); Haggard (2018) *Developmental States*.

**Kỹ trị:** Centeno (1993) *Theory and Society* 22(3); Putnam (1977) *Comparative Political Studies*; Meynaud (1968) *Technocracy*; Dargent (2015) *Technocracy and Democracy in Latin America*; Bickerton & Invernizzi Accetti (2021) *Technopopulism*.

**Năng lực nhà nước:** Mann (1984) *European Journal of Sociology* 25(2); Soifer (2008) *Studies in Comparative International Development* 43; Fukuyama (2013) *Governance* 26(3); Hanson & Sigman (2021) *Journal of Politics* 83(4); Evans & Rauch (1999) *American Sociological Review* 64(5); Besley & Persson (2011) *Pillars of Prosperity*.

**Việt Nam:** [ISEAS Perspective 2025/14, Nguyen Khac Giang, về cải cách bộ máy](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-14-vietnams-bureaucratic-reforms-opportunities-and-challenges-in-the-era-of-national-rise-by-nguyen-khac-giang/); [PAPI, UNDP Việt Nam](https://papi.org.vn/eng/); [Chỉ số quản trị của Edmund Malesky, Duke](https://sites.duke.edu/malesky/governance-indices/).

**Cơ chế MD (đọc trực tiếp từ file):** `common/ideas/AA_law_budget.txt` (bureau_01…05, police, edu, health, social, military), `common/scripted_effects/00_budget_effects.txt` (tax_rate, corruption), `history/countries/VIE - Vietnam.txt` (giá trị khởi đầu của Việt Nam).

---

## Bước 5: Khung xây dựng nhà nước bên trong Đổi Mới tiếp tục

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

---

## Bước 6: Ánh xạ khung xây dựng nhà nước vào Đổi Mới tiếp tục

# Bước 6: Ánh xạ khung xây dựng nhà nước vào "Đổi Mới tiếp tục"

> Tiếp theo STEP 1–5. **Chưa** vẽ transition graph cuối (STEP 8), **chưa** lên kế hoạch code (STEP 9).
> Bảng ánh xạ đầy đủ nằm ở **`D:\HOI4Mods\_gen\axis_map.py`** — file dữ liệu máy đọc được, không phải văn xuôi.
>
> Nhãn: **[SỰ KIỆN]** · **[HỌC THUẬT]** · **[TIỀN ĐỀ KỊCH BẢN]** · **[TRỪU TƯỢNG GAMEPLAY]**

---

## 0. Kết quả bước này trong một đoạn

Tôi đã gán hiệu ứng trục cho **167 trên 197 focus thân lịch sử (85%)**, rồi chạy thử: nếu người chơi đi hết thân lịch sử, cấu hình nhà nước thu được **tái tạo đúng hồ sơ của Việt Nam thật ở từng giai đoạn** — kể cả những chỗ phản trực giác như thị trường **thụt lùi** giai đoạn 2007–2010 và phân cấp **âm** giai đoạn 2021–2026. Mô hình không được tinh chỉnh để ra kết quả đó; nó ra như vậy vì bản thân các focus đã đúng lịch sử.

Nhưng phép thử cũng phơi ra một vấn đề thật: **bốn trên bảy trục không phải là lựa chọn** trong thân lịch sử — chúng chỉ có một chiều đi. Mục 6 và 7 xử lý chuyện đó.

---

## 1. Đổi Mới: từ một focus thành xương sống

**[SỰ KIỆN]** Hiện nay `VIE_doi_moi_continues` là một focus gốc ở (27, 0), phần thưởng là một idea, và **không có vai trò cơ chế nào sau đó**. 486 focus còn lại không đọc nó.

**[TIỀN ĐỀ KỊCH BẢN]** Trong thiết kế này nó đảm nhận ba việc:

1. **Khởi tạo** bảy trục bằng giá trị Việt Nam năm 2000 và gắn `VIE_state_modifier`
2. **Là điểm đọc**: mọi capstone (`era_of_rising`, `party_centennial_2030`, `developed_nation_2045`) và mọi cửa rẽ chế độ đọc cấu hình trục thay vì đọc cờ
3. **Là khung kể chuyện**: năm giai đoạn ở mục 3 cho người chơi biết mình đang ở đâu trong quá trình

Quan trọng: **không thêm focus mới nào** cho việc này. Đổi Mới thành xương sống bằng cách các focus lịch sử sẵn có bắt đầu đẩy trục.

---

## 2. Việt Nam năm 2000: giá trị khởi đầu của bảy trục

**[SỰ KIỆN] + [HỌC THUẬT]** Mỗi giá trị đều có căn cứ, không phải đoán:

| Trục | Khởi đầu | Căn cứ |
|---|---|---|
| **size** quy mô bộ máy | **+3** | MD đặt VIE ở `bureau_03` trên thang 1–5. Khu vực công 7,9% lực lượng lao động, thuộc nhóm lớn nhất Đông Nam Á (ISEAS 2025/14) |
| **merit** chất lượng bộ máy | **−2** | MD đặt VIE ở `corruption_level_08` trên thang 1–10. Hệ cán bộ vận hành bằng bảo trợ, chưa có thi tuyển cạnh tranh diện rộng |
| **decent** phân cấp | **+1** | Các tỉnh Việt Nam có quyền tự quyết trên thực tế cao bất thường — PCI ra đời năm 2005 chính vì 63 tỉnh quản trị rất khác nhau (Malesky) |
| **checks** ràng buộc quyền lực | **−2** | Quốc hội tồn tại và đang dần chất vấn mạnh hơn, nhưng không có tư pháp độc lập. V-Dem: **closed autocracy** |
| **market** nhà nước ↔ thị trường | **−2** | Năm 2000 DNNN chiếm ưu thế, Luật Doanh nghiệp vừa có hiệu lực, khu vực tư nhân chính thức còn rất nhỏ |
| **civil** cưỡng chế ↔ dân sự | **−3** | MD đặt VIE ở `police_05`, **mức cao nhất**. Không có báo chí độc lập |
| **integ** hội nhập | **0** | Đã vào ASEAN 1995 và bình thường hóa với Mỹ 1995, nhưng chưa có BTA, chưa vào WTO |

---

## 3. Năm giai đoạn của Đổi Mới và hồ sơ trục

**[SỰ KIỆN]** Chia theo mốc có thật, rồi cộng hiệu ứng trục của các focus bị khóa theo năm trong từng khoảng. **Không tinh chỉnh gì** — đây là kết quả thô:

| Giai đoạn | Focus | Trục chuyển mạnh nhất | Có khớp lịch sử không |
|---|---|---|---|
| **1. 2000–2006** Hội nhập và luật chơi thị trường | 82 | `integ +38`, `merit +33`, `decent +11`, `market +9` | **Khớp.** BTA 2001, Luật Doanh nghiệp, Luật Đầu tư chung 2005, Luật PCTN 2005, PAR 2001–2010, chuẩn bị WTO |
| **2. 2007–2010** Vào WTO rồi vấp | 14 | `integ +7`, `merit +4`, **`market −2`** | **Khớp, và đây là chỗ đáng chú ý.** Trục thị trường **đi lùi** — đúng với thời kỳ tập đoàn kinh tế nhà nước, Vinashin, và lạm phát 2008 |
| **3. 2011–2015** Tái cơ cấu và HD-981 | 13 | `integ +9`, **`checks +4`**, `civil +1` | **Khớp.** Hiến pháp 2013, Luật Biển 2012, tái cơ cấu ba trọng tâm |
| **4. 2016–2020** Đốt lò và thắt chặt | 19 | `merit +7`, **`civil −6`**, `west +5` | **Khớp.** Chống tham nhũng mạnh lên **đồng thời** Luật An ninh mạng 2018 và Lực lượng 47 siết không gian mạng. Hai chiều ngược nhau cùng lúc |
| **5. 2021–2026** Tinh gọn và Kỷ nguyên vươn mình | 26 | `integ +13`, **`decent −7`**, `market +6`, **`size −5`** | **Khớp.** Sáp nhập tỉnh, bỏ cấp huyện, hợp nhất bộ — vừa thu nhỏ bộ máy vừa **tập trung** quyền lực. Nghị quyết 68 đẩy thị trường |

**[HỌC THUẬT]** Ba chỗ mô hình nói đúng điều mà một thiết kế "chọn ý thức hệ" sẽ bỏ sót:

- **Giai đoạn 2, thị trường đi lùi.** Hội nhập và tự do hóa **không** đi cùng nhau. Vào WTO xong, Việt Nam lập tập đoàn kinh tế nhà nước. Đây là ca ràng buộc ngân sách mềm của Kornai, xảy ra thật.
- **Giai đoạn 4, hai chiều ngược nhau.** Chất lượng bộ máy tăng **cùng lúc** quyền dân sự giảm. Chống tham nhũng và siết kiểm soát là hai mặt của cùng một chiến dịch, không phải hai lựa chọn loại trừ.
- **Giai đoạn 5, tinh gọn là tập trung.** Bộ máy nhỏ đi nhưng quyền lực **tập trung hơn**, không phân tán hơn. `size` và `decent` cùng âm.

---

## 4. Bảng ánh xạ

**[SỰ KIỆN]** File `D:\HOI4Mods\_gen\axis_map.py`. Đã kiểm: **mọi ID đều tồn tại trong mod**, không có ID sai.

| | |
|---|---|
| Focus thân lịch sử | 197 |
| Đã gán hiệu ứng trục | **167 (85%)** |
| Chưa gán | 30 |

**30 focus chưa gán** là các focus thuần kết quả, không phải lựa chọn thể chế: mốc thu nhập (`upper_middle_income`, `high_income_2045`), môi trường (`forest_protection`, `plastic_waste`), văn hóa thể thao (`sea_games_bid`, `heritage_preservation`), vệ tinh và chip (`vinasat`, `chip_design`). **[TIỀN ĐỀ KỊCH BẢN]** Để trống là đúng — không phải focus nào cũng phải đẩy trục, nếu không mô hình thành nhiễu.

**Quy tắc gán đã dùng:**

1. **Biên độ 1 / 2 / 3** — nhỏ, vừa, lớn. Không có 4 trở lên.
2. **Một focus tối đa 3 trục.** Nếu phải gán 4 thì focus đó mơ hồ, nên xem lại.
3. **Capstone đọc trục, không đẩy trục** — trừ `era_of_rising`, xem dưới.
4. **Cùng một cải cách có thể đẩy hai trục ngược nhau.** `two_tier_local_gov`: `size −2` và `decent −1`. Bỏ cấp huyện làm xã mạnh hơn nhưng giảm số đầu mối trung gian.
5. **Hiệu ứng theo bản chất thể chế, không theo tên.** `VIE_party_inspection` (Ủy ban Kiểm tra TƯ) cho `merit +1` nhưng `checks −1`: đó là trách nhiệm giải trình **dọc** trong Đảng, không phải kiểm soát **ngang** theo nghĩa O'Donnell.

**Một ngoại lệ có chủ ý:** `era_of_rising` được gán `checks −2, size −1` dù là capstone. **[SỰ KIỆN]** Căn cứ là ISEAS 2026/29: hợp nhất Tổng Bí thư và Chủ tịch nước đưa mô hình lãnh đạo sang dạng "hạt nhân", và tác giả cảnh báo hệ thống yếu kiểm soát ngang khó xử lý đánh đổi và khó tiếp thu phản hồi. Capstone của giai đoạn 5 phải phản ánh điều đó, nếu không mô hình sẽ nói dối về thời kỳ hiện tại.

---

## 5. Kiểm chứng: đi hết thân lịch sử thì ra nhà nước nào

**[SỰ KIỆN]** Cộng tất cả, bỏ các lựa chọn loại trừ nhau:

| Trục | Tổng thô | Trần dương | Trần âm | Chuẩn hóa −10…+10 |
|---|---|---|---|---|
| size | −3 | +6 | −12 | **+2** (nhỏ hơn một chút) |
| merit | +48 | +50 | 0 | **+10** (kịch trần) |
| decent | +6 | +15 | −10 | **+4** |
| checks | +6 | +16 | −8 | **+4** |
| market | +17 | +38 | −19 | **+4** |
| civil | −12 | +2 | −11 | **−11** (kịch trần âm) |
| integ | +75 | +77 | −2 | **+10** (kịch trần) |
| west | +22 | +22 | 0 | **+10** |
| mob | +4 | +4 | 0 | +10 |

**[HỌC THUẬT] Đối chiếu với Việt Nam thật 2026:**

| Trục | Mô hình nói | Thực tế | |
|---|---|---|---|
| integ kịch trần | Hội nhập tối đa | Thương mại trên GDP thuộc nhóm cao nhất thế giới; 17 FTA | ✅ |
| civil kịch trần âm | Cưỡng chế rất mạnh | V-Dem closed autocracy; `police_05` | ✅ |
| market chỉ +4 | Vẫn nhiều nhà nước | Kinh tế nhà nước vẫn giữ vai trò chủ đạo theo Hiến pháp | ✅ |
| size +2 | Bộ máy thu nhỏ nhẹ | Đang giảm 20% biên chế nhưng vẫn 7,9% lực lượng lao động | ✅ |
| checks +4 | Ràng buộc tăng nhẹ | Quốc hội mạnh hơn 2000, nhưng 2026 đi lùi | ✅ hợp lý |
| **merit kịch trần** | Bộ máy chất lượng cao | `corruption_level` thực tế **vẫn cao**; PAPI cải thiện chậm | ❌ **Mô hình nói quá** |

**[TIỀN ĐỀ KỊCH BẢN] Chỗ sai duy nhất, và cách sửa:** trục `merit` quá dễ lên vì có **25 focus** cùng đẩy nó lên và **không focus nào** kéo xuống. Sửa không phải bằng cách giảm con số, mà bằng cách gắn **cái giá của Geddes**: mỗi lần `merit` tăng thì mất một ít opinion của `communist_cadres` và một ít ổn định. Cải cách công vụ tước đi nguồn lực mua liên minh — đó là lý thuyết, và nó biến trục một chiều thành trục có đánh đổi.

---

## 6. Vấn đề thật: trục nào là lựa chọn, trục nào không

**[SỰ KIỆN]** Đây là phát hiện quan trọng nhất của bước 6.

| Trục | Số focus đẩy lên | Số focus kéo xuống | Có phải lựa chọn không |
|---|---|---|---|
| **market** | nhiều | nhiều (`state_conglomerates −3`, `petrovietnam −2`…) | **Có** — trục tốt nhất |
| **decent** | 15 điểm | 10 điểm | **Có** |
| **checks** | 16 điểm | 8 điểm | **Có** |
| **size** | 6 điểm | 12 điểm | **Có**, lệch một chiều |
| **civil** | chỉ 2 điểm | 11 điểm | **Gần như không** |
| **merit** | 50 điểm | **0** | **Không** |
| **integ** | 77 điểm | chỉ 2 điểm | **Không** |

Ba trục cuối chỉ có một chiều đi. **[HỌC THUẬT]** Và điều đó **đúng về mặt lịch sử** — Việt Nam 2000–2026 thực sự chỉ đi một chiều trên cả ba: hội nhập ngày càng sâu, chống tham nhũng ngày càng mạnh, kiểm soát không gian mạng ngày càng chặt. Nếu cho người chơi "chọn không hội nhập" trong thân lịch sử thì đó không còn là lịch sử.

**Vậy vấn đề không phải mô hình sai, mà là: lựa chọn không nằm ở thân lịch sử.**

---

## 7. Bốn cách tạo lựa chọn thật mà không phá lịch sử

**[TIỀN ĐỀ KỊCH BẢN]**

### 7.1 Khan hiếm thời gian — đã có sẵn, chưa được dùng

**[SỰ KIỆN]** Toàn bộ nội dung lịch sử tốn **45 năm** thời gian focus, và một ván 2000–2045 có đúng **45 năm**. Người chơi **không thể lấy hết**. Mỗi focus lịch sử bỏ qua là một điểm trục không được cộng.

Đây là cơ chế lựa chọn **mạnh nhất và đã tồn tại**, nhưng hiện vô hình. Chỉ cần làm cho nó **nhìn thấy được**: hiển thị cấu hình trục để người chơi biết mình đang đánh đổi cái gì khi bỏ qua một nhánh.

### 7.2 Giá của mỗi bước — biến trục một chiều thành trục có giá

Ba trục một chiều đều có cái giá trong literature:

| Trục | Cái giá | Nguồn |
|---|---|---|
| `merit` | Mất công cụ bảo trợ → giảm opinion `communist_cadres`, giảm ổn định | Geddes (1994) *Politician's Dilemma* |
| `integ` | Tăng phụ thuộc bên ngoài, dễ tổn thương trước cú sốc; và **linkage tạo áp lực thể chế** | Kuik (2008); Levitsky & Way (2010) |
| `civil` âm | Bộ máy cưỡng chế mạnh lên thì **tự nó thành mối đe dọa**; và giảm khả năng tiếp thu phản hồi | Greitens (2016); ISEAS 2026/29 |

Không cần đổi hướng, chỉ cần **mỗi điểm trục đều có hóa đơn**.

### 7.3 Sáu cặp loại trừ đã có, giữ nguyên

**[SỰ KIỆN]** Thân lịch sử đã có 6 focus loại trừ nhau: xây ↔ gác điện hạt nhân, pháp lý biển ↔ khẳng định chủ quyền, ngả Trung Quốc ↔ ngả phương Tây. Cả ba cặp đều gắn với **điểm quyết định có thật** — đúng nguyên tắc của plan v6. **Không thêm cặp loại trừ mới vào thân lịch sử**, vì làm vậy sẽ bịa ra ngã rẽ không có thật.

### 7.4 Quyết định lặp lại — chỗ duy nhất nên thêm cơ chế mới

**[SỰ KIỆN]** Mod đã có `VIE_military_readiness_category` với 6 quyết định lặp lại, có `days_re_enable` và chi phí PP/ngân khố. Mẫu này chạy được.

**[TIỀN ĐỀ KỊCH BẢN]** Một danh mục song song — tạm gọi "Xây dựng nhà nước" — cho phép người chơi **chủ động đẩy một trục** ngoài dòng lịch sử, với chi phí thật và thời gian chờ. Ví dụ về dạng thức, chưa phải danh sách cuối:

- Đợt thi tuyển công chức cạnh tranh: `merit +1`, tốn PP, giảm opinion cán bộ
- Giao quyền cho tỉnh thí điểm: `decent +1`, tăng chênh lệch vùng
- Nâng mức luật bộ máy: đổi `bureau_law`, tốn ngân sách thường xuyên
- Nới kiểm soát nội dung: `civil +1`, giảm ổn định ngắn hạn

Đây là chỗ **nên** thêm cơ chế, vì nó cho lựa chọn mà không đụng vào tính lịch sử của cây.

---

## 8. Chuẩn hóa và hiển thị

**[TRỪU TƯỢNG GAMEPLAY]**

- **Chuẩn hóa:** giá trị hiển thị = `round(10 × tổng / trần cùng dấu)`, cho mọi trục nằm trong −10…+10 và so sánh được với nhau. Biến thô vẫn lưu nguyên để tính điều kiện.
- **Hiển thị:** một mục trong danh sách modifier quốc gia, đúng như `VIE_armed_forces_modifier` đang làm. Bảy dòng, mỗi dòng một trục, kèm tên hai cực.
- **Không** làm GUI riêng, **không** thêm power balance (MD tối đa 3, VIE đã dùng hết 3).

---

## 9. Việc chưa làm và chỗ cần kiểm chứng

1. **Chưa gán trục cho dải chế độ (159 focus).** Đó là STEP 7.
2. **Chưa gán trục cho nhánh quân sự (133 focus).** Theo nguyên tắc mục XIII của bạn, quân sự nối vào `decent` (dân quân), `market` (công nghiệp quốc phòng), `integ` (nội địa hóa) — nhưng chưa làm.
3. **Ngưỡng cho điều kiện mở nhánh chưa có số.** Cần chốt ở STEP 8.
4. **Chưa kiểm `merit` sau khi thêm cái giá của Geddes** — phải chạy lại mô phỏng.
5. **30 focus chưa gán** cần rà lại một lượt xem có cái nào thực sự nên có trục không.
6. **Chưa thử đổi `bureau_law` bằng focus trong game** — nợ từ STEP 5, và nó chặn mục 7.4.

---

## Nguồn mới dùng ở bước này

Geddes (1994) *Politician's Dilemma*; Kornai (1986) "The Soft Budget Constraint"; O'Donnell (1998) về trách nhiệm giải trình ngang; Greitens (2016); Kuik (2008); Levitsky & Way (2010).

Dữ liệu Việt Nam: [ISEAS Perspective 2025/14](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-14-vietnams-bureaucratic-reforms-opportunities-and-challenges-in-the-era-of-national-rise-by-nguyen-khac-giang/) · [ISEAS Perspective 2026/29](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2026-29-vietnams-reconfigured-leadership-personnel-and-power-in-the-new-era-by-nguyen-khac-giang/) · [PAPI](https://papi.org.vn/eng/) · [Chỉ số quản trị – Malesky, Duke](https://sites.duke.edu/malesky/governance-indices/) · [V-Dem Democracy Report 2025](https://v-dem.net/documents/54/v-dem_dr_2025_lowres_v1.pdf).

Dữ liệu mod: `D:\HOI4Mods\_gen\axis_map.py` (167 ánh xạ, đã kiểm ID), `D:\HOI4Mods\_gen\trunk_list2.txt` (197 focus kèm mốc năm).

---

## Bước 7: Ánh xạ khung vào toàn bộ nhánh hiện có

# Bước 7: Ánh xạ khung vào toàn bộ nhánh hiện có

> Tiếp theo STEP 1–6. Dữ liệu: **`D:\HOI4Mods\_gen\axis_map_mil_alt.py`** (quân sự + dải chế độ) bên cạnh `axis_map.py` (thân lịch sử).
> **Chưa** vẽ transition graph (STEP 8), **chưa** lên kế hoạch code (STEP 9).
>
> Nhãn: **[SỰ KIỆN]** · **[HỌC THUẬT]** · **[TIỀN ĐỀ KỊCH BẢN]**

---

## 0. Kết quả trong một đoạn

Gán xong hiệu ứng trục cho **152/159 focus dải chế độ (96%)** và **51/131 focus quân sự (39%)**. Kết quả quan trọng nhất: **mỗi dải chế độ có một "chữ ký trục" riêng biệt, và chữ ký đó khớp với thứ literature dự đoán** — mà tôi không hề tinh chỉnh để nó khớp. Tài phiệt lộ ra ở `merit −20`, Dân túy ở `mob +24`, Nhà nước An ninh ở `civil −16`. Đó là bằng chứng khung bảy trục mô tả đúng nội dung đã code.

Một phát hiện đi kèm: dải `developmental_state` có chữ ký `checks +17, merit +14` — nghĩa là nó **không phải** một dải "nhà nước kiến tạo", mà là một dải **kiến tạo rồi dân chủ hóa**. Đúng con đường Slater & Wong mà STEP 3 đã nêu.

---

## 1. Chữ ký trục của 19 dải chế độ

**[SỰ KIỆN]** Cộng hiệu ứng trục của từng thành phần liên thông, chỉ hiện trục có |giá trị| ≥ 3:

| Dải | Focus gán | Chữ ký trục | Literature dự đoán gì |
|---|---|---|---|
| `ol_bailout` Tài phiệt | 12/12 | **merit −20**, checks −9, civil −4, integ +3 | Evans: mất tự chủ bộ máy. **Đúng — và merit là con số duy nhất cần để nhận ra nó** |
| `np_street_mandate` Dân túy | 14/14 | **mob +24**, integ −11, civil −6, checks −4 | Mudde + Linz: huy động là đặc trưng phân biệt. **Đúng** |
| `lb_sez_law` Đặc khu | 12/13 | **market +26**, integ +12, decent +9 | Mô hình kinh tế + cấu hình lãnh thổ, không phải ý thức hệ. **Đúng** |
| `sec_cyber_control` An ninh | 8/8 | **civil −16**, integ −4 | Greitens: thiết kế bộ máy cưỡng chế. **Đúng** |
| `round_table_talks` Dân chủ hóa | 6/6 | **checks +16**, civil +9 | O'Donnell & Schmitter. **Đúng** |
| `developmental_state` Kiến tạo | 15/15 | **checks +17**, merit +14, civil +7 | **Không khớp nhãn.** Xem mục 2 |
| `wa_development_council` Hội đồng Phát triển | 15/15 | **west +10**, merit +9, integ +6, market −4, checks −4 | Độc đoán phát triển ngả Tây. **Đúng** |
| `defend_the_foundation` Bảo thủ | 6/6 | integ −9, market −8, civil −7 | Phái trong chế độ đảng trị, đóng cửa. **Đúng** |
| `mn_recall_royal_house` Quân chủ | 8/10 | checks +10, civil +3 | Quân chủ lập hiến = ràng buộc hành pháp. **Đúng** |
| `tc_strategic_autonomy` Tự chủ | 15/15 | integ −6, decent +5, market −4, west −3 | Định hướng đối ngoại + kinh tế. **Đúng** |
| `lh_ethnic_nationalism` Lạc Hồng | 3/3 | **mob +9, civil −9**, checks −3 | Paxton + Mann: huy động cộng bạo lực. **Đúng** |
| `national_salvation_council` Junta | 8/8 | checks −4, civil −4, market −3 | Geddes: quân sự **giải huy động** (mob −2). **Đúng** |
| `ng_technocratic_caretaker` Lâm thời | 6/6 | checks +5, civil +4, merit +3 | Chuyển tiếp, không phải đích đến. **Đúng** |
| `wk_workers_commune` Công xã | 2/3 | decent +6, market −3 | **Đúng** |
| `gr_green_coalition` Xanh | 7/9 | checks +3 | **Chữ ký quá yếu.** Xem mục 4 |
| 4 gói `dm_*` | 15/16 | mỗi gói một chữ ký kinh tế/xã hội nhẹ | Họ đảng, không phải chế độ. **Đúng** |

**[HỌC THUẬT]** Hai hàng đáng chú ý nhất:

- **Tài phiệt lộ ra bằng đúng một con số.** `merit −20` là chữ ký duy nhất cần thiết. Điều này biến luận điểm của Evans thành cơ chế: bạn không "chọn làm tài phiệt", bạn để chất lượng bộ máy sụp xuống và nó thành tài phiệt.
- **Junta có `mob −2`.** Đây là chỗ mô hình nói đúng một điều tinh tế: chế độ quân sự **dập** huy động quần chúng, khác hẳn dân túy. Geddes và Linz đều nhấn mạnh điểm này, và nó là lý do junta **chặn** đường tới Lạc Hồng chứ không dẫn tới đó.

---

## 2. Phát hiện: dải "Nhà nước kiến tạo" thực ra là dải dân chủ hóa

**[SỰ KIỆN]** Chữ ký của nó là `checks +17, merit +14, civil +7`. Trục tăng mạnh nhất **không phải** merit mà là **checks**.

Lý do: dải này trong code gồm 15 focus liền mạch, đi từ `developmental_state → technocrat_cabinet → meritocratic_service → judicial_reform → press_relaxation → front_coalition → vetted_elections → managed_pluralism`. Nghĩa là **phần kiến tạo chỉ chiếm 5 focus đầu**, 10 focus sau là mở rộng tham gia chính trị.

**[HỌC THUẬT]** Đây chính xác là lộ trình Slater & Wong (2013): đảng cầm quyền **xây năng lực trước, rồi nhượng bộ từ thế mạnh**. Mod đã code đúng lộ trình này từ lâu mà tài liệu gọi nó là "Nhà nước kiến tạo".

**[TIỀN ĐỀ KỊCH BẢN] Đề xuất:** đổi **tên gọi và cách hiểu**, không đổi ID và không tách dải. Dải này nên được mô tả là **"Kiến tạo và mở cửa chính trị"** — một con đường, hai giai đoạn. Năm focus đầu là lựa chọn xây dựng nhà nước dùng được ở mọi chế độ; mười focus sau là con đường dân chủ hóa từ thế mạnh.

---

## 3. Quân sự: trả lời mục XIII

**[SỰ KIỆN]** Chỉ **51/131 focus quân sự (39%)** có hiệu ứng trục. 80 focus còn lại là năng lực thuần túy — xe tăng, radar, tàu ngầm — **không có nội dung thể chế** và không nên gán gì.

**[TIỀN ĐỀ KỊCH BẢN] Trả lời câu hỏi của bạn:** các lựa chọn quân sự là **lựa chọn chính sách quốc phòng độc lập** — **không** khóa theo chế độ. Nhưng chúng **đẩy trục**, và trục mới quyết định chế độ nào với tới được. Đó là cách nối gián tiếp mà bạn yêu cầu, thay cho "ý thức hệ X → quân sự X".

51 focus có nội dung thể chế chia thành năm nhóm:

| Nhóm | Trục | Ví dụ |
|---|---|---|
| **Phòng thủ lãnh thổ và dân quân** | `decent +`, `mob +` | `path_peoples_war` (decent +3, mob +2), `army_dan_quan_modern`, `army_underground_bases` |
| **Chuyên nghiệp hóa** | `merit +`, `decent −` | `army_nco_corps`, các học viện, `army_c4isr` |
| **Viễn chinh** | `decent −`, `integ +` | `army_exp_brigades`, `army_intervention_force` (thêm `checks −1`) |
| **Nội địa hóa và công nghiệp quốc phòng** | `integ −`, `market −` | `def_supply_chain` (integ −2), `def_industry_2030` (integ −2, market −2), `z_factories` |
| **Răn đe hạt nhân giả định** | `integ −−`, `checks −` | `msl_minimum_deterrent` (integ −3, checks −2) |

**[HỌC THUẬT] Bằng chứng khung này đúng:** trục `decent` được đẩy **cùng lúc** bởi một lựa chọn quân sự (`path_peoples_war +3`) và một lựa chọn chế độ (`tc_self_management +2`) và một focus lịch sử (`VIE_decentralization +3`). Ba nguồn khác nhau hội tụ vào **cùng một chiều thể chế**. Đó là điều không thể làm được nếu gắn cứng quân sự vào ý thức hệ.

**Hệ quả cụ thể:** một nhà nước dân chủ vẫn chọn được phòng thủ lãnh thổ — nó chỉ làm `decent` tăng. Một nhà nước dân tộc chủ nghĩa vẫn chọn được từ chối biển. Một nhà nước kiến tạo kỹ trị vẫn xây được lực lượng viễn chinh, nhưng phải trả giá `checks −1`.

---

## 4. Bảng xử lý toàn bộ nhánh hiện có

**[TIỀN ĐỀ KỊCH BẢN]** Nguyên tắc: **không xóa focus nào**. Chỉ đổi nhãn, đổi điều kiện, hoặc mở rộng phạm vi sử dụng.

| Nhánh | Loại thật (STEP 2) | Giữ? | Xử lý đề xuất |
|---|---|---|---|
| `developmental_state` 15 | Mô hình quản trị **+** con đường dân chủ hóa | **Giữ** | Đổi tên hiểu thành "Kiến tạo và mở cửa chính trị". **Tách 5 focus đầu** (`technocrat_cabinet`, `meritocratic_service`, `judicial_reform`, `singapore_model`, `performance_legitimacy`) thành **lựa chọn dùng chung** cho mọi chế độ. Đổi điều kiện mở từ `VIE_bop_is_reformist` sang 3 điều kiện Doner–Ritchie–Slater |
| `tc_strategic_autonomy` 15 | Đối ngoại + kinh tế | **Giữ** | Không đổi cấu trúc. Điều kiện mở nên đọc `integ` thấp thay vì chỉ đọc cờ |
| `round_table_talks` 6 | **Cơ chế chuyển đổi** | **Giữ** | **Hai lối vào, hai hệ quả:** từ `managed_pluralism` (nhượng bộ từ thế mạnh → ổn định) và từ Collapse (thay thế → bất ổn, `merit` bị phạt) |
| `defend_the_foundation` 6 | Phái trong chế độ đảng trị | **Giữ** | Mô tả lại là **cấu hình**, không phải "chế độ khác" |
| `wa_development_council` 15 | Chế độ **+** nội dung kinh tế trùng lặp | **Giữ chế độ** | **Gộp phần kinh tế** (`wa_five_year_plans`, `wa_national_champions`, `wa_heavy_industry`, `wa_export_drive`, `wa_technical_education`) vào lựa chọn kiến tạo dùng chung, để không viết chính sách công nghiệp ba lần |
| `np_street_mandate` 14 | Ý thức hệ mỏng + huy động | **Giữ** | Là bản lề B4 → A. Điều kiện mở nên đọc `mob` thay vì chỉ đọc cờ HD-981 |
| `lh_ethnic_nationalism` 3 | **Điểm thoái hóa** | **Giữ nguyên** | Thêm điều kiện cấu trúc: cần ít nhất hai trong ba — khủng hoảng chính danh, tinh hoa ly khai, rạn độc quyền bạo lực |
| `sec_cyber_control` 8 | Chế độ **+** thiết kế bộ máy an ninh | **Giữ chế độ** | Nội dung thiết kế bộ máy an ninh nên **dùng được ở chế độ khác** với mức độ nhẹ hơn |
| `ol_bailout` 12 | **Cấu trúc tinh hoa** | **Giữ** | Điều kiện mở đổi thành **`merit` dưới ngưỡng + tham nhũng cao + faction `oligarchs`**, thay cho cờ khủng hoảng ngân hàng đơn thuần |
| `lb_sez_law` 13 | Mô hình kinh tế + lãnh thổ | **Giữ** | Là đường dẫn tới Tài phiệt khi `merit` không theo kịp `market` |
| `national_salvation_council` 8 | **Chế độ thật** (quân sự) | **Giữ** | Giữ `mob −2` — junta dập huy động, đây là điều phân biệt nó với dân túy |
| `ng_technocratic_caretaker` 6 | **Cơ chế chuyển tiếp** | **Giữ** | **Gắn thời hạn.** Chính phủ lâm thời không nên là trạng thái vĩnh viễn |
| `mn_recall_royal_house` 10 | Chế độ thật (quân chủ) | **Giữ** | Kết cục hiếm, không cần sửa |
| `gr_green_coalition` 9 | **Họ đảng / định hướng chính sách** | **Hạ cấp** | Chữ ký trục quá yếu (`checks +3`) để là một chế độ. Nên thành **gói chính sách môi trường dùng chung** cộng một gói đảng trong dân chủ |
| `wk_workers_commune` 3 | Kết cục nội chiến | **Giữ** | Không sửa |
| 4 gói `dm_*` 16 | **Họ đảng cầm quyền** | **Giữ** | **Không gói nào quy định đối ngoại.** Trục `west` phải chọn riêng |

---

## 5. Cái gì nên là event, cái gì nên là lựa chọn, cái gì nên là thoái hóa

**[TIỀN ĐỀ KỊCH BẢN]** Theo nguyên tắc plan v6 — *focus là thứ người chơi chọn, event là thứ xảy ra*:

### Nên chuyển thành event (hệ quả, không phải lựa chọn)

| Khái niệm | Vì sao |
|---|---|
| **Hóa đơn đến hạn** của mỗi cấu hình | Người chơi không chọn hậu quả. `merit` thấp lâu → event bê bối; `integ` cao + cú sốc bên ngoài → event khủng hoảng chuỗi cung ứng; `civil` rất âm → event bộ máy an ninh tự tung tự tác |
| **Bị bắt cóc bởi tài phiệt** | Winters: là kết quả của động lực, không phải quyết sách. Khi `merit` xuống dưới ngưỡng, event tự bắn |
| **Rạn nứt cứng rắn ↔ mềm dẻo** | O'Donnell & Schmitter: chuyển đổi bắt đầu từ rạn nứt nội bộ, không từ một nút bấm |
| **Bộ máy cưỡng chế thành mối đe dọa** | Greitens: hệ quả cấu trúc của việc tập trung hóa an ninh |

### Nên thành lựa chọn xây dựng nhà nước dùng chung

`technocrat_cabinet`, `meritocratic_service`, `judicial_reform`, `singapore_model`, nhóm kinh tế kiến tạo của `wa_*`, thiết kế bộ máy an ninh của `sec_*`, chủ nghĩa dân tộc kinh tế của `tc_*` và `np_*`. **[SỰ KIỆN]** Đây đúng là các nhóm trùng lặp mà STEP 1 đã đo được.

### Nên là đường thoái hóa, không phải cửa vào

Lạc Hồng (đã đúng), Tài phiệt (cần đổi điều kiện), Collapse (đã đúng).

---

## 6. Những thứ không nên làm

1. **Không xóa dải nào** vì phân loại thay đổi. Kể cả `gr_green_coalition` bị hạ cấp vẫn giữ nguyên 9 focus.
2. **Không gắn cứng quân sự vào chế độ.** Bằng chứng ở mục 3 cho thấy nối gián tiếp qua trục hoạt động tốt hơn.
3. **Không viết lại nội dung trùng lặp thành focus mới.** Gộp bằng cách cho dùng chung, không bằng cách xóa rồi viết lại.
4. **Không cho gói đảng dân chủ quy định đối ngoại.** Ấn Độ và Indonesia là dân chủ không liên kết.
5. **Không biến 80 focus quân sự thuần năng lực thành có trục.** Gán bừa sẽ làm nhiễu mô hình.
6. **Không thêm power balance.** MD tối đa 3, VIE đã dùng hết.

---

## 7. Còn thiếu

| Việc | Trạng thái |
|---|---|
| 7 focus dải chế độ chưa gán | Chủ yếu là capstone và focus trang trí — cần rà một lượt |
| Ngưỡng cụ thể cho từng điều kiện mở nhánh | **Chưa có số.** Là việc của STEP 8 |
| Cái giá của Geddes cho trục `merit` | Đã thiết kế ở STEP 6, chưa đưa vào file dữ liệu |
| Chữ ký của Xanh quá yếu | Cần quyết: hạ cấp hay bổ sung nội dung |
| Thử đổi `bureau_law` bằng focus trong game | **Vẫn nợ từ STEP 5**, chặn phần quyết định lặp lại |
| Literature quan hệ dân sự – quân sự Việt Nam | **Vẫn nợ từ STEP 3**, cần cho ngưỡng của junta |

---

## Nguồn

Evans (1995) *Embedded Autonomy*; Winters (2011) *Oligarchy*; Mudde (2004); Linz (2000); Geddes, Wright & Frantz (2014); Greitens (2016); O'Donnell & Schmitter (1986); Slater & Wong (2013); Paxton (2004); Mann (2004); Doner, Ritchie & Slater (2005); Kuik (2008); Levitsky & Way (2010).

Dữ liệu mod: `D:\HOI4Mods\_gen\axis_map.py` (167 ánh xạ thân lịch sử), `D:\HOI4Mods\_gen\axis_map_mil_alt.py` (51 quân sự + 152 dải chế độ). Mọi ID đã kiểm, không có ID sai.

---

## Bước 8: Đồ thị chuyển chế độ với ngưỡng cụ thể

# Bước 8: Đồ thị chuyển chế độ với ngưỡng cụ thể

> Tiếp theo STEP 1–7. Đây là bước chốt **con số**, thứ đã bị treo từ STEP 5. **Chưa** lên kế hoạch code (STEP 9).
>
> Nhãn: **[SỰ KIỆN]** · **[HỌC THUẬT]** · **[TIỀN ĐỀ KỊCH BẢN]**

---

## 0. Kết quả trong một đoạn

Chốt được thang chuẩn hóa, **vân tay của con đường lịch sử**, và **ngưỡng cho 11 cạnh chuyển chế độ**. Phép thử quan trọng nhất đã chạy: **một người chơi đi hết con đường lịch sử không tự động mở nhánh chế độ nào** ngoài nhánh Kiến tạo — và nhánh đó vẫn bị chặn thêm bởi hai điều kiện ngoài trục. Mọi nhánh khác đòi hỏi người chơi **cố ý lệch khỏi lịch sử**, và lệch bao nhiêu thì đo được.

---

## 1. Thang chuẩn hóa

**[TIỀN ĐỀ KỊCH BẢN]** Mỗi trục quy về **−10…+10**, chia theo phạm vi đạt được **khi chưa vào dải chế độ nào** — tức là những gì người chơi làm được bằng thân lịch sử cộng nhánh quân sự. Cách chia này có lý do: ngưỡng là để **mở cửa vào** dải, nên phải đo bằng thứ đạt được **trước khi** vào.

| Trục | Tối đa dương | Tối đa âm | SPAN dùng để chia |
|---|---|---|---|
| size quy mô bộ máy | +6 | −12 | 12 |
| merit chất lượng bộ máy | +59 | 0 | 59 |
| decent phân cấp | +24 | −15 | 24 |
| checks ràng buộc | +19 | −15 | 19 |
| market thị trường | +41 | −40 | 41 |
| civil quyền dân sự | +5 | −14 | 14 |
| integ hội nhập | +98 | −26 | 98 |
| mob huy động | +12 | 0 | 12 |
| west linkage phương Tây | +29 | −6 | 29 |

`giá trị hiển thị = round(10 × thô / SPAN)`, cắt ở ±10.

**[HỌC THUẬT]** Hai trục có phạm vi rất lệch — `merit` và `integ` chỉ đi một chiều, đúng như STEP 6 đã phát hiện. Điều đó không phải lỗi thang đo mà là đặc điểm thật của lịch sử Việt Nam 2000–2026.

---

## 2. Vân tay của con đường lịch sử

**[SỰ KIỆN]** Đi hết thân lịch sử và nhánh quân sự, không rẽ nhánh nào:

| merit | integ | west | civil | mob | decent | checks | size | market |
|---|---|---|---|---|---|---|---|---|
| **+10** | **+7** | **+8** | **−10** | +5 | +4 | +3 | −2 | 0 |

Đọc bằng lời: **bộ máy được làm sạch tới mức tối đa, hội nhập rất sâu và nghiêng phương Tây, quyền dân sự bị siết gần kịch trần, năng lực huy động quần chúng cao nhưng do nhà nước kiểm soát, phân cấp và ràng buộc quyền lực nhích lên một chút, nhà nước và thị trường cân bằng.**

**[HỌC THUẬT]** Đây là một mô tả trung thực về Việt Nam 2026, và nó rơi ra từ mô hình chứ không được đặt vào.

**Một lưu ý về `mob`:** giá trị +5 không có nghĩa là đường phố sôi sục. Nó đo **năng lực huy động có tổ chức** — Mặt trận, dân quân tự vệ, đoàn thanh niên, hội cựu chiến binh. Theo Linz, thứ nguy hiểm không phải huy động mà là **huy động ngoài tầm kiểm soát của nhà nước**. Vì vậy `mob` cao chỉ thành nguy hiểm khi đi kèm `checks` thấp và một sự kiện làm mất kiểm soát. Đó là điều kiện ghép, không cần thêm biến.

---

## 3. Đồ thị chuyển

**[TIỀN ĐỀ KỊCH BẢN]** Sửa lại bản nháp ở mục XIV của bạn theo kết quả STEP 3 và STEP 7:

```
                     ĐỔI MỚI TIẾP TỤC  (slot 19, closed autocracy)
                                │
                 ─── vùng cấu hình B1/B2 ───
            (tự chủ chiến lược + phát triển chủ nghĩa dân tộc;
                     KHÔNG đổi chế độ, vẫn slot 19)
                                │
      ┌──────────────┬──────────┼───────────┬──────────────┐
      │              │          │           │              │
  market thấp    merit cao   mob cao    civil rất thấp  market cao
  integ thấp     + tổn thương + checks    + checks thấp   + decent cao
      │          hệ thống      thấp          │              │
      ▼              ▼          ▼            ▼              ▼
  BẢO THỦ (4)   KIẾN TẠO (19)  DÂN TÚY(20)  AN NINH (7)  ĐẶC KHU (16)
                     │             │                          │
              merit≥7,civil≥−6     │                    merit không
              checks≥5             │                    theo kịp market
                     │      ┌──────┴──────┐                   │
                     ▼      ▼             ▼                   ▼
            ĐA ĐẢNG CÓ   JUNTA (22)   LẠC HỒNG (21)      TÀI PHIỆT (15)
            KIỂM SOÁT     mob≥9        mob≥9, checks≤−5        │
                     │    quân đội     + 2/3 điều kiện    merit tiếp tục
                     ▼    can thiệp      cấu trúc          sụp đổ
              DÂN CHỦ (1/2/14/18)  │           │                │
              — lối vào "thế mạnh" │           ▼                ▼
                                   │      thoái hóa thành  ┌─────────┐
                     ┌─────────────┘      độc đoán thường  │ SỤP ĐỔ  │
                     ▼                                     └────┬────┘
            HỘI ĐỒNG PHÁT TRIỂN (0)                             │
            west≥6, merit≥5, checks≤−4              ┌───────┬────┴───┬────────┐
                     │                              ▼       ▼        ▼        ▼
                     ▼ "khoảnh khắc 1987"        JUNTA  QUÂN CHỦ  DÂN CHỦ  ĐOÀN KẾT
              DÂN CHỦ — lối vào "thế mạnh"                       (lối vào
                                                                 "thay thế",
                                                                  bị phạt)
```

**Ba quy luật, đều rút từ literature:**

1. **Không có cạnh nào đi thẳng từ Đổi Mới tới Lạc Hồng.** Chỉ tới được qua Dân túy, và Dân túy đòi `mob ≥ 7` mà con đường lịch sử chỉ đạt +5.
2. **Vùng B1/B2 không phải một nút.** Tự chủ chiến lược và phát triển chủ nghĩa dân tộc **không đổi chế độ** — chúng là cấu hình. Đây là sửa lớn nhất so với bản nháp của bạn.
3. **Dân chủ có hai lối vào, hai hệ quả.** "Nhượng bộ từ thế mạnh" (Slater & Wong) đi qua Đa đảng có kiểm soát; "thay thế" (O'Donnell & Schmitter) đi qua Sụp đổ và **bị phạt**.

---

## 4. Ngưỡng cho từng cạnh

**[TIỀN ĐỀ KỊCH BẢN]** Điều kiện trục **cộng thêm** cửa event hiện có, không thay thế nó. Cờ vẫn là điều kiện cần; trục là điều kiện đủ.

| Cạnh | Điều kiện trục | Điều kiện ngoài trục | Cơ sở |
|---|---|---|---|
| → **Bảo thủ** (4) | `market ≤ −2` **và** `integ ≤ +3` | Cửa D1 Đại hội IX, BoP phía bảo thủ | Đóng cửa kinh tế là dấu hiệu nhận biết, không phải khẩu hiệu |
| → **Kiến tạo** (19) | `merit ≥ +4` | **Đe dọa bên ngoài** cao **và** ngân khố eo hẹp **và** cần chính danh quần chúng | Doner, Ritchie & Slater (2005): kiến tạo bị ép ra đời |
| → **Tự chủ** (19) | `integ ≤ +4` **và** `west ≤ +4` | Cửa D4 HD-981, phản ứng cứng rắn | Kuik (2008) |
| → **Dân túy** (20) | `mob ≥ +7` **và** `checks ≤ 0` | Cửa D4, để đường phố dẫn dắt | Mudde (2004); Levitsky & Loxton (2013) |
| → **An ninh** (7) | `civil ≤ −8` **và** `checks ≤ −2` | Cửa D3 khủng hoảng trật tự | Greitens (2016) |
| → **Đặc khu** (16) | `market ≥ +5` **và** `decent ≥ +3` | Cửa D6 Luật Đặc khu 2018 | — |
| → **Tài phiệt** (15) | `merit ≤ +2` **và** `market ≥ +3` | `corruption_level ≥ 07`, faction `oligarchs` đã có | Evans (1995): mất tự chủ; Winters (2011) |
| → **Đa đảng có kiểm soát → Dân chủ** | `merit ≥ +7` **và** `civil ≥ −6` **và** `checks ≥ +5` | Tăng trưởng tốt, đảng còn tự tin | **Slater & Wong (2013): nhượng bộ từ thế mạnh** |
| → **Junta** (22) | `mob ≥ +9` | Quân đội can thiệp (đã có `vie_alt.15.a`) | Geddes et al.: quân sự **giải huy động** |
| → **Lạc Hồng** (21) | `mob ≥ +9` **và** `checks ≤ −5` | **Ít nhất 2 trong 3:** khủng hoảng chính danh đang hoạt động · một bộ phận tinh hoa đã ly khai · độc quyền bạo lực đã rạn | Paxton giai đoạn 3; Mann (2004) |
| → **Hội đồng Phát triển** (0) | `west ≥ +6` **và** `merit ≥ +5` **và** `checks ≤ −4` | Đã ở Junta hoặc An ninh, hoặc đã `pivot_to_the_west` | Mô hình Park Chung-hee: kiến tạo **cộng** độc đoán |

**[HỌC THUẬT] Hai ngưỡng đáng giải thích:**

- **Tài phiệt đòi `merit ≤ +2`** trong khi lịch sử đạt `+10`. Nghĩa là người chơi phải **chủ động bỏ gần hết nội dung chống tham nhũng** trong suốt 25 năm. Đó đúng là điều kiện: đầu sỏ không phải thứ bạn chọn, nó là thứ xảy ra khi bạn không xây bộ máy.
- **Hội đồng Phát triển đòi `checks ≤ −4`.** Tôi thêm điều kiện này sau khi chạy thử: nếu chỉ đòi `west` và `merit` thì con đường lịch sử tự động mở nó, mà điều đó sai — Hội đồng Phát triển là chế độ **độc đoán** phát triển, nên phải phá kiểm soát ngang mới vào được.

---

## 5. Kiểm chứng: con đường lịch sử mở được gì

**[SỰ KIỆN]** Chạy vân tay lịch sử qua toàn bộ bảng ngưỡng:

| Nhánh | Kết quả | Vì sao |
|---|---|---|
| Bảo thủ | **đóng** | `integ +7` vượt xa ngưỡng ≤ +3 |
| **Kiến tạo** | **mở** | `merit +10 ≥ +4` — nhưng vẫn cần ba điều kiện tổn thương hệ thống |
| Tự chủ | **đóng** | `integ +7` và `west +8` đều quá cao |
| Dân túy | **đóng** | `mob +5 < +7`, và `checks +3 > 0` |
| An ninh | **đóng** | `civil −10` đủ, nhưng `checks +3 > −2` |
| Đặc khu | **đóng** | `market 0 < +5` |
| Tài phiệt | **đóng** | `merit +10` cách ngưỡng ≤ +2 rất xa |
| Dân chủ từ thế mạnh | **đóng** | `civil −10 < −6`: phải **cố ý nới kiểm soát** mới vào được |
| Lạc Hồng | **đóng** | thiếu cả `mob` lẫn `checks` |
| Junta | **đóng** | `mob +5 < +9` |
| Hội đồng Phát triển | **đóng** | `checks +3 > −4` |

**[HỌC THUẬT]** Kết quả này là thứ cần đạt: **10 trên 11 nhánh đóng**, và nhánh duy nhất mở là nhánh mà lịch sử thật cũng có xu hướng đi tới. Người chơi muốn nhánh khác phải trả giá bằng việc **bỏ bớt nội dung lịch sử** — và vì toàn bộ nội dung lịch sử đã chiếm trọn 45 năm của một ván 2000–2045, bỏ bớt là có thật, không phải tượng trưng.

Đáng chú ý: hàng **Dân chủ từ thế mạnh** đóng vì `civil`. Người chơi đã xây một bộ máy sạch và giàu, nhưng vẫn phải **chủ động nới kiểm soát** mới mở được cửa. Đó đúng là điều Przeworski và O'Donnell mô tả: tự do hóa là một quyết định riêng, không phải hệ quả tự động của phát triển.

---

## 6. Cạnh thất bại và đảo ngược

**[HỌC THUẬT]** STEP 3 đã chỉ ra literature nói kết cục **phổ biến nhất** của cả A lẫn C là "nửa chừng", không phải cực đoan. Bốn cạnh sau hiện **chưa có trong code**:

| Cạnh | Điều kiện | Cơ sở |
|---|---|---|
| **Lạc Hồng → độc đoán thường** | Sau N năm không chiến tranh lớn, `mob` tụt dưới ngưỡng | Paxton giai đoạn 5: mất năng lượng cách mạng, thành chế độ bảo thủ bình thường |
| **Dân chủ hóa dừng ở độc đoán cạnh tranh** | Vào được Đa đảng có kiểm soát nhưng `merit` hoặc `checks` không đạt ngưỡng | Levitsky & Way: đây là kết cục phổ biến nhất |
| **Kiến tạo → Tài phiệt** | `market` tăng nhanh hơn `merit`, khoảng cách vượt một ngưỡng | **Evans (1995): gắn kết cao mà tự chủ thấp thì bị bắt cóc.** Đây là cạnh quan trọng nhất còn thiếu |
| **Bất kỳ → Sụp đổ** | Stability dưới ngưỡng, ≥2 khủng hoảng, trục ở cực | Đã có trong plan v6, chưa nối vào trục |

**[TIỀN ĐỀ KỊCH BẢN]** Cạnh thứ ba đáng làm nhất. Nó biến toàn bộ luận điểm Evans thành một luật chơi: *nếu bạn mở thị trường nhanh hơn tốc độ xây bộ máy, bạn không được nhà nước kiến tạo, bạn được tài phiệt.* Và nó giải thích vì sao Đặc khu dẫn tới Tài phiệt — Đặc khu cho `market +26` mà không cho `merit` điểm nào.

---

## 7. Thay đổi so với code hiện tại

**[SỰ KIỆN]** Hiện nay 16 gốc dải mở bằng cờ do event đặt (`VIE_developmental_unlocked`, `VIE_oligarch_unlocked`…), không đọc gì khác.

**[TIỀN ĐỀ KỊCH BẢN]** Thay đổi là **thêm vào `available`**, không xóa cờ:

```
available = {
    has_country_flag = VIE_oligarch_unlocked      # giữ nguyên: cửa event
    check_variable = { VIE_ax_merit < 2 }         # thêm: điều kiện cấu hình
    check_variable = { VIE_ax_market > 3 }
    has_idea = corruption_level_07                # hoặc cao hơn
}
```

Nghĩa là: **cửa event mở cơ hội, cấu hình quyết định bạn có đi được hay không.** Không focus nào bị xóa, không ID nào đổi, không cờ nào mất tác dụng.

---

## 8. Còn thiếu

| Việc | Ghi chú |
|---|---|
| **Ngưỡng cho cạnh thất bại** | Bốn cạnh ở mục 6 mới có điều kiện định tính, chưa có số |
| **Ba điều kiện tổn thương hệ thống** | "Đe dọa bên ngoài", "ngân khố eo hẹp", "cần chính danh quần chúng" chưa quy ra biến game cụ thể |
| **Ba điều kiện cấu trúc của Lạc Hồng** | "Khủng hoảng chính danh", "tinh hoa ly khai", "rạn độc quyền bạo lực" chưa có cách đo |
| **Cái giá Geddes cho `merit`** | Thiết kế ở STEP 6, chưa vào file dữ liệu, nên `merit` vẫn quá dễ lên |
| **Thử đổi `bureau_law` bằng focus** | **Nợ từ STEP 5**, vẫn chặn phần quyết định lặp lại |
| **Quan hệ dân sự – quân sự Việt Nam** | **Nợ từ STEP 3**, cần cho ngưỡng Junta — hiện `mob ≥ 9` là suy ra, không có nguồn Việt Nam |

---

## Nguồn

Doner, Ritchie & Slater (2005) *International Organization* 59(2); Slater & Wong (2013) *Perspectives on Politics* 11(3); Evans (1995) *Embedded Autonomy*; Winters (2011) *Oligarchy*; Paxton (2004) *The Anatomy of Fascism*; Mann (2004) *Fascists*; Mudde (2004); Levitsky & Loxton (2013); Levitsky & Way (2010); Geddes, Wright & Frantz (2014); Greitens (2016); O'Donnell & Schmitter (1986); Przeworski (1991); Linz (2000); Kuik (2008).

Dữ liệu mod: `D:\HOI4Mods\_gen\axis_map.py`, `axis_map_mil_alt.py`. Vân tay lịch sử và bảng kiểm chứng ngưỡng đều tính từ hai file này.

---

## Bước 9: Kế hoạch thi công theo batch

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

---

## Phụ lục I: Thiết kế Statebuilding v1

# Báo cáo Thiết kế & Hoàn tất Thi công Hệ thống Xây dựng Nhà nước (V1)
## Millennium Dawn: Submod Việt Nam (tag VIE) — Đợt triển khai STEP 1–9

> Ngày hoàn thành: 20/09/2026.
> Quy chiếu: `VIE_regime_taxonomy_step1_2.md` → `VIE_three_families_step3.md` → `VIE_technocracy_capacity_step4.md` → `VIE_statebuilding_framework_step5.md` → `VIE_doimoi_backbone_step6.md` → `VIE_branch_mapping_step7.md` → `VIE_transition_graph_step8.md` → `VIE_implementation_plan_step9.md`.
> Kết quả kiểm tra tĩnh: **`python tools/check_static.py` in 0 errors (487 focus, 171 ideas, 186 events, 2344 loc keys)**.
> Bản sao lưu nguyên trạng trước khi sửa: `D:\HOI4Mods\_backup_v5`.

---

## 1. Tóm tắt Kiến trúc & Các Batch đã Hoàn thành

Toàn bộ 8 batch thi công theo kế hoạch `VIE_implementation_plan_step9.md` đã được triển khai đầy đủ và kiểm chứng:

### Batch 0: Hạ tầng Đo lường (Không đổi gameplay)
- **Dynamic modifier `VIE_state_modifier`** (`common/dynamic_modifiers/VIE_md_state_modifier.txt`): Đọc và phản ánh 9 biến trục xây dựng nhà nước.
- **Scripted effects `VIE_ax_init` & `VIE_ax_normalize`** (`common/scripted_effects/VIE_md_effects_axis.txt`):
  - Khởi tạo giá trị ban đầu cho 9 trục: `size = 3`, `merit = -2`, `decent = 1`, `checks = -2`, `market = -2`, `civil = -3`, `integ = 0`, `mob = 0`, `west = 0`.
  - Chuẩn hóa thang đo về `-10 .. +10` dựa trên SPAN: `size (12)`, `merit (59)`, `decent (24)`, `checks (19)`, `market (41)`, `civil (14)`, `integ (98)`, `mob (12)`, `west (29)`.
  - Tính toán các modifier hiệu ứng biên độ ±3% ở hai đầu cực.
- **Hook hàng tháng**: Nối `VIE_ax_normalize = yes` vào `on_monthly` (`common/on_actions/VIE_md_on_actions.txt`) và focus gốc `VIE_doi_moi_continues`.

### Batch 1: Gắn Trục vào Thân Lịch sử (168 Focus)
- Chèn `add_to_variable = { VIE_ax_<axis> = <val> tooltip = VIE_ax_<axis>_tt }` vào toàn bộ 168 focus thân Đổi Mới theo dữ liệu `_gen/axis_map.py`.

### Batch 2: Gắn Trục vào Quốc phòng & Dải Chế độ (202 Focus)
- Chèn biến trục vào 51 focus quân sự (MIL) và 151 focus dải chế độ (ALT) theo dữ liệu `_gen/axis_map_mil_alt.py`.
- Tổng cộng 370 focus đã được gán biến trục đầy đủ.

### Batch 3: Nối vào Hệ thống Luật & Ngân sách Millennium Dawn (15 Focus)
- Nối các focus cải cách hành chính (`VIE_streamline_apparatus`, `VIE_merge_ministries`, `VIE_provincial_merger`, `VIE_two_tier_local_gov`) vào `decrease_centralization = yes` và điều chỉnh ngân sách công vụ (`change_expected_bureaucracy_spending`).
- Nối các focus an ninh (`VIE_cybersecurity_law`, `VIE_force_47`, `VIE_sec_public_order`) vào `increase_policing_budget = yes`.
- Nối các focus giáo dục, y tế, an sinh (`VIE_free_tuition`, `VIE_education_reform`, `VIE_universal_health_insurance`, `VIE_grassroots_clinics`, `VIE_social_insurance_reform`, `VIE_dm_soc_welfare_state`) vào các luật chi tiêu ngân sách xã hội của MD.

### Batch 4: Cơ chế Đánh đổi & Cấu trúc Faction Tinh hoa
- **Cái giá Geddes (1994) cho Meritocracy**: Mọi focus tăng `merit` đều làm giảm mức độ hài lòng của cán bộ Đảng (`change_communist_cadres_opinion = -2`) do làm mất nguồn lực bảo trợ chính trị truyền thống.
- **Tiến hóa Faction Nội bộ (`VIE_ax_faction_check`)**: Tuân thủ tuyệt đối giới hạn **chính xác 3 slot internal factions** của MD:
  - Khi kinh tế thị trường vượt quá năng lực kiểm soát (`market_norm >= 4` và `merit_norm <= 2`), `oligarchs` thay thế `industrial_conglomerates`.
  - Khi trật tự an ninh bị siết chặt (`civil_norm <= -6`), `intelligence_community` thay thế `farmers`.
  - Khi huy động quần chúng dâng cao (`mob_norm >= 8`) hoặc Junta, `the_military` tham gia chính trường.
  - Khi nới lỏng thể chế và mở rộng kiểm soát ngang (`checks_norm >= 5`), `labour_unions` xuất hiện.
  - Khi thị trường phát triển lành mạnh (`market_norm >= 3` và `merit_norm >= 3`), `small_medium_business_owners` xuất hiện.

### Batch 5: Ngưỡng Mở nhánh Cấu hình & 4 Cạnh Đảo ngược
- Cập nhật điều kiện `available` của 11 gốc dải chế độ giả định: giữ nguyên cờ event (điều kiện cần), bổ sung điều kiện ngưỡng trục (điều kiện đủ) theo đúng bảng STEP 8 mục 4.
- Thêm 4 sự kiện đảo ngược/thất bại mới (`events/VIE_md_axis.txt`):
  - `vie_axis.1`: Nhà nước kiến tạo bị tài phiệt thao túng khi thị trường vượt xa chất lượng bộ máy công quyền (Evans 1995).
  - `vie_axis.2`: Cực hữu Lạc Hồng thoái hóa thành độc đoán an ninh thông thường sau thời gian nguội lạnh cách mạng (Paxton phase 5).
  - `vie_axis.3`: Dân chủ hóa dừng lại ở điểm cân bằng độc đoán cạnh tranh (Levitsky & Way).
  - `vie_axis.4`: Cảnh báo khủng hoảng đa tầng đe dọa sụp đổ nhà nước.

### Batch 6: Quyết định Lặp lại "Xây dựng Nhà nước"
- Bổ sung danh mục quyết định mới `VIE_statebuilding_category` (`common/decisions/categories/VIE_md_categories.txt`).
- Thêm 6 quyết sách lặp lại (`common/decisions/VIE_md_decisions.txt`):
  1. `VIE_civil_service_examination`: Thi tuyển công chức cạnh tranh (`merit +1`, tốn PP, giảm opinion cán bộ).
  2. `VIE_provincial_pilot_program`: Giao quyền thí điểm thể chế cho địa phương (`decent +1`).
  3. `VIE_streamline_administrative_org`: Tinh gọn đầu mối bộ máy hành chính (`size -1`, `decrease_centralization`).
  4. `VIE_relax_media_scrutiny`: Cởi mở không gian báo chí & phản biện (`civil +1`, `checks +1`, giảm ổn định ngắn hạn).
  5. `VIE_strengthen_internal_discipline`: Siết chặt kỷ cương & trật tự xã hội (`civil -1`, `checks -1`, tăng ổn định).
  6. `VIE_negotiate_economic_pact`: Đàm phán thỏa thuận thương mại & đầu tư mới (`integ +1`, tăng ngân khố).

### Batch 7: Localisation Tiếng Việt Hoàn chỉnh
- File `localisation/english/replace/VIE_md_vi_axis_l_english.yml` cung cấp đầy đủ tên và mô tả tiếng Việt có dấu cho toàn bộ 9 trục, 18 cực, 9 tooltips, danh mục quyết định, 6 quyết định và 4 sự kiện mới.

---

## 2. Kiểm chứng Hệ thống (Verification Summary)

1. **Static Validation (`tools/check_static.py`)**:
   - Focuses: **487** (không trùng cell, quan hệ prerequisite / mutual exclusion hoàn chỉnh).
   - Ideas: **171** (không idea mồ côi).
   - Events: **186** (tăng từ 182, bao gồm 4 sự kiện trục `vie_axis`).
   - Localisation Keys: **2344** (tăng từ 2279).
   - **0 errors**.
2. **Độ an toàn Lưu trữ & Tính tương thích**:
   - Không thay đổi ID focus nào.
   - Giữ nguyên cấu trúc cây và hệ thống scheduler lặp lại theo tháng.
   - Thừa hưởng 100% cơ chế native của Millennium Dawn 1.19.

---

## Phụ lục II: Thiết kế Statebuilding 4 trục

# Thiết kế lại "Xây dựng Nhà nước & Năng lực Thể chế": 9 trục → 4 trục

> Ngày: 03/10/2026. Trạng thái: **thiết kế, chưa code.**
> Thay thế phần hiển thị và quyết sách của `VIE_statebuilding_design_v1.md` (Batch 0, 4, 5, 6).

## 0. Vấn đề

- Panel hiện 9 thanh trục và 9 quyết sách, người chơi không biết nên quan tâm cái nào.
- 9 trục đều được ghi ở khoảng 370 focus, nhưng **chỉ 5 trục có chỗ đọc lại** (merit, checks, market, civil, mob) trong cổng focus, faction hoặc event.
  `size`, `decent`, `integ`, `west` chỉ ảnh hưởng tới modifier ±3%, nên người chơi theo dõi chúng mà không thấy hệ quả.
- Các quyết sách bị chia vụn: hai quyết sách cùng chỉnh một trục theo hai hướng, hoặc một quyết sách cộng một chút vào 2–3 trục.

**Mục tiêu:** chỉ còn 4 trục và 4 quyết sách. Trục nào cũng phải dẫn tới hệ quả nhìn thấy được. Không đổi ID focus và không làm hỏng save cũ.

---

## 1. Bốn trục

| Trục | Cực trái (−10) | Cực phải (+10) | Gộp từ | Câu hỏi cho người chơi |
|---|---|---|---|---|
| **A. Năng lực Bộ máy** | Bảo trợ, cồng kềnh | Tinh gọn, chuyên nghiệp | T2 Công vụ, T1 Quy mô (đảo dấu) | Bộ máy làm việc giỏi hay nuôi người nhà? |
| **B. Không gian Chính trị** | Kiểm soát, huy động | Cởi mở, phản biện | T4 Ràng buộc, T6 Dân sự, T8 Huy động (đảo dấu) | Siết hay nới? |
| **C. Mô hình Kinh tế** | Nhà nước, tập trung | Thị trường, phân cấp | T5 Thị trường, T3 Phân cấp | Trung ương chỉ huy hay để địa phương và thị trường tự chạy? |
| **D. Định hướng Đối ngoại** | Tự chủ | Hội nhập | T7 Hội nhập, T9 Phương Tây | Đóng hay mở với thế giới? |

### Vì sao Huy động (T8) vào B mà không vào D

- Trong code, `mob` cao tương ứng huy động quần chúng có tổ chức (dân quân, phong trào, tuyên truyền). Đây là **công cụ kiểm soát xã hội trong nước**, cùng họ với siết dân sự và giảm ràng buộc quyền lực.
- Trục D nói về quan hệ với bên ngoài. Nếu gộp Huy động vào D, trục này sẽ có hai nghĩa: một focus về dân quân tự vệ lại đẩy quốc gia về phía "đóng cửa kinh tế", trong khi hai việc đó không liên quan.
- Yếu tố quân sự hóa vẫn giữ được thông qua **tổ hợp** B thấp và D thấp, dùng làm điều kiện cho faction The Military (xem mục 5).

---

## 2. Công thức tính (lớp tương thích) — ĐÃ CODE

**Không sửa 370 focus.** Chín biến `VIE_ax_<x>` vẫn tồn tại như biến ẩn và vẫn được focus ghi vào như hiện nay.
Mỗi tháng, `VIE_ax_normalize` tính 4 trục mới từ các giá trị `_norm` đã có, rồi cộng thêm độ lệch của quyết sách:

```
VIE_sb_A = merit_norm - size_norm/2                + VIE_sb_A_dec
VIE_sb_B = civil_norm + (checks_norm - mob_norm)/2 + VIE_sb_B_dec
VIE_sb_C = market_norm + decent_norm/2             + VIE_sb_C_dec
VIE_sb_D = integ_norm + west_norm/2                + VIE_sb_D_dec
```

Kẹp vào [-10, +10] và làm tròn. *Khác bản nháp đầu:* bản nháp dùng trung bình, nhưng trung bình làm các trục khó chạm ±6
(mọi thành phần phải cùng chạm ±6). Dùng tổng có trọng số thì một thành phần chủ đạo (trọng số 1) tự đẩy trục đi xa được.

- Panel, modifier, faction, cổng mở nhánh và event **chỉ đọc `VIE_sb_A..D`**.
- `VIE_sb_X_dec` chỉ do 4 quyết sách ghi, nên tick tháng không xóa tác động của quyết sách.
- Save cũ: các biến mới chưa đặt mặc định bằng 0, nên A–D được tính ra ngay ở tick tháng đầu tiên.

**Giá trị khởi đầu 2000** (tính tay từ giá trị khởi tạo): A = -2 (Trì trệ), B = -3 (Kỷ cương), C = 0 (Hỗn hợp), D = 0 (Đa phương hóa).

---

## 3. Vùng giá trị và cách hiển thị

Mỗi trục chia 5 vùng. Panel hiện **tên vùng**, con số đặt trong ngoặc.

| Giá trị | −10…−6 | −5…−2 | −1…+1 | +2…+5 | +6…+10 |
|---|---|---|---|---|---|
| **A** | Bộ máy bảo trợ | Trì trệ | Cân bằng | Chuyên nghiệp hóa | Nhà nước kiến tạo |
| **B** | Nhà nước an ninh | Kỷ cương | Cân bằng | Nới lỏng | Đa nguyên hóa |
| **C** | Kế hoạch hóa | Chủ đạo nhà nước | Hỗn hợp | Thị trường | Tự do hóa |
| **D** | Tự lực | Thận trọng | Đa phương hóa | Hội nhập sâu | Liên kết phương Tây |

Mockup mô tả category:

```
Các chính sách điều chỉnh bộ máy, mô hình kinh tế, không gian chính trị
và đối ngoại của Việt Nam.

=== NĂNG LỰC THỂ CHẾ ===
A Năng lực Bộ máy    ▓▓▓▓▓░|░░░░░  Trì trệ (−3)
B Không gian CT      ▓▓▓▓▓▓|░░░░░  Kỷ cương (−4)
C Mô hình Kinh tế    ░░░░░▓|░░░░░  Hỗn hợp (0)
D Đối ngoại          ░░░░░░|▓▓░░░  Hội nhập sâu (+2)
(Cập nhật hàng tháng và ngay sau khi hoàn thành focus hoặc quyết sách.)
```

- Thanh vẽ vẫn dùng cơ chế của `common/scripted_localisation/VIE_md_axis_bars.txt`, nhưng chỉ còn 4 dòng.
- Màu của thanh theo **vùng**: xám ở vùng giữa, vàng ở ±2…5, đỏ hoặc xanh ở hai cực. Không tô màu theo hướng trái/phải như hiện nay.
- Tooltip của focus đổi từ `VIE_ax_<x>_tt` sang hiện trục mới, ví dụ "Năng lực Bộ máy ▲". Chỉ hiện mũi tên, không hiện số lẻ, vì một focus thường chỉ dịch trục mới khoảng 0,3–0,7.

---

## 4. Hiệu ứng (dynamic modifier `VIE_state_modifier`)

- Vùng giữa (−1…+1): không có hiệu ứng.
- Vùng ±2…5: nhận **một nửa** hiệu ứng của cực tương ứng.
- Vùng ±6…10: nhận **đủ** hiệu ứng.

Mỗi cực đều có cả lợi và hại.

| Trục | Cực trái (đủ hiệu ứng) | Cực phải (đủ hiệu ứng) |
|---|---|---|
| **A** | +0,15 PP/ngày, +ý kiến cán bộ Đảng, −5% hiệu suất sản xuất, tham nhũng dễ tăng | +5% tốc độ nghiên cứu, +5% hiệu suất sản xuất, −0,15 PP/ngày, −ý kiến cán bộ (cái giá Geddes) |
| **B** | +8% ổn định, +5% war support, −5% tốc độ nghiên cứu | +5% tốc độ nghiên cứu, +đồng thuận xã hội, −8% ổn định |
| **C** | +8% sản lượng nhà máy quân sự, +4% ổn định, −thu thuế | +8% tốc độ xây dựng dân sự, +thu thuế, −4% ổn định, mở điều kiện cho tài phiệt |
| **D** | Giảm 50% tác động trừng phạt, +4% sản lượng nội địa, −đầu tư nước ngoài | +đầu tư nước ngoài, +thương mại, +quan hệ đối tác, −chi phí độc lập chính sách (bị ép trong event) |

*Các con số chỉ là mức khởi điểm và sẽ chỉnh khi chạy `tools/audit/nf_balance.py`.*

---

## 5. Faction nội bộ, cổng mở nhánh, event

### Faction (`VIE_ax_faction_check`, vẫn giữ giới hạn 3 slot của MD)

| Hệ quả | Điều kiện cũ | Điều kiện mới |
|---|---|---|
| Oligarchs thay Industrial Conglomerates | market > 3, merit < 3, tham nhũng ≥ 7 | **C ≥ +4 và A ≤ +1**, tham nhũng ≥ 7 |
| Intelligence Community thay Farmers | civil < −7 và checks < −1 (hoặc flag an ninh) | **B ≤ −6** (hoặc flag an ninh) |
| The Military thay Farmers | mob > 7 | **B ≤ −6 và D ≤ −4** |
| Labour Unions thay Farmers | checks > 4 | **B ≥ +5** |
| SME Owners thay Farmers | market > 2, merit > 2 | **C ≥ +3 và A ≥ +3** |

### Cổng mở nhánh trong focus
- `VIE_md_focus.txt:4462-4463`: điều kiện civil ≤ −8 và checks ≤ −2 đổi thành **B ≤ −6**, kèm tooltip mới `VIE_gate_B_le_m6`.
- Các cổng ngưỡng khác của 11 gốc dải chế độ (Batch 5) được viết lại theo cùng nguyên tắc: **mỗi cổng chỉ dùng 1–2 trục mới**.

### Event (`events/VIE_md_axis.txt`)

| Event | Điều kiện mới |
|---|---|
| `vie_axis.1` Tài phiệt thao túng | C ≥ +5 và A ≤ 0 |
| `vie_axis.2` Lạc Hồng thoái hóa | Giữ cờ chế độ hiện tại, ngưỡng đổi thành B ≤ −7 |
| `vie_axis.3` Độc đoán cạnh tranh | B nằm trong khoảng +2…+5 kéo dài 2 năm mà không vượt lên +6 |
| `vie_axis.4` Khủng hoảng đa tầng | Ổn định < 20% và (B ≤ −6 hoặc A ≤ −4) |

---

## 6. Bốn quyết sách

Mỗi quyết sách **mở một event có 2 lựa chọn** (đẩy trục sang trái hoặc sang phải).
Event dùng namespace mới `vie_sb`, gồm `vie_sb.1` đến `vie_sb.4`.

| Quyết sách | Mở khi | Giá | Hồi chiêu | Lựa chọn trái | Lựa chọn phải |
|---|---|---|---|---|---|
| **Cải cách Bộ máy** | `VIE_public_admin_reform` | 75 PP | 180 ngày | *Củng cố đội ngũ*: A −1, +ý kiến cán bộ, +0,05 ổn định | *Thi tuyển & tinh gọn*: A +1, −ý kiến cán bộ, `decrease_centralization` |
| **Điều chỉnh Không gian Chính trị** | `VIE_constitution_2013` **hoặc** `VIE_cybersecurity_law` | 50 PP | 180 ngày | *Siết kỷ cương*: B −1, +5% ổn định trong 180 ngày | *Mở phản biện*: B +1, −5% ổn định trong 90 ngày, +ý kiến các nhóm xã hội |
| **Định hướng Kinh tế** | `VIE_decentralization` **hoặc** `VIE_wto_negotiations` | 50 PP | 180 ngày | *Tăng vai trò DNNN*: C −1, +nhà máy quân sự tạm thời | *Thí điểm địa phương & cởi trói*: C +1, +tốc độ xây dựng tạm thời |
| **Chính sách Đối ngoại** | `VIE_wto_negotiations` | 75 PP | 240 ngày | *Tự chủ chiến lược*: D −1, +war support | *Đàm phán FTA mới*: D +1, +ngân khố |

### Các lựa chọn mở thêm (không làm danh sách quyết sách dài thêm)

Event có thể có **lựa chọn thứ 3**. Lựa chọn này chỉ hiện khi đã hoàn thành focus tương ứng, và mạnh hơn nhưng đắt hơn:

| Event | Lựa chọn thứ 3 | Điều kiện | Hiệu ứng |
|---|---|---|---|
| Cải cách Bộ máy | *Chiến dịch chống tham nhũng* (thay `VIE_anticorruption_campaign`) | `VIE_party_discipline`, không ở chế độ party rule | A +2, giảm 1 bậc tham nhũng, −ý kiến cán bộ, quyết sách hồi chiêu 730 ngày |
| Cải cách Bộ máy | *Luân chuyển cán bộ* (thay `VIE_cadre_rotation`) | `VIE_clean_cadres` | A +1, C +0,5 (phá nhóm lợi ích địa phương), bộ máy xáo trộn 180 ngày |
| Điều chỉnh Không gian Chính trị | *Tham vấn công chúng* (thay `VIE_public_consultation`) | `VIE_grassroots_democracy` | B +1, C +0,5, chỉ −2% ổn định |

### Các quyết sách cũ bị bỏ

| Quyết sách cũ | Chuyển thành |
|---|---|
| `VIE_civil_service_examination` | Cải cách Bộ máy, lựa chọn phải |
| `VIE_streamline_administrative_org` | Cải cách Bộ máy, lựa chọn phải (gộp với thi tuyển) |
| `VIE_provincial_pilot_program` | Định hướng Kinh tế, lựa chọn phải |
| `VIE_relax_media_scrutiny` | Điều chỉnh Không gian CT, lựa chọn phải |
| `VIE_strengthen_internal_discipline` | Điều chỉnh Không gian CT, lựa chọn trái |
| `VIE_negotiate_economic_pact` | Chính sách Đối ngoại, lựa chọn phải |
| `VIE_anticorruption_campaign` | Cải cách Bộ máy, lựa chọn thứ 3 |
| `VIE_public_consultation` | Điều chỉnh Không gian CT, lựa chọn thứ 3 |
| `VIE_cadre_rotation` | Cải cách Bộ máy, lựa chọn thứ 3 |

### Ghi chú kỹ thuật
- Quyết sách mới **cộng thẳng vào biến A/B/C/D**, không cộng vào 9 biến cũ. Vì A/B/C/D được tính lại từ 9 biến mỗi tháng, mỗi trục cần thêm một biến lệch riêng:
  `VIE_ax_A = (công thức) + VIE_ax_A_dec`. Quyết sách chỉ ghi vào `VIE_ax_A_dec`. Như vậy tác động của quyết sách không bị tick tháng xóa mất.
- Với lựa chọn thứ 3, AI chỉ chọn khi đang đi theo hướng chế độ phù hợp. Đặt `ai_chance` theo cờ chế độ.
- Các quyết sách cũ phải xóa hẳn chứ không chỉ ẩn, để không còn key thừa. Chạy `tools/check_static.py` để bắt loc key mồ côi.

---

## 7. Phạm vi thay đổi khi code

| File | Thay đổi |
|---|---|
| `common/scripted_effects/VIE_md_effects_axis.txt` | Tính A–D và 4 biến `_dec`, viết lại `faction_check` và `events_check` |
| `common/dynamic_modifiers/VIE_md_state_modifier.txt` | Bỏ 18 cực cũ, thay bằng 4 trục × 2 cực × 2 mức |
| `common/scripted_localisation/VIE_md_axis_bars.txt` | 4 thanh, tên vùng, màu theo vùng |
| `common/decisions/VIE_md_decisions.txt` | Bỏ 9 quyết sách cũ, thêm 4 quyết sách mới |
| `events/VIE_md_statebuilding.txt` (mới) | `vie_sb.1` đến `vie_sb.4` |
| `events/VIE_md_axis.txt` | Viết lại điều kiện 4 event |
| `common/national_focus/VIE_md_focus.txt` | Chỉ sửa các cổng ngưỡng (dòng 4462 và các gốc dải chế độ), **không động tới** các dòng `add_to_variable` |
| Tooltip focus | Đổi `VIE_ax_<x>_tt` (9 key) thành 4 key mới. Có thể làm bằng script đổi tên tooltip theo bảng gộp ở mục 1 |
| `localisation/.../VIE_md_vi_axis_l_english.yml` | 4 trục, 20 tên vùng, 4 quyết sách, 4 event |

**Kiểm tra sau khi code:** `tools/check_static.py` phải báo 0 lỗi. Chơi thử 2000→2010 theo nhánh Đổi Mới chuẩn, A–D phải dao động hợp lý (không trục nào chạm ±10 trước năm 2010).