import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # Sort the array to easily find min and max
        nums.sort()
        averages = set()
        
        # Use two pointers to find min and max
        left, right = 0, len(nums) - 1
        
        while left < right:
            # Calculate the average of the current min and max
            average = (nums[left] + nums[right]) / 2
            # Add the average to the set of averages
            averages.add(average)
            # Move the pointers inward
            left += 1
            right -= 1
        
        # The number of distinct averages is the size of the set
        return len(averages)

def distinctAverages(nums: List[int]) -> int:
    return Solution().distinctAverages(nums)