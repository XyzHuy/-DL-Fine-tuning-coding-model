import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top_row = grid[0]
        bottom_row = grid[1]
        
        # Compute the prefix sum for the top row
        top_prefix_sum = [0] * n
        top_prefix_sum[0] = top_row[0]
        for i in range(1, n):
            top_prefix_sum[i] = top_prefix_sum[i - 1] + top_row[i]
        
        # Compute the suffix sum for the bottom row
        bottom_suffix_sum = [0] * n
        bottom_suffix_sum[n - 1] = bottom_row[n - 1]
        for i in range(n - 2, -1, -1):
            bottom_suffix_sum[i] = bottom_suffix_sum[i + 1] + bottom_row[i]
        
        # Calculate the minimum of the maximum points the second robot can collect
        min_max_points = float('inf')
        for i in range(n):
            top_points = top_prefix_sum[n - 1] - top_prefix_sum[i] if i < n - 1 else 0
            bottom_points = bottom_suffix_sum[0] - bottom_suffix_sum[i] if i > 0 else 0
            max_points_second_robot = max(top_points, bottom_points)
            min_max_points = min(min_max_points, max_points_second_robot)
        
        return min_max_points

def gridGame(grid: List[List[int]]) -> int:
    return Solution().gridGame(grid)