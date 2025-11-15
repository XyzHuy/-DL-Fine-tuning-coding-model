import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        while word * (k + 1) in sequence:
            k += 1
        return k

def maxRepeating(sequence: str, word: str) -> int:
    return Solution().maxRepeating(sequence, word)