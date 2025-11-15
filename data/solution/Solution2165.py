import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        # Convert the number to a string and remove the sign
        num_str = str(abs(num))
        
        # Sort the digits
        sorted_digits = sorted(num_str)
        
        if num > 0:
            # Find the first non-zero digit and swap it with the first digit
            for i, digit in enumerate(sorted_digits):
                if digit != '0':
                    # Swap to avoid leading zero
                    sorted_digits[0], sorted_digits[i] = sorted_digits[i], sorted_digits[0]
                    break
            
            # Join the sorted digits and convert back to integer
            return int(''.join(sorted_digits))
        else:
            # For negative numbers, just reverse the sorted digits to get the smallest value
            return -int(''.join(sorted_digits[::-1]))

def smallestNumber(num: int) -> int:
    return Solution().smallestNumber(num)