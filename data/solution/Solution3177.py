import random
import functools
import collections
import string
import math
import datetime


from functools import lru_cache
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        @lru_cache(None)
        def dp(index, last_num, changes):
            if index == len(nums):
                return 0
            
            # Option 1: Skip the current number
            max_length = dp(index + 1, last_num, changes)
            
            # Option 2: Include the current number
            if last_num == -1 or nums[index] == last_num:
                max_length = max(max_length, 1 + dp(index + 1, nums[index], changes))
            elif changes < k:
                max_length = max(max_length, 1 + dp(index + 1, nums[index], changes + 1))
            
            return max_length
        
        return dp(0, -1, 0)

def maximumLength(nums: List[int], k: int) -> int:
    return Solution().maximumLength(nums, k)