import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Check for right triangles with grid[r][c] as the right angle
                    # Look for 1s in the same row to the right of grid[r][c]
                    for c2 in range(c + 1, cols):
                        if grid[r][c2] == 1:
                            # Look for 1s in the same column below grid[r][c]
                            for r2 in range(r + 1, rows):
                                if grid[r2][c] == 1:
                                    count += 1
                            # Look for 1s in the same column above grid[r][c]
                            for r2 in range(r - 1, -1, -1):
                                if grid[r2][c] == 1:
                                    count += 1
                    # Look for 1s in the same row to the left of grid[r][c]
                    for c2 in range(c - 1, -1, -1):
                        if grid[r][c2] == 1:
                            # Look for 1s in the same column below grid[r][c]
                            for r2 in range(r + 1, rows):
                                if grid[r2][c] == 1:
                                    count += 1
                            # Look for 1s in the same column above grid[r][c]
                            for r2 in range(r - 1, -1, -1):
                                if grid[r2][c] == 1:
                                    count += 1
        return count

def numberOfRightTriangles(grid: List[List[int]]) -> int:
    return Solution().numberOfRightTriangles(grid)