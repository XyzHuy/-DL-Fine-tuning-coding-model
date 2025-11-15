import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char_map[s[right]] = right
            
            if len(char_map) > k:
                # Find the leftmost character to remove
                leftmost_char = min(char_map, key=char_map.get)
                left = char_map.pop(leftmost_char) + 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    return Solution().lengthOfLongestSubstringKDistinct(s, k)