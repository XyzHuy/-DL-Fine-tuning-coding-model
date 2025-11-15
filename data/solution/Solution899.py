import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            # If k > 1, we can sort the string to get the lexicographically smallest string
            return ''.join(sorted(s))
        else:
            # If k == 1, we can only rotate the string
            # We need to find the lexicographically smallest rotation
            n = len(s)
            s = s + s  # Concatenate the string with itself
            smallest = s[:n]
            for i in range(1, n):
                if s[i:i+n] < smallest:
                    smallest = s[i:i+n]
            return smallest

def orderlyQueue(s: str, k: int) -> str:
    return Solution().orderlyQueue(s, k)