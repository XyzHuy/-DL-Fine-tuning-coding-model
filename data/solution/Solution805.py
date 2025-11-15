import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        
        # If the array has only one element, it's not possible to split it into two non-empty parts
        if n == 1:
            return False
        
        # Precompute the possible sums for each subset size
        @lru_cache(None)
        def possible_sums(index, count):
            if count == 0:
                return {0}
            if index == n:
                return set()
            
            # Include the current number in the subset
            with_current = {x + nums[index] for x in possible_sums(index + 1, count - 1)}
            # Exclude the current number from the subset
            without_current = possible_sums(index + 1, count)
            
            return with_current | without_current
        
        # Check for each possible subset size (from 1 to n//2)
        for i in range(1, (n // 2) + 1):
            if total_sum * i % n == 0:
                target_sum = total_sum * i // n
                if target_sum in possible_sums(0, i):
                    return True
        
        return False

def splitArraySameAverage(nums: List[int]) -> bool:
    return Solution().splitArraySameAverage(nums)