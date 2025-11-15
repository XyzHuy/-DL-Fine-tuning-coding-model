import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Iterate over all pairs of rows
        for i in range(m):
            for j in range(i + 1, m):
                # Count the number of columns with 1s in both rows i and j
                common_ones = 0
                for k in range(n):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        common_ones += 1
                
                # If there are at least two common 1s, we can form rectangles
                if common_ones >= 2:
                    # Number of ways to choose 2 columns out of common_ones
                    count += (common_ones * (common_ones - 1)) // 2
        
        return count

def countCornerRectangles(grid: List[List[int]]) -> int:
    return Solution().countCornerRectangles(grid)