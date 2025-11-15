import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                # This means we have a two-digit number followed by '#'
                num = int(s[i:i+2])
                result.append(chr(num + ord('a') - 1))
                i += 3  # Move past the two digits and the '#'
            else:
                # This means we have a single-digit number
                num = int(s[i])
                result.append(chr(num + ord('a') - 1))
                i += 1  # Move past the single digit
        return ''.join(result)

def freqAlphabets(s: str) -> str:
    return Solution().freqAlphabets(s)