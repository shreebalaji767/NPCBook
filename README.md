# 📱 NPCBook — Social Media for NPCs

> **A social network where nobody is the main character.**

NPCBook is a parody social-media website populated entirely by randomly generated **NPCs (Non-Playable Characters)**.

Every time the website is opened or refreshed, NPCBook creates a completely new temporary world containing different NPCs, posts, comments, quests, trends, marketplace items, statistics, and random NPC activity.

---

## ✨ Features

### 🤖 Random NPC Generation

NPCBook automatically creates NPCs with randomly generated:

* Names
* Ages
* Occupations
* Locations
* Moods
* Activities
* Dialogue
* Thoughts
* Levels
* HP
* Energy
* Intelligence
* Dialogue variety
* Repetition rate
* Friends
* Followers
* Personal quests

Example:

```text
🤖 Rajesh Kumar

Occupation:
Professional Bench Sitter

Location:
Near the tea stall

Mood:
😐 Neutral

Level:
47

Dialogue Variety:
12%

Repetition:
94%

Current Activity:
Standing quietly
```

---

## 📰 Dynamic NPC Feed

The homepage contains a social-media-style feed populated with randomly generated NPC posts.

Posts can include things like:

> "Today I was standing near the gate. Very productive."

> "BREAKING: Nothing happened near the tea stall. More updates when nothing continues."

> "I saw Rajesh again. We did not speak. A successful interaction."

Posts also contain randomly generated:

* 👍 Likes
* 💬 Comments
* ↗ Shares
* Hashtags
* NPC moods
* Posting times

---

## 💬 NPC Interactions

Visitors can interact with temporary posts.

Available actions include:

* Like
* Unlike
* Comment
* Share
* Generate another NPC
* Generate another post
* Search NPCs

The interactions exist only in the current browser session.

Refreshing the page creates a new world.

---

## 🎯 NPC Quests

NPCs have completely unnecessary quests such as:

```text
🎯 Find the missing bucket
🎯 Inspect the suspicious pigeon
🎯 Guard the important chair
🎯 Locate the blue scooter
🎯 Return the mysterious key
```

Each quest receives a random completion percentage and XP reward.

---

## 🔥 Trending

NPCBook generates temporary trending topics such as:

```text
#Tea
#GateLife
#MissingBucket
#Weather
#SameBench
#SuspiciousPigeon
#NothingHappened
#QuestProblems
#ChairPolitics
#StandingAround
```

The number of posts associated with each trend is randomly generated.

---

## 🛒 NPC Marketplace

NPCBook also contains a completely ridiculous temporary marketplace.

Example items:

```text
🛒 Slightly Used Stick
🛒 Mysterious Rock
🛒 Old Bread
🛒 Key That Opens Nothing
🛒 Suspicious Bucket
🛒 One Left Shoe
🛒 Chair With History
🛒 Empty Box
🛒 Rare Looking Leaf
```

Prices and stock quantities are randomly generated.

---

# 🔄 New World Every Refresh

This is the central concept of NPCBook.

When the page loads:

```text
OPEN NPCBook
      ↓
GENERATE NPCs
      ↓
GENERATE POSTS
      ↓
GENERATE QUESTS
      ↓
GENERATE TRENDS
      ↓
GENERATE MARKETPLACE
      ↓
DISPLAY WORLD
```

When the visitor refreshes:

```text
REFRESH
   ↓
OLD WORLD DISAPPEARS
   ↓
NEW WORLD GENERATED
```

If the browser is closed and NPCBook is opened again:

```text
CLOSE
  ↓
OPEN AGAIN
  ↓
NEW WORLD
```

The website intentionally does not preserve the previous world.

---

# 🚫 No Database

NPCBook does **not** use a database.

There is:

* ❌ MySQL
* ❌ PostgreSQL
* ❌ MongoDB
* ❌ SQLite
* ❌ Firebase
* ❌ Supabase
* ❌ Any database server

All generated information is temporary.

---

# 🚫 No LocalStorage

NPCBook does not use:

```javascript
localStorage
```

It also does not use:

```javascript
sessionStorage
```

No NPC information, posts, likes, comments, quests, or marketplace data are saved by the browser.

---

# 🚫 No Cookies

NPCBook does not require cookies for storing the generated world.

---

# 🧠 How It Works

NPCBook is designed as a **static website**.

Python is used as a build-time generator.

The Python file contains the complete website:

```text
app.py
```

Inside that one file are:

* HTML
* CSS
* JavaScript
* NPC data
* NPC generation logic
* Static-site generation logic

Running:

```bash
python app.py
```

creates:

```text
index.html
```

The resulting `index.html` contains the complete website.

---

# 📁 Project Structure

The project intentionally remains extremely small:

```text
NPCBook/
│
└── app.py
```

After running the build:

```text
NPCBook/
│
├── app.py
└── index.html
```

`index.html` is the generated static website.

---

# 🌐 Hosting on Render

NPCBook is designed to be deployed as a **Render Static Site**, not a Web Service.

## Render configuration

### Service Type

```text
Static Site
```

### Build Command

```bash
python app.py
```

### Publish Directory

```text
.
```

Render runs the Python build script.

The script generates:

```text
index.html
```

Render then serves the generated static website.

---

# ⚡ Why Static Site?

NPCBook does not require a permanent backend.

There is no reason to keep a server running just to store NPCs because the entire concept is based on temporary generated content.

The architecture is:

```text
GitHub
   │
   │
   ▼
Render Static Site
   │
   │
   ├── runs app.py during build
   │
   ▼
index.html
   │
   ▼
Visitor's Browser
   │
   ▼
JavaScript generates temporary NPC world
```

---

# 📱 Responsive Design

NPCBook is designed to work across different screen sizes.

Supported layouts include:

* 📱 Mobile phones
* 🤖 Android phones
* 🍎 iPhones
* 📲 Tablets
* 🖥️ Desktop computers
* 💻 Laptops
* 🖐️ Touchscreen devices

The interface automatically adapts to the available screen width.

On smaller devices, the desktop sidebars disappear and a compact mobile navigation bar is displayed.

---

# 🖐️ Touchscreen Support

The interface uses larger interactive controls on touchscreen devices.

Buttons are designed to be easier to tap rather than requiring precise mouse-pointer movement.

The mobile navigation also avoids covering important feed content as much as possible.

---

# 🎲 Random Generation

NPCBook uses JavaScript's random number generation to create a new world.

For example:

```javascript
const name = pick(DATA.names);
const job = pick(DATA.jobs);
const mood = pick(DATA.moods);
```

These values are combined to create temporary NPCs.

The same technique is used for:

* Posts
* Likes
* Comments
* Shares
* Quests
* Marketplace items
* Trends
* NPC statistics

---

# 🔐 Data & Privacy

NPCBook is intentionally designed without persistent application data.

The site does not need:

* User accounts
* Passwords
* Database records
* Saved NPC profiles
* Saved posts
* Saved comments
* Saved likes
* Saved quests

The generated NPC universe exists only while the current page is running.

Refreshing the page destroys the current JavaScript state and creates a new one.

---

# 🎭 The Concept

NPCBook is a parody of modern social-media platforms.

Instead of focusing on famous people, influencers, celebrities, or main characters, NPCBook focuses on ordinary background characters.

The NPCs may spend their entire digital lives:

* Standing beside a gate
* Drinking tea
* Watching traffic
* Looking for a bucket
* Guarding a door
* Sitting on the same bench
* Discussing the weather
* Repeating the same dialogue
* Completing pointless quests

The result is a deliberately absurd social network populated by characters who behave like video-game NPCs.

---

# 🏆 Example NPC

```text
╔════════════════════════════════╗
║         🤖 NPC PROFILE         ║
╠════════════════════════════════╣
║ Name: Rajesh Kumar             ║
║ Age: 52                         ║
║ Job: Tea Observer               ║
║ Location: Near the tea stall   ║
║ Mood: 😐 Neutral               ║
║ Level: 63                       ║
║ HP: 81/100                      ║
║ Energy: 57/100                  ║
║ Intelligence: 38/100           ║
║ Dialogue Variety: 11%           ║
║ Repetition Rate: 96%            ║
║ Friends: 3                      ║
║ Followers: 417                  ║
╠════════════════════════════════╣
║ Quest: Find the missing bucket  ║
╚════════════════════════════════╝
```

---

# 🛠️ Running Locally

Make sure Python is installed.

Then run:

```bash
python app.py
```

This generates:

```text
index.html
```

Open `index.html` in a browser.

No Python server is required for the final static website.

---

# 🚀 Deploying

1. Create a GitHub repository.
2. Add `app.py`.
3. Push the repository to GitHub.
4. Create a new **Static Site** on Render.
5. Connect the GitHub repository.
6. Set the build command:

```bash
python app.py
```

7. Set the publish directory:

```text
.
```

8. Deploy.

Render generates the static `index.html` during deployment.

---

# 📌 Technical Summary

| Component              | NPCBook      |
| ---------------------- | ------------ |
| Backend server         | ❌            |
| Database               | ❌            |
| LocalStorage           | ❌            |
| SessionStorage         | ❌            |
| Cookies for app data   | ❌            |
| External API           | ❌            |
| User accounts          | ❌            |
| Persistent NPCs        | ❌            |
| Python                 | ✅ Build-time |
| HTML                   | ✅            |
| CSS                    | ✅            |
| JavaScript             | ✅            |
| Render Static Site     | ✅            |
| Mobile responsive      | ✅            |
| Touchscreen friendly   | ✅            |
| Fresh world on refresh | ✅            |
| Single source file     | ✅            |

---

# 📜 License

This project is a parody/social-media experiment.

You can modify the NPC generator, add new NPC types, create new jokes, expand the feed, and customize the interface for your own project.

---

## NPCBook

**Social media for NPCs.**

**Everyone has a profile.
Nobody has a purpose.
Someone is still looking for that bucket.** 🤖🪣
