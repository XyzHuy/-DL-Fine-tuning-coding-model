import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Replace non-digit characters with spaces
        modified_word = ''.join([' ' if not c.isdigit() else c for c in word])
        # Split the string by spaces to get all number strings
        number_strings = modified_word.split()
        # Convert to integers to remove leading zeros and use a set to get unique numbers
        unique_numbers = set(map(int, number_strings))
        # Return the count of unique numbers
        return len(unique_numbers)

def numDifferentIntegers(word: str) -> int:
    return Solution().numDifferentIntegers(word)