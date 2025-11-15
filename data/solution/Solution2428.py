import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        rows, cols = len(grid), len(grid[0])
        
        # Iterate over each possible starting point of an hourglass
        for i in range(rows - 2):
            for j in range(cols - 2):
                # Calculate the sum of the current hourglass
                current_sum = (grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                               grid[i+1][j+1] +
                               grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2])
                # Update max_sum if the current_sum is greater
                max_sum = max(max_sum, current_sum)
        
        return max_sum

def maxSum(grid: List[List[int]]) -> int:
    return Solution().maxSum(grid)