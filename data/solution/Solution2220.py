import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR start and goal to find differing bits
        xor_result = start ^ goal
        # Count the number of 1s in the binary representation of xor_result
        return bin(xor_result).count('1')

def minBitFlips(start: int, goal: int) -> int:
    return Solution().minBitFlips(start, goal)