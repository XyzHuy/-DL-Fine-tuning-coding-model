import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # total_sum - left_sum - nums[i] gives the right sum
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        
        return -1

def pivotIndex(nums: List[int]) -> int:
    return Solution().pivotIndex(nums)