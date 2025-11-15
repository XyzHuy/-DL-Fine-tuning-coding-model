import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)  # Start with n
        for i in range(len(nums)):
            missing ^= i ^ nums[i]  # XOR i and nums[i] and the current missing value
        return missing

def missingNumber(nums: List[int]) -> int:
    return Solution().missingNumber(nums)