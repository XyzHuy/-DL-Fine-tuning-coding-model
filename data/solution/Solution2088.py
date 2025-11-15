import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Function to count pyramidal plots
        def count_pyramids(grid):
            dp = [[0] * n for _ in range(m)]
            count = 0
            
            # Fill the dp table for pyramids
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 0:
                        continue
                    if r == 0 or c == 0 or c == n - 1:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1]) + 1
                    count += max(0, dp[r][c] - 1)
            
            return count
        
        # Count pyramidal plots
        total_pyramids = count_pyramids(grid)
        
        # Count inverse pyramidal plots by flipping the grid upside down
        total_inverse_pyramids = count_pyramids(grid[::-1])
        
        return total_pyramids + total_inverse_pyramids

def countPyramids(grid: List[List[int]]) -> int:
    return Solution().countPyramids(grid)