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

        # Initialize variables to track the minimum cost and maximum profit for up to two transactions
        min_cost1 = float('inf')
        min_cost2 = float('inf')
        max_profit1 = 0
        max_profit2 = 0

        for price in prices:
            # Calculate the maximum profit after the first transaction
            max_profit1 = max(max_profit1, price - min_cost1)
            # Update the minimum cost for the first transaction
            min_cost1 = min(min_cost1, price)
            
            # Calculate the maximum profit after the second transaction
            max_profit2 = max(max_profit2, price - min_cost2)
            # Update the minimum cost for the second transaction
            min_cost2 = min(min_cost2, price - max_profit1)

        return max_profit2

def maxProfit(prices: List[int]) -> int:
    return Solution().maxProfit(prices)