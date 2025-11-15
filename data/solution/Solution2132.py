import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Create a prefix sum grid for the original grid
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix_sum[i + 1][j + 1] = grid[i][j] + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]
        
        # Create a grid to mark where stamps can be placed
        stamp_grid = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill stamp_grid with 1 if a stamp can be placed starting at (i, j)
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                # Calculate the sum of the submatrix grid[i:i+stampHeight][j:j+stampWidth]
                if prefix_sum[i + stampHeight][j + stampWidth] - prefix_sum[i][j + stampWidth] - prefix_sum[i + stampHeight][j] + prefix_sum[i][j] == 0:
                    stamp_grid[i][j] = 1
        
        # Create a prefix sum grid for the stamp_grid
        stamp_prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                stamp_prefix_sum[i + 1][j + 1] = stamp_grid[i][j] + stamp_prefix_sum[i][j + 1] + stamp_prefix_sum[i + 1][j] - stamp_prefix_sum[i][j]
        
        # Check if every empty cell is covered by at least one stamp
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # Check if there is a stamp covering the cell (i, j)
                    # We need to check the submatrix stamp_grid[i-stampHeight+1:i+1][j-stampWidth+1:j+1]
                    top = max(0, i - stampHeight + 1)
                    left = max(0, j - stampWidth + 1)
                    if stamp_prefix_sum[i + 1][j + 1] - stamp_prefix_sum[i + 1][left] - stamp_prefix_sum[top][j + 1] + stamp_prefix_sum[top][left] == 0:
                        return False
        
        return True

def possibleToStamp(grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
    return Solution().possibleToStamp(grid, stampHeight, stampWidth)