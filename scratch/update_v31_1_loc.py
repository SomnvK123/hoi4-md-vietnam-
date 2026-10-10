# Script to update localisation in VIE_md_vi_military_l_english.yml

loc_ideas = """
 ### National Spirits Hoc thuyet V31.1 (P / M / R)
 VPA_Defensive_Doctrine_1:0 "Học thuyết Phòng thủ Chiến lược Chủ động (Cơ bản)"
 VPA_Defensive_Doctrine_1_desc:0 "Xác lập ưu tiên bảo toàn lực lượng, chuẩn bị công sự trận địa vững chắc và sẵn sàng tiêu hao mũi tiến công của đối phương."
 VPA_Defensive_Doctrine_2:0 "Học thuyết Phòng thủ Chiến lược Hoàn chỉnh"
 VPA_Defensive_Doctrine_2_desc:0 "Đỉnh cao của nghệ thuật phòng thủ chiều sâu: kết hợp trận địa kiên cố, lực lượng dự bị cơ động và đòn phản kích sấm sét làm thất bại ý đồ của đối phương."

 VPA_Mechanized_Doctrine_1:0 "Học thuyết Phản công Cơ giới Hợp thành (Cơ bản)"
 VPA_Mechanized_Doctrine_1_desc:0 "Ưu tiên đầu tư cho các đơn vị thiết giáp và bộ binh cơ giới, tạo mũi nhọn đột phá hỏa lực mạnh mẽ."
 VPA_Mechanized_Doctrine_2:0 "Phản công Cơ giới Hợp thành Chiến dịch"
 VPA_Mechanized_Doctrine_2_desc:0 "Hoàn thiện nghệ thuật phản công chiến dịch bằng các binh đoàn cơ giới hợp thành, hiệp đồng tác chiến thần tốc và giành lại địa bàn quyết định."

 VPA_Mobile_Doctrine_1:0 "Học thuyết Tác chiến Cơ động Linh hoạt (Cơ bản)"
 VPA_Mobile_Doctrine_1_desc:0 "Ưu tiên tốc độ triển khai, ngụy trang phân tán và tính linh hoạt của lực lượng bộ binh trên mọi địa hình hiểm trở."
 VPA_Mobile_Doctrine_2:0 "Nghệ thuật Tác chiến Cơ động Địa hình Hoàn thiện"
 VPA_Mobile_Doctrine_2_desc:0 "Làm chủ nghệ thuật cơ động chuyển hóa thế trận, thích nghi tuyệt hảo với địa hình rừng núi sông ngòi, đánh bại đối phương bằng sự mưu lược và bất ngờ."

 VIE_synergy_defense_commando_idea:0 "Hiệp đồng Phòng ngự Chiều sâu - Đặc công"
 VIE_synergy_defense_commando_idea_desc:0 "Các phân đội đặc công luồn sâu nắm chắc ý đồ tiến công của địch, phục kích quấy rối hậu phương và phối hợp đắc lực cho tuyến phòng thủ."
 VIE_synergy_mech_commando_idea:0 "Hiệp đồng Đột kích Cơ giới - Đặc công"
 VIE_synergy_mech_commando_idea_desc:0 "Đặc công tiềm nhập mở cửa đánh chiếm các cứ điểm đầu cầu, tạo điều kiện cho thọc sâu cơ giới tiến công áp đảo."
 VIE_synergy_mobility_commando_idea:0 "Hiệp đồng Cơ động Linh hoạt - Đặc công"
 VIE_synergy_mobility_commando_idea_desc:0 "Sự kết hợp giữa bộ binh cơ động nhẹ và đặc công tinh nhuệ giúp làm chủ hoàn toàn các vùng địa hình hiểm trở và chia cắt đối phương."
"""

loc_focuses_p = """
 ### HOC THUYET P: PHONG THU CHIEN LUOC CHU DONG
 VIE_lf_p1_strategic_defense:0 "Học thuyết Phòng thủ Chiến lược Chủ động"
 VIE_lf_p1_strategic_defense_desc:0 "Xác lập tư duy lấy phòng thủ chiều sâu làm gốc, bảo toàn sinh lực trước ưu thế công nghệ và hỏa lực của đối phương, kiên trì chờ đợi thời cơ phản kích."
 VIE_lf_p2_multi_layered_defense:0 "Tổ chức Phòng ngự Nhiều tuyến"
 VIE_lf_p2_multi_layered_defense_desc:0 "Bố trí trận địa phòng thủ liên hoàn, nhiều tầng nấc có chiều sâu, bảo đảm lực lượng có thể linh hoạt chuyển đổi trận địa khi bị hỏa lực địch dồn ép."
 VIE_lf_p3_operational_reserves:0 "Xây dựng Lực lượng Dự bị Chiến dịch"
 VIE_lf_p3_operational_reserves_desc:0 "Chuẩn hóa các trung đoàn, sư đoàn dự bị chiến dịch cơ động, sẵn sàng tăng viện cho các hướng phòng thủ bị uy hiếp hoặc bịt lỗ thủng phòng tuyến."
 VIE_lf_p4_defensive_anti_breakthrough_firepower:0 "Tăng cường Hỏa lực Chống đột phá"
 VIE_lf_p4_defensive_anti_breakthrough_firepower_desc:0 "Tập trung hỏa lực pháo binh, tên lửa chống tăng và phòng không lục quân bảo đảm bẻ gãy các mũi nhọn đột phá thiết giáp của quân địch."
 VIE_lf_p5_protracted_combat_sustainment:0 "Duy trì Tác chiến Chiến tranh Kéo dài"
 VIE_lf_p5_protracted_combat_sustainment_desc:0 "Củng cố năng lực bảo đảm vật tư, phân tán kho tàng và duy trì chỉ huy tác chiến thông suốt khi phải đương đầu với áp lực tiến công dồn dập nhiều ngày."
 VIE_lf_p6_active_defense_counterattack:0 "Phòng thủ Vững chắc, Phản kích Đúng thời cơ"
 VIE_lf_p6_active_defense_counterattack_desc:0 "Đỉnh cao học thuyết phòng thủ chủ động: khi đối phương tiêu hao sức mạnh và sa lầy, lực lượng phòng ngự phối hợp với dự bị chiến dịch đồng loạt phản kích."
"""

loc_focuses_m = """
 ### HOC THUYET M: PHAN CONG CO GIOI HOP THANH
 VIE_lf_m1_combined_arms_mechanized:0 "Học thuyết Tác chiến Cơ giới Hợp thành"
 VIE_lf_m1_combined_arms_mechanized_desc:0 "Lựa chọn phát triển lực lượng cơ giới hỏa lực mạnh làm quả đấm thép của Lục quân, sẵn sàng đánh đòn tiêu diệt vào cụm quân đối phương."
 VIE_lf_m2_armor_combat_readiness:0 "Sẵn sàng Chiến đấu của Tăng Thiết giáp"
 VIE_lf_m2_armor_combat_readiness_desc:0 "Chuẩn hóa công tác bảo dưỡng, đại tu, huấn luyện kíp xe và cải thiện độ tin cậy vận hành của các trung đoàn, lữ đoàn tăng thiết giáp."
 VIE_lf_m3_mechanized_infantry_formations:0 "Hoàn thiện Đội hình Bộ binh Cơ giới"
 VIE_lf_m3_mechanized_infantry_formations_desc:0 "Trang bị đồng bộ xe chiến đấu bộ binh và xe bọc thép chở quân, bảo đảm bộ binh cơ giới cơ động cùng tốc độ và bảo vệ sườn cho xe tăng."
 VIE_lf_m4_mobile_fire_support:0 "Phát triển Hỏa lực Yểm trợ Cơ động"
 VIE_lf_m4_mobile_fire_support_desc:0 "Trang bị pháo tự hành và pháo phản lực bánh lốp cơ động cao, bám sát yểm trợ hỏa lực liên tục cho mũi tiến công cơ giới hiệp đồng."
 VIE_lf_m5_operational_combined_arms_units:0 "Đơn vị Hợp thành Cơ động Chiến dịch"
 VIE_lf_m5_operational_combined_arms_units_desc:0 "Tổ chức các lữ đoàn hợp thành độc lập với mạng lưới chỉ huy số và hậu cần cơ động thông suốt, đủ sức tác chiến thọc sâu trên nhiều hướng."
 VIE_lf_m6_operational_mechanized_counteroffensive:0 "Phản công Cơ giới Chiến dịch Quyết định"
 VIE_lf_m6_operational_mechanized_counteroffensive_desc:0 "Năng lực tập trung sức mạnh xe tăng và hỏa lực mở màn các chiến dịch phản công hiệp đồng quy mô lớn, đè bẹp phòng tuyến và giành lại thế trận."
"""

loc_focuses_r = """
 ### HOC THUYET R: TAC CHIEN CO DONG LINH HOAT
 VIE_lf_r1_flexible_mobile_warfare:0 "Học thuyết Tác chiến Cơ động Linh hoạt"
 VIE_lf_r1_flexible_mobile_warfare_desc:0 "Lựa chọn lối đánh cơ động phân tán, tận dụng triệt để địa hình và tính linh hoạt mưu lược để làm phá sản các kế hoạch tác chiến của địch."
 VIE_lf_r2_modernize_mobile_infantry:0 "Hiện đại hóa Bộ binh Cơ động"
 VIE_lf_r2_modernize_mobile_infantry_desc:0 "Nâng cao thể lực, trang bị cá nhân gọn nhẹ, thông tin liên lạc vệ tinh và khả năng tác chiến độc lập của các đơn vị bộ binh cơ động cao."
 VIE_lf_r3_terrain_adaptive_warfare:0 "Thích nghi Tác chiến Đa dạng Địa hình"
 VIE_lf_r3_terrain_adaptive_warfare_desc:0 "Huấn luyện bộ đội tác chiến điêu luyện trên địa hình rừng núi hiểm trở, đồng bằng chia cắt và sông nước, biến địa hình thành đồng minh chiến đấu."
 VIE_lf_r4_tactical_motorized_mobility:0 "Cơ động hóa Lực lượng Bằng Xe Chiến thuật"
 VIE_lf_r4_tactical_motorized_mobility_desc:0 "Trang bị xe cơ động đa dụng, xe bọc thép bánh lốp việt dã và phương tiện kỹ thuật chiến thuật phục vụ hành quân cơ động thần tốc."
 VIE_lf_r5_rapid_reaction_corps:0 "Lực lượng Phản ứng Nhanh Cấp chiến dịch"
 VIE_lf_r5_rapid_reaction_corps_desc:0 "Xây dựng các đơn vị ứng trực có khả năng chuyển trạng thái sẵn sàng chiến đấu tức thì, lập tức cơ động tới phong tỏa và đánh chặn các hướng nguy cấp."
 VIE_lf_r6_terrain_maneuver_mastery:0 "Tác chiến Cơ động Chuyển hóa Thế trận"
 VIE_lf_r6_terrain_maneuver_mastery_desc:0 "Đỉnh cao nghệ thuật vận động chiến: thoắt ẩn thoắt hiện, cơ động chia cắt đội hình địch, chuyển hóa từ thế phòng ngự sang thế bao vây tiêu diệt bất ngờ."
"""

loc_decisions = """
 ### Quyet dinh Chien luoc Hoc thuyet Luc quan V31.1
 VIE_decision_p_backup_defense_line:0 "Thiết lập Tuyến Phòng thủ Dự phòng"
 VIE_decision_p_backup_defense_line_desc:0 "Bố trí công sự dã chiến và tuyến chiến hào dự bị phía sau, tăng cường sức chống chịu và tốc độ đào công sự của các đơn vị trên hướng phòng thủ."
 VIE_decision_p_operational_reserves_boost:0 "Tăng cường Dự bị Chiến dịch"
 VIE_decision_p_operational_reserves_boost_desc:0 "Huy động nguồn lực cấp bách tăng cường vũ khí và quân số cho các trung đoàn dự bị, nâng cao tốc độ tiếp viện và khả năng phục hồi trận tuyến."
 VIE_decision_p_local_counterattack:0 "Tổ chức Phản kích Cục bộ"
 VIE_decision_p_local_counterattack_desc:0 "Tận dụng thời cơ quân địch mất đà tiến công trước tuyến phòng ngự kiên cố, tung lực lượng dự bị phản kích dũng mãnh để khôi phục trận địa."

 VIE_decision_m_mbt_modernization:0 "Chương trình Hiện đại hóa Xe tăng Chủ lực"
 VIE_decision_m_mbt_modernization_desc:0 "Đầu tư nâng cấp hệ thống ngắm bắn kỹ thuật số, giáp phản ứng nổ và tăng cường độ tin cậy động cơ cho lực lượng tăng thiết giáp chủ lực."
 VIE_decision_m_combined_arms_deployment:0 "Tổ chức Lực lượng Cơ giới Hợp thành"
 VIE_decision_m_combined_arms_deployment_desc:0 "Triển khai cơ cấu hiệp đồng chặt chẽ giữa xe tăng, xe chiến đấu bộ binh và pháo tự hành, nâng cao sức mạnh hỏa lực đột phá."
 VIE_decision_m_counteroffensive_surge:0 "Tập trung Sức mạnh Phản công Chiến dịch"
 VIE_decision_m_counteroffensive_surge_desc:0 "Dồn toàn bộ khí tài cơ giới và hỏa lực pháo binh mở mũi tiến công đột phá quyết định, bẻ gãy cánh quân đối phương."

 VIE_decision_r_terrain_mobility_training:0 "Huấn luyện Cơ động Thích nghi Địa hình"
 VIE_decision_r_terrain_mobility_training_desc:0 "Diễn tập chuyên sâu kỹ năng vượt sông suối, cơ động rừng núi và hành quân đêm, giảm hao mòn trang bị và nâng cao tốc độ cơ động."
 VIE_decision_r_rapid_readiness_force:0 "Thiết lập Lực lượng Ứng trực Cơ động Cao"
 VIE_decision_r_rapid_readiness_force_desc:0 "Duy trì trạng thái trực ban chiến đấu 100% cho các lữ đoàn phản ứng nhanh, nâng cao tinh thần và khả năng trinh sát phát hiện sớm."
 VIE_decision_r_maneuver_tempo_surge:0 "Tăng cường Nhịp độ Cơ động Chiến dịch"
 VIE_decision_r_maneuver_tempo_surge_desc:0 "Phát lệnh chuyển quân thần tốc trên toàn mặt trận, thay đổi hướng tác chiến bất ngờ khiến đối phương không kịp trở tay."

 ### Ideas tu Quyet dinh gameplay
 VIE_idea_p_backup_defense_line:0 "Tuyến Phòng thủ Dự phòng Đã Thiết lập"
 VIE_idea_p_backup_defense_line_desc:0 "Hệ thống công sự chiều sâu giúp bộ đội đào công sự nhanh hơn và giữ trận địa kiên cường."
 VIE_idea_p_operational_reserves:0 "Lực lượng Dự bị Sẵn sàng Tiếp viện"
 VIE_idea_p_operational_reserves_desc:0 "Tăng cường quân số và trang bị bảo đảm khả năng bổ sung lực lượng nhanh chóng vào vị trí chiến đấu."
 VIE_idea_p_local_counterattack:0 "Đợt Phản kích Cục bộ Đang Diễn ra"
 VIE_idea_p_local_counterattack_desc:0 "Lực lượng phòng ngự đang dồn hỏa lực đánh bật mũi tiến công của đối phương."
 VIE_idea_m_mbt_modernization:0 "Đội ngũ Xe tăng Nâng cấp Hiện đại"
 VIE_idea_m_mbt_modernization_desc:0 "Khí tài tăng thiết giáp được nâng cấp hỏa lực và giáp bảo vệ, tăng hiệu quả tác chiến."
 VIE_idea_m_combined_arms:0 "Đội hình Cơ giới Hiệp đồng Tác chiến"
 VIE_idea_m_combined_arms_desc:0 "Hiệp đồng chặt chẽ giữa bộ binh cơ giới, pháo binh và xe tăng nâng cao sức công phá."
 VIE_idea_m_counteroffensive_surge:0 "Cao trào Phản công Chiến dịch Cơ giới"
 VIE_idea_m_counteroffensive_surge_desc:0 "Mũi tiến công bọc thép đang thọc sâu với hỏa lực và sức đột phá tối đa."
 VIE_idea_r_terrain_mobility:0 "Lực lượng Cơ động Địa hình Tinh nhuệ"
 VIE_idea_r_terrain_mobility_desc:0 "Khả năng hành quân vượt địa hình giúp duy trì tốc độ và hạn chế hỏng hóc xe cộ."
 VIE_idea_r_rapid_readiness:0 "Lực lượng Ứng trực Phản ứng Nhanh"
 VIE_idea_r_rapid_readiness_desc:0 "Tinh thần cảnh giác và khả năng trinh sát giúp đơn vị triển khai chớp nhoáng khi có lệnh."
 VIE_idea_r_maneuver_tempo:0 "Nhịp độ Cơ động Thần tốc"
 VIE_idea_r_maneuver_tempo_desc:0 "Tốc độ hành quân và lập phương án tác chiến được đẩy lên mức cao nhất."

 ### Tech bonuses
 VIE_p4_artillery_bonus:0 "Nghiên cứu Hỏa lực Chống Đột phá"
 VIE_m4_sp_arty_bonus:0 "Nghiên cứu Pháo Tự hành Cơ động"
 VIE_r4_motorized_bonus:0 "Nghiên cứu Xe Cơ động Chiến thuật"
"""

fp = r'localisation\english\replace\VIE_md_vi_military_l_english.yml'
with open(fp, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace ideas section
import re
text = re.sub(r' VPA_Land_Doctrine_Mech_1:0[\s\S]*?VIE_synergy_mobility_commando_idea_desc:[^\n]+', loc_ideas.strip(), text)

# Replace focuses section
text = re.sub(r' VIE_lf_doctrine_combined_arms_mechanized:0[\s\S]*?VIE_lf_complex_terrain_mobile_capstone_desc:[^\n]+', (loc_focuses_p + loc_focuses_m + loc_focuses_r).strip(), text)

# Append decisions and tech bonuses at end
text = text.rstrip() + '\n' + loc_decisions.strip() + '\n'

with open(fp, 'w', encoding='utf-8-sig') as f:
    f.write(text)

print('Updated localisation file successfully with UTF-8 BOM!')
