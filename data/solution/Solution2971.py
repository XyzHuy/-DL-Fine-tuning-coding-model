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
        
        # Initialize the sum of the first two smallest sides
        current_sum = nums[0] + nums[1]
        largest_perimeter = -1
        
        # Iterate from the third element to the end
        for i in range(2, len(nums)):
            # Check if the current element can form a polygon with the previous elements
            if current_sum > nums[i]:
                # Update the largest perimeter found
                largest_perimeter = current_sum + nums[i]
            # Add the current element to the sum of the previous elements
            current_sum += nums[i]
        
        return largest_perimeter

def largestPerimeter(nums: List[int]) -> int:
    return Solution().largestPerimeter(nums)