import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0

def isPowerOfFour(n: int) -> bool:
    return Solution().isPowerOfFour(n)