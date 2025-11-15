import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Calculate the number of integers in the range
        total_numbers = high - low + 1
        
        # If the total number of integers is even, half of them will be odd
        # If the total number of integers is odd, check the parity of low or high
        if total_numbers % 2 == 0:
            return total_numbers // 2
        else:
            # If the total number of integers is odd, and low is odd, then there will be one more odd number
            # If the total number of integers is odd, and low is even, then the number of odd numbers will be half of total_numbers
            return total_numbers // 2 + (low % 2)

def countOdds(low: int, high: int) -> int:
    return Solution().countOdds(low, high)