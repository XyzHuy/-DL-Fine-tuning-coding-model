import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed_s = s[::-1]
        for i in range(len(s) - 1):
            substring = s[i:i+2]
            if substring in reversed_s:
                return True
        return False

def isSubstringPresent(s: str) -> bool:
    return Solution().isSubstringPresent(s)