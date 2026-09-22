from pathlib import Path
import json
import html
import re


# ============================================================
# NPC OMNIVERSE
# STATIC SITE GENERATOR
# ============================================================

OUTPUT_DIR = Path("site")

OUTPUT_FILE = OUTPUT_DIR / "index.html"
ROBOTS_FILE = OUTPUT_DIR / "robots.txt"
SITEMAP_FILE = OUTPUT_DIR / "sitemap.xml"
MANIFEST_FILE = OUTPUT_DIR / "site.webmanifest"


# ============================================================
# SITE DATA
#
# THIS IS THE MAIN CONTENT AREA.
#
# Add/remove content here.
#
# Duplicate content is automatically removed during build.
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
        "characters",
        "fantasy characters",
        "game characters",
        "worlds",
        "quests",
        "factions",
        "lore",
        "stories",
        "omniverse",
        "fictional universe",
    ],

    "stats": {
        "NPCs": 12840,
        "Worlds": 426,
        "Quests": 1892,
        "Factions": 317,
    },

    "categories": [

        {
            "name": "Warriors",
            "icon": "⚔️",
            "description": (
                "Fighters, soldiers, champions and legendary warriors."
            ),
        },

        {
            "name": "Mages",
            "icon": "🔮",
            "description": (
                "Spellcasters, sorcerers, wizards and arcane beings."
            ),
        },

        {
            "name": "Assassins",
            "icon": "🗡️",
            "description": (
                "Stealth specialists, spies, killers and shadows."
            ),
        },

        {
            "name": "Adventurers",
            "icon": "🧭",
            "description": (
                "Explorers, travelers and heroes of unknown worlds."
            ),
        },

        {
            "name": "Warlords",
            "icon": "👑",
            "description": (
                "Rulers, generals and commanders of great armies."
            ),
        },

        {
            "name": "Mystics",
            "icon": "✨",
            "description": (
                "Ancient beings, prophets and mysterious entities."
            ),
        },

    ],

    "featured_npcs": [

        {
            "name": "Kael Veyron",
            "role": "Dimensional Wanderer",
            "world": "The Shattered Realms",
            "level": 87,
            "description": (
                "A mysterious traveler capable of crossing between "
                "fractured realities."
            ),
        },

        {
            "name": "Lyra Solenne",
            "role": "Starborn Mage",
            "world": "Aetheris",
            "level": 72,
            "description": (
                "A powerful mage who draws her magic from ancient stars."
            ),
        },

        {
            "name": "Drax Ironfall",
            "role": "Warlord",
            "world": "Ashen Dominion",
            "level": 94,
            "description": (
                "A ruthless commander who controls one of the largest "
                "armies in the Ashen Dominion."
            ),
        },

        {
            "name": "Mira Nightshade",
            "role": "Shadow Assassin",
            "world": "Nocturne",
            "level": 65,
            "description": (
                "A silent assassin who moves through darkness "
                "without leaving a trace."
            ),
        },

    ],

    "worlds": [

        {
            "name": "Aetheris",
            "type": "Fantasy",
            "population": "8.4B",
            "description": (
                "A vast magical world filled with ancient civilizations, "
                "floating cities and powerful magic."
            ),
        },

        {
            "name": "Nocturne",
            "type": "Dark Fantasy",
            "population": "2.1B",
            "description": (
                "A mysterious realm where shadows, monsters and forgotten "
                "kingdoms dominate the night."
            ),
        },

        {
            "name": "Ashen Dominion",
            "type": "War",
            "population": "14.7B",
            "description": (
                "A massive war-torn civilization ruled by powerful "
                "warlords and competing factions."
            ),
        },

        {
            "name": "The Shattered Realms",
            "type": "Multiverse",
            "population": "Unknown",
            "description": (
                "A collection of broken realities connected by unstable "
                "dimensional pathways."
            ),
        },

    ],

    "quests": [

        {
            "name": "The Lost Crown",
            "difficulty": "Legendary",
            "world": "Aetheris",
            "reward": "50,000 XP",
            "description": (
                "Recover an ancient crown lost beneath the ruins "
                "of an abandoned kingdom."
            ),
        },

        {
            "name": "Echoes of Nocturne",
            "difficulty": "Hard",
            "world": "Nocturne",
            "reward": "18,000 XP",
            "description": (
                "Investigate mysterious voices coming from the "
                "forgotten districts of Nocturne."
            ),
        },

        {
            "name": "The Iron Rebellion",
            "difficulty": "Extreme",
            "world": "Ashen Dominion",
            "reward": "75,000 XP",
            "description": (
                "Join the resistance against the Iron Dominion "
                "before the rebellion is destroyed."
            ),
        },

    ],
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


def normalize_text(value):
    """
    Normalize text for duplicate detection.

    Examples:

        "Kael Veyron"
        " kael   veyron "
        "KAEL VEYRON"

    are treated as the same value.
    """

    if value is None:
        return ""

    value = str(value)

    value = value.replace("\u00a0", " ")

    value = re.sub(r"\s+", " ", value)

    return value.strip().casefold()


def search_text(*values):
    return " ".join(
        str(value).lower()
        for value in values
        if value is not None
    )


def json_attr(value):
    return esc(
        json.dumps(
            value,
            ensure_ascii=False,
        )
    )


# ============================================================
# UNIQUE KEY
# ============================================================

def content_key(item, fields):
    """
    Create a normalized duplicate key.

    The same content with different capitalization or
    accidental spacing gets the same key.
    """

    return tuple(
        normalize_text(item.get(field, ""))
        for field in fields
    )


# ============================================================
# REMOVE DUPLICATES
# ============================================================

def remove_duplicate_items(items, fields):
    """
    Remove duplicate records.

    The FIRST occurrence is preserved.

    Example:

        Kael Veyron
        KAEL VEYRON
        kael   veyron

    are considered duplicates when name is used as a key.
    """

    result = []
    seen = set()

    for item in items or []:

        if not isinstance(item, dict):
            continue

        key = content_key(
            item,
            fields,
        )

        if key in seen:
            continue

        seen.add(key)
        result.append(dict(item))

    return result


# ============================================================
# ENSURE UNIQUE SLUGS
# ============================================================

def add_unique_ids(items, prefix):
    """
    Give every item a unique internal ID.

    Duplicate slugs are automatically suffixed:

        kael-veyron
        kael-veyron-2
        kael-veyron-3
    """

    result = []

    used = set()

    for item in items or []:

        item = dict(item)

        base = slug(
            item.get("name", "")
        )

        if not base:
            base = prefix

        candidate = base
        counter = 2

        while candidate in used:

            candidate = (
                f"{base}-{counter}"
            )

            counter += 1

        used.add(candidate)

        item["id"] = (
            f"{prefix}-{candidate}"
        )

        item["slug"] = candidate

        result.append(item)

    return result


# ============================================================
# CLEAN ALL CONTENT
# ============================================================

def clean_site_data(data):
    """
    Clean the complete site before generation.

    This is the main anti-duplication system.
    """

    cleaned = dict(data)

    # --------------------------------------------------------
    # CATEGORIES
    # --------------------------------------------------------

    categories = remove_duplicate_items(
        data.get("categories", []),
        [
            "name",
        ],
    )

    cleaned["categories"] = add_unique_ids(
        categories,
        "category",
    )

    # --------------------------------------------------------
    # NPCS
    #
    # Name is treated as the primary identity.
    #
    # This means two NPC records with the same name are
    # considered the same NPC even if other fields differ.
    # --------------------------------------------------------

    npcs = remove_duplicate_items(
        data.get("featured_npcs", []),
        [
            "name",
        ],
    )

    cleaned["featured_npcs"] = add_unique_ids(
        npcs,
        "npc",
    )

    # --------------------------------------------------------
    # WORLDS
    # --------------------------------------------------------

    worlds = remove_duplicate_items(
        data.get("worlds", []),
        [
            "name",
        ],
    )

    cleaned["worlds"] = add_unique_ids(
        worlds,
        "world",
    )

    # --------------------------------------------------------
    # QUESTS
    # --------------------------------------------------------

    quests = remove_duplicate_items(
        data.get("quests", []),
        [
            "name",
        ],
    )

    cleaned["quests"] = add_unique_ids(
        quests,
        "quest",
    )

    return cleaned


# ============================================================
# DUPLICATE REPORT
# ============================================================

def count_removed(original, cleaned, field):
    return max(
        0,
        len(original.get(field, []))
        -
        len(cleaned.get(field, []))
    )


def print_duplicate_report(original, cleaned):

    categories_removed = count_removed(
        original,
        cleaned,
        "categories",
    )

    npcs_removed = count_removed(
        original,
        cleaned,
        "featured_npcs",
    )

    worlds_removed = count_removed(
        original,
        cleaned,
        "worlds",
    )

    quests_removed = count_removed(
        original,
        cleaned,
        "quests",
    )

    total_removed = (
        categories_removed
        + npcs_removed
        + worlds_removed
        + quests_removed
    )

    print()
    print("CONTENT DUPLICATION CHECK")
    print("-" * 60)

    print(
        f"Duplicate categories removed : "
        f"{categories_removed}"
    )

    print(
        f"Duplicate NPCs removed        : "
        f"{npcs_removed}"
    )

    print(
        f"Duplicate worlds removed      : "
        f"{worlds_removed}"
    )

    print(
        f"Duplicate quests removed      : "
        f"{quests_removed}"
    )

    print(
        f"Total duplicates removed      : "
        f"{total_removed}"
    )

    print("-" * 60)


# ============================================================
# SEO KEYWORDS
# ============================================================

def generate_keywords(data):

    keywords = list(
        data.get(
            "keywords",
            [],
        )
    )

    for npc in data.get(
        "featured_npcs",
        [],
    ):

        keywords.extend(
            [
                npc.get("name", ""),
                npc.get("role", ""),
                npc.get("world", ""),
            ]
        )

    for world in data.get(
        "worlds",
        [],
    ):

        keywords.extend(
            [
                world.get("name", ""),
                world.get("type", ""),
            ]
        )

    for quest in data.get(
        "quests",
        [],
    ):

        keywords.extend(
            [
                quest.get("name", ""),
                quest.get("difficulty", ""),
                quest.get("world", ""),
            ]
        )

    result = []

    seen = set()

    for keyword in keywords:

        keyword = str(
            keyword
        ).strip()

        normalized = normalize_text(
            keyword
        )

        if not normalized:
            continue

        if normalized in seen:
            continue

        seen.add(normalized)
        result.append(keyword)

    return ", ".join(result)


# ============================================================
# STATS
# ============================================================

def build_stats_html(data):

    items = []

    for label, value in data.get(
        "stats",
        {},
    ).items():

        items.append(
            f"""
            <div class="stat-card">
                <div class="stat-number">{esc(value)}</div>
                <div class="stat-label">{esc(label)}</div>
            </div>
            """
        )

    return "\n".join(items)


# ============================================================
# CATEGORY HTML
# ============================================================

def build_category_html(data):

    cards = []

    for category in data.get(
        "categories",
        [],
    ):

        name = category.get(
            "name",
            "",
        )

        icon = category.get(
            "icon",
            "✦",
        )

        description = category.get(
            "description",
            "",
        )

        cards.append(
            f"""
            <article
                class="category-card"
                data-type="category"
                data-name="{esc(name)}"
                data-search="{esc(search_text(name, description))}"
            >

                <div class="category-icon">
                    {esc(icon)}
                </div>

                <div class="category-content">

                    <h3>
                        {esc(name)}
                    </h3>

                    <p>
                        {esc(description)}
                    </p>

                    <button
                        class="card-button"
                        type="button"
                        onclick="showCategory({json_attr(name)})"
                    >
                        Explore →
                    </button>

                </div>

            </article>
            """
        )

    return "\n".join(cards)


# ============================================================
# NPC HTML
# ============================================================

def build_npc_html(data):

    cards = []

    for npc in data.get(
        "featured_npcs",
        [],
    ):

        name = npc.get(
            "name",
            "",
        )

        role = npc.get(
            "role",
            "",
        )

        world = npc.get(
            "world",
            "",
        )

        level = npc.get(
            "level",
            "",
        )

        description = npc.get(
            "description",
            "",
        )

        searchable = search_text(
            name,
            role,
            world,
            level,
            description,
        )

        cards.append(
            f"""
            <article
                class="npc-card"
                data-type="npc"
                data-name="{esc(name)}"
                data-role="{esc(role)}"
                data-world="{esc(world)}"
                data-search="{esc(searchable)}"
            >

                <div class="card-top">

                    <div class="avatar">
                        {esc(name[:1].upper())}
                    </div>

                    <div class="level-badge">
                        LVL {esc(level)}
                    </div>

                </div>

                <div class="card-body">

                    <div class="card-type">
                        NPC
                    </div>

                    <h3>
                        {esc(name)}
                    </h3>

                    <div class="role">
                        {esc(role)}
                    </div>

                    <div class="world-name">
                        🌍 {esc(world)}
                    </div>

                    <p>
                        {esc(description)}
                    </p>

                    <button
                        class="card-button"
                        type="button"
                        onclick="openNPC(
                            {json_attr(name)},
                            {json_attr(role)},
                            {json_attr(world)},
                            {json_attr(str(level))},
                            {json_attr(description)}
                        )"
                    >
                        View Character →
                    </button>

                </div>

            </article>
            """
        )

    return "\n".join(cards)


# ============================================================
# WORLD HTML
# ============================================================

def build_world_html(data):

    cards = []

    for world in data.get(
        "worlds",
        [],
    ):

        name = world.get(
            "name",
            "",
        )

        world_type = world.get(
            "type",
            "",
        )

        population = world.get(
            "population",
            "",
        )

        description = world.get(
            "description",
            "",
        )

        searchable = search_text(
            name,
            world_type,
            population,
            description,
        )

        cards.append(
            f"""
            <article
                class="world-card"
                data-type="world"
                data-name="{esc(name)}"
                data-search="{esc(searchable)}"
            >

                <div class="world-symbol">
                    ◈
                </div>

                <div class="card-body">

                    <div class="card-type">
                        WORLD
                    </div>

                    <h3>
                        {esc(name)}
                    </h3>

                    <div class="world-meta">

                        <span>
                            {esc(world_type)}
                        </span>

                        <span>
                            {esc(population)}
                        </span>

                    </div>

                    <p>
                        {esc(description)}
                    </p>

                    <button
                        class="card-button"
                        type="button"
                        onclick="openWorld(
                            {json_attr(name)},
                            {json_attr(world_type)},
                            {json_attr(population)},
                            {json_attr(description)}
                        )"
                    >
                        Explore World →
                    </button>

                </div>

            </article>
            """
        )

    return "\n".join(cards)


# ============================================================
# QUEST HTML
# ============================================================

def build_quest_html(data):

    cards = []

    for quest in data.get(
        "quests",
        [],
    ):

        name = quest.get(
            "name",
            "",
        )

        difficulty = quest.get(
            "difficulty",
            "",
        )

        world = quest.get(
            "world",
            "",
        )

        reward = quest.get(
            "reward",
            "",
        )

        description = quest.get(
            "description",
            "",
        )

        searchable = search_text(
            name,
            difficulty,
            world,
            reward,
            description,
        )

        cards.append(
            f"""
            <article
                class="quest-card"
                data-type="quest"
                data-name="{esc(name)}"
                data-search="{esc(searchable)}"
            >

                <div class="quest-symbol">
                    ✦
                </div>

                <div class="card-body">

                    <div class="card-type">
                        QUEST
                    </div>

                    <h3>
                        {esc(name)}
                    </h3>

                    <div class="quest-meta">

                        <span>
                            {esc(difficulty)}
                        </span>

                        <span>
                            {esc(world)}
                        </span>

                    </div>

                    <p>
                        {esc(description)}
                    </p>

                    <div class="reward">
                        Reward:
                        {esc(reward)}
                    </div>

                    <button
                        class="card-button"
                        type="button"
                        onclick="openQuest(
                            {json_attr(name)},
                            {json_attr(difficulty)},
                            {json_attr(world)},
                            {json_attr(reward)},
                            {json_attr(description)}
                        )"
                    >
                        View Quest →
                    </button>

                </div>

            </article>
            """
        )

    return "\n".join(cards)


# ============================================================
# JSON-LD
# ============================================================

def build_json_ld(data):

    base_url = data[
        "url"
    ].rstrip("/")

    graph = [

        {
            "@type": "WebSite",
            "@id": base_url + "/#website",
            "url": base_url + "/",
            "name": data["name"],
            "description": data["description"],
            "inLanguage": data["language"],
        },

        {
            "@type": "WebPage",
            "@id": base_url + "/#webpage",
            "url": base_url + "/",
            "name": data["name"],
            "description": data["description"],
            "isPartOf": {
                "@id": base_url + "/#website"
            },
        },

        {
            "@type": "CollectionPage",
            "name": "NPC Directory",
            "description": (
                "Explore NPC characters from NPC OMNIVERSE."
            ),
            "url": base_url + "/#npcs",
        },

        {
            "@type": "CollectionPage",
            "name": "World Directory",
            "description": (
                "Explore worlds and realities from NPC OMNIVERSE."
            ),
            "url": base_url + "/#worlds",
        },

        {
            "@type": "CollectionPage",
            "name": "Quest Directory",
            "description": (
                "Explore quests and adventures from NPC OMNIVERSE."
            ),
            "url": base_url + "/#quests",
        },

    ]

    for npc in data.get(
        "featured_npcs",
        [],
    ):

        graph.append(
            {
                "@type": "Person",
                "@id": (
                    base_url
                    + "/#"
                    + npc.get("id", "")
                ),
                "name": npc.get(
                    "name",
                    "",
                ),
                "jobTitle": npc.get(
                    "role",
                    "",
                ),
                "description": npc.get(
                    "description",
                    "",
                ),
                "isPartOf": {
                    "@type": "CreativeWork",
                    "name": npc.get(
                        "world",
                        "",
                    ),
                },
            }
        )

    for world in data.get(
        "worlds",
        [],
    ):

        graph.append(
            {
                "@type": "Place",
                "@id": (
                    base_url
                    + "/#"
                    + world.get("id", "")
                ),
                "name": world.get(
                    "name",
                    "",
                ),
                "description": world.get(
                    "description",
                    "",
                ),
                "additionalType": world.get(
                    "type",
                    "",
                ),
            }
        )

    schema = {
        "@context": "https://schema.org",
        "@graph": graph,
    }

    return json.dumps(
        schema,
        ensure_ascii=False,
        indent=2,
    )


# ============================================================
# MAIN HTML
# ============================================================

def build_html(data):

    site_name = esc(
        data["name"]
    )

    tagline = esc(
        data["tagline"]
    )

    description = esc(
        data["description"]
    )

    canonical_url = esc(
        data["url"]
    )

    keywords = esc(
        generate_keywords(data)
    )

    stats_html = build_stats_html(
        data
    )

    categories_html = build_category_html(
        data
    )

    npc_html = build_npc_html(
        data
    )

    worlds_html = build_world_html(
        data
    )

    quests_html = build_quest_html(
        data
    )

    json_ld = build_json_ld(
        data
    )

    data_json = json.dumps(
        data,
        ensure_ascii=False,
    )

    return f"""<!DOCTYPE html>
<html lang="{esc(data["language"])}">

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
NPC OMNIVERSE — Explore NPCs, Worlds, Quests & Stories
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
    content="{site_name}"
>

<meta
    name="robots"
    content="index, follow, max-image-preview:large"
>

<link
    rel="canonical"
    href="{canonical_url}"
>


<meta
    property="og:type"
    content="website"
>

<meta
    property="og:title"
    content="NPC OMNIVERSE — Explore the Omniverse"
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


<meta
    name="twitter:card"
    content="summary_large_image"
>

<meta
    name="twitter:title"
    content="NPC OMNIVERSE — Explore the Omniverse"
>

<meta
    name="twitter:description"
    content="{description}"
>


<link
    rel="manifest"
    href="/site.webmanifest"
>


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
}}

body {{
    min-height: 100vh;

    background:
        radial-gradient(
            circle at top,
            #18213d 0%,
            #0c1020 35%,
            #070910 75%,
            #05060a 100%
        );

    color: #f4f7ff;

    font-family:
        Inter,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    line-height: 1.6;
}}

button,
input {{
    font: inherit;
}}

button {{
    cursor: pointer;
}}

a {{
    color: inherit;
    text-decoration: none;
}}

body::before {{
    content: "";

    position: fixed;

    inset: 0;

    pointer-events: none;

    opacity: .15;

    background-image:
        linear-gradient(
            rgba(255,255,255,.025) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(255,255,255,.025) 1px,
            transparent 1px
        );

    background-size: 40px 40px;

    z-index: -1;
}}


/* ============================================================
   HEADER
============================================================ */

.site-header {{
    position: sticky;

    top: 0;

    z-index: 1000;

    background:
        rgba(5,7,15,.90);

    backdrop-filter:
        blur(18px);

    border-bottom:
        1px solid
        rgba(255,255,255,.08);
}}

.header-inner {{
    width:
        min(1400px,94%);

    min-height: 74px;

    margin: auto;

    display: flex;

    align-items: center;

    gap: 22px;
}}

.logo {{
    display: flex;

    align-items: center;

    gap: 12px;

    font-size: 20px;

    font-weight: 900;

    letter-spacing: .08em;

    white-space: nowrap;
}}

.logo-mark {{
    width: 38px;
    height: 38px;

    display: grid;

    place-items: center;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            #6d5dfc,
            #00d4ff
        );

    box-shadow:
        0 0 30px
        rgba(79,115,255,.35);
}}

.logo-text {{
    background:
        linear-gradient(
            90deg,
            #fff,
            #8ddcff
        );

    -webkit-background-clip: text;

    background-clip: text;

    color: transparent;
}}


/* ============================================================
   SEARCH
============================================================ */

.header-search {{
    flex: 1;

    max-width: 680px;

    margin-left: auto;
}}

.search-box {{
    position: relative;
}}

.search-input {{
    width: 100%;

    height: 48px;

    padding:
        0 92px
        0 46px;

    border:
        1px solid
        rgba(255,255,255,.12);

    border-radius: 15px;

    outline: none;

    color: #fff;

    background:
        rgba(255,255,255,.055);
}}

.search-input::placeholder {{
    color: #8d96aa;
}}

.search-input:focus {{
    border-color:
        rgba(96,197,255,.65);

    background:
        rgba(255,255,255,.08);

    box-shadow:
        0 0 0 4px
        rgba(70,170,255,.08);
}}

.search-icon {{
    position: absolute;

    left: 15px;
    top: 50%;

    transform:
        translateY(-50%);

    color: #8d96aa;

    pointer-events: none;
}}

.clear-search {{
    position: absolute;

    right: 52px;
    top: 50%;

    transform:
        translateY(-50%);

    width: 30px;
    height: 30px;

    border: none;

    border-radius: 8px;

    background:
        rgba(255,255,255,.07);

    color: #b8c0d1;

    display: none;

    place-items: center;
}}

.search-key {{
    position: absolute;

    right: 13px;
    top: 50%;

    transform:
        translateY(-50%);

    padding:
        2px 6px;

    border:
        1px solid
        rgba(255,255,255,.12);

    border-radius: 6px;

    color: #7e879a;

    font-size: 11px;
}}


/* ============================================================
   NAV
============================================================ */

.header-nav {{
    display: flex;

    gap: 6px;
}}

.header-nav a {{
    padding:
        8px 10px;

    border-radius: 9px;

    color: #aeb7c9;

    font-size: 14px;
}}

.header-nav a:hover {{
    background:
        rgba(255,255,255,.06);

    color: white;
}}


/* ============================================================
   CONTAINER
============================================================ */

.container {{
    width:
        min(1400px,94%);

    margin: auto;
}}


/* ============================================================
   HERO
============================================================ */

.hero {{
    min-height: 590px;

    display: grid;

    grid-template-columns:
        1.15fr .85fr;

    gap: 50px;

    align-items: center;

    padding:
        90px 0 70px;
}}

.eyebrow {{
    display: inline-flex;

    padding:
        7px 12px;

    border:
        1px solid
        rgba(120,190,255,.18);

    border-radius: 999px;

    background:
        rgba(100,170,255,.06);

    color: #8ddcff;

    font-size: 12px;

    font-weight: 800;

    letter-spacing: .12em;

    margin-bottom: 22px;
}}

.hero h1 {{
    font-size:
        clamp(48px,7vw,92px);

    line-height: .95;

    letter-spacing:
        -.055em;

    margin-bottom: 25px;
}}

.gradient-text {{
    background:
        linear-gradient(
            90deg,
            #fff,
            #9ee8ff,
            #8d7dff
        );

    -webkit-background-clip: text;

    background-clip: text;

    color: transparent;
}}

.hero-description {{
    max-width: 680px;

    color: #aab4c8;

    font-size:
        clamp(16px,2vw,20px);

    margin-bottom: 32px;
}}

.hero-actions {{
    display: flex;

    flex-wrap: wrap;

    gap: 12px;
}}

.primary-button,
.secondary-button {{
    border: none;

    border-radius: 12px;

    padding:
        13px 19px;

    font-weight: 800;
}}

.primary-button {{
    color: white;

    background:
        linear-gradient(
            135deg,
            #6658ff,
            #328dff
        );
}}

.secondary-button {{
    color: #dce5f5;

    background:
        rgba(255,255,255,.06);

    border:
        1px solid
        rgba(255,255,255,.1);
}}


/* ============================================================
   ORB
============================================================ */

.hero-visual {{
    min-height: 430px;

    display: grid;

    place-items: center;
}}

.orb {{
    width:
        min(390px,75vw);

    aspect-ratio: 1;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #b9f5ff,
            #4d96ff 15%,
            #624eff 38%,
            #22134d 65%,
            #080914 75%
        );

    box-shadow:
        0 0 90px
        rgba(83,92,255,.32);
}}

.orb::after {{
    content: "∞";

    display: grid;

    place-items: center;

    width: 100%;
    height: 100%;

    color:
        rgba(255,255,255,.72);

    font-size: 100px;

    font-weight: 900;
}}


/* ============================================================
   SECTIONS
============================================================ */

section {{
    scroll-margin-top: 100px;
}}

.section {{
    padding:
        70px 0;
}}

.section-header {{
    display: flex;

    justify-content: space-between;

    align-items: end;

    margin-bottom: 30px;
}}

.section-title {{
    font-size:
        clamp(30px,4vw,48px);

    line-height: 1.05;

    letter-spacing: -.04em;
}}

.section-description {{
    color: #8993a7;

    max-width: 650px;

    margin-top: 8px;
}}


/* ============================================================
   STATS
============================================================ */

.stats-grid {{
    display: grid;

    grid-template-columns:
        repeat(4,1fr);

    gap: 14px;
}}

.stat-card {{
    padding: 25px;

    border:
        1px solid
        rgba(255,255,255,.08);

    border-radius: 18px;

    background:
        rgba(255,255,255,.035);

    text-align: center;
}}

.stat-number {{
    font-size: 32px;

    font-weight: 900;
}}

.stat-label {{
    color: #8993a7;

    font-size: 13px;

    text-transform: uppercase;

    letter-spacing: .1em;
}}


/* ============================================================
   GRIDS
============================================================ */

.card-grid {{
    display: grid;

    grid-template-columns:
        repeat(4,minmax(0,1fr));

    gap: 18px;
}}

.category-grid {{
    display: grid;

    grid-template-columns:
        repeat(3,minmax(0,1fr));

    gap: 18px;
}}


/* ============================================================
   CARDS
============================================================ */

.npc-card,
.world-card,
.quest-card,
.category-card {{
    position: relative;

    overflow: hidden;

    border:
        1px solid
        rgba(255,255,255,.08);

    border-radius: 20px;

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.055),
            rgba(255,255,255,.025)
        );

    transition:
        transform .25s,
        border-color .25s,
        box-shadow .25s;
}}

.npc-card:hover,
.world-card:hover,
.quest-card:hover,
.category-card:hover {{
    transform:
        translateY(-5px);

    border-color:
        rgba(115,201,255,.28);

    box-shadow:
        0 22px 60px
        rgba(0,0,0,.25);
}}

.card-body {{
    padding: 22px;
}}

.card-type {{
    color: #6fbcff;

    font-size: 10px;

    font-weight: 900;

    letter-spacing: .15em;

    margin-bottom: 8px;
}}

.card-body h3 {{
    font-size: 22px;

    line-height: 1.15;

    margin-bottom: 8px;
}}

.card-body p {{
    color: #8f99ad;

    font-size: 14px;

    margin:
        13px 0 18px;
}}


/* ============================================================
   NPC
============================================================ */

.card-top {{
    min-height: 135px;

    padding: 18px;

    display: flex;

    align-items: start;

    justify-content: space-between;

    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(91,159,255,.18),
            transparent 60%
        );
}}

.avatar {{
    width: 58px;
    height: 58px;

    display: grid;

    place-items: center;

    border-radius: 16px;

    background:
        linear-gradient(
            135deg,
            #6b58ff,
            #28c7ff
        );

    font-size: 25px;

    font-weight: 900;
}}

.level-badge {{
    padding:
        5px 9px;

    border-radius: 8px;

    background:
        rgba(255,255,255,.08);

    color: #c8d0df;

    font-size: 11px;

    font-weight: 800;
}}

.role {{
    color: #b58cff;

    font-size: 13px;

    font-weight: 700;
}}

.world-name {{
    color: #7f8ba2;

    font-size: 12px;

    margin-top: 7px;
}}


/* ============================================================
   WORLD / QUEST
============================================================ */

.world-card,
.quest-card {{
    min-height: 280px;
}}

.world-symbol,
.quest-symbol {{
    height: 130px;

    display: grid;

    place-items: center;

    font-size: 55px;

    background:
        radial-gradient(
            circle,
            rgba(79,163,255,.2),
            transparent 68%
        );

    color: #8ddcff;
}}

.world-meta,
.quest-meta {{
    display: flex;

    flex-wrap: wrap;

    gap: 7px;

    margin-top: 10px;
}}

.world-meta span,
.quest-meta span {{
    padding:
        4px 8px;

    border-radius: 7px;

    background:
        rgba(255,255,255,.055);

    color: #a7b0c2;

    font-size: 11px;
}}

.reward {{
    color: #79e5b3;

    font-size: 13px;

    font-weight: 800;

    margin-bottom: 15px;
}}


/* ============================================================
   CATEGORY
============================================================ */

.category-card {{
    display: flex;

    gap: 18px;

    padding: 22px;
}}

.category-icon {{
    flex: 0 0 56px;

    width: 56px;
    height: 56px;

    display: grid;

    place-items: center;

    border-radius: 15px;

    background:
        rgba(105,118,255,.13);

    font-size: 25px;
}}

.category-content {{
    flex: 1;
}}

.category-content h3 {{
    font-size: 18px;

    margin-bottom: 5px;
}}

.category-content p {{
    color: #8993a7;

    font-size: 13px;

    margin-bottom: 13px;
}}


/* ============================================================
   BUTTON
============================================================ */

.card-button {{
    width: 100%;

    padding:
        10px 12px;

    border:
        1px solid
        rgba(255,255,255,.09);

    border-radius: 10px;

    background:
        rgba(255,255,255,.045);

    color: #dfe7f5;

    font-weight: 750;
}}

.card-button:hover {{
    background:
        rgba(95,181,255,.11);

    border-color:
        rgba(100,200,255,.25);
}}


/* ============================================================
   SEARCH RESULTS
============================================================ */

.search-results-section {{
    display: none;

    padding:
        40px 0 30px;
}}

.search-results-section.active {{
    display: block;
}}

.search-panel {{
    padding: 22px;

    border:
        1px solid
        rgba(100,190,255,.16);

    border-radius: 20px;

    background:
        linear-gradient(
            135deg,
            rgba(80,130,255,.08),
            rgba(255,255,255,.025)
        );
}}

.search-header {{
    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 15px;

    margin-bottom: 20px;
}}

.search-header h2 {{
    font-size: 25px;
}}

.search-count {{
    color: #8ddcff;

    font-size: 13px;

    font-weight: 800;
}}

.search-result-list {{
    display: grid;

    gap: 10px;
}}

.search-result {{
    display: grid;

    grid-template-columns:
        auto 1fr auto;

    align-items: center;

    gap: 14px;

    padding: 15px;

    border:
        1px solid
        rgba(255,255,255,.07);

    border-radius: 14px;

    background:
        rgba(255,255,255,.035);

    color: white;

    text-align: left;
}}

.search-result:hover {{
    background:
        rgba(255,255,255,.06);

    border-color:
        rgba(110,200,255,.2);
}}

.search-result-icon {{
    width: 44px;
    height: 44px;

    display: grid;

    place-items: center;

    border-radius: 12px;

    background:
        rgba(105,130,255,.14);

    font-size: 20px;
}}

.search-result-title {{
    font-weight: 850;
}}

.search-result-meta {{
    color: #8993a7;

    font-size: 12px;
}}

.search-result-type {{
    padding:
        4px 7px;

    border-radius: 6px;

    background:
        rgba(255,255,255,.05);

    color: #8792a7;

    font-size: 9px;

    font-weight: 900;

    letter-spacing: .1em;
}}

.no-results {{
    padding:
        45px 20px;

    text-align: center;

    color: #8993a7;
}}

.no-results strong {{
    display: block;

    color: white;

    font-size: 20px;

    margin-bottom: 5px;
}}


/* ============================================================
   MODAL
============================================================ */

.modal {{
    position: fixed;

    inset: 0;

    z-index: 2000;

    display: none;

    place-items: center;

    padding: 20px;

    background:
        rgba(0,0,0,.72);

    backdrop-filter:
        blur(12px);
}}

.modal.active {{
    display: grid;
}}

.modal-box {{
    width:
        min(650px,100%);

    max-height: 90vh;

    overflow: auto;

    padding: 30px;

    border:
        1px solid
        rgba(255,255,255,.12);

    border-radius: 24px;

    background: #0c1120;
}}

.modal-close {{
    float: right;

    width: 35px;
    height: 35px;

    border: none;

    border-radius: 10px;

    background:
        rgba(255,255,255,.07);

    color: white;

    font-size: 18px;
}}

.modal-type {{
    color: #72cfff;

    font-size: 10px;

    font-weight: 900;

    letter-spacing: .15em;

    margin-bottom: 8px;
}}

.modal h2 {{
    font-size: 35px;

    line-height: 1.05;

    margin-bottom: 8px;
}}

.modal-subtitle {{
    color: #a98bff;

    font-weight: 750;

    margin-bottom: 18px;
}}

.modal p {{
    color: #9ba5b8;

    margin-top: 15px;
}}


/* ============================================================
   FOOTER
============================================================ */

.site-footer {{
    margin-top: 60px;

    padding:
        45px 0;

    border-top:
        1px solid
        rgba(255,255,255,.07);

    color: #707a8e;
}}

.footer-inner {{
    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 20px;
}}

.footer-title {{
    color: #dce4f2;

    font-weight: 800;
}}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width:1150px) {{

    .card-grid {{
        grid-template-columns:
            repeat(3,minmax(0,1fr));
    }}

}}

@media (max-width:900px) {{

    .header-inner {{
        flex-wrap: wrap;

        padding:
            12px 0;
    }}

    .header-search {{
        order: 3;

        flex-basis: 100%;

        max-width: none;

        margin: 0;
    }}

    .header-nav {{
        margin-left: auto;
    }}

    .hero {{
        grid-template-columns: 1fr;

        padding-top: 60px;
    }}

    .hero-visual {{
        min-height: 300px;

        order: -1;
    }}

    .orb {{
        width: 260px;
    }}

    .stats-grid {{
        grid-template-columns:
            repeat(2,1fr);
    }}

    .card-grid {{
        grid-template-columns:
            repeat(2,minmax(0,1fr));
    }}

    .category-grid {{
        grid-template-columns:
            repeat(2,minmax(0,1fr));
    }}

}}

@media (max-width:600px) {{

    .container {{
        width:
            min(94%,520px);
    }}

    .logo {{
        font-size: 15px;
    }}

    .header-nav {{
        display: none;
    }}

    .hero {{
        min-height: auto;

        padding:
            45px 0 50px;
    }}

    .hero h1 {{
        font-size:
            clamp(43px,14vw,65px);
    }}

    .hero-visual {{
        min-height: 230px;
    }}

    .orb {{
        width: 210px;
    }}

    .stats-grid {{
        grid-template-columns:
            1fr 1fr;
    }}

    .card-grid,
    .category-grid {{
        grid-template-columns: 1fr;
    }}

    .section {{
        padding:
            50px 0;
    }}

    .section-header {{
        align-items: start;

        flex-direction: column;
    }}

    .search-result {{
        grid-template-columns:
            auto 1fr;
    }}

    .search-result-type {{
        display: none;
    }}

    .footer-inner {{
        flex-direction: column;

        align-items: flex-start;
    }}

    .modal-box {{
        padding: 23px;
    }}

    .modal h2 {{
        font-size: 28px;
    }}

}}

</style>

</head>


<body>


<!-- =========================================================
     HEADER
========================================================= -->

<header class="site-header">

    <div class="header-inner">

        <a
            class="logo"
            href="#home"
            aria-label="NPC OMNIVERSE Home"
        >

            <span class="logo-mark">
                ∞
            </span>

            <span class="logo-text">
                NPC OMNIVERSE
            </span>

        </a>


        <div class="header-search">

            <div class="search-box">

                <span class="search-icon">
                    🔎
                </span>

                <input
                    id="searchInput"
                    class="search-input"
                    type="search"
                    autocomplete="off"
                    placeholder="Search NPCs, worlds, quests..."
                    aria-label="Search NPCs, worlds and quests"
                >

                <button
                    id="clearSearch"
                    class="clear-search"
                    type="button"
                    aria-label="Clear search"
                >
                    ×
                </button>

                <span class="search-key">
                    /
                </span>

            </div>

        </div>


        <nav class="header-nav">

            <a href="#npcs">
                NPCs
            </a>

            <a href="#worlds">
                Worlds
            </a>

            <a href="#quests">
                Quests
            </a>

        </nav>

    </div>

</header>


<!-- =========================================================
     MAIN
========================================================= -->

<main>


<section
    id="home"
    class="hero container"
>

    <div class="hero-content">

        <div class="eyebrow">
            ✦ THE DIGITAL OMNIVERSE
        </div>

        <h1>
            Explore the
            <span class="gradient-text">
                Infinite.
            </span>
        </h1>

        <p class="hero-description">
            {description}
        </p>

        <div class="hero-actions">

            <a
                class="primary-button"
                href="#npcs"
            >
                Explore NPCs →
            </a>

            <a
                class="secondary-button"
                href="#worlds"
            >
                Discover Worlds
            </a>

        </div>

    </div>


    <div class="hero-visual">

        <div class="orb"></div>

    </div>

</section>


<!-- =========================================================
     STATS
========================================================= -->

<section class="section">

    <div class="container">

        <div class="stats-grid">

            {stats_html}

        </div>

    </div>

</section>


<!-- =========================================================
     SEARCH RESULTS
========================================================= -->

<section
    id="searchResultsSection"
    class="search-results-section"
>

    <div class="container">

        <div class="search-panel">

            <div class="search-header">

                <div>

                    <h2>
                        Search Results
                    </h2>

                    <div
                        id="searchCount"
                        class="search-count"
                    >
                        0 results
                    </div>

                </div>

                <button
                    class="secondary-button"
                    type="button"
                    onclick="clearSearch()"
                >
                    Clear
                </button>

            </div>

            <div
                id="searchResultList"
                class="search-result-list"
            ></div>

        </div>

    </div>

</section>


<!-- =========================================================
     CATEGORIES
========================================================= -->

<section
    id="categories"
    class="section"
>

    <div class="container">

        <div class="section-header">

            <div>

                <h2 class="section-title">
                    Categories
                </h2>

                <p class="section-description">
                    Explore different types of characters
                    across the omniverse.
                </p>

            </div>

        </div>

        <div class="category-grid">

            {categories_html}

        </div>

    </div>

</section>


<!-- =========================================================
     NPCS
========================================================= -->

<section
    id="npcs"
    class="section"
>

    <div class="container">

        <div class="section-header">

            <div>

                <h2 class="section-title">
                    NPC Directory
                </h2>

                <p class="section-description">
                    Discover characters from across
                    the infinite realities.
                </p>

            </div>

        </div>

        <div
            id="npcGrid"
            class="card-grid"
        >

            {npc_html}

        </div>

    </div>

</section>


<!-- =========================================================
     WORLDS
========================================================= -->

<section
    id="worlds"
    class="section"
>

    <div class="container">

        <div class="section-header">

            <div>

                <h2 class="section-title">
                    Worlds
                </h2>

                <p class="section-description">
                    Explore realities, civilizations
                    and dimensions.
                </p>

            </div>

        </div>

        <div
            id="worldGrid"
            class="card-grid"
        >

            {worlds_html}

        </div>

    </div>

</section>


<!-- =========================================================
     QUESTS
========================================================= -->

<section
    id="quests"
    class="section"
>

    <div class="container">

        <div class="section-header">

            <div>

                <h2 class="section-title">
                    Quests
                </h2>

                <p class="section-description">
                    Adventures waiting to be discovered.
                </p>

            </div>

        </div>

        <div
            id="questGrid"
            class="card-grid"
        >

            {quests_html}

        </div>

    </div>

</section>


</main>


<!-- =========================================================
     FOOTER
========================================================= -->

<footer class="site-footer">

    <div class="container">

        <div class="footer-inner">

            <div>

                <div class="footer-title">
                    {site_name}
                </div>

                <div>
                    {tagline}
                </div>

            </div>

            <div>
                © 2026 NPC OMNIVERSE
            </div>

        </div>

    </div>

</footer>


<!-- =========================================================
     MODAL
========================================================= -->

<div
    id="modal"
    class="modal"
    role="dialog"
    aria-modal="true"
    aria-hidden="true"
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


<!-- =========================================================
     JAVASCRIPT DATA
========================================================= -->

<script>

const SITE_DATA = {data_json};


/* ============================================================
   ELEMENTS
============================================================ */

const searchInput =
    document.getElementById("searchInput");

const clearSearchButton =
    document.getElementById("clearSearch");

const searchResultsSection =
    document.getElementById("searchResultsSection");

const searchResultList =
    document.getElementById("searchResultList");

const searchCount =
    document.getElementById("searchCount");

const modal =
    document.getElementById("modal");

const modalContent =
    document.getElementById("modalContent");


/* ============================================================
   NORMALIZE
============================================================ */

function normalizeText(value) {{

    return String(value ?? "")
        .replace(/\\s+/g, " ")
        .trim()
        .toLowerCase();

}}


/* ============================================================
   BUILD SEARCH ITEMS
============================================================ */

function buildSearchItems() {{

    const items = [];

    const seen = new Set();


    function addItem(item) {{

        const key =
            item.type +
            "::" +
            normalizeText(item.name);

        if (seen.has(key)) {{
            return;
        }}

        seen.add(key);

        items.push(item);

    }}


    /* ========================================================
       NPCS
    ======================================================== */

    (SITE_DATA.featured_npcs || [])
        .forEach(npc => {{

            addItem({{

                type: "npc",

                icon: "👤",

                name:
                    npc.name || "",

                meta:
                    (npc.role || "") +
                    " • " +
                    (npc.world || ""),

                description:
                    npc.description || "",

                search:
                    [
                        npc.name,
                        npc.role,
                        npc.world,
                        npc.level,
                        npc.description
                    ]
                    .join(" ")
                    .toLowerCase()

            }});

        }});


    /* ========================================================
       WORLDS
    ======================================================== */

    (SITE_DATA.worlds || [])
        .forEach(world => {{

            addItem({{

                type: "world",

                icon: "🌍",

                name:
                    world.name || "",

                meta:
                    (world.type || "") +
                    " • Population: " +
                    (world.population || ""),

                description:
                    world.description || "",

                search:
                    [
                        world.name,
                        world.type,
                        world.population,
                        world.description
                    ]
                    .join(" ")
                    .toLowerCase()

            }});

        }});


    /* ========================================================
       QUESTS
    ======================================================== */

    (SITE_DATA.quests || [])
        .forEach(quest => {{

            addItem({{

                type: "quest",

                icon: "⚔️",

                name:
                    quest.name || "",

                meta:
                    (quest.difficulty || "") +
                    " • " +
                    (quest.world || ""),

                description:
                    quest.description || "",

                search:
                    [
                        quest.name,
                        quest.difficulty,
                        quest.world,
                        quest.reward,
                        quest.description
                    ]
                    .join(" ")
                    .toLowerCase()

            }});

        }});


    return items;

}}


const SEARCH_ITEMS =
    buildSearchItems();


/* ============================================================
   SEARCH SCORE
============================================================ */

function getSearchScore(item, query) {{

    const q =
        query.trim().toLowerCase();

    const name =
        item.name.toLowerCase();

    const search =
        item.search.toLowerCase();


    if (!q) {{
        return 0;
    }}


    /* NPC exact name */
    if (
        item.type === "npc" &&
        name === q
    ) {{
        return 100000;
    }}


    /* NPC starts with */
    if (
        item.type === "npc" &&
        name.startsWith(q)
    ) {{
        return 90000;
    }}


    /* NPC contains */
    if (
        item.type === "npc" &&
        name.includes(q)
    ) {{
        return 80000;
    }}


    /* Exact name */
    if (name === q) {{
        return 70000;
    }}


    /* Starts with */
    if (name.startsWith(q)) {{
        return 60000;
    }}


    /* Contains */
    if (name.includes(q)) {{
        return 50000;
    }}


    /* NPC metadata */
    if (item.type === "npc") {{

        const combined =
            [
                item.meta,
                item.description
            ]
            .join(" ")
            .toLowerCase();

        if (combined.includes(q)) {{
            return 30000;
        }}

    }}


    /* Other content */
    if (search.includes(q)) {{

        if (item.type === "world") {{
            return 20000;
        }}

        if (item.type === "quest") {{
            return 10000;
        }}

        return 5000;
    }}


    return -1;

}}


/* ============================================================
   ESCAPE HTML
============================================================ */

function escapeHTML(value) {{

    const div =
        document.createElement("div");

    div.textContent =
        String(value ?? "");

    return div.innerHTML;

}}


/* ============================================================
   SEARCH
============================================================ */

function performSearch(
    query,
    shouldScroll = false
) {{

    const q =
        query.trim().toLowerCase();


    if (!q) {{

        searchResultsSection
            .classList
            .remove("active");

        searchResultList.innerHTML = "";

        searchCount.textContent =
            "0 results";

        clearSearchButton.style.display =
            "none";

        return;
    }}


    clearSearchButton.style.display =
        "grid";


    const results =
        SEARCH_ITEMS

            .map(item => ({{
                item,
                score:
                    getSearchScore(
                        item,
                        q
                    )
            }}))

            .filter(
                result =>
                    result.score >= 0
            )

            .sort((a,b) => {{

                if (
                    b.score !== a.score
                ) {{
                    return (
                        b.score -
                        a.score
                    );
                }}


                const order = {{
                    npc: 0,
                    world: 1,
                    quest: 2
                }};


                return (
                    order[a.item.type] -
                    order[b.item.type]
                );

            }});


    searchResultsSection
        .classList
        .add("active");


    searchCount.textContent =
        results.length +
        (
            results.length === 1
                ? " result"
                : " results"
        );


    if (!results.length) {{

        searchResultList.innerHTML = `
            <div class="no-results">
                <strong>No results found</strong>
                Try another NPC name, world,
                quest or keyword.
            </div>
        `;

    }} else {{

        searchResultList.innerHTML =
            results
                .map(result => {{

                    const item =
                        result.item;

                    return `
                        <button
                            class="search-result"
                            type="button"
                            onclick='openSearchItem(
                                ${{JSON.stringify(item.name)}},
                                ${{JSON.stringify(item.type)}}
                            )'
                        >

                            <span
                                class="search-result-icon"
                            >
                                ${{escapeHTML(item.icon)}}
                            </span>

                            <span>

                                <span
                                    class="search-result-title"
                                >
                                    ${{escapeHTML(item.name)}}
                                </span>

                                <span
                                    class="search-result-meta"
                                >
                                    ${{escapeHTML(item.meta)}}
                                </span>

                            </span>

                            <span
                                class="search-result-type"
                            >
                                ${{escapeHTML(item.type)}}
                            </span>

                        </button>
                    `;

                }})

                .join("");

    }}


    if (shouldScroll) {{

        searchResultsSection
            .scrollIntoView({{
                behavior: "smooth",
                block: "start"
            }});

    }}

}}


/* ============================================================
   SEARCH ITEM
============================================================ */

function openSearchItem(
    name,
    type
) {{

    if (type === "npc") {{

        const npc =
            SITE_DATA.featured_npcs.find(
                entry =>
                    normalizeText(entry.name) ===
                    normalizeText(name)
            );

        if (npc) {{

            openNPC(
                npc.name,
                npc.role,
                npc.world,
                String(npc.level),
                npc.description
            );

        }}

        return;
    }}


    if (type === "world") {{

        const world =
            SITE_DATA.worlds.find(
                entry =>
                    normalizeText(entry.name) ===
                    normalizeText(name)
            );

        if (world) {{

            openWorld(
                world.name,
                world.type,
                world.population,
                world.description
            );

        }}

        return;
    }}


    if (type === "quest") {{

        const quest =
            SITE_DATA.quests.find(
                entry =>
                    normalizeText(entry.name) ===
                    normalizeText(name)
            );

        if (quest) {{

            openQuest(
                quest.name,
                quest.difficulty,
                quest.world,
                quest.reward,
                quest.description
            );

        }}

    }}

}}


/* ============================================================
   SEARCH EVENTS
============================================================ */

let searchTimer = null;


searchInput.addEventListener(
    "input",
    function() {{

        const value =
            this.value;

        clearTimeout(
            searchTimer
        );

        searchTimer =
            setTimeout(
                () =>
                    performSearch(
                        value,
                        false
                    ),
                80
            );

    }}
);


searchInput.addEventListener(
    "keydown",
    function(event) {{

        if (
            event.key === "Enter"
        ) {{

            event.preventDefault();

            performSearch(
                this.value,
                true
            );

        }}


        if (
            event.key === "Escape"
        ) {{

            clearSearch();

        }}

    }}
);


clearSearchButton.addEventListener(
    "click",
    clearSearch
);


/* ============================================================
   CLEAR SEARCH
============================================================ */

function clearSearch() {{

    searchInput.value = "";

    performSearch("");

    searchInput.focus();

}}


/* ============================================================
   KEYBOARD SHORTCUT
============================================================ */

document.addEventListener(
    "keydown",
    function(event) {{

        const tag =
            document.activeElement?.tagName;

        const isTyping =
            tag === "INPUT" ||
            tag === "TEXTAREA";


        if (
            event.key === "/" &&
            !isTyping
        ) {{

            event.preventDefault();

            searchInput.focus();

        }}


        if (
            event.key === "Escape" &&
            modal.classList.contains("active")
        ) {{

            closeModal();

        }}

    }}
);


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

    modalContent.innerHTML = `

        <div class="modal-type">
            NPC CHARACTER
        </div>

        <h2>
            ${{escapeHTML(name)}}
        </h2>

        <div class="modal-subtitle">
            ${{escapeHTML(role)}}
        </div>

        <div class="world-meta">

            <span>
                🌍 ${{escapeHTML(world)}}
            </span>

            <span>
                LEVEL ${{escapeHTML(level)}}
            </span>

        </div>

        <p>
            ${{escapeHTML(description)}}
        </p>

    `;

    openModal();

}}


/* ============================================================
   WORLD MODAL
============================================================ */

function openWorld(
    name,
    type,
    population,
    description
) {{

    modalContent.innerHTML = `

        <div class="modal-type">
            WORLD
        </div>

        <h2>
            ${{escapeHTML(name)}}
        </h2>

        <div class="modal-subtitle">
            ${{escapeHTML(type)}}
        </div>

        <div class="world-meta">

            <span>
                Population:
                ${{escapeHTML(population)}}
            </span>

        </div>

        <p>
            ${{escapeHTML(description)}}
        </p>

    `;

    openModal();

}}


/* ============================================================
   QUEST MODAL
============================================================ */

function openQuest(
    name,
    difficulty,
    world,
    reward,
    description
) {{

    modalContent.innerHTML = `

        <div class="modal-type">
            QUEST
        </div>

        <h2>
            ${{escapeHTML(name)}}
        </h2>

        <div class="modal-subtitle">
            ${{escapeHTML(difficulty)}}
        </div>

        <div class="quest-meta">

            <span>
                🌍 ${{escapeHTML(world)}}
            </span>

            <span>
                🎁 ${{escapeHTML(reward)}}
            </span>

        </div>

        <p>
            ${{escapeHTML(description)}}
        </p>

    `;

    openModal();

}}


/* ============================================================
   CATEGORY
============================================================ */

function showCategory(name) {{

    searchInput.value =
        name;

    performSearch(
        name,
        true
    );

}}


/* ============================================================
   MODAL
============================================================ */

function openModal() {{

    modal
        .classList
        .add("active");

    modal.setAttribute(
        "aria-hidden",
        "false"
    );

    document.body.style.overflow =
        "hidden";

}}


function closeModal() {{

    modal
        .classList
        .remove("active");

    modal.setAttribute(
        "aria-hidden",
        "true"
    );

    document.body.style.overflow =
        "";

}}


modal.addEventListener(
    "click",
    function(event) {{

        if (
            event.target === modal
        ) {{

            closeModal();

        }}

    }}
);


/* ============================================================
   INITIALIZATION
============================================================ */

document.addEventListener(
    "DOMContentLoaded",
    function() {{

        searchInput.value = "";

        searchResultsSection
            .classList
            .remove("active");

    }}
);

</script>

</body>
</html>
"""


# ============================================================
# ROBOTS.TXT
# ============================================================

def build_robots(data):

    base_url = data[
        "url"
    ].rstrip("/")

    return f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""


# ============================================================
# SITEMAP
# ============================================================

def build_sitemap(data):

    base_url = data[
        "url"
    ].rstrip("/")

    return f"""<?xml version="1.0" encoding="UTF-8"?>

<urlset
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
>

    <url>

        <loc>
            {esc(base_url)}/
        </loc>

    </url>

</urlset>
"""


# ============================================================
# WEB MANIFEST
# ============================================================

def build_manifest(data):

    manifest = {

        "name":
            data["name"],

        "short_name":
            "NPCBook",

        "description":
            data["description"],

        "start_url":
            "/",

        "display":
            "standalone",

        "background_color":
            "#080b14",

        "theme_color":
            "#080b14",

        "lang":
            data["language"],

    }

    return json.dumps(
        manifest,
        ensure_ascii=False,
        indent=2,
    )


# ============================================================
# BUILD
# ============================================================

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )


    # ========================================================
    # CLEAN CONTENT FIRST
    # ========================================================

    cleaned_data = clean_site_data(
        SITE_DATA
    )


    # ========================================================
    # REPORT DUPLICATES
    # ========================================================

    print_duplicate_report(
        SITE_DATA,
        cleaned_data,
    )


    # ========================================================
    # BUILD FILES
    # ========================================================

    html_content = build_html(
        cleaned_data
    )

    robots_content = build_robots(
        cleaned_data
    )

    sitemap_content = build_sitemap(
        cleaned_data
    )

    manifest_content = build_manifest(
        cleaned_data
    )


    # ========================================================
    # WRITE FILES
    # ========================================================

    OUTPUT_FILE.write_text(
        html_content,
        encoding="utf-8",
    )

    ROBOTS_FILE.write_text(
        robots_content,
        encoding="utf-8",
    )

    SITEMAP_FILE.write_text(
        sitemap_content,
        encoding="utf-8",
    )

    MANIFEST_FILE.write_text(
        manifest_content,
        encoding="utf-8",
    )


    # ========================================================
    # BUILD COMPLETE
    # ========================================================

    print()

    print("=" * 60)

    print(
        "NPC OMNIVERSE BUILD COMPLETE"
    )

    print("=" * 60)

    print()

    print(
        f"Generated: {OUTPUT_FILE}"
    )

    print(
        f"Generated: {ROBOTS_FILE}"
    )

    print(
        f"Generated: {SITEMAP_FILE}"
    )

    print(
        f"Generated: {MANIFEST_FILE}"
    )

    print()

    print(
        "CONTENT COUNTS"
    )

    print(
        f"Categories: "
        f"{len(cleaned_data.get('categories', []))}"
    )

    print(
        f"NPCs: "
        f"{len(cleaned_data.get('featured_npcs', []))}"
    )

    print(
        f"Worlds: "
        f"{len(cleaned_data.get('worlds', []))}"
    )

    print(
        f"Quests: "
        f"{len(cleaned_data.get('quests', []))}"
    )

    print()

    print(
        "Static site is ready for deployment."
    )

    print("=" * 60)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
