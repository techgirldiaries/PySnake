"""
PySnake v2.0 - Launcher Script
Launches the game from the v2.0 root directory
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the game
from main import main

if __name__ == "__main__":
    main()
