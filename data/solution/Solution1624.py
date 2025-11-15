import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Dictionary to store the first occurrence of each character
        first_occurrence = {}
        max_length = -1
        
        # Iterate over the string with index
        for i, char in enumerate(s):
            # If the character is already seen, calculate the length of the substring
            if char in first_occurrence:
                # Update max_length if the current substring is longer
                max_length = max(max_length, i - first_occurrence[char] - 1)
            else:
                # Store the first occurrence of the character
                first_occurrence[char] = i
        
        return max_length

def maxLengthBetweenEqualCharacters(s: str) -> int:
    return Solution().maxLengthBetweenEqualCharacters(s)