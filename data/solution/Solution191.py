import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert the integer to its binary representation and count the '1's
        return bin(n).count('1')

def hammingWeight(n: int) -> int:
    return Solution().hammingWeight(n)