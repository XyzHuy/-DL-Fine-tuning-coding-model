import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)

def strStr(haystack: str, needle: str) -> int:
    return Solution().strStr(haystack, needle)