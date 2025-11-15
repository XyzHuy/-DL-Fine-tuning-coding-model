import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2  # Skip the next bit as it's part of a two-bit character
            else:
                i += 1  # Move to the next bit as it's a one-bit character
        return i == len(bits) - 1  # Check if we ended at the last character

def isOneBitCharacter(bits: List[int]) -> bool:
    return Solution().isOneBitCharacter(bits)