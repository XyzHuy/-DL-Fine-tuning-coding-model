import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        # dp[i][j] will store the probability of getting j heads with the first i coins
        dp = [[0.0] * (target + 1) for _ in range(n + 1)]
        
        # Base case: there's 1 way to get 0 heads with 0 coins
        dp[0][0] = 1.0
        
        for i in range(1, n + 1):
            # If we have i coins and we want 0 heads, the probability is the product of the tails probabilities
            dp[i][0] = dp[i - 1][0] * (1 - prob[i - 1])
            
            for j in range(1, min(i, target) + 1):
                # dp[i][j] can be obtained by:
                # 1. Getting j-1 heads with the first i-1 coins and then getting a head with the i-th coin
                # 2. Getting j heads with the first i-1 coins and then getting a tail with the i-th coin
                dp[i][j] = dp[i - 1][j - 1] * prob[i - 1] + dp[i - 1][j] * (1 - prob[i - 1])
        
        return dp[n][target]

def probabilityOfHeads(prob: List[float], target: int) -> float:
    return Solution().probabilityOfHeads(prob, target)