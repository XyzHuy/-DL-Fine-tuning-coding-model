import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Dictionary to store the maximum length of substring ending with each character
        max_len_ending_with = {chr(ord('a') + i): 0 for i in range(26)}
        
        # Function to check if two characters are consecutive in the wraparound string
        def is_consecutive(c1, c2):
            return (ord(c2) - ord(c1)) % 26 == 1
        
        # Initialize the length of the current valid substring
        current_length = 0
        
        # Iterate over the string
        for i in range(len(s)):
            if i > 0 and is_consecutive(s[i - 1], s[i]):
                current_length += 1
            else:
                current_length = 1
            
            # Update the maximum length of substring ending with s[i]
            max_len_ending_with[s[i]] = max(max_len_ending_with[s[i]], current_length)
        
        # The total number of unique substrings is the sum of the maximum lengths
        return sum(max_len_ending_with.values())

def findSubstringInWraproundString(s: str) -> int:
    return Solution().findSubstringInWraproundString(s)