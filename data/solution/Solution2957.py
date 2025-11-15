import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        operations = 0
        i = 1
        while i < len(word):
            # Check if current character and previous character are almost-equal
            if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
                operations += 1
                # Skip the next character as it is affected by the current operation
                i += 1
            i += 1
        return operations

def removeAlmostEqualCharacters(word: str) -> int:
    return Solution().removeAlmostEqualCharacters(word)