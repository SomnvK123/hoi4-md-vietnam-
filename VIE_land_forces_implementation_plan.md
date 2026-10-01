# Plan triển khai: roster tướng lĩnh Lục quân VIE theo 2 giai đoạn

> **Đã được thay bằng [VIE_land_forces_implementation_plan_v2.md](VIE_land_forces_implementation_plan_v2.md).** v1 giả định vòng "retire rồi tuyển lại" chạy được và để 8 commander ở bookmark 2000; v2 kiểm tra giả định đó trước và theo công thức số tướng của MD. Giữ file này chỉ để tham khảo.

**Ngày:** 01/10/2026
**Cơ sở:** [VIE_land_forces_roster_rebuild.md](VIE_land_forces_roster_rebuild.md) (dữ liệu và lý do; plan này chỉ nói *làm gì, ở file nào, theo thứ tự nào*).
**Mục tiêu:** bookmark 2000 có roster Giai đoạn 1; ngày 01/01/2015 đổi sang roster Giai đoạn 2; 7 commander Quân đoàn 12/34 tuyển riêng từ 2026.

## 0. Quyết định cần chốt trước khi code

| # | Quyết định | Mặc định trong plan |
|---|---|---|
| D1 | 7 commander Quân đoàn 12/34/QK7 | Phương án A: giữ event riêng, dời ngưỡng sang `date > 2025.12.31` |
| D2 | Lê Mạnh (tùy chọn) và Huỳnh Chiến Thắng (tùy chọn) | Tạo Mạnh (Giai đoạn 1), tuyển Thắng (Giai đoạn 2) |
| D3 | Hải quân/Không quân (Hậu, Thất, Khoa, Đạm, Nam, Phương) | **Không đổi ngày hiện có** (mục 3.4) |
| D4 | Vai trò của Thanh, Nghiên, Tỵ | `corps_commander`, không phải `field_marshal`, để bookmark 2000 không có 5 field marshal cùng lúc. Chỉ Dũng và Vịnh là `field_marshal` |
| D5 | Character mới thiếu portrait (Dũng, Nghiên, Mạnh) | Bỏ khối `portraits` ban đầu, test `error.log`, bổ sung ảnh sau |

## 1. Thứ tự làm

1. Tạo nhánh `claude/land-roster-2-phase` từ `main` (repo đang sạch).
2. Bước 2: character mới.
3. Bước 3: localisation.
4. Bước 4: startup.
5. Bước 5: event và scheduler.
6. Bước 6: kiểm tra tĩnh, rồi trong game.
7. Bước 7: dọn tài liệu cũ.

Mỗi bước commit riêng để rollback từng phần. Bước 4 và 5 phải đi cùng nhau trước khi test, vì làm một mình sẽ cho roster lệch.

## 2. Bước 2: Character mới

**File mới:** `common/characters/VIE_md_army_legacy.txt`. Giữ prefix `VIE_army_` để không đụng ID upstream. Copy đúng khuôn của [VIE_md_army_expansion.txt](common/characters/VIE_md_army_expansion.txt).

| ID | Tên hiển thị | Vai trò | Ghi chú |
|---|---|---|---|
| `VIE_army_le_van_dung` | Lê Văn Dũng | `field_marshal` | Chưa có portrait |
| `VIE_army_pham_van_tra` | Phạm Văn Trà | `advisor` slot `high_command`, ledger `army` | Có `Portrait_Pham_Van_Tra.dds` |
| `VIE_army_phung_quang_thanh` | Phùng Quang Thanh | `corps_commander` | Có `Portrait_Phung_Quang_Thanh.dds` |
| `VIE_army_nguyen_khac_nghien` | Nguyễn Khắc Nghiên | `corps_commander` | Chưa có portrait |
| `VIE_army_do_ba_ty` | Đỗ Bá Tỵ | `corps_commander` | Có `Portrait_Do_Ba_Ty.dds` |
| `VIE_army_le_manh` | Lê Mạnh | `corps_commander` | Chưa có portrait |

**Skill/trait đề xuất** (số là điểm khởi đầu để cân bằng, không phải dữ kiện lịch sử). Chỉ dùng trait đã có trong repo hoặc upstream:

| ID | Trait | skill / attack / defense / planning / logistics |
|---|---|---|
| Dũng | `defensive_doctrine organizer` | 3 / 2 / 3 / 3 / 3 |
| Thanh | `organizer infantry_leader` | 3 / 2 / 3 / 3 / 2 |
| Nghiên | `offensive_doctrine organizer` | 3 / 3 / 2 / 3 / 2 |
| Tỵ | `infantry_leader organizer` | 3 / 2 / 3 / 3 / 2 |
| Mạnh | `defensive_doctrine infantry_leader` | 2 / 2 / 3 / 2 / 2 |
| Trà (advisor) | `army_entrenchment_2`, `cost = 100`, `ai_will_do = { factor = 1 }` | không áp dụng |

**Lưu ý schema:** advisor cần `idea_token = vie_army_pham_van_tra` (chữ thường). Đường dẫn portrait: `gfx/leaders/VIE/Portrait_X.dds` và `gfx/leaders/VIE/small/Portrait_X_small.dds` (ba người có ảnh đều đã có bản `small`).

**Việc cần xác nhận khi test:** chưa chắc HOI4 chấp nhận character không có `portraits`. Nếu `error.log` báo lỗi, dùng tạm một portrait có sẵn hoặc làm ảnh mới.

## 3. Bước 3: Localisation

**Sửa:** [VIE_army_commanders_l_english.yml](localisation/english/VIE_army_commanders_l_english.yml). File này giữ BOM UTF-8, dùng cú pháp `key:0 "text"` có một dấu cách đầu dòng.

Thêm các khóa, theo đúng khuôn của 7 dòng hiện có (khóa trùng ID):

```yaml
 VIE_army_le_van_dung:0 "Lê Văn Dũng"
 VIE_army_pham_van_tra:0 "Phạm Văn Trà"
 vie_army_pham_van_tra:0 "Phạm Văn Trà"
 VIE_army_phung_quang_thanh:0 "Phùng Quang Thanh"
 VIE_army_nguyen_khac_nghien:0 "Nguyễn Khắc Nghiên"
 VIE_army_do_ba_ty:0 "Đỗ Bá Tỵ"
 VIE_army_le_manh:0 "Lê Mạnh"
```

**Phí Quốc Tuấn** (upstream ghi "Phi"): làm sau cùng và là việc tùy chọn. Cần thử đặt khóa `VIE_Phi_Quoc_Tuan` trong `localisation/english/replace/` và xem game có lấy bản đó không. Không chắc cách MD lấy tên character, nên đừng làm việc này trước khi mọi thứ khác chạy.

## 4. Bước 4: Startup

**Sửa:** [VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt), khối `if date < 2015.1.1` (dòng 9-29).

1. **Xóa 4 dòng retire** của Giai đoạn 1 upstream: `VIE_Ngo_Xuan_Lich`, `VIE_Phi_Quoc_Tuan`, `VIE_Tran_Don`, `VIE_Vo_Trong_Viet`.
2. **Giữ nguyên** các dòng retire còn lại, kể cả Hải quân/Không quân (D3).
3. **Thêm khối tuyển Giai đoạn 1 (lần đầu)** trong cùng scope `VIE = { ... }`:

```txt
if = {
	limit = {
		date < 2015.1.1
		NOT = { has_country_flag = VIE_army_phase1_recruited }
	}
	recruit_character = VIE_army_le_van_dung
	recruit_character = VIE_army_pham_van_tra
	recruit_character = VIE_army_phung_quang_thanh
	recruit_character = VIE_army_nguyen_khac_nghien
	recruit_character = VIE_army_do_ba_ty
	recruit_character = VIE_army_le_manh
	set_country_flag = VIE_army_phase1_recruited
}
```

**Vì sao cần cờ:** `on_startup` chạy cả khi load save, không chỉ khi bắt đầu game. Không có cờ thì mỗi lần load save 2005 sẽ tuyển lại. Điều kiện `date < 2015.1.1` giữ cho save sau 2015 không tuyển lại nhóm đã bị rút.

## 5. Bước 5: Event và scheduler

### 5.1. Scheduler

**Sửa:** [VIE_md_effects_p16.txt](common/scripted_effects/VIE_md_effects_p16.txt). Hàm này được gọi hằng tháng từ `on_monthly`, nên mốc ngày sẽ bắn trong tháng đầu tiên sau mốc.

| Khối | Thay đổi |
|---|---|
| 2015 (`vie_army_commanders.2`) | Bỏ dòng `NOT = { has_character = VIE_Ngo_Xuan_Lich }`. Cờ `VIE_md_roster_recruited_2015` đã đủ |
| 2016 (`vie_army_commanders.3`) | **Xóa cả khối** (Giang, Trường chuyển vào event .2) |
| 2021 (`vie_army_commanders.4`) | Bỏ dòng `NOT = { has_character = VIE_Nguyen_Tan_Cuong }`. Giữ ngưỡng `date > 2020.12.31` và cờ `VIE_md_roster_recruited_2021` |
| 7 commander submod | Đổi `date > 2022.12.31` thành `date > 2025.12.31` |

### 5.2. Event

**Sửa:** [VIE_army_commanders.txt](events/VIE_army_commanders.txt).

**`vie_army_commanders.2` (đổi roster 2015).** Thay danh sách `immediate`:

```txt
immediate = {
	# Giai đoạn 2, Lục quân
	recruit_character = VIE_Be_Xuan_Truong
	recruit_character = VIE_Vo_Minh_Luong
	recruit_character = VIE_Phan_Van_Giang
	recruit_character = VIE_Nguyen_Trong_Nghia
	recruit_character = VIE_Hoang_Xuan_Chien
	recruit_character = VIE_Nguyen_Tan_Cuong
	recruit_character = VIE_Le_Xuan_Duy
	recruit_character = VIE_Pham_Van_Hung
	recruit_character = VIE_Hyunh_Chien_Thang   # tùy chọn (D2)

	# Giữ nguyên, ngoài phạm vi Lục quân (D3)
	recruit_character = VIE_Nguyen_Quang_Dam
	recruit_character = VIE_Pham_Kim_Hau
	recruit_character = VIE_Tran_Viet_Khoa
	recruit_character = VIE_Dinh_Gia_That

	# Rút nhóm Giai đoạn 1 đã hết vai trò
	retire_character = VIE_army_le_van_dung
	retire_character = VIE_army_pham_van_tra
	retire_character = VIE_army_phung_quang_thanh
	retire_character = VIE_army_nguyen_khac_nghien
	retire_character = VIE_army_do_ba_ty
	retire_character = VIE_army_le_manh
	retire_character = VIE_Phi_Quoc_Tuan

	set_country_flag = VIE_md_roster_recruited_2015
	clr_country_flag = VIE_md_roster_event_pending
}
```

Ở lại qua 2015, không rút: Nguyễn Chí Vịnh, Trần Đơn, Ngô Xuân Lịch, Võ Trọng Việt.

**`vie_army_commanders.3`:** xóa cả event, kèm khóa `vie_army_commanders.3.a` trong localisation.

**`vie_army_commanders.4` (2021):** chỉ còn hai người ngoài phạm vi: `VIE_Pham_Hoai_Nam` và `VIE_Tran_Quang_Phuong`. Bỏ Cương, Nghĩa, Võ Minh Lương, Hoàng Xuân Chiến (đã chuyển sang event .2).

**`vie_army_commanders.1`:** không đổi nội dung.

## 6. Bước 6: Kiểm tra

### 6.1. Kiểm tra tĩnh

Chạy theo [tools/TESTING.md](tools/TESTING.md) và [tools/audit/README.md](tools/audit/README.md):

```bash
python3 tools/verify_all_loc.py
python3 tools/audit/live.py     # tham chiếu chéo
python3 tools/audit/ev.py       # namespace, id trùng, loc, orphan (sẽ bắt event .3 bị xóa sót loc)
```

`tools/check_static.py` hardcode đường dẫn Windows tới Millennium Dawn nên chưa chạy được nếu chưa sửa hằng số.

### 6.2. Trong game (chưa ai chạy)

1. Thêm mod sau Millennium Dawn, mở game, đọc `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log`, tìm `VIE`, `vie_`, `character`, `portrait`.
2. Bắt đầu bookmark 2000, chơi VIE.

| Thời điểm | Lục quân có mặt (số lượng mong đợi) |
|---|---|
| 01/2000 | Vịnh, Dũng, Trà, Thanh, Nghiên, Tỵ, Mạnh, Phí Quốc Tuấn, Đơn, Lịch, Việt = **11** |
| Sau 01/2015 (tháng đầu) | Vịnh, Đơn, Lịch, Việt + Bế, Lương, Giang, Nghĩa, Chiến, Cương, Duy, Hùng, (Thắng) = **12-13**. Dũng, Trà, Thanh, Nghiên, Tỵ, Mạnh, Tuấn không còn |
| Sau 01/2021 | Như trên, thêm Phạm Hoài Nam và Trần Quang Phương (ngoài Lục quân) |
| Sau 01/2026 | Thêm 7 commander submod |

3. **Test nhanh bằng console** (dùng bản sao save, bật `debug`): `tag VIE`, `event vie_army_commanders.2` để kiểm tra đổi roster ngay mà không cần chờ đến 2015, và `event vie_army_commanders.1` cho nhóm 7 người.
4. **Load save giữa giai đoạn** (ví dụ 2007): xác nhận không có người bị tuyển lặp và roster vẫn là Giai đoạn 1.
5. **Load save sau mốc 2015:** xác nhận roster Giai đoạn 2 vẫn còn, Giai đoạn 1 không quay lại.
6. **Câu hỏi còn mở cần chốt bằng thử nghiệm:** `retire_character` có thực sự gỡ người khỏi recruit panel không, và có tuyển lại được bằng `recruit_character` ở 2015 không (hiện startup đang dựa vào điều này cho 14 người, nhưng chưa ai xác nhận trong game).

## 7. Bước 7: Dọn tài liệu

| File | Sửa |
|---|---|
| [VIE_generals_and_commander_system_research_report.md](VIE_generals_and_commander_system_research_report.md) | Bỏ "tuyển khi khởi động"; sửa "8 portrait" thành 14 file `.dds`; bỏ "chưa có portrait riêng" cho 7 commander |
| [VIE_commander_timeline_research_report.md](VIE_commander_timeline_research_report.md) | Bỏ mốc 2005 và đoạn "Chí Vịnh căn cứ mạnh ở 2000" |
| `VIE_land_forces_2000_2005_2010_research_report.md` | Xóa hoặc thêm dòng đầu "đã thay bằng `VIE_land_forces_roster_rebuild.md`" (file chưa commit nên xóa là mất hẳn) |
| [tools/TESTING.md](tools/TESTING.md) | Thêm mục kiểm tra roster như 6.2 |

## 8. Rủi ro và cách xử lý

| Rủi ro | Xử lý |
|---|---|
| Character không có portrait gây lỗi | Dùng portrait tạm; làm ảnh sau |
| `on_startup` tuyển lặp khi load save | Cờ `VIE_army_phase1_recruited` (mục 4) |
| Save cũ đã chạy event 2015 theo bản cũ | Phase 1 không bị rút cho save đó; chấp nhận, cần ghi vào changelog |
| Bắt đầu bookmark sau 2015 (nếu MD có) | Event .2 vẫn chạy sau 1 tháng; thử trước khi hứa là hỗ trợ |
| Thanh và Tỵ bị rút sớm ~1 năm | Chấp nhận, đã ghi trong báo cáo |
| 11 người xuất hiện cùng lúc ở 2000, lệch 9-12 năm | Chấp nhận theo yêu cầu 2 giai đoạn |

## 9. Ngoài phạm vi (không đụng trong đợt này)

- Hải quân: Phạm Hoài Nam, Phạm Kim Hậu, Đinh Gia Thất.
- Không quân: Trần Quang Phương, Trần Việt Khoa.
- Nguyễn Quang Đạm.
- Cân bằng skill/trait chi tiết.
- Tạo portrait mới cho Dũng, Nghiên, Mạnh.
- Thêm commander cho các quân khu khác ngoài chuỗi QK7.
