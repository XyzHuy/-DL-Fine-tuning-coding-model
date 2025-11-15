import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = [0] * (n + 1)
        
        # Calculate prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        # dp[i][j] will be the maximum difference Alice can achieve over Bob
        # when playing optimally with stones[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Fill the dp table
        for length in range(2, n + 1):  # length of the subarray
            for i in range(n - length + 1):
                j = i + length - 1
                # Alice can choose to take the leftmost or rightmost stone
                take_left = prefix_sum[j + 1] - prefix_sum[i + 1] - dp[i + 1][j]
                take_right = prefix_sum[j] - prefix_sum[i] - dp[i][j - 1]
                dp[i][j] = max(take_left, take_right)
        
        return dp[0][n - 1]

def stoneGameVII(stones: List[int]) -> int:
    return Solution().stoneGameVII(stones)