import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Dictionary to store the first occurrence of each state
        state_index = {0: -1}
        # Bitmask representing the parity of the count of vowels
        current_state = 0
        max_length = 0
        
        # Iterate over the string
        for i, char in enumerate(s):
            if char in 'aeiou':
                # Toggle the bit corresponding to the vowel
                current_state ^= 1 << ('aeiou'.index(char))
            
            # If the state has been seen before, calculate the length of the substring
            if current_state in state_index:
                max_length = max(max_length, i - state_index[current_state])
            else:
                # Store the first occurrence of the state
                state_index[current_state] = i
        
        return max_length

def findTheLongestSubstring(s: str) -> int:
    return Solution().findTheLongestSubstring(s)