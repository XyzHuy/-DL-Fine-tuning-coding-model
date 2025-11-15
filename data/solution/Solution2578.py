import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def splitNum(self, num: int) -> int:
        # Convert the number to a string and sort its digits
        digits = sorted(str(num))
        
        # Create two numbers by alternating digits from the sorted list
        num1 = digits[::2]
        num2 = digits[1::2]
        
        # Convert the lists of digits back to integers
        num1 = int(''.join(num1))
        num2 = int(''.join(num2))
        
        # Return the sum of the two numbers
        return num1 + num2

def splitNum(num: int) -> int:
    return Solution().splitNum(num)