# Lục quân Việt Nam: 42 focus, v39

## Baseline và phạm vi

Triển khai trên `b63e463648b4d1a043f51f8b5b2add69afbea56a`, ngày 10/10/2026.
Người dùng đã yêu cầu bắt đầu code sau implementation plan trong chat.
Nhánh làm việc: `codex/vietnam-land-force-42`. Dành cho ván mới; không có migration
save V31, không phục hồi những chương trình đã được người dùng xóa.

Cây có 359 focus: 317 focus baseline giữ nguyên nội dung, thêm 42 focus mới.
37 ID lấy lại từ snapshot `7e7e5d1`; 5 ID công nghiệp lục quân mới.
`structure.json` lưu hợp đồng graph, tọa độ, cost, gate ngày và hash các focus ngoài
phạm vi. Validator đọc implementation thật và đối chiếu hợp đồng này.

## Cấu trúc

- L0 mở D1, B1, I1; ba chương trình song song.
- D6 cần D4 AND D5; B7 cần B3 AND B4; B8 cần B6 AND B7.
- I4 cần I2 AND I3; I5 chỉ cần I4 và mốc 2025, không phải gate của F2.
- P1/M1/R1 mở từ B8, mutex đối xứng ba cặp.
- Mỗi capstone route cần đủ hai tuyến chuyên sâu.
- F1 cần P6 OR M6 OR R6; F2 cần F1 AND D8 bằng hai prerequisite rõ ràng.
- Không có focus Đặc công hoặc synergy dựa vào Đặc công.
- Mỗi ván hoàn thành một route: 30 focus nếu lấy đủ I, 25 nếu bỏ cả nhánh I.

Không thay học thuyết bằng `set_grand_doctrine`. Spirit ưu tiên thể hiện phân bổ
đầu tư; bậc sau thay bậc trước. Các modifier chung dùng backing variable của
`VIE_armed_forces_modifier`; không sửa định nghĩa dynamic modifier hiện hữu.

## Khác biệt cần thiết so với plan

HEAD mới xóa procurement sau khi plan được lập. Vì vậy:

- Không phục hồi `VIE_md_effects_p14.txt`, event, scheduler hoặc game rule mua sắm.
- M2 chuẩn bị giáo trình/mô phỏng/bảo dưỡng, nhận 15 XP/mastery; không cấp T-90,
  không thêm cờ hoặc bonus conditional T-90 không có writer.
- Không thêm route flags chỉ để phục vụ consumer procurement đã bị xóa.
- Không giữ ưu đãi thời gian dựa trên `VIE_bmp3_lessons` đã mất nguồn cấp.
- XCB nghiên cứu 365 ngày, đánh giá 180 ngày, chuẩn bị loạt 365 ngày.

Gate B2 năm 2015, B7 năm 2020, I4 năm 2022, I5 năm 2025 theo plan. B7 là tiền đề
bắt buộc của cả ba route nên P/M/R không mở trước 2020. B1 là cải tổ chung;
description không khẳng định Quân đoàn 12/34 tồn tại từ năm 2000.

## Reward và vòng đời

Reward mỗi focus có country guard và cờ `VIE_lf_reward_<mã>_applied` chống replay.
Trigger achieved kiểm completed focus OR reward flag để reconciliation thấy
trạng thái ngay trong completion reward. Cờ này không thay prerequisite của cây.
Không khởi tạo biến bằng 0 và không thêm scheduler định kỳ.

Reconciliation được gọi từ mọi completion và bàn giao chương trình. Nó chỉ
chuẩn hóa spirit, không cộng lại variable, XP hoặc research bonus:

- D1/D4/D8: core defence 1%/2%/4%, một bậc tại một thời điểm.
- P/M/R: một spirit ưu tiên bậc 1 hoặc bậc 2.
- I2 AND (D6 OR P5): attrition -1%, không thưởng hai lần.
- M3 AND I3 AND I4: training time -1%, không phụ thuộc thứ tự hoàn thành.
- Hoàn tất serial preparation: IFV IC cost -5% qua equipment bonus.

## XCB-01

Ba decision trong category `VIE_military_readiness_category` hiện hữu. Focus I4/I5
chỉ mở chương trình, không hoàn tất thiết kế hay sản xuất loạt.

| Giai đoạn | Chi phí treasury | Thời gian | Điều kiện bổ sung |
|---|---:|---:|---|
| Thiết kế | 0,6 tỷ | 365 ngày | I4 |
| Đánh giá chế thử | 0,3 tỷ | 180 ngày | Thiết kế hoàn tất; technology nền phù hợp |
| Chuẩn bị loạt | 0,6 tỷ | 365 ngày | I5; đánh giá hoàn tất |

Với NSB, gate kỹ thuật là `mbt_tech_2`; trường hợp còn lại là `IFV_4`.
Đây là nền kỹ thuật đã có trong MD, không phải một technology XCB mới.
MD dùng `medium_tank_flame_chassis` làm archetype IFV; production bonus theo mẫu
`POL_ifv_production` trong bản cài đặt.

Khả dụng và start effect đều kiểm treasury >= chi phí, chưa running/done và không
bankruptcy. Chi phí PP là 0. Thanh toán qua `modify_treasury_effect`, không tự vay.
Start đặt running; remove effect sau days_remove đặt done, xóa running và bàn giao.
Không fire_only_once, không cancellation trigger, không auto stockpile/factory.
Engine timer, capitulation/civil-war và save thật vẫn phải kiểm trong game.

## AI và tài nguyên

Hai persona hiện hữu giữ nguyên. Historical ưu tiên P, Hardline ưu tiên M;
focus miễn phí không có bankruptcy factor 0. Decision đắt bảo vệ dự trữ AI.
Force mix cũ tắt khi đã chọn M/R; strategy hẹp sau lựa chọn sử dụng role của MD.
Không thay generic templates, research overrides, naval AI hoặc scheduler.

Reuse 26 texture focus cho 42 consumer, không sửa sprite hay master ảnh.
`icons_native.png` là contact sheet 1:1 để QA, không phải texture được game nạp.
Spirit reuse `army_planning`, `generic_central_planning` và icon XCB hiện hữu.
Localisation mới nằm ở file thường, UTF-8 BOM, l_english, nội dung tiếng Việt.

## Kiểm tra tích hợp trước merge

Ba commit `aff8efe`, `97bbb91`, `50ec587` gộp localisation, events và effects
trên cùng nhánh triển khai. Giữ cấu trúc gộp này: 51 effect `VIE_lf_*` nằm trong
`common/scripted_effects/VIE_md_effects.txt`; 182 key mới nằm trong
`localisation/english/VIE_md_military_l_english.yml`. Validator balance đọc
effect thật trong file gộp và chỉ chọn namespace lục quân để kiểm reward caps.

Đối chiếu AST trước/sau gộp: cả 240 effect cũ giữ nguyên, không trùng định nghĩa;
185 event và 20 namespace giữ nguyên. Đối chiếu localisation sau khi áp dụng
ưu tiên `replace`: giữ nguyên cả 3818 key nền và giá trị, thêm đúng 182 key mới.
Kiểm tra lại toàn bộ bộ lệnh bên dưới sau khi cập nhật đường dẫn validator.
`main` local và remote được xác minh cùng ở `b63e463` trước merge; không có
thay đổi phân kỳ phải chọn giữa hai phía. Merge dùng commit riêng để giữ lịch sử.
Kiểm tra diff toàn merge phát hiện dòng trống dư cuối 10 file gộp từ các commit
refactor; chỉ bỏ dòng trống dư, giữ BOM và kiểu xuống dòng, không đổi gameplay.

## Kiểm tra đã chạy

- `land_42_structure.py`: PASS; graph, ngày/cost/anchor/mutex, ba route và toàn bộ
  317 focus ngoài phạm vi/protected files được giữ nguyên.
- `land_42_balance.py --md <MD cài đặt>`: PASS; đọc script/effect/idea thật, kiểm
  replay, thay bậc, mọi thứ tự hợp lệ của synergy, XP/mastery, ngày, scope,
  ngưỡng tiền, bankruptcy và ba giai đoạn trên cả hai DLC paths.
- Provider MD: category, technology gate, IFV archetype và spirit sprites đã tra
  định nghĩa trong MD 2.0.2 cài đặt cho HOI4 1.19.*.
- Focus audit: 359 focus; không dangling/collision/forward anchor/cycle.
- Live audit: MISSING=0; còn một idea hải quân mồ côi baseline.
- Loc syntax/coverage: 0 lỗi; đủ title/description/tooltip. Toàn bộ loc: 4000 key,
  không lỗi được validator báo.
- Event audit: không event trùng/mồ côi/thiếu loc của event hiển thị.
- DDS: 382 file, 0 format/content error, 0 texture thiếu. Riêng 42 focus mới:
  26 DDS hiện hữu, 93x91 RGBA, 33980 byte, alpha viền ngoài bằng 0; đã xem native.
- `git diff --check`: không lỗi whitespace.

Audit đồ họa toàn repo vẫn báo 9 naval sprite thiếu từ baseline và 182 warning
event picture ngoài submod. Nhánh này không thêm event hoặc sửa các consumer đó.
Không gọi toàn repository sạch chỉ vì exit code 0.

Ledger bao gồm reward mới và một lớp riêng gồm spirit root, territorial cũ và
variable militia. Không bao phủ mọi luật, technology, MIO, trait hoặc buff ngoài
nhánh. PASS số học không chứng minh ba route cân bằng trong chiến đấu thực tế.

## Chạy lại

Từ gốc repo, dùng Python thực có Pillow cho audit ảnh:

```text
python tools/audit/land_42_structure.py
python tools/audit/land_42_balance.py --md "<thư mục Millennium Dawn cài đặt>"
python tools/audit/audit.py
python tools/audit/live.py
python tools/audit_loc_errors.py
python tools/verify_all_loc.py
python tools/audit/ev.py
python tools/audit_dds_and_gfx.py
```

## Runtime còn phải nghiệm thu

Chưa chạy HOI4 hoặc kiểm error.log của nội dung mới. Cần playset MD rồi submod,
game mới VIE năm 2000, và kiểm:

- Đường nối/tên dài/icon/hover tại native size, nhất là D8 -> F2.
- Ngày mở từng chương trình và tiến độ của cả ba route.
- Treasury thiếu/vừa đủ, chương trình đang chạy qua save/load và capitulation.
- Nội chiến không bàn giao sớm, không double charge hoặc thưởng sang quốc gia khác.
- IFV designer/production thực tế có/không có NSB, IC giảm đúng 5% sau bàn giao.
- Historical/Hardline và historical-focus setting độc lập; AI thực sự chọn và
  hoàn tất route, giữ ngân sách và sản xuất force mix tương ứng.
- Không tăng lỗi của hải quân, procurement đã xóa, game rules hoặc các nhánh khác.
