# Millennium Dawn: schema character và roster VIE đã có sẵn

**Ngày kiểm tra:** 01/10/2026  
**Nguồn chính:** `MillenniumDawn/Millennium-Dawn/common/characters/VIE.txt` và `history/countries/VIE - Vietnam.txt` trên GitHub.

## 1. Kết luận quan trọng

Millennium Dawn upstream **đã có character file VIE và đã recruit các nhân vật này trong history Việt Nam**. Submod không được tạo lại các ID `VIE_*` trùng với upstream.

Roster upstream hiện có:

- 1 `field_marshal`.
- 3 `corps_commander` được định nghĩa, trong đó 2 được recruit history và `VIE_Hyunh_Chien_Thang` hiện không nằm trong danh sách recruit.
- 1 `navy_leader`.
- Nhóm advisor cho `army_chief`, `navy_chief`, `air_chief` và `high_command`.
- History VIE tuyển 19 character.

## 2. Schema live của Millennium Dawn

File character dùng wrapper:

```txt
characters = {
	TAG_character_id = {
		name = "Displayed Name"
		portraits = {
			army = {
				small = "gfx/leaders/TAG/small/Portrait_small.dds"
				large = "gfx/leaders/TAG/Portrait.dds"
			}
		}
		field_marshal = {
			traits = { trait_name }
			skill = 3
			attack_skill = 3
			defense_skill = 3
			planning_skill = 3
			logistics_skill = 3
		}
	}
}
```

Role block hợp lệ trong MD gồm:

- `field_marshal`
- `corps_commander`
- `navy_leader`
- `advisor`

### Advisor schema

```txt
advisor = {
	slot = army_chief # army_chief / navy_chief / air_chief / high_command
	idea_token = character_token
	ledger = army # bắt buộc cho high_command; army / navy / air
	traits = {
		army_chief_logistics_2
	}
	cost = 100
	ai_will_do = {
		factor = 1
	}
}
```

### Commander schema

Lục quân dùng:

```txt
corps_commander = {
	traits = { infantry_leader }
	skill = 3
	attack_skill = 2
	defense_skill = 3
	planning_skill = 3
	logistics_skill = 2
}
```

Field marshal dùng cùng bốn skill chiến dịch. Hải quân dùng schema riêng:

```txt
navy_leader = {
	traits = { navy_career_officer chief_engineer naval_lineage }
	skill = 4
	attack_skill = 4
	defense_skill = 2
	maneuvering_skill = 3
	coordination_skill = 4
}
```

Không dùng `create_country_leader` cho commander. Đó là hệ lãnh đạo chính trị riêng.

## 3. Roster 8 nhân vật chắc dữ kiện để làm mẫu

Đây là **8 character đã tồn tại upstream**, không tạo lại ID.

| ID | Vai trò MD | Dữ liệu upstream đáng chú ý |
|---|---|---|
| `VIE_Nguyen_Chi_Vinh` | `field_marshal` | `trait_engineer`, `hill_fighter`, `jungle_rat`, `organizer`; skill 4, attack 3, defense 2, planning 3, logistics 5 |
| `VIE_Phi_Quoc_Tuan` | `corps_commander` | `old_guard`, `skilled_staffer`; skill 3, attack 2, defense 2, planning 4, logistics 2 |
| `VIE_Nguyen_Tan_Cuong` | `army_chief` | `army_chief_logistics_2`, cost 100 |
| `VIE_Phan_Van_Giang` | `high_command`, ledger army | `army_armored_1`, cost 100 |
| `VIE_Pham_Hoai_Nam` | `navy_chief`, ledger navy | `navy_chief_reform_2`, cost 150 |
| `VIE_Dinh_Gia_That` | `navy_chief` + `navy_leader` | Advisor `navy_chief_maneuver_2`; commander traits `navy_career_officer`, `chief_engineer`, `naval_lineage`; skill 4, attack 4, defense 2, maneuvering 3, coordination 4 |
| `VIE_Tran_Don` | `high_command`, ledger army | `army_infantry_3`, cost 125 |
| `VIE_Be_Xuan_Truong` | `high_command`, ledger army | `army_militia_2`, cost 100 |

Roster này phủ đủ bốn nhóm gameplay: chỉ huy chiến dịch, tham mưu lục quân, hải quân và high command.

## 4. Character upstream nhưng cần lưu ý

| ID | Tình trạng |
|---|---|
| `VIE_Ngo_Xuan_Lich` | Có `corps_commander`, được recruit history; cần đọc tiếp block đầy đủ nếu cân bằng trait/skill |
| `VIE_Hyunh_Chien_Thang` | Có `corps_commander`, nhưng không được recruit trong history VIE hiện tại |
| `VIE_Nguyen_Quang_Dam` | `army_chief`, reform trait |
| `VIE_Nguyen_Trong_Nghia` | `high_command`, army entrenchment |
| `VIE_Pham_Kim_Hau` | `navy_chief`, maneuver |
| `VIE_Pham_Van_Hung` | `high_command`, army regrouping |
| `VIE_Tran_Quang_Phuong` | `air_chief`, air reform |
| `VIE_Tran_Viet_Khoa` | `air_chief`, bomber interception |
| `VIE_Vo_Minh_Luong` | `high_command`, ledger air |
| `VIE_Vo_Trong_Viet` | `high_command`, ledger air |
| `VIE_Le_Xuan_Duy` | `high_command`, artillery |
| `VIE_Hoang_Xuan_Chien` | `army_chief`, drill |

## 5. Quy ước kiến trúc của MD

### File ownership

- `common/characters/VIE.txt`: định nghĩa character.
- `history/countries/VIE - Vietnam.txt`: `recruit_character` character vào quốc gia.
- `gfx/leaders/VIE/`: portrait lớn/nhỏ.
- `common/country_leader/`: trait của advisor/high command.
- `common/ideas/`: idea token và national spirits nếu advisor cần.
- `localisation/english/`: tên character và tên idea token.

### Naming

- ID dùng `VIE_` + tên Latin hóa, không dấu.
- `name` có thể là chuỗi hiển thị Latin hóa theo convention MD.
- Portrait dùng đường dẫn trực tiếp `gfx/leaders/VIE/...dds` trong character file.
- `idea_token` dùng snake_case, thường trùng tên nhân vật không có prefix quốc gia.
- Không tạo thêm sprite GFX riêng nếu character đã dùng đường dẫn portrait trực tiếp theo MD.

### Recruitment

History VIE đã có dạng:

```txt
recruit_character = VIE_Nguyen_Chi_Vinh
recruit_character = VIE_Ngo_Xuan_Lich
recruit_character = VIE_Phi_Quoc_Tuan
...
```

Không thêm các lệnh này vào `on_startup` nếu history đã recruit; làm vậy dễ tạo duplicate hoặc lỗi tuyển lặp.

### Trait và skill

- Không gán skill chỉ dựa vào cấp hàm.
- `field_marshal` dùng planning/logistics để phản ánh tham mưu chiến dịch.
- `corps_commander` dùng attack/defense/planning theo hồ sơ chỉ huy.
- `navy_leader` dùng `maneuvering_skill` và `coordination_skill`, không dùng `planning_skill`.
- Advisor trait phải thuộc đúng pool: `army_chief_*`, `navy_chief_*`, `air_chief_*`, `army_*`, `air_*`, `navy_*`.
- Không tự tạo trait mới nếu trait MD hiện có đã diễn đạt đúng vai trò.

## 6. Những gì đã sửa trong submod sau khi kiểm tra GitHub

Trước khi kiểm tra upstream, submod đã tạm thêm 8 ID `VIE_cmd_*`. Sau khi xác nhận MD đã có character VIE, các thay đổi duplicate đã được gỡ:

- Không còn `VIE_cmd_*` trong workspace.
- Không còn `recruit_character = VIE_cmd_*`.
- Không còn file character/portrait/localization duplicate.
- `common/on_actions/VIE_md_on_actions_startup.txt` không tuyển commander mới.

Đây là trạng thái đúng: dùng roster base của MD, chỉ override khi có nhu cầu gameplay cụ thể và ID mới thật sự cần thiết.

## 7. Hướng mở rộng an toàn

Nếu muốn mô phỏng chuyển giao commander theo thời gian:

1. Giữ nguyên character ID upstream.
2. Dùng event/focus để bật/tắt `visible` hoặc thay advisor role, không định nghĩa lại character.
3. Chỉ thêm character mới khi người đó không tồn tại trong `common/characters/VIE.txt` upstream.
4. Trước khi thêm, kiểm tra cả `VIE.txt` và `history/countries/VIE - Vietnam.txt` để tránh trùng ID và recruit lặp.
5. Test `error.log` sau khi load bookmark 2000 và tuyển character.

## Nguồn GitHub

- [VIE character definitions](https://github.com/MillenniumDawn/Millennium-Dawn/blob/main/common/characters/VIE.txt)
- [VIE country history](https://github.com/MillenniumDawn/Millennium-Dawn/blob/main/history/countries/VIE%20-%20Vietnam.txt)
- [MD add-leader skill](https://github.com/MillenniumDawn/Millennium-Dawn/blob/main/.claude/skills/add-leader/SKILL.md)
- [MD character validator](https://github.com/MillenniumDawn/Millennium-Dawn/blob/main/tools/validation/validate_characters.py)
