import json
import re

content_file = r"C:\Users\doans\.gemini\antigravity-ide\brain\88944a19-10ef-43c2-9a97-f4fd994609d6\.system_generated\steps\2642\content.md"
with open(content_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Tim enqueue(...)
m = re.findall(r'enqueue\((.*?)\);', text)
print(f"Found {len(m)} enqueue matches")

found_strings = []
for i, arg in enumerate(m):
    try:
        parsed_str = json.loads(arg)
        stream_data = json.loads(parsed_str)
        for item in stream_data:
            if isinstance(item, str) and len(item) > 100:
                found_strings.append(item)
    except Exception as e:
        # try regex for text in parts
        pass

if not found_strings:
    # search directly for parts or long markdown text
    matches = re.finditer(r'\"content_type\":\s*\"text\",\s*\"parts\":\s*\[\"(.*?)\"\]', text)
    for match in matches:
        s = match.group(1).encode('utf-8').decode('unicode_escape', errors='ignore')
        found_strings.append(s)

print(f"Total extracted strings: {len(found_strings)}")

out_path = 'scratch/extracted_new_naval_chat.md'
with open(out_path, 'w', encoding='utf-8') as f:
    for i, s in enumerate(found_strings):
        f.write(f"\n\n<!-- === MESSAGE {i+1} (len: {len(s)}) === -->\n\n")
        f.write(s)

print(f"Saved to {out_path}")
