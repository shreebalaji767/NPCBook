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
# Generates:
#     site/index.html
#     site/robots.txt
#     site/sitemap.xml
#     site/site.webmanifest
#
# No Flask
# No database
# No server
# ============================================================


OUTPUT_DIR = Path("site")
OUTPUT_FILE = OUTPUT_DIR / "index.html"
ROBOTS_FILE = OUTPUT_DIR / "robots.txt"
SITEMAP_FILE = OUTPUT_DIR / "sitemap.xml"
MANIFEST_FILE = OUTPUT_DIR / "site.webmanifest"


# ============================================================
# WEBSITE DATA
# ============================================================

SITE_DATA = {

    "name": "NPC OMNIVERSE",

    "tagline": "Explore. Create. Discover.",

    "description": (
        "NPC OMNIVERSE is an interactive universe of NPCs, "
        "worlds, quests, factions, lore and stories."
    ),

    "url": "https://npcbook.onrender.com/",

    "language": "en",

    "author": "NPC OMNIVERSE",

    "keywords": [
        "NPC",
        "NPCs",
        "NPC database",
        "fictional characters",
        "fictional NPCs",
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
    #
    # Add more NPCs here.
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
    return html.escape(str(value), quote=True)


def slug(value):
    value = str(value).lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def search_text(*values):
    return " ".join(
        str(value).lower()
        for value in values
    )


# ============================================================
# SEO KEYWORDS
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

    result = []
    seen = set()

    for keyword in keywords:

        value = str(keyword).strip()
        key = value.lower()

        if key and key not in seen:
            seen.add(key)
            result.append(value)

    return ", ".join(result)


# ============================================================
# NPC HTML
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

        npc_json = json.dumps(
            {
                "name": npc["name"],
                "role": npc["role"],
                "world": npc["world"],
                "level": str(npc["level"]),
                "description": npc["description"]
            },
            ensure_ascii=False
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

                    <span class="npc-badge">
                        NPC
                    </span>

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
                    onclick='openNPC({json.dumps(npc["name"], ensure_ascii=False)}, {json.dumps(npc["role"], ensure_ascii=False)}, {json.dumps(npc["world"], ensure_ascii=False)}, {json.dumps(str(npc["level"]), ensure_ascii=False)}, {json.dumps(npc["description"], ensure_ascii=False)})'
                >
                    View Character →
                </button>

            </div>

        </article>
        """

    return output


# ============================================================
# WORLD HTML
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
# QUEST HTML
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
# CATEGORY HTML
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
                onclick='showCategory({json.dumps(category["name"], ensure_ascii=False)})'
            >
                Explore →
            </button>

        </article>
        """

    return output


# ============================================================
# STATS HTML
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
# JSON-LD
#
# IMPORTANT:
# This function fixes the original SyntaxError.
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
            "@id": base_url + "/#npc-directory",
            "name": "NPC Directory",
            "description": (
                "Explore NPC characters from NPC OMNIVERSE."
            ),
            "url": base_url + "/#npcs"
        },

        {
            "@type": "CollectionPage",
            "@id": base_url + "/#world-directory",
            "name": "World Directory",
            "description": (
                "Explore worlds and realities from NPC OMNIVERSE."
            ),
            "url": base_url + "/#worlds"
        },

        {
            "@type": "CollectionPage",
            "@id": base_url + "/#quest-directory",
            "name": "Quest Directory",
            "description": (
                "Explore quests and adventures from NPC OMNIVERSE."
            ),
            "url": base_url + "/#quests"
        }
    ]


    # --------------------------------------------------------
    # NPC structured data
    # --------------------------------------------------------

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
# MAIN HTML
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

    template = r"""<!DOCTYPE html>
<html lang="__LANGUAGE__">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<meta
    name="theme-color"
    content="#070b16"
>

<title>
    __SITE_NAME__ — Explore NPCs, Worlds, Quests & Stories
</title>

<meta
    name="description"
    content="__DESCRIPTION__"
>

<meta
    name="keywords"
    content="__KEYWORDS__"
>

<meta
    name="author"
    content="__AUTHOR__"
>

<meta
    name="robots"
    content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
>

<link
    rel="canonical"
    href="__CANONICAL__"
>

<link
    rel="manifest"
    href="/site.webmanifest"
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
    content="__SITE_NAME__ — Explore the Omniverse"
>

<meta
    property="og:description"
    content="__DESCRIPTION__"
>

<meta
    property="og:url"
    content="__CANONICAL__"
>

<meta
    property="og:site_name"
    content="__SITE_NAME__"
>

<meta
    property="og:locale"
    content="en_US"
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
    content="__SITE_NAME__ — Explore the Omniverse"
>

<meta
    name="twitter:description"
    content="__DESCRIPTION__"
>


<!-- ========================================================
     STRUCTURED DATA
========================================================= -->

<script type="application/ld+json">
__JSON_LD__
</script>


<style>

/* ============================================================
   RESET
============================================================ */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    min-height: 100vh;
    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    color: #f4f7ff;
    background:
        radial-gradient(
            circle at 20% 10%,
            rgba(88, 71, 255, 0.16),
            transparent 32%
        ),
        radial-gradient(
            circle at 80% 20%,
            rgba(0, 210, 255, 0.10),
            transparent 30%
        ),
        #070b16;

    line-height: 1.6;
}

body.modal-open {
    overflow: hidden;
}

button,
input {
    font: inherit;
}

button {
    cursor: pointer;
}

a {
    color: inherit;
    text-decoration: none;
}


/* ============================================================
   HEADER
============================================================ */

.site-header {
    position: sticky;
    top: 0;
    z-index: 1000;

    backdrop-filter: blur(20px);

    background: rgba(7, 11, 22, 0.88);

    border-bottom:
        1px solid
        rgba(255, 255, 255, 0.08);
}

.header-inner {
    width: min(1400px, calc(100% - 32px));
    min-height: 76px;
    margin: auto;

    display: flex;
    align-items: center;
    gap: 20px;
}

.logo {
    display: flex;
    align-items: center;
    gap: 11px;

    min-width: max-content;
}

.logo-mark {
    width: 42px;
    height: 42px;

    display: grid;
    place-items: center;

    border-radius: 14px;

    background:
        linear-gradient(
            135deg,
            #735cff,
            #18c8ff
        );

    box-shadow:
        0 10px 35px
        rgba(71, 117, 255, 0.25);
}

.logo-text {
    font-size: 16px;
    font-weight: 900;
    letter-spacing: 0.05em;
}

.logo-sub {
    color: #7f8ba9;
    font-size: 10px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}


/* ============================================================
   SEARCH
============================================================ */

.search {
    position: relative;
    flex: 1;
    max-width: 620px;
    margin-left: auto;
}

.search-box {
    display: flex;
    align-items: center;
    gap: 10px;

    min-height: 46px;

    padding: 0 12px;

    border:
        1px solid
        rgba(255, 255, 255, 0.10);

    border-radius: 15px;

    background:
        rgba(255, 255, 255, 0.045);

    transition:
        border-color 0.2s ease,
        background 0.2s ease,
        box-shadow 0.2s ease;
}

.search-box:focus-within {
    border-color:
        rgba(114, 92, 255, 0.75);

    background:
        rgba(255, 255, 255, 0.07);

    box-shadow:
        0 0 0 4px
        rgba(114, 92, 255, 0.10);
}

.search-icon {
    color: #8590aa;
    font-size: 18px;
}

.search-input {
    width: 100%;
    min-width: 0;

    border: 0;
    outline: 0;

    color: #fff;
    background: transparent;
}

.search-input::placeholder {
    color: #68748e;
}

.search-shortcut {
    flex: none;

    padding: 3px 7px;

    border:
        1px solid
        rgba(255, 255, 255, 0.10);

    border-radius: 7px;

    color: #78849d;
    font-size: 11px;
}

.search-clear {
    display: none;

    width: 30px;
    height: 30px;

    border: 0;
    border-radius: 9px;

    color: #aab4c9;
    background: rgba(255, 255, 255, 0.06);
}

.search-clear.visible {
    display: grid;
    place-items: center;
}


/* ============================================================
   SEARCH RESULTS PANEL
============================================================ */

.search-panel {
    position: absolute;

    left: 0;
    right: 0;
    top: calc(100% + 10px);

    display: none;

    max-height: 70vh;
    overflow-y: auto;

    padding: 10px;

    border:
        1px solid
        rgba(255, 255, 255, 0.10);

    border-radius: 18px;

    background:
        rgba(10, 15, 29, 0.98);

    box-shadow:
        0 30px 80px
        rgba(0, 0, 0, 0.45);

    z-index: 2000;
}

.search-panel.active {
    display: block;
}

.search-status {
    padding: 9px 10px 7px;

    color: #7e8aa4;

    font-size: 12px;
}

.search-section-title {
    padding:
        12px
        10px
        6px;

    color: #7d8aff;

    font-size: 11px;
    font-weight: 900;

    letter-spacing: 0.13em;
    text-transform: uppercase;
}

.search-result {
    display: flex;
    align-items: center;
    gap: 12px;

    padding: 10px;

    border-radius: 13px;

    transition:
        background 0.15s ease,
        transform 0.15s ease;
}

.search-result:hover {
    background:
        rgba(255, 255, 255, 0.06);

    transform: translateX(2px);
}

.search-result-avatar {
    width: 42px;
    height: 42px;

    flex: none;

    display: grid;
    place-items: center;

    border-radius: 12px;

    color: #fff;
    background:
        linear-gradient(
            135deg,
            #735cff,
            #18c8ff
        );

    font-weight: 900;
}

.search-result-info {
    min-width: 0;
}

.search-result-title {
    font-weight: 800;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.search-result-meta {
    margin-top: 2px;

    color: #78849d;

    font-size: 12px;

    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.no-results {
    padding: 30px 16px;

    text-align: center;

    color: #8994aa;
}

.no-results strong {
    color: #fff;
}


/* ============================================================
   HERO
============================================================ */

.hero {
    position: relative;

    width: min(1400px, calc(100% - 32px));

    margin: 0 auto;

    padding:
        100px
        0
        70px;

    display: grid;
    grid-template-columns:
        minmax(0, 1.15fr)
        minmax(280px, 0.85fr);

    gap: 70px;

    align-items: center;
}

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;

    padding:
        7px
        12px;

    border:
        1px solid
        rgba(116, 93, 255, 0.25);

    border-radius: 999px;

    color: #9c91ff;

    background:
        rgba(116, 93, 255, 0.08);

    font-size: 11px;
    font-weight: 900;

    letter-spacing: 0.12em;
    text-transform: uppercase;
}

.hero h1 {
    margin-top: 22px;

    max-width: 850px;

    font-size:
        clamp(44px, 7vw, 86px);

    line-height: 0.98;

    letter-spacing: -0.055em;
}

.gradient-text {
    background:
        linear-gradient(
            110deg,
            #ffffff 10%,
            #9d91ff 48%,
            #48dfff 90%
        );

    -webkit-background-clip: text;
    background-clip: text;

    color: transparent;
}

.hero-description {
    max-width: 700px;

    margin-top: 24px;

    color: #8e9ab4;

    font-size:
        clamp(16px, 2vw, 19px);
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;

    gap: 12px;

    margin-top: 30px;
}

.primary-button,
.secondary-button {
    min-height: 48px;

    padding:
        0
        18px;

    border-radius: 13px;

    font-weight: 800;
}

.primary-button {
    border: 0;

    color: #fff;

    background:
        linear-gradient(
            135deg,
            #735cff,
            #28bff0
        );

    box-shadow:
        0 14px 35px
        rgba(83, 91, 255, 0.22);
}

.secondary-button {
    border:
        1px solid
        rgba(255, 255, 255, 0.10);

    color: #dbe2f3;

    background:
        rgba(255, 255, 255, 0.04);
}


/* ============================================================
   HERO ORB
============================================================ */

.hero-visual {
    min-height: 390px;

    display: grid;
    place-items: center;

    position: relative;
}

.orb {
    width:
        clamp(220px, 30vw, 360px);

    aspect-ratio: 1;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #d9faff 0%,
            #7e83ff 16%,
            #4534a6 38%,
            #111b46 67%,
            #080b16 72%
        );

    box-shadow:
        0 0 90px
        rgba(91, 95, 255, 0.35),

        inset
        -30px
        -30px
        70px
        rgba(0, 0, 0, 0.50);

    animation:
        floatOrb 7s ease-in-out infinite;
}

.orb::before,
.orb::after {
    content: "";

    position: absolute;

    border-radius: 50%;

    border:
        1px solid
        rgba(140, 160, 255, 0.25);

    transform: rotate(-20deg);
}

.orb::before {
    width: 120%;
    height: 45%;
}

.orb::after {
    width: 45%;
    height: 120%;
}

@keyframes floatOrb {
    0%,
    100% {
        transform: translateY(0) rotate(0deg);
    }

    50% {
        transform: translateY(-14px) rotate(4deg);
    }
}


/* ============================================================
   SECTION
============================================================ */

.section {
    width:
        min(1400px, calc(100% - 32px));

    margin: 0 auto;

    padding:
        65px
        0;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: end;

    gap: 20px;

    margin-bottom: 25px;
}

.section-kicker {
    color: #8277ff;

    font-size: 11px;
    font-weight: 900;

    letter-spacing: 0.15em;
    text-transform: uppercase;
}

.section-title {
    margin-top: 5px;

    font-size:
        clamp(27px, 4vw, 42px);

    letter-spacing: -0.035em;
}

.section-description {
    max-width: 570px;

    color: #7f8aa3;
}


/* ============================================================
   STATS
============================================================ */

.stats-grid {
    display: grid;

    grid-template-columns:
        repeat(4, minmax(0, 1fr));

    gap: 14px;
}

.stat-card {
    padding: 25px;

    border:
        1px solid
        rgba(255, 255, 255, 0.08);

    border-radius: 20px;

    background:
        rgba(255, 255, 255, 0.035);
}

.stat-number {
    font-size: 34px;
    font-weight: 950;
    letter-spacing: -0.04em;
}

.stat-label {
    margin-top: 4px;

    color: #78849d;

    font-size: 12px;
    font-weight: 800;

    text-transform: uppercase;
    letter-spacing: 0.1em;
}


/* ============================================================
   CARD GRIDS
============================================================ */

.category-grid,
.npc-grid,
.world-grid,
.quest-grid {
    display: grid;

    grid-template-columns:
        repeat(4, minmax(0, 1fr));

    gap: 16px;
}


/* ============================================================
   CATEGORY CARDS
============================================================ */

.category-card {
    padding: 24px;

    border:
        1px solid
        rgba(255, 255, 255, 0.08);

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.055),
            rgba(255,255,255,0.02)
        );

    transition:
        transform 0.2s ease,
        border-color 0.2s ease;
}

.category-card:hover,
.npc-card:hover,
.world-card:hover,
.quest-card:hover {
    transform: translateY(-4px);

    border-color:
        rgba(124, 105, 255, 0.35);
}

.category-icon {
    width: 52px;
    height: 52px;

    display: grid;
    place-items: center;

    margin-bottom: 18px;

    border-radius: 16px;

    background:
        rgba(114, 92, 255, 0.10);

    font-size: 25px;
}

.category-card h3 {
    font-size: 20px;
}

.category-card p {
    min-height: 78px;

    margin:
        8px
        0
        18px;

    color: #7f8aa3;

    font-size: 14px;
}


/* ============================================================
   NPC CARDS
============================================================ */

.npc-card {
    display: flex;
    gap: 16px;

    min-width: 0;

    padding: 20px;

    border:
        1px solid
        rgba(255, 255, 255, 0.08);

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.055),
            rgba(255,255,255,0.018)
        );

    transition:
        transform 0.2s ease,
        border-color 0.2s ease,
        opacity 0.2s ease;
}

.npc-avatar {
    width: 58px;
    height: 58px;

    flex: none;

    display: grid;
    place-items: center;

    border-radius: 17px;

    color: #fff;

    background:
        linear-gradient(
            135deg,
            #735cff,
            #18c8ff
        );

    font-size: 22px;
    font-weight: 950;

    box-shadow:
        0 10px 30px
        rgba(75, 90, 255, 0.20);
}

.npc-content {
    min-width: 0;
    flex: 1;
}

.npc-top {
    display: flex;
    justify-content: space-between;
    gap: 10px;

    margin-bottom: 8px;
}

.npc-badge,
.npc-level,
.world-type,
.difficulty {
    display: inline-block;

    padding:
        4px
        8px;

    border-radius: 999px;

    font-size: 9px;
    font-weight: 900;

    letter-spacing: 0.09em;
    text-transform: uppercase;
}

.npc-badge {
    color: #8e84ff;
    background: rgba(113, 92, 255, 0.10);
}

.npc-level {
    color: #73dfff;
    background: rgba(35, 198, 241, 0.08);
}

.npc-card h3,
.world-card h3,
.quest-card h3 {
    font-size: 20px;
    line-height: 1.2;
}

.npc-role {
    margin-top: 4px;

    color: #a298ff;

    font-size: 13px;
    font-weight: 800;
}

.npc-world {
    margin-top: 6px;

    color: #78849d;

    font-size: 12px;
}

.npc-card p {
    margin-top: 11px;

    color: #7f8aa3;

    font-size: 13px;
}


/* ============================================================
   BUTTON
============================================================ */

.card-button {
    width: 100%;

    min-height: 42px;

    margin-top: 16px;

    border:
        1px solid
        rgba(255, 255, 255, 0.09);

    border-radius: 11px;

    color: #e8ecf7;

    background:
        rgba(255, 255, 255, 0.035);

    font-size: 12px;
    font-weight: 850;

    transition:
        background 0.15s ease,
        border-color 0.15s ease;
}

.card-button:hover {
    background:
        rgba(114, 92, 255, 0.12);

    border-color:
        rgba(114, 92, 255, 0.30);
}


/* ============================================================
   WORLD CARDS
============================================================ */

.world-card,
.quest-card {
    padding: 22px;

    border:
        1px solid
        rgba(255, 255, 255, 0.08);

    border-radius: 20px;

    background:
        rgba(255, 255, 255, 0.035);

    transition:
        transform 0.2s ease,
        border-color 0.2s ease;
}

.world-symbol {
    width: 55px;
    height: 55px;

    display: grid;
    place-items: center;

    margin-bottom: 17px;

    border-radius: 16px;

    background:
        rgba(28, 196, 238, 0.08);

    font-size: 25px;
}

.world-type {
    color: #63d9f5;

    background:
        rgba(25, 190, 232, 0.08);
}

.world-card p {
    margin-top: 10px;

    color: #7f8aa3;

    font-size: 13px;
}

.world-info {
    margin-top: 18px;

    color: #a7b0c5;

    font-size: 12px;
    font-weight: 800;
}


/* ============================================================
   QUEST CARDS
============================================================ */

.quest-icon {
    width: 55px;
    height: 55px;

    display: grid;
    place-items: center;

    margin-bottom: 17px;

    border-radius: 16px;

    background:
        rgba(255, 116, 116, 0.08);

    font-size: 25px;
}

.difficulty {
    color: #ffb28d;

    background:
        rgba(255, 133, 96, 0.09);
}

.quest-card h3 {
    margin-top: 9px;
}

.quest-card p {
    margin-top: 8px;

    color: #7f8aa3;

    font-size: 13px;
}

.quest-reward {
    margin-top: 17px;

    color: #8ee7bc;

    font-size: 13px;
    font-weight: 900;
}


/* ============================================================
   SEARCH FILTERING
============================================================ */

.npc-card.hidden,
.world-card.hidden,
.quest-card.hidden {
    display: none;
}

.search-highlight {
    border-color:
        rgba(115, 92, 255, 0.70) !important;

    box-shadow:
        0 0 0 3px
        rgba(115, 92, 255, 0.08);
}


/* ============================================================
   MODAL
============================================================ */

.modal {
    position: fixed;
    inset: 0;

    display: none;

    place-items: center;

    padding: 20px;

    background:
        rgba(0, 0, 0, 0.72);

    backdrop-filter: blur(10px);

    z-index: 5000;
}

.modal.active {
    display: grid;
}

.modal-box {
    position: relative;

    width:
        min(620px, 100%);

    max-height: 85vh;
    overflow-y: auto;

    padding: 30px;

    border:
        1px solid
        rgba(255, 255, 255, 0.11);

    border-radius: 24px;

    background:
        #0c1221;

    box-shadow:
        0 40px 100px
        rgba(0, 0, 0, 0.55);
}

.modal-close {
    position: absolute;

    right: 18px;
    top: 18px;

    width: 36px;
    height: 36px;

    border: 0;
    border-radius: 10px;

    color: #aab4c8;

    background:
        rgba(255, 255, 255, 0.06);

    font-size: 18px;
}

.modal-box h2 {
    padding-right: 45px;

    font-size: 30px;
}

.modal-box p {
    margin-top: 15px;

    color: #8b96ad;
}

.modal-meta {
    margin-top: 25px;

    padding: 18px;

    border-radius: 15px;

    background:
        rgba(255, 255, 255, 0.04);

    color: #a9b3c8;

    font-size: 14px;
}

.modal-meta strong {
    color: #fff;
}


/* ============================================================
   FOOTER
============================================================ */

.footer {
    width:
        min(1400px, calc(100% - 32px));

    margin: auto;

    padding:
        50px
        0
        40px;

    border-top:
        1px solid
        rgba(255, 255, 255, 0.07);

    color: #68748e;

    font-size: 12px;
}

.footer-inner {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width: 1100px) {

    .hero {
        grid-template-columns: 1fr;

        padding-top: 70px;

        gap: 30px;
    }

    .hero-visual {
        min-height: 300px;
    }

    .category-grid,
    .npc-grid,
    .world-grid,
    .quest-grid {
        grid-template-columns:
            repeat(2, minmax(0, 1fr));
    }

    .stats-grid {
        grid-template-columns:
            repeat(2, minmax(0, 1fr));
    }
}


@media (max-width: 760px) {

    .header-inner {
        width:
            min(100% - 20px, 1400px);

        min-height: 70px;

        flex-wrap: wrap;

        padding:
            10px
            0;
    }

    .logo {
        flex: 1;
    }

    .logo-text {
        font-size: 14px;
    }

    .search {
        order: 3;

        flex-basis: 100%;

        max-width: none;

        margin: 0;
    }

    .search-shortcut {
        display: none;
    }

    .hero {
        width:
            min(100% - 20px, 1400px);

        padding:
            60px
            0
            40px;
    }

    .hero h1 {
        font-size:
            clamp(42px, 14vw, 68px);
    }

    .section {
        width:
            min(100% - 20px, 1400px);

        padding:
            45px
            0;
    }

    .section-header {
        align-items: start;

        flex-direction: column;
    }

    .category-grid,
    .npc-grid,
    .world-grid,
    .quest-grid {
        grid-template-columns: 1fr;
    }

    .stats-grid {
        grid-template-columns:
            repeat(2, minmax(0, 1fr));
    }

    .stat-card {
        padding: 18px;
    }

    .stat-number {
        font-size: 27px;
    }

    .footer {
        width:
            min(100% - 20px, 1400px);
    }

    .footer-inner {
        flex-direction: column;
    }
}


@media (max-width: 440px) {

    .stats-grid {
        grid-template-columns: 1fr;
    }

    .npc-card {
        flex-direction: column;
    }

    .npc-avatar {
        width: 52px;
        height: 52px;
    }

    .hero-actions {
        flex-direction: column;
    }

    .primary-button,
    .secondary-button {
        width: 100%;
    }
}

</style>

</head>


<body>


<!-- ========================================================
     HEADER
========================================================= -->

<header class="site-header">

    <div class="header-inner">

        <a
            href="#home"
            class="logo"
            aria-label="NPC OMNIVERSE Home"
        >

            <div class="logo-mark">
                ✦
            </div>

            <div>
                <div class="logo-text">
                    NPC OMNIVERSE
                </div>

                <div class="logo-sub">
                    Explore the Universe
                </div>
            </div>

        </a>


        <div class="search">

            <div class="search-box">

                <span class="search-icon">
                    ⌕
                </span>

                <input
                    id="searchInput"
                    class="search-input"
                    type="search"
                    autocomplete="off"
                    spellcheck="false"
                    placeholder="Search NPCs, worlds, quests..."
                    aria-label="Search NPCs, worlds and quests"
                >

                <span
                    id="searchShortcut"
                    class="search-shortcut"
                >
                    /
                </span>

                <button
                    id="searchClear"
                    class="search-clear"
                    type="button"
                    aria-label="Clear search"
                >
                    ×
                </button>

            </div>


            <div
                id="searchPanel"
                class="search-panel"
                role="region"
                aria-label="Search results"
            >

                <div
                    id="searchStatus"
                    class="search-status"
                ></div>

                <div
                    id="searchResults"
                ></div>

            </div>

        </div>

    </div>

</header>


<!-- ========================================================
     HERO
========================================================= -->

<main>

<section
    id="home"
    class="hero"
>

    <div>

        <span class="hero-eyebrow">
            ✦ THE NPC DATABASE
        </span>

        <h1>
            Welcome to the
            <span class="gradient-text">
                Omniverse.
            </span>
        </h1>

        <p class="hero-description">
            __TAGLINE__
            Discover NPCs, worlds, quests, factions,
            lore and stories from an ever-expanding
            fictional universe.
        </p>


        <div class="hero-actions">

            <a
                href="#npcs"
                class="primary-button"
                style="display:inline-flex;align-items:center;justify-content:center;"
            >
                Explore NPCs →
            </a>

            <button
                class="secondary-button"
                type="button"
                onclick="randomNPC()"
            >
                ✦ Random NPC
            </button>

        </div>

    </div>


    <div class="hero-visual">

        <div class="orb"></div>

    </div>

</section>


<!-- ========================================================
     STATS
========================================================= -->

<section class="section">

    <div class="stats-grid">

        __STATS__

    </div>

</section>


<!-- ========================================================
     CATEGORIES
========================================================= -->

<section
    id="categories"
    class="section"
>

    <div class="section-header">

        <div>

            <div class="section-kicker">
                Universe
            </div>

            <h2 class="section-title">
                Explore Everything
            </h2>

        </div>

        <p class="section-description">
            Navigate through different parts of
            the NPC OMNIVERSE.
        </p>

    </div>


    <div class="category-grid">

        __CATEGORIES__

    </div>

</section>


<!-- ========================================================
     NPC DIRECTORY
========================================================= -->

<section
    id="npcs"
    class="section"
>

    <div class="section-header">

        <div>

            <div class="section-kicker">
                Characters
            </div>

            <h2 class="section-title">
                NPC Directory
            </h2>

        </div>

        <p class="section-description">
            Search for a character using their name,
            role, world or description.
        </p>

    </div>


    <div
        id="npcGrid"
        class="npc-grid"
    >

        __NPCS__

    </div>

</section>


<!-- ========================================================
     WORLDS
========================================================= -->

<section
    id="worlds"
    class="section"
>

    <div class="section-header">

        <div>

            <div class="section-kicker">
                Realities
            </div>

            <h2 class="section-title">
                Worlds
            </h2>

        </div>

        <p class="section-description">
            Explore the realities where NPCs,
            civilizations and stories exist.
        </p>

    </div>


    <div class="world-grid">

        __WORLDS__

    </div>

</section>


<!-- ========================================================
     QUESTS
========================================================= -->

<section
    id="quests"
    class="section"
>

    <div class="section-header">

        <div>

            <div class="section-kicker">
                Adventures
            </div>

            <h2 class="section-title">
                Quests
            </h2>

        </div>

        <p class="section-description">
            Missions, adventures and challenges
            from across the Omniverse.
        </p>

    </div>


    <div class="quest-grid">

        __QUESTS__

    </div>

</section>

</main>


<!-- ========================================================
     MODAL
========================================================= -->

<div
    id="modal"
    class="modal"
    onclick="closeModal(event)"
    role="dialog"
    aria-modal="true"
    aria-labelledby="modalTitle"
>

    <div class="modal-box">

        <button
            class="modal-close"
            type="button"
            onclick="closeModal()"
            aria-label="Close"
        >
            ×
        </button>

        <div id="modalContent"></div>

    </div>

</div>


<!-- ========================================================
     FOOTER
========================================================= -->

<footer class="footer">

    <div class="footer-inner">

        <div>
            © 2026 __SITE_NAME__
        </div>

        <div>
            Explore. Create. Discover.
        </div>

    </div>

</footer>


<script>

/* ============================================================
   SITE DATA
============================================================ */

const SITE_DATA = __SITE_DATA__;


/* ============================================================
   ELEMENTS
============================================================ */

const searchInput =
    document.getElementById("searchInput");

const searchClear =
    document.getElementById("searchClear");

const searchPanel =
    document.getElementById("searchPanel");

const searchResults =
    document.getElementById("searchResults");

const searchStatus =
    document.getElementById("searchStatus");

const modal =
    document.getElementById("modal");


/* ============================================================
   NORMALIZE SEARCH
============================================================ */

function normalize(value) {

    return String(value || "")
        .toLowerCase()
        .normalize("NFKD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/[^a-z0-9\s-]/g, " ")
        .replace(/\s+/g, " ")
        .trim();

}


/* ============================================================
   ESCAPE HTML
============================================================ */

function escapeHTML(value) {

    return String(value || "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}


/* ============================================================
   GET SEARCH ITEMS
============================================================ */

function getSearchItems() {

    const items = [];


    /*
       NPCS
    */

    SITE_DATA.featured_npcs.forEach(
        (npc, index) => {

            items.push({

                type: "npc",

                index: index,

                name: npc.name,

                role: npc.role,

                world: npc.world,

                description: npc.description,

                level: npc.level

            });

        }
    );


    /*
       WORLDS
    */

    SITE_DATA.worlds.forEach(
        (world, index) => {

            items.push({

                type: "world",

                index: index,

                name: world.name,

                role: world.type,

                world: world.name,

                description: world.description,

                population: world.population

            });

        }
    );


    /*
       QUESTS
    */

    SITE_DATA.quests.forEach(
        (quest, index) => {

            items.push({

                type: "quest",

                index: index,

                name: quest.title,

                role: quest.difficulty,

                world: quest.world,

                description: quest.reward

            });

        }
    );


    return items;

}


/* ============================================================
   SEARCH SCORE
============================================================

   NPC PRIORITY:

   10000  exact NPC name
    9000  NPC name starts with query
    8000  NPC name contains query
    6000  NPC role exact/starts/contains
    5000  NPC world match
    4000  NPC description match

   WORLD:

    3000  exact name
    2800  starts with name
    2500  contains name
    2200  type
    2000  description

   QUEST:

    1800  exact title
    1600  title starts with query
    1500  title contains query
    1300  world
    1200  difficulty
    1100  reward
============================================================ */

function scoreResult(item, query) {

    const name =
        normalize(item.name);

    const role =
        normalize(item.role);

    const world =
        normalize(item.world);

    const description =
        normalize(item.description);


    let score = 0;


    /* ========================================================
       NPC
    ======================================================== */

    if (item.type === "npc") {

        if (name === query) {

            score = 10000;

        }

        else if (name.startsWith(query)) {

            score = 9000;

        }

        else if (name.includes(query)) {

            score = 8000;

        }

        else if (role === query) {

            score = 6500;

        }

        else if (role.startsWith(query)) {

            score = 6200;

        }

        else if (role.includes(query)) {

            score = 6000;

        }

        else if (world === query) {

            score = 5500;

        }

        else if (world.startsWith(query)) {

            score = 5300;

        }

        else if (world.includes(query)) {

            score = 5000;

        }

        else if (description.includes(query)) {

            score = 4000;

        }

    }


    /* ========================================================
       WORLD
    ======================================================== */

    else if (item.type === "world") {

        if (name === query) {

            score = 3000;

        }

        else if (name.startsWith(query)) {

            score = 2800;

        }

        else if (name.includes(query)) {

            score = 2500;

        }

        else if (role === query) {

            score = 2300;

        }

        else if (role.includes(query)) {

            score = 2200;

        }

        else if (description.includes(query)) {

            score = 2000;

        }

    }


    /* ========================================================
       QUEST
    ======================================================== */

    else if (item.type === "quest") {

        if (name === query) {

            score = 1800;

        }

        else if (name.startsWith(query)) {

            score = 1600;

        }

        else if (name.includes(query)) {

            score = 1500;

        }

        else if (world.includes(query)) {

            score = 1300;

        }

        else if (role.includes(query)) {

            score = 1200;

        }

        else if (description.includes(query)) {

            score = 1100;

        }

    }


    /*
       Small bonus for words.
    */

    if (
        score > 0 &&
        name.split(" ").includes(query)
    ) {

        score += 50;

    }


    return score;

}


/* ============================================================
   SEARCH
============================================================ */

function searchSite() {

    const query =
        searchInput.value.trim();

    const normalizedQuery =
        normalize(query);


    updateClearButton();


    if (!normalizedQuery) {

        closeSearch();

        clearSearchFiltering();

        return;

    }


    const items =
        getSearchItems();


    let results =
        items
            .map(item => ({

                item: item,

                score:
                    scoreResult(
                        item,
                        normalizedQuery
                    )

            }))
            .filter(result =>
                result.score > 0
            );


    /*
       IMPORTANT:

       If an NPC name matches, NPC name
       results stay above world/quest results.

       This is an explicit NPC-first rule.
    */

    const npcNameMatches =
        results.filter(result => {

            if (result.item.type !== "npc") {
                return false;
            }

            const name =
                normalize(
                    result.item.name
                );

            return (
                name === normalizedQuery ||
                name.startsWith(normalizedQuery) ||
                name.includes(normalizedQuery)
            );

        });


    if (npcNameMatches.length) {

        results.sort((a, b) => {

            const aNpc =
                a.item.type === "npc";

            const bNpc =
                b.item.type === "npc";


            if (aNpc !== bNpc) {

                return bNpc - aNpc;

            }


            return b.score - a.score;

        });

    }

    else {

        results.sort(
            (a, b) =>
                b.score - a.score
        );

    }


    renderSearchResults(
        results,
        normalizedQuery
    );


    applySearchFiltering(
        results,
        normalizedQuery
    );

}


/* ============================================================
   RENDER SEARCH RESULTS
============================================================ */

function renderSearchResults(
    results,
    query
) {

    searchPanel.classList.add("active");


    if (!results.length) {

        searchStatus.textContent =
            `No results for "${query}"`;

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

    }


    searchStatus.textContent =
        `${results.length} result(s) for "${query}"`;


    let output = "";

    let lastType = "";


    results
        .slice(0, 25)
        .forEach(result => {

            const item =
                result.item;


            /*
               Section heading
            */

            if (item.type !== lastType) {

                const label =
                    item.type === "npc"
                        ? "NPCs"
                        : item.type === "world"
                            ? "Worlds"
                            : "Quests";


                output += `

                    <div class="search-section-title">
                        ${label}
                    </div>

                `;


                lastType =
                    item.type;

            }


            /*
               NPC
            */

            if (item.type === "npc") {

                output += `

                    <a
                        href="#npcs"
                        class="search-result"
                        onclick="selectNPCSearch(${item.index}); return false;"
                    >

                        <div
                            class="search-result-avatar"
                        >
                            ${escapeHTML(
                                item.name.charAt(0)
                            )}
                        </div>

                        <div
                            class="search-result-info"
                        >

                            <div
                                class="search-result-title"
                            >
                                ${escapeHTML(
                                    item.name
                                )}
                            </div>

                            <div
                                class="search-result-meta"
                            >
                                NPC ·
                                ${escapeHTML(
                                    item.role
                                )}
                                ·
                                🌌
                                ${escapeHTML(
                                    item.world
                                )}
                            </div>

                        </div>

                    </a>

                `;

            }


            /*
               WORLD
            */

            else if (item.type === "world") {

                output += `

                    <a
                        href="#worlds"
                        class="search-result"
                        onclick="selectWorldSearch(${item.index}); return false;"
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
                                ${escapeHTML(
                                    item.name
                                )}
                            </div>

                            <div
                                class="search-result-meta"
                            >
                                World ·
                                ${escapeHTML(
                                    item.role
                                )}
                            </div>

                        </div>

                    </a>

                `;

            }


            /*
               QUEST
            */

            else {

                output += `

                    <a
                        href="#quests"
                        class="search-result"
                        onclick="selectQuestSearch(${item.index}); return false;"
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
                                ${escapeHTML(
                                    item.name
                                )}
                            </div>

                            <div
                                class="search-result-meta"
                            >
                                Quest ·
                                ${escapeHTML(
                                    item.world
                                )}
                            </div>

                        </div>

                    </a>

                `;

            }

        });


    searchResults.innerHTML =
        output;

}


/* ============================================================
   FILTER PAGE CARDS
============================================================ */

function applySearchFiltering(
    results,
    query
) {

    const resultNames =
        new Set(
            results.map(
                result =>
                    normalize(
                        result.item.name
                    )
            )
        );


    /*
       NPC CARDS
    */

    document
        .querySelectorAll(".npc-card")
        .forEach(card => {

            const name =
                normalize(
                    card.dataset.name
                );

            card.classList.toggle(
                "hidden",
                !resultNames.has(name)
            );

        });


    /*
       WORLD CARDS
    */

    document
        .querySelectorAll(".world-card")
        .forEach(card => {

            const name =
                normalize(
                    card.dataset.name
                );

            card.classList.toggle(
                "hidden",
                !resultNames.has(name)
            );

        });


    /*
       QUEST CARDS
    */

    document
        .querySelectorAll(".quest-card")
        .forEach(card => {

            const name =
                normalize(
                    card.dataset.name
                );

            card.classList.toggle(
                "hidden",
                !resultNames.has(name)
            );

        });


    /*
       Move NPC matches according to score.

       This means if the user searches:

           Kael

       Kael Veyron appears first inside
       the NPC grid as well.
    */

    const npcGrid =
        document.getElementById(
            "npcGrid"
        );


    if (npcGrid) {

        const npcResults =
            results
                .filter(
                    result =>
                        result.item.type === "npc"
                )
                .sort(
                    (a, b) =>
                        b.score - a.score
                );


        npcResults.forEach(result => {

            const card =
                document.querySelector(
                    `.npc-card[data-index="${result.item.index}"]`
                );


            if (card) {

                npcGrid.appendChild(card);

                card.classList.add(
                    "search-highlight"
                );

            }

        });

    }

}


/* ============================================================
   CLEAR FILTERING
============================================================ */

function clearSearchFiltering() {

    document
        .querySelectorAll(
            ".npc-card, .world-card, .quest-card"
        )
        .forEach(card => {

            card.classList.remove(
                "hidden"
            );

            card.classList.remove(
                "search-highlight"
            );

        });


    searchStatus.textContent = "";

}


/* ============================================================
   SELECT NPC
============================================================ */

function selectNPCSearch(index) {

    const npc =
        SITE_DATA.featured_npcs[index];


    if (!npc) {
        return;
    }


    closeSearch();

    clearSearchFiltering();


    const card =
        document.querySelector(
            `.npc-card[data-index="${index}"]`
        );


    if (card) {

        card.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

        card.classList.add(
            "search-highlight"
        );

    }


    setTimeout(() => {

        openNPC(
            npc.name,
            npc.role,
            npc.world,
            npc.level,
            npc.description
        );

    }, 350);

}


/* ============================================================
   SELECT WORLD
============================================================ */

function selectWorldSearch(index) {

    closeSearch();

    clearSearchFiltering();


    const cards =
        document.querySelectorAll(
            ".world-card"
        );

    const card =
        cards[index];


    if (card) {

        card.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

        card.classList.add(
            "search-highlight"
        );

    }

}


/* ============================================================
   SELECT QUEST
============================================================ */

function selectQuestSearch(index) {

    closeSearch();

    clearSearchFiltering();


    const cards =
        document.querySelectorAll(
            ".quest-card"
        );

    const card =
        cards[index];


    if (card) {

        card.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

        card.classList.add(
            "search-highlight"
        );

    }

}


/* ============================================================
   CLOSE SEARCH
============================================================ */

function closeSearch() {

    searchPanel.classList.remove(
        "active"
    );

}


/* ============================================================
   CLEAR SEARCH
============================================================ */

function clearSearch() {

    searchInput.value = "";

    updateClearButton();

    closeSearch();

    clearSearchFiltering();

}


/* ============================================================
   CLEAR BUTTON
============================================================ */

function updateClearButton() {

    if (
        searchInput.value.trim()
    ) {

        searchClear.classList.add(
            "visible"
        );

    }

    else {

        searchClear.classList.remove(
            "visible"
        );

    }

}


/* ============================================================
   NPC MODAL
============================================================ */

function openNPC(
    name,
    role,
    world,
    level,
    description
) {

    document.getElementById(
        "modalContent"
    ).innerHTML = `

        <h2 id="modalTitle">
            ${escapeHTML(name)}
        </h2>

        <p>
            ${escapeHTML(description)}
        </p>

        <div class="modal-meta">

            <strong>
                Role:
            </strong>

            ${escapeHTML(role)}

            <br><br>

            <strong>
                World:
            </strong>

            🌌
            ${escapeHTML(world)}

            <br><br>

            <strong>
                Level:
            </strong>

            ${escapeHTML(level)}

        </div>

    `;


    modal.classList.add(
        "active"
    );

    document.body.classList.add(
        "modal-open"
    );

}


/* ============================================================
   RANDOM NPC
============================================================ */

function randomNPC() {

    const npcs =
        SITE_DATA.featured_npcs;


    if (!npcs.length) {
        return;
    }


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

}


/* ============================================================
   CATEGORY
============================================================ */

function showCategory(category) {

    openModal(
        category,
        `Explore the ${escapeHTML(
            category
        )} section of NPC OMNIVERSE.`
    );

}


/* ============================================================
   GENERIC MODAL
============================================================ */

function openModal(
    title,
    content
) {

    document.getElementById(
        "modalContent"
    ).innerHTML = `

        <h2 id="modalTitle">
            ${escapeHTML(title)}
        </h2>

        <p>
            ${content}
        </p>

    `;


    modal.classList.add(
        "active"
    );

    document.body.classList.add(
        "modal-open"
    );

}


/* ============================================================
   CLOSE MODAL
============================================================ */

function closeModal(event) {

    if (
        !event ||
        event.target === modal ||
        event.target.classList.contains(
            "modal-close"
        )
    ) {

        modal.classList.remove(
            "active"
        );

        document.body.classList.remove(
            "modal-open"
        );

    }

}


/* ============================================================
   SEARCH INPUT
============================================================ */

searchInput.addEventListener(
    "input",
    searchSite
);


searchInput.addEventListener(
    "focus",
    () => {

        if (
            searchInput.value.trim()
        ) {

            searchSite();

        }

    }
);


/* ============================================================
   SEARCH CLEAR
============================================================ */

searchClear.addEventListener(
    "click",
    () => {

        clearSearch();

        searchInput.focus();

    }
);


/* ============================================================
   CLICK OUTSIDE SEARCH
============================================================ */

document.addEventListener(
    "click",
    event => {

        const search =
            document.querySelector(
                ".search"
            );


        if (
            search &&
            !search.contains(
                event.target
            )
        ) {

            closeSearch();

        }

    }
);


/* ============================================================
   KEYBOARD
============================================================ */

document.addEventListener(
    "keydown",
    event => {

        /*
           ESCAPE
        */

        if (
            event.key === "Escape"
        ) {

            if (
                modal.classList.contains(
                    "active"
                )
            ) {

                modal.classList.remove(
                    "active"
                );

                document.body.classList.remove(
                    "modal-open"
                );

            }

            else {

                clearSearch();

            }

            return;

        }


        /*
           / SEARCH SHORTCUT

           Do not trigger while typing in
           another input or textarea.
        */

        if (
            event.key === "/" &&
            document.activeElement !== searchInput
        ) {

            const tag =
                document.activeElement.tagName;


            if (
                tag !== "INPUT" &&
                tag !== "TEXTAREA"
            ) {

                event.preventDefault();

                searchInput.focus();

            }

        }


        /*
           CTRL + K
           COMMAND + K
        */

        if (
            (event.ctrlKey ||
             event.metaKey) &&
            event.key.toLowerCase() === "k"
        ) {

            event.preventDefault();

            searchInput.focus();

            searchInput.select();

        }


        /*
           ENTER

           If a search result exists,
           selecting the first result happens
           when Enter is pressed.
        */

        if (
            event.key === "Enter" &&
            document.activeElement === searchInput
        ) {

            const first =
                searchResults.querySelector(
                    ".search-result"
                );


            if (first) {

                event.preventDefault();

                first.click();

            }

        }

    }
);


/* ============================================================
   INITIALIZATION
============================================================ */

updateClearButton();

console.log(
    "NPC OMNIVERSE loaded successfully."
);

console.log(
    "NPC-first search enabled."
);

console.log(
    "Exact NPC name matches receive highest priority."
);

</script>


</body>
</html>
"""


    # ========================================================
    # SAFE PLACEHOLDER REPLACEMENT
    #
    # We intentionally use .replace() instead of a giant
    # Python f-string. This prevents CSS/JavaScript braces
    # from causing Python syntax problems.
    # ========================================================

    replacements = {

        "__LANGUAGE__":
            esc(data["language"]),

        "__SITE_NAME__":
            site_name,

        "__DESCRIPTION__":
            description,

        "__KEYWORDS__":
            keywords,

        "__AUTHOR__":
            esc(data["author"]),

        "__CANONICAL__":
            canonical_url,

        "__TAGLINE__":
            tagline,

        "__STATS__":
            stats_html,

        "__CATEGORIES__":
            categories_html,

        "__NPCS__":
            npc_html,

        "__WORLDS__":
            worlds_html,

        "__QUESTS__":
            quests_html,

        "__JSON_LD__":
            json_ld,

        "__SITE_DATA__":
            data_json
    }


    for key, value in replacements.items():

        template = template.replace(
            key,
            value
        )


    return template


# ============================================================
# ROBOTS.TXT
# ============================================================

def build_robots(data):

    base_url = data["url"].rstrip("/")

    return (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {base_url}/sitemap.xml\n"
    )


# ============================================================
# SITEMAP
#
# IMPORTANT:
# URL fragments such as #home or #npcs are NOT separate
# crawlable URLs and should not be included in sitemap.xml.
# ============================================================

def build_sitemap(data):

    base_url = data["url"].rstrip("/")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
>
    <url>
        <loc>{html.escape(base_url + "/")}</loc>
    </url>
</urlset>
"""


# ============================================================
# WEB MANIFEST
# ============================================================

def build_manifest(data):

    manifest = {

        "name": data["name"],

        "short_name": "NPC OMNIVERSE",

        "description": data["description"],

        "start_url": "/",

        "display": "standalone",

        "background_color": "#070b16",

        "theme_color": "#070b16",

        "lang": data["language"],

        "icons": []

    }

    return json.dumps(
        manifest,
        ensure_ascii=False,
        indent=2
    )


# ============================================================
# VALIDATE DATA
# ============================================================

def validate_data(data):

    required_keys = [

        "name",
        "tagline",
        "description",
        "url",
        "language",
        "author",
        "keywords",
        "stats",
        "categories",
        "featured_npcs",
        "worlds",
        "quests"

    ]


    for key in required_keys:

        if key not in data:

            raise ValueError(
                f"Missing SITE_DATA key: {key}"
            )


    for index, npc in enumerate(
        data["featured_npcs"]
    ):

        required = [
            "name",
            "role",
            "world",
            "level",
            "description"
        ]

        for key in required:

            if key not in npc:

                raise ValueError(
                    f"NPC #{index + 1} is missing: {key}"
                )


    for index, world in enumerate(
        data["worlds"]
    ):

        required = [
            "name",
            "type",
            "population",
            "description"
        ]

        for key in required:

            if key not in world:

                raise ValueError(
                    f"World #{index + 1} is missing: {key}"
                )


    for index, quest in enumerate(
        data["quests"]
    ):

        required = [
            "title",
            "difficulty",
            "world",
            "reward"
        ]

        for key in required:

            if key not in quest:

                raise ValueError(
                    f"Quest #{index + 1} is missing: {key}"
                )


# ============================================================
# MAIN BUILD
# ============================================================

def main():

    print()
    print("=" * 70)
    print("NPC OMNIVERSE STATIC SITE GENERATOR")
    print("=" * 70)
    print()


    # --------------------------------------------------------
    # Validate
    # --------------------------------------------------------

    print("Checking website data...")

    validate_data(
        SITE_DATA
    )

    print("✓ Data validation passed")


    # --------------------------------------------------------
    # Create output directory
    # --------------------------------------------------------

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    # --------------------------------------------------------
    # index.html
    # --------------------------------------------------------

    print("Generating index.html...")

    html_content =
        build_html(SITE_DATA)

    OUTPUT_FILE.write_text(
        html_content,
        encoding="utf-8"
    )

    print(
        f"✓ Created {OUTPUT_FILE}"
    )


    # --------------------------------------------------------
    # robots.txt
    # --------------------------------------------------------

    print("Generating robots.txt...")

    ROBOTS_FILE.write_text(
        build_robots(SITE_DATA),
        encoding="utf-8"
    )

    print(
        f"✓ Created {ROBOTS_FILE}"
    )


    # --------------------------------------------------------
    # sitemap.xml
    # --------------------------------------------------------

    print("Generating sitemap.xml...")

    SITEMAP_FILE.write_text(
        build_sitemap(SITE_DATA),
        encoding="utf-8"
    )

    print(
        f"✓ Created {SITEMAP_FILE}"
    )


    # --------------------------------------------------------
    # webmanifest
    # --------------------------------------------------------

    print("Generating site.webmanifest...")

    MANIFEST_FILE.write_text(
        build_manifest(SITE_DATA),
        encoding="utf-8"
    )

    print(
        f"✓ Created {MANIFEST_FILE}"
    )


    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    print()
    print("-" * 70)
    print("BUILD COMPLETE")
    print("-" * 70)

    print()
    print(
        f"NPCs:       {len(SITE_DATA['featured_npcs'])}"
    )

    print(
        f"Worlds:     {len(SITE_DATA['worlds'])}"
    )

    print(
        f"Quests:     {len(SITE_DATA['quests'])}"
    )

    print(
        f"Categories: {len(SITE_DATA['categories'])}"
    )

    print()
    print("Generated files:")
    print(f"  ✓ {OUTPUT_FILE}")
    print(f"  ✓ {ROBOTS_FILE}")
    print(f"  ✓ {SITEMAP_FILE}")
    print(f"  ✓ {MANIFEST_FILE}")

    print()
    print("Search:")
    print("  ✓ Exact NPC name = highest priority")
    print("  ✓ NPC name starts-with = very high priority")
    print("  ✓ NPC name contains = high priority")
    print("  ✓ NPC role/world/description matching")
    print("  ✓ NPC results prioritized over worlds/quests")
    print("  ✓ Search result count")
    print("  ✓ No-results message")
    print("  ✓ Clear search button")
    print("  ✓ / keyboard shortcut")
    print("  ✓ Ctrl + K / Cmd + K shortcut")
    print("  ✓ Escape closes/clears search")
    print("  ✓ Mobile search")
    print("  ✓ NPC result opens character modal")

    print()
    print("SEO:")
    print("  ✓ Canonical URL")
    print("  ✓ Robots meta")
    print("  ✓ Open Graph")
    print("  ✓ Twitter metadata")
    print("  ✓ JSON-LD")
    print("  ✓ robots.txt")
    print("  ✓ sitemap.xml")
    print("  ✓ Web manifest")

    print()
    print("Website:")
    print(
        SITE_DATA["url"]
    )

    print()
    print("=" * 70)
    print()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()
