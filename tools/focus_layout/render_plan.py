import json, sys, re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plan = json.load(open(sys.argv[1]))
out = sys.argv[2]
pos = {f: tuple(v) for f, v in plan['pos'].items()}
if len(sys.argv) >= 5:
    xa, xb = float(sys.argv[3]), float(sys.argv[4])
    pos = {f: v for f, v in pos.items() if xa <= v[0] <= xb}
pre = plan['pre']
xs = [p[0] for p in pos.values()]; ys = [p[1] for p in pos.values()]
x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
W = (x1 - x0) * 0.42 + 1; H = (y1 - y0) * 0.55 + 1
fig, ax = plt.subplots(figsize=(min(max(W, 6), 40), min(max(H, 4), 30)), dpi=90)
for f, (x, y) in pos.items():
    for g in pre.get(f, []):
        for q in g:
            if q in pos:
                qx, qy = pos[q]; my = (qy + y) / 2
                ax.plot([qx, qx, x, x], [qy, my, my, y], color='tab:red' if len(g) > 1 else 'tab:blue', lw=0.7, alpha=0.7)
for f, (x, y) in pos.items():
    ax.text(x, y, f.replace('VIE_', '')[:16], fontsize=4.2, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.15', fc='lightyellow', ec='gray', lw=0.4))
ax.set_xlim(x0 - 1, x1 + 1); ax.set_ylim(y1 + 1, y0 - 1); ax.axis('off')
plt.savefig(out, bbox_inches='tight')
print('saved', out, 'bbox', x0, x1, y0, y1)
