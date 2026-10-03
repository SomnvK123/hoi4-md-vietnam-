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
