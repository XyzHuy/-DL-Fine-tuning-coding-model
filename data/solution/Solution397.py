import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                # If n is 3 or the last two bits are 01, it's better to subtract 1
                if n == 3 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1
            count += 1
        return count

def integerReplacement(n: int) -> int:
    return Solution().integerReplacement(n)