import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Initialize pointers for both strings
        i, j = 0, 0
        
        # Traverse both strings
        while i < len(s) and j < len(t):
            # If characters match, move the pointer in t
            if s[i] == t[j]:
                j += 1
            # Always move the pointer in s
            i += 1
        
        # The number of characters to append is the remaining characters in t
        return len(t) - j

def appendCharacters(s: str, t: str) -> int:
    return Solution().appendCharacters(s, t)