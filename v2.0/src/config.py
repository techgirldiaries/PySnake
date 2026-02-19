"""
PySnake v2.0 - Configuration and Constants
Contains all game constants, enums, and configuration settings
"""

from enum import Enum

# Window Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 60

# Game States
class GameState(Enum):
    MENU = 1
    MODE_SELECT = 2
    PLAYING = 3
    PAUSED = 4
    GAME_OVER = 5
    SETTINGS = 6

# Game Modes
class GameMode(Enum):
    SINGLE_PLAYER = 1
    AI_OPPONENT = 2

# Directions
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

# Difficulty Levels
class Difficulty(Enum):
    EASY = {"name": "Easy", "speed": 8, "multiplier": 1, "ai_skill": 0.3}
    MEDIUM = {"name": "Medium", "speed": 12, "multiplier": 1.5, "ai_skill": 0.6}
    HARD = {"name": "Hard", "speed": 16, "multiplier": 2, "ai_skill": 0.9}

# Power-up Types  
class PowerUpType(Enum):
    SPEED_BOOST = {"name": "Speed Boost", "duration": 5000}
    INVINCIBILITY = {"name": "Invincibility", "duration": 7000}
    SCORE_MULTIPLIER = {"name": "Score x2", "duration": 10000}

# Player Types
class PlayerType(Enum):
    HUMAN = 1
    AI = 2

# Visual Themes
class Theme(Enum):
    CYBERPUNK = "Cyberpunk"
    RETRO = "Retro Arcade"
    OCEAN = "Ocean"
    FOREST = "Forest"

# Font Sizes
FONT_XLARGE = 84
FONT_LARGE = 72
FONT_MEDIUM = 48
FONT_SMALL = 36
FONT_TINY = 24
FONT_MICRO = 18

# Sound Files (relative to parent directory)
SOUND_FILES = {
    'eat': '../assets/sounds/eat.wav',
    'game_over': '../assets/sounds/game_over.wav',
    'power_up': '../assets/sounds/power_up.wav'
}

# Game Settings
POWER_UP_SPAWN_CHANCE = 0.3
POWER_UP_MAX_ON_SCREEN = 2
POWER_UP_LIFETIME = 15000  # milliseconds
INITIAL_SNAKE_LENGTH = 3
SPEED_INCREASE_PER_10_SEGMENTS = 1

# AI Settings
AI_UPDATE_FREQUENCY = 5  # Update AI path every N frames
AI_RANDOM_MOVE_CHANCE = 0.05  # 5% chance of random move (adds unpredictability)
