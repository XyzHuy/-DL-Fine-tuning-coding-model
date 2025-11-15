import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        cumulative_shift = 0
        n = len(s)
        result = []
        
        # Compute the cumulative shifts from the end to the beginning
        for i in range(n - 1, -1, -1):
            cumulative_shift += shifts[i]
            cumulative_shift %= 26  # Ensure the shift is within the range of 0-25
        
        # Apply the cumulative shifts to the string
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result.append(new_char)
            cumulative_shift -= shifts[i]  # Update cumulative shift for the next character
        
        return ''.join(result)

def shiftingLetters(s: str, shifts: List[int]) -> str:
    return Solution().shiftingLetters(s, shifts)