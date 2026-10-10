import json
import re

with open('scratch/chatgpt_s4.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for JSON containing 'mapping'
# Look for start of JSON object containing "mapping":
m = re.search(r'\{[^{}]*"mapping"\s*:\s*\{', text)
if m:
    print('Found mapping pattern at', m.start())
    # Let's try to extract the entire JSON object
    # Or find all "parts": [ ... ] or "text": "..."
    # In newer ChatGPT, message parts might look like: "text": "..." or "parts": ["..."]
    pass
else:
    print('Pattern not matched directly, let search index of "mapping"')
    idx = text.find('"mapping"')
    print('Index:', idx)
    print(text[idx-50:idx+200])

# Let's extract all strings that look like markdown or conversation
# Usually messages have "author": {"role": ...} or "content": ...
# Let's search for "role": "user" and "role": "assistant"
print('User roles count:', text.count('"role":"user"'))
print('Assistant roles count:', text.count('"role":"assistant"'))

# Let's find occurrences of "parts" or "text"
# In modern chatgpt: "message":{"id":..., "author":{"role":"user"|"assistant"}, "content":{"content_type":"text","parts":[...]}}
# Let's search with regex
pattern = r'\"author\":\s*\{\"role\":\s*\"(user|assistant)\"[^}]*\},\"create_time\":[^,]*,\"update_time\":[^,]*,\"content\":\s*\{\"content_type\":\s*\"text\",\s*\"parts\":\s*\[(.*?)\]\}'
# Or more relaxed:
matches = re.finditer(r'\"role\":\s*\"(user|assistant)\".*?\"content_type\":\s*\"text\",\s*\"parts\":\s*\[\"(.*?)\"\]', text)
found = 0
for match in matches:
    found += 1
    role = match.group(1)
    content = match.group(2)
    print(f'=== Message {found} ({role}) ===')
    # unescape unicode and newlines
    content = content.encode('utf-8').decode('unicode_escape', errors='ignore')
    print(content[:500])
    print('...\n')
print(f'Total matched: {found}')
