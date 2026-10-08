# Nhánh công nghiệp Việt Nam — v17 (08/10/2026)

35 focus cũ được giữ ID, thêm 4 focus chính sách thành 39. Đây là tài liệu hiện hành
cho nhánh công nghiệp, thay phần 2.4 và quy tắc giấu phụ thuộc nội bộ trong tài liệu
`VIE_economic_spine_horizontal_architecture.md` ngày 05/10/2026.

## Bố cục và quan hệ

- Vùng x=124..140 được giữ; độ sâu tăng từ y=1..7 lên y=1..9. Tất cả focus con thấp
  hơn từng prerequisite, khoảng cách giữa tâm focus cùng hàng ít nhất 2 đơn vị.
- Anchor là một prerequisite đã khai báo trước. Các nhánh ngoài công nghiệp giữ
  nguyên toàn bộ block gameplay và tọa độ tuyệt đối.
- Một khối prerequisite nhiều focus là OR; nhiều khối là AND. Cặp chính sách có
  `mutually_exclusive` hai chiều, đứng cạnh nhau. Không loại trừ các ngành/doanh nghiệp.
- Điều kiện nội bộ dùng đường nối. WTO, CPTPP, EVFTA, giáo dục đại học là điều kiện
  ngoài nhánh, có tooltip tham chiếu tên focus thực qua localisation `$key$`.

| Cụm | Quan hệ |
|---|---|
| Đóng tàu | Vinashin → xử lý khủng hoảng và SBIC → liên doanh → kết cấu điện gió |
| Dệt may | Xuất khẩu → xuất xứ CPTPP → dệt–nhuộm → sản xuất xanh |
| Thép | Formosa và Hòa Phát mở độc lập; Hòa Phát → Dung Quất 2 |
| Chuỗi cung ứng | Công nghiệp hỗ trợ mở từ gốc → cấp 1, cơ khí, ô tô và China+1 |
| Trung tâm chế tạo | Công nghiệp hỗ trợ AND (Samsung OR China+1) |
| Apple | Trung tâm chế tạo AND một trong hai lựa chọn FDI |
| Bán dẫn | Intel → tham vọng → một lựa chọn hỗ trợ → thiết kế / OSAT / đào tạo song song → fab thử nghiệm cần cả ba |
| Ô tô | Chương trình ô tô → cụm cung ứng → xe điện và pin → xuất khẩu |
| Chính sách | NQ23 → NQ29 → quỹ hỗ trợ / chương trình năng suất song song; khu công nghiệp sinh thái là nhánh riêng dưới NQ23 |

Xem [bảng 39 focus và thay đổi reward](.claude/docs/industry/industry_changes.md),
[manifest trước](.claude/docs/industry/industry_before.json) và
[manifest sau](.claude/docs/industry/industry_after.json).

## Lựa chọn, chi phí và sự kiện

| Focus mới | Thời gian | Reward / chi phí |
|---|---|---|
| `VIE_fdi_fast_track` | cost 5 | Một lần tăng trưởng; cờ mở cửa; Apple tiếp tục gọi sự kiện xuất xứ |
| `VIE_fdi_technology_screening` | cost 5 | +2 điểm nội địa hóa; -25 PP; không thưởng tăng trưởng trực tiếp |
| `VIE_chip_design_packaging_priority` | cost 5 | -1 tỷ; +2 điểm; một bonus microchip 50% |
| `VIE_chip_pilot_fab_priority` | cost 5 | -3 tỷ; +3 điểm; một bonus microchip 50% |

Nhà máy thử nghiệm thu thêm 2 tỷ chỉ trên đường ưu tiên thiết kế/đóng gói. Tổng hỗ
trợ trên cả hai đường là 3 tỷ. Cả hai vẫn cần thiết kế, OSAT và nhân lực. Helper xây
nhà máy của MD được gọi đúng một lần tại fab và tính giá công trình riêng.

Reward của 35 focus giữ nguyên, ngoại trừ bỏ caller `vie_ind.1` tại China+1 và thêm
khoản hỗ trợ bổ sung có điều kiện tại fab. Sự kiện `vie_ind.1` được giữ cho hàng đợi
save cũ; không có caller gameplay mới. Effect FDI dùng chung có guard hai kết quả,
không cấp thưởng hoặc đảo lựa chọn nếu event tới sau focus. Focus tương ứng bypass
khi lựa chọn đã được event xác nhận; phương án còn lại bị chặn.

SBIC đọc cờ `VIE_vinashin_crisis_processed`, được đặt khi chọn một option của
`vie_eco.5`, khi fallback được áp dụng, hoặc khi lịch sử được xử lý trong catch-up
của bookmark muộn. Cờ scheduler chỉ nói rằng event đã được lên lịch, không mở SBIC.

## Mốc lịch sử và năng lực

Các focus năng lực chung bỏ khóa năm: xuất khẩu dệt may, cơ khí chính xác, nhà cung
ứng cấp 1, cụm phụ trợ ô tô, dệt–nhuộm, dệt may xanh, tham vọng bán dẫn, đào tạo kỹ
sư và năng suất. Dệt may xanh vẫn cần EVFTA; đào tạo vẫn cần luật giáo dục đại học.
Xe điện–pin không còn phụ thuộc Quy hoạch điện VIII.

| Focus | Mở từ | Ý nghĩa |
|---|---|---|
| Formosa | 01/07/2008 | Giai đoạn đầu tư/xây dựng; không mô tả là bắt đầu sản xuất thương mại |
| Intel | 29/10/2010 | Nhà máy lắp ráp và kiểm thử khai trương |
| SBIC | 21/10/2013 | Đổi mô hình sau xử lý khủng hoảng |
| Hòa Phát HRC | 02/05/2020 | Mẻ HRC đầu tiên |
| NQ23 | 22/03/2018 | Ngày ban hành nghị quyết |
| NQ29 | 17/11/2022 | Ngày ban hành nghị quyết |
| Kết cấu điện gió | 19/05/2023 | Hợp đồng PTSC–Ørsted trong mô tả |
| OSAT | 11/10/2023 | Mốc khánh thành Amkor trong mô tả |
| Xuất khẩu / Nasdaq | 15/08/2023 | Mốc niêm yết VFS được nêu trong focus và event |

Nguồn chính: [Intel](https://www.intel.co.jp/content/dam/www/public/apac/xa/en/asset/world-economic-forum/pdf/Investing%20in%20asean%20region/article%204/VNAT%20Opening%20press%20release%20102910%20Final.pdf),
[Hòa Phát](https://www.hoaphat.com.vn/tin-tuc/hoa-phat-can-moc-san-luong-5-trieu-tan-hrc.html),
[PTSC](https://www.ptsc.com.vn/ptsc-va-rsted-ky-hop-dong-che-tao-va-cung-cap-chan-de-cho-du-an-dien-gio-ngoai-khoi-greater-changhua-2b-4).
[Amkor](https://amkor.com/blog/amkor-inaugurates-latest-factory-in-vietnam/) xác nhận
ngày khánh thành OSAT; [Nasdaq](https://www.nasdaq.com/videos/vinfast-auto-rings-the-nasdaq-stock-market-opening-bell)
xác nhận ngày niêm yết được mô tả trong focus xuất khẩu.
Ngày mở focus là mốc nội dung, không phải thời gian xây một nhà máy ngoài đời.

Điểm nội địa hóa là chỉ số năng lực gameplay, không phải một tỷ lệ thống kê quốc
gia. Loc HRC bỏ khẳng định tự chủ 100%; đào tạo là chương trình nhân lực; fab là
dây chuyền thử nghiệm ở công nghệ trưởng thành. Đã sửa BOM thiếu tại
`VIE_md_l_english.yml`, nơi định nghĩa title Samsung.

## Đích cuối và AI

`VIE_modern_industrial_nation_2030` giữ ID và reward, tên hiển thị là **Nền công
nghiệp hiện đại**. Chỉ có prerequisite chương trình năng suất; available yêu cầu
≥45 điểm và ≥3/6 nhóm sau, mỗi nhóm tính một lần:

1. Kết cấu điện gió ngoài khơi.
2. Dệt may xanh.
3. Dung Quất 2.
4. Trung tâm chế tạo **và** nhà cung ứng cấp 1.
5. Thiết kế chip **và** đóng gói OSAT.
6. Xe điện–pin.

`count_triggers` kiểm ba nhóm; sáu getter scripted localisation hiển thị trạng
thái từng nhóm trong tooltip. Không có khóa năm hoặc bắt buộc fab/xe điện cho người
chơi. Đường đóng tàu + dệt may + thép, thêm phụ trợ và cơ khí, đạt 48 điểm.

Historical plan ưu tiên FDI chọn lọc và thiết kế/đóng gói. Guard ngày chỉ nằm trong
`ai_will_do` cho tham vọng bán dẫn (2021), đào tạo (2024), fab (2026), năng suất
(11/2023), đích cuối (2030). Người chơi được phát triển năng lực sớm. Không thêm
persona AI hoặc thay đổi trọng số nghiên cứu/chính trị ngoài phạm vi này.

## Bàn giao và kiểm định

![Trước](.claude/docs/industry/industry_before.png)

![Sau](.claude/docs/industry/industry_after.png)

[Sơ đồ Diagram.net hai trang, XML không nén](.claude/docs/industry/industry_redesign.drawio).
Các hình là sơ đồ thiết kế từ tọa độ thật, không phải ảnh runtime HOI4. Đường XML
có đầu/cuối là focus, OR dùng dashed và mutex dùng một LINK. Không sinh skeleton
ghi đè file gameplay. Nguồn quy ước: [Focus Tree Tool](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/focus-tree-tool/),
[Design Principles](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/focus-tree-design-principles/).

Tái xuất: `python tools/focus_layout/industry_diagram.py` (cần Pillow).
Kiểm logic: `python tools/audit/industry.py`. Xem kết quả audit và checklist trong
[validation.md](.claude/docs/industry/validation.md).

Save mới là chuẩn nghiệm thu. Save cũ giữ ID nhưng không hoàn nguyên reward cũ;
phương án FDI chọn lọc đã chọn trước bản này không có cờ nên không thể tự nhận diện.
Save cũ đã xử lý Vinashin cũng có thể thiếu cờ mới. Bypass/event guard chỉ xử lý các
trạng thái có bằng chứng, không suy diễn cờ lịch sử từ cờ scheduler.
