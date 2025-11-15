import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ways = 0
        
        # Check if no student is selected
        if nums[0] > 0:
            ways += 1
        
        # Check for each possible number of selected students
        for i in range(n):
            # If selecting i+1 students makes them happy
            if (i + 1 > nums[i] and (i == n - 1 or i + 1 < nums[i + 1])):
                ways += 1
        
        return ways

def countWays(nums: List[int]) -> int:
    return Solution().countWays(nums)