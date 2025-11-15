import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)

def repeatedCharacter(s: str) -> str:
    return Solution().repeatedCharacter(s)