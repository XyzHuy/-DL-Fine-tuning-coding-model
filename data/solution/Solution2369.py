import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty array is trivially partitionable

        for i in range(2, n + 1):
            # Check for the condition of two equal elements
            if i >= 2 and nums[i - 1] == nums[i - 2]:
                dp[i] = dp[i] or dp[i - 2]
            
            # Check for the condition of three equal elements
            if i >= 3 and nums[i - 1] == nums[i - 2] == nums[i - 3]:
                dp[i] = dp[i] or dp[i - 3]
            
            # Check for the condition of three consecutive increasing elements
            if i >= 3 and nums[i - 1] - nums[i - 2] == 1 and nums[i - 2] - nums[i - 3] == 1:
                dp[i] = dp[i] or dp[i - 3]

        return dp[n]

def validPartition(nums: List[int]) -> bool:
    return Solution().validPartition(nums)