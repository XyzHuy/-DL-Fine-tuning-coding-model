import random
import functools
import collections
import string
import math
import datetime


from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Initialize the numerator and denominator
        x, y = 0, 6 * 7 * 8 * 9 * 10  # LCM of denominators 1 through 10
        
        # If the expression starts with a digit, prepend a '+' to handle it uniformly
        if expression[0].isdigit():
            expression = '+' + expression
        
        i, n = 0, len(expression)
        
        while i < n:
            # Determine the sign of the current fraction
            sign = -1 if expression[i] == '-' else 1
            i += 1
            
            # Find the end of the current fraction
            j = i
            while j < n and expression[j] not in '+-':
                j += 1
            
            # Extract the fraction and split it into numerator and denominator
            s = expression[i:j]
            a, b = s.split('/')
            
            # Add the current fraction to the total
            x += sign * int(a) * y // int(b)
            
            # Move to the next fraction
            i = j
        
        # Simplify the resulting fraction
        z = gcd(x, y)
        x //= z
        y //= z
        
        # Return the result in the required format
        return f'{x}/{y}'

def fractionAddition(expression: str) -> str:
    return Solution().fractionAddition(expression)