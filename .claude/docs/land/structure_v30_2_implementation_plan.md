# Kế hoạch triển khai nhánh Lục quân V30.2

Nguồn nội dung: `VIE_Luc_Quan_Focus_V30_2_Noi_Dung.html` do người dùng cung cấp. HTML được dùng làm đề xuất về mục tiêu, các cụm focus và đồ thị mở khóa; các mô tả gameplay trong đó chưa phải reward đã triển khai. Sơ đồ SVG dùng tọa độ pixel, không thể chép thẳng thành `x/y` của Clausewitz.

## 1. Mục tiêu và phạm vi

- Chuyển cây hiện tại từ 38 lên **44 focus ID duy nhất**: 7 focus nền tảng/chỉ huy, 18 focus trong sáu chương trình năng lực chung, 15 focus thuộc ba hướng loại trừ nhau và 4 focus hoàn thiện.
- Chỉ ba focus chọn hướng M/R/D loại trừ nhau. Sáu chương trình năng lực mở độc lập từ Lục quân và vẫn có thể phát triển sau khi chọn hướng.
- Mỗi hướng có một đường hoàn thiện riêng; ba đích mở Cải cách chỉ huy II theo OR.
- Cải cách chỉ huy II mở Hiện đại hóa chọn lọc khi hoàn thành ít nhất 3 trong 6 chương trình năng lực.
- Giữ ID của 38 focus hiện có nếu ánh xạ ngữ nghĩa phù hợp. Không đổi reward chỉ để khớp hình; lập bảng reward trước/sau và cân lại tổng modifier trên các đường mới.

## 2. Sửa lỗi định danh trong HTML trước khi tạo focus

Mã dựng sơ đồ gọi 44 node, nhưng `byId` sẽ ghi đè node trùng ID. Hai cặp trùng là:

| ID bị dùng hai lần | Vị trí trong đề cương | Cách xử lý đề xuất |
|---|---|---|
| `VIE_lf_mech_equipment` | Chương trình B3 “Chương trình cơ giới hóa” và hướng M, “Thiết giáp hợp thành” | Giữ ID hiện có cho B3. Tạo ID mới riêng cho M3, với reward hiệp đồng thiết giáp khác reward nghiên cứu trang bị chung. |
| `VIE_lf_mobile_fire_support` | Hướng M, “Hỏa lực cơ động” và hướng R, “Hỏa lực chi viện cơ động” | Giữ ID hiện có ở R3. Tạo ID mới riêng cho M4, đặt tên và reward phản ánh hỏa lực của đội hình cơ giới. |

“Focus mới” ở A3 và C3 tạo hai ID mới. Hai bước cải tổ L4/L5 tạo thêm hai ID mới. Dùng `VIE_lf_cap_info_ops` đang tồn tại cho E3 “Số hóa thông tin chỉ huy” thay cho placeholder `Focus mới`, sau khi cập nhật localization và reward phù hợp. Như vậy 38 ID hiện có được giữ và có đúng sáu ID mới: L4, L5, A3, C3, M3 và M4. Đây là cách đạt 44 focus thật mà không bỏ focus cũ hoặc nhân đôi ID.

## 3. Đồ thị prerequisite đề xuất

### Nền tảng và sáu chương trình chung

| Focus | ID | Prerequisite |
|---|---|---|
| L1 Kiện toàn tổ chức Lục quân | `VIE_lf_army_reform` | `VIE_modernize_vpa`; giữ điều kiện ngày hiện có |
| L2 Chuẩn hóa hệ thống huấn luyện | `VIE_lf_basic_training` | L1 |
| L3 Cải cách hậu cần và kỹ thuật | `VIE_lf_logistics_merge` | L1 |
| L4 Cán bộ và hạ sĩ quan chuyên nghiệp | ID mới | L2 |
| L5 Tái cơ cấu đơn vị chiến đấu | ID mới | L3 |
| L6 Hiệp đồng binh chủng | `VIE_lf_combined_arms` | L4 **AND** L5 |
| L7 Chuẩn hóa chỉ huy chiến thuật | `VIE_lf_command_reform_1` | L6 |

Sáu chương trình đều bắt đầu từ L1, không bị khóa bởi hướng M/R/D. Các mắt xích trong mỗi nhóm là prerequisite trực tiếp theo thứ tự sau:

| Nhóm | Chuỗi focus | Focus hoàn tất nhóm để đếm 3/6 |
|---|---|---|
| A — Bộ binh | `arm_infantry_org` → `arm_infantry_train` → A3 UAV chiến thuật (ID mới) | A3 |
| B — Tăng thiết giáp | `arm_armor_org` → `arm_armor_train` → `mech_equipment` | `mech_equipment` |
| C — Pháo binh | `arm_arty_org` → `arm_arty_train` → C3 trinh sát/điều khiển hỏa lực (ID mới) | C3 |
| G — Công binh/bảo đảm | `arm_engineers` → `arm_engineer_train` → `mech_sustainment` | `mech_sustainment` |
| E — Phòng không/thông tin/điện tử | `cap_army_ad` → `cap_ad_coord` → `cap_info_ops` → `cap_cyber_ew` | `cap_cyber_ew` |
| F — Địa hình/khu vực | `cap_border_urban` → `cap_area_control` | `cap_area_control` |

HTML ghi E3 cần “L1 và công nghệ số hóa”, nhưng không nêu technology hoặc focus ID. Không tạo một điều kiện giả. Trước khi code phải xác minh công nghệ/điều kiện cụ thể; nếu đó là technology ngoài nhánh, dùng `available` có tooltip đúng tên và ID đã kiểm chứng. Nếu ý đó chỉ là nội dung của E3, bỏ gate ngoài và giữ prerequisite nội bộ rõ ràng.

L6 không còn đợi hoàn thành ba trong bốn binh chủng: nó cần hai cải cách L4/L5. Bốn nhánh tổ chức/huấn luyện cũ trở thành các mắt xích trong chương trình năng lực chung và không còn là lựa chọn bị giới hạn số slot.

### Ba hướng chiến lược và phần hoàn thiện

- M1/R1/D1 lần lượt giữ các ID `fs_main_corps`, `fs_mobile_force`, `fs_depth_defence`; cả ba cần L7 và loại trừ nhau từng cặp.
- M: M2 `fs_lean_corps` và M3 mới cùng cần M1; M4 mới cần M2; M5 `mech_complete` cần M3 **AND** M4.
- R: R2 `fs_mobile_corps` và R3 `mobile_fire_support` cùng cần R1; R4 `mobile_sustainment` cần R2; R5 `dev_strategic` cần R3 **AND** R4.
- D: D2 `fs_militia_units`, D3 `territorial_reserve`, D4 `territorial_coordination` cùng cần D1; D5 `dev_territorial` cần đủ D2 **AND** D3 **AND** D4.
- K1 `command_reform_2` cần M5 **OR** R5 **OR** D5.
- K2 `selective_modernization` cần K1; `available` yêu cầu hoàn tất ít nhất 3/6 focus kết thúc chương trình.
- K3 `command_reform_3` cần K2; K4 `force_complete` cần K3.

Các ID M3/M4 mới giải quyết va chạm trong HTML; không khai báo hai focus cùng một ID hoặc dùng một focus chung làm hai nút chiến lược khác nhau.

## 4. Rà soát reward/effect hiện có

Đã đối chiếu các focus live với `common/scripted_effects/VIE_md_effects_p17.txt`, `VIE_md_triggers_p17.txt`, `VIE_md_on_actions_startup.txt` và audit Trục 3. Một số helper mang tên cũ nhưng nội dung hiện tại có thiết bị, công trình, template và chi phí; không thể suy ra reward từ tiêu đề focus.

| Khu vực | Reward đang được gọi | Phát hiện và hướng xử lý |
|---|---|---|
| L1 | `VIE_lf_n1_reward` | PP/CP, XP hoặc mastery, treasury +1, military opinion, idea và modifier tổ chức/nhân sự. Nội dung HTML nói “chi phí chuyển đổi tạm thời” nhưng chưa định nghĩa khoản chi hay cơ chế hoàn lại; không tự thêm cost/revert. Chốt lại câu chữ hoặc reward. |
| L2/L3 | `VIE_lf_n3_reward` / `VIE_lf_n2_reward` | N3 có doctrine cost reduction, training-time/XP-gain/org; N2 có xe hậu cần, support equipment, fuel reserves, utility-vehicle research và supply/fuel modifiers. Hợp chức năng ở mức tổng quát nhưng cần giữ số liệu trong ledger mới. |
| Các focus bộ binh/tăng/pháo/công binh | `bb1/bb2`, `tg1/tg2`, `pb1/pb2`, `cb` | Có stockpile vũ khí/APC/tăng/pháo, tech bonus, MIO funds; một số reward tạo division template hoặc công trình. Chỉ giữ cấp quân/trang bị khi tiêu đề và mô tả nói rõ đưa đơn vị/khí tài vào trang bị; huấn luyện/tổ chức không mặc định cấp ngay sư đoàn hoặc kho đầy thiết bị. |
| B2/B3 | `VIE_lf_mech_equipment_reward` | B3 có bonus 25% một lần cho `CAT_main_battle_tanks`, XP/mastery và modifier. Giữ ở focus chương trình cơ giới hóa dùng chung; focus M3 mới cần reward khác để không thưởng trùng nghiên cứu. |
| G3 | `VIE_lf_mech_sustainment_reward` | XP/mastery, CP và supply consumption −5%; phù hợp hơn với bảo đảm kỹ thuật chung. Chuyển ID này ra khỏi đường M và đặt trong nhóm G. Tính lại tổng modifier của đường M sau khi chuyển. |
| A1/A2/C1/C2/G1/G2 | `bb*`, `pb*`, `cb` tương ứng | Rà riêng từng template, `create_unit`, stockpile và bonus công nghiệp. Các hiệu ứng vật chất hiện hữu không được nhân bản sang node mới A3/C3. |
| E/F hiện hành | `l1`, `l2`, `a1`, `a2`, `y1`, `y2` | Có bunker, AA/radar/network infrastructure, xe/UAV/AA stockpile, research bonus và dynamic modifier. Đặc biệt loc hiện tại của phòng không nói khí tài/công trình không thuộc nhánh, trong khi `a1_reward` cấp AA equipment và xây AA; phải sửa reward hoặc thu hẹp/mở rộng mô tả cho nhất quán. Các focus hỏa lực/địa bàn cũng cần quyết định rõ có thực sự cấp bunker/vật tư hay chỉ là tổ chức/huấn luyện. |
| K2 | `VIE_lf_mod_reward` | Có treasury −2 rồi gọi `one_state_arms_factory`. Theo quy ước MD của repo, helper `one_state_*` tự trừ phí; khoản trừ trực tiếp có nguy cơ tính tiền hai lần. Nếu giữ nhà máy thì bỏ khoản trừ thủ công; nếu khoản 2 tỷ là chi khác thì mô tả và tách riêng rõ ràng. |
| K4 | `VIE_lf_cap_reward` | Tương tự, treasury −3 rồi gọi `one_state_arms_factory`, cần xử lý nguy cơ thu phí hai lần. Reward còn có national idea, stability/war support, XP và modifier theo M/R/D; giữ các nhánh theo cờ chọn hướng nhưng cân lại sau khi mở sáu chương trình. |
| K3/K4 | `VIE_lf_cr3_reward`, `VIE_lf_cap_reward` | Đang cấp raw `army_experience`; các focus Lục quân mới cần theo helper `VIE_lf_xp_*` để đổi sang land mastery khi đã chọn Land Grand Doctrine và chỉ cấp Army XP khi chưa chọn. Kiểm tra mọi focus trong ledger theo quy tắc này. |

Reward mới nên dùng helper riêng có tên `VIE_lf_<id>_reward`, dòng focus chỉ gọi helper. Modifier phải dùng biến `VIE_af_*` đã tồn tại, tooltip đúng và `VIE_lf_refresh = yes`. XP dùng các helper doctrine-aware hiện có. Chưa chốt phần trăm/điểm số: trước hết tổng hợp ledger cho từng focus và tính toàn bộ stack khi hoàn tất cả sáu chương trình, mỗi hướng M/R/D và K2/K4. Không tái dùng một helper chỉ vì tên focus tương tự.

Kiểm tra riêng `VIE_lf_fav_discount`: nó giảm cost một số focus chuyên ngành khi người chơi đã chọn hướng. Sau khi các chương trình mở ngay từ L1, người chơi có thể hoàn tất focus được giảm cost trước khi chọn hướng; quyết định giữ cơ chế này, đổi sang thưởng không phụ thuộc thứ tự, hay bỏ phải được ghi trong ledger.

## 5. Gate, biến đếm và save cũ

- Xóa gate 3/4 cho tổ chức/huấn luyện binh chủng nếu đồ thị mới cho phép hoàn tất cả sáu chương trình; rà các lần gọi `VIE_lf_arm_slot_free`, `VIE_lf_arm_done_3`, `VIE_lf_arm_count`, `VIE_lf_arm_done` và phần khởi tạo trong startup.
- Thay gate 2/3 lĩnh vực hiện tại bằng 3/6 chương trình. Sáu terminal là A3, B3, C3, G3, E4, F2. Mỗi terminal chỉ được đếm một lần.
- Dùng biến/trigger mới có tooltip 3/6; không tái dùng `VIE_lf_cap_done` đang bị giới hạn 2. Cập nhật focus K2, loc positive/NOT, startup init và scenario audit đồng bộ.
- Cần quyết định tương thích save trước khi code gate: biến mới không tự biết focus cũ nào đã hoàn tất. Thiết kế migration/backfill dựa trên trạng thái focus đã hoàn tất, hoặc ghi rõ phạm vi yêu cầu bắt đầu save mới. Không cấp lại reward cho focus cũ đã hoàn tất.
- Giữ cờ `VIE_lf_regular/mobile/depth` vì decision và reward cuối đang đọc chúng. Giữ ID route terminal vì các decision hiện hành tham chiếu `dev_strategic` và `dev_territorial`.

## 6. Layout, localization và assets

1. Chốt ID và nội dung trong các bảng trên trước.
2. Lập bảng **tọa độ tuyệt đối** cho 44 node theo tầng/chức năng; bố trí sáu chương trình thành các cột độc lập hai bên cụm chỉ huy, ba lựa chọn chiến lược ở hàng ngang, capstone xuống dưới các cha. Ưu tiên các khoảng cách đủ bề rộng focus card, không lấy pixel SVG làm `x/y`.
3. Chọn `relative_position_id` từ prerequisite trực tiếp đã khai báo trước; sau đó mới quy đổi tọa độ tuyệt đối thành `x/y` tương đối. Kiểm mọi cha nằm trên con, trục giữa K1–K4, gap ngang, node treo và dây nối xuyên cụm.
4. Cập nhật title/description/tooltip cho sáu ID mới và các ID cũ đổi vai trò. Lưu ý `VIE_lf_basic_training_desc`, `combined_arms`, `selective_modernization`, `cap_army_ad`, `cap_info_ops` và các focus capability hiện ghi gate/reward cũ.
5. Kiểm sprite đã có cho từng ID. Có thể tái sử dụng icon hiện hữu nếu đúng nghĩa; nếu cần icon mới thì tạo/đăng ký DDS theo skill `md-focus`, không để tham chiếu `GFX_focus_*` thiếu.

## 7. Trình tự code và nghiệm thu

1. Chốt sáu ID mới, phân vai ID trùng, E3 gate và chính sách save cũ.
2. Viết bảng prerequisite/effect trước-sau; chốt từng reward vật chất, research bonus, template, chi phí và tổng modifier.
3. Sửa focus graph, cost, search filters, AI, prerequisites/mutex/available và tọa độ trong `VIE_md_focus.txt`; tăng version header.
4. Thêm/sửa scripted effects và triggers; sửa init biến; rà discount, decision callers và các reference chéo.
5. Cập nhật localization, tooltip, icon/GFX và manifest/sơ đồ cây.
6. Thêm tools/audit/land_structure_v30_2.py và manifest riêng, giữ audit V29 làm tài liệu lịch sử.
7. Chạy `python tools/audit/audit.py`, `python tools/audit/live.py`, `python tools/audit_loc_errors.py`, `python tools/verify_all_loc.py`, `python tools/audit_dds_and_gfx.py`, `python tools/audit/prov.py` nếu thay reward xây công trình, audit balance mới và render PNG từ code. Kiểm output thực dù lệnh trả 0.
8. Mở game để kiểm layout, tooltip, thứ tự mở khóa, chi phí Treasury, tech bonus và save migration. Audit tĩnh không thay kiểm tra engine.

## Quyết định đã chốt khi triển khai

1. Thêm sáu ID mới và giữ 38 ID cũ; hai cặp ID trùng trong HTML được tách thành focus riêng.
2. Bỏ gate công nghệ ngoài E3 vì HTML không cung cấp ID đã kiểm chứng; giữ prerequisite tuần tự trong cụm E.
3. Gỡ stockpile khỏi các focus tổ chức/huấn luyện chung và bỏ tạo sẵn division; giữ template chỉnh sửa ở các focus tổ chức theo hướng. Giữ trang bị/công trình khi mô tả focus gọi đúng năng lực đó. Các chương trình chung không phụ thuộc thứ tự chọn cơ cấu.
4. Save cũ được hỗ trợ bằng cách đếm trực tiếp focus terminal đã hoàn tất, không tạo counter mới hay phát lại reward.
## Tình trạng triển khai (2026-10-09)

Đã triển khai trong common/national_focus/VIE_md_focus.txt và các helper liên quan:

- Giữ 38 ID cũ, thêm sáu ID riêng: VIE_lf_cadre_professional, VIE_lf_force_reorganization, VIE_lf_arm_uav, VIE_lf_arty_fire_control, VIE_lf_mech_coordination, VIE_lf_mech_fire_support. Tổng số focus Lục quân là 44 ID duy nhất.
- Cải tổ I cần đồng thời hai cải cách nền L4/L5. Sáu chương trình năng lực mở từ L1 và vẫn mở sau khi chọn hướng. Gỡ các gate đếm 3/4 và 2/3.
- Ba hướng M/R/D nằm cùng hàng và loại trừ lẫn nhau. Mỗi capstone yêu cầu đúng các dự án theo sơ đồ; Cải tổ chỉ huy II mở bằng OR từ ba capstone.
- Hiện đại hóa chọn lọc yêu cầu Cải tổ chỉ huy II và ít nhất 3/6 terminal. Trigger đếm trạng thái focus đã hoàn tất trực tiếp, nên không cần backfill counter cho save cũ và không cấp lại reward.
- E3 không dùng gate công nghệ ngoài nhánh vì tài liệu HTML không chỉ rõ technology/focus ID.
- Các reward chung không còn đọc cờ hướng M/R/D tại thời điểm hoàn thành; người chơi có thể làm chương trình trước hoặc sau khi chọn cơ cấu mà không mất modifier. Reward có hướng riêng tiếp tục nằm ở CR2 và capstone cuối.
- Giữ số XP gốc ở các focus cuối nhưng chuyển qua helper doctrine-aware. Bỏ khoản treasury trừ thêm trước one_state_arms_factory, vốn đã thu phí theo helper MD.
- Đã xuất sơ đồ live tại .claude/docs/land/land_focus_v30_2.png và cập nhật .claude/docs/land/land_focus_current.png. Audit mới là tools/audit/land_structure_v30_2.py; manifest tọa độ/graph là .claude/docs/land/structure_v30_2.json.
- Layout chuẩn hóa theo kiến trúc phân tầng trên-dưới (X=172..188, Y=2..15):
  + Tầng trên (Y=2..6): Nền tảng chỉ huy & 4 Binh chủng truyền thống (Bộ binh, Thiết giáp, Pháo binh, Công binh), chạy thẳng đứng song song không cắt chéo.
  + Tầng giữa (Y=7..10): 3 Hướng chiến lược (M, R, D) độc lập, cân đối từng hàng Y, triệt tiêu khoảng hẫng tầng.
  + Tầng dưới (Y=11..15): Cải cách chỉ huy II mở ra 2 chương trình nâng cao (Phòng không/Cyber và Biên giới/Đô thị) cùng trục Hiện đại hóa chọn lọc & Capstone.
  + Hoàn toàn cách ly khỏi dải Kinh tế (X<=170), Công nghiệp Quốc phòng (X>=188 ở Y=3..5) và Hải quân (X>=196).

Kiểm tra tĩnh xác nhận graph, anchor trực tiếp khai báo trước, không có ô tọa độ tuyệt đối trùng trong toàn bộ focus tree, gate 3/6, OR/AND và helper reward. Cần kiểm tra trong game để xác nhận Clausewitz route dây, tooltip, chi phí Treasury và hiển thị card.
