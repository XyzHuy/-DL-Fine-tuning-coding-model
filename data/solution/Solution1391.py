import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Define possible directions for each type of street
        directions = {
            1: [(0, -1), (0, 1)],  # left, right
            2: [(-1, 0), (1, 0)],  # up, down
            3: [(0, -1), (1, 0)],  # left, down
            4: [(0, 1), (1, 0)],   # right, down
            5: [(0, -1), (-1, 0)], # left, up
            6: [(0, 1), (-1, 0)]   # right, up
        }
        
        # Define the opposite directions
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }
        
        # Initialize the queue with the starting position and visited set
        queue = [(0, 0)]
        visited = set((0, 0))
        m, n = len(grid), len(grid[0])
        
        # Perform BFS
        while queue:
            x, y = queue.pop(0)
            if (x, y) == (m - 1, n - 1):
                return True
            
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    # Check if the neighboring cell can connect back to the current cell
                    if (-dx, -dy) in directions[grid[nx][ny]]:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False

def hasValidPath(grid: List[List[int]]) -> bool:
    return Solution().hasValidPath(grid)