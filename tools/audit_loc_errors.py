import sys
import re
from pathlib import Path

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    print("=" * 60)
    print("AUDITING LOCALISATION & FOCUS TREE TEXT")
    print("=" * 60)

    # 1. Parse all localization files
    loc_map = {}
    yaml_errors = []
    yml_files = list(Path("localisation").glob("**/*.yml"))
    print(f"Total .yml files found: {len(yml_files)}")

    for yml in yml_files:
        raw = yml.read_bytes()
        has_bom = raw.startswith(b"\xef\xbb\xbf")
        rel_p = str(yml).replace("\\", "/")

        if not has_bom:
            yaml_errors.append((rel_p, "MISSING UTF-8 BOM (HOI4 requires UTF-8 with BOM for localization)"))

        try:
            txt = raw.decode("utf-8-sig")
        except Exception as e:
            yaml_errors.append((rel_p, f"Encoding error: {e}"))
            continue

        lines = txt.splitlines()
        if not lines:
            continue
        first_line = lines[0].strip()
        if not (first_line.startswith("l_english:") or first_line.startswith("l_vietnamese:")):
            yaml_errors.append((rel_p, f"Invalid header line 1: '{first_line}'"))

        for line_no, line in enumerate(lines[1:], 2):
            line_s = line.strip()
            if not line_s or line_s.startswith("#"):
                continue
            m = re.match(r"^([A-Za-z0-9_.\-]+):(\d*)\s*(.*)$", line_s)
            if m:
                key = m.group(1)
                val = m.group(3).strip()
                if not (val.startswith('"') and val.endswith('"')):
                    yaml_errors.append((rel_p, f"Line {line_no}: Value not properly enclosed in quotes: {val[:40]}"))
                else:
                    loc_map[key] = val[1:-1]
            else:
                yaml_errors.append((rel_p, f"Line {line_no}: Malformed line: {line_s[:60]}"))

    print(f"\nLocalisation syntax errors: {len(yaml_errors)}")
    for f, err in yaml_errors:
        print(f"  [ERROR] {f}: {err}")

    # 2. Check all focuses in VIE_md_focus.txt
    txt_focus = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")
    focus_pattern = re.compile(r"(?m)^\tfocus\s*=\s*\{")
    matches = list(focus_pattern.finditer(txt_focus))
    print(f"\nTotal focuses in VIE_md_focus.txt: {len(matches)}")

    missing_titles = []
    missing_descs = []
    missing_tooltips = []
    missing_ideas = []

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
        if not fid_m:
            continue
        fid = fid_m.group(1)

        # Check title
        if fid not in loc_map:
            missing_titles.append(fid)

        # Check description
        desc_key = fid + "_desc"
        if desc_key not in loc_map:
            missing_descs.append(fid)

        # Check custom tooltips
        for tt_m in re.finditer(r'\btooltip\s*=\s*([A-Za-z0-9_]+)', block):
            tt = tt_m.group(1)
            if tt not in loc_map and not tt.startswith("VIE_ax_") and tt != "yes" and tt != "no":
                missing_tooltips.append((fid, tt))

        for ctt_m in re.finditer(r'\bcustom_effect_tooltip\s*=\s*([A-Za-z0-9_]+)', block):
            ctt = ctt_m.group(1)
            if ctt not in loc_map:
                missing_tooltips.append((fid, ctt))

        # Check ideas added in reward
        for idea_m in re.finditer(r'\badd_ideas\s*=\s*([A-Za-z0-9_]+)', block):
            idea = idea_m.group(1)
            if idea not in loc_map:
                missing_ideas.append((fid, idea))

    print(f"\nFocuses missing title: {len(missing_titles)}")
    for f in missing_titles:
        print(f"  [MISSING TITLE] {f}")

    print(f"Focuses missing description: {len(missing_descs)}")
    for f in missing_descs:
        print(f"  [MISSING DESC] {f}")

    print(f"Missing tooltips referenced in focus tree: {len(missing_tooltips)}")
    for fid, tt in missing_tooltips:
        print(f"  [MISSING TOOLTIP] in focus {fid}: '{tt}'")

    print(f"Missing idea names referenced in focus tree: {len(missing_ideas)}")
    for fid, idn in missing_ideas:
        print(f"  [MISSING IDEA] in focus {fid}: '{idn}'")

if __name__ == "__main__":
    main()
