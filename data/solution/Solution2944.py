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
        # dp[i] will hold the minimum coins needed to acquire the first i fruits
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No cost to acquire 0 fruits

        for i in range(1, n + 1):
            # Option 1: Buy the ith fruit
            dp[i] = dp[i - 1] + prices[i - 1]
            # Option 2: Use the reward from buying a previous fruit to take the ith fruit for free
            for j in range(1, i):
                if i <= 2 * j:  # Check if the ith fruit can be taken for free after buying the jth fruit
                    dp[i] = min(dp[i], dp[j - 1] + prices[j - 1])

        return dp[n]

def minimumCoins(prices: List[int]) -> int:
    return Solution().minimumCoins(prices)