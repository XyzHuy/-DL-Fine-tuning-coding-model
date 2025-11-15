import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def lastSubstring(self, s: str) -> str:
        # Initialize the starting index of the maximum substring
        max_index = 0
        # Initialize the current index we are comparing
        current_index = 1
        # Initialize the offset to compare characters
        offset = 0
        
        # Get the length of the string
        n = len(s)
        
        # Loop until the current index reaches the end of the string
        while current_index + offset < n:
            # Compare characters at max_index + offset and current_index + offset
            if s[max_index + offset] == s[current_index + offset]:
                offset += 1
            else:
                # If the character at current_index + offset is greater
                if s[current_index + offset] > s[max_index + offset]:
                    # Update max_index to be current_index if the current character is greater
                    max_index = current_index
                # Move current_index to the next potential starting point
                current_index = current_index + offset + 1 if current_index + offset < max_index else current_index + 1
                # Reset offset for the next comparison
                offset = 0
        
        # Return the lexicographically maximum substring
        return s[max_index:]

def lastSubstring(s: str) -> str:
    return Solution().lastSubstring(s)