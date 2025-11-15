import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        occurrences = 0
        
        for char in s:
            if char == c:
                occurrences += 1
                count += occurrences
        
        return count

def countSubstrings(s: str, c: str) -> int:
    return Solution().countSubstrings(s, c)