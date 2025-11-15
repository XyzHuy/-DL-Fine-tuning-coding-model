import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize the dp array with zeros
        dp = [0] * (target + 1)
        # There is one way to make the sum 0, which is by choosing no elements
        dp[0] = 1
        
        # Fill the dp array
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]

def combinationSum4(nums: List[int], target: int) -> int:
    return Solution().combinationSum4(nums, target)