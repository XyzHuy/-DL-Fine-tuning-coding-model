import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # Initialize the dp array with 0s
        dp = [0] * (k + 1)
        
        for pile in piles:
            # Create a prefix sum array for the current pile
            prefix_sums = [0]
            for coin in pile:
                prefix_sums.append(prefix_sums[-1] + coin)
            
            # Update the dp array in reverse order
            for i in range(k, -1, -1):
                for take in range(1, min(i, len(pile)) + 1):
                    dp[i] = max(dp[i], dp[i - take] + prefix_sums[take])
        
        return dp[k]

def maxValueOfCoins(piles: List[List[int]], k: int) -> int:
    return Solution().maxValueOfCoins(piles, k)