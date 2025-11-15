import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def confusingNumber(self, n: int) -> bool:
        # Mapping of digits to their 180-degree rotated counterparts
        rotation_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        # Convert the number to a string to process each digit
        n_str = str(n)
        rotated_str = []
        
        # Rotate each digit
        for char in n_str:
            if char not in rotation_map:
                return False  # If the digit is invalid, return False
            rotated_str.append(rotation_map[char])
        
        # Form the rotated number by reversing the rotated digits
        rotated_number = ''.join(rotated_str[::-1])
        
        # Convert the rotated number back to an integer to remove leading zeros
        rotated_number = int(rotated_number)
        
        # Check if the rotated number is different from the original
        return rotated_number != n

def confusingNumber(n: int) -> bool:
    return Solution().confusingNumber(n)