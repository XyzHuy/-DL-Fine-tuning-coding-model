import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of ways to reach each cell
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first row and first column to 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The bottom-right corner will have the number of unique paths
        return dp[m - 1][n - 1]

def uniquePaths(m: int, n: int) -> int:
    return Solution().uniquePaths(m, n)