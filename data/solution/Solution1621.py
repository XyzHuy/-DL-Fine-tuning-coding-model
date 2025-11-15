import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize dp table with zeros
        dp = [[0] * (k + 1) for _ in range(n)]
        
        # Base case: There is one way to draw zero segments with any number of points
        for i in range(n):
            dp[i][0] = 1
        
        # Fill the dp table
        for j in range(1, k + 1):
            prefix_sum = 0
            for i in range(1, n):
                # Update prefix sum excluding the i-th point
                if i - 1 >= 0:
                    prefix_sum = (prefix_sum + dp[i - 1][j - 1]) % MOD
                # The number of ways to draw j segments using i points
                dp[i][j] = (dp[i - 1][j] + prefix_sum) % MOD
        
        # The result is the number of ways to draw k segments using n points
        return dp[n - 1][k]

def numberOfSets(n: int, k: int) -> int:
    return Solution().numberOfSets(n, k)