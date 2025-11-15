import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        g = {}
        for i, row in enumerate(grid):
            mask = 0
            for j, x in enumerate(row):
                mask |= x << j
            if mask == 0:
                return [i]
            g[mask] = i
        for a, i in g.items():
            for b, j in g.items():
                if (a & b) == 0:
                    return sorted([i, j])
        return []

def goodSubsetofBinaryMatrix(grid: List[List[int]]) -> List[int]:
    return Solution().goodSubsetofBinaryMatrix(grid)