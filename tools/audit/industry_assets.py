"""Resolve live industry focus, idea, decision and event sprites against MD."""
import json
from pathlib import Path
import sys
from PIL import Image, ImageDraw
from industry import ROOT, parse, value, values


def main():
    md = Path(sys.argv[1]).resolve()
    manifest = json.loads((ROOT/'.claude/docs/industry/v31/structure.json').read_text(encoding='utf-8'))
    definitions = {}
    base = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else None
    for provider in ([base] if base else [])+[md, ROOT]:
        files = [provider/'interface/eventpictures.gfx'] if provider == base else (provider/'interface').glob('*.gfx')
        for file in files:
            for group in values(parse(file.read_text(encoding='utf-8-sig')), 'spriteTypes'):
                for sprite in values(group, 'spriteType'):
                    definitions[value(sprite, 'name')] = (provider, sprite)
    names = {f['icon'] for f in manifest['focuses']}
    for file in (ROOT/'common/ideas').glob('*.txt'):
        for group in values(value(parse(file.read_text(encoding='utf-8-sig')), 'ideas', []), 'country'):
            for key, _, idea in group:
                if key in manifest['ideas']:
                    names.add('GFX_idea_'+value(idea, 'picture'))
    names.add('GFX_decision_generic_form_nation')
    for file in ('VIE_industry_events.txt', 'VIE_automotive_events.txt'):
        for event in values(parse((ROOT/'events'/file).read_text(encoding='utf-8-sig')), 'country_event'):
            names.add(value(event, 'picture'))
    missing = sorted(names-definitions.keys())
    assert not missing, ('Missing provider sprites', missing)
    sheet = Image.new('RGB', (1200, ((len(names)+3)//4)*235), '#dedede')
    draw = ImageDraw.Draw(sheet)
    for index, name in enumerate(sorted(names)):
        provider, sprite = definitions[name]
        texture = provider/value(sprite, 'texturefile')
        assert texture.is_file(), texture
        with Image.open(texture) as source:
            icon = source.convert('RGBA')
            assert icon.width <= 300 and icon.height <= 185, (name, icon.size)
            x = index%4*300; y = index//4*235
            sheet.paste(icon, (x+(300-icon.width)//2, y+3), icon)
            draw.multiline_text((x+4, y+188), name.replace('_', ' '), fill='black')
            print(f'PASS {name}: {icon.width}x{icon.height}; frames={value(sprite,"noOfFrames","1")}; {texture}')
    sheet.save(ROOT/'.claude/docs/industry/v31/reused_icons_native.png')
    print('PASS actual MD/local providers; native texture contact sheet; no artwork changed')


if __name__ == '__main__':
    main()
