import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = {}
        
        # Count the occurrences of each row
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1
        
        count = 0
        
        # Check each column against the row counts
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            if col_tuple in row_count:
                count += row_count[col_tuple]
        
        return count

def equalPairs(grid: List[List[int]]) -> int:
    return Solution().equalPairs(grid)