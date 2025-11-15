import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
        
        return i == len(name)

def isLongPressedName(name: str, typed: str) -> bool:
    return Solution().isLongPressedName(name, typed)