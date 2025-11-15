import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def secondHighest(self, s: str) -> int:
        # Use a set to store unique digits found in the string
        digits = set()
        
        # Iterate through each character in the string
        for char in s:
            # Check if the character is a digit
            if char.isdigit():
                # Add the digit to the set
                digits.add(int(char))
        
        # Convert the set to a sorted list in descending order
        sorted_digits = sorted(digits, reverse=True)
        
        # Check if there are at least two unique digits
        if len(sorted_digits) < 2:
            return -1
        
        # Return the second largest digit
        return sorted_digits[1]

def secondHighest(s: str) -> int:
    return Solution().secondHighest(s)