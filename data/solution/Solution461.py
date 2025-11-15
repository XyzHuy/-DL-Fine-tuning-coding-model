import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers to find differing bits
        xor_result = x ^ y
        # Count the number of 1s in the binary representation of the XOR result
        return bin(xor_result).count('1')

def hammingDistance(x: int, y: int) -> int:
    return Solution().hammingDistance(x, y)