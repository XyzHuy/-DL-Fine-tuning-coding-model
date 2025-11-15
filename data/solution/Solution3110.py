import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score

def scoreOfString(s: str) -> int:
    return Solution().scoreOfString(s)