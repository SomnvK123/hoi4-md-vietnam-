"""Script to build Focus Icons for Vietnam National Defence & People's War
(Nhánh Quốc phòng Toàn dân - 8 focuses) in Millennium Dawn.

8 Focuses:
1. def_peoples_defence: Quốc phòng toàn dân (Heavy heraldic shield, crossed steel swords, antique bronze laurel wreath, gold star)
2. def_provincial_defence_zones: Khu vực phòng thủ tỉnh (Hardened concrete citadel fortress, strategic defense zones, bastion crest)
3. def_militia_law: Luật Dân quân tự vệ (Militia rifleman patrol, pith helmet, red armband, law docket, golden rice sheaves)
4. def_force_47: Lực lượng 47 và Không gian mạng (Radiant cybernetic shield, cyan optical crosshair HUD, digital firewall, VPA star)
5. def_cyber_command: Bộ Tư lệnh Tác chiến Không gian mạng (BTL 86) (Cyberspace globe, crossed golden lightning bolts, cyber shield)
6. def_limited_war_doctrine: Học thuyết Chiến tranh Bảo vệ Tổ quốc (Strategic war map, operational vectors, crossed sword and shield)
7. def_un_peacekeeping: Lực lượng Gìn giữ Hòa bình LHQ (UN blue helmet peacekeeper, white dove of peace, Vietnam flag & cockade)
8. def_four_nos_doctrine: Học thuyết Quốc phòng Bốn Không (4 golden defense pillars, treaty scroll, dove of peace, non-alignment shield)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, exactly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Registers spriteTypes in interface/VIE_md_focus_icons.gfx
- Updates common/national_focus/VIE_md_focus.txt
"""

import math
import re
import struct
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
GFX_FILE = ROOT / "interface" / "VIE_md_focus_icons.gfx"
FOCUS_FILE = ROOT / "common" / "national_focus" / "VIE_md_focus.txt"
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")

TARGET_SIZE = (93, 91)

# =========================================================================
# UTILITIES: DDS & PNG SAVER, SHADOWS, HERALDRY
# =========================================================================

def save_game_ready_icon(canvas: Image.Image, stem: str):
    """Save canvas as transparent PNG and 32-bit BGRA uncompressed DDS."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert canvas.size == TARGET_SIZE
    assert canvas.mode == "RGBA"

    # Enforce pure alpha=0 at 1-pixel border to guarantee clean cutouts
    w, h = TARGET_SIZE
    pixels = canvas.load()
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)

    # Save PNG
    png_path = PNG_DIR / f"{stem}.png"
    canvas.save(png_path)

    # Write uncompressed 32-bit BGRA DDS
    r, g, b, a = canvas.split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()
    header = b"DDS " + struct.pack(
        "<7I11I8I5I",
        124, 0x100F, TARGET_SIZE[1], TARGET_SIZE[0], TARGET_SIZE[0] * 4, 0, 0, *([0] * 11),
        32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000, 0x1000, 0, 0, 0, 0
    )
    assert len(header) == 128
    dds_path = DDS_DIR / f"{stem}.dds"
    dds_path.write_bytes(header + data)
    assert len(dds_path.read_bytes()) == 33980
    print(f"  [SAVED] {stem} -> PNG & DDS (33,980 bytes)")


def create_gold_star(size: int) -> Image.Image:
    """Generate a sharp 5-pointed gold star with faceted shading."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1
    r_inner = r_outer * 0.382

    pts = []
    for i in range(10):
        ang = i * math.pi / 5 - math.pi / 2
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))

    draw.polygon(pts, fill=(255, 220, 20, 255), outline=(170, 130, 15, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 245, 110, 160))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(190, 140, 10, 170))
    return im


def create_gold_star_with_glow(size: int) -> Image.Image:
    """Generate faceted gold star with high-depth drop shadow."""
    star = create_gold_star(size)
    pad = 4
    canvas = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow.paste(star, (pad, pad + 1), star)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(1.2))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(star, (pad, pad), star)
    return canvas


def create_vpa_cockade(size: int = 24, naval: bool = False) -> Image.Image:
    """Generate official VPA or Naval roundel cockade."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(215, 175, 45, 255), outline=(130, 95, 20, 255))
    if naval:
        r_mid = r_outer - 1.5
        draw.ellipse((cx - r_mid, cy - r_mid, cx + r_mid, cy + r_mid), fill=(15, 45, 105, 255), outline=(10, 25, 60, 255))
        r_inner = r_mid - 2.5
        draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(195, 25, 25, 255), outline=(120, 15, 15, 255))
    else:
        r_inner = r_outer - 2.0
        draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(195, 25, 25, 255), outline=(120, 15, 15, 255))

    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im


def create_vietnam_flag(w: int = 26, h: int = 17, waving: bool = True) -> Image.Image:
    """Generate a high-fidelity Vietnamese national flag with golden star."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, w - 1, h - 1], fill=(215, 25, 25, 255), outline=(140, 15, 15, 255))
    star = create_gold_star(int(h * 0.65))
    im.paste(star, (int((w - star.width) / 2), int((h - star.height) / 2)), star)
    if waving:
        for x in range(w):
            alpha_wave = int(math.sin(x / 3.0) * 35)
            if alpha_wave > 0:
                draw.line([(x, 0), (x, h - 1)], fill=(255, 255, 255, alpha_wave))
            elif alpha_wave < 0:
                draw.line([(x, 0), (x, h - 1)], fill=(0, 0, 0, abs(alpha_wave)))
    return im


def apply_ambient_drop_shadow(canvas: Image.Image, radius: float = 1.8) -> Image.Image:
    """Generate soft ambient occlusion drop shadow behind entire composite icon."""
    out = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow.paste(canvas, (0, 1), canvas)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(radius))
    shadow_a = shadow.split()[-1].point(lambda p: int(p * 0.8))
    shadow = Image.merge("RGBA", (black, black, black, shadow_a))
    out.paste(shadow, (0, 0), shadow)
    out.paste(canvas, (0, 0), canvas)
    return out


# =========================================================================
# 8 BUILDER FUNCTIONS FOR NATIONAL DEFENCE & PEOPLE'S WAR
# =========================================================================

# 1. VIE_peoples_defence
def build_def_peoples_defence() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "special_forces.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 73), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Central crimson heart shield with 3D gold star
    draw = ImageDraw.Draw(canvas)
    pts_shield = [(36, 26), (56, 26), (56, 42), (46, 52), (36, 42)]
    draw.polygon(pts_shield, fill=(195, 25, 25, 255), outline=(235, 195, 45, 255), width=2)
    center_star = create_gold_star(16)
    canvas.paste(center_star, ((TARGET_SIZE[0] - center_star.width) // 2, 30), center_star)

    # Top faceted gold star with glow
    star_top = create_gold_star_with_glow(20)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -1), star_top)

    # Bottom VPA cockade pinning the golden ribbon
    cockade = create_vpa_cockade(17, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "def_peoples_defence")
    return canvas


# 2. VIE_provincial_defence_zones
def build_def_provincial_defence_zones() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "city_fort.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.15)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((82, 74), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Citadel fortification crest & strategic defense rings
    draw = ImageDraw.Draw(canvas)
    # Tactical radar perimeter arc
    draw.arc([18, 30, 74, 70], start=190, end=350, fill=(245, 210, 45, 180), width=2)
    draw.arc([24, 34, 68, 66], start=190, end=350, fill=(245, 210, 45, 120), width=1)

    # Top faceted gold star
    star_top = create_gold_star_with_glow(20)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -1), star_top)

    # Bottom defense zone shield cockade
    cockade = create_vpa_cockade(18, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "def_provincial_defence_zones")
    return canvas


# 3. VIE_militia_law
def build_def_militia_law() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "belarus" / "blr_people_militia.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Self-defense militia red armband accent
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([28, 48, 36, 55], fill=(210, 25, 25, 240), outline=(140, 15, 15, 255))
    star_arm = create_gold_star(7)
    canvas.paste(star_arm, (29, 48), star_arm)

    # Top faceted gold star
    star_top = create_gold_star_with_glow(20)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -1), star_top)

    # Bottom militia cockade
    cockade = create_vpa_cockade(18, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "def_militia_law")
    return canvas


# 4. VIE_force_47
def build_def_force_47() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "china" / "golden_shield_project.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 74), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Glowing Cyan optical HUD targeting crosshair & digital circuit grid
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 42
    draw.ellipse((cx - 16, cy - 16, cx + 16, cy + 16), outline=(40, 220, 255, 150), width=1)
    draw.line([(cx - 20, cy), (cx + 20, cy)], fill=(40, 220, 255, 180), width=1)
    draw.line([(cx, cy - 20), (cx, cy + 20)], fill=(40, 220, 255, 180), width=1)

    # Central VPA star
    vpa_star = create_gold_star(16)
    canvas.paste(vpa_star, ((TARGET_SIZE[0] - vpa_star.width) // 2, 34), vpa_star)

    # Top faceted gold star
    star_top = create_gold_star_with_glow(20)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -1), star_top)

    # Bottom cyber lock cockade
    cockade = create_vpa_cockade(17, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "def_force_47")
    return canvas


# 5. VIE_cyber_command
def build_def_cyber_command() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "army_cyberwar.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Crossed golden lightning bolts of Military Cyberspace Command (BTL 86)
    draw = ImageDraw.Draw(canvas)
    # Left bolt
    draw.polygon([(28, 28), (35, 38), (31, 39), (37, 50), (28, 41), (32, 40)], fill=(255, 230, 60, 240), outline=(210, 160, 20, 255))
    # Right bolt
    draw.polygon([(65, 28), (58, 38), (62, 39), (56, 50), (65, 41), (61, 40)], fill=(255, 230, 60, 240), outline=(210, 160, 20, 255))

    # Top faceted gold star
    star_top = create_gold_star_with_glow(21)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -2), star_top)

    # Bottom Command cockade
    cockade = create_vpa_cockade(18, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "def_cyber_command")
    return canvas


# 6. VIE_limited_war_doctrine
def build_def_limited_war_doctrine() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "draw_up_war_plans.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Strategic red defense shield repelling invasion vectors
    draw = ImageDraw.Draw(canvas)
    draw.polygon([(36, 32), (56, 32), (56, 46), (46, 54), (36, 46)], fill=(195, 25, 25, 255), outline=(235, 195, 45, 255), width=2)
    star_center = create_gold_star(14)
    canvas.paste(star_center, ((TARGET_SIZE[0] - star_center.width) // 2, 35), star_center)

    # Counter-offensive tactical arrows (VPA Red and Gold)
    draw.polygon([(26, 38), (14, 30), (22, 28)], fill=(225, 30, 30, 240), outline=(150, 20, 20, 255))
    draw.polygon([(66, 38), (78, 30), (70, 28)], fill=(245, 205, 40, 240), outline=(160, 120, 15, 255))

    # Top faceted gold star
    star_top = create_gold_star_with_glow(20)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -1), star_top)

    # Bottom General Staff cockade
    cockade = create_vpa_cockade(17, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "def_limited_war_doctrine")
    return canvas


# 7. VIE_un_peacekeeping
def build_def_un_peacekeeping() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "soldiers" / "un_peace_keeping.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Ceremonial Vietnam National Flag with gold flagpole
    draw = ImageDraw.Draw(canvas)
    # Gold flagpole
    draw.line([(15, 14), (15, 42)], fill=(225, 185, 45, 255), width=2)
    draw.ellipse((13, 12, 17, 16), fill=(255, 225, 55, 255), outline=(150, 110, 15, 255))
    # Fluttering flag
    flag = create_vietnam_flag(24, 15, waving=True)
    canvas.paste(flag, (16, 16), flag)

    # Top faceted gold star
    star_top = create_gold_star_with_glow(20)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -1), star_top)

    # Bottom Peacekeeping Cockade
    cockade = create_vpa_cockade(18, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "def_un_peacekeeping")
    return canvas


# 8. VIE_four_nos_doctrine
def build_def_four_nos_doctrine() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_diplomacy" / "treaty2.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 75), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # 4 Golden Defense Pillars of Non-Alignment
    draw = ImageDraw.Draw(canvas)
    # 4 vertical gold pillar bars
    for px in [32, 40, 52, 60]:
        draw.rectangle([px, 30, px + 3, 50], fill=(245, 210, 45, 240), outline=(150, 110, 20, 255))
        draw.rectangle([px - 1, 28, px + 4, 30], fill=(255, 230, 80, 255))
        draw.rectangle([px - 1, 50, px + 4, 52], fill=(255, 230, 80, 255))

    # Central gold star
    star_center = create_gold_star(14)
    canvas.paste(star_center, ((TARGET_SIZE[0] - star_center.width) // 2, 33), star_center)

    # Top faceted gold star
    star_top = create_gold_star_with_glow(20)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -1), star_top)

    # Bottom diplomatic cockade
    cockade = create_vpa_cockade(17, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "def_four_nos_doctrine")
    return canvas


# =========================================================================
# REGISTRATION & IN-TREE INTEGRATION
# =========================================================================

FOCUS_MAP = {
    "VIE_peoples_defence": "def_peoples_defence",
    "VIE_provincial_defence_zones": "def_provincial_defence_zones",
    "VIE_militia_law": "def_militia_law",
    "VIE_force_47": "def_force_47",
    "VIE_cyber_command": "def_cyber_command",
    "VIE_limited_war_doctrine": "def_limited_war_doctrine",
    "VIE_un_peacekeeping": "def_un_peacekeeping",
    "VIE_four_nos_doctrine": "def_four_nos_doctrine",
}


def register_sprites():
    """Register spriteTypes in interface/VIE_md_focus_icons.gfx."""
    gfx_txt = GFX_FILE.read_text(encoding="utf-8")
    new_entries = []
    for fid, stem in FOCUS_MAP.items():
        sprite_name = f"GFX_focus_VIE_{stem}"
        if sprite_name not in gfx_txt:
            entry = f"\tspriteType = {{\n\t\tname = \"{sprite_name}\"\n\t\ttexturefile = \"gfx/interface/goals/{stem}.dds\"\n\t}}"
            new_entries.append(entry)

    if new_entries:
        last_brace_idx = gfx_txt.rfind("}")
        updated_gfx = gfx_txt[:last_brace_idx] + "\n".join(new_entries) + "\n}\n"
        GFX_FILE.write_text(updated_gfx, encoding="utf-8")
        print(f"Registered {len(new_entries)} new spriteTypes in {GFX_FILE.name}")
    else:
        print("All spriteTypes already registered.")


def update_focus_tree():
    """Update icon references in common/national_focus/VIE_md_focus.txt."""
    tree_txt = FOCUS_FILE.read_text(encoding="utf-8")
    updated_count = 0
    for fid, stem in FOCUS_MAP.items():
        sprite_name = f"GFX_focus_VIE_{stem}"
        pattern = re.compile(rf"(id\s*=\s*{re.escape(fid)}\s*\n\s*icon\s*=\s*)(\S+)")
        m = pattern.search(tree_txt)
        if m and m.group(2) != sprite_name:
            tree_txt = pattern.sub(rf"\g<1>{sprite_name}", tree_txt)
            updated_count += 1
            print(f"  Updated {fid} -> icon = {sprite_name}")

    if updated_count > 0:
        FOCUS_FILE.write_text(tree_txt, encoding="utf-8")
        print(f"Updated {updated_count} focus icons in {FOCUS_FILE.name}")
    else:
        print("All focus icons already up to date.")


def create_showcase_artifact(icons: dict[str, Image.Image]):
    """Create a contact sheet showcase image of all 8 National Defence focus icons."""
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "national_defence_icons_showcase.png"

    cols = 4
    rows = (len(icons) + cols - 1) // cols
    card_w, card_h = 195, 145
    pad_x, pad_y = 20, 20
    header_h = 90

    total_w = pad_x * 2 + cols * card_w + (cols - 1) * 15
    total_h = header_h + rows * card_h + (rows - 1) * 15 + pad_y

    canvas = Image.new("RGBA", (total_w, total_h), (14, 18, 24, 255))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_id = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
        font_name = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
    except Exception:
        font_title = font_sub = font_id = font_name = None

    draw.text((pad_x, 20), "BỘ ICON GFX QUỐC PHÒNG TOÀN DÂN (NATIONAL DEFENCE)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "8 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "def_peoples_defence": "Quốc phòng Toàn dân",
        "def_provincial_defence_zones": "Khu vực Phòng thủ Tỉnh",
        "def_militia_law": "Luật Dân quân Tự vệ",
        "def_force_47": "Lực lượng 47 và Không gian mạng",
        "def_cyber_command": "Bộ Tư lệnh Tác chiến mạng",
        "def_limited_war_doctrine": "Học thuyết Chiến tranh BV Tổ quốc",
        "def_un_peacekeeping": "Gìn giữ Hòa bình LHQ",
        "def_four_nos_doctrine": "Quốc phòng Bốn Không",
    }

    for idx, (stem, img) in enumerate(icons.items()):
        c = idx % cols
        r = idx // cols
        x = pad_x + c * (card_w + 15)
        y = header_h + r * (card_h + 15)

        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=8, fill=(22, 28, 38, 255), outline=(45, 60, 80, 255))

        icon_x = x + (card_w - img.width) // 2
        icon_y = y + 10
        canvas.paste(img, (icon_x, icon_y), img)

        t_title = focus_titles.get(stem, stem)
        draw.text((x + 10, y + card_h - 36), stem, fill=(240, 200, 80, 255), font=font_id)
        draw.text((x + 10, y + card_h - 20), t_title, fill=(200, 215, 230, 255), font=font_name)

    canvas.save(out_path)
    print(f"Showcase image saved: {out_path}")


def main():
    print("=" * 65)
    print("BUILDING 8 NATIONAL DEFENCE FOCUS ICONS (PAINTERLY 3D MD STYLE)")
    print("=" * 65)

    built_icons = {}
    built_icons["def_peoples_defence"] = build_def_peoples_defence()
    built_icons["def_provincial_defence_zones"] = build_def_provincial_defence_zones()
    built_icons["def_militia_law"] = build_def_militia_law()
    built_icons["def_force_47"] = build_def_force_47()
    built_icons["def_cyber_command"] = build_def_cyber_command()
    built_icons["def_limited_war_doctrine"] = build_def_limited_war_doctrine()
    built_icons["def_un_peacekeeping"] = build_def_un_peacekeeping()
    built_icons["def_four_nos_doctrine"] = build_def_four_nos_doctrine()

    print("\nRegistering in interface/VIE_md_focus_icons.gfx...")
    register_sprites()

    print("\nUpdating focus tree icons in common/national_focus/VIE_md_focus.txt...")
    update_focus_tree()

    print("\nGenerating visual showcase artifact...")
    create_showcase_artifact(built_icons)

    print("\n" + "=" * 65)
    print("BUILD COMPLETE: ALL 8 NATIONAL DEFENCE ICONS INTEGRATED")
    print("=" * 65)


if __name__ == "__main__":
    main()
