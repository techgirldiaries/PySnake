# PySnake (Python Snake) Game 🐍

A classic snake game implemented in Python, available in both terminal-based and modern GUI versions. Perfect for Python enthusiasts and gamers alike.

**Current Version**: 2.0 (Modern Edition)  
**Original Version**: 1.1 (Terminal Edition)  
**Contributor**: Tech Girl Diaries

---

## 📋 Table of Contents

1. [Quick Start](#-quick-start)
2. [Available Versions](#-available-versions)
3. [Features](#-features)
4. [Controls](#-controls)
5. [Gameplay Guide](#-gameplay-guide)
6. [Technical Documentation](#-technical-documentation)
7. [Troubleshooting](#-troubleshooting)
8. [Development](#-development)
9. [Licence](#-licence)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation (v2.0 Modern Edition)

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the game**:

   ```bash
   python play.py
   ```

   Or, if you prefer to run from the src directory:

   ```bash
   cd src
   python snake_pygame.py
   ```

3. **Upgrade Python and pip** (if needed):

   ```bash
   python.exe -m pip install --upgrade pip
   ```

That's it! The game runs even without audio files.

### Installation (v1.0 Terminal Edition)

1. Navigate to the root PySnake directory
2. Run the game:

   ```bash
   python snake.py
   ```

No external dependencies required!

---

## 📦 Available Versions

### v2.0 - Modern Edition (GUI)

Feature-rich Pygame implementation with power-ups, AI opponent, multiple game modes and persistent high scores.

- **Location**: `v2.0/` directory
- **Requires**: Pygame 2.5.0+
- **Code**: 2000+ lines of professional modular architecture
- **Graphics**: Full GUI with smooth animations
- **Features**: AI opponent, power-ups system, customisable themes, multiple difficulty levels

### v1.0 - Terminal Edition (Classic)

Simple curses-based terminal snake game, perfect for learning Python basics.

- **Location**: Root directory (`snake.py`)
- **Requires**: Python standard library only (curses)
- **Code**: 70 lines
- **Graphics**: ASCII characters

---

## ✨ Features

### v2.0 Modern Edition

#### Core Gameplay

- **Smooth Graphics**: 800×600 window with grid-based movement running at 60 FPS
- **Intuitive Controls**: Arrow keys or WASD for movement, ESC for pause
- **Game Modes**:
  - **Single Player**: Classic snake gameplay with power-ups
  - **AI Opponent**: Compete against an intelligent computer snake with BFS pathfinding
- **Multiple Difficulty Levels**: Easy, Medium and Hard with speed and score multipliers
- **Dynamic Themes**: Four beautiful colour schemes (Cyberpunk, Retro, Ocean, Forest)
- **Score System**: Points with difficulty-based multipliers and power-up bonuses

#### Advanced Features

- 🎮 **Power-ups System**:
  - **Speed Boost** (Yellow) - Temporarily increases snake speed for 5 seconds
  - **Invincibility** (Cyan) - Pass through your own body for 7 seconds
  - **Score Multiplier** (Purple) - 2× points for 10 seconds

- 🤖 **AI Opponent**:
  - Intelligent pathfinding using BFS (Breadth-First Search) algorithm
  - Competes for food and power-ups
  - Displays separate score for human vs AI
  - Colour-coded snakes (Teal for Player, Magenta for AI)

- 🎯 **Game States**:
  - Main menu with difficulty and theme selection
  - Mode selection (Single Player or AI Opponent)
  - Settings menu for customisation
  - Pause functionality (ESC or P)
  - Game over screen with detailed statistics

- 💾 **Persistent Data**:
  - High score tracking saved to `db/highscores.json`
  - Separate high scores for Single Player and AI Opponent modes
  - Auto-saves when you beat your record
  - Database folder automatically created on first run

- 🎨 **Visual Styling**:
  - Animated snake with eyes that follow movement direction
  - Colour-coded power-ups with visual effects
  - Smooth gradient fading on snake body
  - Grid overlay for better visibility
  - Real-time HUD with score, high score and active effects
  - Theme-specific colour palettes for immersive experience

#### Module Architecture (Clean & Maintainable)

v2.0 uses a professional modular structure for scalability:

- **config.py**: Game constants, enumerations and configuration values
- **styles.py**: Colour palettes, theme management and visual styling
- **snake.py**: Snake class with movement, collision detection and rendering
- **power_up.py**: Power-up spawning, collection and effect management
- **ai_player.py**: AI pathfinding logic and decision-making algorithms
- **game.py**: Main game engine with state management and rendering
- **snake_pygame.py**: Entry point for the application

#### Customisation Settings

- Sound effects toggle (when audio files available)
- Music toggle (when audio files available)
- Power-ups enable/disable
- **Theme switching** (Press T in main menu to cycle through themes)

### v1.0 Terminal Edition

- Simple and intuitive arrow key controls
- Terminal-based ASCII graphics
- Increasing difficulty as the snake grows longer
- Lightweight with no external dependencies
- Perfect for learning Python basics

---

## 🎮 Controls

### v2.0 Modern Edition

#### Main Menu

- **SPACE/ENTER**: Start game (proceed to mode selection)
- **1/2/3**: Select difficulty (Easy/Medium/Hard)
- **T**: Cycle themes (Cyberpunk → Retro → Ocean → Forest)
- **S**: Settings
- **Q**: Quit game

#### Mode Selection

- **1**: Single Player mode
- **2**: AI Opponent mode
- **ESC**: Back to main menu

#### In-Game

- **Arrow Keys** or **WASD**: Move snake (UP/W, DOWN/S, LEFT/A, RIGHT/D)
- **ESC** or **P**: Pause game
- **Q** (in pause menu): Quit to menu

#### Pause Menu

- **ESC** or **P**: Resume game
- **Q**: Quit to main menu

#### Game Over

- **SPACE/ENTER**: Play again with same settings
- **Q/ESC**: Return to main menu

### v1.0 Terminal Edition

- **Arrow Keys**: Move snake (↑ ↓ ← →)
- **Q** or **Ctrl+C**: Quit game

---

## 📖 Gameplay Guide

### Difficulty Levels

| Level  | Speed  | Score Multiplier | Description             |
| ------ | ------ | ---------------- | ----------------------- |
| Easy   | Slow   | 1×               | Ideal for beginners     |
| Medium | Normal | 1.5×             | Balanced challenge      |
| Hard   | Fast   | 2×               | For experienced players |

**Note**: Speed increases progressively as your snake grows longer!

### Themes

| Theme     | Style           | Colour Palette                                 |
| --------- | --------------- | ---------------------------------------------- |
| Cyberpunk | Neon/Futuristic | Teal player, magenta AI, deep space background |
| Retro     | Classic Arcade  | Green player, magenta AI, black background     |
| Ocean     | Aquatic         | Cyan player, orange AI, deep blue background   |
| Forest    | Natural         | Lime player, brown AI, dark green background   |

**Tip**: Press **T** in the main menu to switch themes instantly!

### Power-ups

| Power-up         | Colour | Duration   | Effect                                   |
| ---------------- | ------ | ---------- | ---------------------------------------- |
| Speed Boost      | Yellow | 5 seconds  | Increases movement speed significantly   |
| Invincibility    | Cyan   | 7 seconds  | Pass through your own body without dying |
| Score Multiplier | Purple | 10 seconds | Doubles all points earned                |

**Strategy**: Power-ups spawn randomly. Collect them to gain temporary advantages!

### Scoring System

- **Base points per food**: 10
- **Multiplied by difficulty level** (1×, 1.5×, or 2×)
- **Multiplied again if Score Multiplier power-up is active**
- **Example**: On Hard difficulty with 2× power-up = 10 × 2 × 2 = **40 points per food**!

### Strategy Tips

1. **Plan Ahead**: Think about where your tail will be, not just your head's direction
2. **Use Power-ups Wisely**: Invincibility helps navigate tight spaces when your snake is large
3. **Speed Management**: Speed Boost allows faster scoring but increases danger
4. **Corner Strategy**: Stay near edges in early game, move towards centre as you grow
5. **Spiral Pattern**: When your snake is large, create spirals from outside to inside
6. **AI Competition**: In AI mode, race the computer to food and power-ups for higher scores

### AI Opponent Mode

- AI uses **Breadth-First Search (BFS)** pathfinding to navigate efficiently
- AI targets food, power-ups and avoids collisions
- Separate score tracking for Human vs AI
- First to reach target score or last snake standing wins!

---

## 🔧 Technical Documentation

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.7 or higher
- **Dependencies**: Pygame 2.5.0+ (v2.0 only)
- **Display**: 800×600 minimum resolution
- **Storage**: ~5 MB (including code and optional audio files)

### Architecture

#### Design Patterns (v2.0)

- **Object-Oriented Design**: Clean separation of concerns with Snake, Game, PowerUpManager and AIPlayer classes
- **State Machine**: Proper game state management using GameState enum (MENU, MODE_SELECT, PLAYING, PAUSED, GAME_OVER, SETTINGS)
- **Strategy Pattern**: AI behaviour encapsulated in AIPlayer class
- **Factory Pattern**: Power-up creation and management in PowerUpManager
- **Singleton Pattern**: ThemeManager for global theme state
- **Enum Classes**: Type-safe enumerations for Direction, Difficulty, PowerUpType, PlayerType, GameMode and Theme

#### Data Structures

- **Dataclasses**: Modern Python data structures for PowerUp objects
- **Deque**: Efficient snake body management using collections.deque
- **Dictionary**: Fast lookup for high scores and theme colour palettes

### Performance

- **Frame Rate**: 60 FPS for smooth animations and responsive controls
- **Movement Speed**: Calculated independently from rendering loop for consistent gameplay
- **Collision Detection**: Efficient algorithms checking only relevant game objects
- **Memory Management**: Optimised to handle large snakes without performance degradation

### File Structure

```text
PySnake/
├── snake.py                    # v1.0 Terminal Edition
├── LICENSE.md                  # Licence information
├── README.md                   # Project overview
└── v2.0/                       # Modern Edition
    ├── play.py                 # Main launcher script
    ├── requirements.txt        # Python dependencies
    ├── README.md               # This file
    ├── .gitignore              # Git exclusion rules
    ├── src/                    # Source code directory
    │   ├── __init__.py         # Package initialisation
    │   ├── snake_pygame.py     # Entry point (58 lines)
    │   ├── game.py             # Main game engine (~700 lines)
    │   ├── config.py           # Constants and enums (~85 lines)
    │   ├── styles.py           # Colour palettes and themes (~200 lines)
    │   ├── snake.py            # Snake class (~180 lines)
    │   ├── power_up.py         # Power-up system (~170 lines)
    │   └── ai_player.py        # AI pathfinding (~250 lines)
    ├── docs/                   # Documentation directory
    │   ├── ARCHITECTURE.md     # Detailed technical documentation
    │   └── QUICKSTART.md       # Quick start guide
    ├── db/                     # Database directory
    │   └── highscores.json     # Auto-generated high score storage
    └── assets/                 # Optional assets folder
        ├── README.md           # Assets information
        └── sounds/             # Optional sound effects
            ├── eat.wav
            ├── game_over.wav
            └── power_up.wav
```

### Audio System (Optional)

To enable sound effects, add `.wav` files to the `assets/sounds/` directory:

- **eat.wav** - Played when snake consumes food
- **game_over.wav** - Played on game over
- **power_up.wav** - Played when collecting power-ups

**Note**: The game works perfectly without audio files! Sound is completely optional.

#### Free Sound Resources

- [Freesound.org](https://freesound.org/) - Creative Commons audio library
- [OpenGameArt.org](https://opengameart.org/) - Free game assets
- [ZapSplat](https://www.zapsplat.com/) - Sound effects library

---

## 🐛 Troubleshooting

### Game Won't Start

**Problem**: Error when running `python play.py`

**Solutions**:

- Ensure Pygame is installed: `pip install pygame`
- Check Python version: `python --version` (should be 3.7 or higher)
- Verify you're in the `v2.0/` directory
- Try reinstalling dependencies: `pip install -r requirements.txt --force-reinstall`

### No Sound

**Problem**: Game runs but no audio plays

**Solution**: This is normal! Sound files are **optional**. Add `.wav` files to `assets/sounds/` directory if you want audio. The game is fully functional without sound.

### Game Too Fast/Slow

**Problem**: Movement speed doesn't feel right

**Solutions**:

- Adjust difficulty in the main menu (press **1** for Easy, **2** for Medium, **3** for Hard)
- Remember: Speed increases naturally as your snake grows longer
- Try different themes - some may feel faster due to colour contrast

### High Score Not Saving

**Problem**: High score resets when restarting the game

**Solutions**:

- Check write permissions in the game directory
- The game automatically creates `db/highscores.json` in the database folder
- Ensure the file and folder aren't read-only
- On Windows, try running as Administrator if permission issues persist

### Theme Not Changing

**Problem**: Pressing **T** doesn't switch themes

**Solution**: Ensure you're in the **main menu**, not in-game or in settings. Theme switching only works from the main menu screen.

### AI Opponent Freezes

**Problem**: AI snake stops moving or behaves erratically

**Solution**: This is rare but can occur if the AI gets trapped. Restart the game. The BFS algorithm should prevent this in most cases.

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'pygame'`

**Solutions**:

- Install Pygame: `pip install pygame`
- If using virtual environment, ensure it's activated
- Check pip is installing to the correct Python version: `python -m pip install pygame`

### Terminal Edition Not Working

**Problem**: v1.0 `snake.py` crashes or displays incorrectly

**Solutions**:

- Ensure you're using a terminal that supports curses (bash, PowerShell, Command Prompt)
- On Windows, try Windows Terminal for better compatibility
- Check Python installation includes curses library (standard on most systems)

---

## 🔮 Future Enhancements

Planned features for upcoming versions:

- [ ] Background music support
- [ ] Local multiplayer mode (split screen)
- [ ] Obstacles and maze levels
- [ ] Additional custom themes/skins
- [ ] Leaderboard with player names
- [ ] Online multiplayer functionality
- [ ] Mobile touch controls
- [ ] Achievement system with badges
- [ ] Daily challenges and missions
- [ ] Level editor for custom maps

---

## 📝 Version History

### v2.0 (2026-02-19) - Modern Edition

- Complete rewrite using Pygame with modular architecture
- Added AI Opponent mode with BFS pathfinding algorithm
- Implemented power-ups system (Speed Boost, Invincibility, Score Multiplier)
- Multiple difficulty levels (Easy, Medium, Hard) with dynamic speed scaling
- **Theme system** with four colour palettes (Cyberpunk, Retro, Ocean, Forest)
- **In-game theme switcher** (Press T in menu)
- Modern menu system with GUI and state management
- Settings menu for customisation options
- High score persistence to JSON file with separate tracking for each game mode
- Visual polish: animated snake eyes, gradient effects, real-time HUD
- Comprehensive documentation (README, ARCHITECTURE, QUICKSTART)
- Professional modular code structure (7 separate modules, ~2000 lines)

### v1.1 (2025)

- Fixed issues and performance improvements
- Added ability to read from file
- First stable release of terminal version

### v1.0 (2020-06-10)

- First attempt at Snake game
- Basic terminal implementation using curses

### v0.4.1.3 (2020-06-10)

- Original curses-based terminal version
- Arrow key controls
- Basic collision detection
- Food spawn system

---

## 👨‍💻 Development

**Author**: Oluwakemi T Obadeyi (Tech Girl Diaries)  
**Repository**: [github.com/techgirldiaries/PySnake](https://github.com/techgirldiaries/PySnake)

### Technology Stack

- **Python 3.7+**: Core programming language
- **Pygame 2.5.0+**: Graphics and game engine (v2.0 only)
- **curses**: Terminal graphics library (v1.0/v1.1 - standard library)
- **JSON**: High score persistence
- **Collections**: Deque for efficient snake body management

### Contributing

We welcome contributions! This is a learning project and pull requests are appreciated.

**How to contribute**:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Contribution ideas**:

- New themes and colour schemes
- Additional power-up types
- Performance optimisations
- Bug fixes and issue resolution
- Documentation improvements
- New game modes

---

## 📄 Licence

Licensed under the **PolyForm Noncommercial Licence** - Commercial use is prohibited.

Copyright © 2025 Oluwakemi Obadeyi

See [LICENSE.md](../LICENSE.md) in the root directory for full licence details.

---

## 🙏 Acknowledgements

- Built with ❤️ and Python
- Inspired by the classic Snake game
- Thanks to the Pygame community for excellent documentation
- Sound effects from various Creative Commons sources (optional)

---

**Enjoy playing PySnake v2.0!** 🐍🎮

Questions, feedback, or issues? Feel free to open an issue on [GitHub](https://github.com/techgirldiaries/PySnake).
