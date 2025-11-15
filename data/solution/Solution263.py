import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1

def isUgly(n: int) -> bool:
    return Solution().isUgly(n)