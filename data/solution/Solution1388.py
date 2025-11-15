import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def solve(sub_slices):
            n = len(sub_slices)
            take = (n + 1) // 3
            dp = [[0] * (take + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, take + 1):
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i > 1 else 0) + sub_slices[i - 1])
            return dp[n][take]
        
        # We have two cases to consider:
        # 1. We take the first slice, so we cannot take the last slice.
        # 2. We do not take the first slice, so we can take the last slice.
        return max(solve(slices[:-1]), solve(slices[1:]))

def maxSizeSlices(slices: List[int]) -> int:
    return Solution().maxSizeSlices(slices)