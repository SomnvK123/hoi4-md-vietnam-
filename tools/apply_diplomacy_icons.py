"""Script to integrate all 34 Diplomacy Focus Icons:
1. Append 34 spriteType definitions to interface/VIE_md_focus_icons.gfx
2. Update icon = GFX_focus_VIE_<stem> in common/national_focus/VIE_md_focus.txt
3. Generate high-res showcase contact sheet in brain directory
"""

import math
import re
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
GFX_FILE = ROOT / "interface" / "VIE_md_focus_icons.gfx"
FOCUS_FILE = ROOT / "common" / "national_focus" / "VIE_md_focus.txt"
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")

FOCUS_STEM_MAP = [
    # Cluster 1: Láng giềng Đông Dương & Trục Việt - Trung (12)
    ("VIE_border_settlement", "border_settlement"),
    ("VIE_special_relations_laos", "special_relations_laos"),
    ("VIE_cambodia_relations", "cambodia_relations"),
    ("VIE_indochina_solidarity", "indochina_solidarity"),
    ("VIE_indochina_federation", "indochina_federation"),
    ("VIE_16_words", "16_words"),
    ("VIE_border_trade_gates", "border_trade_gates"),
    ("VIE_defence_hotline", "defence_hotline"),
    ("VIE_gulf_of_tonkin", "gulf_of_tonkin"),
    ("VIE_shared_future", "shared_future"),
    ("VIE_cambodia_border", "cambodia_border"),
    ("VIE_funan_techo_response", "funan_techo_response"),
    # Cluster 2: Trục ASEAN, Đa phương & Biểu tượng Cây tre (9)
    ("VIE_asean_integration", "asean_integration"),
    ("VIE_asean_chair", "asean_chair"),
    ("VIE_code_of_conduct", "code_of_conduct"),
    ("VIE_un_security_council", "un_security_council"),
    ("VIE_multilateral_champion", "multilateral_champion"),
    ("VIE_apec_host", "apec_host"),
    ("VIE_mekong_commission", "mekong_commission"),
    ("VIE_mekong_dams_response", "mekong_dams_response"),
    ("VIE_bamboo_diplomacy", "bamboo_diplomacy"),
    # Cluster 3: Đối tác Chiến lược Lớn & Toàn cầu (13)
    ("VIE_us_engagement", "us_engagement"),
    ("VIE_us_comprehensive_partnership", "us_comprehensive_partnership"),
    ("VIE_us_embargo_lifted", "us_embargo_lifted"),
    ("VIE_us_carrier_visit", "us_carrier_visit"),
    ("VIE_us_tariff_deal", "us_tariff_deal"),
    ("VIE_csp_network", "csp_network"),
    ("VIE_japan_partnership", "japan_partnership"),
    ("VIE_korea_partnership", "korea_partnership"),
    ("VIE_india_partnership", "india_partnership"),
    ("VIE_australia_partnership", "australia_partnership"),
    ("VIE_france_eu", "france_eu"),
    ("VIE_gulf_investment", "gulf_investment"),
    ("VIE_global_south_ties", "global_south_ties"),
]

def update_gfx_file():
    print("Updating interface/VIE_md_focus_icons.gfx...")
    content = GFX_FILE.read_text(encoding="utf-8")

    new_sprites = []
    for fid, stem in FOCUS_STEM_MAP:
        sprite_name = f"GFX_focus_{fid}"
        if f'name = "{sprite_name}"' in content or f'name = {sprite_name}' in content:
            print(f"  [EXISTS] {sprite_name}")
            continue
        new_sprites.append(
            f'\tspriteType = {{\n'
            f'\t\tname = "{sprite_name}"\n'
            f'\t\ttexturefile = "gfx/interface/goals/{stem}.dds"\n'
            f'\t}}'
        )

    if new_sprites:
        idx = content.rfind("}")
        if idx != -1:
            updated_content = content[:idx] + "\n".join(new_sprites) + "\n}\n"
            GFX_FILE.write_text(updated_content, encoding="utf-8")
            print(f"  [ADDED] {len(new_sprites)} new spriteTypes to {GFX_FILE.name}")
        else:
            print("  [ERROR] Closing bracket not found in GFX file")
    else:
        print("  All spriteTypes already present.")


def update_focus_file():
    print("\nUpdating common/national_focus/VIE_md_focus.txt...")
    content = FOCUS_FILE.read_text(encoding="utf-8")
    updated_count = 0

    for fid, stem in FOCUS_STEM_MAP:
        sprite_name = f"GFX_focus_{fid}"
        # Match focus block for fid
        pattern = re.compile(rf'(id\s*=\s*{fid}\b[\s\S]*?icon\s*=\s*)(\S+)')
        m = pattern.search(content)
        if m:
            old_icon = m.group(2)
            if old_icon != sprite_name:
                content = content[:m.start(2)] + sprite_name + content[m.end(2):]
                updated_count += 1
                print(f"  [UPDATED] {fid}: {old_icon} -> {sprite_name}")
            else:
                print(f"  [ALREADY] {fid}: {sprite_name}")
        else:
            print(f"  [NOT FOUND] Focus {fid}")

    FOCUS_FILE.write_text(content, encoding="utf-8")
    print(f"Updated {updated_count} focus icon references.")


def generate_showcase():
    print("\nGenerating diplomacy icons showcase contact sheet...")
    cols = 6
    rows = math.ceil(len(FOCUS_STEM_MAP) / cols)
    cell_w, cell_h = 130, 130
    sheet_w = cols * cell_w + 40
    sheet_h = rows * cell_h + 100

    sheet = Image.new("RGBA", (sheet_w, sheet_h), (18, 22, 28, 255))
    draw = ImageDraw.Draw(sheet)

    # Header banner
    draw.rectangle([0, 0, sheet_w, 60], fill=(26, 32, 44, 255))
    draw.line([(0, 60), (sheet_w, 60)], fill=(215, 175, 45, 255), width=2)
    draw.text((25, 18), "VIETNAM DIPLOMACY & FOREIGN AFFAIRS - 34 FOCUS ICONS SHOWCASE", fill=(255, 225, 75, 255))

    for idx, (fid, stem) in enumerate(FOCUS_STEM_MAP):
        c = idx % cols
        r = idx // cols
        x = 20 + c * cell_w
        y = 75 + r * cell_h

        # Cell background card
        draw.rounded_rectangle([x + 4, y + 4, x + cell_w - 4, y + cell_h - 4], radius=6, fill=(28, 36, 48, 255), outline=(50, 65, 85, 255))

        # Paste icon
        png_path = PNG_DIR / f"{stem}.png"
        if png_path.exists():
            icon = Image.open(png_path).convert("RGBA")
            ox = x + (cell_w - icon.width) // 2
            oy = y + 10
            sheet.paste(icon, (ox, oy), icon)

        # Label
        label = stem
        if len(label) > 16:
            label = label[:14] + ".."
        draw.text((x + 10, y + 104), label, fill=(200, 210, 225, 255))

    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "diplomacy_icons_showcase.png"
    sheet.save(out_path)
    print(f"  [SAVED] Showcase contact sheet to {out_path}")


def main():
    update_gfx_file()
    update_focus_file()
    generate_showcase()
    print("\nIntegration and showcase generation complete!")


if __name__ == "__main__":
    main()
