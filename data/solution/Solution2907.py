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
        max_profit = -1
        
        # Precompute the best profit we can get for each j as the middle element
        best_before = [-float('inf')] * n
        for j in range(1, n):
            for i in range(j):
                if prices[i] < prices[j]:
                    best_before[j] = max(best_before[j], profits[i])
        
        # Now find the best profit we can get with each k as the last element
        for k in range(2, n):
            for j in range(k):
                if prices[j] < prices[k] and best_before[j] != -float('inf'):
                    max_profit = max(max_profit, best_before[j] + profits[j] + profits[k])
        
        return max_profit if max_profit != -1 else -1

def maxProfit(prices: List[int], profits: List[int]) -> int:
    return Solution().maxProfit(prices, profits)