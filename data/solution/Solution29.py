import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize the quotient
        quotient = 0
        
        # Bit manipulation to find the largest multiple
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply the sign to the quotient
        if negative:
            quotient = -quotient
        
        return quotient

def divide(dividend: int, divisor: int) -> int:
    return Solution().divide(dividend, divisor)