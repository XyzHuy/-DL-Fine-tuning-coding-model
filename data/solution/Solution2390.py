import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for char in s:
            if char == '*':
                if result:
                    result.pop()
            else:
                result.append(char)
        return ''.join(result)

def removeStars(s: str) -> str:
    return Solution().removeStars(s)