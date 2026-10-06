import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
import math

ROOT = Path(__file__).resolve().parents[1]
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")
TARGET_SIZE = (93, 91)

def create_gold_star(size: int) -> Image.Image:
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

    draw.polygon(pts, fill=(255, 222, 35, 255), outline=(160, 120, 10, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 248, 125, 170))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(185, 135, 10, 180))
    return im

def create_gold_star_with_glow(size: int, shadow_blur: float = 1.3) -> Image.Image:
    star = create_gold_star(size)
    pad = 4
    canvas = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow.paste(star, (pad, pad + 1), star)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(shadow_blur))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(star, (pad, pad), star)
    return canvas

def create_vpa_cockade(size: int = 20) -> Image.Image:
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(215, 175, 45, 255), outline=(125, 90, 15, 255))
    r_inner = r_outer - 2.0
    draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(195, 25, 25, 255), outline=(120, 15, 15, 255))

    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im

def apply_ambient_drop_shadow(canvas: Image.Image, radius: float = 1.8) -> Image.Image:
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

def enforce_border(canvas: Image.Image) -> Image.Image:
    pixels = canvas.load()
    w, h = TARGET_SIZE
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)
    return canvas

# --- BUILDERS ---

def build_semiconductor_ambition() -> Image.Image:
    # 1. VIE_semiconductor_ambition: Silicon Wafer Die, Tech Pedestal, Laurels, 3D Gold Star
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_energy_resources" / "microschip_production.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade on pedestal
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    return enforce_border(canvas)

def build_chip_design() -> Image.Image:
    # 2. VIE_chip_design: Wafer Die Grid & Microprocessor with Gold Pins & Laurels
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "taiwan" / "TAI_tsmc.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Central microprocessor IC chip covering the text: square ceramic chip with gold core
    draw = ImageDraw.Draw(canvas)
    cx, cy = TARGET_SIZE[0] // 2, 43
    # Ceramic package
    draw.rectangle([cx - 14, cy - 14, cx + 14, cy + 14], fill=(28, 36, 48, 255), outline=(215, 175, 45, 255), width=1)
    # Silicon die in center
    draw.rectangle([cx - 9, cy - 9, cx + 9, cy + 9], fill=(20, 85, 160, 255), outline=(80, 190, 255, 255), width=1)
    # Gold circuit traces
    for dx in (-16, 15):
        for offset in (-8, -3, 2, 7):
            draw.line([(cx + dx, cy + offset), (cx + dx + (2 if dx < 0 else -2), cy + offset)], fill=(245, 205, 45, 255), width=1)
    for dy in (-16, 15):
        for offset in (-8, -3, 2, 7):
            draw.line([(cx + offset, cy + dy), (cx + offset, cy + dy + (2 if dy < 0 else -2))], fill=(245, 205, 45, 255), width=1)
    # Center mini gold star on silicon die
    mini_star = create_gold_star(10)
    canvas.paste(mini_star, (cx - mini_star.width // 2, cy - mini_star.height // 2), mini_star)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    return enforce_border(canvas)

def build_osat_packaging() -> Image.Image:
    # 3. VIE_osat_packaging: Automated Precision Robotic Assembly Arm, Gear & Laurels
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_economy" / "economic_robots.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade on gear rim
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    return enforce_border(canvas)

def build_chip_engineers() -> Image.Image:
    # 4. VIE_chip_engineers: STEM Technological University Hall, Gear & Laurels
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "japan" / "goal_JAP_tech_university.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade on university gear rim
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    return enforce_border(canvas)

def build_semiconductor_fab() -> Image.Image:
    # 5. VIE_semiconductor_fab: Cleanroom High-Tech Fab Facility, Shield, Laurels, 3 Gold Stars
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_economy" / "industry4.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # 3 Faceted 3D Gold Stars across apex (Foundry Fab Capstone)
    s_center = create_gold_star_with_glow(20)
    s_side = create_gold_star_with_glow(15)
    cx = TARGET_SIZE[0] // 2
    canvas.paste(s_center, (cx - s_center.width // 2, -1), s_center)
    canvas.paste(s_side, (cx - 24 - s_side.width // 2, 4), s_side)
    canvas.paste(s_side, (cx + 24 - s_side.width // 2, 4), s_side)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 67), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    return enforce_border(canvas)

def main():
    icons = {
        "semiconductor_ambition": build_semiconductor_ambition(),
        "chip_design": build_chip_design(),
        "osat_packaging": build_osat_packaging(),
        "chip_engineers": build_chip_engineers(),
        "semiconductor_fab": build_semiconductor_fab(),
    }

    # Render showcase
    cols = 5
    rows = 1
    card_w, card_h = 185, 145
    pad_x, pad_y = 20, 20
    header_h = 90

    total_w = pad_x * 2 + cols * card_w + (cols - 1) * 15
    total_h = header_h + rows * card_h + pad_y

    canvas = Image.new("RGBA", (total_w, total_h), (14, 18, 24, 255))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_id = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
        font_name = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
    except Exception:
        font_title = font_sub = font_id = font_name = None

    draw.text((pad_x, 20), "BỘ ICON GFX: CHIẾN LƯỢC BÁN DẪN & VI MẠCH (SEMICONDUCTOR VIETNAM)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "5 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "semiconductor_ambition": "Khát vọng Bán dẫn & AI",
        "chip_design": "Thiết kế Vi mạch (IC Design)",
        "osat_packaging": "Đóng gói & Kiểm thử (OSAT)",
        "chip_engineers": "50.000 Kỹ sư Bán dẫn",
        "semiconductor_fab": "Nhà máy Chế tạo Chip Fab",
    }

    for idx, (stem, img) in enumerate(icons.items()):
        x = pad_x + idx * (card_w + 15)
        y = header_h

        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=8, fill=(22, 28, 38, 255), outline=(45, 60, 80, 255))
        icon_x = x + (card_w - img.width) // 2
        icon_y = y + 10
        canvas.paste(img, (icon_x, icon_y), img)

        t_title = focus_titles.get(stem, stem)
        draw.text((x + 8, y + card_h - 36), stem, fill=(240, 200, 80, 255), font=font_id)
        draw.text((x + 8, y + card_h - 20), t_title, fill=(200, 215, 230, 255), font=font_name)

    out = BRAIN_DIR / "semiconductor_icons_showcase.png"
    canvas.save(out)
    print("Saved semiconductor showcase to", out)

if __name__ == "__main__":
    main()
