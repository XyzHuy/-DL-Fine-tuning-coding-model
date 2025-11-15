import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def count_factors(x, factor):
            count = 0
            while x % factor == 0:
                x //= factor
                count += 1
            return count
        
        m, n = len(grid), len(grid[0])
        # Prefix sums for factors of 2 and 5
        twos = [[0] * (n + 1) for _ in range(m + 1)]
        fives = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill prefix sums
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                twos[i][j] = twos[i][j - 1] + count_factors(grid[i - 1][j - 1], 2)
                fives[i][j] = fives[i][j - 1] + count_factors(grid[i - 1][j - 1], 5)
        
        # Prefix sums for vertical direction
        twos_col = [[0] * (n + 1) for _ in range(m + 1)]
        fives_col = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill prefix sums for vertical direction
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                twos_col[i][j] = twos_col[i - 1][j] + count_factors(grid[i - 1][j - 1], 2)
                fives_col[i][j] = fives_col[i - 1][j] + count_factors(grid[i - 1][j - 1], 5)
        
        max_zeros = 0
        
        # Check all possible cornered paths for each cell
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Right and down paths
                right_twos = twos[i][n] - twos[i][j - 1]
                right_fives = fives[i][n] - fives[i][j - 1]
                down_twos = twos_col[m][j] - twos_col[i - 1][j]
                down_fives = fives_col[m][j] - fives_col[i - 1][j]
                
                # Check right-down corner
                max_zeros = max(max_zeros, min(right_twos + down_twos - count_factors(grid[i - 1][j - 1], 2),
                                              right_fives + down_fives - count_factors(grid[i - 1][j - 1], 5)))
                
                # Check left-down corner
                left_twos = twos[i][j] - twos[i][0]
                left_fives = fives[i][j] - fives[i][0]
                max_zeros = max(max_zeros, min(left_twos + down_twos - count_factors(grid[i - 1][j - 1], 2),
                                              left_fives + down_fives - count_factors(grid[i - 1][j - 1], 5)))
                
                # Check right-up corner
                up_twos = twos_col[i][j] - twos_col[0][j]
                up_fives = fives_col[i][j] - fives_col[0][j]
                max_zeros = max(max_zeros, min(right_twos + up_twos - count_factors(grid[i - 1][j - 1], 2),
                                              right_fives + up_fives - count_factors(grid[i - 1][j - 1], 5)))
                
                # Check left-up corner
                max_zeros = max(max_zeros, min(left_twos + up_twos - count_factors(grid[i - 1][j - 1], 2),
                                              left_fives + up_fives - count_factors(grid[i - 1][j - 1], 5)))
        
        return max_zeros

def maxTrailingZeros(grid: List[List[int]]) -> int:
    return Solution().maxTrailingZeros(grid)