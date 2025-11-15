import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Dictionary to count occurrences of each bitmask
        count = {0: 1}
        current_mask = 0
        result = 0
        
        for char in word:
            # Toggle the bit corresponding to the current character
            current_mask ^= 1 << (ord(char) - ord('a'))
            
            # Add the count of substrings with the same bitmask
            result += count.get(current_mask, 0)
            
            # Check for substrings that differ by at most one bit
            for i in range(10):
                result += count.get(current_mask ^ (1 << i), 0)
            
            # Update the count of the current bitmask
            count[current_mask] = count.get(current_mask, 0) + 1
        
        return result

def wonderfulSubstrings(word: str) -> int:
    return Solution().wonderfulSubstrings(word)