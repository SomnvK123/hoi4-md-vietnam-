# -*- coding: utf-8 -*-
import os

# 1. Update common/national_focus/VIE_md_focus.txt
with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    focus_text = f.read()

# Add version line at top
v34_line = "## v34 (10/10/2026): De an V32.1 - tai thiet ke hoan chinh nhanh Hai quan Nhan dan Viet Nam (40 focus N00, T01-T04, C01-C06, S01-S05, W01-W07, L01-L05, X01-X05, Y01-Y05, F01-F02). Cay focus: 332 -> 372 focus.\n"
idx_v33 = focus_text.find("## v33")
if idx_v33 != -1:
    focus_text = focus_text[:idx_v33] + v34_line + focus_text[idx_v33:]
else:
    print('WARNING: ## v33 not found in header')

# Read new focuses
with open('scratch/v32_focuses.txt', 'r', encoding='utf-8') as f:
    new_focuses_code = f.read()

nav_marker = "# Nhánh Hải quân & CNQP Hải quân đã được gỡ bỏ"
if nav_marker in focus_text:
    replacement = f"""\t# ======================================================================
\t# NHANH HAI QUAN NHAN DAN VIET NAM V32.1 (40 FOCUS)
\t# ======================================================================

{new_focuses_code}"""
    focus_text = focus_text.replace(nav_marker, replacement, 1)
    print('Successfully inserted 40 naval focuses at nav_marker!')
else:
    print('ERROR: nav_marker not found in VIE_md_focus.txt!')

with open('common/national_focus/VIE_md_focus.txt', 'w', encoding='utf-8') as f:
    f.write(focus_text)
print('Updated common/national_focus/VIE_md_focus.txt')

# 2. Append to localisation/english/replace/VIE_md_vi_military_l_english.yml
with open('scratch/v32_loc.txt', 'r', encoding='utf-8') as f:
    new_loc = f.read()

with open('localisation/english/replace/VIE_md_vi_military_l_english.yml', 'r', encoding='utf-8') as f:
    current_loc = f.read()

header_loc = """
 ### ====================================================================
 ### V32.1: HAI QUAN NHAN DAN VIET NAM (40 FOCUS + IDEAS + DECISIONS)
 ### ====================================================================
"""

updated_loc = current_loc.rstrip() + "\n" + header_loc + new_loc + "\n"
with open('localisation/english/replace/VIE_md_vi_military_l_english.yml', 'w', encoding='utf-8') as f:
    f.write(updated_loc)
print('Updated localisation/english/replace/VIE_md_vi_military_l_english.yml')
