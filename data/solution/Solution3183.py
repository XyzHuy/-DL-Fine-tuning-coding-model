import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Create a dp array to store the number of ways to make each value up to n
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to make 0, which is using no coins
        
        # Iterate over each coin type
        for coin in [1, 2, 6]:
            for i in range(coin, n + 1):
                dp[i] = (dp[i] + dp[i - coin]) % MOD
        
        # Now, we need to consider the two 4-coin cases
        # Case 1: No 4-coin used
        result = dp[n]
        
        # Case 2: One 4-coin used
        if n >= 4:
            result = (result + dp[n - 4]) % MOD
        
        # Case 3: Two 4-coins used
        if n >= 8:
            result = (result + dp[n - 8]) % MOD
        
        return result

def numberOfWays(n: int) -> int:
    return Solution().numberOfWays(n)