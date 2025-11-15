import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # If the array length is 1 or 2, it can always be split into arrays of size 1
        if len(nums) <= 2:
            return True
        
        # Check if there exists any pair of adjacent elements whose sum is at least m
        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] >= m:
                return True
        
        return False

def canSplitArray(nums: List[int], m: int) -> bool:
    return Solution().canSplitArray(nums, m)