import re
import struct
import sys
from pathlib import Path
from PIL import Image

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    print("=" * 60)
    print("COMPREHENSIVE DDS & GFX AUDIT")
    print("=" * 60)

    # 1. Audit all DDS files on disk
    dds_files = list(Path("gfx").glob("**/*.dds"))
    print(f"Total DDS files found in gfx/: {len(dds_files)}")

    dds_errors = []
    blank_warnings = []

    for p in dds_files:
        data = p.read_bytes()
        rel_p = str(p).replace("\\", "/")

        if len(data) < 128:
            dds_errors.append((rel_p, f"File too small ({len(data)} bytes)"))
            continue
        if data[:4] != b"DDS ":
            dds_errors.append((rel_p, f"Invalid magic header: {data[:4]}"))
            continue

        header = data[4:128]
        size, flags, height, width, pitch, depth, mipmaps = struct.unpack("<7I", header[:28])

        if size != 124:
            dds_errors.append((rel_p, f"Invalid header size {size} (expected 124)"))

        pf = header[72:104]
        pf_size, pf_flags, fourcc, bitcount, rmask, gmask, bmask, amask = struct.unpack("<2I4s5I", pf)
        fourcc_str = fourcc.decode("latin1", errors="replace").strip("\x00")

        if width <= 0 or height <= 0:
            dds_errors.append((rel_p, f"Invalid dimensions: {width}x{height}"))
            continue

        # Expected size verification for uncompressed
        if not fourcc_str:
            if bitcount == 32 and mipmaps <= 1:
                expected_size = 128 + width * height * 4
                if len(data) != expected_size:
                    dds_errors.append((rel_p, f"Size mismatch: {len(data)} bytes vs expected {expected_size} bytes"))
            elif bitcount == 24 and mipmaps <= 1:
                expected_size = 128 + width * height * 3
                if len(data) != expected_size:
                    dds_errors.append((rel_p, f"Size mismatch: {len(data)} bytes vs expected {expected_size} bytes"))

        # Try opening with PIL and check for empty/blank content
        try:
            with Image.open(p) as img:
                # Check for completely blank/transparent image
                extrema = img.getextrema()
                if img.mode == "RGBA":
                    # extrema is ((min_r, max_r), (min_g, max_g), (min_b, max_b), (min_a, max_a))
                    alpha_ext = extrema[3]
                    if alpha_ext[1] == 0:
                        blank_warnings.append((rel_p, "Image is 100% transparent (alpha=0 everywhere)"))
        except Exception as e:
            dds_errors.append((rel_p, f"Pillow failed to decode DDS: {e}"))

    print(f"\nDDS Format Errors: {len(dds_errors)}")
    for f, err in dds_errors:
        print(f"  [ERROR] {f}: {err}")

    print(f"DDS Content Warnings: {len(blank_warnings)}")
    for f, warn in blank_warnings:
        print(f"  [WARN] {f}: {warn}")

    # 2. Check all .gfx files in interface/
    gfx_files = list(Path("interface").glob("*.gfx"))
    print(f"\nChecking {len(gfx_files)} .gfx files in interface/...")

    all_sprites = {}
    missing_texture_files = []

    for g in gfx_files:
        txt = g.read_text(encoding="utf-8", errors="replace")
        pattern = re.compile(r"spriteType\s*=\s*\{([^}]+)\}", re.DOTALL)
        for m in pattern.finditer(txt):
            block = m.group(1)
            name_m = re.search(r'name\s*=\s*"([^"]+)"', block) or re.search(r'name\s*=\s*([^\s]+)', block)
            tex_m = re.search(r'texturefile\s*=\s*"([^"]+)"', block) or re.search(r'texturefile\s*=\s*([^\s]+)', block)
            if name_m and tex_m:
                sname = name_m.group(1).strip()
                tpath = tex_m.group(1).strip().replace("\\", "/")
                all_sprites[sname] = (tpath, g.name)

                # Check if texturefile exists in mod
                p_tex = Path(tpath)
                if not p_tex.exists():
                    missing_texture_files.append((g.name, sname, tpath))

    print(f"Total spriteType definitions: {len(all_sprites)}")
    print(f"Missing texturefiles referenced in .gfx: {len(missing_texture_files)}")
    for gname, sname, tpath in missing_texture_files:
        print(f"  [MISSING FILE] in {gname}: sprite '{sname}' references non-existent '{tpath}'")

    # 3. Check all focus icon references in VIE_md_focus.txt
    txt_focus = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")
    focus_pattern = re.compile(r"(?m)^\tfocus\s*=\s*\{")
    matches = list(focus_pattern.finditer(txt_focus))
    
    missing_sprites_in_focus = []
    vanilla_fallback_icons = []
    custom_gfx_icons = []

    for m in matches:
        start = m.start()
        brace = 1
        for j in range(m.end(), len(txt_focus)):
            if txt_focus[j] == '{': brace += 1
            elif txt_focus[j] == '}':
                brace -= 1
                if brace == 0:
                    end = j + 1
                    break
        block = txt_focus[start:end]
        fid_m = re.search(r'\bid\s*=\s*(\S+)', block)
        fid = fid_m.group(1) if fid_m else "unknown"
        icon_m = re.search(r'\bicon\s*=\s*(\S+)', block)
        if not icon_m:
            continue
        icon = icon_m.group(1)

        if icon.startswith("GFX_"):
            custom_gfx_icons.append((fid, icon))
            if icon not in all_sprites:
                missing_sprites_in_focus.append((fid, icon))
        else:
            vanilla_fallback_icons.append((fid, icon))

    print(f"\nFocus Tree Icon References:")
    print(f"  Custom GFX_ references: {len(custom_gfx_icons)}")
    print(f"  Vanilla / MD fallback icon tags: {len(vanilla_fallback_icons)}")
    print(f"  Missing spriteType definitions for GFX_ icons: {len(missing_sprites_in_focus)}")
    for fid, icon in missing_sprites_in_focus:
        print(f"  [MISSING SPRITE DEF] Focus {fid} references unknown '{icon}'")

    # 4. Check Decision Category icons & Decision icons
    dec_cat_files = list(Path("common/decisions/categories").glob("*.txt"))
    for dcf in dec_cat_files:
        txt_cat = dcf.read_text(encoding="utf-8", errors="replace")
        for icon_match in re.finditer(r'\bicon\s*=\s*(\S+)', txt_cat):
            icon = icon_match.group(1)
            if icon.startswith("GFX_") and icon not in all_sprites:
                print(f"  [MISSING SPRITE DEF] Decision category in {dcf.name} references unknown '{icon}'")

    # 5. Check Event pictures
    event_files = list(Path("events").glob("*.txt"))
    missing_event_pictures = []
    for ef in event_files:
        txt_ev = ef.read_text(encoding="utf-8", errors="replace")
        for pic_match in re.finditer(r'\bpicture\s*=\s*(\S+)', txt_ev):
            pic = pic_match.group(1)
            if pic.startswith("GFX_") and pic not in all_sprites:
                missing_event_pictures.append((ef.name, pic))

    print(f"Missing event picture sprites in events/: {len(missing_event_pictures)}")
    for efname, pic in missing_event_pictures[:20]:
        print(f"  [MISSING EVENT PIC] in {efname}: '{pic}'")

    print("\n" + "=" * 60)
    print("AUDIT COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()
