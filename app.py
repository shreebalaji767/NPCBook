from pathlib import Path

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#07101d">
<meta name="description" content="NPCBook — Social Media for NPCs">
<title>NPCBook — Social Media for NPCs</title>

<style>
:root{
    --bg:#07101d;
    --bg2:#0c1626;
    --card:#101b2d;
    --card2:#142238;
    --card3:#182941;
    --text:#edf4ff;
    --muted:#8fa2bb;
    --muted2:#6f829d;
    --line:#24364e;
    --blue:#5b8cff;
    --purple:#9a72ff;
    --pink:#ff5d8f;
    --green:#43d49b;
    --yellow:#f5c451;
    --danger:#ff6677;
    --radius:18px;
    --top:66px;
}

*{
    box-sizing:border-box;
    -webkit-tap-highlight-color:transparent;
}

html{
    background:var(--bg);
    scroll-behavior:smooth;
}

body{
    margin:0;
    min-height:100vh;
    overflow-x:hidden;
    color:var(--text);
    background:
        radial-gradient(circle at 10% 0%,rgba(91,140,255,.10),transparent 28%),
        radial-gradient(circle at 90% 5%,rgba(154,114,255,.09),transparent 28%),
        var(--bg);
    font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
}

button,input{
    font:inherit;
}

button{
    color:inherit;
    cursor:pointer;
    touch-action:manipulation;
}

button:focus-visible,
input:focus-visible{
    outline:3px solid rgba(91,140,255,.4);
    outline-offset:2px;
}

.app{
    min-height:100vh;
}

/* TOP BAR */

.topbar{
    position:sticky;
    top:0;
    z-index:100;
    height:var(--top);
    background:rgba(7,16,29,.9);
    border-bottom:1px solid rgba(255,255,255,.07);
    backdrop-filter:blur(18px);
    -webkit-backdrop-filter:blur(18px);
}

.topbar-inner{
    width:min(1500px,100%);
    height:100%;
    margin:auto;
    padding:0 18px;
    display:grid;
    grid-template-columns:250px minmax(200px,520px) 1fr;
    gap:18px;
    align-items:center;
}

.logo{
    border:0;
    background:transparent;
    display:flex;
    align-items:center;
    gap:10px;
    padding:4px;
    text-align:left;
    font-weight:900;
}

.logo-icon{
    width:40px;
    height:40px;
    border-radius:13px;
    display:grid;
    place-items:center;
    background:linear-gradient(135deg,#5b8cff,#9a72ff);
    box-shadow:0 8px 25px rgba(91,140,255,.25);
    font-size:20px;
}

.logo-text{
    font-size:21px;
}

.logo-sub{
    color:var(--muted);
    display:block;
    font-size:9px;
    letter-spacing:1px;
    margin-top:2px;
}

.search{
    position:relative;
}

.search input{
    width:100%;
    height:43px;
    padding:0 15px 0 42px;
    border:1px solid var(--line);
    border-radius:14px;
    background:#0d1829;
    color:var(--text);
    outline:none;
}

.search input::placeholder{
    color:#71839d;
}

.search-icon{
    position:absolute;
    left:14px;
    top:50%;
    transform:translateY(-50%);
    color:var(--muted);
    pointer-events:none;
}

.top-actions{
    display:flex;
    justify-content:flex-end;
    gap:7px;
}

.icon-btn,
.top-avatar{
    width:44px;
    min-width:44px;
    height:44px;
    border:1px solid var(--line);
    border-radius:13px;
    background:#101c2e;
    display:grid;
    place-items:center;
    font-size:18px;
}

.top-avatar{
    border:0;
    overflow:hidden;
}

/* MAIN */

.layout{
    width:min(1500px,100%);
    margin:auto;
    padding:20px 18px 100px;
    display:grid;
    grid-template-columns:225px minmax(0,700px) 290px;
    gap:22px;
}

.sidebar{
    min-width:0;
}

.sidebar-card{
    position:sticky;
    top:86px;
    background:rgba(16,27,45,.82);
    border:1px solid var(--line);
    border-radius:18px;
    padding:9px;
}

.nav{
    width:100%;
    min-height:46px;
    border:0;
    border-radius:12px;
    background:transparent;
    color:#c6d3e5;
    display:flex;
    align-items:center;
    gap:11px;
    padding:10px 12px;
    margin:2px 0;
    text-align:left;
    font-weight:700;
}

.nav:hover,
.nav.active{
    background:#17263c;
    color:white;
}

.nav-icon{
    width:23px;
    text-align:center;
}

.nav-divider{
    height:1px;
    background:var(--line);
    margin:9px 5px;
}

.nav-title{
    padding:9px 12px 5px;
    font-size:10px;
    color:var(--muted2);
    text-transform:uppercase;
    letter-spacing:1px;
    font-weight:900;
}

/* FEED */

.heading{
    display:flex;
    justify-content:space-between;
    gap:12px;
    align-items:center;
    margin-bottom:13px;
}

.heading h1{
    margin:0;
    font-size:23px;
}

.heading p{
    margin:4px 0 0;
    color:var(--muted);
    font-size:12px;
}

.btn{
    min-height:43px;
    padding:0 14px;
    border-radius:12px;
    font-weight:800;
}

.primary{
    border:0;
    color:white;
    background:linear-gradient(135deg,#5b8cff,#8067ff);
}

.secondary{
    border:1px solid var(--line);
    background:#121f33;
}

.composer,
.post,
.side-card,
.profile-info{
    background:rgba(16,27,45,.92);
    border:1px solid var(--line);
    box-shadow:0 8px 28px rgba(0,0,0,.13);
}

.composer{
    border-radius:18px;
    padding:14px;
    margin-bottom:14px;
}

.composer-row{
    display:flex;
    gap:10px;
}

.avatar{
    width:44px;
    height:44px;
    flex:0 0 44px;
    border-radius:50%;
    display:grid;
    place-items:center;
    font-size:22px;
    background:linear-gradient(135deg,#263e63,#182a42);
    border:1px solid rgba(255,255,255,.08);
}

.composer input{
    flex:1;
    min-width:0;
    height:44px;
    border-radius:22px;
    border:1px solid var(--line);
    background:#0b1728;
    color:var(--text);
    padding:0 17px;
}

.composer-tools{
    display:flex;
    flex-wrap:wrap;
    gap:7px;
    margin-top:10px;
}

.chip{
    min-height:37px;
    padding:0 11px;
    border:1px solid var(--line);
    border-radius:10px;
    background:#111f32;
    color:#aebed2;
}

/* POST */

.post{
    border-radius:18px;
    padding:15px;
    margin-bottom:14px;
}

.post-header{
    display:flex;
    gap:10px;
    align-items:flex-start;
}

.post-author{
    flex:1;
    min-width:0;
}

.author{
    border:0;
    padding:0;
    background:transparent;
    text-align:left;
    max-width:100%;
}

.author-name{
    display:flex;
    align-items:center;
    gap:5px;
    font-weight:850;
}

.author-name-text{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.verify{
    width:16px;
    height:16px;
    flex:0 0 16px;
    border-radius:50%;
    background:#4b8dff;
    display:grid;
    place-items:center;
    color:white;
    font-size:9px;
}

.handle{
    color:var(--muted);
    font-size:12px;
    margin-top:2px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.time{
    color:var(--muted2);
    font-size:11px;
    white-space:nowrap;
}

.more{
    width:38px;
    height:38px;
    border:0;
    border-radius:10px;
    background:transparent;
    color:var(--muted);
}

.more:hover{
    background:#17263c;
}

.post-text{
    margin:13px 2px;
    font-size:15px;
    line-height:1.62;
    white-space:pre-wrap;
    overflow-wrap:anywhere;
}

.tags{
    display:flex;
    gap:6px;
    flex-wrap:wrap;
    margin:7px 2px 11px;
}

.tag{
    min-height:25px;
    display:inline-flex;
    align-items:center;
    padding:0 8px;
    border-radius:8px;
    border:1px solid #273d59;
    background:#15253b;
    color:#9fb5d0;
    font-size:10px;
    font-weight:800;
}

.tag.world{
    color:#c0adff;
    border-color:rgba(154,114,255,.25);
    background:rgba(154,114,255,.08);
}

.scene{
    position:relative;
    min-height:190px;
    margin:10px 0 13px;
    overflow:hidden;
    border-radius:15px;
    border:1px solid rgba(255,255,255,.08);
    display:flex;
    align-items:flex-end;
}

.scene::before{
    content:"";
    position:absolute;
    inset:0;
    background:
        radial-gradient(circle at 20% 20%,rgba(255,255,255,.15),transparent 20%),
        radial-gradient(circle at 80% 30%,rgba(255,255,255,.10),transparent 25%),
        linear-gradient(135deg,var(--a),var(--b));
}

.scene-inner{
    position:relative;
    z-index:1;
    width:100%;
    padding:19px;
    background:linear-gradient(transparent,rgba(0,0,0,.72));
}

.scene-icon{
    font-size:39px;
}

.scene-title{
    margin-top:7px;
    font-weight:900;
}

.scene-sub{
    color:#c7d5e7;
    font-size:11px;
    margin-top:4px;
}

.post-stats{
    display:flex;
    justify-content:space-between;
    color:var(--muted);
    font-size:11px;
    padding:0 3px 8px;
}

.actions{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    border-top:1px solid rgba(255,255,255,.06);
    padding-top:8px;
    gap:4px;
}

.action{
    min-height:42px;
    border:0;
    border-radius:10px;
    background:transparent;
    color:#94a8c0;
    display:flex;
    justify-content:center;
    align-items:center;
    gap:6px;
    font-size:12px;
    font-weight:750;
}

.action:hover{
    background:#17263c;
    color:white;
}

.action.liked{
    color:var(--pink);
}

.action.saved{
    color:var(--yellow);
}

.comments{
    border-top:1px solid rgba(255,255,255,.05);
    margin-top:8px;
    padding-top:8px;
}

.comment{
    color:#aebed1;
    font-size:12px;
    line-height:1.45;
    margin:6px 0;
}

.comment b{
    color:#e7effb;
}

/* RIGHT SIDE */

.side-card{
    border-radius:18px;
    padding:14px;
    margin-bottom:14px;
}

.side-card h3{
    margin:0 0 10px;
    font-size:14px;
}

.trend{
    padding:9px 0;
    border-bottom:1px solid rgba(255,255,255,.06);
}

.trend:last-child{
    border-bottom:0;
}

.trend small{
    color:var(--muted2);
}

.trend b{
    display:block;
    margin-top:3px;
}

.mini-user{
    display:flex;
    gap:9px;
    align-items:center;
    padding:8px 0;
}

.mini-info{
    flex:1;
    min-width:0;
}

.mini-name{
    font-weight:750;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.mini-handle{
    color:var(--muted);
    font-size:10px;
}

.follow{
    min-height:34px;
    padding:0 9px;
    border:1px solid #31507c;
    border-radius:9px;
    background:#15243a;
    font-size:11px;
    font-weight:800;
}

/* PROFILE */

.profile-cover{
    height:220px;
    border-radius:20px 20px 0 0;
    position:relative;
    overflow:hidden;
}

.profile-cover::before{
    content:"";
    position:absolute;
    inset:0;
    background:
        radial-gradient(circle at 15% 25%,rgba(255,255,255,.20),transparent 18%),
        radial-gradient(circle at 80% 20%,rgba(255,255,255,.14),transparent 22%),
        linear-gradient(135deg,var(--a),var(--b));
}

.profile-cover::after{
    content:"NPC WORLD";
    position:absolute;
    right:20px;
    bottom:15px;
    color:rgba(255,255,255,.07);
    font-weight:1000;
    font-size:clamp(30px,7vw,72px);
    letter-spacing:3px;
}

.profile-info{
    border-top:0;
    border-radius:0 0 20px 20px;
    padding:0 20px 18px;
    margin-bottom:15px;
}

.profile-main{
    position:relative;
    z-index:2;
    margin-top:-54px;
    display:flex;
    align-items:flex-end;
    gap:14px;
}

.profile-avatar{
    width:106px;
    height:106px;
    flex:0 0 106px;
    border:5px solid var(--card);
    border-radius:50%;
    display:grid;
    place-items:center;
    font-size:48px;
    background:linear-gradient(135deg,#2a4167,#172b46);
}

.profile-buttons{
    margin-left:auto;
    display:flex;
    gap:7px;
    flex-wrap:wrap;
}

.profile-details{
    margin-top:11px;
}

.profile-details h1{
    margin:0;
    font-size:25px;
}

.profile-handle{
    color:var(--muted);
    margin-top:2px;
}

.bio{
    color:#c6d4e6;
    line-height:1.55;
    margin:11px 0;
}

.profile-stats{
    display:flex;
    flex-wrap:wrap;
    gap:18px;
    color:var(--muted);
    font-size:12px;
}

.profile-stats b{
    color:white;
}

.profile-tabs{
    display:flex;
    gap:4px;
    overflow-x:auto;
    scrollbar-width:none;
    margin-top:15px;
    border-top:1px solid rgba(255,255,255,.06);
    padding-top:7px;
}

.profile-tabs::-webkit-scrollbar{
    display:none;
}

.tab{
    min-height:41px;
    padding:0 13px;
    border:0;
    border-radius:9px;
    background:transparent;
    color:var(--muted);
    font-weight:800;
    white-space:nowrap;
}

.tab.active{
    background:#17263c;
    color:white;
}

.back{
    margin-bottom:11px;
}

/* EMPTY */

.empty{
    border:1px solid var(--line);
    background:rgba(16,27,45,.8);
    border-radius:18px;
    padding:45px 20px;
    text-align:center;
    color:var(--muted);
}

.empty-icon{
    font-size:45px;
    margin-bottom:10px;
}

/* MODAL */

.modal-layer{
    position:fixed;
    inset:0;
    z-index:500;
    background:rgba(0,0,0,.68);
    display:none;
    align-items:center;
    justify-content:center;
    padding:18px;
}

.modal-layer.open{
    display:flex;
}

.modal{
    width:min(620px,100%);
    max-height:90vh;
    overflow:auto;
    border:1px solid var(--line);
    border-radius:20px;
    background:#101b2d;
    box-shadow:0 30px 100px rgba(0,0,0,.55);
}

.modal-head{
    position:sticky;
    top:0;
    z-index:2;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:14px 16px;
    border-bottom:1px solid var(--line);
    background:rgba(16,27,45,.95);
    backdrop-filter:blur(12px);
}

.modal-head h2{
    margin:0;
    font-size:17px;
}

.close{
    width:42px;
    height:42px;
    border:0;
    border-radius:10px;
    background:#18283e;
    font-size:19px;
}

.modal-body{
    padding:16px;
}

.notice{
    padding:13px;
    margin-bottom:9px;
    border:1px solid #263d5b;
    border-radius:12px;
    background:#132239;
    color:#bfccde;
    line-height:1.5;
}

/* MOBILE */

.mobile-nav{
    display:none;
}

.toast{
    position:fixed;
    left:50%;
    bottom:24px;
    z-index:700;
    transform:translate(-50%,20px);
    opacity:0;
    pointer-events:none;
    background:#16253a;
    border:1px solid #304a6d;
    border-radius:12px;
    padding:11px 16px;
    color:white;
    box-shadow:0 12px 40px rgba(0,0,0,.35);
    max-width:90vw;
    text-align:center;
    font-size:12px;
    transition:.2s;
}

.toast.show{
    opacity:1;
    transform:translate(-50%,0);
}

/* TABLET */

@media(max-width:1180px){
    .layout{
        grid-template-columns:205px minmax(0,1fr);
    }

    .right-sidebar{
        display:none;
    }

    .topbar-inner{
        grid-template-columns:220px minmax(180px,1fr) auto;
    }
}

/* MOBILE */

@media(max-width:800px){
    :root{
        --top:60px;
    }

    body{
        padding-bottom:calc(74px + env(safe-area-inset-bottom));
    }

    .topbar-inner{
        padding:0 9px;
        grid-template-columns:auto minmax(0,1fr) auto;
        gap:8px;
    }

    .logo{
        font-size:0;
    }

    .logo-icon{
        width:39px;
        height:39px;
    }

    .logo-text,
    .logo-sub{
        display:none;
    }

    .top-actions{
        gap:4px;
    }

    .top-actions .icon-btn:nth-child(1){
        display:none;
    }

    .top-avatar{
        display:none;
    }

    .layout{
        display:block;
        padding:11px 9px 95px;
    }

    .left-sidebar,
    .right-sidebar{
        display:none;
    }

    .mobile-nav{
        position:fixed;
        display:grid;
        grid-template-columns:repeat(5,1fr);
        left:0;
        right:0;
        bottom:0;
        z-index:200;
        min-height:63px;
        padding:4px 5px calc(4px + env(safe-area-inset-bottom));
        background:rgba(7,16,29,.95);
        border-top:1px solid rgba(255,255,255,.08);
        backdrop-filter:blur(18px);
        -webkit-backdrop-filter:blur(18px);
    }

    .mobile-nav button{
        min-height:50px;
        border:0;
        border-radius:11px;
        background:transparent;
        color:#7f93ad;
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        gap:2px;
        font-size:10px;
        font-weight:800;
    }

    .mobile-nav button.active{
        background:#16263c;
        color:white;
    }

    .mobile-nav span:first-child{
        font-size:18px;
    }

    .post{
        border-radius:15px;
        padding:13px;
    }

    .composer{
        border-radius:15px;
    }

    .profile-cover{
        height:170px;
    }

    .profile-main{
        flex-wrap:wrap;
    }

    .profile-avatar{
        width:88px;
        height:88px;
        flex-basis:88px;
        font-size:39px;
    }

    .profile-buttons{
        width:100%;
        margin-left:0;
    }

    .modal-layer{
        padding:7px;
        align-items:flex-end;
    }

    .modal{
        max-height:92vh;
        border-radius:19px 19px 0 0;
    }
}

@media(max-width:520px){
    .search input{
        padding-left:36px;
        font-size:12px;
    }

    .heading .secondary{
        display:none;
    }

    .actions{
        grid-template-columns:repeat(4,1fr);
    }

    .action{
        min-height:45px;
    }

    .action .label{
        display:none;
    }

    .scene{
        min-height:165px;
    }

    .profile-info{
        padding-left:14px;
        padding-right:14px;
    }
}

@media(pointer:coarse){
    button,
    input{
        min-height:44px;
    }

    .nav{
        min-height:48px;
    }
}

@media(prefers-reduced-motion:reduce){
    *,
    *::before,
    *::after{
        scroll-behavior:auto!important;
        transition:none!important;
    }
}
</style>
</head>

<body>

<div class="app">

<header class="topbar">
<div class="topbar-inner">

<button class="logo" onclick="goHome()" aria-label="NPCBook Home">
    <div class="logo-icon">📱</div>
    <div>
        <div class="logo-text">NPCBook</div>
        <div class="logo-sub">SOCIAL MEDIA FOR NPCs</div>
    </div>
</button>

<div class="search">
    <span class="search-icon">🔎</span>
    <input
        id="searchInput"
        type="search"
        placeholder="Search NPCs, worlds, posts..."
        autocomplete="off"
        oninput="searchSite(this.value)"
    >
</div>

<div class="top-actions">
    <button class="icon-btn" onclick="showNotifications()" title="Notifications">🔔</button>
    <button class="icon-btn" onclick="showMessages()" title="Messages">💬</button>
    <button class="icon-btn" onclick="newWorld()" title="New world">🌍</button>
    <button class="top-avatar" id="topAvatar" onclick="showMyNPC()">🧑</button>
</div>

</div>
</header>

<div class="layout">

<aside class="sidebar">
<div class="sidebar-card">

<button class="nav active" id="homeNav" onclick="renderHome()">
<span class="nav-icon">🏠</span> Home
</button>

<button class="nav" onclick="showMyNPC()">
<span class="nav-icon">🧑</span> My NPC
</button>

<button class="nav" onclick="showTrending()">
<span class="nav-icon">🔥</span> Trending
</button>

<button class="nav" onclick="showNotifications()">
<span class="nav-icon">🔔</span> Notifications
</button>

<button class="nav" onclick="showMessages()">
<span class="nav-icon">💬</span> Messages
</button>

<div class="nav-divider"></div>

<div class="nav-title">NPC World</div>

<button class="nav" onclick="showQuests()">
<span class="nav-icon">⚔️</span> Quests
</button>

<button class="nav" onclick="showMarket()">
<span class="nav-icon">🛒</span> NPC Market
</button>

<button class="nav" onclick="newNPC()">
<span class="nav-icon">✨</span> Generate NPC
</button>

<button class="nav" onclick="randomPost()">
<span class="nav-icon">🎲</span> Random Post
</button>

<div class="nav-divider"></div>

<button class="nav" onclick="showSettings()">
<span class="nav-icon">⚙️</span> Settings
</button>

<button class="nav" onclick="newWorld()">
<span class="nav-icon">🌌</span> New World
</button>

</div>
</aside>

<main id="main"></main>

<aside class="right-sidebar">
<div id="right"></div>
</aside>

</div>

<nav class="mobile-nav">
<button id="mobileHome" class="active" onclick="renderHome()">
<span>🏠</span>
<span>Home</span>
</button>

<button onclick="showTrending()">
<span>🔥</span>
<span>Trends</span>
</button>

<button onclick="showMyNPC()">
<span>🧑</span>
<span>NPC</span>
</button>

<button onclick="showQuests()">
<span>⚔️</span>
<span>Quests</span>
</button>

<button onclick="newWorld()">
<span>🌍</span>
<span>New</span>
</button>
</nav>

<div class="modal-layer" id="modalLayer" onclick="modalOutside(event)">
<div class="modal" id="modal"></div>
</div>

<div class="toast" id="toast"></div>

</div>

<script>

/* ============================================================
   RANDOM ENGINE
   ============================================================

   crypto.getRandomValues() is used instead of Math.random()
   so every page refresh receives a fresh high-quality random
   sequence.

   No LocalStorage.
   No SessionStorage.
   No cookies.
   No database.
   ============================================================ */

function randomUint(){
    const a=new Uint32Array(1);
    crypto.getRandomValues(a);
    return a[0];
}

function rand(max){
    if(max<=0) return 0;
    return randomUint()%max;
}

function pick(arr){
    return arr[rand(arr.length)];
}

function chance(percent){
    return rand(100)<percent;
}

function shuffle(arr){
    const a=[...arr];
    for(let i=a.length-1;i>0;i--){
        const j=rand(i+1);
        [a[i],a[j]]=[a[j],a[i]];
    }
    return a;
}

function clamp(n,min,max){
    return Math.max(min,Math.min(max,n));
}

function escapeHTML(value){
    return String(value)
        .replaceAll("&","&amp;")
        .replaceAll("<","&lt;")
        .replaceAll(">","&gt;")
        .replaceAll('"',"&quot;")
        .replaceAll("'","&#039;");
}

function slug(value){
    return String(value)
        .toLowerCase()
        .replace(/[^a-z0-9]+/g,"")
        .slice(0,18);
}

/* ============================================================
   GLOBAL DATA
   ============================================================ */

const COUNTRIES=[
["India","🇮🇳",["Delhi","Mumbai","Bengaluru","Hyderabad","Jaipur","Hansi","Pune","Kolkata","Chennai"],["Aarav","Vihaan","Arjun","Rohan","Kabir","Aditya","Ishaan","Dev","Kunal","Rahul","Nikhil","Manav","Ananya","Aanya","Diya","Meera","Riya","Kavya","Nisha","Pooja"],["Sharma","Kumar","Singh","Verma","Gupta","Malik","Mehta","Patel","Kapoor","Bansal","Yadav","Joshi","Saini","Chawla","Agarwal"]],
["Japan","🇯🇵",["Tokyo","Osaka","Kyoto","Sapporo","Yokohama","Nagoya"],["Haruto","Ren","Yuki","Sota","Kaito","Daiki","Hiroto","Takumi","Aoi","Hana","Yuna","Mio","Sakura","Rin","Akari"],["Sato","Suzuki","Takahashi","Tanaka","Watanabe","Ito","Yamamoto","Nakamura","Kobayashi","Kato"]],
["South Korea","🇰🇷",["Seoul","Busan","Incheon","Daegu","Daejeon","Gwangju"],["Min-jun","Seo-jun","Ji-ho","Hyun-woo","Joon","Do-yun","Ji-min","Seo-yeon","Ha-eun","Soo-jin","Min-seo","Ye-jun"],["Kim","Lee","Park","Choi","Jung","Kang","Cho","Yoon","Jang","Han"]],
["United States","🇺🇸",["New York","Los Angeles","Chicago","Seattle","Boston","Austin","Denver","Portland"],["Liam","Noah","Ethan","Mason","Logan","James","Lucas","Oliver","Emma","Olivia","Ava","Mia","Chloe","Lily","Grace"],["Smith","Johnson","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson","Thomas","Jackson","White"]],
["United Kingdom","🇬🇧",["London","Manchester","Liverpool","Bristol","Leeds","Edinburgh","Glasgow"],["Oliver","George","Harry","Jack","Arthur","Charlie","Henry","Oscar","Amelia","Isla","Emily","Sophie","Grace","Ella"],["Smith","Jones","Taylor","Brown","Williams","Wilson","Davies","Evans","Thomas","Roberts"]],
["France","🇫🇷",["Paris","Lyon","Marseille","Nice","Toulouse","Bordeaux"],["Louis","Gabriel","Arthur","Hugo","Jules","Lucas","Nathan","Emma","Louise","Chloé","Camille","Léa","Manon"],["Martin","Bernard","Dubois","Thomas","Robert","Richard","Petit","Durand","Leroy","Moreau"]],
["Germany","🇩🇪",["Berlin","Munich","Hamburg","Cologne","Frankfurt","Leipzig"],["Maximilian","Paul","Leon","Felix","Lukas","Jonas","Noah","Anna","Emma","Mia","Lena","Clara","Sophie"],["Müller","Schmidt","Schneider","Fischer","Weber","Meyer","Wagner","Becker","Schulz","Hoffmann"]],
["Brazil","🇧🇷",["São Paulo","Rio de Janeiro","Brasília","Salvador","Curitiba","Recife"],["Miguel","Gabriel","Lucas","Arthur","Pedro","Rafael","Matheus","João","Helena","Alice","Laura","Manuela","Beatriz"],["Silva","Santos","Oliveira","Souza","Pereira","Costa","Rodrigues","Almeida","Nascimento","Lima"]],
["Mexico","🇲🇽",["Mexico City","Guadalajara","Monterrey","Puebla","Cancún","Mérida"],["Santiago","Mateo","Sebastián","Diego","Daniel","Alejandro","Emiliano","Carlos","Sofía","Valentina","Camila","Mariana","Lucía"],["García","Hernández","Martínez","López","González","Pérez","Rodríguez","Sánchez","Ramírez","Torres"]],
["Italy","🇮🇹",["Rome","Milan","Naples","Florence","Turin","Bologna"],["Lorenzo","Matteo","Leonardo","Francesco","Marco","Luca","Alessandro","Andrea","Giulia","Sofia","Aurora","Chiara","Alice"],["Rossi","Russo","Ferrari","Esposito","Bianchi","Romano","Colombo","Ricci","Marino","Greco"]],
["Spain","🇪🇸",["Madrid","Barcelona","Valencia","Seville","Bilbao","Málaga"],["Hugo","Mateo","Martín","Lucas","Leo","Daniel","Alejandro","Pablo","Sofía","Lucía","Martina","Julia","Valeria"],["García","Fernández","González","Rodríguez","López","Martínez","Sánchez","Pérez","Gómez","Martín"]],
["Portugal","🇵🇹",["Lisbon","Porto","Braga","Coimbra","Faro"],["João","Miguel","Tiago","Diogo","Pedro","Rafael","Inês","Beatriz","Mariana","Leonor","Marta"],["Silva","Santos","Ferreira","Pereira","Oliveira","Costa","Rodrigues","Martins","Gomes","Sousa"]],
["Russia","🇷🇺",["Moscow","Saint Petersburg","Kazan","Novosibirsk","Yekaterinburg"],["Alexander","Dmitri","Ivan","Mikhail","Nikolai","Sergei","Alexei","Andrei","Anna","Maria","Sofia","Elena","Daria"],["Ivanov","Petrov","Sidorov","Smirnov","Volkov","Morozov","Popov","Sokolov","Kuznetsov","Orlov"]],
["Poland","🇵🇱",["Warsaw","Kraków","Gdańsk","Wrocław","Poznań"],["Jakub","Antoni","Jan","Kacper","Piotr","Mateusz","Adam","Zofia","Julia","Maja","Hanna","Oliwia"],["Nowak","Kowalski","Wiśniewski","Wójcik","Kowalczyk","Kamiński","Lewandowski","Zieliński","Szymański","Woźniak"]],
["Greece","🇬🇷",["Athens","Thessaloniki","Patras","Heraklion"],["Nikos","Giorgos","Dimitris","Alexandros","Yannis","Kostas","Maria","Eleni","Sofia","Anna"],["Papadopoulos","Pappas","Nikolaidis","Georgiou","Dimitriou","Vasilakis","Ioannidis"]],
["Turkey","🇹🇷",["Istanbul","Ankara","Izmir","Bursa","Antalya"],["Emir","Kerem","Arda","Mert","Yusuf","Ahmet","Can","Ece","Zeynep","Elif","Defne","Derya"],["Yılmaz","Kaya","Demir","Şahin","Çelik","Yıldız","Aydın","Öztürk","Arslan","Doğan"]],
["Egypt","🇪🇬",["Cairo","Alexandria","Giza","Luxor"],["Omar","Ahmed","Youssef","Karim","Mohamed","Hassan","Amir","Mariam","Nour","Salma","Laila","Yasmin"],["Hassan","Ali","Mahmoud","Ibrahim","Abdelrahman","Fahmy","Sayed","Mostafa","Khalil"]],
["Nigeria","🇳🇬",["Lagos","Abuja","Ibadan","Benin City","Kano"],["Chinedu","Emeka","Obinna","Tunde","Femi","Kunle","Daniel","Adaeze","Amaka","Chioma","Blessing","Zainab"],["Okafor","Adeyemi","Okoye","Eze","Balogun","Adebayo","Nwosu","Ibrahim","Olawale"]],
["Kenya","🇰🇪",["Nairobi","Mombasa","Kisumu","Nakuru"],["Brian","Kevin","Daniel","Samuel","David","Ian","Amani","Wanjiku","Njeri","Aisha","Faith","Mercy"],["Otieno","Kamau","Mwangi","Ochieng","Kiptoo","Wanjala","Mutua","Kariuki"]],
["South Africa","🇿🇦",["Johannesburg","Cape Town","Durban","Pretoria"],["Liam","Thabo","Sipho","Kagiso","Daniel","Ethan","Mandla","Ayanda","Zanele","Naledi","Aisha","Lerato"],["Mokoena","Ndlovu","Dlamini","Khumalo","Molefe","Naidoo","Jacobs","Botha"]],
["Canada","🇨🇦",["Toronto","Vancouver","Montreal","Ottawa","Calgary"],["Liam","Noah","Ethan","Benjamin","William","Lucas","Oliver","Emma","Charlotte","Amelia","Maya","Sophie"],["Smith","Brown","Wilson","Martin","Thompson","Anderson","Taylor","Campbell","Clark","Mitchell"]],
["Australia","🇦🇺",["Sydney","Melbourne","Brisbane","Perth","Adelaide"],["Jack","Oliver","Henry","Noah","William","Lachlan","Charlie","Isla","Mia","Charlotte","Ruby","Ella"],["Smith","Jones","Williams","Brown","Wilson","Taylor","Johnson","Martin","Anderson","Walker"]],
["Indonesia","🇮🇩",["Jakarta","Bandung","Surabaya","Yogyakarta","Denpasar"],["Budi","Rizky","Dimas","Andi","Fajar","Aditya","Putra","Sari","Ayu","Dewi","Nadia","Intan"],["Saputra","Pratama","Wijaya","Santoso","Hidayat","Setiawan","Kurniawan"]],
["Philippines","🇵🇭",["Manila","Cebu City","Davao","Quezon City"],["Juan","Miguel","Gabriel","Paolo","Marco","Carlos","Andrei","Maria","Angela","Sofia","Bea","Isabel"],["Santos","Reyes","Cruz","Garcia","Mendoza","Bautista","Navarro","Flores"]],
["Thailand","🇹🇭",["Bangkok","Chiang Mai","Phuket","Pattaya"],["Narin","Krit","Thanawat","Phanupong","Arthit","Kanya","Nok","Pim","Mali","Suda","Nicha"],["Sukhum","Srisuk","Wongsa","Chaiyaporn","Kittisak","Saengsawang"]],
["Vietnam","🇻🇳",["Hanoi","Ho Chi Minh City","Da Nang","Hai Phong"],["Minh","Duc","Huy","Nam","Long","Quang","An","Linh","Mai","Lan","Thao","Trang"],["Nguyen","Tran","Le","Pham","Hoang","Vu","Phan","Bui","Dang","Do"]],
["China","🇨🇳",["Beijing","Shanghai","Shenzhen","Guangzhou","Chengdu","Hangzhou"],["Wei","Jun","Hao","Ming","Chen","Tao","Li","Jing","Mei","Lin","Yue","Xiao"],["Wang","Li","Zhang","Liu","Chen","Yang","Huang","Zhao","Wu","Zhou"]],
["Argentina","🇦🇷",["Buenos Aires","Córdoba","Rosario","Mendoza"],["Mateo","Santiago","Tomás","Nicolás","Lucas","Martín","Juan","Sofía","Valentina","Camila","Lucía"],["García","González","Rodríguez","Fernández","López","Martínez","Pérez","Sánchez"]],
["Colombia","🇨🇴",["Bogotá","Medellín","Cali","Cartagena"],["Santiago","Sebastián","Mateo","Daniel","Alejandro","Nicolás","Valentina","Mariana","Sofía","Isabella"],["García","Rodríguez","Martínez","López","González","Hernández","Pérez","Sánchez"]],
["Chile","🇨🇱",["Santiago","Valparaíso","Concepción","Antofagasta"],["Mateo","Benjamín","Vicente","Tomás","Lucas","Joaquín","Sofía","Martina","Isidora","Emilia"],["González","Muñoz","Rojas","Díaz","Pérez","Soto","Contreras","Silva"]],
["Netherlands","🇳🇱",["Amsterdam","Rotterdam","Utrecht","Eindhoven"],["Daan","Lars","Lucas","Sem","Finn","Milan","Sophie","Emma","Julia","Fleur","Anna"],["De Jong","Jansen","De Vries","Van den Berg","Van Dijk","Bakker","Visser","Smit"]],
["Sweden","🇸🇪",["Stockholm","Gothenburg","Malmö","Uppsala"],["Erik","Oscar","William","Hugo","Liam","Alexander","Elsa","Astrid","Alice","Maja","Sofia"],["Andersson","Johansson","Karlsson","Nilsson","Eriksson","Larsson","Olsson","Persson"]],
["Norway","🇳🇴",["Oslo","Bergen","Trondheim","Stavanger"],["Lars","Erik","Magnus","Oskar","Henrik","Emil","Nora","Ingrid","Emma","Sofie","Maja"],["Hansen","Johansen","Olsen","Larsen","Andersen","Pedersen","Nilsen","Kristiansen"]],
["Finland","🇫🇮",["Helsinki","Espoo","Tampere","Turku"],["Mika","Jussi","Elias","Aino","Emilia","Ella","Veeti","Eero","Sofia"],["Korhonen","Virtanen","Mäkinen","Nieminen","Mäkelä","Hämäläinen"]]
];

/* WORLD DEFINITIONS */

const WORLDS=[
["Game","Fantasy RPG","⚔️",["Ashen Kingdom","Eldoria","The Forgotten Vale","Kingdom of Seven Bells","Moonfall Online"],"#193957","#57396d"],
["Game","Open World","🎮",["Neon Valley","Metro City Online","Grand Horizon","District Nine"],"#173d4d","#653b35"],
["Game","Survival","🏕️",["Dead Pine Island","Frostline","The Last Camp","Red Desert"],"#253d2c","#62482c"],
["Game","MMORPG","🛡️",["RealmNet","Eternal Quest Online","Mythic Frontier","World of Ten Moons"],"#242e57","#54356b"],
["Game","Horror","👻",["Blackwood Manor","Night Shift","The Empty Hospital","Floor 13"],"#17202b","#4d2535"],
["Game","Sci-Fi","🚀",["Orbit-9","Helios Station","Mars Colony 7","The Outer Ring"],"#153649","#34266a"],
["Game","Farming Sim","🌾",["Sunflower Valley","Cozy Acres","Harvest Moonlight","Greenfield"],"#1c4535","#53622b"],
["Game","Detective","🔎",["Rainfall City","Murder on Platform 4","The Crimson District","Noir Harbor"],"#20283b","#4d384e"],
["Game","Soulslike","🔥",["Kingdom of Ash","The Dying Throne","Cathedral of Silence","Gravefire"],"#291c23","#513a27"],
["Game","Dungeon Crawler","🗝️",["The Endless Dungeon","Floor Zero","Cursed Catacombs","Vault of Kings"],"#20253d","#4e3040"],

["Manhwa","Dungeon Hunter","⚡",["Hunter Association","Gate City","Ranker World","Dungeon Seoul"],"#172c4d","#44316c"],
["Manhwa","Regression","⏳",["Second Life Timeline","The Returned Hero","Regression Academy"],"#23334d","#5d3155"],
["Manhwa","Tower","🏯",["Tower of Trials","The 100th Floor","Tower of Endless Skills"],"#1d3044","#49336c"],
["Manhwa","Murim","🥋",["Murim Alliance","Heavenly Sect","Nine Mountain Province","Jade Valley"],"#203b36","#5a432c"],
["Manhwa","Academy","🎓",["Magic Academy","Hunter Academy","Royal Academy","Villain Academy"],"#273b58","#513b68"],
["Manhwa","Romance Fantasy","🌹",["Duchy of Roses","The Villainess Estate","Empire of Moonlight"],"#4b263d","#4e3564"],
["Manhwa","Villainess","👑",["Royal Court","The Duke's Estate","Empire of Seven Crowns"],"#432640","#473764"],

["Book","Fantasy Novel","📖",["The Kingdom Beyond Winter","The Crown of Ravens","The Last Wizard","The Silver Forest"],"#233c4c","#59376a"],
["Book","Detective Novel","🕵️",["Black Rain London","The Glass Room","Harbor Street Mysteries","The Clockmaker Case"],"#222d3e","#51414b"],
["Book","Dystopian Novel","🏙️",["Sector Nine","The Quiet City","Ministry District","The Last Census"],"#202b38","#53363d"],
["Book","Romance Novel","💌",["Riverside Apartments","Autumn in Paris","The Bookshop Upstairs"],"#492d42","#473963"],
["Book","Historical Fiction","🏰",["The Merchant's Road","Winter Court","The Old Kingdom","Letters from 1897"],"#493b2b","#51402e"],
["Book","Cosmic Horror","🌌",["The Lighthouse Beyond Time","The Black Ocean","The Observatory"],"#111c30","#352c5a"],

["Real World","Ordinary Life","☕",["Earth — Today","Downtown","Neighborhood Life","Office District"],"#273746","#42504a"],
["Real World","Retail","🛍️",["Local Mall","Corner Shop","Supermarket","Night Market"],"#26384b","#51422e"],
["Real World","Office","💼",["Corporate Tower","Open Office","Government Office","Startup Floor"],"#1e3346","#443e58"],
["Real World","Transport","🚌",["City Bus Network","Metro System","Airport Terminal","Railway Station"],"#183c4a","#51412e"],
["Real World","School","🏫",["Public School","University Campus","Night College","Training Institute"],"#223b4a","#493c5d"],
["Real World","Hospital","🏥",["City Hospital","Emergency Department","Community Clinic"],"#183b43","#433d58"],
["Real World","Food Service","🍜",["Neighborhood Café","Restaurant District","Food Court","Late-Night Diner"],"#493624","#513048"],
["Real World","Delivery","📦",["Delivery Network","City Logistics","Courier District"],"#243c4a","#58412e"]
];

const JOBS=[
"shopkeeper","librarian","barista","teacher","mechanic","receptionist",
"security guard","delivery rider","taxi driver","train worker",
"bus conductor","office clerk","chef","cook","bookshop assistant",
"museum guide","pharmacist","research assistant","software developer",
"game tester","street vendor","market seller","fisherman","farmer",
"blacksmith","armorer","potion seller","innkeeper","stable worker",
"guild clerk","healer","quest clerk","guard","messenger","cartographer",
"gatekeeper","dungeon clerk","academy instructor","hunter guild receptionist",
"magic librarian","royal messenger","village elder","castle servant",
"tavern worker","airship mechanic","space station technician",
"robot maintenance worker","ship navigator","station engineer",
"wand shop assistant","dragon stable keeper","monster researcher",
"adventurer support staff"
];

const PERSONALITIES=[
"deadpan observer","overworked professional","accidentally philosophical",
"optimistic disaster","professional complainer","quiet overthinker",
"chaotic helpful person","suspiciously calm","retired adventurer",
"unwilling hero","background-character enthusiast","serial people-watcher",
"dramatic introvert","local gossip expert","underpaid employee",
"perpetually confused","rule follower","rule breaker","secret softie",
"sarcastic realist","hopeful pessimist","tired veteran",
"accidental celebrity","professional side character","amateur detective",
"extremely literal person","quiet menace","friendly cynic",
"reluctant mentor","NPC union supporter","barrel enthusiast",
"quest-object specialist","background merchant","door guardian",
"map reader","healer with boundaries","shopkeeper philosopher",
"retired chosen-one","professional witness","unpaid quest giver",
"confused local"
];

const SITUATIONS=[
"a legendary hero returned after disappearing for three months",
"a stranger asked the same question for the 847th time",
"someone walked into the building and ignored every sign",
"the most important person in the world forgot the password",
"a customer tried to pay with something that definitely was not money",
"a mysterious package arrived with no sender",
"the local boss announced a completely unnecessary meeting",
"someone defeated a terrifying enemy and then got stuck on a wooden fence",
"a stranger asked for directions while standing directly beside the destination",
"the chosen one bought the cheapest item in the shop and somehow received a legendary item",
"someone activated a quest nobody remembered creating",
"a suspiciously powerful person ordered the cheapest meal on the menu",
"the entire town stopped working because one person moved a chair",
"a famous adventurer returned just to complain about prices",
"someone asked for a discount after destroying half the shop",
"the royal messenger arrived with news that could have been sent as a text",
"the hero saved everyone and immediately stole someone's transportation",
"a dungeon party forgot to bring food",
"a stranger tried to sell an obviously cursed object",
"the person who caused the problem returned to ask who caused the problem",
"someone defeated the final boss before finishing the tutorial",
"a customer asked whether the obvious door was actually a door",
"the local celebrity entered and nobody recognized them",
"someone asked for a map and then used it upside down",
"a meeting that should have taken five minutes lasted three hours",
"someone brought a dragon into a place with a no-pets policy",
"a mysterious notification appeared on everyone's screen",
"someone claimed they had never been here despite having a loyalty card",
"the village held a festival because nobody could think of a better excuse",
"the office printer became the most powerful entity in the building",
"someone arrived late and somehow blamed time itself",
"the guild introduced a new form that requires another new form",
"a stranger asked whether I was an important NPC",
"the local villain opened a small business",
"a legendary weapon was left at the lost-and-found",
"someone defeated a monster using an item meant for cooking",
"a person with endgame equipment asked where the bathroom was",
"the town's biggest secret turned out to be extremely boring",
"someone skipped the entire story and somehow reached the ending",
"a customer returned the same item for the fourth time",
"a stranger started narrating their own actions out loud",
"the boss announced that everyone should be more passionate about unpaid overtime",
"someone asked for emotional support from a vending machine",
"the map showed a location nobody could remember",
"the quest reward was less valuable than the receipt",
"someone opened a forbidden door because it said DO NOT OPEN",
"a legendary prophecy was printed with a spelling mistake",
"the neighborhood gained a mysterious new resident",
"someone started a rumor and then believed it themselves",
"the system assigned me a quest I absolutely did not agree to",
"a person walked past the obvious solution three times",
"someone bought an item specifically because the description said it was useless",
"a powerful stranger asked for directions to the nearest toilet",
"the final boss had better customer service than the town",
"someone tried to negotiate with a locked door",
"the entire party forgot the healer again",
"a mysterious stranger offered me exactly one coin for my entire shop",
"someone discovered that the ancient artifact was basically a kitchen utensil",
"the town guard asked if I had seen anything suspicious while standing beside the suspicious thing",
"someone started a side quest in the middle of another side quest",
"a person arrived carrying seventeen identical potions",
"the legendary hero spent thirty minutes deciding what snack to buy",
"the royal family opened a public complaint form",
"someone defeated the monster and then asked whether there was a receipt",
"the dungeon elevator stopped between floors",
"a customer wanted to speak to the manager of the dungeon",
"someone discovered a secret passage that led directly to the storage room",
"the supposedly immortal wizard forgot their own birthday",
"a stranger asked me to identify an object they were already holding",
"someone turned a serious emergency into a group chat argument",
"the city announced a new rule nobody understood",
"a famous character walked past me without triggering my dialogue",
"someone tried to speedrun a conversation",
"the most dangerous creature in the region turned out to be allergic to cheese",
"the village ran out of chairs",
"someone demanded a refund for an experience they survived",
"the protagonist returned after five minutes and acted like ten years had passed",
"someone asked if the background music was coming from my house",
"the local authority created a committee to investigate why committees exist",
"a stranger asked me where the nearest save point was",
"someone bought a cursed sword because it matched their outfit",
"the town's most important event was interrupted by a delivery driver",
"a mysterious character appeared and disappeared before anyone learned their name",
"someone tried to barter using three potatoes and a mysterious crystal",
"the adventurer party had a meeting about having too many meetings",
"someone asked whether my dialogue changes after sunset",
"a monster wandered into town and apologized for being early",
"the hero returned the quest item without completing the quest",
"someone asked for a secret entrance while standing at the secret entrance",
"the world-saving mission was delayed because somebody lost their keys",
"a new employee received absolutely no training",
"someone asked me to hold their extremely suspicious bag",
"the local café became the unofficial headquarters for a rebellion",
"someone tried to fight the tutorial boss at level one",
"the castle announced new opening hours",
"a customer complained that the dungeon was too dark",
"someone discovered that the ancient scroll was just a grocery list",
"the person everyone feared turned out to be terrible at small talk",
"the office held a team-building exercise nobody wanted",
"someone asked if I knew the protagonist personally",
"a quest marker appeared above the wrong person",
"the city installed a statue of someone who was still alive",
"someone came into the shop solely to ask what year it was",
"a stranger offered a suspiciously generous tip",
"the guild changed its logo for the sixth time",
"someone accidentally became the mayor",
"a customer tried to return a potion because it worked too well",
"the final dungeon was closed for maintenance",
"someone brought a horse onto public transport",
"a mysterious notification said 'You have been selected'",
"the protagonist asked me for lore I was never programmed to know",
"someone opened a shop directly opposite mine and copied everything",
"the village discovered social media",
"a famous warrior posted an embarrassing selfie",
"the monster raid was cancelled because of bad weather",
"someone arrived at the airport with a sword",
"the train announcement contradicted the timetable",
"the librarian discovered a book that described today's events",
"someone asked why every important conversation happens beside the same fountain",
"a customer bought one apple and asked for a loyalty reward",
"the hero spent their entire reward on cosmetic items",
"someone accidentally leaked the villain's grocery list",
"the dungeon boss filed a workplace complaint",
"a town meeting became a debate about snacks",
"someone tried to bribe the guard with a coupon",
"the mysterious prophecy predicted something extremely ordinary",
"someone asked if this was the real world",
"the server apparently had another update",
"someone discovered that the legendary sword has a warranty",
"the hero returned because they forgot to loot one barrel",
"the local newspaper printed yesterday's news again",
"a stranger asked where the nearest checkpoint was",
"the kingdom launched a customer satisfaction survey",
"someone attempted to negotiate with an automated voice",
"the town's most feared assassin became a part-time baker",
"the villain complained about the cost of rent",
"a mysterious portal opened in the staff room",
"someone requested a quest reward in cash",
"the royal accountant discovered missing coins",
"the hero asked if the castle had Wi-Fi",
"a suspiciously familiar person appeared in town again",
"someone asked whether respawning was covered by insurance"
];

const OBJECTS=[
"a rusty key","a suspicious potion","a wooden spoon","a legendary sword",
"a bus ticket","a library card","a mysterious crystal","three stale sandwiches",
"an ancient map","a broken compass","a glowing receipt","a cursed umbrella",
"a golden coin","a quest scroll","a tiny dragon","a supermarket loyalty card",
"a suspiciously expensive hat","a box marked IMPORTANT","an empty treasure chest",
"a completely normal chair","a magic calculator","a talking vending machine",
"a broken save point","a government form","a mysterious USB drive",
"a cookbook","a fake treasure map","a badly translated prophecy",
"a backpack full of rocks","a helmet with someone's name written inside"
];

const ACTIVITIES=[
"standing beside the same doorway",
"restocking the same shelf",
"waiting for the next quest",
"pretending to understand the instructions",
"repairing something that was already broken",
"watching adventurers make terrible decisions",
"counting inventory",
"answering the same question",
"waiting for my shift to end",
"explaining the obvious",
"cleaning up after heroes",
"checking the timetable",
"making coffee",
"filing paperwork",
"reading the local newspaper",
"watching the rain",
"feeding the local animals",
"waiting for a customer",
"trying to finish lunch",
"avoiding another meeting",
"updating the quest board",
"organizing the library",
"fixing the elevator",
"guarding a completely ordinary door",
"checking whether the mysterious noise is actually mysterious"
];

const EMOTIONS=[
"mildly concerned","deeply tired","strangely proud",
"professionally disappointed","confused but committed",
"emotionally unavailable","surprisingly optimistic",
"one inconvenience away from retirement","calm enough to be suspicious",
"personally offended","quietly impressed","too tired to investigate",
"philosophically exhausted","delighted for reasons I cannot explain",
"just happy to be included"
];

const ENDINGS=[
"Anyway, my shift ends in six hours.",
"Nobody warned me this would be part of the job.",
"I have questions. Management has forms.",
"At least the barrel is still here.",
"I am choosing to believe this is normal.",
"Tomorrow I will probably do the exact same thing.",
"The hero thanked me. I will be framing that moment.",
"I asked for a quiet life. The universe laughed.",
"Somehow I am now involved.",
"I have decided not to ask follow-up questions.",
"This is apparently above my pay grade.",
"I miss when my biggest problem was inventory.",
"The quest continues. My patience does not.",
"Nobody got hurt, so technically this was a success.",
"I wish I were joking.",
"The system has no explanation and neither do I.",
"I have seen stranger things, but not many.",
"Tomorrow's problem can be tomorrow's problem.",
"I am beginning to suspect the protagonist is the problem.",
"Please send help. Or snacks.",
"There is definitely a form for this.",
"I have been told this is character development.",
"I am not emotionally prepared for another update.",
"At this point I just work here."
];

const COMMENTS=[
"Honestly, same.",
"This is the most NPC thing I've ever read.",
"Wait. That happened to me too.",
"I thought I was the only one.",
"Management will pretend this never happened.",
"Please tell me there is a sequel.",
"Why is this weirdly relatable?",
"Classic protagonist behavior.",
"That sounds like a side quest.",
"I need context immediately.",
"At least you got paid.",
"You are definitely not getting paid enough.",
"The system has spoken.",
"Have you tried turning it off and on again?",
"I would simply go home.",
"That escalated quickly.",
"This world needs better documentation.",
"I blame the tutorial.",
"Absolutely legendary.",
"Saving this for later.",
"Someone needs to investigate.",
"NPCBook was not ready for this.",
"I have questions.",
"Same energy as my workplace."
];

/* ============================================================
   STATE
   ============================================================ */

const STATE={
    npcs:[],
    posts:[],
    currentNPC:null,
    viewedTab:"posts",
    generatedAt:Date.now(),
    usedPosts:new Set(),
    usedProfiles:new Set(),
    followed:new Set(),
    liked:new Set(),
    saved:new Set()
};

/* ============================================================
   ID
   ============================================================ */

function id(prefix){
    return prefix+"_"+Date.now().toString(36)+"_"+randomUint().toString(36);
}

/* ============================================================
   NAME GENERATION
   ============================================================ */

function createName(){
    const c=pick(COUNTRIES);

    let first=pick(c[3]);
    let last=pick(c[4]);
    let name=first+" "+last;

    return {
        country:c[0],
        flag:c[1],
        city:pick(c[2]),
        name:name
    };
}

/* ============================================================
   WORLD GENERATION
   ============================================================ */

function createWorld(){
    const w=pick(WORLDS);

    return {
        type:w[0],
        genre:w[1],
        icon:w[2],
        world:pick(w[3]),
        a:w[4],
        b:w[5]
    };
}

/* ============================================================
   HANDLES
   ============================================================ */

function createHandle(name){
    const clean=slug(name.replace(/\s+/g,""));
    const suffix=pick([
        "npc",
        "official",
        "local",
        "main",
        "real",
        "here",
        "daily",
        "online",
        "world",
        "42",
        "404",
        "77",
        "001"
    ]);

    return "@"+clean+"_"+suffix+rand(999);
}

/* ============================================================
   BIO GENERATION
   ============================================================ */

function createBio(npc){
    const templates=[
        `${npc.job}. ${npc.personality}. Apparently important to the plot.`,
        `${npc.country} • ${npc.city} • ${npc.world}. I was told this was a normal life.`,
        `${npc.job} by profession, background character by destiny.`,
        `Just trying to survive ${npc.world} one completely unnecessary event at a time.`,
        `${npc.personality}. Usually found ${pick(ACTIVITIES)}.`,
        `Local ${npc.job}. Professional witness to other people's decisions.`,
        `I work here. I know things. Most of them are unfortunately classified.`,
        `No prophecy. No destiny. Just ${npc.job}.`,
        `Trying to finish my shift before another protagonist arrives.`,
        `Apparently my dialogue is important enough to screenshot.`
    ];

    return pick(templates);
}

/* ============================================================
   NPC GENERATION
   ============================================================ */

function createNPC(){
    let npc=null;

    for(let attempt=0;attempt<100;attempt++){
        const person=createName();
        const world=createWorld();
        const job=pick(JOBS);
        const personality=pick(PERSONALITIES);

        const profileKey=[
            person.name,
            person.country,
            person.city,
            world.world,
            world.genre,
            job
        ].join("|");

        if(STATE.usedProfiles.has(profileKey)) continue;

        STATE.usedProfiles.add(profileKey);

        npc={
            id:id("npc"),
            name:person.name,
            handle:createHandle(person.name),
            country:person.country,
            flag:person.flag,
            city:person.city,
            world:world.world,
            genre:world.genre,
            worldType:world.type,
            icon:world.icon,
            colorA:world.a,
            colorB:world.b,
            job:job,
            personality:personality,
            level:rand(80)+1,
            followers:rand(850000)+500,
            following:rand(2500)+30,
            verified:chance(12),
            online:chance(65),
            bio:"",
            posts:[]
        };

        npc.bio=createBio(npc);

        return npc;
    }

    return null;
}

/* ============================================================
   POST TEXT ENGINE
   ============================================================ */

function cleanText(text){
    return text
        .replace(/\s+/g," ")
        .replace(/\s([,.!?])/g,"$1")
        .trim();
}

function postTemplate(npc){
    const situation=pick(SITUATIONS);
    const emotion=pick(EMOTIONS);
    const ending=pick(ENDINGS);
    const object=pick(OBJECTS);
    const activity=pick(ACTIVITIES);

    const templates=[
        `Today ${situation}. I was ${activity}. Naturally, nobody thought to ask me first. I am ${emotion}. ${ending}`,

        `NPC update: ${situation}.\n\nMeanwhile, I am still ${activity}. The important part is that I still have ${object}. ${ending}`,

        `I need everyone to understand something: ${situation}.\n\nI have been ${activity} all day, and somehow this became my problem. ${ending}`,

        `POV: you are a ${npc.job} in ${npc.world}.\n\n${situation}. My official response is: absolutely not.\n\nMy unofficial response is: ${ending}`,

        `Nobody:\nAbsolutely nobody:\n\nThe universe: ${situation}.\n\nMe, a ${npc.job}: ${emotion}.\n${ending}`,

        `I was ${activity} when ${situation}.\n\nThere are moments when you realize your life has become a side quest. This was one of them. ${ending}`,

        `Breaking news from ${npc.city}: ${situation}.\n\nI would like to remind everyone that I am merely a ${npc.job}. Please stop assigning me legendary responsibilities. ${ending}`,

        `Daily report:\n• World: ${npc.world}\n• Job: ${npc.job}\n• Current activity: ${activity}\n• Current situation: ${situation}\n• Emotional state: ${emotion}\n• Survival status: questionable\n\n${ending}`,

        `Someone please explain why ${situation}.\n\nI was having a perfectly normal day until five minutes ago. Now I am ${emotion} and holding ${object}. ${ending}`,

        `There are three things I know for certain:\n1. I am a ${npc.job}.\n2. I was ${activity}.\n3. ${situation}.\n\nEverything after that is above my pay grade. ${ending}`,

        `I have worked here long enough to recognize trouble.\n\nUnfortunately, ${situation}.\n\nI recognized it immediately.\nI still couldn't stop it.\n\n${ending}`,

        `Someone asked what happened today.\n\nI said: "${cleanText(situation)}."\n\nThey laughed.\n\nI wish they understood that I was being completely serious. ${ending}`,

        `Status update from a completely ordinary ${npc.job}:\n\n${situation}.\n\nNo, this is not a joke.\nYes, I am ${emotion}.\nNo, management has not replied. ${ending}`,

        `I thought today would be boring.\n\nThat was my first mistake.\n\n${situation}.\n\nNow everyone is pretending this was part of the plan. ${ending}`,

        `The protagonist walked in.\n\nI knew something terrible was about to happen because ${situation}.\n\nI am ${emotion}.\n\nI miss yesterday. ${ending}`,

        `I am beginning to suspect that my entire career exists to witness ${situation}.\n\nAnyway, back to ${activity}. ${ending}`,

        `Today's achievement unlocked:\n🏆 "${pick([
            "Survived another protagonist",
            "Answered the same question again",
            "Did not open the suspicious door",
            "Finished my shift",
            "Found the missing quest item",
            "Avoided becoming a boss fight",
            "Successfully ignored the prophecy",
            "Kept the shop standing"
        ])}"\n\nDifficulty: ${pick(["Normal","Hard","Nightmare","Why Is This My Job?"])}.\n\n${ending}`,

        `I don't want to alarm anyone, but ${situation}.\n\nThe last time this happened, someone blamed the ${pick(["wizard","manager","hero","intern","tutorial","weather","server","prophecy"])}.\n\nI am preparing to be blamed again. ${ending}`,

        `Confession:\n\nI have been ${activity} for so long that ${situation} somehow feels like a reasonable interruption.\n\nThat sentence concerns me. ${ending}`,

        `If anyone needs me, I will be ${activity} and pretending ${situation} is not happening.\n\nPlease do not involve me in the main storyline. ${ending}`
    ];

    return cleanText(pick(templates));
}

/* ============================================================
   UNIQUE POST GENERATION
   ============================================================ */

function createUniquePost(npc){
    for(let attempt=0;attempt<150;attempt++){

        const text=postTemplate(npc);

        /*
          Exact normalized fingerprint.
          This prevents the same post text from being created twice
          in the current temporary world.
        */
        const fingerprint=text
            .toLowerCase()
            .replace(/[^a-z0-9]+/g," ")
            .trim();

        const key=fingerprint;

        if(STATE.usedPosts.has(key)){
            continue;
        }

        STATE.usedPosts.add(key);

        const world={
            type:npc.worldType,
            genre:npc.genre,
            name:npc.world,
            icon:npc.icon,
            a:npc.colorA,
            b:npc.colorB
        };

        const now=Date.now();

        const post={
            id:id("post"),
            authorId:npc.id,
            text:text,
            timestamp:new Date(
                now-rand(1000*60*60*72)
            ),
            likes:rand(250000)+3,
            comments:rand(25000),
            shares:rand(12000),
            views:rand(300000)+100,
            world:world,
            tag:npc.genre,
            liked:false,
            saved:false,
            commentsList:[]
        };

        if(chance(42)){
            post.commentsList.push({
                name:pick(COMMENTS).split(" ").slice(0,2).join(" "),
                text:pick(COMMENTS)
            });
        }

        if(chance(22)){
            post.commentsList.push({
                name:pick(COMMENTS).split(" ").slice(0,2).join(" "),
                text:pick(COMMENTS)
            });
        }

        npc.posts.push(post);
        STATE.posts.push(post);

        return post;
    }

    return null;
}

/* ============================================================
   GENERATE WORLD
   ============================================================ */

function generateWorld(){
    STATE.npcs=[];
    STATE.posts=[];
    STATE.currentNPC=null;
    STATE.usedPosts=new Set();
    STATE.usedProfiles=new Set();
    STATE.followed=new Set();
    STATE.liked=new Set();
    STATE.saved=new Set();
    STATE.generatedAt=Date.now();

    /*
      24 NPCs per world.
      Each receives 3–5 unique posts.
      Approximately 80–120 posts per refresh.
    */

    for(let i=0;i<24;i++){
        const npc=createNPC();

        if(!npc) continue;

        STATE.npcs.push(npc);

        const count=3+rand(3);

        for(let p=0;p<count;p++){
            createUniquePost(npc);
        }
    }

    /*
      Extra global posts until we have a healthy feed.
    */
    while(STATE.posts.length<90){
        const npc=pick(STATE.npcs);
        if(!npc) break;
        createUniquePost(npc);
    }

    STATE.posts=shuffle(STATE.posts);

    STATE.currentNPC=STATE.npcs[0];

    document.getElementById("topAvatar").textContent=
        STATE.currentNPC ? STATE.currentNPC.icon : "🧑";
}

/* ============================================================
   TIME
   ============================================================ */

function timeAgo(date){
    const diff=Math.max(0,Date.now()-date.getTime());

    const sec=Math.floor(diff/1000);
    if(sec<60) return sec+"s";

    const min=Math.floor(sec/60);
    if(min<60) return min+"m";

    const hrs=Math.floor(min/60);
    if(hrs<24) return hrs+"h";

    const days=Math.floor(hrs/24);
    return days+"d";
}

/* ============================================================
   NUMBER FORMAT
   ============================================================ */

function number(n){
    if(n>=1000000){
        return (n/1000000).toFixed(n>=10000000?0:1)+"M";
    }

    if(n>=1000){
        return (n/1000).toFixed(n>=10000?0:1)+"K";
    }

    return String(n);
}

/* ============================================================
   POST HTML
   ============================================================ */

function postHTML(post){
    const npc=STATE.npcs.find(n=>n.id===post.authorId);

    if(!npc) return "";

    const liked=STATE.liked.has(post.id);
    const saved=STATE.saved.has(post.id);

    return `
    <article class="post" id="${post.id}">

        <div class="post-header">

            <button class="avatar author"
                onclick="openProfile('${npc.id}')"
                aria-label="Open ${escapeHTML(npc.name)} profile">
                ${npc.icon}
            </button>

            <div class="post-author">

                <button class="author" onclick="openProfile('${npc.id}')">
                    <div class="author-name">
                        <span class="author-name-text">
                            ${escapeHTML(npc.name)}
                        </span>

                        ${npc.verified
                            ? `<span class="verify">✓</span>`
                            : ""}
                    </div>

                    <div class="handle">
                        ${escapeHTML(npc.handle)}
                        · ${escapeHTML(npc.country)}
                    </div>
                </button>

            </div>

            <div class="time">${timeAgo(post.timestamp)}</div>

            <button class="more" onclick="postMenu('${post.id}')">•••</button>

        </div>

        <div class="post-text">${escapeHTML(post.text)}</div>

        <div class="tags">
            <span class="tag world">
                ${escapeHTML(post.world.icon)}
                ${escapeHTML(post.world.name)}
            </span>

            <span class="tag">
                ${escapeHTML(post.tag)}
            </span>

            <span class="tag">
                ${escapeHTML(npc.job)}
            </span>
        </div>

        <div
            class="scene"
            style="--a:${post.world.a};--b:${post.world.b}"
        >
            <div class="scene-inner">
                <div class="scene-icon">${post.world.icon}</div>
                <div class="scene-title">
                    ${escapeHTML(post.world.name)}
                </div>
                <div class="scene-sub">
                    ${escapeHTML(post.world.type)}
                    · POV of ${escapeHTML(npc.name)}
                </div>
            </div>
        </div>

        <div class="post-stats">
            <span>❤️ ${number(post.likes)}</span>
            <span>
                ${number(post.comments)} comments
                · ${number(post.shares)} shares
            </span>
        </div>

        <div class="actions">

            <button
                class="action ${liked?"liked":""}"
                onclick="toggleLike('${post.id}')"
            >
                ❤️ <span class="label">${liked?"Liked":"Like"}</span>
            </button>

            <button
                class="action"
                onclick="openComments('${post.id}')"
            >
                💬 <span class="label">Comment</span>
            </button>

            <button
                class="action"
                onclick="sharePost('${post.id}')"
            >
                ↗️ <span class="label">Share</span>
            </button>

            <button
                class="action ${saved?"saved":""}"
                onclick="toggleSave('${post.id}')"
            >
                🔖 <span class="label">${saved?"Saved":"Save"}</span>
            </button>

        </div>

        ${
            post.commentsList.length
            ?
            `<div class="comments">
                ${post.commentsList.slice(0,2).map(c=>`
                    <div class="comment">
                        <b>${escapeHTML(c.name)}</b>
                        ${escapeHTML(c.text)}
                    </div>
                `).join("")}
            </div>`
            :""
        }

    </article>
    `;
}

/* ============================================================
   RIGHT SIDEBAR
   ============================================================ */

function renderRight(){
    const trends=[
        ["#NPCProblems","48.2K posts"],
        ["#MainCharacterEnergy","37.8K posts"],
        ["#QuestFailed","29.4K posts"],
        ["#BackgroundCharacter","21.9K posts"],
        ["#DungeonLife","18.7K posts"],
        ["#OfficeNPC","14.3K posts"]
    ];

    const users=shuffle(STATE.npcs).slice(0,4);

    document.getElementById("right").innerHTML=`

    <div class="side-card">

        <h3>🔥 Trending in NPCWorld</h3>

        ${trends.map((t,i)=>`
            <div class="trend">
                <small>Trending #${i+1}</small>
                <b>${t[0]}</b>
                <small>${t[1]}</small>
            </div>
        `).join("")}

    </div>

    <div class="side-card">

        <h3>👥 NPCs you may know</h3>

        ${users.map(n=>`
            <div class="mini-user">

                <button
                    class="avatar"
                    onclick="openProfile('${n.id}')"
                >
                    ${n.icon}
                </button>

                <div class="mini-info">
                    <div class="mini-name">
                        ${escapeHTML(n.name)}
                    </div>

                    <div class="mini-handle">
                        ${escapeHTML(n.handle)}
                    </div>
                </div>

                <button
                    class="follow"
                    onclick="toggleFollow('${n.id}',this)"
                >
                    ${STATE.followed.has(n.id)?"Following":"Follow"}
                </button>

            </div>
        `).join("")}

    </div>

    <div class="side-card">

        <h3>🌍 Current World</h3>

        <div class="notice">
            ${STATE.npcs.length} NPCs generated.
            ${STATE.posts.length} unique posts generated.
            <br><br>
            Refresh the page to create a completely new temporary world.
        </div>

        <button class="btn primary" style="width:100%" onclick="newWorld()">
            🌌 Generate New World
        </button>

    </div>

    `;
}

/* ============================================================
   HOME
   ============================================================ */

function renderHome(){
    setNav("home");

    const posts=shuffle([...STATE.posts]);

    document.getElementById("main").innerHTML=`

    <div class="heading">
        <div>
            <h1>Home</h1>
            <p>
                ${STATE.npcs.length} NPCs ·
                ${STATE.posts.length} unique posts ·
                fresh world
            </p>
        </div>

        <button class="btn secondary" onclick="newWorld()">
            🌍 New World
        </button>
    </div>

    <div class="composer">

        <div class="composer-row">

            <button
                class="avatar"
                onclick="showMyNPC()"
            >
                ${STATE.currentNPC?.icon||"🧑"}
            </button>

            <input
                placeholder="What's happening in the NPC world?"
                readonly
                onclick="newNPC()"
            >

        </div>

        <div class="composer-tools">
            <button class="chip" onclick="newNPC()">✨ Generate NPC</button>
            <button class="chip" onclick="randomPost()">🎲 Random post</button>
            <button class="chip" onclick="showQuests()">⚔️ Quests</button>
            <button class="chip" onclick="showTrending()">🔥 Trends</button>
        </div>

    </div>

    <div id="feed">
        ${posts.map(postHTML).join("")}
    </div>
    `;

    renderRight();
    window.scrollTo({top:0,behavior:"smooth"});
}

/* ============================================================
   PROFILE
   ============================================================ */

function openProfile(npcId){
    const npc=STATE.npcs.find(n=>n.id===npcId);

    if(!npc) return;

    STATE.currentNPC=npc;

    const posts=npc.posts;

    document.getElementById("main").innerHTML=`

    <div class="back">
        <button class="btn secondary" onclick="renderHome()">
            ← Back to Home
        </button>
    </div>

    <div class="profile-cover"
        style="--a:${npc.colorA};--b:${npc.colorB}">
    </div>

    <div class="profile-info">

        <div class="profile-main">

            <div class="profile-avatar">
                ${npc.icon}
            </div>

            <div class="profile-buttons">

                <button
                    class="btn ${STATE.followed.has(npc.id)?"secondary":"primary"}"
                    onclick="toggleFollow('${npc.id}',this)"
                >
                    ${STATE.followed.has(npc.id)?"✓ Following":"＋ Follow"}
                </button>

                <button class="btn secondary" onclick="messageNPC('${npc.id}')">
                    💬 Message
                </button>

                <button class="btn secondary" onclick="shareProfile('${npc.id}')">
                    ↗️ Share
                </button>

            </div>

        </div>

        <div class="profile-details">

            <h1>
                ${escapeHTML(npc.name)}
                ${npc.verified?`<span class="verify">✓</span>`:""}
            </h1>

            <div class="profile-handle">
                ${escapeHTML(npc.handle)}
                · ${npc.flag} ${escapeHTML(npc.country)}
            </div>

            <div class="bio">
                ${escapeHTML(npc.bio)}
            </div>

            <div class="profile-stats">
                <span>📍 ${escapeHTML(npc.city)}</span>
                <span>🎭 ${escapeHTML(npc.personality)}</span>
                <span>🎯 Level ${npc.level}</span>
                <span><b>${number(npc.followers)}</b> followers</span>
                <span><b>${number(npc.following)}</b> following</span>
            </div>

            <div class="profile-tabs">
                <button class="tab active">Posts ${posts.length}</button>
                <button class="tab">Replies</button>
                <button class="tab">Media</button>
            </div>

        </div>

    </div>

    <div>
        ${
            posts.length
            ? posts.map(postHTML).join("")
            : `
                <div class="empty">
                    <div class="empty-icon">📭</div>
                    This NPC has no posts yet.
                </div>
            `
        }
    </div>
    `;

    renderRight();
    window.scrollTo({top:0,behavior:"smooth"});
}

/* ============================================================
   MY NPC
   ============================================================ */

function showMyNPC(){
    if(!STATE.currentNPC){
        STATE.currentNPC=STATE.npcs[0];
    }

    openProfile(STATE.currentNPC.id);
}

/* ============================================================
   LIKE
   ============================================================ */

function toggleLike(postId){
    const post=STATE.posts.find(p=>p.id===postId);

    if(!post) return;

    if(STATE.liked.has(postId)){
        STATE.liked.delete(postId);
        post.likes=Math.max(0,post.likes-1);
    }else{
        STATE.liked.add(postId);
        post.likes++;
    }

    refreshCurrentView(postId);
}

/* ============================================================
   SAVE
   ============================================================ */

function toggleSave(postId){
    if(STATE.saved.has(postId)){
        STATE.saved.delete(postId);
        toast("Removed from saved posts.");
    }else{
        STATE.saved.add(postId);
        toast("Post saved for this session.");
    }

    refreshCurrentView(postId);
}

/* ============================================================
   REFRESH CURRENT VIEW
   ============================================================ */

function refreshCurrentView(){
    if(STATE.currentNPC){
        const profileVisible=document.querySelector(".profile-cover");

        if(profileVisible){
            openProfile(STATE.currentNPC.id);
            return;
        }
    }

    renderHome();
}

/* ============================================================
   COMMENTS
   ============================================================ */

function openComments(postId){
    const post=STATE.posts.find(p=>p.id===postId);

    if(!post) return;

    const npc=STATE.npcs.find(n=>n.id===post.authorId);

    openModal(`
        <div class="modal-head">
            <h2>Comments</h2>
            <button class="close" onclick="closeModal()">×</button>
        </div>

        <div class="modal-body">

            <div class="notice">
                <b>${escapeHTML(npc.name)}</b><br>
                ${escapeHTML(post.text)}
            </div>

            ${
                post.commentsList.length
                ?
                post.commentsList.map(c=>`
                    <div class="notice">
                        <b>${escapeHTML(c.name)}</b><br>
                        ${escapeHTML(c.text)}
                    </div>
                `).join("")
                :
                `<div class="notice">No comments yet. The NPC population is suspiciously quiet.</div>`
            }

            <button
                class="btn primary"
                style="width:100%;margin-top:5px"
                onclick="addGeneratedComment('${postId}')"
            >
                ✨ Generate NPC Comment
            </button>

        </div>
    `);
}

function addGeneratedComment(postId){
    const post=STATE.posts.find(p=>p.id===postId);

    if(!post) return;

    const commenter=pick(STATE.npcs);

    post.commentsList.push({
        name:commenter.name,
        text:pick(COMMENTS)
    });

    post.comments++;

    openComments(postId);
}

/* ============================================================
   SHARE
   ============================================================ */

function sharePost(postId){
    const post=STATE.posts.find(p=>p.id===postId);

    if(!post) return;

    post.shares++;

    toast("Post shared into the NPCBook universe.");
}

/* ============================================================
   PROFILE SHARE
   ============================================================ */

function shareProfile(npcId){
    const npc=STATE.npcs.find(n=>n.id===npcId);

    if(!npc) return;

    toast("Shared "+npc.name+"'s NPC profile.");
}

/* ============================================================
   FOLLOW
   ============================================================ */

function toggleFollow(npcId,button){
    const npc=STATE.npcs.find(n=>n.id===npcId);

    if(!npc) return;

    if(STATE.followed.has(npcId)){
        STATE.followed.delete(npcId);
        toast("Unfollowed "+npc.name+".");
    }else{
        STATE.followed.add(npcId);
        toast("Following "+npc.name+".");
    }

    if(button){
        button.textContent=
            STATE.followed.has(npcId)
            ?"✓ Following"
            :"＋ Follow";
    }

    if(document.querySelector(".profile-cover")){
        openProfile(npcId);
    }else{
        renderHome();
    }
}

/* ============================================================
   POST MENU
   ============================================================ */

function postMenu(postId){
    openModal(`
        <div class="modal-head">
            <h2>Post options</h2>
            <button class="close" onclick="closeModal()">×</button>
        </div>

        <div class="modal-body">

            <div class="notice">
                This is a temporary generated NPC world.
                Nothing here is saved after refresh.
            </div>

            <button
                class="btn secondary"
                style="width:100%;margin-bottom:8px"
                onclick="toggleSave('${postId}');closeModal()"
            >
                🔖 Save / Unsave
            </button>

            <button
                class="btn secondary"
                style="width:100%;margin-bottom:8px"
                onclick="sharePost('${postId}');closeModal()"
            >
                ↗️ Share
            </button>

            <button
                class="btn secondary"
                style="width:100%"
                onclick="closeModal()"
            >
                Cancel
            </button>

        </div>
    `);
}

/* ============================================================
   SEARCH
   ============================================================ */

function searchSite(value){
    const q=value.trim().toLowerCase();

    if(!q){
        renderHome();
        return;
    }

    const matchingNPCs=STATE.npcs.filter(n=>
        [
            n.name,
            n.handle,
            n.country,
            n.city,
            n.job,
            n.world,
            n.genre,
            n.personality,
            n.bio
        ].join(" ").toLowerCase().includes(q)
    );

    const matchingPosts=STATE.posts.filter(p=>
        p.text.toLowerCase().includes(q) ||
        p.tag.toLowerCase().includes(q) ||
        p.world.name.toLowerCase().includes(q)
    );

    setNav("");

    document.getElementById("main").innerHTML=`

    <div class="heading">
        <div>
            <h1>Search</h1>
            <p>Results for "${escapeHTML(value)}"</p>
        </div>
    </div>

    ${
        matchingNPCs.length
        ?
        `
        <div class="side-card" style="margin-bottom:14px">
            <h3>👥 NPCs</h3>

            ${matchingNPCs.map(n=>`
                <div class="mini-user">

                    <button
                        class="avatar"
                        onclick="openProfile('${n.id}')"
                    >
                        ${n.icon}
                    </button>

                    <div class="mini-info">
                        <div class="mini-name">
                            ${escapeHTML(n.name)}
                        </div>
                        <div class="mini-handle">
                            ${escapeHTML(n.handle)}
                            · ${escapeHTML(n.job)}
                        </div>
                    </div>

                    <button
                        class="follow"
                        onclick="openProfile('${n.id}')"
                    >
                        View
                    </button>

                </div>
            `).join("")}

        </div>
        `
        :
        ""
    }

    ${
        matchingPosts.length
        ?
        matchingPosts.map(postHTML).join("")
        :
        `<div class="empty">
            <div class="empty-icon">🔎</div>
            No matching NPCs or posts found.
        </div>`
    }
    `;

    renderRight();
}

/* ============================================================
   TRENDING
   ============================================================ */

function showTrending(){
    setNav("trending");

    const posts=shuffle([...STATE.posts])
        .sort((a,b)=>(b.likes+b.comments*3)-(a.likes+a.comments*3))
        .slice(0,12);

    document.getElementById("main").innerHTML=`

    <div class="heading">
        <div>
            <h1>🔥 Trending</h1>
            <p>Posts causing the most NPC activity in this temporary world.</p>
        </div>
    </div>

    ${posts.map(postHTML).join("")}
    `;

    renderRight();
    window.scrollTo({top:0,behavior:"smooth"});
}

/* ============================================================
   QUESTS
   ============================================================ */

function showQuests(){
    setNav("quests");

    const quests=[
        ["⚔️","Find the protagonist","Locate the person who keeps triggering every side quest.","Rare"],
        ["🗝️","Return the suspicious key","Someone left it beside a door marked DO NOT OPEN.","Common"],
        ["📦","Deliver the mysterious package","Nobody knows what is inside. Please stop asking.","Epic"],
        ["🧙","Locate the wizard","Last seen arguing with a vending machine.","Rare"],
        ["🏰","Protect the village","Mostly from paperwork.","Legendary"],
        ["🍜","Feed the adventuring party","They somehow forgot food again.","Common"],
        ["📜","Read the prophecy","It may contain important information or a grocery list.","Epic"],
        ["🚪","Guard the door","Do not open it. Seriously.","Legendary"],
        ["💼","Survive Monday","Difficulty: impossible.","Mythic"]
    ];

    document.getElementById("main").innerHTML=`

    <div class="heading">
        <div>
            <h1>⚔️ Quests</h1>
            <p>NPC-generated quests from the current world.</p>
        </div>
    </div>

    ${quests.map(q=>`
        <div class="side-card">

            <div style="display:flex;gap:12px;align-items:center">

                <div style="font-size:31px">${q[0]}</div>

                <div style="flex:1">
                    <h3 style="margin:0">${q[1]}</h3>
                    <div style="color:var(--muted);font-size:12px;margin-top:5px">
                        ${q[2]}
                    </div>
                </div>

                <span class="tag">${q[3]}</span>

            </div>

        </div>
    `).join("")}
    `;

    renderRight();
}

/* ============================================================
   MARKET
   ============================================================ */

function showMarket(){
    setNav("market");

    const items=[
        ["🗡️","Definitely Normal Sword","999 gold","May or may not be cursed."],
        ["🧪","Potion of Questionable Healing","47 gold","The label says 'probably works.'"],
        ["🗝️","Mystery Key","12 gold","Opens something. Probably."],
        ["📜","Ancient Prophecy","3 gold","Slightly used."],
        ["🪑","Legendary Chair","850 gold","The previous owner defeated a dragon while sitting on it."],
        ["🍎","Apple of Mild Importance","2 gold","Quest item according to someone."],
        ["🎩","Wizard Hat","240 gold","Wizard not included."],
        ["📦","Mystery Box","100 gold","No refunds."],
        ["🧭","Broken Compass","9 gold","Points somewhere."],
        ["📚","Forbidden Book","600 gold","Library fine not included."]
    ];

    document.getElementById("main").innerHTML=`

    <div class="heading">
        <div>
            <h1>🛒 NPC Market</h1>
            <p>Items being sold by NPCs who may or may not know what they are doing.</p>
        </div>
    </div>

    ${items.map(i=>`
        <div class="side-card">

            <div style="display:flex;gap:12px;align-items:center">

                <div style="font-size:35px">${i[0]}</div>

                <div style="flex:1">
                    <h3 style="margin:0">${i[1]}</h3>
                    <div style="color:var(--muted);font-size:12px;margin-top:4px">
                        ${i[3]}
                    </div>
                </div>

                <button
                    class="btn primary"
                    onclick="toast('Purchase simulated. No real money involved.')"
                >
                    ${i[2]}
                </button>

            </div>

        </div>
    `).join("")}
    `;

    renderRight();
}

/* ============================================================
   NOTIFICATIONS
   ============================================================ */

function showNotifications(){
    openModal(`
        <div class="modal-head">
            <h2>🔔 Notifications</h2>
            <button class="close" onclick="closeModal()">×</button>
        </div>

        <div class="modal-body">

            <div class="notice">
                ❤️ Someone liked your completely fictional NPC post.
            </div>

            <div class="notice">
                ⚔️ A quest has been assigned to someone else.
            </div>

            <div class="notice">
                👥 ${STATE.npcs.length} NPCs are currently online.
            </div>

            <div class="notice">
                🌍 Your temporary world contains ${STATE.posts.length} unique generated posts.
            </div>

            <div class="notice">
                🧠 No activity from this world is stored after refresh.
            </div>

        </div>
    `);
}

/* ============================================================
   MESSAGES
   ============================================================ */

function showMessages(){
    const people=shuffle(STATE.npcs).slice(0,7);

    openModal(`
        <div class="modal-head">
            <h2>💬 Messages</h2>
            <button class="close" onclick="closeModal()">×</button>
        </div>

        <div class="modal-body">

            ${people.map(n=>`
                <div
                    class="notice"
                    style="display:flex;align-items:center;gap:10px;cursor:pointer"
                    onclick="closeModal();openProfile('${n.id}')"
                >
                    <div class="avatar">${n.icon}</div>

                    <div>
                        <b>${escapeHTML(n.name)}</b>

                        <div style="color:var(--muted);font-size:11px;margin-top:3px">
                            "${escapeHTML(pick([
                                "Are you also seeing this quest?",
                                "I think the protagonist is coming.",
                                "Do you know where the save point is?",
                                "Management just sent another form.",
                                "I found the suspicious key.",
                                "Please tell me you saw that.",
                                "The dungeon is closed again."
                            ]))}"
                        </div>
                    </div>
                </div>
            `).join("")}

        </div>
    `);
}

/* ============================================================
   SETTINGS
   ============================================================ */

function showSettings(){
    openModal(`
        <div class="modal-head">
            <h2>⚙️ NPCBook Settings</h2>
            <button class="close" onclick="closeModal()">×</button>
        </div>

        <div class="modal-body">

            <div class="notice">
                <b>World generation</b><br>
                A fresh temporary world is generated whenever this page is refreshed.
            </div>

            <div class="notice">
                <b>Storage</b><br>
                NPCBook does not use LocalStorage, SessionStorage, cookies for app data,
                or a database.
            </div>

            <div class="notice">
                <b>Duplicate protection</b><br>
                Exact duplicate post fingerprints are rejected during each generated world.
            </div>

            <div class="notice">
                <b>Generated now</b><br>
                ${STATE.npcs.length} NPCs · ${STATE.posts.length} unique posts
            </div>

            <button
                class="btn primary"
                style="width:100%"
                onclick="closeModal();newWorld()"
            >
                🌌 Generate Completely New World
            </button>

        </div>
    `);
}

/* ============================================================
   MESSAGE NPC
   ============================================================ */

function messageNPC(npcId){
    const npc=STATE.npcs.find(n=>n.id===npcId);

    if(!npc) return;

    openModal(`
        <div class="modal-head">
            <h2>💬 Message ${escapeHTML(npc.name)}</h2>
            <button class="close" onclick="closeModal()">×</button>
        </div>

        <div class="modal-body">

            <div class="notice">
                ${npc.icon}
                <b>${escapeHTML(npc.name)}</b><br>
                ${escapeHTML(npc.bio)}
            </div>

            <div class="notice">
                <b>${escapeHTML(npc.name)}:</b><br>
                ${escapeHTML(pick([
                    "I am currently dealing with a side quest.",
                    "Please don't ask me about the locked door.",
                    "The protagonist was here five minutes ago.",
                    "I am technically working right now.",
                    "I think the system assigned me another quest.",
                    "Do you have snacks?",
                    "Management says everything is under control."
                ]))}
            </div>

            <button
                class="btn primary"
                style="width:100%"
                onclick="toast('Message sent into the temporary NPC universe.');closeModal()"
            >
                Send "Hello"
            </button>

        </div>
    `);
}

/* ============================================================
   RANDOM POST
   ============================================================ */

function randomPost(){
    const post=pick(STATE.posts);

    if(!post) return;

    renderHome();

    setTimeout(()=>{
        const element=document.getElementById(post.id);

        if(element){
            element.scrollIntoView({
                behavior:"smooth",
                block:"center"
            });

            element.style.boxShadow=
                "0 0 0 3px rgba(91,140,255,.45),0 15px 50px rgba(0,0,0,.35)";

            setTimeout(()=>{
                element.style.boxShadow="";
            },1600);
        }
    },80);
}

/* ============================================================
   NEW NPC
   ============================================================ */

function newNPC(){
    const npc=createNPC();

    if(!npc){
        toast("NPC generator reached a temporary combination limit.");
        return;
    }

    STATE.npcs.push(npc);

    const amount=4+rand(4);

    for(let i=0;i<amount;i++){
        createUniquePost(npc);
    }

    STATE.currentNPC=npc;

    toast("New NPC generated: "+npc.name);

    openProfile(npc.id);
}

/* ============================================================
   NEW WORLD
   ============================================================ */

function newWorld(){
    closeModal();

    generateWorld();

    const search=document.getElementById("searchInput");

    if(search){
        search.value="";
    }

    renderHome();

    toast(
        "🌌 New NPC world generated: "+
        STATE.npcs.length+
        " NPCs · "+
        STATE.posts.length+
        " unique posts"
    );
}

/* ============================================================
   HOME / REFRESH
   ============================================================ */

function goHome(){
    /*
      A real page reload is intentional.
      The browser then creates a brand-new random world.
    */
    window.location.reload();
}

/* ============================================================
   NAV STATE
   ============================================================ */

function setNav(name){
    document.querySelectorAll(".nav").forEach(n=>{
        n.classList.remove("active");
    });

    if(name==="home"){
        document.getElementById("homeNav")?.classList.add("active");
    }

    const mobile=document.getElementById("mobileHome");

    if(mobile){
        mobile.classList.toggle("active",name==="home");
    }
}

/* ============================================================
   MODALS
   ============================================================ */

function openModal(content){
    document.getElementById("modal").innerHTML=content;
    document.getElementById("modalLayer").classList.add("open");
    document.body.style.overflow="hidden";
}

function closeModal(){
    document.getElementById("modalLayer").classList.remove("open");
    document.body.style.overflow="";
}

function modalOutside(event){
    if(event.target.id==="modalLayer"){
        closeModal();
    }
}

/* ============================================================
   TOAST
   ============================================================ */

let toastTimer=null;

function toast(message){
    const el=document.getElementById("toast");

    el.textContent=message;
    el.classList.add("show");

    clearTimeout(toastTimer);

    toastTimer=setTimeout(()=>{
        el.classList.remove("show");
    },2200);
}

/* ============================================================
   KEYBOARD
   ============================================================ */

document.addEventListener("keydown",event=>{
    if(event.key==="Escape"){
        closeModal();
    }
});

/* ============================================================
   START
   ============================================================ */

generateWorld();
renderHome();

</script>
</body>
</html>
'''

Path("index.html").write_text(HTML, encoding="utf-8")

print("NPCBook generated successfully.")
print("index.html created.")
print("Fresh NPC worlds are generated in the browser on every page refresh.")
print("No LocalStorage, SessionStorage, app-data cookies, or database are used.")
'''

Path("app.py").write_text(Path(__file__).read_text(encoding="utf-8") if "__file__" in globals() else "", encoding="utf-8")
