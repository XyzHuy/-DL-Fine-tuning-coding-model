import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        while i < len(word):
            c = word[i]
            count = 0
            # Count the number of consecutive characters
            while i < len(word) and word[i] == c and count < 9:
                count += 1
                i += 1
            # Append the count and the character to the compressed string
            comp.append(str(count) + c)
        return ''.join(comp)

def compressedString(word: str) -> str:
    return Solution().compressedString(word)