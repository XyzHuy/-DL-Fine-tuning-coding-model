import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # Create a 2D DP array to store the maximum number of uncrossed lines
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The answer is in the bottom-right cell of the DP array
        return dp[m][n]

def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    return Solution().maxUncrossedLines(nums1, nums2)