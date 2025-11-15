import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Compute prefix sums for rows and columns
        row_sums = [[0] * (n + 1) for _ in range(m + 1)]
        col_sums = [[0] * (n + 1) for _ in range(m + 1)]
        diag_sums = [[0] * (n + 2) for _ in range(m + 2)]
        anti_diag_sums = [[0] * (n + 2) for _ in range(m + 2)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                row_sums[i][j] = row_sums[i][j - 1] + grid[i - 1][j - 1]
                col_sums[i][j] = col_sums[i - 1][j] + grid[i - 1][j - 1]
                diag_sums[i][j] = diag_sums[i - 1][j - 1] + grid[i - 1][j - 1]
                anti_diag_sums[i][j] = anti_diag_sums[i - 1][j + 1] + grid[i - 1][j - 1]
        
        def is_magic(r, c, k):
            target = row_sums[r][c + k - 1] - row_sums[r][c - 1]
            for i in range(r, r + k):
                if row_sums[i][c + k - 1] - row_sums[i][c - 1] != target:
                    return False
            for j in range(c, c + k):
                if col_sums[r + k - 1][j] - col_sums[r - 1][j] != target:
                    return False
            if diag_sums[r + k - 1][c + k - 1] - diag_sums[r - 1][c - 1] != target:
                return False
            if anti_diag_sums[r + k - 1][c] - anti_diag_sums[r - 1][c + k] != target:
                return False
            return True
        
        max_k = min(m, n)
        for k in range(max_k, 1, -1):
            for r in range(1, m - k + 2):
                for c in range(1, n - k + 2):
                    if is_magic(r, c, k):
                        return k
        return 1

def largestMagicSquare(grid: List[List[int]]) -> int:
    return Solution().largestMagicSquare(grid)