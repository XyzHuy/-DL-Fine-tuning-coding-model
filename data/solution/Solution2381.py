import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_values = [0] * (n + 1)
        
        # Apply the shifts using a difference array technique
        for start, end, direction in shifts:
            if direction == 1:
                shift_values[start] += 1
                shift_values[end + 1] -= 1
            else:
                shift_values[start] -= 1
                shift_values[end + 1] += 1
        
        # Compute the final shift values for each character
        for i in range(1, n):
            shift_values[i] += shift_values[i - 1]
        
        # Create the final shifted string
        result = []
        for i in range(n):
            # Calculate the new character position with wrapping
            new_char = chr((ord(s[i]) - ord('a') + shift_values[i]) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)

def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    return Solution().shiftingLetters(s, shifts)