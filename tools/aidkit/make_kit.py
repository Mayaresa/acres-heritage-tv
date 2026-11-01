# Usage (from anywhere): python3 tools/aidkit/make_kit.py <slug>
# Makes out/<slug>/ : A4 sign (png+pdf) + two QR pngs for the AID in aids.json. Needs: pip install qrcode[pil]; node + playwright.
import sys,json,os,subprocess,qrcode,html
HERE=os.path.dirname(os.path.abspath(__file__));REPO=os.path.dirname(os.path.dirname(HERE))
slug=sys.argv[1]; a=json.load(open(os.path.join(REPO,'aids.json')))[slug]
base='https://mayaresa.github.io/acres-heritage-tv/'
U={'free':f'{base}?aid={slug}&utm_source=qr&utm_campaign=aid_watch','join':f'{base}?aid={slug}&utm_source=qr&utm_campaign=aid_order#order'}
out=os.path.join(os.getcwd(),'out',slug);os.makedirs(out,exist_ok=True)
for k,u in U.items():
    q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,border=0);q.add_data(u);q.make(fit=True);m=q.get_matrix();n=len(m)
    open(f'{out}/{k}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" shape-rendering="crispEdges" fill="#272727">'+''.join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for y,r in enumerate(m) for x,v in enumerate(r) if v)+'</svg>')
    q2=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,border=4,box_size=24);q2.add_data(u);q2.make(fit=True)
    q2.make_image(fill_color='#272727',back_color='white').save(f'{out}/{slug}-qr-{"watch" if k=="free" else "order"}.png')
import re
d=''.join(c for c in a['wa'] if c.isdigit())
wa=re.sub(r'^233(\d{2})(\d{3})(\d{4})$',r'+233 \1 \2 \3',d);wa=re.sub(r'^1(\d{3})(\d{3})(\d{4})$',r'+1 \1 \2 \3',wa)
wa=wa if wa.startswith('+') else '+'+wa
s=open(os.path.join(HERE,'sheet.html')).read().replace('__DIR__','file://'+HERE)
s=s.replace('src="free.svg"',f'src="file://{os.path.abspath(out)}/free.svg"').replace('src="join.svg"',f'src="file://{os.path.abspath(out)}/join.svg"')
local=('0'+d[3:]) if d.startswith('233') else wa
local=re.sub(r'^(\d{3})(\d{3})(\d{4})$',r'\1 \2 \3',local)
area=a.get('areaText') or ((a.get('area','')+' & Surroundings') if a.get('area') else '')
label=(a.get('label') or 'Your Local FONIO Distributor').upper()
band=f'<div class="aband"><div class="r1"><span class="al">{html.escape(label)}</span><b>{html.escape(a["name"])}</b></div><div class="r2"><span class="ap">📞 Call or WhatsApp {local}</span>{"<span class=ar>"+html.escape(area)+"</span>" if area else ""}</div></div>'
s=s.replace('<div class="cards">',band+'<div class="cards">')
s=s.replace('<span>WhatsApp +1 240 408 0158</span>','')
if a.get('gift'):
    s=s.replace('<h2>Unlock all<br>31 episodes</h2><div class="sub">Order 5kg DIM Fonio · ₵330 club price<br>Season Pass included</div>','<h2>Send fonio<br>to family</h2><div class="sub">5kg DIM Fonio delivered in Ghana<br>All 31 episodes included for you</div>').replace('SCAN TO ORDER &amp; JOIN','SCAN TO SEND A BAG')
s=s.replace('</style>','.aband{background:#0A8FC2;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;height:118px;font-size:28px;font-weight:700;white-space:nowrap}.aband .r1,.aband .r2{display:flex;align-items:center;gap:22px}.aband .al{font-weight:900;font-size:22px;letter-spacing:4px}.aband b{font-family:"Baloo 2";font-weight:800;font-size:40px;line-height:1;color:#FFF200}.aband .ar{background:#fff;color:#0A6F97;font-weight:800;padding:6px 18px;border-radius:999px;font-size:24px}.cards{padding:26px 64px 18px !important}.qr img{width:330px !important;height:330px !important}.ft{justify-content:center !important;gap:80px}</style>')
open(f'{out}/sheet.html','w').write(s)
subprocess.run(['node','-e',f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1754,height:1240}},deviceScaleFactor:2}});
await p.goto('file://{os.path.abspath(out)}/sheet.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({{path:'{out}/{slug}-qr-sign.png'}});await p.pdf({{path:'{out}/{slug}-qr-sign.pdf',width:'297mm',height:'210mm',printBackground:true,pageRanges:'1',scale:297/(1754/96*25.4)}});await b.close();}})();"""],check=True)
print('ok',out)
