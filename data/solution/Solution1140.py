import random
import functools
import collections
import string
import math
import datetime


from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Compute the suffix sums of the piles array
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        @lru_cache(None)
        def dp(i, m):
            # If we have taken all piles, return 0
            if i == n:
                return 0
            # If the remaining piles can be taken in one move, take all
            if i + 2 * m >= n:
                return suffix_sum[i]
            # Calculate the maximum stones Alice can get
            max_stones = 0
            for x in range(1, 2 * m + 1):
                max_stones = max(max_stones, suffix_sum[i] - dp(i + x, max(m, x)))
            return max_stones
        
        return dp(0, 1)

def stoneGameII(piles: List[int]) -> int:
    return Solution().stoneGameII(piles)