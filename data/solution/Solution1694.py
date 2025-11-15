import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reformatNumber(self, number: str) -> str:
        # Remove all spaces and dashes
        cleaned_number = number.replace(" ", "").replace("-", "")
        
        # Initialize an empty list to hold the blocks
        blocks = []
        
        # Process the digits in chunks
        while len(cleaned_number) > 4:
            # Take the first 3 digits and add them to the blocks
            blocks.append(cleaned_number[:3])
            # Remove the first 3 digits from the cleaned_number
            cleaned_number = cleaned_number[3:]
        
        # Handle the remaining digits
        if len(cleaned_number) == 4:
            # Split into two blocks of 2 digits each
            blocks.append(cleaned_number[:2])
            blocks.append(cleaned_number[2:])
        else:
            # Add the remaining digits as a single block
            blocks.append(cleaned_number)
        
        # Join the blocks with dashes and return the result
        return "-".join(blocks)

def reformatNumber(number: str) -> str:
    return Solution().reformatNumber(number)