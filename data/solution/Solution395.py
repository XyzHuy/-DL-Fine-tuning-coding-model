import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        # Count the frequency of each character in the string
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find the first character that does not meet the frequency requirement
        for char in s:
            if char_count[char] < k:
                # Split the string by this character and check each substring
                return max(self.longestSubstring(substring, k) for substring in s.split(char))
        
        # If all characters meet the frequency requirement, return the length of the string
        return len(s)

def longestSubstring(s: str, k: int) -> int:
    return Solution().longestSubstring(s, k)