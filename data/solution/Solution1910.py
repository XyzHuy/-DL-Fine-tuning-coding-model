import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s

def removeOccurrences(s: str, part: str) -> str:
    return Solution().removeOccurrences(s, part)