import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1):  # Start from 'a' to avoid duplicate pairs (a, b) and (b, a)
                c_squared = a * a + b * b
                c = int(c_squared ** 0.5)
                if c <= n and c * c == c_squared:
                    count += 2  # Count both (a, b, c) and (b, a, c)
        return count

def countTriples(n: int) -> int:
    return Solution().countTriples(n)