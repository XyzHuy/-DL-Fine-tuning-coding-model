import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Convert the number to a list of its digits
        digits = list(str(n))
        length = len(digits)
        
        # Flag to mark the position where we need to start changing digits to '9'
        flag = length
        
        # Traverse the digits from right to left
        for i in range(length - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                # Mark the position
                flag = i
                # Decrease the previous digit by 1
                digits[i - 1] = str(int(digits[i - 1]) - 1)
        
        # Change all digits to the right of the flag to '9'
        for i in range(flag, length):
            digits[i] = '9'
        
        # Join the digits to form the resulting number
        return int(''.join(digits))

def monotoneIncreasingDigits(n: int) -> int:
    return Solution().monotoneIncreasingDigits(n)