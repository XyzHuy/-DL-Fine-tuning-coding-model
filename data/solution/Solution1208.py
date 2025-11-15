import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Initialize pointers for the sliding window
        left = 0
        current_cost = 0
        max_length = 0
        
        # Iterate over the string with the right pointer
        for right in range(len(s)):
            # Calculate the cost of changing s[right] to t[right]
            current_cost += abs(ord(s[right]) - ord(t[right]))
            
            # If the current cost exceeds maxCost, shrink the window from the left
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            # Update the maximum length of the valid substring
            max_length = max(max_length, right - left + 1)
        
        return max_length

def equalSubstring(s: str, t: str, maxCost: int) -> int:
    return Solution().equalSubstring(s, t, maxCost)