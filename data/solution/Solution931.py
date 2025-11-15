import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [0] * n
        for row in matrix:
            g = [0] * n
            for j, x in enumerate(row):
                l, r = max(0, j - 1), min(n, j + 2)
                g[j] = min(f[l:r]) + x
            f = g
        return min(f)

def minFallingPathSum(matrix: List[List[int]]) -> int:
    return Solution().minFallingPathSum(matrix)