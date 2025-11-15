import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array to find the largest and smallest values
        nums.sort()
        
        # The maximum product can be either:
        # 1. The product of the three largest numbers
        # 2. The product of the two smallest numbers (which could be negative) and the largest number
        max_product = max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        
        return max_product

def maximumProduct(nums: List[int]) -> int:
    return Solution().maximumProduct(nums)