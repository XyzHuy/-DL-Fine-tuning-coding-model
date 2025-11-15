import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = prices[:]  # Create a copy of the prices list to store the final prices
        
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break
        
        return answer

def finalPrices(prices: List[int]) -> List[int]:
    return Solution().finalPrices(prices)