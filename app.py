from pathlib import Path

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#4267B2">
<title>NPCBook — Social Media for NPCs</title>

<style>
:root{
    --bg:#eef1f5;
    --card:#ffffff;
    --text:#172033;
    --muted:#687386;
    --line:#dce2ea;
    --blue:#4267b2;
    --blue-dark:#365899;
    --soft:#f4f6f9;
    --green:#20a464;
    --red:#e53958;
    --shadow:0 2px 12px rgba(0,0,0,.07);
}

*{
    box-sizing:border-box;
}

html{
    scroll-behavior:smooth;
}

body{
    margin:0;
    background:var(--bg);
    color:var(--text);
    font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
}

button,
input{
    font:inherit;
}

button{
    cursor:pointer;
    -webkit-tap-highlight-color:transparent;
}

.topbar{
    position:sticky;
    top:0;
    z-index:100;
    background:white;
    border-bottom:1px solid var(--line);
    padding:
        9px
        max(10px,env(safe-area-inset-right))
        9px
        max(10px,env(safe-area-inset-left));
}

.topbar-inner{
    max-width:1200px;
    margin:auto;
    display:flex;
    align-items:center;
    gap:10px;
}

.logo{
    color:var(--blue);
    font-size:24px;
    font-weight:950;
    letter-spacing:-1px;
    white-space:nowrap;
}

.search{
    flex:1;
    max-width:430px;
}

.search input{
    width:100%;
    border:0;
    outline:none;
    background:var(--soft);
    border-radius:999px;
    padding:11px 16px;
}

.nav{
    margin-left:auto;
    display:flex;
    gap:6px;
}

.nav button{
    min-height:42px;
    border:1px solid var(--line);
    background:white;
    border-radius:10px;
    padding:8px 12px;
    font-weight:800;
}

.nav button:hover{
    background:var(--soft);
}

.layout{
    width:min(1200px,100%);
    margin:18px auto;
    padding:0 14px;
    display:grid;
    grid-template-columns:220px minmax(0,1fr) 260px;
    gap:18px;
}

.sidebar,
.rightbar{
    display:flex;
    flex-direction:column;
    gap:14px;
}

.card,
.post,
.composer,
.profile{
    background:var(--card);
    border:1px solid var(--line);
    border-radius:14px;
    box-shadow:var(--shadow);
}

.side-card{
    padding:12px;
}

.side-item{
    padding:11px;
    border-radius:10px;
    font-weight:800;
    cursor:pointer;
}

.side-item:hover{
    background:var(--soft);
}

.main{
    min-width:0;
}

.hero{
    padding:20px;
    margin-bottom:14px;
    color:white;
    background:linear-gradient(135deg,#4267b2,#7187cb);
}

.hero h1{
    margin:0 0 5px;
    font-size:29px;
}

.hero p{
    margin:0;
    opacity:.93;
}

.profile{
    overflow:hidden;
    margin-bottom:14px;
}

.cover{
    height:105px;
    background:linear-gradient(135deg,#253c72,#8ca2dc);
}

.profile-body{
    padding:0 16px 16px;
}

.avatar{
    width:46px;
    height:46px;
    border-radius:50%;
    display:grid;
    place-items:center;
    color:white;
    font-weight:950;
    flex:0 0 auto;
    box-shadow:0 2px 6px rgba(0,0,0,.18);
}

.avatar.large{
    width:76px;
    height:76px;
    font-size:27px;
    margin-top:-38px;
    border:4px solid white;
}

.profile h2{
    margin:7px 0 2px;
}

.small{
    color:var(--muted);
    font-size:12px;
}

.badge{
    display:inline-block;
    margin-top:7px;
    padding:5px 9px;
    border-radius:999px;
    background:#fff2c8;
    color:#745700;
    font-size:11px;
    font-weight:900;
}

.stat-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:7px;
    margin-top:12px;
}

.stat{
    padding:9px;
    background:var(--soft);
    border-radius:9px;
    text-align:center;
}

.stat b{
    display:block;
    font-size:17px;
}

.stat span{
    color:var(--muted);
    font-size:10px;
}

.composer{
    padding:14px;
    margin-bottom:14px;
}

.compose-row{
    display:flex;
    align-items:center;
    gap:10px;
}

.fake-input{
    flex:1;
    border:0;
    background:var(--soft);
    border-radius:999px;
    padding:12px 16px;
    color:var(--muted);
    text-align:left;
}

.compose-actions{
    display:flex;
    gap:7px;
    margin-top:10px;
}

.compose-actions button{
    flex:1;
    border:1px solid var(--line);
    background:white;
    border-radius:9px;
    padding:9px;
    font-weight:800;
}

.post{
    padding:15px;
    margin-bottom:13px;
}

.post-header{
    display:flex;
    align-items:center;
    gap:10px;
}

.post-name{
    font-weight:900;
}

.post-body{
    padding:14px 0 10px;
    line-height:1.55;
    font-size:16px;
}

.tags{
    display:flex;
    gap:5px;
    flex-wrap:wrap;
}

.tag{
    background:#eef2ff;
    color:#40579b;
    padding:4px 8px;
    border-radius:999px;
    font-size:10px;
    font-weight:900;
}

.post-stats{
    display:flex;
    justify-content:space-between;
    border-bottom:1px solid var(--line);
    padding:8px 0;
    color:var(--muted);
    font-size:13px;
}

.post-actions{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:5px;
    padding-top:7px;
}

.post-actions button{
    border:0;
    background:transparent;
    padding:10px;
    border-radius:8px;
    font-weight:850;
    color:#536071;
}

.post-actions button:hover{
    background:var(--soft);
}

.post-actions .liked{
    color:var(--blue);
}

.right-card{
    padding:14px;
}

.right-card h3{
    margin:0 0 10px;
    font-size:15px;
}

.trend,
.quest,
.market-item{
    padding:9px 0;
    border-bottom:1px solid var(--line);
}

.trend:last-child,
.quest:last-child,
.market-item:last-child{
    border-bottom:0;
}

.trend b,
.market-item b{
    display:block;
}

.quest{
    background:var(--soft);
    padding:10px;
    border-radius:9px;
    margin-bottom:7px;
    border:0;
}

.toast{
    position:fixed;
    z-index:500;
    left:50%;
    bottom:max(20px,env(safe-area-inset-bottom));
    transform:translate(-50%,20px);
    background:#111827;
    color:white;
    padding:12px 17px;
    border-radius:999px;
    opacity:0;
    pointer-events:none;
    transition:.25s;
    max-width:90vw;
    text-align:center;
    box-shadow:0 8px 30px rgba(0,0,0,.3);
}

.toast.show{
    opacity:1;
    transform:translate(-50%,0);
}

.mobile-nav{
    display:none;
}

.empty{
    padding:35px;
    text-align:center;
    color:var(--muted);
}

@media(max-width:1000px){
    .layout{
        grid-template-columns:190px minmax(0,1fr);
    }

    .rightbar{
        display:none;
    }
}

@media(max-width:700px){
    .topbar-inner{
        flex-wrap:wrap;
    }

    .logo{
        font-size:21px;
    }

    .search{
        order:3;
        flex-basis:100%;
        max-width:none;
    }

    .nav{
        gap:3px;
    }

    .nav button{
        min-width:42px;
        padding:8px;
    }

    .nav .text{
        display:none;
    }

    .layout{
        display:block;
        margin:10px auto;
        padding:0 8px 78px;
    }

    .sidebar{
        display:none;
    }

    .hero{
        padding:16px;
        border-radius:12px;
    }

    .hero h1{
        font-size:23px;
    }

    .post,
    .composer,
    .profile{
        border-radius:11px;
    }

    .post{
        padding:12px;
    }

    .stat-grid{
        grid-template-columns:repeat(2,1fr);
    }

    .mobile-nav{
        position:fixed;
        display:flex;
        left:0;
        right:0;
        bottom:0;
        z-index:200;
        background:white;
        border-top:1px solid var(--line);
        padding:
            6px
            max(6px,env(safe-area-inset-right))
            max(6px,env(safe-area-inset-bottom))
            max(6px,env(safe-area-inset-left));
        justify-content:space-around;
    }

    .mobile-nav button{
        border:0;
        background:transparent;
        border-radius:9px;
        padding:7px 11px;
        font-weight:850;
        color:#566276;
    }

    .mobile-nav button:active{
        background:var(--soft);
    }
}

@media(hover:none) and (pointer:coarse){
    button,
    .fake-input,
    .side-item{
        min-height:44px;
    }
}
</style>
</head>

<body>

<header class="topbar">
    <div class="topbar-inner">

        <div class="logo">📱 NPCBook</div>

        <div class="search">
            <input
                id="search"
                type="search"
                placeholder="Search NPCs, jobs, quests..."
                autocomplete="off">
        </div>

        <nav class="nav">
            <button onclick="newWorld()" title="Generate a completely new world">
                🔄 <span class="text">New World</span>
            </button>

            <button onclick="showMessage()">
                💬 <span class="text">Messages</span>
            </button>

            <button onclick="showNotifications()">
                🔔
            </button>
        </nav>

    </div>
</header>


<div class="layout">

    <aside class="sidebar">

        <div class="card side-card">

            <div class="side-item">🏠 Home</div>

            <div class="side-item" onclick="newNPC()">
                🤖 Generate NPC
            </div>

            <div class="side-item" onclick="showTrending()">
                🔥 Trending
            </div>

            <div class="side-item" onclick="showQuests()">
                🎯 Quests
            </div>

            <div class="side-item" onclick="showMarket()">
                🛒 Marketplace
            </div>

            <div class="side-item" onclick="showSettings()">
                ⚙️ Settings
            </div>

        </div>

        <div class="card side-card">
            <b>NPCBook Rule</b>
            <p class="small">
                Nothing is saved. Refreshing this page creates
                another temporary NPC universe.
            </p>
        </div>

    </aside>


    <main class="main">

        <section class="hero card">

            <h1>Social Media for NPCs</h1>

            <p>
                A social network where nobody is the main character.
            </p>

        </section>


        <section id="profile"></section>


        <section class="composer">

            <div class="compose-row">

                <div id="miniAvatar" class="avatar">
                    NPC
                </div>

                <button
                    class="fake-input"
                    onclick="randomPost()">
                    What is your NPC thinking?
                </button>

            </div>

            <div class="compose-actions">

                <button onclick="randomPost()">
                    📝 NPC Post
                </button>

                <button onclick="newNPC()">
                    🤖 New NPC
                </button>

                <button onclick="newWorld()">
                    🎲 New World
                </button>

            </div>

        </section>


        <section id="feed"></section>

    </main>


    <aside class="rightbar">

        <section class="card right-card">

            <h3>🔥 NPC Trending</h3>

            <div id="trends"></div>

        </section>


        <section class="card right-card">

            <h3>🎯 Active Quests</h3>

            <div id="quests"></div>

        </section>


        <section class="card right-card">

            <h3>🛒 NPC Marketplace</h3>

            <div id="market"></div>

        </section>

    </aside>

</div>


<div id="toast" class="toast"></div>


<nav class="mobile-nav">

    <button onclick="goTop()">
        🏠<br><small>Home</small>
    </button>

    <button onclick="newNPC()">
        🤖<br><small>NPC</small>
    </button>

    <button onclick="newWorld()">
        🎲<br><small>New</small>
    </button>

    <button onclick="showQuests()">
        🎯<br><small>Quests</small>
    </button>

    <button onclick="showMarket()">
        🛒<br><small>Shop</small>
    </button>

</nav>


<script>

/*
===========================================================
NPCBOOK
===========================================================

NO DATABASE
NO LOCALSTORAGE
NO SESSIONSTORAGE
NO COOKIES
NO API
NO BACKEND

Everything exists only in JavaScript memory.

Every page load creates a completely new NPC world.
Every refresh creates another new NPC world.
===========================================================
*/


const DATA = {

    names:[
        "Rajesh Kumar",
        "Sunita Devi",
        "Vikas Sharma",
        "Priya Singh",
        "Ramesh Gupta",
        "Amit Verma",
        "Neha Kumari",
        "Suresh Yadav",
        "Pooja Mehta",
        "Manoj",
        "Kavita",
        "Deepak",
        "Anita",
        "Vijay",
        "Rekha",
        "Mohan",
        "Seema",
        "Rohit",
        "Geeta",
        "Ashok",
        "Nisha",
        "Rakesh",
        "Meena",
        "Sanjay",
        "Mahesh",
        "Komal",
        "Ravi",
        "Anil",
        "Sunil",
        "Pankaj"
    ],

    jobs:[
        "Professional Bench Sitter",
        "Tea Observer",
        "Gate Guard",
        "Suspicious Neighbour",
        "Village Gossip Analyst",
        "Roadside Philosopher",
        "Part-Time Walker",
        "Queue Specialist",
        "Weather Commentator",
        "Lost Key Researcher",
        "Shop Counter Guardian",
        "Pigeon Supervisor",
        "Parking Space Defender",
        "Bus Stop Resident",
        "Street Corner Manager",
        "Unofficial Area Expert",
        "Doorway Specialist",
        "Local Rumour Consultant",
        "Electric Pole Inspector",
        "Professional Looking Busy",
        "Chair Reservation Specialist",
        "Road Crossing Advisor",
        "Tea Stall Strategist",
        "Neighbourhood Watcher",
        "Government Office Chair Tester"
    ],

    places:[
        "near the tea stall",
        "beside the gate",
        "outside the shop",
        "at the bus stop",
        "behind the building",
        "near the same bench",
        "on the corner",
        "next to the parked scooter",
        "outside the pharmacy",
        "under the tree",
        "near the water tank",
        "beside the closed door",
        "near the electric pole",
        "outside the office",
        "beside the staircase"
    ],

    moods:[
        "😐 Neutral",
        "🙂 Mildly Happy",
        "🤨 Suspicious",
        "😴 Sleepy",
        "😤 Slightly Annoyed",
        "🤔 Confused",
        "😎 Unnecessarily Confident",
        "😶 Socially Available",
        "👀 Watching",
        "🫠 Existing"
    ],

    activities:[
        "standing quietly",
        "drinking tea",
        "looking at the road",
        "checking the same phone notification",
        "walking in a small circle",
        "watching someone else work",
        "waiting for absolutely nothing",
        "moving three metres and returning",
        "looking for a key",
        "discussing the weather",
        "guarding a door",
        "sitting on the usual bench",
        "looking behind them",
        "checking whether the shop is open",
        "waiting for someone who never arrives"
    ],

    dialogue:[
        "Hmm... maybe.",
        "Nothing unusual today.",
        "Have you been here before?",
        "I know a shortcut.",
        "The shopkeeper knows.",
        "Wait here.",
        "It is a nice day.",
        "I was just coming.",
        "I have seen this before.",
        "What brings you here?",
        "You should ask someone else.",
        "Everything is normal.",
        "I must get back to my post.",
        "No, I haven't seen it.",
        "Maybe tomorrow.",
        "I don't know.",
        "That happens sometimes.",
        "You came at the right time.",
        "I was told to stand here."
    ],

    thoughts:[
        "I should probably go home.",
        "Why is everyone walking so fast?",
        "The tea could be warmer.",
        "I have been standing here for a long time.",
        "Someone moved my chair.",
        "I think I forgot something.",
        "Tomorrow I will do something different.",
        "This is exactly where I was yesterday.",
        "Nobody has explained the quest.",
        "I should buy a bucket.",
        "I wonder where everyone is going.",
        "Something feels suspicious.",
        "I need to sit down.",
        "I have seen that person before."
    ],

    things:[
        "a bucket",
        "the missing key",
        "tea",
        "that strange noise",
        "the blue scooter",
        "the locked door",
        "a sandwich",
        "the suspicious pigeon",
        "the old bench",
        "the weather",
        "a plastic chair",
        "a mysterious box"
    ],

    questThings:[
        "the missing bucket",
        "a mysterious key",
        "the suspicious pigeon",
        "the old bench",
        "a red umbrella",
        "three identical boxes",
        "the tea stall",
        "a locked door",
        "a lost sandal",
        "the blue scooter",
        "the invisible package",
        "the important chair"
    ],

    questVerbs:[
        "Find",
        "Deliver",
        "Inspect",
        "Guard",
        "Return",
        "Locate",
        "Question",
        "Follow",
        "Count",
        "Protect",
        "Observe",
        "Recover"
    ],

    items:[
        "Slightly Used Stick",
        "Mysterious Rock",
        "Old Bread",
        "Key That Opens Nothing",
        "Bent Spoon",
        "Unidentified Button",
        "Almost New Rope",
        "Suspicious Bucket",
        "One Left Shoe",
        "Chair With History",
        "Empty Box",
        "Rare Looking Leaf",
        "Plastic Bottle of Unknown Origin",
        "Extremely Ordinary Stone",
        "Broken Umbrella"
    ],

    tags:[
        "#NPCLife",
        "#SideQuest",
        "#NothingHappened",
        "#DailyRoutine",
        "#BackgroundCharacter",
        "#ImportantUpdate",
        "#QuestProblems",
        "#NPCDrama"
    ],

    trends:[
        "#Tea",
        "#GateLife",
        "#MissingBucket",
        "#Weather",
        "#SameBench",
        "#SuspiciousPigeon",
        "#NothingHappened",
        "#QuestProblems",
        "#ChairPolitics",
        "#StandingAround"
    ]

};


let WORLD = {

    npcs:[],
    posts:[],
    quests:[],
    market:[],
    trends:[],
    profile:null

};


/* RANDOM HELPERS */

function pick(array){

    return array[
        Math.floor(
            Math.random()*array.length
        )
    ];

}


function number(min,max){

    return Math.floor(
        Math.random()*(max-min+1)
    )+min;

}


function initials(name){

    return name
        .split(/\s+/)
        .map(x=>x[0])
        .slice(0,2)
        .join("");

}


function avatarColor(index){

    return "hsl("+
        ((index*47)%360)+
        " 55% 48%)";

}


/* NPC GENERATOR */

function createNPC(index){

    const name=pick(DATA.names);

    const npc={

        id:crypto.randomUUID
            ?crypto.randomUUID()
            :String(Date.now())+Math.random(),

        name:name,

        job:pick(DATA.jobs),

        place:pick(DATA.places),

        mood:pick(DATA.moods),

        activity:pick(DATA.activities),

        dialogue:pick(DATA.dialogue),

        thought:pick(DATA.thoughts),

        quest:pick(DATA.questThings),

        age:number(18,79),

        level:number(1,99),

        hp:number(35,100),

        energy:number(20,100),

        intelligence:number(8,95),

        dialogueVariety:number(3,48),

        repeat:number(61,99),

        friends:number(0,18),

        followers:number(0,9999),

        avatar:avatarColor(index)

    };

    return npc;

}


/* POST GENERATOR */

function createPost(npc){

    const templates=[

        `Today I ${npc.activity}. Very productive.`,

        `Someone asked me about ${pick(DATA.things)}. I said: "${npc.dialogue}"`,

        `I have been ${npc.activity} ${npc.place}. Nobody has questioned it.`,

        `Important update: ${npc.thought}`,

        `I saw ${pick(DATA.names)} again. We did not speak. A successful interaction.`,

        `My current professional responsibility is ${npc.job}.`,

        `BREAKING: Nothing happened ${npc.place}. More updates when nothing continues.`,

        `I have a quest: ${npc.quest}. Please do not make it complicated.`,

        `Just thinking about ${pick(DATA.things)}.`,

        `Daily report: ${npc.dialogue}`,

        `I moved from one place to another today. Nobody knows why.`,

        `I have officially been ${npc.activity} for several hours.`

    ];

    return{

        id:crypto.randomUUID
            ?crypto.randomUUID()
            :String(Date.now())+Math.random(),

        npc:npc,

        text:pick(templates),

        time:number(1,59)+"m",

        likes:number(0,999),

        comments:number(0,90),

        shares:number(0,70),

        tag:pick(DATA.tags),

        liked:false

    };

}


/* GENERATE COMPLETE WORLD */

function generateWorld(){

    const count=number(16,24);

    WORLD.npcs=[];

    WORLD.posts=[];

    for(let i=0;i<count;i++){

        const npc=createNPC(i);

        WORLD.npcs.push(npc);

        WORLD.posts.push(
            createPost(npc)
        );

    }


    WORLD.profile=
        pick(WORLD.npcs);


    WORLD.quests=[];

    for(let i=0;i<6;i++){

        WORLD.quests.push({

            title:
                pick(DATA.questVerbs)+
                " "+
                pick(DATA.questThings),

            progress:number(0,99),

            reward:number(5,999)

        });

    }


    WORLD.market=[];

    for(let i=0;i<6;i++){

        WORLD.market.push({

            item:pick(DATA.items),

            price:number(3,4999),

            stock:number(1,15)

        });

    }


    WORLD.trends=[];

    for(let i=0;i<7;i++){

        WORLD.trends.push({

            tag:pick(DATA.trends),

            posts:number(5,99999)

        });

    }

}


/* PROFILE */

function renderProfile(npc){

    document.getElementById("profile").innerHTML=`

        <section class="profile">

            <div class="cover"></div>

            <div class="profile-body">

                <div
                    class="avatar large"
                    style="background:${npc.avatar}">
                    ${escapeHTML(initials(npc.name))}
                </div>

                <h2>
                    ${escapeHTML(npc.name)}
                </h2>

                <div class="small">
                    ${escapeHTML(npc.job)}
                    ·
                    ${escapeHTML(npc.place)}
                    ·
                    Level ${npc.level}
                </div>

                <span class="badge">
                    ${escapeHTML(npc.mood)}
                    ·
                    NPC Energy ${npc.repeat}%
                </span>

                <div class="stat-grid">

                    <div class="stat">
                        <b>${npc.followers}</b>
                        <span>Followers</span>
                    </div>

                    <div class="stat">
                        <b>${npc.friends}</b>
                        <span>Friends</span>
                    </div>

                    <div class="stat">
                        <b>${npc.dialogueVariety}%</b>
                        <span>Dialogue Variety</span>
                    </div>

                    <div class="stat">
                        <b>${npc.repeat}%</b>
                        <span>Repetition</span>
                    </div>

                </div>

            </div>

        </section>

    `;


    const mini=document.getElementById("miniAvatar");

    mini.style.background=npc.avatar;

    mini.textContent=initials(npc.name);

}


/* HTML ESCAPE */

function escapeHTML(value){

    return String(value)
        .replaceAll("&","&amp;")
        .replaceAll("<","&lt;")
        .replaceAll(">","&gt;")
        .replaceAll('"',"&quot;")
        .replaceAll("'","&#039;");

}


/* FEED */

function renderFeed(posts=WORLD.posts){

    const feed=document.getElementById("feed");

    if(!posts.length){

        feed.innerHTML=`

            <div class="card empty">

                No NPC found.

                <br>

                They may be standing somewhere else.

            </div>

        `;

        return;

    }


    feed.innerHTML=posts.map(post=>`

        <article class="post">

            <div class="post-header">

                <div
                    class="avatar"
                    style="background:${post.npc.avatar}">
                    ${escapeHTML(
                        initials(post.npc.name)
                    )}
                </div>

                <div>

                    <div class="post-name">
                        ${escapeHTML(post.npc.name)}
                    </div>

                    <div class="small">
                        ${escapeHTML(post.npc.job)}
                        ·
                        ${post.time} ago
                    </div>

                </div>

            </div>


            <div class="post-body">

                ${escapeHTML(post.text)}

            </div>


            <div class="tags">

                <span class="tag">
                    ${escapeHTML(post.tag)}
                </span>

                <span class="tag">
                    ${escapeHTML(post.npc.mood)}
                </span>

            </div>


            <div class="post-stats">

                <span>
                    👍 ${post.likes}
                </span>

                <span>
                    💬 ${post.comments}
                    ·
                    ↗ ${post.shares}
                </span>

            </div>


            <div class="post-actions">

                <button
                    class="${post.liked?"liked":""}"
                    onclick="likePost('${post.id}')">

                    ${post.liked?"👍 Liked":"👍 Like"}

                </button>


                <button
                    onclick="commentPost('${post.id}')">

                    💬 Comment

                </button>


                <button
                    onclick="sharePost('${post.id}')">

                    ↗ Share

                </button>

            </div>

        </article>

    `).join("");

}


/* SIDEBAR */

function renderSidebar(){

    document.getElementById("trends").innerHTML=

        WORLD.trends.map(item=>`

            <div class="trend">

                <b>
                    ${escapeHTML(item.tag)}
                </b>

                <span class="small">
                    ${item.posts.toLocaleString()}
                    NPC posts
                </span>

            </div>

        `).join("");


    document.getElementById("quests").innerHTML=

        WORLD.quests.map(item=>`

            <div class="quest">

                <b>
                    🎯
                    ${escapeHTML(item.title)}
                </b>

                <div class="small">

                    ${item.progress}%
                    complete

                    ·

                    Reward ${item.reward} XP

                </div>

            </div>

        `).join("");


    document.getElementById("market").innerHTML=

        WORLD.market.map(item=>`

            <div class="market-item">

                <b>
                    🛒
                    ${escapeHTML(item.item)}
                </b>

                <span class="small">

                    ₹${item.price.toLocaleString()}

                    ·

                    ${item.stock} left

                </span>

            </div>

        `).join("");

}


/* FULL RENDER */

function render(){

    renderProfile(WORLD.profile);

    renderFeed();

    renderSidebar();

}


/* NEW WORLD */

function newWorld(){

    generateWorld();

    render();

    toast(
        "🌎 Completely new NPC universe generated."
    );

    goTop();

}


/* NEW NPC */

function newNPC(){

    const npc=createNPC(
        WORLD.npcs.length+
        number(1,1000)
    );

    WORLD.npcs.unshift(npc);

    WORLD.posts.unshift(
        createPost(npc)
    );

    WORLD.profile=npc;

    render();

    toast(
        "🤖 New NPC spawned."
    );

    goTop();

}


/* RANDOM POST */

function randomPost(){

    const npc=pick(WORLD.npcs);

    WORLD.posts.unshift(
        createPost(npc)
    );

    renderFeed(
        filteredPosts()
    );

    toast(
        "📝 NPC posted something extremely important."
    );

}


/* LIKE */

function likePost(id){

    const post=
        WORLD.posts.find(
            x=>x.id===id
        );

    if(!post)return;

    post.liked=!post.liked;

    post.likes+=
        post.liked?1:-1;

    renderFeed(
        filteredPosts()
    );

}


/* COMMENT */

function commentPost(id){

    const post=
        WORLD.posts.find(
            x=>x.id===id
        );

    if(!post)return;

    post.comments++;

    renderFeed(
        filteredPosts()
    );

    toast(
        '💬 NPC commented: "Hmm... maybe."'
    );

}


/* SHARE */

function sharePost(id){

    const post=
        WORLD.posts.find(
            x=>x.id===id
        );

    if(!post)return;

    post.shares++;

    renderFeed(
        filteredPosts()
    );

    toast(
        "↗ Shared with absolutely nobody."
    );

}


/* SEARCH */

function filteredPosts(){

    const query=
        document
        .getElementById("search")
        .value
        .trim()
        .toLowerCase();

    if(!query){

        return WORLD.posts;

    }


    return WORLD.posts.filter(post=>{

        const text=

            post.npc.name+
            " "+
            post.npc.job+
            " "+
            post.text+
            " "+
            post.tag+
            " "+
            post.npc.quest;

        return text
            .toLowerCase()
            .includes(query);

    });

}


document
.getElementById("search")
.addEventListener(
    "input",
    ()=>{
        renderFeed(
            filteredPosts()
        );
    }
);


/* UI */

function showMessage(){

    toast(
        "💬 No messages. NPCs are busy repeating themselves."
    );

}


function showNotifications(){

    toast(
        "🔔 3 NPCs noticed you. None know why."
    );

}


function showTrending(){

    toast(
        "🔥 Trending: "+
        pick(WORLD.trends).tag
    );

}


function showQuests(){

    const quest=pick(WORLD.quests);

    toast(
        "🎯 "+
        quest.title+
        " — "+
        quest.progress+
        "% complete"
    );

}


function showMarket(){

    const item=pick(WORLD.market);

    toast(
        "🛒 "+
        item.item+
        " — ₹"+
        item.price
    );

}


function showSettings(){

    toast(
        "⚙️ Settings are imaginary."
    );

}


function goTop(){

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });

}


let toastTimer;

function toast(message){

    const element=
        document.getElementById("toast");

    element.textContent=message;

    element.classList.add("show");

    clearTimeout(toastTimer);

    toastTimer=setTimeout(
        ()=>{
            element.classList.remove("show");
        },
        2500
    );

}


/*
===========================================================
INITIAL LOAD

This is intentionally executed every time the HTML page
loads.

NO STORAGE IS USED.

Therefore:

Refresh -> new world
Close -> reopen -> new world
New browser tab -> new world
Different device -> new world
===========================================================
*/

generateWorld();

render();

</script>

</body>
</html>
'''


# ==========================================================
# PYTHON STATIC SITE GENERATOR
# ==========================================================

output = Path("index.html")

output.write_text(
    HTML,
    encoding="utf-8"
)

print("NPCBook static site generated successfully.")
print(f"Created: {output.resolve()}")
