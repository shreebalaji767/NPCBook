from pathlib import Path
import html, json, re

OUTPUT_DIR = Path(".")
SITE_URL = "https://npcbook.onrender.com"
BRAND = "BLSSNVJ21"
LOGO_URL = f"{SITE_URL}/logo.svg"
FAVICON_URL = f"{SITE_URL}/favicon.svg?v=10"
FAVICON_ICO_BASE64 = "AAABAAEAICAAAAEAIABoAAAAFgAAAIlQTkcNChoKAAAADUlIRFIAAAAgAAAAIAgGAAAAc3p69AAAAC9JREFUeNrtzqEBAAAIAyCrwe7/j+oZKwQ61bOXVAICAgICAgICAgICAgICAunAA66ptD3mbRNKAAAAAElFTkSuQmCC"

SITE = {
    "name": "NPCBook — NPC OMNIVERSE",
    "short_name": "NPCBook",
    "tagline": "Explore NPCs, fictional worlds, quests and lore.",
    "description": "NPCBook is a fast fictional NPC encyclopedia and worldbuilding explorer featuring characters, worlds, quests, factions and lore.",
    "keywords": ["NPCBook","NPC Omniverse","BLSSNVJ21","NPC encyclopedia","fictional NPCs","fictional characters","worldbuilding","quests","lore","fantasy characters"],
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
COLLECTIONS={"npcs":("NPCs","👤",NPCS),"worlds":("Worlds","🌍",WORLDS),"quests":("Quests","⚔️",QUESTS),"posts":("Lore","📜",POSTS)}

def esc(v): return html.escape(str(v or ""),quote=True)
def slug(v): return re.sub(r"[^a-z0-9]+","-",str(v).lower()).strip("-") or "item"
def unique(records):
    out=[]; seen=set()
    for item in records:
        item=dict(item); key=item.get("id") or slug(item.get("name","item"))
        if key not in seen: seen.add(key); item["id"]=key; out.append(item)
    return out

def card(item,collection):
    label,icon,_=COLLECTIONS[collection]
    meta=[item[k] for k in ("category","rarity","role","type","difficulty","status","world") if item.get(k)]
    tags="".join('<span class="tag">#'+esc(t)+'</span>' for t in item.get("tags",[])[:6])
    return f'''<article class="card" data-type="{esc(collection)}" data-search="{esc(" ".join(str(v) for v in item.values()))}" data-item="{esc(json.dumps(item,ensure_ascii=False))}">
<div class="card-top"><span class="eyebrow">{icon} {esc(label)}</span><button class="icon-btn" aria-label="Share" onclick="shareItem(this.closest('.card'))">↗</button></div>
<h3>{esc(item["name"])}</h3><p>{esc(item.get("description",""))}</p><div class="meta">{"".join("<span>"+esc(x)+"</span>" for x in meta)}</div><div class="tags">{tags}</div>
<div class="card-actions"><button class="btn small x-view" onclick="openItem(this.closest('.card'))">View</button><button class="btn small ghost x-screenshot" onclick="screenshotCard(this.closest('.card'))">Screenshot</button></div></article>'''

def build_html():
    cards=[]
    for collection,(_,_,records) in COLLECTIONS.items():
        cards += [card(i,collection) for i in unique(records)]
    categories="".join(f'<button class="filter" data-filter="{k}" onclick="setFilter(this.dataset.filter)">{icon} {label}</button>' for k,(label,icon,_) in COLLECTIONS.items())
    stats=[("NPCs",12846,"👤"),("Worlds",430,"🌍"),("Quests",1896,"⚔️"),("Lore",320,"📜")]
    stat_html="".join(f'<div class="stat"><b>{icon}</b><strong>{v:,}</strong><span>{n}</span></div>' for n,v,icon in stats)
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#090d18"><meta name="color-scheme" content="dark">
<meta name="description" content="{esc(SITE["description"])}"><meta name="keywords" content="{esc(", ".join(SITE["keywords"]))}">
<meta name="author" content="{BRAND}"><meta name="publisher" content="{BRAND}"><meta name="application-name" content="NPCBook">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="{SITE_URL}/"><link rel="alternate" hreflang="en" href="{SITE_URL}/">
<meta property="og:locale" content="en_US"><meta property="og:type" content="website"><meta property="og:site_name" content="NPCBook">
<meta property="og:title" content="{esc(SITE["name"])}"><meta property="og:description" content="{esc(SITE["description"])}"><meta property="og:url" content="{SITE_URL}/"><meta property="og:image" content="{LOGO_URL}"><meta property="og:image:alt" content="NPCBook — BLSSNVJ21 logo"><meta property="og:image:type" content="image/svg+xml">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(SITE["name"])}"><meta name="twitter:description" content="{esc(SITE["description"])}"><meta name="twitter:image" content="{LOGO_URL}"><meta name="twitter:image:alt" content="NPCBook — BLSSNVJ21 logo">
<meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="NPCBook"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="format-detection" content="telephone=no"><meta name="mobile-web-app-title" content="NPCBook"><meta name="referrer" content="strict-origin-when-cross-origin"><meta name="color-scheme" content="dark light"><meta name="generator" content="NPCBook / BLSSNVJ21">\n<link rel="manifest" href="/manifest.webmanifest"><link rel="icon" href="/favicon.ico?v=10" sizes="32x32" type="image/x-icon"><link rel="icon" href="{FAVICON_URL}" type="image/svg+xml" sizes="any"><link rel="shortcut icon" href="/favicon.ico?v=10" type="image/x-icon"><link rel="apple-touch-icon" href="{LOGO_URL}?v=6"><meta name="msapplication-TileColor" content="#090d18">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":[{"@type":"WebSite","name":SITE["name"],"alternateName":["NPCBook","NPC OMNIVERSE",BRAND],"url":SITE_URL+"/","description":SITE["description"],"keywords":SITE["keywords"],"inLanguage":"en"},{"@type":"Organization","name":"BLSSNVJ21","url":SITE_URL+"/","logo":LOGO_URL},{"@type":"WebApplication","name":"NPCBook","applicationCategory":"EntertainmentApplication","operatingSystem":"Web","url":SITE_URL+"/","description":SITE["description"],"browserRequirements":"Requires JavaScript","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}},{"@type":"ItemList","name":"NPCBook collections","numberOfItems":4,"itemListElement":[{"@type":"ListItem","position":1,"name":"NPCs"},{"@type":"ListItem","position":2,"name":"Worlds"},{"@type":"ListItem","position":3,"name":"Quests"},{"@type":"ListItem","position":4,"name":"Lore"}]}]},ensure_ascii=False)}</script>
<title>{esc(SITE["name"])} | Fictional NPCs, Worlds, Quests & Lore</title>
<style>
:root{{--bg:#070a12;--text:#f5f7ff;--muted:#8e9ab1;--line:#202b40;--accent:#7c6cff;--accent2:#31d8ff}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:radial-gradient(circle at 15% -10%,#30277755,transparent 32rem),radial-gradient(circle at 90% 5%,#087a9850,transparent 28rem),var(--bg);font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif;color:var(--text)}}button,input{{font:inherit}}button{{cursor:pointer}}a{{color:inherit;text-decoration:none}}
.skip-link{{position:fixed;left:12px;top:12px;z-index:300;background:#fff;color:#111827;padding:10px 14px;border-radius:10px;transform:translateY(-160%);font-weight:800}}.skip-link:focus{{transform:translateY(0)}}.topbar{{position:sticky;top:0;z-index:50;background:#070a12dd;backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}}.nav{{max-width:1250px;margin:auto;padding:12px 20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}}.brand{{display:flex;align-items:center;gap:10px;font-weight:900;white-space:nowrap}}.logo{{width:40px;height:40px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:grid;place-items:center;font-size:21px;box-shadow:0 8px 30px #5550ff55}}.search{{flex:1;min-width:220px;max-width:650px;margin:auto;position:relative}}.search input{{width:100%;background:#101827;border:1px solid var(--line);color:var(--text);border-radius:14px;padding:12px 44px 12px 15px;outline:0}}.kbd{{position:absolute;right:10px;top:9px;color:#68748a;border:1px solid var(--line);border-radius:7px;padding:2px 7px;font-size:12px}}.actions{{display:flex;gap:8px}}.btn,.icon-btn{{border:1px solid var(--line);background:#111827;color:var(--text);border-radius:11px;padding:9px 12px}}.icon-btn{{width:40px;height:40px;padding:0}}.btn.primary{{border:0;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;font-weight:800}}.btn.small{{padding:8px 11px;font-size:13px}}.btn.ghost{{background:transparent}}.install{{display:inline-flex}}.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}}
.hero{{max-width:1250px;margin:auto;padding:70px 20px 30px;display:grid;grid-template-columns:1.35fr .65fr;gap:30px;align-items:center}}.eyebrow{{color:#8e9bff;font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:1px}}.hero h1{{font-size:clamp(42px,7vw,78px);line-height:.95;margin:12px 0 20px;letter-spacing:-4px}}.gradient{{background:linear-gradient(90deg,#fff,var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent}}.hero p{{max-width:720px;color:var(--muted);font-size:18px;line-height:1.7;margin:0 0 24px}}.hero-buttons{{display:flex;gap:10px;flex-wrap:wrap}}.orb{{min-height:290px;border:1px solid var(--line);border-radius:28px;background:#0b101bcc;display:grid;place-items:center;overflow:hidden}}.orb-core{{font-size:92px;animation:float 4s ease-in-out infinite}}@keyframes float{{50%{{transform:translateY(-12px) rotate(4deg)}}}}
.stats{{max-width:1250px;margin:auto;padding:10px 20px 30px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}.stat{{background:#0c121fbb;border:1px solid var(--line);border-radius:18px;padding:17px;display:grid;grid-template-columns:auto 1fr;column-gap:10px}}.stat b{{grid-row:span 2;font-size:25px}}.stat strong{{font-size:21px}}.stat span{{color:var(--muted);font-size:13px}}
.main{{max-width:1250px;margin:auto;padding:0 20px 100px}}.toolbar{{display:flex;gap:10px;flex-wrap:wrap;margin:15px 0 22px}}.filters{{display:flex;gap:8px;overflow:auto;padding-bottom:4px;flex:1}}.filter{{white-space:nowrap;border:1px solid var(--line);background:#0d1320;color:#aeb8cb;border-radius:999px;padding:8px 12px}}.filter.active,.filter:hover{{color:#fff;border-color:#6875b5;background:#171d31}}.result-count{{color:var(--muted);font-size:13px;white-space:nowrap;padding-top:9px}}.grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}}.card{{background:linear-gradient(160deg,#0f1624,#0b101a);border:1px solid var(--line);border-radius:20px;padding:18px;min-height:280px;display:flex;flex-direction:column;transition:.18s}}.card:hover{{transform:translateY(-3px);border-color:#43517a;box-shadow:0 16px 45px #0004}}.card.hidden{{display:none}}.card-top{{display:flex;justify-content:space-between;align-items:center}}.card h3{{font-size:22px;margin:16px 0 8px}}.card p{{color:var(--muted);line-height:1.6;margin:0 0 15px}}.meta{{display:flex;gap:7px;flex-wrap:wrap;color:#c4ccda;font-size:12px}}.meta span{{padding:5px 8px;border-radius:8px;background:#151d2c;border:1px solid #202b40}}.tags{{display:flex;gap:6px;flex-wrap:wrap;margin-top:auto;padding-top:16px}}.tag{{font-size:11px;color:#8995ff}}.card-actions{{display:flex;gap:7px;margin-top:15px}}.empty{{display:none;text-align:center;padding:70px 20px;color:var(--muted);border:1px dashed var(--line);border-radius:20px}}.empty.show{{display:block}}footer{{border-top:1px solid var(--line);padding:30px 20px;color:#6f7b91;text-align:center;font-size:13px}}
.modal{{position:fixed;inset:0;background:#000b;backdrop-filter:blur(10px);z-index:100;display:none;place-items:center;padding:20px}}.modal.open{{display:grid}}.dialog{{width:min(680px,100%);max-height:85vh;overflow:auto;background:#0c121e;border:1px solid #2a3650;border-radius:24px;padding:24px;box-shadow:0 18px 60px #0007}}.dialog-head{{display:flex;justify-content:space-between;gap:15px}}.dialog h2{{font-size:30px;margin:8px 0}}.dialog p{{color:var(--muted);line-height:1.75}}.detail-row{{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:20px 0}}.detail{{background:#111827;border:1px solid var(--line);border-radius:13px;padding:12px}}.detail small{{display:block;color:#6f7b91;margin-bottom:4px}}.toast{{position:fixed;left:50%;bottom:25px;transform:translate(-50%,20px);opacity:0;pointer-events:none;background:#f5f7ff;color:#0b101a;padding:11px 16px;border-radius:12px;font-weight:700;z-index:200;transition:.2s}}.toast.show{{opacity:1;transform:translate(-50%,0)}}
@media(max-width:900px){{.hero{{grid-template-columns:1fr}}.orb{{min-height:220px}}.grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}.stats{{grid-template-columns:repeat(2,1fr)}}}}@media(max-width:620px){{.nav{{padding:10px 13px;gap:8px}}.brand span:last-child{{display:none}}.actions .btn{{min-height:40px}}.search{{order:3;flex-basis:100%;max-width:none}}.hero{{padding:48px 16px 25px}}.hero h1{{font-size:47px;letter-spacing:-2.5px}}.main,.stats{{padding-left:16px;padding-right:16px}}.grid{{grid-template-columns:1fr}}.stats{{gap:8px}}.stat{{padding:13px}}.detail-row{{grid-template-columns:1fr}}}}@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important;animation:none!important;transition:none!important}}}}
</style></head><body>
<a class="sr-only skip-link" href="#explore">Skip to content</a><header class="topbar"><nav class="nav"><a class="brand" href="/" aria-label="NPCBook home"><span class="logo">🤖</span><span>NPC OMNIVERSE · {BRAND}</span></a><div class="search"><label class="sr-only" for="search">Search NPCBook</label><input id="search" type="search" placeholder="Search NPCs, worlds, quests, lore…" autocomplete="off" enterkeyhint="search" spellcheck="false" aria-controls="resultsGrid" aria-describedby="resultCount"><span class="kbd">/</span></div><div class="actions"><button class="btn" type="button" onclick="openHistory()">🗃️ Library</button><button class="btn primary install show" id="installBtn" type="button">📲 Install App</button><button class="icon-btn" id="themeBtn" type="button" onclick="toggleTheme()" aria-label="Switch to light theme" title="Switch theme">☼</button></div></nav></header>
<section class="hero"><div><div class="eyebrow">NPCBOOK · {BRAND}</div><h1>The fictional<br><span class="gradient">NPC universe.</span></h1><p>{esc(SITE["tagline"])} Discover characters, worlds, quests and lore in a fast, mobile-first encyclopedia that works across phones, tablets and desktops.</p><div class="hero-buttons"><a class="btn primary" href="#explore">Explore NPCBook</a><button class="btn" onclick="randomDiscovery()">🎲 Random discovery</button><button class="btn" onclick="newUniverse()">🌌 New Universe</button><button class="btn ghost" onclick="exportUniverse()">⬇ Export Universe</button><label class="btn ghost" for="importUniverse" style="display:inline-flex;align-items:center">⬆ Import Universe</label><input class="sr-only" id="importUniverse" type="file" accept="application/json"></div></div><div class="orb"><div class="orb-core">🤖</div></div></section>
<section class="stats" aria-label="NPCBook collection statistics">{stat_html}</section>
<noscript><div style="max-width:1250px;margin:20px auto;padding:16px;border:1px solid #202b40;border-radius:14px">JavaScript is required for interactive NPCBook search, filters, sharing and PWA installation.</div></noscript><main class="main" id="explore"><div class="toolbar"><div class="filters"><button class="filter active" data-filter="all" onclick="setFilter('all')">✨ All</button>{categories}</div><span class="result-count" id="resultCount"></span></div><section class="grid" id="resultsGrid" aria-live="polite">{"".join(cards)}</section><div class="empty" role="status" id="empty"><h2>Nothing found.</h2><p>Even the mysterious pigeon council has no record of that search.</p><button class="btn" onclick="clearSearch()">Clear search</button></div></main>
<footer><strong>NPCBook</strong> · NPC OMNIVERSE · {BRAND}<br>Fictional characters, worlds, quests and lore.<br><span>Fast • Responsive • Installable • Offline-ready</span></footer>
<div class="modal" id="modal" role="dialog" aria-modal="true" onclick="if(event.target===this)closeModal()"><div class="dialog"><div class="dialog-head"><div><div class="eyebrow" id="modalType"></div><h2 id="modalTitle"></h2></div><button class="icon-btn" onclick="closeModal()" aria-label="Close">×</button></div><p id="modalDescription"></p><div class="detail-row" id="modalDetails"></div><div class="tags" id="modalTags"></div><br><button class="btn primary" onclick="shareModal()">↗ Share</button><button class="btn" onclick="saveSelected()">☆ Save</button></div></div><div class="toast" id="toast"></div>
<script>
const state={{filter:'all',query:'',selected:null}},search=document.getElementById('search'),cards=[...document.querySelectorAll('.card')];
function apply(){{let n=0;for(const c of cards){{const ok=(state.filter==='all'||(state.filter==='saved'&&isSaved(JSON.parse(c.dataset.item)))||c.dataset.type===state.filter)&&(!state.query||c.dataset.search.toLowerCase().includes(state.query));c.classList.toggle('hidden',!ok);if(ok)n++}}document.getElementById('resultCount').textContent=n+' result'+(n===1?'':'s');document.getElementById('empty').classList.toggle('show',n===0)}}
function setFilter(f){{state.filter=f;document.querySelectorAll('.filter').forEach(b=>b.classList.toggle('active',b.dataset.filter===f));apply()}}
const WORLD_HISTORY_KEY='npcbook-universe-history-v1';
const THEME_KEY='npcbook-theme-v1';
const WORDS={{
  prefixes:['Astra','Eldra','Nyx','Veyra','Sol','Kael','Orin','Zeph','Luma','Thorne','Aether','Riven','Mora','Cinder','Vel','Arca','Nexa','Oryn','Vanta','Eira'],
  middles:['veil','fall','reach','mere','dawn','forge','hollow','spire','rift','vale','drift','crown','wilds','harbor','gate','bloom','frontier','echo','realm','sanctum'],
  suffixes:['Prime','Ascendant','Eternal','Beyond','Unbound','Zero','IX','Omega','Horizon','Unknown','Awakening','Afterlight']
}};
const NPC_NAMES=['Kael','Lyra','Drax','Mira','Oren','Selene','Veyra','Ronan','Nyra','Talon','Iris','Zarek','Elara','Voss','Kira','Orin','Sable','Juno','Ari','Nox','Maren','Cyra','Vale','Riven'];
const NPC_SURNAMES=['Veyron','Solenne','Ironfall','Nightshade','Voss','Vale','Starborn','Ashcroft','Moonmere','Rook','Everis','Thorne','Dusk','Storme','Quill','Draven','Frost','Ember','Raine','Hollow'];
const ROLES=['Rift Cartographer','Void Mechanist','Star Seer','Memory Hunter','Storm Warden','Clockwork Diplomat','Dream Forger','Gatekeeper','Moon Archivist','Probability Knight','Echo Ranger','Grave Alchemist','Sky Corsair','Reality Broker','Runic Detective','Solar Monk'];
const BIOMES=['floating citadels','glass deserts','singing forests','gravity oceans','crystal tundra','endless twilight','living mountains','clockwork valleys','neon ruins','mirror archipelagos','storm plains','underground suns'];
const QUEST_GOALS=['recover a vanished crown','find the city that moves every dawn','seal a hungry dimensional rift','escort a memory that can walk','solve the bell that rings in empty space','steal a map from tomorrow','protect the last blue star','wake the sleeping machine beneath the sea','locate the missing hour','return a forbidden name'];
const LORE_HOOKS=['A door appeared where no wall exists.','Every shadow in the capital is facing the wrong direction.','A forgotten moon has started sending messages.','The royal library now contains books written next week.','Someone has been buying identical keys in every timeline.','The northern sky briefly turned into an ocean.','A village woke up with memories belonging to strangers.','An ancient statue keeps changing its expression.','The city clocks all disagree by exactly one impossible minute.','A harmless pigeon has been delivering sealed royal orders.'];
const FACTIONS=['The Glass Parliament','The Ember Choir','The Null Cartographers','The Midnight Guild','The Seven Lanterns','The Copper Covenant','The Quiet Legion','The Astral Market','The Hollow Court','The Last Navigators'];
function esc(v){{return String(v??'').replace(/[&<>\"']/g,m=>({{'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}}[m]))}}\nfunction pick(a){{return a[Math.floor(Math.random()*a.length)]}}
function sample(a,n){{return [...a].sort(()=>Math.random()-.5).slice(0,n)}}
function safeHistory(){{try{{const x=JSON.parse(localStorage.getItem(WORLD_HISTORY_KEY)||'[]');return Array.isArray(x)?x:[]}}catch(_){{return[]}}}}
function rememberUniverse(signature){{try{{const h=safeHistory();h.push(signature);localStorage.setItem(WORLD_HISTORY_KEY,JSON.stringify(h.slice(-100)));return h.length}}catch(_){{return 0}}}}
function makeUniverse(){{
  const history=safeHistory(); let u,signature,tries=0;
  do{{
    const worldName=`${{pick(WORDS.prefixes)}} ${{pick(WORDS.middles)}} ${{pick(WORDS.suffixes)}}`;
    const worldType=pick(['Cosmic Fantasy','Dark Sci-Fi','Mythic Space Opera','Surreal Fantasy','Post-Magic Future','Dimensional Adventure']);
    const faction=pick(FACTIONS), biome=pick(BIOMES);
    const npcNames=sample(NPC_NAMES,8), surnames=sample(NPC_SURNAMES,8), roles=sample(ROLES,8);
    const npcs=npcNames.map((n,i)=>({{id:`npc-${{i}}`,name:`${{n}} ${{surnames[i]}}`,category:'NPC',rarity:pick(['Common','Rare','Epic','Legendary','Mythic']),role:roles[i],world:worldName,description:`${{roles[i]}} of ${{worldName}}, currently operating from the ${{biome}} for the ${{faction}}.`,tags:[worldType.toLowerCase(),roles[i].toLowerCase().split(' ')[0],faction.split(' ')[1]?.toLowerCase()||'lore']}}));
    const worlds=[{{id:'world-0',name:worldName,type:worldType,status:'New Universe',description:`${{worldName}} is a newly discovered universe of ${{biome}}, ruled by rumor, unstable physics and ${{faction}}.`,tags:[worldType.toLowerCase(),'new universe',biome.split(' ')[0],faction.split(' ')[1]?.toLowerCase()||'lore']}}];
    const quests=sample(QUEST_GOALS,4).map((goal,i)=>({{id:`quest-${{i}}`,name:['The First Crossing','The Impossible Hour','The Unwritten Map','The Last Signal'][i],difficulty:pick(['Hard','Extreme','Legendary','Mythic']),status:'New',world:worldName,description:`In ${{worldName}}, ${{goal}} before the ${{faction}} reaches the ${{biome}}.`,tags:['quest',worldType.toLowerCase().split(' ')[0],'expedition']}}));
    const posts=sample(LORE_HOOKS,6).map((hook,i)=>({{id:`lore-${{i}}`,name:['World Signal','Strange Report','Archive Fragment','Traveler Note','Forbidden Rumor','Universe Bulletin'][i],type:pick(['Lore','Rumor','Faction','Discovery']),world:worldName,description:hook+` Witnesses place the event somewhere in ${{worldName}}.`,tags:['lore',worldType.toLowerCase().split(' ')[0],faction.split(' ')[1]?.toLowerCase()||'mystery']}}));
    signature=JSON.stringify({{worldName,worldType,faction,biome,npcs:npcs.map(x=>x.name),quests:quests.map(x=>x.name+x.description),posts:posts.map(x=>x.description)}});
    u={{worldName,worldType,faction,biome,npcs,worlds,quests,posts}}; tries++;
  }}while(history.includes(signature)&&tries<100);
  rememberUniverse(signature); return u;
}}
function makeCard(item,type,icon,label){{
  const card=document.createElement('article');card.className='card';card.dataset.type=type;card.dataset.search=Object.values(item).join(' ').toLowerCase();card.dataset.item=JSON.stringify(item);
  const meta=['category','rarity','role','type','difficulty','status','world'].filter(k=>item[k]).map(k=>`<span>${{esc(item[k])}}</span>`).join('');
  const tags=(item.tags||[]).slice(0,6).map(t=>`<span class="tag">#${{esc(t)}}</span>`).join('');
  card.innerHTML=`<div class="card-top"><span class="eyebrow">${{icon}} ${{esc(label)}}</span><div style="display:flex;gap:6px"><button class="icon-btn x-save" aria-label="Save item" onclick="toggleSaved(this.closest('.card'))">☆</button><button class="icon-btn" aria-label="Share" onclick="shareItem(this.closest('.card'))">↗</button></div></div><h3>${{esc(item.name)}}</h3><p>${{esc(item.description||'')}}</p><div class="meta">${{meta}}</div><div class="tags">${{tags}}</div><div class="card-actions"><button class="btn small x-view" onclick="openItem(this.closest('.card'))">View</button><button class="btn small ghost" onclick="screenshotCard(this.closest('.card'))">Screenshot</button></div>`;
  return card;
}}
function renderUniverse(provided,archiveIt=false){{
  const u=provided||makeUniverse(),grid=document.getElementById('resultsGrid');grid.innerHTML='';cards.length=0;
  const data=[['npcs','👤','NPCs',u.npcs],['worlds','🌍','Worlds',u.worlds],['quests','⚔️','Quests',u.quests],['posts','📜','Lore',u.posts]];
  for(const [type,icon,label,list] of data)for(const item of list){{const c=makeCard(item,type,icon,label);grid.appendChild(c);cards.push(c)}}
  const hero=document.querySelector('.hero .eyebrow');if(hero)hero.textContent=`NPCBOOK · ${{u.worldName}} · NEW UNIVERSE`;
  const title=document.querySelector('.hero h1');if(title)title.innerHTML=`The fictional<br><span class="gradient">${{esc(u.worldName)}}.</span>`;
  saveCurrent(u);if(archiveIt)saveArchive(u);syncSaveButtons();
  const desc=document.querySelector('.hero p');if(desc)desc.textContent=`${{u.worldType}} · ${{u.faction}} · ${{u.biome}}. Every refresh creates a different universe; previously generated universes are remembered locally so they are not repeated.`;
}}
search.addEventListener('input',e=>{{state.query=e.target.value.trim().toLowerCase();apply()}});
document.addEventListener('keydown',e=>{{if(e.key==='/'&&document.activeElement!==search){{e.preventDefault();search.focus()}}if(e.key==='Escape')closeModal()}});
function clearSearch(){{search.value='';state.query='';setFilter('all')}}
function openItem(card){{const i=JSON.parse(card.dataset.item);state.selected=i;document.getElementById('modalType').textContent=card.dataset.type.toUpperCase();document.getElementById('modalTitle').textContent=i.name;document.getElementById('modalDescription').textContent=i.description||'';document.getElementById('modalDetails').innerHTML=Object.entries(i).filter(([k,v])=>!['id','name','description','tags'].includes(k)&&v).map(([k,v])=>'<div class="detail"><small>'+k+'</small><strong>'+String(Array.isArray(v)?v.join(', '):v)+'</strong></div>').join('');document.getElementById('modalTags').innerHTML=(i.tags||[]).map(t=>'<span class="tag">#'+t+'</span>').join('');document.getElementById('modal').classList.add('open');document.body.style.overflow='hidden'}}
function closeModal(){{document.getElementById('modal').classList.remove('open');document.body.style.overflow=''}}
async function shareModal(){{if(state.selected)shareData(state.selected.name,state.selected.description||location.href)}}
async function shareItem(c){{const i=JSON.parse(c.dataset.item);shareData(i.name,i.description||location.href)}}
async function shareData(title,text){{try{{if(navigator.share)await navigator.share({{title,text,url:location.href}});else{{await navigator.clipboard.writeText(location.href);toast('Link copied')}}}}catch(_){{}}}}
function randomDiscovery(){{const p=cards.filter(c=>!c.classList.contains('hidden')),pool=p.length?p:cards,t=pool[Math.floor(Math.random()*pool.length)];t.scrollIntoView({{behavior:'smooth',block:'center'}});openItem(t)}}
function newUniverse(){{location.reload()}}
const ARCHIVE_KEY='npcbook-universe-archive-v1',SAVED_KEY='npcbook-saved-items-v1',CURRENT_KEY='npcbook-current-universe-v1';
function readStore(key,fallback){{try{{const v=JSON.parse(localStorage.getItem(key)||'null');return v===null?fallback:v}}catch(_){{return fallback}}}}
function writeStore(key,value){{try{{localStorage.setItem(key,JSON.stringify(value));return true}}catch(_){{toast('Local storage is full');return false}}}}
function saveArchive(u){{const archive=readStore(ARCHIVE_KEY,[]);archive.unshift({{id:Date.now().toString(36),name:u.worldName,type:u.worldType,faction:u.faction,universe:u}});writeStore(ARCHIVE_KEY,archive.slice(0,12))}}
function saveCurrent(u){{writeStore(CURRENT_KEY,u)}}
function savedItems(){{return readStore(SAVED_KEY,[])}}
function isSaved(item){{return savedItems().some(x=>x.id===item.id&&x.name===item.name)}}
function toggleSaved(card){{const item=JSON.parse(card.dataset.item),list=savedItems(),idx=list.findIndex(x=>x.id===item.id&&x.name===item.name);if(idx>=0){{list.splice(idx,1);toast('Removed from saved')}}else{{list.unshift(item);toast('Saved to your library')}}writeStore(SAVED_KEY,list.slice(0,100));syncSaveButtons()}}
function saveSelected(){{if(!state.selected)return;const fake=document.createElement('article');fake.dataset.item=JSON.stringify(state.selected);toggleSaved(fake)}}
function syncSaveButtons(){{cards.forEach(c=>{{const b=c.querySelector('.x-save');if(!b)return;const i=JSON.parse(c.dataset.item);b.textContent=isSaved(i)?'★':'☆';b.title=isSaved(i)?'Remove saved item':'Save item'}})}}
function openHistory(){{const archive=readStore(ARCHIVE_KEY,[]),saved=savedItems();const items=archive.map((a,i)=>'<div class="detail"><small>Universe '+(i+1)+'</small><strong>'+esc(a.name)+'</strong><span style="display:block;color:var(--muted);margin-top:5px">'+esc(a.type)+' · '+esc(a.faction)+'</span><button class="btn small x-load-archive" data-archive-id="'+esc(a.id)+'" style="margin-top:8px">Load</button></div>').join('');document.getElementById('modalType').textContent='LOCAL LIBRARY';document.getElementById('modalTitle').textContent=archive.length+' universes · '+saved.length+' saved items';document.getElementById('modalDescription').textContent='Your generated universes and saved discoveries live only in this browser.';document.getElementById('modalDetails').innerHTML=items||'<div class="detail"><strong>No archived universes yet.</strong><span style="display:block;color:var(--muted);margin-top:5px">Generate a universe and it will appear here.</span></div>';document.getElementById('modalTags').innerHTML='<button class="btn small ghost" onclick="clearLibrary()">Clear local library</button>';document.getElementById('modal').classList.add('open');document.body.style.overflow='hidden'}}
document.getElementById('modalDetails').addEventListener('click',e=>{{const b=e.target.closest('.x-load-archive');if(b)loadArchived(b.dataset.archiveId)}})
function loadArchived(id){{const a=readStore(ARCHIVE_KEY,[]).find(x=>x.id===id);if(!a)return;renderUniverse(a.universe);closeModal();toast('Loaded '+a.name)}}
function clearLibrary(){{if(confirm('Clear saved items and universe history from this browser?')){{localStorage.removeItem(ARCHIVE_KEY);localStorage.removeItem(SAVED_KEY);localStorage.removeItem(WORLD_HISTORY_KEY);toast('Local library cleared');closeModal()}}}}
function exportUniverse(){{const u=readStore(CURRENT_KEY,null);if(!u){{toast('Generate a universe first');return}}const blob=new Blob([JSON.stringify(u,null,2)],{{type:'application/json'}}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='npcbook-'+slugify(u.worldName)+'.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);toast('Universe exported')}}
function slugify(v){{return String(v||'universe').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')}}
document.getElementById('importUniverse').addEventListener('change',function(e){{
  const file=e.target.files&&e.target.files[0];if(!file)return;
  const reader=new FileReader();
  reader.onload=function(){{
    try{{
      const u=JSON.parse(reader.result);
      if(!u.worldName||!Array.isArray(u.npcs)||!Array.isArray(u.quests))throw new Error('invalid');
      writeStore(CURRENT_KEY,u);saveArchive(u);renderUniverse(u,true);apply();toast('Universe imported');
    }}catch(_){{
      toast('Invalid NPCBook universe file');
    }}
    e.target.value='';
  }};
  reader.readAsText(file);
}});

function screenshotCard(card){{const i=JSON.parse(card.dataset.item),c=document.createElement('canvas'),w=1200,h=700,d=2;c.width=w*d;c.height=h*d;const x=c.getContext('2d');x.scale(d,d);x.fillStyle='#080b14';x.fillRect(0,0,w,h);x.fillStyle='#8d88ff';x.font='800 18px Arial';x.fillText('NPCBOOK · {BRAND}',70,75);x.fillStyle='#fff';x.font='800 48px Arial';x.fillText(i.name,70,145);x.fillStyle='#aeb7ca';x.font='24px Arial';x.fillText((i.description||'').slice(0,90),70,205);x.fillStyle='#69758c';x.font='16px Arial';x.fillText((i.tags||[]).map(t=>'#'+t).join('   '),70,610);c.toBlob(b=>{{const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='npcbook-'+String(i.name||'item').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')+'.png';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}},'image/png')}}
function toast(m){{const t=document.getElementById('toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1800)}}
let themeMode=localStorage.getItem(THEME_KEY)==='light'?'light':'dark';
function applyTheme(){{
  const root=document.documentElement,btn=document.getElementById('themeBtn');
  if(themeMode==='light'){{
    root.style.setProperty('--bg','#f5f7fb');root.style.setProperty('--text','#111827');root.style.setProperty('--muted','#5f6b80');root.style.setProperty('--line','#dbe1ec');
    btn.textContent='☾';btn.setAttribute('aria-label','Switch to dark theme');btn.title='Switch to dark theme';
  }}else{{
    root.style.setProperty('--bg','#070a12');root.style.setProperty('--text','#f5f7ff');root.style.setProperty('--muted','#8e9ab1');root.style.setProperty('--line','#202b40');
    btn.textContent='☼';btn.setAttribute('aria-label','Switch to light theme');btn.title='Switch to light theme';
  }}
}}
function toggleTheme(){{
  themeMode=themeMode==='dark'?'light':'dark';localStorage.setItem(THEME_KEY,themeMode);applyTheme();
  const root=document.documentElement,btn=document.getElementById('themeBtn');
  if(themeMode==='light'){{
    root.style.setProperty('--bg','#f5f7fb');root.style.setProperty('--text','#111827');root.style.setProperty('--muted','#5f6b80');root.style.setProperty('--line','#dbe1ec');
    btn.textContent='☾';btn.setAttribute('aria-label','Switch to dark theme');btn.title='Switch to dark theme';
  }}else{{
    root.style.setProperty('--bg','#070a12');root.style.setProperty('--text','#f5f7ff');root.style.setProperty('--muted','#8e9ab1');root.style.setProperty('--line','#202b40');
    btn.textContent='☼';btn.setAttribute('aria-label','Switch to light theme');btn.title='Switch to light theme';
  }}
}}
document.querySelector('.filters').insertAdjacentHTML('beforeend','<button class="filter" data-filter="saved" onclick="setFilter(\'saved\')">⭐ Saved</button>');
function cycleFilter(){{const fs=['all','npcs','worlds','quests','posts','saved'],i=fs.indexOf(state.filter);setFilter(fs[(i+1)%fs.length])}}
document.addEventListener('keydown',e=>{{if(e.key.toLowerCase()==='n'&&!e.ctrlKey&&!e.metaKey){{e.preventDefault();newUniverse()}}if(e.key.toLowerCase()==='s'&&!e.ctrlKey&&!e.metaKey&&document.activeElement!==search){{e.preventDefault();setFilter('saved')}}if(e.key.toLowerCase()==='f'&&!e.ctrlKey&&!e.metaKey&&document.activeElement!==search){{e.preventDefault();search.focus()}}if(e.key.toLowerCase()==='c'&&!e.ctrlKey&&!e.metaKey&&document.activeElement!==search){{e.preventDefault();cycleFilter()}}}});
applyTheme();
let deferredInstall=null;window.addEventListener('beforeinstallprompt',e=>{{e.preventDefault();deferredInstall=e;document.getElementById('installBtn').classList.add('show')}});document.getElementById('installBtn').addEventListener('click',async()=>{{if(!deferredInstall)return;deferredInstall.prompt();await deferredInstall.userChoice;deferredInstall=null;document.getElementById('installBtn').classList.remove('show')}});
window.addEventListener('online',()=>toast('Back online'));window.addEventListener('offline',()=>toast('Offline mode: cached content available'));window.addEventListener('appinstalled',()=>toast('NPCBook installed successfully'));
renderUniverse(null,true);apply();
if('serviceWorker' in navigator)window.addEventListener('load',()=>navigator.serviceWorker.register('/sw.js').then(reg=>{{if(reg.waiting)toast('A newer NPCBook version is ready');reg.addEventListener('updatefound',()=>{{const w=reg.installing;if(w)w.addEventListener('statechange',()=>{{if(w.state==='installed'&&navigator.serviceWorker.controller)toast('NPCBook updated — refresh for the latest version')}})}})}}).catch(()=>{{}}));</script></body></html>'''

def build_manifest():
    return json.dumps({"name":SITE["name"],"short_name":"NPCBook","id":"/","description":SITE["description"],"start_url":"/","scope":"/","display":"standalone","display_override":["window-controls-overlay","standalone","minimal-ui"],"orientation":"any","background_color":"#070a12","theme_color":"#090d18","categories":["entertainment","books","games"],"lang":"en","shortcuts":[{"name":"Explore NPCs","short_name":"NPCs","url":"/#explore"},{"name":"Random discovery","short_name":"Random","url":"/#explore"}],"icons":[{"src":"/favicon.svg?v=10","sizes":"any","type":"image/svg+xml","purpose":"any maskable"},{"src":"/favicon.ico?v=10","sizes":"32x32","type":"image/x-icon","purpose":"any"}]},indent=2)

def build_sw():
    return """const CACHE='npcbook-v17';const CORE=['/','/index.html','/manifest.webmanifest','/favicon.svg','/favicon.ico','/logo.svg','/robots.txt','/sitemap.xml','/404.html'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==CACHE).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;let u;try{u=new URL(e.request.url)}catch(_){return}if(u.protocol!=='http:'&&u.protocol!=='https:')return;if(u.origin!==self.location.origin)return;e.respondWith(fetch(e.request).then(r=>{if(r.ok&&e.request.cache!=='no-store'){return caches.open(CACHE).then(c=>c.put(e.request,r.clone()).then(()=>r).catch(()=>r))}return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('/404.html'))))});
"""
def build_favicon():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128"><defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="#7c6cff"/><stop offset="1" stop-color="#31d8ff"/></linearGradient></defs><rect width="128" height="128" rx="30" fill="#090d18"/><rect x="12" y="12" width="104" height="104" rx="26" fill="url(#g)"/><path d="M34 48c0-10 8-18 18-18h24c10 0 18 8 18 18v20c0 10-8 18-18 18H58l-14 12V86c-6-3-10-9-10-18V48Z" fill="#fff"/><circle cx="58" cy="58" r="6" fill="#111827"/><circle cx="78" cy="58" r="6" fill="#111827"/><path d="M55 73c7 5 15 5 22 0" fill="none" stroke="#111827" stroke-width="5" stroke-linecap="round"/></svg>'''
def build_404():
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>NPCBook — Page not found</title><link rel="icon" href="/favicon.ico?v=10" type="image/x-icon"><link rel="icon" href="/favicon.svg?v=10" type="image/svg+xml"><style>body{margin:0;background:#070a12;color:#fff;font-family:system-ui;display:grid;place-items:center;min-height:100vh;text-align:center}main{max-width:520px;padding:30px}a{display:inline-block;padding:11px 16px;border-radius:12px;background:#7c6cff;color:#fff;text-decoration:none;font-weight:800}</style><main><div style="font-size:80px">🤖</div><h1>NPC not found.</h1><p>This page probably walked into another dimension.</p><a href="/">Return to NPCBook</a></main>'''
def build_robots(): return f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
def build_sitemap(): return f'''<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE_URL}/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url></urlset>'''
def build():
    OUTPUT_DIR.mkdir(parents=True,exist_ok=True)
    files={"index.html":build_html(),"404.html":build_404(),"favicon.svg":build_favicon(),"logo.svg":build_favicon(),"favicon.ico":__import__("base64").b64decode(FAVICON_ICO_BASE64),"manifest.webmanifest":build_manifest(),"sw.js":build_sw(),"robots.txt":build_robots(),"sitemap.xml":build_sitemap()}
    for name,data in files.items():(OUTPUT_DIR/name).write_bytes(data) if isinstance(data,bytes) else (OUTPUT_DIR/name).write_text(data,encoding="utf-8")
    print("NPCBook build complete:",OUTPUT_DIR.resolve())
if __name__=="__main__": build()
