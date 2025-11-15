import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Start at the origin (0, 0)
        x, y = 0, 0
        # Use a set to keep track of visited positions
        visited = set()
        # Add the starting position to the set
        visited.add((x, y))
        
        # Define direction vectors for each move
        directions = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        
        # Traverse the path
        for move in path:
            # Update the current position based on the move
            dx, dy = directions[move]
            x += dx
            y += dy
            
            # Check if the new position has been visited before
            if (x, y) in visited:
                return True
            
            # Add the new position to the set of visited positions
            visited.add((x, y))
        
        # If no position is visited more than once, return False
        return False

def isPathCrossing(path: str) -> bool:
    return Solution().isPathCrossing(path)