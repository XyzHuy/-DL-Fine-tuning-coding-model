import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Initialize dp array to store the maximum sum with remainder 0, 1, 2
        dp = [0, 0, 0]
        
        for num in nums:
            # For each number, calculate the new sums with the current number added
            for i in dp[:]:  # Use a copy of dp to avoid using updated values in the same iteration
                dp[(i + num) % 3] = max(dp[(i + num) % 3], i + num)
        
        # The result is the maximum sum with remainder 0
        return dp[0]

def maxSumDivThree(nums: List[int]) -> int:
    return Solution().maxSumDivThree(nums)