import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add the start and end points of the stick to the cuts list and sort it
        cuts = sorted(cuts + [0, n])
        
        @lru_cache(None)
        def dp(left, right):
            # If there are no cuts between left and right, the cost is 0
            if right - left <= 1:
                return 0
            # Try every possible cut between left and right
            min_cost = float('inf')
            for i in range(left + 1, right):
                # The cost of making a cut at cuts[i] is the length of the stick (cuts[right] - cuts[left])
                # plus the cost of the left and right subproblems
                cost = cuts[right] - cuts[left] + dp(left, i) + dp(i, right)
                min_cost = min(min_cost, cost)
            return min_cost
        
        # Start the recursion with the full length of the stick
        return dp(0, len(cuts) - 1)

def minCost(n: int, cuts: List[int]) -> int:
    return Solution().minCost(n, cuts)