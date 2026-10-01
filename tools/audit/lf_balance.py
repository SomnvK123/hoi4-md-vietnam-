#!/usr/bin/env python3
"""Truc 3 (xay dung luc luong Luc quan): kiem tra so hoc balance.

Nguon: VIE_truc3_review_and_plan.md muc 5.4 (gia tri moi) va bao cao Luc quan muc 8.11 (gia tri goc).
Kiem tra:
  1. diem tung node theo he so moi W' = W / S so voi diem bao cao (lech <= NODE_TOL)
  2. rong ba huong First Force Structure va hai huong phat trien (lech nhau <= NET_TOL)
  3. tong cong don cho 9 duong day du (3 huong x 3 cap linh vuc) so voi tran (CAPS)

In ASCII de chay duoc tren console Windows. Thoat ma 1 neu co kiem tra that bai.
Chay tu bat ky thu muc nao, khong can cai gi them. Sua so lieu thi sua bang DATA o duoi.
"""
import itertools
import sys
from collections import defaultdict

# Hieu ung: org, def, atk, spd, dig, man, log (hau can, tinh bang "giam tieu hao"), xp, artatk,
# cost (chi phi, tang = xau). Gia tri am = phat.
W = {'atk': 1.2, 'org': 1.0, 'def': 1.0, 'xp': 1.0, 'man': 0.6, 'log': 0.5,
     'dig': 0.5, 'spd': 0.4, 'cost': -1.0, 'artatk': 1.2}
S = {'atk': 0.7, 'org': 0.7, 'def': 0.7, 'spd': 0.4, 'dig': 0.5, 'man': 0.7,
     'log': 1.0, 'xp': 1.0, 'cost': 1.0, 'artatk': 0.7}
WN = {k: W[k] / S[k] for k in W}

NODE_TOL = 0.4
NET_TOL = 0.4
# Tran toan duong (don vi %): (gia tri toi da cho phep). 'log' la muc giam tieu hao.
CAPS = {'spd': 25, 'dig': 26, 'org': 21, 'def': 16, 'man': 12, 'atk': 10, 'log': 10}

# (gia tri bao cao 8.11, gia tri moi muc 5.4). Cost nam cung node voi huong de tinh ron.
NODES = {
    'BB1': ({'org': 2}, {'org': 1.5}),
    'BB2': ({'def': 2, 'log': 1}, {'def': 1.5, 'log': 1}),
    'TG1': ({'spd': 5}, {'spd': 2}),
    'TG2': ({'atk': 2}, {'atk': 1.5}),
    'PB1': ({'dig': 4}, {'dig': 2}),
    'PB2': ({'artatk': 2}, {'artatk': 1.5}),
    'CB':  ({'dig': 5}, {'dig': 2.5}),
    'HD':  ({'org': 3}, {'org': 2}),
    'CR1': ({'org': 2, 'log': 2}, {'org': 1.5, 'log': 2}),
    'FM1': ({'spd': 8, 'org': 2, 'man': -2, 'cost': 2, 'dig': -4},
            {'spd': 3, 'org': 1.5, 'man': -1.5, 'cost': 2, 'dig': -2}),
    'FM2': ({'spd': 6, 'atk': 3}, {'spd': 2.5, 'atk': 2}),
    'FR1': ({'org': 3, 'def': 2, 'cost': 2, 'xp': -1}, {'org': 2, 'def': 1.5, 'cost': 2, 'xp': -1}),
    'FR2': ({'org': 2, 'log': 4}, {'org': 1.5, 'log': 4}),
    'FD1': ({'dig': 6, 'def': 2, 'atk': -2, 'spd': -2}, {'dig': 3, 'def': 1.5, 'atk': -1.5, 'spd': -1}),
    'FD2': ({'man': 7}, {'man': 5}),
    'PS':  ({'spd': 5, 'org': 2, 'log': 2, 'cost': 1}, {'spd': 2, 'org': 1.5, 'log': 2, 'cost': 1}),
    'PT':  ({'man': 5, 'dig': 4, 'cost': 1}, {'man': 3.5, 'dig': 2, 'cost': 1}),
    'CR2_reg': ({'org': 2, 'def': 1}, {'org': 1.5, 'def': 0.5}),
    'CR2_mob': ({'org': 2, 'spd': 2.5}, {'org': 1.5, 'spd': 1}),
    'CR2_dep': ({'def': 2, 'dig': 2}, {'def': 1.5, 'dig': 1}),
    'CR3': ({'org': 1, 'log': 4}, {'org': 1, 'log': 3}),
    'MOD_land': ({'dig': 3}, {'dig': 1.5}),
    'MOD_ad': ({'def': 1.5}, {'def': 1}),
    'MOD_cyber': ({'org': 1.5}, {'org': 1}),
    'CAP_reg': ({'org': 3, 'def': 3}, {'org': 2, 'def': 2}),
    'CAP_mob': ({'spd': 9, 'atk': 2}, {'spd': 3.5, 'atk': 1.5}),
    'CAP_dep': ({'man': 5, 'dig': 6}, {'man': 3.5, 'dig': 3}),
}
# Nang luc: (goc, cuoi) theo (linh vuc, huong). Cuoi nhan 1,5 neu la so truong (xem FAV_FINAL).
CAP = {
    ('land', 'reg'): (({'def': 3}, {'def': 2}), ({'org': 3, 'def': 3}, {'org': 2, 'def': 2})),
    ('land', 'mob'): (({'spd': 5, 'def': 1}, {'spd': 2, 'def': 0.5}), ({'atk': 3, 'spd': 6}, {'atk': 2, 'spd': 2.5})),
    ('land', 'dep'): (({'dig': 4, 'def': 1}, {'dig': 2, 'def': 0.5}), ({'dig': 8, 'def': 2}, {'dig': 4, 'def': 1.5})),
    ('ad', 'reg'): (({'def': 3}, {'def': 2}), ({'org': 3, 'def': 3}, {'org': 2, 'def': 2})),
    ('ad', 'mob'): (({'org': 2, 'spd': 2.5}, {'org': 1.5, 'spd': 1}), ({'org': 4, 'spd': 5}, {'org': 3, 'spd': 2})),
    ('ad', 'dep'): (({'dig': 4, 'def': 1}, {'dig': 2, 'def': 0.5}), ({'def': 4, 'dig': 4}, {'def': 3, 'dig': 2})),
    ('cyber', 'reg'): (({'org': 3}, {'org': 2}), ({'org': 3, 'def': 3}, {'org': 2, 'def': 2})),
    ('cyber', 'mob'): (({'spd': 5, 'org': 1}, {'spd': 2, 'org': 0.5}), ({'atk': 3, 'spd': 6}, {'atk': 2, 'spd': 2.5})),
    ('cyber', 'dep'): (({'dig': 6}, {'dig': 3}), ({'def': 4, 'dig': 4}, {'def': 3, 'dig': 2})),
}
FAV = {'mob': 'cyber', 'reg': 'ad', 'dep': 'land'}
# O so truong: gia tri node cuoi (plan 5.4, da lam tron 0,5). Bao cao: x1,5.
FAV_FINAL = {
    ('land', 'dep'): {'dig': 6, 'def': 2.5},
    ('ad', 'reg'): {'org': 3, 'def': 3},
    ('cyber', 'mob'): {'atk': 3, 'spd': 4},
}


def pts(d, w):
    return sum(w[k] * v for k, v in d.items())


def main():
    fails = []

    print('1. Diem tung node (bao cao W, moi W/S):')
    for name, (old, new) in NODES.items():
        po, pn = pts(old, W), pts(new, WN)
        flag = '' if abs(pn - po) <= NODE_TOL else '  <-- LECH'
        if flag:
            fails.append('node %s lech %.2f' % (name, pn - po))
        print('   %-9s bao cao %6.2f  moi %6.2f  lech %+5.2f%s' % (name, po, pn, pn - po, flag))
    for (area, d), cells in CAP.items():
        for lab, (old, new) in zip(('goc', 'cuoi'), cells):
            po, pn = pts(old, W), pts(new, WN)
            flag = '' if abs(pn - po) <= NODE_TOL else '  <-- LECH'
            if flag:
                fails.append('cap %s %s %s lech %.2f' % (area, d, lab, pn - po))
            print('   %-6s %s %-4s bao cao %5.2f  moi %5.2f  lech %+5.2f%s' % (area, d, lab, po, pn, pn - po, flag))

    print('\n2. Rong hai huong va huong phat trien (moi):')
    ffs = {'mob': ('FM1', 'FM2'), 'reg': ('FR1', 'FR2'), 'dep': ('FD1', 'FD2')}
    nets = {d: sum(pts(NODES[n][1], WN) for n in ns) for d, ns in ffs.items()}
    for d, v in nets.items():
        print('   FFS %s: %.2f' % (d, v))
    spread = max(nets.values()) - min(nets.values())
    print('   chenh lech toi da %.2f (tran %.2f)' % (spread, NET_TOL))
    if spread > NET_TOL:
        fails.append('FFS spread %.2f' % spread)
    dev = {'PS': pts(NODES['PS'][1], WN), 'PT': pts(NODES['PT'][1], WN)}
    print('   huong phat trien: PS %.2f  PT %.2f' % (dev['PS'], dev['PT']))
    if abs(dev['PS'] - dev['PT']) > NET_TOL:
        fails.append('PS/PT spread')

    print('\n3. Tong cong don cho 9 duong day du:')
    worst = defaultdict(float)
    for d in ('reg', 'mob', 'dep'):
        for areas in itertools.combinations(('land', 'ad', 'cyber'), 2):
            t = defaultdict(float)

            def add(e):
                for k, v in e.items():
                    t[k] += v
            for n in ('BB1', 'BB2', 'TG1', 'TG2', 'PB1', 'PB2', 'HD', 'CR1'):
                add(NODES[n][1])
            for n in ffs[d]:
                add(NODES[n][1])
            add(NODES['PS' if d == 'mob' else 'PT'][1])
            add(NODES['CR2_' + d][1])
            for a in areas:
                root, final = CAP[(a, d)][0][1], CAP[(a, d)][1][1]
                add(root)
                add(FAV_FINAL[(a, d)] if (a, d) in FAV_FINAL else final)
                add(NODES['MOD_' + a][1])
            add(NODES['CR3'][1])
            add(NODES['CAP_' + d][1])
            row = {k: round(v, 1) for k, v in sorted(t.items())}
            print('   %s %-14s %s' % (d, '+'.join(areas), row))
            for k, v in t.items():
                worst[k] = max(worst[k], v)
    print('\n   Toi da moi modifier vs tran:')
    for k, cap in CAPS.items():
        v = worst.get(k, 0.0)
        ok = v <= cap + 1e-9
        print('   %-4s %5.1f / %-4s %s' % (k, v, cap, 'OK' if ok else '<-- VUOT'))
        if not ok:
            fails.append('tran %s %.1f > %s' % (k, v, cap))

    print()
    if fails:
        print('THAT BAI: %d' % len(fails))
        for f in fails:
            print('  - ' + f)
        return 1
    print('PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
