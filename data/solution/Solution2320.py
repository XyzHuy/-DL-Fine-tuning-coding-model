import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i] will store the number of ways to place houses on i plots on one side
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to arrange 0 plots
        dp[1] = 2  # Base case: 2 ways to arrange 1 plot (either place a house or not)
        
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        
        # The total number of ways to place houses on both sides is dp[n] * dp[n]
        return (dp[n] * dp[n]) % MOD

def countHousePlacements(n: int) -> int:
    return Solution().countHousePlacements(n)