import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        chars = '0123456789abcdef'
        s = []
        # Handle negative numbers using two's complement
        if num < 0:
            num += 2**32
        for i in range(7, -1, -1):
            x = (num >> (4 * i)) & 0xF
            if s or x != 0:
                s.append(chars[x])
        return ''.join(s)

def toHex(num: int) -> str:
    return Solution().toHex(num)