import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return n // 2
        else:
            return n

def numberOfCuts(n: int) -> int:
    return Solution().numberOfCuts(n)