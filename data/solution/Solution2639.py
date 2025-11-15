import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # Transpose the grid to iterate over columns
        transposed_grid = zip(*grid)
        
        # For each column, find the maximum length of the integers when converted to strings
        column_widths = [max(len(str(num)) for num in column) for column in transposed_grid]
        
        return column_widths

def findColumnWidth(grid: List[List[int]]) -> List[int]:
    return Solution().findColumnWidth(grid)