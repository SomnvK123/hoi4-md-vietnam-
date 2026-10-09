"""Render the current land-force branch from live focus coordinates and gates."""
from pathlib import Path
import json
import re
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'audit'))
from industry import ROOT, focus_map, groups, positions, value, values

FOCUS_FILE = ROOT / 'common/national_focus/VIE_md_focus.txt'
LOC_DIR = ROOT / 'localisation/english'
OUT = ROOT / '.claude/docs/land/land_focus_current.png'
PREFIX = 'VIE_lf_'
CARD_W, CARD_H = 194, 92
ROW_H = 148
TOP = 310
LEFT = 250
X_STEP = 50
COLORS = {
    'base': '#a6b7c7', 'arms': '#7cae91', 'structure': '#c1a16b',
    'choice': '#bd8585', 'capability': '#8fa4cc', 'end': '#b18cc5',
}
SPEC = json.loads((ROOT / '.claude/docs/land/structure_v29.json').read_text(encoding='utf-8'))
PATH_COLORS = {'regular': '#72b2d0', 'mobile': '#79b69b', 'depth': '#c2a667'}
PATH_NODES = {'VIE_lf_'+n[0]: PATH_COLORS[p['flag']] for p in SPEC['paths'] for n in p['nodes']}


def node_color(fid):
    if fid in PATH_NODES:
        return PATH_NODES[fid]
    if fid in {'VIE_lf_army_reform', 'VIE_lf_logistics_merge', 'VIE_lf_basic_training'}:
        return COLORS['base']
    if any(s in fid for s in ('arm_infantry', 'arm_armor', 'arm_arty', 'arm_engineer', 'combined_arms')):
        return COLORS['arms']
    if any(s in fid for s in ('fs_', 'dev_', 'command_reform_1', 'command_reform_2')):
        return COLORS['choice'] if any(s in fid for s in ('fs_mobile_force', 'fs_main_corps', 'fs_depth_defence', 'dev_')) else COLORS['structure']
    if any(s in fid for s in ('cap_', 'selective_modernization')):
        return COLORS['capability']
    if fid in {'VIE_lf_command_reform_3', 'VIE_lf_force_complete'}:
        return COLORS['end']
    return COLORS['structure']


def labels():
    result = {}
    for p in sorted(LOC_DIR.glob('*.yml')) + sorted((LOC_DIR / 'replace').glob('*.yml')):
        text = p.read_text(encoding='utf-8-sig')
        for m in re.finditer(r'^ ([\w.]+):\d "(.*)"', text, re.M):
            result[m[1]] = m[2]
    return result


def main():
    focuses = focus_map(FOCUS_FILE.read_text(encoding='utf-8'))
    land = {fid: node for fid, node in focuses.items() if fid.startswith(PREFIX)}
    pos = positions(focuses)
    names = labels()
    min_x = min(pos[f][0] for f in land)
    max_x = max(pos[f][0] for f in land)
    max_y = max(pos[f][1] for f in land)
    width = (max_x - min_x) * X_STEP + LEFT * 2 + CARD_W
    height = TOP + max_y * ROW_H + 135
    canvas = Image.new('RGB', (width, height), '#111a22')
    draw = ImageDraw.Draw(canvas)
    font_regular = Path('C:/Windows/Fonts/arial.ttf')
    font_bold = Path('C:/Windows/Fonts/arialbd.ttf')
    if not font_regular.exists():
        font_regular = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
        font_bold = font_regular.with_name('DejaVuSans-Bold.ttf')

    def font(size, bold=False):
        path = font_bold if bold else font_regular
        return ImageFont.truetype(str(path), size) if path.exists() else ImageFont.load_default(size=size)

    coords = {fid: (LEFT + (pos[fid][0] - min_x) * X_STEP, TOP + pos[fid][1] * ROW_H) for fid in land}
    draw.text((44, 26), 'CÂY FOCUS LỤC QUÂN • XÂY DỰNG LỰC LƯỢNG (TRỤC 3)', font=font(30, True), fill='#f1f5f9')
    draw.text((44, 70), f'{len(land)} focus hiện hành • mỗi hướng có một hàng ngang 3 focus rồi kết thúc bằng một focus hoàn thiện', font=font(17), fill='#bdcbd6')
    draw.text((44, 104), 'Mũi tên liền: prerequisite bắt buộc  |  Nét đứt: OR trong cùng khối prerequisite  |  Đỏ đôi: mutually_exclusive', font=font(16), fill='#bdcbd6')
    legend = [('Nền tảng', 'base'), ('Binh chủng', 'arms'), ('Năng lực tiếp theo', 'capability'),
              ('Cơ giới hóa', 'regular'), ('Cơ động nhẹ', 'mobile'), ('Địa phương và dự bị', 'depth')]
    for i, (label, color) in enumerate(legend):
        x = 46 + (i % 3) * 400
        y = 143 + (i // 3) * 29
        draw.rounded_rectangle((x, y + 4, x + 18, y + 22), radius=3, fill=(COLORS | PATH_COLORS)[color])
        draw.text((x + 26, y), label, font=font(15), fill='#d6e0e7')

    row_labels = {
        2: '01  NỀN TẢNG', 3: '02  HẬU CẦN + ĐÀO TẠO', 4: '03  TỔ CHỨC BINH CHỦNG',
        5: '04  HUẤN LUYỆN BINH CHỦNG', 6: '05  HỢP ĐỒNG BINH CHỦNG',
        7: '06  CHUẨN HÓA THAM MƯU', 8: '07  CHỌN MỘT HƯỚNG ƯU TIÊN',
        9: '08  BA DỰ ÁN SONG SONG TRONG HƯỚNG ĐÃ CHỌN', 10: '09  HOÀN THIỆN HƯỚNG (CẦN ĐỦ CẢ BA)',
        11: '10  CẢI CÁCH CHỈ HUY II', 12: '11  LĨNH VỰC NĂNG LỰC',
        13: '12  PHÁT TRIỂN CHUYÊN NGÀNH', 14: '13  HIỆN ĐẠI HÓA CHỌN LỌC',
        15: '14  CHỈ HUY SỐ', 16: '15  HOÀN THÀNH',
    }
    for y, label in row_labels.items():
        yy = TOP + y * ROW_H
        draw.line((35, yy - CARD_H // 2 - 18, width - 35, yy - CARD_H // 2 - 18), fill='#273541', width=1)
        draw.text((42, yy - CARD_H // 2 - 15), label, font=font(12, True), fill='#8799a7')

    # The shared military root is a prerequisite outside this land-force cluster.
    root = 'VIE_lf_army_reform'
    rx, ry = coords[root]
    draw.rounded_rectangle((rx - 190, TOP - 105, rx + 190, TOP - 47), radius=8, fill='#26333e', outline='#a6b7c7', width=2)
    draw.text((rx, TOP - 94), 'Tiền đề ngoài nhánh: VIE_modernize_vpa', font=font(15, True), fill='#f2f5f7', anchor='mt')
    draw.line((rx, TOP - 47, rx, ry - CARD_H // 2), fill='#b5c5d3', width=3)
    draw.polygon([(rx, ry - CARD_H // 2), (rx - 6, ry - CARD_H // 2 - 10), (rx + 6, ry - CARD_H // 2 - 10)], fill='#b5c5d3')

    # Draw live prerequisite edges; separate prerequisite blocks remain separate AND requirements.
    for fid, node in land.items():
        for group in groups(node):
            kind = 'or' if len(group) > 1 else 'and'
            for parent in group:
                if parent not in land:
                    continue
                x1, y1 = coords[parent]
                x2, y2 = coords[fid]
                color = '#d1bd8b' if kind == 'or' else '#b5c5d3'
                if y2 > y1:
                    mid = (y1 + y2) // 2
                    points = [(x1, y1 + CARD_H // 2), (x1, mid), (x2, mid), (x2, y2 - CARD_H // 2)]
                else:
                    side = 1 if x2 >= x1 else -1
                    lane = (x1 + x2) // 2
                    points = [(x1 + side * CARD_W // 2, y1), (lane, y1), (lane, y2), (x2 - side * CARD_W // 2, y2)]
                if kind == 'and':
                    draw.line(points, fill=color, width=3)
                else:
                    for a, b in zip(points, points[1:]):
                        dx, dy = b[0] - a[0], b[1] - a[1]
                        length = max(abs(dx), abs(dy), 1)
                        for start in range(0, length, 18):
                            end = min(start + 10, length)
                            draw.line((a[0] + dx * start / length, a[1] + dy * start / length,
                                       a[0] + dx * end / length, a[1] + dy * end / length), fill=color, width=3)
                if kind == 'and':
                    ex, ey = points[-1]
                    draw.polygon([(ex, ey), (ex - 6, ey - 10), (ex + 6, ey - 10)], fill=color)

    # Mutual exclusions are undirected and symmetric in the source; render each pair once.
    mutex = set()
    for fid, node in land.items():
        for other in values(value(node, 'mutually_exclusive', []), 'focus'):
            if other in land:
                mutex.add(tuple(sorted((fid, other))))
    for a, b in sorted(mutex):
        x1, y1 = coords[a]
        x2, y2 = coords[b]
        draw.line((x1, y1 - 4, x2, y2 - 4), fill='#d97b7b', width=2)
        draw.line((x1, y1 + 4, x2, y2 + 4), fill='#d97b7b', width=2)

    gates = {
        'VIE_lf_army_reform': 'Gate: VIE_lf_gate_open',
        'VIE_lf_arm_infantry_org': 'Gate: VIE_lf_arm_slot_free',
        'VIE_lf_arm_armor_org': 'Gate: VIE_lf_arm_slot_free',
        'VIE_lf_arm_arty_org': 'Gate: VIE_lf_arm_slot_free',
        'VIE_lf_arm_engineers': 'Gate: VIE_lf_arm_slot_free',
        'VIE_lf_combined_arms': 'Gate: VIE_lf_arm_done_3',
        'VIE_lf_cap_border_urban': 'Gate: VIE_lf_cap_slot_free',
        'VIE_lf_cap_army_ad': 'Gate: VIE_lf_cap_slot_free',
        'VIE_lf_cap_cyber_ew': 'Gate: VIE_lf_cap_slot_free',
        'VIE_lf_selective_modernization': 'Gate: VIE_lf_cap_done_2',
    }
    for fid, (x, y) in coords.items():
        color = node_color(fid)
        draw.rounded_rectangle((x - CARD_W // 2, y - CARD_H // 2, x + CARD_W // 2, y + CARD_H // 2),
                               radius=10, fill='#202d38', outline=color, width=3)
        title = names.get(fid, fid)
        title = re.sub(r'\\n', ' ', title)
        words, lines, line = title.split(), [], ''
        for word in words:
            trial = (line + ' ' + word).strip()
            if line and draw.textlength(trial, font=font(15, True)) > CARD_W - 18:
                lines.append(line); line = word
            else:
                line = trial
        if line: lines.append(line)
        start = y - CARD_H // 2 + 8
        for i, text in enumerate(lines[:3]):
            draw.text((x, start + i * 19), text, font=font(15, True), fill='#f2f5f7', anchor='mt')
        short = fid.removeprefix(PREFIX)
        draw.text((x, y + 17), short, font=font(10), fill='#a6b8c8', anchor='mt')
        if fid in gates:
            draw.text((x, y + 31), gates[fid], font=font(9, True), fill='#e4c77e', anchor='mt')

    foot = 'Chọn 1 hướng → hoàn thành 3 dự án nằm ngang → focus cuối yêu cầu đủ cả 3 → Cải cách chỉ huy II. Năng lực tiếp theo giữ gate 2/3.'
    draw.text((42, height - 82), foot, font=font(14), fill='#d6e0e7')
    draw.text((42, height - 52), f'{len(land)} focus • x={min_x}–{max_x}, y=2–{max_y} • sơ đồ tĩnh đọc từ code; gate available là điều kiện bổ sung', font=font(14), fill='#9fb0bd')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT)
    print(f'Exported {len(land)} live land-force focuses to {OUT} ({width}x{height}); {len(mutex)} mutex pairs.')


if __name__ == '__main__':
    main()
