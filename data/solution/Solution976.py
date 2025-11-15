import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in non-decreasing order
        nums.sort()
        
        # Iterate from the end to the beginning to find the largest perimeter
        for i in range(len(nums) - 1, 1, -1):
            # Check the triangle inequality theorem
            if nums[i] < nums[i - 1] + nums[i - 2]:
                # If the condition is satisfied, return the perimeter
                return nums[i] + nums[i - 1] + nums[i - 2]
        
        # If no valid triangle is found, return 0
        return 0

def largestPerimeter(nums: List[int]) -> int:
    return Solution().largestPerimeter(nums)