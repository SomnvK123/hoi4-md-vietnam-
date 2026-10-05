import sys
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")
TARGET_SIZE = (93, 91)

def create_gold_star(size: int) -> Image.Image:
    import math
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
        draw.polygon([center, tip, valley_left], fill=(255, 245, 110, 150))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(190, 140, 10, 160))
    return im

def create_vpa_cockade(size: int = 24, naval: bool = False) -> Image.Image:
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

def add_drop_shadow(im: Image.Image, radius: float = 2.0, offset=(0, 2)) -> Image.Image:
    """Creates a soft, realistic HOI4-style ambient drop shadow."""
    canvas = Image.new("RGBA", im.size, (0, 0, 0, 0))
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    shadow.paste(im, offset, im)
    r, g, b, a = shadow.split()
    black = Image.new("L", im.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(radius))
    # Multiply alpha slightly for nice contrast
    shadow_a = shadow.split()[-1].point(lambda p: int(p * 0.85))
    shadow = Image.merge("RGBA", (black, black, black, shadow_a))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(im, (0, 0), im)
    return canvas

def build_painterly_sf_sapper() -> Image.Image:
    """Redraw sf_sapper in true HOI4 / Millennium Dawn painterly style."""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    
    # 1. Base wreath & medal frame from MD: iran_commie_knife or special_forces
    base_p = MD_GOALS / "iran" / "iran_commie_knife.dds"
    base = Image.open(base_p).convert("RGBA")
    
    # Scale to fill 93x91 nicely
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    
    # Position base medal
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, (TARGET_SIZE[1] - base.height) // 2 + 1), base)
    
    # 2. Add Dac Cong lightning bolts in brilliant golden electricity
    draw = ImageDraw.Draw(canvas)
    # Left lightning bolt
    draw.polygon([(26, 30), (32, 40), (28, 41), (34, 52), (25, 43), (29, 42)], fill=(255, 235, 80, 240), outline=(210, 160, 20, 255))
    # Right lightning bolt
    draw.polygon([(67, 30), (61, 40), (65, 41), (59, 52), (68, 43), (64, 42)], fill=(255, 235, 80, 240), outline=(210, 160, 20, 255))
    
    # 3. Add faceted 3D Gold Star at apex replacing the red star
    star = create_gold_star(22)
    # Shadow for star
    star_shadow = Image.new("RGBA", (26, 26), (0, 0, 0, 0))
    star_shadow.paste(star, (2, 3), star)
    star_shadow = Image.merge("RGBA", (Image.new("L", star_shadow.size, 0), Image.new("L", star_shadow.size, 0), Image.new("L", star_shadow.size, 0), star_shadow.split()[-1])).filter(ImageFilter.GaussianBlur(1.0))
    canvas.paste(star_shadow, (34, 1), star_shadow)
    canvas.paste(star, (36, 1), star)
    
    # 4. Add VPA Cockade on the lower banner
    cockade = create_vpa_cockade(16, naval=False)
    canvas.paste(cockade, (38, 68), cockade)
    
    # Enforce 1px transparent border
    pixels = canvas.load()
    w, h = TARGET_SIZE
    for x in range(w):
        pixels[x, 0] = (0, 0, 0, 0)
        pixels[x, h - 1] = (0, 0, 0, 0)
    for y in range(h):
        pixels[0, y] = (0, 0, 0, 0)
        pixels[w - 1, y] = (0, 0, 0, 0)
        
    return canvas

def build_painterly_sf_marine() -> Image.Image:
    """Redraw sf_marine in true HOI4 / Millennium Dawn painterly style."""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    
    # Base: amphibious_assault.dds (magnificent sculpted anchor, crossed rifles, navy blue medallion, bronze wreath)
    base_p = MD_GOALS / "00_navy" / "amphibious_assault.dds"
    base = Image.open(base_p).convert("RGBA")
    
    # Enhance vibrance & contrast
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    
    # Resize to fit 93x91
    base = base.resize((82, 75), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, (TARGET_SIZE[1] - base.height) // 2 - 1), base)
    
    # Place Vietnam People's Navy cockade in the center over the anchor crossbar
    cockade = create_vpa_cockade(20, naval=True)
    # Add shadow to cockade
    c_shadow = Image.new("RGBA", (26, 26), (0, 0, 0, 0))
    c_shadow.paste(cockade, (3, 4), cockade)
    c_shadow = Image.merge("RGBA", (Image.new("L", c_shadow.size, 0), Image.new("L", c_shadow.size, 0), Image.new("L", c_shadow.size, 0), c_shadow.split()[-1])).filter(ImageFilter.GaussianBlur(1.2))
    canvas.paste(c_shadow, (34, 34), c_shadow)
    canvas.paste(cockade, (36, 34), cockade)
    
    # Top faceted gold star
    star = create_gold_star(18)
    canvas.paste(star, (37, 2), star)
    
    # Enforce 1px transparent border
    pixels = canvas.load()
    w, h = TARGET_SIZE
    for x in range(w):
        pixels[x, 0] = (0, 0, 0, 0)
        pixels[x, h - 1] = (0, 0, 0, 0)
    for y in range(h):
        pixels[0, y] = (0, 0, 0, 0)
        pixels[w - 1, y] = (0, 0, 0, 0)
        
    return canvas

def make_comparison_showcase():
    out_dir = BRAIN_DIR / "art_style_study"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Load old versions
    old_sapper = Image.open(ROOT / "assets" / "focus_icons" / "png" / "sf_sapper.png")
    old_marine = Image.open(ROOT / "assets" / "focus_icons" / "png" / "sf_marine.png")
    
    # Build new versions
    new_sapper = build_painterly_sf_sapper()
    new_marine = build_painterly_sf_marine()
    
    # Save individual new pngs
    new_sapper.save(out_dir / "new_sf_sapper.png")
    new_marine.save(out_dir / "new_sf_marine.png")
    
    # Create side-by-side comparison board (700x320)
    board = Image.new("RGBA", (720, 360), (18, 22, 28, 255))
    draw = ImageDraw.Draw(board)
    
    # Fonts
    from PIL import ImageFont
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 18)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_h = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 15)
        font_tag = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
        font_note = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    except Exception:
        font_title = font_sub = font_h = font_tag = font_note = None

    # Title
    draw.text((24, 16), "SO SÁNH PHONG CÁCH VẼ FOCUS ICON (HOI4 / MILLENNIUM DAWN)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((24, 42), "Trái: Vẽ vector phẳng bằng Pillow (Bị thô)  |  Phải: Phong cách Minh họa Sơn dầu Tả thực chuẩn MD", fill=(160, 180, 200, 255), font=font_sub)
    
    # Column 1: Sapper Old vs New
    draw.rounded_rectangle([24, 80, 345, 335], radius=8, fill=(26, 32, 42, 255), outline=(50, 65, 85, 255))
    draw.text((36, 90), "1. sf_sapper (Binh chủng Đặc công)", fill=(240, 240, 240, 255), font=font_h)
    
    # Old card
    draw.rounded_rectangle([36, 118, 175, 258], radius=6, fill=(14, 18, 24, 255), outline=(90, 50, 50, 255))
    draw.text((44, 126), "CŨ: Vector thô", fill=(240, 100, 100, 255), font=font_tag)
    board.paste(old_sapper, (59, 153), old_sapper)
    
    # New card
    draw.rounded_rectangle([190, 118, 330, 258], radius=6, fill=(14, 18, 24, 255), outline=(50, 130, 75, 255))
    draw.text((198, 126), "MỚI: Sơn dầu 3D", fill=(100, 240, 140, 255), font=font_tag)
    board.paste(new_sapper, (214, 153), new_sapper)
    draw.text((36, 276), "• Có chất kim loại đồng, lưỡi thép, chiều sâu", fill=(165, 185, 205, 255), font=font_note)
    draw.text((36, 298), "• Nguyệt quế nổi khối & sao vàng 3D chân thực", fill=(165, 185, 205, 255), font=font_note)
    
    # Column 2: Marine Old vs New
    draw.rounded_rectangle([370, 80, 695, 335], radius=8, fill=(26, 32, 42, 255), outline=(50, 65, 85, 255))
    draw.text((382, 90), "2. sf_marine (Hải quân Đánh bộ)", fill=(240, 240, 240, 255), font=font_h)
    
    # Old card
    draw.rounded_rectangle([382, 118, 522, 258], radius=6, fill=(14, 18, 24, 255), outline=(90, 50, 50, 255))
    draw.text((390, 126), "CŨ: Vector thô", fill=(240, 100, 100, 255), font=font_tag)
    board.paste(old_marine, (405, 153), old_marine)
    
    # New card
    draw.rounded_rectangle([538, 118, 678, 258], radius=6, fill=(14, 18, 24, 255), outline=(50, 130, 75, 255))
    draw.text((546, 126), "MỚI: Sơn dầu 3D", fill=(100, 240, 140, 255), font=font_tag)
    board.paste(new_marine, (562, 153), new_marine)
    draw.text((382, 276), "• Mỏ neo thép đúc, súng trường tả thực", fill=(165, 185, 205, 255), font=font_note)
    draw.text((382, 298), "• Khung nguyệt quế đồng & cockade hải quân", fill=(165, 185, 205, 255), font=font_note)
    
    comp_path = BRAIN_DIR / "focus_art_style_comparison.png"
    board.save(comp_path)
    print("Saved comparison showcase:", comp_path)

if __name__ == "__main__":
    make_comparison_showcase()

