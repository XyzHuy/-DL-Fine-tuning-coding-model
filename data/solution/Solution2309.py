import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def greatestLetter(self, s: str) -> str:
        # Create a set to store unique characters in the string
        char_set = set(s)
        # Initialize a variable to keep track of the greatest letter
        greatest = ''
        
        # Iterate over the string
        for char in s:
            # Check if both the character and its uppercase/lowercase counterpart are in the set
            if char.islower() and char.upper() in char_set:
                # Update the greatest letter if the current character is greater
                if char.upper() > greatest:
                    greatest = char.upper()
            elif char.isupper() and char.lower() in char_set:
                # Update the greatest letter if the current character is greater
                if char > greatest:
                    greatest = char
        
        return greatest

def greatestLetter(s: str) -> str:
    return Solution().greatestLetter(s)