import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Helper function to rob a linear sequence of houses
        def rob_linear(houses: List[int]) -> int:
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            prev1, prev2 = 0, 0
            for amount in houses:
                current = max(prev2 + amount, prev1)
                prev2 = prev1
                prev1 = current
            return prev1
        
        # Rob houses excluding the last one or excluding the first one
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

def rob(nums: List[int]) -> int:
    return Solution().rob(nums)