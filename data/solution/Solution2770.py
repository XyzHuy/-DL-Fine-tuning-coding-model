import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Initialize a dp array where dp[i] represents the maximum number of jumps to reach index i
        dp = [-1] * n
        dp[0] = 0  # Starting point requires 0 jumps

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if -target <= diff <= target and dp[j] != -1:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n - 1]

def maximumJumps(nums: List[int], target: int) -> int:
    return Solution().maximumJumps(nums, target)