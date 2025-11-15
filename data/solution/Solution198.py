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
        
        # Initialize the dp array
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill the dp array
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # The last element of dp array will have the result
        return dp[-1]

def rob(nums: List[int]) -> int:
    return Solution().rob(nums)