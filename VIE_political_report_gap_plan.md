# Kế hoạch code: đối chiếu "Báo cáo nghiên cứu — Nền tảng lịch sử cho Political Focus Tree VIE" với code hiện tại

> **Đã thay thế** bởi `VIE_congress_spine_redesign.md`. Mục 3.2 của tài liệu này sai một phần: 4 trên 7 event được đề xuất đã có sẵn dưới ID khác (đất đai `vie_pol.20`, Formosa `vie_eco.6`, dự luật đặc khu `vie_alt.6`, Luật An ninh mạng `vie_pol.10`). Bộ luật Lao động 2019 đã được code thành `vie_pol.27`. Luật Thực hiện dân chủ ở cơ sở 2022 được xử lý bằng mốc ngày của `peoples_oversight` trong thiết kế mới. Phản ứng về bauxite Tây Nguyên 2009 chưa làm (`vie_pol.18` là bất ổn 2004, khác chủ đề).

> Input: báo cáo nghiên cứu 26/9/2026 (Tầng 0–4, phân tích SIA, đề xuất H1/H2...). Đây **không phải** kế hoạch đầu tiên cho nhánh chính trị — nó đến **sau** `VIE_regime_taxonomy_step1_2.md` → `VIE_three_families_step3.md` → `VIE_technocracy_capacity_step4.md` → `VIE_statebuilding_framework_step5.md` → `VIE_doimoi_backbone_step6.md` → `VIE_branch_mapping_step7.md` → `VIE_transition_graph_step8.md` → `VIE_implementation_plan_step9.md` → `VIE_political_branch_plan_review.md` → `VIE_nationalism_branch_research_report.md` → `VIE_report_focus_event_decision.md` (audit hiện trạng, 26/9/2026, **502 focus / 191 event / 16 decision**, đã có tree chính trị 210 focus thân lịch sử + 159 focus dải chế độ giả định).
>
> Việc của tài liệu này: **không thiết kế lại từ đầu**. Đối chiếu từng đề xuất của báo cáo mới với code thật, đánh dấu cái gì **đã có** (đừng code lại), cái gì **thiếu thật** (code thêm), và gộp phần thiếu vào đúng chỗ trong backlog ưu tiên đã có ở `VIE_report_focus_event_decision.md` §7.
>
> Nhãn: **[ĐÃ CÓ]** · **[THIẾU — LÀM THÊM]** · **[CỐ Ý KHÔNG LÀM]** · **[CẦN XÁC MINH TRONG GAME]**

---

## 1. Kết luận ngắn

Khoảng **80–90% nội dung** báo cáo mới (Tầng 0 di sản, Tầng 1 xương sống Đại hội, phần lớn Tầng 2, khung 7 trục thay "Coup Risk", H1/H2 alt-history) **đã được code**, thường còn chi tiết hơn báo cáo đề xuất. Đây là dấu hiệu tốt — hai quá trình nghiên cứu độc lập hội tụ về cùng kiến trúc.

Phần thực sự thiếu là hẹp và cụ thể:

1. **7 event lịch sử thuộc "áp lực từ dưới lên"** (mục 6.6 của báo cáo) chưa tồn tại dưới dạng event — đây là input duy nhất đáng code mới từ báo cáo này.
2. **1 focus ngoại giao thiếu 1 target** (EU vào thang CSP).
3. **1 việc kiểm tra anachronism** (đối chiếu ngày tháng, không phải code).
4. Phần còn lại của báo cáo (H1, H2a/H2b, tầng 3 G1/G2/G3, thang đối tác, "Bốn không") đã có, có khi kỹn hơn.

**Ưu tiên thật sự cao hơn cả 4 việc trên** vẫn là backlog đã có sẵn ở `VIE_report_focus_event_decision.md` §7 (chưa chạy thử trong game, 127 cặp focus chen sát, 4 focus bị xóa cần xác nhận, dọn `.bak`). Mục 5 dưới đây xếp việc mới vào đúng vị trí trong backlog đó, không tạo backlog song song.

---

## 2. Đối chiếu Tầng 0–4 của báo cáo với code

| Đề xuất của báo cáo | Trạng thái | Bằng chứng |
|---|---|---|
| Tầng 0 di sản (Đổi Mới, Hiến pháp 1992, "không liên minh") | **[ĐÃ CÓ]** | STEP6: `VIE_doi_moi_continues` là gốc khởi tạo 7 trục bằng giá trị 2000, không phải focus chơi lại quá khứ — đúng nguyên tắc mục 9.6 của báo cáo mới |
| Tầng 1 xương sống chu kỳ Đại hội (IX→XIV) | **[ĐÃ CÓ]**, nhưng **ẩn trong hiệu ứng, không phải node riêng** | STEP6 mục 3: 5 giai đoạn (2000–06, 07–10, 11–15, 16–20, 21–26) đã đối chiếu hiệu ứng trục với đúng 82/14/13/19/26 focus mỗi giai đoạn. Đại hội XIV (2026) là flag `VIE_fourteenth_congress_held` gắn trong `VIE_era_of_rising`, không phải focus riêng |
| Nghị quyết là đơn vị chính sách, có độ trễ | **[ĐÃ CÓ]** | `resolution_57_68`, `institutional_bottlenecks`, `public_admin_reform`, `e_government`, `cybersecurity_law` đều tồn tại là focus riêng (đã bị một bản kế hoạch cũ bỏ sót, `political_branch_plan_review.md` §2 đã bắt lỗi đó) |
| Coup Risk kiểu Thái Lan → thay bằng thước đo phù hợp VN | **[ĐÃ CÓ]**, đúng như báo cáo đề xuất ở mục 4.2 | STEP5: không thêm thanh mới, dùng `VIE_state_modifier` (7→9 trục) + 3 power balance sẵn có của MD. Không có "coup risk" giả tạo |
| Đảng cầm quyền không đổi → gắn nhánh với "đường lối hiện hành" thay vì "ruling party" | **[ĐÃ CÓ]**, đúng cơ chế báo cáo đề xuất ở mục 5.2 | STEP7: chữ ký trục theo dải chế độ, không theo đảng; `VIE_political_branch_plan_review.md` §3.1 sửa đúng lỗi "gắn nhánh với cờ tĩnh thay vì trạng thái thực" mà PR #4362 của Thái Lan mắc phải |
| Thang đối tác ngoại giao (CSP/SR) | **[ĐÃ CÓ]**, thiếu 1 target | `VIE_csp_network` cộng `VIE_ax_integ`/`VIE_ax_west`, tạo opinion modifier `VIE_strategic_partnership` với US/JAP/KOR/RAJ (Ấn Độ). **Thiếu EU** (đối tác CLTD thứ 15, 29/1/2026) — xem mục 3.1 |
| "Bốn không" là ràng buộc hệ thống lên ngoại giao/quân sự | **[ĐÃ CÓ]** | `VIE_four_nos_doctrine` tồn tại; nhánh hạt nhân trong quốc phòng đòi rõ "không còn Bốn Không" làm điều kiện (theo `VIE_report_focus_event_decision.md` §2.3) — đúng cách báo cáo mới mô tả đây là trần của mọi nhánh (mục 8.2) |
| Tầng 3 G1/G2/G3 (biến thể đường lối, không phải phe) | **[ĐÃ CÓ]** | Gia đình A/B/C của `VIE_three_families_step3.md`, chữ ký trục xác nhận ở STEP7 (developmental_state = "kiến tạo rồi dân chủ hóa", đúng Slater & Wong mà báo cáo mới cũng trích) |
| Tầng 4 H1 đa nguyên có kiểm soát | **[ĐÃ CÓ]** | 4 gói `dm_*` (22 focus, dân chủ hóa qua round-table) trong dải chế độ giả định, đúng điều kiện "chỉ mở khi hội tụ khủng hoảng" mà báo cáo mới yêu cầu ở mục 6.9 |
| Tầng 4 H2a chủ quyền trong chế độ | **[ĐÃ CÓ]**, và **đã tốt hơn báo cáo mới đề xuất** | `VIE_nationalism_branch_research_report.md` đã thay thế hoàn toàn nhánh `VIE_np_*`/`VIE_lh_*` cũ bằng 4 trụ cột đúng tinh thần "chủ nghĩa dân tộc phòng thủ, khẳng định chủ quyền" — báo cáo mới mục 6.9 H2a mô tả lại đúng thứ đã redesign. **Không làm lại.** |
| Tầng 4 H2b dân tộc chủ nghĩa ngoài chế độ | **[CỐ Ý KHÔNG LÀM]**, đúng khuyến nghị "rất thấp khả thi" của báo cáo mới | Nationalism report đã loại bỏ hướng cực hữu/thanh trừng sắc tộc, giữ đúng cảnh báo mục 9.13 của báo cáo mới |
| Nhánh phục hồi lãnh thổ kiểu Greater Thailand | **[CỐ Ý KHÔNG LÀM]** | Không có trong code, đúng khuyến nghị mục 4.3/9.8 |
| Phục hồi VNCH/quân chủ | **[CỐ Ý KHÔNG LÀM]** | Không có trong code, đúng mục 9.14 |
| Capstone neo 2030/2045 | **[ĐÃ CÓ]** | `VIE_ninh_thuan_nuclear`... không liên quan; capstone thật là `party_centennial_2030` (2030) — tồn tại, và theo `political_branch_plan_review.md` §4.3 đã có kế hoạch nâng cấp bằng `swap_ideas` thay vì thêm focus độn |

**Kết luận mục 2:** không cần hành động thiết kế mới cho Tầng 0, 1, 3, 4. Phần đáng làm nằm ở Tầng 2E (áp lực xã hội) — mục 3 dưới đây.

---

## 3. Phần thiếu thật — cụ thể để code

### 3.1 EU vào thang đối tác chiến lược toàn diện (nhỏ)

**Báo cáo nói gì [S]:** EU trở thành đối tác CLTD thứ 15 ngày 29/1/2026 (mục 8.3, dòng cuối bảng 7.2).

**Code hiện tại:** `VIE_csp_network` (`common/national_focus/VIE_md_focus.txt`, khoảng dòng chứa `id = VIE_csp_network`) cộng opinion modifier `VIE_strategic_partnership` cho USA/JAP/KOR/RAJ, `available = { date > 2023.8.31 has_completed_focus = VIE_us_comprehensive_partnership }`. Không có EU (mã quốc gia MD cho EU — kiểm tra xem MD có tag `EUR`/siêu quốc gia hay chỉ có các nước thành viên riêng lẻ trước khi code, vì HOI4 gốc không có "EU" như một country tag chơi được).

**Việc cần làm:**
- Kiểm tra trong `common/countries` hoặc tag list của MD xem có tồn tại một thực thể ngoại giao đại diện EU (nhiều mod dùng opinion với từng nước lớn EU thay vì một tag EU). Nếu không có tag EU, **bỏ qua việc này** — không bịa tag.
- Nếu có, thêm 1 dòng `add_opinion_modifier`/`reverse_add_opinion_modifier` vào đúng focus `VIE_csp_network`, hoặc thêm focus con nhỏ `VIE_eu_csp_2026` (cost 5, `available = { date > 2026.1.28 }`, prerequisite `VIE_csp_network`) nếu muốn giữ mốc ngày riêng.
- Độ ưu tiên: **thấp**. Đây là chi tiết trang trí, không phải cấu trúc.

### 3.2 Bảy event "áp lực từ dưới lên" (mục 6.6 báo cáo) — đây là phần đáng code nhất

**Vấn đề đã xác nhận bằng grep:** namespace `vie_pol` hiện có 13 event (1–9, 23–26), namespace `vie_soc` có 19 event xã hội, nhưng **không event nào** khớp các mốc: Tiên Lãng/Văn Giang (đất đai 2012), Formosa hậu quả chính trị (2016, khác với focus kinh tế `VIE_formosa_steel_complex` đã có), biểu tình dự luật đặc khu + Luật An ninh mạng (6/2018), Bộ luật Lao động 2019 + phê chuẩn ILO 98/105 (điều kiện CPTPP/EVFTA), Luật Thực hiện dân chủ ở cơ sở (2022).

**Vì sao đáng code:** báo cáo mới đúng khi nói đây là "tương đương chức năng của Coup Risk" — nguồn rủi ro ổn định thật của Việt Nam. Code hiện tại đã có cơ chế nhận (7–9 trục, đặc biệt `civil`, `checks`, BoP cải cách/bảo thủ) nhưng **thiếu input lịch sử** đẩy vào cơ chế đó. Đây không phải lỗ hổng kiến trúc — là thiếu nội dung.

**Nguyên tắc thiết kế (giữ đúng nguyên tắc đã có trong mod, không thêm thanh mới):**
- Đây là "sự kiện xảy ra VỚI chính phủ" → **event, không phải focus** (đúng phân loại mục 3.4 của chính báo cáo, và đúng cách `vie_pol`/`vie_scs` hiện tại vận hành: "lịch sử chạy bằng event, lựa chọn chạy bằng focus").
- Mỗi event ghi trục bằng `add_to_variable = { VIE_ax_xxx = ± }` rồi `VIE_ax_normalize = yes` (đúng mẫu đã dùng ở `vie_pol.23-26`), **không** tạo track/modifier mới.
- Không cho lựa chọn "miễn phí" — mỗi option có ít nhất 1 cái giá, theo đúng phê bình đã có ở `political_branch_plan_review.md` §3.5.

**Danh sách 7 event đề xuất, namespace tiếp nối `vie_pol.27` trở đi (namespace đang dừng ở `.26`):**

| ID | Tên | Kích hoạt (`trigger`/mtth) | Option A (lịch sử/nhượng bộ) | Option B (cứng rắn) |
|---|---|---|---|---|
| `vie_pol.27` | Tranh chấp đất đai Tiên Lãng – Văn Giang | `date > 2012.1.1`, ngẫu nhiên trong cửa sổ 2012–2013, chỉ bắn nếu chưa có `VIE_land_law_2013_flag` | Cưỡng chế theo kế hoạch: ổn định −0.02, `VIE_ax_civil −1` | Đối thoại, dừng cưỡng chế: PP −25, `VIE_ax_checks +1` |
| `vie_pol.28` | Bauxite Tây Nguyên: phản ứng của giới trí thức | gắn `has_completed_focus = VIE_bauxite_tay_nguyen`, mtth ngắn sau đó | Giữ dự án, không phản hồi thư kiến nghị: `VIE_ax_civil −1` | Công khai báo cáo tác động môi trường: ổn định +0.01, chi phí dự án nhẹ |
| `vie_pol.29` | Formosa: bồi thường và biểu tình (hậu quả chính trị của `VIE_formosa_steel_complex`) | `has_completed_focus = VIE_formosa_steel_complex`, `date > 2016.4.1` | Bồi thường nhanh, hạn chế biểu tình: `VIE_ax_civil −1`, ổn định +0.01 | Cho phép biểu tình giám sát môi trường: `VIE_ax_checks +1`, quan hệ Đài Loan (chủ đầu tư Formosa) −nhẹ |
| `vie_pol.30` | Biểu tình phản đối dự luật đặc khu (6/2018) | `date = 2018.6.10 ± vài ngày`, độc lập focus (đây là sự kiện đã xảy ra dù người chơi làm gì — đúng nguyên tắc "hệ thống tự kích hoạt" mục 4.1 của báo cáo) | **Hoãn dự luật (lịch sử):** ổn định +0.02, PP −30, uy tín đường lối hiện hành −nhẹ | **Giữ nguyên dự luật (phản thực tế):** `VIE_ax_civil −1`, ổn định −0.03, `VIE_ax_checks −1` |
| `vie_pol.31` | Luật An ninh mạng: phạm vi áp dụng | gắn ngay sau `vie_pol.30`, hoặc `has_completed_focus = VIE_cybersecurity_law` nếu tồn tại làm focus riêng | Áp dụng đầy đủ: `VIE_ax_civil −1`, FDI công nghệ −nhẹ (nếu có modifier FDI công nghệ, dùng chung với `VIE_fdi_attraction`) | Áp dụng có ngoại lệ cho big tech: `VIE_ax_west +1`, `VIE_ax_civil` không đổi |
| `vie_pol.32` | Bộ luật Lao động 2019 và phê chuẩn ILO | `has_completed_focus = VIE_cptpp_member` HOẶC gần `VIE_evfta`, `date > 2019.11.1` — nên đặt làm **điều kiện `available` ngược của chính hai focus đó** nếu chưa có, theo đúng mục 8.1(b) báo cáo: hội nhập đòi điều kiện thể chế | Phê chuẩn đầy đủ (lịch sử, cần cho EVFTA): `VIE_ax_checks +1`, Tổng Liên đoàn Lao động phản ứng nhẹ (opinion nội bộ nếu MD có cơ chế công đoàn, nếu không thì bỏ) | Trì hoãn: EVFTA/CPTPP bị treo (thêm điều kiện chặn ở chính hai focus đó nếu muốn ràng buộc cứng) |
| `vie_pol.33` | Luật Thực hiện dân chủ ở cơ sở (2022): kênh xả áp lực | gắn sau chuỗi trên, `date > 2022.11.1` | Thực thi nghiêm: `VIE_ax_checks +1`, `VIE_ax_civil` không đổi | Hình thức, ít thực chất: không đổi trục, chỉ +PP nhỏ (mô phỏng "xả áp lực giả") |

**Ghi chú kỹ thuật bắt buộc trước khi code (để không lặp lỗi mà `political_branch_plan_review.md` đã bắt được ở kế hoạch trước):**
1. Kiểm tra `VIE_ax_civil`, `VIE_ax_checks`, `VIE_ax_west` là đúng tên biến trong `common/dynamic_modifiers/VIE_md_state_modifier.txt` trước khi dùng (báo cáo trên liệt kê 9 biến `VIE_ax_*`, chưa liệt kê hết — đọc file thật, đừng đoán tên).
2. Mọi thay đổi trục qua `add_to_variable` phải theo sau bằng gọi chuẩn hóa `VIE_ax_normalize` đúng cú pháp đang dùng ở `vie_pol.23-26` (xem `events/VIE_md_pol.txt` dòng quanh 332–428 làm mẫu).
3. Đặt event trong `events/VIE_md_pol.txt` (namespace `vie_pol` đã khai báo ở đó), **không** tạo file event mới, để không phải khai báo namespace lần nữa.
4. Loc tiếng Việt đặt ở `localisation/english/replace/*_l_english.yml` theo đúng quy ước đã ghi trong `political_branch_plan_review.md` §3.6 (không phải `localisation/VIE_md_l_english.yml` gốc).
5. `ai_chance` cho mỗi event: dùng `factor` cố định trước (khớp thực trạng "chỉ 17% event có modifier theo ngữ cảnh" ghi ở `VIE_report_focus_event_decision.md` §3.2) — không bắt buộc phải làm AI-aware ngay, nhưng nếu làm thì việc này gộp chung với khuyến nghị #5 của backlog đã có ("bổ sung modifier AI cho D1–D8").
6. Sau khi thêm, chạy `python tools/check_static.py` — phải vẫn ra 0 lỗi.

### 3.3 QA: audit anachronism theo mục 9 báo cáo mới (không phải code, là rà soát)

Báo cáo liệt kê các mốc thuật ngữ chính xác (mục 9.12): "kinh tế thị trường định hướng XHCN" chỉ từ 2001, "ngoại giao cây tre" chỉ từ 2021 (dù khái niệm groundwork có sớm hơn), "Kỷ nguyên vươn mình" chỉ từ cuối 2024, "Bốn không" chỉ từ 2019.

**Việc cần làm:** grep tên các idea/loc string chứa các cụm trên trong `common/ideas/*.txt` và các file `localisation/**/*.txt|yml` có tham chiếu, đối chiếu `available`/ngày mở khóa của focus mang các idea đó. Đây là việc kiểm tra 30 phút, không phải thiết kế lại. Không có bằng chứng hiện tại cho thấy có lỗi (vd. `VIE_bamboo_diplomacy` đã tồn tại như một focus riêng, hợp lý nếu khóa theo ngày ≥ 2021 — cần xác nhận `available` thật của nó).

---

## 4. Việc KHÔNG làm (để tránh phá vỡ kiến trúc đã ổn định)

- **Không** thêm power balance/thước đo mới cho "bức xúc xã hội" — dùng 7–9 trục sẵn có (`civil`, `checks` là đại diện đúng nhất), đúng ràng buộc kỹ thuật đã xác lập ở STEP5 (tối đa 3 power balance, VIE đã dùng đủ 3).
- **Không** tách `resolution_57_68` thành 4 focus riêng theo đúng cấu trúc "mỗi nghị quyết một node" của báo cáo mới — vi phạm nguyên tắc "một nhánh, một spirit, nâng cấp dần" đã thống nhất ở `political_branch_plan_review.md` §4.1.3, và số lượng focus thân lịch sử (210) đã đủ dày.
- **Không** làm lại nhánh dân tộc chủ nghĩa (H2a/H2b) — đã có bản redesign riêng, tốt hơn đề xuất của báo cáo này.
- **Không** thêm focus Đại hội IX/X/XI/XIII làm node riêng cho "đẹp lịch sử" — STEP6 đã quyết định giữ Đại hội là điểm đọc trục ẩn trong các focus liên quan, không phải node trang trí, và việc thêm 4 focus không hiệu ứng riêng sẽ chỉ làm cây dày thêm mà không đổi gameplay — đúng cảnh báo "focus độn" mà `political_branch_plan_review.md` đã tự phê bình và sửa.

---

## 5. Thứ tự thực hiện thật (gộp vào backlog đã có, không tạo backlog riêng)

Đây là backlog `VIE_report_focus_event_decision.md` §7, chèn 2 việc mới của báo cáo này vào đúng vị trí ưu tiên:

| # | Việc | Nguồn | File |
|---|---|---|---|
| 1 | Chạy một ván ngắn, gửi `error.log` | backlog cũ, vẫn P0 | — |
| 2 | Sửa 127 cặp focus chen sát trong bố cục | backlog cũ | `common/national_focus/VIE_md_focus.txt` |
| 3 | Xác nhận 4 focus bị xóa là cố ý (`VIE_forest_protection`, `VIE_hanoi_air_quality`, `VIE_plastic_waste`, `VIE_jetp`→`VIE_jetp_partnership`) | backlog cũ | — |
| 4 | Dọn `.bak*` và `scratch/` trước khi đóng gói | backlog cũ | thư mục gốc |
| 5 | **Thêm 7 event `vie_pol.27–33`** (mục 3.2 ở trên) | báo cáo mới | `events/VIE_md_pol.txt` |
| 6 | Loc tiếng Việt cho 7 event trên | báo cáo mới | `localisation/english/replace/` |
| 7 | Rà anachronism thuật ngữ (mục 3.3) | báo cáo mới | grep, không sửa trừ khi thấy lỗi |
| 8 | Bổ sung modifier AI cho event điểm rẽ D1–D8 **và** `vie_pol.27–33` cùng lúc | backlog cũ + báo cáo mới gộp chung | `events/VIE_md_pol.txt` |
| 9 | Bổ sung decision cho nhánh dân chủ hóa/môi trường nếu muốn cân bằng | backlog cũ | `common/decisions/VIE_md_decisions.txt` |
| 10 | Thêm phương án trung gian `vie_disaster.1`, `vie_petro.1` | backlog cũ | events tương ứng |
| 11 | (Tùy chọn, ưu tiên thấp) EU vào `VIE_csp_network` — chỉ nếu MD có tag đại diện EU | báo cáo mới, mục 3.1 | `common/national_focus/VIE_md_focus.txt` |
| 12 | Chạy lại `python tools/check_static.py`, phải vẫn 0 lỗi | cả hai | — |

**Việc 5–7 và 11 là phần thật sự mới từ báo cáo vừa nhận.** Việc 1–4, 8–10 đã được xác định độc lập trước khi báo cáo này tới và có mức ưu tiên kỹ thuật cao hơn (chặn chạy thử game thật).
