import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import defaultdict
        
        # Dictionary to store the lengths of special substrings
        special_substrings = defaultdict(int)
        
        # Find all special substrings
        n = len(s)
        for i in range(n):
            if i == 0 or s[i] != s[i-1]:
                start = i
            # When the current character is different from the next one or it's the last character
            if i == n-1 or s[i] != s[i+1]:
                length = i - start + 1
                for l in range(1, length + 1):
                    special_substrings[(s[i], l)] += (length - l + 1)
        
        # Find the maximum length of special substring that occurs at least thrice
        max_length = -1
        for (char, length), count in special_substrings.items():
            if count >= 3:
                max_length = max(max_length, length)
        
        return max_length

def maximumLength(s: str) -> int:
    return Solution().maximumLength(s)