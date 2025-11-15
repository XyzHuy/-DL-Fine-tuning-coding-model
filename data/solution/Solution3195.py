import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        top, bottom, left, right = float('inf'), float('-inf'), float('inf'), float('-inf')
        
        # Find the bounding rectangle coordinates
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)
        
        # Calculate the area of the bounding rectangle
        height = bottom - top + 1
        width = right - left + 1
        return height * width

def minimumArea(grid: List[List[int]]) -> int:
    return Solution().minimumArea(grid)