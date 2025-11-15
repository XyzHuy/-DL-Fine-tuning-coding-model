import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        max_kills = 0
        
        # Create a 3D array to store the number of enemies killed in each direction
        # dp[i][j][0] -> left, dp[i][j][1] -> right, dp[i][j][2] -> up, dp[i][j][3] -> down
        dp = [[[0] * 4 for _ in range(n)] for _ in range(m)]
        
        # Fill the dp array for left and up directions
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'W':
                    if j > 0:
                        dp[i][j][0] = dp[i][j-1][0] + (1 if grid[i][j-1] == 'E' else 0)
                    if i > 0:
                        dp[i][j][2] = dp[i-1][j][2] + (1 if grid[i-1][j] == 'E' else 0)
        
        # Fill the dp array for right and down directions and calculate the maximum kills
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] != 'W':
                    if j < n - 1:
                        dp[i][j][1] = dp[i][j+1][1] + (1 if grid[i][j+1] == 'E' else 0)
                    if i < m - 1:
                        dp[i][j][3] = dp[i+1][j][3] + (1 if grid[i+1][j] == 'E' else 0)
                
                if grid[i][j] == '0':
                    max_kills = max(max_kills, sum(dp[i][j]))
        
        return max_kills

def maxKilledEnemies(grid: List[List[str]]) -> int:
    return Solution().maxKilledEnemies(grid)