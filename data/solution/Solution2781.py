import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        max_length = 0
        n = len(word)
        
        # Initialize the start of the window
        i = 0
        
        # Iterate over the end of the window
        for j in range(n):
            # Check all substrings ending at j
            for end in range(j, max(j - 10, i - 1), -1):
                substring = word[end:j + 1]
                if substring in forbidden_set:
                    # If a forbidden substring is found, move the start of the window
                    i = end + 1
                    break
            
            # Update the maximum length of valid substring
            max_length = max(max_length, j - i + 1)
        
        return max_length

def longestValidSubstring(word: str, forbidden: List[str]) -> int:
    return Solution().longestValidSubstring(word, forbidden)