# PySnake v2.0 - Modern Edition

A Python classic snake game with AI opponent, power-ups, multiple themes and smooth Pygame graphics.

**Version**: v2.0 Modern Edition  
**Author**: Tech Girl Diaries

## Quick Start

### Installation

1. **Install dependencies**:

```bash
   pip install -r requirements.txt
```

2. **Run the game**:

```bash
  python play.py
```

That's it! The game runs perfectly without audio files.

## Features

- **Two Game Modes**: Single Player or AI Opponent
- **Power-ups System**: Speed Boost, Invincibility, Score Multiplier
- **Four Dynamic Themes**: Cyberpunk, Retro, Ocean, Forest (Press **T** in menu)
- **Three Difficulty Levels**: Easy, Medium, Hard
- **AI Opponent**: Intelligent pathfinding using BFS algorithm
- **Persistent High Scores**: Auto-saved to `db/highscores.json`
- **Smooth 60 FPS Graphics**: Professional animations and visual effects
- **Full Settings Menu**: Customise sound, music and power-ups

## Controls

### Main Menu

- **SPACE**: Start game
- **1/2/3**: Select difficulty (Easy/Medium/Hard)
- **T**: Cycle themes (Cyberpunk Retro Ocean Forest)
- **S**: Settings
- **Q**: Quit

### In-Game

- **Arrow Keys** or **WASD**: Move snake
- **ESC** or **P**: Pause
- **Q** (in pause): Quit to menu

## Gameplay Overview

### Game Modes

- **Single Player**: Classic snake gameplay with power-ups
- **AI Opponent**: Compete against an intelligent computer snake

### Difficulty Levels

| Level  | Speed  | Score Multiplier |
| ------ | ------ | ---------------- |
| Easy   | Slow   | 1                |
| Medium | Normal | 1.5              |
| Hard   | Fast   | 2                |

### Power-ups

| Power-up         | Colour | Duration   | Effect                     |
| ---------------- | ------ | ---------- | -------------------------- |
| Speed Boost      | Yellow | 5 seconds  | Increases movement speed   |
| Invincibility    | Cyan   | 7 seconds  | Pass through your own body |
| Score Multiplier | Purple | 10 seconds | Doubles all points earned  |

### Themes

Press **T** in the main menu to cycle through:

- **Cyberpunk**: Neon colours with teal player and magenta AI
- **Retro**: Classic arcade with green player and magenta AI
- **Ocean**: Aquatic with cyan player and orange AI
- **Forest**: Natural with lime player and brown AI

## Project Structure

```text
v2.0/
├── play.py                 # Main launcher
├── requirements.txt        # Dependencies
├── README.md               # This file (quick reference)
├── README_DETAILED.md      # Full documentation (archived)
├── GAMEPLAY.md             # Complete gameplay strategies
├── .gitignore              # Git exclusion rules
├── src/                    # Source code directory
│   ├── snake_pygame.py     # Entry point
│   ├── game.py             # Game engine (~800 lines)
│   ├── config.py           # Constants & enums
│   ├── styles.py           # Themes & colour palettes
│   ├── snake.py            # Snake class
│   ├── power_up.py         # Power-up system
│   └── ai_player.py        # AI pathfinding (BFS)
├── docs/                   # Documentation directory
│   ├── ARCHITECTURE.md     # Technical architecture
│   └── QUICKSTART.md       # Detailed setup guide
├── db/                     # Database directory
│   └── highscores.json     # Auto-generated high scores
└── assets/                 # Optional assets folder
    └── sounds/             # Optional sound effects (.wav)
        ├── eat.wav
        ├── game_over.wav
        └── power_up.wav
```

## Troubleshooting

### Game won't start

```bash
pip install pygame
python --version  # Should be 3.7+
```

### No sound

Sound files are **optional**. Add `.wav` files to `assets/sounds/` if you want audio:

- `eat.wav`, `game_over.wav`, `power_up.wav`

### High score not saving

- Check write permissions in game directory
- Ensure `db/` folder exists (auto-created on first run)

### Theme not changing

- Press **T** only in the **main menu** (not in-game or settings)

For detailed troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## Documentation

- **README.md** (this file) - Quick reference and overview
- **[docs/QUICKSTART.md](docs/QUICKSTART.md)** - Detailed getting started guide
- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Technical architecture details
- **[docs/GAMEPLAY.md](GAMEPLAY.md)** - Complete gameplay guide with strategies
- **[docs/TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Comprehensive troubleshooting
- **[docs/README_DETAILED.md](README_DETAILED.md)** - Full detailed documentation (archived)

---

## System Requirements

- Python 3.7 or higher
- Pygame 2.5.0+
- 5 MB storage
- Optional: Sound files (WAV format)

## Future Features

- [ ] Background music support
- [ ] Local multiplayer (split screen)
- [ ] Obstacles and maze levels
- [ ] Additional themes
- [ ] Leaderboard with names
- [ ] Achievement system

---

## Development

**Author**: Oluwakemi T Obadeyi (Tech Girl Diaries)  
**Repository**: [github.com/techgirldiaries/PySnake](https://github.com/techgirldiaries/PySnake)

### Technology Stack

- Python 3.7+
- Pygame 2.5.0+
- JSON for high score persistence

### Contributing

Contributions welcome! Fork the repository and submit a pull request.

**Contribution ideas**:

- New themes and colour schemes
- Additional power-up types
- Performance optimisations
- Bug fixes
- Documentation improvements

---

## Licence

Licensed under the **PolyForm Noncommercial Licence** - Commercial use prohibited.

Copyright 2025 Oluwakemi Obadeyi

See [LICENSE.md](../LICENSE.md) for full details.

---

## Version History

### v2.0 (2026-02-19) - Modern Edition

- Complete Pygame rewrite with modular architecture
- AI Opponent mode with BFS pathfinding
- Power-ups system (Speed, Invincibility, Multiplier)
- **Dynamic theme system** with 4 colour palettes
- **In-game theme switcher** (Press T)
- Multiple difficulty levels
- High score persistence
- Professional 60 FPS graphics

### v1.1 (2025)

- Terminal version improvements
- File reading capability

### v1.0 (2020)

- Original terminal-based snake game

---

**Enjoy playing PySnake v2.0!**

Questions or feedback? Open an issue on [GitHub](https://github.com/techgirldiaries/PySnake).
