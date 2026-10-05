import glob, re, sys

sys.stdout.reconfigure(encoding='utf-8')

for p in glob.glob('localisation/**/*.yml', recursive=True):
    with open(p, encoding='utf-8-sig', errors='ignore') as fp:
        lines = fp.readlines()
    for idx, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith('#') or s.startswith('l_english:'):
            continue
        unescaped_quotes = []
        i = 0
        while i < len(s):
            if s[i] == '"':
                bs = 0
                j = i - 1
                while j >= 0 and s[j] == '\\':
                    bs += 1
                    j -= 1
                if bs % 2 == 0:
                    unescaped_quotes.append(i)
            i += 1
        
        if len(unescaped_quotes) != 2:
            print(f"{p}:{idx} (unescaped count={len(unescaped_quotes)}): {s}")
