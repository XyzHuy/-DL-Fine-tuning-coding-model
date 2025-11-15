import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            fish_count = grid[r][c]
            grid[r][c] = 0  # Mark the cell as visited
            for dr, dc in directions:
                fish_count += dfs(r + dr, c + dc)
            return fish_count
        
        max_fish = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish

def findMaxFish(grid: List[List[int]]) -> int:
    return Solution().findMaxFish(grid)