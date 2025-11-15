import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(a: float, n: int) -> float:
            ans = 1
            while n:
                if n & 1:
                    ans *= a
                a *= a
                n >>= 1
            return ans

        return qpow(x, n) if n >= 0 else 1 / qpow(x, -n)

def myPow(x: float, n: int) -> float:
    return Solution().myPow(x, n)