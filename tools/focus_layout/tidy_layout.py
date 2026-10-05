"""Political-style layout for the whole focus tree (standard: VIE_focus_coding_standards.md 7.3).

Per component (branch):
  1. reduce: an AND prerequisite that is not on the row directly above becomes `available` (no long connector)
  2. flatten pure vertical chains (>= 3) into one row under the chain parent (links go to `available`)
  3. one row per layer (longest path), x by barycenter + packing (gap 2), parents centred over their children
  4. components are put side by side in one strip, every component starting on row 1
Usage:  python tools/focus_layout/tidy_layout.py <plan.json> [--skip-prefix VIE_resolution ...] [--only root ...]
It only computes; apply with apply_plan.py, preview with render_plan.py.
"""
import re, sys, json, collections

SRC = 'common/national_focus/VIE_md_focus.txt'
t = open(SRC, 'rb').read().decode('utf-8').replace('\r\n', '\n')


def parse(text):
    F = {}; order = []
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
        F[fid] = dict(x=x, y=y, rel=r.group(1) if r else None, pre=pre, ex=ex)
        order.append(fid)
    return F, order


F, order = parse(t)
idx = {f: i for i, f in enumerate(order)}


def absolute():
    memo = {}
    def ab(f):
        if f in memo: return memo[f]
        d = F[f]; x, y = d['x'], d['y']
        if d['rel']:
            px, py = ab(d['rel']); x += px; y += py
        memo[f] = (x, y); return memo[f]
    return {f: ab(f) for f in F}


pos = absolute()


def components():
    adj = collections.defaultdict(set)
    for f, d in F.items():
        for g in d['pre']:
            for q in g:
                if q in F: adj[f].add(q); adj[q].add(f)
        for q in d['ex']:      # mutually exclusive focuses belong to the same branch (kept side by side)
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
    avail = collections.defaultdict(list)       # focus -> list of ('and', id) / ('or', [ids])

    def compute_layers(p):
        memo = {}
        def layer(f):
            if f in memo: return memo[f]
            ps = [q for g in p[f] for q in g]
            memo[f] = 0 if not ps else 1 + max(layer(q) for q in ps)
            return memo[f]
        return {f: layer(f) for f in nodes}

    # --- 1. reduce AND groups that are not on the row directly above
    L = compute_layers(pre)
    new_pre = {}
    for f in nodes:
        gs = pre[f]
        if len(gs) <= 1:
            new_pre[f] = [list(g) for g in gs]; continue
        keyed = sorted(gs, key=lambda g: -max(L[q] for q in g))
        primary = keyed[0]
        keep = [primary]
        for g in keyed[1:]:
            if all(L[q] == L[f] - 1 for q in g) and max(L[q] for q in primary) == L[f] - 1:
                keep.append(g)              # hub: every parent sits on the row above, keep the lines
            else:
                avail[f].append(('and', g[0]) if len(g) == 1 else ('or', list(g)))
        new_pre[f] = [list(g) for g in gs if g in keep]
    # --- 2. flatten pure vertical chains
    children = collections.defaultdict(list)
    for f, gs in new_pre.items():
        for g in gs:
            for q in g: children[q].append(f)
    def single_parent(f):
        gs = new_pre[f]
        return gs[0][0] if len(gs) == 1 and len(gs[0]) == 1 else None
    seen = set(); chain_prev = {}
    for f in sorted(nodes, key=lambda z: idx[z]):
        if f in seen: continue
        sp = single_parent(f)
        if sp is not None and len(children[sp]) == 1 and single_parent(sp) is not None and not F[sp]['ex']: continue
        path = [f]; cur = f
        while len(children[cur]) == 1 and single_parent(children[cur][0]) == cur and not F[children[cur][0]]['ex'] and not F[cur]['ex']:
            cur = children[cur][0]; path.append(cur)
        if len(path) >= 3 and sp is not None:
            for i, c in enumerate(path):
                seen.add(c)
                if i >= 1:
                    new_pre[c] = [[sp]]
                    avail[c].append(('and', path[i - 1])); chain_prev[c] = path[i - 1]
    # --- 3. layers + x
    L = compute_layers(new_pre)
    rows = collections.defaultdict(list)
    for f in nodes: rows[L[f]].append(f)
    maxl = max(rows)
    children = collections.defaultdict(list)
    for f, gs in new_pre.items():
        for g in gs:
            for q in g: children[q].append(f)
    # tidy seeds: forest of primary parents (deepest prerequisite), leaves on consecutive slots 2 apart,
    # parents centred over their children. Only the left-to-right ORDER comes from the old layout.
    primary = {}
    for f in nodes:
        ps = [q for g in new_pre[f] for q in g]
        if ps: primary[f] = max(ps, key=lambda q: (L[q], -pos[q][0], -idx[q]))
    tchildren = collections.defaultdict(list)
    for f, q in primary.items(): tchildren[q].append(f)
    for q in tchildren: tchildren[q].sort(key=lambda z: (pos[z][0], idx[z]))
    # Reingold-Tilford style packing with contours keyed by ROW (layer): sibling sub-trees may interleave on
    # different rows but keep `gap` columns apart on every shared row; big sub-branches get an extra gutter.
    size = {}
    def subtree_size(f):
        if f in size: return size[f]
        size[f] = 1 + sum(subtree_size(c) for c in tchildren.get(f, []))
        return size[f]
    GUTTER = {1: 4, 2: 2}      # extra columns between sibling sub-branches of >= 3 focuses, by depth below the root
    rel = {}                    # focus -> x relative to its tree parent
    def build(f, depth):
        """returns the contour of f's sub-tree relative to f: {row: [min, max]}"""
        ch = tchildren.get(f, [])
        cont = {L[f]: [0.0, 0.0]}
        if not ch: return cont
        placed = {}             # child -> x in the local frame
        comb = {}
        prev = None; prev_big = False
        for c in ch:
            cc = build(c, depth + 1)
            big = subtree_size(c) >= 3
            gap = 2 + (GUTTER.get(depth + 1, 0) if (prev is not None and (big or prev_big)) else 0)
            s = -1e9 if prev is None else placed[prev] + 2
            for l, (lo, hi) in cc.items():
                if l in comb: s = max(s, comb[l][1] + gap - lo)
            if prev is None: s = 0.0
            placed[c] = s
            for l, (lo, hi) in cc.items():
                if l in comb: comb[l] = [min(comb[l][0], lo + s), max(comb[l][1], hi + s)]
                else: comb[l] = [lo + s, hi + s]
            prev = c; prev_big = big
        mid = (placed[ch[0]] + placed[ch[-1]]) / 2.0
        for c in ch: rel[c] = placed[c] - mid
        for l, (lo, hi) in comb.items():
            lo -= mid; hi -= mid
            if l in cont: cont[l] = [min(cont[l][0], lo), max(cont[l][1], hi)]
            else: cont[l] = [lo, hi]
        return cont
    X = {}
    roots_sorted = sorted([f for f in nodes if f not in primary], key=lambda z: (pos[z][0], idx[z]))
    comb = {}; start = 0.0; prev_root = None
    root_x = {}
    for r in roots_sorted:
        cc = build(r, 0)
        s = 0.0 if prev_root is None else root_x[prev_root] + 2
        for l, (lo, hi) in cc.items():
            if l in comb: s = max(s, comb[l][1] + 8 - lo)
        root_x[r] = s
        for l, (lo, hi) in cc.items():
            if l in comb: comb[l] = [min(comb[l][0], lo + s), max(comb[l][1], hi + s)]
            else: comb[l] = [lo + s, hi + s]
        prev_root = r
    def assign(f, x):
        X[f] = x
        for c in tchildren.get(f, []): assign(c, x + rel[c])
    for r in roots_sorted: assign(r, root_x[r])

    def pack(row, desired):
        row = sorted(row, key=lambda z: (desired[z], pos[z][0], idx[z]))
        out = {}; prev = None
        for f in row:
            v = desired[f]
            if prev is not None and v < out[prev] + 2: v = out[prev] + 2
            out[f] = v; prev = f
        if row:
            shift = (sum(desired[z] for z in row) - sum(out[z] for z in row)) / len(row)
            for z in row: out[z] += shift
        return out
    for it in range(0):
        for l in range(0, maxl + 1):
            des = {}
            for f in rows[l]:
                ps = [q for g in new_pre[f] for q in g]
                des[f] = (sum(X[q] for q in ps) / len(ps)) if ps else X[f]
                if f in chain_prev: des[f] = max(des[f], X[chain_prev[f]] + 2)
            X.update(pack(rows[l], des))
        for l in range(maxl - 1, -1, -1):
            des = {}
            for f in rows[l]:
                ch = [c for c in children[f] if L[c] > L[f]]
                des[f] = (sum(X[c] for c in ch) / len(ch)) if ch else X[f]
            X.update(pack(rows[l], des))
    for l in rows:
        r = sorted(rows[l], key=lambda z: X[z]); prev = None
        for f in r:
            v = int(round(X[f]))
            if prev is not None and v < X[prev] + 2: v = int(X[prev]) + 2
            X[f] = v; prev = f
    minx = min(X.values())
    return {f: (int(X[f] - minx), L[f]) for f in nodes}, new_pre, avail


if __name__ == '__main__':
    out = sys.argv[1]
    skip = []; only = []
    a = sys.argv[2:]
    while a:
        k = a.pop(0)
        if k == '--skip-prefix': skip.append(a.pop(0))
        elif k == '--only': only.append(a.pop(0).replace('VIE_', ''))
    comps = components()
    sel = []
    for c in comps:
        if any(f.startswith(tuple(skip)) for f in c): continue
        rts = [f for f in c if not any(F[f]['pre'])]
        if only and not any(r.replace('VIE_', '') in only for r in rts): continue
        sel.append(c)
    sel.sort(key=lambda c: min(pos[f][0] for f in c))
    cursor = int(sys.argv[sys.argv.index('--start') + 1]) if '--start' in sys.argv else 0
    result = {}; allpre = {}; allavail = {}
    for c in sel:
        npos, npre, navail = layout_component(c)
        w = max(p[0] for p in npos.values())
        for f, (x, y) in npos.items(): result[f] = (x + cursor, y + 1)
        allpre.update(npre); allavail.update(navail)
        cursor += w + 10
    json.dump(dict(pos=result, pre=allpre, avail={f: v for f, v in allavail.items()}), open(out, 'w'))
    print('components', len(sel), 'focuses', len(result), 'strip width', cursor,
          'rows max', max(p[1] for p in result.values()))
