import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # If the total number of cells is odd, we cannot have an equal number of 0's and 1's
        if (m + n - 1) % 2 != 0:
            return False
        
        # Use a set to keep track of possible differences between the number of 1's and 0's
        # (1's - 0's) at each cell
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0] * 2 - 1)  # Start with the top-left cell
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                current_dp = set()
                if i > 0:
                    for diff in dp[j]:
                        current_dp.add(diff + grid[i][j] * 2 - 1)
                if j > 0:
                    for diff in dp[j-1]:
                        current_dp.add(diff + grid[i][j] * 2 - 1)
                dp[j] = current_dp
        
        # Check if there is a path with an equal number of 0's and 1's
        return 0 in dp[n-1]

def isThereAPath(grid: List[List[int]]) -> bool:
    return Solution().isThereAPath(grid)