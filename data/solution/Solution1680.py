import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        length = 0
        
        for i in range(1, n + 1):
            # Determine the length of the binary representation of i
            if i & (i - 1) == 0:  # i is a power of 2
                length += 1
            # Shift result to the left by the length of i's binary representation
            # and add the binary representation of i
            result = ((result << length) | i) % MOD
        
        return result

def concatenatedBinary(n: int) -> int:
    return Solution().concatenatedBinary(n)