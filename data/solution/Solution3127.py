import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        # Check all possible 2x2 squares in the 3x3 grid
        for i in range(2):
            for j in range(2):
                # Count the number of 'B' and 'W' in the current 2x2 square
                count_B = 0
                count_W = 0
                for x in range(i, i + 2):
                    for y in range(j, j + 2):
                        if grid[x][y] == 'B':
                            count_B += 1
                        else:
                            count_W += 1
                # If the current 2x2 square has 3 or more of the same color,
                # we can change one cell to make it a 2x2 square of the same color
                if count_B >= 3 or count_W >= 3:
                    return True
        # If no such 2x2 square is found, return False
        return False

def canMakeSquare(grid: List[List[str]]) -> bool:
    return Solution().canMakeSquare(grid)