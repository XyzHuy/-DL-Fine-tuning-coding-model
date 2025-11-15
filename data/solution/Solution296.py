import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Collect row and column indices of all homes
        rows = [i for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
        cols = [j for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == 1]
        
        # Function to calculate minimum distance for a given sorted list of coordinates
        def min_distance(points):
            return sum(abs(points[i] - points[len(points) // 2]) for i in range(len(points)))
        
        # Calculate the minimum total distance using the median
        return min_distance(rows) + min_distance(cols)

def minTotalDistance(grid: List[List[int]]) -> int:
    return Solution().minTotalDistance(grid)