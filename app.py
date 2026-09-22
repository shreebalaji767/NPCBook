from flask import Flask, render_template_string, jsonify, request
import random
import html

app = Flask(__name__)

# ============================================================
# NPC OMNIVERSE
# Single-file Flask application
# No database
# No localStorage
# Temporary in-memory data
# ============================================================

NPCS = [
    {
        "id": 1,
        "name": "Kael Veyron",
        "role": "Void Cartographer",
        "world": "Eclipse Realm",
        "level": 42,
        "online": True,
        "avatar": "https://i.pravatar.cc/150?img=12",
        "bio": "Maps places that should not exist."
    },
    {
        "id": 2,
        "name": "Mira Solen",
        "role": "Sky Mechanic",
        "world": "Aetheria",
        "level": 28,
        "online": True,
        "avatar": "https://i.pravatar.cc/150?img=47",
        "bio": "Repairs airships above the endless clouds."
    },
    {
        "id": 3,
        "name": "Rook",
        "role": "Wandering Mercenary",
        "world": "Iron Frontier",
        "level": 35,
        "online": False,
        "avatar": "https://i.pravatar.cc/150?img=68",
        "bio": "Never asks who started the war."
    },
    {
        "id": 4,
        "name": "Nyx Arclight",
        "role": "Dream Hacker",
        "world": "Neon Metropolis",
        "level": 51,
        "online": True,
        "avatar": "https://i.pravatar.cc/150?img=32",
        "bio": "Breaks into dreams instead of computers."
    },
    {
        "id": 5,
        "name": "Elder Varo",
        "role": "Time Keeper",
        "world": "Chronos",
        "level": 77,
        "online": False,
        "avatar": "https://i.pravatar.cc/150?img=53",
        "bio": "Claims he remembers tomorrow."
    },
]

WORLDS = [
    {
        "id": 1,
        "name": "Eclipse Realm",
        "type": "Dark Fantasy",
        "population": "8.4M NPCs",
        "color": "purple",
        "description": "A world where ancient kingdoms fight creatures from beyond reality."
    },
    {
        "id": 2,
        "name": "Aetheria",
        "type": "Sky Civilization",
        "population": "3.1M NPCs",
        "color": "blue",
        "description": "Floating cities, sky pirates and enormous mechanical airships."
    },
    {
        "id": 3,
        "name": "Iron Frontier",
        "type": "Post-Apocalyptic",
        "population": "1.8M NPCs",
        "color": "orange",
        "description": "Human settlements survive between ruined megacities."
    },
    {
        "id": 4,
        "name": "Neon Metropolis",
        "type": "Cyberpunk",
        "population": "12.7M NPCs",
        "color": "pink",
        "description": "A gigantic city controlled by corporations and artificial intelligence."
    },
    {
        "id": 5,
        "name": "Chronos",
        "type": "Time Fantasy",
        "population": "???",
        "color": "green",
        "description": "Past, present and future exist simultaneously."
    },
]

POSTS = [
    {
        "id": 1,
        "npc": "Kael Veyron",
        "role": "Void Cartographer",
        "avatar": "https://i.pravatar.cc/150?img=12",
        "world": "Eclipse Realm",
        "time": "12 min ago",
        "text": "I found a road beneath the old cathedral. It wasn't there yesterday.",
        "likes": 284,
        "comments": 41,
        "reposts": 18,
        "tag": "DISCOVERY"
    },
    {
        "id": 2,
        "npc": "Mira Solen",
        "role": "Sky Mechanic",
        "avatar": "https://i.pravatar.cc/150?img=47",
        "world": "Aetheria",
        "time": "28 min ago",
        "text": "The western engines are finally working again. If anyone asks, that explosion was completely intentional.",
        "likes": 721,
        "comments": 83,
        "reposts": 96,
        "tag": "AETHERIA"
    },
    {
        "id": 3,
        "npc": "Nyx Arclight",
        "role": "Dream Hacker",
        "avatar": "https://i.pravatar.cc/150?img=32",
        "world": "Neon Metropolis",
        "time": "1 hr ago",
        "text": "Someone uploaded a memory from a person who hasn't been born yet.",
        "likes": 1342,
        "comments": 219,
        "reposts": 307,
        "tag": "ANOMALY"
    },
    {
        "id": 4,
        "npc": "Rook",
        "role": "Wandering Mercenary",
        "avatar": "https://i.pravatar.cc/150?img=68",
        "world": "Iron Frontier",
        "time": "2 hrs ago",
        "text": "Three settlements. Two armies. One water source. This is going to be a long week.",
        "likes": 497,
        "comments": 66,
        "reposts": 31,
        "tag": "FRONTIER"
    },
]

QUESTS = [
    {
        "name": "The Missing Cartographer",
        "world": "Eclipse Realm",
        "difficulty": "Hard",
        "reward": "4,500 XP"
    },
    {
        "name": "Repair the Sky Engine",
        "world": "Aetheria",
        "difficulty": "Medium",
        "reward": "2,800 XP"
    },
    {
        "name": "The Neon Memory",
        "world": "Neon Metropolis",
        "difficulty": "Extreme",
        "reward": "8,000 XP"
    },
    {
        "name": "Water War",
        "world": "Iron Frontier",
        "difficulty": "Hard",
        "reward": "5,200 XP"
    },
]

MARKET = [
    ("Void Compass", "Eclipse Realm", "2,400"),
    ("Aether Engine Core", "Aetheria", "8,900"),
    ("Rustbreaker Rifle", "Iron Frontier", "4,100"),
    ("Dream Shard", "Neon Metropolis", "6,700"),
    ("Chrono Crystal", "Chronos", "12,500"),
]


def safe(value):
    return html.escape(str(value))


@app.route("/")
def index():
    return render_template_string(PAGE)


@app.route("/api/npcs")
def api_npcs():
    return jsonify(NPCS)


@app.route("/api/worlds")
def api_worlds():
    return jsonify(WORLDS)


@app.route("/api/posts")
def api_posts():
    return jsonify(POSTS)


@app.route("/api/quests")
def api_quests():
    return jsonify(QUESTS)


@app.route("/api/generate/npc", methods=["POST"])
def generate_npc():
    names = [
        "Aeris Vonn",
        "Drax",
        "Selene Korr",
        "Vex",
        "Orin Vale",
        "Luna Ash",
        "Tarin",
        "Zera Quinn",
    ]

    roles = [
        "Rogue Engineer",
        "Forbidden Mage",
        "Starship Captain",
        "Dream Merchant",
        "Ancient Guardian",
        "Cyber Detective",
        "Time Traveler",
        "Shadow Assassin",
    ]

    worlds = [w["name"] for w in WORLDS]

    npc = {
        "id": len(NPCS) + 1,
        "name": random.choice(names),
        "role": random.choice(roles),
        "world": random.choice(worlds),
        "level": random.randint(1, 99),
        "online": True,
        "avatar": f"https://i.pravatar.cc/150?img={random.randint(1, 70)}",
        "bio": "A newly generated resident of the NPC Omniverse."
    }

    NPCS.append(npc)

    return jsonify(npc)


@app.route("/api/generate/world", methods=["POST"])
def generate_world():
    world_types = [
        "Dark Fantasy",
        "Cyberpunk",
        "Space Opera",
        "Post-Apocalyptic",
        "Mystical",
        "Steampunk",
        "Time Fantasy",
        "Alien Civilization",
    ]

    names = [
        "Veyra",
        "Astralis",
        "Nexora",
        "Valthera",
        "Oblivion",
        "Solara",
        "Eldoria",
        "Zenith",
    ]

    world = {
        "id": len(WORLDS) + 1,
        "name": random.choice(names) + " " + random.choice(
            ["Prime", "Frontier", "Realm", "Sector", "System"]
        ),
        "type": random.choice(world_types),
        "population": f"{random.randint(1, 30)}.{random.randint(1,9)}M NPCs",
        "color": random.choice(["purple", "blue", "pink", "green", "orange"]),
        "description": "A newly generated universe waiting for its first story."
    }

    WORLDS.append(world)

    return jsonify(world)


@app.route("/api/post", methods=["POST"])
def create_post():
    data = request.get_json() or {}

    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Post cannot be empty"}), 400

    post = {
        "id": len(POSTS) + 1,
        "npc": "You",
        "role": "Omniverse Traveler",
        "avatar": "https://i.pravatar.cc/150?img=11",
        "world": "Omniverse",
        "time": "just now",
        "text": text,
        "likes": 0,
        "comments": 0,
        "reposts": 0,
        "tag": "NEW"
    }

    POSTS.insert(0, post)

    return jsonify(post)


PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0, viewport-fit=cover"
>

<meta
    name="description"
    content="NPC OMNIVERSE — A living social universe for NPCs."
>

<title>NPC OMNIVERSE</title>

<style>

/* ============================================================
   RESET
============================================================ */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --bg: #07080d;
    --panel: #10121a;
    --panel2: #151824;
    --panel3: #1b1f2b;
    --border: rgba(255,255,255,.08);

    --text: #f4f6fb;
    --muted: #9298aa;

    --accent: #8b5cf6;
    --accent2: #06b6d4;
    --pink: #ec4899;
    --green: #22c55e;
    --orange: #f59e0b;

    --radius: 18px;
    --max: 1500px;
}

html {
    scroll-behavior: smooth;
}

body {
    background:
        radial-gradient(circle at 20% 0%, rgba(139,92,246,.12), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(6,182,212,.08), transparent 25%),
        var(--bg);

    color: var(--text);
    font-family:
        Inter,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    min-height: 100vh;
}

button,
input,
textarea {
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
   APP
============================================================ */

.app {
    width: min(100%, var(--max));
    margin: auto;
    min-height: 100vh;
}

/* ============================================================
   TOPBAR
============================================================ */

.topbar {
    height: 70px;
    position: sticky;
    top: 0;
    z-index: 100;

    display: flex;
    align-items: center;
    gap: 18px;

    padding: 0 20px;

    background: rgba(7,8,13,.82);
    backdrop-filter: blur(20px);

    border-bottom: 1px solid var(--border);
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;

    min-width: 245px;
}

.logo-icon {
    width: 40px;
    height: 40px;

    display: grid;
    place-items: center;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            var(--accent),
            var(--accent2)
        );

    box-shadow:
        0 0 25px rgba(139,92,246,.35);

    font-size: 21px;
}

.logo strong {
    font-size: 17px;
    letter-spacing: .5px;
}

.logo span {
    display: block;
    color: var(--muted);
    font-size: 11px;
    margin-top: 2px;
}

.search {
    flex: 1;
    max-width: 650px;
    position: relative;
}

.search input {
    width: 100%;
    height: 42px;

    border: 1px solid var(--border);
    border-radius: 14px;

    background: var(--panel);

    color: var(--text);

    padding: 0 15px 0 42px;

    outline: none;
}

.search input:focus {
    border-color: rgba(139,92,246,.6);
}

.search-icon {
    position: absolute;
    left: 15px;
    top: 50%;

    transform: translateY(-50%);

    color: var(--muted);
}

.top-actions {
    margin-left: auto;

    display: flex;
    align-items: center;
    gap: 8px;
}

.icon-btn {
    width: 40px;
    height: 40px;

    display: grid;
    place-items: center;

    border: 1px solid var(--border);
    border-radius: 12px;

    background: var(--panel);
    color: var(--text);
}

.icon-btn:hover {
    border-color: var(--accent);
}

/* ============================================================
   LAYOUT
============================================================ */

.layout {
    display: grid;

    grid-template-columns:
        230px
        minmax(0, 1fr)
        300px;

    gap: 18px;

    padding: 18px;
}

/* ============================================================
   SIDEBAR
============================================================ */

.sidebar {
    position: sticky;
    top: 88px;
    height: calc(100vh - 105px);

    display: flex;
    flex-direction: column;
    gap: 16px;
}

.nav-card,
.widget,
.card {
    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.025),
            rgba(255,255,255,.012)
        ),
        var(--panel);

    border: 1px solid var(--border);
    border-radius: var(--radius);
}

.nav-card {
    padding: 10px;
}

.nav-item {
    width: 100%;

    display: flex;
    align-items: center;
    gap: 12px;

    padding: 12px;

    border: 0;
    border-radius: 12px;

    background: transparent;
    color: var(--muted);

    text-align: left;
}

.nav-item:hover,
.nav-item.active {
    background: rgba(139,92,246,.13);
    color: var(--text);
}

.nav-item .nav-icon {
    width: 22px;
    text-align: center;
}

.side-generate {
    padding: 16px;
}

.side-generate h3 {
    font-size: 14px;
    margin-bottom: 7px;
}

.side-generate p {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.5;
    margin-bottom: 14px;
}

/* ============================================================
   BUTTONS
============================================================ */

.btn {
    border: 0;

    border-radius: 12px;

    padding: 10px 14px;

    color: white;

    background: var(--panel3);

    border: 1px solid var(--border);
}

.btn:hover {
    border-color: rgba(255,255,255,.2);
}

.btn-primary {
    background:
        linear-gradient(
            135deg,
            var(--accent),
            #6366f1
        );

    border: 0;
}

.btn-cyan {
    background:
        linear-gradient(
            135deg,
            var(--accent2),
            #0891b2
        );

    border: 0;
}

.btn-full {
    width: 100%;
}

/* ============================================================
   MAIN
============================================================ */

.main {
    min-width: 0;
}

.page {
    display: none;
}

.page.active {
    display: block;
}

.page-header {
    margin-bottom: 16px;
}

.page-header h1 {
    font-size: clamp(22px, 4vw, 30px);
    margin-bottom: 6px;
}

.page-header p {
    color: var(--muted);
    font-size: 14px;
}

/* ============================================================
   HERO
============================================================ */

.hero {
    position: relative;
    overflow: hidden;

    padding: 26px;

    margin-bottom: 16px;

    border-radius: 22px;

    background:
        radial-gradient(
            circle at 80% 20%,
            rgba(6,182,212,.18),
            transparent 25%
        ),
        radial-gradient(
            circle at 10% 90%,
            rgba(139,92,246,.2),
            transparent 30%
        ),
        var(--panel);

    border: 1px solid var(--border);
}

.hero h1 {
    font-size: clamp(28px, 5vw, 44px);
    line-height: 1;
    margin-bottom: 12px;
}

.gradient-text {
    background:
        linear-gradient(
            90deg,
            #a78bfa,
            #22d3ee,
            #f472b6
        );

    -webkit-background-clip: text;
    color: transparent;
}

.hero p {
    color: var(--muted);
    max-width: 650px;
    line-height: 1.6;
}

.hero-actions {
    display: flex;
    gap: 9px;
    flex-wrap: wrap;
    margin-top: 20px;
}

/* ============================================================
   COMPOSER
============================================================ */

.composer {
    padding: 16px;
    margin-bottom: 16px;
}

.composer-top {
    display: flex;
    gap: 12px;
}

.avatar {
    width: 44px;
    height: 44px;

    border-radius: 50%;

    object-fit: cover;

    border: 2px solid rgba(139,92,246,.4);
}

.composer textarea {
    flex: 1;

    min-height: 80px;

    resize: vertical;

    border: 0;
    outline: 0;

    background: transparent;
    color: var(--text);

    padding: 6px;

    font-size: 14px;
}

.composer-bottom {
    display: flex;
    justify-content: flex-end;
    margin-top: 8px;
}

/* ============================================================
   POST
============================================================ */

.post {
    padding: 17px;
    margin-bottom: 14px;
}

.post-head {
    display: flex;
    align-items: center;
    gap: 11px;
}

.post-user {
    flex: 1;
}

.post-user strong {
    font-size: 14px;
}

.post-user small {
    display: block;
    color: var(--muted);
    font-size: 11px;
    margin-top: 2px;
}

.post-tag {
    padding: 5px 8px;

    border-radius: 8px;

    background: rgba(139,92,246,.1);

    color: #b9a3ff;

    font-size: 9px;
    font-weight: 800;
    letter-spacing: .7px;
}

.post-body {
    padding: 15px 0 12px 55px;

    font-size: 14px;
    line-height: 1.65;
}

.post-meta {
    color: var(--muted);
    font-size: 11px;
    margin-bottom: 12px;
}

.post-actions {
    display: grid;
    grid-template-columns: repeat(4,1fr);

    border-top: 1px solid var(--border);

    padding-top: 10px;
}

.post-action {
    border: 0;
    background: transparent;
    color: var(--muted);

    padding: 9px;

    border-radius: 10px;
}

.post-action:hover {
    background: rgba(255,255,255,.04);
    color: var(--text);
}

/* ============================================================
   GRID CARDS
============================================================ */

.grid {
    display: grid;
    grid-template-columns: repeat(2,minmax(0,1fr));
    gap: 14px;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3,minmax(0,1fr));
    gap: 14px;
}

.world-card,
.npc-card,
.quest-card,
.market-card {
    padding: 17px;
}

.world-cover {
    height: 105px;

    border-radius: 14px;

    margin-bottom: 13px;

    background:
        radial-gradient(
            circle at 20% 30%,
            rgba(255,255,255,.25),
            transparent 15%
        ),
        linear-gradient(
            135deg,
            rgba(139,92,246,.75),
            rgba(6,182,212,.4)
        );
}

.world-card:nth-child(2) .world-cover {
    background:
        linear-gradient(
            135deg,
            rgba(6,182,212,.7),
            rgba(59,130,246,.25)
        );
}

.world-card:nth-child(3) .world-cover {
    background:
        linear-gradient(
            135deg,
            rgba(245,158,11,.7),
            rgba(120,53,15,.3)
        );
}

.world-card:nth-child(4) .world-cover {
    background:
        linear-gradient(
            135deg,
            rgba(236,72,153,.7),
            rgba(79,70,229,.3)
        );
}

.world-card h3,
.npc-card h3,
.quest-card h3,
.market-card h3 {
    font-size: 15px;
    margin-bottom: 5px;
}

.card-muted {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.5;
}

.card-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;

    margin-top: 14px;
}

.pill {
    display: inline-flex;

    padding: 5px 8px;

    border-radius: 8px;

    background: rgba(255,255,255,.05);

    color: var(--muted);

    font-size: 10px;
}

.online {
    width: 8px;
    height: 8px;

    display: inline-block;

    border-radius: 50%;

    background: var(--green);

    box-shadow: 0 0 10px var(--green);
}

/* ============================================================
   NPC CARD
============================================================ */

.npc-card {
    display: flex;
    gap: 12px;
}

.npc-card .avatar {
    width: 52px;
    height: 52px;
}

.npc-info {
    min-width: 0;
}

.npc-info h3 {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.npc-status {
    display: flex;
    gap: 6px;
    align-items: center;
    margin-top: 6px;
}

/* ============================================================
   RIGHT PANEL
============================================================ */

.rightbar {
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.widget {
    padding: 16px;
}

.widget-title {
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin-bottom: 13px;
}

.widget-title strong {
    font-size: 14px;
}

.widget-title span {
    color: var(--muted);
    font-size: 11px;
}

.trend {
    padding: 11px 0;
    border-bottom: 1px solid var(--border);
}

.trend:last-child {
    border-bottom: 0;
}

.trend small {
    color: var(--muted);
    font-size: 10px;
}

.trend strong {
    display: block;
    margin: 4px 0;
    font-size: 13px;
}

.trend span {
    color: var(--muted);
    font-size: 10px;
}

/* ============================================================
   PROFILE
============================================================ */

.profile-cover {
    height: 180px;

    border-radius: 20px 20px 0 0;

    background:
        radial-gradient(
            circle at 20% 30%,
            rgba(255,255,255,.2),
            transparent 15%
        ),
        linear-gradient(
            135deg,
            #312e81,
            #7c3aed,
            #0891b2
        );
}

.profile-body {
    padding: 0 20px 20px;
}

.profile-avatar {
    width: 90px;
    height: 90px;

    border-radius: 50%;

    object-fit: cover;

    border: 4px solid var(--panel);

    margin-top: -45px;

    position: relative;
}

.profile-body h1 {
    margin-top: 10px;
    font-size: 25px;
}

.profile-role {
    color: var(--muted);
    margin-top: 3px;
}

.profile-bio {
    margin-top: 14px;
    color: #c4c8d3;
    line-height: 1.6;
    font-size: 14px;
}

.stats {
    display: flex;
    gap: 25px;
    margin-top: 18px;
}

.stat strong {
    display: block;
    font-size: 18px;
}

.stat span {
    color: var(--muted);
    font-size: 11px;
}

/* ============================================================
   EMPTY / LOADING
============================================================ */

.empty {
    padding: 45px 20px;

    text-align: center;

    color: var(--muted);
}

.empty-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

/* ============================================================
   MODAL
============================================================ */

.modal {
    position: fixed;
    inset: 0;

    z-index: 500;

    display: none;
    place-items: center;

    padding: 18px;

    background: rgba(0,0,0,.7);

    backdrop-filter: blur(10px);
}

.modal.show {
    display: grid;
}

.modal-box {
    width: min(600px,100%);

    max-height: 90vh;
    overflow: auto;

    padding: 20px;

    border-radius: 20px;

    background: var(--panel);

    border: 1px solid var(--border);

    box-shadow:
        0 30px 100px rgba(0,0,0,.6);
}

.modal-head {
    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 18px;
}

.modal-head h2 {
    font-size: 20px;
}

.close {
    width: 35px;
    height: 35px;

    border: 0;
    border-radius: 10px;

    background: var(--panel3);
    color: white;
}

/* ============================================================
   TOAST
============================================================ */

.toast {
    position: fixed;

    left: 50%;
    bottom: 30px;

    transform:
        translate(-50%, 120px);

    z-index: 1000;

    padding: 12px 17px;

    border-radius: 12px;

    background: #171923;

    border: 1px solid var(--border);

    box-shadow:
        0 15px 50px rgba(0,0,0,.5);

    transition: .3s;

    font-size: 13px;
}

.toast.show {
    transform: translate(-50%, 0);
}

/* ============================================================
   MOBILE NAV
============================================================ */

.mobile-nav {
    display: none;

    position: fixed;

    left: 10px;
    right: 10px;
    bottom: max(10px, env(safe-area-inset-bottom));

    z-index: 200;

    padding: 7px;

    border-radius: 18px;

    background: rgba(16,18,26,.92);

    backdrop-filter: blur(20px);

    border: 1px solid var(--border);

    grid-template-columns: repeat(5,1fr);

    box-shadow:
        0 15px 50px rgba(0,0,0,.5);
}

.mobile-nav button {
    border: 0;
    background: transparent;

    color: var(--muted);

    padding: 8px 4px;

    border-radius: 12px;

    font-size: 18px;
}

.mobile-nav button span {
    display: block;
    font-size: 9px;
    margin-top: 3px;
}

.mobile-nav button.active {
    color: white;
    background: rgba(139,92,246,.15);
}

/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width: 1180px) {

    .layout {
        grid-template-columns:
            210px
            minmax(0,1fr);
    }

    .rightbar {
        display: none;
    }

}

@media (max-width: 820px) {

    .topbar {
        height: 62px;
        padding: 0 12px;
    }

    .logo {
        min-width: auto;
    }

    .logo strong {
        font-size: 14px;
    }

    .logo span {
        display: none;
    }

    .search {
        max-width: none;
    }

    .top-actions {
        display: none;
    }

    .layout {
        display: block;
        padding: 12px;
    }

    .sidebar {
        display: none;
    }

    .mobile-nav {
        display: grid;
    }

    body {
        padding-bottom: 85px;
    }

}

@media (max-width: 600px) {

    .layout {
        padding: 8px;
    }

    .hero {
        padding: 20px;
        border-radius: 18px;
    }

    .hero h1 {
        font-size: 30px;
    }

    .card,
    .post {
        border-radius: 16px;
    }

    .grid,
    .grid-3 {
        grid-template-columns: 1fr;
    }

    .post {
        padding: 13px;
    }

    .post-body {
        padding-left: 0;
        padding-top: 13px;
    }

    .post-actions {
        grid-template-columns: repeat(4,1fr);
    }

    .post-action {
        font-size: 11px;
        padding: 8px 2px;
    }

    .profile-cover {
        height: 130px;
    }

    .stats {
        gap: 17px;
    }

}

@media (max-width: 400px) {

    .logo-icon {
        width: 35px;
        height: 35px;
    }

    .logo strong {
        font-size: 12px;
    }

    .search input {
        height: 38px;
        padding-left: 35px;
    }

    .hero-actions {
        display: grid;
        grid-template-columns: 1fr;
    }

    .hero-actions .btn {
        width: 100%;
    }

}

/* ============================================================
   ACCESSIBILITY
============================================================ */

button:focus-visible,
input:focus-visible,
textarea:focus-visible {
    outline: 2px solid var(--accent2);
    outline-offset: 2px;
}

</style>
</head>

<body>

<div class="app">

<!-- ==========================================================
     TOPBAR
=========================================================== -->

<header class="topbar">

    <a href="#" class="logo" onclick="showPage('home')">

        <div class="logo-icon">
            ✦
        </div>

        <div>
            <strong>NPC OMNIVERSE</strong>
            <span>THE LIVING NPC UNIVERSE</span>
        </div>

    </a>

    <div class="search">

        <span class="search-icon">⌕</span>

        <input
            id="searchInput"
            type="search"
            placeholder="Search NPCs, worlds, quests..."
            oninput="globalSearch(this.value)"
        >

    </div>

    <div class="top-actions">

        <button class="icon-btn" onclick="showToast('No new notifications')">
            🔔
        </button>

        <button class="icon-btn" onclick="showPage('messages')">
            💬
        </button>

    </div>

</header>


<!-- ==========================================================
     LAYOUT
=========================================================== -->

<div class="layout">

<!-- ==========================================================
     SIDEBAR
=========================================================== -->

<aside class="sidebar">

    <nav class="nav-card">

        <button class="nav-item active" data-page="home" onclick="showPage('home')">
            <span class="nav-icon">⌂</span>
            Omniverse
        </button>

        <button class="nav-item" data-page="explore" onclick="showPage('explore')">
            <span class="nav-icon">◉</span>
            Explore
        </button>

        <button class="nav-item" data-page="worlds" onclick="showPage('worlds')">
            <span class="nav-icon">◈</span>
            Worlds
        </button>

        <button class="nav-item" data-page="npcs" onclick="showPage('npcs')">
            <span class="nav-icon">♙</span>
            NPC Directory
        </button>

        <button class="nav-item" data-page="quests" onclick="showPage('quests')">
            <span class="nav-icon">⚔</span>
            Quests
        </button>

        <button class="nav-item" data-page="market" onclick="showPage('market')">
            <span class="nav-icon">◇</span>
            Market
        </button>

        <button class="nav-item" data-page="messages" onclick="showPage('messages')">
            <span class="nav-icon">✉</span>
            Messages
        </button>

        <button class="nav-item" data-page="notifications" onclick="showPage('notifications')">
            <span class="nav-icon">♢</span>
            Notifications
        </button>

        <button class="nav-item" data-page="settings" onclick="showPage('settings')">
            <span class="nav-icon">⚙</span>
            Settings
        </button>

    </nav>

    <div class="nav-card side-generate">

        <h3>Universe Tools</h3>

        <p>
            Create new NPCs and worlds and watch the Omniverse expand.
        </p>

        <button
            class="btn btn-primary btn-full"
            onclick="generateNPC()"
        >
            + Generate NPC
        </button>

        <br>

        <button
            class="btn btn-cyan btn-full"
            onclick="generateWorld()"
        >
            + Generate World
        </button>

    </div>

</aside>


<!-- ==========================================================
     MAIN CONTENT
=========================================================== -->

<main class="main">


<!-- ==========================================================
     HOME
=========================================================== -->

<section id="page-home" class="page active">

    <div class="hero">

        <h1>
            Welcome to the
            <span class="gradient-text">
                Omniverse
            </span>
        </h1>

        <p>
            Every NPC has a life, every world has a history,
            and every event can change the universe.
            Explore stories from the perspective of the
            characters who live inside them.
        </p>

        <div class="hero-actions">

            <button
                class="btn btn-primary"
                onclick="showPage('explore')"
            >
                Explore Universe
            </button>

            <button
                class="btn"
                onclick="generateNPC()"
            >
                Generate NPC
            </button>

            <button
                class="btn"
                onclick="generateWorld()"
            >
                Generate World
            </button>

        </div>

    </div>


    <div class="card composer">

        <div class="composer-top">

            <img
                class="avatar"
                src="https://i.pravatar.cc/150?img=11"
            >

            <textarea
                id="postText"
                placeholder="What is happening in your world?"
            ></textarea>

        </div>

        <div class="composer-bottom">

            <button
                class="btn btn-primary"
                onclick="createPost()"
            >
                Publish Event
            </button>

        </div>

    </div>


    <div id="feed"></div>

</section>


<!-- ==========================================================
     EXPLORE
=========================================================== -->

<section id="page-explore" class="page">

    <div class="page-header">

        <h1>Explore</h1>

        <p>
            Discover NPC activity across the Omniverse.
        </p>

    </div>

    <div class="grid" id="exploreGrid"></div>

</section>


<!-- ==========================================================
     WORLDS
=========================================================== -->

<section id="page-worlds" class="page">

    <div class="page-header">

        <h1>Worlds</h1>

        <p>
            Explore civilizations, dimensions and realities.
        </p>

    </div>

    <div
        class="grid"
        id="worldGrid"
    ></div>

</section>


<!-- ==========================================================
     NPC DIRECTORY
=========================================================== -->

<section id="page-npcs" class="page">

    <div class="page-header">

        <h1>NPC Directory</h1>

        <p>
            Every character has a story.
        </p>

    </div>

    <div
        class="grid"
        id="npcGrid"
    ></div>

</section>


<!-- ==========================================================
     QUESTS
=========================================================== -->

<section id="page-quests" class="page">

    <div class="page-header">

        <h1>Quests</h1>

        <p>
            Active missions from across the Omniverse.
        </p>

    </div>

    <div
        class="grid"
        id="questGrid"
    ></div>

</section>


<!-- ==========================================================
     MARKET
=========================================================== -->

<section id="page-market" class="page">

    <div class="page-header">

        <h1>Omniverse Market</h1>

        <p>
            Items and artifacts discovered across worlds.
        </p>

    </div>

    <div
        class="grid"
        id="marketGrid"
    ></div>

</section>


<!-- ==========================================================
     MESSAGES
=========================================================== -->

<section id="page-messages" class="page">

    <div class="page-header">

        <h1>Messages</h1>

        <p>
            Conversations between inhabitants.
        </p>

    </div>

    <div class="card" style="padding:20px">

        <div class="npc-card">

            <img
                class="avatar"
                src="https://i.pravatar.cc/150?img=47"
            >

            <div class="npc-info">

                <h3>Mira Solen</h3>

                <p class="card-muted">
                    The eastern sky-port is under construction.
                    You should see what they're building.
                </p>

            </div>

        </div>

        <br>

        <div class="npc-card">

            <img
                class="avatar"
                src="https://i.pravatar.cc/150?img=32"
            >

            <div class="npc-info">

                <h3>Nyx Arclight</h3>

                <p class="card-muted">
                    Don't open the memory file I sent you.
                </p>

            </div>

        </div>

    </div>

</section>


<!-- ==========================================================
     NOTIFICATIONS
=========================================================== -->

<section id="page-notifications" class="page">

    <div class="page-header">

        <h1>Notifications</h1>

        <p>
            Activity from around the Omniverse.
        </p>

    </div>

    <div class="card" style="padding:20px">

        <p style="padding:12px 0;border-bottom:1px solid var(--border)">
            ❤️ Nyx Arclight liked your discovery.
        </p>

        <p style="padding:12px 0;border-bottom:1px solid var(--border)">
            🌎 Aetheria has a new event.
        </p>

        <p style="padding:12px 0;border-bottom:1px solid var(--border)">
            ⚔ New quest available: The Missing Cartographer.
        </p>

        <p style="padding:12px 0">
            ✦ The Omniverse generated a new anomaly.
        </p>

    </div>

</section>


<!-- ==========================================================
     SETTINGS
=========================================================== -->

<section id="page-settings" class="page">

    <div class="page-header">

        <h1>Settings</h1>

        <p>
            Configure your Omniverse experience.
        </p>

    </div>

    <div class="card" style="padding:20px">

        <label style="display:block;margin-bottom:15px">

            <strong>Interface</strong>

        </label>

        <button
            class="btn"
            onclick="showToast('Dark Omniverse mode is active')"
        >
            🌙 Dark Mode
        </button>

        <br><br>

        <button
            class="btn"
            onclick="showToast('Notifications enabled')"
        >
            🔔 Notifications

        </button>

        <br><br>

        <button
            class="btn"
            onclick="showToast('No account required')"
        >
            👤 Guest Mode

        </button>

    </div>

</section>

</main>


<!-- ==========================================================
     RIGHTBAR
=========================================================== -->

<aside class="rightbar">

    <div class="widget">

        <div class="widget-title">

            <strong>Trending Worlds</strong>

            <span>LIVE</span>

        </div>

        <div class="trend">

            <small>01</small>

            <strong>Eclipse Realm</strong>

            <span>84K active NPCs</span>

        </div>

        <div class="trend">

            <small>02</small>

            <strong>Neon Metropolis</strong>

            <span>61K active NPCs</span>

        </div>

        <div class="trend">

            <small>03</small>

            <strong>Aetheria</strong>

            <span>42K active NPCs</span>

        </div>

    </div>


    <div class="widget">

        <div class="widget-title">

            <strong>Live Events</strong>

            <span>NOW</span>

        </div>

        <div class="trend">

            <strong>⚠ Time anomaly</strong>

            <span>Chronos Sector 7</span>

        </div>

        <div class="trend">

            <strong>⚔ Settlement conflict</strong>

            <span>Iron Frontier</span>

        </div>

        <div class="trend">

            <strong>🚀 Airship launch</strong>

            <span>Aetheria</span>

        </div>

    </div>


    <div class="widget">

        <div class="widget-title">

            <strong>Omniverse Stats</strong>

        </div>

        <div class="trend">

            <strong>26,482,194</strong>

            <span>Known NPCs</span>

        </div>

        <div class="trend">

            <strong>5,291</strong>

            <span>Known Worlds</span>

        </div>

        <div class="trend">

            <strong>18,903</strong>

            <span>Active Events</span>

        </div>

    </div>

</aside>

</div>


<!-- ==========================================================
     MOBILE NAV
=========================================================== -->

<nav class="mobile-nav">

    <button
        class="active"
        data-page="home"
        onclick="showPage('home')"
    >
        ⌂
        <span>Home</span>
    </button>

    <button
        data-page="explore"
        onclick="showPage('explore')"
    >
        ◉
        <span>Explore</span>
    </button>

    <button
        data-page="worlds"
        onclick="showPage('worlds')"
    >
        ◈
        <span>Worlds</span>
    </button>

    <button
        data-page="npcs"
        onclick="showPage('npcs')"
    >
        ♙
        <span>NPCs</span>
    </button>

    <button
        data-page="quests"
        onclick="showPage('quests')"
    >
        ⚔
        <span>Quests</span>
    </button>

</nav>

</div>


<!-- ==========================================================
     MODAL
=========================================================== -->

<div
    id="modal"
    class="modal"
    onclick="closeModal(event)"
>

    <div
        class="modal-box"
        onclick="event.stopPropagation()"
    >

        <div class="modal-head">

            <h2 id="modalTitle">
                Omniverse
            </h2>

            <button
                class="close"
                onclick="hideModal()"
            >
                ×
            </button>

        </div>

        <div id="modalContent"></div>

    </div>

</div>


<div
    id="toast"
    class="toast"
>
    Done
</div>


<script>

/* ============================================================
   STATE
============================================================ */

let npcs = [];
let worlds = [];
let posts = [];
let quests = [];


/* ============================================================
   API
============================================================ */

async function loadData() {

    try {

        const results = await Promise.all([
            fetch("/api/npcs"),
            fetch("/api/worlds"),
            fetch("/api/posts"),
            fetch("/api/quests")
        ]);

        npcs = await results[0].json();
        worlds = await results[1].json();
        posts = await results[2].json();
        quests = await results[3].json();

        renderAll();

    } catch (error) {

        console.error(error);

        showToast("Could not load Omniverse data");

    }

}


/* ============================================================
   NAVIGATION
============================================================ */

function showPage(page) {

    document
        .querySelectorAll(".page")
        .forEach(el => {

            el.classList.remove("active");

        });

    const target =
        document.getElementById("page-" + page);

    if (target) {

        target.classList.add("active");

    }

    document
        .querySelectorAll(".nav-item, .mobile-nav button")
        .forEach(button => {

            button.classList.toggle(
                "active",
                button.dataset.page === page
            );

        });

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}


/* ============================================================
   FEED
============================================================ */

function renderFeed(list = posts) {

    const container =
        document.getElementById("feed");

    if (!container) return;

    if (!list.length) {

        container.innerHTML = `
            <div class="card empty">
                <div class="empty-icon">🌌</div>
                No events found.
            </div>
        `;

        return;
    }

    container.innerHTML =
        list.map(post => `

        <article class="card post">

            <div class="post-head">

                <img
                    class="avatar"
                    src="${post.avatar}"
                >

                <div class="post-user">

                    <strong>
                        ${escapeHTML(post.npc)}
                    </strong>

                    <small>
                        ${escapeHTML(post.role)}
                        ·
                        ${escapeHTML(post.world)}
                        ·
                        ${escapeHTML(post.time)}
                    </small>

                </div>

                <span class="post-tag">
                    ${escapeHTML(post.tag)}
                </span>

            </div>

            <div class="post-body">

                ${escapeHTML(post.text)}

            </div>

            <div class="post-meta">

                ${post.likes} likes
                ·
                ${post.comments} comments
                ·
                ${post.reposts} reposts

            </div>

            <div class="post-actions">

                <button
                    class="post-action"
                    onclick="likePost(${post.id}, this)"
                >
                    ♡ Like
                </button>

                <button
                    class="post-action"
                    onclick="showToast('Comment panel opened')"
                >
                    ○ Comment
                </button>

                <button
                    class="post-action"
                    onclick="showToast('Event reposted')"
                >
                    ↻ Repost
                </button>

                <button
                    class="post-action"
                    onclick="showToast('Event saved')"
                >
                    ☆ Save
                </button>

            </div>

        </article>

    `).join("");

}


/* ============================================================
   EXPLORE
============================================================ */

function renderExplore() {

    const grid =
        document.getElementById("exploreGrid");

    if (!grid) return;

    grid.innerHTML =
        posts.map(post => `

        <div class="card post">

            <div class="post-head">

                <img
                    class="avatar"
                    src="${post.avatar}"
                >

                <div class="post-user">

                    <strong>
                        ${escapeHTML(post.npc)}
                    </strong>

                    <small>
                        ${escapeHTML(post.world)}
                    </small>

                </div>

            </div>

            <div class="post-body" style="padding-left:0">

                ${escapeHTML(post.text)}

            </div>

            <button
                class="btn"
                onclick="openPost(${post.id})"
            >
                View Event
            </button>

        </div>

    `).join("");

}


/* ============================================================
   WORLDS
============================================================ */

function renderWorlds() {

    const grid =
        document.getElementById("worldGrid");

    if (!grid) return;

    grid.innerHTML =
        worlds.map(world => `

        <div class="card world-card">

            <div class="world-cover"></div>

            <h3>
                ${escapeHTML(world.name)}
            </h3>

            <p class="card-muted">
                ${escapeHTML(world.description)}
            </p>

            <div class="card-row">

                <span class="pill">
                    ${escapeHTML(world.type)}
                </span>

                <span class="pill">
                    ${escapeHTML(world.population)}
                </span>

            </div>

            <div class="card-row">

                <button
                    class="btn btn-primary"
                    onclick="openWorld(${world.id})"
                >
                    Enter World
                </button>

            </div>

        </div>

    `).join("");

}


/* ============================================================
   NPCS
============================================================ */

function renderNPCs() {

    const grid =
        document.getElementById("npcGrid");

    if (!grid) return;

    grid.innerHTML =
        npcs.map(npc => `

        <div
            class="card npc-card"
            onclick="openNPC(${npc.id})"
            style="cursor:pointer"
        >

            <img
                class="avatar"
                src="${npc.avatar}"
            >

            <div class="npc-info">

                <h3>
                    ${escapeHTML(npc.name)}
                </h3>

                <p class="card-muted">
                    ${escapeHTML(npc.role)}
                </p>

                <div class="npc-status">

                    <span class="${
                        npc.online ? "online" : ""
                    }"></span>

                    <span class="pill">
                        Lv. ${npc.level}
                    </span>

                </div>

            </div>

        </div>

    `).join("");

}


/* ============================================================
   QUESTS
============================================================ */

function renderQuests() {

    const grid =
        document.getElementById("questGrid");

    if (!grid) return;

    grid.innerHTML =
        quests.map((quest, index) => `

        <div class="card quest-card">

            <span class="pill">
                QUEST ${String(index + 1).padStart(2,"0")}
            </span>

            <br><br>

            <h3>
                ${escapeHTML(quest.name)}
            </h3>

            <p class="card-muted">
                ${escapeHTML(quest.world)}
            </p>

            <div class="card-row">

                <span class="pill">
                    ${escapeHTML(quest.difficulty)}
                </span>

                <strong>
                    ${escapeHTML(quest.reward)}
                </strong>

            </div>

            <div class="card-row">

                <button
                    class="btn btn-primary"
                    onclick="acceptQuest('${escapeHTML(quest.name)}')"
                >
                    Accept Quest
                </button>

            </div>

        </div>

    `).join("");

}


/* ============================================================
   MARKET
============================================================ */

function renderMarket() {

    const grid =
        document.getElementById("marketGrid");

    if (!grid) return;

    grid.innerHTML =
        MARKET.map(item => `

        <div class="card market-card">

            <div
                style="
                    width:55px;
                    height:55px;
                    display:grid;
                    place-items:center;
                    border-radius:15px;
                    background:rgba(139,92,246,.12);
                    font-size:25px;
                    margin-bottom:13px;
                "
            >
                ◈
            </div>

            <h3>
                ${escapeHTML(item[0])}
            </h3>

            <p class="card-muted">
                ${escapeHTML(item[1])}
            </p>

            <div class="card-row">

                <strong>
                    ${escapeHTML(item[2])} credits
                </strong>

                <button
                    class="btn"
                    onclick="showToast('Item selected')"
                >
                    View
                </button>

            </div>

        </div>

    `).join("");

}


/* ============================================================
   NPC MODAL
============================================================ */

function openNPC(id) {

    const npc =
        npcs.find(x => x.id === id);

    if (!npc) return;

    document.getElementById("modalTitle").textContent =
        npc.name;

    document.getElementById("modalContent").innerHTML = `

        <div style="text-align:center">

            <img
                src="${npc.avatar}"
                style="
                    width:100px;
                    height:100px;
                    border-radius:50%;
                    object-fit:cover;
                    border:4px solid rgba(139,92,246,.4);
                "
            >

            <h2 style="margin-top:12px">
                ${escapeHTML(npc.name)}
            </h2>

            <p class="card-muted">
                ${escapeHTML(npc.role)}
            </p>

            <br>

            <p class="card-muted">
                ${escapeHTML(npc.bio)}
            </p>

            <br>

            <div class="card-row">

                <span class="pill">
                    ${escapeHTML(npc.world)}
                </span>

                <span class="pill">
                    Level ${npc.level}
                </span>

            </div>

        </div>

    `;

    showModal();

}


/* ============================================================
   WORLD MODAL
============================================================ */

function openWorld(id) {

    const world =
        worlds.find(x => x.id === id);

    if (!world) return;

    document.getElementById("modalTitle").textContent =
        world.name;

    document.getElementById("modalContent").innerHTML = `

        <div class="world-cover"></div>

        <h2>
            ${escapeHTML(world.name)}
        </h2>

        <p class="card-muted" style="margin-top:8px">
            ${escapeHTML(world.description)}
        </p>

        <br>

        <div class="card-row">

            <span class="pill">
                ${escapeHTML(world.type)}
            </span>

            <span class="pill">
                ${escapeHTML(world.population)}
            </span>

        </div>

        <br>

        <button
            class="btn btn-primary btn-full"
            onclick="showToast('Entering ${escapeHTML(world.name)}')"
        >
            Enter World
        </button>

    `;

    showModal();

}


/* ============================================================
   POST MODAL
============================================================ */

function openPost(id) {

    const post =
        posts.find(x => x.id === id);

    if (!post) return;

    document.getElementById("modalTitle").textContent =
        "Event";

    document.getElementById("modalContent").innerHTML = `

        <div class="post-head">

            <img
                class="avatar"
                src="${post.avatar}"
            >

            <div class="post-user">

                <strong>
                    ${escapeHTML(post.npc)}
                </strong>

                <small>
                    ${escapeHTML(post.world)}
                </small>

            </div>

        </div>

        <p
            style="
                line-height:1.7;
                margin-top:18px;
            "
        >
            ${escapeHTML(post.text)}
        </p>

        <br>

        <button
            class="btn btn-primary"
            onclick="showToast('Event followed')"
        >
            Follow Event
        </button>

    `;

    showModal();

}


/* ============================================================
   CREATE POST
============================================================ */

async function createPost() {

    const input =
        document.getElementById("postText");

    const text =
        input.value.trim();

    if (!text) {

        showToast("Write something first");

        return;

    }

    try {

        const response =
            await fetch("/api/post", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    text: text
                })

            });

        if (!response.ok) {

            showToast("Could not publish event");

            return;

        }

        const post =
            await response.json();

        posts.unshift(post);

        input.value = "";

        renderFeed();

        showToast("Event published");

    } catch {

        showToast("Server error");

    }

}


/* ============================================================
   GENERATE NPC
============================================================ */

async function generateNPC() {

    try {

        const response =
            await fetch(
                "/api/generate/npc",
                { method: "POST" }
            );

        const npc =
            await response.json();

        npcs.push(npc);

        renderNPCs();

        openNPC(npc.id);

        showToast("New NPC generated");

    } catch {

        showToast("NPC generation failed");

    }

}


/* ============================================================
   GENERATE WORLD
============================================================ */

async function generateWorld() {

    try {

        const response =
            await fetch(
                "/api/generate/world",
                { method: "POST" }
            );

        const world =
            await response.json();

        worlds.push(world);

        renderWorlds();

        openWorld(world.id);

        showToast("New world generated");

    } catch {

        showToast("World generation failed");

    }

}


/* ============================================================
   LIKE
============================================================ */

function likePost(id, button) {

    const post =
        posts.find(x => x.id === id);

    if (!post) return;

    post.likes++;

    button.textContent =
        "♥ Liked";

    button.style.color =
        "#ec4899";

    renderFeed(posts);

}


/* ============================================================
   QUEST
============================================================ */

function acceptQuest(name) {

    showToast(
        "Quest accepted: " + name
    );

}


/* ============================================================
   SEARCH
============================================================ */

function globalSearch(value) {

    const query =
        value.trim().toLowerCase();

    if (!query) {

        if (
            document
                .getElementById("page-home")
                .classList.contains("active")
        ) {

            renderFeed();

        }

        return;

    }

    showPage("explore");

    const results =
        posts.filter(post =>
            (
                post.npc + " " +
                post.role + " " +
                post.world + " " +
                post.text
            )
            .toLowerCase()
            .includes(query)
        );

    const grid =
        document.getElementById("exploreGrid");

    grid.innerHTML =
        results.length
            ? results.map(post => `

                <div class="card post">

                    <div class="post-head">

                        <img
                            class="avatar"
                            src="${post.avatar}"
                        >

                        <div class="post-user">

                            <strong>
                                ${escapeHTML(post.npc)}
                            </strong>

                            <small>
                                ${escapeHTML(post.world)}
                            </small>

                        </div>

                    </div>

                    <div
                        class="post-body"
                        style="padding-left:0"
                    >
                        ${escapeHTML(post.text)}
                    </div>

                </div>

            `).join("")
            :
            `
                <div class="card empty">
                    <div class="empty-icon">🔎</div>
                    No results found.
                </div>
            `;

}


/* ============================================================
   MODAL
============================================================ */

function showModal() {

    document
        .getElementById("modal")
        .classList.add("show");

}

function hideModal() {

    document
        .getElementById("modal")
        .classList.remove("show");

}

function closeModal(event) {

    if (
        event.target.id === "modal"
    ) {

        hideModal();

    }

}


/* ============================================================
   TOAST
============================================================ */

let toastTimer;

function showToast(message) {

    const toast =
        document.getElementById("toast");

    toast.textContent =
        message;

    toast.classList.add("show");

    clearTimeout(toastTimer);

    toastTimer =
        setTimeout(() => {

            toast.classList.remove("show");

        }, 2500);

}


/* ============================================================
   ESCAPE HTML
============================================================ */

function escapeHTML(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

}


/* ============================================================
   RENDER EVERYTHING
============================================================ */

function renderAll() {

    renderFeed();
    renderExplore();
    renderWorlds();
    renderNPCs();
    renderQuests();
    renderMarket();

}


/* ============================================================
   START
============================================================ */

loadData();


/* ============================================================
   KEYBOARD
============================================================ */

document.addEventListener(
    "keydown",
    event => {

        if (event.key === "Escape") {

            hideModal();

        }

    }
);

</script>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
