"""
PySnake v2.0 - Modern Pygame Edition
Author: Tech Girl Diaries (Oluwakemi T Obadeyi)
Description: A modern Snake game with GUI, AI opponent, power-ups and beautiful styling!
"""

import pygame
from game import Game


def main():
    """Main entry point for PySnake v2.0"""
    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()
    
    # Create and run game
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        import traceback
        traceback.print_exc()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
