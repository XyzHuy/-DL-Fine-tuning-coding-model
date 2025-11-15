import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a dictionary to count characters in s
        char_count = {}
        
        # Count each character in s
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Check each character in t
        for char in t:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                # If the character is not found or is extra, return it
                return char

def findTheDifference(s: str, t: str) -> str:
    return Solution().findTheDifference(s, t)