import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        # We will count the number of shifts needed for each possible shift amount (1 to 25)
        shift_count = [0] * 26
        
        # Calculate the required shifts for each character
        for i in range(len(s)):
            shift = (ord(t[i]) - ord(s[i])) % 26
            if shift != 0:
                shift_count[shift] += 1
        
        # Check if we can achieve all the required shifts within k moves
        for shift in range(1, 26):
            max_allowed_shift = shift + (shift_count[shift] - 1) * 26
            if max_allowed_shift > k:
                return False
        
        return True

def canConvertString(s: str, t: str, k: int) -> bool:
    return Solution().canConvertString(s, t, k)