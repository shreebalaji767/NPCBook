from pathlib import Path

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#101114">
<meta name="description" content="NPCBook — Social Media for NPCs">
<title>NPCBook — Social Media for NPCs</title>

<style>
:root{
    --bg:#0b0c0f;
    --panel:#111318;
    --panel2:#17191f;
    --panel3:#1d2027;
    --border:#2a2e38;
    --text:#f4f5f7;
    --muted:#9ca3af;
    --accent:#7c5cff;
    --accent2:#a78bfa;
    --danger:#ff5577;
    --success:#39d98a;
    --warning:#f6c85f;
    --blue:#4da3ff;
    --shadow:0 12px 35px rgba(0,0,0,.25);
    --radius:18px;
    --max:1440px;
}

*{
    box-sizing:border-box;
}

html{
    scroll-behavior:smooth;
}

body{
    margin:0;
    background:
        radial-gradient(circle at 20% -10%,rgba(124,92,255,.13),transparent 28%),
        radial-gradient(circle at 90% 0%,rgba(77,163,255,.08),transparent 25%),
        var(--bg);
    color:var(--text);
    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    min-height:100vh;
    overflow-x:hidden;
}

button,
input,
textarea,
select{
    font:inherit;
}

button{
    cursor:pointer;
    touch-action:manipulation;
}

a{
    color:inherit;
    text-decoration:none;
}

img{
    max-width:100%;
}

.hidden{
    display:none !important;
}

.app-shell{
    min-height:100vh;
}

/* TOP BAR */

.topbar{
    position:sticky;
    top:0;
    z-index:1000;
    height:66px;
    border-bottom:1px solid var(--border);
    background:rgba(11,12,15,.92);
    backdrop-filter:blur(18px);
}

.topbar-inner{
    width:min(100%,var(--max));
    height:100%;
    margin:auto;
    padding:0 18px;
    display:flex;
    align-items:center;
    gap:14px;
}

.logo{
    display:flex;
    align-items:center;
    gap:9px;
    font-weight:900;
    font-size:20px;
    white-space:nowrap;
}

.logo-icon{
    width:38px;
    height:38px;
    border-radius:12px;
    display:grid;
    place-items:center;
    background:linear-gradient(135deg,#7c5cff,#4da3ff);
    box-shadow:0 7px 25px rgba(124,92,255,.28);
}

.logo-text span{
    color:var(--accent2);
}

.top-search{
    flex:1;
    max-width:520px;
    margin-left:10px;
    position:relative;
}

.top-search input{
    width:100%;
    height:42px;
    border:1px solid var(--border);
    border-radius:13px;
    background:#17191f;
    color:var(--text);
    padding:0 16px 0 42px;
    outline:none;
}

.top-search input:focus{
    border-color:var(--accent);
    box-shadow:0 0 0 3px rgba(124,92,255,.13);
}

.search-icon{
    position:absolute;
    left:14px;
    top:50%;
    transform:translateY(-50%);
    color:var(--muted);
}

.top-actions{
    margin-left:auto;
    display:flex;
    align-items:center;
    gap:7px;
}

.icon-btn{
    width:42px;
    height:42px;
    border:1px solid transparent;
    background:transparent;
    color:var(--muted);
    border-radius:12px;
    display:grid;
    place-items:center;
    font-size:19px;
}

.icon-btn:hover{
    background:var(--panel2);
    color:var(--text);
    border-color:var(--border);
}

.profile-mini{
    width:40px;
    height:40px;
    border-radius:50%;
    overflow:hidden;
    border:2px solid var(--border);
}

.profile-mini img{
    width:100%;
    height:100%;
    object-fit:cover;
}

/* LAYOUT */

.layout{
    width:min(100%,var(--max));
    margin:auto;
    padding:20px 18px 90px;
    display:grid;
    grid-template-columns:230px minmax(0,680px) 300px;
    gap:20px;
    align-items:start;
}

.sidebar{
    position:sticky;
    top:86px;
}

.nav-card{
    background:rgba(17,19,24,.88);
    border:1px solid var(--border);
    border-radius:var(--radius);
    padding:10px;
    box-shadow:var(--shadow);
}

.nav-item{
    width:100%;
    border:0;
    background:transparent;
    color:var(--muted);
    padding:12px 13px;
    border-radius:12px;
    display:flex;
    align-items:center;
    gap:12px;
    text-align:left;
    min-height:46px;
    font-weight:650;
}

.nav-item:hover,
.nav-item.active{
    background:var(--panel3);
    color:var(--text);
}

.nav-item.active{
    color:#c8bbff;
}

.nav-icon{
    width:24px;
    text-align:center;
    font-size:18px;
}

.sidebar-divider{
    height:1px;
    background:var(--border);
    margin:9px 6px;
}

.side-user{
    margin-top:14px;
    padding:14px;
    border:1px solid var(--border);
    background:rgba(17,19,24,.8);
    border-radius:var(--radius);
}

.side-user-row{
    display:flex;
    align-items:center;
    gap:10px;
}

.side-user img{
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
}

.side-user-name{
    font-weight:750;
}

.side-user-handle{
    color:var(--muted);
    font-size:12px;
}

/* FEED */

.feed{
    min-width:0;
}

.feed-header{
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:14px;
}

.feed-title{
    font-size:22px;
    font-weight:900;
}

.feed-subtitle{
    color:var(--muted);
    font-size:12px;
}

.world-refresh{
    border:1px solid var(--border);
    background:var(--panel);
    color:var(--text);
    border-radius:12px;
    min-height:42px;
    padding:0 13px;
    font-weight:700;
}

.world-refresh:hover{
    border-color:var(--accent);
}

/* COMPOSER */

.composer{
    background:rgba(17,19,24,.92);
    border:1px solid var(--border);
    border-radius:var(--radius);
    padding:15px;
    margin-bottom:14px;
    box-shadow:var(--shadow);
}

.composer-top{
    display:flex;
    gap:12px;
}

.composer-avatar{
    width:44px;
    height:44px;
    border-radius:50%;
    object-fit:cover;
    flex:none;
}

.composer textarea{
    flex:1;
    resize:none;
    min-height:62px;
    max-height:180px;
    background:transparent;
    border:0;
    outline:0;
    color:var(--text);
    padding:8px 0;
    line-height:1.5;
}

.composer textarea::placeholder{
    color:#737985;
}

.composer-bottom{
    border-top:1px solid var(--border);
    margin-top:10px;
    padding-top:10px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
}

.composer-tools{
    display:flex;
    gap:5px;
}

.composer-tool{
    width:40px;
    height:38px;
    border:0;
    background:transparent;
    color:var(--muted);
    border-radius:10px;
}

.composer-tool:hover{
    background:var(--panel3);
    color:var(--text);
}

.post-btn{
    border:0;
    background:linear-gradient(135deg,var(--accent),#5b4bd8);
    color:#fff;
    border-radius:11px;
    min-height:40px;
    padding:0 18px;
    font-weight:800;
    box-shadow:0 8px 20px rgba(124,92,255,.2);
}

.post-btn:hover{
    filter:brightness(1.1);
}

/* POSTS */

.post{
    background:rgba(17,19,24,.94);
    border:1px solid var(--border);
    border-radius:var(--radius);
    padding:16px;
    margin-bottom:14px;
    box-shadow:0 7px 28px rgba(0,0,0,.12);
}

.post:hover{
    border-color:#343947;
}

.post-head{
    display:flex;
    gap:11px;
    align-items:flex-start;
}

.avatar-btn{
    border:0;
    padding:0;
    background:transparent;
    flex:none;
}

.post-avatar{
    width:46px;
    height:46px;
    border-radius:50%;
    object-fit:cover;
    display:block;
}

.post-author{
    min-width:0;
    flex:1;
}

.author-line{
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:5px;
}

.author-name{
    font-weight:850;
    cursor:pointer;
}

.author-name:hover{
    text-decoration:underline;
}

.verified{
    color:#55a9ff;
    font-size:14px;
}

.author-handle,
.post-time{
    color:var(--muted);
    font-size:13px;
}

.post-meta{
    color:var(--muted);
    font-size:12px;
    margin-top:3px;
    display:flex;
    gap:7px;
    flex-wrap:wrap;
}

.world-badge{
    display:inline-flex;
    align-items:center;
    border:1px solid rgba(124,92,255,.28);
    background:rgba(124,92,255,.1);
    color:#c7bcff;
    border-radius:999px;
    padding:3px 8px;
    font-size:11px;
    font-weight:700;
}

.more-btn{
    width:34px;
    height:34px;
    border:0;
    background:transparent;
    color:var(--muted);
    border-radius:9px;
}

.more-btn:hover{
    background:var(--panel3);
    color:var(--text);
}

.post-text{
    margin:13px 0 12px 57px;
    line-height:1.58;
    white-space:pre-wrap;
    overflow-wrap:anywhere;
}

.post-media{
    margin:0 0 12px 57px;
    min-height:130px;
    border-radius:15px;
    border:1px solid var(--border);
    overflow:hidden;
    position:relative;
    background:
        radial-gradient(circle at 20% 30%,rgba(124,92,255,.5),transparent 30%),
        radial-gradient(circle at 80% 70%,rgba(77,163,255,.3),transparent 32%),
        linear-gradient(135deg,#181b27,#101216);
    display:flex;
    align-items:flex-end;
    padding:16px;
}

.media-overlay{
    width:100%;
    padding:15px;
    border-radius:13px;
    background:rgba(0,0,0,.42);
    backdrop-filter:blur(5px);
}

.media-title{
    font-weight:900;
    font-size:17px;
}

.media-caption{
    color:#d4d7de;
    margin-top:4px;
    font-size:12px;
}

.post-actions{
    margin-left:57px;
    border-top:1px solid var(--border);
    padding-top:8px;
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:3px;
}

.action-btn{
    min-height:42px;
    border:0;
    border-radius:10px;
    background:transparent;
    color:var(--muted);
    display:flex;
    align-items:center;
    justify-content:center;
    gap:6px;
    font-size:13px;
}

.action-btn:hover{
    background:var(--panel3);
    color:var(--text);
}

.action-btn.liked{
    color:#ff5d82;
}

.action-btn.saved{
    color:#f3ca5f;
}

.action-btn.reposted{
    color:#42dc93;
}

.action-count{
    font-size:12px;
}

.comment-preview{
    margin:8px 0 0 57px;
    padding:9px 11px;
    border-radius:12px;
    background:#15171c;
    color:#c8ccd4;
    font-size:13px;
}

.comment-preview strong{
    color:var(--text);
}

.comment-box{
    margin:9px 0 0 57px;
    display:flex;
    gap:7px;
}

.comment-box input{
    flex:1;
    min-width:0;
    height:40px;
    border:1px solid var(--border);
    border-radius:11px;
    background:#15171c;
    color:var(--text);
    padding:0 12px;
    outline:none;
}

.comment-box input:focus{
    border-color:var(--accent);
}

.comment-send{
    height:40px;
    padding:0 12px;
    border:0;
    border-radius:10px;
    background:var(--accent);
    color:white;
    font-weight:750;
}

.comments-list{
    margin:8px 0 0 57px;
}

.comment{
    padding:8px 0;
    border-bottom:1px solid rgba(42,46,56,.65);
}

.comment:last-child{
    border-bottom:0;
}

.comment-author{
    font-weight:750;
    font-size:13px;
}

.comment-text{
    color:#c5c9d1;
    font-size:13px;
    margin-top:2px;
}

/* RIGHT SIDEBAR */

.right-column{
    position:sticky;
    top:86px;
    display:flex;
    flex-direction:column;
    gap:14px;
}

.widget{
    background:rgba(17,19,24,.88);
    border:1px solid var(--border);
    border-radius:var(--radius);
    padding:15px;
}

.widget-title{
    font-size:15px;
    font-weight:850;
    margin-bottom:12px;
}

.trend{
    padding:9px 0;
    border-bottom:1px solid rgba(42,46,56,.7);
}

.trend:last-child{
    border-bottom:0;
}

.trend-label{
    color:var(--muted);
    font-size:11px;
}

.trend-name{
    font-weight:750;
    margin-top:2px;
}

.trend-count{
    color:var(--muted);
    font-size:11px;
    margin-top:2px;
}

.quest{
    border:1px solid var(--border);
    border-radius:13px;
    padding:11px;
    margin-bottom:8px;
    background:#15171c;
}

.quest:last-child{
    margin-bottom:0;
}

.quest-title{
    font-weight:750;
    font-size:13px;
}

.quest-desc{
    color:var(--muted);
    font-size:11px;
    margin-top:3px;
}

.progress{
    height:5px;
    background:#252932;
    border-radius:99px;
    overflow:hidden;
    margin-top:8px;
}

.progress > div{
    height:100%;
    background:linear-gradient(90deg,var(--accent),#4da3ff);
}

/* PROFILE */

.profile-page{
    grid-column:2;
}

.profile-cover{
    height:190px;
    border-radius:20px 20px 0 0;
    background:
        radial-gradient(circle at 20% 20%,rgba(124,92,255,.8),transparent 28%),
        radial-gradient(circle at 80% 40%,rgba(77,163,255,.6),transparent 30%),
        linear-gradient(135deg,#181b28,#111318);
    border:1px solid var(--border);
}

.profile-main{
    background:var(--panel);
    border:1px solid var(--border);
    border-top:0;
    border-radius:0 0 20px 20px;
    padding:0 20px 20px;
}

.profile-top{
    display:flex;
    align-items:flex-end;
    justify-content:space-between;
    gap:15px;
    transform:translateY(-38px);
    margin-bottom:-20px;
}

.profile-avatar{
    width:92px;
    height:92px;
    border-radius:50%;
    border:5px solid var(--panel);
    object-fit:cover;
}

.follow-btn{
    min-height:40px;
    padding:0 18px;
    border-radius:11px;
    border:1px solid var(--border);
    background:var(--text);
    color:#101114;
    font-weight:800;
}

.follow-btn.following{
    background:transparent;
    color:var(--text);
}

.profile-name{
    font-size:23px;
    font-weight:900;
}

.profile-handle{
    color:var(--muted);
}

.profile-bio{
    margin-top:12px;
    line-height:1.5;
}

.profile-info{
    display:flex;
    flex-wrap:wrap;
    gap:13px;
    color:var(--muted);
    font-size:13px;
    margin-top:12px;
}

.profile-stats{
    display:flex;
    gap:25px;
    margin-top:15px;
}

.stat strong{
    color:var(--text);
}

.stat{
    color:var(--muted);
    font-size:13px;
}

.profile-tabs{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    border-top:1px solid var(--border);
    margin-top:18px;
}

.profile-tab{
    border:0;
    background:transparent;
    color:var(--muted);
    min-height:48px;
    font-weight:750;
}

.profile-tab.active{
    color:var(--text);
    border-bottom:2px solid var(--accent);
}

/* MODAL */

.modal-backdrop{
    position:fixed;
    inset:0;
    z-index:3000;
    background:rgba(0,0,0,.72);
    backdrop-filter:blur(7px);
    display:flex;
    align-items:center;
    justify-content:center;
    padding:20px;
}

.modal{
    width:min(100%,620px);
    max-height:min(90vh,800px);
    overflow:auto;
    background:#111318;
    border:1px solid var(--border);
    border-radius:20px;
    box-shadow:0 25px 80px rgba(0,0,0,.5);
}

.modal-header{
    position:sticky;
    top:0;
    z-index:2;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:16px 18px;
    background:rgba(17,19,24,.96);
    backdrop-filter:blur(12px);
    border-bottom:1px solid var(--border);
}

.modal-title{
    font-weight:900;
}

.modal-body{
    padding:18px;
}

.close-btn{
    width:38px;
    height:38px;
    border:0;
    background:var(--panel3);
    color:var(--text);
    border-radius:10px;
}

.modal-input,
.modal-textarea{
    width:100%;
    border:1px solid var(--border);
    border-radius:12px;
    background:#17191f;
    color:var(--text);
    padding:12px;
    outline:none;
}

.modal-textarea{
    min-height:130px;
    resize:vertical;
}

.modal-label{
    display:block;
    color:var(--muted);
    font-size:12px;
    margin:0 0 6px;
}

.modal-field{
    margin-bottom:13px;
}

.modal-submit{
    width:100%;
    min-height:45px;
    border:0;
    border-radius:12px;
    background:var(--accent);
    color:#fff;
    font-weight:850;
}

.option-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:10px;
}

.option-card{
    border:1px solid var(--border);
    background:#15171c;
    padding:13px;
    border-radius:13px;
}

.option-card strong{
    display:block;
}

.option-card span{
    color:var(--muted);
    font-size:11px;
}

/* MOBILE NAV */

.mobile-nav{
    display:none;
}

/* TOAST */

.toast-container{
    position:fixed;
    z-index:5000;
    right:18px;
    bottom:18px;
    display:flex;
    flex-direction:column;
    gap:8px;
    pointer-events:none;
}

.toast{
    background:#20232b;
    border:1px solid var(--border);
    color:var(--text);
    padding:12px 15px;
    border-radius:12px;
    box-shadow:var(--shadow);
    font-size:13px;
    animation:toastIn .2s ease;
}

@keyframes toastIn{
    from{
        opacity:0;
        transform:translateY(10px);
    }
    to{
        opacity:1;
        transform:none;
    }
}

/* EMPTY */

.empty{
    border:1px dashed var(--border);
    background:rgba(17,19,24,.7);
    border-radius:18px;
    padding:45px 20px;
    text-align:center;
    color:var(--muted);
}

.empty-icon{
    font-size:40px;
    margin-bottom:10px;
}

/* RESPONSIVE */

@media(max-width:1180px){
    .layout{
        grid-template-columns:210px minmax(0,1fr);
    }

    .right-column{
        display:none;
    }
}

@media(max-width:820px){
    .topbar{
        height:60px;
    }

    .topbar-inner{
        padding:0 12px;
    }

    .logo-text{
        display:none;
    }

    .top-search{
        margin-left:0;
    }

    .top-actions .desktop-only{
        display:none;
    }

    .layout{
        display:block;
        padding:14px 12px calc(85px + env(safe-area-inset-bottom));
    }

    .sidebar{
        display:none;
    }

    .feed{
        width:100%;
    }

    .mobile-nav{
        position:fixed;
        left:0;
        right:0;
        bottom:0;
        z-index:2000;
        display:grid;
        grid-template-columns:repeat(5,1fr);
        min-height:64px;
        padding:5px 5px calc(5px + env(safe-area-inset-bottom));
        background:rgba(12,13,17,.96);
        border-top:1px solid var(--border);
        backdrop-filter:blur(18px);
    }

    .mobile-nav button{
        border:0;
        background:transparent;
        color:var(--muted);
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        gap:2px;
        border-radius:10px;
        min-height:50px;
    }

    .mobile-nav button.active{
        color:#c8bbff;
    }

    .mobile-nav-icon{
        font-size:19px;
    }

    .mobile-nav-label{
        font-size:9px;
    }

    .post{
        padding:13px;
    }

    .post-text,
    .post-media,
    .post-actions,
    .comment-preview,
    .comment-box,
    .comments-list{
        margin-left:0;
    }

    .post-actions{
        grid-template-columns:repeat(5,1fr);
    }

    .action-btn{
        font-size:12px;
    }

    .profile-page{
        width:100%;
    }
}

@media(max-width:520px){
    .topbar-inner{
        gap:7px;
    }

    .top-search input{
        height:40px;
    }

    .icon-btn{
        width:39px;
        height:39px;
    }

    .profile-mini{
        width:36px;
        height:36px;
    }

    .feed-title{
        font-size:19px;
    }

    .world-refresh{
        padding:0 10px;
        font-size:12px;
    }

    .composer{
        padding:12px;
    }

    .composer-avatar{
        width:38px;
        height:38px;
    }

    .composer-tool{
        width:36px;
    }

    .post-avatar{
        width:42px;
        height:42px;
    }

    .author-handle,
    .post-time{
        font-size:12px;
    }

    .post-text{
        font-size:14px;
    }

    .post-actions{
        gap:1px;
    }

    .action-btn{
        min-height:44px;
        padding:0 2px;
        gap:3px;
    }

    .action-label{
        display:none;
    }

    .comment-box{
        flex-direction:row;
    }

    .profile-cover{
        height:145px;
    }

    .profile-main{
        padding:0 14px 16px;
    }

    .profile-avatar{
        width:76px;
        height:76px;
    }

    .profile-name{
        font-size:20px;
    }

    .option-grid{
        grid-template-columns:1fr;
    }

    .modal-backdrop{
        padding:8px;
        align-items:flex-end;
    }

    .modal{
        max-height:94vh;
        border-radius:18px 18px 0 0;
    }
}

@media(pointer:coarse){
    button,
    .nav-item,
    .action-btn,
    .icon-btn{
        min-height:44px;
    }

    input,
    textarea{
        font-size:16px;
    }
}

@media(max-width:360px){
    .top-actions{
        gap:2px;
    }

    .top-search{
        min-width:0;
    }

    .top-search input{
        padding-left:35px;
    }

    .logo-icon{
        width:34px;
        height:34px;
    }
}
</style>
</head>

<body>
<div class="app-shell">

<header class="topbar">
    <div class="topbar-inner">

        <button class="logo" onclick="window.location.reload()" aria-label="NPCBook Home">
            <span class="logo-icon">📱</span>
            <span class="logo-text">NPC<span>Book</span></span>
        </button>

        <div class="top-search">
            <span class="search-icon">🔎</span>
            <input
                id="searchInput"
                type="search"
                placeholder="Search NPCs, worlds, posts..."
                autocomplete="off"
                oninput="handleSearch(this.value)"
            >
        </div>

        <div class="top-actions">
            <button class="icon-btn desktop-only" onclick="showNotifications()" title="Notifications">🔔</button>
            <button class="icon-btn desktop-only" onclick="showMessages()" title="Messages">💬</button>
            <button class="icon-btn" onclick="newWorld()" title="New Random World">🎲</button>
            <button class="profile-mini" onclick="openProfile(currentUser.id)" title="My NPC">
                <img id="topAvatar" src="" alt="Profile">
            </button>
        </div>

    </div>
</header>

<main class="layout">

    <aside class="sidebar">

        <div class="nav-card">

            <button class="nav-item active" id="nav-home" onclick="goHome()">
                <span class="nav-icon">🏠</span>
                <span>Home</span>
            </button>

            <button class="nav-item" id="nav-profile" onclick="openProfile(currentUser.id)">
                <span class="nav-icon">🧑</span>
                <span>My NPC</span>
            </button>

            <button class="nav-item" id="nav-trending" onclick="showTrending()">
                <span class="nav-icon">🔥</span>
                <span>Trending</span>
            </button>

            <button class="nav-item" id="nav-quests" onclick="showQuests()">
                <span class="nav-icon">🎯</span>
                <span>Quests</span>
            </button>

            <button class="nav-item" id="nav-market" onclick="showMarket()">
                <span class="nav-icon">🛒</span>
                <span>NPC Market</span>
            </button>

            <div class="sidebar-divider"></div>

            <button class="nav-item" onclick="generateNPC()">
                <span class="nav-icon">✨</span>
                <span>Generate NPC</span>
            </button>

            <button class="nav-item" onclick="randomPost()">
                <span class="nav-icon">🎲</span>
                <span>Random Post</span>
            </button>

            <button class="nav-item" onclick="showSettings()">
                <span class="nav-icon">⚙️</span>
                <span>Settings</span>
            </button>

        </div>

        <div class="side-user">
            <div class="side-user-row">
                <img id="sideAvatar" src="" alt="">
                <div>
                    <div class="side-user-name" id="sideName"></div>
                    <div class="side-user-handle" id="sideHandle"></div>
                </div>
            </div>
        </div>

    </aside>

    <section class="feed" id="mainContent">

        <div class="feed-header">
            <div>
                <div class="feed-title" id="feedTitle">Home</div>
                <div class="feed-subtitle" id="feedSubtitle">The internet is full of NPCs.</div>
            </div>

            <button class="world-refresh" onclick="newWorld()">
                🎲 New World
            </button>
        </div>

        <div id="feedContent"></div>

    </section>

    <aside class="right-column">

        <div class="widget">
            <div class="widget-title">🔥 Trending NPC Lore</div>
            <div id="trendsWidget"></div>
        </div>

        <div class="widget">
            <div class="widget-title">🎯 Active Quests</div>
            <div id="questsWidget"></div>
        </div>

        <div class="widget">
            <div class="widget-title">👥 NPCs You May Know</div>
            <div id="peopleWidget"></div>
        </div>

    </aside>

</main>

<nav class="mobile-nav">
    <button id="mobile-home" class="active" onclick="goHome()">
        <span class="mobile-nav-icon">🏠</span>
        <span class="mobile-nav-label">Home</span>
    </button>

    <button id="mobile-search" onclick="focusSearch()">
        <span class="mobile-nav-icon">🔎</span>
        <span class="mobile-nav-label">Search</span>
    </button>

    <button id="mobile-create" onclick="focusComposer()">
        <span class="mobile-nav-icon">➕</span>
        <span class="mobile-nav-label">Post</span>
    </button>

    <button id="mobile-notifications" onclick="showNotifications()">
        <span class="mobile-nav-icon">🔔</span>
        <span class="mobile-nav-label">Alerts</span>
    </button>

    <button id="mobile-profile" onclick="openProfile(currentUser.id)">
        <span class="mobile-nav-icon">👤</span>
        <span class="mobile-nav-label">Profile</span>
    </button>
</nav>

<div class="toast-container" id="toastContainer"></div>

<div class="modal-backdrop hidden" id="modalBackdrop" onclick="backdropClose(event)">
    <div class="modal" id="modal">
        <div class="modal-header">
            <div class="modal-title" id="modalTitle">NPCBook</div>
            <button class="close-btn" onclick="closeModal()">✕</button>
        </div>
        <div class="modal-body" id="modalBody"></div>
    </div>
</div>

</div>

<script>
"use strict";

/* =========================================================
   RANDOM HELPERS
========================================================= */

function rand(max){
    if(max <= 0) return 0;

    if(window.crypto && crypto.getRandomValues){
        const a = new Uint32Array(1);
        crypto.getRandomValues(a);
        return a[0] % max;
    }

    return Math.floor(Math.random() * max);
}

function pick(arr){
    return arr[rand(arr.length)];
}

function chance(percent){
    return rand(100) < percent;
}

function uid(prefix="id"){
    const a = new Uint32Array(3);

    if(window.crypto && crypto.getRandomValues){
        crypto.getRandomValues(a);
        return prefix + "_" +
            a[0].toString(36) +
            a[1].toString(36) +
            a[2].toString(36);
    }

    return prefix + "_" + Date.now().toString(36) + Math.random().toString(36).slice(2);
}

function escapeHTML(value){
    return String(value ?? "")
        .replace(/&/g,"&amp;")
        .replace(/</g,"&lt;")
        .replace(/>/g,"&gt;")
        .replace(/"/g,"&quot;")
        .replace(/'/g,"&#039;");
}

/* =========================================================
   COUNTRY DATA
========================================================= */

const COUNTRY_DATA = [
    {
        country:"India",
        cities:["Delhi","Mumbai","Bengaluru","Hyderabad","Pune","Chennai","Jaipur","Hansi","Kolkata"],
        first:["Aarav","Arjun","Rohan","Kabir","Aditya","Vihaan","Ishaan","Rahul","Karan","Neha","Ananya","Priya","Kavya","Meera","Riya","Aditi"],
        last:["Sharma","Verma","Singh","Kumar","Patel","Mehta","Gupta","Malik","Joshi","Yadav","Kapoor","Chauhan"]
    },
    {
        country:"Japan",
        cities:["Tokyo","Osaka","Kyoto","Yokohama","Sapporo","Nagoya"],
        first:["Haruto","Ren","Yuki","Sota","Kaito","Daiki","Hina","Aoi","Yuna","Mio","Sakura","Rin"],
        last:["Sato","Suzuki","Takahashi","Tanaka","Watanabe","Ito","Yamamoto","Nakamura"]
    },
    {
        country:"South Korea",
        cities:["Seoul","Busan","Incheon","Daegu","Daejeon"],
        first:["Minjun","Jiho","Seojun","Hyunwoo","Jisoo","Minseo","Sora","Yuna","Eunji","Hana"],
        last:["Kim","Lee","Park","Choi","Jung","Kang","Cho","Yoon","Han"]
    },
    {
        country:"Brazil",
        cities:["São Paulo","Rio de Janeiro","Brasília","Curitiba","Salvador"],
        first:["Lucas","Gabriel","Mateus","Rafael","Bruno","Thiago","Marina","Beatriz","Camila","Larissa","Julia"],
        last:["Silva","Santos","Oliveira","Souza","Costa","Pereira","Almeida","Ribeiro"]
    },
    {
        country:"France",
        cities:["Paris","Lyon","Marseille","Nice","Toulouse"],
        first:["Louis","Hugo","Gabriel","Arthur","Lucas","Emma","Chloe","Camille","Lea","Manon"],
        last:["Martin","Bernard","Dubois","Thomas","Robert","Richard","Petit","Durand"]
    },
    {
        country:"Germany",
        cities:["Berlin","Munich","Hamburg","Cologne","Frankfurt"],
        first:["Lukas","Leon","Paul","Felix","Jonas","Max","Anna","Lena","Mia","Hannah","Laura"],
        last:["Müller","Schmidt","Schneider","Fischer","Weber","Meyer","Wagner","Becker"]
    },
    {
        country:"United States",
        cities:["New York","Chicago","Seattle","Austin","Boston","Los Angeles","Denver"],
        first:["Ethan","Noah","Liam","Mason","Lucas","Oliver","Emma","Olivia","Ava","Mia","Chloe","Sophie"],
        last:["Smith","Johnson","Brown","Davis","Miller","Wilson","Moore","Taylor","Anderson","Thomas"]
    },
    {
        country:"Canada",
        cities:["Toronto","Vancouver","Montreal","Calgary","Ottawa"],
        first:["Liam","Ethan","Noah","Jack","Owen","Maya","Emma","Claire","Sophie","Ella"],
        last:["Smith","Brown","Martin","Wilson","Taylor","Campbell","Anderson","Clark"]
    },
    {
        country:"United Kingdom",
        cities:["London","Manchester","Bristol","Leeds","Liverpool","Edinburgh"],
        first:["Oliver","George","Harry","Jack","Arthur","Charlie","Amelia","Isla","Emily","Sophie","Grace"],
        last:["Smith","Jones","Taylor","Brown","Williams","Wilson","Davies","Evans"]
    },
    {
        country:"Australia",
        cities:["Sydney","Melbourne","Brisbane","Perth","Adelaide"],
        first:["Jack","William","Noah","Oliver","Leo","James","Charlotte","Isla","Mia","Ruby","Grace"],
        last:["Smith","Jones","Williams","Brown","Wilson","Taylor","Anderson","Walker"]
    },
    {
        country:"Spain",
        cities:["Madrid","Barcelona","Valencia","Seville","Bilbao"],
        first:["Alejandro","Daniel","Pablo","Carlos","Miguel","Lucas","Sofia","Lucia","Elena","Carmen","Clara"],
        last:["Garcia","Fernandez","Gonzalez","Rodriguez","Lopez","Martinez","Sanchez","Perez"]
    },
    {
        country:"Italy",
        cities:["Rome","Milan","Naples","Turin","Florence"],
        first:["Luca","Matteo","Marco","Andrea","Alessandro","Francesco","Sofia","Giulia","Chiara","Elena"],
        last:["Rossi","Russo","Ferrari","Esposito","Bianchi","Romano","Colombo","Ricci"]
    },
    {
        country:"Mexico",
        cities:["Mexico City","Guadalajara","Monterrey","Puebla","Cancún"],
        first:["Santiago","Mateo","Diego","Luis","Carlos","Javier","Sofia","Valeria","Camila","Lucia"],
        last:["Garcia","Hernandez","Martinez","Lopez","Gonzalez","Perez","Rodriguez","Sanchez"]
    },
    {
        country:"Egypt",
        cities:["Cairo","Alexandria","Giza","Luxor"],
        first:["Omar","Youssef","Karim","Adam","Ahmed","Amr","Mariam","Nour","Salma","Laila"],
        last:["Hassan","Ali","Mahmoud","Ibrahim","Mostafa","Khalil","Farouk"]
    },
    {
        country:"Nigeria",
        cities:["Lagos","Abuja","Ibadan","Kano"],
        first:["Daniel","David","Samuel","Michael","Joshua","James","Ada","Amara","Chioma","Grace"],
        last:["Okafor","Adeyemi","Okoro","Adebayo","Eze","Balogun","Obi"]
    },
    {
        country:"Turkey",
        cities:["Istanbul","Ankara","Izmir","Bursa","Antalya"],
        first:["Emir","Kerem","Mert","Can","Arda","Efe","Zeynep","Elif","Derya","Defne"],
        last:["Yilmaz","Kaya","Demir","Sahin","Celik","Aydin","Arslan"]
    },
    {
        country:"Poland",
        cities:["Warsaw","Krakow","Gdansk","Wroclaw"],
        first:["Jakub","Jan","Antoni","Piotr","Kacper","Adam","Zofia","Julia","Maja","Oliwia"],
        last:["Nowak","Kowalski","Wisniewski","Wojcik","Kaminski","Lewandowski"]
    },
    {
        country:"Russia",
        cities:["Moscow","Saint Petersburg","Kazan","Novosibirsk"],
        first:["Alexander","Dmitri","Nikolai","Mikhail","Ivan","Alexei","Anna","Sofia","Maria","Elena"],
        last:["Ivanov","Petrov","Sokolov","Smirnov","Volkov","Kuznetsov"]
    },
    {
        country:"Greece",
        cities:["Athens","Thessaloniki","Patras"],
        first:["Nikos","Giorgos","Dimitris","Alexandros","Maria","Eleni","Sofia","Katerina"],
        last:["Papadopoulos","Georgiou","Nikolaidis","Pappas","Dimitriou"]
    },
    {
        country:"China",
        cities:["Shanghai","Beijing","Shenzhen","Guangzhou","Chengdu"],
        first:["Wei","Jun","Hao","Ming","Tao","Li","Yue","Mei","Xin","Lin"],
        last:["Wang","Li","Zhang","Liu","Chen","Yang","Huang","Zhao"]
    },
    {
        country:"Thailand",
        cities:["Bangkok","Chiang Mai","Pattaya","Phuket"],
        first:["Narin","Krit","Than","Anan","Preecha","Mali","Nicha","Pim","Suda"],
        last:["Sukhum","Chai","Srisuk","Wong","Kittisak"]
    },
    {
        country:"Vietnam",
        cities:["Hanoi","Ho Chi Minh City","Da Nang","Hai Phong"],
        first:["Minh","Nam","Huy","Long","Duc","Lan","Linh","Mai","Thao"],
        last:["Nguyen","Tran","Le","Pham","Hoang","Vo","Phan"]
    },
    {
        country:"Indonesia",
        cities:["Jakarta","Bandung","Surabaya","Yogyakarta","Bali"],
        first:["Rizky","Dimas","Budi","Arif","Fajar","Ayu","Putri","Sari","Dewi"],
        last:["Santoso","Wijaya","Saputra","Pratama","Hidayat"]
    },
    {
        country:"South Africa",
        cities:["Johannesburg","Cape Town","Durban","Pretoria"],
        first:["Liam","Thabo","Sipho","Daniel","Ethan","Zanele","Aisha","Maya","Lerato"],
        last:["Nkosi","Dlamini","Mokoena","Naidoo","Pillay"]
    }
];

/* =========================================================
   WORLDS
========================================================= */

const WORLD_CATALOG = [
    {
        type:"video-game",
        name:"Fantasy RPG",
        emoji:"⚔️",
        locations:["Moonfall Village","Ironroot Forest","Kingdom of Eldoria","Whispering Ruins"]
    },
    {
        type:"video-game",
        name:"MMORPG",
        emoji:"🛡️",
        locations:["Central Spawn","Crystal Harbor","Guild District","Old Market"]
    },
    {
        type:"video-game",
        name:"Dungeon Crawler",
        emoji:"🏰",
        locations:["Dungeon Entrance","Floor 17","Potion Alley","Boss Room Lobby"]
    },
    {
        type:"video-game",
        name:"Survival Game",
        emoji:"🏕️",
        locations:["Pine Camp","Abandoned Factory","River Base","Northern Outpost"]
    },
    {
        type:"video-game",
        name:"Sandbox Game",
        emoji:"🧱",
        locations:["Spawn Village","Redstone District","Sky Island","Creeper Plains"]
    },
    {
        type:"video-game",
        name:"Farming Sim",
        emoji:"🌾",
        locations:["Sunflower Farm","Green Valley","Market Town","Windmill Road"]
    },
    {
        type:"video-game",
        name:"Sci-Fi Game",
        emoji:"🚀",
        locations:["Orbital Station","Mars Colony","Neon Sector","Outer Rim"]
    },
    {
        type:"video-game",
        name:"Horror Game",
        emoji:"👻",
        locations:["Old Hospital","Foggy Town","Basement Level","Abandoned Motel"]
    },
    {
        type:"video-game",
        name:"Soulslike",
        emoji:"🔥",
        locations:["Ashen Cathedral","Forgotten Keep","Black Marsh","Ruined Capital"]
    },
    {
        type:"video-game",
        name:"Tactical Game",
        emoji:"🎯",
        locations:["Command Center","Training Yard","Northern Front","Watchtower"]
    },

    {
        type:"novel",
        name:"Fantasy Novel",
        emoji:"📖",
        locations:["Royal Capital","Mage Quarter","Ancient Library","Dragon Pass"]
    },
    {
        type:"novel",
        name:"Detective Mystery",
        emoji:"🕵️",
        locations:["Rainy District","Police Archive","Old Theater","Harbor Street"]
    },
    {
        type:"novel",
        name:"Romance Novel",
        emoji:"🌹",
        locations:["Riverside Café","Old Bookshop","University Street","Seaside Hotel"]
    },
    {
        type:"novel",
        name:"Dystopian Fiction",
        emoji:"🏙️",
        locations:["Sector 9","Central Authority","Lower District","Checkpoint 4"]
    },
    {
        type:"novel",
        name:"Historical Fiction",
        emoji:"🏛️",
        locations:["Old Capital","Market Square","Royal Court","Harbor Quarter"]
    },
    {
        type:"novel",
        name:"Sci-Fi Novel",
        emoji:"🪐",
        locations:["Orbital Colony","Lunar City","Research Ring","Deep Space Port"]
    },
    {
        type:"novel",
        name:"Mystery Novel",
        emoji:"🔎",
        locations:["Fog Street","Manor House","Village Station","Locked Library"]
    },

    {
        type:"manhwa",
        name:"Dungeon Hunter",
        emoji:"🗡️",
        locations:["Hunter Association","Gate District","Ranker Plaza","Dungeon Lobby"]
    },
    {
        type:"manhwa",
        name:"Regression",
        emoji:"⏳",
        locations:["Second Timeline","Academy Gate","Future Capital","Old Guild Hall"]
    },
    {
        type:"manhwa",
        name:"Tower",
        emoji:"🗼",
        locations:["Tower Floor 1","Tower Floor 50","Ranker Lobby","Testing Room"]
    },
    {
        type:"manhwa",
        name:"Murim",
        emoji:"🥋",
        locations:["Mountain Sect","Training Yard","Tea House","Martial Market"]
    },
    {
        type:"manhwa",
        name:"Academy",
        emoji:"🎓",
        locations:["Magic Academy","Dormitory","Training Hall","Library Wing"]
    },
    {
        type:"manhwa",
        name:"Villainess",
        emoji:"👑",
        locations:["Royal Ballroom","Noble District","Garden Palace","Tea Room"]
    },
    {
        type:"manhwa",
        name:"Hunter Guild",
        emoji:"🏹",
        locations:["Guild Office","Raid Gate","Hunter Café","Equipment Shop"]
    },

    {
        type:"comic",
        name:"DC Comics — Gotham City",
        emoji:"🦇",
        locations:["Gotham Docks","Crime Alley","Wayne District","Gotham Market"]
    },
    {
        type:"comic",
        name:"DC Comics — Metropolis",
        emoji:"🦸",
        locations:["Metropolis Downtown","Daily Planet District","Centennial Park","West End"]
    },
    {
        type:"comic",
        name:"DC Comics — Central City",
        emoji:"⚡",
        locations:["Central City Station","Downtown","Police Lab","Riverside"]
    },
    {
        type:"comic",
        name:"DC Comics — Themyscira",
        emoji:"🏛️",
        locations:["Island Harbor","Training Grounds","Temple Road","Royal Gardens"]
    },
    {
        type:"comic",
        name:"Marvel Comics — New York",
        emoji:"🕷️",
        locations:["Queens","Hell's Kitchen","Midtown","Brooklyn"]
    },
    {
        type:"comic",
        name:"Marvel Comics — Wakanda",
        emoji:"🐾",
        locations:["Golden City","Market District","Research Center","Royal Road"]
    },
    {
        type:"comic",
        name:"Marvel Comics — Asgard",
        emoji:"⚡",
        locations:["Rainbow Bridge","Royal Road","Golden Hall","Market Square"]
    },
    {
        type:"comic",
        name:"Superhero Comic City",
        emoji:"💥",
        locations:["Hero Plaza","Villain District","City Hall","Metro Station"]
    },
    {
        type:"comic",
        name:"Noir Comic Universe",
        emoji:"🕶️",
        locations:["Rainy Boulevard","Back Alley","Neon Club","Old Station"]
    },
    {
        type:"comic",
        name:"Cosmic Comic Universe",
        emoji:"🌌",
        locations:["Starport","Nebula Market","Orbital City","Void Station"]
    },
    {
        type:"comic",
        name:"Supernatural Comic Town",
        emoji:"🌙",
        locations:["Old Cemetery","Moonlit Street","Occult Bookshop","Forest Edge"]
    },
    {
        type:"comic",
        name:"Indie Slice-of-Life Comic",
        emoji:"☕",
        locations:["Corner Café","Apartment Block","Local Bookshop","Bus Stop"]
    },

    {
        type:"real-world",
        name:"Real World — City Life",
        emoji:"🏙️",
        locations:["Downtown","Bus Stop","Office District","Shopping Street"]
    },
    {
        type:"real-world",
        name:"Real World — Café",
        emoji:"☕",
        locations:["Corner Café","Coffee Counter","Back Kitchen","Window Table"]
    },
    {
        type:"real-world",
        name:"Real World — Office",
        emoji:"💼",
        locations:["Open Office","Meeting Room","Reception","Break Room"]
    },
    {
        type:"real-world",
        name:"Real World — School",
        emoji:"🏫",
        locations:["Classroom","Staff Room","Library","School Gate"]
    },
    {
        type:"real-world",
        name:"Real World — Hospital",
        emoji:"🏥",
        locations:["Reception","Staff Corridor","Cafeteria","Waiting Area"]
    },
    {
        type:"real-world",
        name:"Real World — Shop",
        emoji:"🏪",
        locations:["Front Counter","Storage Room","Market Street","Cash Desk"]
    },
    {
        type:"real-world",
        name:"Real World — Transport",
        emoji:"🚌",
        locations:["Bus Terminal","Railway Station","Taxi Stand","Platform"]
    },
    {
        type:"real-world",
        name:"Real World — Workshop",
        emoji:"🔧",
        locations:["Garage","Workshop Floor","Tool Room","Service Desk"]
    }
];

/* =========================================================
   NPC JOBS
========================================================= */

const JOBS = [
    "Barista",
    "Receptionist",
    "Teacher",
    "Librarian",
    "Mechanic",
    "Delivery Rider",
    "Security Guard",
    "Cashier",
    "Shopkeeper",
    "Photographer",
    "Office Worker",
    "Software Developer",
    "Chef",
    "Waiter",
    "Taxi Driver",
    "Bus Conductor",
    "Hotel Receptionist",
    "Farmer",
    "Warehouse Worker",
    "Bookstore Clerk",
    "Electrician",
    "Graphic Designer",
    "Nurse",
    "Journalist",
    "Accountant",
    "Construction Worker",
    "Cleaner",
    "Sales Assistant",
    "Florist",
    "Bakery Worker"
];

/* =========================================================
   NPC PERSONALITIES
========================================================= */

const PERSONALITIES = [
    "quiet observer",
    "overly enthusiastic",
    "sarcastic realist",
    "friendly gossip",
    "professional complainer",
    "optimistic disaster",
    "sleep-deprived worker",
    "mysteriously calm",
    "permanent side-quest energy",
    "local legend according to exactly three people",
    "extremely literal",
    "accidentally philosophical",
    "chaotic but polite",
    "suspiciously organized",
    "quietly ambitious",
    "dramatic for no reason",
    "helpful but exhausted",
    "competitive about everything"
];

/* =========================================================
   POST TEMPLATES
========================================================= */

const POST_TEMPLATES = [

    "The hero came back today. Apparently he needed another identical healing potion. I have been selling him the same bottle for three years. Neither of us has questioned this.",

    "Someone asked me where the castle is. I pointed directly at it. They walked into a tree.",

    "I have one line of dialogue. They have heard it 847 times. Somehow I am the repetitive one.",

    "The chosen one saved the kingdom today. Immediately afterwards, they stole someone's horse.",

    "Management announced that we are now 'living our best NPC lives.' They also removed our pensions.",

    "A stranger walked into my shop, opened every chest, broke three chairs and left without buying anything.",

    "I watched someone spend twenty minutes deciding which door to open. Both doors lead to the same room.",

    "The boss fight started at 9:00. I am technically still waiting for the cutscene to finish.",

    "My entire job is standing here until someone walks close enough to activate my dialogue.",

    "I have been guarding this bridge for six years. Nobody has ever asked what is under it.",

    "A player asked if this quest was optional. I have been standing here holding the quest item since Tuesday.",

    "Today someone complimented my hat. This is the best character development I have received all year.",

    "The legendary warrior bought three sandwiches and asked if I had a loyalty card.",

    "I saw the main character today. They were carrying seventeen swords and absolutely no food.",

    "The adventurer sold me a rare magical sword for the price of a sandwich. I am beginning to suspect the economy is broken.",

    "My shift ends when the hero leaves town. The hero has been in town for eleven hours.",

    "The prophecy said a great warrior would arrive. A confused tourist arrived instead. We gave them the prophecy anyway.",

    "I work at the inn. The same party has rented the same room for six months and somehow never sleeps.",

    "The wizard asked for directions to the library. I pointed at the building labelled LIBRARY.",

    "Someone tried to intimidate me by dramatically removing their sunglasses. It was nighttime.",

    "Today I learned that being a background character does not exempt you from paperwork.",

    "The guild board has 37 quests. Every single one involves collecting something from the same forest.",

    "I opened the shop this morning. A legendary warrior immediately sold me seventeen spoons.",

    "A mysterious stranger entered town during a thunderstorm. Turns out they were just looking for the bus stop.",

    "The dungeon has a secret door. I know because I installed it.",

    "Nobody notices the NPCs until they need directions.",

    "I have never seen the final boss. I have, however, seen everyone return from there and complain about the music.",

    "Today a customer asked if the item was rare. I said yes. They bought six.",

    "The quest giver next door has started using motivational quotes. Morale is somehow worse.",

    "Someone asked whether the sword was cursed. I said probably. They bought it anyway.",

    "My workplace has a mysterious locked room. Management calls it 'the server room.' The adventurers call it 'bonus content.'",

    "The hero said they would return tomorrow. They always say tomorrow.",

    "I saw the same person die seven times today. They kept coming back like nothing happened.",

    "The town guard has officially banned people from jumping on the furniture. The furniture has filed an appeal.",

    "A customer complained that my dialogue options were too limited. I have filed a complaint with management.",

    "Someone stole the town bell. Nobody knows why. Everyone is pretending this is normal.",

    "The blacksmith says business is slow. Then three heroes arrived carrying broken swords.",

    "I asked the mage why they were glowing. They said it was 'a passive effect.' I regret asking.",

    "Today was peaceful. Suspiciously peaceful. I expect a dragon by dinner.",

    "My manager said the customer is always right. The customer asked me where the moon is.",

    "I spent the whole day polishing the same sword. Nobody has ever bought it.",

    "The delivery arrived three days early. The customer accused us of time travel.",

    "My boss scheduled a meeting to discuss why nobody attends meetings.",

    "Someone stole the office stapler. The investigation has been going on for two weeks.",

    "I said I was five minutes away. Traffic has now become a philosophical problem.",

    "The coffee machine made a noise that sounded like a warning. We all ignored it.",

    "My shift started at 8. The clock says 8:03. Management says I am already late.",

    "A customer asked for decaf and then ordered three energy drinks.",

    "The printer has been broken for six months. Today it printed one page by itself. Nobody wants to talk about it.",

    "The library is quiet until someone whispers loudly about how quiet the library is.",

    "I organized the entire storage room. Someone immediately moved everything.",

    "The elevator stopped on every floor today. It has become a sightseeing tour.",

    "My lunch break lasted twelve minutes. Seven were spent finding somewhere to sit.",

    "A customer returned an item because it 'felt suspicious.' Honestly, fair.",

    "The meeting could have been an email. The email could have been silence.",

    "Someone asked me to fix their computer. It was not plugged in.",

    "I have explained the same policy seventeen times today. The policy has not changed.",

    "My neighbor bought a new lawn chair and now considers themselves an outdoor enthusiast.",

    "The bus was late. Everyone complained. Then it arrived early tomorrow.",

    "A tourist asked me where the famous local landmark was while standing directly beside it.",

    "The café ran out of cups. We have entered a new phase of civilization.",

    "I accidentally waved back at someone who was waving at a person behind me. We are now friends.",

    "My phone battery is at 3%. I have chosen optimism.",

    "The weather app said clear skies. The sky has submitted a rebuttal.",

    "I went to the supermarket for one thing. I returned with twelve things and forgot the one thing.",

    "I have no idea what is happening, but everyone else is walking quickly, so I am walking quickly too.",

    "The mechanic said the car makes a strange noise. I said it has always made that noise. He stared at me for ten seconds.",

    "The receptionist asked who I was here to see. I forgot why I came.",

    "I spent an hour looking for my glasses. They were on my head.",

    "The office group chat has 96 unread messages. I am choosing peace.",

    "I cleaned the counter five minutes ago. Someone has already spilled coffee on it.",

    "The shop is closing in ten minutes. Suddenly everyone has urgent shopping to do.",

    "My coworker said 'quick question.' It was not a quick question.",

    "The librarian gave me a look because I laughed. The book was funny.",

    "I arrived early. This is not a personality trait. I simply misunderstood the time.",

    "The delivery address said 'blue door.' There are seventeen blue doors.",

    "I fixed the machine. It immediately broke again out of respect.",

    "Someone asked if I work here while I was wearing the uniform, name badge and standing behind the counter.",

    "I am not saying the office printer is haunted. I am saying it knows when I am in a hurry.",

    "Today I discovered a shortcut. It took longer than the normal route.",

    "My boss said we need to think outside the box. We are still inside the meeting room.",

    "I made a to-do list. Writing the list became item number one.",

    "The customer said 'no rush.' Then checked the time six times.",

    "I have mastered the art of looking busy when there is absolutely nothing to do."
];

/* =========================================================
   WORLD-SPECIFIC TEMPLATES
========================================================= */

const SPECIAL_POSTS = {
    "Gotham": [
        "The rain started again. Gotham apparently has a subscription.",
        "Someone left a mysterious package outside the shop. I am not touching it. I have learned from previous incidents.",
        "The night shift is quiet. Too quiet. Somewhere, a dramatic cape is probably moving across a rooftop."
    ],
    "Metropolis": [
        "Something flew over the city at impossible speed. I was more concerned about my sandwich.",
        "The skyline looks beautiful today. Someone is repairing another building. Again.",
        "A superhero battle happened three blocks away. Management still expects everyone to arrive on time."
    ],
    "Marvel": [
        "The city had another super-powered incident. The coffee shop stayed open anyway.",
        "Someone dropped a strange piece of technology on the sidewalk. Nobody knows who owns it.",
        "I have officially stopped being surprised when something explodes downtown."
    ],
    "Dungeon": [
        "Another adventurer asked me whether Floor 17 is dangerous. I said yes. They asked if the loot is good. I said yes. They went anyway.",
        "The dungeon receptionist has processed 400 raid parties this month.",
        "Someone defeated the boss and immediately asked where the nearest snack shop was."
    ],
    "Tower": [
        "Floor 50 has a boss. Floor 49 has paperwork. Somehow the paperwork is scarier.",
        "Everyone wants to climb the tower. Nobody wants to clean the stairs.",
        "A ranker asked for directions. I pointed upward. That was apparently sufficient."
    ],
    "Hunter": [
        "The guild is full again. Someone brought a sword longer than the meeting table.",
        "A hunter sold three rare items and immediately spent all the money on snacks.",
        "The gate opened at 9. Everyone arrived at 8:30 and complained about waiting."
    ]
};

/* =========================================================
   APP STATE
========================================================= */

let npcs = [];
let posts = [];
let currentUser = null;
let currentView = "home";
let currentProfileId = null;
let searchTerm = "";
let usedNames = new Set();
let usedHandles = new Set();
let usedPostSignatures = new Set();
let feedMode = "home";

/* =========================================================
   AVATARS
========================================================= */

function avatarFor(seed){
    return "https://api.dicebear.com/9.x/adventurer/svg?seed=" +
        encodeURIComponent(seed);
}

/* =========================================================
   NPC GENERATION
========================================================= */

function makeName(country){
    let attempts = 0;

    while(attempts < 100){
        attempts++;

        const first = pick(country.first);
        const last = pick(country.last);
        const name = first + " " + last;

        if(!usedNames.has(name)){
            usedNames.add(name);
            return name;
        }
    }

    return pick(country.first) + " " + pick(country.last) + " " + rand(9999);
}

function makeHandle(name){
    const base = name
        .toLowerCase()
        .replace(/[^a-z0-9]+/g,"")
        .slice(0,18);

    let handle = "@" + base;

    if(usedHandles.has(handle)){
        handle = "@" + base + rand(99999);
    }

    usedHandles.add(handle);
    return handle;
}

function makeNPC(forceWorld=null){

    const country = pick(COUNTRY_DATA);
    const name = makeName(country);
    const world = forceWorld || pick(WORLD_CATALOG);

    let job;

    if(world.type === "real-world"){
        job = pick(JOBS);
    }else{
        job = pick([
            "Merchant",
            "Quest Giver",
            "Blacksmith",
            "Innkeeper",
            "Guard",
            "Healer",
            "Scout",
            "Archivist",
            "Guild Clerk",
            "Village Baker",
            "Potion Seller",
            "Map Maker",
            "Shopkeeper",
            "Courier",
            "Gatekeeper",
            "Trainer"
        ]);
    }

    const personality = pick(PERSONALITIES);
    const location = pick(
        world.locations.length
            ? world.locations
            : country.cities
    );

    const id = uid("npc");

    const npc = {
        id,
        name,
        handle:makeHandle(name),
        country:country.country,
        location,
        avatar:avatarFor(name + id),
        cover:avatarFor("cover-" + id),
        job,
        bio:buildBio(name,job,personality,world),
        personality,
        npcType:world.type === "real-world" ? "Real Person NPC" : "Fictional World NPC",
        worldType:world.type,
        world:world.name,
        worldEmoji:world.emoji,
        level:rand(100)+1,
        followers:rand(90000)+120,
        following:rand(1800)+20,
        online:chance(45),
        verified:chance(8),
        posts:[]
    };

    npcs.push(npc);

    return npc;
}

function buildBio(name,job,personality,world){
    const bios = [
        `${job} in ${world.name}. ${personality}.`,
        `${job} • ${personality} • currently surviving ${world.name}.`,
        `Just another ${job} trying to finish today's quest.`,
        `${job} with permanent side-quest energy.`,
        `I work here. Apparently that makes me important.`,
        `${personality}. Professionally employed as a ${job}.`,
        `Background character. Unexpectedly opinionated.`
    ];

    return pick(bios);
}

/* =========================================================
   POST GENERATION
========================================================= */

function specialTemplateFor(worldName){
    if(worldName.includes("Gotham")) return pick(SPECIAL_POSTS.Gotham);
    if(worldName.includes("Metropolis")) return pick(SPECIAL_POSTS.Metropolis);
    if(worldName.includes("Marvel")) return pick(SPECIAL_POSTS.Marvel);
    if(worldName.includes("Dungeon")) return pick(SPECIAL_POSTS.Dungeon);
    if(worldName.includes("Tower")) return pick(SPECIAL_POSTS.Tower);
    if(worldName.includes("Hunter")) return pick(SPECIAL_POSTS.Hunter);

    return null;
}

function createPost(npc){

    let text;
    let attempts = 0;

    while(attempts < 100){
        attempts++;

        const special = specialTemplateFor(npc.world);

        if(special && chance(35)){
            text = special;
        }else{
            text = pick(POST_TEMPLATES);
        }

        const signature = npc.id + "|" + text;

        if(!usedPostSignatures.has(signature)){
            usedPostSignatures.add(signature);
            break;
        }
    }

    const post = {
        id:uid("post"),
        authorId:npc.id,
        text,
        timestamp:randomTimestamp(),
        likes:rand(9000),
        comments:rand(800),
        shares:rand(500),
        reposts:rand(300),
        saves:rand(900),
        media:chance(19),
        tag:pick([
            "NPC Life",
            "Side Quest",
            "Daily Routine",
            "Lore",
            "Quest Update",
            "Work",
            "World Event",
            "Unimportant News"
        ]),
        world:npc.world,
        reactions:{
            laugh:rand(300),
            fire:rand(200),
            confused:rand(180)
        },
        isLiked:false,
        isSaved:false,
        isReposted:false,
        commentsList:[]
    };

    posts.push(post);
    npc.posts.push(post.id);

    return post;
}

function randomTimestamp(){
    const minutes = rand(60*24*8);
    return Date.now() - minutes * 60 * 1000;
}

/* =========================================================
   GENERATE WORLD
========================================================= */

function generateWorld(){

    npcs = [];
    posts = [];
    usedNames = new Set();
    usedHandles = new Set();
    usedPostSignatures = new Set();

    const count = 22 + rand(10);

    for(let i=0;i<count;i++){
        const npc = makeNPC();

        const postCount = 2 + rand(3);

        for(let p=0;p<postCount;p++){
            createPost(npc);
        }
    }

    currentUser = npcs[0];

    renderEverything();
}

/* =========================================================
   RENDER
========================================================= */

function renderEverything(){
    renderUser();
    renderHomeFeed();
    renderWidgets();
}

function renderUser(){

    if(!currentUser) return;

    document.getElementById("topAvatar").src = currentUser.avatar;
    document.getElementById("sideAvatar").src = currentUser.avatar;
    document.getElementById("sideName").textContent = currentUser.name;
    document.getElementById("sideHandle").textContent = currentUser.handle;
}

function getNPC(id){
    return npcs.find(n => n.id === id);
}

function getPost(id){
    return posts.find(p => p.id === id);
}

function sortedPosts(){
    return [...posts].sort((a,b) => b.timestamp - a.timestamp);
}

function filteredPosts(){

    let result = sortedPosts();

    if(searchTerm.trim()){
        const q = searchTerm.toLowerCase();

        result = result.filter(post => {

            const npc = getNPC(post.authorId);

            return (
                post.text.toLowerCase().includes(q) ||
                post.world.toLowerCase().includes(q) ||
                post.tag.toLowerCase().includes(q) ||
                npc.name.toLowerCase().includes(q) ||
                npc.handle.toLowerCase().includes(q) ||
                npc.country.toLowerCase().includes(q)
            );
        });
    }

    return result;
}

function renderHomeFeed(){

    if(currentView !== "home") return;

    const feed = document.getElementById("feedContent");

    document.getElementById("feedTitle").textContent =
        searchTerm ? "Search Results" : "Home";

    document.getElementById("feedSubtitle").textContent =
        searchTerm
            ? `Searching for "${searchTerm}"`
            : "Fresh NPC activity from multiple worlds.";

    let html = "";

    if(!searchTerm){
        html += renderComposer();
    }

    const list = filteredPosts();

    if(!list.length){
        html += `
            <div class="empty">
                <div class="empty-icon">🫥</div>
                <strong>No NPCs found.</strong>
                <div>Try another search.</div>
            </div>
        `;
    }else{
        list.forEach(post => {
            html += renderPost(post);
        });
    }

    feed.innerHTML = html;
}

function renderComposer(){

    return `
        <div class="composer" id="composer">
            <div class="composer-top">
                <img class="composer-avatar"
                     src="${escapeHTML(currentUser.avatar)}"
                     alt="${escapeHTML(currentUser.name)}">

                <textarea
                    id="composerText"
                    maxlength="1000"
                    placeholder="What is happening in your NPC life?"
                ></textarea>
            </div>

            <div class="composer-bottom">

                <div class="composer-tools">
                    <button class="composer-tool" onclick="addComposerHint('📷')" title="Add media">📷</button>
                    <button class="composer-tool" onclick="addComposerHint('🎮')" title="Game">🎮</button>
                    <button class="composer-tool" onclick="addComposerHint('📍')" title="Location">📍</button>
                    <button class="composer-tool" onclick="addComposerHint('😂')" title="Emoji">😂</button>
                    <button class="composer-tool" onclick="generatePostIdea()" title="Random idea">✨</button>
                </div>

                <button class="post-btn" onclick="createUserPost()">
                    Post
                </button>

            </div>
        </div>
    `;
}

function renderPost(post){

    const npc = getNPC(post.authorId);

    if(!npc) return "";

    const comments = post.commentsList || [];

    return `
        <article class="post" id="${escapeHTML(post.id)}">

            <div class="post-head">

                <button class="avatar-btn"
                        onclick="openProfile('${escapeHTML(npc.id)}')"
                        aria-label="Open ${escapeHTML(npc.name)} profile">

                    <img
                        class="post-avatar"
                        src="${escapeHTML(npc.avatar)}"
                        alt="${escapeHTML(npc.name)}"
                    >

                </button>

                <div class="post-author">

                    <div class="author-line">

                        <span
                            class="author-name"
                            onclick="openProfile('${escapeHTML(npc.id)}')"
                        >
                            ${escapeHTML(npc.name)}
                        </span>

                        ${npc.verified ? `<span class="verified">✓</span>` : ""}

                        <span class="author-handle">
                            ${escapeHTML(npc.handle)}
                        </span>

                        <span class="post-time">
                            · ${formatTime(post.timestamp)}
                        </span>

                    </div>

                    <div class="post-meta">

                        <span class="world-badge">
                            ${escapeHTML(npc.worldEmoji)} ${escapeHTML(npc.world)}
                        </span>

                        <span>•</span>

                        <span>${escapeHTML(post.tag)}</span>

                    </div>

                </div>

                <button
                    class="more-btn"
                    onclick="postMenu('${escapeHTML(post.id)}')"
                    title="More"
                >
                    ⋯
                </button>

            </div>

            <div class="post-text">
                ${escapeHTML(post.text)}
            </div>

            ${
                post.media
                ?
                `
                <div class="post-media">
                    <div class="media-overlay">
                        <div class="media-title">
                            ${escapeHTML(npc.worldEmoji)} ${escapeHTML(post.tag)}
                        </div>
                        <div class="media-caption">
                            Scene from ${escapeHTML(npc.world)}
                        </div>
                    </div>
                </div>
                `
                :
                ""
            }

            <div class="post-actions">

                <button
                    class="action-btn ${post.isLiked ? "liked" : ""}"
                    onclick="toggleLike('${escapeHTML(post.id)}')"
                    title="Like"
                >
                    <span>${post.isLiked ? "❤️" : "♡"}</span>
                    <span class="action-label">Like</span>
                    <span class="action-count">${formatNumber(post.likes)}</span>
                </button>

                <button
                    class="action-btn"
                    onclick="toggleComments('${escapeHTML(post.id)}')"
                    title="Comment"
                >
                    <span>💬</span>
                    <span class="action-label">Comment</span>
                    <span class="action-count">${formatNumber(post.comments)}</span>
                </button>

                <button
                    class="action-btn ${post.isReposted ? "reposted" : ""}"
                    onclick="repost('${escapeHTML(post.id)}')"
                    title="Repost"
                >
                    <span>🔁</span>
                    <span class="action-label">Repost</span>
                    <span class="action-count">${formatNumber(post.reposts)}</span>
                </button>

                <button
                    class="action-btn"
                    onclick="sharePost('${escapeHTML(post.id)}')"
                    title="Share"
                >
                    <span>📤</span>
                    <span class="action-label">Share</span>
                    <span class="action-count">${formatNumber(post.shares)}</span>
                </button>

                <button
                    class="action-btn ${post.isSaved ? "saved" : ""}"
                    onclick="toggleSave('${escapeHTML(post.id)}')"
                    title="Save"
                >
                    <span>${post.isSaved ? "🔖" : "🏷️"}</span>
                    <span class="action-label">Save</span>
                </button>

            </div>

            <div id="comments-${escapeHTML(post.id)}" class="hidden">

                ${
                    comments.length
                    ?
                    `
                    <div class="comments-list">
                        ${comments.map(comment => `
                            <div class="comment">
                                <div class="comment-author">
                                    ${escapeHTML(comment.author)}
                                </div>
                                <div class="comment-text">
                                    ${escapeHTML(comment.text)}
                                </div>
                            </div>
                        `).join("")}
                    </div>
                    `
                    :
                    ""
                }

                <div class="comment-box">

                    <input
                        id="comment-input-${escapeHTML(post.id)}"
                        type="text"
                        maxlength="300"
                        placeholder="Write a comment..."
                        onkeydown="commentKey(event,'${escapeHTML(post.id)}')"
                    >

                    <button
                        class="comment-send"
                        onclick="addComment('${escapeHTML(post.id)}')"
                    >
                        Send
                    </button>

                </div>

            </div>

            ${
                comments.length
                ?
                `
                <div class="comment-preview">
                    <strong>${escapeHTML(comments[comments.length-1].author)}</strong>
                    · ${escapeHTML(comments[comments.length-1].text)}
                </div>
                `
                :
                ""
            }

        </article>
    `;
}

/* =========================================================
   FEED ACTIONS
========================================================= */

function toggleLike(id){

    const post = getPost(id);

    if(!post) return;

    if(post.isLiked){
        post.isLiked = false;
        post.likes = Math.max(0,post.likes - 1);
        toast("Like removed");
    }else{
        post.isLiked = true;
        post.likes++;
        toast("❤️ Liked");
    }

    refreshPost(id);
}

function toggleSave(id){

    const post = getPost(id);

    if(!post) return;

    post.isSaved = !post.isSaved;

    toast(post.isSaved ? "🔖 Saved" : "Removed from saved");

    refreshPost(id);
}

function repost(id){

    const post = getPost(id);

    if(!post) return;

    if(post.isReposted){
        post.isReposted = false;
        post.reposts = Math.max(0,post.reposts - 1);
        toast("Repost removed");
    }else{
        post.isReposted = true;
        post.reposts++;
        toast("🔁 Reposted");
    }

    refreshPost(id);
}

function sharePost(id){

    const post = getPost(id);

    if(!post) return;

    post.shares++;

    const text =
        `NPCBook: ${post.text}`;

    if(navigator.share){

        navigator.share({
            title:"NPCBook",
            text
        }).then(()=>{
            toast("📤 Shared");
        }).catch(()=>{
            toast("Share cancelled");
        });

    }else{

        if(navigator.clipboard){
            navigator.clipboard.writeText(text)
                .then(()=>{
                    toast("📋 Post copied to clipboard");
                })
                .catch(()=>{
                    toast("📤 Share link prepared");
                });
        }else{
            toast("📤 Share action completed");
        }
    }

    refreshPost(id);
}

function toggleComments(id){

    const box = document.getElementById("comments-" + id);

    if(!box) return;

    box.classList.toggle("hidden");

    if(!box.classList.contains("hidden")){

        const input =
            document.getElementById("comment-input-" + id);

        if(input){
            setTimeout(()=>input.focus(),100);
        }
    }
}

function commentKey(event,id){

    if(event.key === "Enter"){
        event.preventDefault();
        addComment(id);
    }
}

function addComment(id){

    const post = getPost(id);

    if(!post) return;

    const input =
        document.getElementById("comment-input-" + id);

    if(!input) return;

    const text = input.value.trim();

    if(!text){
        toast("Write something first");
        return;
    }

    if(!post.commentsList){
        post.commentsList = [];
    }

    post.commentsList.push({
        id:uid("comment"),
        author:currentUser.name,
        text
    });

    post.comments++;

    input.value = "";

    toast("💬 Comment posted");

    refreshPost(id);

    setTimeout(()=>{
        const box = document.getElementById("comments-" + id);

        if(box){
            box.classList.remove("hidden");
        }
    },30);
}

function refreshPost(id){

    if(currentView !== "home") return;

    const postElement = document.getElementById(id);

    if(!postElement) return;

    const post = getPost(id);

    if(!post) return;

    postElement.outerHTML = renderPost(post);

    const commentsBox =
        document.getElementById("comments-" + id);

    if(commentsBox && post.commentsList.length){
        commentsBox.classList.remove("hidden");
    }
}

function postMenu(id){

    const post = getPost(id);

    if(!post) return;

    showModal(
        "Post Options",
        `
        <div class="option-grid">

            <button class="option-card" onclick="toggleSave('${escapeHTML(id)}');closeModal()">
                <strong>🔖 Save / Unsave</strong>
                <span>Keep this post available in your temporary world.</span>
            </button>

            <button class="option-card" onclick="sharePost('${escapeHTML(id)}');closeModal()">
                <strong>📤 Share</strong>
                <span>Share this NPC post.</span>
            </button>

            <button class="option-card" onclick="repost('${escapeHTML(id)}');closeModal()">
                <strong>🔁 Repost</strong>
                <span>Add this post to your temporary activity.</span>
            </button>

            <button class="option-card" onclick="copyPost('${escapeHTML(id)}')">
                <strong>📋 Copy</strong>
                <span>Copy the post text.</span>
            </button>

        </div>
        `
    );
}

function copyPost(id){

    const post = getPost(id);

    if(!post) return;

    if(navigator.clipboard){
        navigator.clipboard.writeText(post.text)
            .then(()=>{
                toast("📋 Copied");
                closeModal();
            });
    }else{
        toast("Copy unavailable on this browser");
    }
}

/* =========================================================
   CREATE USER POST
========================================================= */

function createUserPost(){

    const input = document.getElementById("composerText");

    if(!input) return;

    const text = input.value.trim();

    if(!text){
        toast("Write something before posting");
        input.focus();
        return;
    }

    const post = {
        id:uid("post"),
        authorId:currentUser.id,
        text,
        timestamp:Date.now(),
        likes:0,
        comments:0,
        shares:0,
        reposts:0,
        saves:0,
        media:false,
        tag:"My NPC Post",
        world:currentUser.world,
        reactions:{
            laugh:0,
            fire:0,
            confused:0
        },
        isLiked:false,
        isSaved:false,
        isReposted:false,
        commentsList:[]
    };

    posts.unshift(post);
    currentUser.posts.unshift(post.id);

    input.value = "";

    toast("🚀 Your NPC post is live");

    renderHomeFeed();
}

function addComposerHint(symbol){

    const input = document.getElementById("composerText");

    if(!input) return;

    input.value += " " + symbol + " ";
    input.focus();
}

function generatePostIdea(){

    const input = document.getElementById("composerText");

    if(!input) return;

    const ideas = [
        "Today I discovered that my workplace has a secret side quest.",
        "I have officially become the NPC everyone asks for directions.",
        "Nobody prepared me for today's random encounter.",
        "My daily routine has become suspiciously repetitive.",
        "Someone just gave me a quest and forgot the reward.",
        "I survived another completely normal NPC day.",
        "Breaking news: I have absolutely no idea what is happening."
    ];

    input.value = pick(ideas);
    input.focus();
}

function focusComposer(){

    goHome();

    setTimeout(()=>{
        const composer = document.getElementById("composer");

        if(composer){
            composer.scrollIntoView({
                behavior:"smooth",
                block:"center"
            });

            const input = document.getElementById("composerText");

            if(input){
                input.focus();
            }
        }
    },50);
}

/* =========================================================
   PROFILE
========================================================= */

function openProfile(id){

    const npc = getNPC(id);

    if(!npc) return;

    currentView = "profile";
    currentProfileId = id;

    setNavActive("nav-profile");
    setMobileActive("mobile-profile");

    document.getElementById("feedTitle").textContent = "NPC Profile";
    document.getElementById("feedSubtitle").textContent =
        npc.handle;

    const feed = document.getElementById("feedContent");

    const profilePosts = posts
        .filter(p => p.authorId === id)
        .sort((a,b)=>b.timestamp-a.timestamp);

    feed.innerHTML = `
        <div class="profile-page">

            <div class="profile-cover"></div>

            <div class="profile-main">

                <div class="profile-top">

                    <img
                        class="profile-avatar"
                        src="${escapeHTML(npc.avatar)}"
                        alt="${escapeHTML(npc.name)}"
                    >

                    ${
                        npc.id === currentUser.id
                        ?
                        ""
                        :
                        `
                        <button
                            class="follow-btn ${npc.followingMe ? "following" : ""}"
                            onclick="toggleFollow('${escapeHTML(npc.id)}')"
                        >
                            ${npc.followingMe ? "Following" : "Follow"}
                        </button>
                        `
                    }

                </div>

                <div class="profile-name">
                    ${escapeHTML(npc.name)}
                    ${npc.verified ? `<span class="verified">✓</span>` : ""}
                </div>

                <div class="profile-handle">
                    ${escapeHTML(npc.handle)}
                </div>

                <div class="profile-bio">
                    ${escapeHTML(npc.bio)}
                </div>

                <div class="profile-info">
                    <span>📍 ${escapeHTML(npc.location)}, ${escapeHTML(npc.country)}</span>
                    <span>💼 ${escapeHTML(npc.job)}</span>
                    <span>${escapeHTML(npc.worldEmoji)} ${escapeHTML(npc.world)}</span>
                </div>

                <div class="profile-stats">
                    <div class="stat">
                        <strong>${formatNumber(npc.followers)}</strong> Followers
                    </div>

                    <div class="stat">
                        <strong>${formatNumber(npc.following)}</strong> Following
                    </div>

                    <div class="stat">
                        <strong>${profilePosts.length}</strong> Posts
                    </div>
                </div>

                <div class="profile-tabs">
                    <button class="profile-tab active">Posts</button>
                    <button class="profile-tab" onclick="toast('Replies view coming to this temporary world')">Replies</button>
                    <button class="profile-tab" onclick="showNPCMedia('${escapeHTML(npc.id)}')">Media</button>
                </div>

            </div>

        </div>

        <div style="height:14px"></div>

        ${
            profilePosts.length
            ?
            profilePosts.map(renderPost).join("")
            :
            `
            <div class="empty">
                <div class="empty-icon">📭</div>
                No posts yet.
            </div>
            `
        }
    `;

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });
}

function toggleFollow(id){

    const npc = getNPC(id);

    if(!npc) return;

    npc.followingMe = !npc.followingMe;

    if(npc.followingMe){
        npc.followers++;
        toast("👥 Following " + npc.name);
    }else{
        npc.followers = Math.max(0,npc.followers-1);
        toast("Unfollowed " + npc.name);
    }

    openProfile(id);
}

function showNPCMedia(id){

    const npc = getNPC(id);

    if(!npc) return;

    const mediaPosts =
        posts.filter(p => p.authorId === id && p.media);

    showModal(
        "Media — " + npc.name,
        mediaPosts.length
        ?
        mediaPosts.map(p=>`
            <div class="quest">
                <div class="quest-title">
                    ${escapeHTML(p.tag)}
                </div>
                <div class="quest-desc">
                    ${escapeHTML(p.text)}
                </div>
            </div>
        `).join("")
        :
        `<div class="empty">No media posts in this world.</div>`
    );
}

/* =========================================================
   NAVIGATION
========================================================= */

function goHome(){

    currentView = "home";
    currentProfileId = null;
    searchTerm = "";

    const input = document.getElementById("searchInput");

    if(input){
        input.value = "";
    }

    setNavActive("nav-home");
    setMobileActive("mobile-home");

    renderHomeFeed();

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });
}

function handleSearch(value){

    searchTerm = value.trim();

    currentView = "home";

    setNavActive("nav-home");
    setMobileActive("mobile-search");

    renderHomeFeed();
}

function focusSearch(){

    const input = document.getElementById("searchInput");

    if(input){
        input.focus();

        window.scrollTo({
            top:0,
            behavior:"smooth"
        });
    }
}

function setNavActive(id){

    document.querySelectorAll(".nav-item")
        .forEach(el=>el.classList.remove("active"));

    const el = document.getElementById(id);

    if(el){
        el.classList.add("active");
    }
}

function setMobileActive(id){

    document.querySelectorAll(".mobile-nav button")
        .forEach(el=>el.classList.remove("active"));

    const el = document.getElementById(id);

    if(el){
        el.classList.add("active");
    }
}

/* =========================================================
   RANDOM WORLD
========================================================= */

function newWorld(){

    toast("🎲 Generating a new temporary world...");

    setTimeout(()=>{
        generateWorld();
        goHome();
        toast("🌎 New NPC world generated");
    },80);
}

/* =========================================================
   RANDOM POST
========================================================= */

function randomPost(){

    if(!posts.length) return;

    const post = pick(posts);

    goHome();

    setTimeout(()=>{

        const el = document.getElementById(post.id);

        if(el){
            el.scrollIntoView({
                behavior:"smooth",
                block:"center"
            });

            el.animate(
                [
                    {transform:"scale(1)"},
                    {transform:"scale(1.02)"},
                    {transform:"scale(1)"}
                ],
                {
                    duration:500
                }
            );
        }

    },100);
}

/* =========================================================
   GENERATE NPC
========================================================= */

function generateNPC(){

    const npc = makeNPC();

    const amount = 2 + rand(3);

    for(let i=0;i<amount;i++){
        createPost(npc);
    }

    toast("✨ New NPC generated: " + npc.name);

    renderWidgets();

    if(currentView === "home"){
        renderHomeFeed();
    }else{
        openProfile(npc.id);
    }
}

/* =========================================================
   WIDGETS
========================================================= */

function renderWidgets(){

    const trends = [
        ["#NPCProblems",rand(900000)],
        ["#SideQuest",rand(700000)],
        ["#MainCharacter",rand(600000)],
        ["#QuestUpdate",rand(500000)],
        ["#LoreDrop",rand(400000)],
        ["#BackgroundCharacter",rand(350000)]
    ];

    document.getElementById("trendsWidget").innerHTML =
        trends.map(t=>`
            <div class="trend">
                <div class="trend-label">Trending</div>
                <div class="trend-name">${t[0]}</div>
                <div class="trend-count">${formatNumber(t[1])} posts</div>
            </div>
        `).join("");

    const quests = [
        ["Find the Lost Spoon","Ask three NPCs about a suspicious spoon.",rand(90)],
        ["Survive the Monday Boss Fight","Reach the end of your shift.",rand(80)],
        ["Collect 5 Side Quests","Interact with random NPCs.",rand(70)],
        ["Locate the Legendary Snack","The snack is probably nearby.",rand(60)]
    ];

    document.getElementById("questsWidget").innerHTML =
        quests.map(q=>`
            <div class="quest">
                <div class="quest-title">${q[0]}</div>
                <div class="quest-desc">${q[1]}</div>
                <div class="progress">
                    <div style="width:${q[2]}%"></div>
                </div>
            </div>
        `).join("");

    const people = [...npcs]
        .filter(n=>n.id !== currentUser.id)
        .sort(()=>Math.random()-.5)
        .slice(0,4);

    document.getElementById("peopleWidget").innerHTML =
        people.map(n=>`
            <div class="side-user-row" style="margin-bottom:12px">

                <img
                    src="${escapeHTML(n.avatar)}"
                    style="width:38px;height:38px;border-radius:50%;object-fit:cover"
                    alt=""
                >

                <div style="flex:1;min-width:0">
                    <div
                        style="font-size:13px;font-weight:800;cursor:pointer"
                        onclick="openProfile('${escapeHTML(n.id)}')"
                    >
                        ${escapeHTML(n.name)}
                    </div>

                    <div style="font-size:11px;color:var(--muted)">
                        ${escapeHTML(n.job)}
                    </div>
                </div>

                <button
                    onclick="toggleFollow('${escapeHTML(n.id)}')"
                    style="
                        border:1px solid var(--border);
                        background:transparent;
                        color:var(--text);
                        border-radius:9px;
                        min-height:34px;
                        padding:0 9px;
                        font-size:11px;
                    "
                >
                    Follow
                </button>

            </div>
        `).join("");
}

/* =========================================================
   TRENDING
========================================================= */

function showTrending(){

    currentView = "home";
    feedMode = "trending";

    setNavActive("nav-trending");
    setMobileActive("mobile-home");

    document.getElementById("feedTitle").textContent =
        "🔥 Trending";

    document.getElementById("feedSubtitle").textContent =
        "Posts with suspicious amounts of NPC activity.";

    const trending = [...posts]
        .sort((a,b)=>
            (b.likes+b.comments+b.shares) -
            (a.likes+a.comments+a.shares)
        )
        .slice(0,15);

    document.getElementById("feedContent").innerHTML =
        trending.map(renderPost).join("");

    window.scrollTo({top:0,behavior:"smooth"});
}

/* =========================================================
   QUESTS
========================================================= */

function showQuests(){

    currentView = "panel";

    setNavActive("nav-quests");
    setMobileActive("mobile-home");

    document.getElementById("feedTitle").textContent =
        "🎯 Quests";

    document.getElementById("feedSubtitle").textContent =
        "Every NPC needs unnecessary objectives.";

    const quests = [
        ["The Missing Key","Find the key that nobody actually lost.","23%"],
        ["Talk to 5 NPCs","Ask five people about absolutely nothing.","48%"],
        ["The Legendary Sandwich","Locate the sandwich before someone eats it.","71%"],
        ["Return the Book","A library book has been overdue for 12 years.","12%"],
        ["Defeat Monday","Survive a full Monday without starting a new career.","63%"],
        ["Unlock Secret Dialogue","Say something nobody has heard before.","4%"],
        ["Collect 100 Coins","Nobody knows why.","89%"],
        ["Find the Main Character","They are probably late.","37%"]
    ];

    document.getElementById("feedContent").innerHTML =
        quests.map(q=>`
            <div class="quest" style="margin-bottom:12px;padding:16px">
                <div class="quest-title" style="font-size:15px">
                    ${q[0]}
                </div>

                <div class="quest-desc" style="font-size:13px">
                    ${q[1]}
                </div>

                <div class="progress" style="height:7px">
                    <div style="width:${q[2]}"></div>
                </div>

                <div style="color:var(--muted);font-size:11px;margin-top:7px">
                    Progress ${q[2]}
                </div>
            </div>
        `).join("");

    window.scrollTo({top:0,behavior:"smooth"});
}

/* =========================================================
   MARKET
========================================================= */

function showMarket(){

    currentView = "panel";

    setNavActive("nav-market");
    setMobileActive("mobile-home");

    document.getElementById("feedTitle").textContent =
        "🛒 NPC Market";

    document.getElementById("feedSubtitle").textContent =
        "Completely unnecessary items for completely necessary NPCs.";

    const items = [
        ["🗡️ Slightly Used Hero Sword","+2 confidence, -7 durability","850 gold"],
        ["🧪 Mystery Potion","Probably healing. Probably.","320 gold"],
        ["📜 Ancient Quest Scroll","Contains three paragraphs of instructions.","140 gold"],
        ["🥪 Legendary Sandwich","Restores 100% hunger.","75 gold"],
        ["🗝️ Suspicious Key","No known door.","90 gold"],
        ["🧢 Background NPC Hat","Increases background character energy.","50 gold"],
        ["📚 Forbidden Library Card","Probably not actually forbidden.","210 gold"],
        ["🪙 Completely Normal Coin","Suspiciously shiny.","10 gold"]
    ];

    document.getElementById("feedContent").innerHTML = `
        <div class="option-grid">
            ${items.map(item=>`
                <div class="option-card" style="padding:18px">
                    <div style="font-size:28px">${item[0].split(" ")[0]}</div>
                    <strong>${escapeHTML(item[0].slice(item[0].indexOf(" ")+1))}</strong>
                    <span>${escapeHTML(item[1])}</span>

                    <div style="
                        margin-top:12px;
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                    ">
                        <strong>${escapeHTML(item[2])}</strong>

                        <button
                            onclick="buyItem('${escapeHTML(item[0])}')"
                            style="
                                border:0;
                                background:var(--accent);
                                color:white;
                                border-radius:9px;
                                padding:8px 11px;
                                font-weight:750;
                            "
                        >
                            Buy
                        </button>
                    </div>
                </div>
            `).join("")}
        </div>
    `;

    window.scrollTo({top:0,behavior:"smooth"});
}

function buyItem(item){
    toast("🛒 Purchased " + item + " for this temporary world.");
}

/* =========================================================
   NOTIFICATIONS
========================================================= */

function showNotifications(){

    const notifications = [
        "❤️ Someone liked your NPC activity.",
        "💬 A random NPC commented on a post.",
        "👥 Someone followed your temporary NPC.",
        "🎯 New quest available.",
        "🔥 Your side quest is trending.",
        "📖 A lore update was detected.",
        "🔁 Someone reposted a post."
    ];

    showModal(
        "🔔 Notifications",
        notifications.map((n,i)=>`
            <div class="quest">
                <div class="quest-title">${escapeHTML(n)}</div>
                <div class="quest-desc">${i+1} minutes ago</div>
            </div>
        `).join("")
    );
}

/* =========================================================
   MESSAGES
========================================================= */

function showMessages(){

    const people = [...npcs]
        .filter(n=>n.id !== currentUser.id)
        .slice(0,7);

    showModal(
        "💬 Messages",
        `
        <div style="margin-bottom:12px;color:var(--muted);font-size:12px">
            Temporary messages. Nothing is saved.
        </div>

        ${people.map(n=>`
            <button
                onclick="openChat('${escapeHTML(n.id)}')"
                style="
                    width:100%;
                    display:flex;
                    align-items:center;
                    gap:10px;
                    padding:11px;
                    margin-bottom:7px;
                    border:1px solid var(--border);
                    border-radius:12px;
                    background:#15171c;
                    color:var(--text);
                    text-align:left;
                "
            >
                <img
                    src="${escapeHTML(n.avatar)}"
                    style="width:40px;height:40px;border-radius:50%"
                    alt=""
                >

                <div>
                    <strong>${escapeHTML(n.name)}</strong>
                    <div style="font-size:11px;color:var(--muted)">
                        ${escapeHTML(pick([
                            "Are you free for a side quest?",
                            "You will never believe what happened.",
                            "I found the missing item.",
                            "Meet me at the usual location.",
                            "The quest giver is broken again."
                        ]))}
                    </div>
                </div>
            </button>
        `).join("")}
        `
    );
}

function openChat(id){

    const npc = getNPC(id);

    if(!npc) return;

    showModal(
        "💬 Chat with " + npc.name,
        `
        <div style="
            border:1px solid var(--border);
            border-radius:13px;
            padding:13px;
            margin-bottom:12px;
        ">
            <strong>${escapeHTML(npc.name)}</strong>
            <div style="color:var(--muted);font-size:12px;margin-top:3px">
                ${escapeHTML(npc.world)}
            </div>
        </div>

        <div class="quest">
            <div class="quest-title">NPC</div>
            <div class="quest-desc">
                Hello. I have been waiting here for someone to trigger my dialogue.
            </div>
        </div>

        <div class="modal-field">
            <label class="modal-label">Message</label>
            <input
                id="chatMessage"
                class="modal-input"
                placeholder="Type a message..."
            >
        </div>

        <button
            class="modal-submit"
            onclick="sendChat('${escapeHTML(id)}')"
        >
            Send Message
        </button>
        `
    );
}

function sendChat(id){

    const npc = getNPC(id);
    const input = document.getElementById("chatMessage");

    if(!npc || !input) return;

    const text = input.value.trim();

    if(!text){
        toast("Write a message first");
        return;
    }

    closeModal();

    toast("💬 Message sent to " + npc.name);
}

/* =========================================================
   SETTINGS
========================================================= */

function showSettings(){

    currentView = "panel";

    setNavActive("nav-home");

    document.getElementById("feedTitle").textContent =
        "⚙️ Settings";

    document.getElementById("feedSubtitle").textContent =
        "Temporary settings for this browser session.";

    document.getElementById("feedContent").innerHTML = `

        <div class="widget" style="margin-bottom:12px">

            <div class="widget-title">
                NPCBook Preferences
            </div>

            <div class="quest">
                <div class="quest-title">🌎 World Generation</div>
                <div class="quest-desc">
                    Every refresh creates a new temporary world.
                </div>
            </div>

            <div class="quest">
                <div class="quest-title">💾 Storage</div>
                <div class="quest-desc">
                    NPCBook does not use LocalStorage or SessionStorage.
                    Data exists only in browser memory.
                </div>
            </div>

            <div class="quest">
                <div class="quest-title">📱 Responsive Mode</div>
                <div class="quest-desc">
                    The interface automatically adapts to desktop,
                    tablet, iPad, Android and iPhone screen sizes.
                </div>
            </div>

            <button
                class="modal-submit"
                onclick="newWorld()"
                style="margin-top:10px"
            >
                🎲 Generate Completely New World
            </button>

        </div>
    `;

    window.scrollTo({top:0,behavior:"smooth"});
}

/* =========================================================
   MODAL
========================================================= */

function showModal(title,body){

    document.getElementById("modalTitle").textContent = title;
    document.getElementById("modalBody").innerHTML = body;

    document.getElementById("modalBackdrop")
        .classList.remove("hidden");

    document.body.style.overflow = "hidden";
}

function closeModal(){

    document.getElementById("modalBackdrop")
        .classList.add("hidden");

    document.body.style.overflow = "";
}

function backdropClose(event){

    if(event.target.id === "modalBackdrop"){
        closeModal();
    }
}

/* =========================================================
   FORMAT
========================================================= */

function formatNumber(num){

    num = Number(num) || 0;

    if(num >= 1000000){
        return (num/1000000).toFixed(1).replace(".0","") + "M";
    }

    if(num >= 1000){
        return (num/1000).toFixed(1).replace(".0","") + "K";
    }

    return String(num);
}

function formatTime(timestamp){

    const diff =
        Math.max(0,Date.now() - timestamp);

    const mins =
        Math.floor(diff / 60000);

    if(mins < 1){
        return "now";
    }

    if(mins < 60){
        return mins + "m";
    }

    const hours =
        Math.floor(mins / 60);

    if(hours < 24){
        return hours + "h";
    }

    const days =
        Math.floor(hours / 24);

    if(days < 7){
        return days + "d";
    }

    return Math.floor(days/7) + "w";
}

/* =========================================================
   TOAST
========================================================= */

function toast(message){

    const container =
        document.getElementById("toastContainer");

    const item =
        document.createElement("div");

    item.className = "toast";
    item.textContent = message;

    container.appendChild(item);

    setTimeout(()=>{
        item.remove();
    },2600);
}

/* =========================================================
   KEYBOARD SHORTCUTS
========================================================= */

document.addEventListener("keydown",function(event){

    if(event.key === "Escape"){
        closeModal();
    }

    if((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k"){
        event.preventDefault();
        focusSearch();
    }
});

/* =========================================================
   INITIAL START
========================================================= */

generateWorld();

</script>
</body>
</html>
"""

Path("index.html").write_text(HTML, encoding="utf-8")
print("NPCBook generated successfully: index.html")
