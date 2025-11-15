import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        
        # Dictionary to store the count of characters in the current window
        char_count = defaultdict(int)
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Add the current character to the window
            char_count[s[right]] += 1
            
            # If we have more than 2 distinct characters, shrink the window from the left
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            # Update the maximum length of the window
            max_length = max(max_length, right - left + 1)
        
        return max_length

def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    return Solution().lengthOfLongestSubstringTwoDistinct(s)