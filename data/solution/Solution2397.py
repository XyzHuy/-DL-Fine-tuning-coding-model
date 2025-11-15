import random
import functools
import collections
import string
import math
import datetime


from itertools import combinations
from typing import List

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # Generate all possible combinations of columns to select
        column_combinations = combinations(range(n), numSelect)
        max_covered_rows = 0
        
        for cols in column_combinations:
            covered_rows = 0
            for row in matrix:
                # Check if this row is covered by the selected columns
                if all(row[c] == 0 or c in cols for c in range(n)):
                    covered_rows += 1
            max_covered_rows = max(max_covered_rows, covered_rows)
        
        return max_covered_rows

def maximumRows(matrix: List[List[int]], numSelect: int) -> int:
    return Solution().maximumRows(matrix, numSelect)