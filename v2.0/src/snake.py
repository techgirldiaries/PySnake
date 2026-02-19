"""
PySnake v2.0 - Snake Module
Contains the Snake class for player and AI snakes
"""

from typing import Tuple
from config import Direction, GRID_WIDTH, GRID_HEIGHT, PlayerType, INITIAL_SNAKE_LENGTH


class Snake:
    """Represents a snake (player or AI)"""
    
    def __init__(self, start_x: int, start_y: int, player_type: PlayerType, colour_primary: tuple):
        """
        Initialise a snake
        
        Args:
            start_x: Starting X position (grid coordinates)
            start_y: Starting Y position (grid coordinates)
            player_type: PlayerType.HUMAN or PlayerType.AI
            colour_primary: RGB colour tuple for the snake
        """
        self.player_type = player_type
        self.colour_primary = colour_primary
        self.start_pos = (start_x, start_y)
        self.reset()
    
    def reset(self):
        """Reset snake to initial state"""
        start_x, start_y = self.start_pos
        
        # Create initial body segments
        self.body = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y)
        ]
        
        self.direction = Direction.RIGHT
        self.grow_pending = 0
        self.invincible = False
        self.alive = True
        self.score = 0
    
    def move(self):
        """Move the snake one step in current direction"""
        if not self.alive:
            return
        
        head_x, head_y = self.body[0]
        
        # Calculate new head position
        if self.direction == Direction.UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == Direction.DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == Direction.LEFT:
            new_head = (head_x - 1, head_y)
        elif self.direction == Direction.RIGHT:
            new_head = (head_x + 1, head_y)
        else:
            new_head = (head_x, head_y)
        
        # Insert new head
        self.body.insert(0, new_head)
        
        # Remove tail unless growing
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    
    def change_direction(self, new_direction: Direction):
        """
        Change snake direction (prevents reversing into itself)
        
        Args:
            new_direction: New direction to move in
        """
        if not self.alive:
            return
        
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
        """
        Schedule snake to grow by amount segments
        
        Args:
            amount: Number of segments to grow
        """
        self.grow_pending += amount
    
    def check_wall_collision(self) -> bool:
        """Check if snake head collides with walls"""
        if not self.alive:
            return False
        
        head = self.body[0]
        
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        
        return False
    
    def check_self_collision(self) -> bool:
        """Check if snake head collides with its own body"""
        if not self.alive or self.invincible:
            return False
        
        head = self.body[0]
        
        # Check if head is in body (excluding head itself)
        if head in self.body[1:]:
            return True
        
        return False
    
    def check_collision_with_snake(self, other_snake: 'Snake') -> bool:
        """
        Check if this snake collides with another snake
        
        Args:
            other_snake: Another Snake instance to check collision with
        
        Returns:
            True if collision detected
        """
        if not self.alive or not other_snake.alive or self.invincible:
            return False
        
        head = self.body[0]
        
        # Check collision with other snake's body
        if head in other_snake.body:
            return True
        
        return False
    
    def kill(self):
        """Mark snake as dead"""
        self.alive = False
    
    def get_head_position(self) -> Tuple[int, int]:
        """Get the current head position"""
        return self.body[0] if self.body else (0, 0)
    
    def get_length(self) -> int:
        """Get current snake length"""
        return len(self.body)
    
    def contains_position(self, pos: Tuple[int, int]) -> bool:
        """
        Check if a position is occupied by this snake
        
        Args:
            pos: (x, y) position to check
        
        Returns:
            True if position is in snake body
        """
        return pos in self.body
    
    def add_score(self, points: int):
        """
        Add points to snake's score
        
        Args:
            points: Points to add
        """
        self.score += points
    
    def get_possible_moves(self) -> list:
        """
        Get list of possible directions snake can move (for AI)
        
        Returns:
            List of valid Direction enums
        """
        opposite = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        
        # Can't reverse
        forbidden = opposite.get(self.direction)
        
        return [d for d in Direction if d != forbidden]
    
    def get_direction_to_position(self, target: Tuple[int, int]) -> Direction:
        """
        Get the general direction from head to target position
        
        Args:
            target: (x, y) target position
        
        Returns:
            Direction that moves closer to target
        """
        head_x, head_y = self.body[0]
        target_x, target_y = target
        
        dx = target_x - head_x
        dy = target_y - head_y
        
        # Prioritize larger difference
        if abs(dx) > abs(dy):
            return Direction.RIGHT if dx > 0 else Direction.LEFT
        else:
            return Direction.DOWN if dy > 0 else Direction.UP
