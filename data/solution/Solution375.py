import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # Create a 2D list dp with dimensions (n+1) x (n+1) initialized to 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Fill the dp table for all ranges [i, j]
        for length in range(2, n + 1):  # length of the range
            for i in range(1, n - length + 2):  # start of the range
                j = i + length - 1  # end of the range
                dp[i][j] = float('inf')  # Initialize to infinity
                for k in range(i, j + 1):  # possible guesses
                    cost = k + max(dp[i][k - 1] if k > i else 0, dp[k + 1][j] if k < j else 0)
                    dp[i][j] = min(dp[i][j], cost)
        
        # The result is the minimum amount of money required to guarantee a win for the range [1, n]
        return dp[1][n]

def getMoneyAmount(n: int) -> int:
    return Solution().getMoneyAmount(n)