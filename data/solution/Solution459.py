import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Create a new string by concatenating the original string with itself
        # and removing the first and last character of the new string.
        # This helps in checking if the original string is a repeated pattern.
        new_string = s + s
        # Check if the original string is in the new string, excluding the first and last character.
        return s in new_string[1:-1]

def repeatedSubstringPattern(s: str) -> bool:
    return Solution().repeatedSubstringPattern(s)