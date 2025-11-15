import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getSmallestString(self, s: str) -> str:
        # Convert the string to a list of integers for easier manipulation
        digits = list(map(int, s))
        
        # Iterate through the list of digits
        for i in range(len(digits) - 1):
            # Check if the current digit and the next digit have the same parity
            if (digits[i] % 2 == digits[i + 1] % 2):
                # If they do, and the current digit is greater than the next, swap them
                if digits[i] > digits[i + 1]:
                    digits[i], digits[i + 1] = digits[i + 1], digits[i]
                    # Since we can only swap once, return the result immediately
                    return ''.join(map(str, digits))
        
        # If no swaps were made, return the original string
        return s

def getSmallestString(s: str) -> str:
    return Solution().getSmallestString(s)