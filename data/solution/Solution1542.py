import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestAwesome(self, s: str) -> int:
        # Dictionary to store the first occurrence of each bitmask
        seen = {0: -1}
        max_length = 0
        current_mask = 0
        
        for i, char in enumerate(s):
            # Toggle the bit corresponding to the current character
            current_mask ^= (1 << int(char))
            
            # Check if the current bitmask has been seen before
            if current_mask in seen:
                max_length = max(max_length, i - seen[current_mask])
            
            # Check for bitmasks that differ by exactly one bit
            for j in range(10):
                mask = current_mask ^ (1 << j)
                if mask in seen:
                    max_length = max(max_length, i - seen[mask])
            
            # Store the first occurrence of the current bitmask
            if current_mask not in seen:
                seen[current_mask] = i
        
        return max_length

def longestAwesome(s: str) -> int:
    return Solution().longestAwesome(s)