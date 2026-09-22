from pathlib import Path
import json
import html
import re


# ============================================================
# NPC OMNIVERSE
# STATIC WEBSITE GENERATOR
#
# Run:
#     python app.py
#
# Creates:
#     site/index.html
#     site/robots.txt
#     site/sitemap.xml
#
# No Flask
# No database
# No server
# ============================================================


OUTPUT_DIR = Path("site")
OUTPUT_FILE = OUTPUT_DIR / "index.html"
ROBOTS_FILE = OUTPUT_DIR / "robots.txt"
SITEMAP_FILE = OUTPUT_DIR / "sitemap.xml"


# ============================================================
# WEBSITE SETTINGS
# ============================================================

SITE_DATA = {

    "name": "NPC OMNIVERSE",

    "tagline": "Explore. Create. Discover.",

    "description": (
        "NPC OMNIVERSE is an interactive universe of NPCs, "
        "worlds, quests, factions, lore and stories."
    ),

    # IMPORTANT:
    # This is the public website URL.
    "url": "https://npcbook.onrender.com/",

    "language": "en",

    "author": "NPC OMNIVERSE",

    "keywords": [
        "NPC",
        "NPCs",
        "NPC database",
        "fictional characters",
        "characters",
        "fantasy characters",
        "game characters",
        "worlds",
        "quests",
        "factions",
        "lore",
        "stories",
        "omniverse",
        "fictional universe"
    ],


    # ========================================================
    # STATS
    # ========================================================

    "stats": {
        "NPCs": 12840,
        "Worlds": 426,
        "Quests": 1892,
        "Factions": 317
    },


    # ========================================================
    # CATEGORIES
    # ========================================================

    "categories": [

        {
            "icon": "👤",
            "name": "NPCs",
            "description": (
                "Discover characters from countless worlds, "
                "realities and stories."
            )
        },

        {
            "icon": "🌌",
            "name": "Worlds",
            "description": (
                "Explore civilizations, planets, dimensions "
                "and alternate realities."
            )
        },

        {
            "icon": "⚔️",
            "name": "Quests",
            "description": (
                "Find adventures, missions and challenges "
                "waiting to happen."
            )
        },

        {
            "icon": "🏛️",
            "name": "Factions",
            "description": (
                "Discover powerful groups, organizations "
                "and alliances."
            )
        },

        {
            "icon": "📜",
            "name": "Lore",
            "description": (
                "Explore histories, legends, mysteries "
                "and forgotten knowledge."
            )
        },

        {
            "icon": "✨",
            "name": "Stories",
            "description": (
                "Enter stories created throughout "
                "the Omniverse."
            )
        }
    ],


    # ========================================================
    # NPC DATABASE
    # ========================================================

    "featured_npcs": [

        {
            "name": "Kael Veyron",
            "role": "Dimensional Wanderer",
            "world": "The Shattered Realms",
            "level": 87,
            "description": (
                "A mysterious traveler capable of crossing "
                "unstable dimensions."
            )
        },

        {
            "name": "Lyra Solenne",
            "role": "Starborn Mage",
            "world": "Aetheris",
            "level": 72,
            "description": (
                "A mage who manipulates ancient celestial energy."
            )
        },

        {
            "name": "Drax Ironfall",
            "role": "Warlord",
            "world": "Ashen Dominion",
            "level": 94,
            "description": (
                "Commander of an enormous army fighting "
                "for control of the Dominion."
            )
        },

        {
            "name": "Mira Nightshade",
            "role": "Shadow Assassin",
            "world": "Nocturne",
            "level": 65,
            "description": (
                "A legendary assassin who operates "
                "between worlds."
            )
        }
    ],


    # ========================================================
    # WORLDS
    # ========================================================

    "worlds": [

        {
            "name": "Aetheris",
            "type": "Fantasy",
            "population": "8.4B",
            "description": (
                "A world of floating continents, ancient magic "
                "and celestial civilizations."
            )
        },

        {
            "name": "Nocturne",
            "type": "Dark Fantasy",
            "population": "2.1B",
            "description": (
                "A world permanently covered by an unnatural night."
            )
        },

        {
            "name": "Ashen Dominion",
            "type": "War",
            "population": "14.7B",
            "description": (
                "A massive industrial civilization locked "
                "in endless conflict."
            )
        },

        {
            "name": "The Shattered Realms",
            "type": "Multiverse",
            "population": "Unknown",
            "description": (
                "Fragments of countless destroyed realities "
                "connected together."
            )
        }
    ],


    # ========================================================
    # QUESTS
    # ========================================================

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
# HELPERS
# ============================================================

def esc(value):
    """HTML escape."""
    return html.escape(str(value), quote=True)


def slug(value):
    """Create a simple URL/search slug."""
    value = str(value).lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def search_text(*values):
    """Create normalized searchable text."""
    return " ".join(
        str(value).lower()
        for value in values
    )


# ============================================================
# GENERATE SEO KEYWORDS
# ============================================================

def generate_keywords(data):

    keywords = list(data.get("keywords", []))

    for npc in data["featured_npcs"]:
        keywords.extend([
            npc["name"],
            npc["role"],
            npc["world"]
        ])

    for world in data["worlds"]:
        keywords.extend([
            world["name"],
            world["type"]
        ])

    for quest in data["quests"]:
        keywords.extend([
            quest["title"],
            quest["world"],
            quest["difficulty"]
        ])

    # Remove duplicates while preserving order.
    result = []

    seen = set()

    for keyword in keywords:

        key = str(keyword).lower().strip()

        if key and key not in seen:

            seen.add(key)
            result.append(key)

    return ", ".join(result)


# ============================================================
# BUILD NPC HTML
# ============================================================

def build_npc_html(data):

    output = ""

    for index, npc in enumerate(data["featured_npcs"]):

        name = esc(npc["name"])
        role = esc(npc["role"])
        world = esc(npc["world"])
        level = esc(npc["level"])
        description = esc(npc["description"])

        searchable = esc(
            search_text(
                npc["name"],
                npc["role"],
                npc["world"],
                npc["description"]
            )
        )

        first_letter = esc(
            npc["name"][0]
            if npc["name"]
            else "?"
        )

        output += f"""

        <article
            class="npc-card"
            data-type="npc"
            data-name="{name}"
            data-search="{searchable}"
            data-index="{index}"
        >

            <div class="npc-avatar">
                {first_letter}
            </div>

            <div class="npc-content">

                <div class="npc-top">

                    <span class="npc-level">
                        LVL {level}
                    </span>

                </div>

                <h3>{name}</h3>

                <div class="npc-role">
                    {role}
                </div>

                <div class="npc-world">
                    🌌 {world}
                </div>

                <p>
                    {description}
                </p>

                <button
                    class="card-button"
                    onclick="openNPC(
                        {json.dumps(npc["name"])},
                        {json.dumps(npc["role"])},
                        {json.dumps(npc["world"])},
                        {json.dumps(str(npc["level"]))},
                        {json.dumps(npc["description"])}
                    )"
                >
                    View Character →
                </button>

            </div>

        </article>
        """

    return output


# ============================================================
# BUILD WORLD HTML
# ============================================================

def build_world_html(data):

    output = ""

    for world in data["worlds"]:

        name = esc(world["name"])
        world_type = esc(world["type"])
        population = esc(world["population"])
        description = esc(world["description"])

        searchable = esc(
            search_text(
                world["name"],
                world["type"],
                world["description"]
            )
        )

        output += f"""

        <article
            class="world-card"
            data-type="world"
            data-name="{name}"
            data-search="{searchable}"
        >

            <div class="world-symbol">
                🌌
            </div>

            <div class="world-content">

                <span class="world-type">
                    {world_type}
                </span>

                <h3>
                    {name}
                </h3>

                <p>
                    {description}
                </p>

                <div class="world-info">
                    👥 {population}
                </div>

            </div>

        </article>
        """

    return output


# ============================================================
# BUILD QUEST HTML
# ============================================================

def build_quest_html(data):

    output = ""

    for quest in data["quests"]:

        title = esc(quest["title"])
        difficulty = esc(quest["difficulty"])
        world = esc(quest["world"])
        reward = esc(quest["reward"])

        searchable = esc(
            search_text(
                quest["title"],
                quest["world"],
                quest["difficulty"],
                quest["reward"]
            )
        )

        output += f"""

        <article
            class="quest-card"
            data-type="quest"
            data-name="{title}"
            data-search="{searchable}"
        >

            <div class="quest-icon">
                ⚔️
            </div>

            <div class="quest-content">

                <span class="difficulty">
                    {difficulty}
                </span>

                <h3>
                    {title}
                </h3>

                <p>
                    🌌 {world}
                </p>

                <div class="quest-reward">
                    💎 {reward}
                </div>

            </div>

        </article>
        """

    return output


# ============================================================
# BUILD CATEGORY HTML
# ============================================================

def build_category_html(data):

    output = ""

    for category in data["categories"]:

        name = esc(category["name"])
        icon = esc(category["icon"])
        description = esc(category["description"])

        output += f"""

        <article class="category-card">

            <div class="category-icon">
                {icon}
            </div>

            <h3>
                {name}
            </h3>

            <p>
                {description}
            </p>

            <button
                class="card-button"
                onclick="showCategory(
                    {json.dumps(category["name"])}
                )"
            >
                Explore →
            </button>

        </article>
        """

    return output


# ============================================================
# BUILD STATS
# ============================================================

def build_stats_html(data):

    output = ""

    for name, value in data["stats"].items():

        output += f"""

        <div class="stat-card">

            <div class="stat-number">
                {esc(value)}
            </div>

            <div class="stat-label">
                {esc(name)}
            </div>

        </div>
        """

    return output


# ============================================================
# BUILD JSON-LD SEO
# ============================================================

def build_json_ld(data):

    base_url = data["url"].rstrip("/")

    graph = [

        {
            "@type": "WebSite",
            "@id": base_url + "/#website",
            "url": base_url + "/",
            "name": data["name"],
            "description": data["description"],
            "inLanguage": data["language"]
        },

        {
            "@type": "WebPage",
            "@id": base_url + "/#webpage",
            "url": base_url + "/",
            "name": data["name"],
            "description": data["description"],
            "isPartOf": {
                "@id": base_url + "/#website"
            }
        },

        {
            "@type": "CollectionPage",
            "name": "NPC Directory",
            "description": (
                "Explore NPC characters from NPC OMNIVERSE."
            },
            "url": base_url + "/#npcs"
        },

        {
            "@type": "CollectionPage",
            "name": "World Directory",
            "description": (
                "Explore worlds and realities from NPC OMNIVERSE."
            },
            "url": base_url + "/#worlds"
        }
    ]

    # Add NPC structured data.
    for npc in data["featured_npcs"]:

        graph.append({

            "@type": "Person",

            "name": npc["name"],

            "jobTitle": npc["role"],

            "description": npc["description"],

            "isPartOf": {
                "@type": "CreativeWork",
                "name": npc["world"]
            }
        })

    schema = {
        "@context": "https://schema.org",
        "@graph": graph
    }

    return json.dumps(
        schema,
        ensure_ascii=False,
        indent=2
    )


# ============================================================
# BUILD MAIN HTML
# ============================================================

def build_html(data):

    site_name = esc(data["name"])
    tagline = esc(data["tagline"])
    description = esc(data["description"])
    canonical_url = esc(data["url"])
    keywords = esc(generate_keywords(data))

    stats_html = build_stats_html(data)
    categories_html = build_category_html(data)
    npc_html = build_npc_html(data)
    worlds_html = build_world_html(data)
    quests_html = build_quest_html(data)

    json_ld = build_json_ld(data)

    data_json = json.dumps(
        data,
        ensure_ascii=False
    )

    return f"""<!DOCTYPE html>

<html
    lang="{esc(data["language"])}"
>

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<meta
    name="theme-color"
    content="#080b14"
>

<title>
    {site_name} — Explore NPCs, Worlds, Quests & Stories
</title>

<meta
    name="description"
    content="{description}"
>

<meta
    name="keywords"
    content="{keywords}"
>

<meta
    name="author"
    content="{esc(data["author"])}"
>

<meta
    name="robots"
    content="index, follow, max-image-preview:large"
>

<link
    rel="canonical"
    href="{canonical_url}"
>


<!-- ========================================================
     OPEN GRAPH
========================================================= -->

<meta
    property="og:type"
    content="website"
>

<meta
    property="og:title"
    content="{site_name} — Explore the Omniverse"
>

<meta
    property="og:description"
    content="{description}"
>

<meta
    property="og:url"
    content="{canonical_url}"
>

<meta
    property="og:site_name"
    content="{site_name}"
>


<!-- ========================================================
     TWITTER
========================================================= -->

<meta
    name="twitter:card"
    content="summary_large_image"
>

<meta
    name="twitter:title"
    content="{site_name} — Explore the Omniverse"
>

<meta
    name="twitter:description"
    content="{description}"
>


<!-- ========================================================
     STRUCTURED DATA
========================================================= -->

<script type="application/ld+json">
{json_ld}
</script>


<style>

/* ============================================================
   RESET
============================================================ */

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

html {{
    scroll-behavior: smooth;
    scroll-padding-top: 90px;
}}

body {{

    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    background:

        radial-gradient(
            circle at 10% 0%,
            #18213b 0,
            transparent 35%
        ),

        radial-gradient(
            circle at 90% 20%,
            #19133b 0,
            transparent 30%
        ),

        #05070d;

    color: #f5f7ff;

    min-height: 100vh;

    overflow-x: hidden;
}}

button,
input {{
    font: inherit;
}}

button {{
    cursor: pointer;
}}

button:focus-visible,
input:focus-visible {{
    outline: 2px solid #8b7cff;
    outline-offset: 3px;
}}

.container {{

    width:
        min(
            1400px,
            calc(100% - 40px)
        );

    margin: auto;
}}


/* ============================================================
   HEADER
============================================================ */

header {{

    position: sticky;

    top: 0;

    z-index: 100;

    background:
        rgba(5, 7, 13, .86);

    backdrop-filter:
        blur(20px);

    border-bottom:
        1px solid
        rgba(255,255,255,.08);
}}

.nav {{

    min-height: 74px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 20px;
}}

.logo {{

    font-size: 20px;

    font-weight: 950;

    letter-spacing: -.8px;

    white-space: nowrap;
}}

.logo span {{

    background:
        linear-gradient(
            90deg,
            #9c91ff,
            #49dfff
        );

    -webkit-background-clip: text;

    background-clip: text;

    color: transparent;
}}

.nav-links {{

    display: flex;

    gap: 5px;

    overflow-x: auto;
}}

.nav-links button {{

    background: transparent;

    border: 0;

    color: #aeb6ca;

    padding: 10px 13px;

    border-radius: 10px;

    font-weight: 700;
}}

.nav-links button:hover {{

    background:
        rgba(255,255,255,.07);

    color: white;
}}


/* ============================================================
   SEARCH
============================================================ */

.search {{

    width: 270px;

    position: relative;
}}

.search input {{

    width: 100%;

    background:
        rgba(255,255,255,.065);

    border:
        1px solid
        rgba(255,255,255,.10);

    border-radius: 13px;

    padding: 12px 14px;

    color: white;

    outline: none;
}}

.search input::placeholder {{
    color: #727c94;
}}

.search input:focus {{
    border-color: #7d70ff;
}}


/* ============================================================
   SEARCH PANEL
============================================================ */

.search-panel {{

    position: fixed;

    top: 82px;

    left: 50%;

    transform: translateX(-50%);

    width:
        min(
            850px,
            calc(100% - 30px)
        );

    max-height: 70vh;

    overflow-y: auto;

    background:
        rgba(13,17,29,.98);

    border:
        1px solid
        rgba(255,255,255,.12);

    border-radius: 20px;

    box-shadow:
        0 30px 100px
        rgba(0,0,0,.5);

    padding: 12px;

    display: none;
}}

.search-panel.active {{
    display: block;
}}

.search-result {{

    display: flex;

    align-items: center;

    gap: 14px;

    padding: 13px;

    border-radius: 13px;

    color: white;

    text-decoration: none;

    border:
        1px solid transparent;
}}

.search-result:hover {{

    background:
        rgba(255,255,255,.06);

    border-color:
        rgba(255,255,255,.08);
}}

.search-result-avatar {{

    width: 42px;
    height: 42px;

    min-width: 42px;

    display: grid;
    place-items: center;

    border-radius: 12px;

    background:
        linear-gradient(
            145deg,
            #55508e,
            #15172b
        );

    font-weight: 900;
}}

.search-result-info {{
    min-width: 0;
}}

.search-result-title {{
    font-weight: 850;
}}

.search-result-meta {{

    margin-top: 3px;

    color: #8992a8;

    font-size: 12px;
}}

.search-section-title {{

    padding:
        10px
        10px
        7px;

    color: #8e85ff;

    font-size: 11px;

    text-transform: uppercase;

    letter-spacing: .12em;

    font-weight: 900;
}}

.no-results {{

    padding: 35px 15px;

    text-align: center;

    color: #7e879d;
}}


/* ============================================================
   HERO
============================================================ */

.hero {{

    padding:
        100px
        0
        65px;
}}

.hero-grid {{

    display: grid;

    grid-template-columns:
        minmax(0, 1.4fr)
        minmax(300px, .6fr);

    gap: 35px;

    align-items: center;
}}

.badge {{

    display: inline-flex;

    padding: 7px 12px;

    border-radius: 999px;

    background:
        rgba(125,112,255,.12);

    border:
        1px solid
        rgba(125,112,255,.3);

    color: #bcb5ff;

    font-size: 12px;

    font-weight: 800;

    margin-bottom: 20px;
}}

.hero h1 {{

    font-size:
        clamp(
            44px,
            7vw,
            88px
        );

    line-height: .95;

    letter-spacing: -4px;

    max-width: 900px;
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

    background-clip: text;

    color: transparent;
}}

.hero p {{

    color: #aab3c9;

    font-size: 18px;

    line-height: 1.7;

    max-width: 720px;

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

    border:
        1px solid transparent;

    font-weight: 850;
}}

.primary-btn {{

    background: white;

    color: #070910;
}}

.secondary-btn {{

    background:
        rgba(255,255,255,.06);

    border-color:
        rgba(255,255,255,.10);

    color: white;
}}

.primary-btn:hover,
.secondary-btn:hover {{
    transform: translateY(-2px);
}}


/* ============================================================
   ORB
============================================================ */

.hero-orb {{

    min-height: 340px;

    display: grid;

    place-items: center;

    border-radius: 30px;

    background:

        radial-gradient(
            circle,
            rgba(118,103,255,.30),
            transparent 55%
        ),

        rgba(255,255,255,.035);

    border:
        1px solid
        rgba(255,255,255,.08);
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

        0 0 80px
        rgba(115,100,255,.65),

        inset -30px -25px 50px
        rgba(0,0,0,.5);

    animation:
        float 5s ease-in-out infinite;
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
        1px solid
        rgba(255,255,255,.08);

    border-radius: 18px;
}}

.stat-number {{

    font-size: 30px;

    font-weight: 950;
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
   CATEGORY
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
        1px solid
        rgba(255,255,255,.08);

    border-radius: 20px;

    transition:
        transform .2s,
        border-color .2s,
        box-shadow .2s;

    overflow: hidden;
}}

.category-card:hover,
.npc-card:hover,
.world-card:hover,
.quest-card:hover {{

    transform:
        translateY(-4px);

    border-color:
        rgba(140,130,255,.35);

    box-shadow:
        0 15px 40px
        rgba(0,0,0,.18);
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

    margin:
        8px
        0
        20px;
}}


/* ============================================================
   BUTTONS
============================================================ */

.card-button {{

    border: 0;

    background:
        rgba(255,255,255,.08);

    color: white;

    padding:
        9px
        13px;

    border-radius: 9px;

    font-weight: 750;
}}

.card-button:hover {{
    background:
        rgba(255,255,255,.14);
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

    font-weight: 950;

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

    flex: 1;
}}

.npc-top {{

    display: flex;

    justify-content: end;
}}

.npc-level {{

    font-size: 11px;

    font-weight: 900;

    padding:
        5px
        8px;

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

    margin:
        13px
        0
        18px;
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

    margin:
        4px
        0
        8px;
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
        1px solid
        rgba(255,255,255,.08);

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

    backdrop-filter:
        blur(8px);
}}

.modal.active {{
    display: grid;
}}

.modal-box {{

    width:
        min(
            550px,
            100%
        );

    background: #111522;

    border:
        1px solid
        rgba(255,255,255,.1);

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

.modal-meta {{

    margin-top: 20px;

    padding: 15px;

    border-radius: 13px;

    background:
        rgba(255,255,255,.045);
}}


/* ============================================================
   SEARCH STATES
============================================================ */

.hidden {{
    display: none !important;
}}

.search-highlight {{

    border-color:
        rgba(139,124,255,.7) !important;

    box-shadow:
        0 0 0 2px
        rgba(139,124,255,.12),
        0 20px 50px
        rgba(0,0,0,.2);
}}

#searchStatus {{

    margin-top: 15px;

    color: #929bb0;

    min-height: 20px;
}}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width: 1100px) {{

    .hero-grid {{
        grid-template-columns: 1fr;
    }}

    .hero-orb {{
        min-height: 260px;
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
        width: 220px;
    }}
}}


@media (max-width: 800px) {{

    .nav {{
        min-height: 65px;
    }}

    .nav-links {{
        display: none;
    }}

    .search {{
        width:
            min(
                300px,
                45vw
            );
    }}

    .hero {{
        padding:
            60px
            0
            45px;
    }}

    .stats {{
        grid-template-columns:
            repeat(2, 1fr);

        padding-bottom: 45px;
    }}

    .category-grid,
    .npc-grid,
    .world-grid,
    .quest-grid {{
        grid-template-columns: 1fr;
    }}
}}


@media (max-width: 560px) {{

    .container {{
        width:
            calc(100% - 24px);
    }}

    .logo {{
        font-size: 16px;
    }}

    .search {{
        width: 150px;
    }}

    .hero h1 {{

        font-size: 47px;

        letter-spacing: -2.5px;
    }}

    .hero p {{
        font-size: 16px;
    }}

    .stats {{
        grid-template-columns:
            repeat(2, 1fr);
    }}

    .stat-card {{
        padding: 18px;
    }}

    .stat-number {{
        font-size: 24px;
    }}

    .npc-card {{
        flex-direction: column;
    }}

    .npc-avatar {{

        width: 100%;

        height: 95px;

        min-width: 0;
    }}

    .world-card {{
        flex-direction: column;
    }}

    .section-header {{
        align-items: start;

        flex-direction: column;
    }}

    section {{
        padding-bottom: 45px;
    }}
}}


@media (max-width: 390px) {{

    .logo {{
        font-size: 14px;
    }}

    .search {{
        width: 125px;
    }}

    .hero h1 {{
        font-size: 40px;
    }}

    .stats {{
        grid-template-columns: 1fr;
    }}
}}


/* ============================================================
   REDUCED MOTION
============================================================ */

@media (prefers-reduced-motion: reduce) {{

    *,
    *::before,
    *::after {{

        scroll-behavior: auto !important;

        animation-duration:
            .01ms !important;

        animation-iteration-count:
            1 !important;

        transition-duration:
            .01ms !important;
    }}
}}

</style>

</head>


<body>


<!-- ==========================================================
     HEADER
=========================================================== -->

<header>

<div class="container nav">

<a
    href="#home"
    class="logo"
    style="text-decoration:none;"
    aria-label="NPC OMNIVERSE Home"
>
    🌌 <span>{site_name}</span>
</a>


<nav
    class="nav-links"
    aria-label="Main navigation"
>

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
    autocomplete="off"
    placeholder="Search NPCs, worlds..."
    aria-label="Search NPCs, worlds and quests"
>

</div>

</div>

</header>


<!-- ==========================================================
     LIVE SEARCH PANEL
=========================================================== -->

<div
    id="searchPanel"
    class="search-panel"
    aria-live="polite"
>

    <div id="searchResults"></div>

</div>


<!-- ==========================================================
     MAIN
=========================================================== -->

<main>


<!-- ==========================================================
     HERO
=========================================================== -->

<section
    id="home"
    class="hero"
>

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
    {tagline}
    {description}
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


<div
    class="hero-orb"
    aria-hidden="true"
>

<div class="orb"></div>

</div>

</div>

</section>


<!-- ==========================================================
     STATS
=========================================================== -->

<div class="container">

<div class="stats">

{stats_html}

</div>

</div>


<!-- ==========================================================
     CATEGORIES
=========================================================== -->

<section id="categories">

<div class="container">

<div class="section-header">

<div>

<h2>
    Explore the Omniverse
</h2>

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


<!-- ==========================================================
     NPCS
=========================================================== -->

<section id="npcs">

<div class="container">

<div class="section-header">

<div>

<h2>
    Featured NPCs
</h2>

<p>
    Characters waiting to be discovered.
</p>

<div id="searchStatus"></div>

</div>

</div>


<div
    class="npc-grid"
    id="npcGrid"
>

{npc_html}

</div>

</div>

</section>


<!-- ==========================================================
     WORLDS
=========================================================== -->

<section id="worlds">

<div class="container">

<div class="section-header">

<div>

<h2>
    Worlds
</h2>

<p>
    Explore different realities.
</p>

</div>

</div>


<div
    class="world-grid"
    id="worldGrid"
>

{worlds_html}

</div>

</div>

</section>


<!-- ==========================================================
     QUESTS
=========================================================== -->

<section id="quests">

<div class="container">

<div class="section-header">

<div>

<h2>
    Active Quests
</h2>

<p>
    Adventures across the Omniverse.
</p>

</div>

</div>


<div
    class="quest-grid"
    id="questGrid"
>

{quests_html}

</div>

</div>

</section>


</main>


<!-- ==========================================================
     FOOTER
=========================================================== -->

<footer>

<div class="container">

<strong>
    {site_name}
</strong>

<br>
<br>

Explore. Create. Discover.

<br>
<br>

<span>
    © {site_name}
</span>

</div>

</footer>


<!-- ==========================================================
     MODAL
=========================================================== -->

<div
    id="modal"
    class="modal"
    role="dialog"
    aria-modal="true"
    aria-labelledby="modalTitle"
    onclick="closeModal(event)"
>

<div class="modal-box">

<button
    class="close"
    aria-label="Close"
    onclick="closeModal()"
>
    ×
</button>

<div id="modalContent"></div>

</div>

</div>


<script>

/* ============================================================
   DATA
============================================================ */

const SITE_DATA = {data_json};


/* ============================================================
   ELEMENTS
============================================================ */

const searchInput =
    document.getElementById("searchInput");

const searchPanel =
    document.getElementById("searchPanel");

const searchResults =
    document.getElementById("searchResults");

const searchStatus =
    document.getElementById("searchStatus");


/* ============================================================
   NAVIGATION
============================================================ */

function scrollToSection(id) {{

    const element =
        document.getElementById(id);

    if (element) {{

        element.scrollIntoView({{
            behavior: "smooth",
            block: "start"
        }});

    }}

}}


/* ============================================================
   ESCAPE HTML
   Important for dynamically generated search results.
============================================================ */

function escapeHTML(value) {{

    return String(value)

        .replace(/&/g, "&amp;")

        .replace(/</g, "&lt;")

        .replace(/>/g, "&gt;")

        .replace(/"/g, "&quot;")

        .replace(/'/g, "&#039;");

}}


/* ============================================================
   NORMALIZE SEARCH
============================================================ */

function normalize(value) {{

    return String(value)

        .toLowerCase()

        .normalize("NFKD")

        .replace(/[^\w\s-]/g, "")

        .replace(/\s+/g, " ")

        .trim();

}}


/* ============================================================
   SEARCH SCORING
============================================================ */

/*
    IMPORTANT SEARCH PRIORITY:

    1. Exact NPC name
    2. NPC name starts with query
    3. NPC name contains query
    4. NPC role/world/description
    5. Exact World name
    6. World matches
    7. Quest matches

    This means when searching for:

        Kael Veyron

    Kael Veyron appears at the TOP.
*/

function scoreResult(item, query) {{

    const q =
        normalize(query);

    const name =
        normalize(item.name);

    const role =
        normalize(item.role || "");

    const world =
        normalize(item.world || "");

    const description =
        normalize(item.description || "");

    const difficulty =
        normalize(item.difficulty || "");

    const type =
        item.type;


    /* ========================================================
       NPC PRIORITY
    ======================================================== */

    if (type === "npc") {{

        if (name === q) {{
            return 10000;
        }}

        if (name.startsWith(q)) {{
            return 9000;
        }}

        if (name.includes(q)) {{
            return 8000;
        }}

        if (role.includes(q)) {{
            return 7000;
        }}

        if (world.includes(q)) {{
            return 6500;
        }}

        if (description.includes(q)) {{
            return 5000;
        }}

        return 0;
    }}


    /* ========================================================
       WORLD PRIORITY
    ======================================================== */

    if (type === "world") {{

        if (name === q) {{
            return 6000;
        }}

        if (name.startsWith(q)) {{
            return 5500;
        }}

        if (name.includes(q)) {{
            return 5000;
        }}

        if (world.includes(q)) {{
            return 4500;
        }}

        if (description.includes(q)) {{
            return 3500;
        }}

        return 0;
    }}


    /* ========================================================
       QUEST PRIORITY
    ======================================================== */

    if (type === "quest") {{

        if (name === q) {{
            return 4000;
        }}

        if (name.startsWith(q)) {{
            return 3800;
        }}

        if (name.includes(q)) {{
            return 3600;
        }}

        if (world.includes(q)) {{
            return 3000;
        }}

        if (difficulty.includes(q)) {{
            return 2500;
        }}

        return 0;
    }}


    return 0;
}}


/* ============================================================
   CREATE SEARCH DATA
============================================================ */

function getSearchItems() {{

    const items = [];


    SITE_DATA.featured_npcs.forEach(
        (npc, index) => {{

            items.push({{

                type: "npc",

                name: npc.name,

                role: npc.role,

                world: npc.world,

                description: npc.description,

                level: npc.level,

                index: index
            }});

        }}
    );


    SITE_DATA.worlds.forEach(
        world => {{

            items.push({{

                type: "world",

                name: world.name,

                role: world.type,

                world: world.name,

                description: world.description
            }});

        }}
    );


    SITE_DATA.quests.forEach(
        quest => {{

            items.push({{

                type: "quest",

                name: quest.title,

                role: quest.difficulty,

                world: quest.world,

                difficulty: quest.difficulty,

                description: quest.reward
            }});

        }}
    );


    return items;
}}


/* ============================================================
   SEARCH
============================================================ */

function searchSite() {{

    const query =
        searchInput.value.trim();


    const normalizedQuery =
        normalize(query);


    if (!normalizedQuery) {{

        searchPanel.classList.remove("active");

        searchResults.innerHTML = "";

        clearSearchFiltering();

        return;
    }}


    const items =
        getSearchItems();


    const results =
        items

            .map(item => ({{
                item: item,
                score:
                    scoreResult(
                        item,
                        normalizedQuery
                    )
            }}))

            .filter(result =>
                result.score > 0
            )

            .sort(
                (a, b) =>
                    b.score - a.score
            );


    renderSearchResults(
        results,
        normalizedQuery
    );


    applySearchFiltering(
        results,
        normalizedQuery
    );

}}


/* ============================================================
   RENDER SEARCH RESULTS
============================================================ */

function renderSearchResults(
    results,
    query
) {{

    searchPanel.classList.add("active");


    if (!results.length) {{

        searchResults.innerHTML = `

            <div class="no-results">

                <strong>
                    No results found
                </strong>

                <br><br>

                Try another NPC, world or quest.

            </div>
        `;

        return;
    }}


    let html = "";

    let lastType = "";


    results
        .slice(0, 20)
        .forEach(result => {{

            const item =
                result.item;


            if (item.type !== lastType) {{

                const label =
                    item.type === "npc"
                        ? "NPCs"
                        : item.type === "world"
                            ? "Worlds"
                            : "Quests";


                html += `

                    <div
                        class="search-section-title"
                    >
                        ${{label}}
                    </div>
                `;


                lastType =
                    item.type;
            }}


            if (item.type === "npc") {{

                html += `

                    <a
                        href="#npcs"
                        class="search-result"
                        onclick="selectNPCSearch(
                            ${{item.index}}
                        )"
                    >

                        <div
                            class="search-result-avatar"
                        >
                            ${{escapeHTML(
                                item.name.charAt(0)
                            )}}
                        </div>

                        <div
                            class="search-result-info"
                        >

                            <div
                                class="search-result-title"
                            >
                                ${{escapeHTML(
                                    item.name
                                )}}
                            </div>

                            <div
                                class="search-result-meta"
                            >
                                NPC ·
                                ${{escapeHTML(
                                    item.role
                                )}}
                                ·
                                🌌 ${{escapeHTML(
                                    item.world
                                )}}
                            </div>

                        </div>

                    </a>
                `;
            }}


            else if (item.type === "world") {{

                html += `

                    <a
                        href="#worlds"
                        class="search-result"
                        onclick="closeSearch()"
                    >

                        <div
                            class="search-result-avatar"
                        >
                            🌌
                        </div>

                        <div
                            class="search-result-info"
                        >

                            <div
                                class="search-result-title"
                            >
                                ${{escapeHTML(
                                    item.name
                                )}}
                            </div>

                            <div
                                class="search-result-meta"
                            >
                                World ·
                                ${{escapeHTML(
                                    item.role
                                )}}
                            </div>

                        </div>

                    </a>
                `;
            }}


            else {{

                html += `

                    <a
                        href="#quests"
                        class="search-result"
                        onclick="closeSearch()"
                    >

                        <div
                            class="search-result-avatar"
                        >
                            ⚔️
                        </div>

                        <div
                            class="search-result-info"
                        >

                            <div
                                class="search-result-title"
                            >
                                ${{escapeHTML(
                                    item.name
                                )}}
                            </div>

                            <div
                                class="search-result-meta"
                            >
                                Quest ·
                                ${{escapeHTML(
                                    item.world
                                )}}
                            </div>

                        </div>

                    </a>
                `;
            }}

        }});


    searchResults.innerHTML =
        html;
}}


/* ============================================================
   FILTER PAGE RESULTS
============================================================ */

function applySearchFiltering(
    results,
    query
) {{

    const resultNames =
        new Set(
            results.map(
                result =>
                    normalize(
                        result.item.name
                    )
            )
        );


    const npcCards =
        document.querySelectorAll(
            ".npc-card"
        );


    const worldCards =
        document.querySelectorAll(
            ".world-card"
        );


    const questCards =
        document.querySelectorAll(
            ".quest-card"
        );


    npcCards.forEach(card => {{

        const name =
            normalize(
                card.dataset.name
            );


        card.classList.toggle(
            "hidden",
            !resultNames.has(name)
        );

    }});


    worldCards.forEach(card => {{

        const name =
            normalize(
                card.dataset.name
            );


        card.classList.toggle(
            "hidden",
            !resultNames.has(name)
        );

    }});


    questCards.forEach(card => {{

        const name =
            normalize(
                card.dataset.name
            );


        card.classList.toggle(
            "hidden",
            !resultNames.has(name)
        );

    }});


    /* ========================================================
       MOVE BEST NPC TO TOP
    ======================================================== */

    const npcGrid =
        document.getElementById(
            "npcGrid"
        );


    const sortedNPCs =
        results

            .filter(
                result =>
                    result.item.type === "npc"
            )

            .sort(
                (a, b) =>
                    b.score - a.score
            );


    sortedNPCs.forEach(
        result => {{

            const card =
                document.querySelector(
                    `.npc-card[data-name="${{CSS.escape(
                        result.item.name
                    )}}"]`
                );


            if (card) {{
                npcGrid.appendChild(card);
            }}

        }}
    );


    const best =
        results[0];


    if (best) {{

        searchStatus.textContent =
            `${{results.length}} result(s) for "${{query}}"`;

    }}

}}


/* ============================================================
   CLEAR SEARCH FILTERING
============================================================ */

function clearSearchFiltering() {{

    document
        .querySelectorAll(
            ".npc-card, .world-card, .quest-card"
        )
        .forEach(card => {{

            card.classList.remove(
                "hidden"
            );

            card.classList.remove(
                "search-highlight"
            );

        }});


    searchStatus.textContent = "";

}}


/* ============================================================
   SELECT NPC FROM SEARCH
============================================================ */

function selectNPCSearch(index) {{

    const npc =
        SITE_DATA.featured_npcs[index];


    if (!npc) {{
        return;
    }}


    closeSearch();


    setTimeout(
        () => {{

            openNPC(
                npc.name,
                npc.role,
                npc.world,
                npc.level,
                npc.description
            );

        }},
        250
    );
}}


/* ============================================================
   CLOSE SEARCH
============================================================ */

function closeSearch() {{

    searchPanel.classList.remove(
        "active"
    );
}}


/* ============================================================
   NPC MODAL
============================================================ */

function openNPC(
    name,
    role,
    world,
    level,
    description
) {{

    const safeName =
        escapeHTML(name);

    const safeRole =
        escapeHTML(role);

    const safeWorld =
        escapeHTML(world);

    const safeLevel =
        escapeHTML(level);

    const safeDescription =
        escapeHTML(description);


    document.getElementById(
        "modalContent"
    ).innerHTML = `

        <h2 id="modalTitle">
            ${{safeName}}
        </h2>

        <p>
            ${{safeDescription}}
        </p>

        <div class="modal-meta">

            <strong>
                Role:
            </strong>

            ${{safeRole}}

            <br><br>

            <strong>
                World:
            </strong>

            🌌 ${{safeWorld}}

            <br><br>

            <strong>
                Level:
            </strong>

            ${{safeLevel}}

        </div>
    `;


    document
        .getElementById("modal")
        .classList.add("active");

}}


/* ============================================================
   RANDOM NPC
============================================================ */

function randomNPC() {{

    const npcs =
        SITE_DATA.featured_npcs;


    const npc =
        npcs[
            Math.floor(
                Math.random() *
                npcs.length
            )
        ];


    openNPC(
        npc.name,
        npc.role,
        npc.world,
        npc.level,
        npc.description
    );
}}


/* ============================================================
   CATEGORY
============================================================ */

function showCategory(category) {{

    openModal(
        category,
        `Explore the ${{escapeHTML(
            category
        )}} section of NPC OMNIVERSE.`
    );
}}


/* ============================================================
   GENERIC MODAL
============================================================ */

function openModal(
    title,
    content
) {{

    document.getElementById(
        "modalContent"
    ).innerHTML = `

        <h2 id="modalTitle">
            ${{escapeHTML(title)}}
        </h2>

        <p>
            ${{content}}
        </p>
    `;


    document
        .getElementById("modal")
        .classList.add("active");
}}


/* ============================================================
   CLOSE MODAL
============================================================ */

function closeModal(event) {{

    if (
        !event ||
        event.target.id === "modal" ||
        event.target.classList.contains("close")
    ) {{

        document
            .getElementById("modal")
            .classList.remove("active");
    }}
}}


/* ============================================================
   SEARCH EVENTS
============================================================ */

searchInput.addEventListener(
    "input",
    searchSite
);


searchInput.addEventListener(
    "focus",
    () => {{

        if (
            searchInput.value.trim()
        ) {{
            searchSite();
        }}

    }}
);


/* ============================================================
   CLICK OUTSIDE SEARCH
============================================================ */

document.addEventListener(
    "click",
    event => {{

        const search =
            document.querySelector(
                ".search"
            );


        if (
            !search.contains(event.target) &&
            !searchPanel.contains(event.target)
        ) {{

            closeSearch();

        }}

    }}
);


/* ============================================================
   KEYBOARD
============================================================ */

document.addEventListener(
    "keydown",
    event => {{

        if (event.key === "Escape") {{

            document
                .getElementById("modal")
                .classList.remove(
                    "active"
                );

            closeSearch();

        }}


        /* ====================================================
           CTRL + K / COMMAND + K
        ==================================================== */

        if (
            (event.ctrlKey ||
             event.metaKey) &&
            event.key.toLowerCase() === "k"
        ) {{

            event.preventDefault();

            searchInput.focus();

            searchInput.select();

        }}

    }}
);


/* ============================================================
   INITIALIZATION
============================================================ */

console.log(
    "NPC OMNIVERSE loaded."
);

console.log(
    "NPC search priority enabled."
);

</script>


</body>

</html>
"""


# ============================================================
# ROBOTS.TXT
# ============================================================

def build_robots(data):

    base_url = data["url"].rstrip("/")

    return f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""


# ============================================================
# SITEMAP
# ============================================================

def build_sitemap(data):

    base_url = data["url"].rstrip("/")

    urls = [
        "/",
        "/#home",
        "/#categories",
        "/#npcs",
        "/#worlds",
        "/#quests"
    ]

    entries = ""

    for url in urls:

        entries += f"""
    <url>
        <loc>{html.escape(base_url + url)}</loc>
    </url>
"""


    return f"""<?xml version="1.0" encoding="UTF-8"?>

<urlset
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
>
{entries}
</urlset>
"""


# ============================================================
# MAIN
# ============================================================

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    # --------------------------------------------------------
    # index.html
    # --------------------------------------------------------

    OUTPUT_FILE.write_text(
        build_html(SITE_DATA),
        encoding="utf-8"
    )


    # --------------------------------------------------------
    # robots.txt
    # --------------------------------------------------------

    ROBOTS_FILE.write_text(
        build_robots(SITE_DATA),
        encoding="utf-8"
    )


    # --------------------------------------------------------
    # sitemap.xml
    # --------------------------------------------------------

    SITEMAP_FILE.write_text(
        build_sitemap(SITE_DATA),
        encoding="utf-8"
    )


    print()
    print("=" * 65)
    print("NPC OMNIVERSE STATIC SITE CREATED")
    print("=" * 65)
    print()
    print(f"HTML:    {OUTPUT_FILE}")
    print(f"ROBOTS:  {ROBOTS_FILE}")
    print(f"SITEMAP: {SITEMAP_FILE}")
    print()
    print("Website:")
    print("https://npcbook.onrender.com/")
    print()
    print("Features:")
    print("  ✓ Static HTML")
    print("  ✓ No Flask")
    print("  ✓ No database")
    print("  ✓ SEO metadata")
    print("  ✓ Open Graph")
    print("  ✓ Twitter metadata")
    print("  ✓ JSON-LD structured data")
    print("  ✓ robots.txt")
    print("  ✓ sitemap.xml")
    print("  ✓ Responsive design")
    print("  ✓ NPC-first search ranking")
    print("  ✓ Exact NPC name gets highest priority")
    print("  ✓ NPC partial matches appear before other content")
    print("  ✓ Ctrl + K search shortcut")
    print()
    print("Search priority:")
    print("  1. Exact NPC name")
    print("  2. NPC name starts with search")
    print("  3. NPC name contains search")
    print("  4. NPC role/world/description")
    print("  5. World matches")
    print("  6. Quest matches")
    print()
    print("No server required for the generated site.")
    print()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()
