import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                number = number // 10
                total_sum += digit * digit
            return total_sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

def isHappy(n: int) -> bool:
    return Solution().isHappy(n)