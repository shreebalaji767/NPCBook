from pathlib import Path
import json
import html
import re


# ============================================================
# NPC OMNIVERSE / NPCBOOK
# Static Site Generator
# ============================================================

OUTPUT_DIR = Path("site")

INDEX_FILE = OUTPUT_DIR / "index.html"
ROBOTS_FILE = OUTPUT_DIR / "robots.txt"
SITEMAP_FILE = OUTPUT_DIR / "sitemap.xml"
MANIFEST_FILE = OUTPUT_DIR / "site.webmanifest"


# ============================================================
# SITE CONFIGURATION
# ============================================================

SITE_DATA = {
    "name": "NPC OMNIVERSE",
    "tagline": "Explore. Create. Discover.",
    "description": (
        "Explore NPCs, worlds, quests, factions, lore, characters "
        "and stories from an ever-growing fictional omniverse."
    ),
    "url": "https://npcbook.onrender.com/",
    "language": "en",
    "author": "NPC OMNIVERSE",

    "keywords": [
        "NPC",
        "NPCBook",
        "NPC Omniverse",
        "characters",
        "fictional worlds",
        "quests",
        "lore",
        "factions",
        "fantasy",
        "anime",
        "manga",
        "manhwa",
        "manhua",
        "novels",
        "movies",
        "games",
        "stories",
    ],

    # These can remain as global counters.
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
            "description": "Fighters, soldiers and battle-hardened characters.",
        },
        {
            "name": "Mages",
            "icon": "🔮",
            "description": "Magic users, sorcerers and arcane practitioners.",
        },
        {
            "name": "Assassins",
            "icon": "🗡️",
            "description": "Stealth specialists, hunters and deadly operatives.",
        },
        {
            "name": "Adventurers",
            "icon": "🧭",
            "description": "Explorers, travelers and treasure hunters.",
        },
        {
            "name": "Warlords",
            "icon": "👑",
            "description": "Leaders, conquerors and military rulers.",
        },
        {
            "name": "Mystics",
            "icon": "🌙",
            "description": "Mystics, seers and mysterious supernatural figures.",
        },
    ],

    # ========================================================
    # NPC DATA
    # ========================================================

    "npcs": [
        {
            "id": "kael-veyron",
            "name": "Kael Veyron",
            "category": "Warriors",
            "rarity": "Legendary",
            "role": "Blade Commander",
            "world": "Aetheris",
            "description": (
                "A legendary blade commander whose reputation was forged "
                "during the Crimson War."
            ),
            "tags": [
                "warrior",
                "commander",
                "swordsman",
                "legendary",
            ],
        },
        {
            "id": "lyra-solenne",
            "name": "Lyra Solenne",
            "category": "Mages",
            "rarity": "Epic",
            "role": "Astral Mage",
            "world": "Aetheris",
            "description": (
                "An astral mage capable of reading ancient constellations "
                "and manipulating celestial energy."
            ),
            "tags": [
                "mage",
                "astral",
                "magic",
                "celestial",
            ],
        },
        {
            "id": "drax-ironfall",
            "name": "Drax Ironfall",
            "category": "Warlords",
            "rarity": "Mythic",
            "role": "Iron Warlord",
            "world": "Ashen Dominion",
            "description": (
                "A feared warlord who commands the Iron Legion across "
                "the volcanic frontier."
            ),
            "tags": [
                "warlord",
                "iron legion",
                "commander",
                "battle",
            ],
        },
        {
            "id": "mira-nightshade",
            "name": "Mira Nightshade",
            "category": "Assassins",
            "rarity": "Rare",
            "role": "Shadow Assassin",
            "world": "Nocturne",
            "description": (
                "A silent assassin who travels between cities through "
                "the hidden roads of Nocturne."
            ),
            "tags": [
                "assassin",
                "shadow",
                "stealth",
                "nocturne",
            ],
        },
    ],

    # ========================================================
    # WORLDS
    # ========================================================

    "worlds": [
        {
            "id": "aetheris",
            "name": "Aetheris",
            "type": "High Fantasy",
            "status": "Active",
            "description": (
                "A vast realm of floating kingdoms, ancient magic "
                "and forgotten civilizations."
            ),
            "tags": [
                "fantasy",
                "magic",
                "kingdoms",
                "floating islands",
            ],
        },
        {
            "id": "nocturne",
            "name": "Nocturne",
            "type": "Dark Fantasy",
            "status": "Active",
            "description": (
                "A world where eternal twilight hides ancient creatures "
                "and secret societies."
            ),
            "tags": [
                "dark fantasy",
                "twilight",
                "mystery",
                "assassins",
            ],
        },
        {
            "id": "ashen-dominion",
            "name": "Ashen Dominion",
            "type": "Dark Fantasy",
            "status": "Active",
            "description": (
                "A volcanic empire ruled by powerful warlords and "
                "armies forged in fire."
            ),
            "tags": [
                "volcano",
                "empire",
                "war",
                "warlords",
            ],
        },
        {
            "id": "the-shattered-realms",
            "name": "The Shattered Realms",
            "type": "Multiversal",
            "status": "Expanding",
            "description": (
                "A fractured collection of worlds connected by unstable "
                "portals and ancient dimensional gates."
            ),
            "tags": [
                "multiverse",
                "portals",
                "dimensions",
                "worlds",
            ],
        },
    ],

    # ========================================================
    # QUESTS
    # ========================================================

    "quests": [
        {
            "id": "the-lost-crown",
            "name": "The Lost Crown",
            "difficulty": "Hard",
            "status": "Available",
            "world": "Aetheris",
            "description": (
                "Recover the crown of the fallen king before it is "
                "claimed by the enemies of the northern kingdoms."
            ),
            "tags": [
                "crown",
                "kingdom",
                "treasure",
                "war",
            ],
        },
        {
            "id": "echoes-of-nocturne",
            "name": "Echoes of Nocturne",
            "difficulty": "Extreme",
            "status": "Available",
            "world": "Nocturne",
            "description": (
                "Investigate strange voices appearing every night "
                "beneath the abandoned city."
            ),
            "tags": [
                "mystery",
                "nocturne",
                "voices",
                "city",
            ],
        },
        {
            "id": "the-iron-rebellion",
            "name": "The Iron Rebellion",
            "difficulty": "Legendary",
            "status": "Active",
            "world": "Ashen Dominion",
            "description": (
                "Stop the rebellion spreading through the Iron Legion "
                "before the empire collapses."
            ),
            "tags": [
                "rebellion",
                "iron legion",
                "empire",
                "war",
            ],
        },
    ],

    # ========================================================
    # FUTURE GENERIC POSTS
    #
    # Any future post added here automatically receives:
    # - Search
    # - Modal
    # - Screenshot button
    # - Unique ID
    # - Duplicate protection
    # ========================================================

    "posts": [
        # Example:
        #
        # {
        #     "id": "example-post",
        #     "name": "Example Lore Entry",
        #     "type": "Lore",
        #     "description": "Example lore information.",
        #     "tags": ["lore", "history"]
        # },
    ],
}


# ============================================================
# BASIC HELPERS
# ============================================================

def esc(value):
    return html.escape(str(value or ""), quote=True)


def normalize_key(value):
    value = str(value or "").strip().lower()
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def slug(value):
    result = normalize_key(value)
    return result or "item"


def search_text(value):
    if isinstance(value, list):
        return " ".join(search_text(x) for x in value)

    if isinstance(value, dict):
        return " ".join(
            search_text(v)
            for v in value.values()
        )

    return str(value or "").lower()


def json_attr(value):
    return esc(json.dumps(value, ensure_ascii=False))


def generate_keywords(data):
    keywords = set()

    for word in data.get("keywords", []):
        keywords.add(str(word))

    for category in data.get("categories", []):
        keywords.add(category.get("name", ""))

    for collection_name in [
        "npcs",
        "worlds",
        "quests",
        "posts",
    ]:
        for item in data.get(collection_name, []):
            for key, value in item.items():
                if key in {
                    "description",
                    "name",
                    "title",
                    "role",
                    "category",
                    "world",
                    "type",
                    "difficulty",
                    "status",
                }:
                    if isinstance(value, str):
                        keywords.add(value)

                if key == "tags" and isinstance(value, list):
                    for tag in value:
                        keywords.add(str(tag))

    return sorted(
        x.strip()
        for x in keywords
        if str(x).strip()
    )


# ============================================================
# DEDUPLICATION
# ============================================================

def record_content_key(item):
    """
    Creates a normalized representation of a record.

    This protects the site against repeated content even if
    the same record was accidentally added with another ID.
    """

    clean = {}

    for key, value in item.items():
        if key in {
            "id",
            "slug",
        }:
            continue

        if isinstance(value, list):
            clean[key] = [
                normalize_key(x)
                for x in value
            ]

        elif isinstance(value, dict):
            clean[key] = {
                str(k): normalize_key(v)
                for k, v in value.items()
            }

        else:
            clean[key] = normalize_key(value)

    return json.dumps(
        clean,
        sort_keys=True,
        ensure_ascii=False,
    )


def dedupe_records(records, collection_name):
    """
    Removes duplicate records.

    Duplicate detection works using:
    1. ID
    2. Name/title
    3. Complete normalized content
    """

    result = []

    seen_ids = set()
    seen_names = set()
    seen_content = set()

    for index, original in enumerate(records or []):
        item = dict(original)

        display_name = (
            item.get("name")
            or item.get("title")
            or f"{collection_name}-{index + 1}"
        )

        item_id = item.get("id") or slug(display_name)

        item_id = slug(item_id)

        name_key = normalize_key(display_name)
        content_key = record_content_key(item)

        # Duplicate ID
        if item_id in seen_ids:
            continue

        # Duplicate name within same collection
        if name_key and name_key in seen_names:
            continue

        # Completely identical content
        if content_key in seen_content:
            continue

        seen_ids.add(item_id)

        if name_key:
            seen_names.add(name_key)

        seen_content.add(content_key)

        item["id"] = item_id
        item["slug"] = item_id

        result.append(item)

    return result


def prepare_site_data():
    """
    Cleans and prepares all content before HTML generation.
    """

    data = json.loads(
        json.dumps(
            SITE_DATA,
            ensure_ascii=False,
        )
    )

    for collection in [
        "npcs",
        "worlds",
        "quests",
        "posts",
    ]:
        data[collection] = dedupe_records(
            data.get(collection, []),
            collection,
        )

    # Categories are also deduplicated.
    categories = []

    seen_categories = set()

    for category in data.get("categories", []):
        category = dict(category)

        key = normalize_key(
            category.get("name", "")
        )

        if not key or key in seen_categories:
            continue

        seen_categories.add(key)
        categories.append(category)

    data["categories"] = categories

    return data


SITE_DATA = prepare_site_data()


# ============================================================
# CARD HELPERS
# ============================================================

def item_display_name(item):
    return (
        item.get("name")
        or item.get("title")
        or "Untitled Entry"
    )


def item_type(item, collection):
    if collection == "npcs":
        return "NPC"

    if collection == "worlds":
        return "World"

    if collection == "quests":
        return "Quest"

    if collection == "posts":
        return item.get("type") or "Post"

    return "Post"


def item_icon(collection):
    if collection == "npcs":
        return "👤"

    if collection == "worlds":
        return "🌍"

    if collection == "quests":
        return "⚔️"

    return "📜"


def build_meta_items(item, collection):
    parts = []

    if collection == "npcs":
        if item.get("category"):
            parts.append(
                f'<span>{esc(item["category"])}</span>'
            )

        if item.get("rarity"):
            parts.append(
                f'<span>{esc(item["rarity"])}</span>'
            )

        if item.get("role"):
            parts.append(
                f'<span>{esc(item["role"])}</span>'
            )

        if item.get("world"):
            parts.append(
                f'<span>🌍 {esc(item["world"])}</span>'
            )

    elif collection == "worlds":
        if item.get("type"):
            parts.append(
                f'<span>{esc(item["type"])}</span>'
            )

        if item.get("status"):
            parts.append(
                f'<span>{esc(item["status"])}</span>'
            )

    elif collection == "quests":
        if item.get("difficulty"):
            parts.append(
                f'<span>{esc(item["difficulty"])}</span>'
            )

        if item.get("status"):
            parts.append(
                f'<span>{esc(item["status"])}</span>'
            )

        if item.get("world"):
            parts.append(
                f'<span>🌍 {esc(item["world"])}</span>'
            )

    else:
        if item.get("type"):
            parts.append(
                f'<span>{esc(item["type"])}</span>'
            )

        if item.get("status"):
            parts.append(
                f'<span>{esc(item["status"])}</span>'
            )

        if item.get("world"):
            parts.append(
                f'<span>🌍 {esc(item["world"])}</span>'
            )

    return "".join(parts)


# ============================================================
# SCREENSHOT BUTTON
# ============================================================

def build_screenshot_button(item, collection):
    item_id = esc(item["id"])

    return f"""
        <button
            class="card-action screenshot-button"
            type="button"
            title="Screenshot this post"
            data-screenshot-id="{item_id}"
            data-screenshot-type="{esc(item_type(item, collection))}"
            onclick="event.stopPropagation(); screenshotPost('{item_id}')"
        >
            📸 Screenshot
        </button>
    """


# ============================================================
# CARD BUILDERS
# ============================================================

def build_card(item, collection):
    name = item_display_name(item)
    kind = item_type(item, collection)

    item_id = esc(item["id"])

    description = (
        item.get("description")
        or "No description available."
    )

    tags = item.get("tags", [])

    tags_html = ""

    if isinstance(tags, list):
        for tag in tags[:8]:
            tags_html += (
                f'<span class="tag">{esc(tag)}</span>'
            )

    meta_html = build_meta_items(
        item,
        collection,
    )

    icon = item_icon(collection)

    screenshot_button = build_screenshot_button(
        item,
        collection,
    )

    # Data stored on the card for the screenshot generator.
    screenshot_data = json.dumps(
        {
            "id": item.get("id"),
            "name": name,
            "type": kind,
            "description": description,
            "collection": collection,
            "meta": meta_html,
            "tags": tags,
        },
        ensure_ascii=False,
    )

    return f"""
    <article
        class="content-card"
        id="card-{item_id}"
        data-id="{item_id}"
        data-type="{esc(kind)}"
        data-collection="{esc(collection)}"
        data-search="{esc(search_text(item))}"
        data-screenshot-data="{esc(screenshot_data)}"
        onclick="openPost('{item_id}', '{esc(collection)}')"
    >

        <div class="card-top">
            <div class="card-icon">
                {icon}
            </div>

            <div class="card-type">
                {esc(kind)}
            </div>
        </div>

        <h3 class="card-title">
            {esc(name)}
        </h3>

        <div class="card-meta">
            {meta_html}
        </div>

        <p class="card-description">
            {esc(description)}
        </p>

        <div class="card-tags">
            {tags_html}
        </div>

        <div class="card-actions">
            <button
                class="card-action view-button"
                type="button"
                onclick="event.stopPropagation(); openPost('{item_id}', '{esc(collection)}')"
            >
                View
            </button>

            {screenshot_button}
        </div>

    </article>
    """


def build_collection_section(
    collection,
    title,
    subtitle,
):
    items = SITE_DATA.get(collection, [])

    if not items:
        return ""

    cards = "".join(
        build_card(item, collection)
        for item in items
    )

    return f"""
    <section
        class="content-section"
        id="section-{esc(collection)}"
    >

        <div class="section-heading">
            <div>
                <div class="section-kicker">
                    {esc(collection.upper())}
                </div>

                <h2>
                    {esc(title)}
                </h2>

                <p>
                    {esc(subtitle)}
                </p>
            </div>

            <div class="section-count">
                {len(items)}
            </div>
        </div>

        <div class="card-grid">
            {cards}
        </div>

    </section>
    """


# ============================================================
# STATS
# ============================================================

def build_stats_html():
    stats = SITE_DATA.get("stats", {})

    html_parts = []

    icons = {
        "NPCs": "👤",
        "Worlds": "🌍",
        "Quests": "⚔️",
        "Factions": "🏰",
    }

    for name, value in stats.items():
        icon = icons.get(name, "✦")

        html_parts.append(
            f"""
            <div class="stat-card">
                <div class="stat-icon">
                    {icon}
                </div>

                <div class="stat-value">
                    {esc(value)}
                </div>

                <div class="stat-label">
                    {esc(name)}
                </div>
            </div>
            """
        )

    return "".join(html_parts)


# ============================================================
# CATEGORIES
# ============================================================

def build_category_html():
    parts = []

    for category in SITE_DATA.get("categories", []):
        parts.append(
            f"""
            <button
                class="category-card"
                type="button"
                onclick="searchCategory('{esc(category.get("name", ""))}')"
            >

                <div class="category-icon">
                    {esc(category.get("icon", "✦"))}
                </div>

                <div class="category-name">
                    {esc(category.get("name", ""))}
                </div>

                <div class="category-description">
                    {esc(category.get("description", ""))}
                </div>

            </button>
            """
        )

    return "".join(parts)


# ============================================================
# JSON-LD
# ============================================================

def build_json_ld():
    base_url = SITE_DATA["url"].rstrip("/")

    graph = [
        {
            "@type": "WebSite",
            "name": SITE_DATA["name"],
            "url": base_url,
            "description": SITE_DATA["description"],
        },
        {
            "@type": "WebPage",
            "name": SITE_DATA["name"],
            "url": base_url,
            "description": SITE_DATA["description"],
        },
        {
            "@type": "CollectionPage",
            "name": "NPC Collection",
            "url": base_url,
        },
    ]

    for npc in SITE_DATA.get("npcs", []):
        graph.append(
            {
                "@type": "Person",
                "name": item_display_name(npc),
                "description": npc.get("description", ""),
            }
        )

    for world in SITE_DATA.get("worlds", []):
        graph.append(
            {
                "@type": "Place",
                "name": item_display_name(world),
                "description": world.get("description", ""),
            }
        )

    return json.dumps(
        {
            "@context": "https://schema.org",
            "@graph": graph,
        },
        ensure_ascii=False,
    )


# ============================================================
# COMPLETE HTML
# ============================================================

def build_html():
    keywords = generate_keywords(SITE_DATA)

    all_search_items = []

    for collection in [
        "npcs",
        "worlds",
        "quests",
        "posts",
    ]:
        for item in SITE_DATA.get(collection, []):
            all_search_items.append(
                {
                    "id": item["id"],
                    "name": item_display_name(item),
                    "type": item_type(item, collection),
                    "collection": collection,
                    "description": item.get(
                        "description",
                        "",
                    ),
                    "search": search_text(item),
                }
            )

    search_json = json.dumps(
        all_search_items,
        ensure_ascii=False,
    )

    return f"""<!DOCTYPE html>
<html lang="{esc(SITE_DATA["language"])}">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>
    {esc(SITE_DATA["name"])}
</title>

<meta
    name="description"
    content="{esc(SITE_DATA["description"])}"
>

<meta
    name="keywords"
    content="{esc(", ".join(keywords))}"
>

<meta
    name="author"
    content="{esc(SITE_DATA["author"])}"
>

<meta
    name="theme-color"
    content="#080b14"
>

<link
    rel="manifest"
    href="/site.webmanifest"
>

<style>

* {{
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
}}

body {{
    margin: 0;
    min-height: 100vh;

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
            circle at 15% 10%,
            rgba(92, 72, 255, .12),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 20%,
            rgba(0, 210, 255, .08),
            transparent 30%
        ),
        #070910;

    color: #f4f6ff;
}}

button,
input {{
    font: inherit;
}}

button {{
    cursor: pointer;
}}

.site-header {{
    position: sticky;
    top: 0;
    z-index: 1000;

    backdrop-filter: blur(18px);

    background:
        rgba(7, 9, 16, .82);

    border-bottom:
        1px solid rgba(255,255,255,.08);
}}

.header-inner {{
    max-width: 1400px;
    margin: auto;

    min-height: 74px;

    padding:
        12px 22px;

    display: flex;
    align-items: center;
    gap: 22px;
}}

.brand {{
    display: flex;
    align-items: center;
    gap: 12px;

    min-width: max-content;
}}

.brand-logo {{
    width: 44px;
    height: 44px;

    display: grid;
    place-items: center;

    border-radius: 14px;

    background:
        linear-gradient(
            135deg,
            #6c63ff,
            #00c8ff
        );

    box-shadow:
        0 10px 35px
        rgba(77, 117, 255, .25);

    font-size: 23px;
}}

.brand-text {{
    font-weight: 900;
    letter-spacing: .5px;
}}

.brand-subtitle {{
    color: #8e96ae;
    font-size: 11px;
    margin-top: 2px;
}}

.search-wrap {{
    flex: 1;
    max-width: 720px;
    margin-left: auto;
}}

.search-box {{
    width: 100%;

    display: flex;
    align-items: center;
    gap: 10px;

    padding:
        0 14px;

    min-height: 46px;

    border:
        1px solid rgba(255,255,255,.09);

    border-radius: 14px;

    background:
        rgba(255,255,255,.045);
}}

.search-icon {{
    opacity: .6;
}}

.search-box input {{
    width: 100%;

    border: 0;
    outline: 0;

    background: transparent;
    color: white;

    font-size: 14px;
}}

.search-box input::placeholder {{
    color: #747d96;
}}

.clear-search {{
    border: 0;
    background: transparent;
    color: #8c94a9;
    display: none;
}}

.hero {{
    max-width: 1400px;
    margin: auto;

    padding:
        90px 22px
        60px;

    display: grid;
    grid-template-columns:
        minmax(0, 1.3fr)
        minmax(280px, .7fr);

    gap: 60px;
    align-items: center;
}}

.hero-kicker {{
    color: #7d8cff;

    font-size: 12px;
    font-weight: 900;

    letter-spacing: 2px;

    text-transform: uppercase;

    margin-bottom: 15px;
}}

.hero h1 {{
    margin: 0;

    font-size:
        clamp(42px, 7vw, 82px);

    line-height: .94;

    letter-spacing: -4px;
}}

.hero h1 span {{
    background:
        linear-gradient(
            90deg,
            #8d7cff,
            #4fdcff
        );

    -webkit-background-clip: text;
    background-clip: text;

    color: transparent;
}}

.hero-description {{
    max-width: 720px;

    margin-top: 24px;

    color: #a7aec2;

    line-height: 1.8;

    font-size: 16px;
}}

.hero-actions {{
    display: flex;
    gap: 12px;

    margin-top: 28px;

    flex-wrap: wrap;
}}

.hero-button {{
    border: 0;

    border-radius: 13px;

    padding:
        13px 18px;

    font-weight: 800;

    background:
        linear-gradient(
            135deg,
            #6558ff,
            #009dff
        );

    color: white;

    box-shadow:
        0 12px 35px
        rgba(67, 100, 255, .25);
}}

.hero-button.secondary {{
    background:
        rgba(255,255,255,.06);

    border:
        1px solid rgba(255,255,255,.1);

    box-shadow: none;
}}

.hero-orb-wrap {{
    display: grid;
    place-items: center;
}}

.hero-orb {{
    width: min(350px, 75vw);
    aspect-ratio: 1;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            rgba(255,255,255,.5),
            transparent 7%
        ),
        radial-gradient(
            circle,
            rgba(92,82,255,.4),
            rgba(0,0,0,0) 60%
        );

    border:
        1px solid
        rgba(255,255,255,.12);

    box-shadow:
        inset 0 0 80px
        rgba(101, 88, 255, .2),
        0 0 120px
        rgba(40, 115, 255, .13);

    animation:
        floatOrb 7s ease-in-out infinite;
}}

@keyframes floatOrb {{
    0%,100% {{
        transform: translateY(0);
    }}

    50% {{
        transform: translateY(-16px);
    }}
}}

.stats {{
    max-width: 1400px;
    margin: auto;

    padding:
        0 22px
        50px;

    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 14px;
}}

.stat-card {{
    padding: 22px;

    border:
        1px solid rgba(255,255,255,.08);

    border-radius: 18px;

    background:
        rgba(255,255,255,.035);
}}

.stat-icon {{
    font-size: 22px;
}}

.stat-value {{
    margin-top: 10px;

    font-size: 30px;
    font-weight: 900;
}}

.stat-label {{
    color: #858da3;
    margin-top: 4px;
}}

.content-section {{
    max-width: 1400px;
    margin: auto;

    padding:
        40px 22px;
}}

.section-heading {{
    display: flex;
    justify-content: space-between;
    align-items: end;

    gap: 20px;

    margin-bottom: 22px;
}}

.section-kicker {{
    color: #7d8cff;

    font-size: 11px;
    font-weight: 900;

    letter-spacing: 2px;
}}

.section-heading h2 {{
    margin:
        5px 0 5px;

    font-size: 31px;
}}

.section-heading p {{
    margin: 0;

    color: #81899e;
}}

.section-count {{
    min-width: 42px;
    height: 42px;

    display: grid;
    place-items: center;

    border-radius: 13px;

    background:
        rgba(255,255,255,.06);

    color: #aeb6ca;

    font-weight: 900;
}}

.card-grid {{
    display: grid;

    grid-template-columns:
        repeat(4, minmax(0, 1fr));

    gap: 16px;
}}

.content-card {{
    position: relative;

    padding: 20px;

    border:
        1px solid rgba(255,255,255,.08);

    border-radius: 20px;

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.055),
            rgba(255,255,255,.025)
        );

    transition:
        transform .2s ease,
        border-color .2s ease,
        box-shadow .2s ease;

    overflow: hidden;
}}

.content-card:hover {{
    transform: translateY(-4px);

    border-color:
        rgba(124, 113, 255, .4);

    box-shadow:
        0 20px 50px
        rgba(0,0,0,.22);
}}

.card-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.card-icon {{
    width: 42px;
    height: 42px;

    display: grid;
    place-items: center;

    border-radius: 13px;

    background:
        rgba(255,255,255,.07);

    font-size: 21px;
}}

.card-type {{
    font-size: 10px;

    text-transform: uppercase;

    letter-spacing: 1.3px;

    color: #7f88a0;

    font-weight: 900;
}}

.card-title {{
    margin:
        17px 0 10px;

    font-size: 20px;

    letter-spacing: -.4px;
}}

.card-meta {{
    display: flex;

    gap: 7px;

    flex-wrap: wrap;

    margin-bottom: 12px;
}}

.card-meta span {{
    padding:
        5px 8px;

    border-radius: 8px;

    background:
        rgba(255,255,255,.055);

    color: #9fa8bd;

    font-size: 10px;
}}

.card-description {{
    color: #959db2;

    line-height: 1.65;

    font-size: 13px;

    min-height: 66px;
}}

.card-tags {{
    display: flex;

    flex-wrap: wrap;

    gap: 6px;

    margin-top: 14px;

    min-height: 24px;
}}

.tag {{
    padding:
        5px 8px;

    border-radius: 7px;

    background:
        rgba(93, 82, 255, .11);

    color: #aaa4ff;

    font-size: 10px;
}}

.card-actions {{
    display: flex;

    gap: 8px;

    margin-top: 17px;

    padding-top: 15px;

    border-top:
        1px solid
        rgba(255,255,255,.06);
}}

.card-action {{
    border: 0;

    border-radius: 10px;

    padding:
        9px 11px;

    font-size: 11px;

    font-weight: 800;

    color: white;

    background:
        rgba(255,255,255,.07);

    transition:
        background .2s ease,
        transform .2s ease;
}}

.card-action:hover {{
    background:
        rgba(255,255,255,.12);

    transform: translateY(-1px);
}}

.screenshot-button {{
    background:
        rgba(89, 113, 255, .13);

    color: #b9c0ff;
}}

.category-grid {{
    max-width: 1400px;
    margin: auto;

    padding:
        0 22px
        60px;

    display: grid;

    grid-template-columns:
        repeat(6, minmax(0, 1fr));

    gap: 12px;
}}

.category-card {{
    text-align: left;

    border:
        1px solid rgba(255,255,255,.08);

    border-radius: 16px;

    padding: 17px;

    color: white;

    background:
        rgba(255,255,255,.035);

    transition:
        transform .2s ease,
        border-color .2s ease;
}}

.category-card:hover {{
    transform: translateY(-3px);

    border-color:
        rgba(125, 113, 255, .4);
}}

.category-icon {{
    font-size: 24px;
}}

.category-name {{
    font-weight: 900;

    margin-top: 10px;
}}

.category-description {{
    color: #81899f;

    font-size: 11px;

    line-height: 1.5;

    margin-top: 5px;
}}

.search-results {{
    display: none;

    max-width: 1400px;
    margin: auto;

    padding:
        30px 22px
        60px;
}}

.search-results.visible {{
    display: block;
}}

.search-results-heading {{
    margin-bottom: 20px;

    color: #aeb6ca;
}}

.search-result-list {{
    display: grid;

    grid-template-columns:
        repeat(4, minmax(0, 1fr));

    gap: 12px;
}}

.search-result {{
    padding: 16px;

    border:
        1px solid rgba(255,255,255,.08);

    border-radius: 15px;

    background:
        rgba(255,255,255,.035);

    cursor: pointer;
}}

.search-result:hover {{
    border-color:
        rgba(124, 113, 255, .4);
}}

.search-result-type {{
    color: #7f8cff;

    font-size: 10px;

    font-weight: 900;

    text-transform: uppercase;
}}

.search-result-name {{
    margin-top: 6px;

    font-weight: 900;
}}

.no-results {{
    padding: 30px;

    color: #7e879c;

    border:
        1px dashed rgba(255,255,255,.1);

    border-radius: 15px;
}}

.site-footer {{
    max-width: 1400px;
    margin: auto;

    padding:
        60px 22px
        90px;

    color: #697188;

    text-align: center;

    border-top:
        1px solid
        rgba(255,255,255,.06);
}}


/* ============================================================
   MODAL
   ============================================================ */

.modal {{
    position: fixed;

    inset: 0;

    z-index: 3000;

    display: none;

    align-items: center;
    justify-content: center;

    padding: 20px;

    background:
        rgba(0,0,0,.72);

    backdrop-filter: blur(12px);
}}

.modal.visible {{
    display: flex;
}}

.modal-box {{
    width: min(760px, 100%);

    max-height: 90vh;

    overflow-y: auto;

    border:
        1px solid rgba(255,255,255,.1);

    border-radius: 24px;

    background:
        #0c101b;

    box-shadow:
        0 30px 100px
        rgba(0,0,0,.5);

    padding: 28px;
}}

.modal-close-row {{
    display: flex;

    justify-content: flex-end;
}}

.modal-close {{
    width: 38px;
    height: 38px;

    border: 0;

    border-radius: 10px;

    color: white;

    background:
        rgba(255,255,255,.07);
}}

.modal-icon {{
    font-size: 42px;

    margin-top: 5px;
}}

.modal-title {{
    margin:
        10px 0;

    font-size: 34px;
}}

.modal-type {{
    color: #8d87ff;

    font-size: 11px;

    font-weight: 900;

    text-transform: uppercase;

    letter-spacing: 1.5px;
}}

.modal-description {{
    color: #a1a9bc;

    line-height: 1.8;

    margin-top: 18px;
}}

.modal-meta {{
    display: flex;

    flex-wrap: wrap;

    gap: 8px;

    margin-top: 18px;
}}

.modal-meta span {{
    padding:
        7px 10px;

    border-radius: 9px;

    background:
        rgba(255,255,255,.06);

    color: #aeb6c9;

    font-size: 11px;
}}

.modal-actions {{
    display: flex;

    gap: 10px;

    margin-top: 25px;

    padding-top: 18px;

    border-top:
        1px solid
        rgba(255,255,255,.07);
}}


/* ============================================================
   SCREENSHOT OVERLAY
   ============================================================ */

.screenshot-working {{
    position: fixed;

    inset: 0;

    z-index: 10000;

    display: none;

    align-items: center;
    justify-content: center;

    background:
        rgba(0,0,0,.75);

    backdrop-filter: blur(8px);
}}

.screenshot-working.visible {{
    display: flex;
}}

.screenshot-working-box {{
    padding: 22px 28px;

    border-radius: 16px;

    background:
        #111625;

    border:
        1px solid
        rgba(255,255,255,.1);

    text-align: center;

    box-shadow:
        0 25px 80px
        rgba(0,0,0,.5);
}}

.spinner {{
    width: 34px;
    height: 34px;

    margin:
        0 auto 12px;

    border:
        3px solid
        rgba(255,255,255,.15);

    border-top-color:
        #7d75ff;

    border-radius: 50%;

    animation:
        spin .8s linear infinite;
}}

@keyframes spin {{
    to {{
        transform: rotate(360deg);
    }}
}}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 1100px) {{

    .card-grid {{
        grid-template-columns:
            repeat(3, minmax(0, 1fr));
    }}

    .category-grid {{
        grid-template-columns:
            repeat(3, minmax(0, 1fr));
    }}

    .search-result-list {{
        grid-template-columns:
            repeat(3, minmax(0, 1fr));
    }}
}}

@media (max-width: 800px) {{

    .header-inner {{
        flex-wrap: wrap;
    }}

    .search-wrap {{
        order: 3;

        flex-basis: 100%;

        max-width: none;
    }}

    .hero {{
        grid-template-columns: 1fr;

        padding-top: 60px;
    }}

    .hero-orb-wrap {{
        display: none;
    }}

    .stats {{
        grid-template-columns:
            repeat(2, 1fr);
    }}

    .card-grid {{
        grid-template-columns:
            repeat(2, minmax(0, 1fr));
    }}

    .search-result-list {{
        grid-template-columns:
            repeat(2, minmax(0, 1fr));
    }}

    .category-grid {{
        grid-template-columns:
            repeat(2, minmax(0, 1fr));
    }}
}}

@media (max-width: 520px) {{

    .header-inner {{
        padding: 10px 14px;
    }}

    .hero,
    .content-section,
    .stats,
    .category-grid,
    .search-results {{
        padding-left: 14px;
        padding-right: 14px;
    }}

    .hero h1 {{
        letter-spacing: -2px;
    }}

    .stats {{
        gap: 9px;
    }}

    .stat-card {{
        padding: 16px;
    }}

    .card-grid {{
        grid-template-columns: 1fr;
    }}

    .search-result-list {{
        grid-template-columns: 1fr;
    }}

    .category-grid {{
        grid-template-columns: 1fr;
    }}

    .modal-box {{
        padding: 20px;
    }}

    .modal-title {{
        font-size: 27px;
    }}

}}

</style>

</head>


<body>


<header class="site-header">

    <div class="header-inner">

        <div class="brand">

            <div class="brand-logo">
                ✦
            </div>

            <div>
                <div class="brand-text">
                    {esc(SITE_DATA["name"])}
                </div>

                <div class="brand-subtitle">
                    {esc(SITE_DATA["tagline"])}
                </div>
            </div>

        </div>


        <div class="search-wrap">

            <div class="search-box">

                <span class="search-icon">
                    🔎
                </span>

                <input
                    id="searchInput"
                    type="search"
                    autocomplete="off"
                    placeholder="Search NPCs, worlds, quests, lore..."
                    aria-label="Search"
                >

                <button
                    id="clearSearch"
                    class="clear-search"
                    type="button"
                    onclick="clearSearch()"
                >
                    ✕
                </button>

            </div>

        </div>

    </div>

</header>


<main>


<section class="hero">

    <div>

        <div class="hero-kicker">
            THE EVER-GROWING OMNIVERSE
        </div>

        <h1>
            Explore the
            <span>Unknown.</span>
        </h1>

        <p class="hero-description">
            {esc(SITE_DATA["description"])}
        </p>

        <div class="hero-actions">

            <button
                class="hero-button"
                type="button"
                onclick="document.getElementById('section-npcs').scrollIntoView()"
            >
                Explore NPCs
            </button>

            <button
                class="hero-button secondary"
                type="button"
                onclick="document.getElementById('section-worlds').scrollIntoView()"
            >
                Explore Worlds
            </button>

        </div>

    </div>


    <div class="hero-orb-wrap">

        <div class="hero-orb"></div>

    </div>

</section>


<section class="stats">

    {build_stats_html()}

</section>


<section class="content-section">

    <div class="section-heading">

        <div>

            <div class="section-kicker">
                CATEGORIES
            </div>

            <h2>
                Explore by Type
            </h2>

            <p>
                Jump into a category and discover related entries.
            </p>

        </div>

    </div>

</section>


<div class="category-grid">

    {build_category_html()}

</div>


<section
    id="searchResults"
    class="search-results"
>

    <div class="section-heading">

        <div>

            <div class="section-kicker">
                SEARCH
            </div>

            <h2>
                Search Results
            </h2>

        </div>

    </div>

    <div
        id="searchResultList"
        class="search-result-list"
    ></div>

</section>


{build_collection_section(
    "npcs",
    "Featured NPCs",
    "Characters from across the omniverse."
)}


{build_collection_section(
    "worlds",
    "Worlds",
    "Explore realms, dimensions and civilizations."
)}


{build_collection_section(
    "quests",
    "Quests",
    "Stories, missions and adventures waiting to unfold."
)}


{build_collection_section(
    "posts",
    "Posts & Lore",
    "Additional information from across the omniverse."
)}


</main>


<footer class="site-footer">

    <div>
        ✦ {esc(SITE_DATA["name"])}
    </div>

    <div style="margin-top:8px;">
        {esc(SITE_DATA["tagline"])}
    </div>

</footer>


<!-- ========================================================
     POST MODAL
     ======================================================== -->

<div
    id="postModal"
    class="modal"
    onclick="closeModal(event)"
>

    <div
        class="modal-box"
        onclick="event.stopPropagation()"
    >

        <div class="modal-close-row">

            <button
                class="modal-close"
                type="button"
                onclick="closeModal()"
            >
                ✕
            </button>

        </div>

        <div id="modalContent"></div>

    </div>

</div>


<!-- ========================================================
     SCREENSHOT WORKING OVERLAY
     ======================================================== -->

<div
    id="screenshotWorking"
    class="screenshot-working"
>

    <div class="screenshot-working-box">

        <div class="spinner"></div>

        <div>
            Creating screenshot...
        </div>

    </div>

</div>


<script>

/* ============================================================
   DATA
   ============================================================ */

const SEARCH_ITEMS = {search_json};

const COLLECTION_ICONS = {{
    npcs: "👤",
    worlds: "🌍",
    quests: "⚔️",
    posts: "📜"
}};


/* ============================================================
   ESCAPE HTML
   ============================================================ */

function escapeHTML(value) {{

    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}}


/* ============================================================
   SEARCH
   ============================================================ */

const searchInput =
    document.getElementById("searchInput");

const clearSearchButton =
    document.getElementById("clearSearch");

const searchResults =
    document.getElementById("searchResults");

const searchResultList =
    document.getElementById("searchResultList");


function buildSearchItems() {{

    const seen = new Set();
    const result = [];

    for (const item of SEARCH_ITEMS) {{

        const key =
            `${{item.collection}}:${{item.id}}`;

        if (seen.has(key)) {{
            continue;
        }}

        seen.add(key);

        result.push(item);
    }}

    return result;
}}


const UNIQUE_SEARCH_ITEMS =
    buildSearchItems();


function searchScore(item, query) {{

    const name =
        String(item.name || "").toLowerCase();

    const type =
        String(item.type || "").toLowerCase();

    const description =
        String(item.description || "").toLowerCase();

    const haystack =
        String(item.search || "").toLowerCase();

    let score = 0;

    if (name === query) {{
        score += 1000;
    }}

    if (name.startsWith(query)) {{
        score += 700;
    }}

    if (name.includes(query)) {{
        score += 500;
    }}

    if (type === query) {{
        score += 400;
    }}

    if (description.includes(query)) {{
        score += 100;
    }}

    if (haystack.includes(query)) {{
        score += 50;
    }}

    if (item.collection === "npcs") {{
        score += 20;
    }}

    return score;
}}


function performSearch(query) {{

    query =
        String(query || "")
            .trim()
            .toLowerCase();

    if (!query) {{

        searchResults.classList.remove(
            "visible"
        );

        searchResultList.innerHTML = "";

        clearSearchButton.style.display =
            "none";

        return;
    }}

    clearSearchButton.style.display =
        "block";

    const matches =
        UNIQUE_SEARCH_ITEMS
            .map(item => ({{
                item,
                score: searchScore(
                    item,
                    query
                )
            }}))
            .filter(result => result.score > 0)
            .sort(
                (a, b) =>
                    b.score - a.score
            )
            .slice(0, 50);

    searchResultList.innerHTML = "";

    if (!matches.length) {{

        searchResultList.innerHTML = `
            <div class="no-results">
                No results found for
                <strong>${{escapeHTML(query)}}</strong>.
            </div>
        `;

        searchResults.classList.add(
            "visible"
        );

        return;
    }}

    const seen = new Set();

    for (const result of matches) {{

        const item = result.item;

        const key =
            `${{item.collection}}:${{item.id}}`;

        if (seen.has(key)) {{
            continue;
        }}

        seen.add(key);

        const div =
            document.createElement("div");

        div.className =
            "search-result";

        div.innerHTML = `
            <div class="search-result-type">
                ${{escapeHTML(item.type)}}
            </div>

            <div class="search-result-name">
                ${{escapeHTML(item.name)}}
            </div>
        `;

        div.addEventListener(
            "click",
            () =>
                openPost(
                    item.id,
                    item.collection
                )
        );

        searchResultList.appendChild(div);
    }}

    searchResults.classList.add(
        "visible"
    );
}}


searchInput.addEventListener(
    "input",
    event =>
        performSearch(
            event.target.value
        )
);


searchInput.addEventListener(
    "keydown",
    event => {{

        if (event.key === "Enter") {{

            const first =
                searchResultList
                    .querySelector(
                        ".search-result"
                    );

            if (first) {{
                first.click();
            }}
        }}

        if (event.key === "Escape") {{
            clearSearch();
            closeModal();
        }}
    }}
);


function clearSearch() {{

    searchInput.value = "";

    performSearch("");

    searchInput.focus();
}}


function searchCategory(category) {{

    searchInput.value = category;

    performSearch(category);

    searchResults.scrollIntoView({{
        behavior: "smooth",
        block: "start"
    }});
}}


/* ============================================================
   POST LOOKUP
   ============================================================ */

function findPost(id, collection) {{

    return UNIQUE_SEARCH_ITEMS.find(
        item =>
            item.id === id &&
            item.collection === collection
    );
}}


/* ============================================================
   OPEN POST
   ============================================================ */

function openPost(id, collection) {{

    const item =
        findPost(id, collection);

    if (!item) {{
        return;
    }}

    const icon =
        COLLECTION_ICONS[
            collection
        ] || "📜";

    const card =
        document.getElementById(
            `card-${{CSS.escape(id)}}`
        );

    let originalItem = null;

    if (card) {{

        try {{

            const data =
                card.dataset
                    .screenshotData;

            if (data) {{
                originalItem =
                    JSON.parse(data);
            }}

        }} catch (error) {{
            console.warn(
                "Could not read post metadata.",
                error
            );
        }}
    }}

    const meta =
        originalItem?.meta || "";

    const tags =
        originalItem?.tags || [];

    const tagsHTML =
        Array.isArray(tags)
            ? tags
                .map(
                    tag =>
                        `<span>${{
                            escapeHTML(tag)
                        }}</span>`
                )
                .join("")
            : "";

    document.getElementById(
        "modalContent"
    ).innerHTML = `

        <div class="modal-icon">
            ${{icon}}
        </div>

        <div class="modal-type">
            ${{escapeHTML(item.type)}}
        </div>

        <h2 class="modal-title">
            ${{escapeHTML(item.name)}}
        </h2>

        <div class="modal-meta">
            ${{meta}}
        </div>

        <p class="modal-description">
            ${{escapeHTML(item.description)}}
        </p>

        <div class="modal-meta">
            ${{tagsHTML}}
        </div>

        <div class="modal-actions">

            <button
                class="card-action screenshot-button"
                type="button"
                onclick="
                    screenshotPost(
                        '${{escapeHTML(item.id)}}'
                    )
                "
            >
                📸 Screenshot Post
            </button>

        </div>
    `;

    document
        .getElementById("postModal")
        .classList.add("visible");

    document.body.style.overflow =
        "hidden";
}}


/* ============================================================
   CLOSE MODAL
   ============================================================ */

function closeModal(event) {{

    if (
        event &&
        event.target !== event.currentTarget
    ) {{
        return;
    }}

    document
        .getElementById("postModal")
        .classList.remove("visible");

    document.body.style.overflow = "";
}}


/* ============================================================
   SCREENSHOT SYSTEM
   ============================================================

   This function creates a standalone SVG image containing
   the selected post.

   SVG is converted to PNG using Canvas.

   Therefore:
   - no server
   - no database
   - no external screenshot API
   - no login
   - no localStorage
   ============================================================ */

async function screenshotPost(id) {{

    const card =
        document.getElementById(
            `card-${{CSS.escape(id)}}`
        );

    if (!card) {{
        alert(
            "Could not find this post."
        );
        return;
    }}

    let data = null;

    try {{

        data = JSON.parse(
            card.dataset.screenshotData
        );

    }} catch (error) {{

        console.error(error);

        alert(
            "Could not prepare this post for screenshot."
        );

        return;
    }}

    const overlay =
        document.getElementById(
            "screenshotWorking"
        );

    overlay.classList.add(
        "visible"
    );

    try {{

        const pngBlob =
            await createPostPNG(data);

        const url =
            URL.createObjectURL(
                pngBlob
            );

        const link =
            document.createElement("a");

        const safeName =
            String(
                data.name || "post"
            )
                .trim()
                .toLowerCase()
                .replace(
                    /[^a-z0-9]+/g,
                    "-"
                )
                .replace(
                    /^-+|-+$/g,
                    ""
                ) || "post";

        link.href = url;

        link.download =
            `npcbook-${{safeName}}.png`;

        document.body.appendChild(link);

        link.click();

        link.remove();

        setTimeout(
            () =>
                URL.revokeObjectURL(url),
            1500
        );

    }} catch (error) {{

        console.error(
            "Screenshot error:",
            error
        );

        alert(
            "Unable to create screenshot."
        );

    }} finally {{

        overlay.classList.remove(
            "visible"
        );
    }}
}}


/* ============================================================
   CREATE PNG
   ============================================================ */

function createPostPNG(data) {{

    return new Promise(
        (resolve, reject) => {{

            const width = 1200;

            const padding = 70;

            const title =
                String(
                    data.name || "Untitled"
                );

            const type =
                String(
                    data.type || "Post"
                );

            const description =
                String(
                    data.description || ""
                );

            const tags =
                Array.isArray(data.tags)
                    ? data.tags
                    : [];

            const metaHTML =
                String(
                    data.meta || ""
                );

            /*
             * Convert HTML metadata into
             * plain readable text.
             */

            const temp =
                document.createElement(
                    "div"
                );

            temp.innerHTML =
                metaHTML;

            const metaText =
                temp.textContent
                    .replace(/\\s+/g, " ")
                    .trim();

            const wrappedDescription =
                wrapText(
                    description,
                    82
                );

            const wrappedTitle =
                wrapText(
                    title,
                    34
                );

            const lineHeight = 32;

            const titleHeight =
                wrappedTitle.length *
                62;

            const descriptionHeight =
                wrappedDescription.length *
                lineHeight;

            const tagRows =
                Math.max(
                    1,
                    Math.ceil(
                        tags.length / 5
                    )
                );

            const height =
                470 +
                titleHeight +
                descriptionHeight +
                tagRows * 48;

            const svg =
                createPostSVG({{
                    width,
                    height,
                    titleLines:
                        wrappedTitle,
                    descriptionLines:
                        wrappedDescription,
                    type,
                    metaText,
                    tags
                }});

            const svgBlob =
                new Blob(
                    [svg],
                    {{
                        type:
                            "image/svg+xml;charset=utf-8"
                    }}
                );

            const url =
                URL.createObjectURL(
                    svgBlob
                );

            const image =
                new Image();

            image.onload = () => {{

                const canvas =
                    document.createElement(
                        "canvas"
                    );

                canvas.width =
                    width * 2;

                canvas.height =
                    height * 2;

                const ctx =
                    canvas.getContext(
                        "2d"
                    );

                ctx.scale(2, 2);

                ctx.drawImage(
                    image,
                    0,
                    0,
                    width,
                    height
                );

                canvas.toBlob(
                    blob => {{

                        URL.revokeObjectURL(
                            url
                        );

                        if (!blob) {{
                            reject(
                                new Error(
                                    "PNG creation failed."
                                )
                            );
                            return;
                        }}

                        resolve(blob);
                    }},
                    "image/png",
                    1
                );
            }};

            image.onerror =
                error => {{

                    URL.revokeObjectURL(
                        url
                    );

                    reject(error);
                }};

            image.src = url;
        }}
    );
}}


/* ============================================================
   TEXT WRAPPING
   ============================================================ */

function wrapText(text, maxCharacters) {{

    const words =
        String(text || "")
            .split(/\\s+/);

    const lines = [];

    let line = "";

    for (const word of words) {{

        const test =
            line
                ? `${{line}} ${{word}}`
                : word;

        if (
            test.length >
            maxCharacters
        ) {{

            if (line) {{
                lines.push(line);
            }}

            line = word;

        }} else {{

            line = test;
        }}
    }}

    if (line) {{
        lines.push(line);
    }}

    return lines.length
        ? lines
        : [""];
}}


/* ============================================================
   SVG GENERATOR
   ============================================================ */

function createPostSVG(data) {{

    const {{
        width,
        height,
        titleLines,
        descriptionLines,
        type,
        metaText,
        tags
    }} = data;

    const escXML =
        value =>
            String(value ?? "")
                .replaceAll("&", "&amp;")
                .replaceAll("<", "&lt;")
                .replaceAll(">", "&gt;")
                .replaceAll('"', "&quot;")
                .replaceAll("'", "&apos;");

    const titleSVG =
        titleLines
            .map(
                (line, index) =>
                    `
                    <text
                        x="70"
                        y="${{
                            195 +
                            index * 62
                        }}"
                        fill="#ffffff"
                        font-family="Arial, sans-serif"
                        font-size="48"
                        font-weight="800"
                    >
                        ${{escXML(line)}}
                    </text>
                    `
            )
            .join("");

    const titleBottom =
        195 +
        titleLines.length * 62;

    const metaY =
        titleBottom + 15;

    const descriptionStart =
        metaY + 75;

    const descriptionSVG =
        descriptionLines
            .map(
                (line, index) =>
                    `
                    <text
                        x="70"
                        y="${{
                            descriptionStart +
                            index * 32
                        }}"
                        fill="#aeb7ca"
                        font-family="Arial, sans-serif"
                        font-size="23"
                    >
                        ${{escXML(line)}}
                    </text>
                    `
            )
            .join("");

    const descriptionBottom =
        descriptionStart +
        descriptionLines.length *
        32;

    let tagsSVG = "";

    let tagX = 70;

    let tagY =
        descriptionBottom + 42;

    for (
        let index = 0;
        index < tags.length;
        index++
    ) {{

        const tag =
            String(tags[index]);

        const tagWidth =
            Math.min(
                190,
                Math.max(
                    90,
                    tag.length * 12 + 38
                )
            );

        if (
            tagX +
            tagWidth >
            width - 70
        ) {{

            tagX = 70;

            tagY += 48;
        }}

        tagsSVG += `
            <rect
                x="${{tagX}}"
                y="${{tagY}}"
                width="${{tagWidth}}"
                height="34"
                rx="9"
                fill="#171d31"
                stroke="#303951"
            />

            <text
                x="${{
                    tagX + 17
                }}"
                y="${{
                    tagY + 23
                }}"
                fill="#aeb6ff"
                font-family="Arial, sans-serif"
                font-size="15"
            >
                ${{escXML(tag)}}
            </text>
        `;

        tagX +=
            tagWidth + 10;
    }}

    const footerY =
        height - 55;

    return `
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="${{width}}"
    height="${{height}}"
    viewBox="0 0 ${{width}} ${{height}}"
>

    <defs>

        <linearGradient
            id="bg"
            x1="0"
            y1="0"
            x2="1"
            y2="1"
        >

            <stop
                offset="0%"
                stop-color="#080b14"
            />

            <stop
                offset="100%"
                stop-color="#10182a"
            />

        </linearGradient>

        <linearGradient
            id="accent"
            x1="0"
            y1="0"
            x2="1"
            y2="0"
        >

            <stop
                offset="0%"
                stop-color="#776aff"
            />

            <stop
                offset="100%"
                stop-color="#36d6ff"
            />

        </linearGradient>

        <radialGradient
            id="glow"
            cx="50%"
            cy="20%"
            r="70%"
        >

            <stop
                offset="0%"
                stop-color="#5750ff"
                stop-opacity=".25"
            />

            <stop
                offset="100%"
                stop-color="#5750ff"
                stop-opacity="0"
            />

        </radialGradient>

    </defs>


    <rect
        width="${{width}}"
        height="${{height}}"
        fill="url(#bg)"
    />

    <rect
        width="${{width}}"
        height="${{height}}"
        fill="url(#glow)"
    />


    <rect
        x="45"
        y="45"
        width="${{
            width - 90
        }}"
        height="${{
            height - 90
        }}"
        rx="30"
        fill="#0b101d"
        stroke="#293148"
        stroke-width="2"
    />


    <rect
        x="70"
        y="70"
        width="80"
        height="7"
        rx="4"
        fill="url(#accent)"
    />


    <text
        x="70"
        y="125"
        fill="#8d88ff"
        font-family="Arial, sans-serif"
        font-size="17"
        font-weight="800"
        letter-spacing="3"
    >
        ${{escXML(type.toUpperCase())}}
    </text>


    ${{titleSVG}}


    <text
        x="70"
        y="${{metaY + 35}}"
        fill="#7f8ba4"
        font-family="Arial, sans-serif"
        font-size="17"
    >
        ${{escXML(metaText || "NPC OMNIVERSE")}}
    </text>


    <line
        x1="70"
        y1="${{
            metaY + 60
        }}"
        x2="${{
            width - 70
        }}"
        y2="${{
            metaY + 60
        }}"
        stroke="#242c40"
    />


    ${{descriptionSVG}}


    ${{tagsSVG}}


    <text
        x="${{
            width - 70
        }}"
        y="${{footerY}}"
        text-anchor="end"
        fill="#657087"
        font-family="Arial, sans-serif"
        font-size="16"
        font-weight="700"
    >
        NPC OMNIVERSE
    </text>


    <text
        x="70"
        y="${{footerY}}"
        fill="#4f596f"
        font-family="Arial, sans-serif"
        font-size="14"
    >
        Explore. Create. Discover.
    </text>

</svg>
`;
}}


/* ============================================================
   KEYBOARD SHORTCUT
   ============================================================ */

document.addEventListener(
    "keydown",
    event => {{

        if (
            event.key === "/" &&
            document.activeElement !==
                searchInput
        ) {{

            event.preventDefault();

            searchInput.focus();
        }}

        if (event.key === "Escape") {{
            closeModal();
        }}
    }}
);

</script>

</body>
</html>
"""


# ============================================================
# ROBOTS
# ============================================================

def build_robots():
    base_url = SITE_DATA["url"].rstrip("/")

    return f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""


# ============================================================
# SITEMAP
# ============================================================

def build_sitemap():
    base_url = SITE_DATA["url"].rstrip("/")

    urls = [
        base_url + "/"
    ]

    for collection in [
        "npcs",
        "worlds",
        "quests",
        "posts",
    ]:
        for item in SITE_DATA.get(collection, []):
            urls.append(
                base_url
                + "/#card-"
                + item["id"]
            )

    unique_urls = []

    seen = set()

    for url in urls:
        if url in seen:
            continue

        seen.add(url)
        unique_urls.append(url)

    url_entries = []

    for url in unique_urls:
        url_entries.append(
            f"""
    <url>
        <loc>{esc(url)}</loc>
    </url>
"""
        )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
>
{"".join(url_entries)}
</urlset>
"""


# ============================================================
# WEB MANIFEST
# ============================================================

def build_manifest():
    return json.dumps(
        {
            "name": SITE_DATA["name"],
            "short_name": "NPCBook",
            "description": SITE_DATA["description"],
            "start_url": "/",
            "display": "standalone",
            "background_color": "#070910",
            "theme_color": "#080b14",
            "lang": SITE_DATA["language"],
            "icons": [],
        },
        ensure_ascii=False,
        indent=2,
    )


# ============================================================
# BUILD
# ============================================================

def build_site():
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    INDEX_FILE.write_text(
        build_html(),
        encoding="utf-8",
    )

    ROBOTS_FILE.write_text(
        build_robots(),
        encoding="utf-8",
    )

    SITEMAP_FILE.write_text(
        build_sitemap(),
        encoding="utf-8",
    )

    MANIFEST_FILE.write_text(
        build_manifest(),
        encoding="utf-8",
    )

    print()
    print("=" * 60)
    print("NPC OMNIVERSE BUILD COMPLETE")
    print("=" * 60)
    print()
    print(f"Output directory : {OUTPUT_DIR}")
    print(f"HTML             : {INDEX_FILE}")
    print(f"Robots           : {ROBOTS_FILE}")
    print(f"Sitemap          : {SITEMAP_FILE}")
    print(f"Manifest         : {MANIFEST_FILE}")
    print()
    print(
        "Unique NPCs      :",
        len(SITE_DATA.get("npcs", []))
    )
    print(
        "Unique Worlds    :",
        len(SITE_DATA.get("worlds", []))
    )
    print(
        "Unique Quests    :",
        len(SITE_DATA.get("quests", []))
    )
    print(
        "Unique Posts     :",
        len(SITE_DATA.get("posts", []))
    )
    print()
    print(
        "Every content card automatically has:"
    )
    print("  - View")
    print("  - Screenshot Post")
    print("  - PNG export")
    print("  - Duplicate protection")
    print("  - Search integration")
    print()
    print("=" * 60)


if __name__ == "__main__":
    build_site()
