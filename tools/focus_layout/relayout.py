"""Horizontal re-layout of focus-tree components (standard in VIE_focus_coding_standards.md 7.3).
Usage: relayout.py <out_file> <root_id> [<root_id> ...]  (or 'ALL'); dry run when out_file == '-'.
 1. flatten pure vertical chains (>=3) into one row (siblings under the chain's parent, order kept by `available`)
 2. layer = longest path from the roots  (one row per layer)
 3. x: seeded from the current x, then top-down barycenter / bottom-up centering with row packing (min gap 2)
 4. every focus keeps its current anchor; only (x, y) relative to that anchor change
"""
import re, sys, collections

import os
MODE = os.environ.get('RELAYOUT_MODE', 'bary')
SRC = 'common/national_focus/VIE_md_focus.txt'
t = open(SRC, 'rb').read().decode('utf-8').replace('\r\n', '\n')


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
        pre = [re.findall(r'focus = (\w+)', g) for g in re.findall(r'prerequisite = \{([^}]*)\}', b)]
        ex = [q for g in re.findall(r'mutually_exclusive = \{([^}]*)\}', b) for q in re.findall(r'focus = (\w+)', g)]
        F[fid] = dict(x=x, y=y, rel=r.group(1) if r else None, pre=pre, ex=ex, block=b)
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
pos = absolute(F)
idx = {f: i for i, f in enumerate(order)}
skip_prefix = ('VIE_resolution_congress', )


def components():
    adj = collections.defaultdict(set)
    for f, d in F.items():
        for g in d['pre']:
            for q in g:
                if q in F: adj[f].add(q); adj[q].add(f)
    seen = set(); comps = []
    for f in order:
        if f in seen: continue
        st = [f]; c = []; seen.add(f)
        while st:
            a = st.pop(); c.append(a)
            for b in adj[a]:
                if b not in seen: seen.add(b); st.append(b)
        comps.append(c)
    return comps


def layout_component(nodes):
    nodes = set(nodes)
    pre = {f: [[q for q in g if q in nodes] for g in F[f]['pre']] for f in nodes}
    pre = {f: [g for g in gs if g] for f, gs in pre.items()}
    children = collections.defaultdict(list)
    for f, gs in pre.items():
        for g in gs:
            for q in g: children[q].append(f)
    extra_avail = collections.defaultdict(list)   # focus -> [prerequisite focus ids to move to available]
    new_pre = {f: [list(g) for g in gs] for f, gs in pre.items()}
    # --- 1. flatten pure vertical chains (>= 3)
    def single_parent(f):
        gs = pre[f]
        return gs[0][0] if len(gs) == 1 and len(gs[0]) == 1 else None
    seen = set()
    for f in sorted(nodes, key=lambda z: idx[z]):
        if f in seen: continue
        sp = single_parent(f)
        # f must be the head: its parent is not itself a chain link
        if sp is not None and len(children[sp]) == 1 and single_parent(sp) is not None and not F[sp]['ex']: continue
        path = [f]; cur = f
        while len(children[cur]) == 1 and single_parent(children[cur][0]) == cur and not F[children[cur][0]]['ex'] and not F[cur]['ex']:
            cur = children[cur][0]; path.append(cur)
        if len(path) >= 3 and single_parent(f) is not None:
            P = single_parent(f)
            for i, c in enumerate(path):
                seen.add(c)
                if i >= 1:
                    new_pre[c] = [[P]]
                    extra_avail[c].append(path[i - 1])
    # --- 2. layers
    memo = {}
    def layer(f):
        if f in memo: return memo[f]
        ps = [q for g in new_pre[f] for q in g]
        memo[f] = 0 if not ps else 1 + max(layer(q) for q in ps)
        return memo[f]
    L = {f: layer(f) for f in nodes}
    roots = [f for f in nodes if not new_pre[f]]
    rootx = {f: pos[f][0] for f in roots}
    basey = min(pos[f][1] for f in nodes)
    # --- 3. x placement
    chain_order = {}
    for f, ea in extra_avail.items():
        chain_order[f] = ea[0]
    X = {f: float(pos[f][0]) for f in nodes}
    rows = collections.defaultdict(list)
    for f in nodes: rows[L[f]].append(f)
    maxl = max(rows) if rows else 0
    def pack(row, desired):
        # keep the order of desired x (stable), enforce gap 2
        row = sorted(row, key=lambda z: (desired[z], pos[z][0], idx[z]))
        out = {}; prev = None
        for f in row:
            v = desired[f]
            if prev is not None and v < out[prev] + 2: v = out[prev] + 2
            out[f] = v; prev = f
        # re-center the packed run around its desired mean to limit drift
        if row:
            shift = (sum(desired[z] for z in row) - sum(out[z] for z in row)) / len(row)
            for z in row: out[z] += shift
        return out
    ITERS = 0 if MODE == 'keep' else 3
    for f in nodes:
        if f in chain_order:
            X[f] = X.get(chain_order[f], X[f]) + 2
    for l in range(0, maxl + 1):
        X.update(pack(rows[l], {f: X[f] for f in rows[l]}))
    for it in range(ITERS):
        for l in range(0, maxl + 1):
            des = {}
            for f in rows[l]:
                ps = [q for g in new_pre[f] for q in g]
                des[f] = (sum(X[q] for q in ps) / len(ps)) if ps else X[f]
                if f in chain_order:   # keep chain siblings in order: just right of the previous link
                    des[f] = max(des[f], X.get(chain_order[f], des[f]) + 2)
            X.update(pack(rows[l], des))
        for l in range(maxl - 1, -1, -1):
            des = {}
            for f in rows[l]:
                ch = [c for c in children[f] if L[c] > L[f] and f in [q for g in new_pre[c] for q in g]]
                des[f] = (sum(X[c] for c in ch) / len(ch)) if ch else X[f]
            X.update(pack(rows[l], des))
    # integers, gap >= 2
    for l in rows:
        r = sorted(rows[l], key=lambda z: X[z])
        prev = None
        for f in r:
            v = int(round(X[f]))
            if prev is not None and v < X[prev] + 2: v = int(X[prev]) + 2
            X[f] = v; prev = f
    # translate so the first root keeps its x
    r0 = min(roots, key=lambda z: idx[z])
    dx = rootx[r0] - X[r0]
    Y = {f: basey + L[f] for f in nodes}
    for f in nodes: X[f] += dx
    return {f: (int(X[f]), Y[f]) for f in nodes}, new_pre, extra_avail


R_pos = pos
if __name__ == '__main__':
    out_file = sys.argv[1]
    want = sys.argv[2:]
    comps = components()
    result = {}; allpre = {}; allavail = {}
    for c in comps:
        rts = [f for f in c if not any(F[f]['pre'])]
        if want != ['ALL'] and not any(r.replace('VIE_', '') in [w.replace('VIE_', '') for w in want] for r in rts): continue
        if any(f.startswith('VIE_hl_') or f.startswith('VIE_resolution_congress') or f == 'VIE_prepare_congress_9' for f in c): continue
        if len(c) < 3: continue
        npos, npre, navail = layout_component(c)
        occupied = {f: (result[f] if f in result else R_pos[f]) for f in F if f not in npos}
        occ_rows = collections.defaultdict(list)
        for f, (ox, oy) in occupied.items(): occ_rows[oy].append(ox)
        def fits(dx):
            for f, (x, y) in npos.items():
                for ox in occ_rows.get(y, []):
                    if abs(ox - (x + dx)) < 2: return False
            return True
        shift = None
        for d in [0, -1, 1, -2, 2, -3, 3, -4, 4, -6, 6, -8, 8, -10, 10, -12, 12]:
            if fits(d): shift = d; break
        if shift is None:
            print('SKIP (no free spot):', c[0]); continue
        npos = {f: (x + shift, y) for f, (x, y) in npos.items()}
        result.update(npos); allpre.update(npre); allavail.update(navail)
    import json
    json.dump(dict(pos=result, pre=allpre, avail=allavail), open(out_file, 'w'))
    print('components laid out:', len(result), 'focuses; flattened links:', sum(len(v) for v in allavail.values()))
