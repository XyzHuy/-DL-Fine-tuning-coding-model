import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        
        @lru_cache(None)
        def dp(mask, gain):
            if mask == (1 << n) - 1:
                return 0
            
            days = float('inf')
            for i in range(n):
                if not (mask & (1 << i)):
                    # Days to defeat the i-th monster
                    current_days = (power[i] - 1) // gain + 1
                    # Recursively calculate the days needed for the remaining monsters
                    days = min(days, current_days + dp(mask | (1 << i), gain + 1))
            
            return days
        
        return dp(0, 1)

def minimumTime(power: List[int]) -> int:
    return Solution().minimumTime(power)