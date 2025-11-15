import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x):
            return sum(int(digit) for digit in str(x))
        
        if digit_sum(n) <= target:
            return 0
        
        x = 0
        power_of_ten = 1
        while digit_sum(n + x) > target:
            # Calculate the next power of ten
            power_of_ten *= 10
            # Calculate the amount needed to round up to the next power of ten
            x = power_of_ten - (n % power_of_ten)
        
        return x

def makeIntegerBeautiful(n: int, target: int) -> int:
    return Solution().makeIntegerBeautiful(n, target)