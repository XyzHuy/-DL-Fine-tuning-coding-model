import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # Convert the number to a string to easily access each digit
        n_str = str(n)
        # Initialize the sum
        total_sum = 0
        # Iterate over the digits with their index
        for i, digit in enumerate(n_str):
            # Convert the character to an integer
            num = int(digit)
            # Add or subtract the digit based on its position
            if i % 2 == 0:
                total_sum += num
            else:
                total_sum -= num
        return total_sum

def alternateDigitSum(n: int) -> int:
    return Solution().alternateDigitSum(n)