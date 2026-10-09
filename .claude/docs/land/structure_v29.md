# Cơ cấu lực lượng lục quân v29 — 09/10/2026

## Bố cục đã chốt

Mỗi hướng bắt đầu bằng một focus ưu tiên. Ngay sau đó, ba focus dự án nằm cùng một hàng ngang và đều yêu cầu focus ưu tiên đó. Một focus hoàn thiện ở hàng kế tiếp yêu cầu đủ cả ba dự án. Ba focus hoàn thiện của ba hướng mở `VIE_lf_command_reform_2` bằng một nhóm prerequisite OR, nên hoàn tất một hướng là đủ.

| Hướng | Ưu tiên (Y=8) | Ba dự án song song (Y=9) | Focus cuối (Y=10) |
|---|---|---|---|
| Cơ giới hóa | `VIE_lf_fs_main_corps` | `fs_lean_corps` · `mech_equipment` · `mech_sustainment` | `VIE_lf_mech_complete` |
| Cơ động nhẹ | `VIE_lf_fs_mobile_force` | `fs_mobile_corps` · `mobile_fire_support` · `mobile_sustainment` | `VIE_lf_dev_strategic` |
| Địa phương và dự bị | `VIE_lf_fs_depth_defence` | `fs_militia_units` · `territorial_reserve` · `territorial_coordination` | `VIE_lf_dev_territorial` |

Các focus dự án ở cùng hàng là anh em, không phải chuỗi mở khóa dọc. Từng dự án neo vào focus ưu tiên để dây đi xuống cùng hướng; focus cuối neo vào dự án giữa và có ba khối prerequisite riêng, thể hiện điều kiện AND. Cải cách chỉ huy II dùng một khối chứa ba focus cuối, thể hiện OR.

## Phần còn lại của cây

- Nền tảng và huấn luyện nằm ở Y=2–7. Gate ba trong bốn binh chủng và các mutex ưu tiên được giữ nguyên.
- Cải cách chỉ huy II ở (180,11), ba lĩnh vực năng lực ở Y=12–13, gate hai trong ba ở Y=14, Cải cách III ở Y=15 và focus hoàn thành ở Y=16.
- Nhánh có 38 focus. Mọi anchor là prerequisite trực tiếp đã khai báo trước. Tọa độ tuyệt đối, anchor, AND/OR, mutex và `available` của cả 38 focus được ghi trong `structure_v29.json` và đối chiếu với định nghĩa focus.
- Các hiệu ứng, gate huấn luyện, gate năng lực và tổng modifier/XP/mastery của ba hướng không đổi trong lần chỉnh layout này.

## Kiểm chứng

`python tools/audit/land_structure.py` kiểm tra bố cục, anchor, AND/OR, mutex, các gate, tổng reward và thứ tự hoàn thiện ba dự án. `python tools/focus_layout/land_diagram.py` xuất ảnh PNG trực tiếp từ focus hiện hành.

Audit tĩnh không thay cho kiểm tra hiển thị và tiến trình trong HOI4. In-game validation chưa chạy.
