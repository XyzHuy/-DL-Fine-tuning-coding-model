import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            dp[i + 1] = min(dp[i + 1], dp[i] + prices[i])
            for j in range(1, i + 2):
                if i + j + 1 <= n:
                    dp[i + j + 1] = min(dp[i + j + 1], dp[i] + prices[i])
        
        return dp[n]

def minimumCoins(prices: List[int]) -> int:
    return Solution().minimumCoins(prices)