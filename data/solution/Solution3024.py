import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Sort the sides to simplify the triangle inequality checks
        nums.sort()
        
        # Check if the sides can form a triangle
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        # Check the type of triangle
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        else:
            return "scalene"

def triangleType(nums: List[int]) -> str:
    return Solution().triangleType(nums)