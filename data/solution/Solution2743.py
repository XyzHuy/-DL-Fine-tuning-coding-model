import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        left = 0
        char_index_map = {}

        for right in range(n):
            if s[right] in char_index_map:
                left = max(left, char_index_map[s[right]] + 1)
            char_index_map[s[right]] = right
            count += right - left + 1

        return count

def numberOfSpecialSubstrings(s: str) -> int:
    return Solution().numberOfSpecialSubstrings(s)