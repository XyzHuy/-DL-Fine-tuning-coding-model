import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        min_val = nums[0]
        max_val = nums[-1]
        result = max_val - min_val
        
        for i in range(n - 1):
            # We can either add k to the first i+1 elements or subtract k from the last n-i elements
            # So we consider the new max and min values after making the changes
            high = max(max_val - k, nums[i] + k)
            low = min(min_val + k, nums[i + 1] - k)
            result = min(result, high - low)
        
        return result

def smallestRangeII(nums: List[int], k: int) -> int:
    return Solution().smallestRangeII(nums, k)