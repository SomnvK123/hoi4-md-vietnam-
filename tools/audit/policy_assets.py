"""Check v32 idea pictures against actual MD/local providers, at native size."""
import json
from pathlib import Path
import sys
from PIL import Image, ImageDraw
from industry import ROOT, parse, value, values


def main():
    md=Path(sys.argv[1]).resolve()
    manifest=json.loads((ROOT/'.claude/docs/policy_rewards/v32/structure.json').read_text(encoding='utf-8'))
    definitions={}
    for provider in (md,ROOT):
        for path in (provider/'interface').glob('*.gfx'):
            for group in values(parse(path.read_text(encoding='utf-8-sig')),'spriteTypes'):
                for sprite in values(group,'spriteType'):definitions[value(sprite,'name')]=(provider,sprite)
    ideas={}
    for group in values(value(parse((ROOT/'common/ideas/VIE_policy_rewards_ideas.txt').read_text(encoding='utf-8')),'ideas'),'country'):
        ideas.update({k:v for k,_,v in group})
    assert set(ideas)==set(manifest['new_ideas']) and len(ideas)==35
    names=sorted({'GFX_idea_'+value(ideas[key],'picture') for key in ideas})
    sheet=Image.new('RGB',(len(names)*180,140),'#dddddd');draw=ImageDraw.Draw(sheet)
    for index,name in enumerate(names):
        assert name in definitions,('Missing sprite',name)
        provider,sprite=definitions[name];texture=provider/value(sprite,'texturefile')
        assert texture.is_file(),('Missing texture',texture)
        with Image.open(texture) as source:
            icon=source.convert('RGBA')
            assert icon.width<=180 and icon.height<=100
            sheet.paste(icon,(index*180+(180-icon.width)//2,5),icon)
            draw.multiline_text((index*180+4,108),name.removeprefix('GFX_idea_').replace('_',' '),fill='black')
            print(f'PASS {name}: {icon.width}x{icon.height}; frames={value(sprite,"noOfFrames","1")}; {texture}')
    sheet.save(ROOT/'.claude/docs/policy_rewards/v32/reused_ideas_native.png')
    upstream='\n'.join(p.read_text(encoding='utf-8-sig') for p in (md/'common/ideas').glob('*.txt'))
    modifiers={k for node in manifest['new_ideas'].values() for k in node['modifiers']}
    for token in modifiers:assert token in upstream,('Modifier not evidenced in MD ideas',token)
    for token in ('STATE_519','STATE_521','STATE_522','STATE_523'):
        assert token+':' in (md/'localisation/english/state_names_l_english.yml').read_text(encoding='utf-8-sig')
    print('PASS 35 consumer ideas; actual sprites/textures, modifier and state-name evidence; no artwork modified')


if __name__=='__main__':main()
