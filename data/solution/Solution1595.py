import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n1, n2 = len(cost), len(cost[0])
        
        # Precompute the minimum cost to connect to each point in the second group
        min_cost_to_group2 = [min(c) for c in zip(*cost)]
        
        @lru_cache(None)
        def dp(i, mask):
            if i == n1:
                # If all points in the first group are connected, ensure all points in the second group are connected
                return sum(min_cost_to_group2[j] for j in range(n2) if not mask & (1 << j))
            
            # Connect the current point in the first group to each point in the second group
            connect_costs = [cost[i][j] + dp(i + 1, mask | (1 << j)) for j in range(n2)]
            return min(connect_costs)
        
        return dp(0, 0)

def connectTwoGroups(cost: List[List[int]]) -> int:
    return Solution().connectTwoGroups(cost)