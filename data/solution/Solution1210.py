import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # (r, c, is_horizontal)
        start = (0, 0, True)
        target = (n-1, n-2, True)
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            (r, c, is_horizontal), moves = queue.popleft()
            
            if (r, c, is_horizontal) == target:
                return moves
            
            if is_horizontal:
                # Move right
                if c + 2 < n and grid[r][c+2] == 0 and (r, c+1, True) not in visited:
                    visited.add((r, c+1, True))
                    queue.append(((r, c+1, True), moves + 1))
                # Move down
                if r + 1 < n and grid[r+1][c] == 0 and grid[r+1][c+1] == 0 and (r+1, c, True) not in visited:
                    visited.add((r+1, c, True))
                    queue.append(((r+1, c, True), moves + 1))
                # Rotate clockwise
                if r + 1 < n and grid[r+1][c] == 0 and grid[r+1][c+1] == 0 and (r, c, False) not in visited:
                    visited.add((r, c, False))
                    queue.append(((r, c, False), moves + 1))
            else:
                # Move right
                if c + 1 < n and grid[r][c+1] == 0 and grid[r+1][c+1] == 0 and (r, c+1, False) not in visited:
                    visited.add((r, c+1, False))
                    queue.append(((r, c+1, False), moves + 1))
                # Move down
                if r + 2 < n and grid[r+2][c] == 0 and (r+1, c, False) not in visited:
                    visited.add((r+1, c, False))
                    queue.append(((r+1, c, False), moves + 1))
                # Rotate counterclockwise
                if c + 1 < n and grid[r][c+1] == 0 and grid[r+1][c+1] == 0 and (r, c, True) not in visited:
                    visited.add((r, c, True))
                    queue.append(((r, c, True), moves + 1))
        
        return -1

def minimumMoves(grid: List[List[int]]) -> int:
    return Solution().minimumMoves(grid)