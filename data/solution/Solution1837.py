import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # Convert n from base 10 to base k
        digits = []
        while n > 0:
            digits.append(n % k)
            n //= k
        
        # Sum the digits of the base k number
        return sum(digits)

def sumBase(n: int, k: int) -> int:
    return Solution().sumBase(n, k)