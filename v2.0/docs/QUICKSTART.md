# PySnake v2.0 - Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies

```bash
cd v2.0
pip install -r requirements.txt
```

### 2. Run the Game

```bash
python snake_pygame.py
```

### 3. Play!

- Press `SPACE` to start
- Choose mode: `1` (Single Player) or `2` (VS AI) ⭐
- Use arrows or WASD to move
- Collect food and power-ups!

---

## 🎮 Quick Controls

| Key                                | Action            |
| ---------------------------------- | ----------------- |
| `SPACE` / `ENTER`                  | Start / Confirm   |
| `1` `2` `3`                        | Select Difficulty |
| `↑` `↓` `←` `→` or `W` `A` `S` `D` | Move              |
| `P` / `ESC`                        | Pause             |
| `S`                                | Settings          |
| `Q`                                | Quit / Back       |

---

## ⭐ What's New in v2.0

### AI Opponent Mode

Fight against an intelligent computer snake! The AI uses pathfinding to compete for food and power-ups.

### Beautiful New UI

Modern cyberpunk/neon colour scheme with:

- Teal-green player snake
- Magenta-pink AI snake
- Glowing effects
- Smooth fade effects

### Modular Code

Clean architecture with 7 separate modules for easy customization!

---

## 🎯 Game Modes

### Single Player

Classic snake game - grow as long as possible!

### VS AI Opponent ⭐

- Compete against computer snake
- Separate scores
- Win by outlasting the AI!

---

## 💎 Power-ups

| Icon | Name          | Duration | Effect                |
| ---- | ------------- | -------- | --------------------- |
| 🟡   | Speed Boost   | 5s       | Move 50% faster       |
| 🔵   | Invincibility | 7s       | Pass through yourself |
| 🟣   | Score x2      | 10s      | Double points         |

---

## 🏆 Difficulty Levels

| Level      | Speed  | Points | AI Skill    |
| ---------- | ------ | ------ | ----------- |
| **Easy**   | Slow   | 1x     | Beginner AI |
| **Medium** | Normal | 1.5x   | Balanced AI |
| **Hard**   | Fast   | 2x     | Expert AI   |

---

## 🎨 Customisation

Want to change colours? Edit `styles.py`:

```python
PLAYER_PRIMARY = (0, 255, 150)  # Player colour
AI_PRIMARY = (255, 100, 255)    # AI colour
DEEP_SPACE = (15, 15, 35)       # Background
```

---

## 📊 File Structure

```
v2.0/
├── snake_pygame.py    # ← Run this!
├── game.py            # Game logic
├── config.py          # Settings
├── styles.py          # Colours
├── snake.py           # Snake class
├── power_up.py        # Power-ups
├── ai_player.py       # AI brain
└── assets/            # Optional sounds
```

---

## 🐛 Common Issues

**"No module named 'pygame'"**
→ Run: `pip install pygame`

**Game runs slowly**
→ Lower FPS in config.py: `FPS = 30`

**AI too hard/easy**
→ Change difficulty with keys `1`, `2`, `3`

---

## 💡 Pro Tips

1. **Watch the AI** - Learn strategies by observing AI movement
2. **Use Power-ups Wisely** - Invincibility helps in tight spots
3. **Stay Mobile** - Don't trap yourself in corners
4. **Challenge Yourself** - Try beating the AI on Hard difficulty!
5. **Customise** - Edit styles.py to create your own theme

---

## 📖 Full Documentation

See `ARCHITECTURE.md` for complete technical documentation.

---

**Have fun playing PySnake v2.0!** 🐍🎮

Made with ❤️ by Tech Girl Diaries
