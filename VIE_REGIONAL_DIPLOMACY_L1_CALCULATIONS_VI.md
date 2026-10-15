# L1 — Gate cohesion gói sâu C/E đã chọn

Nguồn: registry B1 và các khóa cohesion_price_bands, cadre_cohesion_required, recovery, cohesion_limits, cohesion_initial, override_cohesion trong JSON chính trị.
Giá phí reader cũ chỉ là ứng viên đã bị rút khỏi kế hoạch áp dụng; bảng này giữ để kiểm lại kết luận.
Chênh toàn dải phí gửi: 38 − 27 = 11 PP.
Một lượt phục hồi: tiết kiệm tối đa 3 PP gửi hoặc 2 PP gửi lại; phí phục hồi lấy đúng JSON.
Không suy từ chênh toàn dải sang lợi ích của một lần phục hồi. Nếu gom nhiều lần gửi có thể thu hồi phí phục hồi; chưa có batch/caller/lịch để chứng minh hành vi đó.
Đã chọn (b): rút reader phí, giữ phí cơ sở B1 và thay bằng gate sâu C/E. Không áp gate này lên các cụm khác.
Gate thiết kế: cohesion hiện tại ≥ 55; đọc trực tiếp cadre_cohesion_required, không thêm tham số.
Kiểm ở soạn/gửi/gửi lại/bắt đầu và nâng gói; phản hồi chấp thuận vẫn được ghi, chờ phục hồi vẫn chịu hạn bắt đầu, sau start không hủy hay viết lại timer vì cohesion giảm.
Tooltip trước: cohesion hiện tại/ngưỡng, gói nhỏ còn mở, phí/lịch phục hồi. Sau: gói đã chốt và chi phí đã trả.
Phép thử bỏ gate: với cùng điều kiện khác, các trạng thái dưới ngưỡng chỉ chọn gói nhỏ/đợi phục hồi khi có gate, có thể gửi sâu ngay khi bỏ gate. Chưa chứng minh cân bằng hoặc đường hồi phục luôn kịp hạn.

| Band | Hệ số | Phí gửi/gửi lại cũ | Tiết kiệm tối đa sau một phục hồi gửi/gửi lại | Trạng thái đạt gate/tổng | Số lượt để đạt | PP phục hồi | Ngày phục hồi |
|---|---|---|---|---|---|---|---|
| 0–19 | 1.25 | 38/25 | 3/2 | 0/20 | 4–6 | 105–150 | 630–990 |
| 20–39 | 1.15 | 35/23 | 3/2 | 0/20 | 2–4 | 60–120 | 270–630 |
| 40–54 | 1.05 | 32/21 | 2/1 | 0/15 | 1–2 | 30–60 | 90–270 |
| 55–69 | 1 | 30/20 | 3/2 | 15/15 | 0–0 | 0–0 | 0–0 |
| 70–100 | 0.9 | 27/18 | 0/0 | 31/31 | 0–0 | 0–0 | 0–0 |

Giả định riêng của phép đạt gate: chọn phục hồi đầu tiên ngay, không có cooldown còn lại, không có thay đổi cohesion khác, đủ PP, chỉ dùng recovery purpose=cohesion.
Ngày đạt với n lượt = recovery.days + (n−1)×recovery.cooldown; n=0 thì không đợi. Không tính số PP quy đổi là thu PP thật.
Tất cả trạng thái nguyên trong cohesion_limits được xuất CSV; band chứa ngưỡng được tách theo giá trị thật, không giả tất cả cùng đạt.

## Sau một lần vượt phản đối

Đọc nguồn: 60 − 8 = 52; 52 < 55 nên gói sâu bị khóa trước start.
Phục hồi tối thiểu: 1 lượt, 30 PP, 90 ngày, cohesion lên 62 ≥ 55.
Không tính cohesion phục hồi thành PP thật; không đưa thêm phí ký/gửi vào khoản phục hồi. Cooldown còn lại hoặc biến động khác sẽ làm khác ngày đạt.
Phép thử bỏ gate đổi tập lựa chọn gói sâu tại trạng thái sau vượt; gate giữ nguyên thì phải phục hồi/chọn gói nhỏ/chờ, không có gate thì không bị chặn vì cohesion.
Đây là chứng cứ cho reader cohesion, không dùng để cho reader BoP hoặc tier hoãn PASS. Chưa chạy engine, chưa kiểm cân bằng.
