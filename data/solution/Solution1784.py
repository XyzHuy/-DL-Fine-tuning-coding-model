import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Since the string does not have leading zeros and starts with '1',
        # we can simply check if there is a '01' pattern in the string.
        # If '01' is found, it means there is more than one segment of ones.
        return '01' not in s

def checkOnesSegment(s: str) -> bool:
    return Solution().checkOnesSegment(s)