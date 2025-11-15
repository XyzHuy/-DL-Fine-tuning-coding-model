import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i] represents the number of ways to tile a 2x[i] board
        # dp1[i] represents the number of ways to tile a 2x[i] board with one square missing at the end (either top or bottom)
        dp = [0] * (n + 1)
        dp1 = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # 1 way to tile a 2x0 board (do nothing)
        dp[1] = 1  # 1 way to tile a 2x1 board (one vertical domino)
        if n > 1:
            dp[2] = 2  # 2 ways to tile a 2x2 board (two vertical dominos or two horizontal dominos)
            dp1[2] = 1 # 1 way to tile a 2x2 board with one square missing at the end (one tromino)
        
        # Fill the dp array using the recurrence relations
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp1[i - 1]) % MOD
            dp1[i] = (dp[i - 2] + dp1[i - 1]) % MOD
        
        return dp[n]

def numTilings(n: int) -> int:
    return Solution().numTilings(n)