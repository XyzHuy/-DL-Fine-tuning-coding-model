import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i, j):
            # Check for boundary conditions and if the current cell is water
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # Mark the current cell as visited by setting it to '0'
            grid[i][j] = '0'
            # Perform DFS in all four possible directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # If the cell is land, it's an unvisited island
                    num_islands += 1
                    dfs(i, j)  # Perform DFS to mark the entire island as visited
        return num_islands

def numIslands(grid: List[List[str]]) -> int:
    return Solution().numIslands(grid)