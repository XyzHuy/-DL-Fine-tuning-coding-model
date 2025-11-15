import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # If the start or end cell is blocked, return -1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # Directions for 8 possible moves
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # BFS initialization
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark the start cell as visited
        
        while queue:
            x, y, path_length = queue.popleft()
            
            # If we reach the bottom-right cell, return the path length
            if x == n - 1 and y == n - 1:
                return path_length
            
            # Explore all 8 possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is within bounds and not visited
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1  # Mark the cell as visited
                    queue.append((nx, ny, path_length + 1))
        
        # If we exhaust the queue without finding a path, return -1
        return -1

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    return Solution().shortestPathBinaryMatrix(grid)