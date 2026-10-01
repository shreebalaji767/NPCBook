from pathlib import Path
import html
import json
import re

OUTPUT_DIR = Path("site")
SITE_URL = "https://npcbook.onrender.com"

SITE = {
    "name": "NPC OMNIVERSE",
    "short_name": "NPCBook",
    "tagline": "A living library of fictional characters, worlds and quests.",
    "description": "Explore fictional NPCs, worlds, quests, factions and lore in a fast, installable static web app.",
    "keywords": ["NPCBook","NPC Omniverse","NPCs","fictional characters","worldbuilding","quests","lore"],
}

NPCS = [
 {"id":"kael-veyron","name":"Kael Veyron","category":"Warriors","rarity":"Legendary","role":"Blade Commander","world":"Aetheris","description":"A legendary blade commander whose reputation was forged during the Crimson War.","tags":["warrior","commander","swordsman","legendary"]},
 {"id":"lyra-solenne","name":"Lyra Solenne","category":"Mages","rarity":"Epic","role":"Astral Mage","world":"Aetheris","description":"An astral mage who reads ancient constellations and manipulates celestial energy.","tags":["mage","astral","magic","celestial"]},
 {"id":"drax-ironfall","name":"Drax Ironfall","category":"Warlords","rarity":"Mythic","role":"Iron Warlord","world":"Ashen Dominion","description":"A feared warlord commanding the Iron Legion across a volcanic frontier.","tags":["warlord","iron legion","empire","battle"]},
 {"id":"mira-nightshade","name":"Mira Nightshade","category":"Assassins","rarity":"Rare","role":"Shadow Assassin","world":"Nocturne","description":"A silent assassin who travels between cities through the hidden roads of Nocturne.","tags":["assassin","shadow","stealth","nocturne"]},
 {"id":"oren-voss","name":"Oren Voss","category":"Adventurers","rarity":"Epic","role":"Rift Cartographer","world":"The Shattered Realms","description":"A mapmaker who records unstable portals before they disappear.","tags":["explorer","maps","portals","adventurer"]},
 {"id":"selene-vale","name":"Selene Vale","category":"Mystics","rarity":"Legendary","role":"Moon Seer","world":"Nocturne","description":"A quiet seer whose prophecies arrive as fragments of forgotten dreams.","tags":["mystic","seer","moon","prophecy"]}
]

WORLDS = [
 {"id":"aetheris","name":"Aetheris","type":"High Fantasy","status":"Active","description":"A vast realm of floating kingdoms, ancient magic and forgotten civilizations.","tags":["fantasy","magic","kingdoms","floating islands"]},
 {"id":"nocturne","name":"Nocturne","type":"Dark Fantasy","status":"Active","description":"A world where eternal twilight hides ancient creatures and secret societies.","tags":["dark fantasy","twilight","mystery","assassins"]},
 {"id":"ashen-dominion","name":"Ashen Dominion","type":"Dark Fantasy","status":"Active","description":"A volcanic empire ruled by powerful warlords and armies forged in fire.","tags":["volcano","empire","war","warlords"]},
 {"id":"shattered-realms","name":"The Shattered Realms","type":"Multiversal","status":"Expanding","description":"A fractured collection of worlds connected by unstable portals and dimensional gates.","tags":["multiverse","portals","dimensions","worlds"]}
]

QUESTS = [
 {"id":"lost-crown","name":"The Lost Crown","difficulty":"Hard","status":"Available","world":"Aetheris","description":"Recover the crown of the fallen king before it is claimed by the northern kingdoms.","tags":["crown","kingdom","treasure","war"]},
 {"id":"echoes-nocturne","name":"Echoes of Nocturne","difficulty":"Extreme","status":"Available","world":"Nocturne","description":"Investigate strange voices appearing every night beneath the abandoned city.","tags":["mystery","voices","city","nocturne"]},
 {"id":"iron-rebellion","name":"The Iron Rebellion","difficulty":"Legendary","status":"Active","world":"Ashen Dominion","description":"Stop the rebellion spreading through the Iron Legion before the empire collapses.","tags":["rebellion","iron legion","empire","war"]},
 {"id":"rift-at-dawn","name":"Rift at Dawn","difficulty":"Mythic","status":"New","world":"The Shattered Realms","description":"Reach a newly opened rift before two incompatible worlds collide.","tags":["rift","portal","multiverse","time"]}
]

POSTS = [
 {"id":"gate-report","name":"The Gate Report","type":"Lore","world":"Aetheris","description":"The eastern gate has been closed for three hundred years. Someone opened it last night.","tags":["lore","mystery","gate"]},
 {"id":"pigeon-council","name":"Pigeon Council","type":"Rumor","world":"Nocturne","description":"Three pigeons were seen meeting on the old bell tower. Nobody knows what they discussed.","tags":["rumor","pigeons","nocturne"]},
 {"id":"iron-legion","name":"Iron Legion Bulletin","type":"Faction","world":"Ashen Dominion","description":"The Iron Legion has doubled patrols along the northern lava road.","tags":["faction","war","legion"]}
]

COLLECTIONS = {
 "npcs":("NPCs","👤",NPCS),
 "worlds":("Worlds","🌍",WORLDS),
 "quests":("Quests","⚔️",QUESTS),
 "posts":("Lore","📜",POSTS)
}

def esc(value):
    return html.escape(str(value or ""), quote=True)

def slug(value):
    return re.sub(r"[^a-z0-9]+","-",str(value).lower()).strip("-") or "item"

def unique(records):
    out=[]; seen=set()
    for item in records:
        item=dict(item)
        key=item.get("id") or slug(item.get("name","item"))
        if key in seen: continue
        seen.add(key); item["id"]=key; out.append(item)
    return out

def card(item, collection):
    label,icon,_=COLLECTIONS[collection]
    meta=[]
    for key in ("category","rarity","role","type","difficulty","status","world"):
        if item.get(key): meta.append(item[key])
    tags="".join('<span class="tag">#'+esc(t)+'</span>' for t in item.get("tags",[])[:6])
    searchable=esc(" ".join(str(v) for v in item.values()))
    payload=esc(json.dumps(item,ensure_ascii=False))
    return f'''
<article class="card" id="card-{esc(item["id"])}" data-type="{esc(collection)}" data-search="{searchable}" data-item="{payload}">
 <div class="card-top"><span class="eyebrow">{icon} {esc(label[:-1] if label.endswith("s") else label)}</span><button class="icon-btn" type="button" aria-label="Share" onclick="shareItem(this.closest('.card'))">↗</button></div>
 <h3>{esc(item["name"])}</h3><p>{esc(item.get("description",""))}</p>
 <div class="meta">{"".join("<span>"+esc(x)+"</span>" for x in meta)}</div>
 <div class="tags">{tags}</div>
 <div class="card-actions"><button class="btn small" type="button" onclick="openItem(this.closest('.card'))">View</button><button class="btn small ghost" type="button" onclick="screenshotCard(this.closest('.card'))">Screenshot</button></div>
</article>'''

def build_html():
    all_cards=[]
    for collection,(_,_,records) in COLLECTIONS.items():
        for item in unique(records): all_cards.append(card(item,collection))
    categories="".join('<button class="filter" data-filter="'+k+'" onclick="setFilter(this.dataset.filter)">'+icon+" "+label+"</button>" for k,(label,icon,_) in COLLECTIONS.items())
    stats=[("NPCs",len(NPCS)+12840,"👤"),("Worlds",len(WORLDS)+426,"🌍"),("Quests",len(QUESTS)+1892,"⚔️"),("Lore",len(POSTS)+317,"📜")]
    stat_html="".join('<div class="stat"><b>'+icon+'</b><strong>'+f"{value:,}"+'</strong><span>'+name+"</span></div>" for name,value,icon in stats)
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#090d18"><meta name="description" content="{esc(SITE["description"])}"><meta name="keywords" content="{esc(", ".join(SITE["keywords"]))}">
<meta name="robots" content="index,follow"><meta property="og:type" content="website"><meta property="og:title" content="{esc(SITE["name"])}"><meta property="og:description" content="{esc(SITE["description"])}"><meta property="og:url" content="{SITE_URL}/">
<link rel="canonical" href="{SITE_URL}/"><link rel="manifest" href="/manifest.webmanifest"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/favicon.svg">
<title>{esc(SITE["name"])} — {esc(SITE["tagline"])}</title>
<style>
:root{{color-scheme:dark;--bg:#070a12;--text:#f5f7ff;--muted:#8e9ab1;--line:#202b40;--accent:#7c6cff;--accent2:#31d8ff;--panel:#0d1320}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:radial-gradient(circle at 20% -10%,#30277755,transparent 32rem),radial-gradient(circle at 90% 10%,#087a9850,transparent 28rem),var(--bg);font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif;color:var(--text)}}button,input{{font:inherit}}button{{cursor:pointer}}a{{color:inherit;text-decoration:none}}
.topbar{{position:sticky;top:0;z-index:50;background:#070a12dd;backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}}.nav{{max-width:1250px;margin:auto;padding:14px 20px;display:flex;align-items:center;gap:18px}}.brand{{display:flex;align-items:center;gap:11px;font-weight:900;white-space:nowrap}}.logo{{width:38px;height:38px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:grid;place-items:center;font-size:20px}}.search{{flex:1;max-width:620px;margin:auto;position:relative}}.search input{{width:100%;background:#101827;border:1px solid var(--line);color:var(--text);border-radius:14px;padding:12px 44px 12px 15px;outline:none}}.search input:focus{{border-color:#6f7cff;box-shadow:0 0 0 4px #6f7cff18}}.kbd{{position:absolute;right:10px;top:9px;color:#68748a;border:1px solid var(--line);border-radius:7px;padding:2px 7px;font-size:12px}}.actions{{display:flex;gap:8px}}
.btn,.icon-btn{{border:1px solid var(--line);background:#111827;color:var(--text);border-radius:11px;padding:9px 12px}}.icon-btn{{width:40px;height:40px;padding:0}}.btn:hover,.icon-btn:hover{{border-color:#5967a0;background:#172033}}.btn.primary{{border:0;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;font-weight:800}}.btn.small{{padding:8px 11px;font-size:13px}}.btn.ghost{{background:transparent}}.install{{display:none}}.install.show{{display:inline-flex}}
.hero{{max-width:1250px;margin:auto;padding:70px 20px 30px;display:grid;grid-template-columns:1.4fr .8fr;gap:30px;align-items:center}}.eyebrow{{color:#8e9bff;font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:1px}}.hero h1{{font-size:clamp(42px,7vw,78px);line-height:.95;margin:12px 0 20px;letter-spacing:-4px}}.gradient{{background:linear-gradient(90deg,#fff,var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}}.hero p{{max-width:700px;color:var(--muted);font-size:18px;line-height:1.7;margin:0 0 24px}}.hero-buttons{{display:flex;gap:10px;flex-wrap:wrap}}.orb{{min-height:290px;border:1px solid var(--line);border-radius:28px;background:#0b101bcc;display:grid;place-items:center;overflow:hidden}}.orb-core{{font-size:90px;animation:float 4s ease-in-out infinite}}@keyframes float{{50%{{transform:translateY(-12px) rotate(4deg)}}}}
.stats{{max-width:1250px;margin:auto;padding:10px 20px 30px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}.stat{{background:#0c121fbb;border:1px solid var(--line);border-radius:18px;padding:17px;display:grid;grid-template-columns:auto 1fr;column-gap:10px}}.stat b{{grid-row:span 2;font-size:25px}}.stat strong{{font-size:21px}}.stat span{{color:var(--muted);font-size:13px}}
.main{{max-width:1250px;margin:auto;padding:0 20px 100px}}.toolbar{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:15px 0 22px}}.filters{{display:flex;gap:8px;overflow:auto;padding-bottom:4px;flex:1}}.filter{{white-space:nowrap;border:1px solid var(--line);background:#0d1320;color:#aeb8cb;border-radius:999px;padding:8px 12px}}.filter.active,.filter:hover{{color:#fff;border-color:#6875b5;background:#171d31}}.result-count{{color:var(--muted);font-size:13px;white-space:nowrap}}.grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}}.card{{background:linear-gradient(160deg,#0f1624,#0b101a);border:1px solid var(--line);border-radius:20px;padding:18px;min-height:280px;display:flex;flex-direction:column;transition:transform .18s,border-color .18s,box-shadow .18s}}.card:hover{{transform:translateY(-3px);border-color:#43517a;box-shadow:0 16px 45px #0004}}.card.hidden{{display:none}}.card-top{{display:flex;justify-content:space-between;align-items:center}}.card h3{{font-size:22px;margin:16px 0 8px}}.card p{{color:var(--muted);line-height:1.6;margin:0 0 15px}}.meta{{display:flex;gap:7px;flex-wrap:wrap;color:#c4ccda;font-size:12px}}.meta span{{padding:5px 8px;border-radius:8px;background:#151d2c;border:1px solid #202b40}}.tags{{display:flex;gap:6px;flex-wrap:wrap;margin-top:auto;padding-top:16px}}.tag{{font-size:11px;color:#8995ff}}.card-actions{{display:flex;gap:7px;margin-top:15px}}.empty{{display:none;text-align:center;padding:70px 20px;color:var(--muted);border:1px dashed var(--line);border-radius:20px}}.empty.show{{display:block}}footer{{border-top:1px solid var(--line);padding:30px 20px;color:#6f7b91;text-align:center;font-size:13px}}
.modal{{position:fixed;inset:0;background:#000b;backdrop-filter:blur(10px);z-index:100;display:none;place-items:center;padding:20px}}.modal.open{{display:grid}}.dialog{{width:min(680px,100%);max-height:85vh;overflow:auto;background:#0c121e;border:1px solid #2a3650;border-radius:24px;padding:24px;box-shadow:0 18px 60px #0007}}.dialog-head{{display:flex;justify-content:space-between;gap:15px}}.dialog h2{{font-size:30px;margin:8px 0}}.dialog p{{color:var(--muted);line-height:1.75}}.detail-row{{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:20px 0}}.detail{{background:#111827;border:1px solid var(--line);border-radius:13px;padding:12px}}.detail small{{display:block;color:#6f7b91;margin-bottom:4px}}.toast{{position:fixed;left:50%;bottom:25px;transform:translate(-50%,20px);opacity:0;pointer-events:none;background:#f5f7ff;color:#0b101a;padding:11px 16px;border-radius:12px;font-weight:700;z-index:200;transition:.2s}}.toast.show{{opacity:1;transform:translate(-50%,0)}}
@media(max-width:900px){{.hero{{grid-template-columns:1fr}}.orb{{min-height:220px}}.grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}.stats{{grid-template-columns:repeat(2,1fr)}}}}@media(max-width:620px){{.nav{{padding:10px 13px;gap:8px}}.brand span:last-child{{display:none}}.search{{order:3;flex-basis:100%;max-width:none}}.topbar{{padding-bottom:10px}}.hero{{padding:48px 16px 25px}}.hero h1{{font-size:47px;letter-spacing:-2.5px}}.main,.stats{{padding-left:16px;padding-right:16px}}.grid{{grid-template-columns:1fr}}.stats{{gap:8px}}.stat{{padding:13px}}.detail-row{{grid-template-columns:1fr}}}}@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important;animation:none!important;transition:none!important}}}}
</style></head><body>
<header class="topbar"><nav class="nav"><a class="brand" href="/"><span class="logo">🤖</span><span>NPC OMNIVERSE</span></a><div class="search"><input id="search" type="search" placeholder="Search NPCs, worlds, quests, lore…" autocomplete="off" aria-label="Search"><span class="kbd">/</span></div><div class="actions"><button class="btn primary install" id="installBtn" type="button">Install</button><button class="icon-btn" type="button" onclick="toggleTheme()" aria-label="Toggle theme">☼</button></div></nav></header>
<section class="hero"><div><div class="eyebrow">THE FICTIONAL OMNIVERSE</div><h1>Everyone has a profile.<br><span class="gradient">Nobody has a purpose.</span></h1><p>{esc(SITE["tagline"])} Browse characters, discover worlds, inspect quests and fall into lore rabbit holes — all in a fast static app with no account and no database.</p><div class="hero-buttons"><a class="btn primary" href="#explore">Explore the Omniverse</a><button class="btn" onclick="randomDiscovery()">🎲 Random discovery</button></div></div><div class="orb"><div class="orb-core">🤖</div></div></section>
<section class="stats">{stat_html}</section>
<main class="main" id="explore"><div class="toolbar"><div class="filters"><button class="filter active" data-filter="all" onclick="setFilter('all')">✨ All</button>{categories}</div><span class="result-count" id="resultCount"></span></div><section class="grid" id="grid">{"".join(all_cards)}</section><div class="empty" id="empty"><h2>NPC not found.</h2><p>Even the mysterious pigeon council has no record of that search.</p><button class="btn" onclick="clearSearch()">Clear search</button></div></main>
<footer>NPC OMNIVERSE · Static, fast, installable and intentionally unnecessary.<br>Refresh the page. Discover a different rabbit hole.</footer>
<div class="modal" id="modal" role="dialog" aria-modal="true" onclick="if(event.target===this)closeModal()"><div class="dialog"><div class="dialog-head"><div><div class="eyebrow" id="modalType"></div><h2 id="modalTitle"></h2></div><button class="icon-btn" onclick="closeModal()" aria-label="Close">×</button></div><p id="modalDescription"></p><div class="detail-row" id="modalDetails"></div><div class="tags" id="modalTags"></div><br><button class="btn primary" onclick="shareModal()">↗ Share</button></div></div><div class="toast" id="toast"></div>
<script>
const state={filter:'all',query:'',selected:null}, search=document.getElementById('search'), cards=[...document.querySelectorAll('.card')];
function apply(){let visible=0;for(const c of cards){const mf=state.filter==='all'||c.dataset.type===state.filter,ms=!state.query||c.dataset.search.toLowerCase().includes(state.query),show=mf&&ms;c.classList.toggle('hidden',!show);if(show)visible++;}document.getElementById('resultCount').textContent=visible+' result'+(visible===1?'':'s');document.getElementById('empty').classList.toggle('show',visible===0);}
function setFilter(filter){state.filter=filter;document.querySelectorAll('.filter').forEach(b=>b.classList.toggle('active',b.dataset.filter===filter));apply();}
search.addEventListener('input',e=>{state.query=e.target.value.trim().toLowerCase();apply()});
document.addEventListener('keydown',e=>{if(e.key==='/'&&document.activeElement!==search){e.preventDefault();search.focus()}if(e.key==='Escape')closeModal()});
function clearSearch(){search.value='';state.query='';setFilter('all')}
function openItem(card){const item=JSON.parse(card.dataset.item);state.selected=item;document.getElementById('modalType').textContent=card.dataset.type.toUpperCase();document.getElementById('modalTitle').textContent=item.name;document.getElementById('modalDescription').textContent=item.description||'';document.getElementById('modalDetails').innerHTML=Object.entries(item).filter(([k,v])=>!['id','name','description','tags'].includes(k)&&v).map(([k,v])=>'<div class="detail"><small>'+k+'</small><strong>'+String(Array.isArray(v)?v.join(', '):v)+'</strong></div>').join('');document.getElementById('modalTags').innerHTML=(item.tags||[]).map(t=>'<span class="tag">#'+t+'</span>').join('');document.getElementById('modal').classList.add('open');document.body.style.overflow='hidden'}
function closeModal(){document.getElementById('modal').classList.remove('open');document.body.style.overflow=''}
async function shareModal(){if(state.selected)shareData(state.selected.name,state.selected.description||location.href)}
async function shareItem(card){const item=JSON.parse(card.dataset.item);shareData(item.name,item.description||location.href)}
async function shareData(title,text){try{if(navigator.share)await navigator.share({title:title,text:text,url:location.href});else{await navigator.clipboard.writeText(location.href);toast('Link copied')}}catch(_){}}
function randomDiscovery(){const pool=cards.filter(c=>!c.classList.contains('hidden'));const target=(pool.length?pool:cards)[Math.floor(Math.random()*(pool.length?pool.length:cards.length))];target.scrollIntoView({behavior:'smooth',block:'center'});openItem(target)}
function screenshotCard(card){const item=JSON.parse(card.dataset.item),canvas=document.createElement('canvas'),w=1200,h=700,d=2;canvas.width=w*d;canvas.height=h*d;const ctx=canvas.getContext('2d');ctx.scale(d,d);const g=ctx.createLinearGradient(0,0,w,h);g.addColorStop(0,'#080b14');g.addColorStop(1,'#10182a');ctx.fillStyle=g;ctx.fillRect(0,0,w,h);ctx.fillStyle='#8d88ff';ctx.font='800 18px Arial';ctx.fillText('NPC OMNIVERSE · '+card.dataset.type.toUpperCase(),70,75);ctx.fillStyle='#fff';ctx.font='800 48px Arial';ctx.fillText(item.name,70,145);ctx.fillStyle='#aeb7ca';ctx.font='24px Arial';wrapCanvas(ctx,item.description||'',70,205,1060,34);ctx.fillStyle='#69758c';ctx.font='16px Arial';ctx.fillText((item.tags||[]).map(x=>'#'+x).join('   '),70,610);ctx.fillText('npcbook.onrender.com',70,650);canvas.toBlob(blob=>{const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='npcbook-'+slugify(item.name)+'.png';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)},'image/png')}
function wrapCanvas(ctx,text,x,y,maxWidth,lineHeight){let line='';for(const word of text.split(/\\s+/)){const test=line?line+' '+word:word;if(ctx.measureText(test).width>maxWidth&&line){ctx.fillText(line,x,y);y+=lineHeight;line=word}else line=test}if(line)ctx.fillText(line,x,y)}
function slugify(x){return String(x).toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')||'item'}
function toast(message){const t=document.getElementById('toast');t.textContent=message;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1800)}
function toggleTheme(){const light=document.body.dataset.theme==='light';document.body.dataset.theme=light?'dark':'light';if(!light){document.documentElement.style.setProperty('--bg','#f5f7fb');document.documentElement.style.setProperty('--text','#111827');document.documentElement.style.setProperty('--muted','#5f6b80');document.documentElement.style.setProperty('--line','#dbe1ec')}else location.reload()}
let deferredInstall=null;window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();deferredInstall=e;document.getElementById('installBtn').classList.add('show')});document.getElementById('installBtn').addEventListener('click',async()=>{if(!deferredInstall)return;deferredInstall.prompt();await deferredInstall.userChoice;deferredInstall=null;document.getElementById('installBtn').classList.remove('show')});
if('serviceWorker' in navigator)window.addEventListener('load',()=>navigator.serviceWorker.register('/sw.js').catch(()=>{}));apply();
</script></body></html>'''

def build_manifest():
    return json.dumps({"name":SITE["name"],"short_name":SITE["short_name"],"description":SITE["description"],"start_url":"/","scope":"/","display":"standalone","orientation":"portrait-primary","background_color":"#070a12","theme_color":"#090d18","icons":[{"src":"/favicon.svg","sizes":"any","type":"image/svg+xml","purpose":"any maskable"}]},indent=2)

def build_sw():
    return """const CACHE='npcbook-v3';
const CORE=['/','/index.html','/manifest.webmanifest','/favicon.svg','/404.html'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;e.respondWith(fetch(e.request).then(r=>{const copy=r.clone();caches.open(CACHE).then(c=>c.put(e.request,copy));return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('/404.html'))) )});
"""

def build_favicon():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128"><defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="#7c6cff"/><stop offset="1" stop-color="#31d8ff"/></linearGradient></defs><rect width="128" height="128" rx="30" fill="#090d18"/><rect x="12" y="12" width="104" height="104" rx="26" fill="url(#g)"/><path d="M34 48c0-10 8-18 18-18h24c10 0 18 8 18 18v20c0 10-8 18-18 18H58l-14 12V86c-6-3-10-9-10-18V48Z" fill="#fff"/><circle cx="58" cy="58" r="6" fill="#111827"/><circle cx="78" cy="58" r="6" fill="#111827"/><path d="M55 73c7 5 15 5 22 0" fill="none" stroke="#111827" stroke-width="5" stroke-linecap="round"/></svg>'''

def build_404():
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#090d18"><title>NPC not found</title><style>body{margin:0;background:#070a12;color:#fff;font-family:system-ui;display:grid;place-items:center;min-height:100vh;text-align:center}main{max-width:520px;padding:30px}a{display:inline-block;padding:11px 16px;border-radius:12px;background:#7c6cff;color:#fff;text-decoration:none;font-weight:800}</style><main><div style="font-size:80px">🤖</div><h1>This NPC does not exist.</h1><p>It probably walked into a different dimension.</p><a href="/">Return to NPC OMNIVERSE</a></main>'''

def build_robots():
    return f"User-agent: *\\nAllow: /\\nSitemap: {SITE_URL}/sitemap.xml\\n"

def build_sitemap():
    return f'''<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE_URL}/</loc></url></urlset>'''

def build():
    OUTPUT_DIR.mkdir(parents=True,exist_ok=True)
    files={"index.html":build_html(),"404.html":build_404(),"favicon.svg":build_favicon(),"manifest.webmanifest":build_manifest(),"sw.js":build_sw(),"robots.txt":build_robots(),"sitemap.xml":build_sitemap()}
    for name,content in files.items():(OUTPUT_DIR/name).write_text(content,encoding="utf-8")
    print("NPC OMNIVERSE build complete")
    print("Output:",OUTPUT_DIR.resolve())
    print("NPCs:",len(NPCS),"| Worlds:",len(WORLDS),"| Quests:",len(QUESTS),"| Lore:",len(POSTS))

if __name__=="__main__":
    build()
