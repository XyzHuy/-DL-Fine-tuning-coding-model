import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize the first ugly number
        ugly_numbers = [1]
        
        # Pointers for multiples of 2, 3, and 5
        i2 = i3 = i5 = 0
        
        # Generate ugly numbers until we have the nth one
        while len(ugly_numbers) < n:
            # Next multiple of 2, 3, and 5
            next_multiple_of_2 = ugly_numbers[i2] * 2
            next_multiple_of_3 = ugly_numbers[i3] * 3
            next_multiple_of_5 = ugly_numbers[i5] * 5
            
            # Choose the smallest next ugly number
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly_numbers.append(next_ugly)
            
            # Increment the pointer for the chosen multiple
            if next_ugly == next_multiple_of_2:
                i2 += 1
            if next_ugly == next_multiple_of_3:
                i3 += 1
            if next_ugly == next_multiple_of_5:
                i5 += 1
        
        # Return the nth ugly number
        return ugly_numbers[-1]

def nthUglyNumber(n: int) -> int:
    return Solution().nthUglyNumber(n)