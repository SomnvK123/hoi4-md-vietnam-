"""Export air v19 diagrams, uncompressed drawio and actual before/after relations.

Rendering helpers follow industry_diagram's static diagram convention. Does not
modify gameplay; these routes cannot establish how HOI4 draws focus links.
"""
from pathlib import Path
import json, re, sys, subprocess
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'audit'))
from industry import ROOT, focus_map, groups, positions, value, values, walk
OUT=ROOT/'.claude/docs/air'
COLORS={'Nền tảng lực lượng':'#a5bac9','Ưu tiên ngân sách':'#c4a165','Cơ cấu tác chiến':'#d59369','Phòng không':'#8ca7d9','Đa nhiệm':'#75b3c7','UAV / dữ liệu':'#86b8a2','Công nghiệp bảo đảm':'#b092c4','Hiệp đồng':'#ddd6b0'}
def category(fid):
    if fid.startswith('VIE_apm_'):return 'Công nghiệp bảo đảm'
    if '_priority_' in fid:return 'Ưu tiên ngân sách'
    if '_structure_' in fid:return 'Cơ cấu tác chiến'
    if fid=='VIE_airf_integrated_force':return 'Hiệp đồng'
    if fid in ['VIE_airf_iads','VIE_airf_layered_defence','VIE_airf_ew_antistealth','VIE_airf_iads_command']:return 'Phòng không'
    if fid in ['VIE_airf_multirole','VIE_airf_multirole_fleet','VIE_airf_sustainment','VIE_airf_airlift_tanker','VIE_airf_multirole_wing']:return 'Đa nhiệm'
    if fid in ['VIE_airf_unmanned','VIE_airf_isr_uav','VIE_airf_datalink','VIE_airf_strike_uav','VIE_airf_teaming']:return 'UAV / dữ liệu'
    return 'Nền tảng lực lượng'
def labels(before=False):
    result={}
    for p in sorted((ROOT/'localisation/english').glob('*.yml'))+sorted((ROOT/'localisation/english/replace').glob('*.yml')):
        if before:
            proc=subprocess.run(['git','show','HEAD:'+p.relative_to(ROOT).as_posix()],cwd=ROOT,capture_output=True)
            if proc.returncode:continue
            text=proc.stdout.decode('utf-8-sig')
        else:text=p.read_text(encoding='utf-8-sig')
        result.update({m[1]:m[2] for m in re.finditer(r'^ ([\w.]+):\d "(.*)"',text,re.M)})
    return result

def geometry(graph):
    height = max(n['y'] for n in graph.values()) * 150 + 270
    coords = {f: ((n['x'] - 214) * 112 + 150, n['y'] * 150 + 120) for f, n in graph.items()}
    return 2540, height, coords


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
    legend={k:v for k,v in COLORS.items() if any(category(f)==k for f in graph)}
    for i, (name, color) in enumerate(legend.items()):
        x = 42 + (i % 5) * 405; y = 107 + (i // 5) * 32
        d.rectangle((x, y+4, x+16, y+20), fill=color)
        d.text((x+24, y), name, font=font(18), fill='#d4dce5')
    if len(graph) == 33:
        # These bands describe actual y ranges; they do not emulate in-game GUI.
        d.rounded_rectangle((24,335,2520,480),radius=12,fill='#1b2833',outline='#486071',width=2)
        d.text((42,345),'Root Phòng không–Không quân chung',font=font(20,True),fill='#d4e2ec')
        for first,last,label in [(3,5,'1. Nền tảng và củng cố lực lượng'),(7,7,'2. Một lựa chọn cơ cấu tác chiến'),(9,11,'3. Chỉ huy, dữ liệu và vận tải'),(12,14,'4. Chuyên ngành: mở ngang, hội tụ dưới'),(16,16,'5. Hội tụ lực lượng hiệp đồng')]:
            top=first*150+120-85; bottom=last*150+120+60
            d.rounded_rectangle((24,top,1818,bottom),radius=12,fill='#15212b',outline='#2c3c49',width=2)
            d.text((42,top+10),label,font=font(20,True),fill='#b9cbd9')
        for first,last,label in [(3,4,'1. Thể chế và các trụ kỹ thuật'),(6,6,'2. Tích hợp và UAV'),(8,8,'3. Công nghiệp trưởng thành')]:
            top=first*150+120-85; bottom=last*150+120+60
            d.rounded_rectangle((1830,top,2520,bottom),radius=12,fill='#211d2c',outline='#483951',width=2)
            d.text((1846,top+10),label,font=font(18,True),fill='#c8b6d6')
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
        short = {'VIE_apm_integration':'Cần 2/3 trụ A32–A31–radar', 'VIE_apm_mature':'Tích hợp 2 + 3/4 trụ bậc 2','VIE_airf_integrated_force':'D4 + công nghiệp + 2/3 đích'}.get(f,short)
        if len(short)>29: short=short[:27]+'…'
        d.text((x,y+28),short,font=font(11),fill='#a6b8c8',anchor='mt')
    d.text((42,h-65), f"{len(graph)} focus • x = 214…234 • {max(n['y'] for n in graph.values())} hàng • tọa độ lấy từ file focus",font=font(18),fill='#b5c4d2')
    if len(graph) == 33:
        d.text((42,h-36), 'Một root chung; lực lượng x214–228 / công nghiệp x230–234. Chỉ một hàng mutex; giá theo lựa chọn từng chương trình.',font=font(18),fill='#d4dce5')
    canvas.save(path)


def xml_page(mxfile, graph, names, title):
    w,h,coords = geometry(graph)
    diagram=ET.SubElement(mxfile,'diagram',{'id':title.replace(' ','_'),'name':title})
    model=ET.SubElement(diagram,'mxGraphModel',{'dx':str(w),'dy':str(h),'grid':'1','gridSize':'10','page':'1','pageWidth':str(w),'pageHeight':str(h)})
    root=ET.SubElement(model,'root')
    ET.SubElement(root,'mxCell',{'id':'0'})
    ET.SubElement(root,'mxCell',{'id':'1','parent':'0'})
    for f,(x,y) in coords.items():
        label=names.get(f,f)
        label += {'VIE_apm_integration':' (2/3 trụ; ba nhóm OR kết hợp AND)', 'VIE_apm_mature':' (tích hợp bậc 2 + 3/4 trụ)', 'VIE_airf_integrated_force':' (D4 + công nghiệp + 2/3 đích)'}.get(f,'')
        cell=ET.SubElement(root,'mxCell',{'id':f,'value':label,'style':f'rounded=0;whiteSpace=wrap;html=0;fillColor=#f6f8fa;strokeColor={COLORS[category(f)]};fontSize=16;','vertex':'1','parent':'1'})
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
    before=json.loads((OUT/'air_v18_before.json').read_text(encoding='utf-8'))
    f=focus_map((ROOT/'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8'));xy=positions(f)
    after={fid:dict(x=xy[fid][0],y=xy[fid][1],pre=groups(b),ex=values(value(b,'mutually_exclusive',[]),'focus')) for fid,b in f.items() if fid.startswith(('VIE_airf_','VIE_apm_'))}
    after=dict(sorted(after.items(),key=lambda p:(p[1]['y'],p[1]['x'])))
    (OUT/'air_after.json').write_text(json.dumps(after,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    mxfile=ET.Element('mxfile',{'host':'app.diagrams.net','compressed':'false'})
    before_names={fid:n['label'] for fid,n in before.items()} if all('label' in n for n in before.values()) else labels(True)
    draw(after,labels(),'PK-KQ v19: củng cố → định hướng → năng lực song song',OUT/'air_after.png')
    xml_page(mxfile,before,before_names,'Trước v19: 36 focus, hai hàng lựa chọn')
    xml_page(mxfile,after,labels(),'Sau v19: 33 focus, một hàng lựa chọn')
    ET.indent(mxfile);ET.ElementTree(mxfile).write(OUT/'air_redesign.drawio',encoding='utf-8',xml_declaration=True)
    changes=['# Quan hệ và reward trước/sau v19','','Bản cuối có 33 focus: giữ 29 ID cũ, 3 cơ cấu tác chiến và 1 đích hiệp đồng. Bỏ ba focus ngân sách, giá theo lựa chọn từng chương trình và giảm giá lịch sử. Root chung nối hai cụm. D5 chọn rõ một mục tiêu đủ điều kiện, chỉ một lần.','','| Focus | Cha trước v19 | Cha sau v19 | Reward / điều kiện |','|---|---|---|---|']
    def parents(n):return ' AND '.join('('+' OR '.join(p.removeprefix('VIE_') for p in g)+')' for g in n['pre'])
    fx={k:v for k,_,v in __import__('industry').read('common/scripted_effects/VIE_md_effects_air_force.txt')}
    branch_codes=set('a1 a2 a3 a4 b1 b2 b3 b4 b5 c1 c2 c3 c4 c5'.split())
    for fid,n in after.items():
        old=before.get(fid);reward='Giữ reward; gate theo chương trình/bậc thực, năm chuyển sang AI'
        effect_names=[k for k,_,v in value(f[fid],'completion_reward',[]) if k in fx]
        if any(k.removeprefix('VIE_airf_').removesuffix('_reward') in branch_codes for k in effect_names):reward='Giữ modifier/XP/PP/CP/research của v18'
        if fid in ('VIE_airf_iads','VIE_airf_multirole','VIE_airf_unmanned'):reward+='; nhận bonus nghiên cứu chuyên ngành 25% ×1, chống lặp bonus legacy tương ứng'
        if '_structure_' in fid:reward='Giữ D4: −50 PP, −0,60 tỷ; thưởng sau 360 ngày; hàng mutex duy nhất'
        if fid=='VIE_airf_integrated_force':reward='Giữ +20 XP/mastery, +50 PP, +3% war support; công nghiệp + D4 + 2/3 đích'
        if fid=='VIE_apm_law':reward='Giữ reward; cụm công nghiệp mở trực tiếp từ root không quân'
        if fid=='VIE_apm_mature':reward='Giữ reward; tích hợp bậc 2 AND 3/4 trụ bậc 2; không bắt UAV'
        gates=', '.join(k for k,_,v in value(f[fid],'available',[]))
        changes.append(f"| `{fid}` | {parents(old) if old else 'Mới'} | {parents(n)} | {reward}"+(f"; `{gates}`" if gates else '')+" |")
    for fid in sorted(set(before)-set(after)):
        changes.append(f'| `{fid}` | {parents(before[fid])} | Đã bỏ | Bỏ hệ số giá toàn nhánh; bonus chuyển sang lối vào chuyên ngành tương ứng |')
    changes+=['','D1–D3 và D4 giữ thưởng/PP/thời lượng. D5 có ba decision đích, dùng chung guard một lần: 60 PP, 1 tỷ, 548 ngày, thưởng 0,5/1 điểm phần trăm. Giá cơ sở và giảm giá lịch sử của chương trình giữ nguyên. Xem [thiết kế](../../../VIE_air_force_documentation.md) và [kiểm định](validation.md).']
    (OUT/'air_changes.md').write_text('\n'.join(changes)+'\n',encoding='utf-8')
    print('Exported 36/33 uncompressed before-after drawio, v19 PNG and actual relation/reward changes; frozen v18 preview preserved.')
if __name__=='__main__':main()
