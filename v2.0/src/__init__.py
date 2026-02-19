"""
PySnake v2.0 - Modern Snake Game
A feature-rich Snake game built with Pygame

Modular Architecture:
- game.py: Main game engine with state management
- config.py: Constants, enumerations, and configuration
- styles.py: Colour palettes and theme management
- snake.py: Snake class with movement and collision
- power_up.py: Power-up system
- ai_player.py: AI opponent with pathfinding
- snake_pygame.py: Entry point

Author: Oluwakemi T Obadeyi (Tech Girl Diaries)
Version: 2.0
"""

__version__ = "2.0.0"
__author__ = "Oluwakemi T Obadeyi (Tech Girl Diaries)"

# Package-level imports for convenient access
from .config import *
from .styles import theme_manager
from .game import Game

__all__ = ['Game', 'theme_manager', '__version__', '__author__']
