import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # Directions for 4-directional movement (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes_elapsed = 0
        
        # Perform BFS to rot adjacent fresh oranges
        while queue and fresh_count > 0:
            minutes_elapsed += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
        
        # If there are still fresh oranges left, return -1
        return minutes_elapsed if fresh_count == 0 else -1

def orangesRotting(grid: List[List[int]]) -> int:
    return Solution().orangesRotting(grid)