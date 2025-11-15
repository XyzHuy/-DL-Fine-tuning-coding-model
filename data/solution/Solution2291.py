import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        # Calculate the profit for each stock if bought today
        profits = [(future[i] - present[i], present[i]) for i in range(len(present)) if future[i] > present[i]]
        
        # Sort the stocks by their present price
        profits.sort(key=lambda x: x[1])
        
        # Initialize a DP array where dp[b] is the maximum profit with budget b
        dp = [0] * (budget + 1)
        
        # Iterate over each stock
        for profit, cost in profits:
            # Update the dp array from right to left to avoid using the same stock multiple times
            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b - cost] + profit)
        
        # The maximum profit will be in dp[budget]
        return dp[budget]

def maximumProfit(present: List[int], future: List[int], budget: int) -> int:
    return Solution().maximumProfit(present, future, budget)