import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        # We have four possible scenarios:
        # 1. Remove the 3 largest elements
        # 2. Remove the 2 largest elements and the smallest element
        # 3. Remove the largest element and the 2 smallest elements
        # 4. Remove the 3 smallest elements
        
        # Calculate the difference for each scenario
        diff1 = nums[-1] - nums[3]
        diff2 = nums[-2] - nums[2]
        diff3 = nums[-3] - nums[1]
        diff4 = nums[-4] - nums[0]
        
        # Return the minimum difference
        return min(diff1, diff2, diff3, diff4)

def minDifference(nums: List[int]) -> int:
    return Solution().minDifference(nums)