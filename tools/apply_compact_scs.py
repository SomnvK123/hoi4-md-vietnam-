import sys, os, re
sys.path.insert(0, os.path.abspath("."))
import tools.test_compact_scs as tcs

file_path = "common/national_focus/VIE_md_focus.txt"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Parse all focus blocks in text
focus_blocks = {}
pos = 0
while True:
    m = re.search(r'\bfocus\s*=\s*\{', text[pos:])
    if not m:
        break
    start = pos + m.start()
    depth = 0
    i = pos + m.end() - 1
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                block = text[start:i+1]
                id_m = re.search(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', block, re.MULTILINE)
                if id_m:
                    fid = id_m.group(1)
                    focus_blocks[fid] = (start, i+1, block)
                pos = i + 1
                break
        i += 1
    else:
        break

print(f"Total focus blocks parsed: {len(focus_blocks)}")

for fid in tcs.compact_scs:
    if fid not in focus_blocks:
        print(f"ERROR: missing focus {fid}")
        sys.exit(1)

print("All 24 SCS focuses found in file.")

replacements = []
for fid, layout in tcs.compact_scs.items():
    start, end, block = focus_blocks[fid]
    
    # Replace x = ..., y = ..., relative_position_id = ...
    new_block = block
    new_block = re.sub(r'(\bx\s*=\s*)-?\d+', rf'\g<1>{layout["dx"]}', new_block, count=1)
    new_block = re.sub(r'(\by\s*=\s*)-?\d+', rf'\g<1>{layout["dy"]}', new_block, count=1)
    
    # relative_position_id
    if re.search(r'\brelative_position_id\s*=\s*[a-zA-Z0-9_]+', new_block):
        new_block = re.sub(r'(\brelative_position_id\s*=\s*)[a-zA-Z0-9_]+', rf'\g<1>{layout["rel"]}', new_block, count=1)
    else:
        new_block = re.sub(r'(\by\s*=\s*-?\d+\n)', rf'\g<1>\t\trelative_position_id = {layout["rel"]}\n', new_block, count=1)
    
    replacements.append((start, end, new_block))

# Sort by start descending
replacements.sort(key=lambda x: x[0], reverse=True)

new_text = text
for start, end, new_block in replacements:
    new_text = new_text[:start] + new_block + new_text[end:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Successfully updated {len(replacements)} SCS focuses in {file_path}")
