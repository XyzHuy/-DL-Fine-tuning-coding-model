import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)
        
        # Initialize the DP table with infinity
        dp = [[math.inf] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0  # No cost for 0 subarrays and 0 elements
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                current_and = nums[j - 1]
                for k in range(j, 0, -1):
                    current_and &= nums[k - 1]
                    if current_and == andValues[i - 1]:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + nums[j - 1])
        
        return dp[m][n] if dp[m][n] != math.inf else -1

def minimumValueSum(nums: List[int], andValues: List[int]) -> int:
    return Solution().minimumValueSum(nums, andValues)