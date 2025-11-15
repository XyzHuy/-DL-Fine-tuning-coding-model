import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]
        
        # If the difference in length between letters and digits is more than 1, return ""
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        # Determine which one to start with
        if len(letters) >= len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters
        
        # Interleave the characters
        result = []
        for i in range(len(second)):
            result.append(first[i])
            result.append(second[i])
        
        # If there's one extra character, add it at the end
        if len(first) > len(second):
            result.append(first[-1])
        
        return ''.join(result)

def reformat(s: str) -> str:
    return Solution().reformat(s)