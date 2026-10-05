"""Set absolute positions for some focuses (a JSON {id: [x, y]}) in VIE_md_focus.txt, optionally moving other branches.
Usage: python tools/focus_layout/apply_positions.py <plan.json> [--shift-prefix-ids ids.txt --dx N] [--check-only]
Every focus keeps its anchor; offsets are re-expressed so that all focuses outside the plan keep their absolute
position (unless shifted).  Stops on cell collision or same-row gap < 2.  Run from the repo root."""
import json, re, sys, collections

plan = json.load(open(sys.argv[1]))
args = sys.argv[2:]
shift = {}
if '--shift-ids' in args:
    ids = [l.strip() for l in open(args[args.index('--shift-ids') + 1]) if l.strip()]
    dx = int(args[args.index('--dx') + 1])
    shift = {f: dx for f in ids}
check_only = '--check-only' in args
P = 'common/national_focus/VIE_md_focus.txt'
t = open(P, 'rb').read().decode('utf-8').replace('\r\n', '\n')


def parse(text):
    F = {}; spans = {}; order = []
    for m in re.finditer(r'\n\tfocus = \{', text):
        st = m.end(); d = 1; i = st
        while d:
            d += {'{': 1, '}': -1}.get(text[i], 0); i += 1
        b = text[m.start() + 1:i]
        fid = re.search(r'\bid = (\w+)', b).group(1)
        x = int(re.search(r'\n\t\tx = (-?\d+)', b).group(1)); y = int(re.search(r'\n\t\ty = (-?\d+)', b).group(1))
        r = re.search(r'relative_position_id = (\w+)', b)
        F[fid] = (x, y, r.group(1) if r else None); spans[fid] = (m.start() + 1, i); order.append(fid)
    return F, spans, order


def absolute(F):
    memo = {}
    def ab(f):
        if f in memo: return memo[f]
        x, y, r = F[f]
        if r:
            px, py = ab(r); x += px; y += py
        memo[f] = (x, y); return memo[f]
    return {f: ab(f) for f in F}


F, spans, order = parse(t)
old = absolute(F)
want = dict(old)
for f, dx in shift.items(): want[f] = (old[f][0] + dx, old[f][1])
for f, (x, y) in plan.items():
    assert f in F, f
    want[f] = (x, y)
cells = collections.defaultdict(list)
for f, p in want.items(): cells[p].append(f)
coll = [v for v in cells.values() if len(v) > 1]
rows = collections.defaultdict(list)
for f, (x, y) in want.items(): rows[y].append((x, f))
gaps = []
for y, l in rows.items():
    l.sort()
    for a, b in zip(l, l[1:]):
        if b[0] - a[0] < 2: gaps.append((y, a, b))
idx = {f: i for i, f in enumerate(order)}
print('collisions:', coll[:6], 'same-row gap<2:', gaps[:6])
if coll or gaps or check_only:
    sys.exit(1 if (coll or gaps) else 0)
changed = 0
for f in sorted(F, key=lambda z: -spans[z][0]):
    x, y, a = F[f]
    s, k = spans[f]
    if a:
        dx_ = want[f][0] - want[a][0]; dy_ = want[f][1] - want[a][1]
        if (dx_, dy_) == (x, y): continue
        b = re.sub(r'\n\t\tx = -?\d+\n\t\ty = -?\d+\n\t\trelative_position_id = \w+\n',
                   '\n\t\tx = %d\n\t\ty = %d\n\t\trelative_position_id = %s\n' % (dx_, dy_, a), t[s:k])
    else:
        if (x, y) == want[f]: continue
        b = re.sub(r'\n\t\tx = -?\d+\n\t\ty = -?\d+\n', '\n\t\tx = %d\n\t\ty = %d\n' % want[f], t[s:k])
    t = t[:s] + b + t[k:]
    changed += 1
F2, _, order2 = parse(t)
fin = absolute(F2)
bad = [f for f in want if fin[f] != want[f]]
assert not bad, bad[:5]
fwd = [(f, F2[f][2]) for f in F2 if F2[f][2] and order2.index(F2[f][2]) > order2.index(f)]
assert not fwd, fwd[:5]
open(P, 'wb').write(t.replace('\n', '\r\n').encode('utf-8'))
print('applied; blocks edited:', changed)
