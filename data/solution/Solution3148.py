import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Initialize the dp table with infinity
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                dp[i][j] = min(dp[i][j], grid[i][j])
        
        max_score = float('-inf')
        for i in range(m):
            for j in range(n):
                if i > 0:
                    max_score = max(max_score, grid[i][j] - dp[i-1][j])
                if j > 0:
                    max_score = max(max_score, grid[i][j] - dp[i][j-1])
        
        return max_score

def maxScore(grid: List[List[int]]) -> int:
    return Solution().maxScore(grid)