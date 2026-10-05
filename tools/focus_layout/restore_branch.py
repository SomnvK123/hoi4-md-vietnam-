"""Put one branch (the component that contains <focus_id>) back exactly as in a backup of VIE_md_focus.txt.
Usage: python tools/focus_layout/restore_branch.py <backup_file> <focus_id>
Blocks are replaced with the backup text; offsets are then re-expressed so absolute positions equal the backup's.
Run from the repo root."""
import re, sys, importlib.util

backup, probe = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('tidy_layout', 'tools/focus_layout/tidy_layout.py')
T = importlib.util.module_from_spec(spec)
sys.argv = ['tidy_layout.py', '-']
spec.loader.exec_module(T)
members = next(c for c in T.components() if probe in c)

P = 'common/national_focus/VIE_md_focus.txt'
cur = open(P, 'rb').read().decode('utf-8').replace('\r\n', '\n')
old = open(backup, 'rb').read().decode('utf-8').replace('\r\n', '\n')


def blocks(text):
    out = {}; spans = {}
    for m in re.finditer(r'\n\tfocus = \{', text):
        st = m.end(); d = 1; i = st
        while d:
            d += {'{': 1, '}': -1}.get(text[i], 0); i += 1
        b = text[m.start() + 1:i]
        fid = re.search(r'\bid = (\w+)', b).group(1)
        out[fid] = b; spans[fid] = (m.start() + 1, i)
    return out, spans


def absolute(bl):
    F = {}
    for f, b in bl.items():
        x = int(re.search(r'\n\t\tx = (-?\d+)', b).group(1)); y = int(re.search(r'\n\t\ty = (-?\d+)', b).group(1))
        r = re.search(r'relative_position_id = (\w+)', b)
        F[f] = (x, y, r.group(1) if r else None)
    memo = {}
    def ab(f):
        if f in memo: return memo[f]
        x, y, r = F[f]
        if r:
            px, py = ab(r); x += px; y += py
        memo[f] = (x, y); return memo[f]
    return {f: ab(f) for f in F}, F


old_bl, _ = blocks(old)
old_abs, _ = absolute(old_bl)
cur_bl, cur_sp = blocks(cur)
for f in sorted(members, key=lambda z: -cur_sp[z][0]):
    s, k = cur_sp[f]
    cur = cur[:s] + old_bl[f] + cur[k:]
# re-express offsets of every focus whose anchor moved (restored members and everything anchored to them)
cur_bl, cur_sp = blocks(cur)
now_abs, F = absolute(cur_bl)
want = dict(now_abs)
want.update({f: old_abs[f] for f in members})
fixed = 0
for f in sorted(cur_bl, key=lambda z: -cur_sp[z][0]):
    x, y, a = F[f]
    if not a: continue
    dx = want[f][0] - want[a][0]; dy = want[f][1] - want[a][1]
    if (dx, dy) != (x, y):
        s, k = cur_sp[f]
        b = re.sub(r'\n\t\tx = -?\d+\n\t\ty = -?\d+\n\t\trelative_position_id = \w+\n',
                   '\n\t\tx = %d\n\t\ty = %d\n\t\trelative_position_id = %s\n' % (dx, dy, a), cur[s:k])
        cur = cur[:s] + b + cur[k:]
        fixed += 1
        cur_bl, cur_sp = blocks(cur)
open(P, 'wb').write(cur.replace('\n', '\r\n').encode('utf-8'))
final_abs, _ = absolute(blocks(cur)[0])
bad = [f for f in members if final_abs[f] != old_abs[f]]
print('restored', len(members), 'focuses; re-expressed offsets:', fixed, '; mismatches:', bad[:5])
xs = [old_abs[f][0] for f in members]; ys = [old_abs[f][1] for f in members]
print('restored extent x', min(xs), max(xs), 'y', min(ys), max(ys))
