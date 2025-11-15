import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        # Create a set of characters in the string
        char_set = set(s)
        
        # Iterate through the string to find any character that doesn't have its pair
        for i, char in enumerate(s):
            if char.swapcase() not in char_set:
                # Split the string into two parts and recursively find the longest nice substring
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                # Return the longer of the two substrings
                return max(left, right, key=len)
        
        # If no such character is found, the whole string is nice
        return s

def longestNiceSubstring(s: str) -> str:
    return Solution().longestNiceSubstring(s)