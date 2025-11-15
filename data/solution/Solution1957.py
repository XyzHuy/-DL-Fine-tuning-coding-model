import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        result = [s[0], s[1]]  # Start with the first two characters
        
        for i in range(2, len(s)):
            # Only add the character if it doesn't form three consecutive identical characters
            if s[i] != s[i - 1] or s[i] != s[i - 2]:
                result.append(s[i])
        
        return ''.join(result)

def makeFancyString(s: str) -> str:
    return Solution().makeFancyString(s)