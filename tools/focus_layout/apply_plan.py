"""Write a layout plan (relayout.py / tidy_layout.py output) into VIE_md_focus.txt.
Positions become offsets from each focus's CURRENT anchor (absolute positions are the plan's).
Stops on any cell collision or same-row gap < 2.  Run from the repo root."""
import json, re, sys, collections

plan = json.load(open(sys.argv[1]))
p = 'common/national_focus/VIE_md_focus.txt'
t = open(p, 'rb').read().decode('utf-8').replace('\r\n', '\n')


def parse(text):
    F = {}; order = []; spans = {}
    for m in re.finditer(r'\n\tfocus = \{', text):
        st = m.end(); d = 1; i = st
        while d:
            d += {'{': 1, '}': -1}.get(text[i], 0); i += 1
        b = text[st:i - 1]
        fid = re.search(r'\bid = (\w+)', b).group(1)
        x = int(re.search(r'\n\t\tx = (-?\d+)', b).group(1)); y = int(re.search(r'\n\t\ty = (-?\d+)', b).group(1))
        r = re.search(r'relative_position_id = (\w+)', b)
        F[fid] = dict(x=x, y=y, rel=r.group(1) if r else None)
        order.append(fid); spans[fid] = (m.start() + 1, i)
    return F, order, spans


def absolute(F):
    memo = {}
    def ab(f):
        if f in memo: return memo[f]
        d = F[f]; x, y = d['x'], d['y']
        if d['rel']:
            px, py = ab(d['rel']); x += px; y += py
        memo[f] = (x, y); return memo[f]
    return {f: ab(f) for f in F}


F, order, spans = parse(t)
old = absolute(F)
newpos = {f: tuple(v) for f, v in plan['pos'].items()}
final = dict(old); final.update(newpos)
cells = collections.defaultdict(list)
for f, pxy in final.items(): cells[pxy].append(f)
coll = [v for v in cells.values() if len(v) > 1]
rows = collections.defaultdict(list)
for f, (x, y) in final.items(): rows[y].append((x, f))
gaps = []
for y, l in rows.items():
    l.sort()
    for a, b in zip(l, l[1:]):
        if b[0] - a[0] < 2: gaps.append((y, a, b))
if coll or gaps:
    print('COLLISION', coll[:5], gaps[:5]); sys.exit(1)

NL = '\n'
TB = '\t'
# focuses outside the plan keep their absolute position even when their anchor moved: re-express their offset
targets = set(newpos)
for f, d in F.items():
    a = d['rel']
    if a and (final[f][0] - final[a][0], final[f][1] - final[a][1]) != (d['x'], d['y']):
        targets.add(f)
plan.setdefault('pre', {}); plan.setdefault('avail', {})
for f in targets:
    plan['pre'].setdefault(f, None)
for f in sorted(targets, key=lambda z: -spans[z][0]):
    s, k = spans[f]
    b = t[s:k]
    a = F[f]['rel']
    if a:
        dx = final[f][0] - final[a][0]
        dy = final[f][1] - final[a][1]
        pat = r'\n\t\tx = -?\d+\n\t\ty = -?\d+\n\t\trelative_position_id = \w+\n'
        nb, n = re.subn(pat, NL + TB * 2 + 'x = %d' % dx + NL + TB * 2 + 'y = %d' % dy + NL + TB * 2 + 'relative_position_id = %s' % a + NL, b)
    else:   # the tree's global root keeps absolute coordinates
        pat = r'\n\t\tx = -?\d+\n\t\ty = -?\d+\n'
        nb, n = re.subn(pat, NL + TB * 2 + 'x = %d' % final[f][0] + NL + TB * 2 + 'y = %d' % final[f][1] + NL, b)
    assert n == 1, f
    # prerequisites
    old_pre = re.findall(r'\t\tprerequisite = \{[^}]*\}\n', nb)
    want = plan['pre'][f]
    cur = [re.findall(r'focus = (\w+)', g) for g in re.findall(r'prerequisite = \{([^}]*)\}', nb)]
    if want is not None and want != cur:
        newp = ''.join(TB * 2 + 'prerequisite = { %s }' % ' '.join('focus = %s' % q for q in g) + NL for g in want)
        if old_pre:
            first = nb.index(old_pre[0]); last = nb.rindex(old_pre[-1]) + len(old_pre[-1])
            nb = nb[:first] + newp + nb[last:]
        elif want:
            nb = nb.replace(TB * 2 + 'search_filters', newp + NL + TB * 2 + 'search_filters', 1)
    # conditions that stopped being prerequisites (or chain links) move to `available`
    lines = []
    for kind, val in plan['avail'].get(f, []):
        if kind == 'and':
            line = 'has_completed_focus = %s' % val
            if line not in nb: lines.append(line)
        else:
            blk = 'OR = {' + NL + ''.join(TB * 4 + 'has_completed_focus = %s' % q + NL for q in val) + TB * 3 + '}'
            if blk not in nb: lines.append(blk)
    if lines:
        one = re.search(r'\t\tavailable = \{ ([^\n]*?) \}\n', nb)
        multi = re.search(r'\t\tavailable = \{\n(.*?)\n\t\t\}\n', nb, re.S)
        extra = ''.join(TB * 3 + l + NL for l in lines)
        if one:
            nb = nb[:one.start()] + TB * 2 + 'available = {' + NL + TB * 3 + one.group(1) + NL + extra + TB * 2 + '}' + NL + nb[one.end():]
        elif multi:
            nb = nb[:multi.start()] + TB * 2 + 'available = {' + NL + multi.group(1) + NL + extra + TB * 2 + '}' + NL + nb[multi.end():]
        else:
            nb = nb.replace(TB * 2 + 'completion_reward', TB * 2 + 'available = {' + NL + extra + TB * 2 + '}' + NL + NL + TB * 2 + 'completion_reward', 1)
    t = t[:s] + nb + t[k:]

F2, order2, _ = parse(t)
pos2 = absolute(F2)
bad = [f for f in final if pos2[f] != final[f]]
assert not bad, bad[:5]
fwd = [(f, d['rel']) for f, d in F2.items() if d['rel'] and order2.index(d['rel']) > order2.index(f)]
assert not fwd, fwd[:5]
open(p, 'wb').write(t.replace('\n', '\r\n').encode('utf-8'))
print('applied', len(newpos), 'focuses; moved:', sum(1 for f in newpos if old[f] != final[f]))
