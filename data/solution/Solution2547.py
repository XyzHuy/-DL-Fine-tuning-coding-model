import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            count = [0] * (n + 1)
            trim_length = 0
            
            for j in range(i, 0, -1):
                count[nums[j - 1]] += 1
                
                if count[nums[j - 1]] == 2:
                    trim_length += 2
                elif count[nums[j - 1]] > 2:
                    trim_length += 1
                
                dp[i] = min(dp[i], dp[j - 1] + k + trim_length)
        
        return dp[n]

def minCost(nums: List[int], k: int) -> int:
    return Solution().minCost(nums, k)