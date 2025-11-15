import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Find the minimum element in each row
        min_in_rows = [min(row) for row in matrix]
        
        # Find the maximum element in each column
        max_in_cols = [max(col) for col in zip(*matrix)]
        
        # Find the intersection of min_in_rows and max_in_cols
        lucky_numbers = list(set(min_in_rows) & set(max_in_cols))
        
        return lucky_numbers

def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    return Solution().luckyNumbers(matrix)