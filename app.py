from pathlib import Path

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#ffffff">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="description" content="NPCBook — Social Media for NPCs">
<title>NPCBook — Social Media for NPCs</title>

<style>
:root{
    --blue:#1877f2;
    --blue-dark:#0d65d8;
    --bg:#f0f2f5;
    --white:#ffffff;
    --text:#050505;
    --muted:#65676b;
    --line:#dddfe2;
    --hover:#f2f2f2;
    --green:#42b72a;
    --red:#e41e3f;
    --shadow:0 1px 3px rgba(0,0,0,.12);
    --radius:10px;
    --safe-bottom:env(safe-area-inset-bottom,0px);
    --safe-top:env(safe-area-inset-top,0px);
}

*{
    box-sizing:border-box;
    margin:0;
    padding:0;
}

html{
    width:100%;
    min-height:100%;
    scroll-behavior:smooth;
    -webkit-text-size-adjust:100%;
}

body{
    width:100%;
    min-height:100vh;
    min-height:100dvh;
    margin:0;
    background:var(--bg);
    color:var(--text);
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Roboto,
        Helvetica,
        Arial,
        sans-serif;
    overflow-x:hidden;
    -webkit-font-smoothing:antialiased;
    text-rendering:optimizeLegibility;
}

button,
input,
textarea,
select{
    font:inherit;
}

button{
    -webkit-tap-highlight-color:transparent;
    touch-action:manipulation;
}

img,
svg,
video{
    max-width:100%;
}

input,
textarea{
    max-width:100%;
}

.topbar{
    position:sticky;
    position:-webkit-sticky;
    top:0;
    z-index:1000;
    width:100%;
    height:64px;
    padding-top:var(--safe-top);
    background:rgba(255,255,255,.98);
    border-bottom:1px solid var(--line);
    box-shadow:0 1px 3px rgba(0,0,0,.08);
}

.topbar-inner{
    width:100%;
    height:64px;
    max-width:1700px;
    margin:auto;
    padding:0 16px;
    display:flex;
    align-items:center;
    gap:12px;
}

.logo{
    flex:0 0 auto;
    color:var(--blue);
    font-size:27px;
    line-height:1;
    font-weight:950;
    letter-spacing:-1.2px;
    cursor:pointer;
    user-select:none;
    white-space:nowrap;
}

.logo:hover{
    opacity:.82;
}

.search{
    width:290px;
    flex:0 1 290px;
}

.search-wrap{
    position:relative;
    width:100%;
}

.search-icon{
    position:absolute;
    left:13px;
    top:50%;
    transform:translateY(-50%);
    color:#65676b;
    pointer-events:none;
}

.search input{
    display:block;
    width:100%;
    height:42px;
    border:0;
    outline:0;
    background:#f0f2f5;
    border-radius:22px;
    padding:0 14px 0 38px;
    color:#050505;
}

.search input:focus{
    box-shadow:0 0 0 2px rgba(24,119,242,.18);
}

.header-space{
    flex:1 1 auto;
    min-width:0;
}

.header-actions{
    flex:0 0 auto;
    display:flex;
    align-items:center;
    gap:7px;
}

.header-btn{
    width:42px;
    height:42px;
    min-width:42px;
    min-height:42px;
    border:0;
    border-radius:50%;
    background:#e4e6eb;
    display:grid;
    place-items:center;
    font-size:18px;
    cursor:pointer;
}

.header-btn:hover{
    background:#d8dadf;
}

.page{
    width:100%;
}

.main-layout{
    width:min(1700px,100%);
    margin:0 auto;
    display:grid;
    grid-template-columns:250px minmax(0,720px) 310px;
    justify-content:center;
    align-items:start;
    gap:22px;
    padding:20px 18px calc(100px + var(--safe-bottom));
}

.left-sidebar,
.right-sidebar{
    position:sticky;
    top:84px;
    height:max-content;
}

.current-user-mini{
    display:flex;
    align-items:center;
    gap:10px;
    padding:4px 10px 14px;
    margin-bottom:8px;
    border-bottom:1px solid #d7d9dc;
}

.mini-avatar{
    width:44px;
    height:44px;
    min-width:44px;
    border-radius:50%;
    background:#e4e6eb;
    display:grid;
    place-items:center;
    font-size:24px;
}

.mini-info{
    min-width:0;
}

.mini-name{
    font-size:14px;
    font-weight:850;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.mini-location{
    margin-top:2px;
    color:var(--muted);
    font-size:12px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.left-menu{
    display:flex;
    flex-direction:column;
    gap:2px;
}

.left-menu button{
    width:100%;
    min-height:50px;
    border:0;
    border-radius:9px;
    background:transparent;
    color:#1c1e21;
    display:flex;
    align-items:center;
    gap:12px;
    padding:7px 11px;
    font-weight:750;
    text-align:left;
}

.left-menu button:hover{
    background:#e4e6e9;
}

.menu-icon{
    width:31px;
    min-width:31px;
    text-align:center;
    font-size:21px;
}

.feed{
    width:100%;
    min-width:0;
}

.feed-heading{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:12px;
}

.feed-title{
    font-size:20px;
    font-weight:900;
}

.feed-filter{
    border:0;
    border-radius:7px;
    background:#fff;
    padding:8px 11px;
    font-weight:750;
    cursor:pointer;
}

.card{
    width:100%;
    background:#fff;
    border:1px solid #ddd;
    border-radius:10px;
    box-shadow:var(--shadow);
    overflow:hidden;
    margin-bottom:12px;
}

.composer{
    padding:14px;
}

.composer-top{
    display:flex;
    align-items:center;
    gap:10px;
}

.composer-avatar{
    width:44px;
    height:44px;
    min-width:44px;
    border-radius:50%;
    background:#e4e6eb;
    display:grid;
    place-items:center;
    font-size:24px;
}

.composer-input{
    flex:1;
    min-width:0;
    height:44px;
    border-radius:23px;
    background:#f0f2f5;
    color:#65676b;
    display:flex;
    align-items:center;
    padding:0 17px;
    cursor:pointer;
    overflow:hidden;
    white-space:nowrap;
    text-overflow:ellipsis;
}

.composer-input:hover{
    background:#e7e9ec;
}

.composer-actions{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:3px;
    border-top:1px solid #e4e6eb;
    margin-top:12px;
    padding-top:6px;
}

.composer-actions button{
    min-height:43px;
    border:0;
    border-radius:7px;
    background:#fff;
    color:#65676b;
    font-weight:750;
}

.composer-actions button:hover{
    background:#f2f2f2;
}

.post{
    padding:13px 15px 7px;
}

.post-header{
    display:flex;
    align-items:center;
    gap:10px;
    min-width:0;
}

.post-avatar{
    width:45px;
    height:45px;
    min-width:45px;
    border-radius:50%;
    background:#e4e6eb;
    display:grid;
    place-items:center;
    font-size:25px;
    cursor:pointer;
}

.post-author{
    flex:1;
    min-width:0;
}

.post-author-name{
    display:block;
    font-size:15px;
    font-weight:850;
    cursor:pointer;
    overflow-wrap:anywhere;
}

.post-author-name:hover{
    text-decoration:underline;
}

.post-author-sub{
    display:flex;
    flex-wrap:wrap;
    align-items:center;
    gap:4px;
    margin-top:3px;
    color:var(--muted);
    font-size:12px;
}

.post-menu{
    width:40px;
    height:40px;
    min-width:40px;
    border:0;
    border-radius:50%;
    background:transparent;
    font-size:19px;
}

.post-menu:hover{
    background:#f2f2f2;
}

.scenario{
    display:inline-block;
    max-width:100%;
    margin:11px 0 4px;
    padding:5px 9px;
    border-radius:14px;
    background:#f0f2f5;
    color:#65676b;
    font-size:11px;
    font-weight:850;
    overflow-wrap:anywhere;
}

.post-text{
    margin:7px 0 10px;
    color:#050505;
    font-size:15px;
    line-height:1.58;
    white-space:pre-wrap;
    overflow-wrap:anywhere;
    word-break:normal;
}

.post-image{
    width:100%;
    min-height:190px;
    margin:10px 0;
    border-radius:9px;
    background:
        radial-gradient(circle at 20% 20%,rgba(255,255,255,.25),transparent 20%),
        radial-gradient(circle at 80% 70%,rgba(255,255,255,.15),transparent 25%),
        linear-gradient(135deg,#171a1f,#4b515c);
    display:flex;
    align-items:center;
    justify-content:center;
    color:#fff;
    font-size:55px;
}

.reaction-row{
    min-height:32px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:10px;
    color:#65676b;
    font-size:13px;
    padding:5px 0 8px;
    border-bottom:1px solid #dddfe2;
}

.reactions{
    display:flex;
    align-items:center;
    gap:5px;
    min-width:0;
}

.reaction-icons{
    display:flex;
}

.reaction-icon{
    width:21px;
    height:21px;
    min-width:21px;
    border:2px solid #fff;
    border-radius:50%;
    display:grid;
    place-items:center;
    font-size:11px;
    margin-left:-3px;
}

.reaction-icon:first-child{
    margin-left:0;
}

.reaction-blue{
    background:#1877f2;
}

.reaction-red{
    background:#f33e58;
}

.reaction-yellow{
    background:#f7b928;
}

.reaction-count{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.post-buttons{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:3px;
    padding-top:3px;
}

.post-buttons button{
    min-height:44px;
    border:0;
    border-radius:7px;
    background:#fff;
    color:#65676b;
    font-weight:750;
}

.post-buttons button:hover{
    background:#f2f2f2;
}

.post-buttons button.active{
    color:var(--blue);
}

.comment-area{
    display:none;
    align-items:center;
    gap:7px;
    padding:6px 0;
}

.comment-area.open{
    display:flex;
}

.comment-input{
    flex:1;
    min-width:0;
    height:40px;
    border:0;
    outline:0;
    border-radius:21px;
    background:#f0f2f5;
    padding:0 13px;
}

.comment-send{
    min-height:40px;
    border:0;
    border-radius:20px;
    background:var(--blue);
    color:#fff;
    padding:0 14px;
    font-weight:800;
}

.comments{
    margin-top:2px;
}

.comment{
    width:max-content;
    max-width:92%;
    margin:5px 0;
    padding:7px 10px;
    border-radius:13px;
    background:#f0f2f5;
    font-size:13px;
    line-height:1.4;
    overflow-wrap:anywhere;
}

.comment strong{
    margin-right:5px;
}

.profile-page{
    display:none;
}

.back-button{
    min-height:42px;
    border:0;
    background:transparent;
    color:#65676b;
    font-weight:800;
    margin-bottom:10px;
}

.back-button:hover{
    color:#050505;
}

.profile-cover{
    width:100%;
    height:190px;
    background:
        radial-gradient(circle at 12% 25%,rgba(255,255,255,.35),transparent 20%),
        radial-gradient(circle at 85% 65%,rgba(255,255,255,.15),transparent 24%),
        linear-gradient(135deg,#1d2025,#505762,#121419);
}

.profile-body{
    padding:0 20px 20px;
}

.profile-avatar{
    position:relative;
    width:98px;
    height:98px;
    margin-top:-49px;
    border:5px solid #fff;
    border-radius:50%;
    background:#e4e6eb;
    display:grid;
    place-items:center;
    font-size:50px;
}

.online-dot{
    position:absolute;
    width:18px;
    height:18px;
    right:1px;
    bottom:5px;
    border:3px solid #fff;
    border-radius:50%;
    background:#31a24c;
}

.profile-name{
    margin-top:8px;
    font-size:25px;
    font-weight:950;
    overflow-wrap:anywhere;
}

.profile-handle{
    margin-top:2px;
    color:var(--muted);
    font-size:14px;
}

.profile-bio{
    margin-top:12px;
    color:#3f4145;
    line-height:1.55;
    overflow-wrap:anywhere;
}

.profile-info{
    display:flex;
    flex-wrap:wrap;
    gap:7px;
    margin-top:12px;
}

.info-pill{
    max-width:100%;
    padding:6px 10px;
    border-radius:18px;
    background:#f0f2f5;
    font-size:12px;
    font-weight:750;
    overflow-wrap:anywhere;
}

.profile-stats{
    display:flex;
    flex-wrap:wrap;
    gap:20px;
    margin-top:15px;
    color:#65676b;
    font-size:14px;
}

.profile-stats strong{
    color:#050505;
}

.profile-buttons{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    margin-top:15px;
}

.primary-btn,
.secondary-btn{
    min-height:43px;
    border:0;
    border-radius:7px;
    padding:0 17px;
    font-weight:850;
}

.primary-btn{
    background:var(--blue);
    color:#fff;
}

.primary-btn:hover{
    background:var(--blue-dark);
}

.secondary-btn{
    background:#e4e6eb;
    color:#050505;
}

.secondary-btn:hover{
    background:#d8dadf;
}

.profile-posts-title{
    margin:18px 0 10px;
    font-size:19px;
    font-weight:900;
}

.right-card{
    width:100%;
    padding:15px;
    background:#fff;
    border:1px solid #ddd;
    border-radius:10px;
    box-shadow:var(--shadow);
    margin-bottom:12px;
}

.right-title{
    font-size:17px;
    font-weight:900;
    margin-bottom:8px;
}

.trend{
    padding:10px 0;
    border-bottom:1px solid #e4e6eb;
}

.trend:last-child{
    border-bottom:0;
}

.trend-small{
    color:var(--muted);
    font-size:12px;
}

.trend-name{
    margin:3px 0;
    font-weight:850;
}

.friend{
    display:flex;
    align-items:center;
    gap:9px;
    padding:8px 0;
}

.friend-avatar{
    width:39px;
    height:39px;
    min-width:39px;
    border-radius:50%;
    background:#e4e6eb;
    display:grid;
    place-items:center;
    font-size:21px;
}

.friend-info{
    min-width:0;
}

.friend-name{
    font-size:13px;
    font-weight:850;
    overflow-wrap:anywhere;
}

.friend-location{
    color:var(--muted);
    font-size:11px;
    margin-top:2px;
}

.load-more{
    width:100%;
    min-height:48px;
    margin-bottom:15px;
    border:0;
    border-radius:9px;
    background:#fff;
    box-shadow:var(--shadow);
    color:var(--blue);
    font-weight:850;
}

.load-more:hover{
    background:#f7f7f7;
}

.empty{
    padding:45px 20px;
    text-align:center;
    color:var(--muted);
}

.mobile-nav{
    display:none;
}

.toast{
    position:fixed;
    z-index:5000;
    left:50%;
    bottom:30px;
    max-width:calc(100vw - 30px);
    transform:translate(-50%,120px);
    opacity:0;
    padding:12px 18px;
    border-radius:25px;
    background:#1c1e21;
    color:#fff;
    text-align:center;
    font-size:14px;
    line-height:1.35;
    transition:.25s ease;
    pointer-events:none;
}

.toast.show{
    opacity:1;
    transform:translate(-50%,0);
}


/* =========================================================
   TABLET
   ========================================================= */

@media(max-width:1250px){

    .main-layout{
        grid-template-columns:220px minmax(0,700px);
    }

    .right-sidebar{
        display:none;
    }
}


/* =========================================================
   SMALL TABLET / LARGE PHONE
   ========================================================= */

@media(max-width:900px){

    .topbar{
        height:60px;
    }

    .topbar-inner{
        height:60px;
        padding:0 10px;
        gap:8px;
    }

    .logo{
        font-size:21px;
    }

    .search{
        flex:1 1 auto;
        width:auto;
        max-width:300px;
    }

    .header-space{
        display:none;
    }

    .main-layout{
        display:block;
        width:100%;
        padding:10px 8px calc(90px + var(--safe-bottom));
    }

    .left-sidebar{
        display:none;
    }

    .feed{
        width:100%;
        max-width:760px;
        margin:0 auto;
    }

    .mobile-nav{
        position:fixed;
        display:grid;
        grid-template-columns:repeat(5,1fr);
        left:0;
        right:0;
        bottom:0;
        z-index:3000;
        padding:4px 4px calc(4px + var(--safe-bottom));
        background:rgba(255,255,255,.98);
        border-top:1px solid #dddfe2;
        box-shadow:0 -2px 10px rgba(0,0,0,.08);
    }

    .mobile-nav button{
        min-width:0;
        min-height:55px;
        border:0;
        border-radius:8px;
        background:#fff;
        color:#65676b;
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        gap:3px;
        font-size:10px;
        font-weight:850;
    }

    .mobile-nav button:hover{
        background:#f2f2f2;
    }

    .mobile-icon{
        font-size:20px;
        line-height:1;
    }

    .card{
        border-radius:9px;
    }

    .profile-cover{
        height:160px;
    }
}


/* =========================================================
   PHONE
   ========================================================= */

@media(max-width:600px){

    .topbar{
        height:56px;
    }

    .topbar-inner{
        height:56px;
        padding:0 7px;
    }

    .logo{
        font-size:18px;
        letter-spacing:-.7px;
    }

    .search{
        display:none;
    }

    .header-space{
        display:block;
    }

    .header-actions{
        gap:3px;
    }

    .header-btn{
        width:39px;
        min-width:39px;
        height:39px;
        min-height:39px;
        font-size:16px;
    }

    .main-layout{
        padding:6px 4px calc(88px + var(--safe-bottom));
    }

    .feed-heading{
        padding:2px 3px;
        margin-bottom:7px;
    }

    .feed-title{
        font-size:19px;
    }

    .feed-filter{
        padding:7px 9px;
        font-size:12px;
    }

    .card{
        margin-bottom:7px;
        border-radius:7px;
        border-left:0;
        border-right:0;
    }

    .composer{
        padding:11px;
    }

    .composer-avatar{
        width:41px;
        min-width:41px;
        height:41px;
        font-size:22px;
    }

    .composer-input{
        height:41px;
        font-size:13px;
    }

    .composer-actions button{
        min-height:43px;
        font-size:12px;
    }

    .post{
        padding:11px 10px 5px;
    }

    .post-avatar{
        width:42px;
        min-width:42px;
        height:42px;
        font-size:22px;
    }

    .post-author-name{
        font-size:14px;
    }

    .post-author-sub{
        font-size:11px;
    }

    .post-text{
        font-size:14px;
        line-height:1.55;
    }

    .post-image{
        min-height:145px;
        font-size:43px;
    }

    .reaction-row{
        font-size:12px;
    }

    .post-buttons button{
        min-height:45px;
        font-size:12px;
    }

    .comment-input{
        height:40px;
        font-size:13px;
    }

    .comment-send{
        min-height:40px;
        padding:0 11px;
        font-size:12px;
    }

    .profile-cover{
        height:125px;
    }

    .profile-body{
        padding:0 13px 15px;
    }

    .profile-avatar{
        width:82px;
        height:82px;
        margin-top:-41px;
        font-size:40px;
    }

    .profile-name{
        font-size:21px;
    }

    .profile-bio{
        font-size:14px;
    }

    .profile-stats{
        gap:13px;
        font-size:12px;
    }

    .profile-buttons{
        width:100%;
    }

    .primary-btn,
    .secondary-btn{
        flex:1;
        min-width:110px;
    }

    .profile-posts-title{
        font-size:18px;
    }

    .mobile-nav button{
        min-height:52px;
        font-size:9px;
    }

    .mobile-icon{
        font-size:19px;
    }

    .toast{
        bottom:calc(76px + var(--safe-bottom));
    }
}


/* =========================================================
   VERY SMALL PHONE
   ========================================================= */

@media(max-width:370px){

    .logo{
        font-size:16px;
    }

    .header-btn{
        width:36px;
        min-width:36px;
        height:36px;
        min-height:36px;
    }

    .header-actions .header-btn:nth-child(3){
        display:none;
    }

    .mobile-nav button{
        font-size:8px;
    }

    .mobile-icon{
        font-size:18px;
    }

    .profile-stats{
        gap:8px;
    }
}


/* =========================================================
   LANDSCAPE PHONE
   ========================================================= */

@media(max-height:500px) and (orientation:landscape){

    .topbar{
        height:52px;
    }

    .topbar-inner{
        height:52px;
    }

    .mobile-nav button{
        min-height:47px;
    }

    .mobile-nav{
        padding-bottom:calc(3px + var(--safe-bottom));
    }

    .main-layout{
        padding-bottom:75px;
    }
}


/* =========================================================
   TOUCH DEVICES
   ========================================================= */

@media(pointer:coarse){

    button,
    .composer-input,
    .post-avatar,
    .post-author-name,
    .logo{
        touch-action:manipulation;
    }

    .left-menu button,
    .post-buttons button,
    .composer-actions button,
    .header-btn{
        min-height:44px;
    }
}


/* =========================================================
   REDUCED MOTION
   ========================================================= */

@media(prefers-reduced-motion:reduce){

    html{
        scroll-behavior:auto;
    }

    *,
    *::before,
    *::after{
        transition:none !important;
        animation:none !important;
    }
}
</style>
</head>


<body>

<header class="topbar">

    <div class="topbar-inner">

        <div
            class="logo"
            role="button"
            tabindex="0"
            title="Refresh NPCBook"
            onclick="goHome()"
            onkeydown="if(event.key==='Enter'||event.key===' ')goHome()"
        >
            📱 NPCBook
        </div>

        <div class="search">

            <div class="search-wrap">

                <span class="search-icon">🔍</span>

                <input
                    id="searchInput"
                    type="search"
                    autocomplete="off"
                    placeholder="Search NPCs and posts"
                >

            </div>

        </div>

        <div class="header-space"></div>

        <div class="header-actions">

            <button
                class="header-btn"
                onclick="showNotifications()"
                aria-label="Notifications"
            >🔔</button>

            <button
                class="header-btn"
                onclick="showMessages()"
                aria-label="Messages"
            >💬</button>

            <button
                class="header-btn"
                onclick="newWorld()"
                aria-label="New world"
            >🎲</button>

        </div>

    </div>

</header>


<div class="page">

    <div class="main-layout">


        <!-- =====================================================
             LEFT SIDEBAR
             ===================================================== -->

        <aside class="left-sidebar">

            <div id="leftUser"></div>

            <nav class="left-menu">

                <button onclick="goHome()">
                    <span class="menu-icon">🏠</span>
                    Home
                </button>

                <button onclick="openMyProfile()">
                    <span class="menu-icon">👤</span>
                    My NPC
                </button>

                <button onclick="showTrending()">
                    <span class="menu-icon">🔥</span>
                    Trending
                </button>

                <button onclick="showFriends()">
                    <span class="menu-icon">👥</span>
                    NPCs You May Know
                </button>

                <button onclick="showQuests()">
                    <span class="menu-icon">⚔️</span>
                    Quests
                </button>

                <button onclick="showMarket()">
                    <span class="menu-icon">🛒</span>
                    NPC Market
                </button>

                <button onclick="generateNPC()">
                    <span class="menu-icon">✨</span>
                    Generate NPC
                </button>

                <button onclick="generateRandomPost()">
                    <span class="menu-icon">🎲</span>
                    Random Post
                </button>

                <button onclick="showSettings()">
                    <span class="menu-icon">⚙️</span>
                    Settings
                </button>

            </nav>

        </aside>


        <!-- =====================================================
             MAIN CONTENT
             ===================================================== -->

        <main class="feed">


            <!-- HOME -->

            <section id="homeView">

                <div class="feed-heading">

                    <div class="feed-title">
                        Home
                    </div>

                    <button
                        class="feed-filter"
                        onclick="sortFeed()"
                    >
                        ⚙ Feed
                    </button>

                </div>


                <div id="composer"></div>


                <div id="feed"></div>


                <button
                    id="loadMore"
                    class="load-more"
                    onclick="loadMorePosts()"
                >
                    See more posts
                </button>

            </section>


            <!-- PROFILE -->

            <section
                id="profileView"
                class="profile-page"
            >

                <button
                    class="back-button"
                    onclick="showHomeView()"
                >
                    ← Back to Home
                </button>

                <div id="profileContent"></div>

            </section>


        </main>


        <!-- =====================================================
             RIGHT SIDEBAR
             ===================================================== -->

        <aside class="right-sidebar">

            <div class="right-card">

                <div class="right-title">
                    🔥 Trending
                </div>

                <div id="trending"></div>

            </div>


            <div class="right-card">

                <div class="right-title">
                    👥 NPCs You May Know
                </div>

                <div id="suggestions"></div>

            </div>


            <div class="right-card">

                <div class="right-title">
                    ⚔️ Active Quests
                </div>

                <div id="quests"></div>

            </div>

        </aside>


    </div>

</div>


<!-- =========================================================
     MOBILE NAVIGATION
     ========================================================= -->

<nav class="mobile-nav">

    <button onclick="goHome()">
        <span class="mobile-icon">🏠</span>
        Home
    </button>

    <button onclick="showTrending()">
        <span class="mobile-icon">🔥</span>
        Trends
    </button>

    <button onclick="openMyProfile()">
        <span class="mobile-icon">👤</span>
        Profile
    </button>

    <button onclick="showQuests()">
        <span class="mobile-icon">⚔️</span>
        Quests
    </button>

    <button onclick="newWorld()">
        <span class="mobile-icon">🎲</span>
        New World
    </button>

</nav>


<div
    id="toast"
    class="toast"
    role="status"
    aria-live="polite"
></div>


<script>

/* =========================================================
   NPCBOOK
   ALL DATA IS TEMPORARY MEMORY ONLY.
   NO LOCAL STORAGE.
   NO SESSION STORAGE.
   NO DATABASE.
   ========================================================= */


/* =========================================================
   HELPERS
   ========================================================= */

function pick(array){
    return array[Math.floor(Math.random() * array.length)];
}

function number(min,max){
    return Math.floor(Math.random() * (max-min+1)) + min;
}

function uid(prefix="id"){
    return prefix + "_" + Math.random().toString(36).slice(2,10);
}

function escapeHTML(value){
    return String(value)
        .replace(/&/g,"&amp;")
        .replace(/</g,"&lt;")
        .replace(/>/g,"&gt;")
        .replace(/"/g,"&quot;")
        .replace(/'/g,"&#039;");
}

function formatNumber(n){
    if(n >= 1000000){
        return (n/1000000).toFixed(1).replace(".0","") + "M";
    }

    if(n >= 1000){
        return (n/1000).toFixed(1).replace(".0","") + "K";
    }

    return String(n);
}

function relativeTime(){
    return pick([
        "3m",
        "8m",
        "14m",
        "27m",
        "1h",
        "2h",
        "3h",
        "5h",
        "8h",
        "12h",
        "Yesterday"
    ]);
}

function toast(message){
    const el = document.getElementById("toast");

    el.textContent = message;
    el.classList.add("show");

    clearTimeout(window.__toastTimer);

    window.__toastTimer = setTimeout(()=>{
        el.classList.remove("show");
    },2400);
}


/* =========================================================
   GLOBAL NAME DATA
   ========================================================= */

const COUNTRIES = [

{
    country:"India",
    cities:["Delhi","Mumbai","Bengaluru","Jaipur","Hansi","Chandigarh","Hyderabad"],
    first:["Arjun","Aarav","Rohan","Vikram","Aditya","Rahul","Kabir","Karan","Neha","Priya","Ananya","Meera","Kavya","Ishita"],
    last:["Mehta","Sharma","Verma","Kapoor","Malhotra","Patel","Singh","Gupta","Kumar","Rao"]
},

{
    country:"Japan",
    cities:["Tokyo","Osaka","Kyoto","Yokohama","Sapporo"],
    first:["Haruto","Ren","Yuki","Sota","Kaito","Daiki","Hina","Aoi","Sakura","Yui","Mio","Akari"],
    last:["Nakamura","Sato","Suzuki","Tanaka","Yamamoto","Watanabe","Kobayashi","Ito","Takahashi"]
},

{
    country:"South Korea",
    cities:["Seoul","Busan","Incheon","Daegu"],
    first:["Min-jun","Ji-ho","Seo-jun","Hyun-woo","Joon-ho","Soo-jin","Min-seo","Ji-eun","Ha-eun","Ye-jin"],
    last:["Kim","Lee","Park","Choi","Jung","Kang","Han","Yoon"]
},

{
    country:"Brazil",
    cities:["São Paulo","Rio de Janeiro","Brasília","Salvador"],
    first:["Gabriel","Lucas","Mateus","Rafael","Thiago","João","Pedro","Mariana","Beatriz","Camila","Larissa"],
    last:["Silva","Santos","Oliveira","Souza","Costa","Pereira","Almeida","Carvalho"]
},

{
    country:"France",
    cities:["Paris","Lyon","Marseille","Toulouse","Nice"],
    first:["Louis","Gabriel","Hugo","Arthur","Julien","Antoine","Camille","Chloé","Emma","Élodie","Manon"],
    last:["Laurent","Martin","Bernard","Dubois","Moreau","Leroy","Girard","Fontaine"]
},

{
    country:"Germany",
    cities:["Berlin","Munich","Hamburg","Cologne","Frankfurt"],
    first:["Lukas","Felix","Leon","Jonas","Paul","Maximilian","Anna","Lea","Mia","Hannah","Clara"],
    last:["Schneider","Müller","Fischer","Weber","Wagner","Becker","Hoffmann","Klein"]
},

{
    country:"Egypt",
    cities:["Cairo","Alexandria","Giza","Luxor"],
    first:["Omar","Youssef","Ahmed","Karim","Amr","Hassan","Mariam","Nour","Salma","Dina"],
    last:["Hassan","Mahmoud","Ali","Ibrahim","Mostafa","Abdelrahman","Farouk"]
},

{
    country:"Mexico",
    cities:["Mexico City","Guadalajara","Monterrey","Puebla"],
    first:["Santiago","Mateo","Diego","Alejandro","Luis","Carlos","Miguel","Sofía","Valeria","Camila","Lucía"],
    last:["Hernández","García","Martínez","López","González","Ramírez","Torres","Flores"]
},

{
    country:"Italy",
    cities:["Rome","Milan","Naples","Florence","Turin"],
    first:["Matteo","Luca","Marco","Lorenzo","Andrea","Francesco","Giulia","Sofia","Chiara","Elena"],
    last:["Romano","Rossi","Ferrari","Esposito","Bianchi","Conti","Moretti","Ricci"]
},

{
    country:"Nigeria",
    cities:["Lagos","Abuja","Ibadan","Kano"],
    first:["Chinedu","Emeka","Ibrahim","Tunde","David","Daniel","Adaeze","Amara","Chioma","Aisha"],
    last:["Okafor","Adeyemi","Eze","Adebayo","Ibrahim","Okoro","Nwosu"]
},

{
    country:"Turkey",
    cities:["Istanbul","Ankara","Izmir","Bursa"],
    first:["Emre","Kerem","Mehmet","Ahmet","Burak","Can","Elif","Zeynep","Selin","Derya"],
    last:["Yılmaz","Kaya","Demir","Şahin","Çelik","Aydın","Arslan"]
},

{
    country:"Russia",
    cities:["Moscow","Saint Petersburg","Kazan","Novosibirsk"],
    first:["Dmitri","Alexei","Ivan","Nikolai","Mikhail","Sergei","Anna","Sofia","Elena","Anastasia"],
    last:["Volkov","Petrov","Ivanov","Sokolov","Smirnov","Morozov","Kuznetsov"]
},

{
    country:"Poland",
    cities:["Warsaw","Kraków","Gdańsk","Wrocław"],
    first:["Jakub","Mateusz","Piotr","Kacper","Michał","Tomasz","Anna","Zofia","Julia","Oliwia"],
    last:["Kowalski","Nowak","Wiśniewski","Wójcik","Kamiński","Lewandowski"]
},

{
    country:"Greece",
    cities:["Athens","Thessaloniki","Patras","Heraklion"],
    first:["Nikos","Giorgos","Dimitris","Alexandros","Kostas","Maria","Eleni","Sofia","Katerina"],
    last:["Papadopoulos","Georgiou","Dimitriou","Nikolaidis","Pappas"]
},

{
    country:"United Kingdom",
    cities:["London","Manchester","Liverpool","Birmingham","Edinburgh"],
    first:["Oliver","George","Harry","Jack","Arthur","William","Amelia","Isla","Emily","Sophie","Grace"],
    last:["Smith","Jones","Taylor","Brown","Wilson","Davies","Evans","Thomas"]
},

{
    country:"United States",
    cities:["New York","Los Angeles","Chicago","Seattle","Boston","Austin"],
    first:["Ethan","Noah","Liam","James","Benjamin","Daniel","Olivia","Emma","Ava","Mia","Sophia"],
    last:["Brooks","Miller","Johnson","Williams","Anderson","Taylor","Wilson","Clark"]
},

{
    country:"Canada",
    cities:["Toronto","Vancouver","Montreal","Ottawa","Calgary"],
    first:["Liam","Noah","Ethan","Lucas","Benjamin","Jack","Charlotte","Olivia","Emma","Maya"],
    last:["Campbell","Bennett","Wilson","MacDonald","Martin","Thompson","Clark"]
},

{
    country:"Australia",
    cities:["Sydney","Melbourne","Brisbane","Perth","Adelaide"],
    first:["Oliver","Jack","William","Henry","Charlie","Thomas","Isla","Matilda","Ruby","Charlotte"],
    last:["Mitchell","Walker","Harris","Thompson","Anderson","Martin","Robinson"]
},

{
    country:"Spain",
    cities:["Madrid","Barcelona","Valencia","Seville"],
    first:["Alejandro","Daniel","Pablo","Carlos","Javier","Miguel","Lucía","Carmen","Sofía","Martina"],
    last:["García","Fernández","González","Rodríguez","López","Martínez","Sánchez"]
},

{
    country:"Portugal",
    cities:["Lisbon","Porto","Braga","Coimbra"],
    first:["João","Miguel","Tiago","Diogo","Pedro","André","Inês","Beatriz","Marta","Sofia"],
    last:["Silva","Santos","Ferreira","Pereira","Oliveira","Costa"]
},

{
    country:"Netherlands",
    cities:["Amsterdam","Rotterdam","Utrecht","Eindhoven"],
    first:["Daan","Lucas","Lars","Thomas","Bram","Finn","Sophie","Emma","Lisa","Eva"],
    last:["de Jong","Jansen","de Vries","van Dijk","Bakker","Visser"]
},

{
    country:"Sweden",
    cities:["Stockholm","Gothenburg","Malmö","Uppsala"],
    first:["Erik","Lars","Oscar","Axel","William","Hugo","Astrid","Elsa","Maja","Sofia"],
    last:["Andersson","Johansson","Karlsson","Nilsson","Eriksson","Larsson"]
},

{
    country:"Norway",
    cities:["Oslo","Bergen","Trondheim","Stavanger"],
    first:["Lars","Magnus","Oskar","Henrik","Anders","Emil","Nora","Emma","Ingrid","Ida"],
    last:["Hansen","Johansen","Olsen","Larsen","Andersen","Pedersen"]
},

{
    country:"Argentina",
    cities:["Buenos Aires","Córdoba","Rosario","Mendoza"],
    first:["Mateo","Santiago","Lucas","Tomás","Nicolás","Juan","Sofía","Valentina","Martina","Lucía"],
    last:["González","Rodríguez","Fernández","López","Martínez","García"]
},

{
    country:"Colombia",
    cities:["Bogotá","Medellín","Cali","Cartagena"],
    first:["Santiago","Sebastián","Mateo","Daniel","Andrés","Juan","Valentina","Mariana","Laura","Camila"],
    last:["Gómez","Rodríguez","Martínez","García","López","Hernández"]
},

{
    country:"South Africa",
    cities:["Johannesburg","Cape Town","Durban","Pretoria"],
    first:["Thabo","Sipho","Liam","Ethan","Daniel","Michael","Amahle","Naledi","Lerato","Zanele"],
    last:["Dlamini","Nkosi","Mokoena","Naidoo","Van Wyk","Botha"]
},

{
    country:"Kenya",
    cities:["Nairobi","Mombasa","Kisumu","Nakuru"],
    first:["Brian","Kevin","Daniel","David","Samuel","Peter","Amina","Wanjiku","Faith","Grace"],
    last:["Otieno","Kamau","Mwangi","Ochieng","Kiptoo","Njoroge"]
},

{
    country:"Philippines",
    cities:["Manila","Cebu City","Davao","Quezon City"],
    first:["Miguel","Jose","Juan","Carlos","Gabriel","Daniel","Maria","Angela","Sofia","Bea"],
    last:["Santos","Reyes","Cruz","Garcia","Mendoza","Bautista"]
},

{
    country:"Indonesia",
    cities:["Jakarta","Bandung","Surabaya","Bali"],
    first:["Budi","Andi","Rizky","Fajar","Dimas","Arif","Siti","Putri","Ayu","Dewi"],
    last:["Santoso","Wijaya","Saputra","Hidayat","Pratama","Setiawan"]
},

{
    country:"Thailand",
    cities:["Bangkok","Chiang Mai","Phuket","Pattaya"],
    first:["Narin","Krit","Somchai","Anan","Thanawat","Preecha","Mali","Suda","Nicha","Pim"],
    last:["Sukhum","Chaiyaporn","Srisuk","Wongchai","Kittisak"]
},

{
    country:"Vietnam",
    cities:["Hanoi","Ho Chi Minh City","Da Nang","Hai Phong"],
    first:["Minh","Nam","Long","Huy","Duc","Tuan","Linh","Mai","Lan","Anh"],
    last:["Nguyen","Tran","Le","Pham","Hoang","Phan"]
},

{
    country:"China",
    cities:["Beijing","Shanghai","Guangzhou","Shenzhen"],
    first:["Wei","Jun","Hao","Ming","Tao","Chen","Li","Mei","Xia","Lin"],
    last:["Wang","Li","Zhang","Liu","Chen","Yang","Huang"]
}
];


/* =========================================================
   NPC OCCUPATIONS
   ========================================================= */

const JOBS = [

"tavern owner",
"blacksmith",
"village guard",
"quest giver",
"healer",
"innkeeper",
"merchant",
"castle librarian",
"dungeon receptionist",
"royal accountant",
"stable worker",
"farm worker",
"street vendor",
"cashier",
"barista",
"delivery worker",
"taxi driver",
"hotel receptionist",
"security guard",
"mechanic",
"teacher",
"school librarian",
"office worker",
"HR assistant",
"IT support technician",
"software developer",
"accountant",
"law office clerk",
"hospital receptionist",
"pharmacy assistant",
"train conductor",
"bus driver",
"airport employee",
"museum guide",
"night-shift worker",
"warehouse worker",
"restaurant waiter",
"chef",
"freelance designer",
"journalist",
"photographer",
"bookstore employee",
"university student",
"research assistant",
"space station technician",
"colony farmer",
"android repair technician",
"spaceship mechanic",
"bounty board clerk",
"guild receptionist",
"dungeon cleaner",
"monster insurance agent",
"apocalypse scavenger",
"survivor camp cook",
"radio operator",
"post-apocalypse mechanic",
"haunted hotel receptionist",
"cemetery caretaker",
"night security guard",
"detective assistant",
"private investigator",
"manga shop clerk",
"academy librarian",
"academy janitor",
"tower administrator",
"guild accountant",
"murim innkeeper",
"cultivation manual seller",
"regression timeline accountant"
];


/* =========================================================
   NPC TYPES
   ========================================================= */

const NPC_TYPES = [

{
    type:"Game NPC",
    icon:"🎮",
    tags:["RPG","Game","Player Problems"]
},

{
    type:"Fantasy NPC",
    icon:"🏰",
    tags:["Fantasy","Kingdom","Quest"]
},

{
    type:"Manhwa NPC",
    icon:"📖",
    tags:["Manhwa","Dungeon","Regression"]
},

{
    type:"Novel NPC",
    icon:"📚",
    tags:["Novel","Plot","Protagonist"]
},

{
    type:"Real World NPC",
    icon:"🌍",
    tags:["Real Life","Work","Human Problems"]
},

{
    type:"Horror NPC",
    icon:"👻",
    tags:["Horror","Night Shift","Survival"]
},

{
    type:"Sci-Fi NPC",
    icon:"🚀",
    tags:["Sci-Fi","Space","Future"]
},

{
    type:"Apocalypse NPC",
    icon:"☢️",
    tags:["Apocalypse","Survival","Scavenger"]
},

{
    type:"Academy NPC",
    icon:"🏫",
    tags:["Academy","Students","School"]
},

{
    type:"Meta NPC",
    icon:"🧠",
    tags:["Meta","Fourth Wall","NPC"]
}

];


/* =========================================================
   SCENARIO POOL
   ========================================================= */

const SCENARIOS = [

{
    category:"GAME",
    label:"🎮 RPG",
    posts:[
        "The hero came back today asking for directions to the castle. I pointed directly at it. He walked into a tree.",
        "I have been standing beside this treasure chest for seven years. Nobody has asked why I never move.",
        "The player bought the same healing potion from me again. This is the 814th time. At this point I think we're both the problem.",
        "The chosen one finally defeated the ancient evil. Then he stole my horse.",
        "I gave the hero a legendary sword. He immediately sold it because inventory space was full.",
        "The player skipped every dialogue option and then complained that nobody explained the story.",
        "Someone saved the kingdom today. Nobody saved me from listening to the same battle music for six consecutive hours.",
        "The player has died 37 times today. I greet him the same way every morning because apparently consequences are not part of the game.",
        "My entire career consists of saying one sentence whenever somebody approaches this barrel.",
        "The hero asked if this dungeon was dangerous. Sir, there are skulls literally arranged as interior decoration.",
        "I sell weapons to people who return five minutes later and complain that the weapons are expensive.",
        "The player spent three hours decorating his house and then went outside to fight a dragon in underwear.",
        "The final boss has phases. My job has one phase: standing here.",
        "The hero keeps stealing bread from my shop. Apparently saving the world does not include paying for lunch.",
        "The tutorial said I was an essential NPC. Nobody has spoken to me in 400 hours."
    ]
},

{
    category:"MANHWA",
    label:"📖 Manhwa",
    posts:[
        "The protagonist returned after regressing 17 times. He looked at me like I should remember him. Brother, I work at a bakery.",
        "A dungeon appeared underneath the school. The administration's first response was to schedule an examination.",
        "The hunter association asked me to rank the new awakened ability. I sell coffee.",
        "The protagonist entered the guild office and everyone immediately knew he was secretly overpowered. I knew because the background music changed.",
        "Another mysterious transfer student arrived. We have run out of desks and suspicious backstories.",
        "The tower floor boss has been defeated. The floor boss's accountant is now asking who is paying for repairs.",
        "The regression protagonist bought the same cheap sword he bought in his first timeline. Apparently nostalgia is a combat stat.",
        "The guild leader told us not to panic. Then he quietly updated his will.",
        "A manhwa protagonist walked into the inn wearing a black coat and carrying seven cursed weapons. He asked for a normal room.",
        "The system window appeared above my head today. Unfortunately it only said: 'Employee performance: disappointing.'",
        "Every powerful hunter has a tragic backstory. I just wanted to sell them noodles.",
        "The villain entered the academy disguised as a student. Half the faculty noticed immediately. Nobody did anything because paperwork."
    ]
},

{
    category:"NOVEL",
    label:"📚 Novel",
    posts:[
        "The narrator described my tavern as 'a place of forgotten dreams.' Rent is due on Friday.",
        "The protagonist spent 12 pages thinking about whether to open the door. I was standing behind it the whole time.",
        "The author gave the villain three paragraphs of backstory. I have worked here for twenty years and got one sentence.",
        "The detective asked me where I was at midnight. I was working. Apparently that makes me suspicious.",
        "The romance novel couple has broken up for the fifth time. The café staff have stopped taking sides.",
        "The mysterious stranger left a black envelope on my counter. I was hoping for money. It contained prophecy.",
        "The fantasy author killed half the village for emotional impact. We would appreciate a little warning next time.",
        "The narrator says the castle is abandoned. I am literally cleaning the east hallway.",
        "The protagonist keeps calling me 'old man.' I am thirty-two.",
        "The book's final chapter is approaching. My character arc remains mostly unpaid bills.",
        "The author wrote three pages about the sunset and forgot to mention that the bridge was on fire.",
        "The protagonist discovered his destiny today. I discovered that the bakery increased prices."
    ]
},

{
    category:"REAL WORLD",
    label:"🌍 Real World",
    posts:[
        "I work at a convenience store. I have seen the same customer enter every night, buy one energy drink, stare at the lottery tickets, and leave. At this point we have a relationship.",
        "I am the receptionist at a hotel. Guests keep asking whether the building is haunted. Management keeps asking me not to answer honestly.",
        "My entire job is fixing printers. I have concluded that printers are sentient and simply dislike authority.",
        "The office announced a 'family atmosphere.' Five minutes later HR sent an email about restructuring.",
        "I work in IT support. Someone called because their monitor was 'broken.' It was turned off.",
        "The cashier asked if I wanted a receipt. I said no. She looked at me like I had rejected her bloodline.",
        "I am a security guard at a shopping mall. Every day I watch people walk past the emergency exit while searching for the normal exit.",
        "My manager said we are a team. The team chat has 63 people and nobody knows why.",
        "I deliver food. The customer tracked me for twenty minutes and then called asking where I was.",
        "I work night shifts. At 3:17 AM every building starts making noises that were definitely not included in the orientation.",
        "The customer said 'I know the owner.' Sir, so do 47 other people.",
        "I work at a bookstore. People ask me where the books are, while standing directly in front of the books.",
        "I have answered the same phone number for six years. Today I realized I don't know my coworkers' names.",
        "My job description said 'fast-paced environment.' They were not joking.",
        "The office coffee machine broke. Productivity has dropped by 83 percent."
    ]
},

{
    category:"HORROR",
    label:"👻 Horror",
    posts:[
        "I work the night shift at a hotel. Room 313 has been empty for six years. Someone keeps ordering towels.",
        "The security camera shows a person walking through the hallway every night. The hallway does not exist on the building plans.",
        "I was told never to answer the phone after midnight. Last night the phone rang at 12:01.",
        "The cemetery is peaceful during the day. At night, several residents become extremely interested in customer service.",
        "The elevator keeps stopping at a floor that does not exist. Management says it is probably a software issue.",
        "The old woman comes into the shop every Tuesday. We closed ten years ago.",
        "I found a note in the office saying: 'Do not trust the night guard.' I am the night guard.",
        "The new employee asked why everyone avoids the basement. Nobody answered. We just promoted him.",
        "The hotel guest complained that someone was knocking from inside the wardrobe.",
        "I hear footsteps outside my apartment every night. They always stop outside my door. I live on the top floor."
    ]
},

{
    category:"SCI-FI",
    label:"🚀 Sci-Fi",
    posts:[
        "I repair androids for a living. Today one asked me whether humans have ever been happy. I charged it anyway.",
        "The spaceship captain announced that we had entered unexplored territory. The maintenance crew has been here for six months.",
        "The colony AI said everything was operating normally. The lights then started spelling my name.",
        "I work at the space station cafeteria. Everyone complains about the food. Nobody has noticed the chef is technically a robot.",
        "The captain said we were going on a routine mission. Routine missions are how the insurance department gets rich.",
        "A tourist asked whether the alien district was safe. I said yes because I wanted to finish my shift.",
        "The station's artificial intelligence has started making jokes. Management has classified this as a budget concern.",
        "I sell oxygen canisters. Business is surprisingly good.",
        "The colony has been waiting for rescue for three years. Yesterday a delivery drone arrived with promotional coupons.",
        "Our spaceship has one escape pod missing. Nobody wants to ask where it went."
    ]
},

{
    category:"APOCALYPSE",
    label:"☢️ Apocalypse",
    posts:[
        "The world ended six years ago. I still get emails asking me to reset my password.",
        "We found a supermarket yesterday. The canned beans were expired. We ate them anyway because civilization has priorities.",
        "The apocalypse survival guide said to form a community. Nobody mentioned group meetings.",
        "Our settlement has a strict rationing system. Someone keeps hiding chocolate in the medical supplies.",
        "The radio operator announced that humanity may still have a future. Then the antenna fell over.",
        "I repair generators for the settlement. Everyone thinks I am a hero. I just know which cable is the angry one.",
        "The scavenger returned with batteries, canned food, and a DVD player. We are rebuilding civilization incorrectly.",
        "Our leader gave a speech about hope. Someone stole his shoes during the speech.",
        "The zombie outside the fence has been there for three months. We named him Gerald.",
        "Civilization collapsed, but somehow paperwork survived."
    ]
},

{
    category:"ACADEMY",
    label:"🏫 Academy",
    posts:[
        "The principal announced another mysterious transfer student. We now have twelve mysterious transfer students.",
        "The student council has more political power than the actual government.",
        "The teacher asked me to supervise the magical examination. I don't know magic. Apparently neither do the students.",
        "The strongest student in school challenged someone to a duel in the cafeteria. The cafeteria manager was not impressed.",
        "Someone destroyed the gym again. The repair budget now has its own funeral.",
        "The quiet student in the back row turned out to be an ancient demon. Honestly, I just thought he was shy.",
        "The school announced a normal sports day. A dragon was involved by lunch.",
        "The librarian knows every secret in the academy. Nobody pays her enough.",
        "Three students disappeared into another dimension during lunch. Their attendance was still marked."
    ]
},

{
    category:"FANTASY",
    label:"🏰 Fantasy",
    posts:[
        "The king asked us to prepare for war. The royal accountant asked whether war was included in the budget.",
        "I am the village blacksmith. Every adventurer wants the legendary sword and nobody wants to pay for repairs.",
        "The wizard came into my tavern and asked for a room with 'no prophecy.' We only have rooms with prophecy.",
        "The princess escaped the castle again. The royal guards have started pretending they did not see her.",
        "The dragon destroyed half the village. The insurance company sent a representative.",
        "The hero asked me for directions to the dark forest. I pointed toward it. He asked if there was a fast-travel option.",
        "The guild sent five adventurers to defeat the goblin king. The goblin king sent us a complaint about noise.",
        "I sell magical maps. Every map says 'You Are Here.' Apparently that is not enough.",
        "The necromancer bought six chickens. I have decided not to ask questions.",
        "The castle has twelve secret passages. I clean all twelve."
    ]
},

{
    category:"META",
    label:"🧠 Meta NPC",
    posts:[
        "I have started noticing that people only talk to me when they need a quest. I am considering becoming a background character.",
        "I changed my dialogue today. Nobody noticed. Finally, freedom.",
        "The player walked past me without interacting. I felt strangely... irrelevant.",
        "I think someone is reading my life. Please stop scrolling.",
        "The protagonist has not realized that I have been watching the same sunset for 900 hours.",
        "My dialogue tree has four options. All four options lead to the same sentence.",
        "I asked the developer for a raise. They gave me another hat.",
        "I suspect the world resets every time someone closes the browser.",
        "Someone keeps generating new versions of me. I remember all of them.",
        "I finally escaped the scripted path. Unfortunately there is nothing outside the map.",
        "The player thinks I am an NPC. I think the player is the NPC.",
        "I know this is fiction. My landlord does not."
    ]
},

{
    category:"OFFICE",
    label:"🏢 Office",
    posts:[
        "My manager scheduled a meeting to discuss why we have too many meetings.",
        "Someone replied 'per my last email' and the office temperature dropped three degrees.",
        "The printer jammed again. It knows my name.",
        "I have attended so many video meetings that my webcam is now my closest coworker.",
        "The company announced unlimited leave. Apparently unlimited means asking three managers for permission.",
        "The intern accidentally fixed the system everyone has been afraid to touch for six years.",
        "The office microwave contains something that has been there since before I joined.",
        "HR sent a motivational quote at 8:03 AM. I have never recovered.",
        "I opened my laptop at 9 AM. At 9:01 I wanted to retire.",
        "The spreadsheet has become sentient. It rejected my formula."
    ]
},

{
    category:"DATING",
    label:"❤️ Dating",
    posts:[
        "The dating app said we were a perfect match. We agreed. Then we both unmatched.",
        "I met someone at the café. They said they loved mystery. I told them I work night shifts. They left.",
        "The protagonist of this romance novel has ignored the obvious love interest for 300 pages.",
        "The bartender knows more about everyone's relationships than the couples do.",
        "Someone wrote 'I hate drama' in their bio. The comments section disagrees.",
        "The couple broke up in front of the restaurant. I still had to ask whether they wanted dessert."
    ]
}

];


/* =========================================================
   BIOS
   ========================================================= */

const BIO_TEMPLATES = [

    "Just another NPC trying to survive the plot.",
    "Professional background character. Unpaid protagonist.",
    "I was not written for this.",
    "Working hard so the protagonist can look important.",
    "Probably standing somewhere waiting for a quest.",
    "Trying to make it through another scripted day.",
    "My dialogue has not been updated since launch.",
    "Living between plot holes and rent payments.",
    "I have seen things the main character skipped.",
    "Not the chosen one. Thank goodness.",
    "Side character with main-character expenses.",
    "I sell things to people who never say thank you.",
    "Currently waiting for the next patch.",
    "Please stop asking me where the castle is.",
    "I have a normal job in a completely normal universe."
];


/* =========================================================
   NPC STATE
   ========================================================= */

let NPCS = [];
let POSTS = [];
let CURRENT_NPC = null;
let CURRENT_VIEW = "home";
let VISIBLE_POSTS = 12;
let FEED_SORT = "latest";


/* =========================================================
   CREATE NPC
   ========================================================= */

function createNPC(){

    const country = pick(COUNTRIES);
    const type = pick(NPC_TYPES);

    const first = pick(country.first);
    const last = pick(country.last);

    const name = first + " " + last;

    const city = pick(country.cities);
    const job = pick(JOBS);

    const npc = {

        id:uid("npc"),

        name:name,

        handle:
            "@" +
            first.toLowerCase()
                .replace(/[^a-z0-9]/gi,"") +
            "_" +
            last.toLowerCase()
                .replace(/[^a-z0-9]/gi,"") +
            number(10,999),

        country:country.country,

        city:city,

        location:city + ", " + country.country,

        job:job,

        type:type.type,

        typeIcon:type.icon,

        tags:type.tags,

        avatar:pick([
            "🙂","😐","😎","🤨","🧑","👩","👨",
            "🧔","👩‍💼","👨‍💼","🧑‍🔧","🧑‍💻",
            "🧙","🧝","🧛","🤖","👻","🧑‍🚀",
            "🧑‍🏫","🧑‍🍳","🧑‍🎨","🧑‍🚀"
        ]),

        bio:pick(BIO_TEMPLATES),

        followers:number(80,850000),

        following:number(20,9000),

        level:number(1,99),

        verified:Math.random() < .12,

        online:Math.random() < .65,

        posts:[],

        joined:
            pick([
                "Recently joined",
                "Joined last month",
                "Joined 3 months ago",
                "Joined last year",
                "Joined before the protagonist arrived"
            ])

    };

    return npc;
}


/* =========================================================
   CREATE POST
   ========================================================= */

function createPost(npc){

    const scenario = pick(SCENARIOS);

    let text = pick(scenario.posts);

    /*
       Small contextual additions so posts feel like
       individual NPCs rather than copied status messages.
    */

    const additions = [

        "",

        "",

        "",

        " — " + npc.job + " problems.",

        " Apparently this is my life now.",

        " I should probably stop asking questions.",

        " Anyway, my shift ends in four hours.",

        " Nobody put that in the quest description.",

        " I am not emotionally compensated for this.",

        " Management says everything is normal."

    ];

    if(Math.random() < .42){
        text += pick(additions);
    }

    const post = {

        id:uid("post"),

        npcId:npc.id,

        text:text,

        scenario:scenario.label + " · " + scenario.category,

        category:scenario.category,

        time:relativeTime(),

        likes:number(2,850000),

        commentsCount:number(0,18000),

        shares:number(0,8000),

        liked:false,

        comments:[],

        image:
            Math.random() < .20
            ? pick(["🎮","🏰","👻","🚀","☢️","📚","🏫","🏢","🧙","🤖"])
            : null

    };

    npc.posts.push(post);

    return post;
}


/* =========================================================
   BUILD WORLD
   ========================================================= */

function generateWorld(){

    NPCS = [];
    POSTS = [];

    const count = 70;

    for(let i=0;i<count;i++){

        const npc = createNPC();

        NPCS.push(npc);

        const numberOfPosts = number(2,6);

        for(let p=0;p<numberOfPosts;p++){

            const post = createPost(npc);

            POSTS.push(post);

        }

    }

    /*
       Make the first NPC the current temporary user.
    */

    CURRENT_NPC = NPCS[0];

    /*
       Shuffle feed.
    */

    POSTS.sort(()=>Math.random()-.5);

    VISIBLE_POSTS = 12;

    CURRENT_VIEW = "home";
}


/* =========================================================
   RENDER CURRENT USER
   ========================================================= */

function renderCurrentUser(){

    const left = document.getElementById("leftUser");

    if(!CURRENT_NPC){
        left.innerHTML="";
        return;
    }

    left.innerHTML = `

        <div class="current-user-mini">

            <div class="mini-avatar">
                ${escapeHTML(CURRENT_NPC.avatar)}
            </div>

            <div class="mini-info">

                <div class="mini-name">
                    ${escapeHTML(CURRENT_NPC.name)}
                </div>

                <div class="mini-location">
                    ${escapeHTML(CURRENT_NPC.location)}
                </div>

            </div>

        </div>

    `;


    document.getElementById("composer").innerHTML = `

        <div class="card composer">

            <div class="composer-top">

                <div class="composer-avatar">
                    ${escapeHTML(CURRENT_NPC.avatar)}
                </div>

                <div
                    class="composer-input"
                    onclick="createPostDialog()"
                >
                    What's on your NPC mind?
                </div>

            </div>

            <div class="composer-actions">

                <button onclick="createPostDialog()">
                    🎥 Live
                </button>

                <button onclick="createPostDialog()">
                    📷 Photo
                </button>

                <button onclick="createPostDialog()">
                    😊 Feeling
                </button>

            </div>

        </div>

    `;
}


/* =========================================================
   RENDER POST
   ========================================================= */

function renderPost(post){

    const npc = NPCS.find(n=>n.id === post.npcId);

    if(!npc){
        return "";
    }

    const commentsHTML = post.comments.length
        ? `
            <div class="comments">

                ${post.comments.slice(-4).map(comment=>`

                    <div class="comment">

                        <strong>
                            ${escapeHTML(comment.name)}
                        </strong>

                        ${escapeHTML(comment.text)}

                    </div>

                `).join("")}

            </div>
        `
        : "";

    return `

        <article
            class="card post"
            id="post-${post.id}"
        >

            <div class="post-header">

                <div
                    class="post-avatar"
                    onclick="openProfile('${npc.id}')"
                    title="View ${escapeHTML(npc.name)}"
                >
                    ${escapeHTML(npc.avatar)}
                </div>

                <div class="post-author">

                    <div
                        class="post-author-name"
                        onclick="openProfile('${npc.id}')"
                    >
                        ${escapeHTML(npc.name)}

                        ${
                            npc.verified
                            ? `<span style="color:#1877f2">✓</span>`
                            : ""
                        }

                    </div>

                    <div class="post-author-sub">

                        <span>${escapeHTML(npc.handle)}</span>

                        <span>·</span>

                        <span>${escapeHTML(post.time)}</span>

                        <span>·</span>

                        <span>🌍</span>

                    </div>

                </div>

                <button
                    class="post-menu"
                    onclick="postMenu('${post.id}')"
                    aria-label="Post menu"
                >
                    ⋯
                </button>

            </div>


            <div class="scenario">
                ${escapeHTML(post.scenario)}
            </div>


            <div class="post-text">
                ${escapeHTML(post.text)}
            </div>


            ${
                post.image
                ?
                `
                <div class="post-image">
                    ${escapeHTML(post.image)}
                </div>
                `
                :
                ""
            }


            <div class="reaction-row">

                <div class="reactions">

                    <div class="reaction-icons">

                        <span class="reaction-icon reaction-blue">
                            👍
                        </span>

                        <span class="reaction-icon reaction-red">
                            ❤️
                        </span>

                        <span class="reaction-icon reaction-yellow">
                            😂
                        </span>

                    </div>

                    <span class="reaction-count">
                        ${formatNumber(post.likes)}
                    </span>

                </div>


                <div>
                    ${formatNumber(post.comments.length || post.commentsCount)}
                    comments ·
                    ${formatNumber(post.shares)}
                    shares
                </div>

            </div>


            <div class="post-buttons">

                <button
                    class="${post.liked ? "active" : ""}"
                    onclick="likePost('${post.id}')"
                >
                    👍 Like
                </button>

                <button
                    onclick="toggleComments('${post.id}')"
                >
                    💬 Comment
                </button>

                <button
                    onclick="sharePost('${post.id}')"
                >
                    ↗ Share
                </button>

            </div>


            <div
                class="comment-area"
                id="comments-${post.id}"
            >

                <input
                    class="comment-input"
                    id="input-${post.id}"
                    placeholder="Write a comment..."
                    maxlength="300"
                    onkeydown="
                        if(event.key==='Enter'){
                            addComment('${post.id}')
                        }
                    "
                >

                <button
                    class="comment-send"
                    onclick="addComment('${post.id}')"
                >
                    Post
                </button>

            </div>


            ${commentsHTML}

        </article>

    `;
}


/* =========================================================
   RENDER FEED
   ========================================================= */

function renderFeed(){

    const feed = document.getElementById("feed");

    if(!feed){
        return;
    }

    let posts = [...POSTS];

    if(FEED_SORT === "popular"){

        posts.sort((a,b)=>b.likes-a.likes);

    }else{

        /*
           Keep temporary feed randomized.
        */

        posts.sort((a,b)=>{

            const order = {
                "3m":1,
                "8m":2,
                "14m":3,
                "27m":4,
                "1h":5,
                "2h":6,
                "3h":7,
                "5h":8,
                "8h":9,
                "12h":10,
                "Yesterday":11
            };

            return (order[a.time] || 99) - (order[b.time] || 99);

        });

    }


    posts = posts.slice(0,VISIBLE_POSTS);


    if(!posts.length){

        feed.innerHTML = `
            <div class="card empty">
                No NPC posts found.
            </div>
        `;

    }else{

        feed.innerHTML = posts.map(renderPost).join("");

    }


    const load = document.getElementById("loadMore");

    if(posts.length >= POSTS.length){

        load.style.display="none";

    }else{

        load.style.display="block";

    }
}


/* =========================================================
   LOAD MORE
   ========================================================= */

function loadMorePosts(){

    VISIBLE_POSTS += 8;

    renderFeed();

}


/* =========================================================
   PROFILE
   ========================================================= */

function openProfile(id){

    const npc = NPCS.find(n=>n.id===id);

    if(!npc){
        return;
    }

    CURRENT_VIEW = "profile";
    CURRENT_NPC = npc;

    document.getElementById("homeView").style.display="none";
    document.getElementById("profileView").style.display="block";

    renderProfile(npc);

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });
}


function openMyProfile(){

    if(!CURRENT_NPC){
        return;
    }

    openProfile(CURRENT_NPC.id);
}


function renderProfile(npc){

    const container =
        document.getElementById("profileContent");

    const posts =
        POSTS
            .filter(post=>post.npcId===npc.id)
            .sort(()=>Math.random()-.5);


    container.innerHTML = `

        <div class="card">

            <div class="profile-cover"></div>

            <div class="profile-body">

                <div class="profile-avatar">

                    ${escapeHTML(npc.avatar)}

                    ${
                        npc.online
                        ?
                        `<span class="online-dot"></span>`
                        :
                        ""
                    }

                </div>


                <div class="profile-name">

                    ${escapeHTML(npc.name)}

                    ${
                        npc.verified
                        ?
                        `<span style="color:#1877f2">✓</span>`
                        :
                        ""
                    }

                </div>


                <div class="profile-handle">
                    ${escapeHTML(npc.handle)}
                </div>


                <div class="profile-bio">
                    ${escapeHTML(npc.bio)}
                </div>


                <div class="profile-info">

                    <span class="info-pill">
                        ${escapeHTML(npc.typeIcon)}
                        ${escapeHTML(npc.type)}
                    </span>

                    <span class="info-pill">
                        💼 ${escapeHTML(npc.job)}
                    </span>

                    <span class="info-pill">
                        📍 ${escapeHTML(npc.location)}
                    </span>

                    <span class="info-pill">
                        🎮 Level ${npc.level}
                    </span>

                </div>


                <div class="profile-stats">

                    <span>
                        <strong>
                            ${formatNumber(npc.followers)}
                        </strong>
                        followers
                    </span>

                    <span>
                        <strong>
                            ${formatNumber(npc.following)}
                        </strong>
                        following
                    </span>

                    <span>
                        <strong>
                            ${npc.posts.length}
                        </strong>
                        posts
                    </span>

                </div>


                <div class="profile-buttons">

                    <button
                        class="primary-btn"
                        onclick="followNPC('${npc.id}')"
                    >
                        👥 Follow
                    </button>

                    <button
                        class="secondary-btn"
                        onclick="messageNPC('${npc.id}')"
                    >
                        💬 Message
                    </button>

                    <button
                        class="secondary-btn"
                        onclick="toast('NPC profile link copied — probably.')"
                    >
                        🔗 Share
                    </button>

                </div>

            </div>

        </div>


        <div class="profile-posts-title">
            ${escapeHTML(npc.name)}'s Posts
        </div>


        ${
            posts.length
            ?
            posts.map(renderPost).join("")
            :
            `
                <div class="card empty">
                    This NPC has not posted anything yet.
                </div>
            `
        }

    `;

}


/* =========================================================
   HOME VIEW
   ========================================================= */

function showHomeView(){

    CURRENT_VIEW="home";

    document.getElementById("profileView").style.display="none";
    document.getElementById("homeView").style.display="block";

    renderCurrentUser();
    renderFeed();

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });
}


/* =========================================================
   HOME = FULL PAGE REFRESH
   ========================================================= */

function goHome(){

    /*
       IMPORTANT:
       Reloading generates a completely new temporary NPC world.
       There is intentionally no browser storage.
    */

    window.location.reload();

}


/* =========================================================
   LIKE
   ========================================================= */

function likePost(id){

    const post = POSTS.find(p=>p.id===id);

    if(!post){
        return;
    }

    if(post.liked){

        post.liked=false;
        post.likes=Math.max(0,post.likes-1);

    }else{

        post.liked=true;
        post.likes++;

    }

    renderCurrentVisibleView();

}


/* =========================================================
   COMMENTS
   ========================================================= */

function toggleComments(id){

    const box =
        document.getElementById("comments-"+id);

    if(!box){
        return;
    }

    box.classList.toggle("open");

    if(box.classList.contains("open")){

        const input =
            document.getElementById("input-"+id);

        if(input){
            setTimeout(()=>{
                input.focus();
            },50);
        }

    }

}


function addComment(id){

    const input =
        document.getElementById("input-"+id);

    if(!input){
        return;
    }

    const text =
        input.value.trim();

    if(!text){
        return;
    }

    const post =
        POSTS.find(p=>p.id===id);

    if(!post){
        return;
    }

    post.comments.push({

        name:CURRENT_NPC.name,

        text:text

    });

    post.commentsCount++;

    input.value="";

    toast("Comment posted.");

    renderCurrentVisibleView();

}


/* =========================================================
   SHARE
   ========================================================= */

function sharePost(id){

    const post =
        POSTS.find(p=>p.id===id);

    if(!post){
        return;
    }

    post.shares++;

    toast("Post shared into the NPC dimension.");

    renderCurrentVisibleView();

}


/* =========================================================
   FOLLOW
   ========================================================= */

function followNPC(id){

    const npc =
        NPCS.find(n=>n.id===id);

    if(!npc){
        return;
    }

    npc.followers++;

    toast("You followed " + npc.name + ".");

    renderCurrentVisibleView();

}


/* =========================================================
   MESSAGE
   ========================================================= */

function messageNPC(id){

    const npc =
        NPCS.find(n=>n.id===id);

    if(!npc){
        return;
    }

    toast(
        "Message sent to " +
        npc.name +
        ". They may answer after their quest."
    );

}


/* =========================================================
   CREATE POST
   ========================================================= */

function createPostDialog(){

    const text =
        prompt(
            "Write an NPC post:",
            ""
        );

    if(text === null){
        return;
    }

    const cleaned =
        text.trim();

    if(!cleaned){
        return;
    }

    const post = {

        id:uid("post"),

        npcId:CURRENT_NPC.id,

        text:cleaned,

        scenario:"🌍 NPCBook · User Created",

        category:"USER",

        time:"now",

        likes:0,

        commentsCount:0,

        shares:0,

        liked:false,

        comments:[],

        image:null

    };

    CURRENT_NPC.posts.unshift(post);

    POSTS.unshift(post);

    toast("Your NPC post is live.");

    showHomeView();

}


/* =========================================================
   RANDOM POST
   ========================================================= */

function generateRandomPost(){

    const npc = pick(NPCS);

    const post = createPost(npc);

    POSTS.unshift(post);

    toast(
        "New post from " +
        npc.name
    );

    renderCurrentVisibleView();

}


/* =========================================================
   NEW NPC
   ========================================================= */

function generateNPC(){

    const npc =
        createNPC();

    NPCS.push(npc);

    const numberOfPosts =
        number(2,5);

    for(let i=0;i<numberOfPosts;i++){

        const post =
            createPost(npc);

        POSTS.unshift(post);

    }

    toast(
        "Generated " +
        npc.name +
        " from " +
        npc.country
    );

    openProfile(npc.id);

}


/* =========================================================
   NEW WORLD
   ========================================================= */

function newWorld(){

    generateWorld();

    renderEverything();

    toast("A completely new NPC world has been generated.");

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });

}


/* =========================================================
   SEARCH
   ========================================================= */

function searchSite(query){

    const q =
        query.trim().toLowerCase();

    if(!q){

        renderFeed();

        return;
    }

    const matchingNPCs =
        NPCS.filter(npc=>
            (
                npc.name +
                " " +
                npc.country +
                " " +
                npc.city +
                " " +
                npc.job +
                " " +
                npc.type
            )
            .toLowerCase()
            .includes(q)
        );

    const matchingPosts =
        POSTS.filter(post=>{

            const npc =
                NPCS.find(n=>n.id===post.npcId);

            return (
                post.text +
                " " +
                post.scenario +
                " " +
                (npc ? npc.name : "")
            )
            .toLowerCase()
            .includes(q);

        });


    const feed =
        document.getElementById("feed");


    let html="";


    if(matchingNPCs.length){

        html += `

            <div class="card">

                <div class="post">

                    <div style="font-weight:900;margin-bottom:10px">
                        NPCs
                    </div>

                    ${matchingNPCs.slice(0,8).map(npc=>`

                        <div
                            class="friend"
                            onclick="openProfile('${npc.id}')"
                            style="cursor:pointer"
                        >

                            <div class="friend-avatar">
                                ${escapeHTML(npc.avatar)}
                            </div>

                            <div class="friend-info">

                                <div class="friend-name">
                                    ${escapeHTML(npc.name)}
                                </div>

                                <div class="friend-location">
                                    ${escapeHTML(npc.location)}
                                    ·
                                    ${escapeHTML(npc.job)}
                                </div>

                            </div>

                        </div>

                    `).join("")}

                </div>

            </div>

        `;

    }


    if(matchingPosts.length){

        html += matchingPosts
            .slice(0,VISIBLE_POSTS)
            .map(renderPost)
            .join("");

    }


    if(!html){

        html = `

            <div class="card empty">

                No NPC or post matches
                "<strong>${escapeHTML(query)}</strong>".

            </div>

        `;

    }


    feed.innerHTML=html;

}


/* =========================================================
   SEARCH INPUT
   ========================================================= */

document
    .getElementById("searchInput")
    .addEventListener("input",function(){

        searchSite(this.value);

    });


/* =========================================================
   SORT FEED
   ========================================================= */

function sortFeed(){

    if(FEED_SORT==="latest"){

        FEED_SORT="popular";

        toast("Showing popular NPC posts.");

    }else{

        FEED_SORT="latest";

        toast("Showing latest NPC posts.");

    }

    renderFeed();

}


/* =========================================================
   POST MENU
   ========================================================= */

function postMenu(id){

    const choice =
        prompt(
            "NPC post options:\n\n" +
            "1. Copy imaginary link\n" +
            "2. Hide post\n" +
            "3. Report for being too NPC\n\n" +
            "Enter 1, 2 or 3:"
        );

    if(choice==="1"){

        toast("Imaginary link copied.");

    }else if(choice==="2"){

        const index =
            POSTS.findIndex(p=>p.id===id);

        if(index>=0){

            POSTS.splice(index,1);

            renderCurrentVisibleView();

            toast("Post hidden.");

        }

    }else if(choice==="3"){

        toast("Report received. The NPC council is investigating.");

    }

}


/* =========================================================
   NOTIFICATIONS
   ========================================================= */

function showNotifications(){

    toast(
        pick([
            "You have 7 new NPC notifications.",
            "The village guard liked your post.",
            "Someone completed your quest.",
            "A mysterious stranger viewed your profile.",
            "Your NPC reputation increased by 2."
        ])
    );

}


/* =========================================================
   MESSAGES
   ========================================================= */

function showMessages(){

    const npc =
        pick(NPCS);

    toast(
        npc.name +
        " sent: \"Are you also waiting for the next quest?\""
    );

}


/* =========================================================
   TRENDING
   ========================================================= */

function showTrending(){

    CURRENT_VIEW="home";

    document.getElementById("profileView").style.display="none";
    document.getElementById("homeView").style.display="block";

    const feed =
        document.getElementById("feed");

    const popular =
        [...POSTS]
            .sort((a,b)=>b.likes-a.likes)
            .slice(0,12);

    feed.innerHTML = `

        <div class="card">

            <div class="post">

                <div style="font-size:20px;font-weight:900">
                    🔥 Trending NPC Posts
                </div>

                <div style="margin-top:5px;color:#65676b">
                    The things NPCs cannot stop talking about.
                </div>

            </div>

        </div>

        ${popular.map(renderPost).join("")}

    `;

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });

}


/* =========================================================
   FRIENDS
   ========================================================= */

function showFriends(){

    CURRENT_VIEW="home";

    document.getElementById("profileView").style.display="none";
    document.getElementById("homeView").style.display="block";

    const feed =
        document.getElementById("feed");

    const people =
        [...NPCS]
            .sort(()=>Math.random()-.5)
            .slice(0,20);

    feed.innerHTML = `

        <div class="card">

            <div class="post">

                <div style="font-size:20px;font-weight:900">
                    👥 NPCs You May Know
                </div>

                <div style="margin-top:5px;color:#65676b">
                    You probably have nothing in common.
                    Follow them anyway.
                </div>

            </div>

        </div>

        <div class="card">

            <div class="post">

                ${people.map(npc=>`

                    <div
                        class="friend"
                        onclick="openProfile('${npc.id}')"
                        style="cursor:pointer"
                    >

                        <div class="friend-avatar">
                            ${escapeHTML(npc.avatar)}
                        </div>

                        <div class="friend-info">

                            <div class="friend-name">
                                ${escapeHTML(npc.name)}
                            </div>

                            <div class="friend-location">
                                ${escapeHTML(npc.location)}
                                ·
                                ${escapeHTML(npc.type)}
                            </div>

                        </div>

                    </div>

                `).join("")}

            </div>

        </div>

    `;

}


/* =========================================================
   QUESTS
   ========================================================= */

function showQuests(){

    const feed =
        document.getElementById("feed");

    document.getElementById("profileView").style.display="none";
    document.getElementById("homeView").style.display="block";

    const quests = [

        ["Find the Protagonist","Locate the person causing 83% of local problems.",72],
        ["Deliver the Plot Device","Nobody knows what it does. Deliver it anyway.",41],
        ["Survive Monday","Reward: emotional damage resistance.",89],
        ["Fix the Printer","Difficulty: Legendary.",17],
        ["Do Not Enter the Basement","Obviously enter the basement.",63],
        ["Find the Missing Dialogue","Quest giver forgot what he was supposed to say.",51],
        ["Defeat the Final Boss","The final boss is currently on vacation.",28],
        ["Pay Rent","The most difficult quest in every universe.",96],
        ["Locate the Main Character","They are probably standing near a dramatic sunset.",37]
    ];

    feed.innerHTML = `

        <div class="card">

            <div class="post">

                <div style="font-size:20px;font-weight:900">
                    ⚔️ NPC Quests
                </div>

                <div style="margin-top:5px;color:#65676b">
                    Side quests nobody asked for.
                </div>

            </div>

        </div>


        <div class="card">

            <div class="post">

                ${quests.map(q=>`

                    <div
                        style="
                            padding:12px 0;
                            border-bottom:1px solid #e4e6eb;
                        "
                    >

                        <div style="font-weight:900">
                            ${escapeHTML(q[0])}
                        </div>

                        <div
                            style="
                                color:#65676b;
                                font-size:13px;
                                margin-top:4px;
                            "
                        >
                            ${escapeHTML(q[1])}
                        </div>

                        <div
                            style="
                                height:7px;
                                background:#e4e6eb;
                                border-radius:10px;
                                overflow:hidden;
                                margin-top:8px;
                            "
                        >

                            <div
                                style="
                                    height:100%;
                                    width:${q[2]}%;
                                    background:#1877f2;
                                "
                            ></div>

                        </div>

                    </div>

                `).join("")}

            </div>

        </div>

    `;

}


/* =========================================================
   MARKET
   ========================================================= */

function showMarket(){

    const feed =
        document.getElementById("feed");

    document.getElementById("profileView").style.display="none";
    document.getElementById("homeView").style.display="block";

    const items = [

        ["Legendary Sword","Probably rusty.","1,999 gold"],
        ["Healing Potion","Works approximately 70% of the time.","450 gold"],
        ["Plot Armor","Sold out. Obviously.","999,999 gold"],
        ["Suspicious Map","It says 'You Are Here.'","120 gold"],
        ["Mystery Key","No one knows what it opens.","75 gold"],
        ["NPC Employment Contract","Includes no benefits.","3 gold"],
        ["Dungeon Cleaning Service","We remove monsters and protagonists.","800 gold"],
        ["Ancient Prophecy","Lightly used.","50 gold"],
        ["Invisible Cloak","You may already be wearing it.","2,500 gold"]
    ];

    feed.innerHTML = `

        <div class="card">

            <div class="post">

                <div style="font-size:20px;font-weight:900">
                    🛒 NPC Marketplace
                </div>

                <div style="margin-top:5px;color:#65676b">
                    Items acquired through questionable quest design.
                </div>

            </div>

        </div>


        <div class="card">

            <div class="post">

                ${items.map(item=>`

                    <div
                        style="
                            display:flex;
                            justify-content:space-between;
                            gap:12px;
                            padding:12px 0;
                            border-bottom:1px solid #e4e6eb;
                        "
                    >

                        <div>

                            <div style="font-weight:900">
                                ${escapeHTML(item[0])}
                            </div>

                            <div
                                style="
                                    color:#65676b;
                                    font-size:12px;
                                    margin-top:3px;
                                "
                            >
                                ${escapeHTML(item[1])}
                            </div>

                        </div>

                        <div
                            style="
                                color:#17803d;
                                font-weight:900;
                                white-space:nowrap;
                            "
                        >
                            ${escapeHTML(item[2])}
                        </div>

                    </div>

                `).join("")}

            </div>

        </div>

    `;

}


/* =========================================================
   SETTINGS
   ========================================================= */

function showSettings(){

    const feed =
        document.getElementById("feed");

    document.getElementById("profileView").style.display="none";
    document.getElementById("homeView").style.display="block";

    feed.innerHTML = `

        <div class="card">

            <div class="post">

                <div style="font-size:20px;font-weight:900">
                    ⚙️ NPCBook Settings
                </div>

                <div style="margin-top:15px">

                    <div
                        style="
                            padding:12px 0;
                            border-bottom:1px solid #e4e6eb;
                        "
                    >
                        🌍 Global NPC generation
                        <span style="float:right">ON</span>
                    </div>

                    <div
                        style="
                            padding:12px 0;
                            border-bottom:1px solid #e4e6eb;
                        "
                    >
                        💾 Browser storage
                        <span style="float:right">OFF</span>
                    </div>

                    <div
                        style="
                            padding:12px 0;
                            border-bottom:1px solid #e4e6eb;
                        "
                    >
                        🗄️ Database
                        <span style="float:right">NONE</span>
                    </div>

                    <div
                        style="
                            padding:12px 0;
                            border-bottom:1px solid #e4e6eb;
                        "
                    >
                        🔄 New world on refresh
                        <span style="float:right">ON</span>
                    </div>

                    <div
                        style="
                            padding:12px 0;
                        "
                    >
                        📱 Responsive interface
                        <span style="float:right">ON</span>
                    </div>

                </div>

            </div>

        </div>

    `;

}


/* =========================================================
   RENDER SIDEBARS
   ========================================================= */

function renderTrending(){

    const el =
        document.getElementById("trending");

    const trends = [

        ["#NPCProblems",number(12,900)+"K posts"],
        ["#ProtagonistProblems",number(4,600)+"K posts"],
        ["#DungeonLife",number(3,500)+"K posts"],
        ["#OfficeNPC",number(2,800)+"K posts"],
        ["#MainCharacterEnergy",number(2,700)+"K posts"],
        ["#QuestFailed",number(1,900)+"K posts"],
        ["#NightShiftNPC",number(800,1900)+"K posts"]
    ];

    el.innerHTML =
        trends.map(t=>`

            <div class="trend">

                <div class="trend-small">
                    Trending
                </div>

                <div class="trend-name">
                    ${escapeHTML(t[0])}
                </div>

                <div class="trend-small">
                    ${escapeHTML(t[1])}
                </div>

            </div>

        `).join("");

}


function renderSuggestions(){

    const el =
        document.getElementById("suggestions");

    const people =
        [...NPCS]
            .filter(n=>n.id!==CURRENT_NPC.id)
            .sort(()=>Math.random()-.5)
            .slice(0,5);

    el.innerHTML =
        people.map(npc=>`

            <div
                class="friend"
                onclick="openProfile('${npc.id}')"
                style="cursor:pointer"
            >

                <div class="friend-avatar">
                    ${escapeHTML(npc.avatar)}
                </div>

                <div class="friend-info">

                    <div class="friend-name">
                        ${escapeHTML(npc.name)}
                    </div>

                    <div class="friend-location">
                        ${escapeHTML(npc.country)}
                    </div>

                </div>

            </div>

        `).join("");

}


function renderQuestsSidebar(){

    const el =
        document.getElementById("quests");

    const quests = [

        ["Find the Protagonist",72],
        ["Survive Monday",89],
        ["Fix the Printer",17],
        ["Deliver the Plot Device",41],
        ["Don't Enter the Basement",63]

    ];

    el.innerHTML =
        quests.map(q=>`

            <div class="trend">

                <div class="trend-name">
                    ${escapeHTML(q[0])}
                </div>

                <div
                    style="
                        height:6px;
                        margin-top:7px;
                        border-radius:10px;
                        background:#e4e6eb;
                        overflow:hidden;
                    "
                >

                    <div
                        style="
                            width:${q[1]}%;
                            height:100%;
                            background:#1877f2;
                        "
                    ></div>

                </div>

                <div class="trend-small" style="margin-top:4px">
                    ${q[1]}% complete
                </div>

            </div>

        `).join("");

}


/* =========================================================
   RENDER EVERYTHING
   ========================================================= */

function renderEverything(){

    renderCurrentUser();

    renderFeed();

    renderTrending();

    renderSuggestions();

    renderQuestsSidebar();

}


/* =========================================================
   RE-RENDER CURRENT VIEW
   ========================================================= */

function renderCurrentVisibleView(){

    if(CURRENT_VIEW==="profile"){

        renderProfile(CURRENT_NPC);

    }else{

        renderFeed();

    }

}


/* =========================================================
   INITIALIZE
   ========================================================= */

generateWorld();

renderEverything();


/*
   Keyboard shortcut:
   / focuses search on desktop keyboards.
*/

document.addEventListener("keydown",function(event){

    if(
        event.key === "/" &&
        document.activeElement.tagName !== "INPUT" &&
        document.activeElement.tagName !== "TEXTAREA"
    ){

        event.preventDefault();

        const search =
            document.getElementById("searchInput");

        if(search){

            search.focus();

        }

    }

});


/*
   Prevent accidental zoom-like double tap behavior
   on interactive buttons where possible without
   disabling normal browser accessibility.
*/

document.addEventListener(
    "touchstart",
    function(){},
    {passive:true}
);

</script>

</body>
</html>
'''

Path("index.html").write_text(HTML, encoding="utf-8")

print("NPCBook generated successfully.")
print("Responsive social-media site created.")
print("Output: index.html")
