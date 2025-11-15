import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9, simply add one and return the list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0
        
        # If all digits were 9, we need to add a leading 1
        return [1] + digits

def plusOne(digits: List[int]) -> List[int]:
    return Solution().plusOne(digits)