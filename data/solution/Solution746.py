import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # We will use dynamic programming to solve this problem.
        # Let dp[i] be the minimum cost to reach step i.
        # To reach step i, we could have either come from step i-1 or step i-2.
        # Therefore, dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        # We need to find the minimum cost to reach the top, which is either step n or step n-1.
        
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        
        # Initialize the first two steps
        dp = [0] * (n + 1)
        
        # Fill the dp array
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        # The answer will be the minimum cost to reach either step n-1 or step n
        return dp[n]

def minCostClimbingStairs(cost: List[int]) -> int:
    return Solution().minCostClimbingStairs(cost)