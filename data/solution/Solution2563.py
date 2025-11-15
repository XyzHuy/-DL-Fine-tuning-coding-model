import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            # Find the range of indices for valid j such that lower <= nums[i] + nums[j] <= upper
            left_bound = lower - nums[i]
            right_bound = upper - nums[i]
            
            # Find the first index where nums[j] >= left_bound
            left_index = bisect_left(nums, left_bound, i + 1, n)
            # Find the last index where nums[j] <= right_bound
            right_index = bisect_right(nums, right_bound, i + 1, n) - 1
            
            # All indices from left_index to right_index are valid for j
            if left_index <= right_index:
                count += right_index - left_index + 1
        
        return count

def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
    return Solution().countFairPairs(nums, lower, upper)