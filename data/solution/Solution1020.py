import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0  # Mark the cell as visited by setting it to 0
            # Visit all 4-directionally adjacent cells
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Remove all land cells connected to the boundary
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][cols - 1] == 1:
                dfs(r, cols - 1)
        
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[rows - 1][c] == 1:
                dfs(rows - 1, c)
        
        # Count the remaining land cells that are not connected to the boundary
        return sum(sum(row) for row in grid)

def numEnclaves(grid: List[List[int]]) -> int:
    return Solution().numEnclaves(grid)