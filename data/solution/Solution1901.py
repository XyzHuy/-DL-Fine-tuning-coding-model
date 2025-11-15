import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def find_peak_row(row):
            max_col = 0
            for c in range(1, n):
                if mat[row][c] > mat[row][max_col]:
                    max_col = c
            return max_col

        m, n = len(mat), len(mat[0])
        low, high = 0, m - 1

        while low < high:
            mid = (low + high) // 2
            peak_col = find_peak_row(mid)

            if mat[mid][peak_col] < mat[mid + 1][peak_col]:
                low = mid + 1
            else:
                high = mid

        peak_col = find_peak_row(low)
        return [low, peak_col]

def findPeakGrid(mat: List[List[int]]) -> List[int]:
    return Solution().findPeakGrid(mat)