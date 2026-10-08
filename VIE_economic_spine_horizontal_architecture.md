# Nhánh Kinh tế — Kiến trúc & Bố cục Hàng ngang (Chuẩn hóa theo Cột Chính trị)

> **Tài liệu thiết kế kiến trúc và chuẩn format (05/10/2026)**  
> **Áp dụng:** Tái cấu trúc toàn bộ khối Kinh tế trong `common/national_focus/VIE_md_focus.txt`.  
> **Kế thừa:** Chuẩn bố cục "Hàng ngang" tại [VIE_focus_coding_standards.md mục 7.3](VIE_focus_coding_standards.md) và mô hình Hub-Spine của nhánh Chính trị ([Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md)).

> **Cập nhật 08/10/2026:** Nhánh công nghiệp dùng [thiết kế v17](VIE_industry_branch_redesign.md). Quy tắc hub hai hàng và chuyển mọi phụ thuộc nội bộ sang `available` trong tài liệu này không còn áp dụng cho nhánh công nghiệp. Các phần khác giữ phạm vi hiện tại.

---

## 0. Vấn đề của nhánh Kinh tế cũ & Giải pháp chuẩn hóa

| Vấn đề ở kiến trúc cũ | Giải pháp theo Chuẩn "Hàng ngang" Chính trị |
|---|---|
| **Chuỗi dọc quá sâu (4–8 tầng):** Nhánh đâm thẳng xuống dưới gây dài cây, khó bao quát, người chơi phải cuộn màn hình liên tục. | **Quy tắc Hub 2 hàng:** Mỗi mốc (Hub) quản lý một tầng chính sách. Mọi focus triển khai nằm trên **MỘT hàng ngang ngay dưới mốc (`dy = 1`)**, mốc kế tiếp nằm ở `dy = 2`. |
| **Đường nối chéo chằng chịt (Spaghetti links):** Các focus phụ thuộc lẫn nhau giữa các ngành (ví dụ: bán dẫn cần giáo dục, thép cần phụ trợ, JETP cần thiên tai) kéo dây chéo qua cả màn hình. | **Quy tắc Prerequisite vs Available:** Tuyệt đối chỉ dùng `prerequisite` cho liên kết Cha $\rightarrow$ Con dọc. Mọi phụ thuộc ngang hàng (anh em) hoặc chéo ngành chuyển 100% sang `available = { has_completed_focus = ... }`. |
| **Neo xa / Neo lung tung:** Nhiều focus neo vào một gốc xa (như `doi_moi_continues` x=80) hoặc neo chéo hàng làm lệch lưới tọa độ. | **Neo cha trực tiếp (`relative_position_id = cha`):** Khai báo cha trước, con sau. Con nằm tại $x = 0$ (thẳng dưới) hoặc $\pm 2, \pm 4$ quanh cha. |
| **Ô quá sát nhau hoặc đè ô:** Không đồng nhất khoảng cách $\Delta x$. | **Chuẩn lưới $\Delta x \ge 2$:** Khoảng cách tối thiểu giữa 2 focus cùng hàng là 2 ô, căn giữa đối xứng quanh mốc Hub. |
| **Lẫn lộn tầm vĩ mô với dự án cụ thể:** Quá nhiều focus tiểu dự án (hầm, trạm, liên doanh). | **Gộp & tinh gọn (theo Báo cáo Tinh gọn 03/10/2026):** Giữ lại các luật, nghị quyết, chiến lược quốc gia và ngã rẽ lịch sử; dự án nhỏ chuyển thành mô tả hoặc decision. |

---

## 1. Phân rã 4 Trục chức năng của Khối Kinh tế

Nhánh Kinh tế phân bố bên phải nhánh Chính trị, tỏa ra từ gốc chung `VIE_doi_moi_continues` (hoặc các Hub cấp 1 độc lập) thành **4 Trục chiến lược**:

```text
                               VIE_doi_moi_continues
                                         │
        ┌───────────────────┬────────────┴───────┬───────────────────┐
      TRỤC 1              TRỤC 2               TRỤC 3              TRỤC 4
  DOANH NGHIỆP        TÀI CHÍNH &          NĂNG LƯỢNG &        CÔNG NGHIỆP HÓA
   & THƯƠNG MẠI        NGÂN HÀNG            TÀI NGUYÊN           & CÔNG NGHỆ
   (Luật DN 2000)    (NHNN & DNNN)        (PVN & Vinacomin)     (CNH-HĐH ĐH IX)
```

*(Lưu ý: Khối **Kết cấu Hạ tầng** `VIE_infrastructure_development` đã được chuẩn hóa riêng theo tài liệu [VIE_infrastructure_branch_design.md](VIE_infrastructure_branch_design.md) nên đứng độc lập bên cạnh).*

---

## 2. Chi tiết Kiến trúc & Bố cục từng Trục

### 2.1 TRỤC 1: Doanh nghiệp, Thương mại & Thị trường vốn
* **Gốc (Hub 1):** `VIE_enterprise_law` (Luật Doanh nghiệp 2000 - cột mốc mở cửa kinh tế tư nhân).

#### Cấu trúc Hub & Hàng ngang:
1. **Hàng 1 (Nền tảng mở cửa, dy = 1 dưới `enterprise_law`):**
   * `VIE_equitization_soes` (Cổ phần hóa DNNN đợt 1, $dx = -3$)
   * `VIE_investment_law_2005` (Luật Đầu tư 2005 - Mốc Hub kinh tế tư nhân, $dx = -1$)
   * `VIE_bilateral_trade_agreement_usa` (Hiệp định BTA Việt - Mỹ, $dx = 1$)
   * `VIE_rice_export_power` (Nông nghiệp hàng hóa & xuất khẩu gạo, $dx = 3$)
2. **Hàng 2 (Kinh tế tư nhân & Nông thôn mới, dy = 1 dưới `investment_law_2005` & `rice_export_power`):**
   * Dưới `investment_law_2005`:
     * `VIE_household_business` (Kinh tế hộ cá thể, $dx = -2$)
     * `VIE_private_champions` (Tập đoàn tư nhân lớn, $dx = 0$)
     * `VIE_private_sector_engine` (Động lực kinh tế tư nhân - NQ 10, $dx = 2$, cần `available = private_champions`)
   * Dưới `rice_export_power`:
     * `VIE_new_rural_development` (Nông thôn mới, $dx = -1$)
     * `VIE_land_law_reform` (Sửa đổi Luật Đất đai, $dx = 1$)
3. **Hàng 3 (Hội nhập toàn cầu & FDI, dy = 1 dưới mốc `fdi_attraction`):**
   * **Mốc Hub:** `VIE_fdi_attraction` (Thu hút FDI thế hệ mới)
   * **Hàng con ngang:**
     * `VIE_wto_negotiations` (Gia nhập WTO, $dx = -3$)
     * `VIE_wto_reforms` (Cải cách hậu WTO, $dx = -1$, cần `available = wto_negotiations`)
     * `VIE_cptpp_member` (Hiệp định CPTPP, $dx = 1$)
     * `VIE_evfta` (Hiệp định EVFTA, $dx = 3$)
4. **Hàng 4 (Ngã rẽ Đặc khu kinh tế 2018, dy = 1 dưới `sez_three_zones`):**
   * **Mốc Hub:** `VIE_sez_three_zones` (Đề án 3 Đặc khu: Vân Đồn, Bắc Vân Phong, Phú Quốc)
   * **Ngã rẽ loại trừ nhau:**
     * `VIE_sez_postpone` (Hoãn luật theo nguyện vọng dư luận — *Lịch sử*, $dx = -2$)
     * `VIE_sez_pass_99` (Thông qua ưu đãi thuê đất 99 năm — *Giả định*, $dx = 2$)
   * **Hàng tiếp nối (dy = 1 dưới mỗi lựa chọn):**
     * Dưới `sez_postpone`: `VIE_island_special_zones` (Khu kinh tế ven biển chọn lọc)
     * Dưới `sez_pass_99`: `VIE_sez_strategic_investors` (Thu hút đại bàng tài phiệt)

---

### 2.2 TRỤC 2: Tài chính, Ngân hàng & Sở hữu Nhà nước
* **Gốc (Hub 2):** `VIE_state_bank_modernization` (Hiện đại hóa Ngân hàng Nhà nước).

#### Cấu trúc Hub & Hàng ngang:
1. **Hàng 1 (Điều hành tiền tệ & Thị trường vốn, dy = 1 dưới `state_bank_modernization`):**
   * `VIE_cashless_payments` (Thanh toán không dùng tiền mặt, $dx = -4$)
   * `VIE_hose_exchange` (Sàn chứng khoán HOSE, $dx = -2$)
   * `VIE_corporate_bond_reform` (Thị trường trái phiếu doanh nghiệp, $dx = 0$)
   * `VIE_fight_inflation` (Kiềm chế lạm phát vĩ mô, $dx = 2$)
   * Ngã rẽ Vàng 2012 (loại trừ nhau):
     * `VIE_gold_monopoly_2012` (Nghị định 24 - Độc quyền vàng miếng SJC — *Lịch sử*, $dx = 4$)
     * `VIE_gold_free_market` (Thị trường vàng tự do — *Giả định*, $dx = 6$)
2. **Hàng 2 (Sở hữu Nhà nước & Tái cơ cấu DNNN, dy = 1 dưới `state_conglomerates`):**
   * **Mốc Hub:** `VIE_state_conglomerates` (Tập đoàn kinh tế Nhà nước)
   * **Hàng con:**
     * `VIE_scic` (Thành lập Tổng công ty Đầu tư và Kinh doanh Vốn Nhà nước SCIC, $dx = -2$)
     * Ngã rẽ Cổ phần hóa 2017:
       * `VIE_soe_gradual_restructuring` (Cổ phần hóa thận trọng, giữ vai trò chủ đạo — *Lịch sử*, $dx = 0$)
       * `VIE_soe_rapid_divestment` (Thoái vốn nhanh, tư nhân hóa triệt để — *Giả định*, $dx = 2$)
     * `VIE_soe_governance` (Quản trị DNNN theo chuẩn OECD, $dx = 4$)
3. **Hàng 3 (Tái cơ cấu hệ thống Ngân hàng & Xử lý Nợ xấu, dy = 1 dưới `restructure_banking`):**
   * **Mốc Hub:** `VIE_restructure_banking` (Đề án cơ cấu lại hệ thống các TCTD)
   * **Hàng con ngang:**
     * `VIE_vamc` (Thành lập Công ty VAMC - Mua bán nợ xấu, $dx = -3$)
     * `VIE_cross_ownership_crackdown` (Chống sở hữu chéo ngân hàng, $dx = -1$)
     * Ngã rẽ Ngân hàng 0 đồng 2015:
       * `VIE_zero_dong_acquisition` (Mua lại bắt buộc 0 đồng — *Lịch sử*, $dx = 1$)
       * `VIE_bank_bankruptcy` (Cho phép ngân hàng phá sản theo thị trường — *Giả định*, $dx = 3$)
     * `VIE_compulsory_transfer_2024` (Chuyển giao bắt buộc ngân hàng yếu kém 2024, dy=1 dưới `zero_dong_acquisition`)
4. **Hàng 4 (Đích đến hội tụ Tài chính, dy = 2):**
   * `VIE_international_financial_centre` (Trung tâm Tài chính Quốc tế TP.HCM / Đà Nẵng, $dx = -2$)
   * `VIE_investment_grade` (Đạt mức xếp hạng tín nhiệm đầu tư Baa3/BBB, $dx = 2$)

---

### 2.3 TRỤC 3: Năng lượng & Tài nguyên Khoáng sản
* **Hai Hub cấp 1:** `VIE_vinacomin_founding` (Khoáng sản/Vinacomin) và `VIE_petrovietnam_expansion` (Dầu khí/Điện/PVN).

#### Cấu trúc Hub & Hàng ngang:
1. **Khối Khoáng sản (Dưới `vinacomin_founding`):**
   * Ngã rẽ Bauxite Tây Nguyên 2009:
     * `VIE_bauxite_tay_nguyen` (Tiếp tục khai thác bauxite — *Lịch sử*, $dx = -2$)
     * `VIE_bauxite_suspend` (Dừng dự án vì môi trường & an ninh — *Giả định*, $dx = 2$)
   * Hàng tài nguyên chiến lược (dy = 1):
     * `VIE_rare_earths` (Khai thác đất hiếm, $dx = -3$)
     * `VIE_than_quang_ninh` (Than Quảng Ninh - An ninh năng lượng, $dx = -1$)
     * `VIE_nui_phao_tungsten` (Vonfram Núi Pháo, $dx = 1$)
     * `VIE_thach_khe_mine_start` (Quặng sắt Thạch Khê, $dx = 3$)
2. **Khối Dầu khí & Lọc hóa dầu (Dưới `petrovietnam_expansion`):**
   * Hàng hạ nguồn & chế biến (dy = 1):
     * `VIE_dung_quat_refinery` (Nhà máy Lọc dầu Dung Quất, $dx = -3$)
     * `VIE_nghi_son_refinery` (Lọc hóa dầu Nghi Sơn, $dx = -1$)
     * `VIE_petrolimex_downstream_network` (Mạng lưới phân phối xăng dầu Petrolimex, $dx = 1$)
     * `VIE_strategic_petroleum_reserve` (Dự trữ xăng dầu quốc gia, $dx = 3$)
3. **Khối Lưới điện & Năng lượng tái tạo (Dưới `son_la_dam` & `power_plan_8`):**
   * `VIE_son_la_dam` (Thủy điện Sơn La) $\rightarrow$ Hàng 1 (dy = 1): `VIE_500kv_grid` (Mạch 500kV), `VIE_coal_power` (Nhiệt điện than).
   * **Mốc Hub:** `VIE_power_plan_8` (Quy hoạch Điện VIII) $\rightarrow$ Hàng 2 (dy = 1):
     * Ngã rẽ Điện mặt trời: `VIE_solar_boom` (Giá FIT ưu đãi) ⟷ `VIE_solar_auction` (Đấu thầu giá điện)
     * Ngã rẽ Điện hạt nhân Ninh Thuận: `VIE_shelve_nuclear` (Tạm dừng 2016 — *Lịch sử*) ⟷ `VIE_build_nuclear_plant` (Quyết tâm xây dựng)
     * `VIE_revive_nuclear` (Khởi động lại điện hạt nhân 2024, dy = 1 dưới `shelve_nuclear`)
     * `VIE_offshore_wind` (Điện gió ngoài khơi)
     * `VIE_dppa_market_reform` (Cơ chế mua bán điện trực tiếp DPPA)
   * **Hội tụ Capstone Năng lượng (dy = 2):**
     * `VIE_jetp_partnership` (Quan hệ đối tác chuyển dịch năng lượng bình đẳng JETP)
     * `VIE_net_zero_2050` (Cam kết phát thải ròng bằng 0 - COP26)

---

### 2.4 TRỤC 4: Công nghiệp hóa và công nghệ — v17

Thiết kế hiện hành: [VIE_industry_branch_redesign.md](VIE_industry_branch_redesign.md).
Nhánh có 39 focus (35 ID cũ và 4 chính sách mới), x=124..140, y=1..9.

- Formosa, Hòa Phát, Samsung, Intel và công nghiệp hỗ trợ có lối vào độc lập.
- Đóng tàu, dệt may, thép, ô tô và điện tử phát triển song song.
- Trung tâm chế tạo cần phụ trợ AND (Samsung OR China+1).
- China+1 có cặp lựa chọn FDI; Apple cần một lựa chọn và trung tâm chế tạo.
- Bán dẫn có cặp lựa chọn hỗ trợ; thiết kế, đóng gói, đào tạo cùng mở sau một lựa chọn.
  Fab thử nghiệm yêu cầu đủ cả ba, hai đường có tổng hỗ trợ bằng nhau.
- NQ23 dẫn đến NQ29; quỹ đầu tư và năng suất song song, không buộc khu công nghiệp
  sinh thái hoặc quỹ hỗ trợ thành điều kiện của toàn bộ chính sách.
- Đích cuối cần năng suất, ≥45 điểm nội địa hóa và ≥3/6 nhóm; không khóa năm với
  người chơi, không bắt buộc bán dẫn hoặc xe điện.

Quan hệ nội bộ hiện trên cây bằng prerequisite AND/OR. `available` dành cho điều
kiện ngoài nhánh, ngày của dự án có tên, cờ xử lý sự kiện và ngưỡng năng lực.

---

## 3. Bảng Ánh xạ Chuyển đổi: Prerequisite $\rightarrow$ Available (Cắt đường nối rối)

Bảng lịch sử dưới đây áp dụng cho các nhánh chưa tái thiết kế. Công nghiệp v17 dùng prerequisite cho phụ thuộc nội bộ; chỉ giữ điều kiện ngoài nhánh trong `available`:

| Focus | Cha trực tiếp (`prerequisite`) | Điều kiện logic chuyển sang `available = {}` |
|---|---|---|
| `VIE_fdi_attraction` | `VIE_bilateral_trade_agreement_usa` | `available = { has_completed_focus = VIE_equitization_soes }` (thay vì 2 prerequisite kéo chéo) |
| `VIE_wto_reforms` | `VIE_fdi_attraction` | `available = { has_completed_focus = VIE_wto_negotiations }` |
| `VIE_chip_engineers` | OR hai focus ưu tiên bán dẫn (v17) | `available = { has_completed_focus = VIE_higher_education_law }` (cắt dây chéo sang nhánh Giáo dục) |
| `VIE_net_zero_2050` | `VIE_power_plan_8` | `available = { has_completed_focus = VIE_jetp_partnership }` |
| `VIE_cptpp_member` | `VIE_fdi_attraction` | `available = { date > 2018.1.1 }` |
| `VIE_evfta` | `VIE_fdi_attraction` | `available = { date > 2020.6.30 }` |
| `VIE_tier1_vendor_localization` (v17) | `VIE_supporting_industries` | Không cần Samsung; không còn khóa năm |
| `VIE_semiconductor_ambition` (v17) | `VIE_intel_hcmc` | Không còn khóa năm của người chơi |
| `VIE_revive_nuclear` | `VIE_shelve_nuclear` | `available = { date > 2024.1.1 has_completed_focus = VIE_power_plan_8 }` |

---

## 4. Danh sách Các Cặp Ngã rẽ Lịch sử (Loại trừ nhau)

Tất cả các ngã rẽ đều sử dụng `mutually_exclusive = { focus = ... }` và đặt trên cùng một hàng ($dy = 1$ dưới Hub chung):

1. **Bauxite Tây Nguyên 2009:** `VIE_bauxite_tay_nguyen` $\longleftrightarrow$ `VIE_bauxite_suspend` (Cha: `VIE_vinacomin_founding`).
2. **Thị trường Vàng 2012:** `VIE_gold_monopoly_2012` $\longleftrightarrow$ `VIE_gold_free_market` (Cha: `VIE_state_bank_modernization`).
3. **Ngân hàng 0 đồng 2015:** `VIE_zero_dong_acquisition` $\longleftrightarrow$ `VIE_bank_bankruptcy` (Cha: `VIE_restructure_banking`).
4. **Tái cơ cấu DNNN 2017:** `VIE_soe_gradual_restructuring` $\longleftrightarrow$ `VIE_soe_rapid_divestment` (Cha: `VIE_state_conglomerates`).
5. **Giá điện mặt trời 2017:** `VIE_solar_boom` $\longleftrightarrow$ `VIE_solar_auction` (Cha: `VIE_power_plan_8`).
6. **Đặc khu kinh tế 2018:** `VIE_sez_postpone` $\longleftrightarrow$ `VIE_sez_pass_99` (Cha: `VIE_sez_three_zones`).
7. **Điện hạt nhân Ninh Thuận:** `VIE_shelve_nuclear` $\longleftrightarrow$ `VIE_build_nuclear_plant` (Cha: `VIE_ninh_thuan_nuclear`).
8. **Chiến lược FDI v17:** `VIE_fdi_fast_track` $\longleftrightarrow$ `VIE_fdi_technology_screening` (Cha: `VIE_china_plus_one`).
9. **Hỗ trợ bán dẫn v17:** `VIE_chip_design_packaging_priority` $\longleftrightarrow$ `VIE_chip_pilot_fab_priority` (Cha: `VIE_semiconductor_ambition`).

---

## 5. Quy chuẩn Format Code một Focus Block mẫu

Mỗi focus trong nhánh Kinh tế khi áp dụng vào code phải tuân thủ nghiêm ngặt định dạng chuẩn MD4:

```pdx
focus = {
	id = VIE_equitization_soes
	icon = economic_privatisation

	x = -3
	y = 1
	relative_position_id = VIE_enterprise_law

	cost = 7

	prerequisite = { focus = VIE_enterprise_law }

	search_filters = { FOCUS_FILTER_ECONOMY }

	available = {
		date > 2001.1.1
	}

	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: Focus VIE_equitization_soes"
		increase_economic_growth = yes
		add_political_power = 50
		VIE_bop_reform_small = yes
	}

	ai_will_do = { base = 80 }
}
```

---

## 6. Trạng thái Triển khai Code vào `VIE_md_focus.txt` (HOÀN TẤT 100%)

Toàn bộ 4 Trục Kinh tế (110 focus) đã được chuyển đổi hoàn toàn sang chuẩn Bố cục Hàng ngang:

* [x] **Trục 1:** Doanh nghiệp, Thương mại & Thị trường vốn (`VIE_enterprise_law`): 23 focus (x = 27..39, y = 1..8).
* [x] **Trục 2:** Tài chính, Ngân hàng & Sở hữu Nhà nước (`VIE_state_bank_modernization`): 23 focus (x = 45..65, y = 1..6).
* [x] **Trục 3:** Năng lượng & Tài nguyên Khoáng sản (`VIE_vinacomin_founding` & `VIE_petrovietnam_expansion`): 29 focus (x = 102..122, y = 1..7).
* [x] **Trục 4:** Công nghiệp hóa – Hiện đại hóa & Công nghệ cao (`VIE_industrialization_strategy`): 35 focus (x = 124..140, y = 1..7).

### Kết quả kiểm định kỹ thuật (04/10/2026):
* **Forward references (`relative_position_id`):** 0 lỗi (toàn bộ file tuân thủ nghiêm ngặt Cha khai báo trước Con).
* **Đè ô / Xung đột tọa độ (Collisions):** 0 lỗi (toàn bộ 410 focus của cây mod có tọa độ tuyệt đối phân biệt duy nhất).
* **Khoảng cách hàng ngang:** $\Delta x \ge 2$ tại mọi hàng, 0 vi phạm khoảng cách.
* **Đường nối chéo (Spaghetti):** 0 đường chéo (chuyển toàn bộ phụ thuộc chéo/ngang sang `available = { has_completed_focus = ... }`).
* **Trình kiểm tra tĩnh `check_static.py`:** Baseline giữ vững 90 errors, 4 warnings (đã giải quyết triệt để cảnh báo `WARN VIE_intel_hcmc`).

