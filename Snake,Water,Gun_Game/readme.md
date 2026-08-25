<div align="center">

# 🐍💧🔫 Snake Water Gun — Interactive Web Game

**A Childhood Hand Game, Reimagined as a Playable Browser Experience**

[![React](https://img.shields.io/badge/React-18.2-61DAFB?style=for-the-badge&logo=react&logoColor=black)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)]()
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-CDN-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white)]()
[![No Build Tools](https://img.shields.io/badge/Setup-Zero_Build-00C853?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)]()

*A single-file, zero-install web game — plus the original Python console version it evolved from*

[Play It](#-how-to-run) · [Game Rules](#-rules) · [Architecture](#-architecture) · [Roadmap](#-roadmap)

</div>

---

## 📌 Overview

**Snake Water Gun** is a 3-way hand game played by kids across South Asia — a regional cousin of Rock-Paper-Scissors. This project brings it to the browser as a fully interactive, animated web app, alongside the original Python version it started from.

The web version is built as a **single self-contained HTML file** — React, Babel, and Tailwind are all loaded from a CDN and compiled live in the browser, so there's nothing to install and nothing to configure. Double-click it, and it runs.

### ✨ Key Highlights

- 🎮 **Fully Interactive UI** — tap a move, watch the round play out
- 🌀 **Suspense-Building Reveal** — the computer's pick shuffles through all three options before landing on its final choice
- 🎨 **Hand-Built SVG Icons** — custom snake, water droplet, and pistol silhouettes (no icon library has these)
- 🎊 **Confetti Burst** on every win
- 📊 **Live Scoreboard** — win/loss/tie tallies and round counter, persisted for the session
- 🐍 **Python Origin Story** — includes the original console version this was built from

---

## 🕹️ Rules

Snake Water Gun replaces Rock-Paper-Scissors' three throws with three elements, each beating exactly one other:

| Move | Beats | Why |
|:---:|:---:|---|
| 🐍 **Snake** | 💧 Water | Snake drinks the water |
| 💧 **Water** | 🔫 Gun | Water rusts the gun |
| 🔫 **Gun** | 🐍 Snake | Gun kills the snake |

Matching moves from both players result in a **draw**.

---

## ⚙️ Game Logic

The win/lose decision is driven by a single beats-relationship, checked against whatever the player and computer picked:

```javascript
const BEATS = { snake: "water", water: "gun", gun: "snake" };

function decide(user, computer) {
  if (user === computer) return "tie";
  return BEATS[user] === computer ? "user" : "computer";
}
```

The **original Python version** (`snake_water_gun.py`) encodes the same rules numerically and resolves them with an explicit if/elif ladder instead:

```python
'''
1 for snake, -1 for water, 0 for gun
'''
if (computer == -1 and you == 1):
    print("You Win !!!")      # snake drinks water
elif (computer == 0 and you == -1):
    print("You Win!!!")       # water rusts gun
elif (computer == 1 and you == 0):
    print("You Win!!!")       # gun kills snake
# ...and so on for every losing combination
```

---

## 🚀 How to Run

### Web Version (recommended)

No installation, no dependencies, no terminal required.

1. Download `snake-water-gun-game.html`
2. Double-click it — or right-click → **Open with** → your browser
3. Pick Snake, Water, or Gun and play

Under the hood, this file pulls React, Babel Standalone, and Tailwind CSS from a CDN and compiles everything client-side on load. Great for playing and sharing — **not intended for production deployment** (see [Known Limitations](#-known-limitations)).

### Python Version

```bash
python snake_water_gun.py
```

Follow the on-screen prompts (`s` / `w` / `g`) to play round by round in the terminal.

---

## 📁 Project Structure

```
snake-water-gun/
├── snake-water-gun-game.html       # Standalone browser version — just open it
├── snake-water-gun-colorful.jsx    # Raw React component source (needs a bundler to run)
├── snake_water_gun.py              # Original Python console version
└── README.md                       # This file
```

| File | Purpose |
|---|---|
| `snake-water-gun-game.html` | Zero-install, browser-ready version of the game |
| `snake-water-gun-colorful.jsx` | React component source — for use in a real bundled project (Vite, CRA, etc.) |
| `snake_water_gun.py` | Where it all started — the console version with the if/elif decision ladder |

---

## 🧱 Architecture

**Component breakdown (`.jsx` source):**

| Component | Responsibility |
|---|---|
| `SnakeWaterGunColorful` | Top-level game state — current choices, phase, scores, round count |
| `ArenaSlot` | Renders each player's current pick (or a `?` placeholder) with shake/pop-in animation |
| `Confetti` | Generates and animates a burst of colored pieces on a win |
| `Score` | Renders a single player's tally in the scoreboard |
| `SnakeIcon` / `WaterIcon` / `GunIcon` | Custom filled SVG icons for each move |

**Game flow:**

```
Idle → Player picks a move
     → Computer "shuffles" through random choices (≈600ms)
     → Final computer choice locked in
     → Outcome decided via BEATS lookup
     → Score updated, result + flavor text shown
     → Confetti fires if the player won
     → Ready for next round
```

---

## 🎨 Design Notes

- **Palette:** Teal-to-deep-ocean gradient background, with a warm cream arena panel for contrast
- **Typography:** [Fredoka](https://fonts.google.com/specimen/Fredoka) for display text, [Nunito](https://fonts.google.com/specimen/Nunito) for body copy
- **Motion:** CSS keyframes for shuffling (`shakeIcon`), reveals (`popIn`), floating background blobs (`blobFloat`), and confetti fall (`confettiFall`) — no animation library used

---

## ⚠️ Known Limitations

- **CDN-based, not production-ready** — Tailwind and Babel both compile live in-browser rather than being precompiled, which is fine for casual play but adds unnecessary load time at scale (see the console warnings this produces)
- **No persistence** — scores reset on page refresh; nothing is saved between sessions
- **Single-player only** — plays against a random computer choice, no multiplayer support
- **No sound** — visual and animated feedback only

---

## 🔮 Roadmap

- [ ] Migrate to a proper Vite + React build (removes CDN warnings, enables real deployment)
- [ ] Add sound effects for win/lose/tie
- [ ] "Best of N rounds" match mode
- [ ] Persist scores via `localStorage`
- [ ] Two-player mode (pass-and-play or online)

---

## 📚 What This Project Covers

- Translating simple game logic (if/elif ladder → lookup-table decision function) between languages and paradigms
- React state management for a multi-phase game loop (idle → shuffling → revealed)
- CSS keyframe animation without external libraries
- Building custom SVG iconography for a niche visual need
- The trade-offs between a zero-install CDN setup and a proper bundled build

---

## 👤 Author

**Areeba**
Built as a progression from a Python console script into a fully interactive web game.

---

## 📄 License

Personal / educational project — free to use, adapt, and build on.

---

<div align="center">

**🐍 Snake drinks Water · 💧 Water rusts Gun · 🔫 Gun kills Snake 🔫**

[Back to Top](#-snake-water-gun--interactive-web-game)

</div>
