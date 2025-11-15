import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0

def isPowerOfTwo(n: int) -> bool:
    return Solution().isPowerOfTwo(n)