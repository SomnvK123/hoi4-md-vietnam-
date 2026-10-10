import json
import re

with open('scratch/chatgpt_s9.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# The script does: window.__reactRouterContext.streamController.enqueue("...")
# Let's extract the string inside enqueue(...)
m = re.search(r'enqueue\((.*)\);?', text)
if m:
    arg = m.group(1).strip()
    if arg.endswith(';'):
        arg = arg[:-1]
    # arg is a JSON string literal like "[{\"_1\":2,...}]"
    try:
        parsed_str = json.loads(arg)
        # parsed_str is itself a JSON string representing the stream array
        stream_data = json.loads(parsed_str)
        print('Successfully parsed stream data! Length:', len(stream_data))
        
        # Let's filter out strings in stream_data
        long_strings = [x for x in stream_data if isinstance(x, str) and len(x) > 50]
        print(f'Found {len(long_strings)} long strings!')
        with open('scratch/extracted_naval_chat.md', 'w', encoding='utf-8') as out:
            for i, s in enumerate(long_strings):
                out.write(f'<!-- String {i} (len: {len(s)}) -->\n')
                out.write(s + '\n\n')
        print('Saved to scratch/extracted_naval_chat.md')
    except Exception as e:
        print('Error parsing json:', e)
        # fallback: search for all quoted strings in s9
        strings = re.findall(r'\"([^\"\\]*(?:\\.[^\"\\]*)*)\"', text)
        print('Found raw strings:', len(strings))
