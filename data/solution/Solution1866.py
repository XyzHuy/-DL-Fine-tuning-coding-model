import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize dp table
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        # Fill the dp table using the recurrence relation
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]
                dp[i][j] %= MOD
        
        return dp[n][k]

def rearrangeSticks(n: int, k: int) -> int:
    return Solution().rearrangeSticks(n, k)