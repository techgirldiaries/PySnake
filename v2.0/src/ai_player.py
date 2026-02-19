"""
PySnake v2.0 - AI Player Module
Contains AI logic for computer-controlled snake
"""

import random
from typing import Tuple, List, Optional, Set
from collections import deque
from config import Direction, GRID_WIDTH, GRID_HEIGHT, AI_RANDOM_MOVE_CHANCE
from snake import Snake


class AIPlayer:
    """AI controller for snake using pathfinding and survival strategies"""
    
    def __init__(self, snake: Snake, skill_level: float = 0.6):
        """
        Initialize AI player
        
        Args:
            snake: Snake instance to control
            skill_level: AI skill from 0.0 to 1.0 (affects decision quality)
        """
        self.snake = snake
        self.skill_level = max(0.0, min(1.0, skill_level))
        self.target_position = None
        self.path = []
        self.frames_since_path_update = 0
        self.path_update_frequency = max(1, int(10 * (1 - skill_level)))  # Higher skill = more updates
    
    def update(self, food_position: Tuple[int, int], 
               power_ups: List[Tuple[int, int]],
               obstacles: List[Tuple[int, int]],
               opponent_snake: Optional[Snake] = None):
        """
        Update AI decision making
        
        Args:
            food_position: Position of the food
            power_ups: List of power-up positions
            obstacles: List of obstacle positions (walls, snake bodies)
            opponent_snake: Optional opponent snake to avoid
        """
        if not self.snake.alive:
            return
        
        # Occasionally make random moves for unpredictability
        if random.random() < AI_RANDOM_MOVE_CHANCE * (1 - self.skill_level):
            self._make_safe_random_move(obstacles, opponent_snake)
            return
        
        # Update path periodically
        self.frames_since_path_update += 1
        if self.frames_since_path_update >= self.path_update_frequency:
            self.frames_since_path_update = 0
            self._update_path(food_position, power_ups, obstacles, opponent_snake)
        
        # Follow path if available
        if self.path:
            next_pos = self.path[0]
            direction = self._get_direction_to_adjacent(next_pos)
            if direction:
                self.snake.change_direction(direction)
                self.path.pop(0)
        else:
            # No path, make best guess move
            self._make_best_guess_move(food_position, obstacles, opponent_snake)
    
    def _update_path(self, food_position: Tuple[int, int],
                     power_ups: List[Tuple[int, int]],
                     obstacles: List[Tuple[int, int]],
                     opponent_snake: Optional[Snake]):
        """Update pathfinding to target"""
        head = self.snake.get_head_position()
        
        # Decide target based on priorities
        target = self._choose_target(food_position, power_ups, opponent_snake)
        
        if target:
            # Use BFS to find path
            self.path = self._find_path_bfs(head, target, obstacles, opponent_snake)
    
    def _choose_target(self, food_position: Tuple[int, int],
                      power_ups: List[Tuple[int, int]],
                      opponent_snake: Optional[Snake]) -> Optional[Tuple[int, int]]:
        """
        Choose best target to pursue
        
        Returns:
            Target position or None
        """
        head = self.snake.get_head_position()
        
        # Calculate distances
        food_dist = self._manhattan_distance(head, food_position)
        
        # Consider power-ups if close enough
        closest_powerup = None
        closest_powerup_dist = float('inf')
        
        for pu_pos in power_ups:
            dist = self._manhattan_distance(head, pu_pos)
            if dist < closest_powerup_dist:
                closest_powerup_dist = dist
                closest_powerup = pu_pos
        
        # Decision logic based on skill
        if closest_powerup and self.skill_level > 0.5:
            # High skill: consider power-ups if they're closer or very close
            if closest_powerup_dist < food_dist * 0.7:
                return closest_powerup
        
        # Default to food
        return food_position
    
    def _find_path_bfs(self, start: Tuple[int, int], 
                       target: Tuple[int, int],
                       obstacles: List[Tuple[int, int]],
                       opponent_snake: Optional[Snake]) -> List[Tuple[int, int]]:
        """
        Find path using Breadth-First Search
        
        Returns:
            List of positions forming path (excluding start)
        """
        if start == target:
            return []
        
        # BFS setup
        queue = deque([(start, [])])
        visited: Set[Tuple[int, int]] = {start}
        obstacle_set = set(obstacles)
        
        # Add opponent body to obstacles (but not head, it will move)
        if opponent_snake and opponent_snake.alive:
            obstacle_set.update(opponent_snake.body[1:])
        
        while queue:
            current, path = queue.popleft()
            
            # Check all adjacent positions
            for next_pos in self._get_adjacent_positions(current):
                if next_pos in visited:
                    continue
                
                # Check if valid position
                if not self._is_valid_position(next_pos, obstacle_set):
                    continue
                
                new_path = path + [next_pos]
                
                # Found target
                if next_pos == target:
                    return new_path
                
                visited.add(next_pos)
                queue.append((next_pos, new_path))
        
        # No path found
        return []
    
    def _get_adjacent_positions(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get all adjacent grid positions"""
        x, y = pos
        return [
            (x, y - 1),  # Up
            (x, y + 1),  # Down
            (x - 1, y),  # Left
            (x + 1, y)   # Right
        ]
    
    def _is_valid_position(self, pos: Tuple[int, int], 
                          obstacles: Set[Tuple[int, int]]) -> bool:
        """Check if position is valid (in bounds and not obstacle)"""
        x, y = pos
        
        # Check bounds
        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
            return False
        
        # Check obstacles
        if pos in obstacles:
            return False
        
        return True
    
    def _get_direction_to_adjacent(self, target: Tuple[int, int]) -> Optional[Direction]:
        """Get direction to move to adjacent target position"""
        head_x, head_y = self.snake.get_head_position()
        target_x, target_y = target
        
        dx = target_x - head_x
        dy = target_y - head_y
        
        if dx == 1:
            return Direction.RIGHT
        elif dx == -1:
            return Direction.LEFT
        elif dy == 1:
            return Direction.DOWN
        elif dy == -1:
            return Direction.UP
        
        return None
    
    def _make_best_guess_move(self, food_position: Tuple[int, int],
                              obstacles: List[Tuple[int, int]],
                              opponent_snake: Optional[Snake]):
        """Make best move when no path available"""
        head = self.snake.get_head_position()
        possible_moves = self.snake.get_possible_moves()
        
        # Evaluate each possible move
        best_direction = None
        best_score = -float('inf')
        
        obstacle_set = set(obstacles)
        if opponent_snake and opponent_snake.alive:
            obstacle_set.update(opponent_snake.body)
        
        for direction in possible_moves:
            next_pos = self._get_next_position(head, direction)
            
            # Skip invalid positions
            if not self._is_valid_position(next_pos, obstacle_set):
                continue
            
            # Score this move
            score = self._evaluate_move(next_pos, food_position, obstacle_set)
            
            if score > best_score:
                best_score = score
                best_direction = direction
        
        # Make best move or random safe move
        if best_direction:
            self.snake.change_direction(best_direction)
        else:
            self._make_safe_random_move(obstacles, opponent_snake)
    
    def _evaluate_move(self, position: Tuple[int, int], 
                      food_position: Tuple[int, int],
                      obstacles: Set[Tuple[int, int]]) -> float:
        """
        Evaluate quality of a move position
        
        Returns:
            Score (higher is better)
        """
        score = 0.0
        
        # Distance to food (closer is better)
        food_dist = self._manhattan_distance(position, food_position)
        score -= food_dist * 2
        
        # Distance from walls (prefer center)
        wall_dist = min(
            position[0],
            GRID_WIDTH - 1 - position[0],
            position[1],
            GRID_HEIGHT - 1 - position[1]
        )
        score += wall_dist * 0.5
        
        # Avoid crowded areas
        adjacent_obstacles = sum(
            1 for adj in self._get_adjacent_positions(position)
            if adj in obstacles
        )
        score -= adjacent_obstacles * 3
        
        return score
    
    def _make_safe_random_move(self, obstacles: List[Tuple[int, int]],
                               opponent_snake: Optional[Snake]):
        """Make a random safe move"""
        head = self.snake.get_head_position()
        possible_moves = self.snake.get_possible_moves()
        
        obstacle_set = set(obstacles)
        if opponent_snake and opponent_snake.alive:
            obstacle_set.update(opponent_snake.body)
        
        # Filter to safe moves
        safe_moves = []
        for direction in possible_moves:
            next_pos = self._get_next_position(head, direction)
            if self._is_valid_position(next_pos, obstacle_set):
                safe_moves.append(direction)
        
        if safe_moves:
            self.snake.change_direction(random.choice(safe_moves))
    
    def _get_next_position(self, current: Tuple[int, int], 
                          direction: Direction) -> Tuple[int, int]:
        """Get next position in given direction"""
        x, y = current
        
        if direction == Direction.UP:
            return (x, y - 1)
        elif direction == Direction.DOWN:
            return (x, y + 1)
        elif direction == Direction.LEFT:
            return (x - 1, y)
        elif direction == Direction.RIGHT:
            return (x + 1, y)
        
        return current
    
    def _manhattan_distance(self, pos1: Tuple[int, int], 
                           pos2: Tuple[int, int]) -> int:
        """Calculate Manhattan distance between two positions"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
