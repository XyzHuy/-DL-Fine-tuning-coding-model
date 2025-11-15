import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # Check if the binary representation of each number in the range [1, n] is a substring of s
        for i in range(1, n + 1):
            binary_rep = bin(i)[2:]  # Get binary representation of i, excluding the '0b' prefix
            if binary_rep not in s:
                return False
        return True

def queryString(s: str, n: int) -> bool:
    return Solution().queryString(s, n)