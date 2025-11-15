import random
import functools
import collections
import string
import math
import datetime


from bisect import bisect_left
from functools import cache
from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(rides):
                return 0
            st, ed, tip = rides[i]
            j = bisect_left(rides, ed, lo=i + 1, key=lambda x: x[0])
            return max(dfs(i + 1), dfs(j) + ed - st + tip)

        rides.sort()
        return dfs(0)

def maxTaxiEarnings(n: int, rides: List[List[int]]) -> int:
    return Solution().maxTaxiEarnings(n, rides)