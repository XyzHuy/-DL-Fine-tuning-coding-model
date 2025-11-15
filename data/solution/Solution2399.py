import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = defaultdict(int)
        for i, c in enumerate(map(ord, s), 1):
            j = c - ord("a")
            if d[j] and i - d[j] - 1 != distance[j]:
                return False
            d[j] = i
        return True

def checkDistances(s: str, distance: List[int]) -> bool:
    return Solution().checkDistances(s, distance)