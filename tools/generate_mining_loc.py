# -*- coding: utf-8 -*-
import os

content = """\ufeffl_english:

 ### Pillar 4 Root
 VIE_industrialization_strategy:0 "Công nghiệp hóa - Hiện đại hóa"
 VIE_industrialization_strategy_desc:0 "Đại hội Đảng lần thứ IX (4/2001) xác định đường lối đẩy mạnh công nghiệp hóa, hiện đại hóa, phấn đấu đến năm 2020 cơ bản trở thành một nước công nghiệp. Đây là gốc chung cho các chương trình công nghiệp nặng, công nghiệp chế tạo và công nghiệp hỗ trợ."

 ### Focuses - Vinacomin & Mining Branch
 VIE_vinacomin_founding:0 "Thành lập Tập đoàn Than - Khoáng sản Việt Nam (TKV)"
 VIE_vinacomin_founding_desc:0 "Quyết định 345/2005/QĐ-TTg ngày 26/12/2005 của Thủ tướng Chính phủ hợp nhất Tổng công ty Than Việt Nam và Tổng công ty Khoáng sản Việt Nam thành Tập đoàn Than - Khoáng sản Việt Nam (Vinacomin / TKV). Đây là tập đoàn kinh tế nhà nước giữ vai trò trụ cột trong việc thăm dò, khai thác và cung ứng than, khoáng sản thiết yếu phục vụ an ninh năng lượng quốc gia và nền kinh tế công nghiệp hóa."

 VIE_vinacomin_restructuring:0 "Tái cơ cấu Toàn diện Tập đoàn Vinacomin"
 VIE_vinacomin_restructuring_desc:0 "Quyết định số 2006/QĐ-TTg ngày 12/12/2017 phê duyệt Đề án tái cơ cấu TKV giai đoạn 2017–2020: thoái vốn triệt để khỏi các ngành nghề kinh doanh ngoài ngành (tài chính, ngân hàng, bảo hiểm, bất động sản), tinh gọn bộ máy quản trị, siết chặt kỷ luật phòng chống thất thoát tài nguyên và hiện đại hóa hệ thống quản trị rủi ro theo chuẩn mực quốc tế."

 VIE_green_mining_transition:0 "Chuyển dịch Xanh Ngành Khai thác Mỏ"
 VIE_green_mining_transition_desc:0 "Thực hiện cam kết Net Zero vào năm 2050 tại Hội nghị COP26, TKV đẩy mạnh lộ trình 'xanh hóa' các vùng mỏ: đóng cửa dần các moong khai thác than lộ thiên có nguy cơ sạt lở cao, hoàn nguyên môi trường, phủ xanh các bãi thải mỏ tại Quảng Ninh và chuyển đổi mô hình sang khai thác hầm lò sâu ít phát thải, bảo vệ hệ sinh thái cảnh quan vịnh Hạ Long và môi trường sống của nhân dân."

 VIE_closed_pit_mine_reclamation:0 "Hoàn nguyên & Tái sinh Đô thị Mỏ"
 VIE_closed_pit_mine_reclamation_desc:0 "Chủ trương cải tạo các đại moong than lộ thiên đã dừng khai thác (Cọc Sáu, Đèo Nai, Nam Mẫu) thành các hồ điều hòa sinh thái, công viên địa chất và khu đô thị du lịch xanh. Hoàn nguyên hàng ngàn hecta bãi thải mỏ, kiến tạo không gian sống trong lành, bền vững cho nhân dân vùng mỏ Quảng Ninh và bảo tồn cảnh quan Di sản thiên nhiên vịnh Hạ Long."

 VIE_bauxite_tay_nguyen:0 "Tổ hợp Khai thác Bauxite Tây Nguyên"
 VIE_bauxite_tay_nguyen_desc:0 "Triển khai hai dự án thí điểm bauxite – alumina tại Tân Rai (Lâm Đồng) và Nhân Cơ (Đắk Nông) theo định hướng Nghị quyết 10-NQ/TW của Bộ Chính trị. Dự án mở ra triển vọng xây dựng ngành công nghiệp luyện nhôm quy mô lớn, tạo động lực tăng trưởng kinh tế cho vùng đất đỏ Tây Nguyên nhưng đòi hỏi các giải pháp xử lý hồ bùn đỏ cực kỳ nghiêm ngặt nhằm tránh thảm họa môi trường."

 VIE_bauxite_suspend:0 "Đình chỉ Khai thác Bauxite Tây Nguyên"
 VIE_bauxite_suspend_desc:0 "Lắng nghe ý kiến phản biện tâm huyết của các nhà khoa học, trí thức, cựu lãnh đạo và đồng bào các dân tộc Tây Nguyên, Quốc hội và Chính phủ quyết định tạm đình chỉ các dự án khai thác bauxite quy mô lớn. Quyết định giúp củng cố sự đồng thuận xã hội, bảo vệ nguồn nước ngầm, rừng đầu nguồn và môi trường văn hóa - sinh thái thiêng liêng của vùng đất Tây Nguyên."

 VIE_tay_nguyen_eco_agriculture:0 "Nông nghiệp Sinh thái Tây Nguyên"
 VIE_tay_nguyen_eco_agriculture_desc:0 "Khi các dự án bauxite được tạm đình chỉ, toàn bộ nguồn tài nguyên đất đỏ bazan màu mỡ và rừng nguyên sinh Tây Nguyên được bảo tồn nguyên vẹn. Đẩy mạnh quy hoạch đại ngàn thành thủ phủ nông sản sinh thái chất lượng cao: cà phê đặc sản Robusta, hồ tiêu hữu cơ, mắc-ca và sầu riêng xuất khẩu toàn cầu, củng cố sinh kế lâu dài và văn hóa bản địa của đồng bào các dân tộc Tây Nguyên."

 VIE_rare_earths:0 "Thăm dò & Khai thác Mỏ Đất hiếm"
 VIE_rare_earths_desc:0 "Việt Nam sở hữu trữ lượng đất hiếm ước tính hơn 22 triệu tấn, đứng thứ hai thế giới chỉ sau Trung Quốc, phân bố chủ yếu tại Nậm Xe, Đông Pao (Lai Châu) và Yên Bái. Việc khởi động cấp phép thăm dò và thu hút đầu tư khai thác đất hiếm đặt Việt Nam vào tâm điểm của chuỗi cung ứng công nghệ toàn cầu và mở ra cơ hội hợp tác chiến lược với các cường quốc công nghiệp."

 VIE_rare_earth_processing:0 "Tổ hợp Tinh chế Đất hiếm & Luyện kim Công nghệ cao"
 VIE_rare_earth_processing_desc:0 "Chấm dứt hoàn toàn việc xuất khẩu thô quặng đất hiếm; đầu tư xây dựng các nhà máy chế biến sâu, phân tách các nguyên tố đất hiếm nặng và nhẹ (như Neodymium, Dysprosium, Praseodymium) đạt độ tinh khiết trên 99,9%. Nguồn nguyên liệu chiến lược này là linh hồn sản xuất nam châm vĩnh cửu, động cơ xe điện, tuabin gió và các linh kiện bán dẫn thế hệ mới."

 VIE_rare_earth_magnets:0 "Tổ hợp Nam châm Vĩnh cửu Đất hiếm"
 VIE_rare_earth_magnets_desc:0 "Hợp tác chiến lược với các tập đoàn Nhật Bản và Hàn Quốc xây dựng nhà máy sản xuất nam châm đất hiếm Neodymium (NdFeB) độ tinh khiết cao. Đây là linh kiện không thể thay thế cho động cơ xe điện thông minh, máy phát điện tuabin gió ngoài khơi, robot tự động hóa và các hệ thống vi điện tử quốc phòng thế hệ mới."

 VIE_than_quang_ninh:0 "Hiện đại hóa Vùng Than Quảng Ninh"
 VIE_than_quang_ninh_desc:0 "Vùng than Quảng Ninh chiếm trên 90% sản lượng than cả nước. Đẩy mạnh hiện đại hóa các mỏ Mạo Khê, Cọc Sáu, Vàng Danh, Hà Lầm; chuyển dịch cơ cấu từ khai thác lộ thiên sang khai thác hầm lò ở độ sâu -300m đến -500m bằng các giàn chống tự hành và máy khấu combi hiện đại, bảo đảm sản lượng trên 40 triệu tấn than sạch mỗi năm phục vụ đất nước."

 VIE_thach_khe_mine_start:0 "Tái khởi động Đại dự án Mỏ sắt Thạch Khê"
 VIE_thach_khe_mine_start_desc:0 "Mỏ sắt Thạch Khê (Hà Tĩnh) là mỏ sắt lớn nhất Đông Nam Á với trữ lượng trên 544 triệu tấn quặng hàm lượng sắt rất cao (trên 60%). Vượt qua những lo ngại về hang karst ngầm và thoát nước mỏ, dự án được tái khởi động với hệ thống tường hào chống thấm sâu và công nghệ khai thác tuần hoàn, bảo đảm tự chủ nguồn quặng sắt dồi dào cho ngành công nghiệp luyện thép Việt Nam."

 VIE_thach_khe_steel_cluster:0 "Cụm Luyện kim & Cán thép Thạch Khê"
 VIE_thach_khe_steel_cluster_desc:0 "§YGiả định:§! Gắn kết mỏ sắt Thạch Khê với cảng nước sâu Vũng Áng để hình thành cụm công nghiệp luyện gang thép liên hợp quy mô lớn. Tinh luyện quặng sắt hàm lượng cao nội địa phục vụ trực tiếp cho các nhà máy cán thép xây dựng, thép tấm đóng tàu và thép kỹ thuật cơ khí, giảm thiểu phụ thuộc vào phôi thép và quặng nhập khẩu."

 VIE_coal_to_electricity:0 "Trung tâm Nhiệt điện Than Cung ứng Điện lưới"
 VIE_coal_to_electricity_desc:0 "Gắn kết chuỗi giá trị từ mỏ than Quảng Ninh đến các trung tâm nhiệt điện than quy mô lớn như Mông Dương, Cẩm Phả, Quảng Ninh và Hải Phòng. Nguồn than cung cấp nhiên liệu chạy tải nền ổn định cho lưới điện quốc gia, bảo đảm an ninh năng lượng cho các khu công nghiệp trọng điểm miền Bắc trong các đợt cao điểm nắng nóng."

 VIE_ultra_supercritical_coal:0 "Nhiệt điện Than Siêu tới hạn USC"
 VIE_ultra_supercritical_coal_desc:0 "Chuyển giao và lắp đặt công nghệ nhiệt điện than siêu tới hạn (Ultra-Supercritical - USC) với nhiệt độ và áp suất hơi cực đại tại các tổ máy mới. Hiệu suất nhiệt nâng lên trên 45%, tiết kiệm hàng triệu tấn than mỗi năm, giảm 20% phát thải khí nhà kính và cắt giảm triệt để khói bụi qua hệ thống lọc bụi tĩnh điện và khử lưu huỳnh FGD hiện đại."

 VIE_nui_phao_tungsten:0 "Khai thác Vonfram Mỏ Núi Pháo"
 VIE_nui_phao_tungsten_desc:0 "Mỏ Núi Pháo (Đại Từ, Thái Nguyên) là mỏ vonfram đa kim lớn nhất thế giới ngoài Trung Quốc, được Masan High-Tech Materials phát triển và đưa vào khai thác thương mại. Nguồn vonfram, bismuth, fluorit và đồng từ Núi Pháo khẳng định vị thế của Việt Nam trong chuỗi cung ứng vật liệu công nghệ cao toàn cầu."

 VIE_mining_technology_upgrade:0 "Ứng dụng Công nghệ Khai thác Mỏ 4.0"
 VIE_mining_technology_upgrade_desc:0 "Ứng dụng tự động hóa, trí tuệ nhân tạo (AI) trong điều độ mỏ, băng tải thông minh vận chuyển than kín, hệ thống quan trắc địa kỹ thuật thời gian thực và dây chuyền nghiền lọc tuyển quặng hiện đại. Đổi mới công nghệ giúp giảm thiểu tối đa tai nạn lao động, hạ giá thành khai thác và nâng cao hiệu suất thu hồi khoáng sản."

 VIE_hc_starck_acquisition:0 "Thâu tóm Nền tảng Vonfram Toàn cầu"
 VIE_hc_starck_acquisition_desc:0 "Masan High-Tech Materials hoàn tất thương vụ lịch sử mua lại 100% nền tảng kinh doanh vonfram của Tập đoàn H.C. Starck (CHLB Đức). Việt Nam chính thức sở hữu các nhà máy chế biến sâu tại Đức, Canada, Trung Quốc, làm chủ công nghệ bột vonfram tinh thể và vật liệu pin xe điện thế hệ mới, khẳng định vị thế nhà cung ứng vật liệu công nghệ cao hàng đầu thế giới."

 ### Ideas - Mining & Minerals
 VIE_vinacomin_idea:0 "Tập đoàn Than - Khoáng sản Việt Nam (TKV)"
 VIE_vinacomin_idea_desc:0 "Tập đoàn TKV bảo đảm nguồn cung khoáng sản và năng lượng nền tảng cho sự nghiệp công nghiệp hóa, hiện đại hóa đất nước."

 VIE_coal_power_idea:0 "Nguồn Điện Than Tải nền"
 VIE_coal_power_idea_desc:0 "Các nhà máy nhiệt điện than bảo đảm nguồn cung cấp điện tải nền liên tục và ổn định cho nền sản xuất công nghiệp."

 VIE_rare_earth_processing_idea:0 "Chuỗi Cung ứng Đất hiếm Tinh chế"
 VIE_rare_earth_processing_idea_desc:0 "Năng lực tự chủ chế biến sâu đất hiếm thúc đẩy mạnh mẽ các ngành công nghệ cao, linh kiện điện tử và vi mạch bán dẫn."

 VIE_rare_earth_magnets_idea:0 "Chuỗi Cung ứng Nam châm Đất hiếm"
 VIE_rare_earth_magnets_idea_desc:0 "Làm chủ công nghệ chế tạo nam châm vĩnh cửu NdFeB bảo đảm năng lực tự chủ cho ngành sản xuất xe điện và thiết bị năng lượng tái tạo."

 VIE_usc_coal_power_idea:0 "Nhiệt điện Hiệu suất cao USC"
 VIE_usc_coal_power_idea_desc:0 "Công nghệ siêu tới hạn giúp tiết kiệm tiêu hao than trên mỗi kWh điện và giảm áp lực phát thải môi trường."

 VIE_mining_tech_idea:0 "Công nghệ Khai thác Hiện đại"
 VIE_mining_tech_idea_desc:0 "Hệ thống cơ giới hóa hầm lò và điều độ mỏ tự động giúp tăng năng suất và giảm chi phí sản xuất quặng."

 VIE_hc_starck_idea:0 "Tổ hợp Vật liệu Công nghệ cao H.C. Starck"
 VIE_hc_starck_idea_desc:0 "Mạng lưới chế biến sâu vonfram toàn cầu tại Đức và Bắc Mỹ nâng tầm giá trị xuất khẩu vật liệu kỹ thuật cao của Việt Nam."

 VIE_green_mining_idea:0 "Chiến lược Mỏ Xanh Bền vững"
 VIE_green_mining_idea_desc:0 "Chủ động hoàn nguyên môi trường, giảm phát thải bụi và nước thải mỏ, tạo sự hài hòa giữa phát triển công nghiệp mỏ và bảo vệ cảnh quan sinh thái."

 VIE_bauxite_environmental_idea:0 "Cam kết Bảo vệ Môi trường Tây Nguyên"
 VIE_bauxite_environmental_idea_desc:0 "Việc dừng các dự án bauxite giúp bảo vệ toàn vẹn nguồn nước ngầm, rừng nguyên sinh và môi trường sống của đồng bào các dân tộc Tây Nguyên."
"""

out_path = 'localisation/english/VIE_mining_l_english.yml'
with open(out_path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(content)
print(f"Generated {out_path} successfully.")

replace_path = 'localisation/english/replace/VIE_md_vi_eco_mining_l_english.yml'
with open(replace_path, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(content)
print(f"Generated {replace_path} successfully.")
