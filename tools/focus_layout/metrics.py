import sys, json, collections
sys.argv = [sys.argv[0]] + sys.argv[1:]
import importlib.util
spec = importlib.util.spec_from_file_location('relayout', sys.argv[0].replace('metrics.py', 'relayout.py'))
R = importlib.util.module_from_spec(spec)
sys.argv_backup = sys.argv
sys.argv = ['relayout.py', '-']
spec.loader.exec_module(R)


def segments(pos, pre):
    segs = []
    for f, gs in pre.items():
        for g in gs:
            for q in g:
                if q not in pos or f not in pos: continue
                qx, qy = pos[q]; x, y = pos[f]
                my = (qy + y) / 2.0
                segs.append(('v', qx, qy, my, (q, f)))
                segs.append(('h', my, min(qx, x), max(qx, x), (q, f)))
                segs.append(('v', x, my, y, (q, f)))
    return segs


def crossings(pos, pre):
    segs = segments(pos, pre)
    vs = [s for s in segs if s[0] == 'v']; hs = [s for s in segs if s[0] == 'h']
    n = 0
    for h in hs:
        _, hy, x1, x2, e1 = h
        for v in vs:
            _, vx, y1, y2, e2 = v
            if e1[0] == e2[0] or e1[1] == e2[1]: continue
            if x1 < vx < x2 and min(y1, y2) < hy < max(y1, y2): n += 1
    return n


def length(pos, pre):
    s = 0
    for f, gs in pre.items():
        for g in gs:
            for q in g:
                if q in pos and f in pos:
                    s += abs(pos[f][0] - pos[q][0]) + abs(pos[f][1] - pos[q][1])
    return s


if __name__ == '__main__':
    pass


def report(root_names):
    comps = R.components()
    rows = []
    for c in comps:
        rts = [f for f in c if not any(R.F[f]['pre'])]
        if any(f.startswith('VIE_hl_') or f.startswith('VIE_resolution_congress') or f == 'VIE_prepare_congress_9' for f in c): continue
        if len(c) < 3: continue
        npos, npre, navail = R.layout_component(c)
        old = {f: R.pos[f] for f in c}
        oldpre = {f: [[q for q in g if q in old] for g in R.F[f]['pre']] for f in c}
        oldpre = {f: [g for g in gs if g] for f, gs in oldpre.items()}
        rows.append((rts[0].replace('VIE_', ''), len(c),
                     (max(p[1] for p in old.values()) - min(p[1] for p in old.values()) + 1, max(p[1] for p in npos.values()) - min(p[1] for p in npos.values()) + 1),
                     (max(p[0] for p in old.values()) - min(p[0] for p in old.values()), max(p[0] for p in npos.values()) - min(p[0] for p in npos.values())),
                     (crossings(old, oldpre), crossings(npos, npre)),
                     (length(old, oldpre), length(npos, npre)), len(navail)))
    return rows


for r in report(None):
    print(r)
