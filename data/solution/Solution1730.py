import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # Find the starting position
        start = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    start = (i, j)
                    break
            if start:
                break
        
        # Directions for moving north, east, south, west
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS initialization
        queue = deque([start])
        visited = set([start])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                # Check if we have reached a food cell
                if grid[x][y] == '#':
                    return steps
                
                # Explore neighbors
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] != 'X':
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            
            # Increment the step count after exploring all nodes at the current level
            steps += 1
        
        # If no food cell is reachable
        return -1

def getFood(grid: List[List[str]]) -> int:
    return Solution().getFood(grid)