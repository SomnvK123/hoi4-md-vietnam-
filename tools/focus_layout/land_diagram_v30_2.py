"""Render the live V30.2 land-force branch and prerequisite graph to PNG."""
from pathlib import Path
import re
import sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'audit'))
from industry import ROOT,focus_map,groups,positions,value,values

FOCUS=ROOT/'common/national_focus/VIE_md_focus.txt'
OUT=ROOT/'.claude/docs/land/land_focus_v30_2.png'
CURRENT=ROOT/'.claude/docs/land/land_focus_current.png'
LOC=ROOT/'localisation/english'
PREFIX='VIE_lf_'
W,H=194,92
ROW=150;TOP=300;LEFT=240;STEP=112
COLORS={'foundation':'#9eb6c7','program':'#5ba9b8','strategy':'#d4a354','regular':'#72b2d0','mobile':'#79b69b','depth':'#c2a667','capability':'#8fa4cc','end':'#b18cc5'}
PATH={x:COLORS[c] for xs,c in [
(['VIE_lf_fs_main_corps','VIE_lf_fs_lean_corps','VIE_lf_mech_coordination','VIE_lf_mech_fire_support','VIE_lf_mech_complete'],'regular'),
(['VIE_lf_fs_mobile_force','VIE_lf_fs_mobile_corps','VIE_lf_mobile_fire_support','VIE_lf_mobile_sustainment','VIE_lf_dev_strategic'],'mobile'),
(['VIE_lf_fs_depth_defence','VIE_lf_fs_militia_units','VIE_lf_territorial_reserve','VIE_lf_territorial_coordination','VIE_lf_dev_territorial'],'depth') ] for x in xs}
def main():
 allf=focus_map(FOCUS.read_text(encoding='utf-8')); land={k:v for k,v in allf.items() if k.startswith(PREFIX)}; pos=positions(allf)
 names={}
 for file in list(LOC.glob('*.yml'))+list((LOC/'replace').glob('*.yml')):
  raw=file.read_text(encoding='utf-8-sig')
  names.update({m.group(1):m.group(2) for m in re.finditer(r'^ ([\w.]+):\d "(.*)"',raw,re.M)})
 minx=min(pos[f][0] for f in land);maxx=max(pos[f][0] for f in land);maxy=max(pos[f][1] for f in land)
 width=(maxx-minx)*STEP+LEFT*2+W;height=TOP+maxy*ROW+150
 im=Image.new('RGB',(width,height),'#111a22');d=ImageDraw.Draw(im)
 reg=Path('C:/Windows/Fonts/arial.ttf');bold=Path('C:/Windows/Fonts/arialbd.ttf')
 if not reg.exists():reg=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf');bold=reg.with_name('DejaVuSans-Bold.ttf')
 def font(size,b=False):return ImageFont.truetype(str(bold if b else reg),size) if (bold if b else reg).exists() else ImageFont.load_default(size=size)
 coords={fid:(LEFT+(pos[fid][0]-minx)*STEP,TOP+pos[fid][1]*ROW) for fid in land}
 d.text((38,24),'CÂY FOCUS LỤC QUÂN • V30.2',font=font(30,True),fill='#f1f5f9')
 d.text((40,68),'Phân tầng trên-dưới: Nền tảng & 4 Binh chủng → 3 Hướng chiến lược (M/R/D) → Năng lực nâng cao & Hiện đại hóa',font=font(18),fill='#bdcbd6')
 d.text((40,104),'Mũi tên liền: AND / bắt buộc  |  Nét đứt vàng: OR  |  Viền đỏ đôi: loại trừ  |  K2 yêu cầu 3/6 terminal',font=font(16),fill='#bdcbd6')
 rowlabels={2:'01  NỀN TẢNG',3:'02  TỔ CHỨC 4 BINH CHỦNG + HUẤN LUYỆN / HẬU CẦN',4:'03  HUẤN LUYỆN CHUYÊN NGÀNH + CẢI TỔ CÁN BỘ',5:'04  KHÍ TÀI / HỎA LỰC + HIỆP ĐỒNG BINH CHỦNG',6:'05  CẢI CÁCH BỘ CHỈ HUY I',7:'06  CHỌN CƠ CẤU CHIẾN LƯỢC (1 TRONG 3)',8:'07  TỔ CHỨC & HIỆP ĐỒNG THEO HƯỚNG',9:'08  HỎA LỰC & BẢO ĐẢM / DỰ BỊ THEO HƯỚNG',10:'09  HOÀN THIỆN LỰC LƯỢNG THEO HƯỚNG',11:'10  CẢI CÁCH BỘ CHỈ HUY II',12:'11  HIỆN ĐẠI HÓA 3/6 & NĂNG LỰC NÂNG CAO',13:'12  CHUYÊN SÂU NĂNG LỰC & CHỈ HUY SỐ',14:'13  HOÀN THIỆN LỰC LƯỢNG VŨ TRANG',15:'14  TÁC CHIẾN MẠNG & ĐIỆN TỬ TOÀN DIỆN'}
 for y,label in rowlabels.items():
  yy=TOP+y*ROW;d.line((24,yy-W//2-20,width-24,yy-W//2-20),fill='#273541')
  d.text((28,yy-W//2-16),label,font=font(12,True),fill='#8294a2')
 root='VIE_lf_army_reform';rx,ry=coords[root]
 d.rounded_rectangle((rx-190,TOP-92,rx+190,TOP-40),radius=8,fill='#26333e',outline='#9eb6c7',width=2)
 d.text((rx,TOP-82),'Tiền đề ngoài nhánh: VIE_modernize_vpa',font=font(14,True),fill='#f2f5f7',anchor='mt')
 d.line((rx,TOP-40,rx,ry-W//2),fill='#b5c5d3',width=3)
 for fid,node in land.items():
  for group in groups(node):
   for parent in group:
    if parent not in land:continue
    x1,y1=coords[parent];x2,y2=coords[fid];mid=(y1+y2)//2
    pts=[(x1,y1+H//2),(x1,mid),(x2,mid),(x2,y2-H//2)]
    color='#d5ba78' if len(group)>1 else '#afc0cd'
    if len(group)==1:
     d.line(pts,fill=color,width=3)
     ex,ey=pts[-1];d.polygon([(ex,ey),(ex-6,ey-10),(ex+6,ey-10)],fill=color)
    else:
     for a,b in zip(pts,pts[1:]):
      dx,dy=b[0]-a[0],b[1]-a[1];n=max(abs(dx),abs(dy),1)
      for st in range(0,n,18):
       en=min(st+10,n);d.line((a[0]+dx*st/n,a[1]+dy*st/n,a[0]+dx*en/n,a[1]+dy*en/n),fill=color,width=3)
 mutex=set()
 for fid,node in land.items():
  for other in values(value(node,'mutually_exclusive',[]),'focus'):
   if other in land:mutex.add(tuple(sorted((fid,other))))
 for a,b in mutex:
  x1,y1=coords[a];x2,y2=coords[b]
  d.line((x1,y1-4,x2,y2-4),fill='#df7777',width=2);d.line((x1,y1+4,x2,y2+4),fill='#df7777',width=2)
 base={'VIE_lf_army_reform','VIE_lf_basic_training','VIE_lf_logistics_merge','VIE_lf_cadre_professional','VIE_lf_force_reorganization','VIE_lf_combined_arms','VIE_lf_command_reform_1'}
 final={'VIE_lf_command_reform_2','VIE_lf_selective_modernization','VIE_lf_command_reform_3','VIE_lf_force_complete'}
 gates={'VIE_lf_army_reform':'Gate: date + VIE_modernize_vpa','VIE_lf_selective_modernization':'Gate: 3 trong 6 terminal'}
 for fid,(x,y) in coords.items():
  color=PATH.get(fid,COLORS['foundation'] if fid in base else COLORS['end'] if fid in final else COLORS['capability'] if fid.startswith('VIE_lf_cap_') or fid=='VIE_lf_selective_modernization' else COLORS['program'])
  d.rounded_rectangle((x-W//2,y-H//2,x+W//2,y+H//2),radius=10,fill='#202d38',outline=color,width=3)
  title=names.get(fid,fid).split();lines=[];line=''
  for word in title:
   t=(line+' '+word).strip()
   if line and d.textlength(t,font=font(15,True))>W-16:lines.append(line);line=word
   else:line=t
  if line:lines.append(line)
  for i,t in enumerate(lines[:3]):d.text((x,y-H//2+8+i*18),t,font=font(14,True),fill='#f2f5f7',anchor='mt')
  d.text((x,y+18),fid.removeprefix(PREFIX),font=font(9),fill='#a6b8c8',anchor='mt')
  if fid in gates:d.text((x,y+32),gates[fid],font=font(9,True),fill='#e4c77e',anchor='mt')
 d.text((36,height-85),'Ba hướng cơ cấu nằm ngang; mỗi capstone cần các dự án trong hướng. Chỉ chọn một hướng.',font=font(15),fill='#d6e0e7')
 d.text((36,height-55),f'{len(land)} focus • X={minx}–{maxx}, Y=2–{maxy} • render tĩnh từ prerequisite và tọa độ trong code',font=font(14),fill='#9fb0bd')
 OUT.parent.mkdir(parents=True,exist_ok=True);im.save(OUT);im.save(CURRENT)
 print(f'Wrote {OUT} and updated {CURRENT} ({width}x{height}), {len(land)} focuses, {len(mutex)} mutex pairs')
if __name__=='__main__':main()
