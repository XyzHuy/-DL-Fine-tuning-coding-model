import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        while grid[0]:  # Continue until all columns are removed
            max_values = []
            for row in grid:
                max_value = max(row)
                row.remove(max_value)
                max_values.append(max_value)
            total += max(max_values)
        return total

def deleteGreatestValue(grid: List[List[int]]) -> int:
    return Solution().deleteGreatestValue(grid)