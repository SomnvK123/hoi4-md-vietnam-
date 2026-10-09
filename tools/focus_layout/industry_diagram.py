"""Export the industry's before/after diagrams without modifying gameplay files.

Python 3.10+, Pillow. XML is uncompressed and uses rectangles, dashed OR arrows,
and one shape=link edge per mutually exclusive pair. Paths avoid focus rectangles;
the preview is a design diagram, not a screenshot of HOI4's connection renderer.
"""
from pathlib import Path
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'audit'))
from industry import ROOT, branch_ids, focus_map, groups, positions, value, values

OUT = ROOT / '.claude/docs/industry'
COLORS = {'Đóng tàu': '#5696b1', 'Dệt may': '#73aa8e', 'Thép': '#b29173',
          'Chuỗi cung ứng': '#849ccd', 'Điện tử / FDI': '#a48ac1',
          'Bán dẫn': '#6caca9', 'Ô tô': '#b99c66', 'Chính sách': '#b48486', 'Nền tảng': '#cccccc'}


def category(fid):
    if any(s in fid for s in ('shipbuilding', 'vinashin', 'offshore_wind_fabrication')): return 'Đóng tàu'
    if any(s in fid for s in ('textile', 'yarn_forward')): return 'Dệt may'
    if any(s in fid for s in ('hoa_phat', 'formosa_steel', 'national_steel')): return 'Thép'
    if any(s in fid for s in ('chip_', 'semiconductor', 'osat', 'intel_')): return 'Bán dẫn'
    if any(s in fid for s in ('automotive', 'auto_', 'ev_revolution')): return 'Ô tô'
    if any(s in fid for s in ('nq23', 'nq29', 'eco_industrial', 'investment_support', 'industrial_productivity', 'modern_industrial')): return 'Chính sách'
    if any(s in fid for s in ('samsung', 'china_plus', 'fdi_', 'apple_', 'electronics_', 'manufacturing_hub')): return 'Điện tử / FDI'
    if 'industrialization_strategy' in fid: return 'Nền tảng'
    return 'Chuỗi cung ứng'


def labels(before=False):
    result = {}
    files = sorted((ROOT / 'localisation/english').glob('*.yml')) + sorted((ROOT / 'localisation/english/replace').glob('*.yml'))
    for p in files:
        if before:
            run = subprocess.run(['git', 'show', 'HEAD:' + p.relative_to(ROOT).as_posix()], cwd=ROOT, capture_output=True)
            if run.returncode: continue
            text = run.stdout.decode('utf-8-sig')
        else:
            text = p.read_text(encoding='utf-8-sig')
        for m in re.finditer(r'^ ([\w.]+):\d "(.*)"', text, re.M):
            result[m[1]] = m[2]
    return result


def geometry(graph):
    height = max(n['y'] for n in graph.values()) * 150 + 270
    coords = {f: ((n['x'] - min(v['x'] for v in graph.values())) * 112 + 150, n['y'] * 150 + 120) for f, n in graph.items()}
    return max(2100, int((max(v['x'] for v in graph.values())-min(v['x'] for v in graph.values()))*112+300)), height, coords


def edges(graph):
    for f, n in graph.items():
        for g in n['pre']:
            for p in g:
                if p in graph:
                    yield p, f, 'or' if len(g) > 1 else 'and'
        for q in n.get('ex', []):
            if q in graph and f < q:
                yield f, q, 'mutex'


def route(p, f, kind, coords):
    px, py = coords[p]
    x, y = coords[f]
    if kind == 'mutex':
        return [(px + 96, py), (x - 96, y)]
    if y <= py:
        return [(px, py + 44), (px, py + 69), (x, py + 69), (x, y + 44)]
    if y - py <= 150:
        return [(px, py + 44), (px, py + 75), (x, py + 75), (x, y - 44)]
    # Take an empty corridor beside a column instead of running through nodes.
    corridor = x + (103 if x >= px else -103)
    return [(px, py + 44), (px, py + 72), (corridor, py + 72),
            (corridor, y - 65), (x, y - 65), (x, y - 44)]


def draw(graph, names, title, path):
    from PIL import Image, ImageDraw, ImageFont
    w, h, coords = geometry(graph)
    canvas = Image.new('RGB', (w, h), '#101820')
    d = ImageDraw.Draw(canvas)
    regular = Path('C:/Windows/Fonts/arial.ttf')
    bold = Path('C:/Windows/Fonts/arialbd.ttf')
    if not regular.exists():
        regular = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
        bold = regular.with_name('DejaVuSans-Bold.ttf')
    def font(size, strong=False):
        p = bold if strong else regular
        return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default(size=size)
    d.text((42, 28), title, font=font(30, True), fill='#f1f5f9')
    d.text((42, 70), 'Liền: bắt buộc  |  Đứt: một trong các cha  |  Đỏ đôi: loại trừ nhau  |  Sơ đồ thiết kế, chưa xác nhận trong game', font=font(18), fill='#b5c4d2')
    for i, (name, color) in enumerate(COLORS.items()):
        x = 42 + (i % 5) * 405; y = 107 + (i // 5) * 32
        d.rectangle((x, y+4, x+16, y+20), fill=color)
        d.text((x+24, y), name, font=font(18), fill='#d4dce5')
    for p, f, kind in edges(graph):
        points = route(p, f, kind, coords)
        color = '#e8a5a5' if kind == 'mutex' else '#b5c5d3'
        if kind == 'or':
            for (x1,y1),(x2,y2) in zip(points, points[1:]):
                length = abs(x2-x1)+abs(y2-y1)
                for t in range(0, int(length), 15):
                    a = t/max(length,1); b = min(t+8,length)/max(length,1)
                    d.line((x1+(x2-x1)*a,y1+(y2-y1)*a,x1+(x2-x1)*b,y1+(y2-y1)*b),fill=color,width=2)
        elif kind == 'mutex':
            d.line([(x,y-3) for x,y in points],fill=color,width=2)
            d.line([(x,y+3) for x,y in points],fill=color,width=2)
        else:
            d.line(points,fill=color,width=2)
        if kind != 'mutex':
            x,y = points[-1]
            d.polygon([(x,y),(x-5,y-9),(x+5,y-9)],fill=color)
    for f, (x,y) in coords.items():
        cat = category(f)
        d.rounded_rectangle((x-96,y-44,x+96,y+44),radius=7,fill='#1f2b36',outline=COLORS[cat],width=2)
        title = names.get(f, f)
        for size in range(18, 11, -1):
            title_font = font(size, True)
            title_lines = []
            line = ''
            for word in title.split():
                trial = (line + ' ' + word).strip()
                if line and d.textlength(trial, font=title_font) > 176:
                    title_lines.append(line)
                    line = word
                else:
                    line = trial
            if line:
                title_lines.append(line)
            if len(title_lines) <= 3:
                break
        for j, line in enumerate(title_lines):
            d.text((x,y-34+j*21),line,font=title_font,fill='#f2f5f7',anchor='mt')
        short = f.removeprefix('VIE_')
        if len(short)>29: short=short[:27]+'…'
        d.text((x,y+28),short,font=font(11),fill='#a6b8c8',anchor='mt')
    d.text((42,h-65), f"{len(graph)} focus • x = {min(n['x'] for n in graph.values())}…{max(n['x'] for n in graph.values())} • {max(n['y'] for n in graph.values())} hàng • tọa độ lấy từ file focus",font=font(18),fill='#b5c4d2')
    if len(graph) == 39:
        d.text((42,h-36), 'Đích cuối: năng suất + ít nhất 45 điểm nội địa hóa + ít nhất 3/6 nhóm ngành; xem trạng thái từng nhóm trong hover.',font=font(18),fill='#d4dce5')
    canvas.save(path)


def xml_page(mxfile, graph, names, title):
    w,h,coords = geometry(graph)
    diagram=ET.SubElement(mxfile,'diagram',{'id':title.replace(' ','_'),'name':title})
    model=ET.SubElement(diagram,'mxGraphModel',{'dx':str(w),'dy':str(h),'grid':'1','gridSize':'10','page':'1','pageWidth':str(w),'pageHeight':str(h)})
    root=ET.SubElement(model,'root')
    ET.SubElement(root,'mxCell',{'id':'0'})
    ET.SubElement(root,'mxCell',{'id':'1','parent':'0'})
    for f,(x,y) in coords.items():
        cell=ET.SubElement(root,'mxCell',{'id':f,'value':names.get(f,f),'style':f'rounded=0;whiteSpace=wrap;html=0;fillColor=#f6f8fa;strokeColor={COLORS[category(f)]};fontSize=16;','vertex':'1','parent':'1'})
        ET.SubElement(cell,'mxGeometry',{'x':str(x-96),'y':str(y-44),'width':'192','height':'88','as':'geometry'})
    for i,(p,f,kind) in enumerate(edges(graph)):
        style='edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;exitX=0.5;exitY=1;entryX=0.5;entryY=0;endArrow=block;endFill=1;'
        if kind=='or':style+='dashed=1;'
        if kind=='mutex':style='shape=link;html=0;endArrow=none;startArrow=none;strokeColor=#b85450;exitX=1;exitY=0.5;entryX=0;entryY=0.5;'
        cell=ET.SubElement(root,'mxCell',{'id':f'e{i}','style':style,'edge':'1','parent':'1','source':p,'target':f})
        geo=ET.SubElement(cell,'mxGeometry',{'relative':'1','as':'geometry'})
        points=ET.SubElement(geo,'Array',{'as':'points'})
        for x,y in route(p,f,kind,coords)[1:-1]:ET.SubElement(points,'mxPoint',{'x':str(x),'y':str(y)})


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    before=json.loads((OUT/'industry_before.json').read_text(encoding='utf-8'))
    focuses=focus_map((ROOT/'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8'))
    pos=positions(focuses)
    after={f:dict(x=pos[f][0],y=pos[f][1],pre=groups(focuses[f]),icon=value(focuses[f],'icon'),ex=values(value(focuses[f],'mutually_exclusive',[]),'focus')) for f in branch_ids(focuses)}
    after=dict(sorted(after.items(),key=lambda q:(q[1]['y'],q[1]['x'])))
    (OUT/'industry_after.json').write_text(json.dumps(after,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    old_names=labels(True); names=labels()
    mxfile=ET.Element('mxfile',{'host':'app.diagrams.net','compressed':'false'})
    for graph,lookup,title,stem in [(before,old_names,'Công nghiệp trước sửa','before'),(after,names,'Công nghiệp sau sửa','after')]:
        draw(graph,lookup,title,OUT/f'industry_{stem}.png')
        xml_page(mxfile,graph,lookup,title)
    ET.indent(mxfile)
    ET.ElementTree(mxfile).write(OUT/'industry_redesign.drawio',encoding='utf-8',xml_declaration=True)
    changes=['# Quan hệ và reward trước/sau','', '| Focus | Cha trước | Cha sau | Thay đổi reward |','|---|---|---|---|']
    def parents(n):return ' AND '.join('('+' OR '.join(p.removeprefix('VIE_') for p in g)+')' for g in n['pre'])
    for f,n in after.items():
        old=before.get(f)
        reward='Giữ nguyên'
        if not old:reward='Focus chính sách mới; xem tài liệu thiết kế'
        elif f=='VIE_china_plus_one':reward='Bỏ lần gọi vie_ind.1; thưởng khác giữ nguyên'
        elif f=='VIE_semiconductor_fab':reward='Bổ sung 2 tỷ khi đã chọn ưu tiên thiết kế/đóng gói'
        changes.append(f"| `{f}` | {parents(old) if old else 'Mới'} | {parents(n)} | {reward} |")
    (OUT/'industry_changes.md').write_text('\n'.join(changes)+'\n',encoding='utf-8')
    print('Exported before/after PNGs, 2-page uncompressed drawio, manifests and change table to',OUT)


if __name__=='__main__':main()
