import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        # Length of s1 and s2
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, s2 can't contain a permutation of s1
        if len1 > len2:
            return False
        
        # Count the frequency of each character in s1
        s1_count = Counter(s1)
        # Initialize a counter for the first window in s2 of the same length as s1
        s2_count = Counter(s2[:len1])
        
        # Check if the first window is a permutation
        if s1_count == s2_count:
            return True
        
        # Slide the window over s2 one character at a time
        for i in range(len1, len2):
            # Add the new character to the window
            s2_count[s2[i]] += 1
            # Remove the character that is left out of the window
            s2_count[s2[i - len1]] -= 1
            
            # If the count becomes zero, remove it from the counter
            if s2_count[s2[i - len1]] == 0:
                del s2_count[s2[i - len1]]
            
            # Check if the current window is a permutation
            if s1_count == s2_count:
                return True
        
        return False

def checkInclusion(s1: str, s2: str) -> bool:
    return Solution().checkInclusion(s1, s2)