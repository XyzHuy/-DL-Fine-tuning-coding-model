import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # Create a dictionary to store the prices for given dimensions
        price_dict = {}
        for h, w, p in prices:
            price_dict[(h, w)] = p
        
        # Create a DP table to store the maximum money that can be earned for each dimension
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for h in range(1, m + 1):
            for w in range(1, n + 1):
                # Start with the price of the whole piece if it's available
                dp[h][w] = price_dict.get((h, w), 0)
                
                # Try all possible horizontal cuts
                for i in range(1, h):
                    dp[h][w] = max(dp[h][w], dp[i][w] + dp[h - i][w])
                
                # Try all possible vertical cuts
                for j in range(1, w):
                    dp[h][w] = max(dp[h][w], dp[h][j] + dp[h][w - j])
        
        # The answer will be in dp[m][n]
        return dp[m][n]

def sellingWood(m: int, n: int, prices: List[List[int]]) -> int:
    return Solution().sellingWood(m, n, prices)