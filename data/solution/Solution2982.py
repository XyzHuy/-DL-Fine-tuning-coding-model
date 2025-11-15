import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import defaultdict
        
        # Dictionary to store the counts of special substrings of each length for each character
        special_substrings = defaultdict(lambda: defaultdict(int))
        
        # Iterate over the string to find all special substrings
        n = len(s)
        i = 0
        while i < n:
            start = i
            # Find the end of the current special substring
            while i < n and s[i] == s[start]:
                i += 1
            length = i - start
            # Record all special substrings of lengths 1 to 'length' for the character s[start]
            for l in range(1, length + 1):
                special_substrings[s[start]][l] += (length - l + 1)
        
        # Find the maximum length of a special substring that occurs at least thrice
        max_length = -1
        for char in special_substrings:
            for length in special_substrings[char]:
                if special_substrings[char][length] >= 3:
                    max_length = max(max_length, length)
        
        return max_length

def maximumLength(s: str) -> int:
    return Solution().maximumLength(s)