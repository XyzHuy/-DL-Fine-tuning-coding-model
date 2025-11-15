import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        # Pair up elements from nums1 and nums2
        pairs = sorted(zip(nums1, nums2), key=lambda p: p[1])
        
        # dp[k] will be the maximum sum of nums1 we can make zero in k operations
        dp = [0] * (n + 1)
        
        for i in range(n):
            # Traverse dp array in reverse to avoid overwriting results from the same iteration
            for k in range(n, 0, -1):
                dp[k] = max(dp[k], dp[k - 1] + pairs[i][0] + k * pairs[i][1])
        
        # Calculate total sum of nums1 and nums2
        total_sum_1 = sum(nums1)
        total_sum_2 = sum(nums2)
        
        # Check for each possible number of operations
        for k in range(n + 1):
            if total_sum_1 + k * total_sum_2 - dp[k] <= x:
                return k
        
        return -1

def minimumTime(nums1: List[int], nums2: List[int], x: int) -> int:
    return Solution().minimumTime(nums1, nums2, x)