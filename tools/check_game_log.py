import re, os

log_path = r"C:\Users\doans\OneDrive\Tài liệu\Paradox Interactive\Hearts of Iron IV\logs\error.log"
if not os.path.exists(log_path):
    print("Log not found")
    exit(0)

with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

vie_lines = [l.strip() for l in lines if "VIE" in l or "vietnam" in l.lower()]
print(f"Total VIE error lines: {len(vie_lines)}")

# Group errors
file_errors = {}
for line in vie_lines:
    m = re.search(r'(in file: "([^"]+)"|in ([^ :]+) line)', line)
    target = "other"
    if m:
        target = m.group(2) or m.group(3)
    file_errors.setdefault(target, []).append(line)

for f, errs in file_errors.items():
    print(f"\n=== File: {f} ({len(errs)} errors) ===")
    for e in errs[:5]:
        print("  ", e)
    if len(errs) > 5:
        print(f"   ... and {len(errs) - 5} more")
