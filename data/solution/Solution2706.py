import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Find the two chocolates with the minimum prices
        prices.sort()
        min_sum = prices[0] + prices[1]
        
        # Check if we can buy the two chocolates without going into debt
        if money >= min_sum:
            return money - min_sum
        else:
            return money

def buyChoco(prices: List[int], money: int) -> int:
    return Solution().buyChoco(prices, money)