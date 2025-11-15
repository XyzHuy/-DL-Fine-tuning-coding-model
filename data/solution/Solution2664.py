import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        def dfs(i: int, j: int):
            nonlocal ok
            if g[i][j] == m * n - 1:
                ok = True
                return
            for a, b in pairwise((-2, -1, 2, 1, -2, 1, 2, -1, -2)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and g[x][y] == -1:
                    g[x][y] = g[i][j] + 1
                    dfs(x, y)
                    if ok:
                        return
                    g[x][y] = -1

        def pairwise(iterable):
            a, b = iter(iterable), iter(iterable)
            next(b, None)
            return zip(a, b)

        g = [[-1] * n for _ in range(m)]
        g[r][c] = 0
        ok = False
        dfs(r, c)
        return g

def tourOfKnight(m: int, n: int, r: int, c: int) -> List[List[int]]:
    return Solution().tourOfKnight(m, n, r, c)