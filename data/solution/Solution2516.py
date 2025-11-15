import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        from collections import Counter
        
        # Count the total occurrences of 'a', 'b', and 'c' in the string
        total_count = Counter(s)
        
        # If there are not enough 'a', 'b', or 'c' to satisfy k, return -1
        if total_count['a'] < k or total_count['b'] < k or total_count['c'] < k:
            return -1
        
        # We need to find the longest substring that we can remove from the middle
        # such that the remaining characters on both sides satisfy the condition of having at least k of each character.
        current_count = Counter()
        left = 0
        max_window_size = 0
        
        # Use a sliding window to find the longest valid substring in the middle
        for right in range(len(s)):
            current_count[s[right]] += 1
            
            # While the current window is invalid (i.e., removing it would not leave enough 'a', 'b', or 'c' on the sides)
            while current_count[s[right]] > total_count[s[right]] - k:
                current_count[s[left]] -= 1
                left += 1
            
            # Update the maximum window size
            max_window_size = max(max_window_size, right - left + 1)
        
        # The result is the total length of the string minus the length of the longest valid middle substring
        return len(s) - max_window_size

def takeCharacters(s: str, k: int) -> int:
    return Solution().takeCharacters(s, k)