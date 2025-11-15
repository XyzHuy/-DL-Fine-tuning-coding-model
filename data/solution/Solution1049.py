import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        n = len(stones)
        target = total_sum // 2
        
        # Create a DP array to store the possible sums we can achieve
        dp = [False] * (target + 1)
        dp[0] = True
        
        for stone in stones:
            # Traverse backwards to avoid using the same stone multiple times
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]
        
        # Find the largest possible sum less than or equal to target
        for j in range(target, -1, -1):
            if dp[j]:
                return total_sum - 2 * j

def lastStoneWeightII(stones: List[int]) -> int:
    return Solution().lastStoneWeightII(stones)