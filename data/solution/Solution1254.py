import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        closed_count = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1  # Mark the cell as visited by turning it into water
            
            # Explore all 4 directions
            top = dfs(r - 1, c)
            bottom = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            # The island is closed if all sides are closed
            return top and bottom and left and right
        
        for r in range(rows):
            for c in range(cols):
                # Only check for land cells that are not on the border
                if grid[r][c] == 0 and dfs(r, c):
                    closed_count += 1
        
        return closed_count

def closedIsland(grid: List[List[int]]) -> int:
    return Solution().closedIsland(grid)