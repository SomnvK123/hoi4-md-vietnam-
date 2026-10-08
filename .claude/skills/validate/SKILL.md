---
name: validate
description: 'Bộ công cụ kiểm tra tĩnh, kiểm tra dịch thuật localisation và rà soát chất lượng code (content-review) toàn diện cho MD Vietnam. Dùng khi gọi /validate, /loc-check, review PR hoặc kiểm tra trước khi commit.'
---

# Cẩm nang Toàn diện về Kiểm thử & Đảm bảo Chất lượng (Validation & QA)

Dùng cho mọi hoạt động kiểm tra, rà soát lỗi tĩnh, thẩm định chuỗi dịch thuật (localisation) và review nội dung trước khi merge code vào repository.

Tài liệu tham khảo chuyên sâu:
- [`.claude/docs/validation.md`](../../docs/validation.md): Hướng dẫn giải thích kết quả và xử lý false-positive.
- [`.claude/docs/known-issues.md`](../../docs/known-issues.md): Danh mục nợ kỹ thuật và lỗi đã biết (không nhầm với lỗi mới).
- [`.claude/docs/bug-patterns.md`](../../docs/bug-patterns.md): Các mẫu bug thường gặp trong code Clausewitz / MD.

---

## 1. Lệnh Kiểm tra Nhanh theo Phạm vi

Chạy từ thư mục gốc của repository (`d:\HOI4Mods\md_vietnam`):

| Phạm vi | Lệnh thực thi | Mục đích kiểm tra |
|---|---|---|
| **Toàn bộ mod** | `python tools/audit/audit.py && python tools/audit/live.py && python tools/verify_all_loc.py && python tools/audit_dds_and_gfx.py` | Kiểm tra tổng hợp toàn diện trước khi commit |
| **Cây Focus** | `python tools/audit/audit.py` | Toạ độ, relative_position_id, prerequisite, vòng lặp |
| **Tham chiếu chéo** | `python tools/audit/live.py` | Effect, trigger, idea, modifier thật của Millennium Dawn |
| **Dịch thuật (Loc)** | `python tools/verify_all_loc.py`<br>`python tools/audit_loc_errors.py` | Thiếu key, trùng key replace, mã màu, getter `[Root.GetName]` |
| **Đồ họa & DDS** | `python tools/audit_dds_and_gfx.py` | Kích thước, header 124, 32-bit BGRA, 33.980B, sprite GFX |
| **Sự kiện (Event)** | `python tools/audit/ev.py` | Event ID, trigger, fire_only_once, option effects |
| **Địa lý / State** | `python tools/audit/prov.py` | Province ID, state ownership của VIE (518-524, 526, v.v.) |

---

## 2. Kiểm tra Localisation & Chuỗi Ngôn ngữ (Loc-Check)

Khi vừa thêm focus, idea, decision, event hoặc tooltip mới:

1. **Rà soát Key bắt buộc:**
   - Focus: phải có `VIE_<id>:0 "Tiêu đề"` và `VIE_<id>_desc:0 "Mô tả"`.
   - Idea: phải có `VIE_<id>:0 "Tên"` và `VIE_<id>_desc:0 "Mô tả"`.
   - Event: phải có `VIE_event.<id>.t:0 "Tiêu đề"`, `VIE_event.<id>.d:0 "Mô tả"`, `VIE_event.<id>.a:0 "Lựa chọn"`.
2. **Cơ chế Replace:**
   - File dịch đặt tại `localisation/english/replace/VIE_md_vi_p<N>_b_l_english.yml`.
   - Không khai báo trùng lặp cùng một key trên nhiều file replace khác nhau.
3. **Mã màu & Getter:**
   - Đóng mở mã màu hợp lệ: `§Y...§!`, `§G...§!`, `§R...§!`, `§W...§!`. Không để hở mã màu.
   - Text getter đúng cú pháp Clausewitz (vd: `[Root.GetName]`, `[GetDateText]`). Không để chuỗi `TODO`, `...` hoặc em dash hỏng font.
4. **Số liệu trung thực:** Các con số nêu trong chuỗi mô tả phải khớp chính xác với effect thực tế trong code.

---

## 3. Checklist Rà soát Nội dung trước khi Merge (Content-Review)

Áp dụng cho mọi pull request hoặc diff (`git diff main...HEAD`). Gắn nhãn **BLOCKER** (phải sửa) hoặc **NIT** (gợi ý cải thiện):

- [ ] **1. Tham chiếu chéo (BLOCKER):** Mọi effect/trigger/idea/event/loc gọi đến phải tồn tại thực tế. Không bịa token MD.
- [ ] **2. An toàn State (BLOCKER):** Mọi lệnh `one_state_*` hoặc can thiệp trực tiếp chỉ scope vào các state VIE sở hữu:
  - Đồng bằng Bắc Bộ: 518, 519, 520, 521, 522
  - Miền Trung & Tây Nguyên: 523, 524, 801, 802
  - Nam Bộ: 526, 813, 816
- [ ] **3. Chi ngân sách đúng chuẩn (BLOCKER):** Không dùng thô `add_building_construction` cho nhà máy/công trình kinh tế. Phải trừ tiền qua `treasury_change` + `modify_treasury_effect = yes` hoặc scripted effect MD.
- [ ] **4. Công trình theo Province (BLOCKER):** `bunker`, `coastal_bunker`, `naval_base` bắt buộc phải có tham số `province = <ID>`.
- [ ] **5. Hình học Focus Tree (BLOCKER):** Không trùng toạ độ, không forward-ref, không prerequisite vòng lặp, gap cùng hàng $\ge 2$.
- [ ] **6. Định dạng Đồ họa (BLOCKER):** Icon đúng chuẩn (Focus: 93x91 DDS 33.980B; Idea: 60x68 DDS 16.448B; Decision: 33x32 TGA), sprite registered.
- [ ] **7. Phong cách & Văn phong (NIT):** Ghi chú code viết tiếng Việt không dấu (đồng bộ repo), loc hiển thị tiếng Việt có dấu mạch lạc, trang trọng.

---

## 4. Diễn giải Kết quả & Phân biệt Lỗi

- **Lỗi đường dẫn:** Nếu `tools/audit/live.py` in `DEFS:` với `effect: 0`, tức là bộ định nghĩa rỗng do đường dẫn thư mục MD bị lệch. Báo ngay "kết quả live không dùng được", không liệt kê hàng trăm lỗi giả (false positives).
- **Lỗi đã biết trong `known-issues.md`:** Các báo nhầm đã biết (event ẩn thiếu loc, `GFX_report_event_generic_*`) cần được bỏ qua, chỉ tập trung vào các lỗi mới phát sinh từ diff hiện tại.
- **Tính minh bạch:** Luôn báo cáo trung thực: nếu chỉ mới audit file tĩnh thì nêu rõ là "chưa test runtime trong game".
