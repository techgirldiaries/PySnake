"""
PySnake v2.0 - Main Game Module
Contains the main Game class with AI vs Player support
"""

import pygame
import random
import json
import os
from typing import Optional

from config import *
from styles import *
from snake import Snake
from power_up import PowerUpManager
from ai_player import AIPlayer


class Game:
    """Main game class managing all game logic and rendering"""
    
    def __init__(self):
        """Initialise game"""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("PySnake v2.0 - Modern Edition")
        self.clock = pygame.time.Clock()
        
        # Load fonts
        self.font_xlarge = pygame.font.Font(None, FONT_XLARGE)
        self.font_large = pygame.font.Font(None, FONT_LARGE)
        self.font_medium = pygame.font.Font(None, FONT_MEDIUM)
        self.font_small = pygame.font.Font(None, FONT_SMALL)
        self.font_tiny = pygame.font.Font(None, FONT_TINY)
        self.font_micro = pygame.font.Font(None, FONT_MICRO)
        
        # Game state
        self.state = GameState.MENU
        self.mode = GameMode.SINGLE_PLAYER
        self.difficulty = Difficulty.MEDIUM
        
        # Snakes
        self.player_snake = None
        self.ai_snake = None
        self.ai_controller = None
        
        # Game objects
        self.food_position = None
        self.powerup_manager = PowerUpManager()
        self.move_counter = 0
        
        # Scores
        self.high_scores = self.load_high_scores()
        
        # Settings
        self.sound_enabled = True
        self.music_enabled = True
        self.power_ups_enabled = True
        
        # Sound effects
        self.sounds = self.load_sounds()
        
        # Animation
        self.menu_pulse = 0
    
    def load_sounds(self) -> dict:
        """Load sound effects if they exist"""
        sounds = {}
        for name, path in SOUND_FILES.items():
            try:
                if os.path.exists(path):
                    sounds[name] = pygame.mixer.Sound(path)
            except:
                pass
        return sounds
    
    def play_sound(self, sound_name: str):
        """Play sound effect if enabled"""
        if self.sound_enabled and sound_name in self.sounds:
            self.sounds[sound_name].play()
    
    def load_high_scores(self) -> dict:
        """Load high scores from file"""
        try:
            # Ensure db directory exists
            os.makedirs('../db', exist_ok=True)
            if os.path.exists('../db/highscores.json'):
                with open('../db/highscores.json', 'r') as f:
                    return json.load(f)
        except:
            pass
        return {
            'single_player': 0,
            'ai_opponent_player': 0,
            'ai_opponent_ai': 0
        }
    
    def save_high_scores(self):
        """Save high scores to file"""
        try:
            # Ensure db directory exists
            os.makedirs('../db', exist_ok=True)
            with open('../db/highscores.json', 'w') as f:
                json.dump(self.high_scores, f, indent=2)
        except:
            pass
    
    def initialize_game(self):
        """Initialise/reset game for new round"""
        # Create player snake
        self.player_snake = Snake(
            start_x=GRID_WIDTH // 3,
            start_y=GRID_HEIGHT // 2,
            player_type=PlayerType.HUMAN,
            colour_primary=PLAYER_PRIMARY
        )
        
        # Create AI snake if in AI mode
        if self.mode == GameMode.AI_OPPONENT:
            self.ai_snake = Snake(
                start_x=2 * GRID_WIDTH // 3,
                start_y=GRID_HEIGHT // 2,
                player_type=PlayerType.AI,
                colour_primary=AI_PRIMARY
            )
            
            # Create AI controller
            skill = self.difficulty.value['ai_skill']
            self.ai_controller = AIPlayer(self.ai_snake, skill_level=skill)
        else:
            self.ai_snake = None
            self.ai_controller = None
        
        # Spawn food
        self.food_position = self.spawn_food()
        
        # Reset power-ups
        self.powerup_manager.clear()
        self.move_counter = 0
        
        # Change state
        self.state = GameState.PLAYING
    
    def spawn_food(self) -> tuple:
        """Spawn food at random valid position"""
        max_attempts = 100
        for _ in range(max_attempts):
            pos = (random.randint(0, GRID_WIDTH - 1), 
                  random.randint(0, GRID_HEIGHT - 1))
            
            # Check if position is occupied
            if self.player_snake and self.player_snake.contains_position(pos):
                continue
            if self.ai_snake and self.ai_snake.contains_position(pos):
                continue
            if pos in self.powerup_manager.get_all_positions():
                continue
            
            return pos
        
        # Fallback
        return (GRID_WIDTH // 2, GRID_HEIGHT // 2)
    
    def get_occupied_positions(self) -> list:
        """Get all occupied positions"""
        positions = []
        
        if self.player_snake:
            positions.extend(self.player_snake.body)
        if self.ai_snake:
            positions.extend(self.ai_snake.body)
        
        positions.append(self.food_position)
        positions.extend(self.powerup_manager.get_all_positions())
        
        return positions
    
    def handle_input(self) -> bool:
        """
        Handle keyboard/mouse input
        
        Returns:
            False to quit game, True to continue
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.state == GameState.MENU:
                    return self.handle_menu_input(event.key)
                elif self.state == GameState.MODE_SELECT:
                    return self.handle_mode_select_input(event.key)
                elif self.state == GameState.SETTINGS:
                    return self.handle_settings_input(event.key)
                elif self.state == GameState.PLAYING:
                    return self.handle_playing_input(event.key)
                elif self.state == GameState.PAUSED:
                    return self.handle_paused_input(event.key)
                elif self.state == GameState.GAME_OVER:
                    return self.handle_game_over_input(event.key)
        
        return True
    
    def handle_menu_input(self, key: int) -> bool:
        """Handle menu input"""
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            self.state = GameState.MODE_SELECT
        elif key == pygame.K_s:
            self.state = GameState.SETTINGS
        elif key == pygame.K_q or key == pygame.K_ESCAPE:
            return False
        elif key == pygame.K_1:
            self.difficulty = Difficulty.EASY
        elif key == pygame.K_2:
            self.difficulty = Difficulty.MEDIUM
        elif key == pygame.K_3:
            self.difficulty = Difficulty.HARD
        elif key == pygame.K_t:
            theme_manager.cycle_theme()
        return True
    
    def handle_mode_select_input(self, key: int) -> bool:
        """Handle mode selection input"""
        if key == pygame.K_1:
            self.mode = GameMode.SINGLE_PLAYER
            self.initialize_game()
        elif key == pygame.K_2:
            self.mode = GameMode.AI_OPPONENT
            self.initialize_game()
        elif key == pygame.K_ESCAPE or key == pygame.K_BACKSPACE:
            self.state = GameState.MENU
        return True
    
    def handle_settings_input(self, key: int) -> bool:
        """Handle settings input"""
        if key == pygame.K_ESCAPE or key == pygame.K_BACKSPACE:
            self.state = GameState.MENU
        elif key == pygame.K_s:
            self.sound_enabled = not self.sound_enabled
        elif key == pygame.K_m:
            self.music_enabled = not self.music_enabled
        elif key == pygame.K_p:
            self.power_ups_enabled = not self.power_ups_enabled
        return True
    
    def handle_playing_input(self, key: int) -> bool:
        """Handle playing state input"""
        if key == pygame.K_ESCAPE or key == pygame.K_p:
            self.state = GameState.PAUSED
        elif key in (pygame.K_UP, pygame.K_w):
            if self.player_snake:
                self.player_snake.change_direction(Direction.UP)
        elif key in (pygame.K_DOWN, pygame.K_s):
            if self.player_snake:
                self.player_snake.change_direction(Direction.DOWN)
        elif key in (pygame.K_LEFT, pygame.K_a):
            if self.player_snake:
                self.player_snake.change_direction(Direction.LEFT)
        elif key in (pygame.K_RIGHT, pygame.K_d):
            if self.player_snake:
                self.player_snake.change_direction(Direction.RIGHT)
        return True
    
    def handle_paused_input(self, key: int) -> bool:
        """Handle paused state input"""
        if key == pygame.K_ESCAPE or key == pygame.K_p:
            self.state = GameState.PLAYING
        elif key == pygame.K_q:
            self.state = GameState.MENU
        return True
    
    def handle_game_over_input(self, key: int) -> bool:
        """Handle game over input"""
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            self.initialize_game()
        elif key == pygame.K_q or key == pygame.K_ESCAPE:
            self.state = GameState.MENU
        return True
    
    def update(self):
        """Update game logic"""
        if self.state != GameState.PLAYING:
            return
        
        # Calculate movement speed
        base_speed = self.difficulty.value['speed']
        
        # Player speed
        player_speed = base_speed
        if self.player_snake:
            if self.powerup_manager.has_speed_boost(0):
                player_speed *= 1.5
            player_speed += self.player_snake.get_length() // 10
        
        # AI speed (same as player for fairness)
        ai_speed = player_speed
        
        self.move_counter += 1
        should_move = self.move_counter >= FPS // player_speed
        
        if not should_move:
            return
        
        self.move_counter = 0
        
        # Update AI decision
        if self.ai_controller and self.ai_snake and self.ai_snake.alive and self.food_position:
            obstacles = []
            if self.player_snake:
                obstacles.extend(self.player_snake.body)
            
            self.ai_controller.update(
                food_position=self.food_position,
                power_ups=self.powerup_manager.get_all_positions(),
                obstacles=obstacles,
                opponent_snake=self.player_snake
            )
        
        # Move snakes
        if self.player_snake and self.player_snake.alive:
            self.player_snake.move()
        if self.ai_snake and self.ai_snake.alive:
            self.ai_snake.move()
        
        # Update power-up effects
        if self.player_snake:
            self.player_snake.invincible = self.powerup_manager.has_invincibility(0)
        if self.ai_snake:
            self.ai_snake.invincible = self.powerup_manager.has_invincibility(1)
        
        self.powerup_manager.update(pygame.time.get_ticks())
        
        # Check collisions
        self.check_collisions()
        
        # Check food collection
        self.check_food_collection()
        
        # Check power-up collection
        self.check_powerup_collection()
        
        # Spawn power-ups
        if self.power_ups_enabled:
            self.powerup_manager.spawn_power_up(
                occupied_positions=self.get_occupied_positions(),
                max_power_ups=POWER_UP_MAX_ON_SCREEN,
                spawn_chance=POWER_UP_SPAWN_CHANCE
            )
    
    def check_collisions(self):
        """Check all collision types"""
        player_dead = False
        ai_dead = False
        
        # Check player collisions
        if self.player_snake and self.player_snake.alive:
            # Wall collision
            if self.player_snake.check_wall_collision():
                player_dead = True
            # Self collision
            elif self.player_snake.check_self_collision():
                player_dead = True
            # Collision with AI
            elif self.ai_snake and self.player_snake.check_collision_with_snake(self.ai_snake):
                player_dead = True
        
        # Check AI collisions
        if self.ai_snake and self.ai_snake.alive:
            # Wall collision
            if self.ai_snake.check_wall_collision():
                ai_dead = True
            # Self collision
            elif self.ai_snake.check_self_collision():
                ai_dead = True
            # Collision with player
            elif self.player_snake and self.ai_snake.check_collision_with_snake(self.player_snake):
                ai_dead = True
        
        # Handle deaths
        if player_dead and self.player_snake:
            self.player_snake.kill()
            self.play_sound('game_over')
        
        if ai_dead and self.ai_snake:
            self.ai_snake.kill()
            self.play_sound('game_over')
        
        # Check game over conditions
        if self.mode == GameMode.SINGLE_PLAYER:
            if player_dead:
                self.end_game()
        elif self.mode == GameMode.AI_OPPONENT:
            # Game ends when both are dead or one wins
            if player_dead and ai_dead:
                self.end_game()
            elif player_dead or ai_dead:
                # One snake remaining - they won
                self.end_game()
    
    def check_food_collection(self):
        """Check if any snake collected food"""
        collected = False
        collector = None
        snake_id = 0
        
        if self.player_snake and self.player_snake.alive:
            if self.player_snake.get_head_position() == self.food_position:
                collected = True
                collector = self.player_snake
                snake_id = 0
        
        if not collected and self.ai_snake and self.ai_snake.alive:
            if self.ai_snake.get_head_position() == self.food_position:
                collected = True
                collector = self.ai_snake
                snake_id = 1
        
        if collected and collector:
            self.play_sound('eat')
            collector.grow(1)
            
            # Calculate points
            multiplier = self.difficulty.value['multiplier']
            score_mult = self.powerup_manager.get_score_multiplier(snake_id)
            points = int(10 * multiplier * score_mult)
            collector.add_score(points)
            
            # Spawn new food
            self.food_position = self.spawn_food()
    
    def check_powerup_collection(self):
        """Check if any snake collected power-up"""
        if self.player_snake and self.player_snake.alive:
            pu = self.powerup_manager.check_collection(0, self.player_snake.get_head_position())
            if pu:
                self.play_sound('power_up')
        
        if self.ai_snake and self.ai_snake.alive:
            pu = self.powerup_manager.check_collection(1, self.ai_snake.get_head_position())
            if pu:
                self.play_sound('power_up')
    
    def end_game(self):
        """End current game and show game over screen"""
        self.state = GameState.GAME_OVER
        
        # Update high scores
        if self.mode == GameMode.SINGLE_PLAYER:
            if self.player_snake and self.player_snake.score > self.high_scores['single_player']:
                self.high_scores['single_player'] = self.player_snake.score
                self.save_high_scores()
        elif self.mode == GameMode.AI_OPPONENT:
            if self.player_snake and self.player_snake.score > self.high_scores['ai_opponent_player']:
                self.high_scores['ai_opponent_player'] = self.player_snake.score
                self.save_high_scores()
            if self.ai_snake and self.ai_snake.score > self.high_scores['ai_opponent_ai']:
                self.high_scores['ai_opponent_ai'] = self.ai_snake.score
                self.save_high_scores()
    
    def draw(self):
        """Main draw method"""
        # Background
        self.screen.fill(DEEP_SPACE)
        
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.MODE_SELECT:
            self.draw_mode_select()
        elif self.state == GameState.SETTINGS:
            self.draw_settings()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.PAUSED:
            self.draw_game()
            self.draw_pause_overlay()
        elif self.state == GameState.GAME_OVER:
            self.draw_game()
            self.draw_game_over()
        
        pygame.display.flip()
    
    def draw_menu(self):
        """Draw main menu"""
        # Pulsing animation
        self.menu_pulse = (self.menu_pulse + 1) % 60
        pulse_factor = abs(self.menu_pulse - 30) / 30.0
        
        # Title with shadow
        title = self.font_xlarge.render("PYSNAKE", True, ELECTRIC_CYAN)
        title_shadow = self.font_xlarge.render("PYSNAKE", True, NEON_PINK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2 + 3, 103))
        title_rect_main = title.get_rect(center=(WINDOW_WIDTH // 2, 100))
        self.screen.blit(title_shadow, title_rect)
        self.screen.blit(title, title_rect_main)
        
        # Version
        version = self.font_small.render("v2.0 Modern Edition", True, TEXT_SECONDARY)
        version_rect = version.get_rect(center=(WINDOW_WIDTH // 2, 170))
        self.screen.blit(version, version_rect)
        
        # Instructions
        instructions = [
            ("PRESS SPACE TO START", TEXT_HIGHLIGHT, True),
            ("", TEXT_PRIMARY, False),
            ("Difficulty:", TEXT_PRIMARY, False),
            ("1 - Easy  |  2 - Medium  |  3 - Hard", TEXT_SECONDARY, False),
            ("", TEXT_PRIMARY, False),
            (f"Current: {self.difficulty.value['name']}", LIME_GREEN, False),
            ("", TEXT_PRIMARY, False),
            ("S - Settings  |  Q - Quit", TEXT_SECONDARY, False)
        ]
        
        y = 260
        for text, colour, pulse in instructions:
            if pulse:
                alpha = int(200 + 55 * pulse_factor)
                surf = self.font_small.render(text, True, colour)
                surf.set_alpha(alpha)
            else:
                surf = self.font_tiny.render(text, True, colour)
            
            rect = surf.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(surf, rect)
            y += 40 if text else 20
        
        # Current Theme
        theme_text = self.font_tiny.render(f"Theme: {theme_manager.get_theme_name()}", True, TEXT_SECONDARY)
        theme_rect = theme_text.get_rect(center=(WINDOW_WIDTH // 2, 500))
        self.screen.blit(theme_text, theme_rect)
        
        theme_hint = self.font_tiny.render("(Press T to change)", True, TEXT_SECONDARY)
        theme_hint_rect = theme_hint.get_rect(center=(WINDOW_WIDTH // 2, 520))
        self.screen.blit(theme_hint, theme_hint_rect)
        
        # High Score
        hs = self.high_scores.get('single_player', 0)
        hs_text = self.font_medium.render(f"High Score: {hs}", True, POWERUP_SPEED)
        hs_rect = hs_text.get_rect(center=(WINDOW_WIDTH // 2, 560))
        self.screen.blit(hs_text, hs_rect)
    
    def draw_mode_select(self):
        """Draw game mode selection"""
        title = self.font_large.render("SELECT MODE", True, ELECTRIC_CYAN)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        options = [
            "1 - SINGLE PLAYER",
            "Hunt food and grow your snake",
            "",
            "2 - VS AI OPPONENT",
            "Compete against computer snake!",
            "",
            "ESC - Back to Menu"
        ]
        
        y = 220
        for i, text in enumerate(options):
            if text.startswith(('1', '2')):
                color = LIME_GREEN
                font = self.font_medium
            elif text.startswith('ESC'):
                color = TEXT_SECONDARY
                font = self.font_tiny
            elif not text:
                y += 30
                continue
            else:
                color = TEXT_SECONDARY
                font = self.font_tiny
            
            surf = font.render(text, True, color)
            rect = surf.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(surf, rect)
            y += 50 if text.startswith(('1', '2')) else 30
    
    def draw_settings(self):
        """Draw settings menu"""
        title = self.font_large.render("SETTINGS", True, POWERUP_SPEED)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 80))
        self.screen.blit(title, title_rect)
        
        settings = [
            (f"S - Sound Effects: {'ON' if self.sound_enabled else 'OFF'}", 
             SUCCESS_GREEN if self.sound_enabled else ERROR_RED),
            (f"M - Music: {'ON' if self.music_enabled else 'OFF'}", 
             SUCCESS_GREEN if self.music_enabled else ERROR_RED),
            (f"P - Power-ups: {'ON' if self.power_ups_enabled else 'OFF'}", 
             SUCCESS_GREEN if self.power_ups_enabled else ERROR_RED),
            ("", TEXT_PRIMARY),
            ("ESC - Back to Menu", TEXT_SECONDARY)
        ]
        
        y = 200
        for text, colour in settings:
            if text:
                surf = self.font_small.render(text, True, colour)
                rect = surf.get_rect(center=(WINDOW_WIDTH // 2, y))
                self.screen.blit(surf, rect)
            y += 60
    
    def draw_game(self):
        """Draw game state"""
        # Grid
        self.draw_grid()
        
        # Food
        self.draw_food()
        
        # Power-ups
        self.draw_power_ups()
        
        # Snakes
        if self.player_snake:
            self.draw_snake(self.player_snake, PLAYER_PRIMARY)
        if self.ai_snake:
            self.draw_snake(self.ai_snake, AI_PRIMARY)
        
        # HUD
        self.draw_hud()
    
    def draw_grid(self):
        """Draw grid lines"""
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_LINE, (x, 0), (x, WINDOW_HEIGHT), 1)
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_LINE, (0, y), (WINDOW_WIDTH, y), 1)
    
    def draw_food(self):
        """Draw food"""
        if self.food_position:
            x = self.food_position[0] * GRID_SIZE
            y = self.food_position[1] * GRID_SIZE
            center = (x + GRID_SIZE // 2, y + GRID_SIZE // 2)
            pygame.draw.circle(self.screen, FOOD_RED, center, GRID_SIZE // 2 - 2)
            pygame.draw.circle(self.screen, FOOD_GLOW, center, GRID_SIZE // 3)
    
    def draw_power_ups(self):
        """Draw power-ups"""
        for power_up in self.powerup_manager.power_ups:
            x = power_up.position[0] * GRID_SIZE
            y = power_up.position[1] * GRID_SIZE
            colour = power_up.get_color()
            
            # Diamond shape
            center_x = x + GRID_SIZE // 2
            center_y = y + GRID_SIZE // 2
            size = GRID_SIZE // 2 - 2
            
            points = [
                (center_x, center_y - size),
                (center_x + size, center_y),
                (center_x, center_y + size),
                (center_x - size, center_y)
            ]
            pygame.draw.polygon(self.screen, colour, points)
    
    def draw_snake(self, snake: Snake, base_colour: tuple):
        """Draw a snake"""
        for i, segment in enumerate(snake.body):
            x = segment[0] * GRID_SIZE
            y = segment[1] * GRID_SIZE
            
            # Get segment colour with fade
            colour = get_snake_segment_color(base_colour, i, len(snake.body), snake.invincible)
            
            # Draw segment
            pygame.draw.rect(self.screen, colour, (x + 1, y + 1, GRID_SIZE - 2, GRID_SIZE - 2), border_radius=3)
            
            # Draw eyes on head
            if i == 0:
                eye_colour = BLACK if not snake.invincible else ELECTRIC_CYAN
                self.draw_snake_eyes(snake, x, y, eye_colour)
    
    def draw_snake_eyes(self, snake: Snake, x: int, y: int, colour: tuple):
        """Draw snake eyes"""
        eye_size = 3
        if snake.direction == Direction.RIGHT:
            eye1_pos = (x + GRID_SIZE - 8, y + 5)
            eye2_pos = (x + GRID_SIZE - 8, y + GRID_SIZE - 8)
        elif snake.direction == Direction.LEFT:
            eye1_pos = (x + 5, y + 5)
            eye2_pos = (x + 5, y + GRID_SIZE - 8)
        elif snake.direction == Direction.UP:
            eye1_pos = (x + 5, y + 5)
            eye2_pos = (x + GRID_SIZE - 8, y + 5)
        else:  # DOWN
            eye1_pos = (x + 5, y + GRID_SIZE - 8)
            eye2_pos = (x + GRID_SIZE - 8, y + GRID_SIZE - 8)
        
        pygame.draw.circle(self.screen, colour, eye1_pos, eye_size)
        pygame.draw.circle(self.screen, colour, eye2_pos, eye_size)
    
    def draw_hud(self):
        """Draw heads-up display"""
        # Player score
        if self.player_snake:
            player_text = self.font_small.render(f"Player: {self.player_snake.score}", True, PLAYER_PRIMARY)
            self.screen.blit(player_text, (10, 10))
            
            # Player power-ups
            effects = self.powerup_manager.get_active_effects(0)
            y = 45
            for effect_type, time_left in effects:
                text = self.font_micro.render(f"{effect_type.value['name']}: {time_left}s", 
                                             True, POWERUP_INVINCIBLE)
                self.screen.blit(text, (10, y))
                y += 20
        
        # AI score
        if self.ai_snake:
            ai_text = self.font_small.render(f"AI: {self.ai_snake.score}", True, AI_PRIMARY)
            ai_rect = ai_text.get_rect(topright=(WINDOW_WIDTH - 10, 10))
            self.screen.blit(ai_text, ai_rect)
            
            # AI power-ups
            effects = self.powerup_manager.get_active_effects(1)
            y = 45
            for effect_type, time_left in effects:
                text = self.font_micro.render(f"{effect_type.value['name']}: {time_left}s", 
                                             True, POWERUP_MULTIPLIER)
                text_rect = text.get_rect(topright=(WINDOW_WIDTH - 10, y))
                self.screen.blit(text, text_rect)
                y += 20
        
        # Difficulty
        diff_text = self.font_tiny.render(f"{self.difficulty.value['name']}", True, TEXT_SECONDARY)
        diff_rect = diff_text.get_rect(center=(WINDOW_WIDTH // 2, 15))
        self.screen.blit(diff_text, diff_rect)
    
    def draw_pause_overlay(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(ALPHA_MEDIUM)
        overlay.fill(OVERLAY_DARK)
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render("PAUSED", True, POWERUP_SPEED)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 200))
        self.screen.blit(title, title_rect)
        
        instructions = [
            "P or ESC - Resume",
            "Q - Quit to Menu"
        ]
        
        y = 300
        for text in instructions:
            surf = self.font_medium.render(text, True, TEXT_PRIMARY)
            rect = surf.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(surf, rect)
            y += 60
    
    def draw_game_over(self):
        """Draw game over screen"""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(ALPHA_HEAVY)
        overlay.fill(OVERLAY_DARK)
        self.screen.blit(overlay, (0, 0))
        
        # Determine winner
        if self.mode == GameMode.AI_OPPONENT and self.ai_snake and self.player_snake:
            if self.player_snake.alive and not self.ai_snake.alive:
                title_text = "YOU WIN!"
                title_colour = SUCCESS_GREEN
            elif self.ai_snake.alive and not self.player_snake.alive:
                title_text = "AI WINS!"
                title_colour = ERROR_RED
            else:
                title_text = "DRAW!"
                title_colour = WARNING_AMBER
        else:
            title_text = "GAME OVER"
            title_colour = ERROR_RED
        
        title = self.font_large.render(title_text, True, title_colour)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        # Scores
        y = 250
        if self.player_snake:
            score_text = self.font_medium.render(f"Your Score: {self.player_snake.score}", 
                                                 True, PLAYER_PRIMARY)
            score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(score_text, score_rect)
            y += 50
        
        if self.ai_snake:
            ai_score_text = self.font_medium.render(f"AI Score: {self.ai_snake.score}", 
                                                    True, AI_PRIMARY)
            ai_score_rect = ai_score_text.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(ai_score_text, ai_score_rect)
            y += 50
        
        # High score
        key = 'single_player' if self.mode == GameMode.SINGLE_PLAYER else 'ai_opponent_player'
        hs = self.high_scores.get(key, 0)
        hs_text = self.font_small.render(f"High Score: {hs}", True, POWERUP_SPEED)
        hs_rect = hs_text.get_rect(center=(WINDOW_WIDTH // 2, y + 20))
        self.screen.blit(hs_text, hs_rect)
        
        # Instructions
        instructions = [
            "SPACE - Play Again",
            "Q or ESC - Menu"
        ]
        
        y = 450
        for text in instructions:
            surf = self.font_small.render(text, True, TEXT_SECONDARY)
            rect = surf.get_rect(center=(WINDOW_WIDTH // 2, y))
            self.screen.blit(surf, rect)
            y += 40
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
