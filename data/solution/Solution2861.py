import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        def canProduce(machine, alloys):
            total_cost = 0
            for i in range(n):
                needed = composition[machine][i] * alloys
                if needed > stock[i]:
                    total_cost += (needed - stock[i]) * cost[i]
                    if total_cost > budget:
                        return False
            return True
        
        max_alloys = 0
        for machine in range(k):
            left, right = 0, budget + max(stock)
            while left < right:
                mid = (left + right + 1) // 2
                if canProduce(machine, mid):
                    left = mid
                else:
                    right = mid - 1
            max_alloys = max(max_alloys, left)
        
        return max_alloys

def maxNumberOfAlloys(n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
    return Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)