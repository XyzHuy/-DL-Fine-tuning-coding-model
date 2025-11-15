import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Helper function to convert a base -2 array to a decimal number
        def to_decimal(arr):
            decimal = 0
            power = 1
            for bit in reversed(arr):
                decimal += bit * power
                power *= -2
            return decimal
        
        # Helper function to convert a decimal number to a base -2 array
        def to_negabinary(decimal):
            if decimal == 0:
                return [0]
            negabinary = []
            while decimal != 0:
                decimal, remainder = divmod(decimal, -2)
                if remainder < 0:
                    remainder += 2
                    decimal += 1
                negabinary.append(remainder)
            return negabinary[::-1]
        
        # Convert both arrays to decimal
        decimal1 = to_decimal(arr1)
        decimal2 = to_decimal(arr2)
        
        # Add the decimal numbers
        total_decimal = decimal1 + decimal2
        
        # Convert the sum back to base -2
        result = to_negabinary(total_decimal)
        
        return result

def addNegabinary(arr1: List[int], arr2: List[int]) -> List[int]:
    return Solution().addNegabinary(arr1, arr2)