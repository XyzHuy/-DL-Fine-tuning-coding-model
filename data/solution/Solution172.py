import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

def trailingZeroes(n: int) -> int:
    return Solution().trailingZeroes(n)