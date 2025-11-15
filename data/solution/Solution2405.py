import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def partitionString(self, s: str) -> int:
        # Initialize a set to keep track of characters in the current substring
        current_chars = set()
        # Initialize the count of substrings
        count = 1
        
        # Iterate over each character in the string
        for char in s:
            # If the character is already in the current substring, start a new substring
            if char in current_chars:
                count += 1
                current_chars = set(char)
            else:
                current_chars.add(char)
        
        return count

def partitionString(s: str) -> int:
    return Solution().partitionString(s)