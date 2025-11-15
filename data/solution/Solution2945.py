import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        # dp[i] will store a tuple (length, prefix_sum)
        # where length is the length of the longest non-decreasing subarray ending at i
        # and prefix_sum is the sum of that subarray
        dp = [(1, nums[0]) for _ in range(n)]
        
        for i in range(1, n):
            max_len = 1
            prefix_sum = nums[i]
            
            # Check all previous subarrays ending at j that can be extended by nums[i]
            for j in range(i - 1, -1, -1):
                if dp[j][1] <= prefix_sum:
                    max_len = max(max_len, dp[j][0] + 1)
                    break
                else:
                    prefix_sum += nums[j]
            
            dp[i] = (max_len, prefix_sum)
        
        # The answer is the maximum length of any non-decreasing subarray
        return max(length for length, _ in dp)

def findMaximumLength(nums: List[int]) -> int:
    return Solution().findMaximumLength(nums)