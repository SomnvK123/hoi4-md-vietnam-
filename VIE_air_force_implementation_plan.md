# Plan triển khai: roster chỉ huy Không quân VIE (chuỗi 8 mốc + 12 chỉ huy bổ sung)

**Ngày:** 01/10/2026
**Dữ liệu và nguồn:** [VIE_air_force_commanders_research_report.md](VIE_air_force_commanders_research_report.md), mục 4 và mục 8.
**Liên quan:** [VIE_land_forces_implementation_plan_v2.md](VIE_land_forces_implementation_plan_v2.md) (cùng cơ chế, cùng quy ước).
**Trạng thái:** chỉ là plan, chưa sửa code nào, chưa chạy game.

## Trạng thái triển khai (01/10/2026)

**Đã code trong working tree (chưa commit, chưa chạy game):**

| Hạng mục | Kết quả |
|---|---|
| Character | 20 ID trong [VIE_md_air_commanders.txt](common/characters/VIE_md_air_commanders.txt): 8 `air_chief` + 12 `high_command` ledger air |
| Trait và cost | Cả 20 trait đã đối chiếu với pool của MD: tồn tại, đúng slot (`air_chief` hay `high_command`), hai pool không chồng lấn; cost theo mục 2 |
| Localisation | [VIE_air_commanders_l_english.yml](localisation/english/VIE_air_commanders_l_english.yml): 40 khóa (ID và `idea_token` cho từng người) |
| Portrait | 20 ảnh placeholder (silhouette trung tính, không phải chân dung thật) bằng [tools/build_vie_placeholder_portraits.py](tools/build_vie_placeholder_portraits.py); thay bằng ảnh thật khi có |
| Bước 0 | Khối trong [VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt): tuyển Soát và bốn người đầu, retire Phương và Khoa, có cờ `VIE_air_phase0_done` |
| Bước 1-7 | [VIE_md_effects_air.txt](common/scripted_effects/VIE_md_effects_air.txt) (`VIE_event_scheduler_air`, 7 khối có cờ), gọi hằng tháng từ [VIE_md_on_actions.txt](common/on_actions/VIE_md_on_actions.txt) |
| Tài liệu | Checklist trong [tools/TESTING.md](tools/TESTING.md); ghi chú trong [VIE_md_character_schema_and_roster.md](VIE_md_character_schema_and_roster.md) |

**Chọn nhánh E7 mặc định:** scheduler gọi `recruit_character` và `retire_character` **trực tiếp**, không qua event ẩn, vì chưa thể chạy game để thử. Nếu E7 thất bại thì chuyển sang event ẩn như mục 5, bước 4.

**Đã kiểm tra tĩnh:** 20/20 character hợp lệ về trait, slot, ledger, cost, `idea_token` không trùng; mọi `recruit_character` và `retire_character` trỏ tới character tồn tại; mọi portrait và khóa loc có; mỗi ID được tuyển đúng một lần và chỉ bị retire sau khi đã tuyển; 7 mốc ngày tăng dần; không trùng tên cờ; `verify_all_loc.py` đạt cho file mới; `ev.py` sạch; `live.py` không thêm lỗi nào ngoài việc đánh dấu `VIE_event_scheduler_air` giống mọi scheduler có sẵn (công cụ không đọc được định nghĩa scripted effect).

**Chưa làm:** thí nghiệm E5-E7 và mọi kiểm tra trong game; tạo nhánh git và commit; thay ảnh placeholder.

## 0. Quyết định đã chốt

| # | Quyết định | Nguồn quyết định |
|---|---|---|
| D1 | Slot `air_chief` đi theo **chuỗi 8 mốc** đúng nhiệm kỳ: tuyển người kế nhiệm rồi retire người tiền nhiệm; mỗi ID chỉ tuyển một lần | Bạn chọn |
| D2 | Thêm **12 chỉ huy** bổ sung, tất cả là advisor `high_command` ledger air | Bạn yêu cầu |
| D3 | Retire `VIE_Tran_Quang_Phuong` và `VIE_Tran_Viet_Khoa` ở startup (sai nhân thân) | Đề xuất bạn đã đọc, tôi đồng ý |
| D4 | Giữ nguyên `VIE_Vo_Minh_Luong` và `VIE_Vo_Trong_Viet` (ledger air nhưng là Lục quân) | Như trên |
| D5 | 12 người bổ sung **gắn vào đúng 8 mốc của chuỗi**, không có lịch riêng | Quyết định thiết kế của plan này (mục 1) |

## 1. Thiết kế

Slot `air_chief` chỉ có một người nên chuỗi tuyển/retire đi từng bước là tự nhiên. 12 chỉ huy bổ sung đi cùng các bước đó:
- Người nào có chức vụ **tại thời điểm** một mốc thì được tuyển ở mốc ấy (hoặc ở startup nếu đã giữ chức năm 2000).
- Người nào hết chức vụ thì được retire ở **mốc gần nhất sau đó**.
- Hệ quả: chỉ có **8 mốc ngày** trong toàn bộ plan, không cần lịch thứ hai. Đánh đổi: có người rời pool trễ 1-3 năm (cột "trễ" ở mục 3).

Mọi thao tác đều **một chiều** (tuyển ID chưa tuyển, retire ID đã tuyển). Không có vòng "retire rồi tuyển lại".

Ba điều tôi chưa xác minh và là rủi ro chính, xem mục 4: retire ở startup có chạy không; retire advisor đang được thuê có gỡ khỏi slot không; scheduler có tuyển trực tiếp được không (code hiện tại dùng event ẩn).

## 2. Roster

### 2.1. Chuỗi `air_chief` (8 người, slot `air_chief`, ledger air)

| Bước | Nhân vật | ID | Trait (pool `air_chief`) | cost |
|--:|---|---|---|--:|
| 0 | Nguyễn Đức Soát | `VIE_air_nguyen_duc_soat` | `air_air_superiority_2` | 100 |
| 1 | Nguyễn Văn Thân | `VIE_air_nguyen_van_than` | `air_chief_safety_1` | 100 |
| 2 | Lê Hữu Đức | `VIE_air_le_huu_duc` | `air_bomber_interception_2` | 100 |
| 3 | Phương Minh Hòa | `VIE_air_phuong_minh_hoa` | `air_chief_reform_2` | 150 |
| 4 | Lê Huy Vịnh | `VIE_air_le_huy_vinh` | `air_force_multiplier_2` | 100 |
| 5 | Vũ Văn Kha | `VIE_air_vu_van_kha` | `air_close_air_support_2` | 100 |
| 6 | Nguyễn Văn Hiền | `VIE_air_nguyen_van_hien` | `air_chief_all_weather_2` | 100 |
| 7 | Vũ Hồng Sơn | `VIE_air_vu_hong_son` | `air_chief_reform_1` | 100 |

### 2.2. 12 chỉ huy bổ sung (slot `high_command`, ledger air)

| # | Nhân vật | ID | Chức vụ chính (nguồn) | Trait (pool `high_command`) | cost | Tin cậy |
|--:|---|---|---|---|--:|:-:|
| 1 | Phạm Thanh Ngân | `VIE_air_pham_thanh_ngan` | Tư lệnh Không quân 04/1989-1996; Chủ nhiệm Tổng cục Chính trị 01/1998-05/2001; phi công ace, Thượng tướng 11/1999 | `air_high_command_air_superiority_3` | 125 | A |
| 2 | Hán Vĩnh Tưởng | `VIE_air_han_vinh_tuong` | Phó Tư lệnh chính trị Không quân từ 11/1996; Bí thư Đảng ủy PK-KQ 02/2001-01/2005; phi công, Trung tướng 2002 | `air_high_command_combat_training_2` | 100 | A |
| 3 | Phạm Tuân | `VIE_air_pham_tuan` | Phó Tư lệnh chính trị Không quân 1989; Giám đốc Tổng cục Công nghiệp Quốc phòng 1999; phi công vũ trụ, Trung tướng; nghỉ hưu 2008 | `air_high_command_aircraft_design_2` | 100 | B |
| 4 | Nguyễn Văn Phiệt | `VIE_air_nguyen_van_phiet` | Chính ủy Phòng không/PK-KQ 1992-2001, Trung tướng 1999 | `air_high_command_flight_safety_1` | 100 | B |
| 5 | Võ Văn Tuấn | `VIE_air_vo_van_tuan` | Phó Tư lệnh kiêm Tham mưu trưởng PK-KQ 2008-2011; Phó Tổng Tham mưu trưởng 2011-2017; phi công Su-27, Thượng tướng 2015 | `air_high_command_air_superiority_2` | 100 | A |
| 6 | Nguyễn Văn Thọ | `VIE_air_nguyen_van_tho` | Tham mưu trưởng PK-KQ 2011-2017 (Thiếu tướng); trước đó Sư đoàn trưởng Không quân 372 | `air_high_command_multirole_support_2` | 100 | B |
| 7 | Nguyễn Văn Thanh | `VIE_air_nguyen_van_thanh` | Chính ủy PK-KQ 2011-2016, Trung tướng 2012 | `air_high_command_flight_safety_2` | 100 | A |
| 8 | Lâm Quang Đại | `VIE_air_lam_quang_dai` | Phó Chính ủy từ 06/2015; Chính ủy 2016-2022; Trung tướng 2019 | `air_high_command_combat_training_1` | 100 | A |
| 9 | Phạm Văn Tính | `VIE_air_pham_van_tinh` | Sư đoàn trưởng PK 363 2016-01/2019; Phó Tư lệnh từ 06/2020 (Thiếu tướng) | `air_high_command_interception_2` | 100 | B |
| 10 | Trần Ngọc Quyến | `VIE_air_tran_ngoc_quyen` | Chính ủy PK-KQ từ 16/06/2022, Trung tướng | `air_high_command_air_reform_1` | 100 | A |
| 11 | Phạm Tuấn Anh | `VIE_air_pham_tuan_anh` | Phó Tham mưu trưởng, rồi Phó Tư lệnh PK-KQ từ 07/2023 | `air_high_command_all_weather_1` | 100 | B |
| 12 | Bùi Đức Hiền | `VIE_air_bui_duc_hien` | Tham mưu trưởng PK-KQ từ 06/2025 (Thiếu tướng) | `air_high_command_night_operations_1` | 100 | B |

Ghi chú:
- Trait và `cost` là điểm khởi đầu để cân bằng, **không phải dữ kiện lịch sử**. Tôi đã kiểm tra cả 20 trait tồn tại trong đúng pool của MD và hai pool không chồng lấn. Quy ước cost theo upstream: `reform_2` là 150, trait cấp 3 của `high_command` là 125, còn lại 100.
- 6 người trong số 12 là cán bộ chính trị (Ngân sau 1998, Tưởng, Phiệt, Thanh, Đại, Quyến). Pool trait của MD không có trait chính trị nên họ mang trait chuyên môn gần nhất; đây là xấp xỉ.

## 3. Lịch 8 mốc

Scheduler của mod chạy **hằng tháng**, nên ngày thực tế lệch tối đa 1 tháng. Cột "trễ" là thời gian người bị retire đã hết chức vụ thật.

| Bước | Điều kiện | Tuyển | Retire (trễ) |
|--:|---|---|---|
| 0 | Startup, `date < 2002.2.7` | Soát, Ngân, Tưởng, Tuân, Phiệt | Upstream: `VIE_Tran_Quang_Phuong`, `VIE_Tran_Viet_Khoa` |
| 1 | `date > 2002.2.6` | Thân | Soát (tại mốc), Ngân (trễ 0,7 năm), Phiệt (trễ 0,7 năm) |
| 2 | `date > 2007.1.31` | Đức | Thân (0), Tưởng (trễ 2 năm) |
| 3 | `date > 2010.6.30` | Hòa, Võ Văn Tuấn | Đức (0), Tuân (trễ 2 năm) |
| 4 | `date > 2015.5.20` | Vịnh, Thọ, Thanh, Đại | Hòa (0) |
| 5 | `date > 2019.12.30` | Kha, Tính | Vịnh (0), Võ Văn Tuấn (trễ 2 năm), Thọ (trễ 2 năm), Thanh (trễ 3,5 năm) |
| 6 | `date > 2023.5.18` | Hiền, Tuấn Anh, Quyến | Kha (0), Đại (trễ 1 năm) |
| 7 | `date > 2025.6.27` | Sơn, Bùi Đức Hiền | Hiền (0) |

**Ngày chưa chính xác:** mốc 3 (Hòa) dùng 01/07/2010 vì nguồn chỉ ghi năm 2010. Mốc 2 dùng 01/02/2007 theo ngày Thân nghỉ hưu (02/2007); một nguồn khác ghi Đức nhận chức 2006.

**Người ở lại đến cuối** (không bị retire): Tính, Tuấn Anh, Quyến, Bùi Đức Hiền, Sơn.

**Số người có mặt** (ngoài Lương và Việt của upstream):

| Khoảng thời gian | `air_chief` | `high_command` ledger air |
|---|---|---|
| 2000 - 02/2002 | Soát | Ngân, Tưởng, Tuân, Phiệt |
| 02/2002 - 02/2007 | Thân | Tưởng, Tuân |
| 02/2007 - 07/2010 | Đức | Tuân |
| 07/2010 - 05/2015 | Hòa | Võ Văn Tuấn |
| 05/2015 - 12/2019 | Vịnh | Võ Văn Tuấn, Thọ, Thanh, Đại |
| 12/2019 - 05/2023 | Kha | Tính, Đại |
| 05/2023 - 06/2025 | Hiền | Tính, Tuấn Anh, Quyến |
| từ 06/2025 | Sơn | Tính, Tuấn Anh, Quyến, Bùi Đức Hiền |

Giai đoạn 2007-2015 mỏng (1 người bổ sung) vì nguồn cho cấp Phó Tư lệnh thời đó chưa có. Cần nghiên cứu thêm nếu muốn dày hơn (mục 7).

## 4. Thí nghiệm bắt buộc trước khi code (khoảng 20 phút)

Làm trên bản sao save, bật `debug`, chơi VIE. Kết quả quyết định kỹ thuật ở mục 5.

| # | Thí nghiệm | Nếu thành công | Nếu thất bại |
|---|---|---|---|
| **E5** | Mới vào game 2000: `effect retire_character = VIE_Tran_Quang_Phuong`, mở panel advisor Không quân | Phương biến mất khỏi pool: bước 0 dùng đúng thiết kế | Retire ở startup không đủ: giữ họ và ghi nhận anachronism, hoặc tìm cách khác |
| **E6** | Thuê Phương làm `air_chief`, rồi `effect retire_character = VIE_Tran_Quang_Phuong` | Slot trống, có thể thuê người mới | Nếu slot vẫn giữ người đã retire thì mỗi bước chuỗi phải kèm cách gỡ slot (cần nghiên cứu thêm) |
| **E7** | Tạo effect thử gọi `recruit_character` và `retire_character` trực tiếp trong khối `if` của scheduler tháng (không qua event), đặt cờ | Bỏ event, dùng scheduler trực tiếp (mục 5, bước 4) | Quay lại mẫu hiện có: event ẩn `days = 1`, mỗi bước một event |

Nếu E5 và E6 đều đạt, plan chạy như viết. Nếu E7 thất bại thì chỉ thay bước 4 (mục 5), phần còn lại giữ nguyên.

## 5. Các bước code

### Bước 1: Nhánh git

Tạo `claude/air-roster` từ `main`. Mỗi bước dưới đây một commit.

### Bước 2: Character mới (không phụ thuộc thí nghiệm)

**File mới:** `common/characters/VIE_md_air_commanders.txt`, 20 character. Khuôn mẫu theo `VIE_Tran_Quang_Phuong` upstream:

```txt
VIE_air_nguyen_duc_soat = {
	name = "Nguyen Duc Soat"
	portraits = {
		army = {
			small = "gfx/leaders/VIE/small/Portrait_Nguyen_Duc_Soat_small.dds"
			large = "gfx/leaders/VIE/Portrait_Nguyen_Duc_Soat.dds"
		}
	}
	advisor = {
		slot = air_chief
		idea_token = vie_air_nguyen_duc_soat
		ledger = air
		traits = { air_air_superiority_2 }
		cost = 100
		ai_will_do = { factor = 1 }
	}
}
```

- Chuỗi 8 người: `slot = air_chief`. 12 người bổ sung: `slot = high_command`. Tất cả `ledger = air`.
- Mỗi advisor cần `idea_token` chữ thường (`vie_air_...`), xem mục 2.
- Không có khối `field_marshal` hoặc `corps_commander` (Không quân không có commander).
- Định dạng file: CRLF, ASCII (tên không dấu), thụt dòng bằng tab, như các file character khác của mod.

**Lưu ý đặt tên dễ nhầm:** `nguyen_van_than` (Thân, tư lệnh) và `nguyen_van_thanh` (Thanh, chính ủy) chỉ khác một chữ; `nguyen_van_hien` (Hiền, tư lệnh) và `bui_duc_hien` (Hiền, tham mưu trưởng); `pham_tuan` (phi công vũ trụ) và `pham_tuan_anh` (Phó Tư lệnh). Nên ghi chú một dòng trên đầu file.

### Bước 3: Localisation và portrait (không phụ thuộc thí nghiệm)

**Localisation:** file mới `localisation/english/VIE_air_commanders_l_english.yml`. Giữ BOM UTF-8, CRLF, dòng đầu `l_english:`, tên hiển thị có dấu. Mỗi nhân vật cần **hai khóa** (ID và `idea_token` chữ thường), như nhóm Lục quân:

```yaml
 VIE_air_nguyen_duc_soat:0 "Nguyễn Đức Soát"
 vie_air_nguyen_duc_soat:0 "Nguyễn Đức Soát"
```

**Portrait:** mở rộng [tools/build_vie_placeholder_portraits.py](tools/build_vie_placeholder_portraits.py): thêm 20 stem vào `PLACEHOLDERS` với một bảng màu mới cho Không quân (xanh trời). Ảnh là silhouette trung tính, không phải chân dung thật; ghi đè cùng tên khi có ảnh thật.

### Bước 4: Scheduler (phụ thuộc E7)

**File mới:** `common/scripted_effects/VIE_md_effects_air.txt`, chứa một scripted effect `VIE_event_scheduler_air`. Mỗi bước một khối có cờ:

```txt
VIE_event_scheduler_air = {
	if = {
		limit = {
			date > 2002.2.6
			NOT = { has_country_flag = VIE_air_step_1 }
		}
		recruit_character = VIE_air_nguyen_van_than
		retire_character = VIE_air_nguyen_duc_soat
		retire_character = VIE_air_pham_thanh_ngan
		retire_character = VIE_air_nguyen_van_phiet
		set_country_flag = VIE_air_step_1
	}
	# ... step 2..7 theo bảng mục 3, theo thứ tự thời gian
}
```

**Gọi từ tháng:** thêm một dòng `VIE_event_scheduler_air = yes` ngay sau `VIE_event_scheduler_p16 = yes` trong [VIE_md_on_actions.txt](common/on_actions/VIE_md_on_actions.txt) (khối `on_monthly`, đã có điều kiện loại tag nổi dậy).

**Nếu E7 thất bại:** thay các lệnh trong khối bằng `country_event = { id = vie_air_commanders.N days = 1 }` và đặt các lệnh tuyển/retire trong event ẩn như mẫu của [VIE_army_commanders.txt](events/VIE_army_commanders.txt). Khi đó cần thêm `add_namespace`, một event mỗi bước (7 event) và khóa loc `.a` cho từng option.

### Bước 5: Startup (bước 0, không phụ thuộc E7)

Sửa [VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt), trong scope `VIE = { ... }`, cạnh khối tuyển Lục quân Giai đoạn 1:

```txt
if = {
	limit = {
		date < 2002.2.7
		NOT = { has_country_flag = VIE_air_phase0_done }
	}
	recruit_character = VIE_air_nguyen_duc_soat
	recruit_character = VIE_air_pham_thanh_ngan
	recruit_character = VIE_air_han_vinh_tuong
	recruit_character = VIE_air_pham_tuan
	recruit_character = VIE_air_nguyen_van_phiet
	retire_character = VIE_Tran_Quang_Phuong
	retire_character = VIE_Tran_Viet_Khoa
	set_country_flag = VIE_air_phase0_done
}
```

Cờ bắt buộc vì `on_startup` chạy cả khi load save; không có cờ thì mỗi lần load sẽ tuyển lặp và retire lặp. Điều kiện `date < 2002.2.7` để save sau mốc 1 không tuyển lại người đã hết nhiệm kỳ.

### Bước 6: Cập nhật tài liệu

| File | Việc |
|---|---|
| [VIE_air_force_commanders_research_report.md](VIE_air_force_commanders_research_report.md) | Đã có mục "mở rộng 12 chỉ huy" (mục 8) và quyết định chuỗi 8 mốc |
| [tools/TESTING.md](tools/TESTING.md) | Thêm checklist Không quân như mục 6 dưới đây |
| [VIE_md_character_schema_and_roster.md](VIE_md_character_schema_and_roster.md) | Ghi chú 4 character Không quân upstream sai nhân thân (dẫn sang báo cáo Không quân) |

## 6. Kiểm tra

**Tĩnh** (xem [tools/TESTING.md](tools/TESTING.md)):

```bash
python3 tools/verify_all_loc.py
python3 tools/audit/live.py
python3 tools/audit/ev.py   # chỉ cần nếu E7 thất bại và dùng event
```

**Tự kiểm tra chéo** (như đợt Lục quân): mọi `recruit_character`/`retire_character` trỏ tới character tồn tại; mọi portrait có file; mọi tên và `idea_token` có khóa loc; trait nằm đúng pool của MD (`air_chief` hay `high_command`).

**Trong game (chưa ai chạy):**
- [ ] `error.log` sạch: không báo `VIE_air_`, `trait`, `portrait`, `idea_token`.
- [ ] Bắt đầu 2000, panel Không quân: `air_chief` chỉ có Soát; `high_command` có Ngân, Tưởng, Tuân, Phiệt, cùng Lương và Việt của upstream. Không có Phương, Khoa.
- [ ] Đặt ngày/lấy save ở các mốc 2002, 2007, 2010, 2015, 2019, 2023, 2025: `air_chief` đổi đúng người; không ai bị tuyển hai lần; không có hai `air_chief` cùng lúc.
- [ ] Load save giữa hai mốc (ví dụ 2012): không tuyển lặp, roster vẫn đúng giai đoạn.
- [ ] Mỗi mốc kiểm tra số người có mặt đối chiếu bảng ở mục 3.

## 7. Rủi ro và phần chưa làm

| Rủi ro | Xử lý |
|---|---|
| Retire ở startup không hoạt động (E5) | Chấp nhận anachronism của Phương và Khoa, hoặc tìm cách khác |
| Retire advisor đang được thuê không gỡ khỏi slot (E6) | Cần nghiên cứu thêm cơ chế gỡ slot trước khi triển khai chuỗi |
| Scheduler không tuyển trực tiếp được (E7) | Dùng event ẩn như mẫu Lục quân |
| Retire người trễ 1-3,5 năm | Chấp nhận (mục 3); mỗi mốc là ngày cố định |
| 6/12 người bổ sung là cán bộ chính trị mang trait chuyên môn | Xấp xỉ do pool trait của MD; ghi rõ |
| 6/12 người bổ sung chỉ có một nguồn (nhãn B) | Xem báo cáo, mục 8; xác minh thêm nếu có điều kiện |
| Giai đoạn 2007-2015 mỏng | Chưa có nguồn cho Phó Tư lệnh thời đó; nghiên cứu thêm nếu cần |
| Bookmark khác 2000 | Plan chỉ hỗ trợ bookmark 2000; bắt đầu sau 2002 sẽ không tuyển Soát |

**Ngoài phạm vi:**
- Cấp sư đoàn: Wikipedia VI chỉ ghi sư đoàn trưởng hiện tại (Đại tá), không có danh sách lịch sử; không đưa vào plan.
- Trần Việt Khoa cho Lục quân: vẫn chờ nguồn bổ nhiệm đáng tin cậy.
- **Nguyễn Văn Rinh** (phát hiện trong lúc nghiên cứu): là tướng Lục quân (Tư lệnh Quân đoàn 2 năm 1992, Phó Tổng Tham mưu trưởng 1994-1998, Thứ trưởng 1998-2007, Thượng tướng 2004). Không thuộc Không quân, nhưng là ứng viên `high_command` còn thiếu của roster Lục quân Giai đoạn 1.

## 8. Nguồn

Nguồn từng người nằm ở [báo cáo Không quân](VIE_air_force_commanders_research_report.md), mục 4 và mục 8. Nguồn kỹ thuật:
- [MD VIE.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/characters/VIE.txt), [01_air_chief_traits.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/country_leader/01_air_chief_traits.txt), [01_high_command_traits.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/country_leader/01_high_command_traits.txt)
- [HOI4 Character modding](https://hoi4.paradoxwikis.com/Character_modding)
