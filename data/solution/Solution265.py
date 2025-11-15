import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n = len(costs)
        k = len(costs[0])
        
        # Initialize the dp array with the first house's costs
        dp = costs[0][:]
        
        for i in range(1, n):
            # Find the two minimum costs from the previous house
            min1 = min2 = float('inf')
            min1_idx = -1
            for j in range(k):
                if dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                    min1_idx = j
                elif dp[j] < min2:
                    min2 = dp[j]
            
            # Update the dp array for the current house
            for j in range(k):
                if j == min1_idx:
                    dp[j] = costs[i][j] + min2
                else:
                    dp[j] = costs[i][j] + min1
        
        # The minimum cost to paint all houses is the minimum value in the last dp array
        return min(dp)

def minCostII(costs: List[List[int]]) -> int:
    return Solution().minCostII(costs)