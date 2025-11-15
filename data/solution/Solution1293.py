import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Queue for BFS: (x, y, steps, remaining_k)
        queue = deque([(0, 0, 0, k)])
        
        # Visited set to keep track of visited states (x, y, remaining_k)
        visited = set((0, 0, k))
        
        while queue:
            x, y, steps, remaining_k = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0 and (nx, ny, remaining_k) not in visited:
                        # Move to an empty cell
                        visited.add((nx, ny, remaining_k))
                        queue.append((nx, ny, steps + 1, remaining_k))
                    elif grid[nx][ny] == 1 and remaining_k > 0 and (nx, ny, remaining_k - 1) not in visited:
                        # Eliminate an obstacle if possible
                        visited.add((nx, ny, remaining_k - 1))
                        queue.append((nx, ny, steps + 1, remaining_k - 1))
                    
                    # Check if we reached the bottom-right corner
                    if nx == m - 1 and ny == n - 1:
                        return steps + 1
        
        return -1

def shortestPath(grid: List[List[int]], k: int) -> int:
    return Solution().shortestPath(grid, k)