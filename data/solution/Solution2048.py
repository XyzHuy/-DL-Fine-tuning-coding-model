import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_numerically_balanced(x):
            count = [0] * 10
            while x > 0:
                digit = x % 10
                count[digit] += 1
                x //= 10
            for i in range(10):
                if count[i] > 0 and count[i] != i:
                    return False
            return True

        n += 1
        while not is_numerically_balanced(n):
            n += 1
        return n

def nextBeautifulNumber(n: int) -> int:
    return Solution().nextBeautifulNumber(n)