import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        positive_nums = [num for num in nums if num > 0]
        negative_nums = [num for num in nums if num < 0]
        
        # If there are no positive numbers and at most one negative number, we must pick the largest (least negative) number
        if not positive_nums and len(negative_nums) <= 1:
            return max(nums)
        
        # Sort negative numbers to pick the largest (least negative) ones
        negative_nums.sort()
        
        # If the number of negative numbers is odd, we can only take the largest even count of them
        if len(negative_nums) % 2 != 0:
            negative_nums.pop()  # Remove the smallest (most negative) number
        
        max_strength = 1
        for num in positive_nums + negative_nums:
            max_strength *= num
        
        return max_strength

def maxStrength(nums: List[int]) -> int:
    return Solution().maxStrength(nums)