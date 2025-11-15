import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Precompute the cost of setting the array size to be the maximum of nums[l:r+1] for all l, r
        cost = [[0] * n for _ in range(n)]
        for l in range(n):
            total = 0
            m = 0
            for r in range(l, n):
                total += nums[r]
                m = max(m, nums[r])
                cost[l][r] = m * (r - l + 1) - total
        
        # dp[i][j] will be the minimum space wasted to accommodate nums[0:i+1] with j resizes
        dp = [[math.inf] * (k + 1) for _ in range(n)]
        
        # Initialize the dp array for 0 resizes
        for i in range(n):
            dp[i][0] = cost[0][i]
        
        # Fill the dp array
        for j in range(1, k + 1):
            for i in range(j, n):
                for l in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[l][j - 1] + cost[l + 1][i])
        
        return dp[n - 1][k]

def minSpaceWastedKResizing(nums: List[int], k: int) -> int:
    return Solution().minSpaceWastedKResizing(nums, k)