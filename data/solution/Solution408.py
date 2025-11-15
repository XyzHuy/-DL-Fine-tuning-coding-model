import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':  # Leading zero check
                    return False
                shift = 0
                while j < len(abbr) and abbr[j].isdigit():
                    shift = shift * 10 + int(abbr[j])
                    j += 1
                i += shift
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        return i == len(word) and j == len(abbr)

def validWordAbbreviation(word: str, abbr: str) -> bool:
    return Solution().validWordAbbreviation(word, abbr)