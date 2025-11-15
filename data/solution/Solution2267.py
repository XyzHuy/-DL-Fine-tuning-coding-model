import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # If the total number of cells is odd, it's impossible to have a valid path
        if (m + n) % 2 == 0:
            return False
        
        # Initialize a 3D DP array to keep track of possible balances
        dp = [[set() for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1].add(1 if grid[0][0] == '(' else -1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                current = 1 if grid[i-1][j-1] == '(' else -1
                for balance in dp[i-1][j]:
                    if balance + current >= 0:
                        dp[i][j].add(balance + current)
                for balance in dp[i][j-1]:
                    if balance + current >= 0:
                        dp[i][j].add(balance + current)
        
        # Check if we can end with a balance of 0 at the bottom-right corner
        return 0 in dp[m][n]

def hasValidPath(grid: List[List[str]]) -> bool:
    return Solution().hasValidPath(grid)