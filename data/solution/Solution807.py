import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # Determine the skyline from the top/bottom (i.e., the maximum values of each column)
        max_col_heights = [max(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))]
        
        # Determine the skyline from the left/right (i.e., the maximum values of each row)
        max_row_heights = [max(grid[r]) for r in range(len(grid))]
        
        total_increase = 0
        
        # Iterate through each cell in the grid and calculate the potential increase
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # The new height cannot exceed the minimum of the row and column skylines
                new_height = min(max_col_heights[c], max_row_heights[r])
                # Add the difference to the total increase
                total_increase += new_height - grid[r][c]
        
        return total_increase

def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    return Solution().maxIncreaseKeepingSkyline(grid)