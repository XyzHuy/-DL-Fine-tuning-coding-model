import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isArmstrong(self, n: int) -> bool:
        # Convert the number to a string to easily iterate over digits
        digits = str(n)
        # Calculate the number of digits
        k = len(digits)
        # Calculate the sum of each digit raised to the power of k
        armstrong_sum = sum(int(digit) ** k for digit in digits)
        # Check if the sum is equal to the original number
        return armstrong_sum == n

def isArmstrong(n: int) -> bool:
    return Solution().isArmstrong(n)