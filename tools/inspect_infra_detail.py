import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
import tools.test_infra_layout as til

print("=== ALL 44 INFRASTRUCTURE FOCUSES ===")
for fid, d in sorted(til.INFRA_LAYOUT.items(), key=lambda x: (x[1]['abs'][1], x[1]['abs'][0])):
    pos_str = str(d['abs'])
    print(f"{fid:38} | abs={pos_str:10} | rel={d['rel']:30} | dx={d['dx']:3d}, dy={d['dy']:2d} | pr={d['prereqs']}")
