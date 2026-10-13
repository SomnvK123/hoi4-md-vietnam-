"""Rebuild the paper model from B1. No HOI4 engine or game files are used."""

import argparse
import csv
import hashlib
import itertools
import json
import math
import re
from datetime import date
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARAMS = ROOT / "VIETNAM_POLITICAL_PARAMETERS_VI.json"
DOC = ROOT / "VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md"
CSV = ROOT / "VIETNAM_POLITICAL_BALANCE_VI.csv"
REPORT = ROOT / "VIETNAM_POLITICAL_REVIEW_L1_VI.md"


def table(headers, rows):
    return "\n".join(["| " + " | ".join(headers) + " |",
                       "| " + " | ".join(["---"] * len(headers)) + " |"] +
                      ["| " + " | ".join(map(str, row)) + " |" for row in rows])


def capture_b1():
    data = json.loads(PARAMS.read_text(encoding="utf-8"))
    nodes = {}
    for line in DOC.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\| ((?:F|IX|X|XI|XII|XIII|XIV)\d\d)(?: `[^`]+`)? \| ([^|]+) \| (\d+) \| (.*)", line)
        if match:
            node, name, cost, rest = match.groups()
            nodes[node] = {"cost": int(cost), "name": name.strip(), "source_row": rest.strip()}
    assert len(nodes) == 74, f"Input node count: {len(nodes)}"
    data["parameters"]["focus_nodes"] = {"value": nodes, "refs": "6.2;7.4; toàn bộ cost và giá đã ghi trong các node; giá chưa ghi được đánh dấu ở báo cáo B1"}
    data["baseline_sha256"] = hashlib.sha256(DOC.read_bytes()).hexdigest()
    data["baseline_sections"] = {m.group(1): hashlib.sha256(m.group(0).encode()).hexdigest()
                                  for m in re.finditer(r"^## (\d+)\..*?(?=^## |\Z)", DOC.read_text(encoding="utf-8"), re.M | re.S)}
    PARAMS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def changelog(p):
    return table(["Mục", "Cũ", "Mới", "Lý do", "Cập nhật theo"], [
        ["L1.1", "Mốc sớm chung 660", str(p["early_days"]), "Chuẩn trượt, cấp tốc đạt", "Kết luận;4.2;6.5;7.3;8.3;10;11;12;CSV"],
        ["L1.2", "Thưởng 60 PP", f"{p['early_pp']} PP; dự án phụ {p['side_project']['days']} ngày/{p['side_project']['pp']} PP", "Chênh gói trả đủ chỉ 5 PP", "4.2;8.1;8.3;10;11;12;CSV"],
        ["L1.3", "Vượt không có cổng;40–69 hệ số1", "Sau trừ >=40;40–54 hệ số1.05", "Giá/cổng tác động trước khi cohesion tụt thấp", "3.2;3.3;10;11.3;CSV"],
        ["L1.4", "Thẩm định lại thiếu quy tắc tuần tự", "Nếu A trượt: max(T,690)+180; B đến810; C partial hợp đồng", "Hậu quả E102-C được tính chung", "6.4;6.5;8.3;10;11;CSV"],
        ["L1.5", "Ký tier1/2:35/30", f"Tier1/2:{p['sign_days'][1]}/{p['sign_days'][2]}; XIII09:25;XIV11:21", "Ba cửa sổ có giá trị ở ba tier", "4.4;5.2;6.6;hai hàng7.4;10;11.3"],
        ["L1.6", "Drift có nhưng thiếu cảnh báo", "+0.30→+0.20 khi trả đủ; khóa cấp tốc lần tới", "Giữ mode đã ký, báo trước", "3.1;10;11;CSV"],
        ["L1.7", "min(+900,chuẩn bị kỳ sau)", "+900 cố định; nhỏ nhất còn380 ngày", "Lịch độc lập có dự phòng", "4.2;11;CSV"],
        ["L1.8", "15 hàng; chỉ kiểm tra, event khác giữa tuyến", "Ma trận1296 hàng,648 hợp lệ; cùng E102×E103 ở mọi tuyến", "Tách snapshot, chi từng khoản, k và r", "11.1;CSV;script;B1"],
        ["Theo dõi phạm vi", "Không có nguồn B1", "JSON + bảng B1 + hash mục không đổi", "Giữ nguồn duy nhất và kiểm scope", "Báo cáo lượt1"],
        ["Quyết định checkpoint", "15PP, ngân khố0 mỗi checkpoint", f"15PP + {p['checkpoint_treasury']:.2f} ngân khố; gói55PP + {p['checkpoint_count']*p['checkpoint_treasury']:.2f}", "Người dùng chốt; I3 đổi lựa chọn rẻ nhất theo k", "B1;3.2;4.2–4.3;6;10;11.1;11.3;12;CSV"],
        ["Quyết định I2", "Chỉ báo chênh5PP", "PP thuần5; quy đổi15/25/35 ở k20/40/60", "Giữ định nghĩa PP thuần đã chốt", "4.2;10;11.1;11.3;Báo cáo"],
        ["Quyết định I5", "Ngoại lệ840/825 chưa cho phép", "C+B/C:full840/825/735, dự phòng60/75/165; không thưởng sớm", "Chỉ ngoại lệ do lựa chọn có bảng; không đổi deadline/giá", "B1;4.2;6.4–6.5;10;11.1;11.3;12;CSV"],
    ])


def sync_confirmed(p, rows, exception_table, late_table, checkpoint_rows, package_differences):
    text=DOC.read_text(encoding="utf-8")

    def paragraph(prefix,new):
        nonlocal text
        pattern=rf"^{re.escape(prefix)}.*$"
        assert len(re.findall(pattern,text,re.M))==1, f"Missing/duplicate paragraph: {prefix}"
        text=re.sub(pattern,lambda _:new,text,count=1,flags=re.M)

    if "**Giá checkpoint đã chốt:**" not in text:
        paragraph("Giá gói:", f"Giá gói: **{p['fast_upfront_pp']} PP** khi bắt đầu, cộng hai checkpoint. **Giá checkpoint đã chốt:** mỗi lần thương lượng trả **{p['checkpoint_pp']} PP và {p['checkpoint_treasury']:.2f} ngân khố**; hoặc vượt phản đối với cohesion -{p['override_cohesion']} và BoP +0.05. Thương lượng thành công đẩy BoP -0.05. Vượt chỉ khả dụng nếu cohesion sau trừ ≥{p['override_floor']}. Từ60, hai lần vượt còn44, lần thứ ba44−8=36 bị khóa. Hai lần thương lượng vẫn đưa+0.30→+0.20, khóa cấp tốc lần tới nhưng giữ timer đã ký.")
        paragraph("Giá thanh toán đủ hai checkpoint:",f"Giá thanh toán đủ hai checkpoint: **55 PP và {p['checkpoint_count']*p['checkpoint_treasury']:.2f} ngân khố**. Giá vượt cả hai: **25 PP, ngân khố0 và cohesion -16**. Giá event riêng giữ nguyên. Gói hỗn hợp thu đúng giá mỗi checkpoint: thương lượng có PP/ngân khố, vượt có cohesion/BoP; không thu phí thương lượng cho checkpoint đã vượt.")
        paragraph("Giá 55/25 PP", "Gói trả đủ55PP +0.50ngân khố hoặc vượt đủ25PP/ngân khố0 mua cùng gói chương trình; không thu lại trên từng hành động. Có đúng hai checkpoint định danh. k=20/40/60 chỉ là tham số kiểm tra, không phải tỷ giá thật của game. Biên giá checkpoint và ngân sách đầy đủ ở11.1.")
        paragraph("Gói trả đủ 55 PP", "I2 kiểm **PP thuần**: gói55PP so với thưởng50PP chênh5PP, PASS. Gói trả đủ còn chi0.50ngân khố; chênh quy đổi ở k20/40/60 lần lượt15/25/35PP. Đây là sensitivity, không phải giá engine; không dùng chênh quy đổi để đổi định nghĩa I2. Giá trị còn lại của cấp tốc đến từ dự án phụ L1.2; cửa sổ hợp đồng được theo dõi riêng.")
        paragraph("**Bất biến lịch:**", "**Bất biến lịch:** bắt đầu muộn nhất+900 phải cách chuẩn bị đại hội sau ít nhất100ngày; khoảng nhỏ nhất380ngày theo mục5.1. I5: đường chuẩn/cấp tốc mặc định phải còn≥100ngày dự phòng; ngoại lệ do người chơi chọn E102-C+E103-B/C được miễn nếu có trong bảng6.5. Deadline900 và mọi giá khác giữ nguyên. Ngoài snapshot cohesion60, kiểm tra chuẩn ở cohesion<20 mất thêm60ngày thành810, dự phòng90: điểm này chưa được miễn hoặc sửa.")
        paragraph("Cấp tốc thêm 55 PP", "Cấp tốc thêm55PP và0.50ngân khố nếu thương lượng cả hai checkpoint, hoặc25PP/ngân khố0/cohesion-16 nếu vượt cả hai. Giá bảng là tier cán bộ0, cohesion60; công cụ cơ sở giữ nguyên. CSV cộng phí ngân khố checkpoint một lần cho gói trả đủ, kể cả kiêm nhiệm; event và kiêm nhiệm kê riêng.")
        paragraph("E102-C cộng 90 ngày", "E102-C cộng90ngày vào chuỗi chứng cứ, kiến nghị công khai vẫn phải xử lý để đủ mục tiêu. Tooltip trước lựa chọn E102-C hiển thị kết quả dự kiến từng E103: nếu B/C, full840/825/735 và dự phòng60/75/165 theo mode; nếu A, hiển thị thẩm định lại và partial dự kiến. Khi mode chưa chốt, hiển thị các mode khả dụng; sau khi chốt lấy timer đã ký. Các phương án không tự cho cohesion dương. B rẻ hơn A nhưng bỏ cơ hội kỹ thuật; C hỗ trợ ngắn hạn nhưng làm trễ chứng cứ. Tất cả giá E102 giữ nguyên.")
        paragraph("**Điểm chưa đạt I5:**", "**Ngoại lệ full đã chốt:** chỉ người chơi chọn E102-C kết hợp E103-B hoặc C. Bảng riêng bên dưới ghi mọi mode/tuyến hợp lệ, ngày full, dự phòng900−full và thưởng sớm0; chúng không là đường mặc định. Các lựa chọn không đổi deadline900 hoặc có cơ chế bù. Tooltip E102-C/E103-B/C trước khi chọn ghi: “Dự phòng còn X ngày; chậm thêm sẽ rơi xuống partial.” X lấy từ timer hiện hành; câu này nghĩa là chậm thêm vượt hết X, đúng ngày900 vẫn xét full nếu đủ4/4. I3/I10 còn vướng: trong E102-C, C rẻ hơn B15PP ở mọi k/r và cùng ngày/cohesion/cơ hội đã mô hình hóa; B chỉ khác trạng thái hợp đồng được chấp nhận. Báo lệch này, giữ nguyên giá/hậu quả, chưa bổ sung thưởng cho B.")
        paragraph("UI hiển thị mốc sớm riêng", "UI hiển thị mốc600/690, deadline900, ký45/30/25/21 và giá sau tier/cohesion. Giá mỗi checkpoint thương lượng15PP+0.25ngân khố, gói trả đủ55PP+0.50; vượt8cohesion/cổng sau trừ≥40. Báo trước BoP+0.30→+0.20: giữ timer hiện tại, khóa cấp tốc lần tới. E103-A hiển thị max(T,690)+180. E102-C/E103-B/C hiển thị ngày full, dự phòng X, kết quả partial nếu chậm vượt X; đối chiếu bảng ngoại lệ6.5, không có thưởng sớm cho ngoại lệ. Ký IX/XIII09/XIV11 có cửa sổ30/25/21ngày. Dự án phụ:30PP/270ngày, deadline chuẩn bị kỳ sau, guard một lần. k là tham số kiểm tra, không hiển thị như tỷ giá thật của game.")
        paragraph("AI chọn cấp tốc khi", "AI chọn cấp tốc khi ngày dư mở dự án phụ hoặc có nhu cầu/cơ hội có hạn; so cả55PP+0.50ngân khố với phương án chuẩn, không lấy thưởng50PP làm lợi nhuận chắc chắn. AI kiểm cổng cohesion sau trừ và kho bạc đủ trả0.25 ở mỗi checkpoint; không miễn phí phí thiếu. Giữ timer đã ký khi BoP giảm. Với E102-C+E103-B/C, AI đọc dự phòng còn60/75/165, không tính thưởng sớm hay dự án phụ; không chọn A nếu hồ sơ chắc trễ690. B cần giá trị chấp nhận hợp đồng được chốt, chưa gán trọng số thưởng mới để che lệch với C.")
        paragraph("Thu nhập r=", "Thu nhập r=[0.5,1,1.5], bonus nhánh0.03PP/ngày, cửa sổ1800ngày. k=[20,40,60] **chỉ là tham số kiểm tra**, không phải tỷ giá thật của game. Thu PP=(r+bonus)×cửa sổ; chưa mô hình stock/cap/luật/chiến tranh. Chi quy đổi=PP ròng+ngân khố ròng×k+(cohesion đầu−cuối)×3; cohesion nhận là khoản âm, không thành thu PP thật. CSV có `treasury_checkpoints`:0.50 khi trả cả hai,0 khi vượt hoặc chuẩn; đã cộng vào ngân khố ròng. Side project là lựa chọn riêng, chưa cộng vào tổng programme.")
        paragraph("Chiến tranh, counter reset", "Chiến tranh, counter reset, kiến nghị chưa đóng, công cụ mở muộn và chỉ tiêu kinh tế chưa đạt nằm ngoài lịch cơ sở. CSV không chứng minh full chắc chắn trong game. Checkpoint I3 đã đổi lựa chọn rẻ nhất theo k; ngoại lệ full I5 đã được chốt trong snapshot. E103-C còn trội B trong cặp ngoại lệ; vùng cohesion<20 còn thiếu dự phòng trên đường kiểm tra chuẩn. Các điểm này được báo, không chỉnh thêm số.")
        paragraph("- Chuẩn→cấp tốc", "- Chuẩn→cấp tốc đổi mốc600/690; I2 kiểm PP thuần55−50=5. Gói trả đủ còn0.50ngân khố; chênh quy đổi15/25/35 ở k20/40/60 chỉ là tham số kiểm tra. Giá trị còn lại: dự án phụ270ngày/30PP. Kiểm checkpoint:20/25/30 so với vượt24, biên k40 chỉ1PP; không tự nới biên.")
        paragraph("- Chương trình chuẩn/cấp tốc", "- I5: chuẩn/cấp tốc mặc định full trước900−100=800; deadline+900 cách chuẩn bị kỳ sau≥100. Ngoại lệ full chỉ E102-C+E103-B/C có bảng riêng, ngày/dự phòng và thưởng sớm0. Tooltip báo partial nếu chậm vượt dự phòng; kiểm đúng ngày900 và901. Cohesion<20/kiểm tra chuẩn810 còn cần chốt riêng, chưa được miễn.")
        paragraph("Đã hoàn thành chỉnh tài liệu lượt 1", "Đã cập nhật lượt1 theo hai quyết định người dùng và tính CSV từ B1: checkpoint15PP+0.25ngân khố, gói55PP+0.50, thưởng50; ngoại lệ full E102-C+E103-B/C có bảng riêng, không thưởng sớm. I2 PASS theo PP thuần; checkpoint I3 PASS với biên k40 chỉ1PP; I3 còn FAIL trong cặp E103-B/C. I5 đạt trong snapshot, chưa đạt ở cohesion<20/kiểm tra chuẩn810. I10 không có tổ hợp thống trị toàn bộ hoặc từng tuyến ở mọi k/r đã kiểm, nhưng C trội B trong cặp ngoại lệ. Lượt2/3 và engine/playtest chưa chạy.")
    examples=[]
    for row in rows:
        if row["eligible"] and row["program"]=="inspection" and row["e102"]=="A" and row["e103"]=="B" and row["k"]==p["k_values"][1] and row["r"]==p["r_values"][1]:
            examples.append([row["route"],row["mode"],row["pp_net_cost"],row["treasury_net_cost"],row["potential_full_day"],row["pp_early_reward"],row["cohesion_final"],row["bop_final"],row["converted_cost"],row["side_project_available"]])
    pattern=r"\| Tuyến \| Mode \| Chi PP ròng \|.*?(?=\n\n)"
    replacement=table(['Tuyến','Mode','Chi PP ròng','Chi ngân khố ròng','Ngày full','Thưởng PP sớm','Cohesion cuối','BoP cuối','Chi quy đổi','Dự án phụ mở'],examples)
    assert len(re.findall(pattern,text,re.S))==1
    text=re.sub(pattern,lambda _:replacement,text,count=1,flags=re.S)
    start="**Bảng ngoại lệ full và ngân sách đã tính lại.**"
    end="\n### 6.6."
    extra="\n\n"+start+"\n\nCác bảng dùng snapshot cohesion 60, tier cán bộ 0 và timer đã ký. Toàn bộ tổ hợp mode/tuyến hợp lệ của snapshot được liệt kê; k/r không thay timer. Khi cohesion hoặc trì hoãn khác làm đổi timer, tooltip phải tính lại X, không lấy một số cố định từ bảng.\n\n"+table(["Tuyến","Mode","E102","E103","Ngày full","Dự phòng còn","Thưởng PP sớm","Kết quả"],exception_table)
    extra+="\n\n**Mọi tổ hợp full sau mốc sớm:** đường chuẩn A/B+B/C vẫn là mặc định đủ dự phòng; C+B/C là ngoại lệ được chốt. k/r không đổi ngày nên không lặp hàng theo k/r.\n\n"+table(["Tuyến","Mode","E102","E103","Ngày full","Dự phòng còn","Thưởng PP sớm","Phân loại"],late_table)
    extra+="\n\n**I2 theo PP thuần, chênh quy đổi báo riêng:**\n\n"+table(["k thử","Giá gói PP","Thưởng PP","Chênh PP thuần","Ngân khố gói","Chênh quy đổi"],package_differences)
    extra+="\n\n**I3 checkpoint — biên mỏng k=40:**\n\n"+table(["k thử","Thương lượng quy đổi","Vượt quy đổi","Thương lượng − vượt"],checkpoint_rows)+"\n\n"
    if start in text:
        begin=text.index(start)
        finish=text.index(end,begin)
        text=text[:begin]+extra.lstrip()+text[finish:]
    else:
        text=text.replace(end,extra+end,1)
    assert text.rstrip().endswith("BLUF")
    DOC.write_text(text,encoding="utf-8")


def apply_l1(data, p, make_table, core, gaps, rows, combos):
    original = DOC.read_text(encoding="utf-8")
    if hashlib.sha256(DOC.read_bytes()).hexdigest() != data["baseline_sha256"]:
        raise ValueError("--apply-l1 chỉ áp dụng một lần vào đúng bản đã capture B1; không ghi đè sửa tay.")
    text = original

    def replace(old, new):
        nonlocal text
        assert text.count(old) == 1, f"Expected unique passage: {old[:90]}"
        text = text.replace(old, new)

    def section(heading, following, body):
        nonlocal text
        start = text.index(heading)
        end = text.index(following, start)
        text = text[:start] + heading + "\n\n" + body.rstrip() + "\n\n" + text[end:]

    replace("deadline 900 ngày và mốc thưởng sớm 660 ngày", f"deadline {p['program_deadline']} ngày và mốc thưởng sớm riêng: cán bộ/công vụ/dân vận {p['early_days']['cadre']}, kiểm tra {p['early_days']['inspection']} ngày")
    replace("Các giá trị là thông số thiết kế, đã kiểm tra số học bằng bảng ngân sách.", "Các giá trị là thông số thiết kế từ [bảng tham số B1](VIETNAM_POLITICAL_PARAMETERS_VI.json), đã tính bằng [script ngân sách](VIETNAM_POLITICAL_BALANCE_VI.py). Báo cáo [lượt 1](VIETNAM_POLITICAL_REVIEW_L1_VI.md) ghi các bất biến còn FAIL.")
    replace("Đây là hợp đồng thực thi của nhiệm vụ hiện hành, không phải bản sao BoP.",
            "Đây là hợp đồng thực thi của nhiệm vụ hiện hành, không phải bản sao BoP. Trả đủ hai checkpoint đưa BoP +0.30 xuống +0.20: chương trình hiện tại giữ timer cấp tốc, lần khởi động tiếp theo bị khóa cấp tốc vì BoP không còn trên +0.25. Đây là chủ đích quản lý thanh; tooltip báo trước cả hai thời điểm.")
    replace("Thống nhất trách nhiệm thành công đẩy BoP -0.05.", "Thống nhất trách nhiệm thành công đẩy BoP -0.05. Vượt phản đối chỉ khả dụng khi cohesion sau khi trừ còn ít nhất 40; trigger và tooltip dùng cùng phép kiểm tra. Từ cohesion 60, vượt hai checkpoint còn 44; lần thứ ba bị khóa vì 44−8=36. Đây là giới hạn trước thưởng kết quả hoặc phục hồi.")
    replace("| 40–69 | 1.00 | Giá chuẩn |", "| 55–69 | 1.00 | Giá chuẩn; đủ ngưỡng nhân sự/kiểm chứng cán bộ |\n| 40–54 | 1.05 | Giá khởi động cao hơn; kiêm nhiệm và kiểm chứng cán bộ chưa đủ ngưỡng |")
    replace("Full chương trình: cohesion +6; partial +2; fail -6.", "Muốn vượt đủ hai checkpoint của gói kế tiếp từ 44 cần ít nhất 56; hai lượt phục hồi đưa lên 64, tổng 60 PP, hoàn tất sau 270 ngày nếu chọn ngay và dùng cooldown chung. Một lượt 30 PP đưa lên 54 chỉ đủ một checkpoint. Chương trình cán bộ cấp tốc vượt cần hai lượt phục hồi trước chuỗi kiểm chứng 90 ngày; lịch và chi phí có trong CSV/báo cáo lượt 1.\n\nFull chương trình: cohesion +6; partial +2; fail -6.")
    body = f"""- Chọn trọng tâm trong {p['program_selection_days']} ngày sau bước kiện toàn.
- Khởi động trong {p['program_start_latest']} ngày sau đại hội. Các công cụ cơ sở mở qua F02 hoặc phương án mặc định của đại hội; focus sau đó mở cách làm chuyên sâu.
- Deadline cuối = ngày bắt đầu +{p['program_deadline']} ngày; lịch đại hội vẫn độc lập.
- Mốc thưởng sớm tính từ ngày bắt đầu: cán bộ/công vụ/dân vận {p['early_days']['cadre']} ngày; kiểm tra {p['early_days']['inspection']} ngày. Các mốc bao gồm chuẩn bị, triển khai và kiểm chứng cuối.
- Full: đủ 4/4, tăng một tier và cohesion +{p['outcome_cohesion']['full']}.
- Full đúng hoặc trước mốc riêng: thêm {p['early_pp']} PP một lần, trừ hợp đồng E103 đã bỏ quyền thưởng sớm theo mục 6.5.
- Partial: 2–3/4, cohesion +{p['outcome_cohesion']['partial']}, idea hỗ trợ nhỏ {p['timed_reward_days']} ngày.
- Fail: 0–1/4, cohesion {p['outcome_cohesion']['fail']}, PP factor -3% trong 180 ngày.
- Tier tối đa {p['tier_cap']}; thành công ở tier tối đa nhận thưởng tạm thời thay tier mới.
- E103 và E104 có cửa sổ hợp đồng riêng; resolver chương trình giữ deadline cuối của mình.

**Ngày dư dùng được — decision “Dự án hỗ trợ thực thi sau nghiệm thu”.** Full đúng hoặc trước mốc riêng mở một dự án phụ, kể cả khi đã bỏ thưởng PP qua E103-B/C. Giá {p['side_project']['pp']} PP, ngân khố {p['side_project']['treasury']}; thời gian {p['side_project']['days']} ngày, một mục tiêu: hoàn tất dự án hỗ trợ tại cùng bộ phận đã được nghiệm thu. Khi thành công nhận idea bureaucracy cost factor -1% trong {p['timed_reward_days']} ngày; không trao tier hoặc PP. Idea thay thế cùng loại khi còn hạn, không cộng chồng. Deadline dự án phụ là ngày mở chuẩn bị đại hội sau, tách khỏi mission trọng điểm đã đóng. Bắt đầu chỉ khi còn ít nhất thời gian dự án cộng {p['reserve_days']} ngày dự phòng. Timeout/cancel không trao thưởng; tooltip báo điều kiện và tiền đã chi. Guard `VIE_last_side_project_epoch` ghi lúc nhận dự án, cùng epoch chương trình: tối đa một lần mỗi nhiệm kỳ, hủy cũng không mở lại. F12/timeout/load save dùng chung guard.

Gói trả đủ {p['fast_upfront_pp']+p['checkpoint_count']*p['checkpoint_pp']} PP so với thưởng {p['early_pp']} PP chênh {p['fast_upfront_pp']+p['checkpoint_count']*p['checkpoint_pp']-p['early_pp']} PP. Giá trị còn lại là dự án phụ và cơ hội có hạn, không phải PP miễn phí.

**Bất biến lịch:** bắt đầu muộn nhất + deadline phải cách chuẩn bị đại hội sau ít nhất {p['reserve_days']} ngày. Theo ngày ở mục 5.1, khoảng cách nhỏ nhất là {min(gap for _,gap in gaps)} ngày, đã tính bằng script. Chuỗi chuẩn/cấp tốc mặc định phải xong trước deadline trừ dự phòng; các hậu quả lựa chọn E102/E103 được liệt kê ở mục 6.5. Lượt 1 còn cần chốt các ngoại lệ full nhưng thiếu dự phòng."""
    section("### 4.2. Hai deadline với chức năng khác nhau", "### 4.3.", body)
    replace("ký theo ủy quyền 35 ngày | Mất 5; giảm 10; ký 30 ngày", f"ký theo ủy quyền {p['sign_days'][1]} ngày | Mất 5; giảm 10; ký {p['sign_days'][2]} ngày")
    replace("Tier 2 mở khả năng đáp ứng cửa sổ ký 30 ngày bằng ủy quyền; tier 3 đạt 21 ngày như kiêm nhiệm.", "Tier 1 đáp ứng cửa sổ E104 30 ngày; tier 2 đáp ứng XIII09 25 ngày; tier 3 hoặc kiêm nhiệm đáp ứng XIV11 21 ngày.")
    replace("Tier cán bộ/kiêm nhiệm dùng thời gian ký thấp hơn khi cùng áp dụng, không cộng hai mức giảm.", f"Ký theo tier cán bộ 0/1/2/3 là {'/'.join(map(str,p['sign_days']))} ngày; kiêm nhiệm {p['combined']['sign_days']} ngày. Tier cán bộ/kiêm nhiệm dùng thời gian ký thấp hơn khi cùng áp dụng, không cộng hai mức giảm.")
    replace("Các phương án không tự cho cohesion dương.", "E102-C cộng 90 ngày vào chuỗi chứng cứ trước khi E103 đánh giá; kiến nghị công khai phải được xử lý mới đủ nhóm mục tiêu. Mục 6.5 ghi ngày full tiềm năng khi đã xử lý, cùng cảnh báo quá hạn. Các phương án không tự cho cohesion dương.")
    combo_subset = [row for row in combos if row[0] != "balanced"]
    exceptions = []
    for row in combo_subset:
        if row[4] > p["program_deadline"]:
            exceptions.append([f"{row[0]} / {row[1]} / {row[2]} / {row[3]}", row[4], "partial ở deadline", "A cam kết quá sớm, bị bác; +180 tuần tự", "Chọn B hoặc C ngay từ E103 giữ đường full trước 900; sau khi A bị bác không xóa timer, chốt partial rõ ràng"])
    body = f"""Caller: chương trình kiểm tra đến ngày {p['e103']['caller_day']}, xếp một lần theo epoch. F10 mở cách xử lý chuyên sâu; phương án cơ sở đã có từ chương trình. Hạn cam kết là mốc sớm kiểm tra {p['early_days']['inspection']} tính từ bắt đầu.

| Lựa chọn | Giá | Kết quả |
| --- | --- | --- |
| A — Cam kết nộp hồ sơ đầy đủ đúng hạn | {p['e103']['A_pp']} PP | Đủ 4/4 trước hoặc đúng {p['early_days']['inspection']} được chấp nhận và giữ thưởng sớm. Nếu thiếu: cohesion {p['e103']['rejection_cohesion']}; thẩm định lại chạy tuần tự sau cả hạn cam kết và chứng cứ ban đầu, thêm {p['e103']['reappraisal_days']} ngày. |
| B — Xin gia hạn, công khai phần còn thiếu | {p['e103']['B_pp']} PP | Hạn hợp đồng {p['early_days']['inspection']+p['e103']['extension_days']} ngày; đủ chứng cứ mới được chấp nhận. Hủy thưởng PP sớm, không hủy quyền mở dự án phụ nếu programme thực sự full sớm. |
| C — Công bố kết quả có giới hạn | {p['e103']['C_pp']} PP | Chốt hợp đồng partial; programme vẫn tiếp tục kiểm chứng tới deadline. Bỏ thưởng PP sớm, vẫn có thể full/tier khi đủ 4/4. |

**Một quy tắc tuần tự:** T là ngày sẵn sàng đủ chứng cứ, gồm trễ E102-C. Nếu A chưa đủ ở hạn cam kết thì ngày full tiềm năng = max(T,{p['early_days']['inspection']})+{p['e103']['reappraisal_days']}; không chạy thẩm định lại song song. B/C không thêm thẩm định lại do bị bác, vẫn phải có chứng cứ thật. B trượt hạn hợp đồng không tự chốt mission thất bại; programme được đánh giá độc lập ở {p['program_deadline']}. C không tự tạo nhóm mục tiêu còn thiếu.

**Tổ hợp E102 × E103, tính bằng script.** Tập thể và cân bằng có cùng lịch chuẩn trong bảng; cấp tốc chỉ hợp lệ ở tập trung. Kiêm nhiệm không rút lại timer programme. Ngày full tiềm năng giả định kiến nghị đã được xử lý; thiếu kiến nghị sẽ hiển thị thiếu mục tiêu, không tự full.

{make_table(['Tuyến','Mode','E102','E103','Ngày full tiềm năng','Programme','Hợp đồng','Dự phòng'],combo_subset)}

**Ngoại lệ partial do lựa chọn.** Tooltip A hiển thị T, phép cộng tuần tự, ngày full tiềm năng và kết quả ở deadline trước khi chọn. Bảng xác nhận đường thay thế trước khi cam kết, hoặc partial rõ ràng sau khi đã cam kết; không có fail giấu kín.

{make_table(['Tổ hợp lựa chọn','Ngày full tiềm năng','Kết quả','Lý do','Đường thay thế / phục hồi'],exceptions)}

**Điểm chưa đạt I5:** E102-C + B/C ở đường chuẩn cho ngày full 840 (tập thể/cân bằng) hoặc 825 (tập trung). Các ngày này trước 900 nhưng sau 800, nên thiếu dự phòng; chúng không phải ngoại lệ partial theo quy tắc hiện tại. Đang chờ quyết định, chưa thêm một luật để ép partial. A không còn rẻ nhất tất định: hồ sơ cấp tốc đúng hạn có giá trực tiếp 0; hồ sơ chuẩn bị bác mất 6 cohesion (quy đổi 18 PP) và trượt deadline, còn C giá 15 PP giữ khả năng full. B mua cửa sổ gia hạn; không mua chứng cứ."""
    section("### 6.5. E103: bằng chứng trước hạn, trả tiền không làm chứng cứ xuất hiện", "### 6.6.", body)
    replace("- Tier 1: 35 ngày; tier 2: 30 ngày; tier 3 hoặc kiêm nhiệm: 21 ngày.", f"- Tier 1: {p['sign_days'][1]} ngày; tier 2: {p['sign_days'][2]} ngày; tier 3 hoặc kiêm nhiệm: {p['sign_days'][3]} ngày. Tier 1 đã đủ cửa sổ IX; XIII09 cần 25 ngày và XIV11 cần 21 ngày.")
    replace("timer programme 660/900 vẫn giữ nguyên.", "timer programme dùng mốc sớm 600/690 theo lĩnh vực và deadline 900 ngày.")
    replace("mở hợp đồng hữu hạn nối tiếp E104. |", f"mở hợp đồng hữu hạn nối tiếp E104, cửa sổ {p['late_signature_windows']['XIII09']} ngày (giả định gameplay); tier 2 trở lên hoặc kiêm nhiệm có thể ký đúng hạn, tier 1 có phương án thu hẹp. |")
    replace("Mở danh sách hợp đồng đang hiệu lực và lựa chọn giữ, sửa hoặc chấm dứt với giá có thật. |", f"Mở danh sách hợp đồng đang hiệu lực và lựa chọn giữ, sửa hoặc chấm dứt với giá có thật; hồ sơ gia hạn có cửa sổ {p['late_signature_windows']['XIV11']} ngày (giả định gameplay), tier 3 hoặc kiêm nhiệm ký kịp, các tier thấp hơn chọn sửa/chấm dứt. |")
    replace("| Event đã xếp hàng | Pending guard |", "| Event đã xếp hàng | Pending guard |\n| Dự án phụ đã nhận trong kỳ | `VIE_last_side_project_epoch`, ghi tại nhận; mission phụ lưu deadline chuẩn bị đại hội sau, mục tiêu và kết quả |")
    replace("tính mốc 660 và kết quả hợp đồng E103", "tính mốc sớm theo chương trình 600/690 và kết quả hợp đồng E103")
    replace("Một programme full được +60 PP sớm tối đa một lần", f"Một programme full được +{p['early_pp']} PP sớm tối đa một lần")
    replace("Programme, deadline, mode và giá được tính khi bắt đầu; expiry timed idea không tự tạo success reward.", "Programme, deadline, mode và giá được tính khi bắt đầu; expiry timed idea không tự tạo success reward. Dự án phụ ghi guard nhận theo epoch trước thu PP, không mở lại sau hủy; resolver phụ chỉ trao idea khi mục tiêu đạt, timeout/cancel không thưởng.")
    replace("UI hiển thị mốc 660/900, hạn E103/E104, ngày đủ kiểm chứng, giá sau tier/cohesion và timer theo roster.", "UI hiển thị mốc sớm riêng 600/690, deadline 900, hạn E103/E104, ngày đủ kiểm chứng, giá sau tier/cohesion và timer ký 45/30/25/21 theo roster. Báo trước BoP +0.30→+0.20 khi trả đủ hai checkpoint: giữ timer hiện tại, khóa cấp tốc lần tới. Mỗi lựa chọn vượt hiển thị cohesion sau trừ và cổng ≥40; E103-A hiển thị max(T,690)+180 cùng full/partial dự kiến. Cửa sổ IX/XIII09/XIV11 lần lượt 30/25/21 ngày; tooltip dự án phụ ghi 30 PP, 270 ngày, deadline chuẩn bị kỳ sau và guard một lần.")
    replace("AI biết A-E103 cần hồ sơ, B là gia hạn, C là công bố giới hạn.", "AI biết A-E103 cần hồ sơ thật trước 690 và có thể bị bác rồi +180 tuần tự; B là gia hạn đến 810, C là công bố giới hạn. AI kiểm cổng cohesion sau trừ, giá vùng 40–54, khả năng ký theo tier và việc trả checkpoint làm rơi khỏi vùng tập trung; dự án phụ chỉ được chọn nếu đủ tiền và dự phòng tới deadline riêng.")
    examples = []
    for row in rows:
        if row["eligible"] and row["program"] == "inspection" and row["e102"] == "A" and row["e103"] == "B" and row["k"] == p["k_values"][1] and row["r"] == p["r_values"][1]:
            examples.append([row["route"],row["mode"],row["pp_net_cost"],row["treasury_net_cost"],row["potential_full_day"],row["pp_early_reward"],row["cohesion_final"],row["bop_final"],row["converted_cost"],row["side_project_available"]])
    body = f"""Nguồn duy nhất: [B1 JSON](VIETNAM_POLITICAL_PARAMETERS_VI.json), [script .py](VIETNAM_POLITICAL_BALANCE_VI.py), [CSV](VIETNAM_POLITICAL_BALANCE_VI.csv), [báo cáo lượt 1](VIETNAM_POLITICAL_REVIEW_L1_VI.md). Chạy `python VIETNAM_POLITICAL_BALANCE_VI.py` để dựng lại CSV và bảng kiểm; kết quả là số học, chưa kiểm engine.

CSV có {len(rows)} hàng: bốn chương trình × ba tuyến × bốn mode × k/r, với chín tổ hợp E102×E103 cho chương trình kiểm tra. {sum(row['eligible'] for row in rows)} hàng hợp lệ; các hàng cấp tốc/kiêm nhiệm bị BoP khóa có `eligible=0`, không có kết quả giả. Mỗi tuyến nhận cùng bộ event và lựa chọn khi so cùng programme. Programme khác không tự nhận event kiểm toán.

Snapshot chuẩn hóa: tier cán bộ 0, cohesion {p['cohesion_initial']}, BoP −0.30/0/+0.30. Các khoản focus và kiện toàn trước snapshot được tách khỏi phép so: F01/F07 trao 50 PP, F02 thu25, F04 thu thêm25 ở đường mở tập trung; CSV không giả vờ cân bằng có cùng lịch focus. E101 có caller riêng F05, được kiểm giá trong báo cáo, không cộng vào ma trận programme rồi làm lệch bộ event giữa tuyến. Cần chốt nếu muốn mở rộng snapshot sang cả lịch focus và E101.

Thu nhập r={p['r_values']}, cộng bonus nhánh {p['branch_pp_daily']} PP/ngày trong cửa sổ {p['accounting_days']} ngày. k={p['k_values']} là tỷ giá thử ngân khố/PP. Thu PP mô hình=(r+bonus)×cửa sổ; không bao gồm stock đầu, cap, luật/chiến tranh chưa mô hình hóa. Chi phí quy đổi=PP ròng + ngân khố ròng×k + (cohesion đầu−cuối)×{p['cohesion_pp_rate']}; cohesion nhận là khoản âm, không biến thành thu PP thật. Tỷ lệ chi phí/thu nhập có cả gross và net. Side project là lựa chọn riêng sau full, giá/finish nếu chọn có cột riêng, chưa cộng vào tổng programme.

**Ngày full và mốc sớm cơ sở, tính từ B1:**

{make_table(['Programme','Chuẩn tập thể/cân bằng','Chuẩn tập trung','Mốc sớm','Cấp tốc'],core)}

**So cùng E102-A, E103-B, k=40, r=1:** B đã bỏ thưởng PP sớm ở mọi tuyến. E104 dùng cùng phản hồi đối tác chấp nhận: phân vai tier0 lấy gói thu hẹp, kiêm nhiệm ký gói đầy đủ.

{make_table(['Tuyến','Mode','Chi PP ròng','Chi ngân khố ròng','Ngày full','Thưởng PP sớm','Cohesion cuối','BoP cuối','Chi quy đổi','Dự án phụ mở'],examples)}

Case đổi E103 sang A trên cùng chứng cứ chuẩn phải cộng thẩm định lại tuần tự; CSV ghi cả ngày full tiềm năng và kết quả partial khi quá 900. Case cấp tốc A đủ hồ sơ nhận 50 PP, còn B/C bỏ thưởng PP nhưng vẫn có ngày dư để mở dự án phụ nếu full trước mốc riêng.

**Khoảng cách lịch:** chênh ngày đại hội −180 chuẩn bị −270 khởi động muộn −900 deadline.

{make_table(['Nhiệm kỳ','Ngày còn cách chuẩn bị kỳ sau'],gaps)}

Từ cohesion60, một gói vượt đưa về44; lần vượt tiếp theo bị khóa. Muốn vượt đủ gói sau cần hai lượt phục hồi:60PP, lên64, hoàn tất270ngày với cooldown180. Cadre cần giữ55 liên tục90ngày nên CSV cộng hai lượt30PP trong lúc triển khai; lịch165→255 và345→435 cho phép kiểm chứng465→555. Các programme khác chưa cần phục hồi để nghiệm thu theo giả định của ma trận. BoP cuối chỉ tính hành động đã kê: snapshot tập trung +0.30, trả đủ →+0.20, vượt đủ →+0.40, trả đủ kèm kiêm nhiệm →+0.30. Cả mode hiện tại và quyền lần tới đều được nêu ở tooltip.

Chiến tranh, counter reset, kiến nghị chưa đóng, công cụ mở muộn và kinh tế chưa đạt mục tiêu đều nằm ngoài lịch cơ sở; CSV không chứng minh full chắc chắn trong game. I3 và ngoại lệ dự phòng I5 còn cần quyết định, chi tiết ở báo cáo lượt 1."""
    section("### 11.1. Bảng ngân sách một nhiệm kỳ", "### 11.2.", body)
    replace("Chuẩn→cấp tốc đổi được mốc 660 hoặc một cơ hội có hạn trong ít nhất một case.", "Chuẩn→cấp tốc đổi được mốc 600 (cán bộ/công vụ/dân vận) hoặc 690 (kiểm tra); gói trả55 và thưởng50 chênh5PP. Kiểm riêng quyền dự án phụ270ngày/30PP và cửa sổ ký30/25/21ngày.")
    replace("Chương trình chuẩn vẫn có đường full trước deadline cuối.", "Chương trình chuẩn/cấp tốc mặc định full trước 900−100=800; deadline bắt đầu+900 cách chuẩn bị kỳ sau ít nhất100ngày. Ngoại lệ do lựa chọn ghi tổ hợp, ngày, kết quả và đường thay thế ở6.5; các ngoại lệ full thiếu dự phòng vẫn chưa được chốt.")
    replace("ngày 660/900, hạn ký 30 ngày", "ngày 600/690/900, hạn ký 30/25/21 ngày")
    replace("Đã sửa thiết kế và tạo bảng ngân sách: ba vùng BoP, phản đối thu giá một lần, một trọng tâm, tier cán bộ có giá, thời gian nhất quán, mốc thưởng/cơ hội, event bằng chứng, BoP theo hành vi, kiêm nhiệm dùng ngay và gate theo đại hội.", "Đã hoàn thành chỉnh tài liệu lượt 1 và tính lại CSV bằng script từ B1: mốc riêng 600/690, thưởng50, cổng cohesion sau trừ40, giá vùng40–54=1.05, ký tier30/25/21, deadline+900 và dự án phụ. I3 còn FAIL về giá checkpoint; I5 còn chờ ngoại lệ full thiếu dự phòng. Lượt 2 và lượt 3 chưa thực hiện; chưa tuyên bố mọi bất biến đạt.")
    assert text.rstrip().endswith("BLUF")
    for number in ["1", "2", "9"]:
        block = re.search(rf"^## {number}\..*?(?=^## |\Z)", text, re.M | re.S).group(0)
        assert hashlib.sha256(block.encode()).hexdigest() == data["baseline_sections"][number], f"Changed protected section {number}"
    assert len(re.findall(r"^\| (?:F|IX|X|XI|XII|XIII|XIV)\d\d(?: `[^`]+`)? \|",text,re.M)) == len(p["focus_nodes"])
    DOC.write_text(text,encoding="utf-8")


def run():
    args = argparse.ArgumentParser()
    args.add_argument("--capture-b1", action="store_true")
    args.add_argument("--apply-l1", action="store_true")
    args.add_argument("--sync-confirmed", action="store_true")
    parsed = args.parse_args()
    if parsed.capture_b1:
        capture_b1()
    data = json.loads(PARAMS.read_text(encoding="utf-8"))
    p = {key: row["value"] for key, row in data["parameters"].items()}
    sequences = {"cadre": ["training", "training", "succession", "review"],
                 "administration": ["administration_project", "administration_project", "review"],
                 "inspection": ["audit_standard", "audit", "audit", "review"],
                 "social": ["local_project", "local_project", "review"]}
    names = {"cadre": "Cán bộ", "administration": "Công vụ", "inspection": "Kiểm tra", "social": "Dân vận"}
    routes = list(p["prepare_days"])
    modes = ["standard", "fast_paid", "fast_override", "combined_fast_paid"]

    def timeline(program, route, fast):
        return p["prepare_days"][route] + sum(p["action_days"][action][int(fast)] for action in sequences[program])

    def audit_outcome(base, e102, e103):
        evidence = base + p["e102"][e102][2]
        cutoff = p["early_days"]["inspection"]
        rejected = e103 == "A" and evidence > cutoff
        potential = max(evidence, cutoff) + p["e103"]["reappraisal_days"] if rejected else evidence
        # B buys a contract extension; C closes only the contract as partial.
        # Neither operation substitutes for program evidence.
        contract = "accepted" if e103 == "A" and not rejected else "rejected" if rejected else "extended" if e103 == "B" else "partial"
        if e103 == "B" and evidence > cutoff + p["e103"]["extension_days"]:
            contract = "extension_missed"
        return potential, rejected, contract

    rows = []
    for program, route, mode in itertools.product(sequences, routes, modes):
        fast = mode != "standard"
        combined = mode == "combined_fast_paid"
        legal = not fast or p["bop_route_snapshot"][route] > p["bop_threshold"]
        event_pairs = itertools.product("ABC", "ABC") if program == "inspection" else [("NA", "NA")]
        for e102, e103 in event_pairs:
            for k, r in itertools.product(p["k_values"], p["r_values"]):
                record = {"program": program, "route": route, "mode": mode, "e102": e102, "e103": e103,
                          "k": k, "r": r, "eligible": int(legal), "status": "script_calculation_not_engine" if legal else "locked_by_bop"}
                if not legal:
                    rows.append(record)
                    continue
                cohesion = p["cohesion_initial"]
                bop = p["bop_route_snapshot"][route]
                factor = next(band[2] for band in p["cohesion_price_bands"] if band[0] <= cohesion <= band[1])
                start = int((Decimal(str(p["tools"]["start"][0])) * Decimal(str(factor))).to_integral_value(rounding=ROUND_CEILING))
                tools = sum(p["tools"][action][0] for action in sequences[program])
                treasury = sum(p["tools"][action][1] for action in sequences[program])
                upfront = p["fast_upfront_pp"] if fast else 0
                checkpoints = p["checkpoint_count"] * p["checkpoint_pp"] if fast and mode != "fast_override" else 0
                checkpoint_treasury = p["checkpoint_count"] * p["checkpoint_treasury"] if fast and mode != "fast_override" else 0
                treasury += checkpoint_treasury
                recovery = 0
                office = p["combined"]["pp"] if combined else 0
                if combined:
                    assert bop > p["bop_threshold"] and cohesion >= p["cadre_cohesion_required"]
                    # Program price/mode was signed first; offices merge before checkpoint drift.
                    cohesion += p["combined"]["cohesion"]
                    bop += p["combined"]["bop"]
                if mode == "fast_override":
                    for _ in range(p["checkpoint_count"]):
                        assert cohesion - p["override_cohesion"] >= p["override_floor"]
                        cohesion -= p["override_cohesion"]
                        bop += p["override_bop"]
                    if program == "cadre":
                        # Recover between checkpoints and before succession review.
                        recovery = math.ceil((p["cadre_cohesion_required"] - cohesion) / p["recovery"]["cohesion"])
                        cohesion += recovery * p["recovery"]["cohesion"]
                elif fast:
                    bop += p["checkpoint_count"] * p["consult_bop"]
                if program == "cadre" and combined:
                    recovery = max(0, math.ceil((p["cadre_cohesion_required"] - cohesion) / p["recovery"]["cohesion"]))
                    cohesion += recovery * p["recovery"]["cohesion"]
                day = timeline(program, route, fast)
                event_pp, signature, grant = 0, 0, 0
                contract = "NA"
                rejected = False
                if program == "inspection":
                    event_pp += p["e102"][e102][0] + p["e103"][e103 + "_pp"]
                    treasury += p["e102"][e102][1]
                    day, rejected, contract = audit_outcome(day, e102, e103)
                    if rejected:
                        cohesion += p["e103"]["rejection_cohesion"]
                    if e102 == "A":
                        # Identical partner acceptance scenario on all routes.
                        option = "A" if combined else "B"
                        signature = p["e104"][option + "_pp"]
                        grant = p["e104"][option + "_grant"]
                        treasury -= grant
                full = day <= p["program_deadline"]
                early_full = full and day <= p["early_days"][program]
                early = early_full and (program != "inspection" or contract == "accepted")
                bonus = p["early_pp"] if early else 0
                if full and route == "collective":
                    cohesion += min(p["collective_full_extra"], max(0, p["collective_extra_cap"] - cohesion))
                cohesion += p["outcome_cohesion"]["full" if full else "partial"]
                cohesion = min(p["cohesion_limits"][1], max(p["cohesion_limits"][0], cohesion))
                gross = start + tools + event_pp + upfront + checkpoints + office + signature + recovery * p["recovery"]["pp"]
                net = gross - bonus
                daily = (r + p["branch_pp_daily"]) * p["accounting_days"]
                loss = p["cohesion_initial"] - cohesion
                record.update(pp_start=start, pp_actions=tools, pp_e102=0 if e102 == "NA" else p["e102"][e102][0],
                              pp_e103=0 if e103 == "NA" else p["e103"][e103 + "_pp"], pp_fast_upfront=upfront,
                              pp_checkpoints=checkpoints, pp_combined=office, pp_signature=signature,
                              pp_recovery=recovery * p["recovery"]["pp"], pp_early_reward=bonus,
                              treasury_checkpoints=checkpoint_treasury,
                              pp_gross_cost=gross, pp_net_cost=net, treasury_net_cost=round(treasury, 6),
                              treasury_pp_equivalent=round(treasury*k, 6), potential_full_day=day,
                              full_day=day if full else "", result="full" if full else "partial_at_deadline",
                              remaining_reserve_days=p["program_deadline"]-day if full else "",
                              full_after_early_cutoff=int(full and day>p["early_days"][program]),
                              declared_choice_exception=int(full and day>p["early_days"][program] and program==p["choice_full_exception"]["program"] and e102==p["choice_full_exception"]["e102"] and e103 in p["choice_full_exception"]["e103"]),
                              early_cutoff=p["early_days"][program], early_reward_earned=int(early),
                              cohesion_final=cohesion, cohesion_net_spent=loss, bop_final=round(bop, 6),
                              modeled_pp_income=round(daily, 6), modeled_pp_remaining=round(daily-net, 6),
                              gross_cost_income_ratio=round(gross/daily, 6), net_cost_income_ratio=round(net/daily, 6),
                              converted_cost=round(net+treasury*k+loss*p["cohesion_pp_rate"], 6),
                              converted_cost_income_ratio=round((net+treasury*k+loss*p["cohesion_pp_rate"])/daily,6),
                              e103_contract=contract, e104_grant=grant, side_project_available=int(early_full),
                              side_project_if_taken_pp=p["side_project"]["pp"] if early_full else 0,
                              side_project_if_taken_finish=day+p["side_project"]["days"] if early_full else "",
                              technical_training_opportunity=int(grant > 0),
                              deep_data_cooperation_opportunity=int(grant == p["e104"]["A_grant"]),
                              opportunity_count=int(early_full)+int(grant > 0))
                rows.append(record)
    columns = list(dict.fromkeys(key for row in rows for key in row))
    with CSV.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

    core = [[names[program], timeline(program,"collective",False), timeline(program,"central",False),
             p["early_days"][program], timeline(program,"central",True)] for program in sequences]
    dates = list(p["congress_dates"].items())
    gaps = [[term, (date.fromisoformat(nxt)-date.fromisoformat(now)).days-p["congress_preparation_days"]-p["program_start_latest"]-p["program_deadline"]]
            for (term,now),(_,nxt) in zip(dates,dates[1:])]
    combo_rows = []
    for route, mode, a, b in itertools.product(routes, ["standard","fast_paid"], "ABC", "ABC"):
        if mode != "standard" and route != "central":
            continue
        day, rejected, contract = audit_outcome(timeline("inspection",route,mode!="standard"),a,b)
        combo_rows.append([route,mode,"E102-"+a,"E103-"+b,day,
                           "partial ở 900" if day>p["program_deadline"] else "full",
                           contract, "Ngoại lệ lựa chọn" if day>p["program_deadline"]-p["reserve_days"] else "Trong dự phòng"])
    event_costs = []
    for k in p["k_values"]:
        for option, values in p["e101"].items():
            pp,cash,c,_,_ = values
            event_costs.append(["E101",option,k,pp+cash*k-c*p["cohesion_pp_rate"]])
        for option, values in p["e102"].items():
            pp,cash,_=values
            event_costs.append(["E102",option,k,pp+cash*k])
        for option in "ABC":
            event_costs.append(["E104",option,k,p["e104"][option+"_pp"]-(p["e104"].get(option+"_grant",0)*k)])
        event_costs.extend([["E103 hồ sơ đúng hạn","A",k,p["e103"]["A_pp"]],
                            ["E103 hồ sơ trễ","A",k,p["e103"]["A_pp"]-p["e103"]["rejection_cohesion"]*p["cohesion_pp_rate"]],
                            ["E103","B",k,p["e103"]["B_pp"]], ["E103","C",k,p["e103"]["C_pp"]],
                            ["checkpoint","thương lượng",k,p["checkpoint_pp"]+p["checkpoint_treasury"]*k],
                            ["checkpoint","vượt",k,p["override_cohesion"]*p["cohesion_pp_rate"]]])
    eligible = [row for row in rows if row["eligible"] and row["k"] == p["k_values"][0] and row["r"] == p["r_values"][1]]

    def weakly_better(a,b,cost_key="pp_net_cost"):
        better = [a[cost_key] <= b[cost_key], a["potential_full_day"] <= b["potential_full_day"],
                  a["cohesion_final"] >= b["cohesion_final"],
                  a["side_project_available"] >= b["side_project_available"],
                  a["technical_training_opportunity"] >= b["technical_training_opportunity"],
                  a["deep_data_cooperation_opportunity"] >= b["deep_data_cooperation_opportunity"]]
        return all(better)

    def universal_winners(pool,cost_key="pp_net_cost"):
        return [a for a in pool if all(weakly_better(a,b,cost_key) for b in pool)
                and any(not weakly_better(b,a,cost_key) for b in pool)]

    winners = universal_winners(eligible)
    route_winners = {route: universal_winners([row for row in eligible if row["route"] == route]) for route in routes}
    dominance_checks = []
    for k,r,cost_key in itertools.product(p["k_values"],p["r_values"],["pp_net_cost","converted_cost"]):
        pool=[row for row in rows if row["eligible"] and row["k"]==k and row["r"]==r]
        dominance_checks.append([k,r,cost_key,len(universal_winners(pool,cost_key)),
                                 *[len(universal_winners([row for row in pool if row["route"]==route],cost_key)) for route in routes]])
    representatives=[row for row in rows if row["eligible"] and row["k"]==p["k_values"][0] and row["r"]==p["r_values"][1]]
    late_full=[row for row in representatives if row["program"]=="inspection" and row["full_after_early_cutoff"]]
    full_exceptions=[row for row in late_full if row["declared_choice_exception"]]
    full_exception_table=[[row["route"],row["mode"],row["e102"],row["e103"],row["full_day"],row["remaining_reserve_days"],row["pp_early_reward"],"full"] for row in full_exceptions]
    late_full_table=[[row["route"],row["mode"],row["e102"],row["e103"],row["full_day"],row["remaining_reserve_days"],row["pp_early_reward"],"Ngoại lệ lựa chọn" if row["declared_choice_exception"] else "Chuẩn mặc định, đủ dự phòng"] for row in late_full]
    assert all(row["pp_early_reward"]==0 and row["side_project_available"]==0 for row in full_exceptions)
    reserve_breaks=[row for row in representatives if row["result"]=="full" and row["remaining_reserve_days"]<p["reserve_days"] and not row["declared_choice_exception"]]
    assert not reserve_breaks, "Full thiếu dự phòng chưa được người dùng cho phép"
    checkpoint_rows=[[k,p["checkpoint_pp"]+p["checkpoint_treasury"]*k,p["override_cohesion"]*p["cohesion_pp_rate"],
                      (p["checkpoint_pp"]+p["checkpoint_treasury"]*k)-(p["override_cohesion"]*p["cohesion_pp_rate"])] for k in p["k_values"]]
    assert min(row[3] for row in checkpoint_rows)<0<max(row[3] for row in checkpoint_rows)
    exception_cheapest=[]
    for row in full_exceptions:
        cheapest_all=True
        for k in p["k_values"]:
            pool=[item for item in rows if item["eligible"] and item["program"]==row["program"] and item["route"]==row["route"] and item["mode"]==row["mode"] and item["k"]==k and item["r"]==p["r_values"][1] and item["result"]=="full"]
            match=next(item for item in pool if item["e102"]==row["e102"] and item["e103"]==row["e103"])
            cheapest_all &= match["converted_cost"]<=min(item["converted_cost"] for item in pool)
        exception_cheapest.append([row["route"],row["mode"],row["e102"],row["e103"],"Có" if cheapest_all else "Không"])
    exception_pair_dominance=[]
    for route,mode in sorted({(row["route"],row["mode"]) for row in full_exceptions}):
        pair=[row for row in full_exceptions if row["route"]==route and row["mode"]==mode]
        b=next(row for row in pair if row["e103"]=="B")
        c=next(row for row in pair if row["e103"]=="C")
        assert weakly_better(c,b) and not weakly_better(b,c)
        exception_pair_dominance.append([route,mode,b["pp_net_cost"]-c["pp_net_cost"],b["potential_full_day"],b["cohesion_final"],"C trội B trong ma trận; B chỉ khác trạng thái hợp đồng"])
    assert all(standard > early >= fast and central > early for _,standard,central,early,fast in core)
    assert min(gap for _,gap in gaps) >= p["reserve_days"]
    paid_package = p["fast_upfront_pp"] + p["checkpoint_count"] * p["checkpoint_pp"]
    assert abs(paid_package-p["early_pp"]) <= p["max_fast_reward_pp_difference"]
    assert sorted(c for low,high,_ in p["cohesion_price_bands"] for c in range(low,high+1)) == list(range(p["cohesion_limits"][0],p["cohesion_limits"][1]+1))
    assert len({factor for _,_,factor in p["cohesion_price_bands"]}) == len(p["cohesion_price_bands"])
    boundary_prices = []
    for low,high,factor in p["cohesion_price_bands"]:
        prices = [int((Decimal(str(p["tools"]["start"][0]-discount))*Decimal(str(factor))).to_integral_value(rounding=ROUND_CEILING)) for discount in p["cadre_discount_pp"]]
        boundary_prices.append([f"{low}–{high}",factor,*prices])
    override_checkpoint_cost = p["override_cohesion"]*p["cohesion_pp_rate"]
    package_cash=p["checkpoint_count"]*p["checkpoint_treasury"]
    package_differences=[[k,paid_package,p["early_pp"],paid_package-p["early_pp"],package_cash,paid_package-p["early_pp"]+package_cash*k] for k in p["k_values"]]
    low_cohesion_days=timeline("inspection","collective",False)+p["low_cohesion_prepare_extra"]
    checks = [
        ["I1","PASS", "; ".join(f"{name}: {standard}/{central} > {early} >= {fast}" for name,standard,central,early,fast in core)],
        ["I2","PASS (PP thuần)",f"{paid_package}−{p['early_pp']}={paid_package-p['early_pp']} PP; cộng ngân khố, chênh quy đổi {[row[-1] for row in package_differences]} ở k={p['k_values']}. Giá trị còn lại: dự án phụ L1.2."],
        ["I3","FAIL (E103 trong ngoại lệ)", f"Checkpoint PASS: thương lượng {[row[1] for row in checkpoint_rows]} so với vượt {override_checkpoint_cost}; k=40 biên1PP. Trong E102-C, E103-C rẻ hơn B {p['e103']['B_pp']-p['e103']['C_pp']} PP mọi k, cùng lịch/full/cohesion/cơ hội mô hình. Không tự chỉnh giá."],
        ["I4","PASS (vùng)","BoP: thưởng nghiệm thu / chuẩn / công cụ cấp tốc; cohesion: 1.25/1.15/1.05/1.00/0.90; cổng sau trừ >=40"],
        ["I5","PASS (snapshot); FAIL ngoài snapshot",f"Cohesion60: chuẩn750/cấp tốc645 <=900−100=800; ngoại lệ C+B/C đủ điều kiện bảng riêng, không thưởng sớm; lịch cách tối thiểu{min(gap for _,gap in gaps)} ngày. Cohesion<20: chuẩn kiểm tra{low_cohesion_days}, chỉ còn{p['program_deadline']-low_cohesion_days} ngày, chưa có ngoại lệ được phép."],
        ["I6","FAIL (chưa đạt lượt 2)",f"Đếm {len(p['focus_nodes'])}=2+6×12; giữ cost. 40 node còn thiếu caller/lựa chọn đầy đủ; chưa tự điền."],
        ["I7","FAIL (chưa audit lượt 3)","Guard dự án phụ đã ghi 8.1; registry cũ chưa định danh đầy đủ mission/idea/milestone."],
        ["I8","FAIL (chưa xác minh lượt 2)","Nguồn lịch 5.1 giữ nguyên; trái phiếu XI và tiền đề Biển Đông cần tra nguồn ở lượt 2."],
        ["I9","PASS","Chỉ tính script; không chạy engine/console/playtest."],
        ["I10","PASS (ma trận hữu hạn)" if not any(any(row[3:]) for row in dominance_checks) else "FAIL",f"Kiểm PP ròng và quy đổi ở mọi k/r; số tổ hợp thống trị toàn bộ/theo tuyến: {max(max(row[3:]) for row in dominance_checks)}. Trong cặp ngoại lệ C+B/C, E103-C trội B trong các chỉ số đã mô hình hóa; báo riêng, không sửa giá."]]
    source_rows = []
    for key, row in data["parameters"].items():
        value = "74 node: cost và hàng nguồn được lưu trong JSON" if key == "focus_nodes" else json.dumps(row["value"], ensure_ascii=False)
        source_rows.append([key,value,row.get("old","Giữ / bổ sung theo yêu cầu"),row["refs"]])
    report = "# Lượt 1: kết quả tính script và điểm cần chốt\n\nĐã áp dụng hai quyết định người dùng:0.25ngân khố/checkpoint thương lượng và ngoại lệ full E102-C+E103-B/C. Giữ55PP/50PP, deadline900, mọi giá khác. Dừng trước lượt2; I3 còn vướng E103-B/C trong ngoại lệ, không sửa thêm giá.\n\n"
    report += "## B1: bảng tham số duy nhất\n\nNguồn có thể chạy lại: `VIETNAM_POLITICAL_PARAMETERS_VI.json`. Script đọc nguồn này, không đọc số trong văn xuôi làm đầu vào. Bảng ghi đủ giá đã xác định; giá còn thiếu trong 40 node một dòng là CHƯA XÁC ĐỊNH, cần lượt 2. Các source_row của node là chụp đầu vào để kiểm scope, không là nguồn thay thế tham số chung.\n\n"
    report += table(["Tham số","Giá trị","Cũ","Mục sử dụng"],source_rows)
    report += "\n\n## Bảng bất biến I1–I10\n\n" + table(["Bất biến","Kết quả","Phép tính / giới hạn"],checks)
    report += "\n\n## Ngày full cơ sở\n\n" + table(["Chương trình","Chuẩn tập thể/cân bằng","Chuẩn tập trung","Mốc sớm","Cấp tốc hợp lệ"],core)
    report += "\n\n## Giá khởi động tại mọi biên cohesion/tier\n\nLàm tròn lên bằng Decimal; kiểm đủ vùng0–100, không chồng biên. Kiêm nhiệm ngay sau ký mode/giá không tính lại giá đã ký.\n\n" + table(["Vùng","Hệ số","Tier0","Tier1","Tier2","Tier3"],boundary_prices)
    report += "\n\n## Khoảng cách bắt đầu muộn nhất tới chuẩn bị đại hội sau\n\nCông thức: chênh ngày hai đại hội − chuẩn bị 180 − khởi động muộn 270 − deadline 900.\n\n" + table(["Nhiệm kỳ","Ngày còn cách chuẩn bị kỳ sau"],gaps)
    report += "\n\n## E102 × E103: chuỗi và ngoại lệ do lựa chọn\n\nT là ngày chứng cứ sẵn sàng. E103-A bị bác: full tiềm năng=max(T,690)+180, chạy tuần tự. Nếu quá 900 thì chốt partial; lựa chọn B hoặc C ngay tại E103 giữ đường full theo T. T nằm 801–900 cũng là ngoại lệ dự phòng có cảnh báo, không phải đường mặc định. B sau 810 trượt hợp đồng nhưng programme vẫn được xét đủ chứng cứ trước 900. C chốt hợp đồng partial, tiếp tục hồ sơ để full programme; không nhận thưởng sớm. Không có fail bất ngờ trong các tổ hợp này. Thời gian chứng cứ dưới đây giả định kiến nghị đã xử lý; chưa xử lý thì tooltip nêu nhóm mục tiêu còn thiếu.\n\n"
    report += table(["Tuyến","Mode","E102","E103","Full tiềm năng","Kết quả","Hợp đồng","Dự phòng"],combo_rows)
    report += "\n\n## Ngoại lệ full được người dùng chốt\n\nChỉ E102-C cùng E103-B hoặc C; không là đường mặc định. Miễn yêu cầu dự phòng100ngày nếu nằm trong bảng; deadline900 giữ nguyên. Không nhận thưởng PP sớm hoặc dự án phụ. Các hàng có dự phòng>=100 vẫn được liệt kê vì full sau mốc sớm. Tooltip trước khi chọn ghi ngày full, dự phòng còn X ngày, chậm thêm quá dự phòng sẽ rơi xuống partial. Không có cơ chế bù.\n\n" + table(["Tuyến","Mode","E102","E103","Ngày full","Dự phòng còn","Thưởng PP sớm","Kết quả"],full_exception_table)
    report += "\n\n## Mọi tổ hợp full sau mốc sớm\n\nCác lựa chọn chuẩn A/B+B/C đủ dự phòng là đường cơ sở, tách khỏi ngoại lệ C+B/C. Mọi mode hợp lệ có trong bảng, k/r không đổi timer nên không lặp hàng theo chúng.\n\n" + table(["Tuyến","Mode","E102","E103","Ngày full","Dự phòng còn","Thưởng PP sớm","Phân loại"],late_full_table)
    report += "\n\n## I2: PP thuần và chênh quy đổi bổ sung\n\nk chỉ là tham số sensitivity, không phải tỷ giá thật trong game. I2 theo yêu cầu kiểm PP thuần; không chuyển định nghĩa sang quy đổi. Dự án phụ L1.2 là phần giá trị còn lại; cửa sổ ký được theo dõi độc lập.\n\n" + table(["k thử","Giá gói PP","Thưởng PP","Chênh PP thuần","Ngân khố gói","Chênh quy đổi"],package_differences)
    report += "\n\n## I3: biên checkpoint từng k\n\nDấu âm: thương lượng rẻ hơn; dấu dương: vượt rẻ hơn theo giá quy đổi. Biên k=40 chỉ1PP; chưa kiểm sức mua/engine, không chỉnh rộng biên.\n\n" + table(["k thử","Thương lượng quy đổi","Vượt quy đổi","Thương lượng − vượt"],checkpoint_rows)
    report += "\n\n## I3 trên ngoại lệ: có rẻ nhất ở mọi k không?\n\nSo cùng tuyến/mode với mọi lựa chọn E102×E103 cho kết quả full trong programme kiểm tra; ngày chậm và dữ liệu được giữ riêng.\n\n" + table(["Tuyến","Mode","E102","E103","Rẻ nhất ở mọi k"],exception_cheapest)
    report += "\n\n## Điểm lệch trong chính cặp ngoại lệ\n\nGiữ E102-C, E103-C luôn tiết kiệm15PP so với B trong mọi k/r; cùng ngày/cohesion/cơ hội trong CSV. B chỉ mua trạng thái hợp đồng được chấp nhận, chưa có lợi ích gameplay được định nghĩa riêng. Đây là rủi ro lựa chọn B bị trội, không được che bằng thưởng mới.\n\n" + table(["Tuyến","Mode","C tiết kiệm PP so B","Ngày full chung","Cohesion chung","Kết luận"],exception_pair_dominance)
    report += "\n\n## I10: chạy lại sau khi thêm ngân khố\n\nMỗi hàng kiểm toàn ma trận và từng tuyến. Cơ hội so theo dự án phụ, chuyên gia và hợp tác sâu; không gộp chúng thành một điểm tùy ý. PP ròng và chi quy đổi được kiểm riêng; r chỉ đổi mẫu số thu nhập, không đổi tier/thời gian.\n\n" + table(["k","r","Thước đo chi","Thống trị toàn bộ","Tập thể","Cân bằng","Tập trung"],dominance_checks)
    report += "\n\n## Giá quy đổi từng lựa chọn\n\nGiá=PP+ngân khố×k−cohesion nhận×3; số âm là nguồn lực nhận ròng. Ngày và quyền dữ liệu được ghi riêng, không quy thành PP giả. Không cộng thưởng chương trình vào giá event để tránh tính trùng.\n\n" + table(["Event / bối cảnh","Lựa chọn","k","Giá quy đổi"],event_costs)
    report += "\n\n## Cohesion và phục hồi\n\n60→52→44: một gói vượt đủ hai checkpoint; lần vượt tiếp theo 44−8=36<40 bị khóa. Gói thứ hai cần 44+2×10=64: 60 PP; phục hồi hoàn tất sau 270 ngày nếu chọn ngay ngày 0 và 180. Từ 44 chỉ một lượt 30 PP cho 54 mở được một checkpoint (54−8=46), chưa mở đủ hai (46−8=38). Cadre đòi 55 trong review, nên case vượt cần hai lượt phục hồi trong lúc triển khai: chọn sau checkpoint đầu tại ngày 165, kết thúc 255; chọn lại 345, kết thúc 435; phương án kế cận xong 465, review tới 555. Chi phí 60 PP đã cộng CSV. Đây là lịch số học, chưa kiểm engine.\n\n"
    report += "## Scope CSV\n\nMa trận chuẩn hóa tại bắt đầu programme: cohesion 60, tier cán bộ 0, BoP −0.30/0/+0.30. Focus trước snapshot, thay người, tăng trưởng/chiến tranh và 62 node mở rộng không được giả lập. Cùng một E102×E103 và phản hồi E104 được áp cho mọi tuyến trong chương trình kiểm tra; programme khác không nhận event kiểm toán. Không tự cấp gói cấp tốc cho tập thể/cân bằng: hàng bị khóa có eligible=0 và số kết quả để trống. Kiêm nhiệm được chọn ngay sau khi ký giá/mode programme, trước checkpoint khi BoP/cohesion còn đủ cổng; không chọn sau khi BoP đã giảm về0.20. Cadre kiêm nhiệm mất6 về54, cần một lượt phục hồi30PP trước review (CSV đã cộng); recovery có thể xong ngày90, trước kiểm chứng465. Side project là lựa chọn sau full trước mốc, độc lập quyền nhận thưởng PP; cột chi/finish nếu chọn được tách khỏi tổng programme.\n\n"
    report += f"Đã tạo {len(rows)} hàng, {sum(row['eligible'] for row in rows)} hàng hợp lệ. Tất cả k=20/40/60 và r=0.5/1.0/1.5.\n\n"
    report += "## Mục không đổi\n\nMục 1, 2, 6.1–6.3, danh mục node/cost/loại trừ, 7 trừ hai cửa sổ và tham chiếu timer, 8.2, toàn mục 9 (bao gồm ID và số dòng), 11.2 và dòng BLUF. Không sửa game file, history, localisation hoặc báo cáo Trung Quốc.\n\n"
    report += "Đối chiếu trực tiếp bản đầu vào đã đọc xác nhận 6.1/6.2/6.3/8.2/11.2 giữ nguyên văn và danh sách tham chiếu repo không đổi. Script kiểm hash mục1/2/9, cost của74node và ba bảng ngày/lịch/E102×E103 khớp B1 mỗi lần chạy.\n\n"
    report += "## Cần người dùng quyết định\n\nCheckpoint và ngoại lệ C+B/C đã được chốt, không hỏi lại. Còn I3: khi đã chọn E102-C, E103-C luôn rẻ nhất trong ba lựa chọn (15 so A bị bác mất6cohesion quy đổi18, B30); C cũng trội B trong các chỉ số đã mô hình. Có thể chốt hệ quả cụ thể của hợp đồng được chấp nhận hoặc chấp nhận B là lựa chọn tình huống ngoài các chỉ số này; chưa tự thêm thưởng hay đổi giá. Còn I5 ở cohesion<20: chuẩn kiểm tra750+60=810, dự phòng90<100, không thuộc ngoại lệ E102-C+B/C được phép. Có thể giới hạn I5 cho snapshot hoặc chốt xử lý phase chuẩn bị; chưa chọn thay bạn. E101 không cộng vào ma trận vì caller F05 riêng; các node chưa viết và API/idea chưa có game file vẫn cần lượt2/3.\n\nBLUF\n"
    if parsed.apply_l1:
        apply_l1(data, p, table, core, gaps, rows, combo_rows)
    if parsed.sync_confirmed:
        sync_confirmed(p,rows,full_exception_table,late_full_table,checkpoint_rows,package_differences)
    document = DOC.read_text(encoding="utf-8")
    if "VIETNAM_POLITICAL_PARAMETERS_VI.json" in document:
        assert table(['Programme','Chuẩn tập thể/cân bằng','Chuẩn tập trung','Mốc sớm','Cấp tốc'],core) in document, "Bảng ngày trong tài liệu lệch B1/CSV"
        assert table(['Nhiệm kỳ','Ngày còn cách chuẩn bị kỳ sau'],gaps) in document, "Bảng lịch trong tài liệu lệch B1"
        assert table(['Tuyến','Mode','E102','E103','Ngày full tiềm năng','Programme','Hợp đồng','Dự phòng'],[row for row in combo_rows if row[0] != 'balanced']) in document, "Bảng E102×E103 lệch B1"
        for number in ["1","2","9"]:
            block = re.search(rf"^## {number}\..*?(?=^## |\Z)",document,re.M|re.S).group(0)
            assert hashlib.sha256(block.encode()).hexdigest() == data["baseline_sections"][number], f"Mục {number} đã đổi ngoài phạm vi"
        assert document.rstrip().endswith("BLUF")
        actual_costs = {node:int(cost) for node,cost in re.findall(r"^\| ((?:F|IX|X|XI|XII|XIII|XIV)\d\d)(?: `[^`]+`)? \| [^|]+ \| (\d+) \|",document,re.M)}
        assert actual_costs == {node: row["cost"] for node,row in p["focus_nodes"].items()}, "Node/cost lệch đầu vào B1"
    report = report.replace("\n\nBLUF\n", "\n\n## Changelog lượt 1\n\n" + changelog(p) + "\n\nGiữ74node, deadline900, gói55PP/thưởng50PP và mọi giá khác. k chỉ là tham số kiểm tra; không dùng để đổi định nghĩa I2. Chưa triển khai engine/playtest.\n\nBLUF\n")
    REPORT.write_text(report,encoding="utf-8")
    print(json.dumps({"rows":len(rows),"eligible_rows":sum(row["eligible"] for row in rows),"nodes":len(p["focus_nodes"]),"min_calendar_gap":min(gap for _,gap in gaps),"universal_dominators":len(winners),"checks":checks}, ensure_ascii=True,indent=2))


if __name__ == "__main__":
    run()
