# Lực lượng đặc biệt (Đặc công · Lính dù · HQ Đánh bộ) — đánh giá báo cáo và kế hoạch code

> Đối tượng đọc: tác giả mod. Đối chiếu ngày 05/10/2026 với `main` @ `571afe3`.
> Báo cáo gốc: "BÁO CÁO THIẾT KẾ & XÂY DỰNG EFFECT — Nhánh Special Forces".
> Quy ước đối chiếu: `VIE_focus_coding_standards.md`, nhánh lf/nf/airf đang chạy, `tools/audit/*`.

---

## 0. Quyết định của bạn và kết quả bước 0 (cập nhật 05/10/2026)

**Quyết định — các mục dưới đây bị ghi đè nếu mâu thuẫn:**

| Câu hỏi | Quyết định | Hệ quả |
|---|---|---|
| Vị trí | Trục độc lập, `prerequisite = { focus = VIE_modernize_vpa }`, không phụ thuộc lf | `VIE_sf_command` không còn trỏ `VIE_lf_command_reform_1`. Đường prerequisite từ `VIE_modernize_vpa` (202,1) sang cụm (154,9) cắt qua khối lf; nếu xem trong game thấy rối thì phương án dự phòng là đặt cụm dưới các trục quân sự (y ≥ 17 tuyệt đối). Chốt ở bước 3 |
| Lính dù | **Bỏ** | Còn 11 focus: 1 `VIE_sf_command` + 2 root con (`sapper`, `marine`) + 6 trụ cột + 2 capstone. Bỏ mọi dòng `para_*` và template Dù. Tổng focus 381 → 392. Hai root con đặt ở x = -4 và +4 so với `VIE_sf_command` |
| Ngân sách | Các focus **trang bị** có trừ tiền | `sapper_equipment` và `marine_equipment` gọi `set_temp_variable = { treasury_change = -5 }` + `modify_treasury_effect = yes` (đủ ngưỡng ~5 bn của chuẩn, nên hai focus này mới có guard `bankruptcy_incoming_collapse` trong `ai_will_do`). Các focus khác không trừ, không guard. Mức -5 là điểm khởi đầu, chỉnh ở bước 6 |

Hệ quả cho tổng modifier: `special_forces_cap` +0.03 (command 0.01 + 2 capstone 0.01). Hai nhánh còn lại giữ nguyên bảng 2.4.

**Kết quả bước 0** — đối chiếu với repo MD `main` (`common/units/MD_land_units.txt`, `MD_division_support.txt`, `common/technologies/infantry.txt`, `custom_tech.txt`), tải về từ GitHub vì máy này không có bản cài MD/HOI4:

| Hạng mục | Kết quả |
|---|---|
| `Special_Forces` | Có (`MD_land_units.txt:1582`), là regiment, `can_be_parachuted`, `marines`, `rangers`. Mở bởi tech ở `infantry.txt:76` |
| `L_Ranger_Bat` | **Có**, là regiment (`MD_land_units.txt:1449`), mở bởi `custom_tech.txt:208`. Đính chính mục A3: nó hợp lệ nhưng phải để ở `regiments`, không phải `support` |
| `SP_Arty_Bat` | Là regiment (`MD_land_units.txt:1304`). Đúng như mục A3 |
| `L_Engi_Comp` | Có, nằm trong `MD_division_support.txt:240`, đặt trong `support` là đúng |
| `Mech_Marine_Bat`, `Mot_Marine_Bat`, `L_arm_Bat` | Có; mở bởi `infantry.txt:55`, `infantry.txt:438` và tech giáp |
| `L_Air_Inf_Bat` | Có; không cần nữa vì bỏ nhánh Dù |
| `CAT_special_forces_equipment`, `CAT_landing_craft` | Có trong `MD_all_CATS.json` |
| `add_mastery`, `has_selected_land_grand_doctrine` | Đã dùng sẵn trong `VIE_md_focus.txt` và `VIE_lf_xp_*`, không cần kiểm thêm |
| Dấu của `training_time_factor` | Chưa xác minh được ngoài game. Theo ngữ nghĩa vanilla, giá trị âm là huấn luyện nhanh hơn; vẫn giữ mục kiểm ở bước 8 |

**Rủi ro mới phát hiện:** `Special_Forces`, `L_Ranger_Bat`, `Mech_Marine_Bat`, `Mot_Marine_Bat` đều do **tech mở**. Template dùng chúng được tạo ra thì hợp lệ, nhưng `create_unit` có thể sinh sư đoàn gồm battalion chưa mở khóa nếu VIE chưa có tech đó vào lúc hoàn thành focus. Ở bước 8 phải thử: hoàn thành capstone trên save chưa nghiên cứu các tech này. Nếu lỗi, thêm `set_technology` cho đúng tech trong reward (tên tech lấy từ `infantry.txt`, bước 2).

Template Đặc công chốt: 6× `Special_Forces` (x0–1, y0–2) + `support L_Engi_Comp`; bỏ `L_Ranger_Bat` khỏi `support`. Template Đánh bộ: như bảng 2.5.

---

## 1. Kết luận

**Ý tưởng thiết kế giữ được** (3 binh chủng × kim tự tháp 3→1, ID `VIE_sf_*`, ba trụ cột Huấn luyện / Trang bị / Chỉ huy). **Code trong báo cáo không dán thẳng được**: nó viết cho cấu trúc cũ (v≤10) mà repo đã bỏ. Có 1 lỗi chặn (root cha không tồn tại) và 5 lỗi sẽ cho ra bug hoặc làm hỏng quy ước. Phần còn lại là lệch phong cách, sửa khi viết lại.

### 1.1 Lỗi chặn / lỗi hành vi

| # | Báo cáo nói | Thực tế trong repo | Hậu quả nếu dán thẳng | Cách sửa |
|---|---|---|---|---|
| **A1** | Root cha `VIE_special_forces` (con của `VIE_tank_modernization`) "đã tồn tại" | Cả hai chỉ còn trong `v11_removed_military_all_subbranches.txt`. `VIE_md_focus.txt` không có. Quân sự hiện chỉ có `VIE_modernize_vpa` → `VIE_lf_*` / `VIE_nf_*` / `VIE_airf_*` | `relative_position_id` và `prerequisite` trỏ focus không tồn tại; `live.py` báo lỗi, 3 root con không hiện | Tạo root cha mới `VIE_sf_command`, gắn vào `VIE_lf_command_reform_1` (mục 2.2) |
| **A2** | `category = CAT_special_forces`, `CAT_marine` | Không có trong `tools/audit/md_ref/MD_all_CATS.json`. Có `CAT_special_forces_equipment`, `CAT_landing_craft`, `CAT_transport_helicopters`. Không có `CAT_marine` | `add_tech_bonus` im lặng không tác dụng | Dùng 3 category thật; thêm bước đối chiếu như `air_effects_v2_check.py` |
| **A3** | `SP_Arty_Bat`, `L_Ranger_Bat` đặt trong `support = {}` | Ở OOB gốc MD (`VIE_2000_nsb.txt`, "Naval Infantry Brigade") `SP_Arty_Bat` là **regiment** (x=3). `L_Ranger_Bat` không xuất hiện trong dữ liệu MD đang có (chỉ thấy `L_Ranger_Recce_Comp`) | Template sai → engine bỏ battalion hoặc lỗi load | Sapper: chỉ dùng tên đã thấy trong OOB MD. Marine: sao đúng khuôn MD. Xác minh tên với `common/units` của MD trước khi code (mục 4, bước 0) |
| **A4** | Lính dù = toàn `Special_Forces` | MD tự dựng "Special Forces Brigade" = 3× `Special_Forces` + 2× `L_Air_Inf_Bat`. `L_Air_Inf_Bat` mới là bộ binh đường không | Nhánh Dù không khác nhánh Đặc công | Template Dù dùng `L_Air_Inf_Bat` làm thân |
| **A5** | `army_experience = 10` đứng riêng, rồi lại `if/else … else = { army_experience = 10 }` | Mẫu của repo là helper `VIE_lf_xp_10/15/20` (`VIE_md_effects_p17.txt:34`) và `VIE_nf_xp_*` | Người không chọn học thuyết nhận **gấp đôi** XP; người chọn thì không | Dùng helper, mỗi focus một lần |
| **A6** | Tooltip `supply_consumption_factor_tt`, `recon_factor_tt`, `terrain_penalty_reduction_tt` "đã tồn tại" | Repo dùng `VIE_tt_supply_consumption_factor` (có). Không có key `VIE_tt_recon_factor`, `VIE_tt_terrain_penalty_reduction` trong `localisation/` (`planning_speed_tt` có dùng ở focus hiện hành, nhiều khả năng từ MD base, chưa xác minh) | Tooltip hiện nguyên tên key | Thêm 2 key mới vào `VIE_md_vi_tt_l_english.yml`, đổi tên key supply |

### 1.2 Lệch quy ước (sửa khi viết lại, không gây crash)

| # | Báo cáo | Quy ước đang chạy |
|---|---|---|
| B1 | Effect viết inline trong từng focus | Focus chỉ gọi `VIE_<nhánh>_<mã>_reward = yes`; effect nằm ở `common/scripted_effects/` (lf: `VIE_md_effects_p17.txt`, nf: `…_nav_force.txt`, airf: `…_air_force.txt`) kèm `VIE_<nhánh>_refresh` (`force_update_dynamic_modifier`) và `VIE_nf_dm_tt` cho tooltip |
| B2 | `cost = 10` viết tường minh | Bỏ khi bằng 10 (coding standards mục 3) |
| B3 | Icon `army_officers_communist`, `focus_generic_buy_guns`, `GFX_focus_generic_paratrooper`… | Mỗi focus có `GFX_focus_VIE_<id>` trong `interface/VIE_md_focus_icons.gfx`, sinh bằng `tools/build_vie_focus_icons.py` |
| B4 | `ai_will_do = { base = 55–70 }` không guard | lf/nf/airf dùng `base ≈ 60` + `factor = 0 has_active_mission = bankruptcy_incoming_collapse`. Chuẩn nói chỉ guard khi focus thật sự tiêu tiền |
| B5 | Capstone tạo sư đoàn ở `capital_scope` (Hà Nội, state 522, nội địa) | Đơn vị Đánh bộ cần xuất hiện ở state ven biển (519 Nam Bộ / Nha Trang) |
| B6 | Giá trị modifier +0.04…+0.05 (recon, night attack, terrain, planning) | lf quanh +0.01…+0.035 mỗi node (`VIE_md_effects_p17.txt`). Giá trị trong báo cáo gấp khoảng 2× |
| B7 | "Tổng `special_forces_cap` 0.15 nằm dưới trần" | Không có trần nào được kiểm chứng: `lf_balance.py` và `nf_balance.py` không đụng `special_forces_cap`. Hiện chưa focus nào dùng nó, nên 0.15 là một con số chưa ai kiểm |
| B8 | Marine: `VIE_af_naval_invasion_capacity` +1 ở trụ Chỉ huy **và** +1 ở capstone | `VIE_nf_g3_reward` và `VIE_nf_g4_reward` đã cộng +1 mỗi cái. Thêm +2 nữa là tổng 4 |
| B9 | Dùng `has_selected_naval_grand_doctrine` | Đã có `VIE_nf_xp_*`, dùng helper thay vì gọi trigger trần |
| B10 | Capstone gom: template + create_unit + 2 biến + 2 mastery | Chuẩn: tối đa 5 hiệu ứng vĩnh viễn mỗi focus; tách vào scripted effect cho gọn |
| B11 | Chèn "ngay sau `VIE_special_forces`" | Không còn vị trí đó. Chèn sau `VIE_lf_force_complete` (kết thúc khối lf, trước header `TRUC 3 KHONG QUAN`) |

### 1.3 Những điểm báo cáo **đúng và giữ nguyên**

- Cấu trúc 3 trụ cột → 1 capstone, AND-prerequisite bằng 3 khối `prerequisite` riêng.
- Anchor khai báo trước dependent (khớp luật forward-ref ở coding standards 7.2).
- Dùng lại key `VIE_af_special_forces_cap`, `VIE_af_naval_invasion_*`, `VIE_af_dig_in_speed_factor`, `VIE_af_army_speed_factor`… — tất cả đã nằm trong `VIE_md_dynamic_modifiers.txt`, nên không phải đổi định nghĩa dynamic modifier.
- `VIE_tt_special_forces_cap`, `VIE_tt_land_night_attack`, `VIE_tt_dig_in_speed_factor`, `VIE_tt_army_speed_factor`, `VIE_tt_naval_invasion_*`, `VIE_tt_training_time_factor` có thật trong `VIE_md_vi_tt_l_english.yml`.
- Template `Mech_Marine_Bat` / `Mot_Marine_Bat` / `L_arm_Bat` có trong OOB MD.

---

## 2. Thiết kế đã chỉnh

### 2.1 Cấu trúc (16 focus = 1 root cha + 3 root con + 9 trụ cột + 3 capstone)

```
VIE_lf_command_reform_1   (có sẵn)
        │
   VIE_sf_command                      ← root cha MỚI (báo cáo thiếu)
   ┌────────┼────────┐
sapper     para    marine              ← 3 root con
 3 trụ      3 trụ    3 trụ
   └ capstone   └ capstone   └ capstone
```

Lý do gắn vào `VIE_lf_command_reform_1`: đây là Cải cách bộ chỉ huy I của Trục 3, mở hướng phát triển lực lượng và người chơi chạm tới sau 5 focus. Gắn vào `VIE_lf_force_complete` (y=15) thì nhánh đặc biệt mở quá muộn. Không dùng `mutually_exclusive`: ba binh chủng không loại trừ nhau, và không đọc cờ `VIE_lf_regular/mobile/depth` (giữ quy ước Trục 3 không phụ thuộc chéo).

### 2.2 Tọa độ (tuyệt đối tính từ file hiện tại; viết trong code là tương đối theo `VIE_modernize_vpa` = (202, 1))

Vùng trống: khối lf chiếm x 174…186, y 2…15; kinh tế chiếm x ≤ 170 nhưng chỉ ở y ≤ 7. Bên trái lf, **x 140…172, y ≥ 8 là trống**.

| Focus | `relative_position_id` | x | y | Ghi chú |
|---|---|---|---|---|
| `VIE_sf_command` | `VIE_modernize_vpa` | -48 | 8 | abs (154, 9). Prerequisite `VIE_lf_command_reform_1` (180, 6) |
| `VIE_sf_sapper` | `VIE_sf_command` | -8 | 1 | |
| `VIE_sf_para` | `VIE_sf_command` | 0 | 1 | |
| `VIE_sf_marine` | `VIE_sf_command` | 8 | 1 | |
| `VIE_sf_<x>_training` | root con | -2 | 1 | |
| `VIE_sf_<x>_equipment` | root con | 0 | 1 | |
| `VIE_sf_<x>_command` | root con | 2 | 1 | |
| `VIE_sf_<x>_elite` | root con | 0 | 2 | |

Thay đổi so với báo cáo: khoảng cách giữa 3 root con từ 10 → 8 (cụm rộng khoảng 24 cột, từ x=142 đến 166, vẫn nằm gọn trước x=170); tọa độ tương đối với root cha **mới**. Hai cột hàng xóm gần nhất: lf (x ≥ 174) và `VIE_ageing_society` (170, 2) — cách xa. Hạn chế: đường prerequisite từ `lf_command_reform_1` sang root cha dài khoảng 26 cột. Nếu nhìn xấu, dịch cả cụm sang phải đến sát x=170 (marine ở 168) vẫn không đè.

Thứ tự khai báo trong file: `sf_command` → `sf_sapper`, `sf_para`, `sf_marine` → các trụ cột → các capstone. Chạy `tools/audit/audit.py` xác nhận 0 forward-ref và 0 trùng tọa độ.

### 2.3 Nội dung, lore và nguồn

Giữ nguyên bảng tên và `desc` của báo cáo (mục 1.2 của báo cáo). Hai điều chỉnh:

1. Gắn nhãn nguồn theo kiểu các báo cáo lục quân/hải quân đang dùng: `(THẬT)` cho dữ kiện kiểm chứng, `(ĐỀ XUẤT)` cho phần giả định. Đặc công và Hải quân đánh bộ có nền lịch sử rõ (Bộ Tư lệnh Đặc công, Lữ đoàn HQĐB 101/147). **Lính dù**: tôi không có nguồn xác nhận quân đội Việt Nam có lữ đoàn dù thường trực; nhánh này nên gắn `(ĐỀ XUẤT)` và `desc` nói rõ là hướng phát triển giả định cho tới khi bạn tra được nguồn.
2. `desc` của `VIE_nf_amphibious_fleet` đã ghi *"Lực lượng hải quân đánh bộ thuộc nhánh khác"* — nhánh Marine ở đây chính là "nhánh khác" đó, nên không cần prerequisite chéo sang nf.

### 2.4 Effect (đã thu nhỏ theo thang lf)

Quy ước: mọi focus gọi `VIE_sf_<mã>_reward`, gồm các modifier bên dưới + XP helper + `VIE_sf_refresh` (+ `VIE_sf_dm_tt`). Biến đều là `VIE_af_*` đã có trong dynamic modifier.

| Focus | Modifier (cộng vào biến) | Khác |
|---|---|---|
| `sf_command` | `special_forces_cap` +0.01 | `VIE_lf_xp_10`, `add_command_power = 10`, đặt cờ `VIE_sf_started` |
| `sf_<x>` (3 root con) | — | `VIE_lf_xp_10`, đặt cờ `VIE_sf_<x>_started` |
| `sapper_training` | `training_time_factor` -0.02, `terrain_penalty_reduction` +0.03 | `VIE_lf_xp_10` |
| `sapper_equipment` | `supply_consumption_factor` -0.02 | `add_tech_bonus` `CAT_special_forces_equipment` 0.5 |
| `sapper_command` | `recon_factor` +0.03, `land_night_attack` +0.03 | `VIE_lf_xp_10` |
| `sapper_elite` | `special_forces_cap` +0.01, `dig_in_speed_factor` +0.02 | `VIE_lf_xp_20`, template + 1 sư đoàn |
| `para_training` | `training_time_factor` -0.02 | `VIE_lf_xp_10` |
| `para_equipment` | `supply_consumption_factor` -0.02 | `add_tech_bonus` `CAT_transport_helicopters` 0.5 |
| `para_command` | `planning_speed` +0.03, `recon_factor` +0.03 | `VIE_lf_xp_10` |
| `para_elite` | `special_forces_cap` +0.01, `army_speed_factor` +0.02 | `VIE_lf_xp_20`, template + 1 sư đoàn |
| `marine_training` | `training_time_factor` -0.02, `naval_invasion_planning_bonus_speed` +0.03 | `VIE_lf_xp_10` |
| `marine_equipment` | `supply_consumption_factor` -0.02 | `add_tech_bonus` `CAT_landing_craft` 0.5 |
| `marine_command` | `recon_factor` +0.03, `army_defence_factor` +0.01 | `VIE_lf_xp_10` |
| `marine_elite` | `special_forces_cap` +0.01, `naval_invasion_capacity` +1 | `VIE_lf_xp_20` + `VIE_nf_xp_10`, template + 1 sư đoàn |

Tổng cộng đường đầy đủ: `special_forces_cap` +0.04 (báo cáo: +0.15); `naval_invasion_capacity` thêm +1 (báo cáo: +3); `naval_invasion_planning_bonus_speed` thêm +0.03. Đây là **giá trị khởi điểm**: chốt thật bằng `tools/audit/sf_balance.py` (bước 6) sau khi kiểm tra trong game tác dụng của `special_forces_cap` (đơn vị là tỉ lệ, không phải điểm).

Cần xác minh trong game trước khi tin dấu: `VIE_tt_training_time_factor` hiển thị bằng `-=`, nên chưa rõ biến phải truyền -0.02 hay +0.02. Mở `debug`, hoàn thành `sapper_training`, xem dòng trong dynamic modifier.

### 2.5 Template sư đoàn (cần xác minh tên battalion với `common/units` của MD)

Đặt tên **khác** ba template có sẵn của MD (`Special Forces Brigade`, `Naval Infantry Brigade`) để không trùng.

| Capstone | Tên template | regiments | support |
|---|---|---|---|
| Đặc công | `Lữ đoàn Đặc công Tinh nhuệ` | 6× `Special_Forces` (x0–1, y0–2) | `L_Engi_Comp` |
| Dù | `Lữ đoàn Dù Phản ứng nhanh` | 3× `Special_Forces` (x0, y0–2) + 2× `L_Air_Inf_Bat` (x1, y0–1) — khuôn MD | `L_Engi_Comp` |
| Đánh bộ | `Lữ đoàn HQĐB Tinh nhuệ` | `Mech_Marine_Bat` (0,0), `Mot_Marine_Bat` ×3 (x1, y0–2), `L_arm_Bat` (2,0), `SP_Arty_Bat` (3,0) — khuôn MD | `L_Engi_Comp` |

Vị trí xuất hiện: Đặc công và Dù ở `capital_scope`; Đánh bộ ở state ven biển (đề nghị 519, nhưng chốt theo nguồn về căn cứ thật của lữ đoàn).

---

## 3. Mẫu code đã chỉnh (một focus + một effect; đủ để nhân ra 16)

`common/national_focus/VIE_md_focus.txt` (CRLF, tab thụt, đúng thứ tự trường của chuẩn):

```pdx
	###############################
	## TRUC 4 LUC LUONG DAC BIET - DAC CONG / LINH DU / HAI QUAN DANH BO
	###############################
	# Thiet ke: VIE_special_forces_review_and_plan.md. Cum x 140-172, y >= 9 (trong ben trai khoi lf). Neo vao VIE_modernize_vpa,
	# khai bao theo thu tu command -> root con -> tru cot -> capstone (chong forward-ref).
	focus = {
		id = VIE_sf_command
		icon = GFX_focus_VIE_sf_command

		x = -48
		y = 8
		relative_position_id = VIE_modernize_vpa

		cost = 7

		prerequisite = { focus = VIE_lf_command_reform_1 }

		search_filters = { FOCUS_FILTER_ARMY }

		completion_reward = {
			log = "[GetDateText]: [Root.GetName]: Focus VIE_sf_command"
			VIE_sf_command_reward = yes
		}

		ai_will_do = {
			base = 50
			modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
		}
	}
```

`common/scripted_effects/VIE_md_effects_sf.txt` (file mới; ASCII, comment không dấu như các file effect khác):

```pdx
VIE_sf_refresh = {
	force_update_dynamic_modifier = yes
}
VIE_sf_command_reward = {
	add_to_variable = { VIE_af_special_forces_cap = 0.01 tooltip = VIE_tt_special_forces_cap }
	VIE_lf_xp_10 = yes
	add_command_power = 10
	set_country_flag = VIE_sf_started
	VIE_sf_refresh = yes
}
VIE_sf_sapper_training_reward = {
	add_to_variable = { VIE_af_training_time_factor = -0.02 tooltip = VIE_tt_training_time_factor }
	add_to_variable = { VIE_af_terrain_penalty_reduction = 0.03 tooltip = VIE_tt_terrain_penalty_reduction }
	VIE_lf_xp_10 = yes
	VIE_sf_refresh = yes
}
```

Chi tiết `VIE_sf_dm_tt` làm theo đúng `VIE_nf_dm_tt` / helper trong `VIE_md_effects_air_force.txt:55`.

---

## 4. Kế hoạch code (9 bước, mỗi bước một commit trên nhánh `special-forces-v1`)

Mẫu tiến độ giống đợt `air effects v2` (step 0…8). Mỗi bước có tiêu chí qua cửa riêng; không sang bước sau khi chưa qua.

| Bước | Việc | File | Qua cửa khi |
|---|---|---|---|
| **0** | Xác minh dữ liệu MD: tên battalion (`Special_Forces`, `L_Air_Inf_Bat`, `L_Ranger_Bat`, `L_Engi_Comp`, `SP_Arty_Bat`, …) trong `common/units/*` của MD; 3 tech category (`CAT_special_forces_equipment`, `CAT_transport_helicopters`, `CAT_landing_craft`); trigger/effect `add_mastery`, `has_selected_land_grand_doctrine`. Cần đường dẫn bản cài MD (script cũ hardcode `D:/SteamLibrary/…`) | ghi vào mục 2 của file này | Mỗi tên có dòng bằng chứng; tên không thấy thì sửa template, không đoán |
| **1** | Tooltip + effect nền: `VIE_tt_recon_factor`, `VIE_tt_terrain_penalty_reduction`; đổi dùng `VIE_tt_supply_consumption_factor`; helper `VIE_sf_refresh`, `VIE_sf_dm_tt` | `localisation/english/replace/VIE_md_vi_tt_l_english.yml`, `common/scripted_effects/VIE_md_effects_sf.txt` | `live.py` không báo effect/loc thiếu |
| **2** | 16 scripted effect `VIE_sf_<mã>_reward` + `VIE_sf_<x>_templates` (3 template, 3 `create_unit`) | `VIE_md_effects_sf.txt` | `live.py` 0 call thiếu; mỗi reward ≤ 5 hiệu ứng vĩnh viễn |
| **3** | 16 focus, chèn sau `VIE_lf_force_complete` | `VIE_md_focus.txt` | `audit.py`: 0 forward-ref, 0 trùng tọa độ, 0 cycle; `check_static.py`: 0 error; tổng focus 381 → 397 |
| **4** | Localisation tên + `desc` (16 cặp) kèm nhãn `(THẬT)`/`(ĐỀ XUẤT)`; không dùng `[]` ngoài scripted loc; không `§` trong tiêu đề | `localisation/english/VIE_md_events_sf_l_english.yml` (UTF-8 **có BOM**, như các file cùng thư mục) | `tools/verify_all_loc.py`: 0 key thiếu, BOM đúng |
| **5** | Icon: sinh 16 `GFX_focus_VIE_sf_*`, đăng ký spriteType; mẫu `tools/build_vie_focus_icons.py` / `build_vie_air_focus_icons.py` | `interface/VIE_md_focus_icons.gfx` (hoặc file `.gfx` riêng), `gfx/interface/goals/` | Mọi `icon =` có spriteType, file tồn tại |
| **6** | Script cân bằng `tools/audit/sf_balance.py` (cùng kiểu `lf_balance.py`): tổng `special_forces_cap`, `naval_invasion_*`, so với tổng đã có từ nf; in PASS/FAIL, thoát mã 1 khi lỗi | `tools/audit/sf_balance.py` | In PASS |
| **7** | Validator MD (sparse clone, coding standards 11b): `standardize_focus_tree.py`, `validate_focus_tree.py`; chuyển LF → CRLF | cả repo | 0 error; cảnh báo `unneeded-bankruptcy-guard` xử theo mục B4 |
| **8** | Test trong game (`debug`, save copy): làm lf tới `command_reform_1`; mở cụm SF; đi hết 3 binh chủng; kiểm lỗi `error.log` (`VIE_sf_`, `Special_Forces`, `L_Air_Inf_Bat`, `create_unit`); xem sư đoàn xuất hiện đúng state; xem dấu `training_time_factor`; thêm mục "Special forces" vào `tools/TESTING.md` | `tools/TESTING.md` | Checklist TESTING pass; sửa nốt dấu và template nếu game báo |

Ước lượng: bước 0 là nút thắt (phụ thuộc bản cài MD); bước 1–4 làm liền trong một buổi; bước 5 phụ thuộc cách bạn sinh icon; bước 8 phải có HOI4 thật.

---

## 5. Câu hỏi mở (cần bạn quyết)

1. **Vị trí gắn**: `VIE_lf_command_reform_1` (đề xuất) hay một trục độc lập gắn thẳng vào `VIE_modernize_vpa`? Gắn độc lập thì tránh phụ thuộc lf nhưng cụm này đứng cạnh nf/airf.
2. **Lính dù**: giữ như hướng giả định `(ĐỀ XUẤT)`, hay bỏ nhánh B còn 2 binh chủng cho đến khi có nguồn?
3. **Tiêu tiền**: capstone có nên trừ ngân sách (ví dụ `treasury_change = -3`) cho cân bằng với các nhánh khác? Nếu có thì mới đặt guard `bankruptcy_incoming_collapse` ở ba capstone. Mặc định của tôi: không trừ, không guard.
