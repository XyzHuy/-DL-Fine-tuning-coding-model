import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j] will store the number of ways to arrange i numbers with j inverse pairs
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: one way to arrange 0 numbers with 0 inverse pairs
        
        # Fill the dp table
        for i in range(1, n + 1):
            prefix_sum = 0
            for j in range(k + 1):
                prefix_sum += dp[i - 1][j]
                if j >= i:
                    prefix_sum -= dp[i - 1][j - i]
                prefix_sum = prefix_sum % MOD
                dp[i][j] = prefix_sum
        
        return dp[n][k]

def kInversePairs(n: int, k: int) -> int:
    return Solution().kInversePairs(n, k)