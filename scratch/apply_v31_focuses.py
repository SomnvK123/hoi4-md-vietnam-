# -*- coding: utf-8 -*-
import os, sys

def apply_changes():
    with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Remove old SF block
    idx_sf = text.find('id = VIE_sf_command')
    assert idx_sf != -1, 'VIE_sf_command not found'
    # Find start of comment block before VIE_sf_command
    comment_marker = '## TRUC 4 LUC LUONG DAC BIET'
    comment_pos = text.rfind(comment_marker, 0, idx_sf)
    if comment_pos != -1:
        # Move up to start of # line
        sf_start = text.rfind('\n', 0, comment_pos)
    else:
        sf_start = text.rfind('focus = {', 0, idx_sf)

    idx_airf = text.find('id = VIE_airf_training_standardization')
    assert idx_airf != -1, 'VIE_airf_training_standardization not found'
    # Keep the comment block before airf
    comment_airf = '## TRÚC 3: PHÒNG KHÔNG - KHÔNG QUÂN'
    airf_start = text.rfind(comment_airf, 0, idx_airf)
    if airf_start == -1:
        airf_start = text.rfind('focus = {', 0, idx_airf)
    else:
        airf_start = text.rfind('\n', 0, airf_start)

    text_no_sf = text[:sf_start] + text[airf_start:]

    # 2. Insert new V31 focuses after VIE_modernize_vpa
    idx_vpa = text_no_sf.find('id = VIE_modernize_vpa')
    assert idx_vpa != -1, 'VIE_modernize_vpa not found'
    vpa_start = text_no_sf.rfind('focus = {', 0, idx_vpa)

    brace_count = 0
    pos = vpa_start
    while pos < len(text_no_sf):
        if text_no_sf[pos] == '{':
            brace_count += 1
        elif text_no_sf[pos] == '}':
            brace_count -= 1
            if brace_count == 0:
                pos += 1
                break
        pos += 1
    vpa_end = pos

    with open('scratch/v31_focuses_generated.txt', 'r', encoding='utf-8') as f:
        v31_content = f.read()

    new_text = text_no_sf[:vpa_end] + "\n\n" + v31_content + text_no_sf[vpa_end:]

    with open('common/national_focus/VIE_md_focus.txt', 'w', encoding='utf-8') as f:
        f.write(new_text)

    print("Successfully updated VIE_md_focus.txt!")

if __name__ == '__main__':
    apply_changes()
