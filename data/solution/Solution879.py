import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        G = len(group)
        
        # dp[i][j][k] means the number of ways to achieve exactly j profit using the first i crimes with at most k members
        dp = [[[0] * (n + 1) for _ in range(minProfit + 1)] for _ in range(G + 1)]
        
        # Base case: one way to achieve 0 profit with 0 members and 0 crimes
        for i in range(G + 1):
            dp[i][0][0] = 1
        
        for i in range(1, G + 1):
            g = group[i - 1]
            p = profit[i - 1]
            for j in range(minProfit + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]  # Not taking the ith crime
                    if k >= g:
                        dp[i][j][k] += dp[i - 1][max(0, j - p)][k - g]  # Taking the ith crime
                        dp[i][j][k] %= MOD
        
        # Sum up all ways to achieve at least minProfit with any number of members
        result = sum(dp[G][minProfit][k] for k in range(n + 1)) % MOD
        return result

def profitableSchemes(n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    return Solution().profitableSchemes(n, minProfit, group, profit)