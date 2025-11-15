import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # Mask to get 32 bits
        mask = 0xFFFFFFFF
        
        while b != 0:
            # Calculate carry
            carry = (a & b) << 1
            # Sum without carry
            a = (a ^ b) & mask
            # Update b to carry
            b = carry & mask
        
        # If a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

def getSum(a: int, b: int) -> int:
    return Solution().getSum(a, b)