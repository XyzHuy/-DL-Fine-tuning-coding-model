import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # Create a 2D list to store the minimum health needed at each cell
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = 1 if min_health_on_exit <= 0 else min_health_on_exit
        
        return dp[0][0]

def calculateMinimumHP(dungeon: List[List[int]]) -> int:
    return Solution().calculateMinimumHP(dungeon)