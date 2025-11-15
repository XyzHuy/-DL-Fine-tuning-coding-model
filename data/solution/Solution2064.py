import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_left

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(x):
            return sum((v + x - 1) // x for v in quantities) <= n

        return 1 + bisect_left(range(1, 10**6), True, key=check)

def minimizedMaximum(n: int, quantities: List[int]) -> int:
    return Solution().minimizedMaximum(n, quantities)