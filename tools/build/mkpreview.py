import json,re
s=open('tools/base.html').read()
blob=open('/home/claude/acres-secure/aid-blob.json').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:80],s.count(a)); s=s.replace(a,b)
# noindex
rep('<head>','<head>\n<meta name="robots" content="noindex,nofollow">')
# --- desk products ---
a=s.index('      <div class="k">NOW SELLING</div>');b=s.index('      <form class="order" id="order" novalidate>')
s=s[:a]+'''      <div class="k">NOW SELLING</div>
      <h3>DIM Fonio</h3>
      <p class="note" id="priceNote">Club member price · Pick up at a market stand, or delivery (+ delivery cost)</p>
      <div class="prods">
        <div class="prod"><img src="media/bag.png" alt="5kg bag of DIM Fonio">
          <div class="pt"><b>5kg Family Bag</b><small>5 × 1kg packs in one bag</small></div><span class="pp"><i id="pBag">₵330</i><s id="wBag">₵375</s></span>
          <div class="step"><button type="button" data-it="bag" data-d="-1" aria-label="One bag fewer">−</button><output id="qBag">1</output><button type="button" data-it="bag" data-d="1" aria-label="One bag more">+</button></div></div>
        <div class="prod"><img id="imgTwo" src="media/case10.jpg" alt="Case of ten 1kg packs of DIM Fonio" >
          <div class="pt"><b id="nmTwo">1kg Case of 10</b><small id="subTwo">10 × 1kg packs · share or store</small></div><span class="pp"><i id="pCase">₵670</i><s id="wCase">₵750</s></span>
          <div class="step"><button type="button" data-it="case" data-d="-1" aria-label="One fewer">−</button><output id="qCase">0</output><button type="button" data-it="case" data-d="1" aria-label="One more">+</button></div></div>
      </div>
'''+s[b:]
a=s.index('        <div class="row qty"><span class="fl">Bags of 5kg</span>');b=s.index('        <fieldset class="how">')
s=s[:a]+s[b:]
# AID corner button + stand section after the desk
rep('''      <a class="join" href="https://chat.whatsapp.com/BsuWk5uMUHa32gczMyat8a" target="_blank" rel="noopener">Join the club on WhatsApp ›</a>
    </aside>''','''      <a class="join" href="https://chat.whatsapp.com/BsuWk5uMUHa32gczMyat8a" target="_blank" rel="noopener">Join the club on WhatsApp ›</a>
    </aside>''')
rep('''  </div>

  <section class="guide learn"''','''    <section class="stands" aria-labelledby="standsH">
      <div class="st-k">COMING TO YOUR COMMUNITY</div>
      <h3 id="standsH">ACRES Heritage Market Stands</h3>
      <p class="st-lead">Look out for our kente-topped market stands in communities and markets across Ghana, starting in Accra.</p>
      <div class="st-feats">
        <div class="sf"><span>🌾</span><b>Fonio all year round</b><small>DIM Fonio on display every day. Buy on the spot, or pre-order as a club member and save.</small></div>
        <div class="sf"><span>🥣</span><b>Free fonio tasting</b><small>Taste before you buy. Fonio tasting every Friday at our stands.</small></div>
        <div class="sf"><span>🗓️</span><b>Seasonal heritage foods</b><small>Pre-order seasonal foods like Frafra potato, wild pepper and dwarf okro, and pick them up at your stand.</small></div>
      </div>
    </section>
  </div>

  <section class="guide learn"''')
a0=s.index('<div class="aidwrap">');a1=s.index('</div>\n\n  <div class="grid">',a0)
s=s[:a1]+'<button type="button" class="aidcorner" id="aidCornerBtn"><i>🔒</i><span><small>FOR DISTRIBUTORS ONLY</small><b>AID Wholesale Corner</b></span><em>›</em></button>'+s[a1:]
# AID modal
rep('<div class="modal" id="passModal"','''<div class="modal" id="aidModal" hidden role="dialog" aria-modal="true" aria-labelledby="amT">
  <div class="mbox aidbox">
    <button class="mx" id="amClose" type="button" aria-label="Close">×</button>
    <div class="k">FOR ACRES INDEPENDENT DISTRIBUTORS</div>
    <h3 id="amT">AID Wholesale Corner</h3>
    <div id="amLock"><p class="mnote">Enter your AID code to see wholesale prices and order stock.</p>
      <div class="am-row"><input id="amCode" type="text" autocomplete="off" autocapitalize="characters" placeholder="AID code"><button type="button" id="amGo">Open</button></div>
      <p class="err" id="amErr" hidden>That code didn't work. Check with ACRES HQ.</p></div>
    <div id="amOpen" hidden>
      <div id="amItems"></div>
      <label class="fld"><span class="fl">Your name (AID)</span><input id="amName" type="text"></label>
      <div class="total"><span>Stock total</span><b id="amTot">₵0</b></div>
      <p class="err" id="amMin" hidden></p>
      <button class="send" type="button" id="amSend">Send stock order to ACRES HQ</button>
      <p class="note small" id="amNote"></p>
    </div>
  </div>
</div>
<div class="modal" id="passModal"''')
# text fixes mentioning 330
rep('Order your first 5kg DIM Fonio (₵330) below','Order your first DIM Fonio below')
rep("items.push('<i>5kg DIM Fonio ₵330</i> · Order right here on this page');","items.push('<i>DIM Fonio · 5kg bags & 1kg cases</i> · Order right here on this page');")
# CSS
css='''
/* products + AID corner + stands (preview) */
.prods{display:flex;flex-direction:column;gap:10px}
.prod{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.55);border-radius:14px;padding:8px 10px}
.prod img{flex:none;width:64px;height:64px;object-fit:contain;filter:drop-shadow(0 4px 6px rgba(0,0,0,.25))}
.prod img.sq{object-fit:cover;border-radius:8px;filter:none;box-shadow:0 2px 6px rgba(0,0,0,.2)}
.pt{flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.2}
.pt b{font-family:var(--display);font-weight:800;font-size:18px}.pt small{font-size:12px;opacity:.8}
.pp{margin-top:3px}.pp i{font-style:normal;font-family:var(--display);font-weight:800;font-size:24px}.pp s{font-size:14px;opacity:.55;margin-left:5px}
.prod{display:grid;grid-template-columns:64px 1fr auto;grid-template-areas:'img txt txt' 'img price step';column-gap:10px;row-gap:2px}.prod img{grid-area:img;align-self:center}.pt{grid-area:txt}.prod .pp{grid-area:price;align-self:center;margin:0}.prod .step{grid-area:step;flex:none}.prod .step button{width:38px;height:38px;font-size:20px}.prod .step output{min-width:28px;font-size:19px}
.aidcorner{display:flex;align-items:center;gap:12px;width:100%;margin-top:10px;background:#0A8FC2;color:#fff;box-shadow:0 0 0 3px #fff,0 6px 18px rgba(10,143,194,.45);border:0;border-radius:14px;padding:12px 14px;text-align:left;cursor:pointer;font:inherit}.aidcorner i{flex:none;width:44px;height:44px;border-radius:50%;background:#fff;color:#0A8FC2;font-style:normal;font-size:20px;display:flex;align-items:center;justify-content:center}.aidcorner b{display:block;font-size:17px;font-weight:800}.aidcorner small{display:block;font-size:12px;font-weight:800;letter-spacing:1.5px;color:var(--lemon)}.aidcorner em{margin-left:auto;font-style:normal;font-weight:800;font-size:22px}
.aidbox .am-row{display:flex;gap:8px;margin:8px 0}.aidbox .am-row input{flex:1;min-width:0;padding:12px;border-radius:10px;border:2px solid #ccc;font-size:16px;text-transform:uppercase}
.aidbox .am-row button{padding:0 18px;border-radius:10px;border:0;background:var(--green);font-weight:800;color:#272727}
.am-it{display:flex;align-items:center;gap:10px;border:2px solid #e5e5e5;border-radius:12px;padding:10px;margin:8px 0}
.am-it .pt b{font-size:16px}.am-it .pt em{font-style:normal;font-size:12px;color:#4f8a12;font-weight:700}
.stands{margin-top:18px;border-radius:18px;padding:18px 20px 20px;background:#17200f;border:2px solid rgba(200,255,122,.35);color:#fff}
.st-k{color:var(--green);font-weight:800;font-size:12px;letter-spacing:3px}
.stands h3{margin:2px 0 4px;font-family:var(--display);font-weight:800;font-size:clamp(22px,5.5vw,30px);line-height:1.05}
.st-lead{margin:0 0 12px;color:#dfe5d6;font-size:15px}
.st-feats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px}
.sf{background:rgba(255,255,255,.06);border-radius:14px;padding:12px;display:flex;flex-direction:column;gap:3px}
.sf span{font-size:24px}.sf b{color:var(--lemon);font-size:15px}.sf small{color:#dfe5d6;font-size:13px;line-height:1.35}
'''
rep('</style>\n\n<div class="wrap">',css+'</style>\n\n<div class="wrap">')
# JS: replace order IIFE
a=s.index('// order form -> prefilled WhatsApp message\n(function(){');b=s.index('  upd();\n})();',a)+len('  upd();\n})();')
js='''// order form -> prefilled WhatsApp message (two products; prices depend on who the buyer came through)
// Direct club members (no AID) get club prices; customers of an AID see the AID's retail prices.
const PRICES={club:{bag:330,bagWas:350,case:670,caseWas:750,note:'Club member price · Pick up at a market stand, or delivery (+ delivery cost)'},
  aid:{bag:350,bagWas:0,case:75,caseWas:0,note:'Prices from your local distributor · Pickup or express delivery'}};
// Club members buy wholesale (the case of 10); AID customers buy single 1kg packs.
const TWO={club:{name:'1kg Case of 10',sub:'10 × 1kg packs · share or store',img:'media/case10.jpg',alt:'Case of ten 1kg packs of DIM Fonio',unit:'case'},aid:{name:'1kg Pack',sub:'A single 1kg pack · try it first',img:'media/pack1kg.png',alt:'1kg pack of DIM Fonio',unit:'pack'}};
const Q={bag:1,case:0};
// An AID may set their own retail price in aids.json: price5 (₵330–₵350, default ₵350) and price1 (up to ₵75, default ₵75).
const clamp=(v,lo,hi,d)=>{v=+v;return isFinite(v)&&v>0?Math.min(hi,Math.max(lo,v)):d;};
const PR=()=>AID?Object.assign({},PRICES.aid,{bag:clamp(AID.price5,330,350,350),case:clamp(AID.price1,50,75,75)}):PRICES.club;
function paintPrices(){const p=PR();document.getElementById('pBag').textContent='₵'+p.bag;document.getElementById('wBag').textContent=p.bagWas?'₵'+p.bagWas:'';
  document.getElementById('pCase').textContent='₵'+p.case;document.getElementById('wCase').textContent=p.caseWas?'₵'+p.caseWas:'';document.getElementById('priceNote').textContent=p.note;const t=AID?TWO.aid:TWO.club,im=document.getElementById('imgTwo');document.getElementById('nmTwo').textContent=t.name;document.getElementById('subTwo').textContent=t.sub;if(!im.src.endsWith(t.img)){im.src=t.img;im.alt=t.alt;im.classList.remove('sq');}}
(function(){
  const tot=document.getElementById('tot');
  const how=()=>document.querySelector('input[name=how]:checked').value;
  function upd(){paintPrices();const p=PR();document.getElementById('qBag').textContent=Q.bag;document.getElementById('qCase').textContent=Q.case;
    const t=Q.bag*p.bag+Q.case*p.case;tot.innerHTML='₵'+t+(how()==='delivery'?'<small>+ delivery cost</small>':'');document.getElementById('delNote').hidden=how()!=='delivery';document.getElementById('addrWrap').hidden=how()!=='delivery';return t;}
  window.updOrder=upd;
  document.querySelectorAll('.prod .step button').forEach(b=>b.onclick=()=>{const it=b.dataset.it,d=+b.dataset.d;Q[it]=Math.max(0,Math.min(it==='case'&&AID?50:20,Q[it]+d));upd();});
  document.querySelectorAll('input[name=how]').forEach(r=>r.addEventListener('change',upd));
  document.getElementById('order').addEventListener('submit',e=>{
    e.preventDefault();
    const nm=document.getElementById('nm'),ph=document.getElementById('ph');
    const gift=AID&&AID.gift,rnm=document.getElementById('rnm'),rph=document.getElementById('rph');const req=gift?[nm,ph,rnm,rph]:[nm,ph];
    const miss=req.filter(i=>!i.value.trim());req.forEach(i=>i.classList.toggle('bad',!i.value.trim()));
    const none=Q.bag+Q.case===0;
    document.getElementById('err').textContent=none?'Please choose at least one bag or case.':(gift?'Please add your name and phone, and the recipient\\'s name and phone.':'Please add your name and phone number.');
    document.getElementById('err').hidden=!(miss.length||none);if(none)return;if(miss.length){miss[0].focus();return;}
    const t=upd(),p=PR(),d=how()==='delivery',addr=document.getElementById('addr').value.trim();
    const lines=['*NEW ORDER · ACRES Heritage TV*','','Name: '+nm.value.trim(),'Phone: '+ph.value.trim()];
    if(Q.bag)lines.push('5kg Family Bag: '+Q.bag+' × ₵'+p.bag+' = ₵'+(Q.bag*p.bag));
    if(Q.case)lines.push((AID?TWO.aid:TWO.club).name+': '+Q.case+' × ₵'+p.case+' = ₵'+(Q.case*p.case));
    lines.push('Receive: '+(d?'Express delivery (please confirm delivery cost)':'Easy pickup'),'Zone: '+document.getElementById('zone').value);
    if(gift){lines[0]='*NEW DIASPORA ORDER · ACRES Heritage TV*';lines.push('Send to: '+rnm.value.trim(),'Recipient phone: '+rph.value.trim());}
    if(d)lines.push('Address/landmark: '+(addr||'(will share)'));
    lines.push('*Total: ₵'+t+(d?' + delivery':'')+'*','','Watching: Episode '+cur);
    lines.push(AID?'Distributor: '+AID.name+' ('+AID.slug+')':'Buyer type: Direct club member');
    track('order_whatsapp',{bags:Q.bag,cases:Q.case,value:t,currency:'GHS',delivery:d?'express':'pickup',watching_episode:cur});
    const url='https://api.whatsapp.com/send?phone='+orderNum()+'&text='+encodeURIComponent(lines.join('\\n'));
    const a=document.createElement('a');a.href=url;a.target='_blank';a.rel='noopener';document.body.appendChild(a);a.click();a.remove();
  });
  upd();setTimeout(upd,1500);setTimeout(upd,4000);
})();
// AID Wholesale Corner: prices are encrypted; only the AID code opens them.
const AIDBLOB=%s;
(function(){
  const M=document.getElementById('aidModal');let items=null,AQ={};
  const b64=x=>Uint8Array.from(atob(x),c=>c.charCodeAt(0));
  async function open(code){const k0=await crypto.subtle.importKey('raw',new TextEncoder().encode(code),'PBKDF2',false,['deriveKey']);
    const k=await crypto.subtle.deriveKey({name:'PBKDF2',salt:b64(AIDBLOB.s),iterations:150000,hash:'SHA-256'},k0,{name:'AES-GCM',length:256},false,['decrypt']);
    return JSON.parse(new TextDecoder().decode(await crypto.subtle.decrypt({name:'AES-GCM',iv:b64(AIDBLOB.i)},k,b64(AIDBLOB.c))));}
  function tot(){let t=0,bad=[];items.forEach(it=>{const q=AQ[it.id]||0;t+=q*it.price;if(q&&q<it.min)bad.push('Minimum order for '+it.name+' is '+it.min+' '+it.unit+(it.min>1?'s':'')+'.');document.getElementById('aq_'+it.id).textContent=q;});
    document.getElementById('amTot').textContent='₵'+t;const n=Object.values(AQ).reduce((a,b)=>a+b,0);const m=document.getElementById('amMin');m.textContent=bad.join(' ')||(n?'':'Add at least one item.');m.hidden=!(bad.length||!n);return {t,ok:!bad.length&&n>0};}
  function show(d){items=d.items;const box=document.getElementById('amItems');box.innerHTML='';
    items.forEach(it=>{AQ[it.id]=it.min;const r=document.createElement('div');r.className='am-it';
      r.innerHTML='<div class="pt"><b></b><small></small><span class="pp"><i></i></span><em></em></div><div class="step"><button type="button" data-d="-1">−</button><output id="aq_'+it.id+'"></output><button type="button" data-d="1">+</button></div>';
      r.querySelector('b').textContent=it.name;r.querySelector('small').textContent=it.sub+' · minimum '+it.min+' '+it.unit+(it.min>1?'s':'');r.querySelector('i').textContent='₵'+it.price+' a '+it.unit;r.querySelector('em').textContent=it.retail;
      r.querySelectorAll('button').forEach(bt=>bt.onclick=()=>{AQ[it.id]=Math.max(0,Math.min(200,(AQ[it.id]||0)+ +bt.dataset.d));tot();});box.appendChild(r);});
    document.getElementById('amNote').textContent=d.note;if(AID)document.getElementById('amName').value=AID.name;
    document.getElementById('amLock').hidden=true;document.getElementById('amOpen').hidden=false;tot();}
  document.getElementById('aidCornerBtn').onclick=()=>{M.hidden=false;track('aid_corner_open',{});};
  document.getElementById('amClose').onclick=()=>M.hidden=true;M.addEventListener('click',e=>{if(e.target===M)M.hidden=true;});
  const go=async()=>{const c=document.getElementById('amCode').value.trim().toUpperCase();try{show(await open(c));try{sessionStorage.setItem('acresAidCode',c);}catch(_){}}catch(_){document.getElementById('amErr').hidden=false;}};
  document.getElementById('amGo').onclick=go;document.getElementById('amCode').addEventListener('keydown',e=>{if(e.key==='Enter')go();});
  try{const c=sessionStorage.getItem('acresAidCode');if(c)open(c).then(show).catch(()=>{});}catch(_){}
  document.getElementById('amSend').onclick=()=>{const r=tot();if(!r.ok)return;const nm=document.getElementById('amName').value.trim();
    const lines=['*AID STOCK ORDER · ACRES*','','AID: '+(nm||'(name)')+(AID?' ('+AID.slug+')':'')];
    items.forEach(it=>{const q=AQ[it.id]||0;if(q)lines.push(it.name+': '+q+' × ₵'+it.price+' = ₵'+(q*it.price));});
    lines.push('*Total: ₵'+r.t+'*');track('aid_stock_order',{value:r.t,currency:'GHS'});
    const a=document.createElement('a');a.href='https://api.whatsapp.com/send?phone='+HQ_NUM+'&text='+encodeURIComponent(lines.join('\\n'));a.target='_blank';a.rel='noopener';document.body.appendChild(a);a.click();a.remove();};
})();''' % blob
s=s[:a]+js+s[b:]
open('preview.html','w').write(s)
print('ok')

# ================= CH 3: ACRES NANO market + Learn about ACRES =================
s=open('preview.html').read()
def rep2(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a)); s=s.replace(a,b)
rep2('<p>Heritage foods from our indigenous seeds. <b>Order below</b> from your local distributor.</p>','<p id="shopLine">Heritage foods from our indigenous seeds. <b>Order below</b> from your local distributor.</p>')
# AID rewards inside the corner
rep2("document.getElementById('amNote').textContent=d.note;","document.getElementById('amNote').textContent=d.note;if(d.rewards){const rw=document.getElementById('amRewards');rw.innerHTML='<div class=\"fl\">REFERRAL REWARDS · ACRES NANO</div>';d.rewards.forEach(t=>{const li=document.createElement('p');li.textContent='• '+t;rw.appendChild(li);});rw.hidden=false;}")
rep2('<p class="note small" id="amNote"></p>','<p class="note small" id="amNote"></p>\n      <div class="am-rw" id="amRewards" hidden></div>')
nano='''
    <aside class="desk nano" id="nanoDesk" aria-label="Order ACRES Nano" hidden>
      <div class="k">NOW SELLING · FOR FARMERS &amp; GARDENERS</div>
      <h3>ACRES Nano Organic Fertilizer</h3>
      <p class="nano-why">To make sure our foods grow in clean, living soil, our Heritage Garden Packs come with ACRES Nano Organic Fertilizer. <b>Start your soil today.</b></p>
      <div class="badges"><span>✔ University of Ghana tested</span><span>✔ PPRSD approved (MoFA)</span><span>✔ OMRI-listed organic</span></div>
      <div class="prods">
        <div class="prod"><img src="media/nano-acre.png" alt="ACRES Nano 1 Acre Farm Pack">
          <div class="pt"><b>1 Acre Farm Pack</b><small>10 capsules · treats 1 acre</small></div><span class="pp"><i>₵600</i></span>
          <div class="step"><button type="button" data-n="acre" data-d="-1" aria-label="One fewer">−</button><output id="nqAcre">1</output><button type="button" data-n="acre" data-d="1" aria-label="One more">+</button></div></div>
        <div class="prod"><img src="media/nano-garden.png" alt="ACRES Nano Garden Pack">
          <div class="pt"><b>Heritage Garden Pack</b><small>ACRES Nano fertilizer + 2 heritage seed varieties of your choice</small></div><span class="pp"><i>₵295</i></span>
          <div class="step"><button type="button" data-n="garden" data-d="-1" aria-label="One fewer">−</button><output id="nqGarden">0</output><button type="button" data-n="garden" data-d="1" aria-label="One more">+</button></div></div>
        <div class="prod"><img src="media/nano-garden.png" alt="ACRES Nano Garden Fertilizer Pack">
          <div class="pt"><b>Garden Fertilizer Pack</b><small>ACRES Nano fertilizer only</small></div><span class="pp"><i>₵195</i></span>
          <div class="step"><button type="button" data-n="gfert" data-d="-1" aria-label="One fewer">−</button><output id="nqGfert">0</output><button type="button" data-n="gfert" data-d="1" aria-label="One more">+</button></div></div>
      </div>
      <a class="rst" id="rstBtn" href="https://api.whatsapp.com/send?phone=233208168917&amp;text=Hello%20RST%2C%20I%27d%20like%20ACRES%20Nano%20Organic%20Fertilizer%20for%2010%2B%20acres." target="_blank" rel="noopener"><b>Farming 10 acres or more?</b><span>Bulk orders are handled by RST, our national distributor · WhatsApp RST ›</span></a>
      <form class="order" id="nanoOrder" novalidate>
        <div class="np-note">🚚 <b>Pre-order · Pre-pay · Delivery only.</b> We confirm your order and delivery cost, you pay by MoMo, then we deliver.</div>
        <label class="fld" id="seedWrap" hidden><span class="fl">Your 2 seed choices (Garden Pack)</span><input id="nSeeds" type="text" placeholder="e.g. Frafra potato, dwarf okro"></label>
        <label class="fld"><span class="fl">Delivery town, region and landmark</span><input id="nAddr" type="text" placeholder="e.g. Tamale, Northern Region, near the main market"></label>
        <label class="fld"><span class="fl">Your name</span><input id="nNm" type="text" autocomplete="name"></label>
        <label class="fld"><span class="fl">Your phone (WhatsApp)</span><input id="nPh" type="tel" inputmode="tel" placeholder="e.g. 024 123 4567"></label>
        <div class="total"><span>Total</span><b id="nTot">₵600</b></div>
        <p class="err" id="nErr" hidden></p>
        <button class="send" type="submit">Send my pre-order on WhatsApp</button>
        <p class="note small">Plus delivery cost, confirmed with you before you pay.</p>
      </form>
    </aside>'''
rep2('''    <section class="stands" aria-labelledby="standsH">''',nano+'''
    <section class="stands" id="standsSec" aria-labelledby="standsH">''')
learn='''
  <section class="guide learn" id="learnAcres" aria-label="Learn about ACRES Nano" hidden>
    <div class="learn-h">LEARN ABOUT ACRES NANO</div>
    <details class="whatf" open><summary><img src="media/nano-acre.png" alt="" width="56" height="56" style="object-fit:contain;background:#fff"><span><b>What is ACRES Nano?</b><small>Organic fertilizer for living soil · tap to read</small></span><i aria-hidden="true">＋</i></summary>
      <div class="wf-body">
        <img class="wf-hero" src="media/nano-farm.jpg" alt="Mixing ACRES Nano into a knapsack sprayer on a vegetable farm in Ghana" loading="lazy">
        <p>ACRES Nano Organic Fertilizer brings life back into the soil. It feeds and multiplies the soil's own beneficial microorganisms, which break down plant residues, build organic matter and turn nutrients into a form plants can take up.</p>
        <div class="wf-stats"><div><b>10</b><span>capsules treat 1 acre</span></div><div><b>48 hrs</b><span>to activate in water</span></div><div><b>1-0.1-5.5</b><span>NPK (organic)</span></div></div>
        <ul><li><b>Less to carry, more to grow:</b> a small pack replaces heavy bags</li><li><b>Stronger roots</b> and better water holding in the soil</li><li><b>Works with what you already use:</b> sprayer, drip, hose or watering can</li><li><b>Soil improves season after season</b></li></ul></div></details>
    <details class="whatf hist"><summary><span class="hico" aria-hidden="true">🎓</span><span><b>Proven in Ghana</b><small>University of Ghana field trial · tap to read</small></span><i aria-hidden="true">＋</i></summary>
      <div class="wf-body">
        <p>The Department of Crop Science, University of Ghana, Legon, tested ACRES Nano on lettuce in 2023. At the recommended rate it performed <b>as well as NPK 15:15:15 chemical fertilizer</b>, with no significant difference in leaves, chlorophyll or plant weight.</p>
        <div class="wf-stats"><div><b>+50%</b><span>more leaves than no fertilizer</span></div><div><b>+37%</b><span>heavier plants than no fertilizer</span></div><div><b>= NPK</b><span>same growth as 15:15:15</span></div></div>
        <p>After this trial, ACRES Nano was approved for distribution in Ghana by PPRSD, Ministry of Food and Agriculture. It is also OMRI-listed for organic production in the USA.</p>
        <p class="wf-note">Source: University of Ghana, Dept. of Crop Science, field evaluation on lettuce, May–July 2023.</p></div></details>
    <details class="whatf hist"><summary><span class="hico" aria-hidden="true">💧</span><span><b>How to use it</b><small>Activate · Dilute · Apply</small></span><i aria-hidden="true">＋</i></summary>
      <div class="wf-body"><ol class="tl">
        <li><em>Step 1</em><b>Activate</b><span>Put each capsule in about 60 ml of non-chlorinated water (rain, borehole or bottled water) in a bottle. Shake to dissolve, loosen the cap and leave for 48 hours in a cool place out of the sun.</span></li>
        <li><em>Step 2</em><b>Dilute</b><span>Mix the activated liquid with more water. For a garden or small plot, add about 60 ml of activated ACRES to 8 litres of water in a knapsack sprayer.</span></li>
        <li><em>Step 3</em><b>Apply</b><span>Spray or water it onto the soil before planting, on seeds and seedlings, and on the leaves as plants grow. Use within 10 days of activating.</span></li></ol>
        <p class="wf-note">Store capsules in a cool, dry place out of direct sunlight. Not for human consumption. Keep out of reach of children. For your crop and land size, ask your ACRES representative.</p></div></details>
    <details class="whatf hist"><summary><span class="hico" aria-hidden="true">🌿</span><span><b>What's inside, and is it safe?</b><small>Natural ingredients · tap to read</small></span><i aria-hidden="true">＋</i></summary>
      <div class="wf-body"><ul><li><b>Sea kelp</b>, the source of its natural potash</li><li><b>Humic and fulvic acids</b></li><li><b>Enzymes and beneficial soil microbes</b></li><li><b>Guaranteed analysis:</b> Nitrogen 1.0%, Phosphate 0.1%, Soluble Potash 5.5%</li></ul>
        <p>Tested as not toxic, not corrosive and not an irritant. Safe to handle and store, with no special disposal needed.</p></div></details>
  </section>'''
rep2('''  <section class="guide learn" aria-label="Learn about fonio">''',learn+'''
  <section class="guide learn" id="learnFonio" aria-label="Learn about fonio">''')
css2='''
.nano .nano-why{margin:0;font-size:15px;line-height:1.4}.badges{display:flex;flex-wrap:wrap;gap:6px}.badges span{background:#17200f;color:#c8ff7a;font-weight:800;font-size:12px;border-radius:999px;padding:5px 10px}
.rst{display:block;background:#17200f;color:#fff;border-radius:14px;padding:12px 14px;text-decoration:none}.rst b{display:block;color:var(--lemon);font-size:16px}.rst span{font-size:13px;color:#dfe5d6}
.np-note{background:rgba(255,255,255,.6);border-radius:12px;padding:10px 12px;font-size:14px;line-height:1.35}
.am-rw{margin-top:12px;border-top:2px solid #e5e5e5;padding-top:10px}.am-rw p{margin:4px 0;font-size:14px}
'''
rep2('</style>\n\n<div class="wrap">',css2+'</style>\n\n<div class="wrap">')
js2='''
// ===== CH 3 swaps the market: ACRES Nano for farmers & gardeners; fonio stays on CH 1 & 2 =====
const NANO={acre:{n:'1 Acre Farm Pack (10 capsules)',p:600,q:1},garden:{n:'Heritage Garden Pack (Nano fertilizer + 2 seeds)',p:295,q:0},gfert:{n:'Garden Fertilizer Pack (Nano fertilizer only)',p:195,q:0}};
function nanoUpd(){let t=0;for(const k in NANO){t+=NANO[k].q*NANO[k].p;document.getElementById('nq'+k.charAt(0).toUpperCase()+k.slice(1)).textContent=NANO[k].q;}
  document.getElementById('nTot').innerHTML='₵'+t+'<small>+ delivery cost</small>';document.getElementById('seedWrap').hidden=!NANO.garden.q;
  const big=NANO.acre.q>=10;document.getElementById('rstBtn').classList.toggle('hot',big);return t;}
document.querySelectorAll('#nanoDesk .step button').forEach(b=>b.onclick=()=>{const k=b.dataset.n;NANO[k].q=Math.max(0,Math.min(k==='acre'?9:20,NANO[k].q+ +b.dataset.d));
  if(k==='acre'&&+b.dataset.d>0&&NANO.acre.q===9){document.getElementById('nErr').textContent='For 10 acres or more, please contact RST (button above) for bulk supply.';document.getElementById('nErr').hidden=false;}nanoUpd();});
document.getElementById('nanoOrder').addEventListener('submit',e=>{e.preventDefault();const err=document.getElementById('nErr');
  const f=['nNm','nPh','nAddr'].map(id=>document.getElementById(id));const miss=f.filter(i=>!i.value.trim());f.forEach(i=>i.classList.toggle('bad',!i.value.trim()));
  const none=!(NANO.acre.q+NANO.garden.q+NANO.gfert.q);err.textContent=none?'Please choose at least one pack.':'Please add your name, phone and delivery location.';err.hidden=!(none||miss.length);if(none||miss.length)return;
  const t=nanoUpd();const L=['*ACRES NANO PRE-ORDER · ACRES Heritage TV (CH 3)*','','Name: '+f[0].value.trim(),'Phone: '+f[1].value.trim()];
  for(const k in NANO)if(NANO[k].q)L.push(NANO[k].n+': '+NANO[k].q+' × ₵'+NANO[k].p+' = ₵'+(NANO[k].q*NANO[k].p));
  if(NANO.garden.q)L.push('Seed choices: '+(document.getElementById('nSeeds').value.trim()||'(will choose)'));
  L.push('Deliver to: '+f[2].value.trim(),'*Total: ₵'+t+' + delivery (please confirm)*','Payment: pre-pay by MoMo before delivery');
  L.push(AID?'Referred by AID: '+AID.name+' ('+AID.slug+')':'Referred by: none (direct)');
  track('nano_preorder',{value:t,currency:'GHS',acres:NANO.acre.q,garden:NANO.garden.q,gfert:NANO.gfert.q});
  const a=document.createElement('a');a.href='https://api.whatsapp.com/send?phone='+HQ_NUM+'&text='+encodeURIComponent(L.join('\\n'));a.target='_blank';a.rel='noopener';document.body.appendChild(a);a.click();a.remove();});
const SHOPLINE=document.getElementById('shopLine').innerHTML;
function applyCh3(n){const three=n===3;
  document.querySelector('.desk:not(.nano)').hidden=three;document.getElementById('nanoDesk').hidden=!three;
  document.getElementById('standsSec').hidden=three;document.getElementById('learnFonio').hidden=three;document.getElementById('learnAcres').hidden=!three;
  document.getElementById('shopLine').innerHTML=three?'Clean, living soil for your farm and garden. <b>Pre-order below</b> for delivery.':SHOPLINE;}
const _setCh=setChannel;setChannel=function(n){_setCh(n);applyCh3(n);};
nanoUpd();applyCh3(CH);
'''
i=s.rindex('</script>')
s=s[:i]+js2+s[i:]
s=s.replace(".rst b{",".rst.hot{box-shadow:0 0 0 3px var(--lemon)}.rst b{")
open('preview.html','w').write(s)
print('ch3 ok')

# ================= CH 3 v2: price change, ACRES farm videos, own-video player, Learn videos, Africa gallery =================
import json
s=open('preview.html').read()
def rep3(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:80],s.count(a)); s=s.replace(a,b)
# Garden fertilizer pack price
rep3('<span class="pp"><i>₵195</i></span>','<span class="pp"><i>₵225</i></span>')
rep3("gfert:{n:'Garden Fertilizer Pack (Nano fertilizer only)',p:195,q:0}","gfert:{n:'Garden Fertilizer Pack (Nano fertilizer only)',p:225,q:0}")
# Farm folder first in CH 3
a=s.index('const SEEDS=')+len('const SEEDS=');b=s.index(';\nconst SEEDSEQ')
seeds=json.loads(s[a:b])
farm={"n":"ACRES Nano on Ghanaian Farms","i":"🌱","v":[
 ["8CkHXrmPg3A","Carrot Farmer Boosts Yield","David Ayaba, Ashanti Region, shares his ACRES Nano results.","ACRES"],
 ["awMkgdfLTYk","Field Demo in Lave, Volta Region","Farmers see ACRES Nano applied in the field.","ACRES"],
 ["vMOehJeWPVU","Maize Trial at Ashaiman","Throwback 2023: ACRES Nano on maize in Greater Accra.","ACRES"],
 ["media/nano-pepper.mp4","Pepper Farm Grown with ACRES Nano","A healthy pepper crop in Ghana.","ACRES"],
 ["media/nano-explainer.mp4","How to Use ACRES Nano","10 capsules per acre: activate, dilute, apply.","ACRES"]]}
seeds=[farm]+[f for f in seeds if f['n']!=farm['n']]
s=s[:a]+json.dumps(seeds,ensure_ascii=False,separators=(',',':'))+s[b:]
# local-aware thumbnails + LOCAL flag
rep3("const THUMB=id=>'https://i.ytimg.com/vi/'+id+'/mqdefault.jpg';","var LOCAL=false,EXTRA=false;const ISLOC=id=>id.startsWith('media/');const THUMB=id=>ISLOC(id)?id.replace('.mp4','.jpg'):'https://i.ytimg.com/vi/'+id+'/mqdefault.jpg';")
rep3("setInterval(()=>{if(CH!==3||!ytPlayer||!ytPlayer.getCurrentTime)return;","setInterval(()=>{if(CH!==3||LOCAL||!ytPlayer||!ytPlayer.getCurrentTime)return;")
rep3('<div class="ytbox" id="ytBox" hidden><div id="ytP"></div>','<div class="ytbox" id="ytBox" hidden><div id="ytP"></div><video id="locV" playsinline preload="metadata" hidden></video>')
rep3('.ytbox{position:absolute;inset:0;z-index:2;background:#000}','.ytbox{position:absolute;inset:0;z-index:2;background:#000}.ytbox #locV{position:absolute;inset:0;width:100%;height:100%;background:#000;object-fit:contain}')
# Learn: explainer button in How to use, ACRES story, Africa gallery
rep3('<div class="wf-body"><ol class="tl">\n        <li><em>Step 1</em><b>Activate</b>','<div class="wf-body"><button type="button" class="lv" data-v="media/nano-explainer.mp4" data-t="How to Use ACRES Nano" data-s="10 capsules per acre: activate, dilute, apply."><img src="media/nano-explainer.jpg" alt=""><span><b>▶ Watch: How to use ACRES Nano</b><small>5 min explainer</small></span></button><ol class="tl">\n        <li><em>Step 1</em><b>Activate</b>')
story='''
    <details class="whatf hist"><summary><span class="hico" aria-hidden="true">🎬</span><span><b>Watch the ACRES story</b><small>The Problem · The Solution · The Science</small></span><i aria-hidden="true">＋</i></summary>
      <div class="wf-body">
        <button type="button" class="lv" data-v="dy3wzy2EZ6k" data-t="ACRES Agriculture: The Problem" data-s="Why our soils and food need change."><img src="https://i.ytimg.com/vi/dy3wzy2EZ6k/mqdefault.jpg" alt=""><span><b>▶ 1 · The Problem</b><small>11 min</small></span></button>
        <button type="button" class="lv" data-v="6bJUGN7mHaU" data-t="ACRES Agriculture: The Solution" data-s="How ACRES Nano restores living soil."><img src="https://i.ytimg.com/vi/6bJUGN7mHaU/mqdefault.jpg" alt=""><span><b>▶ 2 · The Solution</b><small>6 min</small></span></button>
        <button type="button" class="lv" data-v="tngKiDJoXMc" data-t="ACRES Agriculture: The Science" data-s="The science behind ACRES Nano."><img src="https://i.ytimg.com/vi/tngKiDJoXMc/mqdefault.jpg" alt=""><span><b>▶ 3 · The Science</b><small>12 min</small></span></button>
      </div></details>
    <details class="whatf hist"><summary><span class="hico" aria-hidden="true">🌍</span><span><b>ACRES across Africa</b><small>Ghana · Tanzania · Burkina Faso</small></span><i aria-hidden="true">＋</i></summary>
      <div class="wf-body">
        <div class="gal-h">GHANA</div>
        <button type="button" class="lv" data-v="media/nano-deputy.mp4" data-t="Deputy Minister visits the ACRES stand" data-s="British Council, Accra."><img src="media/nano-deputy.jpg" alt=""><span><b>▶ The Deputy Minister of Food and Agriculture visits the ACRES stand</b><small>British Council, Accra</small></span></button>
        <button type="button" class="lv" data-v="media/nano-chiefs.mp4" data-t="ACRES with the Chiefs and people" data-s="Presenting ACRES Nano to a community in Ghana."><img src="media/nano-chiefs.jpg" alt=""><span><b>▶ Presenting ACRES Nano to the Chiefs and people of a community</b><small>Ghana</small></span></button>
        <div class="gal-h">TANZANIA</div>
        <div class="gal"><img src="media/gallery/tz1.jpg" alt="Presenting ACRES Nano at the AfDB stand" loading="lazy"><img src="media/gallery/tz2.jpg" alt="" loading="lazy"><img src="media/gallery/tz3.jpg" alt="" loading="lazy"></div>
        <p class="gal-c">ACRES Nano Organic Fertilizer presented at the African Development Bank's Africa Fertilizer Financing Mechanism stand, Tanzania. <span>Swipe ›</span></p>
        <div class="gal-h">BURKINA FASO</div>
        <div class="gal"><img src="media/gallery/bf1.jpg" alt="ACRES team with farmers in a maize field" loading="lazy"><img src="media/gallery/bf2.jpg" alt="" loading="lazy"><img src="media/gallery/bf3.jpg" alt="" loading="lazy"><img src="media/gallery/bf4.jpg" alt="" loading="lazy"></div>
        <p class="gal-c">PhD students from the University of Ouagadougou took ACRES Nano to farmers in all 13 regions, teaching in French under trees, in homes, offices and villages. <span>Swipe ›</span></p>
      </div></details>
  </section>'''
i=s.index('<section class="guide learn" id="learnAcres"');j=s.index('\n  </section>',i)
s=s[:j]+story+s[j+len('\n  </section>'):]
css3='''
.lv{display:flex;align-items:center;gap:12px;width:100%;margin:0 0 10px;background:rgba(255,255,255,.06);border:2px solid rgba(200,255,122,.35);border-radius:14px;padding:8px;color:inherit;font:inherit;text-align:left;cursor:pointer}
.lv img{flex:none;width:112px;height:63px;object-fit:cover;border-radius:8px;background:#111}.lv b{display:block;font-size:15px;line-height:1.25}.lv small{display:block;color:var(--muted);font-size:12px;margin-top:2px}
.gal-h{margin:14px 0 8px;font-weight:900;font-size:12px;letter-spacing:3px;color:var(--lemon)}
.gal{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;padding-bottom:4px}
.gal img{flex:none;height:220px;width:auto;border-radius:12px;scroll-snap-align:start}
.gal-c{margin:6px 0 0;font-size:13px;color:#dfe5d6;line-height:1.4}.gal-c span{color:var(--green);font-weight:800}
'''
rep3('</style>\n\n<div class="wrap">',css3+'</style>\n\n<div class="wrap">')
js3='''
// ===== CH 3 player: plays YouTube items and our own hosted videos (media/*.mp4) =====
const locV=document.getElementById('locV');
function playItem(v,lab,q){sdClear();$s('sdEnd').hidden=true;EXTRA=q==null;if(q!=null)seedCur=q;
  $s('ytPause').style.backgroundImage='url('+(ISLOC(v[0])?v[0].replace('.mp4','.jpg'):'https://i.ytimg.com/vi/'+v[0]+'/hqdefault.jpg')+')';$s('ypTitle').textContent=v[1];
  document.getElementById('nowLab').textContent=lab;document.getElementById('nowTitle').textContent=v[1];document.getElementById('nowSub').textContent=v[2]+' · Video: '+(v[3]||'Jibril Enterprise');
  document.getElementById('prev').disabled=false;document.getElementById('next').disabled=false;renderSeeds();track('seed_play',{video:v[1]});
  if(ISLOC(v[0])){LOCAL=true;try{ytPlayer&&ytPlayer.pauseVideo&&ytPlayer.pauseVideo();}catch(_){}document.getElementById('ytP').style.visibility='hidden';
    locV.hidden=false;locV.src=v[0];locV.play().catch(()=>{});ytPaint(ytState());return;}
  LOCAL=false;locV.pause();locV.hidden=true;locV.removeAttribute('src');document.getElementById('ytP').style.visibility='';ytPaint(-1);
  loadYT().then(()=>{if(CH!==3)return;
    if(!ytPlayer){ytPlayer=new YT.Player('ytP',{videoId:v[0],host:'https://www.youtube-nocookie.com',playerVars:{playsinline:1,rel:0,modestbranding:1,autoplay:1,controls:0,disablekb:1,fs:0,iv_load_policy:3,cc_load_policy:0},
      events:{onReady:e=>{if(CH===3&&!LOCAL)e.target.playVideo();},onStateChange:e=>{if(LOCAL)return;ytPaint(e.data);if(e.data===0&&CH===3){track('seed_complete',{video:v[1]});if(!EXTRA)sdShowEnd();}}}});}
    else ytPlayer.loadVideoById(v[0]);});}
playSeed=function(q,auto){const {k,j,v}=seedAt(q);playItem(v,'NOW SHOWING · '+SEEDS[k].n.toUpperCase()+' · '+(j+1)+' OF '+SEEDS[k].v.length,q);};
const _ytState=ytState;ytState=function(){if(LOCAL)return locV.ended?0:(locV.paused?2:1);return _ytState();};
const _ytToggle=ytToggle;ytToggle=function(){if(LOCAL){if(locV.paused){locV.muted=false;locV.play().catch(()=>{});}else locV.pause();return;}_ytToggle();};
$s('ytShield').onclick=()=>ytToggle();$s('ytPause').onclick=()=>ytToggle();$s('ytPlay').onclick=()=>ytToggle();
const _ytProg=$s('ytProg').onclick;$s('ytProg').onclick=e=>{if(LOCAL){const r=e.currentTarget.getBoundingClientRect();if(locV.duration)locV.currentTime=(e.clientX-r.left)/r.width*locV.duration;return;}_ytProg(e);};
['play','pause','playing','waiting'].forEach(ev=>locV.addEventListener(ev,()=>ytPaint(ytState())));
locV.addEventListener('ended',()=>{ytPaint(0);track('seed_complete',{video:$s('ypTitle').textContent});if(!EXTRA)sdShowEnd();});
locV.addEventListener('timeupdate',()=>{if(!LOCAL)return;const t=locV.currentTime||0,d=locV.duration||0;$s('ytFill').style.width=(d?t/d*100:0)+'%';$s('ytTime').textContent=fmtT(t)+' / '+fmtT(d);});
const _ytStop=ytStop;ytStop=function(){locV.pause();_ytStop();};
document.querySelectorAll('.lv').forEach(b=>b.onclick=()=>{if(CH!==3)setChannel(3);playItem([b.dataset.v,b.dataset.t,b.dataset.s,'ACRES'],'NOW SHOWING · LEARN ABOUT ACRES NANO',null);document.querySelector('.set').scrollIntoView({behavior:'smooth',block:'start'});});
if(CH===3){renderSeeds();playSeed(0,true);}
'''
i=s.rindex('</script>')
s=s[:i]+js3+s[i:]
open('preview.html','w').write(s)
print('v2 ok')

# ================= CH 3 v3: cut-outs, RST end card on ACRES videos, story continuity, pepper portrait, garden pack image =================
s=open('preview.html').read()
def rep4(a,b,c=1):
    global s
    assert s.count(a)==c,(a[:80],s.count(a)); s=s.replace(a,b)
rep4('src="media/case10.jpg"','src="media/case10.png"')
rep4("img:'media/case10.jpg'","img:'media/case10.png'")
rep4('<img src="media/nano-garden.png" alt="ACRES Nano Garden Pack">','<img src="media/garden-pack.png" alt="Heritage Garden Pack: two heritage seed packets with ACRES Nano">')
# farm folder item timings: [id,title,sub,src,start,end]
rep4('["8CkHXrmPg3A","Carrot Farmer Boosts Yield","David Ayaba, Ashanti Region, shares his ACRES Nano results.","ACRES"]','["8CkHXrmPg3A","Carrot Farmer Boosts Yield","David Ayaba, Ashanti Region, shares his ACRES Nano results.","ACRES",0,192]')
rep4('["awMkgdfLTYk","Field Demo in Lave, Volta Region","Farmers see ACRES Nano applied in the field.","ACRES"]','["awMkgdfLTYk","Field Demo in Lave, Volta Region","Farmers see ACRES Nano applied in the field.","ACRES",0,292]')
rep4('["vMOehJeWPVU","Maize Trial at Ashaiman","Throwback 2023: ACRES Nano on maize in Greater Accra.","ACRES"]','["vMOehJeWPVU","Maize Trial at Ashaiman","Throwback 2023: ACRES Nano on maize in Greater Accra.","ACRES",0,276]')
rep4('["media/nano-explainer.mp4","How to Use ACRES Nano","10 capsules per acre: activate, dilute, apply.","ACRES"]','["media/nano-explainer.mp4","How to Use ACRES Nano","10 capsules per acre: activate, dilute, apply.","ACRES-RST"]')
# story buttons: start/end + part labels
rep4('data-v="dy3wzy2EZ6k" data-t="ACRES Agriculture: The Problem"','data-v="dy3wzy2EZ6k" data-en="641" data-p="Part 1 · The Problem" data-t="ACRES Agriculture: The Problem"')
rep4('data-v="6bJUGN7mHaU" data-t="ACRES Agriculture: The Solution"','data-v="6bJUGN7mHaU" data-st="22" data-en="350" data-p="Part 2 · The Solution" data-t="ACRES Agriculture: The Solution"')
rep4('data-v="tngKiDJoXMc" data-t="ACRES Agriculture: The Science"','data-v="tngKiDJoXMc" data-st="24" data-en="693" data-p="Part 3 · The Science" data-t="ACRES Agriculture: The Science"')
rep4('data-v="media/nano-explainer.mp4" data-t="How to Use ACRES Nano"','data-v="media/nano-explainer.mp4" data-src="ACRES-RST" data-t="How to Use ACRES Nano"')
# overlays
rep4('<div class="yt-shield" id="ytShield"></div>','<div class="yt-shield" id="ytShield"></div><div class="part-card" id="partCard" hidden></div><div class="rst-card" id="rstCard" hidden><img src="media/rst-card.jpg" alt="Order ACRES Nano from RST Company Limited, 020 816 8917, 024 475 5947, 020 637 5069"><button type="button" id="rstSkip">Continue ›</button></div>')
css4='''
.part-card{position:absolute;inset:0;z-index:4;display:flex;align-items:center;justify-content:center;background:rgba(10,20,6,.82);color:#fff;font-family:var(--display);font-weight:800;font-size:clamp(22px,6vw,40px);pointer-events:none;animation:pcf 4s forwards}
@keyframes pcf{0%,75%{opacity:1}100%{opacity:0}}
.rst-card{position:absolute;inset:0;z-index:5;background:#fff;display:flex;align-items:center;justify-content:center}.rst-card img{width:100%;height:100%;object-fit:contain}
.rst-card button{position:absolute;right:8px;top:8px;border:0;border-radius:999px;background:rgba(0,150,58,.9);color:#fff;font-weight:800;font-size:12px;padding:5px 10px;cursor:pointer}
.ytbox.portrait #locV{object-fit:contain}
'''
rep4('</style>\n\n<div class="wrap">',css4+'</style>\n\n<div class="wrap">')
# player logic: start/end, part card, RST end card
rep4("function playItem(v,lab,q){sdClear();$s('sdEnd').hidden=true;EXTRA=q==null;if(q!=null)seedCur=q;",
"""let CUR=null,rstT=null;
function showPart(p){const c=$s('partCard');if(!p){c.hidden=true;return;}c.textContent=p;c.hidden=false;c.style.animation='none';void c.offsetWidth;c.style.animation='';setTimeout(()=>c.hidden=true,4000);}
function afterItem(){const v=CUR;if(!v)return;if(v[3]==='ACRES'){$s('rstCard').hidden=false;track('rst_card',{video:v[1]});clearTimeout(rstT);rstT=setTimeout(()=>finishItem(),9000);}else finishItem();}
function finishItem(){clearTimeout(rstT);$s('rstCard').hidden=true;if(!EXTRA)sdShowEnd();else{$s('ytPause').hidden=false;$s('ytPlay').textContent='▶';}}
function playItem(v,lab,q){sdClear();$s('sdEnd').hidden=true;$s('rstCard').hidden=true;clearTimeout(rstT);CUR=v;EXTRA=q==null;if(q!=null)seedCur=q;showPart(v[6]);""")
rep4("document.getElementById('nowSub').textContent=v[2]+' · Video: '+(v[3]||'Jibril Enterprise');","document.getElementById('nowSub').textContent=v[2]+' · Video: '+(v[3]?'ACRES':'Jibril Enterprise');")
rep4("locV.hidden=false;locV.src=v[0];locV.play().catch(()=>{});","locV.hidden=false;locV.src=v[0]+(v[4]?'#t='+v[4]:'');locV.play().catch(()=>{});")
rep4("ytPlayer=new YT.Player('ytP',{videoId:v[0],host:'https://www.youtube-nocookie.com',playerVars:{playsinline:1,rel:0,modestbranding:1,autoplay:1,controls:0,disablekb:1,fs:0,iv_load_policy:3,cc_load_policy:0},\n      events:{onReady:e=>{if(CH===3&&!LOCAL)e.target.playVideo();},onStateChange:e=>{if(LOCAL)return;ytPaint(e.data);if(e.data===0&&CH===3){track('seed_complete',{video:v[1]});if(!EXTRA)sdShowEnd();}}}});}\n    else ytPlayer.loadVideoById(v[0]);",
"ytPlayer=new YT.Player('ytP',{videoId:v[0],host:'https://www.youtube-nocookie.com',playerVars:{playsinline:1,rel:0,modestbranding:1,autoplay:1,controls:0,disablekb:1,fs:0,iv_load_policy:3,cc_load_policy:0,start:v[4]||0},\n      events:{onReady:e=>{if(CH===3&&!LOCAL)e.target.playVideo();},onStateChange:e=>{if(LOCAL)return;ytPaint(e.data);if(e.data===0&&CH===3){track('seed_complete',{video:CUR&&CUR[1]});afterItem();}}}});}\n    else ytPlayer.loadVideoById({videoId:v[0],startSeconds:v[4]||0});")
rep4("locV.addEventListener('ended',()=>{ytPaint(0);track('seed_complete',{video:$s('ypTitle').textContent});if(!EXTRA)sdShowEnd();});",
"""locV.addEventListener('ended',()=>{ytPaint(0);track('seed_complete',{video:$s('ypTitle').textContent});afterItem();});
locV.addEventListener('loadedmetadata',()=>{$s('ytBox').classList.toggle('portrait',locV.videoHeight>locV.videoWidth);});
// stop each ACRES video before its old contact details, then show the RST card
setInterval(()=>{if(CH!==3||!CUR||!CUR[5]||!$s('rstCard').hidden)return;let t=0;if(LOCAL)t=locV.currentTime;else if(ytPlayer&&ytPlayer.getCurrentTime)t=ytPlayer.getCurrentTime();
  if(t>=CUR[5]){try{LOCAL?locV.pause():ytPlayer.pauseVideo();}catch(_){}$s('ytPause').hidden=false;track('seed_complete',{video:CUR[1]});afterItem();}},400);
$s('rstSkip').onclick=()=>finishItem();""")
rep4("playItem([b.dataset.v,b.dataset.t,b.dataset.s,'ACRES'],'NOW SHOWING · LEARN ABOUT ACRES NANO',null);",
"playItem([b.dataset.v,b.dataset.t,b.dataset.s,b.dataset.src||'ACRES',+b.dataset.st||0,+b.dataset.en||0,b.dataset.p||''],b.dataset.p?'NOW SHOWING · THE ACRES STORY':'NOW SHOWING · LEARN ABOUT ACRES NANO',null);")
open('preview.html','w').write(s)
print('v3 ok')
