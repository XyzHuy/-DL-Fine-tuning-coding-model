import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        valid_splits = 0
        
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits

def waysToSplitArray(nums: List[int]) -> int:
    return Solution().waysToSplitArray(nums)