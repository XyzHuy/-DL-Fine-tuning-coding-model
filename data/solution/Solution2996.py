import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find the longest sequential prefix
        longest_sequential_prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                longest_sequential_prefix_sum += nums[i]
            else:
                break
        
        # Find the smallest missing integer greater than or equal to the sum of the longest sequential prefix
        missing_integer = longest_sequential_prefix_sum
        while True:
            if missing_integer not in nums:
                return missing_integer
            missing_integer += 1

def missingInteger(nums: List[int]) -> int:
    return Solution().missingInteger(nums)