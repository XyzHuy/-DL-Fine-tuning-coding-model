import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            # For negative numbers, we want to minimize the absolute value
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            # For positive numbers, we want to maximize the value
            for i in range(len(n)):
                if int(n[i]) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)

def maxValue(n: str, x: int) -> str:
    return Solution().maxValue(n, x)