import re,os,glob,collections
MD=os.path.join(os.path.dirname(os.path.abspath(__file__)),'md_ref'); REPO=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
# build province -> state map from MD files
p2s={}
s_info={}
for f in glob.glob(MD+'/*.txt'):
    if 'country' in f or 'state_names' in f or 'state_categories' in f: continue
    if not re.search(r'^\s*id\s*=\s*\d+', open(f,encoding='utf-8',errors='replace').read(), re.M): continue
    t=open(f,encoding='utf-8',errors='replace').read()
    sid=int(re.search(r'\bid\s*=\s*(\d+)',t).group(1))
    owner=re.search(r'owner\s*=\s*([A-Z]{3})',t)
    m=re.search(r'provinces\s*=\s*\{(.*?)\}',t,re.S)
    provs=[int(x) for x in re.findall(r'\b(\d{2,5})\b',m.group(1))] if m else []
    pass
    comments=re.findall(r'victory_points\s*=\s*\{?\s*(\d+)[^#]*#\s*([^\n\}]*)',t)
    name={int(a):b.strip() for a,b in comments}
    # also multi-line victory_points
    s_info[sid]={'owner':owner.group(1) if owner else '?','provs':provs,'vpnames':name}
    for p in provs: p2s[p]=sid
print('MD Vietnam-related states parsed:',sorted(s_info))
print('province->state map size:',len(p2s))
print()
COASTAL_HINT={4284:'Rach Gia (coastal - MD dat naval_base 4 o day)',4401:'Ho Chi Minh City (coastal)',4119:'Hai Phong (coastal)',
 10309:'Da Nang (coastal)',1157:'Ha Long (coastal)',14178:'Phu Quoc (dao)',11134:'Spratly Is (dao)',11140:'(dao)',11149:'Collins Reef (dao)',
 11168:'Southwest Cay (dao)',11146:'Cuarteron (dao)',11156:'Mischief (dao)',11167:'Subi (dao)',11169:'Fiery Cross (dao)',
 11138:'(dao)',11150:'Commodore Reef (dao)',11165:'Thitu (dao)',11171:'Nanshan (dao)',11131:'Paracel (dao)',11133:'Swallow Reef (dao)',14409:'Paracel (dao)',
 12232:'Vung Tau (coastal)',10162:'Nha Trang (coastal)',10232:'Phan Thiet (coastal)',1285:'Phan Rang (coastal)',4405:'Tuy Hoa (coastal)',4334:'Quy Nhon (coastal)'}
INLAND={4223:'Long Xuyen (An Giang - KHONG giap bien)',1423:'Vinh Long (KHONG giap bien)',12133:'Can Tho (KHONG giap bien)',
 4341:'Ca Mau? ',7303:'Soc Trang? ',1605:'Buon Ma Thuot (KHONG giap bien)',4363:'Pleiku (KHONG giap bien)',7271:'Da Lat (KHONG giap bien)',
 1073:'Thai Nguyen (KHONG giap bien)',9948:'Lang Son (KHONG giap bien)',4397:'Vinh (coastal-ish Nghe An)',10129:'Ha Noi (KHONG giap bien)'}
print('=== every "province = N" / "generator" / "states = {" in the mod, validated against MD ===')
bad=[]
for p in sorted(glob.glob(REPO+'/common/**/*.txt',recursive=True)+glob.glob(REPO+'/events/*.txt')):
    if p.endswith('.bak') or 'removed_' in p: continue
    t=open(p,encoding='utf-8',errors='replace').read()
    lines=t.split('\n')
    for i,l in enumerate(lines,1):
        for m in re.finditer(r'\bprovince\s*=\s*(\d{3,5})\b',l):
            pid=int(m.group(1))
            st=p2s.get(pid)
            rel=os.path.relpath(p,REPO)
            if st is None:
                bad.append((rel,i,pid,'KHONG thuoc state VIE nao trong MD',l.strip())); continue
            btype=re.search(r'type\s*=\s*(\w+)',l) or re.search(r'type\s*=\s*(\w+)',lines[i-2] if i>1 else '')
            note=[]
            if pid in INLAND: note.append('INLAND: '+INLAND[pid])
            if pid in COASTAL_HINT: note.append('coastal: '+COASTAL_HINT[pid])
            print(f'  {rel}:{i}  province {pid} -> state {st} (owner {s_info[st]["owner"]})  {"; ".join(note)}')
            if 'naval' in (btype.group(1) if btype else '') and pid in INLAND:
                bad.append((rel,i,pid,f'naval_base tai province inland {INLAND[pid]}',l.strip()))
            if s_info[st]['owner']!='VIE':
                bad.append((rel,i,pid,f'state {st} do {s_info[st]["owner"]} so huu luc start',l.strip()))
print()
print('=== "NNN = { ... }" state-scope blocks: state ownership at 2000 start ===')
for p in sorted(glob.glob(REPO+'/common/**/*.txt',recursive=True)+glob.glob(REPO+'/events/*.txt')):
    if p.endswith('.bak') or 'removed_' in p: continue
    t=open(p,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r'^\t{3}(51[89]|52[0-6]|80[12]|81[36])\s*=\s*\{',t,re.M):
        sid=int(m.group(1)); ln=t[:m.start()].count('\n')+1
        own=s_info.get(sid,{}).get('owner','?')
        if own!='VIE':
            print(f'  !! {os.path.relpath(p,REPO)}:{ln}  state {sid} scope — MD: owner = {own} (VIE khong so huu)')
print()
print('=== PROVINCE MISMATCH: state-scope block vs province id ===')
for p in sorted(glob.glob(REPO+'/common/**/*.txt',recursive=True)):
    if p.endswith('.bak') or 'removed_' in p: continue
    t=open(p,encoding='utf-8',errors='replace').read()
    lines=t.split('\n')
    cur=None
    for i,l in enumerate(lines,1):
        ms=re.match(r'^\t{3}(51[89]|52[0-6]|80[12]|81[36])\s*=\s*\{',l)
        if ms: cur=(int(ms.group(1)),i)
        if cur:
            mp=re.search(r'\bprovince\s*=\s*(\d{3,5})\b',l)
            if mp:
                pid=int(mp.group(1)); real=p2s.get(pid)
                if real is not None and real!=cur[0]:
                    print(f'  !! {os.path.relpath(p,REPO)}:{i}  block state {cur[0]} (mở dòng {cur[1]}) nhưng province {pid} thuộc state {real}')
                    bad.append((os.path.relpath(p,REPO),i,pid,f'province {pid} thuộc state {real}, block ghi state {cur[0]}',l.strip()))
        if re.match(r'^\t{3}\}',l): cur=None
print()
print(f'=== TỔNG HỢP LỖI: {len(bad)} ===')
for b in sorted(set(bad)): print('  ',b[0],':',b[1],'| province',b[2],'|',b[3])
