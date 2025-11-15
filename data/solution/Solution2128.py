import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        # Check if the grid is empty
        if not grid or not grid[0]:
            return True
        
        # Get the first row
        first_row = grid[0]
        
        # Iterate over the rest of the rows
        for row in grid[1:]:
            # Check if the current row is either the same as the first row
            # or the inverted version of the first row
            if row != first_row and row != [1 - val for val in first_row]:
                return False
        
        return True

def removeOnes(grid: List[List[int]]) -> bool:
    return Solution().removeOnes(grid)