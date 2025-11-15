import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        # Find the minimum and maximum values in the list
        min_val = min(nums)
        max_val = max(nums)
        # Return the first number that is neither min nor max
        for num in nums:
            if num != min_val and num != max_val:
                return num
        return -1

def findNonMinOrMax(nums: List[int]) -> int:
    return Solution().findNonMinOrMax(nums)