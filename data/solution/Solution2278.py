import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if not s:
            return 0
        
        count = s.count(letter)
        percentage = (count / len(s)) * 100
        return int(percentage)

def percentageLetter(s: str, letter: str) -> int:
    return Solution().percentageLetter(s, letter)