import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # Create a dictionary to map characters in chars to their corresponding values in vals
        char_values = {char: val for char, val in zip(chars, vals)}
        
        # Initialize the maximum cost and the current cost
        max_cost = 0
        current_cost = 0
        
        # Iterate over each character in the string s
        for char in s:
            # Determine the value of the current character
            if char in char_values:
                value = char_values[char]
            else:
                value = ord(char) - ord('a') + 1
            
            # Update the current cost
            current_cost = max(current_cost + value, 0)
            
            # Update the maximum cost if the current cost is greater
            max_cost = max(max_cost, current_cost)
        
        return max_cost

def maximumCostSubstring(s: str, chars: str, vals: List[int]) -> int:
    return Solution().maximumCostSubstring(s, chars, vals)