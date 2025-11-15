import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Flatten the grid and sort by value
        flat_grid = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        flat_grid.sort()
        
        # Initialize row and column max arrays
        row_max = [0] * m
        col_max = [0] * n
        
        # Resultant grid
        result = [[0] * n for _ in range(m)]
        
        # Assign values
        for value, i, j in flat_grid:
            # The new value should be greater than the max in the current row and column
            new_value = max(row_max[i], col_max[j]) + 1
            result[i][j] = new_value
            # Update the row and column max
            row_max[i] = new_value
            col_max[j] = new_value
        
        return result

def minScore(grid: List[List[int]]) -> List[List[int]]:
    return Solution().minScore(grid)