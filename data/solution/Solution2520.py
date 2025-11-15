import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countDigits(self, num: int) -> int:
        # Convert the number to a string to iterate over each digit
        num_str = str(num)
        count = 0
        
        # Iterate over each character in the string representation of the number
        for char in num_str:
            digit = int(char)
            # Check if the digit divides the number
            if num % digit == 0:
                count += 1
        
        return count

def countDigits(num: int) -> int:
    return Solution().countDigits(num)