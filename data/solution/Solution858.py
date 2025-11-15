import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from math import gcd
        
        # Find the smallest n such that n * q is a multiple of p
        n = p // gcd(p, q)
        m = n * q // p
        
        # Determine the receptor based on the parity of m and n
        if m % 2 == 0 and n % 2 == 1:
            return 0
        elif m % 2 == 1 and n % 2 == 0:
            return 2
        elif m % 2 == 1 and n % 2 == 1:
            return 1

def mirrorReflection(p: int, q: int) -> int:
    return Solution().mirrorReflection(p, q)