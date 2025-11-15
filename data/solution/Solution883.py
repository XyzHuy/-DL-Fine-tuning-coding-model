import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Top view: count all non-zero cells
        top_view = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        
        # Front view: sum of the maximum values of each row
        front_view = sum(max(row) for row in grid)
        
        # Side view: sum of the maximum values of each column
        side_view = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        
        # Total projection area
        return top_view + front_view + side_view

def projectionArea(grid: List[List[int]]) -> int:
    return Solution().projectionArea(grid)