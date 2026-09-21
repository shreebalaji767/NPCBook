from pathlib import Path

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#111827">
<meta name="description" content="NPCBook — Social Media for NPCs">
<title>NPCBook — Social Media for NPCs</title>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family:
        Inter,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    background: #f0f2f5;
    color: #172033;
    min-height: 100vh;
}

/* =========================
   HEADER
========================= */

.topbar {
    position: sticky;
    top: 0;
    z-index: 1000;
    height: 64px;
    background: #ffffff;
    border-bottom: 1px solid #dfe3e8;
    display: flex;
    align-items: center;
}

.topbar-inner {
    width: min(1400px, 100%);
    margin: auto;
    padding: 0 16px;
    display: flex;
    align-items: center;
    gap: 18px;
}

.logo {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 23px;
    font-weight: 900;
    color: #1877f2;
    cursor: pointer;
    user-select: none;
    white-space: nowrap;
}

.logo:hover {
    opacity: .8;
}

.search {
    flex: 1;
    max-width: 420px;
}

.search input {
    width: 100%;
    height: 42px;
    border: 0;
    outline: none;
    background: #f0f2f5;
    border-radius: 22px;
    padding: 0 18px;
    font-size: 15px;
}

.header-actions {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 8px;
}

.icon-btn {
    width: 42px;
    height: 42px;
    border: 0;
    border-radius: 50%;
    background: #f0f2f5;
    cursor: pointer;
    font-size: 19px;
    display: grid;
    place-items: center;
    touch-action: manipulation;
}

.icon-btn:hover {
    background: #e4e6eb;
}

/* =========================
   LAYOUT
========================= */

.page {
    width: min(1400px, 100%);
    margin: auto;
    padding: 20px 16px 100px;
}

.layout {
    display: grid;
    grid-template-columns: 250px minmax(0, 650px) 280px;
    gap: 20px;
    justify-content: center;
    align-items: start;
}

/* =========================
   SIDEBARS
========================= */

.sidebar,
.rightbar {
    position: sticky;
    top: 84px;
}

.menu {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.menu button {
    width: 100%;
    min-height: 50px;
    border: 0;
    background: transparent;
    border-radius: 10px;
    padding: 10px 12px;
    text-align: left;
    cursor: pointer;
    font-size: 15px;
    font-weight: 700;
    color: #273142;
    display: flex;
    align-items: center;
    gap: 12px;
    touch-action: manipulation;
}

.menu button:hover {
    background: #e4e6eb;
}

.menu-icon {
    width: 30px;
    text-align: center;
    font-size: 21px;
}

/* =========================
   CARDS
========================= */

.card {
    background: #ffffff;
    border: 1px solid #dfe3e8;
    border-radius: 12px;
    margin-bottom: 16px;
    overflow: hidden;
}

.card-header {
    padding: 14px 16px;
}

.card-body {
    padding: 16px;
}

.section-title {
    font-size: 18px;
    font-weight: 800;
}

/* =========================
   PROFILE
========================= */

.profile-cover {
    height: 125px;
    background:
        linear-gradient(
            135deg,
            #667eea,
            #764ba2,
            #f093fb
        );
}

.profile-main {
    padding: 0 18px 18px;
}

.avatar {
    width: 78px;
    height: 78px;
    border-radius: 50%;
    border: 5px solid white;
    margin-top: -39px;
    background: #edf2f7;
    display: grid;
    place-items: center;
    font-size: 40px;
    position: relative;
}

.profile-name {
    margin-top: 8px;
    font-size: 21px;
    font-weight: 900;
}

.profile-handle {
    color: #697386;
    margin-top: 2px;
}

.profile-bio {
    margin-top: 10px;
    line-height: 1.5;
    color: #3f4a5a;
}

.profile-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    margin-top: 15px;
    gap: 8px;
}

.stat {
    background: #f7f8fa;
    border-radius: 9px;
    padding: 10px;
    text-align: center;
}

.stat strong {
    display: block;
    font-size: 18px;
}

.stat span {
    color: #697386;
    font-size: 12px;
}

/* =========================
   COMPOSER
========================= */

.composer {
    padding: 15px;
}

.composer-row {
    display: flex;
    gap: 12px;
    align-items: center;
}

.mini-avatar {
    width: 45px;
    height: 45px;
    flex: 0 0 45px;
    border-radius: 50%;
    background: #edf2f7;
    display: grid;
    place-items: center;
    font-size: 24px;
}

.fake-input {
    flex: 1;
    background: #f0f2f5;
    border-radius: 24px;
    padding: 13px 17px;
    color: #6b7280;
    cursor: pointer;
}

.composer-actions {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    margin-top: 12px;
}

.action-light {
    min-height: 42px;
    border: 0;
    background: white;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 700;
    color: #566173;
    touch-action: manipulation;
}

.action-light:hover {
    background: #f0f2f5;
}

/* =========================
   POSTS
========================= */

.post {
    padding: 15px;
}

.post-head {
    display: flex;
    align-items: center;
    gap: 10px;
}

.post-avatar {
    width: 46px;
    height: 46px;
    border-radius: 50%;
    background: #edf2f7;
    display: grid;
    place-items: center;
    font-size: 25px;
    flex: 0 0 46px;
}

.post-author {
    min-width: 0;
}

.post-name {
    font-weight: 800;
}

.post-meta {
    color: #7a8494;
    font-size: 12px;
    margin-top: 2px;
}

.post-text {
    margin: 13px 0;
    line-height: 1.55;
    white-space: pre-wrap;
    word-break: break-word;
}

.post-tag {
    display: inline-block;
    background: #eef4ff;
    color: #1877f2;
    padding: 5px 9px;
    border-radius: 15px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 10px;
}

.post-stats {
    display: flex;
    justify-content: space-between;
    color: #707988;
    font-size: 13px;
    padding-bottom: 9px;
    border-bottom: 1px solid #e5e7eb;
}

.post-actions {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 5px;
    margin-top: 6px;
}

.post-actions button {
    min-height: 44px;
    border: 0;
    background: transparent;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 700;
    color: #5b6574;
    touch-action: manipulation;
}

.post-actions button:hover {
    background: #f0f2f5;
}

.post-actions button.liked {
    color: #1877f2;
}

.comment-box {
    display: none;
    margin-top: 10px;
    gap: 8px;
}

.comment-box.active {
    display: flex;
}

.comment-box input {
    min-width: 0;
    flex: 1;
    border: 1px solid #d5dae1;
    border-radius: 20px;
    padding: 10px 14px;
    outline: none;
}

.comment-box button {
    border: 0;
    background: #1877f2;
    color: white;
    border-radius: 20px;
    padding: 0 15px;
    font-weight: 700;
    cursor: pointer;
}

/* =========================
   RIGHT BAR
========================= */

.right-card {
    padding: 15px;
}

.right-title {
    font-size: 17px;
    font-weight: 900;
    margin-bottom: 12px;
}

.trend {
    padding: 10px 0;
    border-bottom: 1px solid #edf0f3;
}

.trend:last-child {
    border-bottom: 0;
}

.trend-small {
    color: #788291;
    font-size: 12px;
}

.trend-name {
    font-weight: 800;
    margin: 3px 0;
}

.quest {
    padding: 10px 0;
    border-bottom: 1px solid #edf0f3;
}

.quest:last-child {
    border-bottom: 0;
}

.quest-title {
    font-weight: 800;
}

.quest-progress {
    margin-top: 7px;
    height: 7px;
    border-radius: 10px;
    background: #e9edf2;
    overflow: hidden;
}

.quest-progress span {
    display: block;
    height: 100%;
    background: #1877f2;
}

/* =========================
   MARKET
========================= */

.market-item {
    padding: 11px 0;
    border-bottom: 1px solid #edf0f3;
}

.market-item:last-child {
    border-bottom: 0;
}

.market-name {
    font-weight: 800;
}

.market-price {
    color: #16803c;
    font-weight: 800;
    margin-top: 3px;
}

/* =========================
   MOBILE NAV
========================= */

.mobile-nav {
    display: none;
}

/* =========================
   TOAST
========================= */

.toast {
    position: fixed;
    left: 50%;
    bottom: 24px;
    transform: translateX(-50%) translateY(100px);
    background: #111827;
    color: white;
    padding: 12px 18px;
    border-radius: 25px;
    z-index: 5000;
    opacity: 0;
    pointer-events: none;
    transition: .25s ease;
    font-size: 14px;
    text-align: center;
    max-width: calc(100vw - 30px);
}

.toast.show {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
}

/* =========================
   EMPTY
========================= */

.empty {
    padding: 35px 15px;
    text-align: center;
    color: #707988;
}

/* =========================
   RESPONSIVE
========================= */

@media (max-width: 1150px) {
    .layout {
        grid-template-columns: 210px minmax(0, 650px);
    }

    .rightbar {
        display: none;
    }
}

@media (max-width: 800px) {
    .topbar {
        height: 58px;
    }

    .topbar-inner {
        padding: 0 10px;
        gap: 8px;
    }

    .logo {
        font-size: 19px;
    }

    .search {
        display: none;
    }

    .header-actions {
        gap: 5px;
    }

    .icon-btn {
        width: 40px;
        height: 40px;
    }

    .page {
        padding: 10px 8px 90px;
    }

    .layout {
        display: block;
    }

    .sidebar {
        display: none;
    }

    .mobile-nav {
        position: fixed;
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 2000;
        background: rgba(255,255,255,.97);
        border-top: 1px solid #dfe3e8;
        padding:
            5px
            5px
            calc(5px + env(safe-area-inset-bottom));
        box-shadow: 0 -3px 12px rgba(0,0,0,.08);
    }

    .mobile-nav button {
        min-height: 54px;
        border: 0;
        background: transparent;
        border-radius: 9px;
        cursor: pointer;
        font-size: 12px;
        font-weight: 800;
        color: #566173;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 3px;
        touch-action: manipulation;
    }

    .mobile-nav button:active {
        background: #eef2f7;
    }

    .mobile-nav .nav-icon {
        font-size: 20px;
        line-height: 1;
    }

    .card {
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .profile-cover {
        height: 105px;
    }

    .profile-main {
        padding: 0 14px 15px;
    }

    .profile-stats {
        gap: 5px;
    }

    .post {
        padding: 13px;
    }

    .post-actions button {
        min-height: 46px;
    }

    .composer-actions {
        grid-template-columns: repeat(3, 1fr);
    }
}

@media (max-width: 420px) {
    .logo {
        font-size: 17px;
    }

    .header-actions .icon-btn:nth-child(3) {
        display: none;
    }

    .profile-name {
        font-size: 19px;
    }

    .post-text {
        font-size: 14px;
    }

    .mobile-nav button {
        min-height: 52px;
        font-size: 11px;
    }
}

/* Touchscreen */
@media (pointer: coarse) {
    button,
    .fake-input,
    .logo {
        -webkit-tap-highlight-color: transparent;
    }

    .menu button,
    .action-light,
    .post-actions button {
        min-height: 48px;
    }
}
</style>
</head>

<body>

<header class="topbar">
    <div class="topbar-inner">

        <!-- CLICKING LOGO = FULL REFRESH -->
        <div
            class="logo"
            onclick="goHome()"
            role="button"
            tabindex="0"
            onkeydown="if(event.key==='Enter'||event.key===' ')goHome()"
            title="Refresh NPCBook"
        >
            📱 NPCBook
        </div>

        <div class="search">
            <input
                id="searchInput"
                type="search"
                placeholder="Search NPCs, posts, quests..."
                autocomplete="off"
            >
        </div>

        <div class="header-actions">
            <button class="icon-btn" onclick="showNotifications()" aria-label="Notifications">
                🔔
            </button>

            <button class="icon-btn" onclick="showMessages()" aria-label="Messages">
                💬
            </button>

            <button class="icon-btn" onclick="newWorld()" aria-label="New World">
                🎲
            </button>
        </div>
    </div>
</header>


<main class="page">

    <div class="layout">

        <!-- LEFT SIDEBAR -->
        <aside class="sidebar">

            <div class="menu">

                <!-- HOME = FULL REFRESH -->
                <button onclick="goHome()">
                    <span class="menu-icon">🏠</span>
                    Home
                </button>

                <button onclick="showProfile()">
                    <span class="menu-icon">👤</span>
                    My NPC
                </button>

                <button onclick="showTrending()">
                    <span class="menu-icon">🔥</span>
                    Trending
                </button>

                <button onclick="showQuests()">
                    <span class="menu-icon">⚔️</span>
                    Quests
                </button>

                <button onclick="showMarket()">
                    <span class="menu-icon">🛒</span>
                    NPC Market
                </button>

                <button onclick="newNPC()">
                    <span class="menu-icon">🎲</span>
                    Generate NPC
                </button>

                <button onclick="randomPost()">
                    <span class="menu-icon">✨</span>
                    Random Post
                </button>

                <button onclick="showSettings()">
                    <span class="menu-icon">⚙️</span>
                    Settings
                </button>

            </div>

        </aside>


        <!-- MAIN FEED -->
        <section id="mainContent">

            <div id="profileCard"></div>

            <div class="card composer">
                <div class="composer-row">

                    <div class="mini-avatar" id="composerAvatar">
                        🧑
                    </div>

                    <div
                        class="fake-input"
                        onclick="randomPost()"
                    >
                        What's happening in the NPC world?
                    </div>

                </div>

                <div class="composer-actions">

                    <button class="action-light" onclick="randomPost()">
                        📝 Random Post
                    </button>

                    <button class="action-light" onclick="newNPC()">
                        👤 New NPC
                    </button>

                    <button class="action-light" onclick="newWorld()">
                        🎲 New World
                    </button>

                </div>
            </div>

            <div id="feed"></div>

        </section>


        <!-- RIGHT SIDEBAR -->
        <aside class="rightbar">

            <div class="card right-card">

                <div class="right-title">
                    🔥 NPC Trends
                </div>

                <div id="trends"></div>

            </div>


            <div class="card right-card">

                <div class="right-title">
                    ⚔️ Active Quests
                </div>

                <div id="quests"></div>

            </div>


            <div class="card right-card">

                <div class="right-title">
                    🛒 NPC Marketplace
                </div>

                <div id="market"></div>

            </div>

        </aside>

    </div>

</main>


<!-- MOBILE NAVIGATION -->
<nav class="mobile-nav">

    <!-- HOME = FULL REFRESH -->
    <button onclick="goHome()">
        <span class="nav-icon">🏠</span>
        Home
    </button>

    <button onclick="showTrending()">
        <span class="nav-icon">🔥</span>
        Trends
    </button>

    <button onclick="newNPC()">
        <span class="nav-icon">👤</span>
        NPC
    </button>

    <button onclick="showQuests()">
        <span class="nav-icon">⚔️</span>
        Quests
    </button>

    <button onclick="newWorld()">
        <span class="nav-icon">🎲</span>
        New World
    </button>

</nav>


<div id="toast" class="toast"></div>


<script>

/* =========================================================
   NPCBOOK
   NO DATABASE
   NO LOCALSTORAGE
   NO SESSIONSTORAGE
   NO APP DATA COOKIES
========================================================= */

const DATA = {

    firstNames: [
        "Bob",
        "Steve",
        "John",
        "Kevin",
        "Mike",
        "Alex",
        "Sam",
        "Gary",
        "Dave",
        "Tom",
        "Rick",
        "Ben",
        "Joe",
        "Max",
        "Jack",
        "Chris",
        "Daniel",
        "Brian",
        "NPC-001",
        "Villager-7",
        "Guard-42",
        "Shopkeeper-99",
        "Farmer-12",
        "Wizard-404",
        "Miner-8",
        "Fisher-22"
    ],

    surnames: [
        "Smith",
        "Johnson",
        "Brown",
        "Wilson",
        "Walker",
        "Miller",
        "Taylor",
        "NPCson",
        "Questman",
        "Lootkeeper",
        "Dialogue",
        "Placeholder",
        "Background",
        "Generic",
        "Default",
        "Random"
    ],

    emojis: [
        "🧑",
        "👨",
        "👩",
        "🧙",
        "🧝",
        "🧛",
        "🧟",
        "🤖",
        "👨‍🌾",
        "👨‍🔧",
        "🧑‍🍳",
        "🧑‍🎤",
        "🧑‍🚀",
        "🥷",
        "👴",
        "👵"
    ],

    locations: [
        "Starter Village",
        "Dusty Road",
        "Market District",
        "North Gate",
        "Old Castle",
        "Tutorial Zone",
        "Abandoned Mine",
        "Forest Edge",
        "Pixel City",
        "Quest Hub",
        "Generic Town",
        "Loading Screen",
        "Somewhere Nearby"
    ],

    jobs: [
        "Village Guard",
        "Blacksmith",
        "Farmer",
        "Shopkeeper",
        "Quest Giver",
        "Potion Seller",
        "Innkeeper",
        "Miner",
        "Fisherman",
        "Stable Worker",
        "Tutorial Assistant",
        "Background Character",
        "Professional Loiterer",
        "Door Opener",
        "Chest Protector",
        "Random Merchant"
    ],

    bios: [
        "I have been standing here since the game launched.",
        "Ask me about my quest. I will repeat the same dialogue.",
        "Living life one scripted interaction at a time.",
        "I have absolutely no idea what is happening.",
        "My daily routine is surprisingly predictable.",
        "I sell things nobody needs.",
        "I guard this door. Nobody knows why.",
        "Waiting for the player to return.",
        "I once walked outside the designated path.",
        "My dialogue tree has three options.",
        "I know a secret. Unfortunately, it is scripted.",
        "Just another day in the background."
    ],

    postTemplates: [
        "Anyone else standing around waiting for the player?",
        "The weather has been suspiciously identical for three days.",
        "I walked 17 meters today. Big achievement.",
        "Someone stole my favorite chair again.",
        "Just repeated the same dialogue for the 900th time.",
        "Why does everyone ask me where the blacksmith is?",
        "I have a quest for someone. I forgot what it was.",
        "Breaking news: absolutely nothing happened.",
        "I saw the player walk past me and immediately forgot their face.",
        "My inventory is 90% useless objects.",
        "I opened my shop today. Nobody bought anything.",
        "The economy makes no sense.",
        "I think I am supposed to be guarding something.",
        "Does anyone know why there is a giant invisible wall here?",
        "I accidentally walked into a wall for 12 minutes.",
        "Today's objective: continue standing here.",
        "I have been waiting for this quest since 2014.",
        "NPC meeting at 7 PM. Agenda: stand in a circle.",
        "I found a shiny rock. It is now my personality.",
        "Why do heroes never say hello?"
    ],

    tags: [
        "#NPCLife",
        "#BackgroundCharacter",
        "#QuestLife",
        "#VillageLife",
        "#NPCProblems",
        "#Gaming",
        "#DailyRoutine",
        "#PixelLife",
        "#NoMainCharacter",
        "#GenericThoughts"
    ],

    comments: [
        "Same.",
        "Real NPC behavior.",
        "I have this exact problem.",
        "Stay strong, brother.",
        "Quest accepted.",
        "This is relatable.",
        "Dialogue option unavailable.",
        "I was programmed to agree.",
        "Interesting.",
        "Please report this to the quest manager.",
        "Same location?",
        "Can confirm.",
        "The player did this yesterday too.",
        "Skill issue.",
        "This deserves more XP."
    ],

    quests: [
        "Find the Missing Spoon",
        "Talk to the Person Standing Nearby",
        "Collect 7 Extremely Ordinary Rocks",
        "Deliver This Completely Unimportant Letter",
        "Stand Near the Village Gate",
        "Find Out Who Stole the Chair",
        "Escort the Player for 12 Seconds",
        "Locate the Legendary Turnip",
        "Ask Three NPCs the Same Question",
        "Return to the Quest Giver"
    ],

    items: [
        "Suspicious Potato",
        "Wooden Spoon",
        "Rusty Sword",
        "Mysterious Rock",
        "Empty Bottle",
        "Old Boot",
        "Quest Scroll",
        "Broken Shield",
        "Common Apple",
        "Very Average Helmet",
        "NPC Hat",
        "Decorative Key",
        "Invisible Potion"
    ]

};


let WORLD = null;


/* =========================================================
   RANDOM HELPERS
========================================================= */

function pick(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function number(min, max) {
    return Math.floor(
        Math.random() * (max - min + 1)
    ) + min;
}

function uid() {

    if (
        typeof crypto !== "undefined" &&
        typeof crypto.randomUUID === "function"
    ) {
        return crypto.randomUUID();
    }

    return (
        Date.now().toString(36) +
        Math.random().toString(36).slice(2)
    );
}

function escapeHTML(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


/* =========================================================
   NPC GENERATOR
========================================================= */

function createNPC() {

    const first = pick(DATA.firstNames);
    const last = pick(DATA.surnames);

    return {

        id: uid(),

        name: `${first} ${last}`,

        handle:
            "@" +
            first.toLowerCase().replace(/[^a-z0-9]/g, "") +
            number(10, 999),

        avatar: pick(DATA.emojis),

        location: pick(DATA.locations),

        job: pick(DATA.jobs),

        bio: pick(DATA.bios),

        level: number(1, 99),

        followers: number(2, 9999),

        following: number(1, 500),

        posts: number(1, 300),

        online:
            Math.random() > 0.25

    };

}


/* =========================================================
   POST GENERATOR
========================================================= */

function createPost(npc) {

    const comments =
        Array.from(
            { length: number(0, 5) },
            () => ({
                author: pick(DATA.firstNames),
                text: pick(DATA.comments)
            })
        );

    return {

        id: uid(),

        npcId: npc.id,

        text: pick(DATA.postTemplates),

        tag: pick(DATA.tags),

        minutesAgo: number(1, 7200),

        likes: number(0, 9999),

        shares: number(0, 999),

        comments: comments,

        liked: false

    };

}


/* =========================================================
   WORLD GENERATOR
========================================================= */

function generateWorld() {

    const npcCount = number(14, 25);

    const npcs = [];

    for (let i = 0; i < npcCount; i++) {
        npcs.push(createNPC());
    }

    const posts = [];

    npcs.forEach(npc => {

        const postCount = number(1, 3);

        for (let i = 0; i < postCount; i++) {
            posts.push(createPost(npc));
        }

    });

    posts.sort(
        () => Math.random() - 0.5
    );

    const quests =
        Array.from(
            { length: 5 },
            () => ({
                title: pick(DATA.quests),
                progress: number(5, 95)
            })
        );

    const market =
        Array.from(
            { length: 5 },
            () => ({
                name: pick(DATA.items),
                price: number(5, 999)
            })
        );

    const trends =
        Array.from(
            { length: 6 },
            () => ({
                title: pick(DATA.tags),
                posts: number(12, 99999)
            })
        );

    WORLD = {

        npcs,

        posts,

        quests,

        market,

        trends,

        me: npcs[0],

        generatedAt: new Date()

    };

}


/* =========================================================
   PROFILE
========================================================= */

function renderProfile(npc = WORLD.me) {

    document.getElementById("profileCard").innerHTML = `

        <div class="card">

            <div class="profile-cover"></div>

            <div class="profile-main">

                <div class="avatar">
                    ${npc.avatar}
                </div>

                <div class="profile-name">
                    ${escapeHTML(npc.name)}
                </div>

                <div class="profile-handle">
                    ${escapeHTML(npc.handle)}
                    ·
                    ${npc.online ? "🟢 Online" : "⚪ Offline"}
                </div>

                <div class="profile-bio">
                    ${escapeHTML(npc.bio)}
                </div>

                <div class="profile-bio">
                    📍 ${escapeHTML(npc.location)}
                    ·
                    💼 ${escapeHTML(npc.job)}
                    ·
                    ⭐ Level ${npc.level}
                </div>

                <div class="profile-stats">

                    <div class="stat">
                        <strong>${npc.posts}</strong>
                        <span>Posts</span>
                    </div>

                    <div class="stat">
                        <strong>${npc.followers}</strong>
                        <span>Followers</span>
                    </div>

                    <div class="stat">
                        <strong>${npc.following}</strong>
                        <span>Following</span>
                    </div>

                </div>

            </div>

        </div>

    `;

    document.getElementById("composerAvatar").textContent =
        npc.avatar;
}


/* =========================================================
   FEED
========================================================= */

function renderFeed(posts = WORLD.posts) {

    const feed =
        document.getElementById("feed");

    if (!posts.length) {

        feed.innerHTML = `
            <div class="card empty">
                No NPC posts found.
            </div>
        `;

        return;
    }

    feed.innerHTML =
        posts.map(post => {

            const npc =
                WORLD.npcs.find(
                    n => n.id === post.npcId
                );

            if (!npc) return "";

            return `

                <article class="card post">

                    <div class="post-head">

                        <div class="post-avatar">
                            ${npc.avatar}
                        </div>

                        <div class="post-author">

                            <div class="post-name">
                                ${escapeHTML(npc.name)}
                            </div>

                            <div class="post-meta">
                                ${escapeHTML(npc.handle)}
                                ·
                                ${post.minutesAgo < 60
                                    ? post.minutesAgo + "m"
                                    : Math.floor(post.minutesAgo / 60) + "h"}
                                ago
                                ·
                                ${escapeHTML(npc.location)}
                            </div>

                        </div>

                    </div>

                    <div class="post-text">
                        ${escapeHTML(post.text)}
                    </div>

                    <div class="post-tag">
                        ${escapeHTML(post.tag)}
                    </div>

                    <div class="post-stats">

                        <span>
                            👍 ${post.likes.toLocaleString()}
                        </span>

                        <span>
                            💬 ${post.comments.length}
                            ·
                            🔁 ${post.shares}
                        </span>

                    </div>

                    <div class="post-actions">

                        <button
                            class="${post.liked ? "liked" : ""}"
                            onclick="likePost('${post.id}')"
                        >
                            ${post.liked ? "👍 Liked" : "👍 Like"}
                        </button>

                        <button
                            onclick="commentPost('${post.id}')"
                        >
                            💬 Comment
                        </button>

                        <button
                            onclick="sharePost('${post.id}')"
                        >
                            🔁 Share
                        </button>

                    </div>

                    <div
                        class="comment-box"
                        id="comment-${post.id}"
                    >

                        <input
                            id="input-${post.id}"
                            type="text"
                            placeholder="Write an NPC comment..."
                            maxlength="180"
                            onkeydown="
                                if(event.key==='Enter')
                                    submitComment('${post.id}')
                            "
                        >

                        <button
                            onclick="submitComment('${post.id}')"
                        >
                            Send
                        </button>

                    </div>

                    ${
                        post.comments.length
                        ?
                        `
                        <div
                            style="
                                margin-top:10px;
                                padding-top:8px;
                                border-top:1px solid #edf0f3;
                            "
                        >
                            ${
                                post.comments
                                    .slice(-3)
                                    .map(c => `
                                        <div
                                            style="
                                                font-size:13px;
                                                margin-top:6px;
                                            "
                                        >
                                            <strong>
                                                ${escapeHTML(c.author)}
                                            </strong>
                                            ${escapeHTML(c.text)}
                                        </div>
                                    `)
                                    .join("")
                            }
                        </div>
                        `
                        :
                        ""
                    }

                </article>

            `;

        }).join("");

}


/* =========================================================
   RIGHT SIDEBAR
========================================================= */

function renderSidebar() {

    document.getElementById("trends").innerHTML =
        WORLD.trends.map(t => `

            <div class="trend">

                <div class="trend-small">
                    NPCBook Trending
                </div>

                <div class="trend-name">
                    ${escapeHTML(t.title)}
                </div>

                <div class="trend-small">
                    ${t.posts.toLocaleString()} posts
                </div>

            </div>

        `).join("");


    document.getElementById("quests").innerHTML =
        WORLD.quests.map(q => `

            <div class="quest">

                <div class="quest-title">
                    ⚔️ ${escapeHTML(q.title)}
                </div>

                <div class="quest-progress">
                    <span style="width:${q.progress}%"></span>
                </div>

                <div
                    class="trend-small"
                    style="margin-top:4px"
                >
                    ${q.progress}% complete
                </div>

            </div>

        `).join("");


    document.getElementById("market").innerHTML =
        WORLD.market.map(item => `

            <div class="market-item">

                <div class="market-name">
                    ${escapeHTML(item.name)}
                </div>

                <div class="market-price">
                    🪙 ${item.price} gold
                </div>

            </div>

        `).join("");

}


/* =========================================================
   RENDER
========================================================= */

function render() {

    renderProfile();

    renderFeed();

    renderSidebar();

}


/* =========================================================
   HOME
   IMPORTANT:
   FULL PAGE REFRESH
========================================================= */

function goHome() {

    /*
        This intentionally reloads the entire static page.

        Because WORLD is generated in JavaScript
        when the page loads, a reload creates:

        - New NPCs
        - New posts
        - New quests
        - New trends
        - New marketplace
        - New stats
    */

    window.location.reload();

}


/* =========================================================
   NEW WORLD
========================================================= */

function newWorld() {

    generateWorld();

    render();

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

    toast(
        "🎲 A completely new NPC world has appeared!"
    );

}


/* =========================================================
   NEW NPC
========================================================= */

function newNPC() {

    const npc =
        createNPC();

    WORLD.npcs.unshift(npc);

    WORLD.me = npc;

    for (let i = 0; i < 2; i++) {

        WORLD.posts.unshift(
            createPost(npc)
        );

    }

    render();

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

    toast(
        `👤 ${npc.name} has entered NPCBook!`
    );

}


/* =========================================================
   RANDOM POST
========================================================= */

function randomPost() {

    const npc =
        pick(WORLD.npcs);

    const post =
        createPost(npc);

    WORLD.posts.unshift(post);

    renderFeed(WORLD.posts);

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

    toast(
        "✨ A random NPC posted something!"
    );

}


/* =========================================================
   LIKE
========================================================= */

function likePost(id) {

    const post =
        WORLD.posts.find(
            p => p.id === id
        );

    if (!post) return;

    if (post.liked) {

        post.likes =
            Math.max(0, post.likes - 1);

        post.liked = false;

    } else {

        post.likes++;

        post.liked = true;

    }

    renderFeed(filteredPosts());

}


/* =========================================================
   COMMENT
========================================================= */

function commentPost(id) {

    const box =
        document.getElementById(
            `comment-${id}`
        );

    if (!box) return;

    box.classList.toggle("active");

    if (box.classList.contains("active")) {

        const input =
            document.getElementById(
                `input-${id}`
            );

        setTimeout(() => {

            if (input) {
                input.focus();
            }

        }, 50);

    }

}


/* =========================================================
   SUBMIT COMMENT
========================================================= */

function submitComment(id) {

    const input =
        document.getElementById(
            `input-${id}`
        );

    if (!input) return;

    const text =
        input.value.trim();

    if (!text) {

        toast(
            "Write something first."
        );

        return;
    }

    const post =
        WORLD.posts.find(
            p => p.id === id
        );

    if (!post) return;

    post.comments.push({

        author:
            WORLD.me.name,

        text:
            text

    });

    input.value = "";

    renderFeed(
        filteredPosts()
    );

    toast(
        "💬 NPC comment posted!"
    );

}


/* =========================================================
   SHARE
========================================================= */

function sharePost(id) {

    const post =
        WORLD.posts.find(
            p => p.id === id
        );

    if (!post) return;

    post.shares++;

    renderFeed(
        filteredPosts()
    );

    toast(
        "🔁 NPC post shared!"
    );

}


/* =========================================================
   SEARCH
========================================================= */

function filteredPosts() {

    const input =
        document.getElementById(
            "searchInput"
        );

    if (!input) {
        return WORLD.posts;
    }

    const query =
        input.value
            .trim()
            .toLowerCase();

    if (!query) {
        return WORLD.posts;
    }

    return WORLD.posts.filter(post => {

        const npc =
            WORLD.npcs.find(
                n => n.id === post.npcId
            );

        if (!npc) return false;

        return (

            post.text.toLowerCase()
                .includes(query)

            ||

            post.tag.toLowerCase()
                .includes(query)

            ||

            npc.name.toLowerCase()
                .includes(query)

            ||

            npc.handle.toLowerCase()
                .includes(query)

            ||

            npc.job.toLowerCase()
                .includes(query)

            ||

            npc.location.toLowerCase()
                .includes(query)

        );

    });

}


document
    .getElementById("searchInput")
    .addEventListener(
        "input",
        () => {

            renderFeed(
                filteredPosts()
            );

        }
    );


/* =========================================================
   NOTIFICATIONS
========================================================= */

function showNotifications() {

    toast(
        "🔔 You have 17 completely unnecessary NPC notifications."
    );

}


/* =========================================================
   MESSAGES
========================================================= */

function showMessages() {

    toast(
        "💬 Message from Steve: 'Hello.'"
    );

}


/* =========================================================
   PROFILE
========================================================= */

function showProfile() {

    renderProfile(
        WORLD.me
    );

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

    toast(
        "👤 Viewing your NPC profile."
    );

}


/* =========================================================
   TRENDING
========================================================= */

function showTrending() {

    const posts =
        [...WORLD.posts]
            .sort(
                (a, b) =>
                    b.likes - a.likes
            );

    renderFeed(posts);

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

    toast(
        "🔥 Showing the most popular NPC posts."
    );

}


/* =========================================================
   QUESTS
========================================================= */

function showQuests() {

    const content =
        WORLD.quests
            .map(q => `
                <div class="card">
                    <div class="card-body">

                        <div class="section-title">
                            ⚔️ ${escapeHTML(q.title)}
                        </div>

                        <p
                            style="
                                margin-top:8px;
                                color:#697386;
                            "
                        >
                            Progress: ${q.progress}%
                        </p>

                        <div
                            class="quest-progress"
                            style="margin-top:10px"
                        >
                            <span
                                style="width:${q.progress}%"
                            ></span>
                        </div>

                        <button
                            style="
                                margin-top:12px;
                                border:0;
                                background:#1877f2;
                                color:#fff;
                                padding:10px 15px;
                                border-radius:8px;
                                font-weight:700;
                                cursor:pointer;
                            "
                            onclick="toast('⚔️ Quest accepted!')"
                        >
                            Accept Quest
                        </button>

                    </div>
                </div>
            `)
            .join("");

    document.getElementById(
        "feed"
    ).innerHTML = content;

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}


/* =========================================================
   MARKET
========================================================= */

function showMarket() {

    const content =
        WORLD.market
            .map(item => `

                <div class="card">

                    <div class="card-body">

                        <div
                            style="
                                font-size:32px;
                            "
                        >
                            🛒
                        </div>

                        <div
                            class="section-title"
                            style="margin-top:8px"
                        >
                            ${escapeHTML(item.name)}
                        </div>

                        <div
                            style="
                                margin-top:5px;
                                color:#16803c;
                                font-weight:800;
                            "
                        >
                            🪙 ${item.price} gold
                        </div>

                        <button
                            style="
                                margin-top:12px;
                                border:0;
                                background:#16803c;
                                color:white;
                                padding:10px 15px;
                                border-radius:8px;
                                font-weight:700;
                                cursor:pointer;
                            "
                            onclick="toast('🛒 Purchase failed: NPC economy unavailable.')"
                        >
                            Buy
                        </button>

                    </div>

                </div>

            `)
            .join("");

    document.getElementById(
        "feed"
    ).innerHTML = content;

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}


/* =========================================================
   SETTINGS
========================================================= */

function showSettings() {

    document.getElementById(
        "feed"
    ).innerHTML = `

        <div class="card">

            <div class="card-body">

                <div class="section-title">
                    ⚙️ NPCBook Settings
                </div>

                <div
                    style="
                        margin-top:15px;
                        line-height:1.8;
                        color:#4b5563;
                    "
                >

                    <p>
                        🌐 Site Type:
                        Static
                    </p>

                    <p>
                        💾 Database:
                        None
                    </p>

                    <p>
                        📦 LocalStorage:
                        None
                    </p>

                    <p>
                        🗃️ SessionStorage:
                        None
                    </p>

                    <p>
                        🍪 App Data Cookies:
                        None
                    </p>

                    <p>
                        🎲 World Generation:
                        Random
                    </p>

                    <p>
                        🔄 Refresh:
                        New NPC World
                    </p>

                </div>

                <button
                    style="
                        margin-top:15px;
                        border:0;
                        background:#1877f2;
                        color:white;
                        padding:12px 18px;
                        border-radius:8px;
                        font-weight:800;
                        cursor:pointer;
                    "
                    onclick="goHome()"
                >
                    🔄 Reset / Refresh NPCBook
                </button>

            </div>

        </div>

    `;

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}


/* =========================================================
   TOAST
========================================================= */

let toastTimer = null;

function toast(message) {

    const el =
        document.getElementById(
            "toast"
        );

    el.textContent =
        message;

    el.classList.add("show");

    clearTimeout(
        toastTimer
    );

    toastTimer =
        setTimeout(
            () => {

                el.classList.remove(
                    "show"
                );

            },
            2200
        );

}


/* =========================================================
   INITIAL WORLD
========================================================= */

generateWorld();

render();

</script>

</body>
</html>
'''

output = Path("index.html")
output.write_text(HTML, encoding="utf-8")

print("NPCBook static site generated successfully.")
print("Created:", output.resolve())
