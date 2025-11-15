import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        # Determine the sign of the result
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        
        # Work with absolute values to simplify the process
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Calculate the integer part
        integer_part = numerator // denominator
        remainder = numerator % denominator
        
        # If there is no remainder, return the integer part with the sign
        if remainder == 0:
            return sign + str(integer_part)
        
        # Dictionary to store the seen remainders and their corresponding position in the result
        seen_remainders = {}
        fractional_part = []
        position = 0
        
        # Calculate the fractional part
        while remainder != 0:
            # If the remainder is seen before, we have a repeating part
            if remainder in seen_remainders:
                start = seen_remainders[remainder]
                non_repeating = ''.join(fractional_part[:start])
                repeating = ''.join(fractional_part[start:])
                return sign + str(integer_part) + '.' + non_repeating + '(' + repeating + ')'
            
            # Record the position of this remainder
            seen_remainders[remainder] = position
            position += 1
            
            # Calculate the next digit in the fractional part
            remainder *= 10
            digit = remainder // denominator
            fractional_part.append(str(digit))
            remainder %= denominator
        
        # If no repeating part, return the integer and fractional parts
        return sign + str(integer_part) + '.' + ''.join(fractional_part)

def fractionToDecimal(numerator: int, denominator: int) -> str:
    return Solution().fractionToDecimal(numerator, denominator)