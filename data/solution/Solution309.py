import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # hold: the maximum profit we can have while holding a stock
        # sold: the maximum profit we can have just after selling a stock
        # rest: the maximum profit we can have while being in cooldown
        hold, sold, rest = float('-inf'), 0, 0

        for price in prices:
            # Update hold to be the max of itself or the profit from the rest state minus the price of the stock
            hold = max(hold, rest - price)
            # Update rest to be the max of itself or the previous sold state
            rest = max(rest, sold)
            # Update sold to be the profit from holding a stock and selling it at the current price
            sold = hold + price

        # The answer will be the max profit we can have in the rest or sold state (since we cannot hold a stock in the end)
        return max(sold, rest)

def maxProfit(prices: List[int]) -> int:
    return Solution().maxProfit(prices)