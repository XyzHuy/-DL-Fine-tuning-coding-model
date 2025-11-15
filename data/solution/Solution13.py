import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to map Roman numeral characters to their integer values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the total to 0
        total = 0
        # Get the length of the input string
        n = len(s)
        
        # Iterate through each character in the string
        for i in range(n):
            # If the current value is less than the next value, subtract it
            if i < n - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            else:
                # Otherwise, add the current value
                total += roman_values[s[i]]
        
        return total

def romanToInt(s: str) -> int:
    return Solution().romanToInt(s)