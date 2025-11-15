import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9

def addDigits(num: int) -> int:
    return Solution().addDigits(num)