import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check if characters at even indices and odd indices can be swapped to match
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])

def canBeEqual(s1: str, s2: str) -> bool:
    return Solution().canBeEqual(s1, s2)