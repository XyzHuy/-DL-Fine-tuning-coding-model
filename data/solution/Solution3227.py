import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        vowel_count = sum(1 for char in s if char in vowels)
        return vowel_count > 0

def doesAliceWin(s: str) -> bool:
    return Solution().doesAliceWin(s)