"""Xuat va kiem bon icon ngoai giao; khong chay builder toan bo."""
from pathlib import Path
import hashlib
import json
import shutil
import struct
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

RAW = Path(__file__).resolve().parent
ROOT = RAW.parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from build_vie_focus_icons import write_dds


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = json.loads((RAW / 'diplomacy_batch_01_prompts.json').read_text(encoding='utf-8'))
    protected = [ROOT / folder / (stem + ext)
                 for stem in ('asean_integration', 'border_settlement')
                 for folder, ext in (('assets/focus_icons/raw', '.png'),
                                     ('assets/focus_icons/png', '.png'),
                                     ('gfx/interface/goals', '.dds'))]
    before = {str(p.relative_to(ROOT)): sha(p) for p in protected}
    focus = (ROOT / 'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8-sig')
    gfx = (ROOT / 'interface/VIE_md_focus_icons.gfx').read_text(encoding='utf-8-sig')
    records = []
    icons = []
    for job in spec['assets']:
        stem = job['stem']
        master = RAW / (stem + '.png')
        source = Path(job['generated_source'])
        if not master.exists():
            shutil.copy2(source, master)
        with Image.open(master) as im:
            assert im.mode == 'RGBA', (stem, im.mode)
            image = im.copy()
        assert image.getchannel('A').getextrema() == (0, 255), stem
        art = ImageOps.contain(image, (91, 89), Image.Resampling.LANCZOS)
        icon = Image.new('RGBA', (93, 91), (0, 0, 0, 0))
        icon.paste(art, ((93 - art.width) // 2, (91 - art.height) // 2))
        png = ROOT / 'assets/focus_icons/png' / (stem + '.png')
        dds = ROOT / 'gfx/interface/goals' / (stem + '.dds')
        icon.save(png)
        write_dds(dds, icon)
        data = dds.read_bytes()
        assert len(data) == 33980
        assert data[:4] == b'DDS '
        assert struct.unpack_from('<I', data, 12)[0] == 91
        assert struct.unpack_from('<I', data, 16)[0] == 93
        assert struct.unpack_from('<I', data, 20)[0] == 93 * 4
        assert struct.unpack_from('<I', data, 80)[0] == 0x41
        assert struct.unpack_from('<5I', data, 84) == (0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF)
        assert struct.unpack_from('<I', data, 104)[0] == 0xFF000000
        assert struct.unpack_from('<I', data, 28)[0] == 0
        with Image.open(dds) as decoded:
            assert decoded.convert('RGBA').tobytes() == icon.tobytes(), stem
        alpha = icon.getchannel('A')
        assert all(alpha.crop(box).getextrema() == (0, 0) for box in
                   ((0, 0, 93, 1), (0, 90, 93, 91), (0, 0, 1, 91), (92, 0, 93, 91)))
        sprite = 'GFX_focus_VIE_' + stem
        assert 'icon = ' + sprite in focus
        assert 'name = "' + sprite + '"' in gfx
        assert 'texturefile = "gfx/interface/goals/' + stem + '.dds"' in gfx
        records.append({'asset_id': 'VIE_' + stem, 'sprite': sprite,
                        'master': str(master.relative_to(ROOT)),
                        'master_size': list(image.size), 'master_sha256': sha(master),
                        'png': str(png.relative_to(ROOT)), 'png_sha256': sha(png),
                        'dds': str(dds.relative_to(ROOT)), 'dds_sha256': sha(dds),
                        'final_size': [93, 91], 'codec': 'RGB32 BGRA, no mipmaps',
                        'dds_bytes': len(data), 'frame_count': 1,
                        'alpha_border': 'pass', 'rgba_round_trip': 'pass',
                        'integration': 'existing sprite and focus mapping verified',
                        'in_game_check': 'unrun'})
        icons.append((stem, icon, image))
        print(stem + ': PASS RGBA round-trip, header, alpha border, mapping')
    assert before == {str(p.relative_to(ROOT)): sha(p) for p in protected}
    preview_dir = ROOT / 'assets/focus_icons/previews/diplomacy_batch_01'
    preview_dir.mkdir(parents=True, exist_ok=True)
    labels = ('ASEAN chair', 'UN Security Council', 'Vietnam-Laos', 'Bamboo diplomacy')
    font = ImageFont.load_default(size=13)
    native = Image.new('RGB', (640, 274), '#18222d')
    draw = ImageDraw.Draw(native)
    draw.text((12, 10), 'Native 93 x 91 - dark / light backgrounds', fill='white', font=font)
    draw.rectangle((0, 145, 639, 273), fill='#e5e2dc')
    for i, (stem, icon, _) in enumerate(icons):
        x = 16 + i * 158
        native.paste(icon, (x + 26, 40), icon)
        native.paste(icon, (x + 26, 164), icon)
        draw.text((x, 132), labels[i], fill='white', font=font)
        draw.text((x, 257), labels[i], fill='#18222d', font=font)
    native.save(preview_dir / 'native_93x91.png')
    large = Image.new('RGB', (1120, 330), '#18222d')
    draw = ImageDraw.Draw(large)
    for i, (_, _, master) in enumerate(icons):
        art = ImageOps.contain(master, (260, 270), Image.Resampling.LANCZOS)
        large.paste(art, (i * 280 + (280 - art.width) // 2, 12), art)
        draw.text((i * 280 + 18, 301), labels[i], fill='white', font=font)
    large.save(preview_dir / 'large.png')
    report = {'date': spec['date'], 'generator': spec['generator'],
              'revision': spec.get('revision', 1),
              'references': spec.get('references', []),
              'reference_use': spec.get('reference_use', 'No external reference inputs'),
              'source_type': spec['source_type'], 'rights_or_license': spec['license'],
              'prompt_manifest': 'diplomacy_batch_01_prompts.json',
              'rebuild': 'python assets/focus_icons/raw/export_diplomacy_batch_01.py',
              'export_recipe': 'RGBA contain 91x89, centered 93x91; write_dds helper only',
              'protected_assets_sha256': before, 'assets': records,
              'known_limitations': 'AI symbolic illustrations, not historical photographs or official emblems; in-game hover untested.'}
    (RAW / 'diplomacy_batch_01_record.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Protected ASEAN / border masters and exports unchanged.')


if __name__ == '__main__':
    main()
