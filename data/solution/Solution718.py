import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Create a 2D DP array to store lengths of longest common suffixes
        # Initialize all values to 0
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        
        # Variable to store the length of the longest common subarray
        max_length = 0
        
        # Build the dp array
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return max_length

def findLength(nums1: List[int], nums2: List[int]) -> int:
    return Solution().findLength(nums1, nums2)