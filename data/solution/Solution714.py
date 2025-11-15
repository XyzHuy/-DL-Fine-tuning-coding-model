import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Initialize the variables to keep track of cash and hold
        cash, hold = 0, float('-inf')
        
        for price in prices:
            # Update cash to be the maximum of itself or the profit from selling at the current price minus the fee
            cash = max(cash, hold + price - fee)
            # Update hold to be the maximum of itself or the profit from buying at the current price
            hold = max(hold, cash - price)
        
        # The maximum profit will be in cash, as we want to end up with no stocks held
        return cash

def maxProfit(prices: List[int], fee: int) -> int:
    return Solution().maxProfit(prices, fee)