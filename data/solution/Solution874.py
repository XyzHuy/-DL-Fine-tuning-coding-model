import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Define the directions in order: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Start at position (0, 0) facing north (direction index 0)
        x, y = 0, 0
        direction_index = 0
        
        # Convert obstacles list to a set for O(1) lookups
        obstacles_set = set(map(tuple, obstacles))
        
        # Variable to keep track of the maximum distance squared
        max_distance_squared = 0
        
        # Process each command
        for command in commands:
            if command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            else:  # Move forward
                dx, dy = directions[direction_index]
                for _ in range(command):
                    # Check if the next position is an obstacle
                    if (x + dx, y + dy) not in obstacles_set:
                        x += dx
                        y += dy
                    else:
                        break
                # Update the maximum distance squared
                max_distance_squared = max(max_distance_squared, x * x + y * y)
        
        return max_distance_squared

def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    return Solution().robotSim(commands, obstacles)