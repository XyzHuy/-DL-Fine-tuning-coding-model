import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Create a DP table with (n+1) x (k+1) dimensions
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Base case: There's one way to distribute 0 candies into 0 bags
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Case 1: Place the i-th candy in one of the j existing bags
                dp[i][j] = j * dp[i - 1][j]
                # Case 2: Place the i-th candy in a new bag
                dp[i][j] += dp[i - 1][j - 1]
                # Take modulo to avoid overflow
                dp[i][j] %= MOD
        
        # The answer is the number of ways to distribute n candies into k bags
        return dp[n][k]

def waysToDistribute(n: int, k: int) -> int:
    return Solution().waysToDistribute(n, k)