import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize a DP table with infinity
        dp = [[math.inf] * n for _ in range(m)]
        
        # Base case: the first row's cost is just the value of the cells themselves
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        # Fill the DP table
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    # Calculate the cost of moving from cell (i-1, k) to cell (i, j)
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + moveCost[grid[i-1][k]][j] + grid[i][j])
        
        # The result is the minimum cost to reach any cell in the last row
        return min(dp[m-1])

def minPathCost(grid: List[List[int]], moveCost: List[List[int]]) -> int:
    return Solution().minPathCost(grid, moveCost)