# Plan triển khai v2: roster tướng Lục quân VIE theo kiểu Millennium Dawn

**Ngày:** 01/10/2026 (cập nhật lần 2: thêm 10 tướng mở rộng)
**Thay thế:** [VIE_land_forces_implementation_plan.md](VIE_land_forces_implementation_plan.md) (v1).
**Dữ liệu, nguồn và lý do chọn người:** [VIE_land_forces_roster_rebuild.md](VIE_land_forces_roster_rebuild.md), đặc biệt mục 10 (10 tướng mở rộng).
**Khác v1 ở đâu:** v1 mặc định nhóm upstream sẽ được "retire lúc khởi động rồi tuyển lại 2015". Chưa ai chứng minh được vòng này chạy. v2 làm thí nghiệm trước, rồi chọn một trong hai nhánh, và chỉ dựa vào thao tác một chiều cho phần chắc chắn.

## 0. Trạng thái triển khai (01/10/2026)

**Đã làm trong working tree (chưa commit, chưa chạy game):**

| Hạng mục | Kết quả |
|---|---|
| Character mới | 15 ID trong [VIE_md_army_legacy.txt](common/characters/VIE_md_army_legacy.txt) (14 mới + Lê Mạnh tùy chọn) và Trương Mạnh Dũng trong [VIE_md_army_expansion.txt](common/characters/VIE_md_army_expansion.txt) |
| Trait và cost | 45 trait đã đối chiếu với `common/unit_leader` và `common/country_leader` của MD: tồn tại, đúng loại vai trò, advisor đúng slot. Cost theo mẫu upstream |
| Sửa 6 commander submod cũ | Trait `engineer` không tồn tại thành `trait_engineer`; `offensive_doctrine`/`defensive_doctrine` chỉ dành cho field marshal nên đổi sang `adaptable`/`desperate_defender` cho corps commander; điểm kỹ năng đưa về tổng 10 |
| Portrait | 13 ảnh placeholder (silhouette, không phải chân dung thật) bằng [tools/build_vie_placeholder_portraits.py](tools/build_vie_placeholder_portraits.py); header DDS trùng byte với ảnh đang chạy |
| Localisation | Tên và `idea_token` cho mọi nhân vật mới |
| Startup, scheduler, event | Tuyển Giai đoạn 1 lúc khởi động; event .2 đổi roster 2015; event .1 thêm Trương Mạnh Dũng; ngưỡng Quân đoàn 12/34 là 2025.12.31 |
| Tài liệu | Cập nhật 3 báo cáo cũ và [tools/TESTING.md](tools/TESTING.md) |

**Quyết định đã áp dụng (nhánh N của mục 4, bước 5):** khối retire ở startup đã bị xóa **toàn bộ**, event .3 và .4 đã bị xóa, nên cả nhóm upstream Giai đoạn 2 (Giang, Cương, Chiến...) **và** nhóm Hải quân/Không quân (Hậu, Thất, Khoa, Đạm, Nam, Phương) đều có mặt từ 2000 theo history MD, thay vì bị giữ đến 2015 hoặc 2021 như code cũ. Event .2 tuyển 5 character mới của Giai đoạn 2 và rút 10 người của Giai đoạn 1.

**Chưa làm:** thí nghiệm E1-E4 (cần chạy game), thay portrait placeholder bằng ảnh thật, tạo nhánh git và commit, và sửa lỗi thiếu BOM có sẵn ở `VIE_md_mil_l_english.yml`.

**Nếu E1 đạt và muốn đưa nhóm upstream về đúng 2015:** khôi phục khối retire ở startup (chỉ nhóm Giai đoạn 2, bỏ Lịch, Tuấn, Đơn, Việt), thêm lại `recruit_character` cho nhóm đó ở event .2 theo mục 4, bước 6 (nhánh R).

## 1. Nguyên tắc thiết kế (rút từ cách MD làm Trung Quốc)

1. **Roster là ảnh chụp của thời kỳ, không phải đường thời gian.** MD tuyển cả nhóm vào khối `2000.1.1` và không xoay theo năm. Vì vậy submod chỉ có đúng một lần đổi (2015), cộng một mốc phụ 2026 cho nhóm Quân đoàn 12/34.
2. **Chỉ dùng thao tác một chiều đã có tiền lệ:** `recruit_character` (chưa tuyển → đã tuyển) và `retire_character` (đã tuyển → nghỉ, không quay lại). Vòng "retire rồi tuyển lại đúng người đó" chỉ dùng khi thí nghiệm E1 chứng minh được.
3. **Số commander theo công thức MD.** VIE 2000 có 34 sư đoàn, công thức ra khoảng 3-4 tướng; upstream có 1 field marshal + 3 corps commander. v2 giữ **tối đa 6 commander** mỗi giai đoạn, phần còn lại là advisor.
4. **Dùng vai trò kép như MD.** Người đứng đầu tham mưu là `field_marshal` + advisor `army_chief`; tư lệnh quân khu có chức tham mưu cấp cao là `corps_commander` + advisor. Người không chỉ huy quân thì chỉ là advisor.
5. **Điểm kỹ năng theo công thức MD:** `skill` là cấp, và `attack + defense + planning + logistics = (skill - 1) × 3 + 4`. Đã đối chiếu: Vịnh (skill 4) tổng 13; Phí Quốc Tuấn, Ngô Xuân Lịch, Huỳnh Chiến Thắng (skill 3) tổng 10. Công thức khớp, nên dùng cho mọi character mới.
6. **Không chép đè ID upstream.** Chỉ thêm ID `VIE_army_*`.
7. **Chỉ Lục quân.** Trong lúc nghiên cứu mở rộng tôi loại Võ Văn Tuấn (gốc Phòng không-Không quân) và Phạm Ngọc Minh (gốc Hải quân/Cảnh sát biển) dù cả hai là Phó Tổng Tham mưu trưởng.

## 2. Roster v2

Nguồn, ngày giữ chức và độ tin cậy của từng người: xem [roster report](VIE_land_forces_roster_rebuild.md) mục 3, 4 và 10.

### 2.1. Giai đoạn 1 (bookmark 2000, đến hết 2014)

| Nhân vật | ID | Vai trò | Nguồn |
|---|---|---|---|
| Nguyễn Chí Vịnh | `VIE_Nguyen_Chi_Vinh` | `field_marshal` (có sẵn) | Upstream |
| Lê Văn Dũng | `VIE_army_le_van_dung` | `field_marshal` + advisor `army_chief` | **Mới** |
| Phùng Quang Thanh | `VIE_army_phung_quang_thanh` | `corps_commander` + advisor `army_chief` | **Mới** |
| Huỳnh Tiền Phong | `VIE_army_huynh_tien_phong` | `corps_commander` | **Mới (mở rộng)** |
| Phí Quốc Tuấn | `VIE_Phi_Quoc_Tuan` | `corps_commander` (có sẵn) | Upstream |
| Ngô Xuân Lịch | `VIE_Ngo_Xuan_Lich` | `corps_commander` (có sẵn) | Upstream |
| Phạm Văn Trà | `VIE_army_pham_van_tra` | advisor `high_command` | **Mới** |
| Nguyễn Khắc Nghiên | `VIE_army_nguyen_khac_nghien` | advisor `army_chief` | **Mới** |
| Đỗ Bá Tỵ | `VIE_army_do_ba_ty` | advisor `army_chief` | **Mới** |
| Nguyễn Văn Được | `VIE_army_nguyen_van_duoc` | advisor `high_command` | **Mới (mở rộng)** |
| Hoàng Kỳ | `VIE_army_hoang_ky` | advisor `high_command` | **Mới (mở rộng)** |
| Phạm Xuân Hùng | `VIE_army_pham_xuan_hung` | advisor `high_command` | **Mới (mở rộng)** |
| Trần Đơn | `VIE_Tran_Don` | advisor `high_command` (có sẵn) | Upstream |
| Võ Trọng Việt | `VIE_Vo_Trong_Viet` | advisor `high_command`, ledger air (có sẵn) | Upstream |

**Commander: 6** (Vịnh, Dũng, Thanh, Phong, Tuấn, Lịch), đúng giới hạn. **Advisor: 10.** Lê Mạnh bị bỏ khỏi mặc định vì Phong thay vai corps commander của quân khu và vì đã đủ 6. Nếu muốn thêm Mạnh, phải loại một người khác hoặc chấp nhận 7 commander.

Dũng, Thanh, Nghiên, Tỵ cùng chiếm slot `army_chief`, mỗi lần người chơi chỉ chọn được một người, nên game tự giữ đúng chuỗi Tổng Tham mưu trưởng.

### 2.2. Giai đoạn 2 (từ 01/01/2015)

| Nhân vật | ID | Vai trò | Nguồn |
|---|---|---|---|
| Phùng Sĩ Tấn | `VIE_army_phung_si_tan` | `corps_commander` | **Mới (mở rộng)** |
| Nguyễn Doãn Anh | `VIE_army_nguyen_doan_anh` | `corps_commander` | **Mới (mở rộng)** |
| Nguyễn Hồng Thái | `VIE_army_nguyen_hong_thai` | `corps_commander` | **Mới (mở rộng)** |
| Huỳnh Chiến Thắng (tùy chọn) | `VIE_Hyunh_Chien_Thang` | `corps_commander` | Upstream |
| Nguyễn Phương Nam | `VIE_army_nguyen_phuong_nam` | advisor `high_command` | **Mới (mở rộng)** |
| Vũ Hải Sản | `VIE_army_vu_hai_san` | advisor `high_command` | **Mới (mở rộng)** |
| Bế Xuân Trường | `VIE_Be_Xuan_Truong` | advisor `high_command` army | Upstream |
| Võ Minh Lương | `VIE_Vo_Minh_Luong` | advisor `high_command` ledger air | Upstream |
| Phan Văn Giang | `VIE_Phan_Van_Giang` | advisor `high_command` army | Upstream |
| Nguyễn Trọng Nghĩa | `VIE_Nguyen_Trong_Nghia` | advisor `high_command` army | Upstream |
| Hoàng Xuân Chiến | `VIE_Hoang_Xuan_Chien` | advisor `army_chief` | Upstream |
| Nguyễn Tân Cương | `VIE_Nguyen_Tan_Cuong` | advisor `army_chief` | Upstream |
| Lê Xuân Duy | `VIE_Le_Xuan_Duy` | advisor `high_command` army (nhãn B) | Upstream |
| Phạm Văn Hùng | `VIE_Pham_Van_Hung` | advisor `high_command` army (nhãn C) | Upstream |

Ở lại từ Giai đoạn 1: Vịnh, Lịch (commander), Đơn, Việt (advisor). Tổng commander Giai đoạn 2: 5 (6 nếu dùng Thắng).

### 2.3. Mốc phụ: Quân đoàn 12/34 và Quân khu 7

Giữ 7 ID `VIE_army_*` hiện có và event hiện có, dời ngưỡng sang `date > 2025.12.31`. **Thêm 1 người:** Trương Mạnh Dũng (`VIE_army_truong_manh_dung`, `corps_commander`): Tư lệnh Quân đoàn 12 từ 12/2023 đến 24/04/2025, Tư lệnh Quân khu 1 từ 26/04/2025, Phó Tổng Tham mưu trưởng từ 22/06/2026. Tổng nhóm này 8 người.

### 2.4. Tổng kết số lượng

| | Trước (v2 bản đầu) | Bản này |
|---|---|---|
| Character mới cần tạo | 5-6 | **15** |
| Commander Giai đoạn 1 | 4-5 | 6 |
| Commander Giai đoạn 2 | 4-5 | 5-6 |

Cách đếm 15 ID mới: 5 từ báo cáo gốc (Dũng, Trà, Thanh, Nghiên, Tỵ; Mạnh đã bị bỏ) + 9 mở rộng cho hai giai đoạn (Phong, Được, Kỳ, Xuân Hùng, Tấn, Doãn Anh, Thái, Nam, Sản) + 1 cho nhóm submod (Trương Mạnh Dũng). Cộng 9 và 1 cho đúng 10 người mở rộng. Mục 4, bước 2 liệt kê đủ 15 ID.

## 3. Thí nghiệm bắt buộc trước khi code (khoảng 15 phút)

Làm trên bản sao save, bật `debug`, chơi VIE.

| # | Thí nghiệm | Kết quả | Hệ quả |
|---|---|---|---|
| **E1** | `effect retire_character = VIE_Phan_Van_Giang` rồi `effect recruit_character = VIE_Phan_Van_Giang`, mở panel advisor | Giang xuất hiện lại | **Nhánh R** |
| | | Không xuất hiện | **Nhánh N** |
| **E2** | Tạo character thử có `visible = { has_global_flag = TEST }`; kiểm tra bị ẩn, rồi `effect set_global_flag = TEST`; kiểm tra hiện ra | Hiện ra | Có thể dùng `visible` cho phần mở rộng (mục 6) |
| **E3** | Character thử không có khối `portraits` | `error.log` không báo lỗi | Bỏ qua ảnh cho 15 character mới (chỉ Trà, Thanh, Tỵ có ảnh) |
| **E4** | Character advisor thử thiếu khóa localisation `idea_token` | Hiển thị khóa trần hay tên | Xác nhận cần khóa chữ thường như trường hợp Trần Đại Thắng |

E3 giờ quan trọng hơn trước: 12 trong 15 character mới chưa có portrait.

## 4. Các bước code

### Bước 1: Nhánh git

Tạo `claude/land-roster-v2` từ `main`. Mỗi bước dưới đây một commit.

### Bước 2: Character mới (không phụ thuộc E1)

**File mới:** `common/characters/VIE_md_army_legacy.txt`, theo khuôn [VIE_md_army_expansion.txt](common/characters/VIE_md_army_expansion.txt). Có thể tách thành hai file (`..._phase1.txt`, `..._phase2.txt`) nếu muốn dễ quản lý.

**Commander (10 người).** Mọi dòng: `skill = 3`, tổng bốn chỉ số = 10 theo công thức.

| ID | Khối | attack / defense / planning / logistics | Trait (đề xuất, đã có trong repo hoặc upstream) |
|---|---|---|---|
| `VIE_army_le_van_dung` | `field_marshal` | 2 / 3 / 3 / 2 | `defensive_doctrine organizer` |
| `VIE_army_phung_quang_thanh` | `corps_commander` | 2 / 3 / 3 / 2 | `organizer infantry_leader` |
| `VIE_army_huynh_tien_phong` | `corps_commander` | 4 / 2 / 2 / 2 | `jungle_rat infantry_leader` |
| `VIE_army_phung_si_tan` | `corps_commander` | 2 / 3 / 3 / 2 | `hill_fighter infantry_leader` |
| `VIE_army_nguyen_doan_anh` | `corps_commander` | 3 / 2 / 3 / 2 | `organizer infantry_leader` |
| `VIE_army_nguyen_hong_thai` | `corps_commander` | 2 / 3 / 2 / 3 | `hill_fighter organizer` |
| `VIE_army_truong_manh_dung` | `corps_commander` | 3 / 2 / 3 / 2 | `offensive_doctrine organizer` |

Phong: Anh hùng lực lượng vũ trang, hồ sơ chiến đấu nên thiên về tấn công. Thanh và Thái thuộc Quân khu 1 (núi phía Bắc) nên một người có `hill_fighter`. Đây là điểm khởi đầu để cân bằng, không phải dữ kiện lịch sử.

**Advisor (tất cả có `ai_will_do = { factor = 1 }`, `ledger = army`):**

| ID | Slot | `idea_token` | Trait | cost |
|---|---|---|---|---|
| `VIE_army_le_van_dung` (khối advisor thêm vào cùng nhân vật) | `army_chief` | `vie_army_le_van_dung` | `army_chief_reform_2` | 150 |
| `VIE_army_phung_quang_thanh` (khối advisor thêm vào cùng nhân vật) | `army_chief` | `vie_army_phung_quang_thanh` | `army_chief_logistics_1` | 100 |
| `VIE_army_nguyen_khac_nghien` | `army_chief` | `vie_army_nguyen_khac_nghien` | `army_chief_drill_2` | 100 |
| `VIE_army_do_ba_ty` | `army_chief` | `vie_army_do_ba_ty` | `army_chief_logistics_2` | 100 |
| `VIE_army_pham_van_tra` | `high_command` | `vie_army_pham_van_tra` | `army_entrenchment_2` | 100 |
| `VIE_army_nguyen_van_duoc` | `high_command` | `vie_army_nguyen_van_duoc` | `army_entrenchment_1` | 100 |
| `VIE_army_hoang_ky` | `high_command` | `vie_army_hoang_ky` | `army_militia_2` | 100 |
| `VIE_army_pham_xuan_hung` | `high_command` | `vie_army_pham_xuan_hung` | `army_artillery_2` | 100 |
| `VIE_army_nguyen_phuong_nam` | `high_command` | `vie_army_nguyen_phuong_nam` | `army_regrouping_2` | 100 |
| `VIE_army_vu_hai_san` | `high_command` | `vie_army_vu_hai_san` | `army_infantry_3` | 125 |

Các trait trên đều đã có trong upstream VIE hoặc CHI. Mức `cost` theo mẫu upstream (cấp trait 3 thì 125, cấp 2 trở xuống thì 100, `reform_2` thì 150).

**Portrait:** Trà, Thanh, Tỵ dùng file có sẵn (`gfx/leaders/VIE/Portrait_*.dds` và bản `small`). 12 người còn lại chưa có ảnh: bỏ khối `portraits` nếu E3 đạt, nếu không thì dùng ảnh tạm. Kích thước ảnh theo MD: 156×210 (lớn), 38×51 (nhỏ).

**Skill của nhóm submod hiện có lệch công thức:** `VIE_army_le_xuan_thuan` tổng 11, `VIE_army_nguyen_thanh_pho` tổng 11, `VIE_army_le_xuan_the` (`field_marshal` skill 3) tổng 12, trong khi công thức cho 10. Sửa tùy ý, không chặn plan.

### Bước 3: Localisation (không phụ thuộc E1)

Sửa [VIE_army_commanders_l_english.yml](localisation/english/VIE_army_commanders_l_english.yml), theo khuôn của 7 dòng hiện có. Mỗi nhân vật có advisor cần **cả hai khóa** (ID và `idea_token` chữ thường):

```yaml
 VIE_army_le_van_dung:0 "Lê Văn Dũng"
 vie_army_le_van_dung:0 "Lê Văn Dũng"
 VIE_army_pham_van_tra:0 "Phạm Văn Trà"
 vie_army_pham_van_tra:0 "Phạm Văn Trà"
 VIE_army_phung_quang_thanh:0 "Phùng Quang Thanh"
 vie_army_phung_quang_thanh:0 "Phùng Quang Thanh"
 VIE_army_nguyen_khac_nghien:0 "Nguyễn Khắc Nghiên"
 vie_army_nguyen_khac_nghien:0 "Nguyễn Khắc Nghiên"
 VIE_army_do_ba_ty:0 "Đỗ Bá Tỵ"
 vie_army_do_ba_ty:0 "Đỗ Bá Tỵ"
 VIE_army_huynh_tien_phong:0 "Huỳnh Tiền Phong"
 VIE_army_nguyen_van_duoc:0 "Nguyễn Văn Được"
 vie_army_nguyen_van_duoc:0 "Nguyễn Văn Được"
 VIE_army_hoang_ky:0 "Hoàng Kỳ"
 vie_army_hoang_ky:0 "Hoàng Kỳ"
 VIE_army_pham_xuan_hung:0 "Phạm Xuân Hùng"
 vie_army_pham_xuan_hung:0 "Phạm Xuân Hùng"
 VIE_army_nguyen_phuong_nam:0 "Nguyễn Phương Nam"
 vie_army_nguyen_phuong_nam:0 "Nguyễn Phương Nam"
 VIE_army_vu_hai_san:0 "Vũ Hải Sản"
 vie_army_vu_hai_san:0 "Vũ Hải Sản"
 VIE_army_phung_si_tan:0 "Phùng Sĩ Tấn"
 VIE_army_nguyen_doan_anh:0 "Nguyễn Doãn Anh"
 VIE_army_nguyen_hong_thai:0 "Nguyễn Hồng Thái"
 VIE_army_truong_manh_dung:0 "Trương Mạnh Dũng"
```

Giữ BOM UTF-8. Lưu ý tên "Phạm Xuân Hùng" (`VIE_army_pham_xuan_hung`) khác "Phạm Văn Hùng" (`VIE_Pham_Van_Hung`, upstream): hai người khác nhau, dễ nhầm khi tìm kiếm. Sửa "Phi" thành "Phí" cho Phí Quốc Tuấn là việc tùy chọn, làm sau cùng.

### Bước 4: Tuyển Giai đoạn 1 (không phụ thuộc E1)

Sửa [VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt), trong scope `VIE = { ... }`:

```txt
if = {
	limit = {
		date < 2015.1.1
		NOT = { has_country_flag = VIE_army_phase1_recruited }
	}
	recruit_character = VIE_army_le_van_dung
	recruit_character = VIE_army_phung_quang_thanh
	recruit_character = VIE_army_huynh_tien_phong
	recruit_character = VIE_army_pham_van_tra
	recruit_character = VIE_army_nguyen_khac_nghien
	recruit_character = VIE_army_do_ba_ty
	recruit_character = VIE_army_nguyen_van_duoc
	recruit_character = VIE_army_hoang_ky
	recruit_character = VIE_army_pham_xuan_hung
	set_country_flag = VIE_army_phase1_recruited
}
```

Cờ bắt buộc vì `on_startup` chạy cả khi load save. Chỉ dùng thao tác một chiều nên bước này chắc chắn.

### Bước 5: Khối retire ở startup (phụ thuộc E1)

Khối `if date < 2015.1.1 { retire_character ... }` hiện có.

| | Nhánh R (E1 đạt) | Nhánh N (E1 không đạt) |
|---|---|---|
| Khối retire | Giữ, nhưng **xóa 4 dòng**: Lịch, Tuấn, Đơn, Việt | **Xóa cả khối.** Upstream giữ nguyên như history MD đã tuyển |
| Giai đoạn 2 upstream | Vắng đến 2015, tuyển lại ở event | Có mặt từ 2000 như MD thiết kế |
| Giai đoạn 2 mới (Tấn, Doãn Anh, Thái, Nam, Sản) | Tuyển ở event 2015 (không phụ thuộc E1: đây là ID chưa từng tuyển) | Như nhánh R |
| Tính chính xác lịch sử | Cao hơn | Giảm cho nhóm upstream: Giang, Cương, Chiến... có mặt sớm |

**Hải quân/Không quân** (Hậu, Thất, Khoa, Đạm, Nam, Phương): ở nhánh R vẫn nằm trong khối retire như hiện tại. Ở nhánh N chúng cũng có mặt từ đầu như MD. Cân nhắc kỹ trước khi xóa, vì ngoài phạm vi báo cáo này. (Lưu ý "Nam" ở đây là Phạm Hoài Nam, Hải quân, khác Nguyễn Phương Nam.)

### Bước 6: Event và scheduler

**Scheduler** [VIE_md_effects_p16.txt](common/scripted_effects/VIE_md_effects_p16.txt) (chạy hằng tháng từ `on_monthly`):

| Khối | Thay đổi |
|---|---|
| 2015 (`.2`) | Bỏ dòng `NOT = { has_character = VIE_Ngo_Xuan_Lich }` |
| 2016 (`.3`) | Xóa cả khối |
| 2021 (`.4`) | Bỏ dòng `NOT = { has_character = VIE_Nguyen_Tan_Cuong }`. Nhánh N: cũng xóa khối này nếu không còn ai để tuyển |
| 7+1 commander | `date > 2022.12.31` thành `date > 2025.12.31` |

**Event** [VIE_army_commanders.txt](events/VIE_army_commanders.txt), `vie_army_commanders.2`:

*Nhánh R:*

```txt
immediate = {
	# Giai đoạn 2, character mới (không phụ thuộc E1)
	recruit_character = VIE_army_phung_si_tan
	recruit_character = VIE_army_nguyen_doan_anh
	recruit_character = VIE_army_nguyen_hong_thai
	recruit_character = VIE_army_nguyen_phuong_nam
	recruit_character = VIE_army_vu_hai_san
	# Giai đoạn 2, upstream (chỉ nhánh R)
	recruit_character = VIE_Be_Xuan_Truong
	recruit_character = VIE_Vo_Minh_Luong
	recruit_character = VIE_Phan_Van_Giang
	recruit_character = VIE_Nguyen_Trong_Nghia
	recruit_character = VIE_Hoang_Xuan_Chien
	recruit_character = VIE_Nguyen_Tan_Cuong
	recruit_character = VIE_Le_Xuan_Duy
	recruit_character = VIE_Pham_Van_Hung
	recruit_character = VIE_Hyunh_Chien_Thang   # tùy chọn
	# Giữ nguyên ngày hiện có, ngoài phạm vi Lục quân
	recruit_character = VIE_Nguyen_Quang_Dam
	recruit_character = VIE_Pham_Kim_Hau
	recruit_character = VIE_Tran_Viet_Khoa
	recruit_character = VIE_Dinh_Gia_That
	# Rút nhóm Giai đoạn 1 hết vai trò
	retire_character = VIE_army_le_van_dung
	retire_character = VIE_army_pham_van_tra
	retire_character = VIE_army_phung_quang_thanh
	retire_character = VIE_army_nguyen_khac_nghien
	retire_character = VIE_army_do_ba_ty
	retire_character = VIE_army_huynh_tien_phong
	retire_character = VIE_army_nguyen_van_duoc
	retire_character = VIE_army_hoang_ky
	retire_character = VIE_army_pham_xuan_hung
	retire_character = VIE_Phi_Quoc_Tuan
	set_country_flag = VIE_md_roster_recruited_2015
	clr_country_flag = VIE_md_roster_event_pending
}
```

*Nhánh N:* bỏ khối "Giai đoạn 2, upstream" và khối "Giữ nguyên ngày hiện có"; giữ 5 dòng tuyển character mới và toàn bộ `retire_character`.

Cả hai nhánh: xóa event `.3` (kèm khóa `vie_army_commanders.3.a`); `.4` chỉ còn `VIE_Pham_Hoai_Nam` và `VIE_Tran_Quang_Phuong` ở nhánh R (nhánh N: xóa luôn); `.1` thêm `recruit_character = VIE_army_truong_manh_dung`.

## 5. Kiểm tra

**Kiểm tra tĩnh** (xem [tools/TESTING.md](tools/TESTING.md), [tools/audit/README.md](tools/audit/README.md)):

```bash
python3 tools/verify_all_loc.py
python3 tools/audit/live.py
python3 tools/audit/ev.py
```

**Trong game** (chưa ai từng chạy): đọc `error.log` (tìm `VIE`, `character`, `portrait`), rồi đối chiếu số mong đợi.

| Thời điểm | Commander Lục quân | Advisor |
|---|---|---|
| 01/2000 | Vịnh, Dũng, Thanh, Phong, Tuấn, Lịch = **6** | Dũng, Thanh, Nghiên, Tỵ (army_chief); Trà, Được, Kỳ, Xuân Hùng, Đơn, Việt (high_command) |
| Sau 01/2015, nhánh R | Vịnh, Lịch, Tấn, Doãn Anh, Thái (+ Thắng) = **5-6** | Đơn, Việt, Nam, Sản, Bế, Lương, Giang, Nghĩa, Chiến, Cương, Duy, Hùng |
| Sau 01/2015, nhánh N | Như nhánh R | Như nhánh R (nhóm upstream đã có từ đầu) |
| Sau 01/2026 | Thêm 8 commander submod | |

Không còn Dũng, Thanh, Phong, Tuấn, Trà, Nghiên, Tỵ, Được, Kỳ, Xuân Hùng sau 2015.

Test console: `tag VIE`, `event vie_army_commanders.2` để kiểm tra đổi roster ngay. Load save giữa giai đoạn (2007, 2016) để chắc chắn không tuyển lặp và roster đúng giai đoạn.

## 6. Mở rộng tùy chọn (chỉ khi E2 đạt)

Gắn `visible` vào character của mình để chia nhỏ thời điểm mà không cần event:

```txt
visible = { date > 2001.5.1 }
```

Có thể áp cho chuỗi Tổng Tham mưu trưởng (Thanh từ 05/2001, Nghiên từ 08/2006, Tỵ từ 11/2010) và nhóm quân khu (Tấn từ 12/2016, Doãn Anh từ 11/2018, Thái từ 10/2019). Cần thí nghiệm thêm: khi `visible` chuyển từ đúng sang sai lúc advisor đã được thuê, người đó có bị gỡ khỏi slot không. Chưa kiểm chứng nên **không nằm trong phạm vi v2**.

## 7. Rủi ro

| Rủi ro | Xử lý |
|---|---|
| Nhánh N làm mất chính xác lịch sử ở Giai đoạn 2 | Chấp nhận như MD, ghi rõ vào changelog |
| 12 character không có portrait gây lỗi | E3; dùng ảnh tạm |
| Tuyển lặp khi load save | Cờ `VIE_army_phase1_recruited` |
| Save cũ đã chạy event 2015 theo bản cũ | Không retire nhóm cũ cho save đó; ghi changelog |
| Thanh, Tỵ, Xuân Hùng bị rút sớm 1-2 năm | Chấp nhận |
| Nhóm mới Tấn, Doãn Anh, Thái xuất hiện sớm 1-4 năm so với chức vụ | Chấp nhận theo yêu cầu hai giai đoạn |
| Tên trùng gần: Phạm Xuân Hùng / Phạm Văn Hùng, Nguyễn Phương Nam / Phạm Hoài Nam | Dùng ID đầy đủ khi tìm kiếm, ghi chú trong file character |
| Dữ liệu 4 người mở rộng chỉ có một nguồn (Được, Kỳ, Xuân Hùng, Thái) | Nhãn B trong roster report; xác minh thêm nếu có điều kiện |

## 8. Ngoài phạm vi

- Hải quân và Không quân (chỉ giữ nguyên).
- Nguyễn Quang Đạm.
- Làm ảnh portrait mới cho 12 người.
- Cân bằng chi tiết ngoài công thức điểm kỹ năng.
- Commander cho các quân khu khác ngoài những người ở mục 2.

## 9. Việc dọn tài liệu

| File | Sửa |
|---|---|
| [VIE_land_forces_roster_rebuild.md](VIE_land_forces_roster_rebuild.md) | Đã thêm mục 10 (10 tướng mở rộng); đồng bộ vai trò Dũng, Thanh, Nghiên, Tỵ; bỏ Mạnh khỏi mặc định |
| [VIE_generals_and_commander_system_research_report.md](VIE_generals_and_commander_system_research_report.md) | Bỏ "tuyển khi khởi động", "8 portrait", "chưa có portrait riêng" |
| [VIE_commander_timeline_research_report.md](VIE_commander_timeline_research_report.md) | Bỏ mốc 2005 và đoạn "Chí Vịnh căn cứ mạnh ở 2000" |
| [tools/TESTING.md](tools/TESTING.md) | Thêm mục kiểm tra roster như mục 5 |

## 10. Nguồn

- [MD New General Guidelines](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/new-general-guidelines/) (công thức số tướng và điểm kỹ năng; tôi chỉ đọc qua bản tóm tắt tự động, nên đối chiếu lại với trang gốc)
- [HOI4 Character modding](https://hoi4.paradoxwikis.com/Character_modding)
- [MD VIE.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/characters/VIE.txt) và [CHI.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/characters/CHI.txt)
- [tools/audit/md_ref/CHI.txt](tools/audit/md_ref/CHI.txt), [VIE_2000_nsb.txt](tools/audit/md_ref/VIE_2000_nsb.txt) (34 sư đoàn)
- Nguồn từng người trong mục 10 của [roster report](VIE_land_forces_roster_rebuild.md).
