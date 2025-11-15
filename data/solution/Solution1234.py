import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def balancedString(self, s: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in the string
        count = Counter(s)
        n = len(s)
        k = n // 4
        
        # Calculate the excess characters that need to be replaced
        excess = {char: cnt - k for char, cnt in count.items() if cnt > k}
        
        # If there are no excess characters, the string is already balanced
        if not excess:
            return 0
        
        # Sliding window to find the minimum length of the substring to replace
        left = 0
        min_length = n
        for right in range(n):
            # Decrease the count of the current character if it's in excess
            if s[right] in excess:
                excess[s[right]] -= 1
            
            # Check if the current window is valid (all excess characters are covered)
            while all(cnt <= 0 for cnt in excess.values()):
                # Update the minimum length of the valid window
                min_length = min(min_length, right - left + 1)
                
                # Try to shrink the window from the left
                if s[left] in excess:
                    excess[s[left]] += 1
                left += 1
        
        return min_length

def balancedString(s: str) -> int:
    return Solution().balancedString(s)