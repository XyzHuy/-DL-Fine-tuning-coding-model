import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        # dp[d][t] means the number of ways to get sum t using d dice
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: one way to get sum 0 with 0 dice
        
        for d in range(1, n + 1):
            for t in range(1, target + 1):
                for f in range(1, k + 1):
                    if t >= f:
                        dp[d][t] = (dp[d][t] + dp[d - 1][t - f]) % MOD
        
        return dp[n][target]

def numRollsToTarget(n: int, k: int, target: int) -> int:
    return Solution().numRollsToTarget(n, k, target)