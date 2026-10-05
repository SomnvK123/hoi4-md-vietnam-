# Nhánh An ninh Nội địa & Kiểm soát Không gian mạng — Kiến trúc & Bố cục Hàng ngang (Chuẩn hóa MD4)

> **Tài liệu thiết kế kiến trúc và chuẩn format (04/10/2026)**  
> **Áp dụng:** Chuẩn hóa và quy tụ toàn bộ 8 focus An ninh Nội địa (`VIE_sec_*`) trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md).

---

## 1. Hiện trạng & Mục tiêu Chuẩn hóa

### 1.1 Vấn đề trước khi chuẩn hóa
1. **Phân mảnh trong file:** 8 focus an ninh bị xé làm 2 cụm: 3 focus đầu (`VIE_sec_cyber_control`, `VIE_sec_surveillance_network`, `VIE_sec_security_economy`) đặt trước Khoa học số, còn 5 focus sau (`VIE_sec_public_order`, `VIE_sec_cyber_sovereignty`, `VIE_sec_loyalty_vetting`, `VIE_sec_border_control`, `VIE_sec_managed_opening`) đặt sau Khoa học số.
2. **Khoảng cách và kết nối:** Cần đồng bộ hóa để đảm bảo toàn bộ các bước nhảy $dy = 1$, $\Delta x \ge 2$, và không có bất kỳ khoảng trống hay dây chéo nào.

### 1.2 Giải pháp Chuẩn hóa
* **Hợp nhất một khối duy nhất:** Toàn bộ 8 focus được gom thành 1 khối duy nhất đặt ngay trước khối Khoa học số 2045.
* **Bố cục Kim tự tháp ngược đối xứng hoàn hảo:**
  - Hàng $y = 13$: Gốc `VIE_sec_cyber_control` tại tọa độ $(93, 13)$.
  - Hàng $y = 14$: 3 trụ cột an ninh: Giám sát $(91)$, Trật tự xã hội $(93)$, Kinh tế an ninh $(95)$.
  - Hàng $y = 15$: 3 mũi nhọn chuyên sâu: Chủ quyền số $(91)$, Thẩm tra lòng trung thành $(93)$, Kiểm soát biên giới $(95)$.
  - Hàng $y = 16$: Mốc chốt mở cửa có quản lý: `VIE_sec_managed_opening` tại trung tâm $(93)$.
* **Toàn bộ $dy = 1$:** 100% các bước chuyển đều liền kề 1 hàng, không có khoảng cách trống.

---

## 2. Bản đồ Cấu trúc & Tọa độ

```text
                           VIE_sec_cyber_control
                         (Kiểm soát Không gian mạng)
                                (x=93, y=13)
                                      │
              ┌───────────────────────┼───────────────────────┐
   VIE_sec_surveillance_network  VIE_sec_public_order   VIE_sec_security_economy
       (Mạng lưới Giám sát)       (Trật tự Công cộng)       (Kinh tế An ninh)
           (x=91, y=14)              (x=93, y=14)              (x=95, y=14)
              │                           │                         │
   VIE_sec_cyber_sovereignty     VIE_sec_loyalty_vetting    VIE_sec_border_control
        (Chủ quyền Số)           (Thẩm tra Lòng trung thành)   (Kiểm soát Biên giới)
           (x=91, y=15)              (x=93, y=15)              (x=95, y=15)
              └───────────────────────────┬─────────────────────────┘
                                   VIE_sec_managed_opening
                                    (Mở cửa có Quản lý)
                                       (x=93, y=16)
```

---

## 3. Bảng Tọa độ & Tham chiếu Chi tiết

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available |
|:---:|---|:---:|---|---|---|
| **y = 13** | `VIE_sec_cyber_control` | (93, 13) | `VIE_doi_moi_continues` (13, 13) | - | `VIE_cybersecurity_law`, ruling_party = 7 / flag |
| **y = 14** | `VIE_sec_surveillance_network` | (91, 14) | `VIE_sec_cyber_control` (-2, 1) | `VIE_sec_cyber_control` | - |
| | `VIE_sec_public_order` | (93, 14) | `VIE_sec_cyber_control` (0, 1) | `VIE_sec_cyber_control` | - |
| | `VIE_sec_security_economy` | (95, 14) | `VIE_sec_cyber_control` (2, 1) | `VIE_sec_cyber_control` | - |
| **y = 15** | `VIE_sec_cyber_sovereignty` | (91, 15) | `VIE_sec_surveillance_network` (0, 1) | `VIE_sec_surveillance_network` | - |
| | `VIE_sec_loyalty_vetting` | (93, 15) | `VIE_sec_public_order` (0, 1) | `VIE_sec_public_order` | - |
| | `VIE_sec_border_control` | (95, 15) | `VIE_sec_security_economy` (0, 1) | `VIE_sec_security_economy` | - |
| **y = 16** | `VIE_sec_managed_opening` | (93, 16) | `VIE_sec_loyalty_vetting` (0, 1) | `VIE_sec_loyalty_vetting`, `VIE_sec_cyber_sovereignty` | - |

---

## 4. Kết quả Kiểm định Kỹ thuật (HOÀN TẤT 100%)

* **Số lượng focus:** Khớp chính xác 8 / 8 focus An ninh (Tổng cây: 410 focus).
* **Xung đột nội bộ (Collisions):** **0 lỗi**.
* **Tham chiếu tiến (`relative_position_id` forward reference):** **0 lỗi**.
* **Độ lệch dọc ($dy$):** 100% các liên kết đạt chuẩn $dy = 1$.
* **Khoảng cách ngang ($\Delta x$):** Đạt chuẩn $\Delta x = 2$ giữa các cột kề nhau.
* **Trình kiểm tra tĩnh `check_static.py`:** Giữ vững baseline **90 errors, 1 warning**.
