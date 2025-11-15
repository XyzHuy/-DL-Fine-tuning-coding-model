import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j] will store the minimum score to triangulate the polygon from vertex i to vertex j
        dp = [[0] * n for _ in range(n)]
        
        # Fill the dp table
        for length in range(2, n):  # length is the distance between i and j
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    # The score of the triangle (i, k, j) plus the minimum score of the two resulting polygons
                    dp[i][j] = min(dp[i][j], values[i] * values[k] * values[j] + dp[i][k] + dp[k][j])
        
        return dp[0][n - 1]

def minScoreTriangulation(values: List[int]) -> int:
    return Solution().minScoreTriangulation(values)