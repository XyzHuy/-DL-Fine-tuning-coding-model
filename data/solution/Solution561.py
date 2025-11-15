import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        # Sum every second element starting from the first
        return sum(nums[::2])

def arrayPairSum(nums: List[int]) -> int:
    return Solution().arrayPairSum(nums)