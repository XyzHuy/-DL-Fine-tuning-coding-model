import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_used = [False] * n
        col_used = [False] * n
        row_count = n
        col_count = n
        total_sum = 0
        
        # Process queries in reverse order
        for t, index, value in reversed(queries):
            if t == 0:  # Row operation
                if not row_used[index]:
                    total_sum += value * col_count
                    row_used[index] = True
                    row_count -= 1
            else:  # Column operation
                if not col_used[index]:
                    total_sum += value * row_count
                    col_used[index] = True
                    col_count -= 1
        
        return total_sum

def matrixSumQueries(n: int, queries: List[List[int]]) -> int:
    return Solution().matrixSumQueries(n, queries)