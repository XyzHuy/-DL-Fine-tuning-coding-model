import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps

def numberOfSteps(num: int) -> int:
    return Solution().numberOfSteps(num)