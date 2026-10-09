# Thiết kế và tái cấu trúc nhánh focus VIE

Đọc khi thêm một cụm focus, làm lại bố cục/quan hệ hoặc review thiết kế. Đây là
các nguyên tắc tái sử dụng từ công nghiệp v17; số focus, tọa độ, năm và reward
của đợt đó không phải khuôn bắt buộc cho nhánh khác.

## 1. Quan hệ và điều kiện

- Hai khối prerequisite riêng là **AND**; nhiều focus trong một khối là **OR**.
  Kiểm từng khối, không gộp danh sách cha rồi coi tất cả là AND.
- Phụ thuộc nội bộ cụ thể phải hiện bằng prerequisite. Nếu B cần A nhưng đang
  cùng hàng, đưa B xuống dưới; không dùng available để giấu quan hệ hoặc làm phẳng cây.
- Ngành/doanh nghiệp cùng tồn tại có lối vào độc lập khi nội dung cho phép.
  Chỉ nối khi có lý do năng lực hoặc lịch sử thực sự.
- available giữ điều kiện ngoài nhánh, ngày, cờ kết quả và ngưỡng năng lực.
  Tooltip nêu đúng tên focus ngoài nhánh, có thể tham chiếu `$VIE_<id>$`.
- Ít nhất N nhóm là ngưỡng năng lực tổng hợp: dùng trigger đã xác minh và tooltip
  rõ tiêu chí/trạng thái. Không coi đó là một prerequisite cụ thể bị giấu.

Ví dụ trung tâm chế tạo cần phụ trợ AND (Samsung OR China+1):

```pdx
prerequisite = { focus = VIE_supporting_industries }
prerequisite = { focus = VIE_samsung_partnership focus = VIE_china_plus_one }
```

### Kiểm tra cửa ngõ năng lực và nhánh con

Trước khi sửa prerequisite, ghi rõ focus cung cấp năng lực gì và cần những năng lực nội bộ nào có trước. Biểu diễn các năng lực bắt buộc theo AND (mỗi điều kiện một khối `prerequisite` riêng); chỉ đặt các phương án trong cùng một khối khi chọn một trong số đó là đủ (OR). Giữ điều kiện bên ngoài như trạng thái sẵn sàng của chương trình trong `available`.

Tiếp theo, rà toàn bộ đường đi xuống các focus con/cháu, không chỉ focus đang sửa. Nếu thiết kế yêu cầu năng lực lõi trước, không để focus bảo đảm, tầm hoạt động, triển khai hoặc chuyên ngành vẫn mở được qua một đường prerequisite song song. Sau khi đổi quan hệ, tính lại tọa độ và anchor phía sau; xác nhận mỗi focus nằm dưới tất cả prerequisite cha trực tiếp.

#### Ví dụ: cửa ngõ năng lực tiêm kích đa năng

Trong thiết kế PK-KQ yêu cầu cả cải tổ chỉ huy lẫn biên chế lực lượng trước khi đưa tiêm kích đa năng vào biên chế, khai báo cửa ngõ như sau:

```pdx
focus = {
    id = VIE_airf_multirole
    prerequisite = { focus = VIE_airf_command_reform_2 }
    prerequisite = { focus = VIE_airf_medium_force }
}
```

Các focus phía sau cũng cần dùng năng lực máy bay làm cửa ngõ cho hoạt động tiêm kích:

- `VIE_airf_multirole_fleet`, `VIE_airf_sustainment` và `VIE_airf_operating_range` phụ thuộc vào `VIE_airf_multirole`.
- `VIE_airf_airlift_tanker` phụ thuộc vào `VIE_airf_operating_range`.
- `VIE_airf_multirole_wing` hội tụ bằng AND từ `VIE_airf_multirole_fleet`, `VIE_airf_sustainment` và `VIE_airf_operating_range`.
- Giữ cờ sẵn sàng công nghiệp/chương trình trong `available`; chúng không thay thế đường focus nội bộ.

Đây là ví dụ riêng cho thiết kế nhánh này, không phải quy tắc buộc mọi focus đều cần cải tổ chỉ huy hay biên chế lực lượng. Giữ đúng logic năng lực dự định của nhánh đang sửa.

## 2. Chính sách, reward và chi phí

- Dùng cặp mutex nhỏ cho chính sách thay thế nhau, khai báo hai chiều và đặt cạnh
  nhau cùng hàng. Nhóm ba phương án phải khai báo loại trừ từng cặp hai chiều.
  Không loại trừ các ngành/doanh nghiệp có thể cùng phát triển.
- Đánh đổi phải có ý nghĩa: tăng trưởng so với nội địa hóa, đầu tư trước so với
  bổ sung sau, lợi ích trước mắt so với rủi ro. Không chỉ thay một con số.
- Ưu tiên hỗ trợ không mặc định cấm năng lực dài hạn. Nếu hai đường cùng đạt một
  dự án, nêu rõ hội tụ, tiền đề và các khoản chi khác nhau.
- Giữ reward cũ khi chỉ tái bố trí, trừ thay đổi nội dung đã được yêu cầu/chốt.
  Bảng trước/sau phải giúp phát hiện mất reward hoặc thưởng lặp.
- cost là thời gian; PP, hỗ trợ ngân sách và giá công trình là các khoản khác nhau.
  Helper công trình MD đã thu tiền; hỗ trợ riêng phải có lý do và thu một lần,
  không lặp lại giá công trình.
- Với từng focus, viết trước một câu nêu năng lực hoặc quyết định mà nó cấp; sau đó
  chọn reward biểu đạt đúng điều đó. Các focus cùng hàng có thể cùng mở bằng AND
  nhưng vẫn cần kết quả riêng, không gán cùng một khoản XP cho đủ focus chỉ để
  làm hàng prerequisite. Nếu chủ đích chỉ là chuẩn bị, huấn luyện hoặc lập kế
  hoạch thì không thưởng ngay trang bị/công trình hoàn tất.
- Trước khi thêm modifier vĩnh viễn, xác minh biến trong dynamic modifier và
  effect đang dùng; tìm giới hạn/cap qua audit hiện hành. Cộng mọi focus có thể
  đi cùng nhau, kể cả các nhánh hội tụ, thay vì kiểm riêng từng reward.
- XP quân chủng: dùng helper doctrine-aware sẵn có trong nhánh nếu đã có. Mẫu
  PK-KQ đổi Air XP sang air mastery khi đã chọn Air Grand Doctrine; nếu chưa
  chọn thì cấp Air XP. Không giả định raw XP tương đương mastery hoặc cộng cả hai.
- Cập nhật completion reward, scripted effect, mô tả/tooltip và hợp đồng audit
  cân bằng cùng lúc. Scenario cần kiểm từng reward, trạng thái doctrine, gate và
  thứ tự hoàn thành song song. Nếu reward đổi sau khi focus đã hoàn tất trong save
  cũ, nêu rõ thay đổi không hồi tố trừ khi đã làm cơ chế bù riêng.

### Ca tham khảo: bốn focus chuẩn bị PK-KQ

Bốn focus sau Cải tổ I minh họa reward theo nhiệm vụ mà không tự cấp khí tài hay
công trình: diễn tập bắn đạn thật cho XP/mastery và command power; GCI/radar cải
thiện phát hiện; tổ chức trung đoàn giảm nhẹ hệ số chi phí nhân sự; căn cứ dự bị
tăng nhẹ phòng thủ trên lãnh thổ. Tổng XP/mastery được giữ bằng mức trước khi sửa.
Đây là ví dụ cân bằng của nhánh PK-KQ, không phải bộ số mặc định cho focus quân
sự khác. Xem effect và cap hiện hành trong `VIE_air_force_documentation.md` và
`tools/audit/air_force_balance.py`.

## 3. Thời điểm, cờ và save cũ

- Dự án/nghị quyết có tên khớp mốc mô tả: đầu tư, xây dựng, khánh thành hay vận
  hành là những thời điểm khác nhau. Kiểm nguồn trước khi đổi ngày.
- Chính sách năng lực chung có thể mở theo tiền đề/năng lực thay vì khóa năm.
  Khi đường thay thế đã chốt, ưu tiên ngày lịch sử cho AI trong ai_will_do;
  không dùng guard AI để khóa người chơi.
- Đào tạo là chương trình, không lập tức có đủ nhân lực; pilot không thành tự chủ
  toàn ngành. Chỉ số gameplay không gắn nhãn tỷ lệ thống kê thực nếu không đo tỷ lệ đó.
- Cờ scheduler chỉ xác nhận lên lịch. Gate sau khủng hoảng đọc cờ kết quả, được
  set ở các option, fallback và catch-up/bookmark liên quan.
- Chuyển lựa chọn từ event sang focus dùng chung effect có guard kết quả.
  Event đã queue không được cấp thưởng lần nữa hoặc đảo phương án đã chọn.
- Chỉ bypass lựa chọn cũ khi có bằng chứng trạng thái, chặn phía đối lập.
  Không suy diễn kết quả từ cờ lịch hoặc tự đặt cờ chỉ để mở gate.
- Giữ ID được tham chiếu khi làm lại. Báo giới hạn nhận diện save cũ; save mới
  là chuẩn kiểm khi thay quan hệ/reward.

## 4. Bố cục và đích cuối

- Anchor là một prerequisite thật, khai báo trước con. Con thấp hơn **tất cả**
  cha; điểm hội tụ ở dưới hàng lựa chọn/tiền đề.
- **Tính tọa độ tuyệt đối trước khi chỉnh layout.** Trong focus HOI4, `x` và `y`
  là độ lệch so với `relative_position_id`, không phải tọa độ toàn cây. Dùng parser/
  sơ đồ để cộng dồn anchor và đánh giá vị trí tuyệt đối; không suy trục từ các số
  `x` cục bộ.
- **Giữ trục giữa xuyên suốt thân cây.** Chọn một trục chuẩn ở tầng gốc, rồi kiểm
  các focus chỉ huy và capstone tối cao nằm trên cùng trục nếu quan hệ thiết kế
  yêu cầu. Sau mỗi lần đổi anchor, tính lại toàn bộ node con và kiểm drift X tích
  lũy; không để mỗi tầng lệch thêm một bước.
- **Căn cột theo cha.** Các focus con cùng chuyên ngành phải tạo thành một cột dễ
  đọc; ở hàng có nhiều nhánh con, tâm nhóm con nên trùng hoặc cân quanh tâm cha.
  Capstone chuyên ngành nằm cùng một hàng và dưới đúng trục của từng chuyên ngành.
  Focus phụ trợ như tanker, kho vận hoặc bảo đảm không chen vào hàng capstone;
  đặt nó ở tầng riêng dưới focus chức năng mà nó cần.
- Giữ gap cùng hàng ít nhất 2 đơn vị; ưu tiên 4 khi có chỗ và bề rộng icon cần
  khoảng thở. Xem cả bề rộng hộp focus, không chỉ ô tọa độ. Không áp luật “x phải
  chẵn” cho toàn cây; điều quan trọng là vị trí tuyệt đối và khoảng cách thực tế.
- Xếp các nhánh song song và cặp chính sách cạnh nhau khi có thể. Rà mọi đường
  prerequisite dài, đặc biệt đường từ root/chỉ huy tới capstone. Nếu một hội tụ đã
  buộc đủ các capstone mà mỗi capstone đều phụ thuộc vào root đó, bỏ cạnh root
  trùng lặp để tránh đường nối rơi xuyên nhiều tầng; chỉ làm khi chứng minh logic
  mở khóa không đổi.
- Không để focus thành node treo về mặt đồ họa. Với điều kiện nội bộ liên nhánh,
  chọn vị trí giúp prerequisite nối vào nhánh đích mà không cắt qua node khác.
  Nếu cần chuyển gate sang `available` để tránh dây cắt, giữ tooltip nêu tên điều
  kiện và chủ động bố trí node gate trong cụm có liên hệ thị giác; không đổi logic
  mở khóa chỉ để làm đẹp dây.
- Trước khi chốt, xuất sơ đồ từ **tọa độ tuyệt đối của file thật**, kiểm hàng/cột,
  node chồng lấn, các nhánh có cân quanh cha không, capstone có thẳng hàng không,
  đường dài có cắt node không, và node có flow nhìn thấy được không. Xem sơ đồ ở
  cỡ hiển thị người dùng; kiểm số liệu giao cắt không thay thế việc xem hình hoặc
  kiểm tra trong game.
- Khi lực lượng và công nghiệp có vòng tiến triển khác nhau, cho mỗi hệ thống
  một cụm và vùng riêng, với khoảng trống rõ ràng. Các cụm có thể cùng mở từ
  root quân chủng theo thiết kế đã chốt; không mặc định tách root độc lập dưới
  gốc quân sự. Focus lực lượng không xen
  vào cột công nghiệp. Gate liên nhánh có thể ở available với tooltip tên focus
  và bậc; quan hệ nội bộ của từng nhánh vẫn phải hiện bằng prerequisite.
- Chia tầng theo ý nghĩa tiến triển: nền tảng → lựa chọn → chỉ huy/bảo đảm
  → năng lực chuyên ngành → hội tụ. Dùng điểm gom và khoảng nghỉ giữa tầng;
  chỉ tách cột nhưng để nút chung rải giữa các chuỗi chưa đủ rõ kiến trúc.
  Tham khảo cấu trúc từ cây MD thực có (ví dụ Đức), không sao chép reward,
  loại trừ chuyên ngành hoặc buộc mọi nhánh theo số tầng cố định của ví dụ.
- Cơ cấu tác chiến, ưu tiên ngân sách và chuyên ngành là ba ý nghĩa khác nhau.
  Tên và vị trí lựa chọn phải giúp người chơi nhận ra ý nghĩa đó. Nếu chuyển
  định hướng từ decision lên cây, giữ chi phí/thời lượng chương trình đã chốt,
  bỏ bề mặt lựa chọn trùng và chặn event đang chờ đảo phương án hoặc thưởng lặp.
- Đặt củng cố nền tảng trước định hướng khi đó là trình tự nội dung. Không mặc
  định mỗi ý nghĩa cần một hàng mutex: ngân sách theo chương trình có thể ở
  option/decision, tránh bắt chọn hai lần trước khi đủ năng lực.
- Hai chức năng bổ sung có thể mở ngang từ nền tảng chung và hội tụ bằng AND.
  Khi bỏ phụ thuộc cũ, cập nhật tên/mô tả cùng quan hệ; giữ ngưỡng bậc và kết quả
  chương trình thực. Chỉ đổi tọa độ không biến một chuỗi năng lực thành song song.
- Capstone công nhận nhiều hướng thành công phù hợp nội dung; tránh ép một ngành
  công nghệ cụ thể khi các ngành khác cũng đáp ứng mục tiêu.
- Với N/M nhóm, mỗi nhóm là một tiêu chí; nhóm nhiều focus cần đủ thành phần.
  Dùng count_triggers đã xác minh, tooltip ngưỡng và trạng thái từng nhóm.
  Thiết kế N/M, ngưỡng điểm và reward theo nhánh; không sao chép cố định 3/6 và 45.

## 5. Sơ đồ và kiểm định

- Diagram.net dùng XML không nén: rectangle là focus, mọi connection FROM/TO
  focus, dashed là OR, một LINK cho mỗi cặp mutex. AND vẫn là cạnh bắt buộc.
  Công cụ sinh skeleton không được ghi đè reward hiện có.
- Bàn giao sơ đồ trước/sau, bảng quan hệ/reward và nguồn mốc lịch sử khi đổi lớn.
  Hình render từ code không chứng minh routing của engine HOI4.
- Chạy lệnh thật trong [.claude/docs/validation.md](../../../../.claude/docs/validation.md);
  đọc cảnh báo dù exit code 0, đối chiếu baseline và provider MD/base game.
- Kiểm đường đạt/không đạt, hai phía OR/mutex, nhóm thiếu thành phần, ngưỡng ngay
  dưới/bằng mức yêu cầu, chi phí từng đường, event đang chờ và save cũ.
- Báo riêng kiểm file/logic tĩnh, tích hợp và runtime. Chỉ xác nhận runtime sau
  khi mở cây VIE, kiểm khóa/đường nối, hover và error.log; AI cần quan sát hành vi.
  Không dùng nochecks/ignoreprerequisites làm bằng chứng gate đúng.

Ví dụ: [thiết kế công nghiệp](../../../../VIE_industry_branch_redesign.md) và
[kiểm định](../../../../.claude/docs/industry/validation.md). Các script industry
chuyên cho fixture đó; nhánh khác phải kiểm theo đồ thị và tiêu chí riêng.

Ví dụ root chung, củng cố trước một hàng cơ cấu và chuyên ngành mở ngang: [PK-KQ v19](../../../../VIE_air_force_documentation.md).
Số focus và tọa độ của ví dụ này không phải chuẩn chung cho các nhánh khác.

Nguồn: [Focus Tree Tool](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/focus-tree-tool/)
và [Design Principles](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/focus-tree-design-principles/).
Tài liệu tool giải thích ký hiệu/xuất skeleton, không yêu cầu mọi nhánh có mutex.



## Convert a tiered sketch into a focus tree

Before editing, make a table in **absolute coordinates**. If diagram Y1 sits below an external national focus, document the difference between displayed Y and absolute file Y. PDX `x/y` are offsets from `relative_position_id`, not tree coordinates.

| Row | Focus IDs / role | Gate | Anchor | Absolute coordinates |
|---|---|---|---|---|
| Y1 | `VIE_airf_training_standardization` shared root | root | `VIE_modernize_vpa` | (220,2) |
| Y2 | `VIE_airf_sam_force`; `VIE_airf_fighter_force` | each needs root | root | (218,3); (222,3) |
| Y3 | `VIE_airf_command_reform_1` | fighter AND SAM | fighter | (220,4) |
| Y4 | `VIE_airf_tactical_exercises`; `VIE_airf_gci_radar_training`; `VIE_airf_regiment_formation`; `VIE_airf_reserve_bases` | all need command reform I | command reform I | (214,5); (218,5); (222,5); (226,5) |
| Y5 | `VIE_airf_first_force` | AND all four Y4 focuses | tactical exercises | (220,6) |
| Y6 | `VIE_airf_structure_territorial`; `_balanced`; `_long_range` | each needs Y5; pairwise mutex | Y5 | (212,7); (220,7); (228,7) |
| Y7 | `VIE_airf_command_reform_2`; `VIE_airf_medium_force` | selected structure | balanced; long range | (218,8); (222,8) |
| Y8 | `VIE_airf_iads`; `VIE_airf_multirole`; `VIE_airf_unmanned` | IADS/UAV need C2; fighter needs C2 AND medium force | C2 | (214,9); (220,9); (226,9) |
| Y9 | `layered_defence`, `ew_antistealth`; `multirole_fleet`, `operating_range`, `sustainment`; `isr_uav`, `datalink`, `strike_uav` (`VIE_airf_` prefix) | each needs its specialty root | own root | X=212/216; 218/220/222; 224/226/228, Y=10 |
| Y10 support | `VIE_airf_airlift_tanker` | operating range | operating range | (220,11) |
| Y11 | `VIE_airf_iads_command`; `VIE_airf_multirole_wing`; `VIE_airf_teaming` | AND within each column; Teaming also needs Datalink and multirole availability gate | same column | (214,12); (220,12); (226,12) |
| Y12 | `VIE_airf_integrated_force` | keep 2/3 capstone gate in `available`; do not require all three | multirole wing | (220,13) |

The Y9 child row has eight focus cards. To keep minimum gap 2, this implementation expands the abstract sketch span to X=212..228 (center 220); the sketch tick range is illustrative and cannot fit eight focus cards at that spacing.

Workflow: verify IDs/icons/localisation; assign absolute coordinates then derive offsets; ensure anchors are direct prerequisites declared earlier; distinguish AND/OR/mutex; check overlap, gap >=2, column/capstone alignment, support rows, long/crossing connectors, and orphan nodes; update scenario coverage and render from the actual focus file. A static diagram does not confirm HOI4 runtime rendering. This mapping describes PK-KQ v24 under external parent `VIE_modernize_vpa`, not a universal coordinate standard.
