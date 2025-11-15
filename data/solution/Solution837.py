import random
import functools
import collections
import string
import math
import datetime


from functools import cache

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @cache
        def dfs(i: int) -> float:
            if i >= k:
                return int(i <= n)
            if i == k - 1:
                return min(n - k + 1, maxPts) / maxPts
            return dfs(i + 1) + (dfs(i + 1) - dfs(i + maxPts + 1)) / maxPts

        return dfs(0)

def new21Game(n: int, k: int, maxPts: int) -> float:
    return Solution().new21Game(n, k, maxPts)