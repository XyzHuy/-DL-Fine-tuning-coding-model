import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import gcd
from functools import lru_cache

class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(start):
            if start == len(nums):
                return 0
            if start == len(nums) - 1:
                return 1 if nums[start] > 1 else float('inf')
            
            min_subarrays = float('inf')
            for end in range(start + 1, len(nums) + 1):
                if gcd(nums[start], nums[end - 1]) > 1:
                    min_subarrays = min(min_subarrays, 1 + dp(end))
            
            return min_subarrays
        
        result = dp(0)
        return result if result != float('inf') else -1

def validSubarraySplit(nums: List[int]) -> int:
    return Solution().validSubarraySplit(nums)