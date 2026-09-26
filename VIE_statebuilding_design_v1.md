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
