"""
PySnake v2.0 - Modern Pygame Edition
Author: ETech Girl Diaries
Description: A modern Snake game with GUI, sound effects, power-ups and more!
"""

import pygame
import random
import json
import os
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Optional

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
DARK_GREEN = (0, 150, 0)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (200, 200, 200)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)

# Game States
class GameState(Enum):
    MENU = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
    SETTINGS = 5

# Directions
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

# Difficulty Levels
class Difficulty(Enum):
    EASY = {"name": "Easy", "speed": 8, "multiplier": 1}
    MEDIUM = {"name": "Medium", "speed": 12, "multiplier": 1.5}
    HARD = {"name": "Hard", "speed": 16, "multiplier": 2}

# Power-up Types
class PowerUpType(Enum):
    SPEED_BOOST = {"name": "Speed Boost", "color": YELLOW, "duration": 5000}
    INVINCIBILITY = {"name": "Invincibility", "color": CYAN, "duration": 7000}
    SCORE_MULTIPLIER = {"name": "Score x2", "color": PURPLE, "duration": 10000}

@dataclass
class PowerUp:
    type: PowerUpType
    position: Tuple[int, int]
    spawn_time: int

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.body = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y)
        ]
        self.direction = Direction.RIGHT
        self.grow_pending = 0
        self.invincible = False
        
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x, head_y)
        
        if self.direction == Direction.UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == Direction.DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == Direction.LEFT:
            new_head = (head_x - 1, head_y)
        elif self.direction == Direction.RIGHT:
            new_head = (head_x + 1, head_y)
        
        self.body.insert(0, new_head)
        
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    
    def change_direction(self, new_direction: Direction):
        # Prevent reversing into itself
        opposite = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        
        if new_direction != opposite.get(self.direction):
            self.direction = new_direction
    
    def grow(self, amount: int = 1):
        self.grow_pending += amount
    
    def check_collision(self) -> bool:
        head = self.body[0]
        
        # Wall collision
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        
        # Self collision (don't count invincibility)
        if not self.invincible and head in self.body[1:]:
            return True
        
        return False

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("PySnake v2.0 - Modern Edition")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        self.font_tiny = pygame.font.Font(None, 24)
        
        self.state = GameState.MENU
        self.snake = Snake()
        self.food_position = self.spawn_food()
        self.score = 0
        self.high_score = self.load_high_score()
        self.difficulty = Difficulty.MEDIUM
        self.move_counter = 0
        self.power_ups: List[PowerUp] = []
        self.active_power_ups = {}
        self.score_multiplier = 1
        
        # Settings
        self.sound_enabled = True
        self.music_enabled = True
        self.power_ups_enabled = True
        
        # Load/Create sound effects (will work even if files don't exist)
        self.sounds = self.load_sounds()
        
    def load_sounds(self):
        """Load sound effects if they exist, otherwise return empty dict"""
        sounds = {}
        sound_files = {
            'eat': 'assets/sounds/eat.wav',
            'game_over': 'assets/sounds/game_over.wav',
            'power_up': 'assets/sounds/power_up.wav'
        }
        
        for name, path in sound_files.items():
            try:
                if os.path.exists(path):
                    sounds[name] = pygame.mixer.Sound(path)
            except:
                pass
        
        return sounds
    
    def play_sound(self, sound_name: str):
        """Play sound effect if it exists and sound is enabled"""
        if self.sound_enabled and sound_name in self.sounds:
            self.sounds[sound_name].play()
    
    def spawn_food(self) -> Tuple[int, int]:
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in self.snake.body:
                return pos
    
    def spawn_power_up(self):
        if not self.power_ups_enabled or len(self.power_ups) >= 2:
            return
        
        if random.random() < 0.3:  # 30% chance
            power_type = random.choice(list(PowerUpType))
            pos = self.spawn_food()  # Use same logic to avoid snake
            self.power_ups.append(PowerUp(power_type, pos, pygame.time.get_ticks()))
    
    def update_power_ups(self):
        current_time = pygame.time.get_ticks()
        
        # Remove expired power-ups from world
        self.power_ups = [pu for pu in self.power_ups if current_time - pu.spawn_time < 15000]
        
        # Remove expired active power-ups
        expired = []
        for pu_type, start_time in self.active_power_ups.items():
            duration = pu_type.value['duration']
            if current_time - start_time > duration:
                expired.append(pu_type)
        
        for pu_type in expired:
            del self.active_power_ups[pu_type]
            if pu_type == PowerUpType.INVINCIBILITY:
                self.snake.invincible = False
            elif pu_type == PowerUpType.SCORE_MULTIPLIER:
                self.score_multiplier = 1
    
    def collect_power_up(self, power_up: PowerUp):
        self.play_sound('power_up')
        self.active_power_ups[power_up.type] = pygame.time.get_ticks()
        
        if power_up.type == PowerUpType.INVINCIBILITY:
            self.snake.invincible = True
        elif power_up.type == PowerUpType.SCORE_MULTIPLIER:
            self.score_multiplier = 2
        elif power_up.type == PowerUpType.SPEED_BOOST:
            pass  # Handled in movement
    
    def load_high_score(self) -> int:
        try:
            if os.path.exists('highscore.json'):
                with open('highscore.json', 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
        except:
            pass
        return 0
    
    def save_high_score(self):
        try:
            with open('highscore.json', 'w') as f:
                json.dump({'high_score': self.high_score}, f)
        except:
            pass
    
    def reset_game(self):
        self.snake.reset()
        self.food_position = self.spawn_food()
        self.score = 0
        self.move_counter = 0
        self.power_ups.clear()
        self.active_power_ups.clear()
        self.score_multiplier = 1
        self.state = GameState.PLAYING
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.state == GameState.MENU:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.reset_game()
                    elif event.key == pygame.K_s:
                        self.state = GameState.SETTINGS
                    elif event.key == pygame.K_q:
                        return False
                    elif event.key == pygame.K_1:
                        self.difficulty = Difficulty.EASY
                    elif event.key == pygame.K_2:
                        self.difficulty = Difficulty.MEDIUM
                    elif event.key == pygame.K_3:
                        self.difficulty = Difficulty.HARD
                
                elif self.state == GameState.SETTINGS:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                        self.state = GameState.MENU
                    elif event.key == pygame.K_s:
                        self.sound_enabled = not self.sound_enabled
                    elif event.key == pygame.K_m:
                        self.music_enabled = not self.music_enabled
                    elif event.key == pygame.K_p:
                        self.power_ups_enabled = not self.power_ups_enabled
                
                elif self.state == GameState.PLAYING:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                        self.state = GameState.PAUSED
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.change_direction(Direction.RIGHT)
                
                elif self.state == GameState.PAUSED:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                        self.state = GameState.PLAYING
                    elif event.key == pygame.K_q:
                        self.state = GameState.MENU
                
                elif self.state == GameState.GAME_OVER:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.reset_game()
                    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        self.state = GameState.MENU
        
        return True
    
    def update(self):
        if self.state != GameState.PLAYING:
            return
        
        # Calculate speed based on difficulty and power-ups
        base_speed = self.difficulty.value['speed']
        speed_boost = PowerUpType.SPEED_BOOST in self.active_power_ups
        current_speed = base_speed * 1.5 if speed_boost else base_speed
        
        # Increase speed as snake grows
        speed_increase = len(self.snake.body) // 10
        current_speed += speed_increase
        
        self.move_counter += 1
        if self.move_counter < FPS // current_speed:
            return
        
        self.move_counter = 0
        
        # Move snake
        self.snake.move()
        
        # Check collisions
        if self.snake.check_collision():
            self.play_sound('game_over')
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            self.state = GameState.GAME_OVER
            return
        
        # Check food collision
        if self.snake.body[0] == self.food_position:
            self.play_sound('eat')
            self.snake.grow(1)
            points = int(10 * self.difficulty.value['multiplier'] * self.score_multiplier)
            self.score += points
            self.food_position = self.spawn_food()
            
            # Chance to spawn power-up
            if self.power_ups_enabled:
                self.spawn_power_up()
        
        # Check power-up collision
        for power_up in self.power_ups[:]:
            if self.snake.body[0] == power_up.position:
                self.collect_power_up(power_up)
                self.power_ups.remove(power_up)
        
        # Update power-ups
        self.update_power_ups()
    
    def draw_grid(self):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, DARK_GRAY, (x, 0), (x, WINDOW_HEIGHT), 1)
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, DARK_GRAY, (0, y), (WINDOW_WIDTH, y), 1)
    
    def draw_snake(self):
        for i, segment in enumerate(self.snake.body):
            x = segment[0] * GRID_SIZE
            y = segment[1] * GRID_SIZE
            
            # Head is brighter, body fades
            if i == 0:
                color = CYAN if self.snake.invincible else GREEN
            else:
                fade = max(100, 255 - i * 3)
                color = (0, fade, 0) if not self.snake.invincible else (0, fade, fade)
            
            pygame.draw.rect(self.screen, color, (x + 1, y + 1, GRID_SIZE - 2, GRID_SIZE - 2))
            
            # Draw eyes on head
            if i == 0:
                eye_size = 3
                if self.snake.direction == Direction.RIGHT:
                    eye1_pos = (x + GRID_SIZE - 8, y + 5)
                    eye2_pos = (x + GRID_SIZE - 8, y + GRID_SIZE - 8)
                elif self.snake.direction == Direction.LEFT:
                    eye1_pos = (x + 5, y + 5)
                    eye2_pos = (x + 5, y + GRID_SIZE - 8)
                elif self.snake.direction == Direction.UP:
                    eye1_pos = (x + 5, y + 5)
                    eye2_pos = (x + GRID_SIZE - 8, y + 5)
                else:  # DOWN
                    eye1_pos = (x + 5, y + GRID_SIZE - 8)
                    eye2_pos = (x + GRID_SIZE - 8, y + GRID_SIZE - 8)
                
                pygame.draw.circle(self.screen, BLACK, eye1_pos, eye_size)
                pygame.draw.circle(self.screen, BLACK, eye2_pos, eye_size)
    
    def draw_food(self):
        x = self.food_position[0] * GRID_SIZE
        y = self.food_position[1] * GRID_SIZE
        pygame.draw.circle(self.screen, RED, 
                         (x + GRID_SIZE // 2, y + GRID_SIZE // 2), 
                         GRID_SIZE // 2 - 2)
    
    def draw_power_ups(self):
        for power_up in self.power_ups:
            x = power_up.position[0] * GRID_SIZE
            y = power_up.position[1] * GRID_SIZE
            color = power_up.type.value['color']
            
            # Draw as a star/diamond
            center_x = x + GRID_SIZE // 2
            center_y = y + GRID_SIZE // 2
            size = GRID_SIZE // 2 - 2
            
            points = [
                (center_x, center_y - size),
                (center_x + size, center_y),
                (center_x, center_y + size),
                (center_x - size, center_y)
            ]
            pygame.draw.polygon(self.screen, color, points)
    
    def draw_hud(self):
        # Score
        score_text = self.font_small.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # High Score
        high_score_text = self.font_tiny.render(f"High: {self.high_score}", True, YELLOW)
        self.screen.blit(high_score_text, (10, 45))
        
        # Difficulty
        diff_text = self.font_tiny.render(f"Difficulty: {self.difficulty.value['name']}", True, LIGHT_GRAY)
        self.screen.blit(diff_text, (WINDOW_WIDTH - 200, 10))
        
        # Active power-ups
        y_offset = 80
        for power_type in self.active_power_ups:
            time_left = (self.active_power_ups[power_type] + power_type.value['duration'] - pygame.time.get_ticks()) // 1000
            text = self.font_tiny.render(f"{power_type.value['name']}: {time_left}s", True, power_type.value['color'])
            self.screen.blit(text, (10, y_offset))
            y_offset += 25
    
    def draw_menu(self):
        # Title
        title = self.font_large.render("PYSNAKE v2.0", True, GREEN)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.font_small.render("Modern Edition", True, LIGHT_GRAY)
        subtitle_rect = subtitle.get_rect(center=(WINDOW_WIDTH // 2, 160))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Instructions
        instructions = [
            "Press SPACE or ENTER to Start",
            "",
            "Select Difficulty:",
            "1 - Easy    2 - Medium    3 - Hard",
            "",
            "S - Settings",
            "Q - Quit"
        ]
        
        y = 250
        for line in instructions:
            text = self.font_tiny.render(line, True, WHITE)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 35
        
        # Current difficulty
        diff_text = self.font_small.render(f"Current: {self.difficulty.value['name']}", True, YELLOW)
        diff_rect = diff_text.get_rect(center=(WINDOW_WIDTH // 2, 500))
        self.screen.blit(diff_text, diff_rect)
        
        # High Score
        hs_text = self.font_medium.render(f"High Score: {self.high_score}", True, CYAN)
        hs_rect = hs_text.get_rect(center=(WINDOW_WIDTH // 2, 560))
        self.screen.blit(hs_text, hs_rect)
    
    def draw_settings(self):
        title = self.font_large.render("SETTINGS", True, YELLOW)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 80))
        self.screen.blit(title, title_rect)
        
        settings = [
            f"S - Sound Effects: {'ON' if self.sound_enabled else 'OFF'}",
            f"M - Music: {'ON' if self.music_enabled else 'OFF'}",
            f"P - Power-ups: {'ON' if self.power_ups_enabled else 'OFF'}",
            "",
            "ESC or BACKSPACE - Back to Menu"
        ]
        
        y = 200
        for line in settings:
            color = GREEN if any(word in line for word in ['ON']) else (RED if 'OFF' in line else WHITE)
            text = self.font_small.render(line, True, color)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 60
    
    def draw_pause(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render("PAUSED", True, YELLOW)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 200))
        self.screen.blit(title, title_rect)
        
        instructions = [
            "P or ESC - Resume",
            "Q - Quit to Menu"
        ]
        
        y = 300
        for line in instructions:
            text = self.font_medium.render(line, True, WHITE)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 60
    
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render("GAME OVER", True, RED)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        score_text = self.font_medium.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, 250))
        self.screen.blit(score_text, score_rect)
        
        if self.score == self.high_score and self.score > 0:
            new_hs = self.font_small.render("NEW HIGH SCORE!", True, YELLOW)
            new_hs_rect = new_hs.get_rect(center=(WINDOW_WIDTH // 2, 310))
            self.screen.blit(new_hs, new_hs_rect)
        else:
            hs_text = self.font_small.render(f"High Score: {self.high_score}", True, CYAN)
            hs_rect = hs_text.get_rect(center=(WINDOW_WIDTH // 2, 310))
            self.screen.blit(hs_text, hs_rect)
        
        instructions = [
            "SPACE or ENTER - Play Again",
            "Q or ESC - Menu"
        ]
        
        y = 400
        for line in instructions:
            text = self.font_small.render(line, True, WHITE)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 50
    
    def draw(self):
        self.screen.fill(BLACK)
        
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.SETTINGS:
            self.draw_settings()
        elif self.state == GameState.PLAYING:
            self.draw_grid()
            self.draw_food()
            self.draw_power_ups()
            self.draw_snake()
            self.draw_hud()
        elif self.state == GameState.PAUSED:
            self.draw_grid()
            self.draw_food()
            self.draw_power_ups()
            self.draw_snake()
            self.draw_hud()
            self.draw_pause()
        elif self.state == GameState.GAME_OVER:
            self.draw_grid()
            self.draw_food()
            self.draw_snake()
            self.draw_game_over()
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
