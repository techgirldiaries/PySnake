# PySnake (Python Snake) Game 🐍

Welcome to PySnake, a classic snake game implemented in Python. This project provides both a simple terminal-based version and a modern GUI version for Python enthusiasts and gamers alike.

**Current Version**: 2.0 (Modern Edition)  
**Original Version**: 1.1 (Terminal Edition)  
**Contributor**: Tech Girl Diaries (Oluwakemi T Obadeyi)

---

## 📦 Available Versions

### v1.0 - Terminal Edition (Classic)

Simple curses-based terminal snake game perfect for learning Python basics.

- Location: Root directory (`snake.py`)
- No dependencies beyond Python standard library
- 70 lines of code
- ASCII graphics

### v2.0 - Modern Edition (GUI)

Feature-rich Pygame implementation with power-ups, menus, and persistent high scores.

- Location: `v2.0/` directory
- Requires Pygame
- 650+ lines of professional code
- Full GUI with smooth graphics

## 🎮 PySnake v2.0 - Modern Edition

A modern, feature-rich Snake game built with Pygame featuring smooth graphics, power-ups, multiple difficulty levels and more!

## ✨ Features

### Core Gameplay

- **Smooth Graphics**: 800x600 window with grid-based movement
- **Intuitive Controls**: Arrow keys or WASD for movement
- **Multiple Difficulty Levels**: Easy, Medium and Hard
- **Score System**: Points with multipliers based on difficulty

### Advanced Features

- 🎮 **Power-ups System**:
  - **Speed Boost** (Yellow) - Temporarily increases snake speed
  - **Invincibility** (Cyan) - Pass through your own body
  - **Score Multiplier** (Purple) - 2x points for a limited time

- 🎯 **Game States**:
  - Main Menu with difficulty selection
  - Settings menu for customization
  - Pause functionality (ESC or P)
  - Game Over screen with statistics

- 💾 **Persistent Data**:
  - High score tracking saved to `highscore.json`
  - Auto-saves when you beat your record

- 🎨 **Visual Polish**:
  - Animated snake with eyes that follow direction
  - Color-coded power-ups
  - Smooth fading effect on snake body
  - Grid overlay for better visibility
  - Real-time HUD with score and active effects

### Settings

- Sound effects toggle (when audio files available)
- Music toggle (when audio files available)
- Power-ups enable/disable

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

1. **Run the game**:

```bash
python snake_pygame.py
```

That's it! The game will run even without audio files.

---

## 🕹️ PySnake v1.0/v1.1 - Terminal Edition (Classic)

The original simple terminal-based snake game using Python's curses library.

### Features

- Simple and intuitive controls
- Terminal-based ASCII graphics
- Increasing difficulty as the snake grows longer
- Lightweight with no external dependencies
- Perfect for learning Python basics

### How to Play (v1.0 Terminal)

1. Navigate to the root PySnake directory
2. Run the game:

```bash
python snake.py
```

1. Use the arrow keys to control the snake and collect food to grow
2. Avoid hitting the walls or your own body
3. Game over occurs when you collide with walls or yourself

### Version 1.1 Improvements

- Fixed issues and performance improvements
- Added ability to read from file

---

## 🎮 Controls

### Menu

- **SPACE/ENTER**: Start game
- **1/2/3**: Select difficulty (Easy/Medium/Hard)
- **S**: Settings
- **Q**: Quit

### In-Game

- **Arrow Keys** or **WASD**: Move snake
- **ESC** or **P**: Pause
- **Q** (in pause): Quit to menu

### Pause Menu

- **ESC** or **P**: Resume
- **Q**: Quit to menu

### Game Over

- **SPACE/ENTER**: Play again
- **Q/ESC**: Return to menu

## 🎵 Optional: Adding Sound Effects

To enable sound effects, add `.wav` files to the `assets/sounds/` directory:

- `eat.wav` - Played when snake eats food
- `game_over.wav` - Played on game over
- `power_up.wav` - Played when collecting power-ups

The game works perfectly without these files!

### Free Sound Resources

- [Freesound.org](https://freesound.org/)
- [OpenGameArt.org](https://opengameart.org/)
- [ZapSplat](https://www.zapsplat.com/)

## 📊 Difficulty Levels

| Level  | Speed  | Score Multiplier |
| ------ | ------ | ---------------- |
| Easy   | Slow   | 1x               |
| Medium | Normal | 1.5x             |
| Hard   | Fast   | 2x               |

**Note**: Speed increases as your snake grows longer!

## 🎯 Power-ups Duration

| Power-up         | Duration   |
| ---------------- | ---------- |
| Speed Boost      | 5 seconds  |
| Invincibility    | 7 seconds  |
| Score Multiplier | 10 seconds |

## 🏆 Scoring System

- Base points per food: 10
- Multiplied by difficulty level
- Multiplied again if Score Multiplier power-up is active
- Example: On Hard with 2x power-up = 10 × 2 × 2 = 40 points per food!

## 🛠️ Technical Details

### Architecture

- **Object-Oriented Design**: Clean separation of concerns with Snake, Game and PowerUp classes
- **State Machine**: Proper game state management (Menu, Playing, Paused, Game Over, Settings)
- **Enum Classes**: Type-safe direction, difficulty and power-up types
- **Dataclasses**: Modern Python data structures

### Performance

- Runs at 60 FPS for smooth animations
- Movement speed calculated independently from rendering
- Efficient collision detection

### File Structure

```text
v2.0/
├── snake_pygame.py      # Main game file
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── highscore.json      # Created automatically to store high scores
└── assets/            # Optional assets folder
    └── sounds/        # Optional sound effects
        ├── eat.wav
        ├── game_over.wav
        └── power_up.wav
```

## 🎮 Gameplay Tips

1. **Plan Ahead**: Think about where your tail will be, not just where you're going
2. **Use Power-ups Wisely**: Invincibility can help you navigate tight spots
3. **Speed Management**: Speed Boost makes scoring faster but also more dangerous
4. **Corner Strategy**: Stay near edges early game, move to center as you grow
5. **Spiral Pattern**: When large, spiral from outside to inside

## 🐛 Troubleshooting

### Game won't start

- Make sure Pygame is installed: `pip install pygame`
- Check Python version: `python --version` (should be 3.7+)

### No sound

- This is normal! Sound files are optional
- Add `.wav` files to `assets/sounds/` if you want audio

### Game too fast/slow

- Adjust difficulty in the main menu (keys 1, 2, 3)
- Speed also increases naturally as snake grows

### High score not saving

- Check write permissions in the game directory
- The game creates `highscore.json` automatically

## 🔮 Future Enhancements (Ideas)

- [ ] Background music support
- [ ] Multiplayer mode (local)
- [ ] Obstacles mode
- [ ] Custom themes/skins
- [ ] Leaderboard with names
- [ ] Online multiplayer
- [ ] Mobile touch controls
- [ ] Achievement system
- [ ] Daily challenges

## 📝 Version History

### v2.0 (2026-02-19) - Modern Edition

- Complete rewrite with Pygame
- Added power-ups system (Speed Boost, Invincibility, Score Multiplier)
- Multiple difficulty levels (Easy, Medium, Hard)
- Modern menu system with GUI
- Settings menu
- High score persistence to file
- Visual polish and animations
- Snake with animated eyes
- Real-time HUD display
- Pause functionality

### v1.1 (2025)

- Fixed issues and performance improvements
- Added ability to read from file
- First stable release

### v1.0 (2020-06-10)

- First attempt at Snake game
- Basic terminal implementation

### v0.4.1.3 (2020-06-10)

- Original curses-based terminal version
- Arrow key controls
- Basic collision detection
- Food spawn system

## 👨‍💻 Development

**Author**: Oluwakemi T Obadeyi (Tech Girl Diaries)  
**Repository**: [github.com/techgirldiaries/PySnake](https://github.com/techgirldiaries/PySnake)

Built with:

- **Python 3.x**
- **Pygame 2.5.0+** (v2.0 only)
- **curses** (v1.0/v1.1 - standard library)
- **Love** ❤️

## 📄 License

Licensed under the **PolyForm Noncommercial License** - Commercial use is prohibited

Copyright © 2025 Oluwakemi Obadeyi

See LICENSE.md in the root directory for full license details.

## 🤝 Contributing

Feel free to fork, modify and submit pull requests! This is a learning project and contributions are welcome.

---

Enjoy playing PySnake v2.0! 🐍🎮

Questions or issues? Feel free to open an issue on GitHub.
