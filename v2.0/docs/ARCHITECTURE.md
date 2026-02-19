# PySnake v2.0 - Modular Architecture Documentation

## 🎉 What's New

Your PySnake game has been completely refactored with exciting new features:

### ✨ Major Features Added

1. **AI Opponent Mode** - Compete against an intelligent computer snake!
2. **Modern Aesthetic UI** - Beautiful cyberpunk/neon color scheme
3. **Modular Code Structure** - Clean, separated, maintainable modules
4. **Enhanced AI** - BFS pathfinding with skill-based decision making
5. **Dual Snake Support** - Player vs AI with separate scoring

---

## 📁 Project Structure

```text
v2.0/
├── snake_pygame.py          # Main entry point (run this!)
├── game.py                  # Core game logic & rendering
├── config.py                # Constants & enumerations
├── styles.py                # Colour palette & visual styling
├── snake.py                 # Snake class (player & AI)
├── power_up.py              # Power-up system
├── ai_player.py             # AI pathfinding & strategy
├── requirements.txt         # Python dependencies
├── README.md                # User documentation
└── assets/                  # Optional sound files
    └── sounds/
```

### 🔍 Module Breakdown

#### `snake_pygame.py` - Entry Point

- Minimal bootstrap file
- Initializes Pygame
- Creates and runs Game instance
- **Run this file to start the game!**

#### `config.py` - Configuration

- All game constants (window size, grid size, FPS)
- Enumerations (GameState, Direction, Difficulty, etc.)
- Game settings (power-up spawn rates, AI skill levels)
- **Edit this to customise game parameters**

#### `styles.py` - Visual Styling

- Modern colour palette (cyberpunk/neon theme)
- Alternative colour schemes (Retro, Ocean, Forest)
- Gradient functions
- Glow effects
- Snake segment coloring logic
- **Edit this to change the entire visual theme**

#### `snake.py` - Snake Class

- Snake data structure and movement logic
- Collision detection (walls, self, other snakes)
- Direction control with anti-reverse
- Growth mechanics
- Player type support (HUMAN/AI)
- **Core snake behavior**

#### `power_up.py` - Power-up System

- PowerUp dataclass
- PowerUpManager for spawning & tracking
- Effect management (active effects, durations)
- Collection detection
- Score multipliers and special effects
- **All power-up related logic**

#### `ai_player.py` - AI Intelligence

- AIPlayer class controlling computer snake
- BFS (Breadth-First Search) pathfinding
- Target prioritization (food vs power-ups)
- Survival strategies
- Skill-based decision making
- Random moves for unpredictability
- **AI brain and strategy**

#### `game.py` - Main Game Engine

- Game class managing all game logic
- State management (Menu, Playing, Paused, etc.)
- Input handling for all game states
- Collision detection between player and AI
- Food spawning
- Score tracking and high score persistence
- All rendering methods (menus, game, HUD)
- **The heart of the game**

---

## 🎮 New Gameplay Features

### Game Modes

#### 1. Single Player Mode

- Classic snake gameplay
- Collect food to grow
- Avoid walls and self-collision
- Power-ups for bonuses

#### 2. AI Opponent Mode ⭐ NEW

- Compete against computer opponent
- Both snakes share the same playing field
- Separate scores for player and AI
- Winner determined when one snake dies
- AI uses pathfinding to hunt food efficiently
- Watch AI strategy in real-time!

### AI Behavior

The AI opponent features:

- **Pathfinding**: Uses BFS algorithm to find optimal path to food
- **Target Selection**: Chooses between food and power-ups strategically
- **Obstacle Avoidance**: Avoids walls, bodies, and the player snake
- **Skill Levels**: AI skill scales with difficulty setting
  - Easy: 30% skill (slower updates, more mistakes)
  - Medium: 60% skill (balanced)
  - Hard: 90% skill (very competitive!)
- **Unpredictability**: ~5% random moves to prevent perfect play

### Visual Enhancements

#### Colour Scheme

- **Deep Space Background**: Dark blue-black (#0F0F23)
- **Player Snake**: Teal-green (#00FF96) with fade to tail
- **AI Snake**: Magenta-pink (#FF64FF) with fade to tail
- **Food**: Bright red-pink (#FF3250) with glow
- **Power-ups**:
  - Speed Boost: Golden yellow
  - Invincibility: Sky blue
  - Score Multiplier: Purple-pink
- **UI**: Electric cyan headers, neon accents

#### Visual Effects

- Snake body fades from head to tail
- Invincible snakes pulse with cyan glow
- Snake eyes follow movement direction
- Grid overlay for better visibility
- Rounded corners on snake segments
- Diamond-shaped power-ups
- Menu text pulsing animation

---

## 🚀 How to Play

### Installation

```bash
cd v2.0
pip install -r requirements.txt
python snake_pygame.py
```

### Controls

**Main Menu:**

- `SPACE` / `ENTER` - Start game (mode selection)
- `1` / `2` / `3` - Select difficulty
- `S` - Settings
- `Q` - Quit

**Mode Selection:**

- `1` - Single Player
- `2` - VS AI Opponent ⭐
- `ESC` - Back to menu

**In-Game:**

- `↑` `↓` `←` `→` or `W` `A` `S` `D` - Move snake
- `P` / `ESC` - Pause
- `Q` (in pause) - Quit to menu

### Difficulty Levels

| Level  | Speed       | Points | AI Skill |
| ------ | ----------- | ------ | -------- |
| Easy   | Slow (8)    | 1x     | 30%      |
| Medium | Normal (12) | 1.5x   | 60%      |
| Hard   | Fast (16)   | 2x     | 90%      |

### Power-ups

| Power-up      | Colour | Duration | Effect              |
| ------------- | ------ | -------- | ------------------- |
| Speed Boost   | Yellow | 5 sec    | +50% movement speed |
| Invincibility | Cyan   | 7 sec    | Pass through bodies |
| Score x2      | Purple | 10 sec   | Double points       |

---

## 🛠️ Customisation Guide

### Change Colours

Edit `styles.py` to change the entire visual theme:

```python
# Change background
DEEP_SPACE = (15, 15, 35)  # Your RGB colour

# Change player colour
PLAYER_PRIMARY = (0, 255, 150)  # Your RGB colour

# Use alternative theme
# Uncomment one of the preset palettes:
# RETRO_PALETTE, OCEAN_PALETTE, FOREST_PALETTE
```

### Adjust Difficulty

Edit `config.py`:

```python
class Difficulty(Enum):
    EASY = {"name": "Easy", "speed": 8, "multiplier": 1, "ai_skill": 0.3}
    # Change speed (higher = faster)
    # Change multiplier (points per food)
    # Change ai_skill (0.0-1.0, higher = smarter AI)
```

### Modify AI Behavior

Edit `config.py`:

```python
AI_UPDATE_FREQUENCY = 5  # Lower = AI thinks more often
AI_RANDOM_MOVE_CHANCE = 0.05  # Higher = more unpredictable
```

### Change Game Parameters

Edit `config.py`:

```python
WINDOW_WIDTH = 800  # Window size
WINDOW_HEIGHT = 600
GRID_SIZE = 20  # Size of each grid cell
FPS = 60  # Frames per second

POWER_UP_SPAWN_CHANCE = 0.3  # 30% chance per food
POWER_UP_MAX_ON_SCREEN = 2  # Maximum simultaneous power-ups
```

---

## 🏆 Score System

### Single Player

- Scores saved to `highscores.json` under key: `single_player`
- Base score: 10 points per food
- Multiplied by difficulty multiplier
- Multiplied by power-up if active

### AI Opponent

- Player score saved under: `ai_opponent_player`
- AI score saved under: `ai_opponent_ai`
- Same scoring rules as single player
- Winner gets bragging rights! 🎉

---

## 🧪 Testing & Development

### Run Tests

```bash
python -m pytest tests/  # If you add unit tests
```

### Debug Mode

Add to `game.py`:

```python
# In Game.__init__:
self.debug_mode = True  # Show AI pathfinding, collision boxes, etc.
```

### Performance Monitoring

Check FPS in terminal:

```python
# In game.py update() method:
if self.move_counter % 60 == 0:
    print(f"FPS: {self.clock.get_fps():.1f}")
```

---

## 📈 Future Enhancement Ideas

### Easy Additions

- [ ] Add more power-up types (Shrink, Teleport, Shield)
- [ ] Implement obstacles/walls mode
- [ ] Add sound effects (files ready in assets/)
- [ ] Create custom themes (change styles.py)

### Medium Additions

- [ ] Local multiplayer (2 human players)
- [ ] Campaign mode with levels
- [ ] Achievement system
- [ ] More AI personalities (aggressive, defensive, balanced)

### Advanced Additions

- [ ] Online multiplayer
- [ ] Leaderboard with names
- [ ] Replay system
- [ ] Level editor
- [ ] Mobile version (Pygame Subset for Android)

---

## 🐛 Troubleshooting

### Game Won't Start

```
Error: ModuleNotFoundError: No module named 'pygame'
```

**Solution:** `pip install pygame`

### Import Errors

```
Error: ImportError: cannot import name 'Game' from 'game'
```

**Solution:** Make sure all module files are in v2.0/ directory

### AI Not Moving

**Solution:** Check that `ai_controller.update()` is being called in `game.py`

### Colors Look Wrong

**Solution:** Verify RGB values are tuples: `(R, G, B)` where each is 0-255

### Performance Issues

**Solution:**

- Reduce FPS in config.py
- Reduce WINDOW_WIDTH/HEIGHT
- Decrease AI_UPDATE_FREQUENCY

---

## 📝 Code Quality

### Architecture Benefits

✅ **Separation of Concerns**: Each module has a single responsibility  
✅ **Reusability**: Snake class works for both player and AI  
✅ **Maintainability**: Easy to find and fix bugs  
✅ **Extensibility**: Add features without breaking existing code  
✅ **Testability**: Each module can be tested independently  
✅ **Readability**: Clear, documented code with type hints

### Design Patterns Used

- **State Pattern**: GameState enum with state-based rendering
- **Strategy Pattern**: AIPlayer implements different strategies
- **Factory Pattern**: PowerUpManager creates power-ups
- **Observer Pattern**: Event system for input handling
- **Singleton**: Game class manages single game instance

---

## 🎓 Learning Resources

### Understanding the Code

1. Start with `snake_pygame.py` (entry point)
2. Read `config.py` to understand constants
3. Study `snake.py` for game objects
4. Explore `game.py` for game loop
5. Analyze `ai_player.py` for algorithms

### Algorithms Used

- **BFS**: Breadth-First Search in AI pathfinding
- **State Machine**: Game state management
- **Collision Detection**: AABB (Axis-Aligned Bounding Box)
- **Manhattan Distance**: AI distance calculations

### Python Features Demonstrated

- Enums (`Enum`)
- Dataclasses (`@dataclass`)
- Type Hints (`List[Tuple[int, int]]`)
- Context Managers (`with open()`)
- List Comprehensions
- Dictionary Comprehensions
- F-strings
- Exception Handling

---

## 🤝 Contributing

Feel free to:

- Add new features
- Improve AI intelligence
- Create new colour themes
- Optimise performance
- Write documentation
- Report bugs

---

## 📄 License

Licensed under the **PolyForm Noncommercial License**  
**Copyright © 2025 Oluwakemi Obadeyi**

Commercial use is prohibited. See LICENSE.md for details.

---

**Enjoy your modernized, modular PySnake! 🐍✨**

_Created by: Tech Girl Diaries (Oluwakemi T Obadeyi)_  
_Enhanced: February 19, 2026_
