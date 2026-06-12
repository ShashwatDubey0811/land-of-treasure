# 🏆 Land of Treasure

A text-based adventure game built with Python and a decorated HTML/CSS/JS frontend. Built as part of the **#100DaysOfCode** challenge.

---

## 🎮 About the Game

You are an adventurer on a mission to find hidden treasure. Every choice you make leads you closer to victory — or to your doom. Navigate through crossroads, lakes, and mysterious doors to claim the treasure!

---

## 🗺️ How to Play

1. You start at a **crossroads** — go left or right
2. If you go left, you reach a **lake** — swim or wait for a boat
3. If you wait, you arrive at an **island** with a house with **3 doors**
4. Choose the **right door** to find the treasure and win!

Only one path leads to victory. Good luck!

---

## 🐍 Python Version

### Requirements
- Python 3.x

### Run the game
```bash
python AdventureGame.py
```

### Game logic
```
Start
├── Right → 💀 Fell into a hole. Game over.
└── Left → Lake
         ├── Swim → 💀 Drowned in a mudhole. Game over.
         └── Wait → Island (3 doors)
                  ├── Red   → 💀 Room full of fire. Game over.
                  ├── Blue  → 💀 Attacked by a demon. Game over.
                  └── Yellow → 🏆 YOU WIN!
```

---

## 🌐 Web Version

A fully decorated browser-based version built with HTML, CSS, and JavaScript.

**Features:**
- Medieval parchment and stone theme
- Animated scene transitions
- Attempts and victories tracker
- Play again button
- Mobile friendly

### Play it live
👉 [land-of-treasure.netlify.app](https://land-of-treasure.netlify.app)

### Run locally
Just open `AdventureGame.html` in any browser — no server needed.

---

## 📁 Project Structure

```
land-of-treasure/
├── AdventureGame.py       # Python terminal version
├── AdventureGame.html     # Web browser version
└── README.md
```

---

## 🛠️ Built With

- Python 3
- HTML5
- CSS3
- JavaScript (Vanilla)
- Hosted on [Netlify](https://netlify.com)

---

## 📅 Progress

Built during **#100DaysOfCode** — Day 3

---

## 📜 License

This project is open source and free to use.
