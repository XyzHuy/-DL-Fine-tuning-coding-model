import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            operations += 1
        # Once target is less than or equal to startValue, we can only use subtraction
        operations += startValue - target
        return operations

def brokenCalc(startValue: int, target: int) -> int:
    return Solution().brokenCalc(startValue, target)