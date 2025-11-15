import random
import functools
import collections
import string
import math
import datetime


from typing import List
import functools

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @functools.lru_cache(None)
        def dp(i, prev_color, groups):
            if i == m:
                return 0 if groups == target else float('inf')
            
            if houses[i] != 0:
                # If the house is already painted
                new_groups = groups + (1 if houses[i] != prev_color else 0)
                return dp(i + 1, houses[i], new_groups)
            else:
                # Try painting the house with each color
                min_cost = float('inf')
                for color in range(1, n + 1):
                    new_groups = groups + (1 if color != prev_color else 0)
                    min_cost = min(min_cost, cost[i][color - 1] + dp(i + 1, color, new_groups))
                return min_cost
        
        result = dp(0, 0, 0)
        return result if result != float('inf') else -1

def minCost(houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    return Solution().minCost(houses, cost, m, n, target)