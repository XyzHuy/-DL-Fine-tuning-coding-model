import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        from string import ascii_lowercase, ascii_uppercase
        
        first, last = {}, {}
        for i, c in enumerate(word):
            if c not in first:
                first[c] = i
            last[c] = i
        
        return sum(
            a in last and b in first and last[a] < first[b]
            for a, b in zip(ascii_lowercase, ascii_uppercase)
        )

def numberOfSpecialChars(word: str) -> int:
    return Solution().numberOfSpecialChars(word)