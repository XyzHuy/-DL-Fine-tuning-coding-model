import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp_max[i][j] stores the maximum product ending at (i, j)
        # dp_min[i][j] stores the minimum product ending at (i, j)
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]
        
        # Initialize the starting point
        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]
        
        # Initialize the first row
        for j in range(1, n):
            dp_max[0][j] = dp_max[0][j-1] * grid[0][j]
            dp_min[0][j] = dp_min[0][j-1] * grid[0][j]
        
        # Initialize the first column
        for i in range(1, m):
            dp_max[i][0] = dp_max[i-1][0] * grid[i][0]
            dp_min[i][0] = dp_min[i-1][0] * grid[i][0]
        
        # Fill the dp tables
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    dp_max[i][j] = max(dp_max[i-1][j], dp_max[i][j-1]) * grid[i][j]
                    dp_min[i][j] = min(dp_min[i-1][j], dp_min[i][j-1]) * grid[i][j]
                else:
                    dp_max[i][j] = min(dp_min[i-1][j], dp_min[i][j-1]) * grid[i][j]
                    dp_min[i][j] = max(dp_max[i-1][j], dp_max[i][j-1]) * grid[i][j]
        
        # The result is the maximum product ending at the bottom-right corner
        max_product = dp_max[m-1][n-1]
        
        return max_product % MOD if max_product >= 0 else -1

def maxProductPath(grid: List[List[int]]) -> int:
    return Solution().maxProductPath(grid)