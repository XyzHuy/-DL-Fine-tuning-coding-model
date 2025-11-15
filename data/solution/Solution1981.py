import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # Preprocess the matrix to remove duplicates and sort each row
        for row in mat:
            row.sort()
            unique_row = list(dict.fromkeys(row))
            row[:] = unique_row
        
        m, n = len(mat), len(mat[0])
        
        @lru_cache(None)
        def dp(row, current_sum):
            if row == m:
                return abs(current_sum - target)
            
            min_diff = float('inf')
            for num in mat[row]:
                new_sum = current_sum + num
                # If new_sum is already larger than target, stop exploring further in this row
                # because the numbers are sorted in ascending order.
                if new_sum >= target:
                    min_diff = min(min_diff, dp(row + 1, new_sum))
                    break
                min_diff = min(min_diff, dp(row + 1, new_sum))
            return min_diff
        
        return dp(0, 0)

def minimizeTheDifference(mat: List[List[int]], target: int) -> int:
    return Solution().minimizeTheDifference(mat, target)