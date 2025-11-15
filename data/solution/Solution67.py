import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers, add them, and then convert the result back to a binary string
        return bin(int(a, 2) + int(b, 2))[2:]

def addBinary(a: str, b: str) -> str:
    return Solution().addBinary(a, b)