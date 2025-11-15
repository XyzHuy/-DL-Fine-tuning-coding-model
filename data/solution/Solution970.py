import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_set = set()
        
        # Since x and y are at least 1, the maximum value for i or j can be log(bound) base(x) or log(bound) base(y)
        max_i = 0 if x == 1 else int(math.log(bound, x))
        max_j = 0 if y == 1 else int(math.log(bound, y))
        
        for i in range(max_i + 1):
            for j in range(max_j + 1):
                value = x**i + y**j
                if value <= bound:
                    powerful_set.add(value)
        
        return list(powerful_set)

def powerfulIntegers(x: int, y: int, bound: int) -> List[int]:
    return Solution().powerfulIntegers(x, y, bound)