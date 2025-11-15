import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Ensure s is the shorter string
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        
        # If the length difference is greater than 1, they can't be one edit distance apart
        if len(t) - len(s) > 1:
            return False
        
        for i in range(len(s)):
            if s[i] != t[i]:
                # Check for the three possible one edit distances
                # 1. Replace one character in s to match t
                # 2. Insert one character in s to match t
                # 3. Delete one character from t to match s
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:] or s[i+1:] == t[i:]
        
        # If all characters are the same, the only way to be one edit distance apart is to add one character to s
        return len(s) + 1 == len(t)

def isOneEditDistance(s: str, t: str) -> bool:
    return Solution().isOneEditDistance(s, t)