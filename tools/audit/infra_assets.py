"""Check MD providers and export native-sized reused icons; requires Pillow.

Usage: python tools/audit/infra_assets.py <MD checkout/install directory>
Does not validate engine rendering or modify gameplay/artwork assets.
"""
from pathlib import Path
import json
import sys
from PIL import Image, ImageDraw, ImageFont
from industry import parse, values, value

ROOT = Path(__file__).resolve().parents[2]


def main():
    md=Path(sys.argv[1]).resolve()
    definitions={}
    for path in (md/'interface').glob('*.gfx'):
        for group in values(parse(path.read_text(encoding='utf-8-sig')),'spriteTypes'):
            for sprite in values(group,'spriteType'):
                definitions[value(sprite,'name')]=sprite
    manifest=json.loads((ROOT/'.claude/docs/infrastructure/structure.json').read_text(encoding='utf-8'))
    names=sorted({f['icon'] for f in manifest['focuses']})
    names+=['GFX_decision_generic_form_nation','GFX_idea_economic_road_idea']
    sheet=Image.new('RGB',(960,((len(names)+3)//4)*150),'#eeeeee')
    draw=ImageDraw.Draw(sheet)
    for i,name in enumerate(names):
        assert name in definitions,('Missing MD sprite',name)
        sprite=definitions[name];texture=md/value(sprite,'texturefile')
        assert texture.is_file(),('Missing MD texture',texture)
        with Image.open(texture) as source:
            icon=source.convert('RGBA')
            assert icon.width>0 and icon.height>0
            x=(i%4)*240;y=(i//4)*150
            # Original texture size: no resizing; oversized exports are reported.
            assert icon.width<=240 and icon.height<=110,('Unexpected icon size',name,icon.size)
            sheet.paste(icon,(x+(240-icon.width)//2,y+3),icon)
            label=name.removeprefix('GFX_').replace('_',' ')
            words=label.split();rows=[];row=''
            for word in words:
                candidate=(row+' '+word).strip()
                if row and draw.textlength(candidate)>224:rows.append(row);row=word
                else:row=candidate
            rows.append(row)
            draw.multiline_text((x+120,y+112),'\n'.join(rows),anchor='ma',align='center',fill='black')
            print(f'PASS {name}: {icon.width}x{icon.height}; frames={value(sprite,"noOfFrames","1")}; {texture.relative_to(md)}')
    out=ROOT/'.claude/docs/infrastructure/reused_icons_native.png'
    sheet.save(out)
    print('PASS native MD textures; contact sheet:',out.relative_to(ROOT))


if __name__=='__main__':main()
