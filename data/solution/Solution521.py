import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If the strings are equal, there is no uncommon subsequence
        if a == b:
            return -1
        # If the strings are not equal, the longest uncommon subsequence
        # is the longer of the two strings
        return max(len(a), len(b))

def findLUSlength(a: str, b: str) -> int:
    return Solution().findLUSlength(a, b)