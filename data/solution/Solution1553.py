import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minDays(self, n: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(n):
            if n <= 1:
                return n
            # Option 1: Eat 1 orange
            # Option 2: If n is divisible by 2, eat n / 2 oranges
            # Option 3: If n is divisible by 3, eat 2 * (n / 3) oranges
            return 1 + min(n % 2 + dp(n // 2), n % 3 + dp(n // 3))
        
        return dp(n)

def minDays(n: int) -> int:
    return Solution().minDays(n)