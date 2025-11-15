import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][r] will store the number of ways to reach cell (i, j) with a path sum % k == r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Initialize the starting point
        dp[0][0][grid[0][0] % k] = 1
        
        # Fill the first row
        for j in range(1, n):
            for r in range(k):
                if dp[0][j-1][r] > 0:
                    new_r = (r + grid[0][j]) % k
                    dp[0][j][new_r] = dp[0][j-1][r]
        
        # Fill the first column
        for i in range(1, m):
            for r in range(k):
                if dp[i-1][0][r] > 0:
                    new_r = (r + grid[i][0]) % k
                    dp[i][0][new_r] = dp[i-1][0][r]
        
        # Fill the rest of the dp table
        for i in range(1, m):
            for j in range(1, n):
                for r in range(k):
                    if dp[i-1][j][r] > 0:
                        new_r = (r + grid[i][j]) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i-1][j][r]) % MOD
                    if dp[i][j-1][r] > 0:
                        new_r = (r + grid[i][j]) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j-1][r]) % MOD
        
        # The answer is the number of ways to reach (m-1, n-1) with a path sum % k == 0
        return dp[m-1][n-1][0]

def numberOfPaths(grid: List[List[int]], k: int) -> int:
    return Solution().numberOfPaths(grid, k)