import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        s = list(num)
        changed = False
        for i, c in enumerate(s):
            d = str(change[int(c)])
            if changed and d < c:
                break
            if d > c:
                changed = True
                s[i] = d
        return "".join(s)

def maximumNumber(num: str, change: List[int]) -> str:
    return Solution().maximumNumber(num, change)