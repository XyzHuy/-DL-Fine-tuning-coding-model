import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = 0
        temp = n
        while temp > 0:
            mask = (mask << 1) | 1
            temp >>= 1
        return n ^ mask

def bitwiseComplement(n: int) -> int:
    return Solution().bitwiseComplement(n)