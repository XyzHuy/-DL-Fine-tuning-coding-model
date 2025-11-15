import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        
        char_count = defaultdict(int)
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            
            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

def maximumLengthSubstring(s: str) -> int:
    return Solution().maximumLengthSubstring(s)