import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def fib(n: int) -> int:
    return Solution().fib(n)