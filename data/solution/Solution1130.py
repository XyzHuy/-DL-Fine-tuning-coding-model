import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dp(left, right):
            if left >= right:
                return 0
            min_cost = float('inf')
            for i in range(left, right):
                cost = max(arr[left:i+1]) * max(arr[i+1:right+1]) + dp(left, i) + dp(i+1, right)
                min_cost = min(min_cost, cost)
            return min_cost
        
        return dp(0, len(arr) - 1)

def mctFromLeafValues(arr: List[int]) -> int:
    return Solution().mctFromLeafValues(arr)