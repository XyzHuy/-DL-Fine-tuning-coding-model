import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        k = k % total_elements  # To handle cases where k is greater than total number of elements
        
        if k == 0:
            return grid
        
        # Flatten the grid into a 1D list
        flat_grid = [grid[i][j] for i in range(m) for j in range(n)]
        
        # Perform the shift operation
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        
        # Convert the flattened list back to a 2D grid
        for i in range(m):
            for j in range(n):
                grid[i][j] = flat_grid[i * n + j]
        
        return grid

def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    return Solution().shiftGrid(grid, k)