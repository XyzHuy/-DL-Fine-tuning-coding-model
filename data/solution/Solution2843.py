import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(x: int) -> bool:
            s = str(x)
            n = len(s)
            if n % 2 != 0:
                return False
            mid = n // 2
            return sum(int(s[i]) for i in range(mid)) == sum(int(s[i]) for i in range(mid, n))
        
        count = 0
        for x in range(low, high + 1):
            if is_symmetric(x):
                count += 1
        return count

def countSymmetricIntegers(low: int, high: int) -> int:
    return Solution().countSymmetricIntegers(low, high)