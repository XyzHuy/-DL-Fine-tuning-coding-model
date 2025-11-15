import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Initialize the first cell
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        
        # Fill up the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[m - 1][n - 1]

def minPathSum(grid: List[List[int]]) -> int:
    return Solution().minPathSum(grid)