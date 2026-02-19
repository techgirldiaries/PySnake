"""
PySnake v2.0 - Power-up Module
Contains power-up management and effects
"""

import random
import pygame
from dataclasses import dataclass
from typing import Tuple, List, Optional
from config import PowerUpType, GRID_WIDTH, GRID_HEIGHT, POWER_UP_LIFETIME
from styles import POWERUP_SPEED, POWERUP_INVINCIBLE, POWERUP_MULTIPLIER


@dataclass
class PowerUp:
    """Represents a power-up on the game board"""
    type: PowerUpType
    position: Tuple[int, int]
    spawn_time: int
    
    def is_expired(self, current_time: int) -> bool:
        """Check if power-up has expired"""
        return current_time - self.spawn_time > POWER_UP_LIFETIME
    
    def get_color(self) -> tuple:
        """Get the display colour for this power-up"""
        color_map = {
            PowerUpType.SPEED_BOOST: POWERUP_SPEED,
            PowerUpType.INVINCIBILITY: POWERUP_INVINCIBLE,
            PowerUpType.SCORE_MULTIPLIER: POWERUP_MULTIPLIER
        }
        return color_map.get(self.type, (255, 255, 255))


class PowerUpManager:
    """Manages power-up spawning, collection, and active effects"""
    
    def __init__(self):
        self.power_ups: List[PowerUp] = []
        self.active_effects = {}  # {(snake_id, PowerUpType): start_time}
    
    def spawn_power_up(self, occupied_positions: List[Tuple[int, int]], 
                       max_power_ups: int, spawn_chance: float) -> bool:
        """
        Try to spawn a new power-up
        
        Args:
            occupied_positions: List of positions that are occupied (snakes, food)
            max_power_ups: Maximum number of power-ups allowed on screen
            spawn_chance: Probability of spawning (0.0 to 1.0)
        
        Returns:
            True if power-up was spawned
        """
        if len(self.power_ups) >= max_power_ups:
            return False
        
        if random.random() > spawn_chance:
            return False
        
        # Find valid position
        position = self._find_valid_position(occupied_positions)
        if position is None:
            return False
        
        # Choose random power-up type
        power_type = random.choice(list(PowerUpType))
        
        # Create power-up
        power_up = PowerUp(
            type=power_type,
            position=position,
            spawn_time=pygame.time.get_ticks()
        )
        
        self.power_ups.append(power_up)
        return True
    
    def _find_valid_position(self, occupied_positions: List[Tuple[int, int]], 
                            max_attempts: int = 50) -> Optional[Tuple[int, int]]:
        """
        Find a valid position that's not occupied
        
        Args:
            occupied_positions: List of positions to avoid
            max_attempts: Maximum number of random attempts
        
        Returns:
            Valid position tuple or None if not found
        """
        for _ in range(max_attempts):
            pos = (random.randint(0, GRID_WIDTH - 1), 
                  random.randint(0, GRID_HEIGHT - 1))
            
            if pos not in occupied_positions:
                return pos
        
        return None
    
    def update(self, current_time: int):
        """
        Update power-ups (remove expired ones)
        
        Args:
            current_time: Current game time in milliseconds
        """
        # Remove expired power-ups from world
        self.power_ups = [pu for pu in self.power_ups 
                        if not pu.is_expired(current_time)]
        
        # Remove expired active effects
        expired_effects = []
        for (snake_id, pu_type), start_time in self.active_effects.items():
            duration = pu_type.value['duration']
            if current_time - start_time > duration:
                expired_effects.append((snake_id, pu_type))
        
        for key in expired_effects:
            del self.active_effects[key]
    
    def check_collection(self, snake_id: int, position: Tuple[int, int]) -> Optional[PowerUp]:
        """
        Check if a snake collected a power-up at given position
        
        Args:
            snake_id: ID of the snake
            position: Position to check
        
        Returns:
            PowerUp if collected, None otherwise
        """
        for power_up in self.power_ups:
            if power_up.position == position:
                self.power_ups.remove(power_up)
                self._activate_power_up(snake_id, power_up)
                return power_up
        
        return None
    
    def _activate_power_up(self, snake_id: int, power_up: PowerUp):
        """
        Activate a power-up effect for a snake
        
        Args:
            snake_id: ID of the snake that collected it
            power_up: The PowerUp that was collected
        """
        key = (snake_id, power_up.type)
        self.active_effects[key] = pygame.time.get_ticks()
    
    def is_effect_active(self, snake_id: int, power_type: PowerUpType) -> bool:
        """
        Check if a power-up effect is active for a snake
        
        Args:
            snake_id: ID of the snake
            power_type: Type of power-up to check
        
        Returns:
            True if effect is active
        """
        return (snake_id, power_type) in self.active_effects
    
    def get_active_effects(self, snake_id: int) -> List[Tuple[PowerUpType, int]]:
        """
        Get all active effects for a snake with time remaining
        
        Args:
            snake_id: ID of the snake
        
        Returns:
            List of (PowerUpType, seconds_remaining) tuples
        """
        current_time = pygame.time.get_ticks()
        active = []
        
        for (sid, pu_type), start_time in self.active_effects.items():
            if sid == snake_id:
                duration = pu_type.value['duration']
                time_left = (start_time + duration - current_time) // 1000
                if time_left > 0:
                    active.append((pu_type, time_left))
        
        return active
    
    def get_score_multiplier(self, snake_id: int) -> float:
        """
        Get score multiplier for a snake
        
        Args:
            snake_id: ID of the snake
        
        Returns:
            Score multiplier (1.0 or higher)
        """
        if self.is_effect_active(snake_id, PowerUpType.SCORE_MULTIPLIER):
            return 2.0
        return 1.0
    
    def has_speed_boost(self, snake_id: int) -> bool:
        """Check if snake has speed boost active"""
        return self.is_effect_active(snake_id, PowerUpType.SPEED_BOOST)
    
    def has_invincibility(self, snake_id: int) -> bool:
        """Check if snake has invincibility active"""
        return self.is_effect_active(snake_id, PowerUpType.INVINCIBILITY)
    
    def clear(self):
        """Clear all power-ups and effects"""
        self.power_ups.clear()
        self.active_effects.clear()
    
    def get_all_positions(self) -> List[Tuple[int, int]]:
        """Get list of all power-up positions"""
        return [pu.position for pu in self.power_ups]
