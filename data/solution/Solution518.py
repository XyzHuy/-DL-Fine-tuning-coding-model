import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize a list to store the number of ways to make each amount up to the target amount
        dp = [0] * (amount + 1)
        # There is one way to make the amount 0, which is to use no coins
        dp[0] = 1
        
        # Iterate over each coin
        for coin in coins:
            # Update the dp array for each amount from the coin value up to the target amount
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        # The answer is the number of ways to make the target amount
        return dp[amount]

def change(amount: int, coins: List[int]) -> int:
    return Solution().change(amount, coins)