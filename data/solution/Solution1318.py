import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):  # Since the maximum value is 10^9, we only need to check up to 32 bits
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            
            if bit_c == 0:
                # If the bit in c is 0, both bits in a and b must be 0
                flips += bit_a + bit_b
            else:
                # If the bit in c is 1, at least one of the bits in a or b must be 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1
        return flips

def minFlips(a: int, b: int, c: int) -> int:
    return Solution().minFlips(a, b, c)