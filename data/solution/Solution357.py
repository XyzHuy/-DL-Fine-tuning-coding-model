import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        # Start with numbers from 0 to 9
        count = 10
        # For the first digit, we have 9 options (1-9)
        # For the second digit, we have 9 options (0-9 except the first digit)
        # For the third digit, we have 8 options (0-9 except the first two digits)
        # And so on...
        unique_digits_count = 9
        available_digits = 9
        
        for i in range(2, n + 1):
            unique_digits_count *= available_digits
            count += unique_digits_count
            available_digits -= 1
        
        return count

def countNumbersWithUniqueDigits(n: int) -> int:
    return Solution().countNumbersWithUniqueDigits(n)