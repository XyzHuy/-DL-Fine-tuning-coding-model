import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        if n < 3:
            return -1
        
        # To store the maximum profit of items with price less than prices[i]
        max_profit_before = [-float('inf')] * n
        # To store the maximum profit of items with price greater than prices[i]
        max_profit_after = [-float('inf')] * n
        
        # Calculate max_profit_before for each item
        for i in range(1, n):
            for j in range(i):
                if prices[j] < prices[i]:
                    max_profit_before[i] = max(max_profit_before[i], profits[j])
        
        # Calculate max_profit_after for each item
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if prices[j] > prices[i]:
                    max_profit_after[i] = max(max_profit_after[i], profits[j])
        
        # Calculate the maximum profit for a valid triplet
        max_profit = -1
        for i in range(1, n-1):
            if max_profit_before[i] != -float('inf') and max_profit_after[i] != -float('inf'):
                max_profit = max(max_profit, max_profit_before[i] + profits[i] + max_profit_after[i])
        
        return max_profit

def maxProfit(prices: List[int], profits: List[int]) -> int:
    return Solution().maxProfit(prices, profits)