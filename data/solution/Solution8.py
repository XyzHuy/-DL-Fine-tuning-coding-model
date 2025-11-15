import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore leading whitespace
        s = s.lstrip()
        
        # Step 2: Check if the string is empty after stripping whitespace
        if not s:
            return 0
        
        # Step 3: Determine the sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        # Step 4: Read in the digits until a non-digit is encountered
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        # Step 5: Apply the sign
        result *= sign
        
        # Step 6: Clamp the result to the 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result

def myAtoi(s: str) -> int:
    return Solution().myAtoi(s)