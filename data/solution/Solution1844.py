import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c, x):
            return chr(ord(c) + x)
        
        result = []
        for i in range(len(s)):
            if s[i].isdigit():
                result.append(shift(s[i-1], int(s[i])))
            else:
                result.append(s[i])
        
        return ''.join(result)

def replaceDigits(s: str) -> str:
    return Solution().replaceDigits(s)