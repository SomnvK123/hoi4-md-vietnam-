# Nhánh Kết cấu Hạ tầng & Giao thông — Kiến trúc & Bố cục Hàng ngang Tối ưu (Chuẩn hóa MD4)

> **Tài liệu thiết kế kiến trúc và chuẩn format (04/10/2026 - Bản Rút Gọn Spacing)**  
> **Áp dụng:** Tái cấu trúc, rút gần khoảng cách x-y và chuẩn hóa toàn bộ 44 focus Hạ tầng & Giao thông trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md), quy hoạch thống nhất cùng nhánh Quân sự, Chính trị và Kinh tế.

---

## 1. Hiện trạng & Lý do Tối ưu Rút gần (Compaction)

### 1.1 Vấn đề ở bản bố cục ban đầu
1. **Bước nhảy dọc quá lớn ($dy = 5$):** `VIE_airport_master_plan` đặt tại hàng $y = 6$ nhưng neo trực tiếp về `VIE_infrastructure_development` (hàng $y = 1$) với $dy = 5$, tạo ra đường liên kết vắt dọc qua 5 tầng trống.
2. **Khoảng cách ngang quá rộng ($dx = -16, -12$):** Hàng $y = 2$ tỏa từ gốc $(82, 1)$ sang Cảng biển với $dx = -16$ (`cai_mep_port`) và $dx = -12$ (`lach_huyen_port`).
3. **Bước nhảy ngang ở nhánh Metro và Sân bay:** `urban_rail_hanoi` nhảy $dx = 10$, `tan_son_nhat_t3` nhảy $dx = 8$.
4. **Hàng rỗng ở chốt hạ:** `VIE_synchronized_infrastructure_2030` đặt ở $y = 10$ với $dy = 2$ từ $y = 8$, để trống hàng $y = 9$.

### 1.2 Giải pháp Tối ưu Rút gần
* **Rút gọn toàn bộ nhánh về $y = 1 .. 9$:** Toàn bộ 44 focus kết thúc ở $y = 9$ thay vì $y = 10$.
* **Triệt tiêu $dy = 5$ tại `airport_master_plan`:** Neo về `VIE_hsr_groundbreaking` tại hàng $y = 5$ với $dx = 0, dy = 1$.
* **Triệt tiêu $dy = 2$ tại `synchronized_infrastructure_2030`:** Đưa lên hàng $y = 9$ ngay dưới `expressway_5000km_2030` (hàng $y = 8$) với $dy = 1$.
* **Thu hẹp độ rộng toàn nhánh:** Giảm từ span 32 ($x = 66..98$) xuống **span 22 ($x = 68..90$)**.
* **Đưa các bước nhảy ngang về $\le 4$:** Đa số các liên kết là $dx \in \{-2, 0, 2\}$.

---

## 2. Sơ đồ Kiến trúc Tổng quan Sau Rút Gọn

```text
                                VIE_doi_moi_continues
                                          │ (dx=0, dy=1)
                           VIE_infrastructure_development
                            (Phát triển Hạ tầng, x=80, y=1)
                                          │
       ┌──────────────────┬───────────────┴───────────────┬──────────────────┐
    TRỤC 1             TRỤC 2                          TRỤC 3             TRỤC 4
 CẢNG BIỂN &        ĐƯỜNG BỘ CAO TỐC &             ĐƯỜNG SẮT CAO TỐC   ĐƯỜNG SẮT ĐÔ THỊ
  LOGISTICS             CẦU HẦM                       & MẠNG LƯỚI ĐS       (METRO)
  (3 focus)            (14 focus)                       (10 focus)         (4 focus)
  x = 68..70           x = 70..76                       x = 78..82        x = 86..90
                                          │
                                       TRỤC 5
                                  CẢNG HÀNG KHÔNG &
                                 HÀNG KHÔNG DÂN DỤNG
                                      (11 focus)
                                      x = 78..84
                                          │
                                        CHỐT HẠ
                          HẠ TẦNG ĐỒNG BỘ 2030 (x=74, y=9)
```

---

## 3. Bảng Tọa độ Chi tiết 44 Focus

| Hàng (y) | Focus ID | Tọa độ Tuyệt đối (x, y) | Neo Cha (`relative_position_id`, dx, dy) | Prerequisite (Dọc) | Available (Ngang/Anh em/Thời gian) |
|:---:|---|:---:|---|---|---|
| **y = 1** | `VIE_infrastructure_development` | (80, 1) | `VIE_doi_moi_continues` (0, 1) | `VIE_doi_moi_continues` | - |
| **y = 2** | `VIE_cai_mep_port` | (68, 2) | `VIE_infrastructure_development` (-12, 1) | `VIE_infrastructure_development` | `date > 2010.12.31` |
| | `VIE_lach_huyen_port` | (70, 2) | `VIE_infrastructure_development` (-10, 1) | `VIE_infrastructure_development` | `date > 2014.12.31` |
| | `VIE_transport_strategy_2004` | (72, 2) | `VIE_infrastructure_development` (-8, 1) | `VIE_infrastructure_development` | `date > 2004.12.9` |
| | `VIE_infrastructure_breakthrough_nq13` | (76, 2) | `VIE_infrastructure_development` (-4, 1) | `VIE_infrastructure_development` | `date > 2011.12.31` |
| | `VIE_hsr_2010_reject` | (78, 2) | `VIE_infrastructure_development` (-2, 1) | `VIE_infrastructure_development` | `date > 2010.4.30` |
| | `VIE_hsr_2010_approve` | (82, 2) | `VIE_infrastructure_development` (2, 1) | `VIE_infrastructure_development` | `date > 2010.4.30` |
| | `VIE_reunification_line_upgrade` | (86, 2) | `VIE_infrastructure_development` (6, 1) | `VIE_infrastructure_development` | `date > 2009.12.31` |
| **y = 3** | `VIE_logistics_strategy` | (70, 3) | `VIE_lach_huyen_port` (0, 1) | `VIE_lach_huyen_port` | `VIE_cai_mep_port`, `date > 2017.7.31` |
| | `VIE_hai_van_tunnel` | (72, 3) | `VIE_transport_strategy_2004` (0, 1) | `VIE_transport_strategy_2004` | `date > 2005.5.31` |
| | `VIE_hcmc_trung_luong_expressway` | (74, 3) | `VIE_transport_strategy_2004` (2, 1) | `VIE_transport_strategy_2004` | `date > 2010.2.2` |
| | `VIE_can_tho_bridge` | (76, 3) | `VIE_transport_strategy_2004` (4, 1) | `VIE_transport_strategy_2004` | `date > 2010.4.23` |
| | `VIE_north_south_hsr` | (80, 3) | `VIE_hsr_2010_reject` (2, 1) | `VIE_hsr_2010_reject` OR `VIE_hsr_2010_approve` | `date > 2024.11.30` |
| | `VIE_lao_cai_haiphong_rail` | (86, 3) | `VIE_reunification_line_upgrade` (0, 1) | `VIE_reunification_line_upgrade` | `date > 2025.11.30` |
| | `VIE_hcmc_metro` | (88, 3) | `VIE_reunification_line_upgrade` (2, 1) | `VIE_reunification_line_upgrade` | `date > 2012.12.31` |
| | `VIE_urban_rail_hanoi` | (90, 3) | `VIE_reunification_line_upgrade` (4, 1) | `VIE_reunification_line_upgrade` | `date > 2021.10.31` |
| **y = 4** | `VIE_northern_expressways` | (72, 4) | `VIE_hcmc_trung_luong_expressway` (-2, 1) | `VIE_hcmc_trung_luong_expressway` | `date > 2015.12.4` |
| | `VIE_north_south_expressway` | (74, 4) | `VIE_hcmc_trung_luong_expressway` (0, 1) | `VIE_hcmc_trung_luong_expressway` | `date > 2017.11.21` |
| | `VIE_hsr_partner_japan` | (78, 4) | `VIE_north_south_hsr` (-2, 1) | `VIE_north_south_hsr` | - |
| | `VIE_hsr_partner_eu` | (80, 4) | `VIE_north_south_hsr` (0, 1) | `VIE_north_south_hsr` | - |
| | `VIE_hsr_partner_china` | (82, 4) | `VIE_north_south_hsr` (2, 1) | `VIE_north_south_hsr` | - |
| | `VIE_domestic_rail_industry` | (86, 4) | `VIE_lao_cai_haiphong_rail` (0, 1) | `VIE_lao_cai_haiphong_rail` | `date > 2025.11.30` |
| | `VIE_urban_rail_special_mechanism_nq188` | (90, 4) | `VIE_urban_rail_hanoi` (0, 1) | `VIE_urban_rail_hanoi` | `VIE_hcmc_metro`, `date > 2025.2.28` |
| **y = 5** | `VIE_expressway_regional_links` | (70, 5) | `VIE_northern_expressways` (-2, 1) | `VIE_northern_expressways` | `date > 2018.12.31` |
| | `VIE_expressway_bot` | (72, 5) | `VIE_north_south_expressway` (-2, 1) | `VIE_north_south_expressway` | `date > 2019.12.31` |
| | `VIE_expressway_public_investment` | (74, 5) | `VIE_north_south_expressway` (0, 1) | `VIE_north_south_expressway` | `date > 2019.12.31` |
| | `VIE_hsr_groundbreaking` | (80, 5) | `VIE_hsr_partner_eu` (0, 1) | `VIE_hsr_partner_japan` OR `EU` OR `China` | `date > 2026.11.30` |
| | `VIE_metro_network_2035` | (90, 5) | `VIE_urban_rail_special_mechanism_nq188` (0, 1) | `VIE_urban_rail_special_mechanism_nq188` | `date > 2028.12.31` |
| **y = 6** | `VIE_north_south_expressway_phase2` | (72, 6) | `VIE_expressway_bot` (0, 1) | `VIE_expressway_bot` | `VIE_expressway_public_investment`, `date > 2022.1.10` |
| | `VIE_airport_master_plan` | (80, 6) | `VIE_hsr_groundbreaking` (0, 1) | - | `VIE_infrastructure_development`, `date > 2008.12.31` |
| **y = 7** | `VIE_ring_roads_hanoi_hcmc` | (70, 7) | `VIE_north_south_expressway_phase2` (-2, 1) | `VIE_north_south_expressway_phase2` | `date > 2022.6.15` |
| | `VIE_expressway_3000km` | (74, 7) | `VIE_north_south_expressway_phase2` (2, 1) | `VIE_north_south_expressway_phase2` | `VIE_expressway_regional_links`, `date > 2025.11.30` |
| | `VIE_aviation_market_opening` | (78, 7) | `VIE_airport_master_plan` (-2, 1) | `VIE_airport_master_plan` | `date > 2011.12.24` |
| | `VIE_noi_bai_t2` | (80, 7) | `VIE_airport_master_plan` (0, 1) | `VIE_airport_master_plan` | `date > 2014.12.31` |
| | `VIE_long_thanh_approval` | (82, 7) | `VIE_airport_master_plan` (2, 1) | `VIE_airport_master_plan` | `date > 2015.6.30` |
| | `VIE_tan_son_nhat_t3` | (84, 7) | `VIE_airport_master_plan` (4, 1) | `VIE_airport_master_plan` | `date > 2025.4.18` |
| **y = 8** | `VIE_expressway_5000km_2030` | (74, 8) | `VIE_expressway_3000km` (0, 1) | `VIE_expressway_3000km` | `date > 2026.6.30` |
| | `VIE_socialized_airports` | (78, 8) | `VIE_aviation_market_opening` (0, 1) | `VIE_aviation_market_opening` | `date > 2017.12.31` |
| | `VIE_acv_monopoly` | (80, 8) | `VIE_aviation_market_opening` (2, 1) | `VIE_aviation_market_opening` | `date > 2017.12.31` |
| | `VIE_long_thanh_airport` | (82, 8) | `VIE_long_thanh_approval` (0, 1) | `VIE_long_thanh_approval` | `date > 2025.12.18` |
| | `VIE_dual_use_airports` | (84, 8) | `VIE_tan_son_nhat_t3` (0, 1) | `VIE_airport_master_plan` | `VIE_tan_son_nhat_t3` |
| **y = 9** | `VIE_synchronized_infrastructure_2030` | (74, 9) | `VIE_expressway_5000km_2030` (0, 1) | `VIE_expressway_5000km_2030` | `VIE_long_thanh_airport`, `date > 2029.12.31` |
| | `VIE_van_don_airport` | (78, 9) | `VIE_socialized_airports` (0, 1) | `VIE_socialized_airports` | `date > 2018.12.31` |
| | `VIE_airport_network_2030` | (80, 9) | `VIE_acv_monopoly` (0, 1) | `VIE_acv_monopoly` | `VIE_socialized_airports`, `date > 2023.5.31` |

---

## 4. Kết quả Kiểm định Kỹ thuật (HOÀN TẤT 100%)

Đã chạy kiểm tra tự động qua các script kiểm định mod:
* **Số lượng focus:** Khớp chính xác 44 / 44 focus Hạ tầng (Tổng cây: 410 focus).
* **Xung đột nội bộ (Collisions):** **0 lỗi**.
* **Xung đột ngoại vi:** **0 lỗi**.
* **Vi phạm khoảng cách ($\Delta x < 2$):** **0 lỗi**.
* **Tham chiếu tiến (`relative_position_id` forward reference):** **0 lỗi**.
* **Vi phạm độ sâu ($y_{child} \le y_{parent}$):** **0 lỗi**.
* **Trình kiểm tra tĩnh `check_static.py`:** Đạt chuẩn **90 errors, 1 warning** (khớp baseline).
