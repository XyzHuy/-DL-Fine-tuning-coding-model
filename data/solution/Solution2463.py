import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        @lru_cache(None)
        def dp(r, f):
            if r == len(robot):
                return 0
            if f == len(factory):
                return float('inf')
            
            # Skip the current factory
            min_cost = dp(r, f + 1)
            cost = 0
            
            # Try to assign robots to the current factory
            for i in range(r, min(r + factory[f][1], len(robot))):
                cost += abs(robot[i] - factory[f][0])
                min_cost = min(min_cost, cost + dp(i + 1, f + 1))
            
            return min_cost
        
        return dp(0, 0)

def minimumTotalDistance(robot: List[int], factory: List[List[int]]) -> int:
    return Solution().minimumTotalDistance(robot, factory)