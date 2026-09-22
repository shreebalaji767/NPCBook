from pathlib import Path
import json
import html

# ============================================================
# NPC OMNIVERSE - STATIC SITE GENERATOR
# ============================================================

OUTPUT_DIR = Path("site")
OUTPUT_FILE = OUTPUT_DIR / "index.html"

# ============================================================
# SITE DATA
# Edit this section to change your website content.
# ============================================================

SITE_DATA = {
    "name": "NPC OMNIVERSE",
    "tagline": "Explore. Create. Discover.",
    "description": "A universe of NPCs, worlds, quests, factions and stories.",

    "stats": {
        "NPCs": 12840,
        "Worlds": 426,
        "Quests": 1892,
        "Factions": 317
    },

    "categories": [
        {
            "icon": "👤",
            "name": "NPCs",
            "description": "Discover characters from countless worlds."
        },
        {
            "icon": "🌌",
            "name": "Worlds",
            "description": "Explore civilizations, planets and dimensions."
        },
        {
            "icon": "⚔️",
            "name": "Quests",
            "description": "Find adventures waiting to happen."
        },
        {
            "icon": "🏛️",
            "name": "Factions",
            "description": "Discover powerful groups and organizations."
        },
        {
            "icon": "📜",
            "name": "Lore",
            "description": "Explore histories, legends and mysteries."
        },
        {
            "icon": "✨",
            "name": "Stories",
            "description": "Enter stories created across the Omniverse."
        }
    ],

    "featured_npcs": [
        {
            "name": "Kael Veyron",
            "role": "Dimensional Wanderer",
            "world": "The Shattered Realms",
            "level": 87,
            "description": "A mysterious traveler capable of crossing unstable dimensions."
        },
        {
            "name": "Lyra Solenne",
            "role": "Starborn Mage",
            "world": "Aetheris",
            "level": 72,
            "description": "A mage who manipulates ancient celestial energy."
        },
        {
            "name": "Drax Ironfall",
            "role": "Warlord",
            "world": "Ashen Dominion",
            "level": 94,
            "description": "Commander of an enormous army fighting for control of the Dominion."
        },
        {
            "name": "Mira Nightshade",
            "role": "Shadow Assassin",
            "world": "Nocturne",
            "level": 65,
            "description": "A legendary assassin who operates between worlds."
        }
    ],

    "worlds": [
        {
            "name": "Aetheris",
            "type": "Fantasy",
            "population": "8.4B",
            "description": "A world of floating continents, ancient magic and celestial civilizations."
        },
        {
            "name": "Nocturne",
            "type": "Dark Fantasy",
            "population": "2.1B",
            "description": "A world permanently covered by an unnatural night."
        },
        {
            "name": "Ashen Dominion",
            "type": "War",
            "population": "14.7B",
            "description": "A massive industrial civilization locked in endless conflict."
        },
        {
            "name": "The Shattered Realms",
            "type": "Multiverse",
            "population": "Unknown",
            "description": "Fragments of countless destroyed realities connected together."
        }
    ],

    "quests": [
        {
            "title": "The Lost Crown",
            "difficulty": "Legendary",
            "world": "Aetheris",
            "reward": "50,000 XP"
        },
        {
            "title": "Echoes of Nocturne",
            "difficulty": "Hard",
            "world": "Nocturne",
            "reward": "18,000 XP"
        },
        {
            "title": "The Iron Rebellion",
            "difficulty": "Extreme",
            "world": "Ashen Dominion",
            "reward": "75,000 XP"
        }
    ]
}


# ============================================================
# HTML GENERATOR
# ============================================================

def build_html(data):
    safe_name = html.escape(data["name"])
    safe_tagline = html.escape(data["tagline"])
    safe_description = html.escape(data["description"])

    stats_html = ""

    for name, value in data["stats"].items():
        stats_html += f"""
        <div class="stat-card">
            <div class="stat-number">{html.escape(str(value))}</div>
            <div class="stat-label">{html.escape(name)}</div>
        </div>
        """

    categories_html = ""

    for category in data["categories"]:
        categories_html += f"""
        <article class="category-card">
            <div class="category-icon">{html.escape(category["icon"])}</div>
            <h3>{html.escape(category["name"])}</h3>
            <p>{html.escape(category["description"])}</p>
            <button onclick="showCategory('{html.escape(category["name"])}')">
                Explore →
            </button>
        </article>
        """

    npc_html = ""

    for npc in data["featured_npcs"]:
        npc_html += f"""
        <article class="npc-card"
                 data-search="{html.escape(
                     npc["name"] + " " +
                     npc["role"] + " " +
                     npc["world"]
                 ).lower()}">

            <div class="npc-avatar">
                {html.escape(npc["name"][0])}
            </div>

            <div class="npc-content">

                <div class="npc-top">
                    <span class="npc-level">
                        LVL {npc["level"]}
                    </span>
                </div>

                <h3>{html.escape(npc["name"])}</h3>

                <div class="npc-role">
                    {html.escape(npc["role"])}
                </div>

                <div class="npc-world">
                    🌌 {html.escape(npc["world"])}
                </div>

                <p>
                    {html.escape(npc["description"])}
                </p>

                <button onclick="openNPC(
                    '{html.escape(npc["name"])}',
                    '{html.escape(npc["role"])}',
                    '{html.escape(npc["world"])}',
                    '${html.escape(str(npc["level"]))}'
                )">
                    View Character
                </button>

            </div>
        </article>
        """

    worlds_html = ""

    for world in data["worlds"]:
        worlds_html += f"""
        <article class="world-card"
                 data-search="{html.escape(
                     world["name"] + " " +
                     world["type"]
                 ).lower()}">

            <div class="world-symbol">🌌</div>

            <div>
                <span class="world-type">
                    {html.escape(world["type"])}
                </span>

                <h3>{html.escape(world["name"])}</h3>

                <p>
                    {html.escape(world["description"])}
                </p>

                <div class="world-info">
                    <span>👥 {html.escape(world["population"])}</span>
                </div>
            </div>

        </article>
        """

    quests_html = ""

    for quest in data["quests"]:
        quests_html += f"""
        <article class="quest-card"
                 data-search="{html.escape(
                     quest["title"] + " " +
                     quest["world"] + " " +
                     quest["difficulty"]
                 ).lower()}">

            <div class="quest-icon">⚔️</div>

            <div class="quest-content">

                <span class="difficulty">
                    {html.escape(quest["difficulty"])}
                </span>

                <h3>{html.escape(quest["title"])}</h3>

                <p>
                    🌌 {html.escape(quest["world"])}
                </p>

                <div class="quest-reward">
                    💎 {html.escape(quest["reward"])}
                </div>

            </div>

        </article>
        """

    data_json = json.dumps(data, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<meta name="theme-color" content="#080b14">

<title>{safe_name}</title>

<meta name="description"
      content="{safe_description}">

<style>

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

html {{
    scroll-behavior: smooth;
}}

body {{
    font-family:
        Inter,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    background:
        radial-gradient(
            circle at top left,
            #18213b 0,
            #080b14 35%,
            #05070d 100%
        );

    color: #f5f7ff;
    min-height: 100vh;
}}

button,
input {{
    font: inherit;
}}

button {{
    cursor: pointer;
}}

.container {{
    width: min(1400px, 94%);
    margin: auto;
}}


/* ============================================================
   HEADER
============================================================ */

header {{
    position: sticky;
    top: 0;
    z-index: 100;

    backdrop-filter: blur(20px);

    background: rgba(5, 7, 13, 0.82);

    border-bottom:
        1px solid rgba(255,255,255,.08);
}}

.nav {{
    min-height: 74px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    gap: 20px;
}}

.logo {{
    font-size: 21px;
    font-weight: 900;
    letter-spacing: -0.8px;

    white-space: nowrap;
}}

.logo span {{
    background:
        linear-gradient(
            90deg,
            #8b7cff,
            #43d9ff
        );

    -webkit-background-clip: text;
    color: transparent;
}}

.nav-links {{
    display: flex;
    gap: 8px;
    overflow-x: auto;
}}

.nav-links button {{
    background: transparent;
    border: 0;
    color: #aeb6ca;

    padding: 10px 14px;
    border-radius: 10px;
}}

.nav-links button:hover {{
    background: rgba(255,255,255,.07);
    color: white;
}}

.search {{
    width: 260px;
}}

.search input {{
    width: 100%;

    background:
        rgba(255,255,255,.06);

    border:
        1px solid rgba(255,255,255,.08);

    border-radius: 12px;

    padding: 11px 14px;

    color: white;
    outline: none;
}}

.search input:focus {{
    border-color: #7d70ff;
}}


/* ============================================================
   HERO
============================================================ */

.hero {{
    padding: 90px 0 60px;
}}

.hero-grid {{
    display: grid;
    grid-template-columns:
        minmax(0, 1.4fr)
        minmax(300px, .6fr);

    gap: 30px;
    align-items: center;
}}

.badge {{
    display: inline-flex;

    padding: 7px 12px;

    border-radius: 999px;

    background:
        rgba(125,112,255,.12);

    border:
        1px solid rgba(125,112,255,.3);

    color: #bcb5ff;

    font-size: 13px;
    font-weight: 700;

    margin-bottom: 20px;
}}

.hero h1 {{
    font-size: clamp(42px, 7vw, 88px);

    line-height: .95;

    letter-spacing: -4px;

    max-width: 850px;
}}

.hero h1 span {{
    background:
        linear-gradient(
            90deg,
            #9c91ff,
            #49dfff,
            #c48cff
        );

    -webkit-background-clip: text;
    color: transparent;
}}

.hero p {{
    color: #aab3c9;

    font-size: 18px;
    line-height: 1.7;

    max-width: 700px;

    margin-top: 25px;
}}

.hero-actions {{
    display: flex;
    gap: 12px;
    flex-wrap: wrap;

    margin-top: 30px;
}}

.primary-btn,
.secondary-btn {{
    border-radius: 12px;
    padding: 13px 19px;

    border: 1px solid transparent;

    font-weight: 800;
}}

.primary-btn {{
    background: white;
    color: #070910;
}}

.secondary-btn {{
    background:
        rgba(255,255,255,.06);

    border-color:
        rgba(255,255,255,.1);

    color: white;
}}


/* ============================================================
   ORB
============================================================ */

.hero-orb {{
    min-height: 330px;

    display: grid;
    place-items: center;

    border-radius: 28px;

    background:
        radial-gradient(
            circle,
            rgba(118,103,255,.3),
            transparent 55%
        ),
        rgba(255,255,255,.035);

    border:
        1px solid rgba(255,255,255,.08);
}}

.orb {{
    width: 190px;
    height: 190px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #d5d0ff,
            #7166ff 35%,
            #272153 65%,
            #090b14 100%
        );

    box-shadow:
        0 0 80px rgba(115,100,255,.65),
        inset -30px -25px 50px rgba(0,0,0,.5);

    animation: float 5s ease-in-out infinite;
}}

@keyframes float {{
    0%,100% {{
        transform: translateY(0);
    }}

    50% {{
        transform: translateY(-15px);
    }}
}}


/* ============================================================
   STATS
============================================================ */

.stats {{
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 14px;

    padding-bottom: 70px;
}}

.stat-card {{
    padding: 25px;

    background:
        rgba(255,255,255,.045);

    border:
        1px solid rgba(255,255,255,.08);

    border-radius: 18px;
}}

.stat-number {{
    font-size: 30px;
    font-weight: 900;
}}

.stat-label {{
    margin-top: 5px;
    color: #8f99b2;
}}


/* ============================================================
   SECTIONS
============================================================ */

section {{
    padding: 35px 0 75px;
}}

.section-header {{
    display: flex;
    align-items: end;
    justify-content: space-between;

    gap: 20px;

    margin-bottom: 25px;
}}

.section-header h2 {{
    font-size: 32px;
    letter-spacing: -1px;
}}

.section-header p {{
    color: #8e97ad;
    margin-top: 5px;
}}


/* ============================================================
   CATEGORY CARDS
============================================================ */

.category-grid {{
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 16px;
}}

.category-card,
.npc-card,
.world-card,
.quest-card {{
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.065),
            rgba(255,255,255,.025)
        );

    border:
        1px solid rgba(255,255,255,.08);

    border-radius: 20px;

    transition:
        transform .2s,
        border-color .2s;

    overflow: hidden;
}}

.category-card:hover,
.npc-card:hover,
.world-card:hover,
.quest-card:hover {{
    transform: translateY(-4px);

    border-color:
        rgba(140,130,255,.35);
}}

.category-card {{
    padding: 25px;
}}

.category-icon {{
    font-size: 34px;
    margin-bottom: 18px;
}}

.category-card h3 {{
    font-size: 20px;
}}

.category-card p {{
    color: #929bb0;
    line-height: 1.6;
    margin: 8px 0 20px;
}}

.category-card button,
.npc-content button {{
    border: 0;

    background:
        rgba(255,255,255,.08);

    color: white;

    padding: 9px 13px;

    border-radius: 9px;

    font-weight: 700;
}}


/* ============================================================
   NPCS
============================================================ */

.npc-grid {{
    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 16px;
}}

.npc-card {{
    display: flex;
}}

.npc-avatar {{
    width: 110px;
    min-width: 110px;

    display: grid;
    place-items: center;

    font-size: 40px;
    font-weight: 900;

    background:
        radial-gradient(
            circle,
            #55508e,
            #15172b
        );
}}

.npc-content {{
    padding: 22px;
    min-width: 0;
}}

.npc-top {{
    display: flex;
    justify-content: end;
}}

.npc-level {{
    font-size: 11px;
    font-weight: 900;

    padding: 5px 8px;

    border-radius: 7px;

    background:
        rgba(96,220,255,.1);

    color: #71ddff;
}}

.npc-content h3 {{
    margin-top: 8px;
    font-size: 23px;
}}

.npc-role {{
    color: #b5aaff;
    margin-top: 4px;
}}

.npc-world {{
    color: #778197;
    margin-top: 10px;
    font-size: 13px;
}}

.npc-content p {{
    color: #929bb0;
    line-height: 1.6;
    margin: 13px 0 18px;
}}


/* ============================================================
   WORLDS
============================================================ */

.world-grid {{
    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 16px;
}}

.world-card {{
    padding: 24px;

    display: flex;
    gap: 20px;
}}

.world-symbol {{
    width: 65px;
    height: 65px;

    min-width: 65px;

    display: grid;
    place-items: center;

    border-radius: 16px;

    font-size: 30px;

    background:
        rgba(117,106,255,.12);
}}

.world-type {{
    color: #8e85ff;

    font-size: 12px;
    font-weight: 800;

    text-transform: uppercase;
}}

.world-card h3 {{
    font-size: 22px;
    margin: 4px 0 8px;
}}

.world-card p {{
    color: #929bb0;
    line-height: 1.6;
}}

.world-info {{
    margin-top: 15px;
    color: #788298;
    font-size: 13px;
}}


/* ============================================================
   QUESTS
============================================================ */

.quest-grid {{
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 16px;
}}

.quest-card {{
    padding: 22px;

    display: flex;
    gap: 15px;
}}

.quest-icon {{
    font-size: 30px;
}}

.difficulty {{
    color: #ffbd72;
    font-size: 11px;
    font-weight: 900;
    text-transform: uppercase;
}}

.quest-card h3 {{
    margin: 5px 0;
}}

.quest-card p {{
    color: #8992a8;
    font-size: 13px;
}}

.quest-reward {{
    margin-top: 15px;

    color: #79e1bd;

    font-weight: 800;
}}


/* ============================================================
   FOOTER
============================================================ */

footer {{
    border-top:
        1px solid rgba(255,255,255,.08);

    padding: 35px 0;

    color: #717b91;

    text-align: center;
}}


/* ============================================================
   MODAL
============================================================ */

.modal {{
    position: fixed;
    inset: 0;

    z-index: 999;

    display: none;
    place-items: center;

    padding: 20px;

    background:
        rgba(0,0,0,.75);

    backdrop-filter: blur(8px);
}}

.modal.active {{
    display: grid;
}}

.modal-box {{
    width: min(550px, 100%);

    background: #111522;

    border:
        1px solid rgba(255,255,255,.1);

    border-radius: 22px;

    padding: 30px;

    position: relative;
}}

.close {{
    position: absolute;

    top: 15px;
    right: 15px;

    border: 0;

    width: 35px;
    height: 35px;

    border-radius: 50%;

    background:
        rgba(255,255,255,.08);

    color: white;

    font-size: 18px;
}}

.modal-box h2 {{
    font-size: 30px;
}}

.modal-box p {{
    color: #969fb4;
    line-height: 1.7;
    margin-top: 12px;
}}


/* ============================================================
   SEARCH RESULTS
============================================================ */

.hidden {{
    display: none !important;
}}

#searchStatus {{
    margin-top: 15px;
    color: #929bb0;
}}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width: 1000px) {{

    .hero-grid {{
        grid-template-columns: 1fr;
    }}

    .hero-orb {{
        min-height: 250px;
    }}

    .category-grid {{
        grid-template-columns:
            repeat(2, 1fr);
    }}

    .quest-grid {{
        grid-template-columns:
            repeat(2, 1fr);
    }}

    .search {{
        display: none;
    }}
}}


@media (max-width: 700px) {{

    .container {{
        width: min(94%, 600px);
    }}

    .nav {{
        min-height: 64px;
    }}

    .logo {{
        font-size: 17px;
    }}

    .nav-links {{
        display: none;
    }}

    .hero {{
        padding: 55px 0 40px;
    }}

    .hero h1 {{
        font-size: 48px;
        letter-spacing: -2.5px;
    }}

    .hero p {{
        font-size: 16px;
    }}

    .stats {{
        grid-template-columns:
            repeat(2, 1fr);

        padding-bottom: 40px;
    }}

    .category-grid,
    .npc-grid,
    .world-grid,
    .quest-grid {{
        grid-template-columns: 1fr;
    }}

    .npc-card {{
        flex-direction: column;
    }}

    .npc-avatar {{
        width: 100%;
        height: 100px;
        min-width: 0;
    }}

    .section-header {{
        align-items: start;
        flex-direction: column;
    }}

    section {{
        padding-bottom: 45px;
    }}
}}


@media (max-width: 420px) {{

    .hero h1 {{
        font-size: 41px;
    }}

    .stats {{
        grid-template-columns: 1fr;
    }}

    .stat-card {{
        padding: 18px;
    }}
}}

</style>

</head>


<body>


<header>

<div class="container nav">

<div class="logo">
    🌌 <span>{safe_name}</span>
</div>

<nav class="nav-links">

<button onclick="scrollToSection('home')">
    Home
</button>

<button onclick="scrollToSection('categories')">
    Explore
</button>

<button onclick="scrollToSection('npcs')">
    NPCs
</button>

<button onclick="scrollToSection('worlds')">
    Worlds
</button>

<button onclick="scrollToSection('quests')">
    Quests
</button>

</nav>

<div class="search">

<input
    id="searchInput"
    type="search"
    placeholder="Search Omniverse..."
    oninput="searchSite()"
/>

</div>

</div>

</header>


<main>


<!-- HERO -->

<section id="home" class="hero">

<div class="container hero-grid">

<div>

<div class="badge">
    ✦ THE INFINITE UNIVERSE
</div>

<h1>
    Welcome to
    <span>the Omniverse.</span>
</h1>

<p>
    {safe_tagline}
    {safe_description}
</p>

<div class="hero-actions">

<button
    class="primary-btn"
    onclick="scrollToSection('categories')"
>
    Explore Universe
</button>

<button
    class="secondary-btn"
    onclick="randomNPC()"
>
    Random NPC
</button>

</div>

</div>


<div class="hero-orb">

<div class="orb"></div>

</div>

</div>

</section>


<!-- STATS -->

<div class="container">

<div class="stats">

{stats_html}

</div>

</div>


<!-- CATEGORIES -->

<section id="categories">

<div class="container">

<div class="section-header">

<div>

<h2>Explore the Omniverse</h2>

<p>
Discover everything inside the universe.
</p>

</div>

</div>


<div class="category-grid">

{categories_html}

</div>

</div>

</section>


<!-- NPCS -->

<section id="npcs">

<div class="container">

<div class="section-header">

<div>

<h2>Featured NPCs</h2>

<p>
Characters waiting to be discovered.
</p>

</div>

</div>


<div class="npc-grid" id="npcGrid">

{npc_html}

</div>

</div>

</section>


<!-- WORLDS -->

<section id="worlds">

<div class="container">

<div class="section-header">

<div>

<h2>Worlds</h2>

<p>
Explore different realities.
</p>

</div>

</div>


<div class="world-grid" id="worldGrid">

{worlds_html}

</div>

</div>

</section>


<!-- QUESTS -->

<section id="quests">

<div class="container">

<div class="section-header">

<div>

<h2>Active Quests</h2>

<p>
Adventures across the Omniverse.
</p>

</div>

</div>


<div class="quest-grid" id="questGrid">

{quests_html}

</div>

</div>

</section>


</main>


<footer>

<div class="container">

<strong>{safe_name}</strong>

<br><br>

Explore. Create. Discover.

</div>

</footer>


<!-- MODAL -->

<div
    id="modal"
    class="modal"
    onclick="closeModal(event)"
>

<div class="modal-box">

<button
    class="close"
    onclick="closeModal()"
>
    ×
</button>

<div id="modalContent"></div>

</div>

</div>


<script>

const SITE_DATA = {data_json};


/* ============================================================
   NAVIGATION
============================================================ */

function scrollToSection(id) {{

    const element = document.getElementById(id);

    if (element) {{
        element.scrollIntoView({{
            behavior: "smooth",
            block: "start"
        }});
    }}

}}


/* ============================================================
   MODAL
============================================================ */

function openModal(title, content) {{

    document.getElementById("modalContent").innerHTML = `
        <h2>${{title}}</h2>
        <p>${{content}}</p>
    `;

    document.getElementById("modal").classList.add("active");

}}


function closeModal(event) {{

    if (
        !event ||
        event.target.id === "modal" ||
        event.target.classList.contains("close")
    ) {{
        document.getElementById("modal")
            .classList.remove("active");
    }}

}}


/* ============================================================
   NPC
============================================================ */

function openNPC(name, role, world, level) {{

    openModal(
        name,
        `
        <strong>Role:</strong> ${{role}}<br><br>
        <strong>World:</strong> ${{world}}<br><br>
        <strong>Level:</strong> ${{level}}
        `
    );

}}


function randomNPC() {{

    const npcs = SITE_DATA.featured_npcs;

    const npc =
        npcs[Math.floor(Math.random() * npcs.length)];

    openNPC(
        npc.name,
        npc.role,
        npc.world,
        npc.level
    );

}}


/* ============================================================
   CATEGORY
============================================================ */

function showCategory(category) {{

    openModal(
        category,
        `Explore the ${{category}} section of NPC OMNIVERSE.`
    );

}}


/* ============================================================
   SEARCH
============================================================ */

function searchSite() {{

    const query =
        document
            .getElementById("searchInput")
            .value
            .toLowerCase()
            .trim();


    const cards =
        document.querySelectorAll(
            ".npc-card, .world-card, .quest-card"
        );


    let found = 0;


    cards.forEach(card => {{

        const text =
            card.dataset.search || "";


        if (!query || text.includes(query)) {{

            card.classList.remove("hidden");

            found++;

        }} else {{

            card.classList.add("hidden");

        }}

    }});


    if (query) {{

        scrollToSection("npcs");

    }}

}}


/* ============================================================
   KEYBOARD
============================================================ */

document.addEventListener(
    "keydown",
    function(event) {{

        if (event.key === "Escape") {{
            document
                .getElementById("modal")
                .classList.remove("active");
        }}

    }}
);

</script>


</body>

</html>
"""


# ============================================================
# CREATE STATIC WEBSITE
# ============================================================

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        build_html(SITE_DATA),
        encoding="utf-8"
    )

    print()
    print("=" * 60)
    print("NPC OMNIVERSE STATIC SITE CREATED")
    print("=" * 60)
    print()
    print(f"Output: {OUTPUT_FILE}")
    print()
    print("Open:")
    print(f"    {OUTPUT_FILE}")
    print()
    print("No Flask required.")
    print("No database required.")
    print("No server required for deployment.")
    print()


if __name__ == "__main__":
    main()
