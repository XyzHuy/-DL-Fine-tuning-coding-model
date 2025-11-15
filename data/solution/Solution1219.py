import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.max_gold = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c, current_gold):
            # Check boundaries and if the cell is already visited or has no gold
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            
            # Collect gold from the current cell
            current_gold += grid[r][c]
            self.max_gold = max(self.max_gold, current_gold)
            
            # Temporarily mark the cell as visited
            original_gold = grid[r][c]
            grid[r][c] = 0
            
            # Explore all four possible directions
            dfs(r + 1, c, current_gold)
            dfs(r - 1, c, current_gold)
            dfs(r, c + 1, current_gold)
            dfs(r, c - 1, current_gold)
            
            # Backtrack: restore the cell's original value
            grid[r][c] = original_gold
        
        # Try starting the DFS from each cell that contains gold
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    dfs(r, c, 0)
        
        return self.max_gold

def getMaximumGold(grid: List[List[int]]) -> int:
    return Solution().getMaximumGold(grid)