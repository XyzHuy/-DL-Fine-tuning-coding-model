import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for char in s:
            if char == 'i':
                result.reverse()
            else:
                result.append(char)
        return ''.join(result)

def finalString(s: str) -> str:
    return Solution().finalString(s)