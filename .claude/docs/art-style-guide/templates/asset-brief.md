# Brief tài nguyên

Sao chép nội dung sang hồ sơ của lô; thay toàn bộ placeholder trước khi tạo ảnh.

- ID gameplay / sprite / stem:
- Loại: focus / idea / decision / category / event / portrait / UI.
- Mục đích: sample hay tích hợp; phạm vi được người dùng yêu cầu.
- Nội dung/năm/nhánh; trạng thái lịch sử hoặc alt-history:
- Điều người chơi cần hiểu ngay:
- Chủ thể chính; hành động; 0–2 yếu tố phụ:
- Consumer đang dùng; file gameplay; sprite; đường dẫn texture; slot GUI nếu có:
- Canvas final / codec / alpha / mipmaps / số frame:
- Style family; palette; vật liệu; frame có sẵn trong GUI hay nằm trong ảnh:
- Board tham chiếu: nguồn, version/hash, điều học từ từng mẫu:
- Chi tiết phải đúng: cờ/logo/chữ/người/vũ khí:
- Chi tiết cần tránh:
- Master path / export path / preview path:
- Prompt; công cụ; các tham chiếu dùng thực tế:
- QA kỹ thuật; QA thẩm mỹ 1:1; kiểm trong game:
- Hạn chế/tài liệu chưa xác minh:

## Ví dụ rút gọn

ID: VIE_border_settlement / GFX_focus_VIE_border_settlement.
Loại: focus ngoại giao, tích hợp thay texture hiện có.
Ý nghĩa: hoàn tất phân giới đất liền; granite là chủ thể, không dùng combat/HUD.
Canvas: 93×91; RGB 32-bit DDS BGRA; alpha ngoài badge, border 1 px.
Tư liệu: concept tập 3 + mẫu raw đã chọn; ghi riêng nếu quốc huy là cách điệu.
Kiểm: sprite tồn tại, DDS round-trip, silhouette ở 1:1, chưa xác minh in-game.

