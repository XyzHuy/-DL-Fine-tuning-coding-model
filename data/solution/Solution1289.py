import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        # Initialize the DP table with the first row of the grid
        dp = [row[:] for row in grid]
        
        for i in range(1, n):
            # Find the smallest and second smallest values in the previous row
            min_val = second_min_val = float('inf')
            min_col = -1
            for j in range(n):
                if dp[i-1][j] < min_val:
                    second_min_val = min_val
                    min_val = dp[i-1][j]
                    min_col = j
                elif dp[i-1][j] < second_min_val:
                    second_min_val = dp[i-1][j]
            
            # Update the DP table for the current row
            for j in range(n):
                if j == min_col:
                    dp[i][j] += second_min_val
                else:
                    dp[i][j] += min_val
        
        # The answer is the minimum value in the last row of the DP table
        return min(dp[-1])

def minFallingPathSum(grid: List[List[int]]) -> int:
    return Solution().minFallingPathSum(grid)