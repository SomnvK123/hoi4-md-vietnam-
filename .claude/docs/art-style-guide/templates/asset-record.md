# Hồ sơ nguồn và kiểm định một asset

Lưu cùng master của lô hoặc trong manifest lô; không sửa tên ảnh chỉ để biến
một asset chưa kiểm tra thành “approved”.

| Trường | Nội dung |
|---|---|
| asset_id / type / branch | |
| master / export / consumer_path | |
| sprite / gameplay_id | |
| final_size / codec / alpha / frame_count | |
| source_type | AI-generated / licensed-photo / official-vector / mixed |
| source_url / upstream_commit / source_sha256 | |
| rights_or_license | nguồn đã kiểm tra; không bịa giấy phép |
| generator / prompt / reference_images | |
| edit_history / rebuild_command | |
| checksum_export | |
| visual_review | người/công cụ, ngày, kết quả ở 1:1 |
| technical_checks | từng lệnh và kết quả, không chỉ exit=0 |
| integration_checks | mapping và path thật |
| in_game_check | passed / failed / unrun; version và lý do |
| known_limitations | |

## Chú ý

Ảnh render AI không tự động là ảnh tư liệu lịch sử. Ảnh portrait placeholder
không được ghi là đã xác nhận danh tính. Screenshot hiển thị trên nền checkerboard
không chứng minh kênh alpha tồn tại trong file.

Các đường dẫn consumer khác nhau có thể trỏ một texture; ghi alias trước khi thay.
Không overwrite sprite generic của MD chỉ để một idea VIE có icon mới.

