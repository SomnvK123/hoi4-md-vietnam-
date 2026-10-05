import re, sys, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

p = 'common/national_focus/VIE_md_focus.txt'
t = open(p, encoding='utf-8').read().replace('\r\n', '\n')
F = {}
for m in re.finditer(r'\n\tfocus = \{', t):
    st = m.end(); d = 1; i = st
    while d:
        d += {'{': 1, '}': -1}.get(t[i], 0); i += 1
    b = t[st:i - 1]
    fid = re.search(r'\bid = (\w+)', b).group(1)
    x = int(re.search(r'\n\t\tx = (-?\d+)', b).group(1)); y = int(re.search(r'\n\t\ty = (-?\d+)', b).group(1))
    r = re.search(r'relative_position_id = (\w+)', b)
    pre = [re.findall(r'focus = (\w+)', g) for g in re.findall(r'prerequisite = \{([^}]*)\}', b)]
    ex = [q for g in re.findall(r'mutually_exclusive = \{([^}]*)\}', b) for q in re.findall(r'focus = (\w+)', g)]
    F[fid] = dict(x=x, y=y, rel=r.group(1) if r else None, pre=pre, ex=ex)
memo = {}
def ab(f):
    if f in memo: return memo[f]
    d = F[f]; x, y = d['x'], d['y']
    if d['rel']:
        px, py = ab(d['rel']); x += px; y += py
    memo[f] = (x, y); return memo[f]
pos = {f: ab(f) for f in F}

x0, x1, y0, y1 = [float(v) for v in sys.argv[1:5]]
out = sys.argv[5]
W = (x1 - x0) * 0.42 + 1; H = (y1 - y0) * 0.55 + 1
fig, ax = plt.subplots(figsize=(min(W, 40), min(H, 30)), dpi=90)
for f, (x, y) in pos.items():
    if not (x0 <= x <= x1 and y0 <= y <= y1): continue
    for g in F[f]['pre']:
        for q in g:
            if q in pos:
                qx, qy = pos[q]
                my = (qy + y) / 2
                col = 'tab:red' if len(g) > 1 else 'tab:blue'
                ax.plot([qx, qx, x, x], [qy, my, my, y], color=col, lw=0.7, alpha=0.7)
    for q in F[f]['ex']:
        if q in pos and f < q:
            qx, qy = pos[q]; ax.plot([x, qx], [y, qy], color='tab:green', lw=0.5, ls='--')
for f, (x, y) in pos.items():
    if not (x0 <= x <= x1 and y0 <= y <= y1): continue
    ax.text(x, y, f.replace('VIE_', '')[:16], fontsize=4.2, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.15', fc='lightyellow', ec='gray', lw=0.4))
ax.set_xlim(x0 - 1, x1 + 1); ax.set_ylim(y1 + 1, y0 - 1)
ax.set_aspect('auto'); ax.axis('off')
plt.savefig(out, bbox_inches='tight')
print('saved', out)
