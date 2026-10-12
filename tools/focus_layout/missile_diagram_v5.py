"""Xuat so do/manifest ten lua tu focus live; khong phai screenshot HOI4."""
from pathlib import Path
import argparse
import json
import re
import runpy
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]


def font(size, bold=False):
    paths = [Path('C:/Windows/Fonts')/('segoeuib.ttf' if bold else 'segoeui.ttf'),
             Path('/usr/share/fonts/truetype/dejavu')/('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')]
    for path in paths:
        if path.is_file():
            return ImageFont.truetype(str(path), size)
    raise RuntimeError('Can font Unicode Segoe UI hoac DejaVu Sans.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'.claude/docs/missile')
    args = parser.parse_args()
    ns = runpy.run_path(str(ROOT/'tools/audit/missile_scenarios.py'))
    focuses, position, value, values = (ns[k] for k in ('FOCUSES', 'position', 'value', 'values'))
    loc = (ROOT/'localisation/english/VIE_missile_l_english.yml').read_text(encoding='utf-8-sig')
    titles = dict(re.findall(r'^ (VIE_msl_\w+):0 "([^"\n]+)"', loc, re.M))
    sprites = {}
    for path in (ROOT/'interface').glob('*.gfx'):
        for block in re.findall(r'spriteType\s*=\s*\{([^}]+)\}', path.read_text(encoding='utf-8-sig')):
            name = re.search(r'name\s*=\s*"([^"\n]+)"', block)
            texture = re.search(r'texturefile\s*=\s*"([^"\n]+)"', block)
            if name and texture:
                sprites[name[1]] = texture[1]
    ids = [fid for fid in focuses if fid.startswith('VIE_msl_')]
    x0 = min(position(fid)[0] for fid in ids)
    x1 = max(position(fid)[0] for fid in ids)
    y0 = min(position(fid)[1] for fid in ids)
    y1 = max(position(fid)[1] for fid in ids)
    image = Image.new('RGB', ((x1-x0)*90+350, (y1-y0)*145+410), '#0e1c27')
    draw = ImageDraw.Draw(image)
    draw.text((30,20), 'Tên lửa V5 • 10 focus • 1 → 6 → 2 → 1', font=font(28, True), fill='#e7eff5')
    draw.text((30,66), 'Tọa độ và prerequisite live • 15 cạnh AND • M08 cần nghiệm thu VCS • Chưa kiểm trong HOI4', font=font(18), fill='#aac1cf')
    xy = {fid: ((position(fid)[0]-x0)*90+175, (position(fid)[1]-y0)*145+135) for fid in ids}
    cards = {}
    for fid in ids:
        x,y = xy[fid]
        cards[fid] = (x-136,y,x+136,y+223)
    edges=[]
    for fid in ids:
        x,y=xy[fid]
        for group in values(focuses[fid], 'prerequisite'):
            for parent in values(group, 'focus'):
                edges.append({'from':parent,'to':fid,'operator':'AND'})
                if parent not in xy:
                    continue
                px,py=xy[parent];middle=y-32
                draw.line([(px,py+223),(px,middle),(x,middle),(x,y)],fill='#79b4c9',width=3)
                draw.polygon([(x,y),(x-6,y-10),(x+6,y-10)],fill='#79b4c9')
    manifest=[]
    for fid in ids:
        x,y=xy[fid];b=focuses[fid]
        colour = '#77b9a5' if fid in [ns['NODES'][code]['id'] for code in ('M05','M06','M07','M08')] else '#86b2d0'
        if fid==ns['NODES']['M09']['id']:colour='#d1b47a'
        draw.rounded_rectangle(cards[fid],radius=12,fill='#1d303d',outline=colour,width=2)
        code=next(n['code'] for n in ns['NODES'].values() if n['id']==fid)
        draw.text((x-122,y+8),code,font=font(17,True),fill=colour)
        draw.text((x+57,y+10),'Cost '+value(b,'cost'),font=font(13),fill='#b7c6d0')
        texture=sprites[value(b,'icon')]
        icon=Image.open(ROOT/texture).convert('RGBA')
        if icon.size!=(93,91):
            raise ValueError('Focus consumer size: '+texture)
        image.paste(icon,(x-46,y+35),icon)
        rows=[];line='';f=font(17)
        for word in titles[fid].split():
            candidate=(line+' '+word).strip()
            if draw.textlength(candidate,font=f)>245 and line:rows.append(line);line=word
            else:line=candidate
        if line:rows.append(line)
        if len(rows)>4:raise ValueError('Title exceeds card: '+fid)
        for i,line in enumerate(rows):
            draw.text((x-draw.textlength(line,font=f)/2,y+130+i*22),line,font=f,fill='#e7eff5')
        if code=='M00':draw.text((x-117,y+205),'Từ VIE_modernize_vpa',font=font(12),fill='#cfb982')
        if code=='M08':draw.text((x-112,y+205),'Gate: VCS đã nghiệm thu',font=font(12),fill='#cfb982')
        manifest.append(dict(code=code,id=fid,title=titles[fid],absolute=list(position(fid)),
                             relative=[int(value(b,'x')),int(value(b,'y'))],anchor=value(b,'relative_position_id'),
                             all=[values(g,'focus') for g in values(b,'prerequisite')],cost=int(value(b,'cost')),
                             icon=value(b,'icon'),texture=texture))
    args.output.mkdir(parents=True,exist_ok=True)
    image.save(args.output/'missile_v5.png')
    (args.output/'missile_v5.json').write_text(json.dumps(dict(nodes=manifest,edges=edges,runtime_validated=False),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Board giu icon o kich thuoc consumer 1:1 de review reuse, khong sua texture.
    textures=list(dict.fromkeys(n['texture'] for n in manifest))
    board=Image.new('RGBA',(len(textures)*150,135),'#152531')
    bd=ImageDraw.Draw(board)
    for i,texture in enumerate(textures):
        icon=Image.open(ROOT/texture).convert('RGBA');board.alpha_composite(icon,(i*150+28,8))
        bd.text((i*150+8,106),Path(texture).stem[:20],font=font(10),fill='#e7eff5')
    board.save(args.output/'reused_icons_native.png')
    print('Exported live diagram, manifest and native-size icon board:',args.output)


if __name__=='__main__':
    main()
