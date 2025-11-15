import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        
        for num in nums:
            next_dp = {}
            for s in dp:
                next_dp[s + num] = next_dp.get(s + num, 0) + dp[s]
                next_dp[s - num] = next_dp.get(s - num, 0) + dp[s]
            dp = next_dp
        
        return dp.get(target, 0)

def findTargetSumWays(nums: List[int], target: int) -> int:
    return Solution().findTargetSumWays(nums, target)