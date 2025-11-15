import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prefix_sum = [[0] * n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prefix_sum[i][j] = grid[i][j]
                elif i == 0:
                    prefix_sum[i][j] = grid[i][j] + prefix_sum[i][j-1]
                elif j == 0:
                    prefix_sum[i][j] = grid[i][j] + prefix_sum[i-1][j]
                else:
                    prefix_sum[i][j] = grid[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
                
                if prefix_sum[i][j] <= k:
                    count += 1
        
        return count

def countSubmatrices(grid: List[List[int]], k: int) -> int:
    return Solution().countSubmatrices(grid, k)