import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]

def getNoZeroIntegers(n: int) -> List[int]:
    return Solution().getNoZeroIntegers(n)