import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # Initialize the DP table
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Calculate the dot product for the current pair of elements
                current_product = nums1[i - 1] * nums2[j - 1]
                
                # Update the DP table entry for dp[i][j]
                dp[i][j] = max(
                    current_product,  # Start a new subsequence with nums1[i-1] and nums2[j-1]
                    current_product + dp[i - 1][j - 1],  # Extend the previous subsequence
                    dp[i - 1][j],  # Skip the current element of nums1
                    dp[i][j - 1]   # Skip the current element of nums2
                )
        
        # The result is the maximum dot product of any non-empty subsequences
        return dp[m][n]

def maxDotProduct(nums1: List[int], nums2: List[int]) -> int:
    return Solution().maxDotProduct(nums1, nums2)