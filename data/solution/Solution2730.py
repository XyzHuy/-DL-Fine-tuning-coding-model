import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        max_length = 1
        start = 0
        first_pair_index = -1
        
        for end in range(1, len(s)):
            if s[end] == s[end - 1]:
                if first_pair_index != -1:
                    start = first_pair_index + 1
                first_pair_index = end - 1
            max_length = max(max_length, end - start + 1)
        
        return max_length

def longestSemiRepetitiveSubstring(s: str) -> int:
    return Solution().longestSemiRepetitiveSubstring(s)