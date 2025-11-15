import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Initialize row and column increment counters
        row_increments = [0] * m
        col_increments = [0] * n
        
        # Apply increments based on indices
        for ri, ci in indices:
            row_increments[ri] += 1
            col_increments[ci] += 1
        
        # Count odd-valued cells
        odd_count = 0
        for ri in range(m):
            for ci in range(n):
                if (row_increments[ri] + col_increments[ci]) % 2 == 1:
                    odd_count += 1
        
        return odd_count

def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
    return Solution().oddCells(m, n, indices)