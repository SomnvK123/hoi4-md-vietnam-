# Mỹ thuật MD Vietnam — tài liệu và skill

Bộ hướng dẫn dùng để tạo, sửa và tích hợp tài nguyên hình ảnh cho submod VIE
của Millennium Dawn. Quy tắc hiện hành được chỉnh sau khi đối chiếu phân tích
Modern Day, DDS upstream và tài nguyên thực tế ngày 08/10/2026.

Bắt đầu từ [skill md-art](../../skills/md-art/SKILL.md). Đọc
[hệ thống thống nhất](07_unified_art_system.md) và chọn skill theo ô giao diện.
Các yêu cầu và mẫu đã chọn của người dùng ưu tiên hơn mặc định tài liệu.

## Skill theo công việc

| Công việc | Skill |
|---|---|
| Điều phối/brief/board/lô/tích hợp | [md-art](../../skills/md-art/SKILL.md) |
| National focus | [md-focus-art](../../skills/md-focus-art/SKILL.md) |
| National spirit, idea, law | [md-idea-art](../../skills/md-idea-art/SKILL.md) |
| Decision, category | [md-decision-art](../../skills/md-decision-art/SKILL.md) |
| Event/news picture | [md-event-art](../../skills/md-event-art/SKILL.md) |
| Leader/commander/advisor portrait | [md-portrait-art](../../skills/md-portrait-art/SKILL.md) |
| BoP, MIO, trait, button, flag/UI khác | [md-ui-art](../../skills/md-ui-art/SKILL.md) |

Các file trong .claude/skills/ là skill của repository. Agent cần đọc SKILL.md;
việc có file trên đĩa không tự chứng minh công cụ tạo ảnh hoặc game đã sẵn sàng.

## Tài liệu tham chiếu

| Tập | Vai trò |
|---|---|
| [01: Phân tích phong cách](01_hoi4_md_art_style_analysis.md) | cách đọc reference; phân biệt stylization, vector, painterly và material |
| [02: Biểu trưng Việt Nam](02_vietnamese_propaganda_and_symbolic_art.md) | tư liệu concept/văn hóa; xác minh logo và lịch sử trước dùng |
| [03: Concept các nhánh](03_concept_thiet_ke_icon_cac_nhanh.md) | ý tưởng kể chuyện; code live quyết định ID/năm/tọa độ |
| [04: Sản xuất và kỹ thuật](04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md) | canvas/codec thực tế, prompt, export, mapping và QA |
| [05: Khung](05_nghien_cuu_va_thiet_ke_khung_focus.md) | frame theo nhánh/slot; cách tránh khung kép |
| [06: Đánh giá phân tích Modern Day](06_review_modern_day_analysis.md) | bảng đúng/sai/có điều kiện, nguồn upstream và số đo |
| [07: Hệ thống mỹ thuật thống nhất](07_unified_art_system.md) | palette, silhouette, độ phức tạp, nhận diện và quy trình lô |

Hồ sơ làm việc: [brief](templates/asset-brief.md) và
[nguồn/kiểm định](templates/asset-record.md).

## Những quyết định đã chốt và phạm vi của chúng

Hai mẫu ngoại giao đã được người dùng chọn và thêm vào mod:
assets/focus_icons/raw/asean_integration.png và border_settlement.png.
Giữ master, export PNG/DDS, sprite hiện có và recipe ở
assets/focus_icons/raw/README.md.

Mẫu khung nguyệt quế vàng/ba sao là mốc của nhóm ngoại giao VIE.
Không bắt buộc lên spirit/decision/event/portrait. HUD/cyan dùng cho đúng chủ đề;
không thay toàn bộ nhận diện VIE thành cyberpunk.

Các ngưỡng số màu, luminance, “AAA” và sáu layer từng nêu trong bản cũ không
phải yêu cầu engine hay tiêu chí pass chung. Bảng kỹ thuật tập 4 và consumer
thực tế thay thế các kích thước phỏng đoán cũ.

## Kiểm tra và báo cáo

Xem bản xuất ở kích thước 1:1, kiểm alpha/codec/path/sprite và kiểm game khi có.
tools/audit_dds_and_gfx.py kiểm DDS và một phần .gfx/focus/event; không bao phủ
tất cả TGA, idea, decision, character, GUI hoặc sprite states.
Không gọi asset “đã hoạt động trong game” chỉ từ generation hay exit=0.
