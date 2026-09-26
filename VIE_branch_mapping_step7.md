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
