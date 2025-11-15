import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to store the count of each character
        char_count = {}
        
        # Count the occurrences of each character in the string
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Find the first character with a count of 1
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no unique character is found, return -1
        return -1

def firstUniqChar(s: str) -> int:
    return Solution().firstUniqChar(s)