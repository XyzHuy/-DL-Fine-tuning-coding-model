import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result

def xorOperation(n: int, start: int) -> int:
    return Solution().xorOperation(n, start)