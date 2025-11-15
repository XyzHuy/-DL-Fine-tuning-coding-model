import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def solve(grid_tuple):
            grid = [list(row) for row in grid_tuple]
            has_one = False
            min_operations = float('inf')
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        has_one = True
                        # Perform the operation: clear row i and column j
                        new_grid = [[grid[x][y] if x != i and y != j else 0 for y in range(n)] for x in range(m)]
                        operations = 1 + solve(tuple(tuple(row) for row in new_grid))
                        min_operations = min(min_operations, operations)
            
            if not has_one:
                return 0
            
            return min_operations
        
        return solve(tuple(tuple(row) for row in grid))

def removeOnes(grid: List[List[int]]) -> int:
    return Solution().removeOnes(grid)