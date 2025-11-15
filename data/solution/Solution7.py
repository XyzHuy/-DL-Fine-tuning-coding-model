import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign of the number
        sign = -1 if x < 0 else 1
        
        # Reverse the digits of the absolute value of the number
        reversed_digits = int(str(abs(x))[::-1])
        
        # Restore the sign
        reversed_number = sign * reversed_digits
        
        # Check if the reversed number is within the 32-bit signed integer range
        if reversed_number < -2**31 or reversed_number > 2**31 - 1:
            return 0
        
        return reversed_number

def reverse(x: int) -> int:
    return Solution().reverse(x)