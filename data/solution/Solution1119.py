import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiou')
        return ''.join([char for char in s if char not in vowels])

def removeVowels(s: str) -> str:
    return Solution().removeVowels(s)