import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        from math import comb
        
        def count_ways(x):
            # Count the number of ways to distribute x candies to 3 children without restrictions
            if x < 0:
                return 0
            return comb(x + 2, 2)
        
        if limit * 3 < n:
            return 0
        
        total_ways = count_ways(n)
        
        # Subtract cases where at least one child gets more than limit candies
        total_ways -= 3 * count_ways(n - limit - 1)
        
        # Add back cases where at least two children get more than limit candies
        total_ways += 3 * count_ways(n - 2 * limit - 2)
        
        return total_ways

def distributeCandies(n: int, limit: int) -> int:
    return Solution().distributeCandies(n, limit)