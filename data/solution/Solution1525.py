import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numSplits(self, s: str) -> int:
        # Initialize dictionaries to count character frequencies
        left_count = {}
        right_count = {}
        
        # Count all characters in the string for the right part initially
        for char in s:
            right_count[char] = right_count.get(char, 0) + 1
        
        # Initialize the number of good splits
        good_splits = 0
        
        # Iterate through the string to simulate splitting
        for char in s:
            # Add the character to the left part
            left_count[char] = left_count.get(char, 0) + 1
            
            # Remove the character from the right part
            if right_count[char] == 1:
                del right_count[char]
            else:
                right_count[char] -= 1
            
            # Compare the number of distinct characters in both parts
            if len(left_count) == len(right_count):
                good_splits += 1
        
        return good_splits

def numSplits(s: str) -> int:
    return Solution().numSplits(s)