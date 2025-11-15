import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1 to both ends of nums to handle edge cases
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] will store the maximum coins obtained by bursting all the balloons between i and j
        dp = [[0] * n for _ in range(n)]
        
        # We will solve this problem by considering all possible lengths of subarrays
        for length in range(2, n):  # length is at least 2 because we added 1 to both ends
            for i in range(n - length):
                j = i + length
                # Now, consider each balloon between i and j as the last balloon to burst
                for k in range(i + 1, j):
                    # Calculate coins obtained by bursting the k-th balloon last
                    coins = nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    # Update dp[i][j] to be the maximum coins obtained
                    dp[i][j] = max(dp[i][j], coins)
        
        # The result is the maximum coins obtained by bursting all the balloons between the two added 1s
        return dp[0][n - 1]

def maxCoins(nums: List[int]) -> int:
    return Solution().maxCoins(nums)