import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = 0  # No score at the last element as we stop there

        for i in range(n - 2, -1, -1):
            max_score = 0
            for j in range(i + 1, n):
                max_score = max(max_score, (j - i) * nums[j] + dp[j])
            dp[i] = max_score

        return dp[0]

def maxScore(nums: List[int]) -> int:
    return Solution().maxScore(nums)