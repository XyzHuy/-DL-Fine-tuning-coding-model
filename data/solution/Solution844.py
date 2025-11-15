import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_char(s, i):
            backspaces = 0
            while i >= 0:
                if s[i] == '#':
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    return s[i], i - 1
                i -= 1
            return '', i
        
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            char_s, i = next_char(s, i)
            char_t, j = next_char(t, j)
            if char_s != char_t:
                return False
        return True

def backspaceCompare(s: str, t: str) -> bool:
    return Solution().backspaceCompare(s, t)