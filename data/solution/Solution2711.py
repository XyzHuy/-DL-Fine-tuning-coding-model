import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        answer = [[0] * n for _ in range(m)]
        
        # Function to calculate the number of distinct values in a diagonal
        def count_distinct(diagonal):
            return len(set(diagonal))
        
        # Calculate the answer for each cell
        for r in range(m):
            for c in range(n):
                # Collect leftAbove diagonal values
                left_above = []
                i, j = r - 1, c - 1
                while i >= 0 and j >= 0:
                    left_above.append(grid[i][j])
                    i -= 1
                    j -= 1
                
                # Collect rightBelow diagonal values
                right_below = []
                i, j = r + 1, c + 1
                while i < m and j < n:
                    right_below.append(grid[i][j])
                    i += 1
                    j += 1
                
                # Calculate the answer for the current cell
                answer[r][c] = abs(count_distinct(left_above) - count_distinct(right_below))
        
        return answer

def differenceOfDistinctValues(grid: List[List[int]]) -> List[List[int]]:
    return Solution().differenceOfDistinctValues(grid)