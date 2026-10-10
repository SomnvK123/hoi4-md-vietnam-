"""Render the live infrastructure graph and its captured pre-migration layout.

Reads actual coordinates/prerequisites. PNGs document layout, not HOI4 routing.
Usage: python tools/focus_layout/infrastructure_diagram.py
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'tools/audit'))
from industry import focus_map, positions, groups, values
from PIL import Image, ImageDraw, ImageFont

DOC = ROOT/'.claude/docs/infrastructure'


def render(pos, pre, titles, out, caption, mutex=(), compact=False):
    # Pillow is already required by repository DDS validation; no plotting runtime dependency.
    image=Image.new('RGB',(2600,1360),'#f4f6f8');draw=ImageDraw.Draw(image)
    ymax=11.8 if compact else 10.35
    def point(x,y):return (round(110+(x-63)*2380/38),round(110+(y-.2)*1140/(ymax-.2)))
    def font(size,bold=False):
        candidates=[Path('C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf'),
                    Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
        for path in candidates:
            if path.exists():return ImageFont.truetype(str(path),size)
        return ImageFont.load_default(size=size)
    def text(x,y,label,size=20,bold=False,color='#1e2d3c'):
        draw.multiline_text(point(x,y),label,font=font(size,bold),fill=color,anchor='mm',align='center',spacing=3)
    def line(points,color='#66788a',dashed=False,width=2):
        points=[point(x,y) for x,y in points]
        if not dashed:draw.line(points,fill=color,width=width);return
        for a,b in zip(points,points[1:]):
            length=max(abs(b[0]-a[0]),abs(b[1]-a[1]))
            if not length:continue
            for start in range(0,length,14):
                end=min(start+8,length)
                draw.line([(round(a[0]+(b[0]-a[0])*t/length),round(a[1]+(b[1]-a[1])*t/length)) for t in (start,end)],fill=color,width=width)
    for x,label,color in [(70,'ĐƯỜNG BỘ','#dcebf7'),(78,'ĐƯỜNG SẮT','#e4edf9'),
                          (86,'CẢNG BIỂN & LOGISTICS','#e0efe5'),(94,'HÀNG KHÔNG','#eee5f4')]:
        if not compact:
            draw.rectangle([point(x-3.9,1.7),point(x+3.9,7.5)],fill=color)
            text(x,1.55,label,size=19,bold=True,color='#34465b')
    for fid,(x,y) in pos.items():
        for group in pre.get(fid,[]):
            for parent in group:
                if parent not in pos:continue
                px,py=pos[parent];mid=(y+py)/2
                line([(px,py+.33),(px,mid),(x,mid),(x,y-.33)],dashed=len(group)>1)
    for a,b in mutex:
        left,right=sorted([pos[a],pos[b]])
        line([(left[0]+1.5,left[1]),(right[0]-1.5,right[1])],color='#b64e55',dashed=True,width=4)
    for fid,(x,y) in pos.items():
        special=fid in ('VIE_infrastructure_development','VIE_synchronized_infrastructure_2030')
        width=6 if special and not compact else (3.15 if not compact else 1.8)
        height=.65 if not compact else .68
        draw.rounded_rectangle([point(x-width/2,y-height/2),point(x+width/2,y+height/2)],radius=9,
                               fill='#f9ebc9' if special else 'white',outline='#516678',width=2)
        label=titles.get(fid,fid.removeprefix('VIE_').replace('_',' '))
        size=19 if not compact else 14
        max_width=point(x+width/2,y)[0]-point(x-width/2,y)[0]-16
        words=label.split();rows=[];row=''
        for word in words:
            candidate=(row+' '+word).strip()
            if row and draw.textlength(candidate,font=font(size))>max_width:
                rows.append(row);row=word
            else:row=candidate
        if row:rows.append(row)
        text(x,y,'\n'.join(rows),size=size)
    text(82,9.7 if not compact else 11.15,
            'Nét liền: prerequisite bắt buộc · Nét đứt: OR · Nét chấm đỏ: mutex\n'
            'Capstone cần 3/4 chương trình đã bàn giao; hoàn thành focus mở chương trình chưa đủ.' if not compact else
            '44 focus trước tái cấu trúc · Quan hệ và tọa độ lấy từ snapshot trước khi sửa',
            size=21,color='#526371')
    draw.text((1300,48),caption,font=font(32,True),anchor='mm',fill='#273b4e')
    image.save(out)
    print('Saved',out.relative_to(ROOT))


def main():
    manifest=json.loads((DOC/'structure.json').read_text(encoding='utf-8'))
    focuses=focus_map((ROOT/'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8-sig'))
    live=positions(focuses);ids={f['id'] for f in manifest['focuses']}
    titles=dict(re.findall(r'^\s*([\w.]+):0 "([^"\n]*)"',
                          (ROOT/'localisation/english/VIE_infra_l_english.yml').read_text(encoding='utf-8-sig'),re.M))
    mutex=[]
    for fid in ids:
        for block in values(focuses[fid],'mutually_exclusive'):
            for peer in values(block,'focus'):
                if fid<peer:mutex.append((fid,peer))
    render({f:live[f] for f in ids},{f:groups(focuses[f]) for f in ids},titles,DOC/'infrastructure_after.png',
           'Hạ tầng Việt Nam · 22 focus · Bốn chương trình quốc gia',mutex)
    before=json.loads((DOC/'before.json').read_text())
    render(before['pos'],before['pre'],{},DOC/'infrastructure_before.png',
           'Hạ tầng Việt Nam · Cấu trúc 44 focus trước tái cấu trúc',compact=True)


if __name__=='__main__':main()
