import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # Skip the next element as it's already paired
                else:
                    i += 1
            return count >= p
        
        low, high = 0, nums[-1] - nums[0]
        
        while low <= high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

def minimizeMax(nums: List[int], p: int) -> int:
    return Solution().minimizeMax(nums, p)