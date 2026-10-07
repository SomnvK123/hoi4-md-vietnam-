"""Build game-ready Idea Icons for XCB-01 and K9 Localization.

Complies with Art Style Guide (01_hoi4_md_art_style_analysis.md & 04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md):
- 60x68 Canvas (standard Paradox Idea size, exactly 16,448 bytes BGRA uncompressed DDS)
- Clean alpha cutout with anti-aliasing and morphology closing
- Contrast & color grading for crisp readability at small scale
- Unsharp mask sharpening for metallic edges
- Pure alpha=0 outer 1-pixel border
- Register GFX in interface/VIE_md_ideas.gfx
- Update picture references in common/ideas/VIE_md_ideas_p15.txt
"""

import struct
from collections import deque
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "ideas" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "ideas"
GFX_FILE = ROOT / "interface" / "VIE_md_ideas.gfx"
IDEAS_FILE = ROOT / "common" / "ideas" / "VIE_md_ideas_p15.txt"

TARGET_SIZE = (60, 68)
MAX_CONTENT_SIZE = (56, 64)


def clean_cutout(img_path: Path, dist_thresh: float = 15.0, blur_rad: float = 0.8) -> Image.Image:
    """Extract foreground cutout using multi-seed BFS flood fill and morphological closing."""
    img = Image.open(img_path).convert("RGB")
    arr = np.array(img, dtype=float)
    h, w, _ = arr.shape

    # Sample corners to determine true studio backdrop color
    corners = np.vstack([
        arr[:15, :15].reshape(-1, 3),
        arr[:15, -15:].reshape(-1, 3),
        arr[-15:, :15].reshape(-1, 3),
        arr[-15:, -15:].reshape(-1, 3)
    ])
    bg_col = corners.mean(axis=0)

    dists = np.linalg.norm(arr - bg_col, axis=2)
    is_similar_to_bg = dists < dist_thresh

    # BFS from outside boundaries only
    visited = np.zeros((h, w), dtype=bool)
    queue = deque()

    for x in range(w):
        if is_similar_to_bg[0, x]:
            queue.append((0, x))
            visited[0, x] = True
        if is_similar_to_bg[h - 1, x]:
            queue.append((h - 1, x))
            visited[h - 1, x] = True
    for y in range(h):
        if is_similar_to_bg[y, 0] and not visited[y, 0]:
            queue.append((y, 0))
            visited[y, 0] = True
        if is_similar_to_bg[y, w - 1] and not visited[y, w - 1]:
            queue.append((y, w - 1))
            visited[y, w - 1] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx]:
                if is_similar_to_bg[ny, nx]:
                    visited[ny, nx] = True
                    queue.append((ny, nx))

    fg_mask = ~visited

    # Morphological closing: Dilation then Erosion to seal any ground cracks
    mask_im = Image.fromarray((fg_mask * 255).astype(np.uint8), mode="L")
    closed = mask_im.filter(ImageFilter.MaxFilter(size=7)).filter(ImageFilter.MinFilter(size=7))
    alpha_smooth = closed.filter(ImageFilter.GaussianBlur(radius=blur_rad))

    r, g, b = img.split()
    cutout = Image.merge("RGBA", (r, g, b, alpha_smooth))
    bbox = alpha_smooth.getbbox()
    if bbox:
        cutout = cutout.crop(bbox)

    return cutout


def fit_and_polish_idea(cutout: Image.Image) -> Image.Image:
    """Scale, polish contrast, sharpen, and center onto 60x68 idea canvas."""
    cw, ch = cutout.size
    scale = min(MAX_CONTENT_SIZE[0] / cw, MAX_CONTENT_SIZE[1] / ch)
    new_w = max(1, int(cw * scale))
    new_h = max(1, int(ch * scale))

    # Downsample with Lanczos
    resized = cutout.resize((new_w, new_h), Image.Resampling.LANCZOS)

    # Color & Contrast grading for small UI icon
    r, g, b, a = resized.split()
    rgb = Image.merge("RGB", (r, g, b))
    rgb = ImageEnhance.Contrast(rgb).enhance(1.15)
    rgb = ImageEnhance.Color(rgb).enhance(1.10)
    rgb = rgb.filter(ImageFilter.UnsharpMask(radius=1.1, percent=125, threshold=2))

    r2, g2, b2 = rgb.split()
    polished = Image.merge("RGBA", (r2, g2, b2, a))

    # Center on transparent canvas
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    offset_x = (TARGET_SIZE[0] - new_w) // 2
    offset_y = (TARGET_SIZE[1] - new_h) // 2
    canvas.paste(polished, (offset_x, offset_y), polished)

    # Zero-out 1-pixel outer border
    w, h = TARGET_SIZE
    pixels = canvas.load()
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)

    return canvas


def save_idea_dds_and_png(img: Image.Image, stem: str):
    """Save 60x68 canvas as PNG and 32-bit BGRA uncompressed DDS."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert img.size == TARGET_SIZE
    assert img.mode == "RGBA"

    png_path = PNG_DIR / f"{stem}.png"
    img.save(png_path)

    # 32-bit BGRA uncompressed DDS standard for HOI4
    r, g, b, a = img.split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()
    header = b"DDS " + struct.pack(
        "<7I11I8I5I",
        124, 0x100F, TARGET_SIZE[1], TARGET_SIZE[0], TARGET_SIZE[0] * 4, 0, 0, *([0] * 11),
        32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000, 0x1000, 0, 0, 0, 0
    )
    assert len(header) == 128
    dds_path = DDS_DIR / f"{stem}.dds"
    dds_path.write_bytes(header + data)
    assert len(dds_path.read_bytes()) == 16448
    print(f"  [SAVED] {stem} -> PNG & DDS ({len(dds_path.read_bytes())} bytes)")


def update_gfx():
    """Register the new spriteTypes in interface/VIE_md_ideas.gfx."""
    content = GFX_FILE.read_text(encoding="utf-8")

    new_entries = """
	# 5. Co gioi hoa theo chuan XCB-01 (IFV)
	spriteType = {
		name = "GFX_idea_VIE_xcb01_mechanized"
		texturefile = "gfx/interface/ideas/VIE_idea_xcb01_mechanized.dds"
	}
	spriteType = {
		name = "GFX_idea_VIE_xcb01_mechanized_idea"
		texturefile = "gfx/interface/ideas/VIE_idea_xcb01_mechanized.dds"
	}

	# 6. Noi dia hoa phao tu hanh K9 (SPG)
	spriteType = {
		name = "GFX_idea_VIE_k9_localization"
		texturefile = "gfx/interface/ideas/VIE_idea_k9_localization.dds"
	}
	spriteType = {
		name = "GFX_idea_VIE_k9_localization_idea"
		texturefile = "gfx/interface/ideas/VIE_idea_k9_localization.dds"
	}
"""

    if "GFX_idea_VIE_xcb01_mechanized" not in content:
        idx = content.rfind("}")
        if idx != -1:
            content = content[:idx] + new_entries + content[idx:]
            GFX_FILE.write_text(content, encoding="utf-8")
            print("  [GFX UPDATED] Registered XCB-01 and K9 in VIE_md_ideas.gfx")
    else:
        print("  [GFX OK] Already registered in VIE_md_ideas.gfx")


def update_ideas_file():
    """Update picture tags in common/ideas/VIE_md_ideas_p15.txt."""
    text = IDEAS_FILE.read_text(encoding="utf-8")
    
    text = text.replace(
        "VIE_xcb01_mechanized_idea = {\n\t\t\tpicture = army_planning",
        "VIE_xcb01_mechanized_idea = {\n\t\t\tpicture = VIE_xcb01_mechanized"
    )
    
    text = text.replace(
        "VIE_k9_localization_idea = {\n\t\t\tpicture = army_planning",
        "VIE_k9_localization_idea = {\n\t\t\tpicture = VIE_k9_localization"
    )
    
    IDEAS_FILE.write_text(text, encoding="utf-8")
    print("  [IDEAS UPDATED] Updated picture tags in VIE_md_ideas_p15.txt")


def main():
    print("=== Processing XCB-01 and K9 Idea Icons (Refined Pipeline) ===")
    src1 = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\8c565b65-55eb-450c-9646-38cab155482e\xcb01_ifv_idea_1791394406510.jpg")
    src2 = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\8c565b65-55eb-450c-9646-38cab155482e\k9_artillery_idea_1791394428032.jpg")

    print("Extracting XCB-01 with BFS + morphological closing...")
    cutout1 = clean_cutout(src1, dist_thresh=15.0, blur_rad=0.8)
    idea1 = fit_and_polish_idea(cutout1)
    save_idea_dds_and_png(idea1, "VIE_idea_xcb01_mechanized")

    print("Extracting K9 Localization with BFS + morphological closing...")
    cutout2 = clean_cutout(src2, dist_thresh=14.0, blur_rad=0.8)
    idea2 = fit_and_polish_idea(cutout2)
    save_idea_dds_and_png(idea2, "VIE_idea_k9_localization")

    update_gfx()
    update_ideas_file()
    print("=== Refined icons built successfully! ===")


if __name__ == "__main__":
    main()
