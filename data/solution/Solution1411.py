import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case: 6 ways for type A, 6 ways for type B
        dp = [[6, 6] for _ in range(n)]
        
        # Fill the dp table
        for i in range(1, n):
            dp[i][0] = (3 * dp[i-1][0] + 2 * dp[i-1][1]) % MOD  # 3A + 2B -> A
            dp[i][1] = (2 * dp[i-1][0] + 2 * dp[i-1][1]) % MOD  # 2A + 2B -> B
        
        # The result is the sum of ways to end with type A or type B on the nth row
        return (dp[n-1][0] + dp[n-1][1]) % MOD

def numOfWays(n: int) -> int:
    return Solution().numOfWays(n)