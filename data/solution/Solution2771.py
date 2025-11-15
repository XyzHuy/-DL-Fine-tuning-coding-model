import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # dp[i][0] means the length of the longest non-decreasing subarray ending at index i with nums1[i]
        # dp[i][1] means the length of the longest non-decreasing subarray ending at index i with nums2[i]
        dp = [[1, 1] for _ in range(n)]
        
        for i in range(1, n):
            if nums1[i] >= nums1[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] + 1)
            if nums1[i] >= nums2[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)
            
            if nums2[i] >= nums1[i - 1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)
            if nums2[i] >= nums2[i - 1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)
        
        return max(max(row) for row in dp)

def maxNonDecreasingLength(nums1: List[int], nums2: List[int]) -> int:
    return Solution().maxNonDecreasingLength(nums1, nums2)