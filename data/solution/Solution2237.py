import random
import functools
import collections
import string
import math
import datetime


from itertools import accumulate
from typing import List

class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        d = [0] * (n + 1)
        for p, r in lights:
            i, j = max(0, p - r), min(n - 1, p + r)
            d[i] += 1
            d[j + 1] -= 1
        return sum(s >= r for s, r in zip(accumulate(d), requirement))

def meetRequirement(n: int, lights: List[List[int]], requirement: List[int]) -> int:
    return Solution().meetRequirement(n, lights, requirement)