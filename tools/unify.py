"""Re-lay the whole military tree as ONE super-branch: root -> 4 columns (army / navy / air / defence industry), layered by rank.
Only x/y change, plus one added prerequisite (VIE_modernize_vpa) on the 4 column heads (they were already gated by `available`).
usage: python3 unify.py [--write]"""
import re, sys, collections
F = 'D:/HOI4Mods/md_vietnam/common/national_focus/VIE_md_focus.txt'
WRITE = '--write' in sys.argv
raw = open(F, 'rb').read(); bom = raw.startswith(b'\xef\xbb\xbf'); text = raw.decode('utf-8-sig')
blocks = {}
for m in re.finditer(r'\n\tfocus\s*=\s*\{', text):
    st = m.end(); d = 1; i = st
    while d:
        d += {'{': 1, '}': -1}.get(text[i], 0); i += 1
    blocks[re.search(r'\bid\s*=\s*(\w+)', text[st:i - 1]).group(1)] = (st, i - 1)
def info(fid):
    s, e = blocks[fid]; b = text[s:e]
    x = int(re.search(r'\n\t\tx\s*=\s*(-?\d+)', b).group(1)); y = int(re.search(r'\n\t\ty\s*=\s*(-?\d+)', b).group(1))
    r = re.search(r'relative_position_id\s*=\s*(\w+)', b)
    pre = [f for g in re.findall(r'prerequisite\s*=\s*\{([^}]*)\}', b) for f in re.findall(r'focus\s*=\s*(\w+)', g)]
    return dict(x=x, y=y, rel=r.group(1) if r else None, pre=pre)
I = {f: info(f) for f in blocks}
ANCH = 27
def absxy(f):
    d = I[f]
    if not d['rel']: return d['x'], d['y']
    a, b = absxy(d['rel']); return a + d['x'], b + d['y']
OLD = {f: absxy(f) for f in blocks}

V = 'VIE_'
ROOT, JOIN = 'VIE_modernize_vpa', 'VIE_defence_strategy_review'
FEED = {
 1: ['tank_modernization', 'rocket_artillery', 'mechanization', 't90_tanks', 'special_forces', 'corps_restructure', 'reserve_mobilization'],
 2: ['navy_modernization', 'naval_aviation', 'kilo_submarines', 'gepard_frigates', 'bastion_p_coastal_defence', 'domestic_corvettes', 'domestic_antiship',
     'naval_infantry', 'cam_ranh_base', 'cam_ranh_port_diplomacy'],
 3: ['air_force_modernization', 'su30mk2_fleet', 'integrated_air_defense', 'yak130_trainers', 'l39ng', 'helicopter_fleet', 'uav_program', 'fighter_replacement', 'air_dominance_coast'],
 4: ['viettel_military_tech', 'russian_arms_deals', 'z_factories', 'licensed_rifles', 'shipyards', 'missile_program', 'defence_expo', 'arms_export',
     'dual_use_industry', 'path_self_reliant_deterrence'],
}
DEV = {
 1: ['army_development', 'army_combined_arms', 'path_peoples_war', 'army_expeditionary', 'army_jungle_warfare', 'army_logistics_reform', 'army_iron_triangle'],
 2: ['navy_development', 'navy_fleet_training', 'path_maritime_denial', 'navy_blue_water', 'navy_asw_capacity', 'navy_forward_basing', 'navy_sea_control'],
 3: ['air_development', 'air_doctrine_reform', 'air_superiority_ops', 'air_deep_strike', 'air_layered_sam', 'air_maritime_strike', 'air_early_warning', 'air_full_spectrum'],
 4: [],
}
COL = {c: [V + n for n in FEED[c] + DEV[c]] for c in FEED}
for f in blocks:
    for pre, c in (('VIE_army_', 1), ('VIE_navy_', 2), ('VIE_air_', 3), ('VIE_def_', 4), ('VIE_msl_', 4)):
        if f.startswith(pre) and not any(f in v for v in COL.values()): COL[c].append(f)
HEADS = {1: 'VIE_tank_modernization', 2: 'VIE_navy_modernization', 3: 'VIE_air_force_modernization', 4: 'VIE_viettel_military_tech'}
col_of = {f: c for c, v in COL.items() for f in v}
M = set(col_of) | {ROOT, JOIN}
assert all(f in blocks for f in M), [f for f in M if f not in blocks]
FEEDERS = {V + n for c in (1, 2, 3) for n in FEED[c]}

par = {f: [p for p in I[f]['pre'] if p in M] for f in M}
for h in HEADS.values():
    if ROOT not in par[h]: par[h].append(ROOT)
par[ROOT] = []; par[JOIN] = []
def ranks(join_rank=None):
    rank = {}
    def rk(f):
        if f in rank: return rank[f]
        if f == JOIN and join_rank is not None: rank[f] = join_rank; return join_rank
        rank[f] = 0
        rank[f] = 1 + max([rk(p) for p in par[f]]) if par[f] else 0
        return rank[f]
    for f in M: rk(f)
    return rank
r0 = ranks()
tail = max(r0[f] for f in FEEDERS)
for d in (V + 'army_development', V + 'navy_development', V + 'air_development'):
    par[d] = par[d] + [JOIN] if JOIN not in par[d] else par[d]
rank = ranks(join_rank=tail + 1)
ROOT_ROW = 10
print('feeder tail rank', tail, 'max rank', max(rank.values()), 'bottom row', ROOT_ROW + max(rank.values()))

SP = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 3
def layout_column(c):
    nodes = COL[c]
    byr = collections.defaultdict(list)
    for f in nodes: byr[rank[f]].append(f)
    pos = {}
    for r in sorted(byr):
        row = byr[r]
        tg = {}
        for f in row:
            ps = [pos[p] for p in par[f] if p in pos]
            tg[f] = sum(ps) / len(ps) if ps else None
        known = sorted([f for f in row if tg[f] is not None], key=lambda f: (tg[f], OLD[f][0]))
        unk = sorted([f for f in row if tg[f] is None], key=lambda f: OLD[f][0])
        # merge unknown by old x relative order into known using their old x as a weak target
        ordered = known + unk if known else unk
        want = []
        for k, f in enumerate(ordered):
            if tg[f] is not None: want.append(tg[f])
            else: want.append((want[-1] + SP) if want else 0.0)
        xs = want[:]
        for k in range(1, len(xs)):
            if xs[k] < xs[k - 1] + SP: xs[k] = xs[k - 1] + SP
        sh = (sum(want) - sum(xs)) / len(xs)
        xs = [v + sh for v in xs]
        for k in range(1, len(xs)):
            if xs[k] < xs[k - 1] + SP: xs[k] = xs[k - 1] + SP
        for f, v in zip(ordered, xs): pos[f] = v
    # integer positions
    return {f: int(round(v)) for f, v in pos.items()}

def pav(d, sp):
    """least-squares x with x[i+1]-x[i] >= sp, targets d (already in left-to-right order)"""
    y = [v - i * sp for i, v in enumerate(d)]
    blocks_ = []  # (sum, count)
    for v in y:
        blocks_.append([v, 1])
        while len(blocks_) > 1 and blocks_[-2][0] / blocks_[-2][1] > blocks_[-1][0] / blocks_[-1][1]:
            s, n = blocks_.pop(); blocks_[-1][0] += s; blocks_[-1][1] += n
    out = []
    for s, n in blocks_: out += [s / n] * n
    return [v + i * sp for i, v in enumerate(out)]

ITER = 0
def layout_column2(c):
    base = layout_column(c)                       # initial positions / order from the first pass
    nodes = COL[c]
    byr = collections.defaultdict(list)
    for f in nodes: byr[rank[f]].append(f)
    kids = collections.defaultdict(list)
    for f in nodes:
        for p in par[f]:
            if p in base: kids[p].append(f)
    pos = {f: float(v) for f, v in base.items()}
    rows = sorted(byr)
    # order = current x order; refine by barycenter sweeps
    CEN = [sum(pos.values()) / len(pos)]
    for it in range(ITER):
        seq = rows if it % 2 == 0 else rows[::-1]
        for r in seq:
            row = byr[r]
            nb = {}
            for f in row:
                ns = [pos[p] for p in par[f] if p in pos] * (2 if it % 2 == 0 else 1) + [pos[k] for k in kids[f]] * (1 if it % 2 == 0 else 2)
                nb[f] = (0.75 * sum(ns) / len(ns) + 0.25 * CEN[0]) if ns else pos[f]
            row.sort(key=lambda f: (nb[f], pos[f]))
            xs = pav([nb[f] for f in row], SP)
            for f, v in zip(row, xs): pos[f] = v
    return {f: int(round(v)) for f, v in pos.items()}

cp = {c: layout_column2(c) for c in (1, 2, 3, 4)}
# rounding can break spacing by 1: repair per row
for c in cp:
    byr = collections.defaultdict(list)
    for f, v in cp[c].items(): byr[rank[f]].append(f)
    for r, row in byr.items():
        row.sort(key=lambda f: cp[c][f])
        for a, b in zip(row, row[1:]):
            if cp[c][b] - cp[c][a] < SP: cp[c][b] = cp[c][a] + SP
GAP = 3
NEW = {}
x_cursor = 34
for c in (1, 2, 3, 4):
    p = cp[c]; lo = min(p.values()); hi = max(p.values())
    for f, v in p.items(): NEW[f] = (v - lo + x_cursor, ROOT_ROW + rank[f])
    print('col', c, 'x', x_cursor, '..', x_cursor + hi - lo, 'nodes', len(p))
    x_cursor += hi - lo + GAP + 1
# join between the three development heads, root centred over the four column heads
dv = [NEW[V + 'army_development'][0], NEW[V + 'navy_development'][0], NEW[V + 'air_development'][0]]
NEW[JOIN] = (round(sum(dv) / 3), ROOT_ROW + rank[JOIN])
hx = [NEW[h][0] for h in HEADS.values()]
NEW[ROOT] = (round(sum(hx) / 4), ROOT_ROW)

if '--manual' in sys.argv:
    sys.path.insert(0, 'D:/HOI4Mods/_gen')
    import manual_layout as ML
    NEW = {}
    for c, mp in ML.MAN.items():
        for k, (lx, r) in mp.items():
            NEW[V + k] = (ML.CENTRES[c] + lx, ROOT_ROW + r)
        miss = [f for f in COL[c] if f not in NEW]
        extra = [k for k in mp if V + k not in COL[c]]
        assert not miss and not extra, (c, miss, extra)
    NEW[JOIN] = (round((NEW[V + 'army_development'][0] + NEW[V + 'navy_development'][0] + NEW[V + 'air_development'][0]) / 3), ROOT_ROW + 5)
    NEW[ROOT] = (round(sum(NEW[h][0] for h in HEADS.values()) / 4), ROOT_ROW)
# --- checks on the final absolute layout
ABS = {f: NEW.get(f, OLD[f]) for f in blocks}
occ = collections.defaultdict(list)
for f, p in ABS.items(): occ[p].append(f)
bad = [(p, v) for p, v in occ.items() if len(v) > 1]
print('same-cell', bad)
close = []
byrow = collections.defaultdict(list)
for f, (x, y) in ABS.items(): byrow[y].append((x, f))
for y, v in byrow.items():
    v.sort()
    for (x1, f1), (x2, f2) in zip(v, v[1:]):
        if x2 - x1 < 2: close.append((f1, f2))
print('too close', close)
NP = {f: [p for p in (par[f] if f in par else I[f]['pre'])] for f in blocks}
hits = set()
for c in blocks:
    cx, cy = ABS[c]
    for p in NP[c]:
        px, py = ABS[p]
        if py >= cy: print('parent not above', p, c)
        mid = cy - 1
        for (x1, y1, x2, y2) in ((px, py + 1, px, mid), (min(px, cx), mid, max(px, cx), mid)):
            for xx in range(x1, x2 + 1):
                for yy in range(y1, y2 + 1):
                    for o in occ.get((xx, yy), []):
                        if o not in (c, p): hits.add((p, c, o))
new_hits = [h for h in hits if h[0] in M or h[1] in M or h[2] in M]
print('connector hits touching the military block:', len(new_hits))
for h in sorted(new_hits)[:60]: print('  ', h)

if WRITE:
    out = text
    # edit from the end so offsets stay valid
    for f in sorted(NEW, key=lambda f: -blocks[f][0]):
        s, e = blocks[f]; b = out[s:e]
        X_, Y_ = NEW[f]
        b = re.sub(r'(\n\t\tx\s*=\s*)-?\d+', lambda m: m.group(1) + str(X_ - ANCH), b, count=1)
        b = re.sub(r'(\n\t\ty\s*=\s*)-?\d+', lambda m: m.group(1) + str(Y_), b, count=1)
        if not re.search(r'relative_position_id\s*=\s*VIE_doi_moi_continues', b):
            print('WARNING: unexpected relative base', f)
        if f in HEADS.values() and ROOT not in I[f]['pre']:
            b = re.sub(r'(\n\t\tcost\s*=\s*\d+\n)', lambda m: m.group(1) + '\n\t\tprerequisite = { focus = %s }' % ROOT, b, count=1)
        out = out[:s] + b + out[e:]
    open(F, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.replace('\r\n', '\n').encode('utf-8'))
    print('written')

if '--dump' in sys.argv:
    for c in (1, 2, 3, 4):
        print('== COL', c)
        for f in sorted(COL[c], key=lambda f: (rank[f], NEW[f][0])):
            print(rank[f], f.replace('VIE_', ''), '<-', [p.replace('VIE_', '') for p in par[f]], ('X ' + str([e for e in ()]) if False else ''))
