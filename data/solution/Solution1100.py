import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        count = 0
        window = {}
        
        # Initialize the first window
        for i in range(k):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1
        
        # Check the first window
        if len(window) == k:
            count += 1
        
        # Slide the window over the string
        for i in range(k, len(s)):
            # Add the new character to the window
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1
            
            # Remove the old character from the window
            window[s[i - k]] -= 1
            if window[s[i - k]] == 0:
                del window[s[i - k]]
            
            # Check if the current window has no repeated characters
            if len(window) == k:
                count += 1
        
        return count

def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    return Solution().numKLenSubstrNoRepeats(s, k)