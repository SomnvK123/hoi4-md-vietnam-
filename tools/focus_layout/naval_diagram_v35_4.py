"""Export live naval layout and its manifest using Pillow and registered DDS icons.

Run from anywhere: python tools/focus_layout/naval_diagram_v35_4.py
This diagram represents file coordinates, not the HOI4 renderer or runtime.
"""
from pathlib import Path
import functools
import json
import re
import runpy
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'.claude/docs/naval'
ns=runpy.run_path(str(ROOT/'tools/audit/naval_scenarios.py'))
FOCUSES,value,values=ns['FOCUSES'],ns['value'],ns['values']
titles={}
for path in (ROOT/'localisation/english/replace').glob('*.yml'):
    titles.update(re.findall(r'^\s*(VIE_nav35_\w+):\d+\s+"([^"\n]+)"',path.read_text(encoding='utf-8-sig'),re.M))
sprites={}
for path in (ROOT/'interface').glob('*.gfx'):
    for block in re.findall(r'spriteType\s*=\s*\{([^}]+)\}',path.read_text(encoding='utf-8-sig')):
        name=re.search(r'name\s*=\s*"([^"\n]+)"',block)
        texture=re.search(r'texturefile\s*=\s*"([^"\n]+)"',block)
        if name and texture:sprites[name[1]]=ROOT/texture[1]

@functools.lru_cache(None)
def pos(fid):
    b=FOCUSES[fid];parent=value(b,'relative_position_id')
    px,py=pos(parent) if parent else (0,0)
    return px+int(value(b,'x',0)),py+int(value(b,'y',0))

def font(size,bold=False):
    candidates=[Path('C:/Windows/Fonts')/('segoeuib.ttf' if bold else 'segoeui.ttf'),Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
    for p in candidates:
        if p.exists():return ImageFont.truetype(str(p),size)
    raise RuntimeError('A Unicode font is required for Vietnamese labels.')

def render(ids,name,title):
    x0=min(pos(fid)[0] for fid in ids);x1=max(pos(fid)[0] for fid in ids)
    y0=min(pos(fid)[1] for fid in ids);y1=max(pos(fid)[1] for fid in ids)
    unitx,unity,margin,header=112,250,130,165
    image=Image.new('RGB',((x1-x0)*unitx+margin*2,(y1-y0)*unity+header+290),'#101b24')
    draw=ImageDraw.Draw(image)
    draw.text((35,25),title,font=font(30,True),fill='#edf5f8')
    draw.text((35,76),'Tọa độ live • Mỗi hướng: hai cột → hội tụ AND • Capstone có gate lực lượng',font=font(18),fill='#a9c1cd')
    draw.text((35,108),'Xanh: prerequisite AND    Vàng nét đứt: OR    Đỏ nét đứt: mutex    Ảnh tham chiếu; chưa kiểm trong game',font=font(16),fill='#a9c1cd')
    xy={fid:((pos(fid)[0]-x0)*unitx+margin,(pos(fid)[1]-y0)*unity+header) for fid in ids}
    def dashed(points,fill,width=2):
        for (ax,ay),(bx,by) in zip(points,points[1:]):
            distance=((bx-ax)**2+(by-ay)**2)**.5
            for start in range(0,int(distance),12):
                stop=min(start+6,distance)
                if distance:draw.line((ax+(bx-ax)*start/distance,ay+(by-ay)*start/distance,ax+(bx-ax)*stop/distance,ay+(by-ay)*stop/distance),fill=fill,width=width)
    for fid in ids:
        x,y=xy[fid]
        for group in values(FOCUSES[fid],'prerequisite'):
            parents=values(group,'focus')
            for parent in parents:
                if parent not in xy:continue
                px,py=xy[parent];mid=y-24
                points=[(px,py+202),(px,mid),(x,mid),(x,y)]
                if len(parents)>1:dashed(points,'#d6b45f')
                else:draw.line(points,fill='#76b5c8',width=3)
        for group in values(FOCUSES[fid],'mutually_exclusive'):
            for other in values(group,'focus'):
                if other not in xy or fid>=other:continue
                ox,oy=xy[other];lane=max(y,oy)+218
                dashed([(x,y+202),(x,lane),(ox,lane),(ox,oy+202)],'#b56868')
    bodyfont=font(14);codefont=font(17,True)
    manifest=[]
    for fid in ids:
        x,y=xy[fid];code=fid.removeprefix('VIE_nav35_')
        colour='#76b49c' if code.startswith('G') else '#76a8d0' if code.startswith('B') else '#b9c6ce'
        draw.rounded_rectangle((x-96,y,x+96,y+202),radius=12,fill='#1b2d39',outline=colour,width=2)
        draw.text((x-84,y+9),code,font=codefont,fill=colour)
        cost=value(FOCUSES[fid],'cost','10')
        draw.text((x+38,y+11),f'{int(cost)*10} ngày',font=font(12),fill='#b0c0c8')
        path=sprites[value(FOCUSES[fid],'icon')]
        icon=Image.open(path).convert('RGBA')
        if icon.size!=(93,91):raise ValueError(f'Unexpected focus texture size: {path}: {icon.size}')
        image.paste(icon,(x-46,y+33),icon)
        wrapped=[];current=''
        for word in titles[fid].split():
            candidate=(current+' '+word).strip()
            if draw.textlength(candidate,font=bodyfont)>180 and current:wrapped.append(current);current=word
            else:current=candidate
        if current:wrapped.append(current)
        if len(wrapped)>4:raise ValueError(f'Title too tall: {fid}')
        for row,text in enumerate(wrapped):
            draw.text((x-draw.textlength(text,font=bodyfont)/2,y+128+row*17),text,font=bodyfont,fill='#e5eff5')
        external=[parent.removeprefix('VIE_nav35_') for group in values(FOCUSES[fid],'prerequisite') for parent in values(group,'focus') if parent not in xy]
        if external:
            draw.text((x-85,y+184),'Ngoài khung: '+', '.join(external),font=font(10),fill='#d6b45f')
        manifest.append(dict(id=fid,title=titles[fid],absolute=list(pos(fid)),anchor=value(FOCUSES[fid],'relative_position_id'),prerequisite=[values(g,'focus') for g in values(FOCUSES[fid],'prerequisite')],cost=int(cost)))
    draw.text((35,image.height-48),'V35.4 • Nguồn: common/national_focus/VIE_md_focus.txt • Icon DDS gốc 93×91 px',font=font(16),fill='#a9c1cd')
    OUT.mkdir(parents=True,exist_ok=True)
    path=OUT/(name+'.png');image.save(path)
    (OUT/(name+'.json')).write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'{path.relative_to(ROOT)}: {image.width}x{image.height}, {len(ids)} focuses')

if __name__=='__main__':
    ids=[fid for fid in FOCUSES if fid.startswith('VIE_nav35_')]
    render(ids,'naval_v35_4','CÂY FOCUS HẢI QUÂN — 47 FOCUS / LAYOUT V47')
    subset=['VIE_nav35_'+code for code in ('H02','P06','G00','B00','G01','G04','G02','G05','G03','B01','B04','B02','B05','B03','F01','F02')]
    render(subset,'green_blue_v35_4','GREENWATER / BLUEWATER — ROOT, HAI NHÁNH, CAPSTONE')
