import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Calculate the minimum number of repetitions needed
        min_repeats = (len(b) + len(a) - 1) // len(a)
        
        # Check if b is a substring of a repeated min_repeats times
        for repeats in range(min_repeats, min_repeats + 2):
            if b in a * repeats:
                return repeats
        
        # If b is not a substring in any of the cases, return -1
        return -1

def repeatedStringMatch(a: str, b: str) -> int:
    return Solution().repeatedStringMatch(a, b)