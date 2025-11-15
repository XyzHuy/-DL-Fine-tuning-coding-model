import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def integerBreak(self, n: int) -> int:
        # Base cases
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        # Dynamic programming array to store the maximum product for each number up to n
        dp = [0] * (n + 1)
        dp[1] = 1
        
        # Fill the dp array
        for i in range(2, n + 1):
            max_product = 0
            for j in range(1, i):
                # We compare j * (i - j) and j * dp[i - j] to consider breaking i - j further or not
                max_product = max(max_product, j * (i - j), j * dp[i - j])
            dp[i] = max_product
        
        return dp[n]

def integerBreak(n: int) -> int:
    return Solution().integerBreak(n)