import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # If n is already even, the smallest multiple of both 2 and n is n itself
        if n % 2 == 0:
            return n
        # If n is odd, the smallest multiple of both 2 and n is 2 * n
        else:
            return 2 * n

def smallestEvenMultiple(n: int) -> int:
    return Solution().smallestEvenMultiple(n)