"""
Function to apply the master layout to VIE_md_focus.txt.
"""
import re

def apply_layout_to_text(content, layout):
    """
    Iterates through all focus blocks in content and replaces x, y, and relative_position_id.
    Preserves all other lines, comments, and structure.
    """
    new_content_parts = []
    last_end = 0

    # find all top-level focus = { ... }
    for m in re.finditer(r'(?m)^\tfocus\s*=\s*\{', content):
        start_idx = m.start()
        # copy content between last_end and start_idx
        new_content_parts.append(content[last_end:start_idx])
        
        brace_count = 1
        end_idx = m.end()
        for i in range(m.end(), len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx = i + 1
                    break
        block_text = content[start_idx:end_idx]
        last_end = end_idx

        # get id
        id_m = re.search(r'\bid\s*=\s*(\S+)', block_text)
        if not id_m:
            new_content_parts.append(block_text)
            continue
        fid = id_m.group(1)
        if fid not in layout:
            new_content_parts.append(block_text)
            continue

        target = layout[fid]
        new_x = target['x']
        new_y = target['y']
        new_rel = target['rel']

        # Replace x = ...
        if re.search(r'\bx\s*=\s*(-?\d+)', block_text):
            block_text = re.sub(r'(\bx\s*=\s*)-?\d+', rf'\g<1>{new_x}', block_text, count=1)
        else:
            # insert after id line
            block_text = re.sub(r'(\bid\s*=\s*\S+)', rf'\1\n\t\tx = {new_x}', block_text, count=1)

        # Replace y = ...
        if re.search(r'\by\s*=\s*(-?\d+)', block_text):
            block_text = re.sub(r'(\by\s*=\s*)-?\d+', rf'\g<1>{new_y}', block_text, count=1)
        else:
            block_text = re.sub(r'(\bx\s*=\s*-?\d+)', rf'\1\n\t\ty = {new_y}', block_text, count=1)

        # Replace or add/remove relative_position_id
        if new_rel is None:
            # remove relative_position_id line if present
            block_text = re.sub(r'\n[ \t]*relative_position_id\s*=\s*\S+', '', block_text, count=1)
        else:
            if re.search(r'\brelative_position_id\s*=\s*\S+', block_text):
                block_text = re.sub(r'(\brelative_position_id\s*=\s*)\S+', rf'\g<1>{new_rel}', block_text, count=1)
            else:
                # add after y line
                block_text = re.sub(r'(\by\s*=\s*-?\d+)', rf'\1\n\t\trelative_position_id = {new_rel}', block_text, count=1)

        new_content_parts.append(block_text)

    new_content_parts.append(content[last_end:])
    return "".join(new_content_parts)

