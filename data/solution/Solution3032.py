import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberCount(self, a: int, b: int) -> int:
        def has_unique_digits(n: int) -> bool:
            digits = str(n)
            return len(digits) == len(set(digits))
        
        count = 0
        for num in range(a, b + 1):
            if has_unique_digits(num):
                count += 1
                
        return count

def numberCount(a: int, b: int) -> int:
    return Solution().numberCount(a, b)