import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize the dp array to store the minimum operations needed
        dp = [[0] * 10 for _ in range(n)]
        
        # Fill the dp array for the last row
        for num in range(10):
            dp[n-1][num] = sum(1 for i in range(m) if grid[i][n-1] != num)
        
        # Fill the dp array for the rest of the columns from right to left
        for j in range(n-2, -1, -1):
            for num in range(10):
                # Calculate the minimum operations needed to make the current column equal to `num`
                dp[j][num] = min(dp[j+1][k] for k in range(10) if k != num) + sum(1 for i in range(m) if grid[i][j] != num)
        
        # The answer is the minimum operations needed for the first column to be any number
        return min(dp[0])

def minimumOperations(grid: List[List[int]]) -> int:
    return Solution().minimumOperations(grid)