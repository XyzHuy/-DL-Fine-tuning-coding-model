import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array with a value greater than the maximum possible number of coins
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0
        
        # Iterate over each amount from 1 to the target amount
        for a in range(1, amount + 1):
            # Check each coin
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        
        # If dp[amount] is still amount + 1, it means it's not possible to form that amount
        return dp[amount] if dp[amount] != amount + 1 else -1

def coinChange(coins: List[int], amount: int) -> int:
    return Solution().coinChange(coins, amount)