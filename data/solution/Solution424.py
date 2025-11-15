import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        # Dictionary to count the frequency of characters in the current window
        char_count = defaultdict(int)
        max_length = 0
        max_count = 0
        start = 0
        
        for end in range(len(s)):
            # Increment the count of the current character
            char_count[s[end]] += 1
            # Update the count of the most frequent character in the current window
            max_count = max(max_count, char_count[s[end]])
            
            # If the current window size minus the count of the most frequent character
            # is greater than k, it means we need more than k replacements,
            # so we shrink the window from the left
            if (end - start + 1) - max_count > k:
                char_count[s[start]] -= 1
                start += 1
            
            # Update the maximum length of the window
            max_length = max(max_length, end - start + 1)
        
        return max_length

def characterReplacement(s: str, k: int) -> int:
    return Solution().characterReplacement(s, k)