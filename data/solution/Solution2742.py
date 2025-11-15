import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        @lru_cache(None)
        def dp(i, remaining):
            if remaining <= 0:
                return 0
            if i >= n:
                return float('inf')
            
            # Option 1: Paid painter paints the ith wall
            paid_painter = cost[i] + dp(i + 1, remaining - time[i] - 1)
            
            # Option 2: Free painter paints the ith wall (if paid painter is occupied)
            free_painter = dp(i + 1, remaining)
            
            return min(paid_painter, free_painter)
        
        return dp(0, n)

def paintWalls(cost: List[int], time: List[int]) -> int:
    return Solution().paintWalls(cost, time)