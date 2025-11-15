import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Initialize the closest number with the first element of the array
        closest = nums[0]
        
        for num in nums:
            # Check if the current number is closer to 0 than the closest found so far
            if abs(num) < abs(closest):
                closest = num
            # If the current number is equally close, choose the larger one
            elif abs(num) == abs(closest) and num > closest:
                closest = num
        
        return closest

def findClosestNumber(nums: List[int]) -> int:
    return Solution().findClosestNumber(nums)