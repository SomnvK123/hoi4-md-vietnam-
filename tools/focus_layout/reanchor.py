"""Re-anchor every focus on one of its own prerequisites (Modern Day style) WITHOUT moving anything on screen.
Absolute positions are recomputed before and after and must be identical."""
import re

p = 'common/national_focus/VIE_md_focus.txt'
t = open(p, 'rb').read().decode('utf-8').replace('\r\n', '\n')


def parse(text):
    F = {}
    order = []
    spans = {}
    for m in re.finditer(r'\n\tfocus = \{', text):
        st = m.end()
        d = 1
        i = st
        while d:
            d += {'{': 1, '}': -1}.get(text[i], 0)
            i += 1
        b = text[st:i - 1]
        fid = re.search(r'\bid = (\w+)', b).group(1)
        x = int(re.search(r'\n\t\tx = (-?\d+)', b).group(1))
        y = int(re.search(r'\n\t\ty = (-?\d+)', b).group(1))
        r = re.search(r'relative_position_id = (\w+)', b)
        pre = [re.findall(r'focus = (\w+)', g) for g in re.findall(r'prerequisite = \{([^}]*)\}', b)]
        F[fid] = dict(x=x, y=y, rel=r.group(1) if r else None, pre=pre)
        order.append(fid)
        spans[fid] = (m.start() + 1, i)
    return F, order, spans


def absolute(F):
    memo = {}

    def ab(f):
        if f in memo:
            return memo[f]
        d = F[f]
        x, y = d['x'], d['y']
        if d['rel']:
            px, py = ab(d['rel'])
            x += px
            y += py
        memo[f] = (x, y)
        return memo[f]
    return {f: ab(f) for f in F}


F, order, spans = parse(t)
pos = absolute(F)
idx = {f: i for i, f in enumerate(order)}

plan = {}
for f in order:
    d = F[f]
    ps = [q for g in d['pre'] for q in g if q in F]
    if not ps or d['rel'] is None:
        continue
    if d['rel'] in ps:
        continue
    cands = [q for q in ps if idx[q] < idx[f]]
    if not cands:
        continue
    fx, fy = pos[f]

    def score(q):
        qx, qy = pos[q]
        dy = fy - qy
        return (0 if dy >= 1 else 1, abs(dy) if dy >= 1 else 99, abs(fx - qx))
    best = min(cands, key=score)
    plan[f] = best

# apply (back to front so spans stay valid)
for f in sorted(plan, key=lambda z: -spans[z][0]):
    a = plan[f]
    s, k = spans[f]
    b = t[s:k]
    dx = pos[f][0] - pos[a][0]
    dy = pos[f][1] - pos[a][1]
    nb, n = re.subn(r'\n\t\tx = -?\d+\n\t\ty = -?\d+\n\t\trelative_position_id = \w+\n',
                    '\n\t\tx = %d\n\t\ty = %d\n\t\trelative_position_id = %s\n' % (dx, dy, a), b)
    assert n == 1, f
    t = t[:s] + nb + t[k:]

F2, order2, _ = parse(t)
pos2 = absolute(F2)
assert order == order2
moved = [f for f in F if pos[f] != pos2[f]]
assert not moved, moved[:5]
# forward anchors?
idx2 = {f: i for i, f in enumerate(order2)}
fwd = [(f, d['rel']) for f, d in F2.items() if d['rel'] and idx2[d['rel']] > idx2[f]]
assert not fwd, fwd[:5]
open(p, 'wb').write(t.replace('\n', '\r\n').encode('utf-8'))
print('re-anchored', len(plan), 'focuses; positions unchanged for all', len(F))
