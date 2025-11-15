import random
import functools
import collections
import string
import math
import datetime


from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the frequency of each character
        char_count = Counter(s)
        # Sort characters by frequency (descending)
        sorted_chars = sorted(char_count.keys(), key=lambda x: -char_count[x])
        
        # Initialize a list to hold the rearranged characters
        result = [''] * len(s)
        index = 0
        
        # Place the most frequent characters first
        for char in sorted_chars:
            if char_count[char] > (len(s) + 1) // 2:
                return ""
            for _ in range(char_count[char]):
                if index >= len(s):
                    index = 1  # Switch to odd indices
                result[index] = char
                index += 2
        
        return ''.join(result)

def reorganizeString(s: str) -> str:
    return Solution().reorganizeString(s)