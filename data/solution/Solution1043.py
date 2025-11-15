import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # dp[i] will be the maximum sum we can have considering arr[0:i]
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            current_max = 0
            # Try all possible subarrays ending at i with length 1 to k
            for j in range(1, min(k, i) + 1):
                current_max = max(current_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + current_max * j)
        
        return dp[n]

def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    return Solution().maxSumAfterPartitioning(arr, k)